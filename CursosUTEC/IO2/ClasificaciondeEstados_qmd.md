---
curso: IO2
titulo: ClasificaciondeEstados
slides: 0
fuente: ClasificaciondeEstados.qmd
---

---
title: "Clasificación de los Estados de Cadenas de Markov Discretas"
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.jpg
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
      transition: slide
editor: visual
date: "Junio,2023"
---

## Objetivos: Clasificación de los estados

-   Clasificar los estados de las cadenas de Markov con miras al cálculo de la distribución estacionaria en los casos en los que sea posible. Interpretar los resultados en cada ejemplo.

## Accesibilidad

Diremos que el estado $j$ es **accesible** desde el estado $i$ si existe $n\geq 0$ tal que $P_{ij}^{(n)} > 0$.

![](Cadena6.png){fig-align="center" width="359"}

Es decir, en el diagrama de transición existe un camino, no necesariamente de un sólo paso, que partiendo del estado $i$ llegue al estado $j$.

## Comunicación:

Si

$$i \rightarrow j$$

$j$ es accesible desde $i$

e $i$ es accesible desde $j$

$$j \rightarrow i,$$

entonces diremos que los estados $i$ y $j$ se **comunican** y lo escribiremos así:

$$i \leftrightarrow j$$

## Propiedades de la comunicación

1\) La comunicación es una relación **reflexiva**:

$$
 i \leftrightarrow i\\\text{ es decir  } i \text{ se comunica con } i \text{ en }  n=0 \text{ pasos }
$$

2\) La comunicación es una relación **simétrica**:

$$i\leftrightarrow j \text{ entonces } j \leftrightarrow i$$

3\) La comunicación es una relación **transitiva**:

$$
\text{Si }i\leftrightarrow j \text{ y } j\leftrightarrow k\\\text{ entonces } i\leftrightarrow k
$$

## La comunicación es una relación transitiva:

$$
\underbrace{i\leftrightarrow j}_{\exists n_1,n_2 \text{ tal que } P_{ij}^{(n_1)} > 0 \text{ y } P_{ji}^{(n_2)} > 0} \text{ y } \underbrace{j\leftrightarrow k}_{\exists m_1,m_2 \text{ tal que } P_{jk}^{(m_1)} > 0 \text{ y } P_{kj}^{(m_2)}>0}\\\text{ entonces }\\P_{ik}^{(n_{1}+m_{1})}=\sum_{j\in S}P_{ij}^{(n_{1})}P_{jk}^{(m_{1})} > 0 \\ P_{ki}^{(m_{2}+n_{2})}=\sum_{j\in S}P_{kj}^{(m_{2})}P_{ji}^{(n_{2})} > 0
$$

entonces $i\leftrightarrow k$

## Observaciones sobre las propiedades de la comunicación:

-   En cualquier relación en la cual se satisfagan estas tres propiedades: reflexividad, simetría y transitividad, diremos que la relación es una **relación de equivalencia**.

-   Cualesquiera dos estados que se comuniquen diremos que pertenecen a la misma **clase de equivalencia**.

-   Cada estado pertenece única y exclusivamente a una clase.

-   Si una cadena de Markov posee una única clase, diremos que la CM es **irreducible**. De lo contrario, diremos que es **reducible**.

## Ejemplo 1)

Consideremos la siguiente CM con matriz de transición dada por:

$$
\begin{equation*} \mathbb{P}=\begin{bmatrix}1/2 & 0 & 1/2 \\1 & 0 & 0 \\1/3 & 1/3 & 1/3 \end{bmatrix}\end{equation*}
$$

![](Cadena1.png){fig-align="center"}

## Ejemplo 2)

Consideremos la CM con matriz de transición dada por:

$$
\begin{equation*} \mathbb{P}=\begin{bmatrix}0 & 0 & 0 & 1 \\0 & 1 & 0 & 0 \\0 & 1/3 & 1/3 & 1/3 \\ 1 & 0 & 0 & 0\end{bmatrix}\end{equation*}
$$

![](Cadena2.png){fig-align="center"}

## Recurrencia y transitoriedad

