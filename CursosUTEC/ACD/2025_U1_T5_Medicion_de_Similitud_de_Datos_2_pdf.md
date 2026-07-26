---
curso: ACD
titulo: [2025] U1_T5 Medición de Similitud de Datos-2
slides: 48
fuente: [2025] U1_T5 Medición de Similitud de Datos-2.pdf
---

## Slide 1

Portada (decorativa: fondo azul con túnel tecnológico y silueta).

**Medición de Similitud y Disimilitud de Datos**
DS3021 Análisis Computacional de Datos

## Slide 2

Slide de objetivo. Imagen decorativa (dos personas trabajando, tinte azul) a la izquierda.

**Objetivo de sesión**

> Comprender qué técnicas o herramientas existen para determinar la similitud y disimilitud de los datos.

## Slide 3

Índice. Imagen decorativa (persona con visor VR, globo terráqueo digital).

**Contenido**

1. Conceptos
2. Proximidad para atributos Nominales
3. Proximidad para atributos Binarios

## Slide 4

Etiqueta morada "RECAPITULANDO".

**Tipos de Atributos — Percepción Analítica**

Diagrama de árbol horizontal. Nodo raíz gris `Data Attributes` se bifurca en dos nodos grises:

- **Numérico** → cajas celestes `Proporción` e `Intervalo`.
- **Categórico** → caja celeste `Ordinal` y caja verde `Nominal`.
  - `Nominal` (verde) → `Binario` (verde) y `No Binario` (verde).
    - `Binario` → `Simétrico` y `Asimétrico` (ambas verdes).

El resaltado en verde marca la rama nominal/binaria, foco de la sesión.

## Slide 5

Separador de sección (imagen decorativa: mano robótica y globo digital).

**1. Conceptos de Similitud y Disimilitud de Datos**

## Slide 6

**Similitud y Disimilitud de Datos**

En Ciencia de Datos, **la medida de similitud** es una forma de medir cómo se relacionan las muestras de datos entre sí.

Por otro lado, **la medida de disimilitud** sirve para indicar en qué medida son distintos los objetos de datos.

**Proximidad** se refiere tanto para similitud como para disimilitud.

## Slide 7

**Similitud de Datos**

- Es una medida numérica que indica **qué tan parecidos** son dos objetos de datos.
  - A mayor valor, mayor coincidencia entre los datos.
  - A menudo cae en el rango [0, 1]
- La similitud podría usarse **para identificar**:
  - Datos duplicados que pueden tener diferencias debido a errores tipográficos.
  - Instancias equivalentes de diferentes conjuntos de datos. Por ejemplo, nombres y/o direcciones que son iguales pero tienen errores ortográficos.
  - Grupos de datos próximos (clusters)

## Slide 8

**Disimilitud de Datos**

- Medida de disimilitud es una medida numérica de cuán diferentes son dos objetos de datos
  - A menor valor, mayor coincidencia
  - La disimilitud mínima suele ser 0, mientras que el límite superior varía dependiendo de cuánta variación se observe
- La disimilitud podría usarse para identificar
  - valores atípicos (outliers)
  - excepciones interesantes. Por ejemplo, fraude de tarjeta de crédito, límites a los grupos, etc.

## Slide 9

**Matriz de Datos**

Una matriz de datos (*object-by-attribute structure*) es una estructura que almacena **n** *data objects* en la forma de una matriz **nxp** donde **p** es el número de atributos.

Visual: matriz encerrada en corchetes, con una flecha celeste rotulada *data object* apuntando a la primera fila:

$$
\begin{bmatrix}
x_{11} & \cdots & x_{1f} & \cdots & x_{1p}\\
\cdots & \cdots & \cdots & \cdots & \cdots\\
x_{i1} & \cdots & x_{if} & \cdots & x_{ip}\\
\cdots & \cdots & \cdots & \cdots & \cdots\\
x_{n1} & \cdots & x_{nf} & \cdots & x_{np}
\end{bmatrix}
$$

**Por ejemplo:** x₁₁ es el valor del *data object* 1 de la columna 1

## Slide 10

**Matriz de Disimilitud**

