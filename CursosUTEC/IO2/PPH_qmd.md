---
curso: IO2
titulo: PPH
slides: 0
fuente: PPH.qmd
---

---
title: "Procesos de Poisson Homogéneos"
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.JPG
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
editor: visual
date: "Mayo,2023"
---

## Objetivos generales: Introducción a procesos de Poisson Homogéneos.

::: incremental
-   Definir **Procesos de Poisson Homogéneo**.

-   Deducir a partir del proceso de Poisson Homogéneo **el proceso estocástico de los tiempos entre llegadas.**

-   Enunciar, distinguir y demostrar la **equivalencia de las dos definiciones de los procesos de Poisson Homogéneos, la operativa y la validadora.**

-   Visualizar los aspectos relacionados con la **validación de un proceso de Poisson homogéneo** a partir de data simulada y real en el contexto de las operaciones propias de la ingeniería industrial.

-   Definir y visualizar **los tiempos entre llegadas y de llegadas de un proceso de Poisson Homogéneo simulado**.
:::

## Recordemos lo que es un proceso estocástico

Un **proceso estocástico** es una colección de variables aleatorias

$$ \{X(\alpha), \alpha \in T\}$$

indexadas por un parámetro $\alpha$ que toma valores en un conjunto de parámetros T.

Las variables aleatorias toman valores en un conjunto $S$ que llamaremos **conjunto de estados** del proceso estocástico. El conjunto $T$ en el cual las variables aleatorias están indexadas lo interpretaremos como el **tiempo**.

## Monitoreo a tiempo discreto

$$T=\{0,1,2,\ldots\}$$

para lo cual escribimos $\{X_n, n\geq 0\}$ en lugar de $\{X(\alpha), \alpha \in T\}$

Con **conjunto de estados** $S$. Algunas veces $S \subseteq \{0,1,\ldots\}$ es **discreto**. Otras veces es **continuo** $S \subset (-\infty,\infty)$

## Ejemplo: tiempo continuo y conjunto de estados discreto

```{r, echo=FALSE}
lambda<-15  #15 llegadas/hora 

t<- 2    #horas

n<-rpois(1,lambda*t)

X<-c(0,sort(runif(n,min=0,max=t)))
```

```{r,echo=FALSE}
plot(X,(0:n),type="s",ylab="Conjunto de estados discreto",xlab="tiempo continuo en horas",main="Número de clientes como función del tiempo")
```

## Monitoreo del tiempo continuo:

El monitoreo del proceso puede ser a **tiempo continuo**:

$$T=[0,\infty)$$

para lo cual escribimos

$$\{X(t), t \geq 0\}$$

en lugar de $\{X(\alpha), \alpha \in T\}$

Con **conjunto de estados** $S$ **continuo o discreto**. Recordemos que el conjunto de estados es la imagen de cada variable aleatoria $X(t)$.

## Ejemplo: tiempo y conjunto de estados continuos

```{r, echo=FALSE}

t <- 0:100  # time

sigma2 <- 0.3

## first, simulate a set of random deviates

W <- rnorm(n = length(t) - 1, sd = sqrt(sigma2))

## now compute their cumulative sum

W <- c(0, cumsum(W))

plot(t, W, ylab= "Conjunto de estados continuo", xlab= "tiempo continuo", type = "l", ylim = c(-6, 6), main="Movimiento Browniano")

```

## Definición de un Proceso Estocástico de Conteo

Se dice que un proceso estocástico $\{N(t), t \geq0\}$ es un **proceso de conteo** si $N(t)$ representa el **número total de "eventos" que han ocurrido en el intervalo** $(0,t]$. Debe satisfacer:

1.  $N(t) \geq 0$

2.  $N(t)$ toma únicamente valores enteros positivos

3.  Si $s < t$, entonces $N(s) \leq N(t)$

4.  Para $s < t, N(t) - N(s)$ es igual al **número de eventos que han ocurrido en el intervalo** $(s,t]$

## Incrementos estacionarios independientes

Se dice que un proceso estocástico $\{N(t), t \geq0\}$ tiene **incrementos estacionarios** si:

