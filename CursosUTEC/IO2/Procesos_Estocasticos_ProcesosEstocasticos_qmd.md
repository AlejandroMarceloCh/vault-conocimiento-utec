---
curso: IO2
titulo: Procesos_Estocasticos__ProcesosEstocasticos
slides: 0
fuente: Procesos_Estocasticos__ProcesosEstocasticos.qmd
---

---
title: "Procesos Estocásticos"
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.jpg
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
      transition: slide
editor: visual
date: "today"
---

## Objetivos

-   **Ilustrar** las diferentes fuentes de incertidumbre en algún contexto real de las operaciones propias de Ingeniería Industrial.

-   **Ejemplificar** a través de diferentes operaciones propias de la ingeniería industrial los diversos tipos de modelos probabilísticos diferenciándolos a través de sus conjuntos de estados, monitoreo del tiempo y memoria.

## ¿Qué es un proceso estocástico? {.scrollable}

-   Un **proceso estocástico** es una colección de variables aleatorias $\{X(t), t \in T\}$, indexadas en un conjunto de parámetros T.

-   Las variables aleatorias $\{X(t), t \in T\}$ que pertenecen a un mismo proceso estocástico, toman valores en un mismo conjunto $S$ que llamaremos **conjunto de estados** del proceso estocástico.

-   El conjunto $T$ en el cual las variables aleatorias del proceso estocático están indexadas lo interpretaremos como el **tiempo**.

-   En el caso en que $T=\{0,1,2,\ldots\}$, escribiremos el proceso estocástico así $\{X_{n}, n\geq 0\}$ en lugar de $\{X(t), t \in T\}$.

-   En el caso en que $T=[0,\infty)$, escribiremos el proceso estocástico así $\{X(t), t \geq 0\}$.

-   Algunas veces $S \subseteq \{0,1,\ldots\}$ o $S \subset (-\infty,\infty)$.

## Ejemplo de un proceso estocástico con conjunto de estados continuo y monitoreo del tiempo continuo.

Variación en el precio de las acciones de la bolsa de valores a lo largo del tiempo.

```{r echo=FALSE}
Z <- rnorm(255,0,1)   # Random normally distributed values, mean = 0, stdv = 1

u <- 0.3              # Expected annual return (30%)

sd <- 0.2             # Expected annual standard deviation (20%)

s <- 100              # Starting price

price <- c(s)         # Price vector

a <- 2                # See below

t <- 1:256            # Time. Days to put on the x axis

for(i in Z)

{

    S = s + s*(u/255 + sd/sqrt(255)*i)

    price[a] <- S                        

    s = S                                 

    a = a + 1

}

plot(t,price,main="Serie de tiempo de la acción ",xlab="tiempo",ylab="precio", type="l",col="blue")
```

## Proceso estocástico con conjuto de estados discreto y monitoreo del tiempo continuo.

Procesos de conteo

```{r echo=FALSE}
set.seed(1)

n<-100

x<-cumsum(rexp(50,rate=0.5))

y<-cumsum(c(0,rep(1,50)))

plot(stepfun(x,y),xlim = c(0,10),do.points = F,main="Número de eventos ocurridos en el tiempo")
```

## Ejemplo de un Proceso de Conteo

Supongamos que los eventos se observan desde el tiempo 0 en adelante.

$X(t)=$ número de eventos durante el intervalo $(0,t]$

$X(0)=0$

$X(t)$ puede representar:

-   Número de clientes que llegan a un banco en el período $(0,t]$

-   Número de nacimientos en un hospital en el período $(0,t]$

-   Número de carros que pasan por un peaje en el período $(0,t]$

-   Número de errores tipográficos en las primeras $n$ páginas de un libro

## Indicadores de interés en procesos de conteo

-   ¿Cuál es la distribución de $X(t)$ para un $t$ fijo?

-   ¿Cuál es la $E[X(t)]$?

-   ¿Qué podemos decir acerca de $X(t)$ para valores grandes de $t$?

-   Si definimos $S_{n}$ como el tiempo de ocurrencia del $n$-ésimo evento, ¿cómo se relaciona el proceso de tiempo discreto $\{S_{n}, n \geq 0\}$ con la suposición adicional de que $S_{0}=0$ con el proceso de tiempo continuo $\{X(t), t \geq0\}$ ?

## Cola con un solo servidor

