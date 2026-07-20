---
curso: BIGDATA
titulo: 16 - Semana 14/Sem14_ Deep Learning
slides: 46
fuente: 16 - Semana 14/Sem14_ Deep Learning.pdf
---

Deep Learning
Mg. Aldo Lezama Benavides


Semana 14
        Objetivo de la sesión

1. Comprender los fundamentos del Deep Learning, identificando sus
   diferencias con el Machine Learning tradicional y sus principales
   ventajas y limitaciones.
2. Explicar el funcionamiento de las Redes Neuronales Profundas y las
   Redes     Neuronales       Convolucionales   (CNN),   analizando   sus
   componentes, proceso de entrenamiento y arquitectura.
3. Aplicar los conceptos de CNN en problemas de clasificación de
   imágenes, conociendo el uso de conjuntos de datos como MNIST y las
   arquitecturas más representativas como AlexNet, VGG, GoogleNet y
   ResNet
                  Contenido de la sesión

    01.                02.                 03.                04.

Modelos de Deep    Redes Neuronales   Redes Neuronales   Clasificación con
  Learning            Profundas       Convolucionales           CNN
01.   Modelos de Deep Learning
IA - ML - DL
¿Componentes de Machine Learning?
Limitaciones de Machine Learning Básico
¿Qué es Deep Learning?
Limitaciones del Deep Learning
¿Cuál es la diferencia entre ML y DL?
¿Cuál es la diferencia entre ML y DL?
02.   Redes Neuronales Profundas
Tipos de redes neuronales profundas
                       Redes profundas con perceptrón multicapa

Un modelo de perceptrón multicapa tiene una estructura similar
a la de un modelo de perceptrón de una sola capa con más
número de capas ocultas. Se entrenan mediante el algoritmo
de retropropagación.
● Se entrena en dos etapas: la etapa hacia adelante y la etapa
hacia atrás.


➢ En la etapa hacia adelante, las funciones de activación se
originan desde la capa de entrada a la capa de salida.


➢ En la etapa hacia atrás, el error entre el valor real observado
y el valor demandado se origina hacia atrás en la capa de
salida para modificar los pesos.
                  Redes profundas con perceptrón multicapa


• El perceptrón multicapa puede tratarse como una red de
  numerosas neuronas artificiales sobre capas variadas, la
  función de activación ya no es lineal, en su lugar se
  despliegan funciones de activación no lineales como las
  funciones sigmoides, TanH, funciones de activación basados
  en ReLU, entre otras, para su ejecución.
• El modelo del perceptrón surge como un clasificador binario
  linealmente separable es decir este modelo funcionará
  siempre y cuando las clases se puedan separar linealmente
  y usando modificaciones se puede realizar una clasificación
  multiclase
Redes profundas con perceptrón multicapa
03.   Redes Neuronales
      Convolucionales
                                      ¿Qué es convolución?
Una convolución es una operación matricial que, en el contexto de las imágenes, permite realizar un filtrado
sobre las mismas. En otras palabras, por medio de una convolución puedes realizar filtros muy útiles como
eliminar toda la información que no sea un borde o difuminar la imagen.
                             Redes Neuronales Convolucionales

• Surgen en 1998.
• Las Redes Neuronales Convolucionales (CNN), son el algoritmo
  utilizado en Aprendizaje Automático para dar la capacidad de “ver”
  al ordenador.
• La CNN es un tipo de Red Neuronal Artificial con aprendizaje que
  procesa sus capas imitando al córtex visual del ojo humano para
  identificar distintas características en las entradas que en definitiva
  hacen que pueda identificar objetos.                                      Aplicaciones:

• La CNN contiene varias capas ocultas especializadas y con una             ❑ Clasificar imágenes

  jerarquía: esto quiere decir que las primeras capas pueden detectar       ❑ Detectar diversos tipos de tumores

  líneas, curvas y se van especializando hasta llegar a capas más           ❑ automáticamente

  profundas que reconocen formas complejas como un rostro o la              ❑ Enseñar a conducir a los coches autónomos

  silueta de un animal.                                                     ❑ Entre otras aplicaciones.
Proceso de una red convolucional

Redes Neuronales Convolucionales
                        Redes Neuronales Convolucionales

Veamos el proceso de convolución de una CNN


• Haremos las llamadas “convoluciones”: Estas consisten
  en tomar “grupos de píxeles cercanos” de la imagen de
  entrada e ir operando matemáticamente (producto
  escalar) contra una pequeña matriz que se llama kernel.


• Ese kernel supongamos de tamaño 3×3 pixels “recorre”
  todas las neuronas de entrada (de izquierda-derecha,
  de arriba-abajo) y genera una nueva matriz de salida,
  que en definitiva será nuestra nueva capa de neuronas
  ocultas.
                                 ¿Cuántos Kernel son?
El kernel se identifica como la matriz de menor tamaño que la capa convolucional anterior que nos permitirá crear las
nuevas capas matriciales, esto se logra mediante el recorrido del kernel por toda la capa anterior
A medida que vamos desplazando el kernel, vamos obteniendo una nueva imagen filtrada. El filtro nos definirá que
rasgo nuevo es el que estamos obteniendo, como pueden ser esquinas, bordes, contornos, cambios de color, etc.
Movimiento del Kernel
                                        ¿Qué es RELU?



RELU


• Es una función de activación, por sus siglas en inglés Rectifier
  Linear Unit.


• Sirve para obtener valores “importantes” de las extracciones
  de características
Mapa de características
Barrido de una imagen
Stride y Padding
Stacking
Componentes de Redes Neuronales Convolucionales




                                             Kernel = (3,3)
                                             Stride = 2
                                             Padding = Same
                                                     Pooling