-   La distribución del incremento $N(t+s)-N(s)$ no depende de $s$.

En otras palabras, las distribuciones de las variables aleatorias $N(t+s)-N(s)$ y de $N(t)$ son las mismas indistintamente de dónde se encuentre el intervalo de tiempo $(s, s+t]$.

En este caso, diremos que $s$ es la posición del intervalo de tiempo y del incremento y $t$ su longitud o duración.

## Incrementos independientes:

-   Diremos que los incrementos son **independientes** si los mismos ocurren sobre **intervalos de tiempo disjuntos**.

## Definición computacional del Proceso de Poisson Homogéneo

Se dice que el proceso de conteo $\{N(t), t \geq0\}$ es un Proceso de Poisson parámetro $\lambda$, $PPH(\lambda)$, con $\lambda > 0$ si:

$$
\begin{align*}
&\text{1) } N(0)=0\\&\text{2) }\{N(t), t\geq 0\} \text{ tiene incrementos disjuntos independientes}\\&\text{3) }P(N(t+s)-N(s) = n)=e^{- \lambda t} \frac{(\lambda t)^n}{n!}\\
\end{align*}
$$

para $n=0,1,2,\ldots$

Observe que cuando $t=1$, el proceso de Poisson parámetro $\lambda t$ se reduce a la conocida variable aleatoria Poisson parámetro $\lambda$.

## ¿Cómo luce un Proceso de Poisson en la práctica?

Observe que aquí el proceso se monitorea en tiempo continuo $T=[0,\infty)$, pero el conjunto de estados $S=\{0,1,2,\cdots\}$ es discreto

$\lambda =$ 10 llegadas por hora.

```{r, echo=FALSE}

lambda<-10 #10 llegadas/hora

t<- 2 #horas

n<-rpois(1,lambda*t)

X<-c(0,sort(runif(n,min=0,max=t)))
```

```{r, echo=FALSE}

plot(X,(0:n),type="s",ylab="número de llegadas",xlab="tiempo en horas",main="Número de llegadas en función del tiempo")

```

## Ejemplo:

Supongamos que los clientes llegan a un banco de acuerdo con $PPH (\lambda)$ con $\lambda = 10$ clientes/hora.

-   ¿Cuál es el número esperado de clientes que llegan al banco durante un día de 8 horas?

## Solución:

El valor esperado de clientes que llegan al banco durante un día de 8 horas es:

$$E[N(8)]=80 \text{ clientes .}$$

## Continuación del ejemplo:

-   ¿Cuál es la distribución del número de clientes atendidos durante un día de 8 horas?

## Solución:

La distribución del número de clientes atendidos durante un día de 8 horas es:

$$N(8)\sim Poiss(8(10)) = Poiss(80)$$

En otras palabras, la **función de probabilidad de masa de** $N(8)$ viene dada por:

$$P(N(8)=k) = \frac{e^{-80} (80)^k}{k!} \qquad k=0,1,2,\ldots$$

## Continuación del ejemplo:

-   ¿Cuál es la probabilidad de que ningún cliente llegue al banco entre la 1:00 PM y la 1:06 PM?

## Solución:

La probabilidad de que ningún cliente llegue al banco entre la 1:00 P.M: y la 1:06 PM se calcula así:

Por la estacionariedad de los incrementos, la probabilidad requerida puede calcularse como sigue:

$$
\begin{align*}
P(N(5.1)-N(5)=0)=&P(N(0.1) = 0)\\=& e^{-10(0.1)}\\=& e^{-1} \approx 0.3678
\end{align*}
$$

## Continuación del ejemplo: {.scrollable}

-   ¿Cuál es la probabilidad de que llegue al banco un cliente entre la 1:00 PM y 1:06 PM y 2 clientes lleguen entre la 1:03 PM y 1:12 PM?

**Cuidado que si los intervalos de tiempo sobre el cual están definidos los incrementos no son disjuntos, entonces los incrementos son variables aleatorias no independientes.**\*

La probabilidad requerida asumiendo que el banco abre a las 8:00 AM,

