---
curso: BIGDATA
titulo: 16 - Semana 14/Sem14_ Deep Learning
slides: 46
fuente: 16 - Semana 14/Sem14_ Deep Learning.pdf
---

## Slide 1

Portada (decorativa): fondo cian con foto del edificio UTEC.

**Deep Learning**
Mg. Aldo Lezama Benavides
Semana 14

## Slide 2

**Objetivo de la sesión**

1. **Comprender** los fundamentos del Deep Learning, identificando sus diferencias con el Machine Learning tradicional y sus principales ventajas y limitaciones.
2. **Explicar** el funcionamiento de las Redes Neuronales Profundas y las Redes Neuronales Convolucionales (CNN), analizando sus componentes, proceso de entrenamiento y arquitectura.
3. **Aplicar** los conceptos de CNN en problemas de clasificación de imágenes, conociendo el uso de conjuntos de datos como MNIST y las arquitecturas más representativas como AlexNet, VGG, GoogleNet y ResNet.

Los tres puntos van dentro de un marco de corchetes blancos.

## Slide 3

**Contenido de la sesión**

Cuatro bloques en fila, cada uno dentro de corchetes blancos con un número grande arriba:

| 01. | 02. | 03. | 04. |
|---|---|---|---|
| Modelos de Deep Learning | Redes Neuronales Profundas | Redes Neuronales Convolucionales | Clasificación con CNN |

## Slide 4

Separador de sección: **01. Modelos de Deep Learning** (número grande "01." entre corchetes, ícono de portapapeles con checklist).

## Slide 5

**IA - ML - DL**

Diagrama de círculos concéntricos (diagrama de Venn anidado), cada uno con una flecha a un cuadro de texto a la derecha:

- Círculo exterior azul claro — **Artificial Intelligence** → "Capacidad de la máquina para imitar el comportamiento humano."
- Círculo medio verde — **Machine Learning** → "Subconjunto de IA que permite que un sistema aprenda y mejore automáticamente a partir de la experiencia."
- Círculo interior rosado — **Deep Learning** → "Subconjunto de Machine Learning usando algoritmos complejos para entrenar modelos neuronales profundos."

## Slide 6

**¿Componentes de Machine Learning?**

"Estos tres componentes forman parte importante en la enseñanza de los softwares de ML."

Tres columnas, cada una con una cabecera en caja redondeada de color (magenta / morado / azul) conectada por una línea a una caja de contenido debajo:

| Conjunto de datos | Características | Algoritmos |
|---|---|---|
| • Son necesarios para entrenar programas de aprendizaje automático para dibujar patrones y correlaciones.<br>• Estos conjuntos de datos incluyen imágenes, números, textos y otras formas de datos. | • También conocidas como variables, resaltan los datos clave en los que el programa debe centrarse.<br>• Seleccionar las características correctas es crucial para entrenar el software, para tomar las decisiones correctas. | • Son métodos de análisis de datos.<br>• El uso de diferentes algoritmos para la misma tarea puede proporcionar soluciones idénticas, la velocidad y la precisión para obtener los resultados pueden diferir. |

★ "La precisión de los resultados dependerá proporcionalmente de la calidad de los datos y sus resultados deseados."

## Slide 7

**Limitaciones de Machine Learning Básico**

- La principal limitación del aprendizaje automático es la necesidad de la intervención humana.
- Aunque estos programas son efectivos para identificar correlaciones, son mucho menos efectivos para identificar la causalidad. Por lo tanto, la participación humana es necesaria para dirigir estos programas hacia la solución "correcta".

Ilustración inferior: tres bloques encadenados por flechas azules — (1) icono de diskette/servidor/documento etiquetado **"Past data"** → (2) monitor con chip e ícono de cerebro-engranaje **"Learns from past data"** → (3) monitor con robot **"Predicts the output"**.

## Slide 8

**¿Qué es Deep Learning?**

"Deep Learning es una subárea del machine learning que utiliza modelos profundos, es decir, redes neuronales profundas. Está compuesto por:"

Diagrama central (recuadro rojo) de una neurona artificial: entradas $x_1, x_2, x_3$ (círculos magenta) con pesos $w_1, w_2, w_3$ ("Pesos sinápticos") más un nodo Bias = 1 con peso $w_0$, todos apuntando a un nodo **Σ** ("Suma ponderada"), que alimenta un círculo naranja **f(x)** ("Función de activación") y finalmente a un nodo amarillo **y** ("Salida"). Debajo de f(x) hay una miniatura con las curvas de Sigmoid ($\sigma(x)=\frac{1}{1+e^{-x}}$), tanh, ReLU ($\max(0,x)$), Leaky ReLU ($\max(0.1x, x)$), Maxout y ELU.

