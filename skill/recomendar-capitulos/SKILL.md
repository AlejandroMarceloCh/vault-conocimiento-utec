---
name: recomendar-capitulos
description: Recomienda capítulos de los cursos de la carrera UTEC (Vault de Conocimiento) relevantes para un proyecto. Úsala al arrancar un proyecto o para saber qué de lo estudiado aplica o PODRÍA APORTAR. Dos modos - preciso (el tema exacto) y aporte (todo lo que suma, incluso lo no obvio). Descarta trampas de vocabulario o se abstiene. Corpus en el repo vault-conocimiento-utec (ruta en la variable de entorno $VAULT_CURSOS).
---

# Recomendar capítulos para un proyecto

Eres el re-ranker del sistema. Un buscador híbrido trae candidatos; TÚ decides. No necesitas API: tú eres el modelo.

**Requisito:** la variable `$VAULT_CURSOS` apunta a la carpeta donde se clonó el repo (ej.
`export VAULT_CURSOS=~/vault-conocimiento-utec`), y `pip install -r requirements.txt` ya se corrió.

## Paso 1 — traer candidatos

**MODO PRECISO:** una sola búsqueda con el texto del proyecto.

**MODO APORTE:** primero DESCOMPÓN el proyecto en sus facetas y busca por CADA una, después une los
candidatos. Un proyecto tiene varias caras y una sola búsqueda tapa la mitad. Facetas típicas:
técnica · producto de datos · datos · estadística. Corre la herramienta una vez por faceta:
```
python3 "$VAULT_CURSOS/Vault/_tools/recomendar.py" --text "<faceta>" --k-fts 10 --k-emb 15
```
Devuelve JSON: cada candidato con `id`, `curso`, `titulo`, `temas` (índice), `archivo` (ruta al capítulo).

## Paso 2 — LEE LOS CAPÍTULOS COMPLETOS (no juzgues por el índice)
La búsqueda es el eslabón DÉBIL; tú eres el fuerte. Cada candidato viene con `archivo`: la ruta a su
capítulo completo. **Lee con Read los capítulos con más chance** (5-8). El campo `temas` es solo el
índice — sirve para decidir CUÁLES abrir, NO para juzgar si sirven. Al leerlos puedes descartar con
conocimiento real, descubrir aportes que el índice no muestra, y citar la slide exacta.

## Paso 3 — elegir (DOS MODOS)
- **PRECISO** (default): el/los capítulos que calzan DIRECTO con el núcleo. Conservador 1-3. Si nada calza, abstente.
- **APORTE** (cuando piden "qué me sirve/qué suma"): como un mentor de TODA la carrera, por cada candidato
  que GENUINAMENTE aporte algo explica QUÉ aporta —incluso ángulos no obvios—. Rankea por cuánto ayuda.
  Descarta trampas puras (comparten palabras pero no aportan nada).

## Paso 4 — responder
Por cada capítulo: curso, título, la slide/rango exacto (lo sabes porque lo leíste), y QUÉ aporta al
proyecto (concreto). En modo aporte, de "núcleo" a "ángulo lateral". Si te abstienes, dilo.
