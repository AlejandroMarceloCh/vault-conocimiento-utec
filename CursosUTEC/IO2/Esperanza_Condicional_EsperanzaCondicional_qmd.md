---
curso: IO2
titulo: Esperanza_Condicional__EsperanzaCondicional
slides: 0
fuente: Esperanza_Condicional__EsperanzaCondicional.qmd
---

---
title: "Esperanza Condicional"
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

-   Definir la **esperanza condicional** $E[Y|A]$ de una variable aleatoria $Y$ dado que se tiene evidencia de que un evento $A$ ha ocurrido.

-   Definir la **esperanza condicional** $E[Y|X]$ de una variable aleatoria $Y$ dada otra variable aleatoria $X$. Comprender **la diferencia entre** $E[Y|X]$ **y** $E[Y|X=x]$.

-   Relacionar la ley de probabilidad total con la **ley de esperanza total**.

-    Enunciar y aplicar **las propiedades torre de la esperanza y la varianza condicional**.

## Ejemplo: Ruteo

Una empresa necesita decidir cuál es la mejor ruta para transportar sus productos desde la ciudad $A$ donde se encuentra hasta una ciudad $B$ donde se encuentran la mayoría de sus clientes potenciales. Se conocen tres rutas principalmente diferenciadas por el medio de transporte que usan. La ruta $j$-ésima toma en promedio $\mu_{j}$ horas llevar dichos productos desde la ciudad A hasta la ciudad B y la desviación estándar del tiempo de transporte a través de la ruta $j$ viene dada por $\sigma_{j}$ para $j=1,2,3$. Si dicha empresa escoge al azar entre las tres rutas cada vez que necesita hacer un envío, **¿cuál es el valor esperado de viaje entre las ciudades** $A$ **y** $B$**?**

## Solución:

$$
\begin{align*}R_{j}& = \text{el evento: la empresa escoge la ruta} j\\T& = \text{la variable aleatoria: que representa el tiempo de viaje} \end{align*}
$$

Sabemos del enunciado que

$$E(T|R_{j})=\mu_{j} \text{ para } j=1,2,3$$

Si la empresa escoge al azar la ruta por la cual transporta sus productos de la ciudad $A$ a la ciudad $B$, podemos decir entonces que

$$P(R_{j})=\frac{1}{3} \text{ para } j=1,2,3$$

## Calculemos el tiempo medio incondicional de viaje

$$E(T)=\sum_{j=1}^{3}E(T|R_{j})P(R_{j})=\frac{1}{3}\sum_{j=1}^{3}\mu_{j}$$

Note que

$$E(T|R_{j})= \mu_{j} \text{ con probabilidad } P(R_{j})=\frac{1}{3}$$

para $j=1,2,3$.

## ¿Cuál es la varianza del tiempo de viaje entre la ciudad A y la B?

Primero recordemos que

$$Var(T)=E(T^{2})-E^{2}(T)$$

y que lo que tenemos es

$$Var(T|R_{j})=\sigma_{j}^{2}=E(T^{2}|R_{j})-E^{2}(T|R_{j})=E(T^{2}|R_{j})-\mu_{j}^{2}$$

De lo que podemos deducir que

$$E(T^{2}|R_{j})=\sigma_{j}^{2}+\mu_{j}^{2}$$

## Continuando con el cálculo de la varianza del tiempo incondicional de viaje {.scrollable}

$$
\begin{align*}E(T^{2})=&\sum_{j=1}^{3}E(T^{2}|R_{j})P(R_{j})\\        =&\frac{1}{3}\sum_{j=1}^{3}\left[\sigma_{j}^{2}+\mu_{j}^{2}\right]\\Var(T)=& E(T^{2})-E^{2}(T)\\      =& \frac{1}{3}\sum_{j=1}^{3}\left[\sigma_{j}^{2}+\mu_{j}^{2}\right]- \left[\frac{1}{3}\sum_{j=1}^{3}\mu_{j}\right]^{2}\\      =& \frac{1}{3}\sum_{j=1}^{3}\sigma_{j}^{2}+\frac{2}{9}\sum_{j=1}^{3}\mu_{j}^{2}-\frac{2}{9}\sum_{i\neq j}\mu_{i}\mu_{j}\end{align*}
$$