Cajas de texto alrededor:
- **Entradas de datos:** Estos son los datos que desea procesar.
- **Pesos:** Estos determinan la importancia de cada entrada en el resultado.
- **Funciones de activación:** Son una combinación de la suma ponderada de las entradas y el sesgo aplicado. Determinan si los datos se transmitirán a la siguiente capa de la red.
- **Iteraciones o sesgo:** Estos representan la cantidad de suposiciones que se hacen sobre la salida. Un sesgo más alto significa que se hacen más suposiciones, mientras que un sesgo más bajo significa que se hacen menos suposiciones.
- **Salidas:** Estas son decisiones tomadas por el programa de aprendizaje profundo.

## Slide 9

**Limitaciones del Deep Learning**

"Algunas limitaciones de los sistemas de aprendizaje profundo son:"

- Dado que entrenar una red de aprendizaje profundo requiere una cantidad increíblemente grande de información, se necesita mucho tiempo y poder de cómputo.
- Sin embargo, a medida que la computación en la nube y las unidades de procesamiento de gráficos (GPU) continúan desarrollándose y evolucionando, el tiempo necesario para entrenar la red podría eventualmente reducirse de semanas a horas.

Ilustración: pipeline de 4 pasos con flechas — mosaico 3×3 de fotos de ojos **"Images of eye retinas"** → monitor con capas de red neuronal **"Fed to a Neural Network for training"** → monitor con foto de un ojo enrojecido **"New image of eye retina"** → dos fondos de ojo (retinografías) **"Identifies Healthy and Diseased eye"**.

## Slide 10

**¿Cuál es la diferencia entre ML y DL?**

"ML y DL están conectadas entres sí, hay algunas diferencias significativas entre ellos:" — dos columnas separadas por línea punteada magenta.

| Machine Learning (ML) | Deep Learning (DL) |
|---|---|
| • ML es un subconjunto de AI | • DL es un subconjunto de ML |
| • El aprendizaje automático exige la extracción manual de funciones. | • Extrae las características y clasifica las suyas. |
| • Utiliza una pequeña cantidad de datos (comparado a DL). | • Requiere grandes conjuntos de datos. |
| • Puede trabajar en la configuración de hardware mínima. | • Requiere máquinas de alta gama para su ejecución. |
| • El aprendizaje automático se lleva a cabo en pasos más pequeños. | • El aprendizaje profundo se lleva a cabo de principio a fin. |
| • Su tiempo de ejecución es proporcional a los datos de entrada. | • Se necesita más tiempo para ejecutar que ML. |
| • Produce sólo valores numéricos. | • Produce una variedad de salidas desde valores numéricos hasta textos, sonidos e imágenes. |
| • Se refiere al término general en el que la computadora aprende de los datos. | • Se refiere a la compleja evolución matemática del aprendizaje automático. |

## Slide 11

**¿Cuál es la diferencia entre ML y DL?**

Infografía comparativa con dos franjas:

- Franja superior (borde punteado turquesa) **MACHINE LEARNING**: foto de un auto rojo (**INPUT**) → laptop con gráficos y cerebro (**FEATURE EXTRACTION**) → red de nodos verdes (**CLASSIFICATION**) → caja verde **CAR / NOT CAR** (**OUTPUT**).
- Franja inferior (borde punteado rojo) **DEEP LEARNING**: mismo auto rojo (**INPUT**) → red neuronal densa con nodos azules y "HIDDEN NEURONS" amarillos (**FEATURE EXTRACTION + CLASSIFICATION**) → caja azul **CAR (Color: Red, Make: Ford, Model: Mustang) / NOT CAR**.

Pie en rojo: **¿Por qué usar Deep Learning?**

## Slide 12

Separador de sección: **02. Redes Neuronales Profundas**.

## Slide 13

**Tipos de redes neuronales profundas**

Cuatro cajas redondeadas de colores (2×2):

- **Red neuronal convolucional (CNN):** Las CNN es una clase de redes neuronales profundas que se usa más comúnmente para el análisis de imágenes.
- **Red neuronal recurrente (RNN):** Las RNN utilizan información secuencial para construir un modelo. A menudo funciona mejor para modelos que tienen que memorizar datos anteriores.
- **Red adversa generativa (GAN):** Las GAN son arquitecturas algorítmicas que utilizan dos redes neuronales para crear nuevas instancias sintéticas de datos que pasan por datos reales. Una GAN entrenada con fotografías puede generar nuevas fotografías que parezcan al menos superficialmente auténticas para los observadores humanos.
- **Deep Belief Network (DBN):** Las DBN es un modelo gráfico generativo que se compone de múltiples capas de variables latentes llamadas unidades ocultas. Cada capa está interconectada, pero las unidades no lo están.

