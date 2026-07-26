---
curso: ACD
titulo: [2025] U4_T1 Ingeniería de Características
slides: 13
fuente: [2025] U4_T1 Ingeniería de Características.pdf
---

## Slide 1

Portada.

**Ingeniería de Características**
DS3021 Análisis Computacional de Datos
Mg. José Espinoza Melgarejo

Imagen de fondo decorativa (silueta caminando por un túnel tecnológico azul). Chrome institucional decorativo.

## Slide 2

**Objetivo de sesión** (título vertical en el margen izquierdo)

> Comprender e identificar la importancia de la ingeniería de características en Ciencia de Datos.

Foto decorativa (dos personas trabajando sobre una mesa, tinte azul).

## Slide 3

Slide separadora de sección.

**1. Ingeniería de Características**

Ícono de portapapeles con checklist junto al título; imagen decorativa de una mano robótica señalando un globo terráqueo digital.

## Slide 4

**Ingeniería de Características**

La **ingeniería de características** es un proceso esencial en el *preprocesamiento de datos* (resaltado en celeste) para mejorar la calidad y la relevancia de las características utilizadas en un *modelo de machine learning*. Este proceso puede involucrar la **extracción de características** a partir de datos brutos, la **selección de características relevantes** y la **eliminación de las no relevantes**, y la **creación de nuevas características** a partir de características existentes.

Banda superior decorativa (foto de equipo trabajando + barra degradado negro→celeste).

## Slide 5

**Tipos de Ingeniería de Características**

Dos bloques paralelos, cada uno con una estrella/badge azul numerada encima de una tarjeta (encabezado celeste + cuerpo blanco con borde):

| # | Tipo | Definición |
|---|------|------------|
| 1 | Preprocesamiento de características (Feature preprocessing) | Consiste en transformar y actualizar las características existentes. |
| 2 | Generación de características (Feature generation) | Consiste en crear nuevas características a partir de los datos existentes. |

## Slide 6

**Importancia de la Ingeniería de Características**

Infografía en zigzag descendente: cinco círculos-ícono azules encadenados por una cinta gris en diagonal (de arriba-izquierda a abajo-derecha), cada uno conectado con una línea amarilla en escuadra a un bloque de texto alternando lado derecho/izquierdo.

1. Ícono lupa → **Mejora de desempeño** (derecha): Las características bien diseñadas pueden elevar la precisión y eficiencia del modelo.
2. Ícono diana → **Manejo de datos ruidosos** (izquierda): Ayuda a identificar y eliminar información irrelevante o ruido, mejorando la calidad de los datos.
3. Ícono cohete → **Captura de patrones específicos** (derecha): Facilita la identificación de patrones no evidentes en las características originales.
4. Ícono calendario/tabla → **Adaptación al modelo** (izquierda): Ajusta características para satisfacer requisitos específicos de ciertos algoritmos.
5. Ícono clip/enlace → **Interpretación y comprensión** (derecha): Características bien diseñadas hacen el modelo más interpretable.

## Slide 7

**Retos que plantea la ingeniería de caraterísticas** [sic]

Tres párrafos numerados, cada uno precedido por un círculo celeste con el número:

1. La *recopilación de datos* es el proceso de agrupar todos los datos que se necesitan para el machine learning. Dicho proceso puede resultar tedioso, ya que los datos residen en muchos orígenes de datos, incluidos portátiles, almacenamientos de datos, la nube, aplicaciones y dispositivos.
2. El *etiquetado de datos* es el proceso para identificar los datos sin procesar (imágenes, archivos de texto, videos, etc.) y agregar una o más etiquetas significativas e informativas para proporcionar contexto, de manera que un modelo de machine learning pueda aprender de estos.
3. Una vez que los datos están limpios y etiquetados, los equipos de machine learning a menudo los exploran para asegurarse de que son correctos y están listos para el machine learning. Las *visualizaciones* como histogramas, gráficos de dispersión, gráficos de caja, gráficos de línea y gráficos de barra son herramientas útiles para confirmar que los datos son correctos.

## Slide 8

Slide separadora de sección.

**2. Técnicas de ingeniería de características**

Mismo layout e imagen decorativa (mano robótica + globo digital) que la slide 3.

## Slide 9

**Técnicas de Ingeniería de Características**

Diagrama de árbol: caja celeste **Transformación de características** (arriba-izquierda) con su definición a la derecha; dos flechas azules bajan hacia dos tarjetas hijas.

> Es el proceso de convertir un tipo de característica en otra forma más legible para un modelo en particular. Esto consiste en transformar datos continuos en datos categóricos, o viceversa.

| Rama | Descripción |
|------|-------------|
| Discretización (binning) | Transforma los valores numéricos continuos en características categóricas. Compara cada valor con los valores vecinos que lo rodean y luego ordena los puntos de datos en varios segmentos o intervalos (bins). |
| Codificación one-hot | Es lo contrario de la discretización. Crea características numéricas a partir de variables categóricas asignando características categóricas a representaciones binarias en una matriz o espacio vectorial. |

## Slide 10

**Técnicas de Ingeniería de Características**

Mismo diagrama de árbol; nodo padre: caja con borde celeste y texto azul **Escalado de características**. Marca de agua de bombilla en el centro.

> Es una técnica de estandarización para cambiar la escala de características y limitar el impacto de las escalas grandes en los modelos.

| Rama | Descripción |
|------|-------------|
| Escalado mínimo-máximo | Reescala todos los valores de una característica determinada para que se sitúen entre los valores mínimo y máximo especificados, a menudo 0 y 1. |
| Escalado de la puntuación Z | Reescala las características para que tengan una desviación estándar compartida de 1 con una media de 0. |

## Slide 11

**Técnicas de Ingeniería de Características**

Mismo diagrama de árbol; nodo padre celeste **Extracción y selección de características**, dos flechas hacia las tarjetas hijas.

> Es una técnica para crear un nuevo espacio dimensional para un modelo mediante la combinación de variables en nuevas variables sustitutas o para reducir las dimensiones del espacio de características del modelo.

| Rama | Descripción |
|------|-------------|
| Análisis de componentes principales (PCA) | Método común de extracción de características que combina y transforma las características originales de un conjunto de datos para producir nuevas características o variables llamadas componentes principales. |
| Análisis discriminatorio lineal (LDA) | Método que proyecta los datos del modelo en un nuevo espacio de menor dimensionalidad, produciendo variables de componentes principalmente destinadas a maximizar la diferencia de clase en los datos. |

## Slide 12

**Técnicas de Ingeniería de Características** — resumen

Tres filas: etiqueta en caja celeste a la izquierda (la segunda con borde celeste y texto azul en vez de relleno sólido) y descripción a la derecha.

| Técnica | Resumen |
|---------|---------|
| Transformación de características | Convierte datos entre formatos continuos y categóricos para mejorar la comprensión del modelo. |
| Escalado de características | Estandariza las características para reducir el efecto de escalas desiguales en los modelos. |
| Extracción y selección de características | Transforma o reduce el espacio de características mediante la combinación de variables para mejorar el rendimiento del modelo. |

## Slide 13

Slide de cierre.

**U4_L1 Ingeniería de Características**

Foto decorativa (dos estudiantes con bata y lentes de seguridad en laboratorio, tinte azul).
