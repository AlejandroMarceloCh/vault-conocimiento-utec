---
curso: ACD
titulo: [2025] U3_T2 Data Cleaning Nivel 3 Detectar
slides: 35
fuente: [2025] U3_T2 Data Cleaning Nivel 3 Detectar.pdf
---

## Slide 1

Portada (decorativa: fondo azul con silueta de robot humanoide en túnel tecnológico).

**Data Cleaning Nivel 3: Detectar**
*DS3021 Análisis Computacional de Datos*

## Slide 2

**¿Qué sabemos de esta marca?**

Visual: logo de **SAMSUNG** (óvalo azul con el nombre en blanco) centrado en la slide, sin texto adicional.

## Slide 3

**Sabían que ….**

En abril de 2018, **Samsung Securities** (la rama de negociación de acciones de la corporación Samsung) distribuyó accidentalmente acciones por valor de alrededor de **105 mil millones de dólares** a sus **empleados**, 30 veces más acciones que el número real de acciones en circulación totales.

(Solo texto sobre fondo azul degradado; "Samsung Securities", "105 mil millones de dólares" y "empleados" resaltados en amarillo.)

## Slide 4

**¿Qué sucedió?**

- Un empleado cometió un "**typo**" (typographical error). Se refiere a un error involuntario al escribir, como una letra mal col) y en lugar de escribir "**won**" (moneda coreana) escribió "**acciones**".
- Como resultado, se emitieron **2800 millones de acciones** (por un valor de **105 mil millones de dólares**) como pago a los empleados.
- La empresa tardó **37 minutos** en darse cuenta de lo sucedido y evitar que los empleados vendieran "acciones fantasmas". Sin embargo, durante ese periodo, **16 empleados** vendieron **5 millones de acciones** por un valor de alrededor **187 millones de dólares**.

Visual: ilustración plana a la derecha de un teclado turquesa con dos manos/dedos índice apuntando a teclas (metáfora del error de tipeo).

## Slide 5

**¿Cuáles fueron las consecuencias?**

- Las acciones cayeron casi un 12%, eliminando alrededor de 300 millones de dólares de su valor de mercado.
- Pérdida de relaciones con clientes importantes, incluido el fondo de pensiones más grande de Corea del Sur, debido a "preocupaciones" por medidas de seguridad deficientes.
- Los reguladores financieros le prohibieron aceptar nuevos clientes durante seis meses.
- El codirector ejecutivo Koo Sung-Hoon renunció.

Visual: ícono a la izquierda de una moneda grande con símbolo "$" (círculo verde), pilas de monedas grises a los lados y tres flechas apuntando hacia abajo encima (caída de valor).

## Slide 6

Slide de transición (solo título sobre fondo azul con comillas decorativas grandes):

**¿Cómo se hubiese evitado?**

## Slide 7

Etiqueta amarilla: **RECAPITULANDO** — **Técnicas** *de Preprocesamiento*

Diagrama de 4 filas (bloque azul con el nombre a la izquierda, descripción a la derecha). El primer bloque, **Data Cleaning**, está resaltado (relleno azul sólido + marco punteado amarillo) porque es el tema de la sesión; los demás tienen borde azul y relleno blanco.

| Técnica | Descripción |
|---|---|
| Data Cleaning | Limpieza de los datos. Remover ruido y corregir inconsistencias en los datos. |
| Data Integration | Mezcla data de diferentes recursos dentro de un almacenamiento coherente de datos (por ejemplo, data warehouse, etc.). |
| Data Reduction | Reducir el tamaño de los datos. Por ejemplo, agregar, eliminar características redundantes, etc. |
| Data Transformation | Normalización puede ser aplicada. |

## Slide 8

Etiqueta amarilla: **RECAP** — **Pasos** *Data Cleaning*

Diagrama circular: un anillo gris con un ícono central amarillo (diana con flecha) del que salen tres nodos azules distribuidos alrededor (arriba: ícono de personas; abajo-izquierda: lupa; abajo-derecha: cohete). Cada nodo conecta con un bloque de texto:

- **Nivel 1: Limpiar cómo luce la tabla** (nodo superior, ícono de personas). Se realiza la limpieza en base a las siguientes 3 características:
  - Estructura de datos estándar
  - Las columnas tienen nombres codificables e intuitivos
  - Cada fila tiene un identificador único