## Slide 14

**Redes profundas con perceptrón multicapa**

Un modelo de perceptrón multicapa tiene una estructura similar a la de un modelo de perceptrón de una sola capa con más número de capas ocultas. Se entrenan mediante el algoritmo de retropropagación.

- Se entrena en dos etapas: la etapa hacia adelante y la etapa hacia atrás.
- ➢ En la etapa hacia adelante, las funciones de activación se originan desde la capa de entrada a la capa de salida.
- ➢ En la etapa hacia atrás, el error entre el valor real observado y el valor demandado se origina hacia atrás en la capa de salida para modificar los pesos.

Diagrama a la derecha (recuadro morado): MLP totalmente conectado — **Capa de Entrada** con 3 nodos amarillos (con flechas de entrada), **Capas Ocultas** con 3 columnas de 4 nodos verdes cada una, todas interconectadas, y **Capa de Salida** con 1 nodo rojo y flecha de salida.

## Slide 15

**Redes profundas con perceptrón multicapa**

- El perceptrón multicapa puede tratarse como una red de numerosas neuronas artificiales sobre capas variadas, la función de activación ya no es lineal, en su lugar se despliegan funciones de activación no lineales como las funciones sigmoides, TanH, funciones de activación basados en ReLU, entre otras, para su ejecución.
- El modelo del perceptrón surge como un clasificador binario linealmente separable, es decir este modelo funcionará siempre y cuando las clases se puedan separar linealmente y usando modificaciones se puede realizar una clasificación multiclase.

Figura derecha (recuadro morado): 4 paneles numerados (1–4) con ejes **size** (vertical) vs **domestication** (horizontal), siluetas de perros (rojo) arriba y gatos (azul) abajo, y una recta separadora que se va ajustando en cada panel; en el panel 4 la recta deja un punto mal clasificado (perro pequeño marcado en rojo). Ilustra la separación lineal iterativa del perceptrón.

## Slide 16

**Redes profundas con perceptrón multicapa**

Slide solo-figura (recuadro rojo): jerarquía de características de una red profunda sobre la foto de un gato.

**INPUT: Descomposición de la imagen en píxeles** → red de 5 columnas de nodos totalmente conectadas → **OUTPUT: "Missi"**.

Etiquetas de capa con ejemplos visuales debajo de cada una:
- CAPA 1 — Píxeles detectados (mosaico pixelado)
- CAPA 2 — Bordes identificados (parches de textura)
- CAPA 3 — Combinación de bordes identificados (parches de oreja/hocico)
- CAPA 4 — Características identificadas (ojos, orejas, nariz)
- CAPA 5 — Combinación de características identificadas (caras completas de gatos)

## Slide 17

Separador de sección: **03. Redes Neuronales Convolucionales**.

## Slide 18

**¿Qué es convolución?**

Una convolución es una operación matricial que, en el contexto de las imágenes, permite realizar un filtrado sobre las mismas. En otras palabras, por medio de una convolución puedes realizar filtros muy útiles como eliminar toda la información que no sea un borde o difuminar la imagen.

Figura (recuadro morado): arquitectura CNN clásica sobre una huella dactilar — **Input** → **Convolution** (pila de mapas verdes) → **Pooling** (mapas azules) → **Convolution** (pila verde más numerosa) → **Pooling** (azules) → **Fully-connected** (barras amarillas) → **Output**.
Debajo, 4 miniaturas de un fotógrafo con trípode etiquetadas IMAGE, f1-IMAGE, f2-IMAGE, f3-IMAGE mostrando el resultado de distintos filtros (original y detecciones de bordes en negro/blanco).

## Slide 19

**Redes Neuronales Convolucionales**

- Surgen en 1998.
- Las Redes Neuronales Convolucionales (CNN), son el algoritmo utilizado en Aprendizaje Automático para dar la capacidad de "ver" al ordenador.
- La CNN es un tipo de Red Neuronal Artificial con aprendizaje que procesa sus capas imitando al córtex visual del ojo humano para identificar distintas características en las entradas que en definitiva hacen que pueda identificar objetos.
- La CNN contiene varias capas ocultas especializadas y con una jerarquía: esto quiere decir que las primeras capas pueden detectar líneas, curvas y se van especializando hasta llegar a capas más profundas que reconocen formas complejas como un rostro o la silueta de un animal.

