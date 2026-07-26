---
curso: ACD
titulo: [2025] U1_T3 Pandas para Ciencia de Datos
slides: 11
fuente: [2025] U1_T3 Pandas para Ciencia de Datos.pdf
---

## Slide 1

Portada.

**Pandas para Ciencia de Datos**
DS3021 Análisis Computacional de Datos

Fondo decorativo (túnel/corredor tecnológico azul con silueta). Chrome institucional omitido.

## Slide 2

**Objetivo de sesión**

Recuadro de texto con borde azul:

> Describir técnicas para cargar, almacenar y manipular de manera efectiva en memoria grandes conjuntos de datos utilizando Python a través de Pandas.

Foto decorativa a la izquierda (dos personas trabajando, teñida de azul).

## Slide 3

**Contenido**

1. Introducción
2. Estructuras de Pandas
3. Laboratorio — Pandas Data Structures

Cada ítem lleva un ícono (portapapeles para el 1; engranaje/bombilla para 2 y 3). Fondo decorativo (persona con visor VR + globo terráqueo digital).

## Slide 4

Slide separadora de sección.

**1. Introducción**

Ícono de portapapeles. Imagen decorativa a la derecha (mano robótica sobre globo digital).

## Slide 5

**Previamente**

- Revisamos la librería NumPy
- Recordemos que el objeto **ndarray** proporciona características esenciales para el tipo de datos limpios y bien organizados que normalmente se ven en las tareas de computación numérica.
- Sin embargo NumPy cuenta con algunas limitaciones cuando necesitamos más flexibilidad (adjuntar etiquetas a los datos, trabajar con datos faltantes, etc.) y agrupaciones.
- Cada una de estas tareas es una pieza importante para analizar los datos menos estructurados disponibles en muchas formas en el mundo que nos rodea.

Foto decorativa a la derecha (profesor escribiendo en pizarra, teñida de azul).

## Slide 6

**Pandas**

Para realizar análisis de datos, primero los datos deben estar estructurados de una manera que podamos **manipular y realizar operaciones** (resaltado en celeste), una forma común en Python en la que esto se hace es a través del módulo Pandas.

**Pandas** es una biblioteca de código abierto que proporciona estructuras de datos y herramientas de análisis de datos fáciles de usar y de alto rendimiento para el lenguaje de programación Python.
- Pandas ha sido construido en base a NumPy.

Visual: a la derecha, el logotipo oficial de pandas (barras verticales en azul oscuro con acentos amarillo y magenta, junto a la palabra "pandas" en minúsculas).

## Slide 7

Slide separadora de sección.

**2. Estructuras de Pandas**

Ícono de portapapeles. Misma imagen decorativa (mano robótica sobre globo digital).

## Slide 8

**Estructuras de Datos en Pandas**

Pandas cuenta con tres estructuras de datos fundamentales:
- Series (1D)
- DataFrame (2D)
- Index

Foto decorativa a la izquierda (dos estudiantes en laboratorio).

## Slide 9

**Serie**

- Una serie es un **array etiquetado unidimensional** capaz de contener cualquier tipo de datos (enteros, cadenas, float, objetos de Python, etc).
- Una serie consta de dos elementos (arrays):
  - Datos unidimensionales (valores)
  - *Indexs* (índices)

> Es similar a una lista o array, pero la diferencia clave radica en su capacidad para mantener un índice, lo que proporciona una búsqueda rápida y capacidad potente de alinear los datos.

Visual (diagrama a la derecha): un recuadro con etiqueta "index" arriba a la izquierda. Dentro, una caja celeste resaltando la columna de índices (0, 1, 2, 3) y al lado la columna de valores (20, 25, 78, 10). Una flecha negra apunta desde la etiqueta "Datos (valores)" hacia la columna de valores.

| index | valores |
|-------|---------|
| 0 | 20 |
| 1 | 25 |
| 2 | 78 |
| 3 | 10 |

## Slide 10

**DataFrame**

- Un DataFrame es una **estructura de datos bidimensional** compuesta de filas y columnas, exactamente como una hoja de cálculo simple o una tabla SQL.
- Cada columna de un DataFrame es una Serie. Estas columnas deben tener la misma longitud, pero pueden tener diferentes tipos de datos: float, int, bool, etc.
- Un dataframe consta de tres elementos:
  - Datos bidimensionales (valores)
  - *Indexs* Columnas
  - *Indexs* Filas

Visual (diagrama a la derecha): recuadro con "index" en celeste a la izquierda, encerrando en una caja celeste la columna de índices de fila (0,1,2,3). Arriba, la etiqueta celeste "Nombre de columnas" señala los encabezados **Edad** y **Puntaje**. Abajo a la derecha, una flecha desde la etiqueta celeste "Valores de columnas" apunta al cuerpo de la tabla.

| index | Edad | Puntaje |
|-------|------|---------|
| 0 | 20 | 10 |
| 1 | 25 | 15 |
| 2 | 78 | 18 |
| 3 | 10 | 10 |

## Slide 11

Slide separadora de sección.

**3. Laboratorio — Pandas Data Structures**

Ícono de portapapeles. Misma imagen decorativa (mano robótica sobre globo digital).
