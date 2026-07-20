---
curso: BIGDATA
titulo: 16 - Semana 14/Sem14_1 Tensorflow
slides: 0
fuente: 16 - Semana 14/Sem14_1 Tensorflow.ipynb
---

<div id="cbfc4c59-6620-44dc-99b3-93f4fd64cc47" class="cell markdown">

## TensorFlow

</div>

<div id="1b2eb71c-290d-46fb-9c93-ea576d7a0206" class="cell markdown">

Docente: Aldo Lezama Benavides

</div>

<div id="a418b88f-067c-4181-ac72-1e1fd14dd4c1" class="cell markdown">

#### 1. ¿Qué es TensorFlow?

TensorFlow es una biblioteca de código abierto desarrollada por TensorFlow para construir modelos de Machine Learning y Deep Learning.

Su objetivo es facilitar:

- Manipulación eficiente de datos.
- Construcción de redes neuronales.
- Entrenamiento en CPU, GPU y TPU.
- Despliegue de modelos en producción.

TensorFlow utiliza estructuras llamadas tensores para representar los datos y realiza cálculos optimizados sobre ellos.

</div>

<div id="ea75f76d-e410-4100-9b2d-38a7eb737847" class="cell markdown">

#### 2. Tensores: La Unidad Fundamental

Un tensor es una generalización de los arreglos de NumPy.

Todo en TensorFlow se representa mediante tensores:

- Datos de entrada
- Pesos de una red neuronal
- Resultados intermedios
- Predicciones

#### Tipos de Tensores

| Tipo    | Dimensión | Ejemplo            |
|---------|-----------|--------------------|
| Escalar | 0D        | `5`                |
| Vector  | 1D        | `[1, 2, 3]`        |
| Matriz  | 2D        | `[[1, 2], [3, 4]]` |
| Tensor  | 3D+       | Imágenes, videos   |

</div>

<div id="77ea35df-d6be-4bc0-a073-4a58bf88a086" class="cell code">

``` python
# !pip install tensorflow
```

</div>

<div id="e0faec42-a7ea-4a30-a3db-31e8dfb3955a" class="cell code">

``` python
import tensorflow as tf
```

</div>

<div id="a82a6b8f-fb13-4c53-a59b-82666cc46166" class="cell code">

``` python
escalar = tf.constant(10)
print(escalar)
```

</div>

<div id="c32ebf10-f385-4fe1-9744-6d42a138836b" class="cell code">

``` python
vector = tf.constant([1,2,3])
print(vector)
```

</div>

<div id="e43c4fe0-2f4d-4686-bf29-30d90c049557" class="cell code">

``` python
matriz = tf.constant([[1,2],[3,4]])
print(matriz)
```

</div>

<div id="9beb0423-cc24-404a-92d6-7d487099f242" class="cell markdown">

#### 3. Formas (Shapes)

Teoría

Cada tensor posee una forma (shape) que describe sus dimensiones.

Ejemplos:

\[1,2,3\] -\> (3,)

\[\[1,2\],\[3,4\]\] -\> (2,2)

Imagen RGB -\> (alto, ancho, 3)

Las formas son fundamentales porque las capas neuronales esperan entradas con dimensiones específicas.

</div>

<div id="91be363d-f807-4378-b57e-85ed46e3c7a0" class="cell code">

``` python
print(escalar.shape)
```

</div>

<div id="6f3334fe-2aa0-4d25-aebe-98bbebb8d8fa" class="cell code">

``` python
print(vector.shape)
```

</div>

<div id="6bd16940-7590-4031-bdb3-6dac5ddbd79d" class="cell code">

``` python
print(matriz.shape)
```

</div>

<div id="e3ef8270-214c-4dee-bada-be6ff313f2f1" class="cell markdown">

#### 4. Operaciones Matemáticas

Teoría

TensorFlow implementa operaciones vectorizadas similares a NumPy, pero optimizadas para hardware acelerado.

Las operaciones se ejecutan sobre todos los elementos simultáneamente.

</div>

<div id="b9be6440-0473-4c02-b1bc-2593a6708dc9" class="cell code">

``` python
a = tf.constant([1,2,3])

b = tf.constant([4,5,6])
```

</div>

