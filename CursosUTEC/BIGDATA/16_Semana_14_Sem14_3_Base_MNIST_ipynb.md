---
curso: BIGDATA
titulo: 16 - Semana 14/Sem14_3 Base MNIST
slides: 0
fuente: 16 - Semana 14/Sem14_3 Base MNIST.ipynb
---

<div id="5c762af0-0687-4c97-9b5c-eec5096fc78c" class="cell markdown">

#### MNIST

Docente: Aldo Lezama Benavides

</div>

<div id="0fd33933-2dbf-4a51-aa71-b9465eca8aa9" class="cell markdown">

#### Modelo Básico

- Dataset
- Red neuronal
- Entrenamiento

</div>

<div id="217d2502-13ee-41ea-9215-015ec1c9865f" class="cell code">

``` python
import tensorflow as tf

(X_train, y_train), _ = tf.keras.datasets.mnist.load_data()

X_train = X_train / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy')

model.fit(X_train, y_train, epochs=5)
```

</div>

<div id="8040c17f-4201-46bf-a852-a294ff3bd17d" class="cell markdown">

#### Agregar evaluación de desempeño

</div>

<div id="b23cf56f-d665-4218-9294-52f2f99108a9" class="cell code">

``` python
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=5)

loss, acc = model.evaluate(X_test, y_test)

print("Accuracy",acc)
```

</div>

<div id="53c506f9-a865-41cc-9774-d32445d0f7ce" class="cell markdown">

#### Visualización

</div>

<div id="66f80b43-4c52-46e0-922b-ca033a3d7a05" class="cell code">

``` python
import matplotlib.pyplot as plt

plt.imshow(X_train[0], cmap='gray')
plt.title(f"Etiqueta: {y_train[0]}")
plt.show()
```

</div>

<div id="6caa0472-a80d-407a-9538-c1840274d1e4" class="cell markdown">

#### Predicciones

</div>

<div id="8d4f92c5-7d1c-435d-ad07-cff897fe3470" class="cell code">

``` python
import numpy as np

pred = model.predict(X_test[:1])

print(pred)

print("Clase predicha:", np.argmax(pred))
```

</div>

<div id="a813ec9e-6698-4cff-9575-aeca1e7309a4" class="cell markdown">

#### Agregamos una capa oculta

</div>

<div id="6d817fd6-8815-43ef-91ed-b43401287c88" class="cell code">

``` python
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=5)

loss, acc = model.evaluate(X_test, y_test)

print("Accuracy",acc)
```

</div>

<div id="81172502-e009-47d4-9627-cd882c07dfd6" class="cell markdown">

#### Agregamos resumen

</div>

<div id="b659dd27-e886-414f-a10b-54c05ee7ffc7" class="cell code">

``` python
model.summary()
```

</div>

<div id="c7c61bc4-0dca-4740-9730-c9db47ceae97" class="cell markdown">

#### Agregar validación

</div>

<div id="25085b3e-583a-4f02-b8cc-2a70225b5222" class="cell code">

``` python
history = model.fit(X_train,y_train,validation_split=0.2, epochs=10)
```

</div>

<div id="f06556f8-3019-434c-98d8-99dd613e0d15" class="cell markdown">

#### Visualización

</div>

<div id="efaf3b83-fb8a-4ba1-b229-75c331fdfce7" class="cell code">

``` python
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.legend(['Train','Validation'])
plt.show()
```

</div>

<div id="80e66798-c74c-42c2-9fc4-56c232e0208a" class="cell markdown">

#### Modelo Terminado

</div>

<div id="0642f74e-5550-4823-b298-bca199b96ef8" class="cell code">

``` python
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

early_stop = tf.keras.callbacks.EarlyStopping(
    patience=3,
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=20,
    callbacks=[early_stop]
)

model.evaluate(X_test, y_test)
```

</div>

<div id="53b33006-3229-4ca4-b2e2-c87684a4d760" class="cell code">

``` python
plt.figure(figsize=(12,5))

# Accuracy
plt.subplot(1,2,1)
plt.plot(history.history['accuracy'], marker='o')
plt.plot(history.history['val_accuracy'], marker='o')
plt.title('Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'])
plt.grid(True)

# Loss
plt.subplot(1,2,2)
plt.plot(history.history['loss'], marker='o')
plt.plot(history.history['val_loss'], marker='o')
plt.title('Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'])
plt.grid(True)

plt.tight_layout()
plt.show()
```

</div>

<div id="082729de-dcff-4028-89b9-1dfcf84aa724" class="cell code">

``` python
```

</div>
