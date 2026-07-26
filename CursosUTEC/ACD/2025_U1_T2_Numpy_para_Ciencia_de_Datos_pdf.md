---
curso: ACD
titulo: [2025] U1_T2 Numpy para Ciencia de Datos
slides: 19
fuente: [2025] U1_T2 Numpy para Ciencia de Datos.pdf
---

## Slide 1

Portada.

**Numpy**
*para Ciencia de Datos*

DS3021 Análisis Computacional de Datos

Mg. José Espinoza Melgarejo

(Fondo decorativo: túnel de datos azul con silueta caminando; logos UTEC / TRANSFORMATEC.)

## Slide 2

**Objetivo de sesión aquí** (título vertical al margen izquierdo)

> Describir técnicas para cargar, almacenar y manipular de manera efectiva en memoria grandes conjuntos de datos utilizando Python a través de librería Numpy.

Foto decorativa (dos personas trabajando frente a una laptop, teñida de azul).

## Slide 3

**Contenido**

1. Introducción (ícono de portapapeles)
2. Numpy (ícono de bombilla/engranaje)
3. Laboratorio Numpy Basics (ícono de bombilla/engranaje)

Fondo decorativo: persona con visor VR y globo terráqueo digital.

## Slide 4

Separador de sección.

**1. Introducción** (con ícono de portapapeles; imagen decorativa de mano robótica tocando un globo digital).

## Slide 5

Texto al pie:

> Los datasets provienen de diferentes recursos y en distintos formatos. Para manejar la heterogeneidad, podríamos pensar en los datasets como un array.

**Visual:** ilustración sobre fondo turquesa. Una nube de íconos heterogéneos (smartphone, llave inglesa, burbuja de chat, reloj, sobre de correo, navegador con enlace, calendario, TV, libro, pin de mapa, diana con flecha, teléfono, lupa, carrito de compras, globo terráqueo, engranajes, gráfico de pastel, periódico, átomo) desciende por un **embudo** y sale hacia abajo convertida en la pantalla de un monitor que muestra un dashboard con gráfico de líneas y barras de colores. Metáfora: datos heterogéneos → embudo → estructura tabular/numérica.

## Slide 6

Cita a la derecha:

> "No importa cuáles sean los datos, **el primer paso** para analizarlos será transformarlos en array (matrices) de números."

**Visual:** tres filas de transformación, cada una con una flecha azul hueca de izquierda a derecha:

1. **Imagen** (ícono de foto: montaña verde, sol amarillo, cielo celeste) → cuadrícula en blanco y negro con un **corazón** dibujado en píxeles → flecha negra → matriz binaria de ceros y unos (bloque de texto tipo `0000000100000000 / 0001110011100 / 001000101000...`), es decir la imagen como matriz de bits.
2. **Audio** (forma de onda naranja, barras verticales de distinta altura) → tabla de una fila con encabezado **"Tiempo"** arriba y primera celda etiquetada **"Intensidad"**, seguida de 4 celdas vacías: la señal muestreada como vector de intensidades por instante de tiempo.
3. **Texto** (captura de un SMS: "Text Message / Today 15:46 — Its Emma. I tried to call you but signal bad. I been taken to hospital after having a fall this morning. If possible can you do me a quick favour and text me x") → secuencia de cajas azules con caracteres: `'a'` `'r'` `'r'` `'a'` `'y'`, es decir el texto como arreglo de caracteres.

## Slide 7

Slide de cita, fondo azul degradado con comillas grandes:

> Por esta razón, el **almacenamiento** y la **manipulación eficientes** de arrays numéricos son fundamentales para el ciclo de vida de la Ciencia de Datos.

## Slide 8

Separador de sección.

**2. Numpy** (mismo fondo de mano robótica; decorativo).

## Slide 9

**Numpy**

NumPy es la biblioteca fundamental del ecosistema Python Data Science para la computación científica. Algunas de las características clave de NumPy incluyen:

- **Velocidad:** las matrices NumPy son hasta 50 veces más rápidas que las listas estándar de Python
- **Rendimiento:** NumPy combina la facilidad de uso de Python con la velocidad de C
- **Indexación y difusión:** las funciones tan utilizadas en Pandas se heredan de NumPy.
- **Herramientas:** NumPy tiene una amplia gama de funciones matemáticas y herramientas computacionales para prácticamente todas las necesidades. Puede realizar operaciones como ajuste de curvas, optimización, álgebra lineal, transformaciones, etc., con facilidad.