Una matriz de disimilitud (*object-by-object structure*) es una estructura que almacena un conjunto de proximidades para todos los pares de **n** *data objects*. Tiene la forma de una matriz **nxn**.

Visual: matriz triangular inferior:

$$
\begin{bmatrix}
0 & & & &\\
d(2,1) & 0 & & &\\
d(3,1) & d(3,2) & 0 & &\\
\vdots & \vdots & \vdots & &\\
d(n,1) & d(n,2) & \cdots & \cdots & 0
\end{bmatrix}
$$

**Por ejemplo:** *d(i,j)* es la medida de disimilitud o diferencia entre el *object i* y el *object j*.

## Slide 11

Slide de actividad (imagen decorativa de laboratorio; marca `# TO DO` arriba).

**Trabajemos juntos — Ejercicios 1 - 4**

## Slide 12

Separador de sección (imagen decorativa de mano robótica).

**2. Proximidad para Atributos Nominales**

## Slide 13

**Proximidad para Atributos Nominales**

- Un atributo nominal puede tener dos o más estados.
- **¿Cómo se calcula disimilitud entre *objects* descritos como atributos nominales?**
  - La disimilitud entre dos *objects* **i** y **j** puede ser calculado basado en la proporción de **mismatches (no coincidencias)**.

$$d(i,j) = \frac{p - m}{p}$$

donde **m** es el número de matches (1 si son iguales y 0 en caso contrario) y **p** es el total de atributos **nominales** de la matriz de datos.

## Slide 14

**Proximidad para Atributos Nominales**

La **similitud** de los datos nominales pueden ser calculados como:

$$sim(i,j) = 1 - d(i,j) = \frac{m}{p}$$

## Slide 15

**Proximidad para Atributos Nominales**

Tabla de datos (izquierda):

| Object Identifier | Atributo Nominal |
|---|---|
| 1 | codeA |
| 2 | codeB |
| 3 | codeC |
| 4 | codeA |

Al centro, la plantilla de matriz de disimilitud 4x4 triangular:

$$
\begin{bmatrix}
0 & & &\\
d(2,1) & 0 & &\\
d(3,1) & d(3,2) & 0 &\\
d(4,1) & d(4,2) & d(4,3) & 0
\end{bmatrix}
$$

Con la fórmula $d(i,j) = \frac{p-m}{p}$ y los cálculos:

```
d(2,1) = (1 - 0)/1 = 1
d(3,1) = (1 - 0)/1 = 1
d(3,2) = (1 - 0)/1 = 1
d(4,1) = (1 - 1)/1 = 0
d(4,2) = ?
d(4,3) = ?
```

Derecha: "Entonces, la **matriz de disimilitud** es:"

$$
\begin{bmatrix}
0 & & &\\
1 & 0 & &\\
1 & 1 & 0 &\\
0 & 1 & 1 & 0
\end{bmatrix}
$$

## Slide 16

Slide de actividad (imagen decorativa de laboratorio).

**Trabajemos juntos — Ejercicios 5 - 7**

## Slide 17

Separador de sección (imagen decorativa de mano robótica).

**3. Proximidad para Atributos Binarios**

## Slide 18

**Proximidad para Atributos Binarios**

- Recordemos que los atributos binarios pueden ser:
  - Simétricos
  - Asimétricos
- Tratar a los atributos binarios como numéricos (1 o 0) podría llevarnos a malos cálculos cuando se refiere a la proximidad de datos.

## Slide 19

**Proximidad para Atributos Binarios Simétricos**

Para binarios simétricos se debe analizar los pesos de los valores. Por ejemplo a través de una tabla de contingencia:

|  | Object j = 1 | Object j = 0 | sum |
|---|---|---|---|
| **Object i** = 1 | q | r | q + r |
| **Object i** = 0 | s | t | s + t |
| **sum** | q + s | r + t | p |

Sean dos data objects **i** y **j**, se define:
- **q:** el número de **atributos** iguales a 1 para ambos objects.
- **r:** el número de atributos que son iguales a 1 para el objeto **i** pero 0 para el objeto **j**.
- **s:** el número de atributos iguales a 0 para el objeto **i** y 1 para el objeto **j**.
- **t:** el número de atributos que son iguales a 0 para ambos objetos.
- **p:** el número total de **atributos binarios** donde **p = q + r + s + t**.