- **Nivel 2: Reestructuración y reformulación de la tabla** (nodo lupa, izquierda). Este nivel de limpieza tiene que ver con el tipo de estructura de datos y formato en el que necesita que esté el dataset para que se puedan realizar el análisis que se tiene en mente.
- **Nivel 3: Evaluar y corregir valores** (nodo cohete, derecha; su bloque está enmarcado en punteado amarillo = tema de la sesión). Este nivel de limpieza tiene que ver con la exactitud y existencia de los valores registrados en el dataset. En este nivel de limpieza, desea asegurarse de que los valores registrados sean correctos y se presenten de la manera que mejor respalde los objetivos analíticos. Aquí se evalúa la presencia de:
  - valores faltantes
  - outliers

## Slide 9

**Objetivo de sesión** (título vertical a la izquierda; foto decorativa teñida de azul de dos personas trabajando sobre planos).

Identificar y reconocer la importancia del proceso de limpieza de datos a nivel III. Especialmente centrado en el primer factor, los datos faltantes.

## Slide 10

**Data Cleaning Nivel 3**

**El objetivo** de este nivel es asegurarse que los datos sean **correctos** y **apropiados.**

Los tres usuales problemas relacionados a los datos registrados son:
- Valores Faltantes
- *Outliers*
- Errores

(Banda superior decorativa: foto de equipo de trabajo teñida de azul.)

## Slide 11

Slide divisoria de sección: **1. Valores Faltantes — Definición** (ícono de portapapeles; imagen decorativa de mano robótica sobre globo terráqueo digital).

## Slide 12

Los **valores faltantes** en un dataset son como **las piezas** de un rompecabezas **que se pierden**.

Visual: fotografía de un rompecabezas blanco armado con una pieza suelta encima y un hueco negro donde falta una pieza.

Nuestro objetivo es **encontrar esas piezas faltantes** y decidir **qué hacer con ellas.**

## Slide 13

**Valores** *Faltantes*

En el contexto de un dataframe, son celdas vacías. En Python, los valores faltantes se representan vía ***NaN (Not a Number).***

Visual: dos tablas lado a lado. La de la izquierda (dataset con celdas vacías) tiene la celda GPA de la fila 1 marcada con un círculo azul, conectada por línea punteada al `NaN` correspondiente en el dataframe de Python de la derecha (también circulado).

Izquierda — *Ejemplo de dataset con valores faltantes*:

| # | Gender | Height | Year | GPA | Personality Type |
|---|---|---|---|---|---|
| 1 | 1 | 190 | Sophomore | (vacío) | ISTJ |
| 2 | 1 | 189 | Freshman | 3.81 | ESNJ |
| 3 | 0 | 160 | Freshman | (vacío) | ISTJ |
| 4 | 1 | 181 | Sophomore | 3.95 | INTP |
| 5 | 1 | (vacío) | Freshman | 3.62 | ISTJ |
| 6 | 0 | 184 | Freshman | 3.87 | (vacío) |
| 7 | 0 | 172 | Junior | 3.31 | ISTP |

Derecha — *Ejemplo de dataframe en Python con valores faltantes*:

| idx | Gender | Height | Year | GPA | Personality Type |
|---|---|---|---|---|---|
| 0 | 1 | 190.0 | Sophomore | NaN | ISTJ |
| 1 | 1 | 189.0 | Freshman | 3.81 | ESNJ |
| 2 | 0 | 160.0 | Freshman | NaN | ISTJ |
| 3 | 1 | 181.0 | Sophomore | 3.95 | INTP |
| 4 | 1 | NaN | Freshman | 3.62 | ISTJ |
| 5 | 0 | 184.0 | Freshman | 3.87 | NaN |
| 6 | 0 | 172.0 | Junior | 3.31 | ISTP |

## Slide 14

**Problemas** *asociados a Valores Faltantes*

- Los valores faltantes pueden hacer que si usamos la data para la fase de modelamiento, **el modelo esté sesgado** si no se manejan con cuidado.
- **Hay una pérdida de poder estadístico** cuando nos faltan valores. Significa que influye negativamente en la probabilidad de que la prueba de hipótesis rechace la hipótesis nula cuando no es válida.
- Se hacen **inferencias incorrectas**, análisis, etc.

Solo texto.

## Slide 15

Slide divisoria de sección: **2. Valores Faltantes — Diagnóstico** (misma plantilla e imagen de mano robótica que la slide 11).

