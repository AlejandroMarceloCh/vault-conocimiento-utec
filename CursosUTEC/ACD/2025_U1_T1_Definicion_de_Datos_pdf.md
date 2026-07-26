---
curso: ACD
titulo: [2025] U1_T1 Definición de Datos
slides: 41
fuente: [2025] U1_T1 Definición de Datos.pdf
---

## Slide 1

Portada.

**Definición de los Datos**
DS3021 Análisis Computacional de Datos

Fondo decorativo (túnel de datos azul con silueta). Resto es chrome institucional.

## Slide 2

**Contenido**

1. Definición de los datos
2. Tipos de atributos

Cada ítem con un ícono (portapapeles / engranaje-bombilla). Fondo decorativo.

## Slide 3

**Objetivo de la sesión**

> Introducir conceptos y tipologías sobre los datos que son esenciales para el pre-procesamiento de datos de manera efectiva.

Foto decorativa de dos personas trabajando, teñida de azul.

## Slide 4

Separador de sección.

**1. Definición de los datos**

Ícono de portapapeles; imagen decorativa de mano robótica sobre globo terráqueo digital.

## Slide 5

Slide de pregunta, fondo azul con comillas grandes.

**¿Qué entendemos por DATOS?**

## Slide 6

**Definición de datos**

Desde una perspectiva de **preprocesamiento de datos**:

**Definimos datos** como símbolos o signos que representan una medida o modelo de la realidad. Estos símbolos y signos **son inútiles en sí mismos** hasta que se utilizan con respecto a convenciones y entendimientos de nivel superior (*Higher-Level Conventions and Understandings* - **HLCU**).

**Nota:** HLCU es un término utilizado en la evaluación de escritura, especialmente en pruebas estandarizadas como el TOEFL, IELTS o AP English Language and Composition.

## Slide 7

**¿Por qué esta definición?**

- Para el preprocesamiento de datos, lo primero que debe decidir es la HLCU que utilizará.
- Es decir, **¿para qué HLCU está preparando sus datos?**
  - Si los datos se preparan para la comprensión humana, el resultado será muy diferente que cuando los datos se preparan para computadoras y algoritmos. No solo eso, la HLCU puede ser diferente de un algoritmo a otro.