## Slide 20

**Proximidad para Atributos Binarios Simétricos**

Basados en la tabla de contingencia, la disimilitud entre los *objects* **binarios simétricos** i y j se calcula de la siguiente manera:

$$d(i,j) = \frac{r + s}{q + r + s + t}$$

## Slide 21

**Ejemplo**

Suponga que la siguiente tabla corresponde a los records de un paciente donde:
- **name**: es el nombre del paciente
- **gender**: es el género del paciente (binario simétrico)
- **fever, cough**: Presencia de fiebre y tos respectivamente (binario asimétrico)
- **test-1, test-2, test-3, test-4**: Resultados de pruebas donde N es negativo y P es positivo (binario asimétrico)

Tabla (las columnas `name` y `gender` están resaltadas con un recuadro celeste, señalando el bloque simétrico):

| name | gender | fever | cough | test-1 | test-2 | test-3 | test-4 |
|---|---|---|---|---|---|---|---|
| Jack | M | Y | N | P | N | N | N |
| Jim | M | Y | Y | N | N | N | N |
| Mary | F | Y | N | P | N | P | N |
| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ |

## Slide 22

**Calculando la disimilitud de atributos binarios simétricos:**

Izquierda: tabla reducida solo a las columnas simétricas:

| name | gender |
|---|---|
| Jack | M |
| Jim | M |
| Mary | F |

Derecha: fórmula $d(i,j) = \frac{r+s}{q+r+s+t}$ y

```
Calculamos:
d(Jack,Jim) =
d(Jack,Mary) =
```

Abajo, la tabla de contingencia genérica (Object i filas 1/0/sum × Object j columnas 1/0/sum con q, r, s, t, p) repetida como referencia.

## Slide 23

**Calculando la disimilitud de atributos binarios simétricos:** (misma slide con respuestas)

Misma tabla name/gender, misma fórmula y tabla de contingencia. Resultados:

```
d(Jack,Jim)  = (0 + 0) / (0 + 0 + 0 + 1) = 0
d(Jack,Mary) = (0 + 1) / (0 + 0 + 1 + 0) = 1
```

## Slide 24

Slide de actividad (imagen decorativa de laboratorio).

**Trabajemos juntos — Ejercicios 8 - 10**

## Slide 25

**Proximidad para Atributos Binarios Asimétricos**

- Para los atributos binarios asimétricos, los dos estados **no son igualmente importantes**, como los resultados positivos (1) y negativos (0) de una prueba de enfermedad.
- Dados dos atributos binarios asimétricos, la concordancia de dos 1s (una coincidencia positiva) se considera más significativa que la de dos 0s (una coincidencia negativa). Por lo tanto, estos atributos binarios a menudo se consideran "**monarios**" (que tienen un estado).
- La disimilitud basada en estos atributos se denomina **disimilitud binaria asimétrica**, donde el número de coincidencias negativas, <u>t, se considera sin importancia</u> y, por lo tanto, se ignora en el siguiente cálculo:

$$d(i,j) = \frac{r + s}{q + r + s}$$

## Slide 26

**Proximidad para Atributos Binarios Asimétricos**

De manera complementaria, podemos medir la diferencia entre dos atributos binarios basándonos en la noción de **similitud en lugar de disimilitud**. Por ejemplo, **la similitud binaria asimétrica** entre los objetos i y j se puede calcular como:

$$sim(i,j) = \frac{q}{q + r + s} = 1 - d(i,j)$$

A la fórmula anterior se la conoce en la literatura como el ***Coeficiente de Jaccard***.

## Slide 27

**Ejemplo**

Mismo enunciado de records de pacientes (name, gender simétrico; fever, cough, test-1..test-4 asimétricos). Aquí el recuadro celeste resalta las columnas **fever, cough, test-1, test-2, test-3, test-4** (el bloque asimétrico).