**Aplicaciones:**
- Clasificar imágenes
- Detectar diversos tipos de tumores
- automáticamente
- Enseñar a conducir a los coches autónomos
- Entre otras aplicaciones.

Figura derecha (recuadro azul): esquema LeNet en gris sobre la foto de un perro — Input → **Convolutions** → **Subsampling** → **Convolutions** (F.maps) → **Subsampling** → **Fully connected**.

## Slide 20

**Proceso de una red convolucional**

Dos bloques:

- Bloque superior (borde verde punteado): imagen en blanco/gris de la letra "A" formada por bloques grises. Texto: "Una imagen…"
- Bloque inferior (borde rojo punteado): la misma letra representada en una cuadrícula 7×7 donde las celdas activas valen **0.6**. Texto: "…es una matriz de pixeles. El valor de los pixeles va de 0 a 255 pero se normaliza para la red neuronal de 0 a 1".

Disposición aproximada de los valores 0.6 (filas 2–5):

```
.    .    .    .    .    .
.    .   0.6  0.6   .    .
0.6   .    .    .   0.6   .
0.6  0.6  0.6  0.6   .    .
0.6   .    .   0.6   .    .
```

## Slide 21

**Redes Neuronales Convolucionales**

Slide solo-figura (marco verde): la misma letra "A" pero en naranja, con una llave verde que la descompone en **tres matrices 7×7 de canales**:

- Canal rojo: celdas con valor **0.2** (resaltadas en rojo)
- Canal verde: celdas con valor **0.4** (resaltadas en verde)
- Canal azul: celdas con valor **0.2** (resaltadas en azul)

Texto: "Si la imagen es a color, estará compuesta de tres canales: rojo, verde, azul."

## Slide 22

**Redes Neuronales Convolucionales**

"Veamos el proceso de convolución de una CNN"

- Haremos las llamadas "convoluciones": Estas consisten en tomar "grupos de píxeles cercanos" de la imagen de entrada e ir operando matemáticamente (producto escalar) contra una pequeña matriz que se llama kernel.
- Ese kernel supongamos de tamaño 3×3 pixels "recorre" todas las neuronas de entrada (de izquierda-derecha, de arriba-abajo) y genera una nueva matriz de salida, que en definitiva será nuestra nueva capa de neuronas ocultas.

Figura derecha (recuadro turquesa): la matriz "Imagen de entrada" con valores 0.6 y una flecha hacia el **kernel** 3×3 (filtro tipo Sobel vertical):

|  |  |  |
|---|---|---|
| 1 | 0 | -1 |
| 2 | 0 | -2 |
| 1 | 0 | -1 |

## Slide 23

**¿Cuántos Kernel son?**

El kernel se identifica como la matriz de menor tamaño que la capa convolucional anterior que nos permitirá crear las nuevas capas matriciales, esto se logra mediante el recorrido del kernel por toda la capa anterior.

A medida que vamos desplazando el kernel, vamos obteniendo una nueva imagen filtrada. El filtro nos definirá que rasgo nuevo es el que estamos obteniendo, como pueden ser esquinas, bordes, contornos, cambios de color, etc.

Figura (marco rojo): a la izquierda la matriz de la imagen (valores 0.6) con un recuadro rojo 3×3 sobre la esquina superior izquierda marcando la ventana del kernel; a la derecha la matriz de salida con la primera celda resaltada en rojo con el valor **-1,2**, resultado de esa primera aplicación.

## Slide 24

**Movimiento del Kernel**

Figura de convolución multicanal con bias:

- Tres matrices de entrada con borde de padding de ceros: **Input Channel #1 (Red)** (valores 156, 155, 156, 158, 158, 153, 154, 157, 159, 159, 149, 151, 155, 158, 159, 146, 146, 149, 153, 158, 145, 143, 143, 148, 158…), **Input Channel #2 (Green)** (167, 166, 167, 169, 169, 164, 165, 168, 170, 170, 160, 162, 166, 169, 170, 156, 156, 159, 163, 168, 155, 153, 153, 158, 168…), **Input Channel #3 (Blue)** (163, 162, 163, 165, 165, 160, 161, 164, 166, 166, 156, 158, 162, 165, 166, 155, 155, 158, 162, 167, 154, 152, 152, 157, 167…). La ventana 3×3 activa está sombreada en la esquina superior izquierda de cada canal.