$$P[N(5.1)-N(5)=1, N(5.2)-N(5.05)=2]$$

Pero podríamos colocar $t=0$ a la 1:00 PM para simplificar la cuenta. Es decir, la probabilidad requerida entonces podría escribirse así:

$$P[N(0.1)-N(0)=1, N(0.2)-N(0.05)=2]$$

## Continuando con el ejemplo del banco:

Como los **intervalos de tiempo** $(0, 0.1]$ **y** $(0.05, 0.2]$ **no son disjuntos,** **sus incrementos** $N(0.1)-N(0)=1$ **y** $N(0.2)-N(0.05)$ **no son independientes**.

Por lo tanto, debemos **disjuntizar los intervalos dados en los siguientes** $(0, 0.05]$**,** $(0.05, 0.1]$ **y** $(0.1, 0.2]$ de la siguiente manera:

$$
\begin{align*}
&P\left[N(0.1)=1, N(0.2)-N(0.05)=2\right]\\&\text{ Caso No.1 }\\&=P\left[N(0.05)=0, N(0.1)-N(0.05)=1, N(0.2)-N(0.1)=1\right]\\&\text{ Caso No. 2 }\\&+ P\left[N(0.05)=1, N(0.1)-N(0.05)=0, N(0.2)-N(0.1)=2\right]\\
\end{align*}
$$

## Usando estacionariedad de los incrementos:

Ahora como los intervalos de tiempo sobre los cuales están definidos los incrementos son disjuntos, podemos garantizar la \*\*independencia de los incrementos\*\*:

$$
\begin{align*}
&P\left[N(0.05)=0, N(0.1)-N(0.05)=1, N(0.2)-N(0.1)=1\right]\\&+ P\left[N(0.05)=1, N(0.1)-N(0.05)=0, N(0.2)-N(0.1)=2\right]\\&=P[N(0.05)=0]P[N(0.1)-N(0.05)=1]P[N(0.2)-N(0.1)=1]\\&+ P[N(0.05)=1)P[N(0.1)-N(0.05)=0]P[N(0.2)-N(0.1)=2]\\
\end{align*}
$$

## Finalmente:

Podemos usar la estacionariedad de los incrementos:

$$
\begin{align*}
P(N(t+s)-N(s) = n) =& P(N(t)=n)\\=&e^{- \lambda t} \frac{(\lambda t)^n}{n!}
\end{align*}
$$

## La probabilidad requerida es:

$$
\begin{align*}
&P[N(0.1)=1, N(0.2)-N(0.05)=2]\\&=P[N(0.05)=0]P[N(0.1)-N(0.05)=1]P[N(0.2)-N(0.1)=1]\\&+ P[N(0.05)=1]P[N(0.1)-N(0.05)=0]P[N(0.2)-N(0.1)=2]\\&\text{ por estacionariedad de los incrementos }\\&=P[N(0.05)=0]P[N(0.05)=1]P[N(0.1)=1]\\&+ P[N(0.05)=1]P[N(0.05)=0]P[N(0.1)=2]\\&=\frac{3}{4}e^{-2}
\end{align*}
$$

## Distribuciones de tiempos entre llegadas y tiempos de llegada {.scrollable}

Considere un **proceso de Poisson Homogéneo parámetro** $\lambda$. Denotemos por

$$T_{1} = \text{ tiempo donde ocurre la primera llegada}$$y para $n > 1$,

$$ 
T_{n}= \text{ tiempo entre las llegadas n-1} \text{ y } n
$$Llamaremos a

$$\{T_n, n\geq 1\}$$

**la sucesión de los tiempos entre llegadas de un proceso de Poisson homogéneo**.

**Observe que** $\{T_n, n\geq 1\}$ **es un proceso estocástico monitoreado a tiempo discreto con conjunto de estados continuo.**

## Queremos determinar:

Las **distribuciones de los tiempos de llegada**

$$P(T_{n} \leq t) \quad \forall \quad n \geq 1$$

a partir del Proceso de Poisson Homogéneo que los genera.

