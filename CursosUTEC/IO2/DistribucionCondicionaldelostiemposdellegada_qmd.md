---
curso: IO2
titulo: DistribucionCondicionaldelostiemposdellegada
slides: 0
fuente: DistribucionCondicionaldelostiemposdellegada.qmd
---

---
title: "Distribución Condicional de los Tiempos de Llegada"
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.jpg
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
      transition: slide
editor: source
date: "Septiembre,2024"
---

## ¿Que hemos aprendido hasta ahora de los Procesos de Poisson?

-   Definir **Procesos de Poisson Homogéneo**.

-   Deducir a partir del proceso de Poisson Homogéneo **el proceso estocástico de los tiempos entre llegadas.**

-   Enunciar, distinguir y demostrar la **equivalencia de las dos definiciones de los procesos de Poisson Homogéneos, la operativa y la validadora**.

-   Visualizar los aspectos relacionados con la **validación de un proceso de Poisson homogéneo** a partir de data simulada y real en el contexto de las operaciones propias de la ingeniería industrial.

-   Definir y visualizar **los tiempos entre llegadas y de llegadas de un proceso de Poisson Homogéneo simulado**.

## Objetivos: Distribución condicional de los tiempos de llegada

-   **Modelar los tiempos de llegada de un** $PPH(\lambda)$**, condicionados al número de eventos ocurridos en** $(0,t]$.

-   **Ejemplificar y aplicar dicho modelo en situaciones propias de las operaciones de ingeniería industrial**.


## Estadísticos de orden de la uniforme

Ahora, sean

$$U_{1}, U_{2}, \ldots, U_{n}$$

una sucesión de v.a. i.i.d. $U[0,t]$.

Diremos que $U_{(1)}, U_{(2)}, \ldots, U_{(n)}$ son los estadísticos de orden de $U_{1}, U_{2}, \ldots, U_{n}$ si

$$
U_{(1)}\leq U_{(2)}\leq\ldots \leq U_{(n)}
$$

## Ejemplos:

```{r echo=TRUE}
t <- 6

# Generemos 10 observaciones de una U(0,t)

U <- runif(10, min=0, max=t)

# Mostremos la sucesión U1, U2, …, Un

U

```

## 

```{r echo=TRUE}
# Ordenemos las 10 observaciones de menor a mayor

O <- sort(U)

# Mostremos los estadísticos de orden U(1),U(2), …, U(n)

O

```

Las v.a. $U_{(1)}, U_{(2)}, \ldots, U_{(n)}$ se denominan los **estadísticos de orden** $U_1, U_2, \ldots, U_n$.

## Densidad conjunta de los estadísticos de orden caso uniforme

La **densidad conjunta de los estadísticos de orden** asociados de la sucesión $U_{1}, U_{2},\cdots U_{n}\sim i.i.d. Unif(0,t)$ viene dada por:

$$f(u_{1},\ldots,u_{n})=\frac{n!}{t^{n}} $$

para $\quad 0 < u_{1} < u_{2} < \ldots < u_{n} < t$

## Densidad y valor esperado de cada estadístico de orden caso uniforme

Con respecto al $k$**-ésimo estadístico de orden,** $U_{(k)}$, tenemos que:

$$
\begin{align*}& \text{ densidad marginal de } U_{(k)}\\& f_{U_{(k)}}(u)=\frac{n!}{(k-1)!(n-k)!} \left(\frac{u}{t}\right)^{k-1} \frac{1}{t}\left(1-\frac{u}{t}\right)^{n-k} \text{ para  } 0\leq u\leq t \\ & E[U_{(k)}]=\frac{kt}{n+1} \text{ para } k=1,2,\cdots n. \end{align*}
$$

## Teorema de los tiempos de llegada condicionales

Sea $\{N(t), t\geq0\} \text{ un } PPH(\lambda)$ y sea $S_n$ el tiempo de llegada del n-ésimo evento. Entonces,

$$\left(S_{1}, S_{2}, \cdots, S_{n}\right)|N(t)=n \sim (U_{(1)}, U_{(2)}, \cdots, U_{(n)})$$

en donde $U_{(1)}, U_{(2)}, \cdots, U_{(n)}$ es la sucesión de los estadísticos de orden asociados a la sucesión

$$U_{1}, U_{2}, \cdots, U_{n}\sim^{\text{i.i.d.}} Unif(0,t)$$



## Vamos a convencernos con un caso sencillo