Kernels 3×3 por canal:

```
Kernel Channel #1     Kernel Channel #2     Kernel Channel #3
 -1  -1   1             1   0   0             0   1   1
  0   1  -1             1  -1  -1             0   1   0
  0   1   1             1   0  -1             1  -1   1
```

Resultados parciales: **308 + (−498) + 164 + 1 (Bias) = −25**, y el −25 se escribe en la primera celda (resaltada en amarillo) de la matriz **Output**.

Texto: "El kernel, permite extraer características relevantes de una imagen: líneas verticales u horizontales, bordes, esquinas o formas más complejas."

## Slide 25

**¿Qué es RELU?**

**RELU**
- Es una función de activación, por sus siglas en inglés Rectifier Linear Unit.
- Sirve para obtener valores "importantes" de las extracciones de características.

Fórmula destacada: $f(x) = \max(0, x)$

Figura derecha (marco magenta): definición de ReLU $\max(0,x)$ con la derivada
$$f'(x) = \begin{cases} 1 & \text{si } x > 0 \\ 0 & \text{otro caso} \end{cases}$$
y la gráfica "Función de activación": recta plana en 0 para $x<0$ y recta de pendiente 1 para $x>0$, ejes de −4 a 5.

## Slide 26

**Mapa de características**

Slide solo-figura (marco turquesa): pipeline de 4 etapas con flechas.

1. **IMAGEN**: cuadrícula 7×7 con celdas 0,6 (la letra "A").
2. **KERNEL**: matriz 3×3 `[1 0 -1; 2 0 -2; 1 0 -1]`.
3. **CONVOLUCION DEL KERNEL**: matriz 4×4 resultante:

```
-1,2  -0,6   0,6   1,2
-1,2   0,6  -0,6   1,2
-1,2   1,2  -1,2   1,2
-0,6   1,2  -1,2   0,6
```

4. **APLICO RELU**: matriz 4×4 con los negativos puestos a 0 (valores positivos resaltados en amarillo):

```
0    0    0,6  1,2
0   0,6    0   1,2
0   1,2    0   1,2
0   1,2    0   0,6
```

Una flecha apunta a esta última matriz con la etiqueta **"Mapa de características"**.

## Slide 27

**Barrido de una imagen**

Slide solo-figura (marco rojo oscuro):

- **Image Matrix** con borde de ceros y valores (105, 102, 100, 97, 96 / 103, 99, 103, 101, 102 / 101, 98, 104, 102, 100 / 99, 101, 106, 104, 99 / 104, 104, 104, 100, 98). La ventana 3×3 superior izquierda está resaltada en morado.
- **Kernel Matrix** 3×3 (filtro de realce/sharpen):

```
 0  -1   0
-1   5  -1
 0  -1   0
```

- **Output Matrix** con la primera celda en verde = **320**.

Cálculo mostrado:
$$0\cdot0 + 0\cdot(-1) + 0\cdot0 + 0\cdot(-1) + 105\cdot5 + 102\cdot(-1) + 0\cdot0 + 103\cdot(-1) + 99\cdot0 = 320$$

Pie: "Convolution with horizontal and vertical strides = 1".

## Slide 28

**Stride y Padding**

- **Stride**, se refiere al número de casillas que se moverá el kernel, en toda la red convolucional. (caja turquesa)
- **Padding** es el relleno de Ceros rodeando a la capa. (caja rosada)

Figura inferior (marco dorado): matriz de entrada azul rodeada por un borde punteado de ceros (padding). Sobre la esquina superior izquierda se superpone la ventana 3×3 con los pesos del kernel en subíndice (0₂ 0₀ 0₁ / 0₁ 2₀ 2₀ / 0₀ 0₁ 1₁). Valores de la entrada: filas `2 2 3 3 3`, `0 1 3 0 3`, `2 3 0 1 3`, `3 3 2 1 2`, `3 3 0 2 3`. A la derecha, la matriz de salida 3×3 en verde azulado:

```
1   6   5
7  10   9
7  10   8
```

## Slide 29

**Stacking**

Slide solo-figura: llave izquierda que une la **Imagen real** (cuadrícula roja 6×6) con un conjunto de 10 **Filtros** (bloques amarillos apilados 3×3), y una llave derecha que lleva al bloque verde **Stacking** con las **Imágenes resultantes** (mapas de características blancos apilados en diagonal, uno por filtro).

## Slide 30

**Componentes de Redes Neuronales Convolucionales**

Figura (marco azul): "Red neuronal convolucional predictiva"

