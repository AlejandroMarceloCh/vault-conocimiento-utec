---
curso: EST
titulo: DISEÑOBLOQUES
slides: 506
fuente: DISEÑOBLOQUES.qmd
---

# DISEÑOBLOQUES

## Índice

Material Quarto/R del curso (código + prosa). Ingesta directa sin transcripción (ya es markdown).

## Quarto

Quarto enables you to weave together content and executable code into a finished document. To learn more about Quarto see <https://quarto.org>.

## Running Code

When you click the **Render** button a document will be generated that includes both content and the output of embedded code. You can embed code like this:

```{r}
1 + 1
```

You can add options to executable code like this

```{r}
#| echo: false
2 * 2
```

The `echo: false` option disables the printing of code (only output is displayed).

# DISEÑO DE BLOQUES

**INTRODUCCIÓN:**

comparación de notas de alumnos mediante 3 **métodos de enseñanza**: M1, M2 , M3

**Forma 1:**

```{r}
T1<-c(15,12,18,15) # notas de 4 alumnos (A, B, C, D)  con el método 1
T2<-c(17,18,17,12) # notas de 4 alumnos (E; F; G; H)  con el método 2
T3<-c(15,08,16,17) # notas de 4 alumnos (I; J; K; L)  con el método 3.
# En total se ha tomado 12 alumnos.
```

Aquí se usaría *Diseño de experimentos con un solo factor. (`aov`)*

**FORMA 2:** (Diseño por bloques)

```{r}
#tomo 4 alumnos y a cada alumno le aplico los 3 métodos de enseñanza:
#ALUMNOS:A, B,  C, D    # Sus notas de c.u. con cada tratamiento será:
T1<-  c(15, 12,18, 15)  
T2<-  c(17, 18,17, 12)   
T3<-  c(15, 08,16, 17) 
# En total solo se usa 4 alumnos y se tiene la misma cantidad de datos.
```

Este último se llama Diseño por bloques.

-   T1, T2, T3 ==\> Tratamientos.

-   A, B, C, D ==\> Bloques.

Aquí cada alumno, representa un BLOQUE y los métodos de enseñanza, representan a los TRATAMIENTOS.

## Diseño aleatorizado por bloques

Debe considerar que a cada unidad experimental (persona u objeto) se le debe asignar sus tratamientos por aleatoriedad (al azar o por sorteo)

Tratamientos: son los tipos que se van a comparar.

Bloques: cada individuo u objeto al cual se le aplica todos los tratamientos.

Objetivos:

-   Entender en qué consiste un **experimento completamente aleatorizado por bloques**.

-   Comparar el diseño completamente aleatorizado por bloques con el **diseño experimental completamente aleatorizado**.

-   Formular las hipótesis necesarias, calcular el estadístico de prueba para poder realizar las comparaciones de manera estadísticamente significativa.

## ¿En qué consiste un experimento aleatorizado por bloques?

**Un diseño aleatorizado por bloques** aparece cuando una muestra aleatoria simple de $n$ individuos (sujetos u objetos) reciben cada uno de los $k$ tratamientos que se desea comparar. Como cada una de las $k$ observaciones, una para cada tratamiento, son obtenidas del mismo sujeto u objeto, las $k$ muestras no son independientes.

n: cantidad de individuos u objetos ==\> bloques.

k: cantidad de tratamientos que se va a comparar.

## Ejemplo 1:

Cuatro tipos de llantas para camiones: A, B, C y D, se quieren comparar en términos de su durabilidad. Una manera de diseñar un experimento para hacer dicha comparación, es seleccionar una muestra aleatoria simple de $n$ camiones y colocarle a cada camión una llanta de cada tipo. Las ubicaciones de las llanta serían frente izquierdo, frente derecho, trasero izquierdo y trasero derecho. **Dichas posiciones serán asignadas aleatoriamente** para cada camión. Después de un número preestablecido de millas rodando con dichos camiones, el desgaste de cada uno de las llantas será evaluado.

Con un diseño por bloques, siempre se obtiene un diseño balanceado ( misma cantidad de datos para cada tratamiento)

