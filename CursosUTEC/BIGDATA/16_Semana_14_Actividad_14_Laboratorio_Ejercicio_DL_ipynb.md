---
curso: BIGDATA
titulo: 16 - Semana 14/Actividad 14_Laboratorio Ejercicio DL
slides: 0
fuente: 16 - Semana 14/Actividad 14_Laboratorio Ejercicio DL.ipynb
---

<div class="cell code" id="yxzC7NgaXi8a">

``` python
# Librerias

import numpy as ___
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.___ as plt
```

</div>

<div class="cell code" id="r1zoQsWuXs8E">

``` python
# Parametros de la base de datos
num_classes = ___
input_shape = (___, ___, 1)

# Cargar los datos y dividirlos en los sets necesarios
(___, ___), (___, ___) = keras.datasets.mnist.load_data()

# Escalar las imagenes entre [0, 1]
x_train = x_train.astype("float32") / ___
x_test = x_test.astype("float32") / ___

# Añadir una dimension para el modelo (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

print(x_train.shape[0], "Cantidad de muestras para entrenamiento")
print(x_test.shape[0], "Cantidad de muestras para pruebas")


# Convertir las clases a un sistema de salida
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
```

</div>

<div class="cell code" id="XsACFtpZq0Ef">

``` python
# Visualizar los datos

plt.figure(figsize=(5,5))
for i in range(0,9):
  plt.___(3,3,i+1)
  plt.___(x_train[i].reshape((28,28)))
plt.___()
```

</div>

<div class="cell code" id="ifayKEHxYHnq">

``` python
#Construir el modelo de acuerdo a las diapositivas

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(6, kernel_size=(5, 5), activation="relu", padding = 'valid'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(16, kernel_size=(5, 5), activation="relu", padding = 'valid'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.___(256),
        layers.___(120),
        layers.___(84),
        layers.___(___, activation="softmax"),
    ]
)

model.summary()
```

</div>

<div class="cell code" id="PaLddduhYMtA">

``` python
# Entrenar el modelo

batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.___(___, ___, batch_size=batch_size, epochs=epochs, validation_split=0.1)
```

</div>

<div class="cell code" id="0uYMbMh6YQOa">

``` python
# Evaluar el modelo

score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
```

</div>

<div class="cell code" id="WuOZ9U9_tMAE">

``` python
x_test[0].shape
```

</div>

<div class="cell code" id="5kCRqg4ws1NE">

``` python
# Ver los resultados de testing
resultados = model.___(x_test[0:9])
for i in range(___,___):
  print('Prediccion: ',resultados[i].___())
  print('Real: ', y_test[i].___())
  plt.figure(figsize=(2,2))
  plt.imshow(x_test[i].reshape((28,28)))
  plt.show()
```

</div>
