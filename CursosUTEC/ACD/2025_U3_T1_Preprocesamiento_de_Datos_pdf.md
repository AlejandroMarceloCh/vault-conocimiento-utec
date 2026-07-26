---
curso: ACD
titulo: [2025] U3_T1 Preprocesamiento de Datos
slides: 19
fuente: [2025] U3_T1 Preprocesamiento de Datos.pdf
---

## Slide 1

Portada.

**Preprocesamiento de Datos**
*DS3021 Análisis Computacional de Datos*

Fondo decorativo (túnel tecnológico azul con silueta humanoide).

## Slide 2

Slide de imagen a pantalla completa: foto de un vertedero de basura con excavadora, sobre la que se superpone el título en blanco:

**Data Cleaning**
*How dirty is real data?*

La metáfora visual: los datos reales son "basura" que hay que limpiar.

## Slide 3

Frase a pantalla completa sobre fondo oscuro con una red de nodos luminosa a la izquierda y una mano tocando una pantalla:

> **Una baja calidad de datos origina una baja calidad de resultados**

## Slide 4

**Objetivo de sesión** (título vertical en el borde izquierdo).

Comprender e identificar la importancia de realizar el preprocesamiento de datos en Ciencia de Datos.

Imagen decorativa: dos personas trabajando sobre planos, con filtro azul.

## Slide 5

Slide separador de sección.

**1. Preprocesamiento de Datos**

Ícono de portapapeles con checklist. Imagen decorativa de mano robótica señalando un globo terráqueo digital.

## Slide 6

**Preprocesamiento de Datos**

El preprocesamiento de datos se puede definir como el proceso de conversión de datos sin procesar (raw data) a un formato que sea **comprensible** y **utilizable** para un análisis posterior. Es un paso importante en la etapa de *Preparación de Datos (ciclo de vida Ciencia de Datos)*. Garantiza que el resultado del análisis sea **preciso, completo y coherente**.

(Banda superior decorativa con foto de equipo de trabajo y grafismos de líneas punteadas.)

## Slide 7

**¿Por qué es importante el Preprocesamiento de Datos?**

Infografía: una cinta/serpentina gris descendente en diagonal (de arriba-izquierda a abajo-derecha) que encadena 5 círculos azules con íconos —lupa, diana, cohete, calendario y clip/eslabón— cada uno conectado por una línea amarilla en escuadra a un bloque de texto que alterna lado derecho / izquierdo:

| Ícono | Concepto | Descripción |
|---|---|---|
| Lupa | **Accuracy (precisión)** | El preprocesamiento de datos garantizará que los datos de entrada sean precisos y confiables al garantizar que no existan errores de entrada manual, duplicados, etc |
| Diana | **Completeness (integridad)** | Garantiza que se manejen los valores faltantes y que los datos estén completos para su posterior análisis. |
| Cohete | **Consistent (consistencia)** | El preprocesamiento de datos garantiza que los datos de entrada sean consistentes, es decir, los mismos datos guardados en diferentes lugares deben coincidir. |
| Calendario | **Trustable (confiable)** | Si los datos provienen de datos confiables o no. |
| Eslabón | **Interpretability (interpretabilidad)** | Los datos sin procesar generalmente no se pueden utilizar y el preprocesamiento de datos los convierte en un formato interpretable. |

## Slide 8

Slide separador de sección.

**2. Técnicas de Preprocesamiento**

Mismo diseño e imagen decorativa que la slide 5 (mano robótica).

## Slide 9

**Técnicas de Preprocesamiento**

Etiqueta en caja celeste sólida: **Data Cleaning** — "Limpieza de los datos. Remover ruido y corregir inconsistencias en los datos."

Diagrama: a la izquierda un cilindro (base de datos) gris con muchos puntos/burbujas celestes desperdigados encima (el ruido); una flecha negra apunta a la derecha hacia un cilindro dibujado con contorno celeste limpio, sin puntos. Detrás, marca de agua de un foco (bombilla).

## Slide 10

**Técnicas de Preprocesamiento**

Etiqueta en caja de contorno celeste: **Data Integration** — "Mezcla data de diferentes recursos dentro de un almacenamiento coherente de datos (por ejemplo data warehouse, etc)"

Diagrama: tres fuentes apiladas a la izquierda —(1) un cilindro/base de datos, (2) un cubo 3D reticulado (cubo OLAP), (3) una fila de celdas tipo tabla/archivo con borde rasgado— y tres flechas negras que convergen en un único cilindro a la derecha (el almacén integrado).

## Slide 11

**Técnicas de Preprocesamiento**

Etiqueta en caja celeste sólida: **Data Reduction** — "Reducir el tamaño de los datos. Por ejemplo, agregar, eliminar características redundantes, etc."

Diagrama: a la izquierda una grilla grande vacía de 5 columnas × 5 filas; una flecha apunta a la derecha hacia una grilla más pequeña de 4 columnas × 4 filas. Representa la reducción de dimensionalidad/tamaño.

