---
curso: ACD
titulo: [2025] U3_T3 Data Cleaning Nivel 3 Outliers
slides: 20
fuente: [2025] U3_T3 Data Cleaning Nivel 3 Outliers.pdf
---

## Slide 1

Portada (decorativa: fondo azul con silueta caminando en túnel tecnológico).

**Data Cleaning Nivel 3: Outliers**
DS3021 Análisis Computacional de Datos

## Slide 2

Etiqueta amarilla "RECAPITULANDO".

**Data Cleaning Nivel 3**

El objetivo de este nivel es asegurarse que los datos sean **correctos** y **apropiados**.

Los tres usuales problemas relacionados a los datos registrados son:
- Valores Faltantes
- *Outliers*
- Errores

## Slide 3

Slide separadora (imagen decorativa: persona con visor VR sobre globo terráqueo digital).

**Data Cleaning Nivel 3 — Outliers**

## Slide 4

Slide de objetivo, con foto decorativa lateral.

**Objetivo de sesión:** Identificar y tratar de manera computacional la presencia de outliers en un conjunto de datos.

## Slide 5

Slide separadora de sección, numeral grande "**1.**" con subrayado celeste e ícono de portapapeles. Imagen decorativa: mano robótica sobre globo digital.

**Outliers — Definición**

## Slide 6

**Outliers**

Los ***outliers*** (valores atípicos) son datos cuyos valores son demasiado diferentes al resto de la población.

Visual: render 3D con cinco esferas alineadas sobre fondo beige; cuatro son azules pequeñas y la del centro es notablemente más grande y de color magenta — metáfora visual del valor atípico frente a la población.

## Slide 7

**¿Por qué es importante *detectar y manejar los outliers*?**

1. Los outliers pueden **ser errores** en la data y **deben detectarse y eliminarse**.
2. Los outliers que **no son errores** pueden **sesgar los resultados** de las herramientas analíticas que son sensibles a la existencia de outliers.
3. Los outliers pueden ser **entradas fraudulentas**.

Foto decorativa lateral (estudiantes en laboratorio).

## Slide 8

Slide separadora de sección, numeral "**2.**" con ícono de portapapeles. Imagen decorativa: mano robótica.

**Outliers — Detección**

## Slide 9

**Detección *de Outliers***

Las herramientas que utilizamos para detectar *outliers* dependen de la cantidad de atributos involucrados.

Diagrama: tres filas escalonadas en diagonal descendente. Cada fila tiene un círculo azul numerado conectado por una línea amarilla con un punto intermedio hacia una píldora azul con texto:

| # | Píldora |
|---|---------|
| 1 | Detección de Outliers UNIVARIADOS |
| 2 | Detección de Outliers BIVARIADOS |
| 3 | Detección de Outliers MULTIVARIADOS |

## Slide 10

Slide separadora con foto decorativa (laboratorio).

**U3_L5 DCNivel3_Outliers**

## Slide 11

Slide separadora con foto decorativa lateral.

**Detección de Outliers — Univariados**

## Slide 12

**Detección de Outliers — Univariados**

- Los outliers univariados son valores **muy grandes** o **pequeños** que ocurren en **una sola variable** en un conjunto de datos.
- Estos valores se consideran extremos y suelen ser diferentes del resto de valores de la variable.
- Es importante identificarlos y abordarlos antes de realizar cualquier análisis o modelado adicional.

Visual (derecha): boxplot vertical estilo R. Eje Y con marcas en 20, 40, 60, 80. La caja está aproximadamente entre 18 y 27, con mediana cerca de 22; bigote inferior baja hasta ~10 y el superior sube hasta ~29. Muy arriba, cerca de 78–82, hay tres puntos sueltos rodeados por un círculo punteado celeste rotulado "**Outliers**".

## Slide 13

**Detección de Outliers — Univariados**

Existen dos métodos principales para identificar outliers univariados:

1. **Métodos estadísticos:** Como el rango intercuartil (IQR), la puntuación Z y la medida de asimetría.
2. **Visualización de datos:** Los histogramas y boxplots son gráficos muy útiles que muestran la distribución de un conjunto de datos. La forma de la distribución puede indicar dónde se encuentran los valores atípicos.

Visual (derecha): esquema anotado de un boxplot horizontal sobre eje de −4 a 4. Caja rosada entre Q1 (percentil 25) y Q3 (percentil 75) con línea amarilla de mediana en 0; llave superior rotulada "Interquartile Range (IQR)". Bigote izquierdo termina en "Minimum" = $Q1 - 1.5 \cdot IQR$ (~−3) y el derecho en "Maximum" = $Q3 + 1.5 \cdot IQR$ (~+3). Fuera de cada bigote hay puntos verdes con flechas rotuladas "Outliers" a ambos lados.

## Slide 14

Slide separadora con foto decorativa lateral.

**Detección de Outliers — Bivariado**

## Slide 15

**Detección de Outliers — Bivariados**

- Los outliers bivariados suelen ser valores grandes o pequeños que ocurren en **dos variables simultáneamente**.
- Individualmente, los valores de cada variable pueden o no ser outliers; sin embargo, **en conjunto, son outliers**.
- Para identificarlos utilizaremos scatterplot o boxplots dependiendo de las variables.

Visual (izquierda): scatterplot Weight (eje X, 40–150) vs Height (eje Y, 60–200). Nube densa azul con tendencia positiva concentrada entre Weight 45–100 y Height 150–195. Arriba a la derecha (Weight ≈ 145–155, Height ≈ 195–205) hay dos puntos separados encerrados por un recuadro punteado amarillo rotulado "**Outliers**". También se ve un punto aislado abajo a la izquierda (Weight ≈ 55, Height ≈ 63).

## Slide 16

Slide separadora con foto decorativa lateral.

**Detección de Outliers — Multivariado**

## Slide 17

**Detección de Outliers — Multivariado**

- Los outliers multivariados son valores extremos que ocurren en **tres o más variables simultáneamente.**
- La mejor manera de realizar la detección de outliers multivariados es mediante el análisis de agrupamiento (clustering).

Visual (derecha): scatterplot 3D titulado "Isolation Forest Anomaly Detection", con leyenda azul = *inliers*, rojo = *outliers*. Ejes: GDP Per Capita (0–120000), Median Age (15–45) y Cases Per Million (0–800000). La masa azul se concentra en GDP bajo y Median Age bajo-medio; los puntos rojos aparecen dispersos en zonas extremas (alto Cases Per Million y GDP/edad altos).

## Slide 18

Slide separadora de sección, numeral "**3.**" con ícono de portapapeles. Imagen decorativa: mano robótica.

**Outliers — Manejo**

## Slide 19

**Outliers — Manejo**

1. No hacer nada
2. Reemplazarlos por:
   a. **Medidas estadísticas:** La media, la mediana o los percentiles del conjunto de datos.
   b. **Interpolación:** Estimar el valor de un outlier utilizando los puntos de datos vecinos del outlier.
   c. **Métodos basados en modelos:** El uso de un modelo de ML para predecir el valor de reemplazo de los valores atípicos.
3. Desarrollar una transformación logarítmica
4. Eliminarlos

Foto decorativa lateral.

## Slide 20

**Cierre *de la Sesión***

- ¿Qué son los outliers?
- ¿Cómo los identificamos y manejamos?

Foto decorativa lateral (científica en laboratorio).
