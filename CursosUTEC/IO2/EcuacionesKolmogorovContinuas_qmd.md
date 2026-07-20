---
curso: IO2
titulo: EcuacionesKolmogorovContinuas
slides: 0
fuente: EcuacionesKolmogorovContinuas.qmd
---

---
title: "Ecuaciones Diferenciales de Kolmogorov"
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

## Objetivos

-   Demostrar las **ecuaciones diferenciales de Kolmogorov**

-   Formular las ecuaciones diferenciales de Kolmogorov de CMTC para algunos ejemplos propios de la ingeniería industrial

-   **Determinar $P_{ij}(t)$** en modelos de CMTC para algunos ejemplos propios de la ingeniería industrial

## Preliminares

Recordemos que la probabilidad de que un proceso que se encuentra a tiempo $s$ en el estado $i \in S$, haga una transición al estado $j\in S$ para $i\neq j$ durante las siguientes $t$ unidades de tiempo viene dada por:

\begin{align*}
P_{ij}(t) &\equiv P\left(X(t+s)=j\left|\right.X(s)=i\right)
\end{align*}

**Queremos saber cómo calcular dicha probabilidad para cualquier cadena de Markov a tiempo continuo. ¿Cómo lo hacemos?**

## Ejemplo familiar: 

Sea **$\{N(t), t\geq 0\}\sim PPH(\lambda)$** pero pensado como un proceso de nacimiento y muerte, entonces para $j>i$ con $i,j \in S$,


\begin{align*}
P_{ij}(t) =& P\left(N(t+s)=j\left|N(s)=i\right.\right) \\
       =& \frac{P\left(N(t+s)=j,N(s)=i\right)}{P\left(N(s)=i\right)}\\
       =& \frac{P\left(N(t+s)-N(s)=j-i,N(s)=i\right)}{P\left(N(s)=i\right)}\\
       & \text{ por independencia de los incrementos}\\
       =& P\left(N(t+s) - N(s) = j-i\right) 
       =\frac{e^{-\lambda t}(\lambda t)^{j-i}}{(j-i)!} 
\end{align*}

## Proceso de Yule

Consideremos un proceso de Yule que comienza con un sólo individuo a tiempo $0$ y sea $T_{i}$ el tiempo entre los nacimientos $i-1$ e $i$. Claramente, $T_{1},T_{2}\dots$ son una sucesión de variables aleatorias exponenciales independientes con tasas $i\lambda\quad\forall i\geq 1$.



**Intentemos calcular $P_{ij}(t)$**

## Cálculo de $P_{ij}(t)$ para un Proceso de Yule

\begin{align*}
P(T_{1}\leq t)=& 1-e^{-\lambda t}\\
P(T_{1}+T_{2}\leq t)=&\int_{0}^{t}P(T_{1}+T_{2}\leq t|T_{1}=x)\lambda e^{-\lambda x}dx\\
=& \int_{0}^{t}P(T_{2}\leq t-x)\lambda e^{-\lambda x}dx\\
=& \int_{0}^{t}(1-e^{-2\lambda(t-x)})\lambda e^{-\lambda x}dx\\
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

## ¿Qué sigue?

Queremos encontrar una forma de calcular $P_{ij}(t)$ para cualquier cadena de Markov homogénea a tiempo continuo que no sea tan contexto dependiente.

La respuesta a esta pregunta son **las ecuaciones diferenciales de Kolmogorov**, las cuales ya resolvimos para el caso de los $PPH(\lambda)$ sin saberlo.

Para tal fin necesitamos los siguientes lemas:


## Lema 1:

**Analogía continua de las ecuaciones de Chapman-Kolmogorov para las CMTD**

\begin{align*}
P_{ij}(t+s) =& \sum_{k\in S}P_{ik}(t)P_{kj}(s) \qquad \forall s\geq 0 , t\geq 0
\end{align*}

## Demostración lema 1: 