| name | gender | fever | cough | test-1 | test-2 | test-3 | test-4 |
|---|---|---|---|---|---|---|---|
| Jack | M | Y | N | P | N | N | N |
| Jim | M | Y | Y | N | N | N | N |
| Mary | F | Y | N | P | N | P | N |
| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ |

## Slide 28

**Calculando la disimilitud de atributos binarios asimétricos:**
Considere Y y P como 1 y el valor N como 0

Izquierda: tabla completa de pacientes (name, gender, fever, cough, test-1..4) y debajo la tabla de contingencia genérica (q, r, s, t, p) y la fórmula $d(i,j)=\frac{r+s}{q+r+s}$.

Derecha, sin resolver:

```
Calculamos:
d(Jack,Jim) =
d(Jack,Mary) =
d(Jim,Mary) =
```

## Slide 29

**Calculando la disimilitud de atributos binarios asimétricos:** (resuelta)
Considere Y y P como 1 y el valor N como 0

La columna `gender` aparece sombreada en gris (excluida del cálculo asimétrico); quedan fever, cough, test-1..test-4.

```
d(Jack,Jim)  = (1 + 1) / (1 + 1 + 1) = 0.67
d(Jack,Mary) = (0 + 1) / (2 + 0 + 1) = 0.33
d(Jim,Mary)  = (1 + 2) / (1 + 1 + 2) = 0.75
```

Estas mediciones sugieren que es **poco probable** que Jim y Mary tengan una enfermedad similar porque tienen el valor de disimilitud más alto entre los tres pares.

De los tres pacientes, Jack y Mary son los que tienen **más probabilidades** de padecer una enfermedad similar.

También se muestran la tabla de contingencia genérica y $d(i,j)=\frac{r+s}{q+r+s}$.

## Slide 30

Slide de actividad (imagen decorativa de laboratorio).

**Trabajemos juntos — Ejercicio 11**

## Slide 31

Separador de sección (imagen decorativa de mano robótica). Numerado "3." (repetido en el original).

**3. Proximidad para Atributos Numéricos**

## Slide 32

**Proximidad para Atributos Numéricos**

- Para medir la disimilitud entre atributos numéricos se utilizan **las distancias Euclidiana, Manhattan y Minkowski.**
- En algunos casos, los datos se normalizan antes de aplicar los cálculos de distancia. Esto implica transformar los datos para que se encuentren dentro de un rango más pequeño o común, como [−1, 1] o [0, 1].
  - Considere un atributo de altura, por ejemplo, que podría medirse en metros o pulgadas. En general, expresar un atributo en unidades más pequeñas conducirá a un rango más amplio para ese atributo y, por lo tanto, tenderá a darle a dichos atributos un mayor efecto o "peso".

## Slide 33

**Proximidad para Atributos Numéricos**

**Distancia Euclidiana:**
Sean dos objects i = (x_{i1}, x_{i2}, …, x_{ip}) y j = (x_{j1}, x_{j2}, …, x_{jp}) descritos por **p** atributos. La distancia Euclidiana entre los objects i y j es definida como:

$$d(i,j) = \sqrt{(x_{i1}-x_{j1})^2 + (x_{i2}-x_{j2})^2 + \cdots + (x_{ip}-x_{jp})^2}$$

**Distancia Manhattan:**

$$d(i,j) = |x_{i1}-x_{j1}| + |x_{i2}-x_{j2}| + \cdots + |x_{ip}-x_{jp}|$$

## Slide 34

**Ejemplo**

| Object Identifier | Atributo Num 1 | Atributo Num 2 |
|---|---|---|
| 1 | 45 | 15 |
| 2 | 22 | 19 |
| 3 | 64 | 14 |
| 4 | 28 | 12 |

Calculando la disimilitud d(2,1) es:

```
d(2,1) = sqrt( (22 – 45)² + (19 – 15)² )
d(2,1) = sqrt( 529 – 16 )
d(2,1) = sqrt( 513 )
d(2,1) = 22.64
```

(Nota: la slide muestra "529 – 16"; la suma correcta sería 529 + 16 = 545.)

## Slide 35

Slide de actividad (imagen decorativa de laboratorio).

