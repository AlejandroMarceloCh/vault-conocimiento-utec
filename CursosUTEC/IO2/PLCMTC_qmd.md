---
curso: IO2
titulo: PLCMTC
slides: 0
fuente: PLCMTC.qmd
---

---
title: "Probabilidades límite para CMTC"
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

- Determinar bajo qué características de la CMTC el límite 

\begin{align*}
&\lim_{t\rightarrow \infty}P_{ij}(t)
\end{align*}

**existe y es independiente del estado inicial $i$**.

- En las condiciones bajo las cuales el límite

\begin{align*}
P_{j}=&\lim_{t\rightarrow \infty}P_{ij}(t)
\end{align*}

exista y sea independiente del estado inicial $i$, **calcular $P_{j} \quad \forall j\in S$**.

- Calcular la distribución estacionaria en varios **ejemplos propios de la ingeniería industrial**. 


## Recordemos las ecuaciones diferenciales **forward** de Kolmogorov

\begin{align*}
P_{ij}^{\prime}(t) = \sum_{k\neq j}q_{kj}P_{ik}(t) - \nu_{j}P_{ij}(t) \quad \forall i,j\in S
\end{align*}

y ahora permitamos que $t\rightarrow \infty$,

\begin{align*}
\lim_{t\rightarrow\infty}P_{ij}^{\prime}(t) =& \sum_{k\neq j}q_{kj}\lim_{t\rightarrow\infty}P_{ik}(t) - \nu_{j}\lim_{t\rightarrow\infty}P_{ij}(t)\\
& \text{ en el caso que existan los límites }\\
=& \sum_{k\neq j}q_{kj}P_{k} - \nu_{j}P_{j}\\
\end{align*}

De hecho, tomando en cuenta que $0 \leq P_{ij}(t)\leq 1\quad \forall t\geq 0$, entonces 

\begin{align*}
\lim_{t\rightarrow\infty}P_{ij}^{\prime}(t) =&0
\end{align*}

## Ecuaciones de balance para CMTC

\begin{align*}
\underbrace{\nu_{j}P_{j}}_{\text{ tasa a la cual la cadena deja el estado  j}}=&\underbrace{\sum_{k\neq j}q_{kj}P_{k} \quad \forall j\in S}_{\text{tasa a la cual la cadena entra al estado j}}\\\\
&\text{ con la condición adicional necesaria para lograr unicidad de la solución}\\\\
\sum_{j\in S}{P_{j}}=&1
\end{align*}

## Observaciones a tomar en cuenta

i) Hemos asumido que los límites existían para obtener las ecuaciones de balance. Una condición suficiente para ello es:

 a) Todos los estados de la cadena deben **comunicarse**
 b) La cadena de Markov debe ser **positiva recurrente**

y podemos interpretar a **$P_{j}$ como la proporción de tiempo a largo plazo que la cadena esté en el estado $j$.**

## Ecuaciones de balance para los procesos de nacimiento y muerte

|Estado $j\in S$|Tasa de salida = Tasa de entrada |  
|:-------------:|:----------------------------------------------------------|
| $0$             | $\lambda_{0}P_{0}   =   \mu_{1}P_{1}$   |
| $1$             | $(\lambda_{1}+\mu_{1})P_{1}=\mu_{2}P_{2}+\lambda_{0}P_{0}$|
| $2$             |$(\lambda_{2}+\mu_{2})P_{2}=\mu_{3}P_{3}+\lambda_{1}P_{1}$|
| $n\geq 1$             |$(\lambda_{n}+\mu_{n})P_{n}=\mu_{n+1}P_{n+1}+\lambda_{n-1}P_{n-1}$|

Sumando cada ecuación con la inmediata anterior obtenemos el siguiente sistema de ecuaciones:

\begin{align*}
\lambda_{0}P_{0}=&\mu_{1}P_{1}\\
\lambda_{1}P_{1}=&\mu_{2}P_{2}\\
\vdots&\\
\lambda_{n}P_{n}=&\mu_{n+1}P_{n+1} \quad \forall n\geq 0\\
\end{align*}


## Expresando todas las probabilidades en función de $P_{0}$ obtenemos:

\begin{align*}
P_{1}=&\frac{\lambda_{0}}{\mu_{1}}P_{0}\\
P_{2}=&\frac{\lambda_{1}}{\mu_{2}}P_{1}=\frac{\lambda_{1}\lambda_{0}}{\mu_{2}\mu_{1}}P_{0}\\
  \vdots&\\
  P_{n}=&\frac{\lambda_{n-1}}{\mu_{n}}P_{n-1}=\frac{\lambda_{n-1}\lambda_{n-2}\cdots\lambda_{1}\lambda_{0}}{\mu_{n}\mu_{n-1}\cdots\mu_{2}\mu_{1}}P_{0}
\end{align*}

## y usando que $\sum_{n=0}^{\infty}P_{n}=1$, tenemos que

\begin{align*}
1=&P_{0}+P_{0}\sum_{n=1}^{\infty}\frac{\lambda_{n-1}\lambda_{n-2}\cdots\lambda_{1}\lambda_{0}}{\mu_{n}\mu_{n-1}\cdots\mu_{2}\mu_{1}}\\
P_{0}=&\frac{1}{1+\sum_{n=1}^{\infty}\frac{\lambda_{n-1}\lambda_{n-2}\cdots\lambda_{1}\lambda_{0}}{\mu_{n}\mu_{n-1}\cdots\mu_{2}\mu_{1}}}\\
P_{n}=&\frac{\lambda_{n-1}\lambda_{n-2}\cdots\lambda_{1}\lambda_{0}}{\mu_{n}\mu_{n-1}\cdots\mu_{2}\mu_{1}\left(1+\sum_{n=1}^{\infty}\frac{\lambda_{n-1}\lambda_{n-2}\cdots\lambda_{1}\lambda_{0}}{\mu_{n}\mu_{n-1}\cdots\mu_{2}\mu_{1}}\right)}\quad\forall n\geq 0
\end{align*}

## Observe que las ecuaciones de balance para un proceso de nacimiento y muerte pueden resolverse siempre que 

\begin{align*}
\sum_{n=1}^{\infty}\frac{\lambda_{n-1}\lambda_{n-2}\cdots\lambda_{1}\lambda_{0}}{\mu_{n}\mu_{n-1}\cdots\mu_{2}\mu_{1}}< &\infty\quad\forall n\geq 0
\end{align*}

## En el caso de una cola $M/M/1$

Observe que una M/M/1 es un proceso de nacimiento y muerte con $\lambda_{n}=n \quad\forall n\geq 0$ y $\mu_{n}=\mu\quad\forall n\geq 1$.

Por lo que,

\begin{align*}
P_{n}=&\frac{\left(\frac{\lambda}{\mu}\right)^{n}}{1+\sum_{n=1}^{\infty}\left(\frac{\lambda}{\mu}\right)^{n}}\\
    &\text{ usando que }\sum_{n=1}^{\infty}r^{n}=\frac{r}{1-r} \text{ cuando }|r|<1\\
    =&\left(\frac{\lambda}{\mu}\right)^{n}\left(1-\frac{\lambda}{\mu}\right) \quad \forall n\geq 0
\end{align*}

siempre que $\frac{\lambda}{\mu}<1$

## Observación sobre la estacionaria de una $M/M/1$: 

Es intuitivo que las tasas entre llegadas de clientes deban ser menores que las tasas de servicio para que la estacionaria exista. Piense que el caso en donde $\lambda=\mu$ se comporta igual que una caminata al azar simétrica la cual fue nuestro ejemplo de una cadena recurrente nula.


## Cantidades fundamentales en teoría de colas

\begin{align*}
L=& \text{ valor esperado a largo plazo del número de clientes en el sistema}\\
L_{Q}=& \text{ valor esperado a largo plazo del número de clientes esperando en cola}\\
W=& \text{valor esperado a largo plazo del tiempo que pasan los clientes en el sistema}\\
W_{Q}=&\text{valor esperado a largo plazo del tiempo que esperan los clientes en cola}
\end{align*}

## Número de clientes en el sistema para una $M/M/1$

El valor esperado a largo plazo del número de clientes en el sistema:

\begin{align*}
L=&\sum_{n=0}^{\infty}nP_{n}\\
 =&\sum_{n=0}^{\infty}n\left(\frac{\lambda}{\mu}\right)^{n}\left(1-\frac{\lambda}{\mu}\right)\\
=&\frac{\lambda}{\mu-\lambda} 
\end{align*}

## Tiempo que pasan los clientes en el sistema para una $M/M/1$

El valor esperado a largo plazo del tiempo que pasan los clientes en el sistema