Lo que hemos usado de manera intuitiva en este ejemplo se conoce con el nombre de **ley de la esperanza total**. Vamos a enunciarla.

## Ley de la esperanza total {.scrollable}

Sea $A_{1}, A_{2}, \cdots A_{n}$ una partición del espacio muestral $S$ con $P(A_{i}) > 0 \quad\forall\quad i$ y sea $Y$ una variable aleatoria sobre dicho espacio muestral. Entonces,

$$E(Y)=\sum_{i=1}^{n}E(Y|A_{i})P(A_{i})$$

**Nota: la ley de probabilidad total es un caso particular de la ley de la esperanza total**

Observe que si $B$ es un evento en el espacio muestral $S$ y tomamos a la variable aleatoria $Y\sim Ber(p)$ con $p=P(B)$, entonces

$$
\begin{align*}&E(Y)=\sum_{i=1}^{n}E(Y|A_{i})P(A_{i})\\& \text{ se convierte en }\\&P(B)=\sum_{i=1}^{n}P(B|A_{i})P(A_{i})\end{align*}
$$

pues la variable aleatoria $Y|A_{i}$ se define de la siguiente manera

$$
Y|A_{i}=\begin{cases}           1 & \text{ con probabilidad } P(B|A_{i})\\           0 & \text{ con probabilidad } 1-P(B|A_{i})\\           \end{cases}
$$

**Nota:** Escogiendo a la variable aleatoria $Y$ de esta forma, **la ley de esperanza total se convierte en la ley de probabilidad total**. Luego veremos que la ley de esperanza total, es a su vez, un caso particular de la propiedad torre de la esperanza condicional.

## Ejemplo: ventas

Supongamos que clientes llegan a una tienda por departamentos siguiendo una variable aleatoria Poisson con tasa de llegada $\lambda$ clientes por hora. Cada cliente hace una compra con probabilidad $p$ independientemente de cualquier otro cliente. Se sabe además que cuando un cliente realiza una compra, la misma tiene una media de $\mu$ dólares y una desviación estándar de $\sigma$ dólares. Note que puede ser que un cliente no compre nada.

**Calcule la media y la varianza de la compra en dólares de un cliente cualquiera**

## Datos del problema:

Note que el enunciado nos proporciona la siguiente información:

$$
\begin{align*}N&= \text{ la v.a. que cuenta el número de clientes por hora }\\C&= \begin{cases}    1 & \text{ si el cliente compra }\\    0 & \text{ si el cliente no compra }    \end{cases}\\X&= \text{ la cantidad en dólares que gasta un cliente}     \end{align*}
$$

Observe que $N\sim Poisson(\lambda)$, $C\sim Ber(p)$.

## Note además quién es aleatorio y quién no

$$
\begin{align*}E(X|C)&=\begin{cases}       \mu & \text{ cuando } C=1\\       0   & \text{ cuando } C=0\\       \end{cases}\\Var(X|C)&= \begin{cases}           \sigma^{2} & \text{ cuando } C=1\\           0          & \text{ cuando } C=0\\           \end{cases}\end{align*}      
$$

Observe que $E(X|C)$ y $Var(X|C)$ son variables aleatorias.

Nos piden calcular $E(X)$ y $Var(X)$. Es decir, el valor esperado y la varianza de la compra independientemente de que el cliente realice una compra o no.

## Solución:

Claramente,

