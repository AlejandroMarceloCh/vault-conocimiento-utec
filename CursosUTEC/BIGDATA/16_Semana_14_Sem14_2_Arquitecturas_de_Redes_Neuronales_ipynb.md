---
curso: BIGDATA
titulo: 16 - Semana 14/Sem14_2 Arquitecturas de Redes Neuronales
slides: 0
fuente: 16 - Semana 14/Sem14_2 Arquitecturas de Redes Neuronales.ipynb
---

<div class="cell markdown" id="Io-uZaOIGUVI">

## Arquitectura de Redes Neuronales en TensorFlow

</div>

<div class="cell markdown" id="To22rbE7GTj_">

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell markdown" id="At7PU1aED3eR">

**Creación de un perceptrón simple**

------------------------------------------------------------------------

- Sequential: construye el modelo capa por capa en forma lineal.

- Dense(1): una capa totalmente conectada con 1 neurona.

- input_shape=(10,): indica que el modelo recibirá 10 features de entrada.

- optimizer='sgd': descenso del gradiente.

- loss='mse': error cuadrático medio.

Es el equivalente a una regresión lineal multivariada.

</div>

<div class="cell code" id="dhDlljM5C5c9">

``` python
from tensorflow.keras import Sequential, layers
from tensorflow.keras.utils import plot_model

model = Sequential([layers.Dense(1, input_shape=(10,))])

model.summary()
plot_model(model, "perceptron.png", show_shapes=True)
```

</div>

<div class="cell markdown" id="YcRPrTl-ENwy">

**Creación de un MLP para clasificación**

------------------------------------------------------------------------

- Primera capa Dense(8): 8 neuronas, aplica ReLU → permite capturar no linealidades.

- Segunda capa Dense(1): salida escalar, útil para regresión.

- Al usar más neuronas, la red puede representar funciones más complejas que un perceptrón simple.

Parámetros:

Primera capa: 10×8 + 8 = 88

Segunda capa: 8×1 + 1 = 9 Total = 97

</div>

<div class="cell code" id="yhdjZs9cC-Mr">

``` python
model = Sequential([
    layers.Dense(8, activation='relu', input_shape=(10,)),
    layers.Dense(1)
])

model.summary()
plot_model(model, "mlp_clasificación.png", show_shapes=True)
```

</div>

<div class="cell markdown" id="u2HfpEN5Et23">

**Creación de un MLP regresión**

</div>

<div class="cell code" id="XpWHBG23FVU4">

``` python
model = Sequential([
    layers.Dense(15, activation='relu', input_shape=(10,)),
    layers.Dense(1)
])

model.summary()
plot_model(model, "mlp_rgresión.png", show_shapes=True)
```

</div>
