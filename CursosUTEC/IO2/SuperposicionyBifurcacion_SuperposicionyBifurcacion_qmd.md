---
curso: IO2
titulo: SuperposicionyBifurcacion__SuperposicionyBifurcacion
slides: 0
fuente: SuperposicionyBifurcacion__SuperposicionyBifurcacion.qmd
---

---
title: "Superposición y Bifurcación de Procesos de Poisson Homogéneos"
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

## Objetivos: Superposición y Bifurcación de Procesos de Poisson Homogéneo

-   **Formular y distinguir** los modelos de **superposición y bifurcación de Procesos de Poisson Homogéneos**.

-   **Ejemplificar y aplicar** los modelos de superposición y bifurcación de los Procesos de Poisson Homogéneos a **situaciones propias de las operaciones de ingeniería industrial**.

## Teorema de Superposición de Procesos de Poisson

Sean $\{N_i(t),t\geq 0\}_{i=1}^{r}$ una colección de $PPH(\lambda_i)$ independientes.

Definamos:

$$N(t)\equiv \sum_{i=1}^{r} N_{i}(t)\\$$

El proceso $\{N(t),t\geq 0\}$ es llamado la **superposición de de la colección de** $PPH$$\{N_i(t),t\geq 0\}_{i=1}^{r}$.

Note que $\{N(t),t\geq 0\}$ es, en sí mismo, un proceso de Poisson Homogéneo con parámetro $\lambda = \lambda_{1} + \ldots + \lambda_{r}$

## Ejemplo:

**Los trabajos presentados para su ejecución en un servidor central en un centro de cómputo se dividen en cuatro clases de prioridad, indexados** $1, 2, 3, 4$**. Los tiempos entre llegadas de dos trabajos consecutivos de la misma prioridad** $i$ **son variables aleatorias exponenciales independientes e idénticamente distribuídas con medias en minutos dadas por** $m_{1}=10, m_{2}=15, m_{3}=30, m_{4}=60$ **respectivamente. Suponga que todas las clases de prioridad se comportan independientemente entre sí. ¿Cuál es la probabilidad de que ningún trabajo llegue en un intervalo de 10 minutos?**

## Solución:

Sea $N(t)$ el número total de trabajos de todas las prioridades que se llegan en $(0,t]$. Observe que

\$\$

\lbrace{{N(t), t\geq 0}}\rbrace \text{ es un PPH }\left(\frac{13}{60}\right)

\$\$

por ser la superposición de los Procesos de Poisson que cuentan los trabajos de las 4 prioridades conocidas.

$$
P\left(N\left(10\right)=0\right)= \frac{e^{-\left(\frac{(13)(10)}{60}\right)}\left[\frac{(13)(10)}{60}\right]^{0}}{0!} = e^{-\frac{13}{6}}
$$

## Teorema: Probabilidad de que un evento provenga de un PPH dado

Sea $Z_{n}=k$ si el n-ésimo evento en el proceso $\{N(t),t\geq 0\}$ que viene del proceso $\{N_{k}(t),t\geq 0\}$. $\{Z_{n},n\geq 1\}$ es una sucesión de v.a. i.i.d. con

$$P\left(Z_{n}=k\right)=\frac{\lambda_{k}}{\lambda} \quad k=1,2,\ldots,r$$

## Prueba: {.scrollable}

Sea $T_{1}^{(k)}$ **el momento en donde se procesa el primer trabajo de prioridad** $k$. Es decir, el primer evento de $\{N_{k}(t),t\geq 0\}$.

Claramente, $T_{1}^{(k)}\sim \exp\left(\lambda_{k}\right)$. Observe además que la colección $\{T_{1}^{(k)},k=1,2,\ldots,r\}$ **es una sucesión de v.a. independientes** ya que los PPH $\{N_{k}(t),t\geq 0\}$ también lo son.

Por lo tanto,

$$
\begin{align}
P\left(Z_{1}=k\right)=& P\left[\text{Primer evento de } N(t) \text{ viene de } N_{k}(t)\right]\\=& P\left[T_{1}^{(k)}\leq \min{\left(T_{1}^{(1)},\ldots,T_{1}^{(r)}\right)}\right]\\=& \frac{\lambda_{k}}{\sum_{i=1}^{r} \lambda_i}= \frac{\lambda_{k}}{\lambda}
\end{align}
$$

