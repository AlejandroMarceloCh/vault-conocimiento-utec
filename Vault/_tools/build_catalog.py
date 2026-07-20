#!/usr/bin/env python3
"""Sprint 0 — compila el catálogo de evidencia (SQLite FTS5) desde el source tree inmutable.

DETERMINISTA: nada de timestamps en el contenido hasheado, todo ordenado, mismo input → mismo
content_sha por capítulo. `--check` reconstruye en memoria y compara contra el DB existente.

Uso:
  build_catalog.py --source <CursosUTEC> --allowlist <allowlist> --out catalog.sqlite
  build_catalog.py --source <CursosUTEC> --out catalog.sqlite --check   # falla si algo cambió
"""
import argparse, json, os, re, sqlite3, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fm

def _nfc(s):
    return unicodedata.normalize("NFC", s)   # macOS guarda NFD; el frontmatter es NFC

def load_lock(lock_path):
    if not lock_path or not os.path.exists(lock_path):
        return {}
    d = json.load(open(lock_path))
    # fix SUBCARPETAS: clave (course, file) en vez de solo file. Antes el dict era global por
    # basename → dos cursos con un archivo del mismo nombre (ej. "Sem1_Intro.pdf") se pisaban y
    # el lookup de procedencia cruzaba sha entre cursos. Ahora cada (curso, fuente) resuelve exacto.
    return {(_nfc(a["course"]), _nfc(a["file"])): a["sha256"] for a in d["assets"]}

def derive_summary(body):
    """Resumen determinista: primer bloque de prosa bajo el primer ## real (no Índice/Glosario)."""
    for m in re.finditer(r"^##\s+(.+)$", body, re.M):
        title = m.group(1).strip()
        if title.lower() in ("índice", "indice", "glosario"):
            continue
        chunk = body[m.end():]
        text = re.sub(r"\s+", " ", re.sub(r"[#*`>|\-]", "", chunk)).strip()
        return text[:240]
    return re.sub(r"\s+", " ", body)[:240]

def build(source, allowlist_path, lock_path):
    lock = load_lock(lock_path)
    rows = []
    with open(allowlist_path) as fh:
        entries = [l.strip().split("\t") for l in fh if l.strip()]
    for iid, rel in entries:
        path = os.path.join(source, rel)
        if not os.path.exists(path):
            raise SystemExit(f"allowlist apunta a nota inexistente: {rel}")
        text = open(path).read()
        try:
            meta, body = fm.split(text)
        except ValueError as ex:
            # M4: un frontmatter roto NO tumba todo el catálogo. Se reporta el archivo, se salta,
            # y se registra como entrada mínima con source_status=frontmatter_broken para que se vea
            # en el dashboard y Claude/Composer lo arreglen. No aparece en FTS (no tiene body válido).
            print(f"SKIP (frontmatter inválido): {rel} → {ex}", file=sys.stderr)
            rows.append({"id": iid, "course": "", "title": f"BROKEN: {os.path.basename(rel)}",
                         "slides": 0, "fuente": "", "source_sha256": "",
                         "source_status": "frontmatter_broken", "content_sha256": "",
                         "summary": f"frontmatter inválido: {ex}", "path": rel, "figures": 0,
                         "_body": ""})
            continue
        fuente = meta.get("fuente", "")
        source_sha = lock.get((_nfc(meta.get("curso", "")), _nfc(fuente)))  # None si no está blindado
        rows.append({
            "id": iid,
            "course": meta.get("curso", ""),
            "title": meta.get("titulo", ""),
            "slides": meta.get("slides", 0),
            "fuente": fuente,
            "source_sha256": source_sha or "",
            "source_status": "verified" if source_sha else "original_unavailable",
            "content_sha256": fm.body_sha256(body),
            "summary": derive_summary(body),
            "path": rel,
            "figures": body.count("**Figura"),
            "_body": body,   # transiente: solo para poblar el índice FTS, no se guarda en chapters
        })
    rows.sort(key=lambda r: r["id"])  # orden estable
    return rows

def write_db(rows, out):
    if os.path.exists(out):
        os.remove(out)
    c = sqlite3.connect(out)
    c.executescript("""
      CREATE TABLE chapters(id TEXT PRIMARY KEY, course TEXT, title TEXT, slides INT,
        fuente TEXT, source_sha256 TEXT, source_status TEXT, content_sha256 TEXT,
        summary TEXT, path TEXT, figures INT);
      CREATE VIRTUAL TABLE fts USING fts5(id UNINDEXED, title, summary, body);
      CREATE TABLE links(id INTEGER PRIMARY KEY, src TEXT, tgt TEXT, relation TEXT,
        src_locator TEXT, tgt_locator TEXT, rationale TEXT, src_quote TEXT, tgt_quote TEXT);
      CREATE TABLE tags(chapter TEXT, tag TEXT);
    """)
    for r in rows:
        c.execute("INSERT INTO chapters VALUES(:id,:course,:title,:slides,:fuente,"
                  ":source_sha256,:source_status,:content_sha256,:summary,:path,:figures)",
                  {k: v for k, v in r.items() if k != "_body"})
        c.execute("INSERT INTO fts(id,title,summary,body) VALUES(?,?,?,?)",
                  (r["id"], r["title"], r["summary"], r["_body"]))
    c.commit(); c.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--allowlist")
    ap.add_argument("--out", required=True)
    ap.add_argument("--lock", help="ruta a sources.lock.json (explícita; NO se deriva de --out, "
                    "para que un rebuild a otra carpeta no pierda procedencia)")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    vault_root = os.path.abspath(os.path.join(os.path.dirname(a.out), ".."))
    # el lock se resuelve explícito o desde la Vault del source tree; nunca desde --out
    default_lock = os.path.join(os.path.dirname(os.path.abspath(a.source)), "Vault", "_meta", "sources.lock.json")
    lock_path = a.lock or (default_lock if os.path.exists(default_lock)
                           else os.path.join(vault_root, "_meta", "sources.lock.json"))
    allow = a.allowlist or os.path.join(vault_root, "_meta", "notes.allowlist")
    rows = build(a.source, allow, lock_path)

    if a.check:
        if not os.path.exists(a.out):
            raise SystemExit("--check pero no existe el DB")
        c = sqlite3.connect(a.out)
        # compara la fila COMPLETA (no solo content_sha): id, course, title, slides, source, summary, figures
        cols = ["id","course","title","slides","fuente","source_sha256","source_status","content_sha256","summary","path","figures"]
        db = {r[0]: dict(zip(cols, r)) for r in c.execute(f"SELECT {','.join(cols)} FROM chapters")}
        c.close()
        drift = []
        for r in rows:
            d = db.get(r["id"])
            if d is None:
                drift.append(f"{r['id']}: ausente en DB")
            elif any(str(d[k]) != str(r[k]) for k in cols):
                diffs = [k for k in cols if str(d[k]) != str(r[k])]
                drift.append(f"{r['id']}: difiere en {diffs}")
        drift += [f"{i}: sobra en DB" for i in db if i not in {r["id"] for r in rows}]
        if drift:
            print("DRIFT (no determinista o editado):"); [print("  -", x) for x in drift]; sys.exit(1)
        print(f"--check OK: {len(rows)} capítulos, filas completas idénticas (determinista)"); return

    write_db(rows, a.out)
    ver = sum(r["source_status"] == "verified" for r in rows)
    print(f"catálogo: {len(rows)} capítulos · {ver}/{len(rows)} con original blindado · "
          f"{sum(r['figures'] for r in rows)} figuras")

if __name__ == "__main__":
    main()