\begin{align*}
P_{ij}(t+s) &\equiv P\left(X(t+s) = j \left|\right. X(s) =i\right)\\ 
&=\sum_{k\in S}P\left(X(t+s)=j, X(t)=k\left|\right.X(0)=i\right) \\ 
&=\sum_{k\in S}P\left(X(t+s)=j\left|\right. X(t)=k,X(0)=i\right) P\left(X(t)=k\left|\right.X(0)=i\right) \\ 
&\text{Propiedad Markoviana de }\{X(t), t\geq 0
\}\\
&=\sum_{k\in S}P(X(t+s)=j| X(t)=k,) P(X(t)=k|X(0)=i)\\
&=\sum_{k\in S}P_{ik}(t)P_{kj}(s) \\
\end{align*}

por estacionariedad de la cadena de Markov a tiempo continuo.

## Lema 2:

**La probabilidad de que en un intervalo pequeño de tiempo $h$ ocurra una transición desde el estado $i\in S$ a cualquier otro es proporcional a $h$** 

\begin{align*}
\lim_{h \to 0} \frac{1- P_{ii}(h)}{h}=&\nu_i
\end{align*}

## Demostración:

\begin{align*}
1-P_{ii}(h) =& P(T_{i} < h)\\
             & T_{i}\sim exp(\nu_{i})\\
            =& 1-e^{-\nu_{i}h}\\
            & \text{expandiendo }e^{-\nu_{i}h} \text{ en su serie de Taylor}\\
            \approx & 1-\sum_{k=0}^{\infty}\frac{(-\nu_{i})^{k}h^{k}}{k!} \\
            =& \nu_{i}h+o(h)\\
            & \text{tomando el límite cuando } h\to 0 \implies \\\\
&\lim_{h \to 0} \frac{1- P_{ii}(h)}{h}=\nu_{i}.
\end{align*}


## Lema 3.

\begin{align*}
\lim_{h\to 0}\frac{P_{ij}(h)}{h}=& q_{ij} \qquad (i \neq j)
\end{align*}

donde $q_{ij}\equiv \nu_{i}P_{ij}$ es la **tasa** a la que se va desde un estado $i$ a un estado $j$.

**Demostración:** Similar a la del Lema 2. La omitimos.


## Ecuaciones diferenciales de Kolmogorov (Backward)

Para todo $i,j,k\in S$ y $t\geq0$

\begin{align*}
P_{ij}^{\prime}(t) =& \nu_i\left[\sum_{k\neq i}P_{ik}P_{kj}(t)-P_{ij}(t) \right]
\end{align*}

## Demostración de las ecuaciones de Kolmogorov (Backward):

Por el Lema 1, sabemos que 

\begin{align*}
P_{ij}(h+t) =& \sum_{k\in S}P_{ik}(h)P_{kj}(t)\\
& \text{ para calcular el cociente incremental de }P_{ij}(t)\\
P_{ij}(h+t) - P_{ij}(t) =& \sum_{k\in S}P_{ik}(h)P_{kj}(t) - P_{ij}(t) \\
=& \sum_{k\neq i}P_{ik}(h)P_{kj}(t) + P_{ii}(h)P_{ij}(t) - P_{ij}(t) \\
=& \sum_{k\neq i}P_{ik}(h)P_{kj}(t) +P_{ij}(t)(1 - P_{ii}(h))
\end{align*}


## Dividiendo por $h$ y tomando el límite cuando $h \to 0$, tenemos que:

\begin{align*}
 \lim_{h \to 0}\frac{P_{ij}(h+t)-P_{ij}(t)}{h}
 =& \lim_{h \to 0}\left[\sum_{k\neq i}\frac{P_{ik}(h)}{h}P_{kj}(t) - \frac{[1-P_{ii}(h)]}{h}P_{ij}(t) \right]\\
=& \sum_{k \neq i}P_{kj}(t)\lim_{h\to 0} \frac{P_{ik}(h)}{h} - P_{ij}(t)\lim_{h \to 0}\frac{1-P_{ii}(h)}{h} \\
=& \sum_{k \neq i}P_{kj}(t)\nu_i P_{ik} - P_{ij}(t)\nu_i=P_{ij}^{\prime}(t)
\end{align*}

como queríamos demostrar.


## ¿Por qué las ecuaciones Backward son útiles?

**Para obtener formas explícitas de** $P_{ij}(t)$

## Ejemplo: Máquina con dos estados

