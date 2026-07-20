#!/usr/bin/env python3
"""Recomendador para AGENTES. Dado el texto de un proyecto, imprime los capítulos candidatos
(búsqueda híbrida: término exacto + significado) con su índice real. El AGENTE que llama esto
hace el re-ranking (elige los que calzan, descarta trampas de vocabulario, se abstiene si nada).
No necesita API ni modelo externo: el agente ES el modelo."""
import argparse, json, os, re, sqlite3, sys
import numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); V=os.path.abspath(os.path.join(HERE,".."))
CU=os.environ.get("VAULT_CURSOS_MD") or os.path.join(os.path.dirname(V),"CursosUTEC")  # portable: hermano de Vault (Mac y server)
def indice(path):
    t=open(f"{CU}/{path}").read(); m=re.search(r"##\s*Índice\s*(.+?)(?=\n##\s|\Z)",t,re.S)
    return re.sub(r"\s+"," ",re.sub(r"[#*`>|]"," ",m.group(1) if m else ""))[:300]
def main():
    # k altos a propósito: el recomendador trae ~70-80 candidatos (coherencia plana hasta k=100, 98% del top: más contexto para el agente sin ruido) y el AGENTE decide (lee y filtra).
    ap=argparse.ArgumentParser(); ap.add_argument("--text",required=True); ap.add_argument("--k-fts",type=int,default=48); ap.add_argument("--k-emb",type=int,default=72)
    a=ap.parse_args()
    if not a.text.strip():   # query vacía -> sin candidatos, no crashea
        print(json.dumps({"proyecto":a.text,"candidatos":[]},ensure_ascii=False,indent=1)); return
    c=sqlite3.connect(f"{V}/_meta/catalog.sqlite")
    meta={r[0]:(r[1],r[2],r[3]) for r in c.execute("SELECT id,path,title,course FROM chapters")}
    import subprocess
    try:   # FTS degrada a [] si recommend.py falla (ej. query de 1 char que rompe FTS5); el embedding igual matchea
        _out=subprocess.run([sys.executable,f"{HERE}/recommend.py","--catalog",f"{V}/_meta/catalog.sqlite","--no-cite","--k",str(a.k_fts),"--min-score","0","--text",a.text],capture_output=True,text=True).stdout
        fts=[r["id"] for r in json.loads(_out)["recomendaciones"]]
    except (json.JSONDecodeError, KeyError):
        fts=[]
    em=json.load(open(f"{V}/_meta/embeddings.json")); vecs=np.load(f"{V}/_meta/embeddings.npy")
    from sentence_transformers import SentenceTransformer
    qv=SentenceTransformer(em["model"]).encode([f"query: {a.text}"],normalize_embeddings=True)[0]
    emb=[em["ids"][i] for i in np.argsort(-(vecs@qv))[:a.k_emb]]
    # Reciprocal Rank Fusion: rankea por consenso de ambos rankings en vez de concatenar, así los
    # capítulos que aparecen en FTS y en embeddings suben. Métricas en eval_recomendador.py.
    K=60; score={}
    for r,iid in enumerate(fts): score[iid]=score.get(iid,0)+1.0/(K+r+1)
    for r,iid in enumerate(emb): score[iid]=score.get(iid,0)+1.0/(K+r+1)
    order=[iid for iid in sorted(score,key=lambda i:-score[i]) if iid in meta]
    cands=[{"id":iid,"curso":meta[iid][2],"titulo":meta[iid][1],"temas":indice(meta[iid][0]),
            "archivo":f"{CU}/{meta[iid][0]}"} for iid in order]   # archivo = para que el agente lo LEA ENTERO
    print(json.dumps({"proyecto":a.text,"candidatos":cands},ensure_ascii=False,indent=1))
if __name__=="__main__": main()