Entrada **32x32** (mosaico 3×3 de dígitos MNIST: 4,1,0,7,8,1,2,7,1) → bloque azul **32** filtros con salida **16 x 16 x 32** → bloque rojo **64** filtros con salida **8 x 8 x 64** → capa verde **10** → círculo amarillo (salida).

Parámetros a la derecha:
- Kernel = (3,3)
- Stride = 2
- Padding = Same

Cálculo de parámetros debajo:

| Capa | Fórmula | Params |
|---|---|---|
| Conv 1 | (3 x 3 + 1) x 32 | 320 |
| Conv 2 | (3x3x32+1) x 64 | 18,496 |
| Densa/salida | (8 x 8 x 64) + 10 | 4,106 |
| **Total** | | **22,922** |

## Slide 31

**Pooling**

- Si solo hiciéramos una nueva convolución a partir de la capa anterior, el número de neuronas de la próxima capa aumentaría por cada nuevo procesamiento (y ello implica mayor procesamiento).
- Para reducir el tamaño de la próxima capa de neuronas haremos un proceso llamado subsampling.
- Ejemplo: Max-pooling, para reducir el tamaño de nuestras imágenes filtradas pero sin perder las características más importantes que detectó cada filtro.
- Subsampling: Max-pooling

Figura derecha (marco naranja): matriz 4×4 (el mapa de características de la slide 26)

```
0    0   0,6  1,2
0   0,6   0   1,2
0   1,2   0   1,2
0   1,2   0   0,6
```

reducida por Max-Pooling 2×2 a la matriz 2×2:

```
0,6  1,2
1,2  1,2
```

Texto: "SUBSAMPLING: Aplico Max-Pooling de 2x2 y reduzco mi salida a la mitad".

## Slide 32

**Max-Pooling**

- La imagen está dividida en regiones del mismo tamaño.
- Consiste en extraer ventanas de los mapas de características de entrada y generar el valor máximo de cada canal que corresponde a un píxel en la imagen (resultante).
- Reducir la cantidad de datos entre una capa y otra, facilita el procesamiento de la imagen y el entrenamiento de la red.

Figura derecha (fondo azul oscuro, marco morado): **IMAGEN ORIGINAL** 6×6

```
12   5   3   9   1  23
 8   6  55   6  13  62
41   8   3  51  22  27
32  67  53  12  26  17
 9  22  15   8  57  62
23  53  25  75  12   9
```

La ventana 2×2 superior izquierda (12, 5, 8, 6) está resaltada en magenta y produce el **12** de la **IMAGEN RESULTANTE** (cuadrícula 3×3, primera celda en magenta).

## Slide 33

**¿Qué obtenemos de una red convolucional?**

La idea de la conectividad local es:
- Un filtro convolucional es una matriz de tamaño relativamente pequeño que se aplica a modo de ventana deslizante sobre toda la imagen. De este modo, un solo kernel representará a un filtro.
- Reducirá el tamaño de la arquitectura a nivel de conexiones entre neuronas, también conseguirá un modelo de aprendizaje que sea capaz de aprender a filtrar las características más relevantes de una imagen de modo totalmente automático.
- Mediante el entrenamiento, se actualizarán los coeficientes del kernel convolucional para filtrar las imágenes del modo que el modelo considere oportuno.

Figura inferior (marco rojo): arquitectura CNN sobre la imagen de un robot — **Input** → **Convolutions** (Feature maps azules grandes) → **Subsampling** (f.maps menores) → **Convolutions** (f.maps) → **Subsampling** (pila fina) → **Fully connected** → **Output**.

## Slide 34

Separador de sección: **04. Clasificación con CNN**.

## Slide 35

**¿Qué es un modelo clasificador?**

Es aquel que puede clasificar cierto patrón dentro de una red neuronal convolucional, es decir, determinar a qué dígito corresponde cada imagen, independientemente de cómo este haya sido escrito. (MINIST)

Figura (marco morado): arriba la ecuación conceptual **Entrada + Operaciones convolucionales = Salida**, con llaves que bajan al diagrama detallado:

**Input Image (28x28 pixels)** con el dígito "7" → **Convolutional Layer 1** (Filter-Weights 5x5 pixels, salida 14x14 pixels, 16 channels) → **Convolutional Layer 2** (Filter-Weights 5x5 pixels, "16 of these…", salida 7x7 pixels, 36 channels) → **Fully-Connected Layer** (128 features) → **Output Layer** (10 features, vector de probabilidades: 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1, 0.8, 0.0, 0.0) → **Class** 0–9, con el **7** circulado como predicción (probabilidad 0.8).