$$
\begin{align*}E(E(X|C))=&E(X|C=1)P(C=1)+E(X|C=0)P(C=0)\\    =& \mu p  + 0 (1-p) =\mu p\\Var(X)=&E(X^{2})-E^{2}(X)\\       =&E(X^{2}|C=1)P(C=1)+E(X^{2}|C=0)P(C=0)-(\mu p)^{2}\\      =& [Var(X|C=1)+E^{2}(X|C=1)]P(C=1)\\      +&[Var(X|C=0)+E^{2}(X|C=0)]P(C=0)-(\mu p)^{2}\\      =& [\sigma^{2}+\mu^{2}]p -(\mu p)^{2}= \sigma^{2}p +\mu^{2}p(1-p)\end{align*}
$$

## Continuando con el ejemplo

**Calcule el valor esperado y la varianza de las ventas realizadas en dicha tienda en un período de 8 horas.**

## Continuando con el ejemplo

Sea $V$ la variable aleatoria que modela las ventas que realiza la tienda en un período de 8 horas.

Claramente, nos piden $E(V)$ y la $Var(V)$. Observe que

$$
\begin{align*}V=&\sum_{i=1}^{N}X_{i}\\X_{i}=& \text{ el valor de la compra que realiza el cliente } i\\N=& \text{ número de clientes que entran a la tienda durante un período de 8 horas}\\N\sim& Poisson(8\lambda)\end{align*}
$$

## Realizando el cálculo

$$
\begin{align*}E(V|N=n)=& E\left(\sum_{i=1}^{N}X_{i}|N=n\right)\\        =& E\left(\sum_{i=1}^{n}X_{i}|N=n\right)\\        =& nE(X)= n\mu p\\E(V|N)  =& N\mu p\\        &\text{ por lo tanto es función de }N \text{, una variable aleatoria}\\E(V)=&E(E(V|N))= E(N\mu p)= \mu p E(N)=8p\mu\lambda         \end{align*}
$$

Esta última propiedad que aplicamos de manera intuitiva se conoce como **la propiedad torre de la esperanza condicional**. La cual enunciamos a continuación:

## Propiedades Torre 

$$
\begin{align*}& \text{ Propiedad torre de la esperanza condicional }\\\\&E(Y)=E(E(Y|X))\\\\& \text{ Propiedad torre de la varianza condicional }\\\\&Var(Y)=E(Var(Y|X))+Var(E(Y|X))\\\\\end{align*}
$$

## Demostración de la propiedad torre de la esperanza condicional

Haremos el caso en el que ambas variables aleatorias son discretas. Los otros casos son muy similares considerando las variantes del caso:

$$
\begin{align*}E(E(Y|X))=&\sum_{x\in Im(X)}E(Y|X=x)P(X=x)\\          &\text{ recordando que } E(Y|X=x)\equiv \sum_{y\in Im(Y)}yP(Y=y|X=x)\\         =& \sum_{x\in Im(X)}\sum_{y\in Im(Y)}yP(Y=y|X=x)P(X=x)\\         =& \sum_{x\in Im(X)}\sum_{y\in Im(Y)}yP(X=x,Y=y)=E(Y)\end{align*}
$$

## Demostración de la propiedad torre de la varianza condicional

$$
\begin{align*}E[Var(Y|X)]&= E[E(Y^{2}|X)-E^{2}(Y|X)]\\           & \text{ por la linealidad de la esperanza }\\           &= E[E(Y^{2}|X)]-E[E^{2}(Y|X)]\\           & \text{ por la propiedad torre aplicada a } Y^{2}\\           &= E(Y^{2})-E[E^{2}(Y|X)]\\\\Var[E(Y|X)]&= E[E^{2}(Y|X)]-E^{2}[E(Y|X)]\\           & \text{ por la propiedad torre aplicada a } Y\\           &= E[E^{2}(Y|X)] - E^{2}(Y)\\\\&E[Var(Y|X)]+ Var[E(Y|X)]=E(Y^{2})-E^{2}(Y)\equiv Var(Y)        \end{align*}
$$

## ¿Cómo calculamos la varianza de las ventas realizada por la tienda en un período de 8 horas? {.scrollable}

Por la propiedad torre de la varianza condicional aplicada al contexto de nuestro ejemplo:

$$
\begin{align*}Var(V)=& E(Var(V|N))+ Var(E(V|N))\\      =& E\left[Var\left(\sum_{i=1}^{N}X_{i}|N\right)\right]+Var(N\mu p)\\      & \text{ por independencia de las } X_{i}\\      =& E(NVar(X))+(\mu p)^{2} Var(N)\\      =& Var(X)E(N)+(\mu p)^{2} Var(N)\\      =& [\sigma^{2}p +\mu^{2}p(1-p)]E(N)+(\mu p)^{2} Var(N)\\      & \text{ como } E(N)=Var(N)=8\lambda\\      =& 8\lambda\left[\sigma^{2}p+\mu^{2}p(1-p)+(\mu p)^{2}\right]= 8\lambda p [\sigma^{2}+\mu^{2}]\end{align*}
$$

## Ejemplo: Mantenimiento de equipos {.scrollable}

El muy querido computador del profesor Renom se sabe tiene un tiempo de funcionamiento exponencial parámetro $\lambda$ hasta que falle la primera vez. Cuando eso pase, él inmediatamente lo llevará a reparar. Con probabilidad $p$, él logrará que se lo reparen con éxito. Si se lo reparan con éxito, el computador estará como nuevo otra vez y durará otro tiempo exponencial parámetro $\lambda$ independiente del tiempo que duró la primera vez sin malograrse. Este proceso se repite idénticamente igual despúes de cada avería. Sin embargo, si despúes de una avería, el profesor Renom no logra que le reparen el computador con éxito, comprará inmediatamente un computador nuevo pues todos sabemos que no puede vivir sin su computadora. Encuentre el valor esperado y la varianza del tiempo hasta que el profesor Renom tenga que comprar un computador nuevo. Asuma que los tiempos que el computador pasa en diagnóstico y reparación así como el tiempo para comprar un computador son negligibles.

## Datos del problema:

Sea $T=$ tiempo hasta que el Prof. Renom se vea obligado a comprar un computador nuevo.

$$
X_{i}=\begin{cases}       1 &\text{ si la avería $i-$ ésima del computador es atendida con éxito con probabilidad } p\\       0 &\text{si la avería no se atiende con éxito con probabilidad } 1-p      \end{cases}
$$

Sea $T_{i}=$ el tiempo que dura la computadora entre las averías $i-1$ y la $i$. Sabemos que $T_{i}\sim exp(\lambda)$ y que $T_{i}$ y $T_{j}$ son independientes para toda avería $i\neq j$.

Sea $N$ la variable aleatoria que cuenta el número de averías que sufre el computador del profesor Renom hasta que se vé obligado a comprar un computador nuevo.

## Solución: {.scrollable}

Note que

$$T=\sum_{i=1}^{N}T_{i}$$

y que

$$
\begin{align*}&E[T|N=n]=E\left[\sum_{i=1}^{n}T_{i}\right]=E\left[\sum_{i=1}^{n}exp(\lambda)\right]=\frac{n}{\lambda}\\&N\sim Geo(1-p)\\&E(T|N)=\frac{N}{\lambda}\\&\text{ por la propiedad torre de la esperanza condicional }\\&E(T)=E(E(T|N))=E\left(\frac{N}{\lambda}\right)=\frac{E(Geo(1-p))}{\lambda}=\frac{1}{\lambda(1-p)}\\\end{align*}
$$

## Examen IO2 2022-1

Una empresa llamada Ride ofrece a sus clientes una plataforma en donde se pueden solicitar taxis y por otro lado, ofrece a sus socios conductores la posibilidad de ofrecer sus servicios de courier. Para sostener la operación y retener a ambos grupos de stakeholders es necesario que haya equilibrio entre la demanda y oferta.

Por lo tanto, la empresa utiliza incentivos como descuentos y promociones para atraer pasajeros a la aplicación. Del dinero recibido por una carrera de un pasajero, la cantidad que se utiliza para pagar estos descuentos se le denomina burn.

## Pregunta 1

