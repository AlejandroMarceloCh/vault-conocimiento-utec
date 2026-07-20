---
curso: DPD
titulo: U3_T1_Ingeniería de Características.pptx
slides: 69
fuente: U3_T1_Ingeniería de Características.pptx.pdf
---

# U3_T1_Ingeniería de Características.pptx

## Índice

| Sección | Subtemas |
|---|---|
| Introducción a la Ingeniería de características | Objetivo de la Sesión; Definición; Ciclo de ciencia de datos; Alcance y técnicas; Importancia; Beneficios |
| Tipos de datos y Procesamiento Básico (REPASO) | Dataset; Manejo de valores faltantes; Codificación de datos categóricos; Feature Scaling; Train–test split; Discretización |
| Creación de características | Interacción de características; Predicción aditiva vs. con interacción; Objetivos de la ingeniería de características |
| Selección de características | Concepto y objetivos; Métodos de Filtro; Métodos envolventes; Métodos embebidos |
| Algunas técnicas de procesamiento de características | Principal Component Analysis (PCA); Autoencoders |
| Conclusiones | Reflexión final sobre selección de características |

## Introducción a la Ingeniería de características

### Objetivo de la Sesión

Proporcionar una comprensión de la importancia de la ingeniería de características en el proceso de modelado de datos y repasar técnicas prácticas para crear y seleccionar características efectivas.

**Figura:** Slide con fondo cian-azul brillante. En el lado izquierdo, el título «Objetivo de la Sesión» en texto blanco grande y negrita. Debajo, el párrafo del objetivo en texto blanco. En el lado derecho, un patrón geométrico grande de formas entrelazadas con contorno blanco (picos estilizados o marcos en zigzag) que enmarcan fragmentos de fotografías del campus UTEC de concreto. Un fragmento en la esquina inferior derecha muestra un letrero con icono de información «i» y el texto «LA NUEVA INGENIERÍA».

(slides 2)

### Definición

La ingeniería de características es el proceso de transformar datos en bruto en características que mejor representan el problema subyacente a los modelos, mejorando así su rendimiento.

Puede considerarse como el arte de seleccionar las características importantes.

**Figura:** En el lado izquierdo, dos oraciones en tipografía gris oscura sans-serif; las frases clave «de transformar datos en bruto en características que mejor representan» y «arte» aparecen resaltadas en color cian brillante. Uno de los marcos superiores tiene un filtro de color cian. Otros marcos muestran pilares, vigas y corredores de concreto en color natural. En la sección inferior derecha, un mural en pared con texto vertical que incluye los fragmentos «NN», «GEVEN», «NIECI» y «RABLE».

(slides 5)

### Ciclo de ciencia de datos

**Figura:** Cinco cajas rectangulares redondeadas de color rojo están dispuestas en un pentágono circular, conectadas por flechas curvas grises oscuras que indican flujo en sentido horario. Un recuadro rectangular de borde azul claro (cian) resalta las dos primeras etapas del ciclo. Las etapas, en orden horario desde la parte superior, son: (1) «Problem Definition» en la parte superior — dentro del recuadro azul claro; (2) «Data Investigation & Cleaning» en la parte superior derecha — también dentro del recuadro azul claro; (3) «Minimal Viable Product» en la parte inferior derecha; (4) «Deployment & Enhancement» en la parte inferior izquierda; (5) «Data Science Ops» en el centro-izquierda, completando el ciclo de vuelta a «Problem Definition».

(slides 6)

### Alcance y técnicas

La Ingeniería de Características engloba diversas técnicas de ciencia de datos, como:

• Selección de características relevantes,
• Manejo de datos faltantes,
• Codificación de datos
• Normalización,
• Creación de características.

**Figura:** En la parte inferior de la slide, un diagrama de flujo horizontal que ilustra el flujo de trabajo de procesamiento de datos. **Fuentes de datos (extremo izquierdo):** tres nodos circulares representan fuentes distintas — «Source 1» (azul), «Source 2» (verde) y «Source n» (rojo). Flechas desde estas fuentes apuntan hacia la siguiente etapa; debajo de las flechas, la etiqueta «Select and merge». **Raw Data:** las flechas conducen a una caja rectangular de color rojo claro etiquetada «Raw Data». **Clean and transform:** entre «Raw Data» y la siguiente caja, un recuadro redondeado rojo resalta la transición; una flecha apunta al texto «Clean and transform». **Features:** una flecha conduce a una caja rectangular azul etiquetada «Features». **Modeling:** desde «Features», una flecha apunta a una caja rectangular verde etiquetada «Modeling» que contiene un icono de dos engranajes entrelazados. **Insights:** la flecha final conduce a una caja rectangular naranja etiquetada «Insights».

(slides 7)

### Importancia

¿Sabes qué es lo que consume la mayor cantidad de tiempo y esfuerzo en un flujo de Machine Learning?

https://www.forbes.com/sites/gilpress/2016/03/23/data-preparation-most-time-consuming-least-enjoyable-data-science-task-survey-says/

**Figura:** La slide presenta dos gráficos de dona (donut charts) con datos estadísticos sobre tareas de ciencia de datos, con fuente en Forbes.

**Gráfico 1 — «What data scientists spend the most time doing»:** La mayor parte del tiempo de un científico de datos se dedica a preparación de datos.
- Cleaning and organizing data: **60%** (sección verde grande)
- Collecting data sets: **19%** (verde azulado/teal)
- Mining data for patterns: **9%** (amarillo)
- Other: **5%** (rosa)
- Refining algorithms: **4%** (naranja)
- Building training sets: **3%** (magenta)

**Gráfico 2 — «What's the least enjoyable part of data science?»:** La tarea que más tiempo consume también es considerada la menos disfrutable.
- Cleaning and organizing data: **57%** (verde)
- Collecting data sets: **21%** (verde azulado/teal)
- Building training sets: **10%** (magenta)
- Other: **5%** (rosa)
- Refining algorithms: **4%** (naranja)
- Mining data for patterns: **3%** (amarillo)

En la parte inferior, la URL de la fuente.

(slides 8)

### Beneficios

Beneficios de la Ingeniería de Características

Una Ingeniería de Características efectiva implica:

• Mayor eficiencia del modelo,
• Algoritmos más sencillos que se ajustan a los datos,
• Facilidad para que los algoritmos detecten patrones en los datos,
• Mayor flexibilidad de las características

Entonces, ¿por dónde empezar?

**Figura:** El título «Beneficios de la Ingeniería de Características» aparece en azul claro en la parte superior izquierda. Debajo, la frase introductoria «Una Ingeniería de Características efectiva implica:» en gris oscuro, seguida de cuatro viñetas en gris oscuro.

(slides 9)

## Tipos de datos y Procesamiento Básico (REPASO)

### Dataset

Dataset:

| | Name | Country | Age | Salary | Cars | Purchased |
|---|---|---|---|---|---|---|
| 0 | Mohan | India | 44.0 | 72000.0 | 2.0 | No |
| 1 | Raquel | Spain | 27.0 | 48000.0 | NaN | Yes |
| 2 | Ilsa | Belgium | 30.0 | 54000.0 | NaN | No |
| 3 | Victor | Spain | 38.0 | 61000.0 | NaN | No |
| 4 | Leon | Belgium | 40.0 | NaN | NaN | Yes |
| 5 | Mimi | India | 35.0 | 58000.0 | NaN | Yes |
| 6 | Anna | Spain | NaN | 52000.0 | NaN | No |
| 7 | Maria | India | 48.0 | 79000.0 | 2.0 | Yes |
| 8 | Natalie | Belgium | 50.0 | 83000.0 | 3.0 | No |
| 9 | Ayshik | India | 37.0 | 67000.0 | 1.0 | Yes |
| 10 | Sourav | India | NaN | 56000.0 | NaN | Yes |
| 11 | Will | Belgium | 42.0 | 76000.0 | NaN | Yes |
| 12 | Smith | Spain | NaN | 87000.0 | NaN | Yes |
| 13 | Nita | India | 34.0 | NaN | 1.0 | No |
| 14 | Anupriya | India | NaN | 45798.0 | 2.0 | No |
| 15 | Brie | Spain | 24.0 | 28000.0 | NaN | No |
| 16 | Monica | Spain | 32.0 | 32000.0 | NaN | Yes |
| 17 | Sheela | India | 28.0 | NaN | NaN | No |
| 18 | Anna | Belgium | 39.0 | 70000.0 | NaN | No |

```python
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
print(x)
```

```
[['India' 44.0 72000.0 2.0]
 ['Spain' 27.0 48000.0 nan]
 ['Belgium' 30.0 54000.0 nan]
 ['Spain' 38.0 61000.0 nan]
 ['Belgium' 40.0 nan nan]
 ['India' 35.0 58000.0 nan]
 ['Spain' nan 52000.0 nan]
 ['India' 48.0 79000.0 2.0]
 ['Belgium' 50.0 83000.0 3.0]
 ['India' 37.0 67000.0 1.0]
 ['India' nan 56000.0 nan]
 ['Belgium' 42.0 76000.0 nan]
 ['Spain' nan 87000.0 nan]
 ['India' 34.0 nan 1.0]
 ['India' nan 45798.0 2.0]
 ['Spain' 24.0 28000.0 nan]
 ['Spain' 32.0 32000.0 nan]
 ['India' 28.0 nan nan]
 ['Belgium' 39.0 70000.0 nan]]
```

```python
print(y)
```

```
['No' 'Yes' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'No' 'Yes' 'Yes' 'Yes' 'Yes' 'No' 'No' 'No' 'Yes' 'No' 'No']
```

**Figura:** En el lado izquierdo, la tabla «Dataset:» con 19 filas (índice 0 a 18) y 6 columnas (Name, Country, Age, Salary, Cars, Purchased), con valores numéricos decimales y celdas faltantes representadas como NaN. En el lado derecho, bloques de código Python que separan el dataset en variables de características (`x`, columnas 1 a penúltima) y variable objetivo (`y`, última columna), con sus respectivas salidas impresas debajo de cada bloque.

(slides 11)

### Manejo de valores faltantes

#### Tipos de valores faltantes

Manejo de valores faltantes

