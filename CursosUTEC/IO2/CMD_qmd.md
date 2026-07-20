---
curso: IO2
titulo: CMD
slides: 0
fuente: CMD.qmd
---

---
title: "Introducción a las Cadenas de Markov Discretas"
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC.JPEG
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
      transition: slide
editor: visual
date: "Junio,2023"
---

## Objetivos: Cadenas de Markov discretas

-   Caracterizar las cadenas de Markov estacionarias y discretas en términos de **la matriz de transición y de la distribución inicial**.

-   Ejemplificar las cadenas de Markov estacionarias y discretas con ejemplos propios de operaciones de la ingeniería industrial.

## Definición Cadena de Markov discreta {.scrollable}

Diremos que un proceso estocástico $\{X_n, n \geq 0\}$ es una **Cadena de Markov a tiempo discreto con espacio de estado** $S$ si:

-   Para todo $n\geq 0$, $X_{n} \in S$ con probabilidad $1$

-   Para todo $n\geq 0$, $x \in S$, $A \subset S$ y $B \subset S^n$,

se cumple que:

$$
\begin{align*}P\left(X_{n+1} \in A\Big|X_{n} = x, \left(X_{o},\ldots,X_{n-1}\right) \in B\right)&=\\\\=P\left(X_{n+1}\in A\Big|X_n=x\right)\end{align*}
$$

En dónde a esta última propiedad se le conoce como la **propiedad Markoviana**.

## Cadenas de Markov con espacio de estados discreto

Cuando el conjunto de estados $S$ es contable, la propiedad Markoviana se puede simplificar así:

$$
\begin{align*}&P(\underbrace {X_{n+1}=j}_{\text{futuro}}\Big|\underbrace {X_n=i}_{\text{presente}}, \underbrace {X_{n-1}= i_{n-1}, \ldots, X_0=i_0}_{\text{pasado}})\\ &\quad = P(\underbrace {X_{n+1}=j}_{\text{futuro}}|\underbrace {X_n=i}_{\text{presente}})\\\end{align*}
$$

$\forall$ $n \geq 0, i,j \quad i_{o},\ldots,i_{n-1}\in S$.

## Probabilidad de transición en un paso a tiempo n

$$P_{ij}(n)\equiv P\left(X_{n+1} =j\Big|X_{n} = i\right)\\$$

a la probabilidad de que la cadena $\{X_n, n \geq 0\}$ cambie del estado $i$ a tiempo $n$ al estado $j$ a tiempo $n+1$.

## Cadena de Markov homogénea en el tiempo {.scrollable}

-   Diremos que una CMTD $\{X_n, n \geq 0\}$ es **homogénea o estacionaria** en el tiempo si las probabilidades condicionales

$$P\left(X_{n+1} \in A\Big|X_{n} =x\right)$$

no dependen de $n$, $\forall x \in S$ y todo subconjunto $A \subset S$.

-   En particular, una CMTD $\{X_n, n \geq 0\}$ con espacio de estados $S$ contable diremos que es **homogénea en el tiempo** si

$$P_{ij}(n)=P_{ij}\quad \forall n \geq 0, i, j \in S.$$

**Observación:** a partir de ahora supondremos que una CMTD es un proceso estocástico Markoviano y homogéneo en el tiempo.

-   Llamaremos a $\mathbb{P}=\left[P_{ij}\right]$ **la matriz de transición en un paso** de la cadena de Markov $\{X_{n}, n\geq 0\}$.

## Definición matriz estocástica

-   Diremos que una **matriz** $\mathbb{A}=[a_{ij}]$ es **estocástica** si satisface que:

i)  

$$a_{ij} \geq 0 \quad \forall i,j \in S$$

ii) 

$$\sum_{j\in S}a_{ij} = 1 \quad i \in S$$

## Teorema:

**La matriz de transición en un paso de una CMTD es estocástica**.

## Prueba:

En efecto,

$$P_{ij}=P\left(X_{n+1} =j\Big|X_{n} = i\right) \geq 0$$

