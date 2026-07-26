---
curso: ACD
titulo: [2025] U1_T4 Plotting y Visualización
slides: 9
fuente: [2025] U1_T4 Plotting y Visualización.pdf
---

## Slide 1

Portada. Imagen de fondo decorativa (túnel tecnológico azul con silueta).

**Plotting y Visualización para Análisis de Datos**
DS3021 Análisis Computacional de Datos

## Slide 2

**Objetivo de sesión**

Describir técnicas computacionales para hacer plotting y visualizaciones en Python con la finalidad de realizar análisis de datos.

Solo texto (fondo decorativo).

## Slide 3

**Contenido**

1. Introducción (icono de portapapeles)
2. Matplotlib (icono de engranaje/bombilla)
3. Laboratorio Matplotlib (icono de engranaje/bombilla)

Imagen lateral decorativa (persona con visor VR sobre globo terráqueo digital).

## Slide 4

Slide separador de sección: **1. Introducción**. Fondo decorativo.

## Slide 5

**Introducción**

- Realizar visualizaciones (a veces llamadas gráficos) es una de las tareas más importantes en el análisis de datos.
- Puede ser parte del proceso exploratorio, por ejemplo, para ayudar a identificar valores atípicos o transformaciones de datos necesarias, o como una forma de generar ideas para modelos.
- Para otros, crear una visualización interactiva para la web puede ser el objetivo final.
- Python tiene muchas bibliotecas complementarias para realizar visualizaciones estáticas o dinámicas, pero nos centraremos principalmente en matplotlib y las bibliotecas que se basan en esta.

Solo texto.

## Slide 6

Slide separador de sección: **2. Matplotlib**. Fondo decorativo.

## Slide 7

**Matplotlib**

- Matplotlib es un paquete de trazado de escritorio diseñado para crear diagramas y figuras adecuadas para su publicación.
- El proyecto fue iniciado por John Hunter en 2002 para habilitar una interfaz de trazado similar a MATLAB en Python. Las comunidades matplotlib e IPython han colaborado para simplificar el trazado interactivo desde el shell de IPython.
- Matplotlib admite varios backends GUI en todos los sistemas operativos y puede exportar visualizaciones a todos los formatos de gráficos rasterizados y vectoriales comunes (PDF, SVG, JPG, PNG, BMP, GIF, etc.).

Solo texto.

## Slide 8

**Anatomía de una figura de Matplotlib** (texto a la izquierda, diagrama a la derecha).

- **Figure:** es el objeto con el nivel más alto en la jerarquía. Corresponde a toda la representación gráfica y generalmente puede contener muchos Axes.
- **Axes (ejes):** Se entiende por diagrama o gráfico. Cada objeto Axe pertenece a una sola Figura y se caracteriza por dos Axes. Otros objetos como el título, label x y label y.
- **Axis:** Los objetos de eje que tienen en cuenta los valores numéricos que se representarán en los ejes definen los límites y administran los ticks (la marca en los ejes) y las etiquetas de tick (el texto de la etiqueta representado en cada tick).

**Diagrama (visual):** una gráfica de una onda senoidal anotada con tres rectángulos anidados de colores que ilustran la jerarquía:

- Rectángulo rojo exterior, etiquetado **Figure** — envuelve toda la imagen.
- Rectángulo verde intermedio, etiquetado **Axes** — envuelve el área del gráfico (el par de ejes).
- Rectángulos azules, etiquetados **Axis** — uno vertical sobre el eje y (ticks 1.0, 0.5, 0.0, -0.5, -1.0) y otro horizontal sobre el eje x (ticks 0 a 6).

La curva es una sinusoide morada: parte cerca de 0 en x=0, sube a máximo ≈1.0 alrededor de x≈1.5, cruza 0 en x≈3, baja a mínimo ≈-1.0 en x≈4.7 y vuelve a subir hacia ≈0 en x≈6.3.

## Slide 9

Slide separador de sección: **3. Laboratorio Matplotlib**. Imagen decorativa (mano robótica sobre globo digital).