• No todos los valores faltantes son iguales
    • Faltante no al azar - Missing not at random (MNAR)
    • Faltante al azar - Missing at random (MAR)
    • Faltante completamente al azar - Missing completely at random (MCAR)

**Figura:** El título «Manejo» aparece en negrita negra sans-serif y «de valores faltantes» en azul claro más delgado. Una viñeta principal indica «No todos los valores faltantes son iguales», seguida de tres sub-viñetas con las categorías MNAR, MAR y MCAR en español e inglés. En la esquina inferior derecha, un emoji con cara amarilla, ojos en espiral y boca ligeramente hacia abajo, transmitiendo confusión o mareo.

#### Faltante no al azar (MNAR)

Manejo de valores faltantes
Faltante no al azar: cuando un valor falta debido al valor en sí

| ID | Age | Gender | Annual income | Marital status | Number of children | Job | Buy? |
|---|---|---|---|---|---|---|---|
| 1 | | A | 150,000 | | 1 | Engineer | No |
| 2 | 27 | B | 50,000 | | | Teacher | No |
| 3 | | A | 100,000 | Married | 2 | | Yes |
| 4 | 40 | B | ($350,000?) | | 2 | Engineer | Yes |
| 5 | 35 | B | ($350,000?) | Single | 0 | Doctor | Yes |
| 6 | | A | 50,000 | | 0 | Teacher | No |
| 7 | 33 | B | 60,000 | Single | | Teacher | No |
| 8 | 20 | B | 10,000 | | | Student | No |

**Figura:** Slide con título «Manejo de valores faltantes» (Manejo en negrita negra, «de valores faltantes» en azul claro) y subtítulo «Faltante no al azar: cuando un valor falta debido al valor en sí». En el centro, una tabla de 8 filas de datos con 8 columnas (ID, Age, Gender, Annual income, Marital status, Number of children, Job, Buy?) con múltiples celdas vacías que representan valores faltantes. Las celdas de «Annual income» para los IDs 4 y 5 están resaltadas en azul claro y contienen el texto «($350,000?)» entre paréntesis con signo de interrogación, ilustrando el concepto de dato faltante no al azar (MNAR) donde el ingreso alto podría no haberse revelado. En la esquina inferior derecha, el número de slide «13».

#### Faltante al azar (MAR)

Manejo de valores faltantes
Faltante al azar: cuando un valor falta debido a otra variable observada

| ID | Age | Gender | Annual income | Marital status | Number of children | Job | Buy? |
|---|---|---|---|---|---|---|---|
| 1 | | A | 150,000 | | 1 | Engineer | No |
| 2 | 27 | B | 50,000 | | | Teacher | No |
| 3 | | A | 100,000 | Married | 2 | | Yes |
| 4 | 40 | B | | | 2 | Engineer | Yes |
| 5 | 35 | B | | Single | 0 | Doctor | Yes |
| 6 | | A | 50,000 | | 0 | Teacher | No |
| 7 | 33 | B | 60,000 | Single | | Teacher | No |
| 8 | 20 | B | 10,000 | | | Student | No |

**Figura:** Slide con título «Manejo de valores faltantes» y subtítulo «Faltante al azar: cuando un valor falta debido a otra variable observada». En el centro, la misma tabla de 8 filas y 8 columnas. Las celdas de «Age» faltantes para los IDs 1, 3 y 6 están resaltadas en azul claro. Las celdas de «Gender» correspondientes a esas mismas filas contienen el valor «A» resaltado en rosa brillante, visualizando que la edad falta porque el género es «A». Otros valores faltantes sin resaltar aparecen en «Annual income» (IDs 4 y 5), «Marital status» (IDs 1, 2, 4, 6, 8), «Number of children» (IDs 2, 7, 8) y «Job» (ID 3). En la esquina inferior derecha, el número de slide «14».

#### Faltante completamente al azar (MCAR)

Manejo de valores faltantes
Faltante completamente al azar: no hay un patrón que determine cuáles
valores faltan

| ID | Age | Gender | Annual income | Marital status | Number of children | Job | Buy? |
|---|---|---|---|---|---|---|---|
| 1 | | A | 150,000 | | 1 | Engineer | No |
| 2 | 27 | B | 50,000 | | | Teacher | No |
| 3 | | A | 100,000 | Married | 2 | | Yes |
| 4 | 40 | B | | | 2 | Engineer | Yes |
| 5 | 35 | B | | Single | 0 | Doctor | Yes |
| 6 | | A | 50,000 | | 0 | Teacher | No |
| 7 | 33 | B | 60,000 | Single | | Teacher | No |
| 8 | 20 | B | 10,000 | | | Student | No |

**Figura:** Slide con título «Manejo de valores faltantes» (Manejo en negrita negra, «de valores faltantes» en azul cursiva) y subtítulo «Faltante completamente al azar: no hay un patrón que determine cuáles valores faltan». En el centro, la tabla de ejemplo con 8 filas y 8 columnas mostrando valores faltantes distribuidos en varias columnas (Age, Annual income, Marital status, Number of children, Job) sin un patrón discernible. La celda de «Job» para el ID 3 está resaltada en azul claro.

#### Estrategias: eliminación e imputación

Manejo de valores faltantes

• Eliminación: eliminar datos con entradas faltantes
• Imputación: rellenar campos faltantes con ciertos valores

Muchas personas prefieren la
eliminación no porque sea mejor,
sino porque es más fácil de hacer

**Figura:** El título «Manejo» en negrita negra y «de valores faltantes» en azul claro sans-serif. Dos viñetas principales: «Eliminación» (eliminar datos con entradas faltantes) e «Imputación» (rellenar campos faltantes con ciertos valores). En la parte inferior izquierda, un párrafo en tipografía rosa vibrante: «Muchas personas prefieren la eliminación no porque sea mejor, sino porque es más fácil de hacer».

#### Eliminación de columnas

Manejo de valores faltantes

• Eliminación

    •   Eliminación de columnas: eliminar columnas con demasiadas
        entradas faltantes
        •   drawbacks – incluso si falta la mitad de los valores, los datos
            restantes aún contienen información potencialmente útil para
            predicciones

        •   por ejemplo, incluso si falta más de la mitad de la columna de 'Estado
            civil', el estado civil sigue estando altamente correlacionado con la
            compra de viviendas

    •   Row deletion

Marital status
Married
Single
Single

**Figura:** Slide con título «Manejo de valores faltantes» (Manejo en negrita negra, «de valores faltantes» en azul claro). Viñeta principal «Eliminación» con sub-viñeta «Eliminación de columnas: eliminar columnas con demasiadas entradas faltantes», seguida de «drawbacks» sobre la información útil que permanece aunque falte la mitad de los valores, y un ejemplo sobre la columna «Estado civil» correlacionada con la compra de viviendas. Debajo, una segunda sub-viñeta «Row deletion» en texto gris claro atenuado. En el lado derecho, una lista vertical que representa entradas de datos de una característica: encabezado «Marital status», seguido de «Married», «Single», «Single». En la esquina inferior derecha, el número de slide «17».

Manejo de Datos Faltantes:

1.   Eliminar Columnas: Consiste en eliminar columnas que
     aparentemente no contribuyen al resultado previsto
     porque contienen muchas entradas vacías.

Podemos establecer un cierto valor umbral, digamos 70%
o 80%, y si el número de valores nulos supera ese umbral,
es posible que queramos eliminar esa columna en
particular de nuestro conjunto de datos de
entrenamiento.

BENEFICIOS

• Reducción de Dimensionalidad
• Reduce la complejidad computacional

DESVENTAJAS

• Causa pérdida de información.

```python
dataset.isnull().sum()
```

```
Name         0
Country      0
Age          4
Salary       3
Cars        13
Purchased    0
dtype: int64
```

```python
threshold=0.7
dataset = dataset[dataset.columns[dataset.isnull().mean() < threshold]]
print(dataset)
```

| | Name | Country | Age | Salary | Purchased |
|---|---|---|---|---|---|
| 0 | Mohan | India | 44.0 | 72000.0 | No |
| 1 | Raquel | Spain | 27.0 | 48000.0 | Yes |
| 2 | Ilsa | Belgium | 30.0 | 54000.0 | No |
| 3 | Victor | Spain | 38.0 | 61000.0 | No |
| 4 | Leon | Belgium | 40.0 | NaN | Yes |
| 5 | Mimi | India | 35.0 | 58000.0 | Yes |
| 6 | Anna | Spain | NaN | 52000.0 | No |
| 7 | Maria | India | 48.0 | 79000.0 | Yes |
| 8 | Natalie | Belgium | 50.0 | 83000.0 | No |
| 9 | Ayshik | India | 37.0 | 67000.0 | Yes |

**Figura:** Slide con título «Manejo de Datos Faltantes:». En la parte superior izquierda, un bloque de código Python `dataset.isnull().sum()` con su salida mostrando conteo de nulos por columna (Name: 0, Country: 0, Age: 4, Salary: 3, Cars: 13, Purchased: 0). En el centro, texto explicativo sobre la técnica «Eliminar Columnas» con umbral del 70% u 80%. En la parte inferior izquierda, listas de BENEFICIOS (Reducción de Dimensionalidad, Reduce la complejidad computacional) y DESVENTAJAS (Causa pérdida de información). En la parte inferior derecha, código Python con `threshold=0.7` que filtra columnas cuyo porcentaje de nulos es menor al umbral, seguido de la tabla resultante sin la columna «Cars» (que tenía 13 nulos, superando el 70%), conservando Name, Country, Age, Salary y Purchased con 10 filas (índice 0–9) y algunos valores NaN restantes en Age y Salary.

#### Eliminación de filas

Manejo de valores faltantes

• Eliminación
   •   Eliminación de Columnas
   •   Eliminación de Filas

**Figura:** El título «Manejo» en negrita negra y «de valores faltantes» en azul claro cursiva. Viñeta principal «Eliminación» con dos sub-viñetas: «Eliminación de Columnas» en texto gris claro atenuado (como tema ya cubierto) y «Eliminación de Filas» en gris oscuro (tema actual).

Manejo de valores faltantes

• Eliminación de filas
      •   Bueno para: datos faltantes completamente random (MCAR) y que
          haya pocos valores faltantes.