**Recuerde que de las propiedades de la variable aleatoria exponencial tenemos que** $\min{\left(T_{1}^{(1)},\ldots,T_{1}^{(r)}\right)}\sim \exp(\lambda)$**, pues todas los** $T_{1}^{(k)}$ **son independientes al ser los tiempos entre llegadas de procesos de Poisson independientes.**

## Ejemplo

**Los clientes que llegan a un banco pueden clasificarse en tres categorías. Los clientes de la categoría** $1$ **sólo depositan dinero, categoría** $2$ **sólo retiran dinero y categoría** $3$ **realizan ambas acciones. Los depósitos toman** $3$ **minutos, los retiros** $4$ **minutos y las transacciones combinadas** $6$ **minutos en promedio. Los clientes de categoría** $i$ **llegan al banco siguiendo un** $PPH(\lambda_{i})$ **con** $\lambda_{1}=20$**,** $\lambda_{2}=15$**,** $\lambda_{3}=10$ **por hora. ¿Cuál es el tiempo promedio de transacción de un cliente típico para el banco? ¿Son los tiempos de transacciones sucesivas independientes?**

## Solución: {.scrollable}

En vista del último teorema, un cliente típico pertenece a la categoría $i$ con las siguientes probabilidades:

$$
P\left(Z_{n}=1\right)=\frac{20}{45}\\P\left(Z_{n}=2\right)=\frac{15}{45}\\P\left(Z_{n}=3\right)=\frac{10}{45}
$$

Por lo tanto, si $T$ **es el tiempo en minutos de una transacción cualquiera**, entonces:

$$E(T)=3\cdot\frac{20}{45} + 4\cdot\frac{15}{45} + 6\cdot\frac{10}{45} = \frac{180}{45} = 4 \text{ minutos }.$$

**Los tiempos de transacciones sucesivas son i.i.d. ya que las categorías de clientes sucesivos son v.a. i.i.d.**

## Teorema: Bifurcación de un PPH

Ahora suponga que un evento de un $PPH(\lambda)$ que llega a tiempo $s$ es clasificado como tipo I o tipo II con probabilidades $P(s)$ y $1-P(s)$ independientemente de todo lo demás.

Entonces, si $N_{i}(t)$ representa el número de eventos tipo $i$ que ocurren en $(0,t]$ con $i=1,2$ entonces $N_1(t)$ **y** $N_2(t)$ **son v.a. poisson independientes con medias** $\lambda tp$ **y** $\lambda t (1-p)$ respectivamente con

$$p \equiv \frac{1}{t} \int_0^t P(s)ds$$

## Ejemplo

**Los clientes entran a una tienda de acuerdo a un proceso de Poisson con tasa de llegada 16 por hora. De manera independiente, cada cliente compra algo con probabilidad** $p = 0.25$ **o sale de la tienda sin comprar nada con probabilidad** $q = 1−p = 0.75$**. ¿Cuál es la probabilidad de que durante la primera hora 9 personas entren a la tienda y sólo tres de estas personas compren algo y las otras 6 no?**

## Solución {.scrollable}

Usemos el teorema de bifurcación de Procesos de Poisson Homogéneos. Sea $N_{C}(t)$ el número de clientes que COMPRAN algo hasta el instante $t$ $\sim Poisson(16*0.25*t)=Poisson(4t)$

Sea $N_{NC}(t)$ el número de clientes que NO COMPRAN algo hasta el instante $t$ $\sim Poisson(16*0.75*t)=Poisson(12t)$

$$
\begin{align}
P[N_{NC}(1)= 6 , N_{C}(1)= 3] =& P[N_{NC}(1)= 6]P[N_{C}(1)= 3]\\&\text{ por independencia de } N_{C}(t) \text{ y } N_{NC}(t)\\& \text{ en vista del teorema de bifurcación }\\=& e^{-12}\frac{(12)^6}{6!}e^{-4}\frac{(4)^3}{3!}
\end{align}
$$