## Comencemos por el primer tiempo de llegada

$$P(T_1 > t) = P(N(t)=0) = e^{- \lambda t}$$

Por lo tanto,

$$T_1 \sim exp(\lambda)$$

## El segundo tiempo entre llegadas {.scrollable}

Para calcular la distribución de \$T\_{2}\$, el tiempo entre la llegada del primer cliente y del segundo debemos condicionar con respecto al momento en el que llegó el primer cliente, \$T\_{1}\$, de la siguiente manera:

$$P(T_2 > t) = \int_{0}^{\infty}P(T_2 > t | T_1 = s)f_{T_{1}}(s)ds$$

donde,

$$
\begin{align*}
P(T_2 > t | T_1 = s) &= P\{0 \text{ eventos en } (s, s+t] | T_1=s\} \\=& P\{0 \text{ eventos en }(s,s+t]\} \\=& P(N(s+t)-N(s)=0)\\&\text{ por la estacionariedad de los incrementos }\\=& P(N(t)=0)\\=& P\{N(t)=0\} \\=& e^{-\lambda t}
\end{align*}
$$

## Independencia de los tiempos entre llegadas:

Observe que,

$$P(T_2 > t | T_1 = s)= e^{-\lambda t}$$

no depende de $s$.

Es decir, $T_{2}$ no depende del lugar donde ocurra $T_{1}$.

Por lo que $T_{1}$ **y** $T_{2}$ **son independientes**

## Finalmente, {.scrollable}

$$
\begin {align*}P(T_2 > t)=& \int_{0}^{\infty}P(T_2 > t | T_1 = s)f_{T_{1}}(s)ds\\=& \int_{0}^{\infty}e^{-\lambda t}\lambda e^{-\lambda s} ds \\=& e^{-\lambda t} \int_o^{\infty} \lambda e^{-\lambda s} ds \\=& e^{-\lambda t} \\\end {align*}
$$

Por lo que hemos demostrado que,

$$T_2 \sim exp(\lambda)$$

y

$$T_{2} \text{ es independiente de } T_{1}$$

## Teorema de los tiempos entre llegadas

Un argumento inductivo nos permitiría demostrar que,

$$\{T_{n}, n\geq 1 \}$$

la sucesión de los **tiempos entre llegadas de un** $PPH(\lambda)$ es una sucesión de variables aleatorias **independientes e idénticamente distribuidas exponenciales parámetro** $\lambda$.

## Teorema de los tiempos de llegada

Sea $S_{n}=$ **el tiempo de llegada del n-ésimo evento**

$$S_{n}=\sum_{i+1}^n T_{i} \quad n \geq 1$$

$$S_{n} \sim Gamma(n,\lambda)=Erlang(n,\lambda)$$

$$f_{S_{n}}(t)= \lambda e^{-\lambda t} \frac{(\lambda t)^{n-1}}{(n-1)!}$$

$$
\begin{align*}
F_{S_n}(t) &= P(S_n \leq t) \\&= P(N(t) \geq n) \\&= \sum_{j=n}^{+ \infty} e^{-\lambda t} \frac{(\lambda t)^j}{j!}
\end{align*}
$$

## Ejemplo:

Asuma que taxis llegan como un $PPH(\lambda=10/hora)$ a una parada. Cada taxi lleva exactamente un pasajero y no más. Tu eres el primero en la cola de los pasajeros, ¿cuál es la probabilidad de que te toque esperar por más de 15 minutos?

## Solución:

Sea $T_{1}$ el tiempo de llegada desde $t=0$ hasta que llega el primer taxi.

La probabilidad requerida es:

$$P\left(T_{1} > \frac{1}{4}\right)= e^{-\frac{10}{4}}= 0.082085$$

```{r, echo=FALSE}
exp(-2.5)

```

## Continuación del ejemplo: {.scrollable}

Supongamos que ahora eres el tercer pasajero en cola. ¿Cuál es la probabilidad que te toque esperar más de 30 minutos?

Sean $T_{i}$ el tiempo entre llegadas de los taxis $i-1$ y $i$ para n=1,2,3.