Calculemos para $s < t$, 

\begin{align*}
P\left(S_{1} > s\Big|N(t)=n\right)=& \frac{P\left(S_{1}>s,N(t)=n\right)}{P\left(N(t)=n\right)}
=\frac{P\left(N(s)=0,N(t)=n\right)}{P\left(N(t)=n\right)}\\
& \text{ incrementos no independientes}\\
=&\frac{P\left(N(s)=0,N(t)-N(s)=n\right)}{P\left(N(t)=n\right)}\\
&\text{ por independencia de los incrementos}\\
=&\frac{P\left(N(s)=0\right)P\left(N(t)-N(s)=n\right)}{P\left(N(t)=n\right)}\\
&\text{ por estacionariedad de los incrementos }\\
=&\frac{P\left(N(s)=0\right)P\left(N(t-s)=n\right)}{P\left(N(t)=n\right)}
= \frac{e^{-\lambda s}\frac{e^{-\lambda(t-s)}(\lambda(t-s))^{n}}{n!}}{\frac{e^{-\lambda t}(\lambda t)^n}{n!}}=\left[1-\frac{s}{t}\right]^n
\end{align*}

## Calculemos la distribución del primer estadístico de orden de una muestra aleatoria simple $Unif(0,t)$

Para $s<t$, la función de distribución acumulativa del primer estadístico de orden de una muestra aleatoria simple $U_{1},U_{2}, \dots, U_{n}\sim Unif(0,t)$ se calcula de la siguiente manera:

\begin{align*}
P\left(U_{(1)}>s\right)=& P\left(\min{\left(U_{1},U_{2}, \dots, U_{n}\right)}>s\right)\\
                        & \text{por independencia de la muestra}\\
                       =& \left[P\left(U_{i}>s\right)\right]^{n}\\
                       =& \left[1-\frac{s}{t}\right]^{n}
\end{align*}

## Hemos demostrado el caso más sencillo del Teorema de los tiempos condicionales de llegada

$$
S_{1}\Big| N(t)=n \sim U_{(1)}\equiv \min{\left(U_{1},\cdots,U_{n}\right)}
$$

donde $U_{1},\cdots,U_{n}\sim \text{ i.i.d. } Unif(0,t)$

## Por lo tanto:

$$
f_{S_{1}|N(t)=n}(u)=f_{U_{(1)}}=\frac{n}{t}\left(1-\frac{u}{t}\right)^{n-1} 
$$

para $\quad 0 < u < t$.

Por lo tanto, la confiabilidad de $S_{1}|N(t)=n$ puede calcularse también por:

$$
\begin{align*}P\left(S_1 > s\Big|N(t)=n\right)=&\int_s^t \frac{n}{t} \left(1-\frac{u}{t}\right)^{n-1}du\\=& \left(1-\frac{s}{t}\right)^n \end{align*}
$$

## Alternativamente:

Podemos usar el siguiente truco:

$$
\begin{align*}P\left(S_{1} > s\Big|N(t)=n\right)=&P\left(\min{\left(U_1,\ldots,U_n\right)} > s\right)\\=&P\left(U_1 > s,\ldots,U_n > s\right)\\=&\prod_{i=1}^n P\left(U_{i} > s\right)\\=&\prod_{i=1}^n\left(1-\frac{s}{t}\right)=\left(1-\frac{s}{t}\right)^n\end{align*}
$$




## Ejemplo


**Suponga que pasajeros llegan a una estación de tren acorde con un** $PPH(\lambda)$**. Si el tren parte a tiempo t, calcule el valor esperado de la suma de los tiempos de espera de los viajeros que hayan llegado en** $(0,t]$**.**

## Solución:

Es decir, el valor esperado requerido viene dado por:

$$
\begin{align*}E\left[\sum_{i=1}^{N(t)} (t-S_i)\right] &= E\left[E\left[\sum_{i=1}^{N(t)} (t-S_i) \Big| N(t)\right]\right]\\ \end{align*}
$$

por la propiedad torre de la esperanza condicional.

## Primero calculemos la esperanza interna {.scrollable}

