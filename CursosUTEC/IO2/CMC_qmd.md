---
curso: IO2
titulo: CMC
slides: 0
fuente: CMC.qmd
---

---
title: "Cadenas de Markov a tiempo continuo"
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.jpg
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
      transition: slide
editor: source
date: "Junio, 2024"
---

## Objetivos: Cadenas de Markov a tiempo continuo

-   Definir y modelar una Cadena de Markov a **tiempo continuo**.

-   Modelar procesos de nacimiento y muerte

## Definición de una Cadena de Markov estacionaria a tiempo continuo. {.scrollable}

Suponga que $\lbrace X(t), t\geq 0\rbrace$ es un proceso estocástico a tiempo continuo que toma valores en los enteros no negativos. Decimos que $\lbrace X(t), t\geq 0\rbrace$ es una cadena de Markov a tiempo continuo (CMTC) si $\forall s,t \geq 0$, los enteros no negativos $i,j\in S$, el conjunto de estados, y $X(u)$ $(0\leq u \leq s)$ cumplen que:

`
\begin{align*}
&P\left(\underbrace {X(t+s)=j}_{\text{futuro}}\left|\right.\underbrace {X(s)=i}_{\text{presente}}, \underbrace {X(u)= x(u)}_{\text{pasado}}\right)\\
=& P\left(\underbrace {X(t+s)=j}_{\text{futuro}}|\underbrace {X(s)=i}_{\text{presente}}\right)\\
\end{align*}

## Para que la cadena de Markov continua sea estacionaria

Pediremos que


\begin{align*}
P_{ij}(t) =& P\left(X(t+s)=j\left|\right.X(s)=i\right)\\\\
          =& P\left(X(t)=j\left|\right.X(0)=i\right)
\end{align*}

sea **independiente de** $s$, para que la CMTC sea **estacionaria**.

## Tiempo que el proceso se queda en un estado $i$ {.scrollable}

Observe que la probabilidad de que el proceso se quede en $i$ después de $t$ unidades de tiempo es:

$$
P\left(X(t+s)=i\left|\right.X(s)=i\right) = P\left(X(t)=i\left|\right.X(0)=i\right)
$$

Ahora si definimos $T_{i}$ como la **cantidad de tiempo que el proceso se queda en el estado** $i$ **antes de pasar a otro estado,** entonces la ecuación anterior es equivalente a la siguiente:

$$
P\left(T_{i}>t+s\left|\right.T_{i}>s\right) = P(T_{i} > t)
$$

la cual es la conocida **propiedad débil de pérdida de memoria**.

## Distribución del tiempo que la cadena transcurre en el estado i

Como $T_i$ es una variable aleatoria continua, entonces ésta debe modelarse como una variable aleatoria exponencial pues ésta es la única variable aleatoria que satisface la propiedad de pérdida de la memoria. Digamos entonces que $T_i \sim exp(\upsilon_i)$ donde $\upsilon_i$ es la **tasa de transición desde el estado** $i$ .

## Definición alternativa de una CMTC {.scrollable}

Se define cómo un proceso estocástico tal que cuando entra en el **estado** $i\in S$**,**

1.  La cantidad de tiempo que la cadena transcurre en el estado $i\in S$ antes de hacer una transición a otro estado en el conjunto de estados es una variable aleatoria exponencial tasa $\upsilon_{i}$

2.  Cuando la cadena deja el estado $i\in S$, hará una transición al estado $j\in S$ con probabilidad $P_{ij}$ en donde las mismas deben satisfacer que


\begin{align*}
&\text{2.1)} P_{ii}=0 \quad \forall i\in S\\\\
&\text{2.2)} \sum_{j\in S} P_{ij} =1\\
\end{align*}

## Ejemplo 1: Puesto de limpiabotas con dos sillas

![](ejemplo1.jpg)

## Enunciado:

Los tiempos de servicio en las dos sillas son variables aleatorias exponenciales independientemente distribuidas con tasas $\mu_1$ y $\mu_2$ respectivamente. Suponga que los clientes llegan con respecto a un $PPH(\lambda)$, pero cuando un cliente llegue, sólo será servido si ambas sillas están vacías.

## ¿Quién es $X(t)$ y cuál es el conjunto de estados?

$X(t)\equiv$ el estado del sistema a tiempo $t$.

| Estado | Interpretación                               |
|--------|----------------------------------------------|
| 0      | El limpiabotas está desocupado               |
| 1      | El limpiabotas está atendiendo en la silla 1 |
| 2      | El limpiabotas está atendiendo en la silla 2 |

Por lo tanto, el conjunto de estados $S=\{0,1,2\}$

## Solución: {.scrollable}

$\upsilon_{0}=$ tasa de transición desde el estado $0$ coincide con la tasa de llegada del primer cliente $\lambda$ . De manera similar, podemos calcular las tasas a las que la cadena deja los estados $1$ y $2$


\begin{align*}
&\upsilon_{0}=\lambda\\
&\upsilon_{1}=\mu_{1}\\
&\upsilon_{2}=\mu_{2}\\
\end{align*}

Note que se trata de una CMTC pues el tiempo de llegada del primer cliente es $exp(\lambda)$. De la misma forma, los tiempos de servicio en cada servidor se distribuyen exponenciales con tasas $\mu_{1}$ y $\mu_{2}$ respectivamente.

## Con respecto a la matriz de transición de la CMTC

La misma viene dada por:

$$
\mathbb{P}=\begin{bmatrix}
           0 & 1 & 0\\
           0 & 0 & 1\\
           1 & 0 & 0
           \end{bmatrix}
$$

## Justificación del cálculo de la matriz de transición:

Está claro que $P_{01} = P_{12} = P_{20} = 1$ pues cuando llega un cliente y ambas sillas están desocupadas, el mismo entra de frente a ocupar la primera silla con probabilidad 1. Cuando el servicio que recibe en la silla 1 termina, pasa de frente al servicio en la silla dos con probabilidad 1 y cuando este servicio termina se va, dejando el sistema vacío nuevamente con probabilidad 1. Por lo que la matriz de transición $\mathbb{P}$ viene dada por:

## Ejemplo 2: M/M/2/2

Ahora asumamos que tenemos dos canales de servicio idénticos por lo que cuando llega un cliente puede ser atendido por cualquiera de los servidores siempre que el mismo se encuentre desocupado. Asumiremos que las llegadas de clientes siguen un $PPH(\lambda)$ y que los tiempos de servicio en cada silla son independientes e idénticamente distribuidos exponencial con tasa $\mu$. Modele esta situación como una CMTC.

## ¿Quién es $X(t)$ y cuál es el conjunto de estados?

$X(t)=$ número de servidores ocupados a tiempo $t$

Por lo que el conjunto de estados viene dado por $S=\{0,1,2\}$

## Con respecto a la matriz de transición:

La misma viene dada por:

$$
\mathbb{P}=\begin{bmatrix}
           0                       & 1 & 0\\ 
           \frac{\mu}{\mu+\lambda} & 0 & \frac{\lambda}{\mu+\lambda}\\
           0                       & 1 & 0
           \end{bmatrix}
$$

## Justificación del cálculo de la matriz de transición:

Cuando ambos servidores están desocupados, sabemos que ocurrirá una llegada con probabilidad 1. Por eso, $P_{01}=1$. Por otro lado, si hay un servidor ocupado, entonces la cadena puede hacer una transición o al estado $0$, en caso el servidor termine su servicio antes de que llegue un cliente, o hacia al estado $2$, en caso llegue un cliente antes que el servidor ocupado termine su servicio. Por lo tanto, $P_{10}=\frac{\mu}{\mu+\lambda}$ y $P_{12}=\frac{\lambda}{\mu+\lambda}$. Cuando ambos servidores están ocupados, uno de ellos se desocupará con probabilidad 1. Por lo tanto, sólo puede ocurrir una transición del estado 2 al estado 1 con probabilidad 1. Note que la probabilidad de que ambos servidores se desocupen al mismo tiempo es cero.

## Con respcto a las tasas: {.scrollable}

$\upsilon_{0}=$ tasa de transición desde el estado $0$ coincide con la tasa de llegada del primer cliente $\lambda$ . De manera similar, podemos calcular las tasas a las que la cadena deja los estados $1$ y $2$


\begin{align*}
&\upsilon_{0}=\lambda\\
&\upsilon_{1}= \text{tasa}\left(\min\{\exp{(\mu)},\exp{(\lambda)}\}\right)=\mu+\lambda\\
&\upsilon_{2}= \text{tasa}\left(\min\{\exp{(\mu)},\exp{(\mu)}\}\right)=2\mu\\
\end{align*}

Por lo tanto, note que


\begin{align*}
&T_{0}\sim\exp{(\lambda)}\\
&T_{1}\sim\exp{(\mu+\lambda)}\\
&T_{2}\sim\exp{(2\mu)}
\end{align*}


## ¿Qué aprendimos hoy?