Y sea $S_{n}\sum_{i=1}^{n}T_{i}\sim Erlang(n,10)$

La probabilidad requerida es:

$$
\begin{align*}
P\left(T_{1}+T_{2}+T_{3}>\frac{1}{2}\right)=&P\left(S_{3}>\frac{1}{2}\right)\\=& P\left[N\left(\frac{1}{2}\right) < 3\right]\\=& \sum_{i=0}^{2}P\left[N\left(\frac{1}{2}\right) = i\right]\\=& e^{-5}+5e^{-5}+\frac{25}{2}e^{-5}=0.124652
\end{align*}
$$

```{r}
ppois(2,5)
pgamma(q=1/2, shape=3, scale=10, lower.tail = FALSE)
```

## Definición validadora de un Proceso de Poisson {.scrollable}

Se dice que el proceso de conteo $\{N(t), t \geq0\}$ es un **Proceso de Poisson Homogéneo** con tasa de llegada $\lambda > 0$, si satisface que:

$$
\begin{align*}
&\text{1) } N(0)=0\\&\text{2) } \{N(t), t\geq 0\}\\&\text{posee incrementos estacionarios e independientes}\\&\text{3) }P(N(h)=1) = \lambda h + o(h)\\&\text{4) }P(N(h) \geq 2)= o(h)
\end{align*}
$$

en donde diremos que una función $f(h)=o(h)$ si satisface que $\lim_{h \to 0} \frac{f(h)}{h}=0$

**Las dos definiciones de Procesos de Poisson Homogéneos, la computacional y la validadora son equivalentes.**

## Visualización de la definición validadora

```{r, echo=FALSE}
lambda<-30 #30 llegadas/hora

t<-6 #horas

n<-rpois(1,lambda*t)

X<-c(0,sort(runif(n,min=0,max=t)))

```

```{r,echo=FALSE}
plot(X,(0:n),type="s",ylab="llegadas",xlab="tiempo (h)",main="Llegadas en función del tiempo")
```

## 

```{r, echo=FALSE}
m<-10

B<-cut(c(X,t),m,include.lowest = TRUE)
table(B)

```

```{r, echo=FALSE}
barplot(table(B),las=3)

```

## Visualizando la condición 3)

```{r, echo=FALSE}
P1<-0

P2m<-1

H<-t

for(m in 2:6000){

B <- cut(c(X,t),m,include.lowest = TRUE)

Y <- table(B)

P1[m] <- sum(Y==1)/m

P2m[m] <- sum(Y>1)/m

H[m]<-t/m

}

```

```{r,echo=FALSE}
library(graphics)

```

```{r,echo=FALSE}
plot(1:m,P1/H,pch=20,col=rgb(0,0,0,0.2),cex=0.5

,xlab="número de intervalos"

,ylab=expression(bold(P)(N(h)==1)/h)

)

abline(h=lambda,col="red")

```

## Visualizando la condición 4)

```{r, echo=FALSE}
plot(1:m,P2m/H,pch=20,cex=0.5,col=rgb(0,0,0,0.2)

,xlab="número de intervalos"

,ylab=expression(bold(P)(N(h)>1)/h)

)

abline(h=0,col="blue")

```

## 

Número de intervalos mínimo para que **todos** los intervalos tengan a lo mucho una sola observación adentro.

```{r, echo=FALSE}
ceiling(t/min(diff(X)))
```

```{r, echo=FALSE}
m<-ceiling(t/min(diff(X)))

B<-cut(c(X,t),m,include.lowest = TRUE)

Y<-table(B)
```

```{r, echo=FALSE}
p1<-sum(Y==1)/m

p2m<-sum(Y>1)/m

```

```{r, echo=FALSE}
lambdaestimado<-p1/(t/m)

lambdaestimado

```

## Visualizando los tiempos entre llegadas