$$
\begin{align*}&E\left[\sum_{i=1}^{N(t)} (t-S_i) \Big| N(t)=n\right] \\&= E\left[\sum_{i=1}^n (t-S_i) \Big| N(t)=n\right] \\&= nt - E\left[\sum_{i=1}^n  S_i \Big| N(t)=n\right] \\&= nt - E\left[\sum_{i=1}^n  U_{(i)}\right]= nt - E\left[\sum_{i=1}^n  U_i\right] \\&= nt - \sum_{i=1}^n E[U_i] = nt - \frac{nt}{2}= \frac{nt}{2}\end{align*}
$$

## Finalmente

$$
\begin{align*}E\left[\sum_{i=1}^{N(t)} (t-S_i)\right] =& E\left[E\left[\sum_{i=1}^{N(t)} (t-S_i) \Big| N(t)\right]\right]\\=&E\left[\frac{N(t)t}{2}\right]=\frac{\lambda t^{2}}{2}\end{align*}
$$



## Valores esperados de los estadísticos de orden

Para $k > n$,

$$E\left[S_k\Big|N(t)=n\right] = t + \frac{(k-n)}{\lambda}$$

Podemos hacer cosas como la siguiente:

$$
\begin{align*}E\left[T_2\Big|N(1)=1\right] =& E\left[S_2-S_1\Big|N(1)=1\right]\\=& E\left[S_2\Big|N(1)=1\right] - E\left[S_1\Big|N(1)=1\right]\\=& 1+\frac{1}{\lambda}-\frac{1}{2}\end{align*}
$$

ambos consecuencia de la propiedad de pérdida de la memoria de la exponencial.

## Distribución condicional del primer tiempo de llegada {.scrollable}

Sea $\{N(t), t\geq 0\}$ un $PPH(\lambda)$. Se desea calcular la distribución del tiempo de llegada del primer evento, $S_{1}$ dado que $N(t)=1$. Es decir, para $0 < s\leq t$, se desea calcular:

$$
\begin{align*}P[S_{1} \leq s|N(t)=1] &= \frac{P[S_{1} \leq s,N(t)=1]}{P(N(t)=1)} \\
                                     &= \frac{P\left[1 \text{ evento en } (0,s], 0 \text{ eventos en } (s,t]\right]}{P(N(t)=1)} \\
                                     &= \frac{P[N(s)=1] P[N(t)-N(s)=0]}{P(N(t)=1)} \\
                                     &= \frac{P[N(s)=1] P[N(t-s)=0]}{P(N(t)=1)} \\
                                     &= \frac{\frac{(\lambda s)^1 e^{-\lambda s}}{1!} \cdot \frac{(\lambda (t-s))^0 e^{-\lambda(t-s)}}{0!}}{\frac{(\lambda t)^1 e^{-\lambda t}}{1!}}= \frac{s}{t} \\
\end{align*}
$$

## Verificando que sea una función de distribución:

La **función de distribución condicional de los tiempos de llegada** viene dada por:

$$
\begin{align*}F_{S_{1}|N(t)=1}(s)\equiv& P[S_{1} \leq s\Big|N(t)=1]\\=&\begin{cases}  0 & \text{ si } s < 0\\  \frac{s}{t} &\text{si } 0\leq s \leq t\\  1 & \text{ si } s > t\\  \end{cases}\end{align*}
$$

## **¿Cómo calculamos la densidad condicional del primer tiempo de llegada?**

Derivando la función de distribución condicional obtenemos **la función de densidad condicional de los tiempos de llegada**:

$$
\begin{align*}f_{S_{1}|N(t)=1}(s)=&\frac{d}{ds}\left[P\left(S_{1} \leq s\Big|N(t)=1\right)\right]\\\\                =&\begin{cases}                \frac{1}{t} & \text{ si } 0 \leq s \leq t\\                0 & \text{ fuera }                \end{cases}\end{align*}
$$

**¿Reconoce usted esta función de densidad?**

## Distribución conjunta condicional de los dos primeros tiempos de llegada

Supongamos ahora que $N(t)=2$ **y que queremos calcular la distribución conjunta de** $S_{1}$ **y** $S_{2}$**, los tiempos de llegada de los primeros dos eventos**.

Es decir, con $0 < t_{1} < t_{2} < t$ y sea $h_{i}$ lo suficientemente pequeño para que $t_{i}+h_{i} < t_{i+1}$ para $i=1,2$ con $t_{3}=t$

Observe que en realidad nos gustaría calcular:

$$\lim_{h_{i}\rightarrow 0}\frac{F_{S_{i}}(t_{i}+h_{i})-F_{S_{i} }(t_{i})}{h_{i}}$$

