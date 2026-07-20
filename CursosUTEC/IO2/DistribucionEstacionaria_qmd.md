---
curso: IO2
titulo: DistribucionEstacionaria
slides: 0
fuente: DistribucionEstacionaria.qmd
---

---
title: "Distribución Estacionaria"
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.jpg
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
      transition: slide
editor: visual
date: "Mayo,2023"
---

## Objetivos: Distribución Estacionaria

-   Entender los conceptos de recurrencia nula y recurrencia positiva.

-   Definir la distribución estacionaria demostrando con ejemplos la utilidad de poderla encontrar.

-   Demostrar la existencia y unicidad de la estacionaria en el caso de Cadenas de Markov irreducibles y ergódicas.

-   Entender las distintas interpretaciones de la estacionaria en otros casos donde el Teorema de existencia y unicidad de la estacionaria no garantice su existencia.

-   Calcular los tiempos medios que la cadena pasa en estados transitorios.

## Recordemos recurrencia y transitoriedad

Para cualesquiera dos estados $i$ y $j$, definamos $f_{ij}^{(n)}$ como la probabilidad de que comenzando en el estado $i$, la primera transición al estado $j$ ocurre a tiempo $n$. Es decir,

$$f_{ij}^{(n)} = P\{X_{n} = j, X_{k} \neq j, k = 1, \ldots , n - 1\Big|X_{0} = i\}$$

Así,

$$f_{ij} = \sum_{n=1}^{+ \infty} f_{ij}^{(n)}$$

es la probabilidad de volver eventualmente al estado $j$, partiendo del estado $i$.

## Recurrencia y transitoriedad

Observe que $f_{ij}$ es positiva $\Leftrightarrow j \leftarrow i$

$$f_{ii} = f_{i}$$

Es decir, diremos que $i$ es un estado **recurrente** si

$$f_{ii} = 1$$

y diremos que es **transitorio** si

$$f_{ii} < 1$$

## Primera vez que la CM visita un estado

Sea

$$T_{i}=\min\{n > 0: X_{n}=i\}$$

Por lo que,

$$
f_{i}= \sum_{n=1}^{\infty}P\left(T_{i}=n\Big| X_{0}=i\right)\\1-f_{i}=P\left(T_{i}=\infty\Big|X_{0}=i\right)
$$

## Tiempo esperado hasta revisitar un estado

Sea

$$m_{i}\equiv E\left(T_{i}\Big|X_{0}=i\right)$$

Observe que cuando $f_{i} < 1$, entonces $m_{i}=\infty$

Sin embargo, cuando $f_{i}=1$, $m_{i}$ puede ser finito o infinito.

## Ejemplo:

Supongamos que

$$
\begin{align*}P(T_{i}=&n\Big| X_{0}=i)=\frac{1}{n(n+1)}\\f_{i}=&\sum_{n=1}^{\infty}\frac{1}{n(n+1)}\\     =&\lim_{m\rightarrow\infty}\sum_{n=1}^{m}\left[\frac{1}{n}-\frac{1}{n+1}\right]\\     =& \lim_{m\rightarrow\infty}\left(1-\frac{1}{m+1}\right)=1\end{align*}
$$

## Continuando con el ejemplo

$$
\begin{align*}m_{i}=&E\left(T_{i}\Big| X_{0}=i\right)\\     =&\sum_{n=1}^{\infty}nP\left(T_{i}=n\Big| X_{0}=i\right)\\     =&\sum_{n=1}^{\infty}\frac{n}{n(n+1)}\\     =& \sum_{n=1}^{\infty}\frac{1}{n+1}=\infty\end{align*}
$$

Es decir, que no necesariamente si $f_{i}=1$, el tiempo esperado de retorno al estado $i$ es finito.Por eso, la siguiente definición es oportuna.

## Recurrencia positiva y nula. Ergodicidad

Para un estado recurrente $i$, si

$$m_{i} < \infty$$

entonces diremos que el estado $i$ es **recurrente positivo**.

En caso contrario, diremos que el estado $i$ es **recurrente nulo**.

En una CM son conjunto de estados finito, todos los estados recurrentes son recurrentes positivos.