<div id="70d88812-e0ea-4c74-97b4-e8075c060194" class="cell code">

``` python
print(tf.add(a,b))
```

</div>

<div id="871964cf-a6b2-4907-b7df-b0c654993220" class="cell code">

``` python
print(tf.multiply(a,b))
```

</div>

<div id="d41af7d5-95fe-4d4d-9816-c193319a7088" class="cell code">

``` python
print(tf.reduce_sum(a))
```

</div>

<div id="10a853f4-3155-4223-966b-d1dfeb39c98b" class="cell markdown">

#### 5. Variables

Teoría

Existen dos tipos principales de tensores:

</div>

<div id="bc6f44d8-ef8a-4adb-ae99-15387446a6ab" class="cell markdown">

#### Constantes

No cambian.

</div>

<div id="3c47f348-ed86-4dfe-8f58-16a258e8afa6" class="cell code">

``` python
tf.constant()
```

</div>

<div id="11dd732d-93fe-45fd-8233-9b8972b5fb80" class="cell markdown">

#### Variables

Pueden modificarse durante el entrenamiento.

</div>

<div id="9b1c31c4-6e89-487b-9acd-72d0264189aa" class="cell code">

``` python
tf.Variable()
```

</div>

<div id="f24f3c31-f7b0-449a-bdf6-c0a41d87a52d" class="cell markdown">

Los pesos de una red neuronal son variables.

</div>

<div id="e45d4049-189d-444e-99b5-7db41e7a0a55" class="cell code">

``` python
peso = tf.Variable(2.0)

print(peso)

peso.assign(5.0)

print(peso)
```

</div>

<div id="3428bcbd-6c24-4a80-b421-09c37bf4a0b4" class="cell markdown">

#### 6. Conversión con NumPy

TensorFlow y NumPy trabajan muy bien juntos.

Es común:

Cargar datos con Pandas Convertirlos a NumPy Pasarlos a TensorFlow

</div>

<div id="f28d7c5e-8267-4fdd-bed8-8d650fcd40ed" class="cell code">

``` python
import numpy as np

arr = np.array([1,2,3])
print(arr)
```

</div>

<div id="abedef75-712e-4fa4-8331-c0d65c0e8d13" class="cell code">

``` python
tensor = tf.convert_to_tensor(arr)
print(tensor)
```

</div>

<div id="a5910dd8-dc9e-435a-abb9-d049c6e76fb8" class="cell code">

``` python
print(tensor.numpy())
```

</div>

<div id="ad4b8cfc-207c-495b-a739-54a8a3a74bc0" class="cell markdown">

#### 7. GradientTape: Derivación Automática

El aprendizaje profundo se basa en calcular derivadas para ajustar los pesos.

TensorFlow utiliza:

</div>

<div id="f914c151-1e57-4f8e-8153-f634c854e27a" class="cell code">

``` python
tf.GradientTape()
```

</div>

<div id="f8472e23-0cb7-4c93-924c-f5d657af3e24" class="cell markdown">

para registrar operaciones y calcular gradientes automáticamente.

</div>

<div id="5bfab6db-2d6c-40e8-af0b-362f9084eae9" class="cell code">

``` python
x = tf.Variable(3.0)

with tf.GradientTape() as tape:
    y = x**2

gradiente = tape.gradient(y, x)

print(gradiente.numpy())
```

</div>

<div id="5fa86a55-2919-4b38-bf6e-265a60279fc1" class="cell markdown">

#### 8. Tipos de Datos (dtypes)

TensorFlow maneja distintos tipos de datos:

tf.int32

tf.int64

tf.float32

tf.float64

tf.bool

tf.string

</div>

<div id="e62fe750-27d9-49a0-9b90-9c3345cfe02e" class="cell code">

``` python
x = tf.constant([1,2,3], dtype=tf.float32)

print(x.dtype)
```

</div>

<div id="ccff8804-f068-494d-8edb-c76e8f822913" class="cell markdown">

#### 9. Manipulación de Tensores

#### Reshape

Cambiar dimensiones

</div>

<div id="6a1f75c8-72f0-4609-b78c-fd4f2986a5f7" class="cell code">

``` python
x = tf.constant([1,2,3,4,5,6])

x = tf.reshape(x,(2,3))

print(x)
```