```{r,echo=FALSE}
hist(diff(X)

#,breaks=20

,col="lightgreen"

,prob=TRUE

,xlab="incrementos"

,ylab="densidad"

,ylim=c(0,lambda+5)

,main="Histograma de incrementos"

)

Abcisas<-seq(0,max(diff(X)),length.out = 100)

lines(Abcisas,dexp(Abcisas,rate=lambda),col="black",lwd=2,lty=2)

lines(Abcisas,dexp(Abcisas,rate=lambdaestimado),col="red",lwd=2)

legend("topright"

,legend=c("densidad teórica","densidad observada")

,col=c("red","black")

,lty=c(1,2)

,lwd=2,bty="n")

```

## Teorema: Equivalencia de las definiciones

**Las dos definiciones de Procesos de Poisson Homogéneos, la computacional y la validadora son equivalentes.**

**Prueba:**

Definición Validadora $\implies$ Definición Computacional

Definamos:

$$P_{n}(t)\equiv P(N(t)=n)$$

## Recordemos el cociente incremental

Comenzaremos por determinar $P_{0}(t)=P(N(t)=0)$.

Para lo cual, se desea plantear una ecuación diferencial cuya solución sea dicha probabilidad. Para hallar su derivada invocaremos a su **cociente incremental**

$$P_{0}´(t)\equiv \lim_{h\rightarrow 0}\frac{P_{0}(t+h)-P_{0}(t)}{h}$$

en caso dicho límite exista.

## Buscando la derivada requerida

Comencemos por calcular $P_{0}(t+h)$

$$
\begin {align*}
P_{0}(t+h) &\equiv P[N(t+h)=0] \\& \text{ disjuntizando}\\&= P[N(t)=0, N(t+h)-N(t)=0] \\& \text{ por independencia de 2) def. validadora}\\&= P[N(t)=0] P[N(t+h)-N(t)=0] \\&\text{ por estacionariedad 2) def. validadora)}\\&= P[N(t)=0] P[N(h)=0] \\&= P_{0}(t)(1-P(N(h)>0)) \\&= P_{0}(t)(1-P(N(h)=1) - P(N(h) \geq 2)) \\& \text{ usando 3) y 4) de la definción validadora}\\&= P_{0}(t)(1-\lambda h + o(h)) \quad \therefore
\end {align*}
$$

## Calculando el cociente incremental

$$
\begin{align*}
\frac{P_{0}(t+h)-P_{0}(t)}{h} &= \frac{P_{0}(t)(1-\lambda h + o(h))-P_{0}(t)}{h} \\&= \frac{-\lambda P_{0}(t) h + P_{0}(t)o(h)}{h} \\&= -\lambda P_{0}(t)+ P_{0}(t)\frac{o(h)}{h} \qquad h\rightarrow 0 \\&= -\lambda P_{0}(t)
\end{align*}
$$

## La ecuación diferencial requerida es:

$$P_{0}'(t)=\lim_{h\to 0} \frac{P_{0}(t+h)-P_{0}(t)}{h}=-\lambda P_{0}(t)$$

$$\frac{P_{0}'(t)}{P_{0}(t)}=-\lambda$$

la cuál es una **ecuación diferencial en variables separables**.

## Resolviendo la ecuación diferencial:

Integrando ambos lados con respecto a $t$, obtenemos que:

$$
\begin{align*}
\log{(P_{0}(t))} =& -\lambda t + c \\&\text{tomando exponencial a ambos lados}\\P_{0}(t) =& k e^{-\lambda t}\\&\text{condición inicial}\\P_{0}(0)=&P(N(0)=0)=1 \implies k=1\\\therefore P_{0}(t)=& P(N(t)=0) = e^{-\lambda t}
\end{align*}
$$

como queríamos demostrar en el caso $n=0$.

## Para el caso general {.scrollable}

Similarmente, para $n \geq 1$,

$$
\begin{align*}
&P_{n}(t+h)=P(N(t+h)=n)\\&\text{ disjuntizando el intervalo } (0,t+h]\\=& P(N(t)=n,N(t+h)-N(t)=0) \\+& P(N(t)=n-1,N(t+h)-N(t)=1) \\+& \sum_{k=2}^{n}P(N(t)=n-k,N(t+h)-N(t)=k)\\
\end{align*}
$$

Usando la independencia de los incrementos definidos sobre intervalos de tiempo disjuntos y su estacionariedad cuyas porpiedades están garantizadas de 2) de la definición validadora:

$$
\begin{align*} \therefore
P_{n}(t+h) =& P_{n}(t)P_{0}(h) + P_{n-1}(t)P_{1}(h)+ \sum_{k=2}^{n}P_{n-k}(t)P_{k}(h)\\
\end{align*}
$$

## Usando 3) y 4) de la definición validadora:

Tenemos que por 3) $P_{1}(h)=P(N(h)=1)=\lambda h + o(h)$, por 4) $P_{k}(h)=P(N(h)=k)=o(h)$ para todo $k\geq 2$ y por el caso $n=0$ $P_{0}(h)=e^{-\lambda h}$, por lo que:

$$
\begin{align*} \therefore
P_{n}(t+h) =& P_{n}(t)P_{0}(h) + P_{n-1}(t)(\lambda h + o(h))+ o(h)\\=& P_{n}(t)P_{0}(h) + P_{n-1}(t)\lambda h + o(h)\\=& P_{n}(t)e^{-\lambda h} + P_{n-1}(t)\lambda h + o(h)\\
\end{align*} 
$$

## Calculando el cociente incremental:

$$
\begin{align*}
\frac{P_{n}(t+h)-P_{n}(t)}{h} =& \left(\frac{e^{-\lambda h}-1}{h}\right) P_{n}(t)+\lambda P_{n-1}(t) + \frac{o(h)}{h}
\end{align*}
$$

Tomando el límite cuando $h\rightarrow 0$, nos queda la siguiente ecuación diferencial lineal, que al ser multiplicada por el factor integrante $e^{\lambda t}$, convierte la ecuación en una ecuación en variables separables:

$$
\begin{align*}
&P_{n}'(t)= -\lambda P_{n}(t)+\lambda P_{n-1}(t) \\&e^{\lambda t}[P_n'(t) + \lambda P_n(t)] = \lambda e^{\lambda t} P_{n-1}(t)\\& \therefore \frac{d}{dt}[e^{\lambda t}P_n(t)] = \lambda e^{\lambda t} P_{n-1}(t) \quad \bigstar
\end{align*}
$$

## Procediendo en forma inductiva

Por $\bigstar$ tenemos que para $n=1$

$$
\begin{align*}
&\frac{d}{dt}[e^{\lambda t}P_{1}(t)]=\lambda e^{\lambda t}P_{0}(t)=\lambda\\&e^{\lambda t}P_1(t)=\lambda t + c\\&P_1(t)=(\lambda t + c)e^{-\lambda t}\\&P_{1}(0)=P(N(0)=1)=0 \quad \Rightarrow c=0\\&P_{1}(t)=\lambda t e^{-\lambda t}
\end{align*}
$$

como queríamos demostrar.

## Caso general {.scrollable}

Queremos probar que $P_{n}(t)=\frac{(\lambda t)^n e^{-\lambda t}}{n!}$,

Asumamos cierto como **hipótesis inductiva** que:

$$\frac{d}{dt}(e^{\lambda t}P_n(t))=\frac{\lambda (\lambda t)^{n-1}}{(n-1)!}$$

$$
\begin{align*}
&\Rightarrow e^{\lambda t}P_{n}(t)= \int \frac{\lambda (\lambda t)^{n-1}}{(n-1)!} dt\\&= \frac{\lambda^n}{(n-1)!} \frac{t^n}{n} + c = \frac{(\lambda t)^n}{n!} + c\\&\text{ calculando la condición inicial }\\&P_{n}(0)=P(N(0)=n)=0 \implies c=0\\&\therefore P_{n}(t)=e^{-\lambda t}\frac{(\lambda t)^n}{n!} \\
\end{align*}
$$

como queríamos demostrar.

$\therefore$ **definición validadora de procesos de Poisson homogéneos** $\implies$ **la computacional**.

La otra implicación queda como ejercicio pues es sencilla.

## ¿Qué aprendimos hoy?