Un estado positivo recurrente y aperiódico es **ergódico**. Si todos los estados de CM son ergódicos, entonces la CM es ergódica.

## Proposición

El estado $i$ es **recurrente** si y solo si

$$\sum_{n=1}^{+\infty} P_{ii}^{(n)} = \infty$$

El estado $i$ es **transitorio** si y sólo si

$$\sum_{n=1}^{+\infty} P_{ii}^{(n)} < \infty$$

## Prueba:

El estado $j$ es recurrente si, con probabilidad 1, un proceso que comienza en $j$ volverá eventualmente a $j$.

Sin embargo, por la propiedad de Markov, el proceso comienza otra vez probabilísticamente cada vez que visita $j$. Es decir, con probabilidad 1, el proceso volverá a $j$. Repitiendo este argumento, vemos que el número de visitas a $j$, es $\infty$ con probabilidad 1. Como consecuencia, tendrá esperanza infinita. Por otro lado, supongamos que $j$ es transitorio. Entonces, cada vez que el proceso regresa $j$, hay una probabilidad $1 - f_{j}$ de que nunca regrese; es decir, el número de visitas es geométrico con esperanza finita $\frac{1}{(1-f_{j})}$.

## Ejemplo: Camino aleatorio simple

$P_{i,i+1} = p = 1-P_{i,i-1} \quad i = 0, \pm 1, \pm 2, \ldots$ donde $0 < p < 1$. Claramente, esta cadena es irreducible. Por lo tanto, es suficiente con ver si $\sum_{n=1}^{+\infty} P_{00}^{(n)}$ es finita o infinita.

$$
\begin{align*}&P_{00}^{(2n+1)} = 0\\  &P_{00}^{(2n)}=\binom{2n}{n}p^{n}(1-p)^n\end{align*}
$$

para $n=1,2,\cdots$.

## Fórmula de Stirling

$$
n! \sim n^{n+\frac{1}{2}}e^{-n}\sqrt{2\pi}\\ \text{ donde diremos que las sucesiones }\\a_{n}\sim b_{n} \text{ cuando }\\\lim_{n\to +\infty} \frac{a_n}{b_n}=1
$$

## Continuando con el ejemplo del paseo aleatorio

$\therefore P_{00}^{(2n)} = \frac{(2n)!}{n!n!} p^n(1-p)^n\sim \frac{(2n)^{2n+\frac{1}{2}} e^{-2n} \sqrt{2\pi}}{n^{n+\frac{1}{2}} n^{n+\frac{1}{2}} e^{-2n} 2\pi} = \frac{2^{2n+\frac{1}{2}}p^n(1-p)^n}{n^{\frac{1}{2}} \sqrt{2\pi}}=\frac{[4p(1-p)]^n}{\sqrt{\pi n}}$

$P_{00}^{(2n)}\sim \frac{[4p(1-p)]^n}{\sqrt{\pi n}} \quad \text{ y como si } \lim_{n\to +\infty} \frac{a_n}{b_n} = 1$

$\Rightarrow \sum_{n=1}^{+\infty} a_n\prec +\infty \text{ si y solo si } \sum_{n=1}^{+\infty} b_n\prec +\infty$.

## 

Entonces, para estudiar la convergencia de $\sum_{n=1}^{+\infty} P_{00}^{(2n)}$ basta con estudiar la convergencia de $\sum_{n=1}^{+\infty}\frac{[4p(1-p)]^n}{\sqrt{\pi n}}$ la cual diverge si $p=\frac{1}{2}$ y converge si $p\neq\frac{1}{2}$

$\therefore$ la cadena es recurrente si $p=\frac{1}{2}$ y transitoria si $p\neq\frac{1}{2}$

## Distribución estacionaria

Para una CM **ergódica e irreducible**, el límite

$$\pi_{j} \equiv \lim_{n\to \infty}P_{ij}^{(n)} \quad j\geq 0$$

**existe**, es **independiente del estado inicial** $i$ y es la **única solución no negativa** del sistema de ecuaciones:

$$
\pi_{j} = \sum_{i \in S}\pi_{i}P_{ij}\\\text{   sujeto a la restricción }\\\sum_{j\in S}\pi_{j}=1
$$