| ID | Age | Gender | Annual income | Marital status | Number of children | Job | Buy? |
|---|---|---|---|---|---|---|---|
| 1 | 39 | A | 150,000 | Married | 1 | Engineer | No |
| 2 | 27 | B | 50,000 | Single | 0 | Teacher | No |
| 3 | | A | 100,000 | Married | 2 | | Yes |
| 4 | 40 | B | 75,000 | Married | 2 | Engineer | Yes |
| 5 | 35 | B | 35,000 | Single | 0 | Doctor | Yes |
| 6 | 32 | A | 50,000 | Married | 0 | Teacher | No |
| 7 | 33 | B | 60,000 | Single | 2 | Teacher | No |
| 8 | 20 | B | 10,000 | Single | 1 | Student | No |

**Figura:** Slide con título «Manejo de valores faltantes» (Manejo en negrita negra, «de valores faltantes» en azul claro). Viñeta «Eliminación de filas» con sub-viñeta indicando que es bueno para datos faltantes completamente random (MCAR) y cuando hay pocos valores faltantes. Debajo, una tabla de 8 filas y 8 columnas con datos completos excepto la fila 3, que tiene valores faltantes (celdas vacías) en «Age» y «Job». La fila 3 completa está resaltada con fondo rojo, indicando que esa fila entera sería eliminada al aplicar la técnica de eliminación de filas. En la esquina inferior derecha, el número de slide «20».

• Eliminación de filas
      •   Malo cuando hay muchas instancias que tienen campos faltantes

| ID | Age | Gender | Annual income | Marital status | Number of children | Job | Buy? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | A | 150,000 | | 1 | Engineer | No |
| 2 | 27 | B | 50,000 | | | Teacher | No |
| 3 | | A | 100,000 | Married | 2 | | Yes |
| 4 | 40 | B | | | 2 | Engineer | Yes |
| 5 | 35 | B | | Single | 0 | Doctor | Yes |
| 6 | | A | 50,000 | | 0 | Teacher | No |
| 7 | 33 | B | 60,000 | Single | | Teacher | No |
| 8 | 20 | B | 10,000 | | | Student | No |

**Figura:** Tabla de dataset con 8 filas (ID 1 a 8) y 8 columnas. El área de datos tiene fondo rojo claro. Varias celdas están vacías, representando valores faltantes en Age, Annual income, Marital status, Number of children y Job. Número de slide «21» en la esquina inferior derecha.

• Eliminación de filas
      •   Malo para: valores faltantes que no son random
      •   Falta de información es de por si información

| ID | Age | Gender | Annual income | Marital status | Number of children | Job | Buy? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | A | 150,000 | | 1 | Engineer | No |
| 2 | 27 | B | 50,000 | | | Teacher | No |
| 3 | | A | 100,000 | Married | 2 | | Yes |
| 4 | 40 | B | ($350,000?) | | 2 | Engineer | Yes |
| 5 | 35 | B | ($350,000?) | Single | 0 | Doctor | Yes |
| 6 | | A | 50,000 | | 0 | Teacher | No |
| 7 | 33 | B | 60,000 | Single | | Teacher | No |
| 8 | 20 | B | 10,000 | | | Student | No |

**Figura:** Misma tabla de dataset de 8 filas. Las celdas de Annual income para los IDs 4 y 5 aparecen resaltadas en azul claro con el texto «($350,000?)», sugiriendo valores cuestionables o atípicos. El resto de celdas vacías representan valores faltantes.

• Eliminación de filas
      •   Malo para: datos faltantes random (MAR)
      •   Puede sesgar los datos potencialmente: hemos eliminado accidentalmente todos los ejemplos con el género 'A'

| ID | Age | Gender | Annual income | Marital status | Number of children | Job | Buy? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | A | 150,000 | | 1 | Engineer | No |
| 2 | 27 | B | 50,000 | | | Teacher | No |
| 3 | | A | 100,000 | Married | 2 | | Yes |
| 4 | 40 | B | | | 2 | Engineer | Yes |
| 5 | 35 | B | | Single | 0 | Doctor | Yes |
| 6 | | A | 50,000 | | 0 | Teacher | No |
| 7 | 33 | B | 60,000 | Single | | Teacher | No |
| 8 | 20 | B | 10,000 | | | Student | No |

**Figura:** Misma tabla de dataset de 8 filas. Las filas con ID 1, 3 y 6 (las únicas con Gender = 'A') están resaltadas en rojo claro, ilustrando que al eliminar filas con valores faltantes (por ejemplo en Age) se perderían todos los registros del género 'A'. Número de slide «23» en la esquina inferior derecha.

(slides 12–23)

#### Imputación

• Llenar los campos faltantes con algunos valores
   • Defaults
        •   Ejemplo: 0.
   •   Medidas estadísticas – promedio, mediana, moda
        •   por ejemplo, si falta el valor de la temperatura de un día en
            julio, rellenarlo con la temperatura mediana de julio

¡Evita rellenar valores faltantes con
valores posibles!

**Figura:** Slide con título «Imputación» en azul claro. Texto en negro con viñetas anidadas para Defaults y Medidas estadísticas. Advertencia en rojo en la parte inferior: «¡Evita rellenar valores faltantes con valores posibles!». Número de slide «24» en la esquina inferior derecha.

2. Imputar Valores Faltantes para Variables Continuas: Consiste
en completar los valores faltantes con algunos valores
calculados a partir de las columnas de características
correspondientes..

Podemos usar varias estrategias para imputar los valores
de variables continuas. Algunas de estas estrategias son
imputar con la Media, Mediana o Moda.

• Media (mean)
• Mediana (median)
• Moda (most frequent)

```python
SimpleImputer(missing_values=np.nan, strategy="mean")
.fit_transform(X[:, 1:3])
```

['Belgium' 42.0 76000.0]

**Figura:** Tres histogramas comparativos. Izquierda: «Original Distribution with Missing Values», distribución aproximadamente normal en azul oscuro entre -4 y 10, Mean = 2.08, Std = 1.95, frecuencia máxima ~175. Arriba a la derecha: «Mean Imputation» marcado con X roja, barras naranjas con pico masivo en 2.08, Mean = 2.08, Std = 1.76, frecuencia máxima ~800. Abajo a la derecha: «Zero Imputation» marcado con X roja, barras naranjas con pico masivo en 0, Mean = 1.66, Std = 1.93, frecuencia máxima ~700. A la derecha, lista de estrategias (Media, Mediana, Moda) y fragmento de código con SimpleImputer. En la parte inferior, fila de datos de ejemplo.

#### KNN Imputation

•   Tiempo de ejecución elevado para la imputación,
    especialmente para conjuntos de datos de alta dimensión.
•   Problemas con el cálculo de distancia en caso de
    características categóricas no faltantes.
•   Requiere escalado de características, etc.

**Figura:** Cuatro histogramas en la parte izquierda. «Original Distribution with Missing Values»: distribución normal en azul, Mean = 2.08, Std = 1.95. «Mean Imputation» (X roja): pico en la media, Mean = 2.08, Std = 1.76. «Zero Imputation» (X roja): pico en cero, Mean = 1.66, Std = 1.93. «kNN Imputation» (checkmark verde): distribución naranja similar a la original, Mean = 2.07, Std = 1.90.

**Figura:** Diagrama del algoritmo kNN Imputation en el centro. Leyenda: cuadrado con borde rojo = valor faltante; cuadrado con borde azul = valor presente en la misma característica; cuadrado con borde verde = valor presente en otras características. Grid de datos con filas 0–4 y columnas A, B, C. Paso 1: seleccionar fila con valor faltante (fila 1, columna C vacía con borde rojo). Paso 2: encontrar k=2 vecinos más cercanos usando características presentes (filas 0 y 4). Paso 3: imputar el valor faltante como promedio de los vecinos en esa característica: Red Square = (Blue Square from Row 0 + Blue Square from Row 4) / 2. Paso 4: repetir para todas las filas con valores faltantes.

#### Missforest Imputation

https://pypi.org/project/missingpy/

**Figura:** Cuatro histogramas en la parte izquierda. «Original Distribution with Missing Values»: Mean = 2.08, Std = 1.95. «Mean Imputation» (X roja): Mean = 2.08, Std = 1.76. «Zero Imputation» (X roja): Mean = 1.66, Std = 1.93. «MissForest Imputation» (checkmark verde): Mean = 2.11, Std = 1.89, distribución similar a la original sin picos artificiales.

**Figura:** Diagrama del algoritmo MissForest a la derecha. Grid con columnas A, B, C y filas 0–4. Leyenda: borde rojo = valor faltante; borde verde = dato presente en otras características; borde azul = dato presente en la característica actual. Paso 1: «Make an initial guess for missing values» (Mean, Median, Mode, etc.) — celdas faltantes rellenadas con patrón diagonal morado. Paso 2: «Train Random Forest with feature 'C' as dependent variable» — caja «Random Forest Model» con seis árboles de decisión; columnas A y B como predictores. Paso 3: «Predict feature 'C' for originally missing values» — celdas con patrón diagonal marrón. Paso 4: «Repeat using the imputed dataset until max iterations or convergence» — flecha de retroalimentación al Paso 2. URL en la parte inferior izquierda.

https://pypi.org/project/missingpy/

**Figura:** Cuatro histogramas en la parte izquierda (mismos que slide 27): Original (Mean = 2.08, Std = 1.95), Mean Imputation (X roja, Std = 1.76), Zero Imputation (X roja, Mean = 1.66), MissForest Imputation (checkmark verde, Mean = 2.11, Std = 1.89).

**Figura:** Diagrama del algoritmo MissForest con múltiples características faltantes. Grid titulado «Data with multiple missing features» con columnas A, B, C, D. Paso 1: «Make an initial guess for missing values» (Mean, Median, Mode, etc.). Paso 2: «Impute in ascending order of missingness» — imputar primero las características con menos valores faltantes. Paso 2.1: «Impute Feature 'C' using Random Forest». Paso 2.2: «Impute Feature 'D' using Random Forest». Flecha de retroalimentación: «Repeat using the imputed dataset until max iterations or convergence». URL en la parte inferior izquierda.

(slides 24–28)

#### Variables categóricas

3. Variables categóricas:

3.1 Eliminar filas que contengan datos faltantes:

```python
dataset.isnull().sum()
```

