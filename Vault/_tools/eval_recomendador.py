#!/usr/bin/env python3
"""Evaluación del recomendador — known-item retrieval + comparación de métodos + curva vs k.
Sin labels humanos: para cada capítulo, genero una query desde su cuerpo (palabras reales, no el
título) y mido en qué rank el sistema lo reencuentra entre los 1177. Recall@k y MRR miden si trae
lo relevante; la coherencia (coseno por posición) mide cuándo empieza a entrar ruido al subir k."""
import json, os, re, sqlite3, random
import numpy as np

random.seed(42)
np.random.seed(42)
os.environ["HF_HUB_OFFLINE"] = "1"; os.environ["TRANSFORMERS_OFFLINE"] = "1"
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_meta")  # portable
CAT = f"{BASE}/catalog.sqlite"

# --- cargar embeddings + modelo ---
em = json.load(open(f"{BASE}/embeddings.json")); V = np.load(f"{BASE}/embeddings.npy")
ids = em["ids"]; idx_of = {i: k for k, i in enumerate(ids)}
from sentence_transformers import SentenceTransformer
model = SentenceTransformer(em["model"], local_files_only=True)

# --- cargar bodies desde FTS ---
c = sqlite3.connect(CAT)
body = {r[0]: (r[1] or "") for r in c.execute("SELECT id, body FROM fts")}
course = {r[0]: r[1] for r in c.execute("SELECT id, course FROM chapters")}

STOP = set("de la el en y a los las que del un una para con por como es su al se lo o e ni "
           "the of to and in is are for with this that on as be by an at from".split())

def query_desde_body(txt):
    """~14 palabras de contenido de una zona media del cuerpo (simula al usuario describiendo)."""
    toks = re.findall(r"[a-záéíóúñA-ZÁÉÍÓÚÑ][a-záéíóúñ]{3,}", txt)
    toks = [t for t in toks if t.lower() not in STOP]
    if len(toks) < 20: return None
    ini = len(toks) // 3          # zona media, evita portada/figura inicial
    return " ".join(toks[ini:ini + 14])

def fts_rank(q, k=100):
    """top-k ids por BM25 (OR de términos, quoteados para no romper FTS5)."""
    terms = re.findall(r"[a-záéíóúñ]{4,}", q.lower())
    if not terms: return []
    match = " OR ".join(f'"{t}"' for t in terms[:14])
    try:
        return [r[0] for r in c.execute(
            "SELECT id FROM fts WHERE fts MATCH ? ORDER BY rank LIMIT ?", (match, k))]
    except sqlite3.OperationalError:
        return []

# --- muestreo de queries known-item ---
N = 200
muestra = [i for i in random.sample(ids, min(N, len(ids))) if query_desde_body(body.get(i, ""))]
queries = [(i, query_desde_body(body[i])) for i in muestra]
print(f"queries evaluadas: {len(queries)}  (known-item, query = ~14 palabras del cuerpo)")

# embeber todas las queries de una
QV = model.encode([f"query: {q}" for _, q in queries], normalize_embeddings=True,
                  batch_size=64, show_progress_bar=False)

KS = [10, 20, 30, 40, 50, 60, 80, 100]
K_RRF = 60
def recall_mrr(ranks_por_q, ks):
    out = {}
    for k in ks:
        out[k] = np.mean([1.0 if r is not None and r < k else 0.0 for r in ranks_por_q])
    mrr = np.mean([1.0 / (r + 1) if r is not None else 0.0 for r in ranks_por_q])
    return out, mrr

rank_emb, rank_fts, rank_hib = [], [], []
coh_por_pos = {k: [] for k in KS}   # coseno del resultado en posición k-1 (coherencia)

for (src, q), qv in zip(queries, QV):
    cos = V @ qv
    order_emb = np.argsort(-cos)
    emb_ids = [ids[j] for j in order_emb[:100]]
    fts_ids = fts_rank(q, 100)
    # RRF
    score = {}
    for r, iid in enumerate(fts_ids): score[iid] = score.get(iid, 0) + 1.0 / (K_RRF + r + 1)
    for r, iid in enumerate(emb_ids): score[iid] = score.get(iid, 0) + 1.0 / (K_RRF + r + 1)
    hib_ids = [i for i in sorted(score, key=lambda x: -score[x])]
    # rank del capítulo fuente en cada método
    def pos(lst):
        return lst.index(src) if src in lst else None
    rank_emb.append(pos(emb_ids)); rank_fts.append(pos(fts_ids)); rank_hib.append(pos(hib_ids))
    # coherencia: coseno del capítulo que cae en cada posición del ranking híbrido
    for k in KS:
        if len(hib_ids) >= k:
            iid_k = hib_ids[k - 1]
            if iid_k in idx_of:
                coh_por_pos[k].append(float(cos[idx_of[iid_k]]))

print("\n=== ¿ENCUENTRA LO RELEVANTE? Recall@k (fracción de queries cuyo capítulo correcto está en top-k) ===")
print(f"{'k':>4} | {'solo-FTS':>9} | {'solo-EMB':>9} | {'HÍBRIDO':>9}")
re_e, mrr_e = recall_mrr(rank_emb, KS); re_f, mrr_f = recall_mrr(rank_fts, KS); re_h, mrr_h = recall_mrr(rank_hib, KS)
for k in KS:
    print(f"{k:>4} | {re_f[k]:>9.3f} | {re_e[k]:>9.3f} | {re_h[k]:>9.3f}")
print(f"\nMRR (qué tan arriba, 1.0=siempre #1):  FTS={mrr_f:.3f}  EMB={mrr_e:.3f}  HÍBRIDO={mrr_h:.3f}")

print("\n=== ¿CUÁNDO ENTRA RUIDO? Coherencia = coseno medio del resultado en la posición k ===")
print("(cae => a partir de ahí los candidatos se parecen menos a la consulta)")
print(f"{'posición k':>10} | {'coseno medio':>12} | {'vs top':>8}")
top = np.mean(coh_por_pos[10]) if coh_por_pos[10] else 1
for k in KS:
    if coh_por_pos[k]:
        m = np.mean(coh_por_pos[k])
        print(f"{k:>10} | {m:>12.4f} | {m/top:>7.2%}")

# ganancia marginal de recall al subir k
print("\n=== GANANCIA MARGINAL de recall al subir k (híbrido) — ¿vale extender? ===")
prev = None
for k in KS:
    g = re_h[k] - (prev if prev is not None else 0)
    print(f"  hasta {k:>3}: recall={re_h[k]:.3f}   (+{g:.3f} vs k anterior)")
    prev = re_h[k]