Sea $X$ = el tiempo de vida en horas de una máquina que asumiremos $X\sim exp(\lambda)$. Sea $Y$ = tiempo de reparación en horas de dicha máquina  con $Y \sim exp(\mu)$

| Estado | Descripción |
|--------|-------------|
| 0      | Operando    |
| 1      | Malograda   |

1) Modele esta situación como una cadena de Marko a tiempo continuo
2) Calcule la probabilidad de que dado que la máquina se encuentra funcionando actualmente, siga trabajando después de 10 horas.

## Solución de 1) 

El funcionamiento de la máquina se puede modelar como una cadena de Markov a tiempo continuo  de la siguiente manera:

\begin{align*}
&\nu_{0} = \lambda\\
&\nu_{1} = \mu\\\\
& \mathbb{P}=\begin{bmatrix}
                  0 & 1\\
                  1 & 0\\
              \end{bmatrix}\\
\end{align*}

## Solución 2) 

Suponga que la máquina está operando a tiempo 0. **Encuentre la probabilidad de que esté trabajando a tiempo 10**. Es decir, la probabilidad requerida es $P_{00}(10)$

Usando las ecuaciones de Kolmogorov:


\begin{align*}
P_{ij}^{\prime}(t) =& \nu_{i}\left[\sum_{k\neq i}P_{ik}P_{kj}(t)-P_{ij}(t) \right]\\
\end{align*}

Obtenemos el siguiente sistema de ecuaciones diferenciales:

\begin{align*}
P_{00}^{\prime}(t) =& \lambda[P_{10}(t) - P_{00}(t)]\\
P_{10}^{\prime}(t) =& \mu[P_{00}(t) - P_{10}(t)]\\\\
P_{01}^{\prime}(t) =& \lambda[P_{11}(t) - P_{01}(t)]\\
P_{11}^{\prime}(t) =& \mu[P_{01}(t) - P_{11}(t)]\\
\end{align*}

## Tomando únicamente las dos primeras ecuaciones que son las que involucran a $P_{00}(t)$ obtenemos


\begin{align*}
\mu P'_{00}(t)  =&\mu \lambda[P_{10}(t) - P_{00}(t)]\\
\lambda P'_{10}(t) =& \mu \lambda[P_{00}(t) - P_{10}(t)] \\
\end{align*}

Sumando ambas ecuaciones obtenemos que 

\begin{align*}
&\mu P'_{00}(t) + \lambda P'_{10}(t) = 0\\\\
&\text{ integrando a ambos lados obtenemos que }\\\\
&\mu P_{00}(t) + \lambda P_{10}(t) = c\\
\end{align*}

Utilizando como condiciones iniciales $P_{00}(0)=1$ y $P_{10}(0)=0$, obtenemos que $c=\mu$ 

## Finalmente,

\begin{align*}
\mu P_{00}(t) + \lambda P_{10}(t) =& \mu\\
\text{despejando }P_{10}(t)&\\\\
\lambda P_{10}(t) =& \mu [1- P_{00}(t)]
\end{align*}

Ahora sustituyendo en la primera ecuación diferencial $P_{10}(t)$ como función de $P_{00}(t)$,

\begin{align*}
P'_{00}(t) =& \lambda[P_{10}(t) - P_{00}(t)] \\
           =& \mu[1-P_{00}(t)] - \lambda P_{00}(t) \\
          =& - (\mu + \lambda) P_{00}(t)+\mu
\end{align*}

La cual es una ecuación diferencial de primer orden que sabemos resolver. 

## Haciendo el cambio de variables 

Sea $h(t) \equiv P_{00}(t) - \frac{\mu}{\mu + \lambda}$