para $i=1,2$ pero $S_{1}$ y $S_{2}$ son claramente dependientes

##  {.scrollable}

Así que debemos utilizar la independencia de los incrementos construidos sobre intervalos de tiempo disjuntos:

$$
\begin{align*}&P\left(t_{1} < S_{1}\leq  t_{1}+ h_{1}, t_{2} < S_{2} \leq t_{2}+ h_{2}\Big| N(t)=2\right)\\&= \frac{P\left(t_{1} < S_{1}\leq  t_{1}+ h_{1}, t_{2} < S_{2} \leq t_{2}+ h_{2}, N(t)=2\right)}{P(N(t)=2)}\\\\&= P(N(t_{1}+h_{1})-N(t_{1})=1)P(N(t_{2}+h_{2})-N(t_{2})=1)P(A)\\&=\frac{P\left(N(h_{1})=1\right)P\left(N(h_{2})=1\right)P\left(N(t-h_{1}-h_{2})=0\right)}{P(N(t)=2)}\\&=\frac{\frac{e^{-\lambda h_{1}}(\lambda h_{1})^{1}}{1!}\frac{e^{-\lambda h_{2}}(\lambda h_{2})^{1}}{1!}\frac{e^{-\lambda(t-h_{1}-h_{2})}[\lambda(t-h_{1}-h_{2})]^{0}}{0!}}{\frac{e^{-\lambda t}(\lambda t)^{2}}{2!}}\\&= \frac{h_{1}h_{2} 2!}{t^{2}}\end{align*}
$$

En donde $A=$ es el evento de obtener cero eventos fuera de los intervalos $(t_{1},t_{1}+h_{1}]$, $(t_{2},t_{2}+h_{2}]$ dentro de $(0,t]$.

## 

Finalmente:

$$
\begin{align*}\lim_{(h_{1},h_{2})\rightarrow (0,0)}\frac{P\left(t_{1} < S_{1}\leq  t_{1}+ h_{1}, t_{2} < S_{2} \leq t_{2}+ h_{2}\Big| N(t)=2\right)}{h_{1}h_{2}}=&\frac{2!}{t^{2}} \end{align*}
$$

## Caso general: {.scrollable}

Tenemos que calcular **la densidad condicional de** $S_{1}, \ldots, S_{n}$ **dado que** $N(t)=n$.

Sea $0 < t_1 < t_2 < \ldots < t_{n-1}=t$ y sea $h_i$ lo suficientemente pequeño para que $t_i+h_i < t_{i+1} \qquad i=1,2,\ldots,n$. Ahora,

$$
\begin{align*}& P(t_i < S_i \leq t_i+h_i, \quad i=1,2,\ldots,n\Big|N(t)=n)\\ &=\frac{P(\text{exactamente 1 evento en } (t_i,t_i+h_i], \quad i=1,\ldots,n)}{P(N(t)=n} \\&= \frac{\lambda h_1 e^{-\lambda h_{1}} \ldots \lambda h_n e^{\lambda h_n} e^{-\lambda (t-h_1-h_2-\ldots -h_n)}}{\frac{e^{-\lambda t}(\lambda t)^n}{n!}} \\&= h_{1}h_{2}\cdots h_{n} \frac{n!}{t^n}\end{align*}
$$

## Recopilando {.scrollable}

$$\frac{P(t_i < S_i \leq t_i+h_i, \quad i=1,2,\ldots,n\Big|N(t)=n)}{h_1\ldots h_n} = \frac{n!}{t^n}$$

Permitiendo que cada $h_{i} \rightarrow 0$ para $i=1,2, \cdots n$, tenemos que **la función de densidad conjunta** de la variable aleatoria $(S_{1}, S_{2},\cdots, S_{n})\Big| N(t)=n$ viene dada por

$$f\left(t_{1}, \ldots, t_{n}\Big|N(t)=n\right) = \frac{n!}{t^n} $$

para $\quad 0 < t_{1} < \ldots < t_n$.

Esta función de densidad se conoce como **la función de densidad conjunta de** $(U_{(1)},U_{(2)},\cdots, U_{(n)})$ **los estadísticos de orden de la sucesión de variables aleatorias independientes** $U_{1}, U_{2}, \cdots, U_{n}\sim U(0,t)$

$$\{(S_1,\ldots,S_n)|N(t)=n\} \sim (U_{(1)},\ldots, U_{(n)})$$

## ¿Qué aprendimos hoy?