## Slide 16

**Tipos** *de Valores Faltantes*

Diagrama en escalera descendente: tres círculos azules numerados (1, 2, 3), cada uno unido por una línea amarilla con un punto a una píldora azul con el nombre del tipo. Los elementos se desplazan progresivamente hacia la derecha y hacia abajo.

1. **Missing Completely at Random (MCAR)**
2. **Missing at Random (MAR)**
3. **Missing not at Random (MNAR)**

## Slide 17

**Tipo 1:** *Missing Completely at Random (MCAR)*

Los valores faltantes **son completamente aleatorios** y **no dependen de ninguna variable** observada o no observada en el dataset.

Tres tarjetas en fila (la del medio, "Impacto", con fondo celeste; las otras dos grises), cada una con un ícono:

| | Ejemplo (ícono de señal/onda emitida) | Impacto (ícono de servidor con bits 0/1 y flechas hacia abajo) | Efecto si lo ignoramos (sello rojo "NO SIDE EFFECTS") |
|---|---|---|---|
| | Un sensor de temperatura que ocasionalmente falla sin ningún patrón identificable | No introduce sesgo, pero reduce la cantidad de datos disponible. | No hay ningún efecto sobre las inferencias (estimaciones imparciales), aunque podría reducir el poder estadístico. |

## Slide 18

**Tipo 2:** *Missing at Random (MAR)*

Los valores faltantes **dependen de alguna variable observada, pero no de la variable con el valor faltante en sí.**

Mismo layout de tres tarjetas:

| | Ejemplo (ícono de dos jóvenes) | Impacto (ícono de balanza desequilibrada con signo de interrogación) | Efecto si lo ignoramos (ícono de balanza tachada + persona con interrogantes) |
|---|---|---|---|
| | Los ingresos de los encuestados pueden faltar más frecuentemente para los encuestados más jóvenes. | Introduce sesgo si no se maneja adecuadamente, pero puede ser corregido si la variable asociada está bien entendida. | Las inferencias y predicciones están sesgadas. |

## Slide 19

**Tipo 3:** *Missing Not at Random (MNAR)*

Los valores faltantes **dependen de la variable con el valor faltante en sí.**

Mismo layout de tres tarjetas:

| | Ejemplo (ícono de hombre de traje con moneda y flecha ascendente) | Impacto (balanza desequilibrada con interrogación) | Efecto si lo ignoramos (balanza tachada + persona con interrogantes) |
|---|---|---|---|
| | Las personas con ingresos muy altos pueden no querer revelar sus ingresos, lo que lleva a una falta de datos en esa variable específica. | Introduce sesgo significativo y es el más difícil de tratar. | Las inferencias y predicciones están sesgadas. |

## Slide 20

**TU TURNO** — slide de actividad (fondo decorativo: mujer con visor de realidad virtual y globo terráqueo digital).

## Slide 21

Visual: ilustración de una pizarra/monitor verde con el logo **Mentimeter** y dos personas ilustradas apoyadas al pie.

Ingresa al enlace https://www.menti.com/ y responde a la pregunta planteada por el docente.

## Slide 22

Slide de código de actividad sobre foto decorativa de laboratorio:

**U3_L3**
**DCNivel3_MissingValues1**

## Slide 23

**Cierre** *de la Sesión*

- ¿Cuál es el objetivo principal del Nivel 3 de la Limpieza de Datos?
- ¿Cuáles son los tipos de valores faltantes?

(Foto decorativa de laboratorista a la izquierda.)

## Slide 24

Slide divisoria de sección: **3. Valores Faltantes — Manejo** (misma plantilla de mano robótica).

## Slide 25

**Objetivo de sesión** (mismo layout que la slide 9).

Identificar las estrategias para manejar los datos faltantes en datasets teniendo en consideración su tipología.

## Slide 26

Slide de transición, solo texto sobre fondo azul degradado:

Una vez **detectado** la presencia de datos faltantes en nuestro dataset

**¿Qué hacemos?**

## Slide 27

**Estrategias** *generales*

Diagrama en zigzag descendente: cuatro círculos azules con íconos, encadenados por una cinta gris en forma de S, cada uno con una etiqueta unida por línea amarilla (alternando derecha/izquierda):