\begin{align*}
h'(t) = P'_{00}(t) =& \mu - (\mu + \lambda)\left[h(t) + \frac{\mu}{\mu + \lambda}\right] \\
h'(t) =& -(\mu + \lambda)h(t) \\
\frac{h'(t)}{h(t)} =& - (\mu + \lambda)\\\\
\text{ integrando a ambos lados }&\\\\
\int \frac{h'(t)}{h(t)}dt =& -\int (\mu + \lambda)dt \\
\log(h(t)) =& -(\mu + \lambda)t + c \\
h(t) =& e^{-(\mu+ \lambda)t + c}=ke^{-(\mu + \lambda)t}
\end{align*}

## Finalmente, devolviendo el cambio de variables

\begin{align*}
P_{00}(0) =& 1 = k + \frac{\mu}{\mu + \lambda} \implies k=\frac{\lambda}{\mu + \lambda}\\\\
P_{00}(t) =& \frac{\lambda}{\mu + \lambda}e^{-(\mu + \lambda)t}+\frac{\mu}{\mu + \lambda} \\
P_{10}(t) =& \frac{\lambda}{\mu + \lambda}e^{-(\mu + \lambda)10}+\frac{\mu}{\mu + \lambda}\\\\
\text{la probabilidad requerida es}&\\\\
P_{00}(10) =& \frac{\lambda}{\mu + \lambda}e^{-(\mu + \lambda)10}+\frac{\mu}{\mu + \lambda} \\
\end{align*}




## Ecuaciones diferenciales de Kolmogorov (Forward) 

\begin{align*}
P_{ij}^{\prime}(t) = \sum_{k\neq j}\nu_{k}P_{kj}P_{ik}(t) - \nu_{j}P_{ij}(t)
\end{align*}

La demostración es similar a la prueba de las backward. La omitimos.

## En el caso de los procesos de nacimiento y muerte las ecuaciones foward de Kolmogorov vienen dadas por:

\begin{align*}
P_{i0}^{\prime}(t)=&-\mu_{1}P_{i1}(t)-\lambda_{0}P_{i0}(t)\\
P_{ij}^{\prime}(t)=&\lambda_{j-1}P_{i,j-1}(t)+\mu_{j+1}P_{i,j+1}(t)-(\lambda_{j}+\mu_{j})P_{ij}(t) \text{ para }j\neq 0
\end{align*}



## En el caso particular en el que el proceso sea de nacimiento puro, las ecuaciones Forward de Kolmogorov vienen dadas por:

\begin{align*}
P_{ii}^{\prime}(t)=&-\lambda_{i}P_{ii}(t)\\
P_{ij}^{\prime}(t)=&\lambda_{j-1}P_{i,j-1}(t)-\lambda_{j}P_{ij}(t) \text{ para } j>i
\end{align*}

En este caso particular, podemos resolver la primera ecuación usando como condición inicial $P_{ii}(0)=1$, obteniendo que

\begin{align*}
P_{ii}(t)=&e^{-\lambda_{i}}
\end{align*}

La probabilidad de que el tiempo hasta que ocurra una transición desde $i$ sea mayor que $t$.

## Para el caso $P_{ij}(t)$ para $j>i$ 

\begin{align*}
e^{\lambda_{j}t}P_{i,j-1}(t)=&e^{\lambda_{j}t}\left[P_{ij}^{\prime}(t)+\lambda_{j}P_{ij}(t)\right]\\
              =&\frac{d}{dt}\left[e^{\lambda_{j}t}P_{ij}(t)\right]
\end{align*}

Integrando y usando como condición inicial $P_{ij}(0)=0$, obteniendo

\begin{align*}
P_{ij}(t)=&\lambda_{j-1}e^{-\lambda_{j}t}\int_{0}^{t}e^{\lambda_{j}s}P_{i,j-1}(s)ds \text{ para } j>i\\
\end{align*}

De esta última ecuación se pueden derivar los casos de procesos de nacimiento puro Poisson y Yule. **Lo cual se deja como ejercicio para los alumnos**

## Caso $PPH(\lambda)$

## En el caso de los procesos de nacimiento y muerte las ecuaciones Backward de Kolmogorov vienen dadas por:

\begin{align*}
P_{0,j}^{\prime}(t)=&\lambda_{0}\left[P_{1,j}(t)-P_{0,j}(t)\right]\\
P_{ij}^{\prime}(t)=& \lambda_{i}P_{i+1,j}(t)+\mu_{i}P_{i-1,j}(t)-(\lambda_{i}+\mu_{i})P_{ij}(t) \text{ para } i > 0\\
\end{align*}



## ¿Cómo escribimos las ecuaciones de Kolmogorov en notación matricial?

Sea 

\begin{align*}
\mathbb{R}\equiv \begin{bmatrix}
             -\nu_{0} & q_{01}  & q_{02} & \dots   & q_{0n}\\ 
              q_{10}  &-\nu_{1} & q_{12} & \dots   & q_{1n}\\
              \vdots  & \vdots  & \vdots & \ddots  & \vdots\\ 
              q_{n0}  & q_{n1}  & q_{n2} & \dots   &-\nu_{n}\\
                \end{bmatrix} 
\end{align*}

en donde $q_{ij} = \nu_{i}P_{ij}$ es la tasa a la que CMTC hace una transición del estado $i$ al estado $j$.

$\mathbb{R}$ es llamada también  **la matriz generadora infinitesimal de una CMTC** o simplemente **matriz generadora de una CMTC.**



## Observaciones

1) **Las filas de $R$** la matriz generadora de una CMTC **suman cero.**


\begin{align*}
\sum_{j \in S, j\neq i}\nu_{i}P_{ij} = \nu_{i}\sum_{j \in S, j\neq i}P_{ij} = \nu_i 
\end{align*}

2)  Las ecuaciones de Kolmogorov pueden ser **escritas matricialmente** como:

\begin{align*}
&\mathbb{P}^{\prime}(t) = \mathbb{R}\mathbb{P}(t)  \text{ (Backward)}\\
&\mathbb{P}^{\prime}(t) = \mathbb{P}(t)\mathbb{R} \text{(Forward)} \\
\end{align*}

en donde $\mathbb{P}(t)=[P_{ij}(t)]_{i,j\in S}$ 


## Continuando con las observaciones

3) $\mathbb{P}(t)$ es **continua en $t=0$** 


4) $\mathbb{P}(t)$ es **continua $\forall t \geq 0$**

Esto se sigue de la observación 3) y $\mathbb{P}(t+h) = \mathbb{P}(t)\mathbb{P}(h)$ la ve\mathbb{R}sión matricial de las ecuaciones de Chapman - Kolmogorov para CMTC.

5) $\mathbb{P}(t)$ **es diferenciable y es la única solución** de 

\begin{align*}
\mathbb{P}^{\prime}(t)=&\mathbb{P}(t)\mathbb{R}\\
                      =&\mathbb{R} \mathbb{P}(t)
\end{align*}

## Continuando con las observaciones

6)**$\mathbb{R}(t)$ caracteriza CMTC por completo**

7) En general, no es fácil calcular $\mathbb{P}(t)$ .

## ¿Qué hacemos para calcular $\mathbb{P}(t)$?

**¿Forward o Backward?**

## Volvamos al ejemplo de la máquina de dos estados pero ahora en formato matricial:

\begin{align*}
\mathbb{R}=\begin{bmatrix} 
           -\lambda & \lambda\\
           \mu      & -\mu\\
           \end{bmatrix}
\end{align*}

\begin{align*}
\mathbb{P}(t)=&\begin{bmatrix} 
                P_{00}(t) & P_{01}(t)\\
                P_{10}(t) & P_{11}(t)
                \end{bmatrix}
\end{align*}

\begin{align*}
\mathbb{P}^{\prime}(t)=&\begin{bmatrix} 
                P_{00}^{\prime}(t) & P_{01}^{\prime}(t)\\
                P_{10}^{\prime}(t) & P_{11}^{\prime}(t)\\
                \end{bmatrix}
\end{align*}

## Ecuaciones diferenciales de Kolmorogov

\begin{align*}
\mathbb{P}^{\prime}(t) = \mathbb{R}\mathbb{P}(t) \text{ (Backward) }\\
\end{align*}
esto es:

\begin{align*}
\begin{bmatrix} 
P_{00}^{\prime}(t) & P_{01}^{\prime}(t)\\
P_{10}^{\prime}(t) & P_{11}^{\prime}(t)
\end{bmatrix} =& \begin{bmatrix}
                 -\lambda & \lambda\\
                      \mu & -\mu\\
                 \end{bmatrix}
                 \begin{bmatrix} 
                  P_{00}(t) & P_{01}(t)\\
                  P_{10}(t) & P_{11}(t)
                 \end{bmatrix}\\
              =&\begin{bmatrix}
              -\lambda P_{00}(t) + \lambda P_{10}(t) & -\lambda P_{01}(t) + \lambda P_{11}(t) \\
              \mu P_{00}(t) - \mu P_{10}(t) & \mu P_{01}(t) - \mu P_{11}(t)\\
                \end{bmatrix} 