Definamos $f_{i}=$ la probabilidad de que comenzando en el estado $i$, la CM eventualmente regrese a $i$ $\forall i \in S$.

Diremos que el estado $i$ es **recurrente** si $f_{i}=1$

Diremos que el estado $i$ es **transitorio** si $f_{i} < 1$

## Volviendo al Ejemplo 2)

![](Cadena2.png){fig-align="center"}

$f_{0}=1 \quad f_{1}=1 \quad f_{2}=1/3 \quad f_{3} =1$

$\{0,3\} \text{ es recurrente } \\ \{1\} \text{ es recurrente } \\ \{2\} \text{ es transitorio}$

## Ejemplo 4)

![](Cadena8.png){fig-align="center"}

$$
\begin{align*}&f_{1}=\frac{1}{3}+ \frac{1}{2}\frac{1}{2}=\frac{7}{12} < 1\\&f_{3}=\frac{2}{3}+\left[\frac{1}{3}\right]^{2}\sum_{k=0}^{\infty}\left[\frac{2}{3}\right]^{k}\\=&\frac{2}{3}+\left[\frac{1}{3}\right]^{2}\frac{1}{1-\frac{2}{3}}=1\end{align*}
$$

## Observaciones sobre la recurrrencia y la transitividad

Sobre **el número de visitas al estado**:

-   Si el estado $i$ es recurrente, entonces dado que la CM comienza en el estado $i$, el estado $i$ será visitado infinitas veces.

-   Si el estado $i$ es transitorio, será visitado solamente un número finito de veces.

-   La distribución del número de veces que un estado transitorio $i$ es visitado dado que la CM comienza en $i$ es geométrica con parámetro $p=1-f_{i}$

$$P(\text{# de visitas} = n)=f_{i}^n (1-f_{i}) \quad \forall n > 0$$

## Observaciones sobre la transitoriedad y la recurrencia

Sobre el **número de estados de la cadena**:

-   En una CM con un conjunto de estados finito, no todos los estados pueden ser transitorios.

-   **La transitoriedad y la recurrencia son propiedades de la clase**.

-   Todos los estados en una CM con conjunto de estados finito e irreducible son recurrentes.

## Absorción:

Diremos que el estado $i$ es **absorbente** si

$$P_{ii}=1$$

**La absorción también es una propiedad de clase**.

## Volviendo al Ejemplo 1)

![](Cadena1.png){fig-align="center"}

No hay estados absorbentes

## Volviendo al Ejemplo 2)

![](Cadena2.png){fig-align="center"}

El estado $\{1\}$ es absorbente.

## Periodicidad

Diremos que el estado i es **periódico** con período $d > 1$ si $P_{ii}^{(n)} > 0$ solamente cuando $n$ es divisible por $d$ y $d$ es el entero más grande con esta propiedad.

Si $d=1$ es el entero más grande que divide todo $n$ tal que $P_{ii}^{(n)}>0$, entonces diremos que el estado $i$ es aperiódico.

**La periodicidad es también una propiedad de la clase**.

## Explicación:

Si en una cadena puedes ir del estado $i$ al estado $i$ en los siguientes números de pasos, $(2,4,8, \ldots)$, entonces el entero más grande que divide a todos estos números es $2$.

Es decir el $d(i)=MCD{(2,4,8, \ldots)}=2$.

Es ese caso diríamos que **el estado** $i$ **es periódico con período** $d(i)=2$. Todos los estados en la misma clase que $i$ serían periódicos período $2$ y también diremos que la **clase a la cuál pertenece el estado** $i$ **es periódica, período** $2$.

## Ejemplo 3)

![](Cadena3.png){fig-align="center"}

## Ejemplo 4)

![](Cadena4.png){fig-align="center"}

## Ejemplo 5)

![](Cadena10.PNG){fig-align="center"}

## Ergodicidad:

Diremos que un estado positivo recurrente y aperiódico es **ergódico**.

Si todos los estados de CM son ergódicos, entonces la CM es ergódica. **La ergodicidad es también una propiedad de clase**.

## ¿Qué aprendimos hoy?
