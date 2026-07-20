---
curso: BIGDATA
titulo: 17 - Semana 15/Actividad 15_5_Predicción_Texto
slides: 0
fuente: 17 - Semana 15/Actividad 15_5_Predicción_Texto.ipynb
---

<div class="cell markdown" id="-af1U9x_vMeA">

# **Predicción Bigram y Trigram**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="AnumyHccvSCm">

``` python
import re
from collections import Counter
import random

# ===========================================================
# 1. Texto
# ===========================================================
file_path = "discurso.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

print("Texto cargado correctamente.")
```

</div>

<div class="cell code" id="pc8-0Sf_vSFx">

``` python
# ======================================================
# 2. Limpieza y tokenización
# ======================================================
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-záéíóúüñ\s]", "", text)
    tokens = text.split()
    return tokens

tokens = preprocess(text)
```

</div>

<div class="cell code" id="8fvkwD4ivSIn">

``` python
# ======================================================
# 3. Construcción de n-gramas
# ======================================================
# Bigrams
bigrams = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
bigram_counts = Counter(bigrams)
unigram_counts = Counter(tokens)

# Trigrams
trigrams = [(tokens[i], tokens[i+1], tokens[i+2])
            for i in range(len(tokens)-2)]
trigram_counts = Counter(trigrams)
```

</div>

<div class="cell code" id="BvtBxiJ-vSLZ">

``` python
# ======================================================
# 4. Probabilidades MLE
# ======================================================

# ---------- BIGRAM ----------
def bigram_prob(w1, w2):
    num = bigram_counts[(w1, w2)]
    den = unigram_counts[w1]
    if den == 0:
        return 0
    return num / den


def predict_bigram(w1):
    # obtener candidatos que comienzan con w1
    candidates = {w2: bigram_counts[(w1, w2)]
                  for (x, w2) in bigram_counts if x == w1}

    if not candidates:
        return None

    # predicción MLE = más frecuente
    return max(candidates, key=candidates.get)

# ---------- TRIGRAM ----------
def trigram_prob(w1, w2, w3):
    num = trigram_counts[(w1, w2, w3)]
    den = bigram_counts[(w1, w2)]
    if den == 0:
        return 0
    return num / den


def predict_trigram(w1, w2):
    candidates = {w3: trigram_counts[(w1, w2, w3)]
                  for (x, y, w3) in trigram_counts if x == w1 and y == w2}

    if not candidates:
        return None

    return max(candidates, key=candidates.get)
```

</div>

<div class="cell code" id="w1SCaIg_ugbl">

``` python
# ======================================================
# 5. Pruebas de predicción
# ======================================================
print("=== Predicción Bigram ===")
w1 = "en"
print(f"Contexto: ({w1})")
print("Predicción:", predict_bigram(w1))

print("\n=== Predicción Trigram ===")
context = ("viva", "el")
print(f"Contexto: {context}")
print("Predicción:", predict_trigram(*context))
```

</div>