• Si solo hiciéramos una nueva convolución a partir de la capa
  anterior, el número de neuronas de la próxima capa
  aumentaría por cada nuevo procesamiento (y ello implica
  mayor procesamiento).
• Para reducir el tamaño de la próxima capa de neuronas
  haremos un proceso llamado subsampling
• Ejemplo: Max-pooling, para reducir el tamaño de nuestras
  imágenes filtradas pero sin perder las características más
  importantes que detectó cada filtro.
• Subsampling: Max-pooling
                                                 Max-Pooling


• La imagen está dividida en regiones del mismo
  tamaño.


• Consiste en extraer ventanas de los mapas de
  características de entrada y generar el valor
  máximo de cada canal que corresponde a un píxel
  en la imagen (resultante).


• Reducir la cantidad de datos entre una capa y otra ,
  facilita el procesamiento de la imagen y el
  entrenamiento de la red.
                   ¿Qué obtenemos de una red convolucional?
La idea de la conectividad local es:
• Un filtro convolucional es una matriz de tamaño relativamente pequeño que se aplica a modo de ventana deslizante sobre
  toda la imagen. De este modo, un solo kernel representará a un filtro.
• Reducirá el tamaño de la arquitectura a nivel de conexiones entre neuronas, también conseguirá un modelo de aprendizaje
  que sea capaz de aprender a filtrar las características más relevantes de una imagen de modo totalmente automático.
• Mediante el entrenamiento, se actualizarán los coeficientes del kernel convolucional para filtrar las imágenes del modo que
  el modelo considere oportuno.
04.   Clasificación con CNN
                          ¿Qué es un modelo clasificador?
Es aquel que puede clasificar cierto patrón dentro de una red neuronal convolucional, es decir, determinar a qué
dígito corresponde cada imagen, independientemente de cómo este haya sido escrito. (MINIST)
                              Conjunto de datos: MNIST
Ejemplo:
• El set, o este conjunto de datos se llama MNIST, y contiene 70,000 imágenes (se sugiere 60,000 de entrenamiento y
  10,000 de validación), cada una de ellas en escala de gris y con un tamaño de 28x28.
• Las imágenes contienen los dígitos del 0 al 9, escritos por diferentes personas:
                                             Laboratorio


• Reto: Completa el reto Reto_01_MNIST para
  copiar la red neuronal convolucional anterior y
  entrenarla usando la base de datos MNIST
• Tips:
Observa   la   documentación   necesaria   de   las
librerías enfocadas a DL en python
               Metodología para la clasificación de imágenes

• La metodología para la clasificación de imágenes consiste de los siguientes pasos:


1. Las imágenes se pre-procesan para que tengan un formato similar, en caso que sean diferentes en tamaño.
2. Estas imágenes son analizadas mediante una red convolucional, la cual extrae las características y forma un mapa
   de rasgos que representa la imagen
3. Dicho mapa de rasgos se pasa por un conjunto de capas Dense, las cuales analizan todo este mapa.
4. Tras pasar por las capas densas, los pesos resultantes llegarán a una capa Softmax, la cual actuará como salida
5. Para asignar la etiqueta correspondiente a la muestra tras haberlo procesado con el modelo, elegimos la etiqueta
   con mayor probabilidad, ya que la salida de la softmax tiene esta propiedad.
Ejemplo de un modelo clasificador
                  Modelos ganadores para la clasificación
AlexNet:
• La Red Neuronal Convoluciona Profunda de Toronto ganó la competencia ImageNet 2012, con una precisión de
  prueba del 84.6%
• Consta de 5 capas convolucionales,una activación ReLU como no lineales, 3 capas Dense y una de Softmax.

                  Modelos ganadores para la clasificación
VGG16:
• Este modelo de Oxford ganó la competencia ImageNet 2013 con un 92.7 % de precisión.
• Utiliza una pila de capas de convolución con pequeños campos receptivos en las primeras capas en lugar de
  pocas capas con grandes campos receptivos.
                        Modelos ganadores para la clasificación

GoogleNet:
❖ Esta red de Google ganó la competencia ImageNet
2014 con una precisión del 93.3 %.


❖ Está compuesto por 22 capas y un bloque de
construcción recientemente introducido llamado módulo
de inicio o auxiliar.


El módulo consta de una capa de red en red, una
operación de agrupación, una capa de convolución de
gran tamaño y una capa de convolución de tamaño
pequeño.
                     Modelos ganadores para la clasificación

ResNet:


• Este modelo de Microsoft ganó la competencia
  ImageNet 2016 con un 96.4 % de precisión.
• Es conocido por su profundidad (152 capas) y la
  introducción de bloques residuales.


Los bloques residuales abordan el problema de entrenar
una   arquitectura   realmente   profunda   mediante   la
introducción de conexiones de salto para que las capas
puedan copiar sus entradas a la siguiente capa.
Análisis de los modelos para clasificación de Imágenes
                      Conclusiones
      El Deep Learning permite resolver problemas complejos mediante el aprendizaje
01.   automático de características, superando muchas de las limitaciones del Machine
      Learning tradicional en tareas como visión por computadora.

      Las Redes Neuronales Convolucionales (CNN) son el estándar para el

02.   procesamiento de imágenes, gracias a componentes como convoluciones,
      funciones de activación (ReLU) y pooling, que permiten extraer características de
      forma eficiente.

      La evolución de arquitecturas como AlexNet, VGG, GoogleNet y ResNet ha

03.   incrementado significativamente la precisión en la clasificación de imágenes,
      impulsando aplicaciones en medicina, vehículos autónomos, reconocimiento facial
      y múltiples industrias.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