por ser una probabilidad.

y

$$
\begin{align*} \sum_{j\in S}P_{ij} &=\sum_{j\in S} P\left(X_{n+1}=j\Big|X_n = i\right)\\                             &= P\left(X_{n+1} \in S\Big|X_n = i\right)=1\\ \end{align*}
$$

pues la probabilidad de que la cadena $\{X_n, n \geq 0\}$ cambie del estado $i$ a cualquier otro estado en $S$ en un sólo paso es 1.

## Caracterización de una cadena de Markov

Definamos

$$\alpha _{i} \equiv P\left(X_{o}=i\right) \quad \forall i\in S$$\$

la **distribución inicial** de la CMTD.

y

$$\mathbb{P}=\left[P_{ij}\right]$$

**la matriz de transición en un paso** de la cadena de Markov $\{X_{n}, n\geq 0\}$.

Una CMTD $\{X_n, n \geq 0\}$ está completamente caracterizada por **la distribución inicial** $\mathbb{\alpha}$, y la **matriz de transición en un paso** $\mathbb{P}$.

## Prueba:

Observe que:

$$
\begin{align*}&P\left(X_{o}=i_{o}\right)=\alpha_{i_{o}}\\\\&P\left(X_{o}=i_{o}, X_{1}=i_{1}\right)\\ =&P\left(X_{1}=i_{1}\Big|X_{o}=i_{o}\right)P\left(X_{o}=i_{o}\right)\\=& P_{i_{o} i_{1}} \alpha_{i_{o}}\end{align*}
$$

Ahora, asuma por **hipótesis inductiva** que lo siguiente es cierto:

$$P\left(X_{o}=i_{o},\ldots,X_{k}=i_{k}\right)=P_{i_{k-1} i_{k}}\ldots P_{i_{1} i_{2}} P_{i_{o} i_{1}} \alpha_{i_{o}}$$

para $k=1,2,\ldots,n-1$.

## ¿Será cierto que la propiedad anterior se cumple siempre?

$$
\begin{align*}&P\left(X_{o}=i_{o},\ldots,X_{n}=i_{n}\right)\\&=P\left(X_{n}=i_{n}\Big|X_{n-1}=i_{n-1},\ldots, X_{o}=i_{o}\right)P\left(X_{n-1}=i_{n-1}, \ldots,X_{o}=i_{o}\right)\\                         & \text{(por la propiedad de Markov)}\\                         &= P\left(X_{n}=i_n\Big|X_{n-1}=i_{n-1}\right) P\left(X_{n-1}=i_{n-1}, \ldots,  X_{o}=i_{o}\right)\\                         & \text{(por hipótesis inductiva evaluada en $k=n-1$)}\\                         &= P_{i_{n-1} i_{n}}P_{i_{n-2} i_{n-1}}\ldots P_{i_{o} i_{1}}\alpha_{i_{o}}  \end{align*}
$$

## Ejemplo: Pronóstico del clima

**Considere un modelo simple de pronóstico del clima en el que se clasifica el clima del día como "soleado" o "lluvioso". Sobre la base de datos anteriores, hemos determinado que, si está soleado hoy, existe un 80% de posibilidades de que esté soleado mañana, independientemente del tiempo pasado, mientras que si está lluvioso hoy hay un 30% de posibilidades de que llueva mañana sin importar el pasado.**

## Solución: {.scrollable}

Definamos el siguiente proceso estocástico $X_n=$ el clima en el día n. Claremente, su conjunto de estados es $S=\{\underbrace 1_{\text{soleado}}, \underbrace 2_{\text{lluvioso}}\}$ y su matríz de transión en un paso viene dada por:

$$
\mathbb{P}=\begin{bmatrix}0.8 & 0.2\\0.7 & 0.3\end{bmatrix}
$$

Como no nos dan información sobre la distribución inicial podríamos tomar la decisión de que la distribución inicial sea:

$$
\mathbb{\alpha}=\begin{bmatrix}0.5 & 0.5\end{bmatrix}
$$