**Trabajemos juntos — Ejercicio 12**

## Slide 36

Separador de sección (imagen decorativa de mano robótica).

**4. Proximidad para Atributos Ordinales**

## Slide 37

**Proximidad para Atributos Ordinales**

- Los valores de un atributo ordinal tienen **un orden o clasificación significativa**, pero se desconoce la magnitud entre valores sucesivos.
- Los atributos ordinales también se pueden obtener a partir de la discretización de atributos numéricos dividiendo el rango de valores en un número finito de categorías.
  - Estas categorías están organizadas en rangos. Es decir, el rango de un atributo numérico se puede asignar a un atributo ordinal **f** que tiene estados **M_f**.

## Slide 38

**Proximidad para Atributos Ordinales**

Suponga que **f** es un atributo ordinal que describe **n objects**. La disimilitud con respecto al atributo involucra los siguientes pasos:

1. Determinar el número de estados posibles **M** de un atributo ordinal **f**. Se denota como **M_f**. Por ejemplo, el atributo `class(o)` cuenta con 3 posibles estados (First, Second, Third). Por lo tanto **M_f = 3**.
2. Reemplazar cada valor del atributo ordinal por su rank (numérico). Por ejemplo: First = 1, Second = 2 y Third = 3. De tal manera que el rankeo es **r_if = {1, …, M_f} = {1, 2, 3}**
3. Dado que cada atributo ordinal puede tener diferentes estados, se debe mapear el rango a cada atributo entre [0, 1] tal que cada atributo tiene el mismo peso. Se normaliza de la siguiente manera:

$$z_{if} = \frac{r_{if} - 1}{M_f - 1}$$

**z_if:** representa el valor f para el i-ésimo object

4. Luego se calcula la disimilitud como para atributos numéricos

## Slide 39

**Ejemplo**

| Object Identifier | Atributo Ordinal |
|---|---|
| 1 | excelente |
| 2 | requiere mejora |
| 3 | bueno |
| 4 | excelente |

1. Dado que tiene tres atributos (excelente, requiere mejora, bueno). Entonces, **M_f = 3**.
2. Reemplazar por su rank (numérico), entonces:
   - Excelente : 3
   - Bueno : 2
   - Requiere Mejora : 1
3. Normalizar usando $z_{if} = \frac{r_{if}-1}{M_f-1}$

```
Requiere Mejora (1) = (1 – 1) / (3 – 1) = 0
Bueno (2)           = (2 – 1) / (3 – 1) = 0.5
Excelente (3)       = (3 – 1) / (3 – 1) = 1
```

Abajo a la izquierda, la plantilla vacía de matriz de disimilitud 4x4 con d(2,1) … d(4,3).

## Slide 40

**Ejemplo (cont)**

| Object Identifier | Atributo Ordinal | Valor normalizado |
|---|---|---|
| 1 | excelente | 1 |
| 2 | requiere mejora | 0 |
| 3 | bueno | 0.5 |
| 4 | excelente | 1 |

Plantilla de matriz de disimilitud triangular con d(2,1) … d(4,3).

Encontrar d(i,j) usando distancia Euclidiana

```
d(2,1) = sqrt( (0 – 1)² )   = 1
d(3,1) = sqrt( (0.5 – 1)² ) = 0.5
d(4,1) = sqrt( (1 – 1)² )   = 0
```

## Slide 41

**Ejemplo (cont)** — misma tabla normalizada, ahora con la matriz completa.

| Object Identifier | Atributo Ordinal | Valor normalizado |
|---|---|---|
| 1 | excelente | 1 |
| 2 | requiere mejora | 0 |
| 3 | bueno | 0.5 |
| 4 | excelente | 1 |

Encontrar d(i,j) usando distancia Euclidiana. Resultado:

$$
\begin{bmatrix}
0 & & &\\
1.0 & 0 & &\\
0.5 & 0.5 & 0 &\\
0 & 1.0 & 0.5 & 0
\end{bmatrix}
$$

## Slide 42

Slide de actividad (imagen decorativa de laboratorio).

**Trabajemos juntos — Ejercicio 13**

## Slide 43