| Columna | Valores nulos |
| --- | --- |
| Name | 0 |
| Country | 0 |
| Age | 4 |
| Salary | 3 |
| Cars | 13 |
| Purchased | 0 |
| dtype | int64 |

| | Name | Country | Gender | Age | Salary | Purchased |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Mohan | India | F | 44.0 | 72000.0 | No |
| 1 | Raquel | Spain | M | 27.0 | 48000.0 | Yes |
| 2 | Ilsa | Belgium | M | 30.0 | 54000.0 | No |
| 3 | Victor | Spain | M | 38.0 | 61000.0 | No |
| 4 | Leon | Belgium | NaN | 40.0 | NaN | Yes |
| 5 | Mimi | India | F | 35.0 | 58000.0 | Yes |
| 6 | Anna | Spain | F | NaN | 52000.0 | No |
| 7 | Maria | India | NaN | 48.0 | 79000.0 | Yes |
| 8 | Natalie | Belgium | NaN | 50.0 | 83000.0 | No |
| 9 | Ayshik | India | M | 37.0 | 67000.0 | Yes |

```python
dataset.dropna(axis=0, subset=['Gender'], inplace=True)
dataset.head(10)
```

**Figura:** Slide dividida en secciones. Arriba a la izquierda, código `dataset.isnull().sum()` con su salida mostrando conteo de nulos por columna. Centro-derecha, tabla con las primeras 10 filas del dataset con valores NaN en Gender (filas 4, 7, 8), Age (fila 6) y Salary (fila 4). Abajo, sección «3.1 Eliminar filas que contengan datos faltantes» con código `dropna`.

3.2 Asignar nueva categoría:

```python
dataset['Gender']= dataset['Gender'].fillna('U')
dataset.head(10)
```

| | Name | Country | Gender | Age | Salary | Cars | Purchased |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Mohan | India | F | 44.0 | 72000.0 | 2.0 | No |
| 1 | Raquel | Spain | M | 27.0 | 48000.0 | NaN | Yes |
| 2 | Ilsa | Belgium | M | 30.0 | 54000.0 | NaN | No |
| 3 | Victor | Spain | M | 38.0 | 61000.0 | NaN | No |
| 4 | Leon | Belgium | U | 40.0 | NaN | NaN | Yes |
| 5 | Mimi | India | F | 35.0 | 58000.0 | NaN | Yes |
| 6 | Anna | Spain | F | NaN | 52000.0 | NaN | No |
| 7 | Maria | India | U | 48.0 | 79000.0 | 2.0 | Yes |
| 8 | Natalie | Belgium | U | 50.0 | 83000.0 | 3.0 | No |
| 9 | Ayshik | India | M | 37.0 | 67000.0 | 1.0 | Yes |

**Figura:** Lado izquierdo, tabla inicial con `dataset.isnull().sum()` y dataset con NaN en Gender. Lado derecho, sección «3.2 Asignar nueva categoría» con código `fillna('U')` y tabla resultante donde Gender NaN se reemplaza por 'U' en filas 4, 7 y 8. Aparece columna adicional «Cars».

3.3 Valor más frecuente:

```python
dataset['Gender']= dataset['Gender'].fillna(dataset['Gender'].mode()[0])
dataset.head(10)
```

| | Name | Country | Gender | Age | Salary | Cars | Purchased |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Mohan | India | F | 44.0 | 72000.0 | 2.0 | No |
| 1 | Raquel | Spain | M | 27.0 | 48000.0 | NaN | Yes |
| 2 | Ilsa | Belgium | M | 30.0 | 54000.0 | NaN | No |
| 3 | Victor | Spain | M | 38.0 | 61000.0 | NaN | No |
| 4 | Leon | Belgium | M | 40.0 | 45798.0 | NaN | Yes |
| 5 | Mimi | India | F | 35.0 | 58000.0 | NaN | Yes |
| 6 | Anna | Spain | F | 28.0 | 52000.0 | NaN | No |
| 7 | Maria | India | M | 48.0 | 79000.0 | 2.0 | Yes |
| 8 | Natalie | Belgium | M | 50.0 | 83000.0 | 3.0 | No |
| 9 | Ayshik | India | M | 37.0 | 67000.0 | 1.0 | Yes |

**Figura:** Lado izquierdo, tabla inicial con `dataset.isnull().sum()` y dataset con NaN en Gender (filas 4, 7, 8). Lado derecho, sección «3.3 Valor más frecuente» con código `fillna(dataset['Gender'].mode()[0])` y tabla resultante donde Gender NaN se reemplaza por 'M'. También se observan valores imputados en Age (fila 6: 28.0) y Salary (fila 4: 45798.0).

(slides 29–31)

### Codificación de datos categóricos

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)
```

Datos de entrada:

```
[['India' 44.0 72000.0 2.0]
 ['Spain' 27.0 48000.0 nan]
 ['Belgium' 30.0 54000.0 nan]
 ['Spain' 38.0 61000.0 nan]
 ['Belgium' 40.0 nan nan]
 ['India' 35.0 58000.0 nan]
 ['Spain' nan 52000.0 nan]
 ['India' 48.0 79000.0 2.0]
 ['Belgium' 50.0 83000.0 3.0]
 ['India' 37.0 67000.0 1.0]
 ['India' nan 56000.0 nan]
 ['Belgium' 42.0 76000.0 nan]
 ['Spain' nan 87000.0 nan]
 ['India' 34.0 nan 1.0]
 ['India' nan 45798.0 2.0]
 ['Spain' 24.0 28000.0 nan]
 ['Spain' 32.0 32000.0 nan]
 ['India' 28.0 nan nan]
 ['Belgium' 39.0 70000.0 nan]]
```

Mapeo conceptual:
- India: 0.0 1.0 0.0
- Spain: 0.0 0.0 1.0
- Belgium: 1.0 0.0 0.0

Salida:

```
[[0.0 0.0 1.0 0.0 44.0 72000.0]
 [0.0 0.0 0.0 1.0 27.0 48000.0]
 [1.0 0.0 0.0 0.0 30.0 54000.0]
 ...
 [0.0 1.0 0.0 0.0 42.0 76000.0]
 ...
 [0.0 0.0 0.0 0.0 36.53333333333333 56000.0]
 ...
 [1.0 0.0 0.0 0.0 39.0 70000.0]]
```

**Figura:** Lado izquierdo, dataset como lista de listas con 19 filas y 4 columnas (Country, Age, Salary, valor numérico), con varios `nan`. Centro-derecha, caja con mapeo One-Hot de India, Spain y Belgium a vectores binarios. Código Python con ColumnTransformer y OneHotEncoder para la columna 0 con `remainder='passthrough'`. Abajo, array resultante con 4 columnas one-hot (por las 4 categorías únicas incluyendo el typo 'Beligum') seguidas de columnas numéricas; valores `nan` en Age imputados con la media (36.53333333333333).

```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)
```

Datos de entrada:

```
[['India' 44.0 72000.0 2.0]
 ['Spain' 27.0 48000.0 nan]
 ['Belgium' 30.0 54000.0 nan]
 ['Spain' 38.0 61000.0 nan]
 ['Belgium' 40.0 nan nan]
 ['India' 35.0 58000.0 nan]
 ['Spain' nan 52000.0 nan]
 ['India' 48.0 79000.0 2.0]
 ['Belgium' 50.0 83000.0 3.0]
 ['India' 37.0 67000.0 1.0]
 ['India' nan 56000.0 nan]
 ['Belgium' 42.0 76000.0 nan]
 ['Spain' nan 87000.0 nan]
 ['India' 34.0 nan 1.0]
 ['India' nan 45798.0 2.0]
 ['Spain' 24.0 28000.0 nan]
 ['Spain' 32.0 32000.0 nan]
 ['India' 28.0 nan nan]
 ['Belgium' 39.0 70000.0 nan]]
```

Salida:

```
[0 1 0 0 1 1 0 1 0 1 1 1 1 0 0 0 1 0 0]
```

**Figura:** Lado izquierdo, mismo dataset de 19 filas con países y valores numéricos (incluyendo 'Beligum' en la fila 12). Centro-derecha, caja con código LabelEncoder de sklearn. Debajo, salida como array de 19 enteros binarios (0s y 1s).

(slides 32–33)

### Feature Scaling

Es el proceso de escalar o convertir todos los valores en
nuestro conjunto de datos a una escala dada.

Algunos algoritmos de aprendizaje automático, como la
regresión lineal, regresión logística, etc., utilizan la
optimización por descenso del gradiente.

Tales algoritmos requieren que los datos estén escalados
para funcionar de manera óptima. K Vecinos Más Cercanos,
Máquina de Vectores de Soporte y el agrupamiento
K-Means también muestran un aumento drástico en el
rendimiento

•   Standardization
•   Normalization

```
[['India' 44.0 72000.0 2.0]
 ['Spain' 27.0 48000.0 nan]
 ['Belgium' 30.0 54000.0 nan]
 ['Spain' 38.0 61000.0 nan]
 ['Belgium' 40.0 nan nan]
 ['India' 35.0 58000.0 nan]
 ['Spain' nan 52000.0 nan]
 ['India' 48.0 79000.0 2.0]
 ['Belgium' 50.0 83000.0 3.0]
 ['India' 37.0 67000.0 1.0]
 ['India' nan 56000.0 nan]
 ['Belgium' 42.0 76000.0 nan]
 ['Spain' nan 87000.0 nan]
 ['India' 34.0 nan 1.0]
 ['India' nan 45798.0 2.0]
 ['Spain' 24.0 28000.0 nan]
 ['Spain' 32.0 32000.0 nan]
 ['India' 28.0 nan nan]
 ['Belgium' 39.0 70000.0 nan]]
```

**Figura:** Tres diagramas de dispersión en la parte inferior derecha. «Actual Data»: puntos rojos dispersos en un plano con ejes desde cero. «After normalizing»: mismos puntos comprimidos en un rango pequeño (típicamente 0 a 1). «After standardization»: puntos centrados alrededor del origen (0,0) con ejes en positivo y negativo.

#### Normalization

La normalización es el proceso de escalar los valores de los datos
de tal manera que el valor de todas las características se
encuentre entre 0 y 1.

$$X_{\text{norm}} = \frac{x - \min(x)}{\max(x) - \min(x)}$$

```python
>>> from sklearn.preprocessing import MinMaxScaler
>>> data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
>>> scaler = MinMaxScaler()
>>> print(scaler.fit(data))
MinMaxScaler()
>>> print(scaler.data_max_)
[ 1. 18.]
>>> print(scaler.transform(data))
[[0.   0.  ]
 [0.25 0.25]
 [0.5  0.5 ]
 [1.   1.  ]]