## Slide 12

**Técnicas de Preprocesamiento**

Etiqueta en caja de contorno celeste: **Data Transformation** — "Normalización puede ser aplicada."

Ejemplo con flecha de izquierda a derecha:

```
-2, 32, 100, 59, 48   →   -0.02, 0.32, 1.00, 0.59, 0.48
```

(Escalado dividiendo entre 100 / normalización al rango de la magnitud máxima.)

## Slide 13

**Técnicas de Preprocesamiento** — resumen de las 4 técnicas en tabla de dos columnas (etiqueta en caja + descripción):

| Técnica | Descripción |
|---|---|
| **Data Cleaning** | Limpieza de los datos. Remover ruido y corregir inconsistencias en los datos. |
| **Data Integration** | Mezcla data de diferentes recursos dentro de un almacenamiento coherente de datos (por ejemplo data warehouse, etc) |
| **Data Reduction** | Reducir el tamaño de los datos. Por ejemplo, agregar, eliminar características redundantes, etc. |
| **Data Transformation** | Normalización puede ser aplicada. |

Las cajas de Cleaning y Reduction van en celeste sólido; Integration y Transformation en contorno celeste.

## Slide 14

Slide separador de sección.

**2. Data Cleaning** (mantiene el número "2." de la sección anterior). Mismo diseño e imagen decorativa de mano robótica.

## Slide 15

**Data Cleaning**

Los datos del mundo real tienden a ser incompletos, ruidosos e inconsistentes. Las rutinas de ***data cleaning*** (limpieza de datos) intentan completar los valores faltantes, suavizar el ruido mientras identifican los valores atípicos y corrigen las inconsistencias en los datos.

## Slide 16

**Pasos Data Cleaning**

Infografía circular: un anillo gris con un círculo amarillo central (ícono de diana/objetivo) rodeado de 6 nodos circulares; 3 de ellos llevan ícono (usuarios arriba, lupa abajo-izquierda, cohete abajo-derecha) y se conectan con una línea celeste a un bloque de texto:

- **Nivel 1: Limpiar cómo luce la tabla** (nodo superior, ícono de usuarios) — Se realiza la limpieza en base a las siguientes 3 características:
  - Estructura de datos estándar
  - Las columnas tienen nombres codificables e intuitivos
  - Cada fila tiene un identificador único
- **Nivel 2: Reestructuración y reformulación de la tabla** (nodo izquierdo, ícono de lupa) — Este nivel de limpieza tiene que ver con el tipo de estructura de datos y formato en el que necesita que esté el dataset para que se puedan realizar el análisis que se tiene en mente.
- **Nivel 3: Evaluar y corregir valores** (nodo derecho, ícono de cohete) — Este nivel de limpieza tiene que ver con la exactitud y existencia de los valores registrados en el dataset. En este nivel de limpieza, desea asegurarse de que los valores registrados sean correctos y se presenten de la manera que mejor respalde los objetivos analíticos. Aquí se evalúa la presencia de:
  - valores faltantes
  - outliers
  - coherencia

## Slide 17

Slide de transición a laboratorio, con foto decorativa de dos personas en un laboratorio (filtro azul):

**U3_L1 DataCleaning_Nivel1**

## Slide 18

Slide de transición a laboratorio, misma foto y diseño que la anterior:

**U3_L2 DataCleaning_Nivel2**

## Slide 19

Texto a la izquierda:

Una respuesta para analizar los discursos es analizar la frecuencia de las palabras:
- voto (vote)
- impuestos (tax)
- campaña (campaign)
- economía (economy)

**Gráfico (matplotlib, barras agrupadas):**
- Eje Y: "Average Word Frequency", de 0.00000 a ~0.00200 (marcas cada 0.00025).
- Eje X: "Year_Month" con 12 categorías rotadas 90°: 2019_Jul, 2019_Aug, 2019_Sep, 2019_Oct, 2019_Nov, 2019_Dec, 2020_Jan, 2020_Feb, 2020_Mar, 2020_Jun, 2020_Aug, 2020_Sep.
- 4 series por grupo (leyenda arriba a la derecha, 2 columnas): **vote** (azul), **tax** (naranja), **campaign** (verde), **economy** (rojo).

Lecturas clave aproximadas:
- "vote" es casi siempre la barra dominante; pico máximo en **2019_Nov (~0.00205)**; también alto en 2019_Jul y 2019_Aug (~0.00160) y en 2020_Aug (~0.00158).
- "tax" tiene su máximo en **2020_Mar (~0.00151)** y valores altos en 2019_Sep (~0.00134) y 2020_Jan (~0.00133).
- "campaign" destaca en **2019_Aug (~0.00150)** y 2019_Oct (~0.00085); en el resto de meses es bajo (<0.0006).
- "economy" se mantiene bajo y estable (~0.00022–0.00067), sin picos marcados.
- En 2019_Oct falta/es nula la barra de "vote" comparativamente baja (~0.00041) y "campaign" supera al resto.
