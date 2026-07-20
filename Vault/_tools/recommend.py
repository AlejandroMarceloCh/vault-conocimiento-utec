#!/usr/bin/env python3
"""Sprint 4 — recomendador determinista por recuperación (FTS5 + BM25).

Dado el texto de un proyecto, recupera los capítulos más relevantes del catálogo y devuelve
recomendaciones. Se ABSTIENE si ningún capítulo supera el umbral. NO usa LLM, NO lee INDEX.md ni el
gold: solo puede devolver capítulos que existen en el catálogo, así que no puede inventar.

Nota: la cita por rango de slides (`--cite`) requiere los PDF originales en `Vault/_sources/` (no
incluidos en el repo) y `pdftotext` (poppler). Sin ellos devuelve citas vacías. El flujo normal
—vía `recomendar.py`— lo invoca con `--no-cite`, así que esto no afecta el uso estándar.

Salida: JSON {abstain: bool, recomendaciones: [{id, course, title, score, slides, terminos}]}.
"""
import argparse, json, os, re, sqlite3, subprocess, sys, unicodedata

STOP = set(("de la el los las un una y o a en con por para que del al se su sus es son este esta "
            "como más menos entre sobre the of to and for with this that").split())

def terms(text):
    toks = re.findall(r"[a-zA-ZáéíóúñÁÉÍÓÚÑ0-9_]{3,}", text.lower())
    seen, out = set(), []
    for t in toks:
        if t in STOP or t in seen:
            continue
        seen.add(t); out.append(t)
    return out[:40]

def fts_query(ts):
    # OR de términos, cada uno citado para FTS5
    return " OR ".join(f'"{t}"' for t in ts)

def find_slides(vault, course, fuente, term, maxslides, cache):
    """Slides del PDF donde aparece el término (cita concreta). '' si no hay original."""
    key = (course, fuente)
    if key not in cache:
        pdf = os.path.join(vault, "_sources", course, unicodedata.normalize("NFD", fuente))
        if not os.path.exists(pdf):
            pdf = os.path.join(vault, "_sources", course, fuente)
        cache[key] = pdf if os.path.exists(pdf) else None
    pdf = cache[key]
    if not pdf:
        return []
    hits = []
    for p in range(1, min(maxslides, 200) + 1):
        t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), pdf, "-"],
                           capture_output=True, text=True).stdout.lower()
        if term.lower() in re.sub(r"\s+", " ", t):
            hits.append(p)
        if len(hits) >= 3:
            break
    return hits

def recommend(catalog, project_text, k=3, min_score=14.0, rel_cutoff=0.7, cite=True):
    """min_score = PISO sobre el mejor score (si el top no lo alcanza → abstención).
    rel_cutoff = banda relativa: solo se devuelven capítulos con score ≥ rel_cutoff * top.
    Así se evita devolver relleno de baja relevancia (mejora precisión) y se abstiene si nada es fuerte."""
    vault = os.path.abspath(os.path.join(os.path.dirname(catalog), ".."))
    c = sqlite3.connect(catalog)
    ts = terms(project_text)
    q = fts_query(ts)
    rows = c.execute(
        "SELECT f.id, bm25(fts) AS s, c.course, c.title, c.fuente, c.slides "
        "FROM fts f JOIN chapters c ON c.id=f.id WHERE fts MATCH ? ORDER BY s LIMIT ?",
        (q, k * 3)).fetchall()
    # bm25 de sqlite: más NEGATIVO = más relevante → convertimos a score positivo
    scored = [(-s, iid, course, title, fuente, slides) for (iid, s, course, title, fuente, slides) in rows]
    top = scored[0][0] if scored else 0.0
    recs = []
    for score, iid, course, title, fuente, slides in scored:
        if top < min_score:          # nada es suficientemente fuerte → abstención
            break
        if score < rel_cutoff * top:  # relleno de baja relevancia respecto al top → se descarta
            continue
        rec = {"id": iid, "course": course, "title": title, "score": round(score, 2)}
        if cite:
            cache = {}
            slidehits = {}
            for t in ts[:12]:
                hs = find_slides(vault, course, fuente, t, slides, cache)
                if hs:
                    slidehits[t] = hs
            rec["citas"] = slidehits
        recs.append(rec)
        if len(recs) >= k:
            break
    c.close()
    return {"abstain": len(recs) == 0, "recomendaciones": recs}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--project", help="archivo con el texto del proyecto")
    ap.add_argument("--text", help="texto directo")
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--min-score", type=float, default=1.0)
    ap.add_argument("--no-cite", action="store_true")
    a = ap.parse_args()
    text = a.text or open(a.project).read()
    out = recommend(a.catalog, text, a.k, a.min_score, cite=not a.no_cite)
    print(json.dumps(out, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