## Observación 1)

Dado que $\pi_{j} = \lim_{n\to \infty}P_{ij}^{(n)}$ existe y es independiente del estado inicial $i$, entonces:

$$
\begin{align*}&P\left(X_{n}=j\right)=\sum_{i\in S}P\left(X_{n}=j\Big| X_{0}=i\right)P(X_{0}=i)\\&\text{tomando límite}\\&\lim_{n\rightarrow \infty}P\left(X_{n}=j\right)=\sum_{i\in S}\underbrace{\lim_{n\rightarrow\infty}P\left(X_{n}=j\Big| X_{0}=i\right)}_{\pi_{j}}P(X_{0}=i)\\&=\sum_{i\in S}\pi_{j}P(X_{0}=i)\\&=\pi_{j}\sum_{i\in S}P(X_{0}=i)=\pi_{j}\end{align*}
$$

## Observación 2):

Dado que $\pi_{j} = \lim_{n\to \infty}P_{ij}^{(n)}$ existe y es independiente del estado inicial $i$, entonces:

$$
\begin{align*}\pi_{j}=&\lim_{n\to \infty} P\left(X_{n+1}=j\right)\\=&\lim_{n\to \infty}\sum_{i\in S }^{\infty}P\left(X_{n+1}=j\Big|X_{n}=i\right)P\left(X_{n}=i\right)\\&\text{por estacionariedad de la CM}\\=& \sum_{i\in S}^{\infty}P_{ij}\lim_{n\to \infty}P(X_{n}=i)\\=& \sum_{i\in S}^{\infty}P_{ij}\pi_{i}\end{align*}
$$

## Observación 3)

De las observaciones 1) y 2) podemos deducir, **en el caso aperiódico**, que $\pi_{j}$, la probabilidad límite de que el proceso esté en el estado $j$ a tiempo $n$, también puede interpretarse como la proporción de tiempo que el proceso pasa en el estado $j$.

## Observación 4)

En el caso **irreducible**, **positivo recurrente** pero **periódico**, todavía tenemos que $\pi_j,j\geq 0$ es la solución única de

$\pi_{j} = \sum_{i\in S}^{\infty}\pi_{i}P_{ij}$

$\sum_{j\to 0}^{\infty}\pi_j=1$

Pero sólo puede interpretarse como la proporción de tiempo a largo plazo que la CM pasa en el estado $j$.

## Volvamos al ejemplo del clima

$X_{n} =$ clima en el día n

$S=\{\underbrace 1_{\text{soleado}}, \underbrace 2_{\text{lluvioso}}\}$

cuya matríz de transición venía dada por:

$$
\begin{equation*} \mathbb{P}=\begin{bmatrix}0.8 & 0.2\\0.7 & 0.3\end{bmatrix}\end{equation*}
$$

cuya cadena es irreducible, recurrente positiva y aperiódica.

Calcule la distribución estacionaria de $\{X_{n}, n\geq 0\}$

## Aplicando el teorema de la distribución estacionaria

La distribución estacionaria de $\{X_{n}, n\geq 0\}$,

$(\pi_{1},\pi_{2})$ es la única solución positiva del sistema de ecuaciones:

$$
\begin{equation*} \begin{bmatrix}\pi_1 & \pi_2\end{bmatrix}\begin{bmatrix}0.8 & 0.2\\0.7 & 0.3\end{bmatrix} =\begin{bmatrix}\pi_1 & \pi_2\end{bmatrix}\end{equation*}
$$

sujeto a la restricción:

$$\pi_{1}+\pi_{2}=1$$

## Resolviendo el sistema de ecuaciones:

$0.8 \pi_1 + 0.7\pi_2 = \pi_1$

$0.2 \pi_1 + 0.3\pi_2 = \pi_2$

$\pi_1 + \pi_2 = 1$

$$\Rightarrow \left[\pi_1,\pi_2\right] = \left[\frac{7}{9}, \frac{2}{9}\right]$$

## En R:

```{r echo=TRUE}
library(markovchain)

M = matrix(c(0.8, 0.2,

             0.7, 0.3), nrow=2, byrow = TRUE)

mc=new("markovchain", transitionMatrix=M, name = "Ejemplo Clima")

summary(mc)

```

## 

```{r echo=TRUE}
steadyStates(mc)
```

## Ejemplo cuando la CM es periódica

Consideremos la siguiente CM:

![](Cadena7.png){fig-align="center"}

cuya matriz de transición viene dada por:

$$
\begin{equation*} \mathbb{P}=\begin{bmatrix}0 & 1\\1 & 0\end{bmatrix}\end{equation*}
$$

## Calculemos algunas potencias de la matriz de transición

$$
\begin{equation*} \mathbb{P}^2=\begin{bmatrix}0 & 1\\1 & 0\end{bmatrix}\begin{bmatrix}0 & 1\\1 & 0\end{bmatrix} =\begin{bmatrix}1 & 0\\0 & 1\end{bmatrix}\end{equation*}
$$

$$
\begin{equation*} \mathbb{P}^3=\begin{bmatrix}1 & 0\\0 & 1\end{bmatrix}\begin{bmatrix}0 & 1\\1 & 0\end{bmatrix} =\begin{bmatrix}0 & 1\\1 & 0\end{bmatrix} = \mathbb{P}\end{equation*}
$$

## Es decir: {.scrollable}

$$
\begin{equation*} \mathbb{P}^{(n)} = \begin{cases} \mathbb{P} & \text{ n es impar  } \\ \mathbb{I} & \text{ n es par }  \end{cases}\end{equation*}
$$

Por lo tanto,

$$\lim_{n\to\infty} P_{ij}^{(n)} \text{ no existe}$$

Sin embargo, es intuitivo que la CM pasa la mitad del tiempo en el estado 0 y la otra mitad en el estado $1$.En efecto, $\left[\pi_{1}, \pi_{2}\right]=\left[\frac{1}{2},\frac{1}{2}\right]$ también satisface:

$$
\pi_{j} = \sum_{i \in S}\pi_{i}P_{ij}\\\text{   sujeto a la restricción }\\\sum_{j\in S}\pi_{j}=1
$$

## En el caso que la CM sea ergódica e irreducible

$$\pi_{j}=\text{ distribución límite de estar en el estado } j$$

$$
\pi_{j}\equiv\lim_{n\to\infty} P_{ij}^{(n)}\\=\lim_{n\to\infty}\frac{\text{ número de visitas al estado j por CM }}{n}
$$

puede también interpretarse como la proporción del tiempo que la CM pasa en el estado $j$.

## Caso irreducible,recurrente positivo pero periódico {.scrollable}

$\pi_{j}$ también satisface:

$$
\pi_{j} = \sum_{i \in S}\pi_{i}P_{ij}\\\text{   sujeto a la restricción }\\\sum_{j\in S}\pi_{j}=1
$$

pero ahora la única interpretación posible es:

$$\pi_{j}=\text{ fracción de tiempo que la CM gasta en el estado } j$$

Es decir, **la periodicidad solo afecta la interpretación de** $\pi_j, \quad \forall j\in S$

## ¿Qué hacemos si la cadena no es irreducible? {.scrollable}

$$
\begin{equation*} \mathbb{P}=\begin{bmatrix}0 & 0 & 0 & 1 \\0 & 1 & 0 & 0 \\0 & 1/3 & 1/3 & 1/3 \\ 1 & 0 & 0 & 0\end{bmatrix}\end{equation*}
$$

$R_{1}=\{1\}$ ergódica $\implies \pi_{1}=1$

$R_{2} = \{0,3\}$ periódica

$\pi_{0} + \pi_{3}=1$

$\sum_{k\in R_2} \pi_k P_{kj}=\pi_j \quad \forall j\in R_2$

$\pi_0 P_{03} + \pi_3 P_{33}= \pi_3$

$\pi_0=\pi_3=\frac{1}{2}$

$T=\{2\}$ transitoria $\Leftarrow \pi_{2} = 0$

Es decir, todavía es posible estudiar el comportamiento a largo plazo de CM reducibles.

## ¿Qué aprendimos hoy?
