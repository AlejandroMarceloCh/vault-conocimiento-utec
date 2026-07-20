#!/usr/bin/env python3
"""Sprint 4b — índice de embeddings (búsqueda semántica) para escalar a ~100 cursos.

Cada capítulo se vectoriza por su título + índice + resumen (lo que dice de qué trata). Modelo
local PINNEADO (reproducible, sin API). Guarda vectores en embeddings.npy + ids + el id del modelo.
Determinista: mismo modelo + mismo texto → mismo vector."""
import argparse, json, os, re, sqlite3, sys
import numpy as np

MODEL = "intfloat/multilingual-e5-base"   # 768d, multilingüe, fuerte en recuperación

def chapter_text(cu, path, summary):
    """Texto rico para embeber: título + índice + cuerpo real (no el resumen débil)."""
    raw = open(os.path.join(cu, path)).read()
    body = re.sub(r"^---.*?---", "", raw, count=1, flags=re.S)
    title_m = re.search(r"#\s*(.+)", body)
    title = title_m.group(1).strip() if title_m else ""
    idx = re.search(r"##\s*Índice\s*(.+?)(?=\n##\s|\Z)", raw, re.S)
    indice = re.sub(r"\s+", " ", re.sub(r"[#*`>|]", " ", idx.group(1) if idx else ""))[:500]
    # cuerpo sin fórmulas/figuras/tablas ruidosas, primeros ~1500 chars de prosa real
    prose = re.sub(r"\*\*Figura:.*?(?=\n)", " ", body)
    prose = re.sub(r"\$[^$]*\$", " ", prose)
    prose = re.sub(r"[#*`>|]", " ", prose)
    prose = re.sub(r"\s+", " ", prose)[:1500]
    return f"passage: {title}. Temas: {indice} {prose}"

def main():
    import hashlib
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--source", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--full", action="store_true", help="re-embeber TODO (ignora caché)")
    a = ap.parse_args()
    c = sqlite3.connect(a.catalog)
    rows = list(c.execute("SELECT id, path, summary FROM chapters ORDER BY id"))
    c.close()
    ids = [r[0] for r in rows]
    texts = [chapter_text(a.source, r[1], r[2]) for r in rows]
    hashes = [hashlib.sha256(t.encode()).hexdigest() for t in texts]   # hash del texto embebido

    # INCREMENTAL (fix A2 de GLM): reusar vectores cuyo texto no cambió; solo re-embeber nuevos/cambiados.
    # A3: la caché SOLO se usa si el .npy coincide con el hash guardado en el .json (detecta
    # desincronización/corrupción entre np.save y json.dump) y si shapes e ids calzan; si no → re-embebe todo.
    prev_vec, prev_hash = None, {}
    jpath = a.out.replace(".npy", ".json")
    if not a.full and os.path.exists(a.out) and os.path.exists(jpath):
        try:
            meta = json.load(open(jpath))
            v = np.load(a.out)
            npy_sha = hashlib.sha256(v.tobytes()).hexdigest()
            consistente = (meta.get("model") == MODEL and "hashes" in meta
                           and meta.get("npy_sha256") == npy_sha
                           and v.shape[0] == len(meta["ids"]) == len(meta["hashes"]))
            if consistente:
                prev_vec = v
                prev_hash = {iid: (h, i) for i, (iid, h) in enumerate(zip(meta["ids"], meta["hashes"]))}
            else:
                print("  caché de embeddings inconsistente (.npy↔.json) → re-embebe todo")
        except Exception as e:
            print(f"  caché de embeddings ilegible ({e}) → re-embebe todo")

    faltan = [i for i, (iid, h) in enumerate(zip(ids, hashes))
              if not (iid in prev_hash and prev_hash[iid][0] == h)]
    dim = prev_vec.shape[1] if prev_vec is not None else None
    vecs = np.zeros((len(ids), dim), dtype="float32") if dim else None
    # reusar los que no cambiaron
    for i, (iid, h) in enumerate(zip(ids, hashes)):
        if i not in faltan:
            vecs[i] = prev_vec[prev_hash[iid][1]]
    # embeber solo los que faltan
    if faltan:
        from sentence_transformers import SentenceTransformer
        nuevos = SentenceTransformer(MODEL).encode([texts[i] for i in faltan],
                                                   normalize_embeddings=True, show_progress_bar=False)
        if vecs is None:
            dim = nuevos.shape[1]; vecs = np.zeros((len(ids), dim), dtype="float32")
        for k, i in enumerate(faltan):
            vecs[i] = nuevos[k]

    # escritura ATÓMICA (fix A3): .npy y .json quedan siempre coherentes; el .json guarda el hash del .npy
    vecs = vecs.astype("float32")
    npy_sha = hashlib.sha256(vecs.tobytes()).hexdigest()
    tmp_npy = a.out + ".tmp"
    np.save(tmp_npy, vecs)
    if os.path.exists(tmp_npy + ".npy"):   # np.save agrega .npy si no lo tiene
        os.replace(tmp_npy + ".npy", a.out)
    else:
        os.replace(tmp_npy, a.out)
    meta = {"model": MODEL, "ids": ids, "dim": int(vecs.shape[1]), "hashes": hashes, "npy_sha256": npy_sha}
    json.dump(meta, open(jpath + ".tmp", "w"), ensure_ascii=False)
    os.replace(jpath + ".tmp", jpath)
    print(f"embeddings: {len(ids)} capítulos · {vecs.shape[1]}d · re-embebidos {len(faltan)} "
          f"(reusados {len(ids)-len(faltan)}) · modelo {MODEL}")

if __name__ == "__main__":
    main()