TRATAMIENTOS: los 4 tipos de llantas

BLOQUES: Cada camión ==\> n camiones.

variable a medir: el desgaste de las llantas ( la durabilidad de las llantas)

## Observación:

En este ejemplo, los $n$ camiones son los bloques y los cuatro grupos a comparar o tratamientos serán los cuatro tipos de llantas. Para cada bloque se tomarán 4 medidas que representarán el desgaste de cada uno de los 4 tipos de llantas correspondientes a cada camión. Por lo tanto, dichas 4 medidas DE LAS LLANTAS no podrán ser consideradas independientes (son dependientes) pues todas fueron sometidas a la misma carga, mismo conductor, mismas condiciones de la vía recorrida, etc. Sin embargo las mediciones de desgaste entre camiones si podrán ser consideradas independientes.

-   entre bloques (entre camiones) ==\> las medidas *son independientes*

-   entre tratamientos (entre llantas) ==\> las medidas *son dependientes*.

## Notar que:

**Otro diseño** posible es usar el tipo de llanta A en $n_{1}$ camiones, el tipo de llanta B en otros $n_{2}$ camiones, el tipo de llanta C en otra muestra disjunta de $n_{3}$ camiones y la llanta D en otra muestra de $n_{4}$ camiones. Para cada camión el desgaste promedio de las cuatro llantas del mismo tipo que usa cada camión, resultando en 4 muestras independientes del desgaste promedio de cada tipo de llanta.

En este caso estarías en presencia de una **ANOVA de una vía o un Factor** con 4 tratamientos.

## Ejemplo 2:

Se desea comparar 3 métodos distintos para determinar el porcentaje de impurezas presente en una porción de un mineral en particular. Un experimento aleatorizado por bloques para hacer dicha comparación consiste en obtener $n$ porciones de dicho mineral y someter cada porción a cada uno de los tres métodos para determinar su porcentaje de impurezas. El orden en el cuál los tres tratamientos son aplicados debe ser aleatorizado para cada muestra. Es decir, se tendrán tres observaciones para cada muestra.

En este ejemplo las $n$ porciones son los bloques y las poblaciones a comparar o los tratamientos son los tres métodos distintos para determinar el porcentaje de impurezas en cada muestra del mineral. Claramente, las tres mediciones obtenidas por cada muestra no pueden ser consideradas independientes pues provienen de la misma muestra.

Tratamientos: los tres métodos para ver porcentajes de impurezas

Bloques: las n porciones de mineral.

## Notar que:

Podríamos tomar una muestra distinta para cada método. En este caso tendríamos tres muestras independientes y estaríamos en presencia de una ANOVA de una vía con tres tratamientos si es que el tamaño de la muestra nos permitiera garantizar la normalidad de los datos.

## Estructura de los datos de un experimento completamente aleatorizado por bloques {.scrollable}

| Tratamientos |          | Bloques  |          |          |
|--------------|----------|----------|----------|----------|
|              | 1        | $2$      | $\cdots$ | $n$      |
| 1            | $X_{11}$ | $X_{12}$ | $\cdots$ | $X_{1n}$ |
|              |          |          |          |          |
| 2            | $X_{21}$ | $X_{22}$ | $\cdots$ | $X_{2n}$ |
| $\vdots$     |          |          |          |          |
| $k$          | $X_{k1}$ | $X_{k2}$ | $\cdots$ | $X_{kn}$ |