Separador de sección (imagen decorativa de mano robótica).

**5. Proximidad para Atributos Mixtos**

## Slide 44

**Proximidad para Atributos Mixtos**

En las secciones anteriores hemos revisado como calcular la disimilitud entre objetos de diferentes tipos. Sin embargo, en muchas bases de datos reales, los objetos se describen mediante una combinación de tipos de atributos.

Entonces,

**¿Cómo podemos calcular la disimilitud entre objetos con tipos de atributos mixtos?**

## Slide 45

**Proximidad para Atributos Mixtos**

- Un enfoque es agrupar cada tipo de atributo, **realizando análisis de datos separados**. Por ejemplo, como en minería (agrupamiento) para cada tipo. Esto es factible si estos análisis derivan resultados compatibles. Sin embargo, en aplicaciones reales, es poco probable que se pueda realizar un análisis por separado por tipo de atributo generará resultados compatibles.
- Un enfoque más preferible es **procesar todos los tipos de atributos juntos**, realizando una análisis único. Una de esas técnicas combina los diferentes atributos en una sola matriz de disimilitud, reuniendo todos los atributos significativos en una escala común del intervalo [0, 1].

## Slide 46

**Proximidad para Atributos Mixtos**

Supongamos que el conjunto de datos contiene **p** atributos de tipo mixto. La disimilitud **d(i, j)** entre los objetos i y j se define como:

$$d(i,j) = \frac{\sum_{f=1}^{p} \delta_{ij}^{(f)} d_{ij}^{(f)}}{\sum_{f=1}^{p} \delta_{ij}^{(f)}}$$

donde:
- $\delta_{ij}^{(f)} = 0$ si $x_{if}$ o $x_{jf}$ no existe o si $x_{if} = x_{jf} = 0$ y el atributo **f** es binario asimétrico.
- $\delta_{ij}^{(f)} = 1$, en caso contrario.

La contribución del atributo **f** para la disimilitud entre i y j ($d_{ij}^{(f)}$) es calculado dependiendo su tipo:

- Si f es **numérico**:

$$d_{ij}^{(f)} = \frac{|x_{if} - x_{jf}|}{\max_h x_{hf} - \min_h x_{hf}}$$

donde h es para todo object del atributo f.

- Si f es **nominal o binario**: $d_{ij}^{(f)} = 0$ si $x_{if} = x_{jf}$; en caso contrario $d_{ij}^{(f)} = 1$
- Si f es **ordinal**: Calcula los ranks $r_{if}$ y $z_{if} = \frac{r_{if}-1}{M_f-1}$ y trata a $z_{if}$ como numérico.

Anotación en celeste al costado de la fórmula numérica: **"Solo numérico cambia"**.

## Slide 47

**Ejemplo**

| Object Identifier | Atributo Nominal | Atributo Ordinal | Atributo Num |
|---|---|---|---|
| 1 | codeA | excelente | 45 |
| 2 | codeB | requiere mejora | 22 |
| 3 | codeC | bueno | 64 |
| 4 | codeA | excelente | 28 |

Desarrollo de d(2,1):

$$d(2,1) = \frac{\delta_{21}^{(Nom)} d_{21}^{(Nom)} + \delta_{21}^{(Ord)} d_{21}^{(Ord)} + \delta_{21}^{(Num)} d_{21}^{(Num)}}{\delta_{21}^{(Nom)} + \delta_{21}^{(Ord)} + \delta_{21}^{(Num)}}$$

$$d(2,1) = \frac{(1)(1) + (1)(1) + (1)\left(\frac{|45-22|}{64-22}\right)}{1+1+1} = \frac{1 + 1 + 0.55}{3} = 0.85$$

Abajo a la izquierda, la plantilla de matriz de disimilitud con d(2,1) … d(4,3).

**Resultado:**

$$
\begin{bmatrix}
0 & & &\\
0.85 & 0 & &\\
0.65 & 0.83 & 0 &\\
0.13 & 0.71 & 0.79 & 0
\end{bmatrix}
$$

## Slide 48

Slide de actividad (imagen decorativa de laboratorio).

**Trabajemos juntos — Ejercicio 14**
