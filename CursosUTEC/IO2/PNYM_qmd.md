---
curso: IO2
titulo: PNYM
slides: 0
fuente: PNYM.qmd
---

---
title: "Procesos de nacimiento y muerte"
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.jpg
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
      transition: slide
editor: source
date: "Julio, 2024"
---

## Objetivos: Procesos de nacimiento y muerte

-   Caracterizar los **procesos de nacimiento y muerte** como ejemplos de cadenas de Markov a tiempo continuo

## Procesos de nacimiento y muerte

Un proceso de **nacimiento y muerte** es tal que si hay $n$ personas en el sistema, entonces:

1.  El tiempo entre llegadas al sistema (nacimientos) $\sim \exp(\lambda_{n})$

2.  El tiempo entre salidas del sistema (muertes) $\sim exp(\mu_{n})$

**Donde los nacimientos y las muertes son independientes**

-   Note que $\lambda_n$ es la **tasa de que ocurra un nacimiento cuando la población tiene** $n$ individuos.

-   Note que $\mu_{n}$ es la **tasa de que ocurra una muerte cuando la población tiene** $n$ individuos.

## Continuando con los modelos de nacimiento y muerte

-   Cuando la población no tiene individuos, sólo puede ocurrir un nacimiento, por lo que la la tasa de transición desde el estado 0 es $\lambda_{0}$

$$
\nu_{0} = \lambda_{0}
$$

-   Si tanto un nacimiento como una muerte pueden ocurrir, la tasa de transición desde el estado $i>0$ es $\mu_{i} + \lambda_{i}$

\begin{align*}
\nu_{i} =& \lambda_{i} + \mu_{i} \qquad i > 0
\end{align*}

## Probabilidades de transición en un proceso de nacimiento y muerte

Si en la población hay $i > 0$ individuos a tiempo $s$, la probabilidad de que ocurra un nacimiento antes que una muerte es:

\begin{align*}
&P_{i,i+1} = \frac{\lambda_{i}}{\lambda_{i} + \mu_{i}} \qquad i > 0\\
&\text{ y una muerte antes que un nacimiento es }\\
&P_{i,i-1} = \frac{\mu_{i}}{\lambda_{i} + \mu_{i}} \qquad i > 0
\end{align*}

Claramente, la excepción es únicamente $P_{01} =1$. Pues cuando la población tiene cero individuos sólo puede hacer una transición del estado cero al estado 1.

## Tasa de transición entre estados

Definiremos $q_{ij}$ a **la tasa de transición del estado $i$ al estado $j$** como

\begin{align*}
&q_{ij}= \nu_{i}P_{ij}\quad \forall i\neq j
\end{align*}

## Probabilidades de transición 

Recordemos que  **$P_{ij}(t)$** es la probabilidad de que la cadena actualmente en el estado $i$ haga una transición al estado $j$, $t$ unidades de tiempo después.

Es decir,

\begin{align*}
&P_{ij}(t)=P\left(X(s+t)=j|X(s)=i\right)
\end{align*}

## Ejemplo: Proceso de nacimiento puro con tasa de nacimiento constante

Sea $\{N(t),t\geq 0\} \sim PPH(\lambda)$ en el que solo hay nacimientos con tasa constante, independientemente del número de individuos que haya en la población.

Es decir, **las tasas de nacimiento y muerte cuando la población tiene $n$ individuos** vienen dadas respectivamente por:

\begin{align*}
&\lambda_{n} = \lambda \qquad \forall n\geq 0\\
&\mu_{n} = 0 \qquad \forall n\geq 0
\end{align*}

## Proceso de nacimiento puro con tasa de nacimiento constante

**Las probabilidades de transición en un proceso de nacimiento puro con tasa de nacimiento constante** pueden calcularse de la siguiente manera:

\begin{align*}
&P_{0,1}=1\\
&P_{i,i+1} = \frac{\lambda_{i}}{\lambda_{i} + \mu_{i}}=\frac{\lambda}{\lambda+0}=1 \qquad i > 0\\
&P_{i,i-1} = \frac{\mu_{i}}{\lambda_{i} + \mu_{i}}=\frac{0}{\lambda+0}=0 \qquad i > 0
\end{align*}



## Probabilidades de transición para un PPH 

Sea **$\{N(t), t\geq 0\}\sim PPH(\lambda)$**, entonces para $j>i$ con $i,j \in S$,