>>> print(scaler.transform([[2, 2]]))
[[1.5 0. ]]
```

```
[['India' 44.0 72000.0 2.0]
 ['Spain' 27.0 48000.0 nan]
 ['Belgium' 30.0 54000.0 nan]
 ['Spain' 38.0 61000.0 nan]
 ['Belgium' 40.0 nan nan]
 ['India' 35.0 58000.0 nan]
 ['Spain' nan 52000.0 nan]
 ['India' 48.0 79000.0 2.0]
 ['Belgium' 50.0 83000.0 3.0]
 ['India' 37.0 67000.0 1.0]
 ['India' nan 56000.0 nan]
 ['Belgium' 42.0 76000.0 nan]
 ['Spain' nan 87000.0 nan]
 ['India' 34.0 nan 1.0]
 ['India' nan 45798.0 2.0]
 ['Spain' 24.0 28000.0 nan]
 ['Spain' 32.0 32000.0 nan]
 ['India' 28.0 nan nan]
 ['Belgium' 39.0 70000.0 nan]]
```

**Figura:** Lado izquierdo, dataset de 19 filas. Lado derecho, definición de normalización, fórmula Min-Max y ejemplo interactivo de MinMaxScaler con datos `[[-1, 2], [-0.5, 6], [0, 10], [1, 18]]` mostrando `data_max_ = [1., 18.]` y transformación a rango [0, 1].

#### Standardization

La estandarización es el proceso de escalar los valores de los
datos de tal manera que adquieran las propiedades de una
distribución normal estándar. Esto significa que los datos se
reescalan de tal forma que la media se convierte en cero y los
datos tienen una desviación estándar unitaria.

$$X_{\text{stand}} = \frac{x - \text{mean}(x)}{\text{standard deviation}(x)}$$

```python
>>> from sklearn.preprocessing import StandardScaler
>>> data = [[0, 0], [0, 0], [1, 1], [1, 1]]
>>> scaler = StandardScaler()
>>> print(scaler.fit(data))
StandardScaler()
>>> print(scaler.mean_)
[0.5 0.5]
>>> print(scaler.transform(data))
[[-1. -1.]
 [-1. -1.]
 [ 1.  1.]
 [ 1.  1.]]
>>> print(scaler.transform([[2, 2]]))
[[3. 3.]]
```

```
[['India' 44.0 72000.0 2.0]
 ['Spain' 27.0 48000.0 nan]
 ['Belgium' 30.0 54000.0 nan]
 ['Spain' 38.0 61000.0 nan]
 ['Belgium' 40.0 nan nan]
 ['India' 35.0 58000.0 nan]
 ['Spain' nan 52000.0 nan]
 ['India' 48.0 79000.0 2.0]
 ['Belgium' 50.0 83000.0 3.0]
 ['India' 37.0 67000.0 1.0]
 ['India' nan 56000.0 nan]
 ['Belgium' 42.0 76000.0 nan]
 ['Spain' nan 87000.0 nan]
 ['India' 34.0 nan 1.0]
 ['India' nan 45798.0 2.0]
 ['Spain' 24.0 28000.0 nan]
 ['Spain' 32.0 32000.0 nan]
 ['India' 28.0 nan nan]
 ['Belgium' 39.0 70000.0 nan]]
```

**Figura:** Lado izquierdo, dataset de 19 filas. Lado derecho, definición de estandarización, fórmula Z-score y ejemplo interactivo de StandardScaler con datos `[[0, 0], [0, 0], [1, 1], [1, 1]]` mostrando `mean_ = [0.5, 0.5]` y transformación donde 0 → -1.0 y 1 → 1.0; transformación de `[2, 2]` da `[[3., 3.]]`.

#### Standardization Vs Normalization

```
[['India' 44.0 72000.0 2.0]
 ['Spain' 27.0 48000.0 nan]
 ['Belgium' 30.0 54000.0 nan]
 ['Spain' 38.0 61000.0 nan]
 ['Belgium' 40.0 nan nan]
 ['India' 35.0 58000.0 nan]
 ['Spain' nan 52000.0 nan]
 ['India' 48.0 79000.0 2.0]
 ['Belgium' 50.0 83000.0 3.0]
 ['India' 37.0 67000.0 1.0]
 ['India' nan 56000.0 nan]
 ['Belgium' 42.0 76000.0 nan]
 ['Spain' nan 87000.0 nan]
 ['India' 34.0 nan 1.0]
 ['India' nan 45798.0 2.0]
 ['Spain' 24.0 28000.0 nan]
 ['Spain' 32.0 32000.0 nan]
 ['India' 28.0 nan nan]
 ['Belgium' 39.0 70000.0 nan]]
```

**Figura:** Slide con subtítulo «2. STANDARDIZATION Vs NORMALIZATION» y dataset de 19 filas mostrado como lista de listas con países, edades, salarios y valores numéricos (muchos `nan`).

**Figura:** Sección superior: comparación de escalas de características. «Income»: rango de $100 a $1,000,000, etiquetado como «Large range» (nota morada con flecha). «Experience»: rango de 0 a 10, etiquetado como «Small range» (nota morada con flecha). Cajas naranjas rodean cada rango.

**Figura:** Sección inferior izquierda: tabla de clasificación de algoritmos bajo encabezado verde «Data Normalization». Columna verde «Typically Needed»: Linear Regression, Logistic Regression, Support Vector Machines (SVM), Neural Networks, k-Nearest Neighbors (k-NN), KMeans Clustering, Principal Component Analysis (PCA). Columna roja «Typically Not Needed»: Decision Trees, Random Forests, Naive Bayes, Gradient Boosting.

**Figura:** Sección inferior derecha: fragmento de árbol de decisión. Nodo raíz naranja «Income > 20000» con ramas «YES» (izquierda) y «NO» (derecha). Rama YES lleva a «Exp > 5»; rama NO lleva a «Exp < 3». Ilustra por qué los modelos basados en árboles no requieren normalización.

(slides 34–38)

### Train – test split

```python
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_train)
print(X_test)
```

Salida de `print(X_train)`:

```
[[0.0 0.0 1.0 -0.19159184384578545 -1.0781259408412425]
 [0.0 1.0 0.0 -0.014117293757057777 -0.07013167641635372]
 [1.0 0.0 0.0 0.566708506533324 0.633562432710455]
 [0.0 0.0 1.0 -0.30453019390224867 -0.30786617274297867]
 [0.0 0.0 1.0 -1.9018011447007988 -1.4204636155551582]
 [1.0 0.0 0.0 1.1475343068237058 1.232653363453549]
 [0.0 1.0 0.0 1.4379472069688968 1.5749910381638885]
 [1.0 0.0 0.0 -0.7401495441200351 -0.5646194287757332]]
```

Salida de `print(X_test)`:

```
[[0.0 1.0 0.0 -1.4661817944830124 -0.90695710348060727]
 [1.0 0.0 0.0 -0.44973664397484414 0.2056403393225306]]