Supongamos que los clientes llegan a una instalación de servicio en los tiempos $L_{1},L_{2},\ldots$ donde $L_{n}$ es la hora de llegada del n-ésimo cliente. Sea $S_{n}$ el tiempo de servicio requerido por el $n$-ésimo cliente. Supongamos que hay un solo servidor que sirve a los clientes uno a la vez en orden de sus llegadas. Se supone también que hay una capacidad infinita en la instalación de servicio para que los clientes esperen.

\[Introducción Teoría de Colas\](https://www.youtube.com/watch?v=VPuRoEOVogo)

\[Introducción Teoría de Colas (II)\](https://www.youtube.com/watch?v=jb3_zvj0w_c)

## Indicadores de interés en teoría de colas {.scrollable}

-   $Q(t)=$ número de clientes en el sistema a tiempo $t$

-   $P(Q(t) \leq x)=$?

-   $\lim_{t \to \infty} Q(t)=$?

-   $S_{n}=$ tiempo de llegada del $n$-ésimo cliente.

-   $I_{n}=$ tiempo de salida del $n$-ésimo cliente.

-   $I_{n}-S_{n}=$ tiempo que el $n$-ésimo cliente pasa en el sistema.

-   $L_{n}=$ tiempo de servicio del $n$-ésimo cliente.

-   $E_{n}=$ tiempo de espera del $n$-ésimo cliente= Tiempo en el sistema del $n$-ésimo cliente- tiempo de servicio del $n$-ésimo cliente =

$$
E_{n}=I_{n}-S_{n}-L_{n}
$$

¿Cuáles son las características del proceso de los tiempos de espera de los clientes $\{E_{n}, n\geq 1 \}$?

## Indicadores de interés en modelos de rendimiento informático

Sea $Z(t)$ el estado del sistema en el instante $t$.

Típicamente $\{Z(t), t > 0\}$ tiene un espacio finito de estados al cual llamaremos $S=\{1,2,\ldots,N\}$.

En el estado $i\in S$, el sistema informático funciona a una velocidad $r(i)$ equivalente al número de instrucciones por segundo.

Sea $W(t)$ = trabajo total realizado hasta el tiempo $t$

$$W(t)=\int_{0}^{t} r(Z(u))du$$

## Lo que supone que no hay pérdida de trabajo cuando el sistema cambia de estado. {.scrollable}

-   Sea $B \subset \{1,\ldots,N\}$ un conjunto dado de **estados inaceptables**, es decir, que el sistema esté en un modo de operación aceptable siempre que no esté en uno de los estados en $B$.

-   Entonces, $T=min\{t > 0:Z(t)\in B\}$ representa el tiempo hasta que el sistema falla por primera vez.

-   Si $\tau$= tiempo teórico de funcionamiento del sistema, uno desearía que $P(T > \tau)$ esté tan cerca de 1 como sea posible.

-   En el contexto del establecimiento de bancos comerciales, donde $r(i)=1 \quad \forall \quad i \notin B$ y $r(i)=0 \quad \forall \quad i \in B, W(t)=$ tiempo total empleado por el sistema en estados aceptables hasta tiempo $t$.

Nos gustaría tener $\frac{W(t)}{t}$ lo más cercano a 1 como sea posible pues representa la fracción del tiempo que el sistema está en marcha.

## ¿Cómo se caracteriza un proceso estocástico?

Supongamos que casi todas las trayectorias de la muestra de $\{X(t), t \geq 0\}$ son continuas a derecha, con un número finito de saltos en un intervalo finito de tiempo. Entonces, el proceso estocástico $\{X(t), t \geq 0\}$ está completamente descrito por:

$$
\begin{align*}&F_{t_{1}, t_{2}, \ldots, t_{n}}(x_{1}, \ldots, x_{n})=\\&P\left(X(t_{1}) \leq x_{1}, X(t_{2}) \leq x_{2}, \ldots, X(t_{n}) \leq x_{n}\right) \end{align*}
$$

$\forall \quad n \geq 1 \quad 0 \leq t_1 < t_2 < \ldots < t_n$

## En el caso de procesos estocásticos monitoreados en tiempo discreto

$$
\begin{align*}&P\left(\underbrace {X_{n+1}=j}_{\text{futuro}}|\underbrace {X_n=i}_{\text{presente}}, \underbrace {X_{n-1}= i_{n-1}, \ldots, X_0=i_0}_{\text{pasado}}\right)\\&=\begin{cases} P(X_{n+1}=j)       & \text{si no hay memoria, fácil} \\\\ P(X_{n+1}=j|X_n=i) & \text{memoria limitada, manejable} \\\\\text{ninguna simplificación posible } & \text{si la memoria es infinita, muy dificil }\end{cases}\end{align*}
$$

## ¿Qué aprendimos hoy?