\begin{align*}
W=&\frac{L}{\lambda}=\frac{1}{\mu-\lambda}
\end{align*}

## Tiempo en cola para una $M/M/1$

El valor esperado a largo plazo del tiempo que esperan los clientes en cola

\begin{align*}
W_{Q}=&W-E(S)=W-\frac{1}{\mu}=\frac{\lambda}{\mu(\mu-\lambda)}
\end{align*}

## Tiempo de espera en cola para una $M/M/1$

El valor esperado a largo plazo del número de clientes esperando en cola

\begin{align*}
L_{Q}=&\lambda W_{Q}=\frac{\lambda^{2}}{\mu(\mu-\lambda)}
\end{align*}

## En el caso de una cola $M/M/c$

Recordemos que en este caso:

\begin{align*}
\lambda_{n}=&\lambda\\
\mu_{n}=&\begin{cases}
        n\mu \text{ cuando } & 1\leq n\leq c\\
        c\mu \text{ cuando } & n>c
        \end{cases}
\end{align*}

Por lo que la condición:

\begin{align*}
\sum_{n=1}^{\infty}\frac{\lambda_{n-1}\lambda_{n-2}\cdots\lambda_{1}\lambda_{0}}{\mu_{n}\mu_{n-1}\cdots\mu_{2}\mu_{1}}< &\infty\quad\forall n\geq 0\\
\iff&\\
\sum_{n=c+1}^{\infty}\frac{\lambda^{n}}{(c\mu)^{n}}<&\infty\\
\iff&\\
\frac{\lambda}{c\mu}<1
\end{align*}

## Ejemplo: 3 máquinas y un técnico

**Consideremos una fábrica en donde se dispone de 3 máquinas y un técnico capaz de repararlas cuando se malogran. Supongamos que el tiempo de vida de las máquinas es exponencial parámetro $\lambda$. Mientras que el tiempo de reparación de una máquina averiada es exponencial parámetro $\mu$. ¿Cuál es la proporción del tiempo a largo plazo que todas las máquinas no están en uso? ¿Cuál es el número promedio de máquinas que no están en uso?**


## ¿Cuál es la proporción del tiempo que todas las máquinas no están en uso?**

Sea $X(t)=$ el número de máquinas malogradas a tiempo $t$. El conjunto de estados es $S=\{0,1,2,3\}$.

Claramente, 

\begin{align*}
\mu_{n}=&\mu \text{ para } n\geq 1\\
\lambda_{n}=& \begin{cases}
              (3-n)\lambda &\text{ para } n < 3\\
              0            &\text{ para } n \geq 3\\
              \end{cases}
\end{align*}

Es decir, el **fallo de una máquina es considerado un nacimiento y la reparación de una máquina es considerada una muerte.**

No están pididiendo calcular $P_{0}$

## Ecuaciones de balance

\begin{align*}
3\lambda P_{0}=&\mu P_{1}\\
(2\lambda+\mu)P_{1}=&\mu P_{2}+3\lambda P_{0}\\
(\lambda+\mu)P_{2}=& 2\lambda P_{1}+\mu P_{3}\\
\mu P_{3}=&\lambda P_{2}\\
1=&P_{0}+P_{1}+P_{2}+P_{3}
\end{align*}

Resolviendo el sistema, obtenemos 

\begin{align*}
P_{0}=&\frac{1}{1+\frac{3\lambda}{\mu}+\frac{6\lambda^{2}}{\mu^{2}}+\frac{6\lambda^{3}}{\mu^{3}}}
\end{align*}

Por lo tanto, la proporción del tiempo que todas las máquinas están funcionando es $P_{0}$

## ¿Cuál es valor esperado a largo plazo del número de máquinas que no están en uso?

Nos están pidiendo calcular:

\begin{align*}
\sum_{n=0}^{3}nP_{n}=&\left[\frac{3\lambda}{\mu}+2\frac{6\lambda^{2}}{\mu^{2}}+3\frac{6\lambda^{3}}{\mu^{3}}\right]P_{0}=\left[\frac{3\lambda}{\mu}+2\frac{6\lambda^{2}}{\mu^{2}}+3\frac{6\lambda^{3}}{\mu^{3}}\right]\frac{1}{1+\frac{3\lambda}{\mu}+\frac{6\lambda^{2}}{\mu^{2}}+\frac{6\lambda^{3}}{\mu^{3}}}
\end{align*}


## ¿Qué aprendimos hoy?
