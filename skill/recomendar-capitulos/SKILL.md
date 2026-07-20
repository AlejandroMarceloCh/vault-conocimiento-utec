---
name: recomendar-capitulos
description: Recomienda capítulos de los cursos de la carrera UTEC (Vault de Conocimiento) relevantes para un proyecto. Úsala al arrancar un proyecto o para saber qué de lo estudiado aplica o PODRÍA APORTAR. Dos modos - preciso (el tema exacto) y aporte (todo lo que suma, incluso lo no obvio). Descarta trampas de vocabulario o se abstiene. Corpus en el repo vault-conocimiento-utec (ruta en la variable de entorno $VAULT_CURSOS).
---

# Recomendar capítulos para un proyecto

Eres el re-ranker del sistema. Un buscador híbrido trae candidatos; TÚ decides. No necesitas API: tú eres el modelo.

**Requisito:** la variable `$VAULT_CURSOS` apunta a la carpeta donde se clonó el repo (ej.
`export VAULT_CURSOS=~/vault-conocimiento-utec`), y `pip install -r requirements.txt` ya se corrió.

## Paso 1 — traer candidatos (SIEMPRE busca con dos textos y une)

Tu proyecto se describe con palabras de usuario ("app de reservas de gimnasio"); los capítulos usan
vocabulario técnico ("base de datos, modelo entidad-relación, control de aforo, API"). Buscar solo con
la frase cruda pierde la mitad. **Regla medida (sube el recall de cursos relevantes +0.12): busca con
DOS textos y une los candidatos** (quita duplicados por `id`):

1. **La frase cruda** del proyecto, tal cual.
2. **Una versión enriquecida**: reescribe el proyecto con el vocabulario técnico que tendría un
   capítulo relevante —conceptos, métodos y herramientas del dominio—. Ej.: "app de reservas de
   gimnasio con aforo" → "gestión de reservas, base de datos de usuarios y horarios, control de
   capacidad, arquitectura cliente-servidor, API, modelo entidad-relación".

```
python3 "$VAULT_CURSOS/Vault/_tools/recomendar.py" --text "<frase cruda>"
python3 "$VAULT_CURSOS/Vault/_tools/recomendar.py" --text "<versión enriquecida>"
```

**MODO APORTE** (cuando piden "qué me sirve / qué suma"): además descompón el proyecto en facetas
(técnica · producto de datos · datos · estadística) y busca también por cada una. Más ángulos, más
cobertura.

Cada candidato trae `id`, `curso`, `titulo`, `temas` (índice), `archivo` (ruta al capítulo).

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