</div>

<div id="8f22ea75-61af-46fb-99f2-e495eccc6bbe" class="cell markdown">

#### Transpose

Intercambiar filas y columnas.

</div>

<div id="ef1a2692-1e06-47ef-ae07-efbceacefbbc" class="cell code">

``` python
x = tf.constant([[1,2],[3,4]], dtype='float64')

tf.transpose(x)
```

</div>

<div id="c886688a-8da7-44f4-ad6b-b0a1759956f4" class="cell markdown">

#### Concatenación

</div>

<div id="e9496590-400a-464b-ba6a-f58b1693a45a" class="cell code">

``` python
a = tf.constant([1,2])

b = tf.constant([3,4])

tf.concat([a,b], axis=0)
```

</div>

<div id="a5e6eee0-d2e7-4c44-a64b-d133aaac4c00" class="cell markdown">

#### 10. Broadcasting

TensorFlow puede expandir dimensiones automáticamente.

</div>

<div id="56808e0a-b767-4a74-981f-408962748d92" class="cell code">

``` python
a = tf.constant([[1,2],[3,4]])

b = tf.constant(10)

print(a + b)
```

</div>

<div id="bd9f7ade-adb0-4c79-861b-e664ee8e028e" class="cell markdown">

#### 11. Operaciones Lineales

Muy utilizadas en Deep Learning.

Multiplicación matricial

</div>

<div id="28f48c8c-03b8-4027-b099-8c9a186cab89" class="cell code">

``` python
A = tf.constant([[1,2],[3,4]])

B = tf.constant([[5,6],[7,8]])

tf.matmul(A,B)
```

</div>

<div id="e06c6314-5dc6-4bab-bdb3-7b815cc91ece" class="cell markdown">

#### 12. Decorador @tf.function

Convierte código Python en un grafo optimizado.

</div>

<div id="1206bb76-49ae-4e35-b72b-b15496addcf3" class="cell code">

``` python
@tf.function
def suma(a,b):
    return a+b
```

</div>

<div id="01c89bb4-3c74-4a83-95d4-b5e9c9ad36b6" class="cell markdown">

Beneficios:

- Más rápido
- Menos memoria
- Compatible con despliegue

</div>

<div id="878c1fa1-87cd-46eb-be62-f2cb37e8ec9b" class="cell markdown">

#### 13. Funciones de Activación

</div>

<div id="4d7b3728-ba6c-4a23-ad9d-b2f7ec6e5c72" class="cell code">

``` python
tf.keras.activations.relu(x)
```

</div>

<div id="1cf1f36a-6b62-459d-b699-04f7fc310752" class="cell code">

``` python
tf.keras.activations.softmax(x)
```

</div>

<div id="ab3c5ed8-b347-4831-835e-556fc0295293" class="cell code">

``` python
tf.keras.activations.sigmoid(x)
```

</div>

<div id="fd6c21a6-8ddd-4356-a763-e1c0730d8a69" class="cell code">

``` python
tf.keras.activations.tanh(x)
```

</div>

<div id="4a8c266a-befd-4fe8-af62-4c10af8e0a55" class="cell markdown">

#### 14. Optimizadores

</div>

<div id="a88877d3-7fa8-4658-ad5f-7cb571b31a07" class="cell markdown">

#### SGD (Stochastic Gradient Descent)

Es el optimizador más básico.

</div>

<div id="f7d1f7dd-439e-4efc-93bb-c701342147f6" class="cell code">

``` python
tf.keras.optimizers.SGD()
```

</div>

<div id="7acac679-d5c2-4f98-a0fc-de8cf497ad89" class="cell markdown">

Actualiza los pesos usando directamente los gradientes.

Ventajas:

- Fácil de entender
- Poco consumo de memoria

Desventajas:

- Puede ser lento
- Puede atascarse en mínimos locales

</div>

<div id="1179a1d5-0a84-4fa4-8f86-c9e4595f81ca" class="cell markdown">

#### SGD con Momentum

Introduce "inercia" en los movimientos.

</div>

<div id="a53eea86-8af1-4b6b-a9d4-91ddb7423d42" class="cell code">

``` python
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01,momentum=0.9)
```

</div>