NumPy es la base sobre la que se construyen muchas otras bibliotecas informáticas científicas. Algunas de las bibliotecas conocidas que utilizan NumPy como son: SciPy, Statsmodels, Scikit-Learn, SpaCy, Matplotlib, Seaborn, etc.

(Foto decorativa a la izquierda: estudiantes en laboratorio.)

## Slide 10

**NumPy**

- **NumPy** (abreviatura de Numerical Python) es una de las principales librerías para usar en computación científica en Python.
- Permite trabajar con arrays multidimensional de alto rendimiento y también proporciona herramientas para trabajar con estos arrays.
- Los arrays pueden tener más de 3 dimensiones, pero en este curso solo trabajaremos con 2 dimensiones.
- Los arrays bidimensionales se pueden ver como **matrices**. Esta es una forma conveniente de almacenar y manipular datos multivariados con Python.

Solo texto (sin figuras).

## Slide 11

**¿Qué es un array?**

Un array es una cuadrícula (grid) de datos numéricos del mismo tipo. Los arrays vienen en diferentes rangos, formas y tamaños.

**Tabla:**

| Concepto | Definición |
|---|---|
| **Rango (ndim)** | El número de dimensiones en un array |
| **Forma (shape)** | El número de elementos en cada dimensión de un array. Es representado como una tupla |
| **Tamaño (size)** | El número total de elementos de un array |

## Slide 12

**Ejemplos**

**A)** Diagrama: una fila horizontal de **8 celdas** contiguas, cada una con el valor `0` (vector 1D dibujado como tabla de 1×8).

```
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
```

Campos en blanco para completar:

- Rango:
- Forma:
- Tamaño:

## Slide 13

**Ejemplos** (misma figura de la slide anterior, ahora resuelta)

**A)** Fila de 8 celdas con valor `0`.

- Rango: 1
- Forma: (8,0)
- Tamaño: 8 (elementos)

*(Nota: "(8,0)" es lo que aparece literalmente en la slide.)*

## Slide 14

**Ejemplos**

**B)** Diagrama: cuadrícula de **3 filas × 5 columnas**, todas las celdas con valor `0` (matriz 2D).

```
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |
```

Campos en blanco para completar:

- Rango:
- Forma:
- Tamaño:

## Slide 15

**Ejemplos** (misma cuadrícula 3×5 de ceros, resuelta)

**B)**

- Rango: 2 - dimensiones
- Forma: (3,5)
- Tamaño: 15 elementos

## Slide 16

**Visual:** foto de un corcho con letras recortadas tipo collage que forman la palabra **"ADVICE"**, sujetas con chinches de colores.

Texto:

> **NumPy** puede soportar todo tipo de calculaciones matemáticas y estadísticas para una colección de números como: *mean, median, standard deviation (std) y variance (var)*.
>
> Otra cosa relacionada a números que no estás seguro que Numpy lo tiene, fácil Numpy sí lo tiene, **googlealo**.

## Slide 17

**¿Cómo llegamos del punto A al punto B?**

**Visual:** ilustración tipo "caminos". A la izquierda una letra **A** grande (naranja claro), a la derecha una **B** (rosada). Entre ambas, cuatro/cinco líneas curvas onduladas de distinto recorrido que unen A con B (rutas alternativas, unas más sinuosas que otras). Abajo a la izquierda, dos vehículos rojos: una **camioneta 4x4** y un **auto deportivo** con alerón. Metáfora: distintos vehículos/rutas para el mismo trayecto.

## Slide 18

**¿Cómo llegamos del punto A al punto B?**

**Visual:** comparación en dos filas, cada una con un vehículo, un símbolo "igual" azul y una etiqueta:

| Ícono | Equivale a | Descripción |
|---|---|---|
| Camioneta 4x4 roja | = | **Una lista de Python** — diseñada para manejar todo tipo de datos. |
| Auto deportivo rojo con alerón | = | **Un array NumPy** — diseñada para datos homogéneos y que implican muchos cálculos. |

## Slide 19

Separador de sección.

**3. Laboratorio — Numpy Basics** (ícono de portapapeles; fondo decorativo de mano robótica).