En R,

```{r echo=TRUE}
dpois(6,12)*dpois(3,4)
```

## Prueba:

Comencemos por calcular la función de probabilidad de masa conjunta de $N_{1}(t)$ y $N_{1}(t)$.

$$
\begin{align}
&P\left(N_1(t)=n, N_2(t)=m\right)\\\\& \text{ por ley de probabilidad total}\\\\=& \sum_{k=0}^{+\infty} P\left(N_1(t)=n, N_2(t)=m|N(t)=k\right) P\left(N(t)=k\right)\\\\&\text{ observe que uno sólo de los sumandos es no nulo}\\\\=& P\left(N_{1}(t)=n, N_2(t)=m|N(t)=n+m\right) P\left(N(t)=n+m\right)
\end{align}
$$

## Continuación de la prueba: {.scrollable}

Ahora, considere un evento que ocurrió en $(0,t]$. Si hubiese ocurrido a tiempo $s < t$, entonces la probabilidad de que de que fuese tipo I es $P(s)$. Entonces, por el **teorema de la distribución condicional de los tiempos de llegada**, este evento ocurrió en algún momento uniformemente distribuido en $(0,t]$, entonces si llamamos $p=$ **la probabilidad de que el evento sea de tipo I**, la misma se puede calcular de la siguiente manera:

$$
\begin{align}
&p = \int_{0}^{t} P(\text{ Evento sea Tipo I }\Big| \text{ ocurrió en } s)f_{S_{1}|N(t)=1}(s)ds\\&=\int_0^t P(s)\frac{1}{t}ds\\&=\frac{1}{t}\int_0^t P(s)ds
\end{align}
$$

independientemente de otros eventos. Por lo tanto,

$$P\left(N_1(t)=n, N_2(t)=m\Big|N(t)=n+m\right)=\binom{n+m}{n}p^n (1-p)^m\\\\$$

## Retomando:

Por lo tanto,

$$
\begin{align}
&P\left(N_1(t)=n, N_2(t)=m\right)\\=& P\left(N_1(t)=n, N_2(t)=m\Big|N(t)=n+m\right) P\left(N(t)=n+m\right)\\=& \binom{n+m}{n}p^n (1-p)^m \cdot \frac{e^{-\lambda t} (\lambda t)^{n+m}}{(n+m)!}\\&\text{reagrupando inteligentemente,}\\=& \frac{(\lambda tp)^n e^{-\lambda tp}}{n!} \frac{[(1-p)\lambda t]^m e^{-\lambda t(1-p)}}{m!}
\end{align}
$$

Lo que prueba, no sólo que $N_{1}(t)\sim Poisson(\lambda t p)$**,** $N_{2}(t)\sim Poisson(\lambda t (1-p))$ **sino además que** $N_{1}(t)$$N_{2}(t)$ **son independientes.**

## Ejemplo

**Clientes llegan a una estación de servicio** $PPH(\lambda)$**. Infinitos servidores con tiempos de servicios independientes e idénticamente distribuidos con función de distribución acumulativa** $G$**. Calcule la distribución conjunta del número de clientes que han completado su tiempo de servicio para tiempo** $t$ **y el número de clientes que están en servicio para tiempo** $t$**.**

## Solución: {.scrollable}

Ahora, si un cliente entra al sistema a tiempo $s$ con $s\leq t$, será de tipo I si su tiempo de servicio es menor que $t-s$ para que haya terminado su servicio a tiempo $t$. Sea $T$ el tiempo de servicio de un cliente. Entonces, la probabilidad de clasificar a un cliente que llega a tiempo $s$ como Tipo I viene dada por:

$$P(s)=P(T \leq t-s) \equiv G(t-s) \qquad s \leq t$$

Por el teorema de bifurcación de los procesos de Poisson homogéneos:

$$
N_1(t)=PPH\left(\lambda \int_0^t G(t-s) ds \right)\\N_2(t)=PPH\left(\lambda \int_0^t (1-G(t-s)) ds \right)
$$

con $N_1(t)$ independiente de $N_2(t)$

## ¿Qué aprendimos hoy?