```

**Figura:** Código Python que aplica StandardScaler solo a las columnas numéricas (índice 3 en adelante) de X_train y X_test, dejando intactas las primeras 3 columnas (valores binarios 0.0/1.0 de one-hot encoding). Salida: X_train con 8 filas y 5 columnas; X_test con 2 filas y 5 columnas.

??

¿Cuál usar, Normalización o estandarización?

¿Cuándo usar el escalado, antes del Split de train-test set o después?

https://drive.google.com/file/d/1YXxe-T6KkYK1DMIiZvyViztxoJ1YOFul/view?usp=sharing

**Figura:** Tres diagramas de dispersión en la parte superior izquierda. «Actual Data»: puntos rojos dispersos en plano cartesiano. «After normalizing»: puntos comprimidos en rango pequeño (0 a 1). «After standardization»: puntos centrados alrededor del origen con ejes en ±1 desviación estándar. En el centro, signos de interrogación grandes «??». Dos preguntas en azul claro sobre elección entre normalización/estandarización y momento del escalado respecto al train-test split. URL de Google Drive en la parte inferior.

(slides 39–40)

### Discretización

Discretización

• Ejemplos
   • Ingreso
     •   Bajo ingreso: $x < \$35{,}000$
     •   Ingreso medio: $\$35{,}000 < x < \$100{,}000$
     •   Ingreso alto: $x > \$100{,}000$
   • Edad
     •   menor: $x < 18$
     •   adolescente: $18 \leq x < 22$
     •   Adulto Joven: $22 \leq x < 30$
     •   $30 \leq x < 40$
     •   $40 \leq x < 65$
     •   Seniors: $x \geq 65$

**Figura:** Slide con título «Discretización» en azul claro en la parte superior izquierda. Lista anidada de viñetas bajo el encabezado «Ejemplos» con dos categorías: «Ingreso» (tres rangos salariales con desigualdades) y «Edad» (seis rangos etarios con desigualdades; los dos rangos centrales de 30–40 y 40–65 no tienen etiqueta de nombre).

(slides 41–42)

## Creación de características

### Interacción de características

Cuando las características interactúan entre sí en un
modelo de predicción, la predicción no puede expresarse
como la suma de los efectos de las características,
porque el efecto de una característica depende del valor
de la otra característica. -Christoph Molnar

**Figura:** En el centro-izquierda, cita en tipografía gris clara sans-serif atribuida a Christoph Molnar sobre interacción de características en modelos de predicción. Uno de los marcos superiores tiene filtro de color cian brillante. En una fotografía inferior, texto vertical en pared con fragmentos «GEVEN», «NIECI» y «RABLE».

(slides 44)

### Predicción aditiva vs. con interacción

La predicción no puede ser expresado como la suma de los efectos individuales de
                               sus características

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_{12} x_{12}$$

| Location | Size | Prediction |
| --- | --- | --- |
| good | big | 300 000 |
| good | small | 200 000 |
| bad | big | 250 000 |
| bad | small | 150 000 |

Se puede descomponer en:
•   Un término constante (150 000)
•   Size (+ 100 000 si big: +0 si small)
•   Location(+50 000 si Good; +0 si bad)

Facilmente se explica la predicción

No hay interacción entre variables

| Location | Size | Prediction |
| --- | --- | --- |
| good | big | 400 000 |
| good | small | 200 000 |
| bad | big | 250 000 |
| bad | small | 150 000 |

Términos de interacción:
•   (+ 100 000 si size==big and
        location==good)

Casas grandes y pequeñas dependen de la
Localización

hay interacción entre variables

**Figura:** Slide con título centrado en la parte superior sobre interacción de variables. Debajo del título, fórmula de descomposición con término constante, efectos principales y término de interacción. Dos columnas comparativas. **Columna izquierda (sin interacción):** tabla de 4 filas con columnas Location, Size y Prediction (valores: good/big/300 000, good/small/200 000, bad/big/250 000, bad/small/150 000). Debajo, descomposición aditiva: término constante 150 000, efecto Size +100 000 si big, efecto Location +50 000 si Good. Texto conclusivo: «Facilmente se explica la predicción» y «No hay interacción entre variables». **Columna derecha (con interacción):** tabla de 4 filas con mismas columnas pero predicción good/big = 400 000 (en lugar de 300 000). Debajo, «Términos de interacción» con término adicional +100 000 si size==big and location==good. Texto conclusivo: «Casas grandes y pequeñas dependen de la Localización» y «hay interacción entre variables».

(slides 45)

### Objetivos de la ingeniería de características

•   Entender las relaciones entre las características en tu conjunto de
    datos y su efecto en la predicción, y evitar sesgos al interpretar
    modelos solo con los efectos principales y no con los efectos
    interactivos.

•   Utilizar la información sobre interacciones para construir
    explícitamente modelos expresivos.

•   Ingeniería de características para mejorar el rendimiento del modelo.

**Figura:** Tres viñetas en tipografía gris oscura cursiva.

(slides 46)

## Selección de características

Set of all Features → Selecting the Best Subset → Learning Algorithm → Performance

**Figura:** Diagrama de flujo lineal horizontal con flechas: «Set of all Features» → «Selecting the Best Subset» → «Learning Algorithm» → «Performance». uno con superposición cian. Texto vertical parcialmente visible en pared: «NN GEVEN NIECI RABLE».

### Concepto y objetivos

La selección de características es el proceso de aislar las características más
consistentes, no redundantes y relevantes para usar en la construcción del modelo.
Reducir metódicamente el tamaño de los conjuntos de datos es importante a medida que
el tamaño y la variedad de los conjuntos de datos continúan creciendo.

El objetivo principal de la selección de características es mejorar el rendimiento de un
modelo predictivo y reducir el costo computacional del modelado.

**Figura:** En el centro de la slide, hexágono azul etiquetado «Benefits of Feature Selection». Seis flechas salen del hexágono hacia seis beneficios, cada uno con icono y caja de texto azul: (1) «Enable Easy Model Building» — icono de tres engranajes entrelazados; (2) «Simplify Model Debugging» — icono de un bug dentro de una lupa; (3) «Easy Model Interpretation» — icono de bombilla sobre silueta de persona; (4) «Efficient Selection of Relevant Features» — icono de diana con flecha en el centro; (5) «Massively Reduce Model Training Time» — icono de cronómetro; (6) «Massively Improve the Model Performance» — icono de gráfico de barras con flecha ascendente.

Métodos de Selección de Características:

      •   Métodos de Filtro
      •   Métodos Envolventes
      •   Métodos Embebidos

**Figura:** En el centro de la slide, rectángulo redondeado naranja etiquetado «Feature Selection». Seis iconos circulares azules rodean el rectángulo central, cada uno con una flecha hacia una caja de texto con un beneficio en inglés: (superior izquierda) icono de diana — «Remove irrelevant features»; (superior derecha) icono de bug en mira — «Easier to Debug»; (centro derecha) icono de bombilla sobre persona — «Easier to understand»; (inferior derecha) icono de laptop con tres engranajes — «Easier to build»; (inferior izquierda) icono de cronómetro con líneas de movimiento — «Make training faster»; (centro izquierda) icono de gráfico de línea con flecha ascendente — «Increase the performance of our models».

(slides 48–49)

### Métodos de Filtro

Los métodos de filtro capturan las propiedades intrínsecas de las características
 medidas a través de estadísticas univariadas en lugar del rendimiento de la validación
 cruzada.

 Estos métodos son más rápidos y menos costosos computacionalmente. Al tratar con datos
 de alta dimensionalidad, es más económico computacionalmente utilizar métodos de filtro.

          •   Ganancia de Información
          •   Chi-square Test
          •   Correlation Score
          •   Variance Threshold
          •   …

**Figura:** Slide con título «1. Métodos de Filtro» en azul claro en la parte superior izquierda. Dos párrafos explicativos en negro; la frase «capturan las propiedades intrínsecas de las características medidas a través de estadísticas» aparece en negrita; la palabra «univariadas» en cursiva azul claro. Lista de viñetas con cuatro métodos de filtro y puntos suspensivos.

#### Ganancia de Información

1.   Métodos de Filtro
     1.1 Ganancia de Información
       La ganancia de información calcula la reducción en entropía a partir de la
       transformación de un conjunto de datos. Se puede utilizar para la selección de
       características evaluando la ganancia de información de cada variable en el contexto de
       la variable objetivo

```python
from sklearn.feature_selection import mutual_info_classif
import matplotlib.pyplot as plt
%matplotlib inline

importances = mutual_info_classif(X, Y)
feat_importances = pd.Series(importances, dataframe.columns[0:len(dataframe.columns)-1])
feat_importances.plot(kind='barh', color = 'teal')
plt.show()
```

**Figura:** Debajo del texto y código, gráfico de barras horizontales (barh) en color teal que muestra la importancia de características. Eje Y (de arriba a abajo): age, pedi, mass, test, skin, pres, plas, preg. Eje X (Importance Score): de 0.00 a 0.10+. plas tiene la puntuación más alta (> 0.10). mass, age y test muestran importancia moderada. skin tiene puntuación cero o casi cero. preg, pres y pedi tienen puntuaciones bajas.

#### Chi-square Test

1.   Métodos de Filtro
     1.2 Chi-square Test
       La prueba de Chi-cuadrado se utiliza para características categóricas en un conjunto de
       datos. Calculamos el Chi-cuadrado entre cada característica y la variable objetivo, y
       seleccionamos el número deseado de características con las mejores puntuaciones de
       Chi-cuadrado. Para aplicar correctamente la prueba de Chi-cuadrado y evaluar la
       relación entre varias características en el conjunto de datos y la variable objetivo, se
       deben cumplir las siguientes condiciones:
       • las variables deben ser categóricas,
       • muestreadas de forma independiente,

```python
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Convert to categorical data by converting data to integers
X_cat = X.astype(int)

# Three features with highest chi-squared statistics are selected
chi2_features = SelectKBest(chi2, k = 3)
X_kbest_features = chi2_features.fit_transform(X_cat, Y)

# Reduced features
print('Original feature number:', X_cat.shape[1])
print('Reduced feature number:', X_kbest_features.shape[1])
```

```
Original feature number: 8
Reduced feature number: 3
```

**Figura:** Slide con subtítulo «1.2 Chi-square Test» en cursiva. Bloque de código Python con fondo gris claro. Debajo, salida del print mostrando reducción de 8 a 3 características.

#### Correlation Coefficient

1.   Métodos de Filtro
     1.3 Correlation Coefficient
       La correlación es una medida de la relación lineal entre 2 o más variables. A través de
       la correlación, podemos predecir una variable a partir de la otra. La lógica detrás de
       usar la correlación para la selección de características es que las buenas variables tienen
       una alta correlación con la variable objetivo. Además, las variables deberían estar
       correlacionadas con la variable objetivo pero no correlacionadas entre sí.

       Podemos calcular la correlación entre variables o con la variable objetivo

```python
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Correlation matrix
cor = dataframe.corr()

# Plotting Heatmap
plt.figure(figsize = (10,6))
sns.heatmap(cor, annot = True)
```

**Figura:** A la derecha del código, mapa de calor (heatmap) de correlación para un dataset con variables: preg, plas, pres, skin, test, mass, pedi, age y class. Matriz 9×9 con valores numéricos anotados en cada celda (annot=True). La diagonal contiene valor 1 en color crema claro. Ejemplo: correlación entre age y preg = 0.54. La variable objetivo parece ser class. Barra de escala de color a la derecha va de 0.0 (morado oscuro/negro) a 1.0 (crema claro).

#### Variance Threshold

1.   Métodos de Filtro
     1.4 Variance Threshold
       El umbral de varianza es un enfoque básico y simple para la selección de
       características. Elimina todas las características cuya varianza no cumple con cierto
       umbral. Por defecto, elimina todas las características de varianza cero, es decir,
       características con el mismo valor en todas las muestras.

```python
from sklearn.feature_selection import VarianceThreshold

# Resetting the value of X to make it non-categorical
X = array[:,0:8]

v_threshold = VarianceThreshold(threshold=0)
v_threshold.fit(X) # fit finds the features with zero variance
v_threshold.get_support()
```

```
array([ True,  True,  True,  True,  True,  True,  True,  True])
```

**Figura:** Slide con subtítulo «1.4 Variance Threshold» en cursiva. Bloque de código Python con fondo gris claro. Debajo, salida de `get_support()` indicando que las 8 características pasan el umbral (todas True).

#### Tabla de métodos de filtro

https://bib.irb.hr/datoteka/763354.MIPRO_2015_JovicBrkicBogunovic.pdf

| Name | Filter class | Applicable to task |
| --- | --- | --- |
| Information gain | univariate, information | classification |
| Gain ratio | univariate, information | classification |
| Symmetrical uncertainty | univariate, information | classification |
| Correlation | univariate, statistical | regression |
| Chi-square | univariate, statistical | classification |
| Inconsistency criterion | multivariate, consistency | classification |
| Minimum redundancy, maximum relevance (mRMR) | multivariate, information | classification, regression |
| Correlation-based feature selection (CFS) | multivariate, statistical | classification, regression |
| Fast correlation-based filter (FCBF) | multivariate, information | classification |
| Fisher score | univariate, statistical | classification |
| Relief and ReliefF | univariate, distance | classification, regression |
| Spectral feature selection (SPEC) and Laplacian Score (LS) | univariate, similarity | classification, clustering |
| Feature selection for sparse clustering | multivariate, similarity | clustering |
| Localized Feature Selection Based on Scatter Separability (LFSBSS) | multivariate, statistical | clustering |
| Multi-Cluster Feature Selection (MCFS) | multivariate, similarity | clustering |
| Feature weighting K-means | multivariate, statistical | clustering |
| ReliefC | univariate, distance | clustering |

**Figura:** Tabla de referencia con tres columnas (Name, Filter class, Applicable to task) y 17 filas de métodos de selección de características. URL de fuente en la parte inferior izquierda: `https://bib.irb.hr/datoteka/763354.MIPRO_2015_JovicBrkicBogunovic.pdf`.