<div id="d1830290-d2ad-4302-9a96-9f0ef8d16ca6" class="cell markdown">

Ventaja:

- Convergencia más rápida.

</div>

<div id="63f0d8cf-d26e-4b9a-8a98-06870c8e72a0" class="cell markdown">

#### Adam (Adaptive Moment Estimation)

Es el optimizador más utilizado actualmente.

</div>

<div id="7dcff549-b583-4caf-82c8-903e57ecc57a" class="cell code">

``` python
tf.keras.optimizers.Adam()
```

</div>

<div id="b8251441-3c5a-4feb-8933-49d5b17d1a3b" class="cell markdown">

Combina:

- Momentum
- Adaptive Learning Rate

Ventajas:

- Rápido
- Robusto
- Funciona bien en muchos problemas

</div>

<div id="3642788e-25ae-4492-afaa-2ea2ce2927b8" class="cell markdown">

#### RMSProp

Ajusta automáticamente el tamaño de los pasos.

</div>

<div id="eff911ec-8efb-4769-acd3-914d4db6e82b" class="cell code">

``` python
tf.keras.optimizers.RMSprop()
```

</div>

<div id="4e220033-2e2b-4c28-a437-a79ccec38870" class="cell markdown">

Muy utilizado históricamente en:

- RNN
- LSTM
- Series temporales

</div>

<div id="97fcbe03-0023-42db-9107-47bb842f578a" class="cell markdown">

#### 15. Funciones de Pérdida

</div>

<div id="e690757a-02d4-47ce-9623-b96d95f07269" class="cell code">

``` python
# Clasificación Binaria
tf.keras.losses.BinaryCrossentropy()
```

</div>

<div id="9dfefd3c-ff58-4b61-8824-91b0b32c6d2f" class="cell code">

``` python
# Clasificación Multiclase
tf.keras.losses.SparseCategoricalCrossentropy()
```

</div>

<div id="d574530e-bd68-4475-82cb-e7417f1d1568" class="cell code">

``` python
# Regresión
tf.keras.losses.MeanSquaredError()
```

</div>

<div id="4b1352e2-f141-4fd9-abac-29604e7c8d6c" class="cell code">

``` python
# Regresión
tf.keras.losses.MeanAbsoluteError()
```

</div>

<div id="cd523b6e-2e7d-439c-bfa8-92fcefb5ebdd" class="cell markdown">

#### 16. Regularización

</div>

<div id="307fb61a-62b3-46d0-b131-680b8f5766f5" class="cell markdown">

##### Problema: Overfitting

Cuando el modelo memoriza.

</div>

<div id="869d3384-e972-4240-8ba4-bcd96f4fe231" class="cell markdown">

##### Dropout

Apaga neuronas aleatoriamente.

</div>

<div id="6ef11d5f-6c9d-4413-9c76-2e72597b1cd9" class="cell code">

``` python
# 20% de neuronas desactivadas.
from tensorflow.keras.layers import Dropout
Dropout(0.2)
```

</div>

<div id="61e51a69-f19c-48c1-a076-e8b6680f67b9" class="cell markdown">

##### L2 Regularization

</div>

<div id="0b6439ea-ec36-456f-87e6-7fc487adf7c9" class="cell markdown">

<code>Dense(64,kernel_regularizer=tf.keras.regularizers.l2(0.001)) </code>

</div>

<div id="c7ce4243-888b-44c2-bfd1-8bf0b6d80cb5" class="cell markdown">

#### 17. Batch Normalization

Acelera entrenamiento.

</div>

<div id="635eae5b-9351-43fd-8b59-7f5055bf3dfc" class="cell code">

``` python
from tensorflow.keras.layers import BatchNormalization

BatchNormalization()
```

</div>

<div id="df6e189f-dcce-4928-ab35-adf809103bbb" class="cell markdown">

Muy común en CNNs modernas

</div>

<div id="be305265-b448-41e6-8d44-5af8793813fe" class="cell markdown">

#### 18. TensorBoard

Permite visualizar:

- Loss
- Accuracy
- Arquitectura
- Histogramas

</div>

<div id="83ba0bba-7d53-4d51-a89d-3eda8af99c57" class="cell code">

``` python
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs")
```

</div>