## Slide 36

**Conjunto de datos: MNIST**

Ejemplo:
- El set, o este conjunto de datos se llama MNIST, y contiene 70,000 imágenes (se sugiere 60,000 de entrenamiento y 10,000 de validación), cada una de ellas en escala de gris y con un tamaño de 28x28.
- Las imágenes contienen los dígitos del 0 al 9, escritos por diferentes personas:

Figura (marco rojo): mosaico de dígitos manuscritos, 10 filas (una por dígito 0–9) × ~16 columnas de variantes de escritura. Llave a la derecha etiquetada **Set MNIST**.

## Slide 37

**Laboratorio**

- Reto: Completa el reto Reto_01_MNIST para copiar la red neuronal convolucional anterior y entrenarla usando la base de datos MNIST
- Tips: Observa la documentación necesaria de las librerías enfocadas a DL en python

Captura derecha: salida de `model.summary()` de Keras.

```
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 conv2d_4 (Conv2D)           (None, 24, 24, 6)         156
 max_pooling2d_4 (MaxPooling (None, 12, 12, 6)         0
 2D)
 conv2d_5 (Conv2D)           (None, 8, 8, 16)          2416
 max_pooling2d_5 (MaxPooling (None, 4, 4, 16)          0
 2D)
 flatten_2 (Flatten)         (None, 256)               0
 dense_1 (Dense)             (None, 256)               65792
 dense_2 (Dense)             (None, 120)               30840
 dense_3 (Dense)             (None, 84)                10164
 dense_4 (Dense)             (None, 10)                850
=================================================================
Total params: 110,218
Trainable params: 110,218
Non-trainable params: 0
```

## Slide 38

**Metodología para la clasificación de imágenes**

- La metodología para la clasificación de imágenes consiste de los siguientes pasos:

1. Las imágenes se pre-procesan para que tengan un formato similar, en caso que sean diferentes en tamaño.
2. Estas imágenes son analizadas mediante una red convolucional, la cual extrae las características y forma un mapa de rasgos que representa la imagen.
3. Dicho mapa de rasgos se pasa por un conjunto de capas Dense, las cuales analizan todo este mapa.
4. Tras pasar por las capas densas, los pesos resultantes llegarán a una capa Softmax, la cual actuará como salida.
5. Para asignar la etiqueta correspondiente a la muestra tras haberlo procesado con el modelo, elegimos la etiqueta con mayor probabilidad, ya que la salida de la softmax tiene esta propiedad.

Slide solo texto.

## Slide 39

**Ejemplo de un modelo clasificador**

Figura (marco morado) dividida en dos tramos: arriba **CAPAS CONVOLUCIONALES: EXTRACCIÓN DE CARACTERÍSTICAS**, abajo **RED NEURONAL: CLASIFICACIÓN**.

Flujo con bloques 3D azules:

**ENTRADA: 28X28X1** (dígito "5") →
- **CONV 1:** 6 filtros, 5x5x1; padding = 0; strides = 1; Activación: ReLU → **24x24x6**
- **MAX-POOLING 1:** 6 filtros, 2x2; padding = 0; strides = 2; Activación: Ninguna → **12x12x6**
- **CONV 2:** 16 filtros, 5x5x6; padding = 0; strides = 1; Activación: ReLU → **8x8x16**
- **MAX-POOLING 2:** 16 filtros, 2x2; padding = 0; strides = 2; Activación: Ninguna → **4x4x16**
- **FLATTEN** → **256x1**
- **FULLY-CONNECTED 1:** 120 neuronas → **120x1**
- **FULLY-CONNECTED 2:** 84 neuronas → **84x1**
- **SOFTMAX:** 10 categorías (0-9) → **SALIDA: y_pred**

## Slide 40

**Modelos ganadores para la clasificación**

**AlexNet:**
- La Red Neuronal Convoluciona Profunda de Toronto ganó la competencia ImageNet 2012, con una precisión de prueba del 84.6%
- Consta de 5 capas convolucionales, una activación ReLU como no lineales, 3 capas Dense y una de Softmax.

Figura (marco rojo): diagrama original de AlexNet con dos ramas paralelas (224×224×3 de entrada, "Stride of 4", bloques 48/128/192/192/128, Max pooling, capas dense 2048/2048/1000). Flechas rojas señalan las **5 Convolutional Layers** (arriba) y las **3 Fully Connected Layers** (abajo), terminando en **1000-way softmax**.

## Slide 41

**Modelos ganadores para la clasificación**