bajo el escenario de máxima incertidumbre sobre cuál es la probabilidad incondicional de que un día sea soleado o lluvioso respectivamente.

## Algunas cuentas sobre el mismo ejemplo:

**¿Cuál es la probabilidad de que el día 1 sea soleado?**

$$
\begin{align*}&P(X_{1}=1)\\=& P(X_{1}=1\Big| X_{0}=1)P(X_{0}=1)+ P(X_{1}=1\Big| X_{0}=2)P(X_{0}=2)\\=& P_{11}\alpha_{1}+P_{21}\alpha_{2}\\=& (0.8)(0.5)+(0.7)(0.5)=0.75\end{align*}
$$

## Ejemplo: El problema de la ruina del jugador

**Considere dos jugadores, A y B, que tienen una fortuna combinada de N soles. Apuestan un sol cada uno al lanzar una moneda. Si en la moneda sale cara, el jugador A gana un sol del jugador B, y si en la moneda sale cruz, B gana un sol del jugador A. Supongamos que los lanzamientos sucesivos de la moneda son independientes y que en la moneda aparece cara con probabilidad p y cruz con probabilidad q = 1-p. El juego finaliza si A o B quiebra. Supongamos que las probabilidad de que el jugador comience con un capital entre 1 y N-1 es 1.**

## Solución: {.scrollable}

Sea

$$X_{n}= \text{ fortuna del jugador A después del n-ésimo lanzamiento}$$

El juego termina cuando $X_{n}=0$ o $X_{n}=N$ a partir de ese momento definiremos $X_{k}=X_{n}$ para todo $k\geq n$.

Si $0 < X_n < N$ tenemos:

$$
\begin{equation*} X_{n+1} = \begin{cases}X_{n}+1 & \text{ con probabilidad  } p \\X_{n}-1 & \text{ con probabilidad } q=1-p \end{cases} \end{equation*}
$$

$\{X_n, n \geq 0\}$ es una CMTD.

$$
\alpha_{i}=P(X_{0}=i)=\begin{cases}           \frac{1}{N-1} & \text{ si }i=1,2,\cdots, N-1\\           0             & \text{ si }i=0, N.           \end{cases}
$$

## Continuando con el ejemplo:

En términos de las probabilidades de transición:

$$
\begin{align*}&P\left(X_{n+1}=i\Big|X_n=i+1\right)=q \quad 0 < i < N \\ &P\left(X_{n+1}=i\Big|X_n=i-1\right)=p \quad 0 < i < N \\ &P\left(X_{k}=0\Big|X_n=0\right)=1 \quad \forall k\geq n \\&P\left(X_{k}=N\Big|X_n=N\right)=1 \quad \forall k\geq n \\\end{align*}
$$

que matricialmente...

## Matriz de transición en un paso:

$$
\begin{equation*} \mathbb{P}=\begin{bmatrix}1 & 0 & 0 & \ldots & \ldots & \ldots & \ldots & 0 \\q & 0 & p & 0 & \ldots & \ldots & \ldots & 0 \\0 & q & 0 & p & 0 & \ldots & \ldots & \ldots \\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\0 & \ldots & \ldots & \ldots & \ldots & q & 0 & p \\0 & 0 & 0 & \ldots & \ldots & \ldots & 0 & 1\end{bmatrix}\end{equation*}
$$

## Ejemplo 3: Sistema de inventario sujeto a una demanda determinística.

**Un periódico usa una tonelada de papel periódico todos los días. Compra su periódico con un distribuidor local. Este distribuidor suministra el papel de periódico en rollos de una tonelada al precio más barato, pero desafortunadamente sus entregas son erráticas. Por lo tanto, la cantidad de rollos de papel periódico en el almacén de periódicos varía de manera aleatoria. Si en un día particular, no hay rollos en el almacén, entonces el periódico compra un rollo a un proveedor de emergencia (y más costoso) para satisfacer los requisitos para ese día en particular. Queremos modelar el inventario de rollos de papel de periódico en el almacén de periódicos como una cadena de Markov discreta.**