\end{align*}

## En particular resolvamos el ejemplo de la máquina de dos estados:

\begin{align*}
\begin{bmatrix} 
P_{00}^{\prime}(t)\\
P_{10}^{\prime}(t)\\
\end{bmatrix} =& \begin{bmatrix}
                 -\lambda & \lambda\\
                      \mu & -\mu\\
                 \end{bmatrix}
                 \begin{bmatrix} 
                  P_{00}(t)\\
                  P_{10}(t)\\ 
                 \end{bmatrix}\\
\end{align*}

Resolvamos este sistema de ecuaciones diferenciales para el caso particular en el que $\lambda=3$ y $\mu=1$. Es decir,

\begin{align*}
\begin{bmatrix} 
P_{00}^{\prime}(t)\\
P_{10}^{\prime}(t)\\
\end{bmatrix} =& \begin{bmatrix}
                 -3 &  3\\
                  1 & -1\\
                 \end{bmatrix}
                 \begin{bmatrix} 
                  P_{00}(t)\\
                  P_{10}(t)\\ 
                 \end{bmatrix}\\
\end{align*}

## Calculemos los autovalores y autovectores asociados a la matriz generadora $R$

\begin{align*}
\det{\begin{bmatrix}
                 -3 &  3\\
                  1 & -1\\
                 \end{bmatrix}-\lambda\begin{bmatrix}
                 1 &  0\\
                  0 & 1\\
                 \end{bmatrix} }=& (3+\lambda)(1+\lambda)-3= \lambda(\lambda+4)=0
\end{align*} 

Por lo que los autovalores de la matriz generadora son $\lambda_{1}=0$ y $\lambda_{2}=-4$. 

Calculemos los autovectores asociados a cada autovalor.

Para $\lambda_{1}=0$,
\begin{align*}
\begin{bmatrix}
                 -3 &  3\\
                  1 & -1\\
                 \end{bmatrix}
                 \begin{bmatrix}
                 x_{1}\\
                 x_{2}\\
                 \end{bmatrix}=& \begin{bmatrix}
                 0\\
                 0\\
                 \end{bmatrix}\implies \begin{bmatrix}
                 x_{1}\\
                 x_{2}\\
                 \end{bmatrix}= \begin{bmatrix}
                  1\\
                  1\\
                 \end{bmatrix}
\end{align*}

Para $\lambda_{2}=-4$,
\begin{align*}
\begin{bmatrix}
                  1 &  3\\
                  1 &  3 \\
                 \end{bmatrix}
                 \begin{bmatrix}
                 x_{1}\\
                 x_{2}\\
                 \end{bmatrix}=& \begin{bmatrix}
                 0\\
                 0\\
                 \end{bmatrix}\implies \begin{bmatrix}
                 x_{1}\\
                 x_{2}\\
                 \end{bmatrix}= \begin{bmatrix}
                  -3\\
                  1\\
                 \end{bmatrix}
\end{align*}

## Las soluciones se calculan así:

\begin{align*}
e^{t\mathbb{R}}\equiv \mathbb{Q}e^{-\mathbb{D}t}\mathbb{Q}^{-1}
\end{align*}

en donde 

\begin{align*}
\mathbb{Q}\equiv&\begin{bmatrix}
                 1&-3\\
                 1& 1\\
                 \end{bmatrix}\\
\mathbb{Q}^{-1}=&\begin{bmatrix}
                 1/4 & 3/4\\
                -1/4 & 1/4\\
                 \end{bmatrix}\\
\mathbb{D}=& \begin{bmatrix}
                 0 & 0\\
                 0 & -4\\
                 \end{bmatrix}\\ 
e^{\mathbb{D}t} =& \begin{bmatrix}
                 1 & 1\\
                 1 & e^{-4t}\\
                 \end{bmatrix}\\                