(slides 50–55)

### Métodos envolventes

Requieren algún método para buscar en el espacio de todos los posibles subconjuntos
 de características, evaluando su calidad mediante el aprendizaje y la evaluación de un
 clasificador con ese subconjunto de características. El proceso de selección de
 características se basa en un algoritmo de aprendizaje automático específico que estamos
 intentando ajustar a un conjunto de datos dado.

          •   Forward Feature Selection
          •   Backward Feature Elimination
          •   Recursive Feature Elimination

**Figura:** Slide con título «2. Métodos envolventes» en azul claro en la parte superior izquierda. Párrafo explicativo en cursiva; la frase «método para buscar en el espacio de todos los posibles subconjuntos de características, evaluando su calidad mediante el aprendizaje y la evaluación de un clasificador» aparece en negrita. Lista de tres técnicas envolventes.

#### Forward Feature Selection

2. Métodos envolventes
   2.1 Forward Feature Selection
     Este es un método iterativo en el que comenzamos con las características que tienen
     un buen rendimiento contra las características objetivo. A continuación, seleccionamos
     otra variable que ofrece el mejor rendimiento en combinación con la primera variable
     seleccionada.

```python
# Forward Feature Selection
from mlxtend.feature_selection import SequentialFeatureSelector
ffs = SequentialFeatureSelector(lr, k_features='best', forward = True, n_jobs=-1)
ffs.fit(X, Y)
features = list(ffs.k_feature_names_)
features = list(map(int, features))
lr.fit(x_train[features], y_train)
y_pred = lr.predict(x_train[features])
```

**Figura:** Slide con subtítulo «2.1 Forward Feature Selection» en cursiva. Bloque de código Python numerado (líneas 1–8) con fondo gris claro que usa `SequentialFeatureSelector` de mlxtend con `forward=True`, extrae nombres de características seleccionadas, y reentrena/predice con `lr` usando solo esas características.

#### Backward Feature Elimination

2. Métodos envolventes
   2.2 Backward Feature Elimination
    Comenzamos con todas las características disponibles y construimos un modelo.
    Luego, eliminamos la variable del modelo que parecen no ayudar al modelo en
    evaluación. Este proceso continúa hasta que se alcanza el criterio preestablecido

```python
# Backward Feature Selection
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector

# Initialize the model
lr = LogisticRegression(class_weight = 'balanced', solver = 'lbfgs', random_state=42, n_jobs=-1, max_iter=500)
lr.fit(X, Y)

# Initialize and fit the Sequential Feature Selector for backward elimination
bfs = SequentialFeatureSelector(lr, k_features='best', forward = False, n_jobs=-1)
bfs.fit(X, Y)

# Extract and process the selected features
features = list(bfs.k_feature_names_)
features = list(map(int, features))

# Retrain the model using only the selected features
lr.fit(x_train[features], y_train)
y_pred = lr.predict(x_train[features])
```

**Figura:** Slide con subtítulo «2.2 Backward Feature Elimination» en cursiva. Párrafo explicativo con «características disponibles y construimos un modelo» en negrita. Bloque de código Python con resaltado de sintaxis que inicializa `LogisticRegression`, crea `SequentialFeatureSelector` con `forward=False`, extrae características seleccionadas y reentrena/predice.

#### Recursive Feature Elimination (RFE)

2. Métodos envolventes
   2.3 Recursive Feature Elimination (RFE)
      •   Método para seleccionar las características más importantes.
      •   Utiliza un estimador externo que asigna pesos a las características.

  Primer Paso - Entrenamiento Inicial

  • Entrenar el estimador en el conjunto inicial de características.
  • Obtener la importancia de cada característica.

  Eliminación de Características
  • Eliminar las características menos importantes del
     conjunto actual.

  Proceso Recursivo

  Repetir el proceso de entrenamiento y eliminación en el
  nuevo conjunto reducido de características.

```python
# Recursive Feature Selection
from sklearn.feature_selection import RFE
rfe = RFE(lr, n_features_to_select=7)
rfe.fit(x_train, y_train)
y_pred = rfe.predict(x_train)
```

**Figura:** Slide con subtítulo «2.3 Recursive Feature Elimination (RFE)» en cursiva. Texto estructurado en tres secciones: «Primer Paso - Entrenamiento Inicial», «Eliminación de Características» y «Proceso Recursivo», con viñetas descriptivas. A la derecha, bloque de código Python numerado (líneas 1–5) que importa `RFE`, lo inicializa con `lr` y `n_features_to_select=7`, ajusta con `x_train`/`y_train` y predice.

(slides 56–59)

### Métodos embebidos

Estos métodos abarcan los beneficios tanto de los métodos de envolventes como de los
 métodos de filtro, al incluir interacciones entre características pero también al mantener
 costos computacionales razonables. Los métodos embebidos son iterativos en el sentido de
 que se encargan de cada iteración del proceso de entrenamiento del modelo y extraen
 cuidadosamente aquellas características que más contribuyen al entrenamiento en una
 iteración particular.

           •   LASSO Regularization (L1)
           •   Random Forest Importance

**Figura:** Slide con título «3. Métodos embebidos» en azul claro en la parte superior izquierda. Párrafo explicativo en negro; las frases «métodos de envolventes como de los métodos de filtro» aparecen en negrita. Lista de dos técnicas embebidas: LASSO Regularization (L1) y Random Forest Importance.

#### LASSO Regularization (L1)

**3.1 LASSO Regularization (L1)**

La regularización consiste en añadir una penalización a los diferentes parámetros del modelo de aprendizaje automático para reducir la libertad del modelo, es decir, para evitar el sobreajuste.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel

# Set the regularization parameter C=1
logistic = LogisticRegression(C=1, penalty="l1", solver='liblinear', random_state=7).fit(X, Y)
model = SelectFromModel(logistic, prefit=True)

X_new = model.transform(X)

# Dropped columns have values of all 0s, keep other columns
selected_columns = selected_features.columns[selected_features.var() != 0]
selected_columns
```

```
Int64Index([0, 1, 2, 3, 4, 5, 6, 7], dtype='int64')
```

**Figura:** La slide presenta el título «3. Métodos embebidos» en la parte superior izquierda, en tipografía grande, negrita y azul cian. Debajo aparece el subtítulo «3.1 LASSO Regularization (L1)» en cursiva y gris oscuro. A la derecha del subtítulo se muestra el párrafo descriptivo sobre regularización. En la zona central-inferior se muestra un bloque de código Python con fondo gris claro que importa `LogisticRegression` y `SelectFromModel`, configura un modelo logístico con penalización L1 (`C=1`, `penalty="l1"`, `solver='liblinear'`, `random_state=7`), lo ajusta con `X` e `Y`, crea un `SelectFromModel` con `prefit=True`, transforma `X` en `X_new`, y selecciona columnas cuya varianza no es cero. Debajo del bloque de código aparece la salida `Int64Index([0, 1, 2, 3, 4, 5, 6, 7], dtype='int64')`.

#### Random Forest

**3.2 Random Forest**

Basicamente consiste en hacer una poda para quedarse con las características más importantes.

```python
from sklearn.ensemble import RandomForestClassifier

# create the random forest with your hyperparameters.
model = RandomForestClassifier(n_estimators=340)

# fit the model to start training.
model.fit(X, Y)

# get the importance of the resulting features.
importances = model.feature_importances_

# create a data frame for visualization.
final_df = pd.DataFrame({"Features": pd.DataFrame(X).columns, "Importances":importances})
final_df.set_index('Importances')

# sort in ascending order to better visualization.
final_df = final_df.sort_values('Importances')