**VGG16:**
- Este modelo de Oxford ganó la competencia ImageNet 2013 con un 92.7 % de precisión.
- Utiliza una pila de capas de convolución con pequeños campos receptivos en las primeras capas en lugar de pocas capas con grandes campos receptivos.

Figura (marco rojo): diagrama de bloques 3D de VGG16 con dimensiones decrecientes: 224×224×3 → 224×224×64 → 112×112×128 → 56×56×256 → 28×28×512 → 14×14×512 → 7×7×512 → 1×1×4096 → 1×1×1000. Leyenda: negro = convolution+ReLU, rojo = max pooling, celeste = fully connected+ReLU, amarillo = softmax.

## Slide 42

**Modelos ganadores para la clasificación**

**GoogleNet:**
- Esta red de Google ganó la competencia ImageNet 2014 con una precisión del 93.3 %.
- Está compuesto por 22 capas y un bloque de construcción recientemente introducido llamado módulo de inicio o auxiliar.

El módulo consta de una capa de red en red, una operación de agrupación, una capa de convolución de gran tamaño y una capa de convolución de tamaño pequeño.

Figura derecha (marco rojo) titulada **MÓDULO AUXILIAR**: bloque "cuerpo principal de la red" con flecha punteada hacia **avg pool 5×5** → **conv 1×1** → capa de 5 nodos **RELU** → otra capa **RELU** → capa **softmax**. Flechas laterales indican **propagación** (azul, hacia abajo por la derecha) y **retropropagación** (magenta, de vuelta al cuerpo principal).

## Slide 43

**Modelos ganadores para la clasificación**

**ResNet:**
- Este modelo de Microsoft ganó la competencia ImageNet 2016 con un 96.4 % de precisión.
- Es conocido por su profundidad (152 capas) y la introducción de bloques residuales.

Los bloques residuales abordan el problema de entrenar una arquitectura realmente profunda mediante la introducción de conexiones de salto para que las capas puedan copiar sus entradas a la siguiente capa.

Figura derecha (marco rojo): diagrama del bloque residual. Entrada **x** se bifurca: una rama pasa por "función de excitación" → **RELU** → "función de excitación" produciendo **F(x)**; la otra rama es la conexión de salto que lleva **x** directo al nodo suma **⊕**; el resultado pasa por **RELU** dando la salida **ReLU(F(x)+x)**.

## Slide 44

**Análisis de los modelos para clasificación de Imágenes**

Dos gráficos (fuente: *An Analysis of Deep Neural Network Models for Practical Applications, 2017*):

1. Gráfico de barras — **Top-1 accuracy [%]** (eje 50–80) por modelo, ordenados de menor a mayor: AlexNet (~55), BN-AlexNet (~57), BN-NIN (~63), ENet (~68), GoogLeNet (~69), ResNet-18 (~70), VGG-16 (~71), VGG-19 (~71), ResNet-34 (~73), ResNet-50 (~76), ResNet-101 (~77.5), ResNet-152 (~78), Inception-v3 (~78.5), Inception-v4 (~80).
2. Gráfico de burbujas — **Top-1 accuracy [%]** vs **Operations [G-Ops]** (eje 0–40); el tamaño de la burbuja representa el número de parámetros (leyenda 5M, 35M, 65M, 95M, 125M, 155M). Se ven AlexNet/BN-AlexNet abajo-izquierda con burbujas enormes (~60M+) y baja accuracy; ENet, BN-NIN, GoogLeNet y ResNet-18 pequeños y a la izquierda; VGG-16 y VGG-19 con burbujas gigantes y alto costo (30–40 G-Ops) pero accuracy ~70; ResNet-50/101/152 e Inception-v3/v4 arriba con mejor relación accuracy/costo.

## Slide 45

**Conclusiones**

**01.** El Deep Learning permite resolver problemas complejos mediante el aprendizaje automático de características, superando muchas de las limitaciones del Machine Learning tradicional en tareas como visión por computadora.

**02.** Las Redes Neuronales Convolucionales (CNN) son el estándar para el procesamiento de imágenes, gracias a componentes como convoluciones, funciones de activación (ReLU) y pooling, que permiten extraer características de forma eficiente.

**03.** La evolución de arquitecturas como AlexNet, VGG, GoogleNet y ResNet ha incrementado significativamente la precisión en la clasificación de imágenes, impulsando aplicaciones en medicina, vehículos autónomos, reconocimiento facial y múltiples industrias.

## Slide 46

Slide de cierre (decorativa): logo UTEC centrado sobre fondo cian. Sin contenido.