\end{align*}

## Finalmente

\begin{align*}
e^{t\mathbb{R}}=&\begin{bmatrix}
                 1/4+(3/4)e^{-4t} & 3/4-(3/4)e^{-4t}\\
                 1/4-(1/4)e^{-4t} & 3/4+(3/4)e^{-4t}\\
                 \end{bmatrix}\\
\end{align*}

Note además que:

\begin{align*}
\lim_{t\rightarrow\infty}e^{t\mathbb{R}}=&\begin{bmatrix}
                 1/4 & 3/4\\
                 1/4 & 3/4\\
                 \end{bmatrix}\\
\end{align*}

**Por lo que a largo plazo la probabilidad de que la máquina esté funcionando es $1/4$**

## Ecuaciones diferenciales  de Kolmogorov

\begin{align*}
\mathbb{P}^{\prime}(t) = \mathbb{P}(t)\mathbb{R} \text{ (Forward)}\\ 
\end{align*}

esto es:

\begin{align*}
\begin{bmatrix} 
P_{00}^{\prime}(t) & P_{01}^{\prime}(t)\\
P_{10}^{\prime}(t) & P_{11}^{\prime}(t)
\end{bmatrix} =& 
                \begin{bmatrix} P_{00}(t) & P_{01}(t)\\
                                P_{10}(t) & P_{11}(t)\\
                \end{bmatrix}
                \begin{bmatrix} 
                -\lambda & \lambda\\
                \mu & -\mu\end{bmatrix}\\
              =&\begin{bmatrix} 
              -\lambda P_{00}(t) + \mu P_{01}(t) & \lambda P_{00}(t) - \mu P_{01}(t) \\
              -\lambda P_{10}(t) + \mu P_{11}(t) & \lambda P_{10}(t) - \mu P_{11}(t)
              \end{bmatrix} 
\end{align*}



## Observaciones

Tenga en cuenta que no necesitamos resolver cuatro ecuaciones simultáneas; necesitamos resolver solo **dos a la vez** como lo hicimos en el ejemplo. Por lo tanto, si nuestro **estado inicial es fijo** y queremos obtener la **distribución condicional de** $X(t)$ , debemos usar las ecuaciones **"Forward"**. Por otro lado, si queremos encontrar la probabilidad de que $X(t)$ **se encuentre en un estado dado** $j$ **para varios estados iniciales**, debemos resolver ecuaciones **"Backward".**


\begin{align*}
 \mathbb{P}(t)=&\begin{bmatrix}     \frac{\lambda}{\lambda+\mu}e^{-(\lambda + \mu)t}+\frac{\mu}{\lambda + \mu} & \frac{\lambda}{\lambda+\mu}(1-e^{-(\lambda + \mu)t})\\
\frac{\mu}{\lambda+\mu}(1-e^{-(\lambda + \mu)t})& \frac{\mu}{\lambda+\mu}e^{-(\lambda + \mu)t}+\frac{\lambda}{\lambda + \mu}
\end{bmatrix}
\end{align*}

## Algunos ejemplos de modelamiento

**Considere un taller mecánico que tiene dos máquinas que son independientes, idénticas y pueden estar en funcionamiento o malogradas. Si una máquina está en funcionamiento, esta falla después de una cantidad de tiempo** $exp(\mu)$**. Si está malograda, se necesita una cantidad de tiempo** $exp(\lambda)$ **para arreglarlo. Una vez arreglada, estará como nueva. Los tiempos sucesivos de avería y reparación son independientes. Sea** $X(t)$ **el número de máquinas en funcionamiento en el tiempo** $t$**. ¿Es** $\lbrace X(t),t\geq0 \rbrace$ **una CMTC? (Cada máquina posee su propio técnico)**

## Solución

Definamos $S = \lbrace 0,1,2\rbrace$

| Estados | Descripción                    |
|---------|--------------------------------|
| 0       | Ambas malogradas               |
| 1       | Una funcionando otra malograda |
| 2       | Ambas funcionando              |

## Analicemos los estados uno a uno:

**Estado 0:** Ambas máquinas están malogradas, cuando una de estas es reparada, el sistema se mueve al estado 1. Esto ocurrirá después de $\min\left(exp(\lambda),exp(\lambda)\right) = exp(2\lambda)$. Entonces, $\nu_0 = 2\lambda$


**Estado 1:** Una máquina está en funcionamiento y la otra está malograda. Existen dos posibilidades:

1.  La máquina en funcionamiento falla $1 \to 0$

2.  La máquina malograda es reparada $1 \to 2$

**Si (1) ocurre antes que (2), entonces** $1\to 0$**, sino** $1\to 2$

\begin{align*}
R=\begin{bmatrix} 
-2\lambda   & 2\lambda     &  0\\ 
\mu         & -(\mu+\lambda)&  \lambda\\
0           & 2\mu          & -2\mu\\
\end{bmatrix}
\end{align*}


![](modelo1.jpg){width="250"}

## ¿Cómo obtenemos $\mathbb{P}$ para $R$?

Recuerde que $\mathbb{P}$ tiene ceros en su diagonal, y que $r_{ij}=\nu_iP_{ij} \qquad i\neq j$. **Entonces, dividiendo** $r_{ij}$ **por** $\nu_i$ **nos dará** $\mathbb{P}$**.**

\begin{align*}
\mathbb{P}=\begin{bmatrix} 
0                      & 1 & 0 \\ 
\frac{\mu}{\mu+\lambda}& 0 &\frac{\lambda}{\mu + \lambda}\\
0                      & 1 & 0
\end{bmatrix}
\end{align*}

## Cambiando el ejemplo

**Ahora suponga que solo hay un técnico y las máquinas son reparadas según el orden "primera malograda, primera reparada". Sea** $X(t)$ **el número de máquinas en funcionamiento a tiempo** $t$**. Determine la matriz generadora.**

\begin{align*}
R=&\begin{bmatrix} 
-\lambda &  \lambda      & 0\\ 
\mu      & -(\mu+\lambda)& \lambda\\
0        & 2\mu          & -2\mu\\
\end{bmatrix}
\end{align*}

## Ejemplo: Clientes en una estación de dos servidores.

**Suponga que los clientes llegan a una estación de 2 servidores como** $PPH(\lambda)$**. No hay sala de espera en la estación. Si un cliente entrante encuentra al menos un servidor vacío, inmediatamente comienza a ser atendido. Los tiempos de servicio son** $exp(\mu)$ **para ambos servidores. Si encuentra ambos servidores ocupados, se va y decimos que el cliente se ha perdido. Modele esto como un CMTC. Encuentre R.**

## Solución

Sea $X(t)$ el número de servidores ocupados a tiempo $t$. $S = \lbrace0,1,2\rbrace$

\begin{align*}
R=&\begin{bmatrix}
-\lambda &  \lambda &0\\ 
\mu & -(\mu+\lambda)&\lambda\\
0& 2\mu & -2\mu
\end{bmatrix}
\end{align*}

## Ejemplo: Cola de reintento.

**Suponga que los clientes llegan a una estación de un solo servidor como** $PPH(\lambda)$**. No hay sala de espera en el servidor. Si un cliente entrante encuentra el servidor vacío, inmediatamente comienza a ser atendido. Los tiempos de servicio son variables aleatorias independientes e indénticamente distribuídas** $exp(\mu)$**. Si encuentra el servidor ocupado, se va (decimos que se une a una órbita) y vuelve a probar suerte después de una cantidad de tiempo** $exp(\theta)$ **independiente de todo lo demás. Persiste de esta manera hasta que es atendido. Todos los clientes se comportan de esta manera. Modele esto como un CMTC**

## Solución {.scrollable}

-   Sea $X(t)$ el número de clientes en servicio a tiempo $t$. Obviamente, $X(t) = 1$ o $X(t) = 0$

-   Sea $R(t)$ el número de clientes en órbita a tiempo $t$.

Consideremos un proceso bivariado $\lbrace(X(t),R(t)) , t \geq 0\rbrace$ con estados en el espacio $S=\lbrace(i,k);i=0,1;k=0,1,2,...\rbrace$

![](modelo2.jpg)

## ¿Qué aprendimos hoy?