# plot the feature importances in bars.
final_df.plot.bar(color = 'teal')
```

```
<AxesSubplot:>
```

**Figura:** La slide presenta el título «3. Métodos embebidos» en la parte superior izquierda, en tipografía grande, negrita y azul cian. Debajo aparece el subtítulo «3.2 Random Forest» en cursiva y gris oscuro. A la derecha del subtítulo se muestra el párrafo descriptivo sobre poda de características. En la zona central se muestra un bloque de código Python con fondo gris claro que importa `RandomForestClassifier`, crea un modelo con `n_estimators=340`, lo ajusta con `X` e `Y`, obtiene `feature_importances_`, construye un DataFrame `final_df` con columnas «Features» e «Importances», llama a `set_index('Importances')`, ordena por «Importances» y genera un gráfico de barras con color teal. Debajo del código aparece la salida `<AxesSubplot:>` seguida de un gráfico de barras agrupadas. El gráfico tiene leyenda con dos series: «Features» (color teal) e «Importances» (color azul marino). El eje X muestra las etiquetas categóricas ordenadas: 3, 4, 0, 2, 6, 7, 5, 1. El eje Y va de 0 a 7. Las barras de «Features» (teal) tienen alturas que coinciden con el valor numérico de la etiqueta del eje X (por ejemplo, la etiqueta 7 tiene barra de altura 7). Las barras de «Importances» (azul marino) son extremadamente cortas, apenas visibles sobre la línea base, indicando valores fraccionarios muy pequeños.

(slides 60–62)

## Algunas técnicas de procesamiento de características

### Principal Component Analysis (PCA)

técnica utilizada para describir un conjunto de datos en términos de nuevas variables ("componentes") no correlacionadas

**Figura:** La slide presenta el título «1. Principal Component Analysis (PCA)» en la parte superior izquierda, en azul. Debajo aparece el subtítulo en español sobre la técnica de componentes no correlacionados. La slide se divide en tres secciones explicativas. **Sección superior izquierda — Transformación de ejes:** subtítulo en naranja «Determine a system of UNCORRELATED axes (x', y') to represent the data». Muestra un diagrama de dispersión con puntos azules (círculos) con correlación lineal positiva en un sistema de coordenadas $x$-$y$ estándar. Sobre los datos se superponen dos ejes nuevos en línea discontinua, $x'$ y $y'$. El eje $x'$ se alinea con la dirección principal de dispersión de los datos, y el eje $y'$ es perpendicular a él. Una etiqueta verde indica un ángulo de **90°** entre estos nuevos ejes, señalando que son no correlacionados. **Sección superior central — Análisis de varianza:** subtítulo en naranja «Find the variance of data along all uncorrelated axes». Muestra el mismo diagrama de dispersión con etiquetas de varianza. Un corchete rojo a lo largo del eje $x'$ está etiquetado como «Direction of HIGH variance». Un corchete verde más pequeño a lo largo del eje $y'$ está etiquetado como «Direction of LOW variance». **Sección inferior — Representación matricial:** ilustra la multiplicación de matrices usada para reducción de dimensionalidad. Matriz **[Data]**: etiqueta «Data», dimensiones $n\_samples$ (filas) por $init\_dimensions$ (columnas). Multiplicada por (×) la matriz **[Eigenvectors]**: etiqueta «Eigenvectors (sorted by decreasing eigenvalues)». Dentro de esta matriz, una subselección está resaltada en un recuadro verde con una etiqueta y flecha que apunta: «selecting first two vectors (k)». Igual (=) a la matriz **[Dimensionally reduced data]**: etiqueta «Dimensionally reduced data», dimensiones $n\_samples$ (filas) por $k$ (columnas).

**Figura:** La slide presenta dos elementos visuales principales sobre PCA. **Diagrama de flujo del proceso PCA (lado izquierdo):** describe los pasos para realizar PCA mediante cuatro paneles ilustrativos en secuencia. **Paso 1 — High dimensional data:** un diagrama de dispersión muestra puntos de datos distribuidos a lo largo de una línea diagonal en un sistema de coordenadas cartesianas 2D con ejes $x$ e $y$. **Paso 2 — Determine a system of UNCORRELATED axes ($x'$, $y'$) to represent the data:** el mismo diagrama de dispersión con nuevos ejes ortogonales ($x'$ e $y'$) introducidos. El eje $x'$ está rotado para alinearse con la dirección de mayor dispersión (varianza) de los datos, y el eje $y'$ es perpendicular a él ($90°$). **Paso 3 — Find the variance of data along all uncorrelated axes:** el diagrama etiqueta el eje $x'$ como «Direction of HIGH variance» y el eje $y'$ como «Direction of LOW variance». **Paso 4 — Final Data with Reduced Dimensions:** el panel muestra el resultado de descartar la dirección de baja varianza ($y'$) y proyectar los puntos originales sobre el eje único de alta varianza ($x'$), reduciendo los datos de espacio 2D a 1D. **Gráfico de varianza explicada acumulada (lado derecho):** gráfico combinado de barras y línea titulado «Cumulative Explained Variance Plot for PCA». Eje X: «Principal Component Number», de 1 a 10. Eje Y: «Explained Variance», de 0% a 100%. **Varianza individual por componente (barras naranjas):** muestra el porcentaje de varianza explicada por cada componente específico: PC 1 ~29%, PC 2 ~27%, PC 3 ~18%, PC 4 ~13%, PC 5 ~6%, PC 6 ~3%, PCs 7–10 porcentajes muy pequeños (1% o menos cada uno). **Varianza acumulada (línea azul con marcadores):** muestra el total acumulado de varianza explicada al agregar componentes, con puntos etiquetados: PC 1 **29%**, PC 2 **56%**, PC 3 **74%**, PC 4 **87%**, PC 5 **93%**, PC 6 **96%**, PC 7 **97%**, PC 8 **98%**, PC 9 **99%**, PC 10 **100%**.

(slides 64–65)

### Autoencoders

**Figura:** La slide presenta el título «2. Autoencoders» en la parte superior izquierda, en azul. **Sección superior — Arquitectura de Autoencoder:** diagrama esquemático clásico de una red neuronal autoencoder. **Entrada y salida:** en los extremos izquierdo y derecho hay barras verticales altas de color amarillo que representan las capas de datos de entrada y salida. Son idénticas en tamaño, ilustrando que el objetivo de la red es reconstruir la entrada. **Encoder:** a la derecha de la entrada, la sección «Encoder» muestra una serie de capas (color beige) que disminuyen progresivamente de tamaño, representando el proceso de reducción de dimensionalidad. **Latent Representation:** en el centro hay una capa pequeña de color naranja con tres segmentos. Es el cuello de botella de la red, conteniendo la representación comprimida de características de la entrada. **Decoder:** a la derecha de la representación latente, la sección «Decoder» muestra capas (color verde claro) que aumentan progresivamente de tamaño, reflejando el encoder para reconstruir los datos a sus dimensiones originales. **Conectividad:** todas las capas están conectadas por una red de líneas negras que representan los pesos y conexiones neuronales entre capas. **Sección inferior — Flujo de trabajo de aplicación:** dividido en tres etapas principales, indicadas por encabezados de color en la parte inferior. **1. Hotspots Detection (azul claro):** «Computing Probability and Intensity» muestra un mapa circular de una «Street-Network» (en azul) y un extracto de «Street-Map». Los datos de estos mapas se mapean a un diagrama de dispersión que compara «Intensity» vs. «Probability» para identificar áreas significativas. «Hotspot Selection» muestra un mapa circular donde los hotspots detectados se resaltan como clusters densos rojos sobre un diseño urbano. **2. Finding Similar Hotspots (rojo claro):** «Hotspot Time Series Embedding» muestra múltiples gráficos de series temporales extraídos de los hotspots. Estos gráficos se alimentan a un modelo autoencoder simplificado etiquetado «Hotspot Embedding (hotspot2vec)». «Grouping and Projection» muestra que la salida del embedding es un conjunto de «Feature Vectors» (representados como bloques apilados). Estos vectores se proyectan en un diagrama de dispersión 2D donde hotspots similares se agrupan en clusters de colores. **3. Finding Relations (verde azulado claro):** «Crime & Infrastructure» vincula los datos agrupados al contexto del mundo real. Muestra cuatro fotografías de street-view de ubicaciones urbanas específicas en diferentes años (2010, 2011, 2015, 2017) junto a un gráfico de línea de timeline/intensidad, sugiriendo un análisis de cómo la infraestructura y los eventos de crimen se relacionan a lo largo del tiempo en esas ubicaciones de hotspots.

(slides 66)

## Conclusiones

La selección de características es un recurso invaluable para los científicos de datos.

Comprender cómo seleccionar características importantes en el aprendizaje automático es crucial para la eficacia del algoritmo de aprendizaje automático. Las características irrelevantes, redundantes y ruidosas pueden contaminar un algoritmo, afectando negativamente el rendimiento del aprendizaje, la precisión y el costo computacional.

La selección de características es cada vez más importante a medida que el tamaño y la complejidad del conjunto de datos promedio continúan creciendo exponencialmente.

**Figura:** Todo el texto está en blanco, tipografía sans-serif limpia, alineado a la izquierda en la sección azul. Contiene tres párrafos sobre la selección de características como recurso invaluable, la importancia de seleccionar características relevantes y el crecimiento exponencial de la importancia de la selección de características.

(slides 68)

## Glosario

- **Ingeniería de características:** proceso de transformar datos en bruto en características que mejor representan el problema subyacente a los modelos, mejorando así su rendimiento. Puede considerarse como el arte de seleccionar las características importantes.
- **MNAR (Missing not at random / Faltante no al azar):** cuando un valor falta debido al valor en sí.
- **MAR (Missing at random / Faltante al azar):** cuando un valor falta debido a otra variable observada.
- **MCAR (Missing completely at random / Faltante completamente al azar):** no hay un patrón que determine cuáles valores faltan.
- **Eliminación:** eliminar datos con entradas faltantes.
- **Imputación:** rellenar campos faltantes con ciertos valores.
- **Normalización:** proceso de escalar los valores de los datos de tal manera que el valor de todas las características se encuentre entre 0 y 1.
- **Estandarización (Standardization):** proceso de escalar los valores de los datos de tal manera que adquieran las propiedades de una distribución normal estándar; la media se convierte en cero y los datos tienen una desviación estándar unitaria.
- **Discretización:** transformación de variables continuas en categorías mediante rangos definidos (por ejemplo, rangos de ingreso o edad).
- **Selección de características:** proceso de aislar las características más consistentes, no redundantes y relevantes para usar en la construcción del modelo.
- **Métodos de Filtro:** capturan las propiedades intrínsecas de las características medidas a través de estadísticas univariadas en lugar del rendimiento de la validación cruzada.
- **Ganancia de Información:** calcula la reducción en entropía a partir de la transformación de un conjunto de datos; se utiliza para la selección de características evaluando la ganancia de información de cada variable en el contexto de la variable objetivo.
- **Variance Threshold (Umbral de varianza):** enfoque básico que elimina todas las características cuya varianza no cumple con cierto umbral; por defecto, elimina características de varianza cero.
- **Métodos envolventes:** requieren algún método para buscar en el espacio de todos los posibles subconjuntos de características, evaluando su calidad mediante el aprendizaje y la evaluación de un clasificador con ese subconjunto.
- **Métodos embebidos:** abarcan los beneficios tanto de los métodos de envolventes como de los métodos de filtro, al incluir interacciones entre características pero manteniendo costos computacionales razonables.
- **Regularización:** consiste en añadir una penalización a los diferentes parámetros del modelo de aprendizaje automático para reducir la libertad del modelo, es decir, para evitar el sobreajuste.
- **PCA (Principal Component Analysis):** técnica utilizada para describir un conjunto de datos en términos de nuevas variables ("componentes") no correlacionadas.