La variable aleatoria conjunta entre el costo de la carrera en soles de un pasajero y el burn en soles que se incurre por pasajero tiene la siguiente función de densidad conjunta:

$$
f(x,y)=\begin{cases}       Cx &\text{para } 0 \leq y\leq x \leq 30\\       0 &\text{fuera }     \end{cases}
$$

**Determine el valor de la constante C para que efectivamente** $f(x,y)$ **sea una función de densidad.**

## Solución

Para que $f(x,y)$ sea una función de densidad, debe cumplirse que:

-   $C > 0$

-   Y además, la constante $C$ debe satisfacer que:

$$
\int_0 ^{30} \int_0 ^x Cxdydx=1 
$$

Resolviendo obtenemos que $C =  \frac{1}{9000}$

## Pregunta 2

Modele la variable aleatoria condicional del burn dado el costo de la carrera.

## Solución:

Debemos calcular la función de densidad condicional del burn dado el costo de la carrera. Es decir:

$$
f(y|X=x) \equiv\begin{cases}       \frac{f(x,y)}{f_X(x)} &\text{para } 0 \leq y\leq x \leq 30\\       0 &\text{si no }     \end{cases}
$$

Donde:

$$
\begin{align*} f_X(x)&=\begin{cases}       \int_0^x Cxdy &\text{cuando } 0\leq x \leq 30\\       0 &\text{cuando no }     \end{cases} \\
& = \begin{cases}        Cx^2 &\text{cuando } 0\leq x \leq 30\\       0 &\text{cuando no }     \end{cases}
\end{align*}
$$

## Continuando con la solución

$$
\begin{align*}
f(y|X=x) &\equiv\begin{cases}       \frac{f(x,y)}{f_X(x)} &\text{para } 0 \leq y\leq x \leq 30\\       0 &\text{si no }     \end{cases} \\
&= \begin{cases}       \frac{Cx}{Cx^2} &\text{para } 0 \leq y\leq x \leq 30\\       0 &\text{si no }     \end{cases} \\
&= \begin{cases}       \frac{1}{x} &\text{para } 0 \leq y\leq x \leq 30\\       0 &\text{si no }     \end{cases} \\
\end{align*}
$$

## Pregunta 3

Calcule el valor esperado del burn utilizando la propiedad torre de la esperanza condicional.

## Solución

Usando la propiedad torre de la esperanza condicional:

$$
E(Y) = E(E(Y|X))
$$

Comencemos por $E(Y|X=x)$

$$
\begin{align*}  E(Y|X=x) &\equiv \int_0^x yf(y|X=x)dy \\ &= \int_0 ^x y \frac{1}{x}dy \forall x \neq 0 \\
&= \frac{x}{2} \forall x \neq 0 \\
&\text{justo el punto medio del intervalo de la uniforme :)} \end{align*} 
$$

## Continuando con la solución:

$$
\begin{align*} E(Y|X) &\equiv E(Y|X=x)_{|x=X} = \frac{X}{2}\\ & \text{finalmente la esperanza deseada viene dada por:} \end{align*}
$$

$$
\begin{align*}
E(Y) &= E(E(Y|X)) = E(\frac{X}{2}) = \frac{E(X)}{2} \\ &= \frac{1}{2} \int_0^{30}xCx^2dx = 11.25 \text{ soles}    \end{align*}
$$

Si usted no sabía la propiedad torre de la esperanza condicional, el valor esperado de $Y$ podría haberlo calculado utilizando la densidad marginal del burn.

## Pregunta 4

Calcule el valor esperado de la ganancia por carrera.

## Solución

Observe que si llamamos $G \equiv X-Y$ la ganancia por carrera, el valor esperado requerido puede calcularse utilizando el hecho de que la esperanza es un operador lineal.

$$
\begin{align*} E(G) & = E(X - Y) = E(X)- E(Y)\\
&=E(X) - \frac{E(X)}{2} =\frac{E(X)}{2} = 11.25 \text{ soles} \end{align*}
$$

## ¿Qué aprendimos hoy?
