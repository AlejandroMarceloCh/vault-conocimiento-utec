# Vault de Conocimiento — cursos UTEC (recomendador)

Cerebro de la carrera: **33 cursos · 1171 capítulos** transcritos a markdown, catalogados
(SQLite + FTS5) y vectorizados (embeddings multilingual-e5-base). Dada la descripción de un proyecto, recomienda
qué capítulos de toda la carrera aplican. El consumidor no es un humano en una web: es un **agente**
(por ejemplo Claude Code) que invoca el recomendador, lee los capítulos completos y decide.

## Estructura
- `CursosUTEC/<curso>/*.md` — los capítulos (texto).
- `Vault/_meta/` — el índice pre-construido: `catalog.sqlite` (FTS5), `embeddings.npy/.json`,
  `notes.allowlist`, `sources.lock.json`.
- `Vault/_tools/` — `recomendar.py` (búsqueda híbrida FTS + embeddings, fusión RRF), `recommend.py`
  (base FTS), `fm.py`, `build_catalog.py`, `build_embeddings.py`, `eval_recomendador.py`.

## Uso
```bash
pip install -r requirements.txt        # numpy + sentence-transformers (baja multilingual-e5-base 1 vez)
python3 Vault/_tools/recomendar.py --text "descripción de tu proyecto"
```
Devuelve JSON con **70-80 capítulos candidatos** (id, curso, título, temas, ruta al `.md`). El agente
que trabaje el proyecto lee los capítulos completos y filtra. Todo es local; no requiere internet
salvo la primera descarga del modelo.

## Calidad del recomendador (medida, reproducible)
La recuperación se evalúa con *known-item retrieval*: para cada capítulo se genera una consulta desde
su contenido y se mide en qué posición el sistema lo reencuentra entre los 1171.

- **Recall@60 ≈ 0.99** (el capítulo correcto casi siempre entra en el top).
- En este test las consultas comparten términos literales con el texto, así que la búsqueda por
  término exacto (FTS) domina el ranking (MRR más alto). La fusión híbrida no busca ganarle ahí:
  iguala su Recall@60 y añade cobertura para las consultas descritas con otras palabras, donde el
  término exacto no aparece y solo el significado (embeddings) las recupera — que es el caso de uso
  real del recomendador.
- El corte en 70-80 candidatos está calibrado: el recall satura hacia k≈60 y la coherencia semántica
  se mantiene plana, de modo que ampliar el contexto no introduce ruido.

Reproducir la evaluación:
```bash
python3 Vault/_tools/eval_recomendador.py
```

## Regenerar el índice (si agregas o editas capítulos)
```bash
python3 Vault/_tools/build_catalog.py --source CursosUTEC --allowlist Vault/_meta/notes.allowlist \
  --lock Vault/_meta/sources.lock.json --out Vault/_meta/catalog.sqlite
python3 Vault/_tools/build_embeddings.py --catalog Vault/_meta/catalog.sqlite --source CursosUTEC \
  --out Vault/_meta/embeddings.npy
```
Los `_raw`/`_sources` pesados no están en el repo: solo se incluye lo necesario para consultar.

## Instalar la skill (para que un agente lo use de forma autónoma)
Sin la skill, el agente no sabe que el vault existe. Con ella, lo consulta solo al arrancar un proyecto.
```bash
# 1. clonar y dependencias (una vez)
git clone https://github.com/AlejandroMarceloCh/vault-conocimiento-utec.git ~/vault-conocimiento-utec
cd ~/vault-conocimiento-utec && pip install -r requirements.txt
# 2. indicar a la skill dónde está el vault (agregar al ~/.bashrc o ~/.zshrc)
echo 'export VAULT_CURSOS=~/vault-conocimiento-utec' >> ~/.bashrc && source ~/.bashrc
# 3. instalar la skill
mkdir -p ~/.claude/skills && cp -r ~/vault-conocimiento-utec/skill/recomendar-capitulos ~/.claude/skills/
```
Desde cualquier repositorio, el agente puede invocar `recomendar-capitulos` para saber qué parte de la
carrera aplica a lo que esté construyendo.
