---
curso: BIGDATA
titulo: 17 - Semana 15/Actividad 15_3_N gram
slides: 0
fuente: 17 - Semana 15/Actividad 15_3_N gram.ipynb
---

<div class="cell markdown" id="YP8ngl4_s2hN">

# **N-gram**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="qR7kOITFognl">

``` python
from collections import Counter
import pandas as pd
import re

file_path = "discurso.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

print("Texto cargado correctamente.")
```

</div>

<div class="cell code" id="W3igpz-dojdN">

``` python
# --- TOKENIZACIÓN ---
# Convierte todo a minúsculas y toma solo palabras
tokens = re.findall(r'\b\w+\b', text.lower())
```

</div>

<div class="cell code" id="iqzPXAkHojgM">

``` python
# --- UNIGRAMAS ---
unigram_counts = Counter(tokens)
```

</div>

<div class="cell code" id="wsxmAkzKojjC">

``` python
# --- BIGRAMAS ---
bigrams = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
bigram_counts = Counter(bigrams)
```

</div>

<div class="cell code" id="8mUchqevonEI">

``` python
# --- DATAFRAME UNIGRAM ---
df_unigrams = (pd.DataFrame(unigram_counts.items(), columns=["Unigram", "Count"]).sort_values("Count", ascending=False))
```

</div>

<div class="cell code" id="uJbeUwz3onHe">

``` python
# --- DATAFRAME BIGRAM ---
df_bigrams = (pd.DataFrame([(" ".join(k), v) for k, v in bigram_counts.items()],columns=["Bigram", "Count"]).sort_values("Count", ascending=False))
```

</div>

<div class="cell code" id="IACjI8XqonKB">

``` python
# --- MOSTRAR RESULTADOS ---
print("=== UNIGRAMAS ===")
print(df_unigrams)
```

</div>

<div class="cell code" id="tnW0RZrKo3wt">

``` python
# --- MOSTRAR RESULTADOS ---
print("\n=== BIGRAMAS ===")
print(df_bigrams)
```

</div>