\begin{align*}
P_{ij}(t) =& P\left(N(t+s)=j\left|N(s)=i\right.\right) \\
       =& \frac{P\left(N(t+s)=j,N(s)=i\right)}{P\left(N(s)=i\right)}\\
       =& \frac{P\left(N(t+s)-N(s)=j-i,N(s)=i\right)}{P\left(N(s)=i\right)}\\
       & \text{ por independencia de los incrementos}\\
       =& P\left(N(t+s) - N(s) = j-i\right) 
       =\frac{e^{-\lambda t}(\lambda t)^{j-i}}{(j-i)!} 
\end{align*}


## Ejemplo: Proceso de nacimiento puro con tasa lineal

Se trata de un proceso de nacimiento y muerte en el que **las tasas de nacimiento y muerte dado que la población tiene $n$ individuos** vienen dadas por

\begin{align*}
&\lambda_{0}=\lambda\\
&\lambda_{n} = n\lambda \qquad n\geq 1\\
&\mu_{n}=0 \qquad n\geq 1\\
\end{align*}

Mientras más personas formen parte de la población, la tasa de nacimiento aumenta. Cada individuo en la población puede tener un hijo con tasa $\lambda$. 

Este proceso de nacimiento y muerte es conocido también como un **Proceso de Yule.**

## Proceso de Yule

**Las probabilidades de transición** en este caso pueden calcularse de la siguiente manera:

\begin{align*}
&P_{0,1}=1\\
&P_{i,i+1} = \frac{\lambda_{i}}{\lambda_{i} + \mu_{i}}=\frac{i\lambda}{i\lambda+0}=1 \qquad i > 0\\
&P_{i,i-1} = \frac{\mu_{i}}{\lambda_{i} + \mu_{i}}=\frac{0}{i\lambda+0}=0 \qquad i > 0
\end{align*}

## Proceso de Yule 


Consideremos un proceso de Yule que comienza con un sólo individuo a tiempo $0$ y sea $T_{i}$ el tiempo entre los nacimientos $i-1$ e $i$. Claramente, $T_{1},T_{2}\dots$ son una sucesión de variables aleatorias exponenciales independientes con tasas $i\lambda\quad\forall i\geq 1$.



**Intentemos calcular $P_{ij}(t)$**



## Cálculo de $P_{ij}(t)$ para un Proceso de Yule

\begin{align*}
P(T_{1}\leq t)=& 1-e^{-\lambda t}\\
P(T_{1}+T_{2}\leq t)=&\int_{0}^{t}P(T_{1}+T_{2}\leq t|T_{1}=x)\lambda e^{-\lambda x}dx\\
=& \int_{0}^{t}P(T_{2}\leq t-x)\lambda e^{-\lambda x}dx\\
=& \int_{0}^{t}(1-e^{2\lambda(t-x)})\lambda e^{-\lambda x}dx\\
=& (1-e^{-\lambda t})^{2}\\
&\vdots \\
P(T_{1}+T_{2}+\cdots T_{j}\leq t)=& (1-e^{-\lambda t})^{j}=P(X(t)\geq j+1|X(0)=1)
\end{align*}

## Finalmente para un proceso de Yule

\begin{align*}
P_{1j}(t)=& P(X(t)=j|X(0)=1)\\
         =& P(X(t)\geq j|X(0)=1)-P(X(t)\geq j+1|X(0)=1)\\
         =& (1-e^{-\lambda t})^{j-1}-(1-e^{-\lambda t})^{j}\\
         =&e^{-\lambda t}(1-e^{-\lambda t})^{j-1}\quad\forall j\geq 1
\end{align*}

Es decir, $X(t)=j|X(0)=1\sim Geo(e^{-\lambda t})$. 

Por lo tanto, si la población comienza con $i$ individuos, la función de probabilidad de masa de $X(t)=j|X(0)=i\sim NegBin(i,e^{-\lambda t})$. Es decir,

\begin{align*}
P_{ij}(t)=& \binom{j-1}{i-1}(e^{-\lambda t })^{i}(1-e^{-\lambda t})^{j-i}
\end{align*}




## Ejemplo crecimiento poblacional lineal

Se trata de un proceso de nacimiento y muerte en el que **las tasas de nacimiento y muerte dado que la población tiene** $n$ individuos vienen dadas por


\begin{align*}
&\lambda_{0}=\lambda\\
&\lambda_{n} = n\lambda \qquad \forall n\geq 0\\
&\mu_{n} = n\mu \qquad \forall n\geq 1\\
\end{align*}

Cada individuo en la población con $n$ individuos nace a una tasa $\lambda$ y muere con una tasa $\mu$

## Modelo de crecimiento poblacional con tasas lineales

**Las probabilidades de transición** en este caso pueden calcularse de la siguiente manera:

\begin{align*}
&P_{0,1}=1\\
&P_{i,i+1} = \frac{\lambda_{i}}{\lambda_{i} + \mu_{i}}=\frac{i\lambda}{i\lambda+i\mu}=\frac{\lambda}{\lambda+\mu} \qquad i > 0\\
&P_{i,i-1} = \frac{\mu_{i}}{\lambda_{i} + \mu_{i}}=\frac{i\mu}{i\lambda+i\mu}=\frac{\mu}{\lambda+\mu} \qquad i > 0
\end{align*}

## Modelo de crecimiento lineal con inmigración

Se trata de un proceso de nacimiento y muerte en el que **las tasas de nacimiento y muerte dado que la población tiene** $n$ individuos vienen dadas por

\begin{align*}
&\mu_{n} = n\mu \qquad \forall n\geq 1\\
&\lambda_{n} = n\lambda + \theta \qquad \forall n\geq 0
\end{align*}

Cada individuo nace con tasa $\lambda$ y adicionalmente hay una tasa de aumento $\theta$ de la población debido a una fuente externa como la inmigración. Las muertes se dan con tasa $\mu$

## Modelo de crecimiento poblacional con inmigración

**Las probabilidades de transición** en este caso pueden calcularse de la siguiente manera:


\begin{align*}
&P_{0,1}=1\\
&P_{i,i+1} = \frac{\lambda_{i}}{\lambda_{i} + \mu_{i}}=\frac{i\lambda+\theta}{i\lambda+\theta +i\mu} \qquad i > 0\\
&P_{i,i-1} = \frac{\mu_{i}}{\lambda_{i} + \mu_{i}}=\frac{i\mu}{i\lambda+\theta +i\mu} \qquad i > 0
\end{align*}

## $M/M/1$:

Los clientes llegan a un sistema (nacen) de servidor único de acuerdo con un Proceso de Poisson con tasa $\lambda$. Si el servidor está ocupado, el cliente debe esperar en la cola. De lo contrario, el cliente es atendido con tiempo de servicio $exp(\mu)$. Una vez realizado el servicio, el cliente abandona el sistema (muere)


\begin{align*}
&\lambda_{n} = \lambda \qquad \forall n\geq 0\\
&\mu_{n} = \mu \qquad \forall n\geq 1\\
\end{align*}

## $M/M/1$

**Las probabilidades de transición** en este caso pueden calcularse de la siguiente manera:


\begin{align*}
&P_{0,1}=1\\
&P_{i,i+1} = \frac{\lambda_{i}}{\lambda_{i} + \mu_{i}}=\frac{\lambda}{\lambda+\mu} \qquad i > 0\\
&P_{i,i-1} = \frac{\mu_{i}}{\lambda_{i} + \mu_{i}}=\frac{\mu}{\lambda+\mu} \qquad i > 0
\end{align*}

## $M/M/c$ {.scrollable}

Considere un sistema de cola exponencial en el que hay $c$ servidores disponibles, cada uno sirviendo a tasa $\mu$. Un cliente que ingresa primero espera en la fila y luego va al primer servidor libre.


\begin{align*}
&\mu_{n} = \begin{cases}n\mu & \text{ si } 1\leq n\leq c\\
                        c\mu & \text{ si } n > c
              \end{cases}\\\\
&\lambda_{n} = \lambda \qquad \forall n\geq 0
\end{align*}


##  $M/M/c$

**Las probabilidades de transición** en este caso pueden calcularse de la siguiente manera:


\begin{align*}
&P_{0,1}=1\\
&P_{i,i+1} = \frac{\lambda_{i}}{\lambda_{i} + \mu_{i}}= 
            \begin{cases}
            \frac{\lambda}{\lambda+i\mu}  & \qquad 1\leq i\leq c \\
            \frac{\lambda}{\lambda+c\mu} & \qquad i > c
            \end{cases}\\
&P_{i,i-1} = \frac{\mu_{i}}{\lambda_{i} + \mu_{i}}=
            \begin{cases}
            \frac{i\mu}{\lambda+i\mu}  & \qquad 1\leq i\leq c \\
            \frac{c\mu}{\lambda+c\mu} & \qquad i > c
            \end{cases}\\
\end{align*}

## ¿Qué aprendimos hoy?

## ¿Para dónde vamos? 

Para

\begin{align*}
P_{ij}(t) &\equiv P\left(X(t+s)=j\left|\right.X(s)=i\right)\\\\
\end{align*}

¿Cómo hacemos para calcular **$P_{ij}(t)$** para cualquier CMTC?
