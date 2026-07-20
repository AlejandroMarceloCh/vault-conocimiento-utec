---
curso: BIGDATA
titulo: 17 - Semana 15/Actividad_15_4_NLP
slides: 0
fuente: 17 - Semana 15/Actividad_15_4_NLP.ipynb
---

<div id="83c60729" class="cell markdown" id="83c60729">

# NLP:

##### Tokenización y Part of Speech

</div>

<div id="s3AOvestGZid" class="cell markdown" id="s3AOvestGZid">

Docente: Aldo Lezama Benavides

</div>

<div id="oAwJleq9GKaA" class="cell code" id="oAwJleq9GKaA">

``` python
import nltk

# Descargar los recursos necesarios (solo la primera vez)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
```

</div>

<div id="H3_2YFFrFGQd" class="cell code" id="H3_2YFFrFGQd">

``` python
# Escribimos las frases
Frase1 = u'El próximo fin de semana visitaremos Machu Picchu con toda la familia.'
Frase2 = u'Un viaje en taxi desde Miraflores hasta el Aeropuerto Jorge Chávez cuesta S/75.80.'

# Creamos una lista con las frases
Frases = [Frase1, Frase2]

# ============================
# TOKENIZACIÓN
# ============================
print("Frases tokenizadas:\n")

for Frase in Frases:
    tokens = nltk.word_tokenize(Frase)

    for token in tokens:
        print(token, end=' | ')

    print("\nNúmero de tokens =", len(tokens))
    print()
```

</div>

<div id="HBICmmGYGE0D" class="cell code" id="HBICmmGYGE0D">

``` python
# ============================
# PART OF SPEECH (PoS)
# ============================
PoS = []

print("\nFrases tokenizadas con sus respectivas PoS:\n")

for Frase in Frases:
    tokens = nltk.word_tokenize(Frase)
    pos = nltk.pos_tag(tokens)

    for palabra, etiqueta in pos:
        PoS.append((palabra, etiqueta))
        print(f"({palabra}, {etiqueta})", end=' | ')

    print("\n")
```

</div>

<div id="e2f17263" class="cell code" id="e2f17263">

``` python
# Declaración de librería para manejo de gráficos
import matplotlib.pyplot as plt

PoS_etiqueta = []

for parte in PoS:
    if parte[1] not in ['.', ',', '$']:
        PoS_etiqueta.append(parte[1])

# Asignar la cantidad de veces que aparecen en un diccionario
PoS_Count = {'Sustantivo' : PoS_etiqueta.count('NN'),
             'Pronombre' : PoS_etiqueta.count('NNP'),
             'Verbos' : PoS_etiqueta.count('VB'),
             'Adjetivos' : PoS_etiqueta.count('JJ'),
             'Adverbios' : PoS_etiqueta.count('RB'),
             'Preposiciones' : PoS_etiqueta.count('IN'),
             'Conjunciones' : PoS_etiqueta.count('CC'),
             'Interjeccciones' : PoS_etiqueta.count('UH'),
             'Determinantes' : PoS_etiqueta.count('DT')}

# Impresión de la gráfica a partir del diccionario
plt.bar(PoS_Count.keys(), PoS_Count.values())
plt.xticks(rotation = 70)
plt.title('Cantidad de veces que aparece cada PoS')
plt.show()
```

</div>