$$
k: \text{ # de tratamientos, cuyas medias se van a comparar}\\
n: \text{ # de bloques, sobre los cuales se aplica los k tratatmientos a c.u.}\\
X_{ij}: \text{  dato j-ésimo del tratamiento i (bloque j del tratamiento i) }
$$

$X_{23}$ ==\> dato que está en el tratamiento 2 y en el bloque 3

Los sujetos u objetos a los que se les aplica cada tratamiento, se les llama **bloques** Un diseño por bloques es llamado aleatorizado si el orden en el cual los $k$ tratamientos son aplicados es aleatorizado para cada bloque. El término **Diseño por bloques completamente aleatorizado** es usado para enfatizar que cada bloque recibe los $k$ tratamientos.

**Observe que las** $k$ observaciones dentro de cada bloque $j$, es decir, $X_{1j}, X_{2j}, \cdots, X_{kj}$ no pueden ser consideradas independientes. Mientras que las columnas si lo son.

El objetivo es determinar como son las medias de cada tratamiento: ¿iguales o diferentes?

## Modelo de un experimento completamente aleatorizado por bloques {.scrollable}

Recordemos que las $k$ observaciones $X_{1j},X_{2j}, \cdots, X_{kj}$ para $j=1,2,\cdots n$ serán en general **correlacionadas**, pero las observaciones en bloques distintos **(columnas distintas)** podremos asumir que son **independientes**. El conjunto de observaciones del tratamiento $i$ se asume que es una muestra aleatoria simple de la población correspondiente al tratamiento $i$ para $i=1,2,\cdots, k$.

Denotemos $\mu_{i}\equiv E(\overline{X_{i.}})$ en donde $\overline{X_{i.}}\equiv\frac{1}{n}\sum_{j=1}^{n}X_{ij}$

y pensaremos que

$$
\mu_{i}=\mu +\alpha_{i}
$$

$$
\mu_{i}: \text{  es la media o esperado del tratamiento i}
$$

en donde $\mu=\frac{1}{k}\sum_{i=1}^{k}\mu_{i}$ la media poblacional global y $\alpha _{i}$ la variación asociada al efecto del tratamiento $i$

## Hipótesis nula

$$
\begin{align*}
&H_{0}: \mu_{1}=\mu_{2}\cdots=\mu_{k} (\text{por tratamientos})\\
&\text{ es equivalente a poner a prueba si}\\
&H_{0}: \alpha_{1}=\alpha_{2}=\cdots=\alpha_{k}=0
\end{align*}
$$

$$
Ha: \text{ alguna media es distinta de otras}
$$

También se puede probar sobre los bloques:

*Ho: todas las medias **por bloques** son iguales*

*Ha: alguna media por bloques es distinta.*

## Volviendo al modelo y sus suposiciones:

Como ahora, en contraste con el modelo completamente aleatorizado, las $k$ observaciones $X_{1j},X_{2j}, \cdots, X_{kj}$ para $j=1,2,\cdots n$ ya no son independientes por lo que el modelo cambia al siguiente:

$$
X_{ij}=\mu +\alpha_{i}+\beta_{j}+\epsilon_{ij}
$$

En donde los $\beta_j$ para todo $j=1,2,\cdots, n$ son los efectos aleatorios asociados a cada bloque $j$ que asumiremos que son variables aleatorias independientes e idénticamente distribuidas con $E(\beta_j)=0$ y $Var(\beta_j)=\sigma_{b}^{2}$ y los $\epsilon_{ij}$. Igual que para el modelo completamente aleatorizado los errores intrínsecos $\epsilon_{ij}$ para todo $i=1,2,\cdots, k$ y todo $j=1,2,\cdots, n$ se asumen independientes entre ellas e independientes de los bloques con $E(\epsilon_{ij})=0$ con $Var(\epsilon_{ij})=\sigma^{2}_{\epsilon}$

## ¿Cómo calculamos el estadístico para someter a prueba las hipótesis

::: {style="font-size: 25px;"}
+--------------+------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------+-----------------------------------+
| Fuente       | Suma de cuadrados                                                                                                | Grados de libertad | Error cuadrático medio       | $F$                               |
+==============+==================================================================================================================+====================+==============================+===================================+
| Tratamientos | $SSTr=\sum_{i=1}^{k}n(\overline{X_{i.}}-\overline{X_{..}})^{2}$                                                  | $k-1$              | $MSTr=\frac{SSTr}{k-1}$      | $F_{H_{0}^{Tr}}=\frac{MSTr}{MSE}$ |
+--------------+------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------+-----------------------------------+
| Bloques      | $SSB=\sum_{j=1}^{n}k\left(\overline{X_{.j}}-\overline{X_{..}}\right)^{2}$                                        | $n-1$              | $MSB=\frac{SSB}{n-1}$        | $F_{H_{0}^{Bl}}=\frac{MSBl}{MSE}$ |
+--------------+------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------+-----------------------------------+
| Error        | $SSE= \sum_{i=1}^{k}\sum_{j=1}^{n}\left(X_{ij}-\overline{X_{i.}}-\overline{X_{.j}}+\overline{X_{..}}\right)^{2}$ | $(n-1)(k-1)$       | $MSE=\frac{SSE}{(n-1)(k-1)}$ |                                   |
+--------------+------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------+-----------------------------------+
| Total        | $SST=SSTr+SSB+SSE$                                                                                               | $nk-1$             |                              |                                   |
+--------------+------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------+-----------------------------------+
:::

o también:

**TABLA DE ANOVA POR BLOQUES**

+--------------+------------+--------------+----------------------------+--------------------------+-----------+
| fuente       | GL         | SC           | CM                         | Fo                       | P valorl6 |
+==============+============+==============+============================+==========================+===========+
| Tratamientos | k-1        | SCTr         | $$                         | $$                       | $$        |
|              |            |              | CMTr=\frac{SCTr}{k-1}      | Fo_{Tr}=\frac{CMTr}{CME} | p_{Tr}    |
|              |            |              | $$                         | $$                       | $$        |
+--------------+------------+--------------+----------------------------+--------------------------+-----------+
| Bloques      | n-1        | SCB          | $$                         | $$                       | $$        |
|              |            |              | CMB=\frac{SCB}{n-1}        | Fo_{B}=\frac{CMB}{CME}   | p_{B}     |
|              |            |              | $$                         | $$                       | $$        |
+--------------+------------+--------------+----------------------------+--------------------------+-----------+
| Error        | (k-1)(n-1) | SCE          | $$                         |                          |           |
|              |            |              | CME=\frac{SCE}{(k-1)(n-1)} |                          |           |
|              |            |              | $$                         |                          |           |
+--------------+------------+--------------+----------------------------+--------------------------+-----------+
| Total        | nk-1       | SCT=         |                            |                          |           |
|              |            |              |                            |                          |           |
|              |            | SCTr+SCB+SCE |                            |                          |           |
+--------------+------------+--------------+----------------------------+--------------------------+-----------+

Siendo los P valores:

$$
P_{Tr}=P(F(k-1;(k-1)(n-1))>Fo_{Tr})
$$

$$
P_{B}=P(F(n-1;(k-1)(n-1)>Fo_{B})
$$

**La prueba principal es: (Hipótesis de igualdad de medias para los tratamientos)**

$$
Ho: \mu1=\mu2=...\mu k
$$

$$
Ha: \text{  alguna media es distinta de otras}
$$

Lo cual se prueba con el P valor de Tratamientos.

O también

En donde, Se rechaza Ho si $Fo_{Tr}>F(1-\alpha,k-1, (k-1)(n-1))$

**Además se puede hacer la siguiente prueba secundaria:**

probar la igualdad de valoración promedio entre los n elementos de los bloques:

$$
Ho: \mu1=\mu2=...\mu n
$$

$$
Ha: \text{alguna media de los bloques es distinta de los otros}
$$

Tener presente las sumas de cuadrados:

$SSTr=\sum_{i=1}^{k}n(\overline{X_{i.}}-\overline{X_{..}})^{2}$

$SSB=\sum_{j=1}^{n}k\left(\overline{X_{.j}}-\overline{X_{..}}\right)^{2}$

$SSE= \sum_{i=1}^{k}\sum_{j=1}^{n}\left(X_{ij}-\overline{X_{i.}}-\overline{X_{.j}}+\overline{X_{..}}\right)^{2}$

$SST=SSTr+SSB+SSE$

**HASTA AQUI POR HOY VIERNES.**

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

## Ejemplo 3: {.scrollable}

```{r}

```

Una muestra de 36 visitantes a un viñedo de Ica, probaron y ranquearon 4 variedades de vino en la escala del 1 al 10. Para tratar de ser lo más imparciales posible, los vinos fueron identificados con los números del 1 al 4. El orden en el cual cada uno de los cuatro vinos fueron presentados a cada visitante fue aleatorizado. La calificación promedio de cada vino y el promedio total resultaron ser

$$
\begin{align*}
\overline{X_{1.}}&=8.97 \text{  promedio del vino 1}\\
\overline{X_{2.}}&=9.04 \text{  promedio del vino 2}\\
\overline{X_{3.}}&=8.36  \text{  promedio del vino 3}\\
\overline{X_{4.}}&=8.31  \text{  promedio del vino 4}\\
\overline{X_{..}}&=8.67 \text{  promedio total de los vinos}\\
\end{align*}
$$

Más aún, la suma de los cuadrado debido a los visitantes (bloques) resultó ser $SSB=11.38$ y la suma de cuadrados totales $SST=65.497$. Con la información suministrada, construya una tabla ANOVA, formule las hipótesis y determine si existe alguna diferencia significativa en el ranqueado de los 4 vinos. Use un nivel de significancia de $\alpha= 0.05.$

Solución:

**K=4** tipos de vino (los tratamientos)

n=36 encuestados ( los bloques)

**TABLA DE ANOVA POR BLOQUES**

+--------------+--------------+----------------+---------------------------------------+---------------------------------------+--------------+
| fuente       | GL           | SC             | CM                                    | Fo                                    | P valorl6    |
+==============+==============+================+=======================================+=======================================+==============+
| Tratamientos | k-1 = **3**  | *SCTr=16.2936* | $$ CMTr=\frac{SCTr}{k-1}=5.4312 $$    | $$ Fo_{Tr}=\frac{CMTr}{CME}=15.086 $$ | $$ p_{Tr} $$ |
+--------------+--------------+----------------+---------------------------------------+---------------------------------------+--------------+
| Bloques      | n-1=**35**   | SCB=**11.38**  | $$ CMB=\frac{SCB}{n-1}=0.3251 $$      | $$ Fo_{B}=\frac{CMB}{CME}=0.9 $$      | $$ p_{B} $$  |
+--------------+--------------+----------------+---------------------------------------+---------------------------------------+--------------+
| Error        | (k-1)(n-1)   | SCE=37.8234    | $$ CME=\frac{SCE}{(k-1)(n-1)}=0.36 $$ |                                       |              |
|              |              |                |                                       |                                       |              |
|              | =**105**     |                |                                       |                                       |              |
+--------------+--------------+----------------+---------------------------------------+---------------------------------------+--------------+
| Total        | nk-1=**143** | SCT=**65.497** |                                       |                                       |              |
+--------------+--------------+----------------+---------------------------------------+---------------------------------------+--------------+

: Debido a los datos que se tiene conviene calcular:

$SCTr=\sum_{i=1}^{k}n(\overline{X_{i.}}-\overline{X_{..}})^{2}=\sum_{i=1}^{4}36(\overline{X_{i.}}-\overline{X_{..}})^{2}$

$$
SCTr=36(8.97-8.67)^2 +36(9.04-8.67)^2 +36(8.36-8.67)^2+36(8.31-8.67)^2
$$

```{r}
SCTr<-36*((8.97-8.67)^2 +(9.04-8.67)^2 +(8.36-8.67)^2+(8.31-8.67)^2)
SCTr
```

Y se halla SCE

```{r}
SCE<- 65.497-11.38-16.2936
SCE
```

Siendo los P valores:

P valor de Tratamientos:

```{r echo=TRUE}
pf(15.086, 3,  105, lower.tail=FALSE )
```

**Para la prueba principal:**

Como este P valor \< Alfa ==\>Rechazo Ho: hay evidencias concluyentes o contundentes de que los promedios son diferentes.

**Para la prueba secundaria:**

Pvalor =P(F(35, 105)\>0.9)

```{r}
pf(0.9, 35, 105, lower.tail= FALSE)
```

Pvalor es mayor que Alfa ==\> No rechazo Ho ==\> No hay evidencias de que los promedios sean diferentes ==\> Podemos asumir que son iguales. Es decir, los visitantes han dado igual valoración promedio, a los tipos de vino.

## Ejemplo:

## Si se tiene los siguientes datos:

Tipos de Vino

```{r  echo=TRUE}
df<-read.table("http://media.pearsoncmg.com/cmg/pmmg_mml_shared/mathstatsresources/Akritas/NapaValleyWT.txt") 
df
# head(df)

```

4 tratamientos (vinos) ==\> k= 4

36 bloques (aqui son los encuestados) ==\> n=36

total: 144 datos

Se sigue manteniendo la notación Xij ==\> i: tratamiento , j: encuestado

## Preparando los datos

```{r echo=TRUE}
sdf<- stack(df)
sdf


```

Se tiene 36 veces W1, 36 veces w2, etc.

aqui los datos ya estan apilados.

&&&&&&&&&&&&&&&&&&&&&&&\
&&&&&&&&&&&&&&&&&&&&&&&

## Renombrando las columnas de los índices y de los visitantes

Cada elemento es $X_{ij}$

$$
i:\text{   Tratamiento  i-ésimo ...   } vinos\\
j:\text{   Bloque j-ésimo....} encuestados
$$

Organizamos los sub índices

primero: $i\in [1:4]$

```{r echo=TRUE}
wine=as.factor((c(rep(1,36),rep(2,36),rep(3,36),rep(4,36))))
wine
```

as.factor ==\> datos organizados

rep ==\> réplicar

rep(1,36)==\> el 1 se repite 36 veces consecutivas

rep(2,36)==\> el 2 se repite 36 veces consecutivas

etc.

ahora $j\in[1:36]$

```{r echo=TRUE}
visitor=as.factor(rep(1:36,4))
visitor
```

## Preparando el dataframe final

```{r echo=TRUE}
sdf1 <- cbind(sdf, wine)
sdf1
#head(sdf1)


```

```{r}
sdf2 <- cbind(sdf1, visitor)
sdf2
#head(sdf2)
#tail(sdf2)
```

## Obteniendo la tabla ANOVA para un modelos aleatorizados por bloques

```{r echo=TRUE}
summary(aov(values~ind+visitor, data=sdf2))  # tratamientos + bloques
```

HIPÓTESIS PRINCIPALES: igualdad de medias de tratamientos.

$$
Ho: \mu1=\mu2=\mu3=\mu4\\
Ha: \text{existe alguna media que es distinta a las otras}
$$

Como Pvalor (tratamientos)= 0.000...00318\<Alfa ==\> Rechazo Ho ==\> Existe alguna media que es distinta de otras. No todas las medias de los tratamientos son iguales: Algún tipo de vino es el mejor o tal vez es el peor.

**Otra forma:**

Estadístico de prueba Fo (Tr) = 15.064

Región crítica: Es una curva de Fisher en el primer cuadrante y que se sombrea por su derecha, a partir de un punto llamado Valor crítico.

Valor Crítico: VC=F(1-alfa, k-1, (k-1)(n-1))= F(0.95, 3, 105)

```{r}
qf(0.95, 3, 105)
```

Como Fo=15.064 \> VC entonces , cae en la zona sombreada y por ello Rechazo Ho: Los tipos de vino tendrían promedios distintos.

```         
```

**HIPÓTESIS SECUNDARIA:** igualdad de valoración para cada visitante

$$ Ho: \mu1=\mu2=\mu3=...=\mu36\\ Ha: \text{existe alguna media que es distinta a las otras} $$

Como Pvalor (Bloques)= 0.626\>Alfa ==\> no Rechazo Ho ==\> las valoraciones son iguales.

Los visitantes han calificado a los 4 tipos de vinos con un promedio similar.

# FIN.

**EXAMEN FINAL:** PROXIMO VIERNES 7:15

jueves: un breve repaso.

EXITOS A TODOS, EN SUS CURSOS.