1. (lupa) → **Ignorar los valores faltantes** — a la derecha
2. (diana) → **Eliminar filas con valores faltantes** — a la izquierda
3. (cohete) → **Eliminar columnas con valores faltantes** — a la derecha
4. (calendario) → **Estimar e imputar un valor** — a la izquierda

## Slide 28

**Estrategia 1:** *Ignorar los valores faltantes*

- Se utiliza esta estrategia en los casos en los que **compartirá estos datos con otras personas** y no será necesariamente usted quien los utilizará para análisis. De esta manera, les permitirá decidir cómo deben abordar los valores faltantes en función de sus necesidades analíticas.
- En segundo lugar, si tanto los objetivos de análisis de datos como las herramientas de análisis de datos que utilizará **pueden manejar sin problemas los valores faltantes**, mantenerlo como está es el mejor enfoque.

(Foto decorativa a la derecha: docente escribiendo en una pizarra, teñida de azul.)

## Slide 29

**Estrategia 2:** *Eliminar filas con valores faltantes*

Este enfoque debe seleccionarse con mucho cuidado porque puede ir en contra de los dos objetivos de abordar con éxito los valores faltantes:
- no introducir sesgos en el conjunto de datos y
- no eliminar información valiosa del dataset.

Por ejemplo, cuando los valores faltantes en un conjunto de datos son del tipo **MNAR** o **MAR**, debemos abstenernos de eliminar las filas con valores faltantes. Esto se debe a que hacerlo significa que se elimina una parte significativamente distinta de la población del conjunto de datos.

Incluso si los valores faltantes son del tipo **MCAR**, primero deberíamos intentar encontrar otras formas de lidiar con los valores faltantes antes de eliminar las filas.

## Slide 30

**Estrategia 3:** *Eliminar columnas con valores faltantes*

Cuando la mayoría de los valores faltantes en un dataset provienen de uno o dos atributos, podríamos **considerar eliminar los atributos** como una forma de lidiar con los valores faltantes.

Por supuesto, si el atributo es **un atributo clave** sin el cual no se puede continuar con el proyecto, enfrentar demasiados valores faltantes en el atributo clave significa que el proyecto no es factible.

Sin embargo, **si los atributos no son absolutamente esenciales** para el proyecto, **eliminar los atributos** con demasiados valores faltantes podría ser el enfoque correcto.

**TIP:** Cuando el número de valores faltantes en un atributo es lo suficientemente grande (aprox > 25%), estimar e ingresar valores faltantes deja de tener sentido y dejar de lado el atributo es mejor que estimar los valores faltantes.

(Foto decorativa a la derecha: docente en pizarra.)

## Slide 31

**Estrategia 4:** *Estimar e imputar un valor*

En este enfoque, usamos nuestro conocimiento, comprensión y herramientas analíticas para completar los valores faltantes.

El término **imputación** captura la esencia de lo que esto le hace a un dataset: **asignamos valor** en lugar de valor faltante sabiendo que esto podría causar sesgo en nuestro análisis.

Si los valores faltantes son del tipo **MCAR o MAR** y la analítica que hemos elegido no puede procesar el dataset con valores faltantes, imputar los valores faltantes podría ser el mejor enfoque.

Solo texto.

## Slide 32

**Estrategia 4:** *Estimar e imputar un valor*

Existen cuatro métodos generales para estimar el reemplazo de los valores faltantes:

- ***Imputar con la tendencia central general*** (media, mediana o moda). Esto es mejor para los valores faltantes de **MCAR**.
- ***Imputar la tendencia central de un grupo de datos más relevante a los valores faltantes.*** Esto es mejor para los valores faltantes de **MAR**.
- ***Análisis de regresión.*** No es ideal, pero si tenemos que proceder con un conjunto de datos al que le faltan valores **MNAR**, este método es mejor para dicho conjunto de datos.
- ***Interpolación.*** Cuando el conjunto de datos es un conjunto de datos de series temporales y los valores faltantes son del tipo **MCAR**.

## Slide 33

**TU TURNO** — slide de actividad (misma imagen decorativa que la slide 20).

## Slide 34

Visual idéntico a la slide 21: ilustración de pizarra verde con el logo **Mentimeter**.

Ingresa al enlace https://www.menti.com/ y responde a la pregunta planteada por el docente.

## Slide 35

Slide de código de actividad sobre foto decorativa de laboratorio:

**U3_L4**
**DCNivel3_MissingValues2**