**Visual:** ilustración plana de un programador de espaldas frente a un monitor con código; a su alrededor, burbujas de colores con logos/nombres de lenguajes y tecnologías (PHP, HTML5, CSS3, http, .com, JAVA, JS, Ruby, CSS3, Swift, C#, Python, Arduino) y símbolos `</>`, lupa, documento. Refuerza la idea de que la "convención de nivel superior" depende del consumidor/tecnología.

## Slide 8

**Pirámide DIKW** — *Data, Information, Knowledge, and Wisdom*

**Visual:** pirámide 3D de 4 capas separadas por bandas grises, de arriba hacia abajo: dorada (1), verde (2), azul (3), verde-azulado/teal (4). Cada capa tiene a la izquierda su etiqueta y descripción, y a la derecha una flecha-banner que nombra el proceso que lleva de una capa a la siguiente.

| # | Capa | Descripción | Proceso hacia arriba (flecha) |
|---|------|-------------|-------------------------------|
| 1 | Sabiduría | Encarnación del Conocimiento y apreciación del **por qué**. | Juicio (entre 2→1) |
| 2 | Conocimiento | Aplicación descriptiva de la *Información* - puede responder la pregunta **cómo** | Cognición (entre 3→2) |
| 3 | Información | Data procesada - puede responder las preguntas: **quién, cuándo, dónde y qué** | Procesamiento (entre 4→3) |
| 4 | Data | Colección de símbolos - **no puede responder** ninguna pregunta | — |

A la derecha, un eje vertical con marcadores: **Futuro** arriba (nivel Sabiduría) y **Pasado** abajo (niveles Información/Data).

## Slide 9

**Pirámide DIKW** — *Data, Information, Knowledge, and Wisdom*

Misma pirámide de 4 capas de la slide anterior, pero ahora las flechas de proceso se reemplazan por 4 cajas etiquetadas, cada una con un ejemplo concreto del semáforo:

| Capa | Caja | Ejemplo |
|------|------|---------|
| 1 Sabiduría | **Aplicado** (borde dorado) | Mejor freno y paro el carro |
| 2 Conocimiento | **Contexto** (borde verde) | Estoy rumbo a mi trabajo, el semáforo que tengo al frente ha cambiado a rojo |
| 3 Información | **Significado** (borde azul) | En la esquina de Av. La Mar y Av. Pardo el semáforo está en rojo a las 10 de la mañana |
| 4 Data | **Raw** (borde gris) | Rojo, 192.234.235.245, true, 10 |

Las descripciones de cada capa a la izquierda son las mismas de la slide 8.

## Slide 10

**Pirámide DIKW** — *Data, Information, Knowledge, and Wisdom*

Slide de transición, solo texto grande centrado:

> … tiene mucho sentido, sin embargo, **no es completamente aplicable** para análisis de datos

("no es completamente aplicable" resaltado en celeste.)

## Slide 11

**Pirámide DDPA** — *Data, Dataset, Pattern, and Action*
Actualización de Pirámide **DIKW** para **IA**

**Visual:** misma pirámide 3D de 4 capas (dorada, verde, azul, teal) con flechas-banner de proceso y una columna de texto explicativo a la derecha.

| # | Capa | Descripción | Flecha (proceso) | Texto a la derecha |
|---|------|-------------|------------------|---------------------|
| 1 | Acción | La decisión es hecha, la cual es informada por los patrones reconocidos | Análisis de riesgo (2→1) | Considerar la incertidumbre de los patrones reconocidos y llegar a una decisión |
| 2 | Patrones | Tendencias y relaciones interesantes y útiles dentro del dataset | Minería (3→2) | Aplicar minería de datos para encontrar patrones. |
| 3 | Dataset | Colección de datos seleccionados de recursos disponibles, limpios y organizados para el siguiente paso | Pre-procesamiento (4→3) | Seleccionar los datos relevantes y preparación para el siguiente paso. |
| 4 | Data | Todos los datos posibles desde todos los recursos de datos | — | — |

## Slide 12

Slide de énfasis, fondo azul con comillas:

**Pirámide para Análisis de Datos = DIKW + DDPA**

## Slide 13

**Pirámide DDVW** — *Data, Dataset, Visualization, and Wisdom*
Actualización de Pirámide **DIKW** para **Data Analytics**

**Visual:** misma pirámide 3D de 4 capas con flechas-banner de proceso.

| # | Capa | Descripción | Flecha (proceso) |
|---|------|-------------|------------------|
| 1 | Sabiduría | Encarnación del Conocimiento y apreciación del por qué. | Juzgar (2→1) |
| 2 | Visualización (resaltada en celeste) | La presentación comprensible de lo que se ha encontrado en el dataset | Analizar (3→2) |
| 3 | Dataset | Colección de datos seleccionados de recursos disponibles, limpios y organizados para el siguiente paso | Pre-procesamiento (4→3) |
| 4 | Data | Todos los datos posibles desde todos los recursos de datos | — |

## Slide 14

Cuando realizamos análisis de datos usamos la tecnología para:

1. Explorar el dataset
2. Testear la hipótesis
3. Reportar los findings relevantes.

**Recuerda:** *No es lo mismo hacer pre-procesamiento para ML que Data Analytics*

Foto decorativa a la izquierda (científica en laboratorio con gradilla de tubos), teñida de azul.

## Slide 15

Slide de pregunta, fondo azul con comillas:

**¿Cuál es la estructura de datos más universal?**

## Slide 16

**Una Tabla**

**Visual:** una tabla genérica anotada con llaves y etiquetas en celeste:
- Llave superior sobre todas las columnas → **Data Attributes**
- Llave izquierda sobre todas las filas → **Data Objects**
- Un óvalo alrededor de la celda (Fila n, Columna 2) → **Data Value**

Estructura de la tabla:

|  | Columna 1 | Columna 2 | . | . | . | Columna n |
|---|---|---|---|---|---|---|
| Fila 1 | xxx | xxx | . | . | . | xxx |
| Fila 2 | xxx | xxx | . | . | . | xxx |
| . | . | . | . | . | . | . |
| . | . | . | . | . | . | . |
| . | . | . | . | . | . | . |
| Fila n | xxx | xxx | . | . | . | xxx |

## Slide 17

**Data Objects**

- Data Objects también son llamados:
  - Data points,
  - Filas,
  - Records,
  - Ejemplos,
  - Tuplas, y más.
- La **definición** de *data objects* es la entidad, concepto, fenómeno o evento que todas las filas comparte.

**Visual:** ícono circular morado con una tarjeta/registro azul a la izquierda y una flecha amarilla apuntando hacia ella desde una pila de tres filas de colores (rosa, verde, amarillo) — metáfora de filas/records.

## Slide 18

**Data Attributes**

- Las columnas de una tabla son llamadas atributos.
- Los *data attributes* **representan características o rasgos** de los *data objects* en una tabla. Cada atributo describe algo sobre todos los *data objects*.
- Los sustantivos: atributo, dimensión, característica y variable a menudo se usan indistintamente en la literatura.
  - Dimensión: Comúnmente usado en data warehousing.
  - Característica (feature): Usado en la literatura de Machine Learning
  - Variable: Usado en estadística
  - Atributo: Usado en data mining, data analytics y base de datos.

**Visual:** ícono de una grilla/tabla azul de 5×5 con **una columna completa resaltada en naranja** — la columna = el atributo.

## Slide 19

**Data Values**

Para realizar un pre-procesamiento de datos exitoso necesitamos entender **los diferentes tipos** de *data values* desde dos perspectivas: **analítica y programación**.

El tipo de los valores de datos genera el tipo de atributo es por ello que se puede encontrar como Tipo de Datos o Tipo de Atributos en la literatura.

## Slide 20

Separador de sección.

**2. Tipos de Atributos — Percepción Analítica**

Imagen decorativa de mano robótica sobre globo digital.

## Slide 21

**Tipos de Atributos — Percepción Analítica**

**Visual:** árbol/diagrama de clasificación de izquierda a derecha, cajas conectadas por líneas celestes. Cajas grises = nodos intermedios; cajas celestes rellenas = hojas destacadas.

```
Data Attributes
├── Numérico
│   ├── Proporción
│   └── Intervalo
└── Categórico
    ├── Ordinal
    └── Nominal
        ├── Binario
        │   ├── Simétrico
        │   └── Asimétrico
        └── No Binario
```

## Slide 22

Separador.

**Nominal (Categórico)**

Foto decorativa de laboratorio teñida de azul.

## Slide 23

**Atributos Nominales**

- Nominal está relacionado a "nombres".
- Los valores de un atributo nominal son símbolos o nombres de cosas. Cada valor representa algún tipo de categoría, código o estado.
- Los valores de un atributo nominal no tienen ningún orden significativo. También se conocen como enumeraciones.

Banda superior decorativa (foto de equipo de trabajo + líneas punteadas).

## Slide 24

**Atributos Nominales**

Tres ejemplos en columnas, cada uno con una ilustración:

1. **Color de cabello** — ilustración de dos mujeres, una de cabello castaño largo y otra pelirroja corta.
   - Negro, Cafe, Rubio, Rojo, Gris, Blanco
2. **Estado civil** — ilustración de un portapapeles "STATUS" con checkboxes SINGLE / MARRIED (marcado) / WIDOWED / DIVORCED, junto a una pareja de novios y una torta de bodas.
   - Soltero, Casado, Viudo, Divorciado
3. **Diferentes presentaciones del atributo de género nominal** — tabla:

| Masculino | M | 0 | 1 | 1 |
|-----------|---|---|---|---|
| Femenino | F | 1 | 0 | 2 |

## Slide 25

**Tipos de Atributos — Percepción Analítica**

Mismo árbol de la slide 21, pero ahora resaltados en **verde** los nodos **Nominal**, **Binario**, **No Binario**, **Simétrico** y **Asimétrico** (la rama nominal completa), mientras Proporción, Intervalo y Ordinal siguen en celeste. Marca el tema que se está desarrollando.

## Slide 26

**Atributos Binarios**

- Un atributo binario es un atributo nominal con solo dos categorías o estados: 0 o 1, donde:
  - 0 normalmente significa que el atributo está ausente y
  - 1 significa que está presente.
- Los atributos binarios se denominan booleanos si los dos estados corresponden a verdadero y falso.

Banda superior decorativa.

## Slide 27

**Atributos Binarios**

Dos ejemplos lado a lado, cada uno con ilustración:

1. **Ilustración:** un cigarrillo encendido con humo gris.
   Dado el atributo fumador que describe un objeto paciente.
   - 1 indica que el paciente fuma,
   - 0 indica que el paciente no fuma.
2. **Ilustración:** sobre fondo turquesa, manos sosteniendo un portapapeles médico (cruz roja) y marcando casillas con check.
   Suponga que un paciente se somete a un examen médico que tiene dos resultados posibles. El atributo prueba médica es binario, donde un valor de
   - 1 significa que el resultado de la prueba para el paciente es positivo,
   - 0 significa que el resultado es negativo.

## Slide 28

**Atributos Binarios: Simétrico y Asimétrico**

- Un atributo **binario es simétrico** si ambos estados <u>son igualmente valiosos</u> y tienen el mismo peso; es decir, no hay preferencia sobre qué resultado debe codificarse como 0 o 1
  - Un ejemplo de ello podría ser el atributo <u>género</u> que tiene los estados masculino y femenino.
- Un atributo **binario es asimétrico** si los resultados de los estados <u>no son igualmente importantes</u>, como los resultados positivos y negativos de una prueba médica para el VIH.
  - Por convención, codificamos el resultado más importante, que suele ser el más raro, por 1 (p. ej., VIH positivo) y el otro por 0 (p. ej., VIH negativo).

## Slide 29

Separador.

**Ordinal (Categórico)**

Foto decorativa de laboratorio.

## Slide 30

**Atributos Ordinales**

- Un atributo **ordinal** es un atributo con valores posibles que tienen <u>un orden significativo</u> o <u>una clasificación</u> entre ellos, pero <u>no se conoce la magnitud</u> entre los valores sucesivos.
- Los atributos ordinales pueden contener mayor información que un atributo nominal.

Banda superior decorativa.

## Slide 31

**Atributos Ordinales**

**Visual:** ilustración de dos vasos de bebida con sorbete y crema, uno pequeño y uno grande, en degradado amarillo-naranja-rosa — muestra visualmente el orden de tamaño.

Suponga que el tamaño de la bebida corresponde al tamaño de las bebidas disponibles en un restaurante de comida rápida.

Este atributo nominal tiene tres valores posibles: **pequeño, mediano y grande.**

Los valores tienen una secuencia significativa (que corresponde al aumento del tamaño de la bebida); sin embargo, no podemos decir a partir de los valores ¿cuánto más grande es un medio que uno grande?.

## Slide 32

Slide solo con imagen (tomada de Google Images): diagrama de árbol **Categorical**.

```
Categorical (caja naranja)
├── Nominal (caja verde)
│   ├── fila de fotos: Pen | Pencil | Eraser
│   └── fila de fotos: Cow | Dog | Cat
└── Ordinal (caja azul)
    ├── fila de emojis: Excellent (cara riendo) | Good (cara sonriente) | Bad (cara triste)
    └── fila de emojis: Fantastic (pulgar arriba) | Okay (gesto OK) | Don't Like (pulgar abajo)
```

Contraste: en Nominal los ejemplos no tienen orden; en Ordinal sí (excelente > bueno > malo).

Pie: "Imagen tomada de Google Images".

## Slide 33

**Atributos Numéricos**

- Un atributo numérico es cuantitativo; es decir, es una cantidad medible, representada en valores enteros o reales. Los atributos numéricos pueden tener:
  - Una escala de intervalo o
  - Una escala de proporción.

Banda superior decorativa.

## Slide 34

Separador.

**Intervalo (Numérico)**

Foto decorativa de laboratorio.

## Slide 35

**Atributos Intervalo**

- Estos atributos contienen más información que **los atributos ordinales**, ya que permiten la comparación de intervalos entre *data objects*.
- Los datos de intervalo se miden a lo largo de una escala numérica que **tiene intervalos iguales entre valores adyacentes.**
- Al pasar de atributos ordinales a atributos de intervalo, también pasamos de símbolos y categorías a números (atributos categóricos a atributos numéricos). Con los números viene <u>la capacidad de saber cuánta diferencia</u> existe entre los *data objects*.

## Slide 36

**Atributos Intervalo**

**Visual:** infografía "INTERVAL DATA" (tomada de Google Images), fondo gris claro:

- Definición: *"Interval data is measured along a numerical scale that has equal intervals between adjacent values."*
- Etiqueta **Examples** (chip morado) con tres mini-gráficos:
  - **Temperature**: eje con 90°, 80°, 70° y una línea quebrada ascendente.
  - **IQ score**: curva tipo campana con el eje marcado 40 – 100 – 160, zona central sombreada en rosa.
  - **Income ranges**: curva suave con eje $19-29k, $30-39k, $40-49k.
- Chip rosa: **How is interval data analyzed?**
  - **Descriptive statistics**: Frequency distribution; mode, median, and mean; range, standard deviation, and variance
  - **Parametric statistical tests** (e.g. t-test, linear regression)

Pie: "Imagen tomada de Google Images".

## Slide 37

Separador.

**Proporción (Numérico)**

Foto decorativa de laboratorio.

## Slide 38

**Atributos Proporción (Ratio)**

- Los datos de proporción son un tipo de datos numéricos.
- Estos datos miden variables en una **escala continua**, con una distancia igual entre valores adyacentes. Si bien comparte estas características con los datos de intervalo, **una propiedad distintiva es que tiene un "true zero"**.
  - En otras palabras, no tienen valores negativos.

## Slide 39

**Atributos Proporción (Ratio)**

**Visual:** infografía "RATIO DATA" (tomada de Google Images), mismo formato que la de intervalo:

- Definición: *"Ratio data is measured along a numerical scale that has equal distances between adjacent values, and a true zero."*
- Chip **Examples** (rosa) con tres mini-gráficos de densidad:
  - **Weight in KG**: eje …50 – 70 – 90…
  - **Number of staff**: eje …10 – 30 – 50…
  - **Income in USD**: eje …20k – 40k – 60k…
- Chip verde: **How is ratio data analyzed?**
  - **Descriptive statistics**: Frequency distribution; mode, median, and mean; range, standard deviation, variance, and coefficient of variation
  - **Parametric statistical tests** (e.g. ANOVA, linear regression)

Diferencia clave frente a la slide 36: aquí se añade el **coeficiente de variación** en la estadística descriptiva y ANOVA en las pruebas paramétricas.

Pie: "Imagen tomada de Google Images".

## Slide 40

**Tipos: *Data Values***

**Visual:** tabla que cruza la perspectiva analítica con la de programación (celdas combinadas):

| Analytic Perspective | | Programming Perspective |
|---|---|---|
| Nominal attributes | Binary | Booleans or strings |
| Nominal attributes | Non-binary | Booleans or strings |
| Ordinal attributes | | Integers |
| Interval-scaled attributes | | Integers or floating points |
| Ration-scaled attributes *(sic, "Ratio")* | | Integers or floating points |

En la imagen original, "Booleans or strings" abarca las dos filas nominales (binary y non-binary), e "Integers or floating points" abarca las filas interval y ratio.

## Slide 41

**Conclusiones**

- ¿Qué es un dato y cuándo adquieren valor? ¿En qué consiste la pirámide DIKW? ¿Cuál es la versión actualizada de dicha pirámide en análisis de datos?
- ¿Cuáles son los dos tipos de atributos? ¿Cómo se clasifican a la vez, estos tipos de atributos?

Foto decorativa de un profesor escribiendo en pizarra frente a alumnos, teñida de azul.