## Solución:

Sea $Y_{n}=$ número de rollos recibidos del distribuidor local en el día $n$. Suponemos que el suministro llega por la noche, mientras que la tonelada de papel se consume por la mañana.

$X_{n}=$ número de rollos en el almacén al comienzo del día $n$ antes de que se haya satisfecho la demanda de una tonelada y haya llegado el suministro para el día $n$.

$$
\begin{equation*} X_{n+1} = \begin{cases}X_{n} - \underbrace {1}_{\text{demanda}} + \underbrace {Y_n}_{\text{suministro regular}} &\text{ si } X_{n} > 0 \\Y_{n} & \text{ si } X_{n}=0
\end{cases}
\end{equation*}
$$

## 

Ahora, supongamos que $\{Y_{n},n\geq 0\}$ es una sucesión de v.a. i.i.d. con función de probabilidad de masa dada por

$$a_{k}=P(Y_{n}=k) \quad k=0,1,2,\ldots$$

Tenemos que demostrar que $\{X_{n}:n\geq 0\}$ es una CMTD.

$$
\begin{align}
&P\left(X_{n+1}=j\Big|X_{n}=0,X_{n-1}=i_{n-1},\ldots,X_{o}=i_{o}\right)\\ &=P\left(Y_n=j\Big|X_{n}=0,X_{n-1}=i_{n-1},\ldots,X_{o}=i_{o}\right)\\ &=P\left(Y_{n}=j\right) = a_{j}
\end{align}
$$

## Continuando con el ejemplo:

Similarmente, para $i > 0$,

$$
\begin{align*}&P\left(X_{n+1}=j\Big|X_{n}=i,X_{n-1}=i_{n-1},\ldots,X_{o}=i_{o}\right)\\=&P\left(X_{n} -1+Y_{n}=j\Big|X_{n}=i,X_{n-1}=i_{n-1},\ldots,X_{o}=i_{o}\right)\\=&P\left(Y_{n}=j-i+1\Big|X_{n}=i,X_{n-1}=i_{n-1},\ldots,X_{o}=i_{o}\right)\\=&P(Y_{n}=j-i+1) = a_{j-i+1}\end{align*}
$$

Luego, $\{X_n,n\geq 0\}$ es una CMTD.

## La matriz de transición en un paso queda así:

$$
\begin{equation*}\mathbb{P}=\begin{bmatrix}a_o & a_1 & a_2 & a_3 & \ldots & \ldots \\a_o & a_1 & a_2 & a_3 & \ldots & \ldots \\0 & a_o & a_1 & a_2 & \ldots & \ldots \\\vdots & \vdots & \ddots & \ddots & \ddots & \ldots \\\ldots & \ldots & \ldots & a_o & a_1 & a_2 \\\end{bmatrix}\end{equation*}
$$

## ¿Qué hacemos con estos modelos?

Queremos calcular la distribución marginal de $X_{n}$. Sea

$$
\begin{align*}\alpha_j^{(n)}=&P\left(X_{n}=j\right)\\=&\sum_{i\in S} P\left(X_{n}=j\Big|X_{o}=i\right)P\left(X_{o}=i\right)\\=& \sum_{i \in S} P\left(X_{n}=j\Big|X_{o}=i\right) \alpha_{i}\\=& \sum_{i \in S}P_{ij}^{(n)}\alpha_{i}\end{align*}
$$

## Probabilidad de transición en n pasos

A $P_{ij}^{(n)}$ la llamaremos **la probabilidad de transición en \$n\$-pasos** del estado $i$ al estado $j$

$$P_{ij}^{(n)}\equiv P\left(X_{n}=j\Big|X_{o}=i\right) \quad \forall i,j \in S$$

Si sabemos calcular $P_{ij}^{(n)}$, podremos calcular la distribución marginal de $X_n$.

## ¿Qué aprendimos hoy?
