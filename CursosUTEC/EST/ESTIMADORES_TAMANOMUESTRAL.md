---
curso: EST
titulo: ESTIMADORES-TAMAÑOMUESTRAL
slides: 1754
fuente: ESTIMADORES-TAMAÑOMUESTRAL.qmd
---

# ESTIMADORES-TAMAÑOMUESTRAL

## Índice

Material Quarto/R del curso (código + prosa). Ingesta directa sin transcripción (ya es markdown).

```{r}
library(readr)
library(plyr)
library(dplyr)
library(tidyr)
library(tidyverse)
```

## Quarto DOCUMENT

Quarto enables you to weave together content and executable code into a finished document. To learn more about Quarto see <https://quarto.org>.

# CARACTERISTICAS DE UNA BUENA MUESTRA

Una muestra es un subconjunto obtenido a partir de la población de interés.

Para que la muestra sea buena debe cumplir las condiciones siguientes:

-   Debe ser aleatoria ( al azar)

-   Debe ser representativa ( un poco de todo)

-   Debe tener el tamaño adecuado ( mediante algunos códigos)

**PROPIEDAD FUNDAMENTAL DE UNA BUENA MUESTRA ALEATORIA:**

Si *X1, X2, X3, ..., Xn* es una buena muestra aleatoria de tamaño n, extraida de una población *X,* entonces debe cumplir lo siguiente:

$$
E(X1)=E(X2)=E(X3)=...=E(Xn)= E(X)=\mu \text{(media poblacional)}
$$

$$
V(X1)=V(X2)=V(X3)=...=V(Xn)=V(X)= \sigma^2 \text{(varianza poblacional)}
$$

$$
f(X1)=f(X2)=f(X3)=...=f(xn)=f(X) \text{  (igual densidad)}
$$

**PROPIEDAD DE LA ESPERANZA Y LA VARIANZA**

si $X,Y,Z$ son parte de una muestra, entonces:

-   $$
    E(aX+bY-cZ+d)=aE(X)+bE(Y)-cE(Z)+d
    $$

-   $$
    V(aX+bY-cZ+d)=a^2 V(X)+b^2 V(Y)+c^2 V(Z)
    $$

## La media muestral ( para variables cuantitativas)

Dada una muestra de variables aleatorias i.i.d. (independientes e igualmente distribuidas) $X_{1}, X_{2}, \cdots, X_{n}$, recordemos que la **media muestral** $\overline{X}(n)$ se define por:

$$
\overline{X}(n)\equiv\frac{1}{n}\sum_{i=1}^{n}X_{i}
$$

**La ley de los grandes números** y el **Teorema Central del Límite** sirven para estudiar cómo se comporta la media muestral cuando el tamaño de la muestra $n$ es "grande".

## Valor esperado de la media muestral

En efecto, $\overline{X}(n)$ es función de la muestra $X_{1}, X_{2}, \cdots, X_{n}$ con $E(X_{i})=\mu$ y $Var(X_{i})=\sigma^{2}$ para todo $I=1,2,\cdots, n$ y como tal es una variable aleatoria en sí misma. Por lo tanto, podemos calcular, su **media**:

$$
\begin{align*}
E\left(\overline{X}(n)\right)=& E\left(\frac{1}{n}\sum_{i=1}^{n}X_{i}\right)\\
                        =& \frac{1}{n}\sum_{i=1}^{n} E(X_{i})\\
                        & \text{ como las } X_{i} \text{ son i.d.}\\
                        =& \frac{1}{n}\sum_{i=1}^{n} E(X)=\mu
\end{align*}
$$

## Varianza de la media muestral

En efecto, $\overline{X}(n)$ es función de la muestra $X_{1}, X_{2}, \cdots, X_{n}$ con $E(X_{i})=\mu$ y $Var(X_{i})=\sigma^{2} < \infty$ para todo $i=1,2,\cdots, n$ y como tal es una variable aleatoria en sí misma. Por lo tanto, podemos calcular, su **varianza**:

$$
\begin{align*}
Var\left(\overline{X}(n)\right)=& Var\left(\frac{1}{n}\sum_{i=1}^{n}X_{i}\right)\\
                        =& \frac{1}{n^{2}}\sum_{i=1}^{n} Var(X_{i})\\
                        & \text{ pues las } X_{i} \text{ son i.i.d}\\
                        =& \frac{1}{n^{2}}\sum_{i=1}^{n} Var(X)=\frac{\sigma^{2}}{n}
\end{align*}
$$

## Ley fuerte de los grandes números

**Teorema:**

Dada una muestra de variables aleatorias i.i.d.

$$
\begin{align*}
& X_{1}, X_{2}, \cdots, X_{n} \text{ con } E(X_{i})=\mu \text{ y } Var(X_{i})=\sigma^{2} < \infty \forall i=1,2,\cdots, n\\\\
&\text{entonces}\\\\
&\overline{X}(n)\rightarrow \mu \text{ cuando } n\rightarrow \infty \text{ con probabilidad }1
\end{align*}
$$

## Método de Monte Carlo para estimar pi

**Un ejemplo famoso del Método de integración por Monte Carlo es el de estimar** $\pi$. Consiste en considerar el círculo unitario $\{(x,y): x^{2}+y^{2}\leq 1\}$ inscrito en el cuadrado $[-1,1]\times[-1,1]$ de área $4$

```{r, echo=FALSE}
library(plotrix)
# Generando una uniforme bivariada en el cuadrado [-1,1]x[-1,1]
nsim <- 10000
x <- runif(nsim, -1,1)
x
y <- runif(nsim, -1,1)
y
plot(x,y, xlim=c(-1,1), ylim=c(-1,1),pch=20, col = ifelse(x^2+y^2<1,"red", "darkgreen") , asp=1)
draw.circle(0,0,1, border = "black", lwd = 2)

```

## Error al estimar pi

```{r, echo=FALSE}
nsim <- 1000



# Generando una uniforme bivariada en el cuadrado $[-1,1]\times[-1,1]$
x <- runif(nsim, -1,1)
y <- runif(nsim, -1,1)
# La proporción de puntos que caen dentro del círculo de área $\pi/4$
p <- 4*cumsum(x^2+y^2<1)/(1:nsim)
p
error <- abs(p-pi)
plot(1:nsim, error ,ylim=c(-3,3), pch="*", main="Error al estimar pi", xlab="tamaño de la muestra n", ylab="Error en función de n")
abline(h=0, col="red")

```

## Teorema  del límite Central (TLC).

## Dada una muestra de variables aleatorias i.i.d.

$$
\begin{align*}
& X_{1}, X_{2}, \cdots, X_{n} \text{ con } E(X_{i})=\mu \text{ y } Var(X_{i})=\sigma^{2} < \infty \forall i=1,2,\cdots, n\\\\
&\text{entonces}\\\\
&\left(\frac{\overline{X}(n)-\mu}{\frac{\sigma}{\sqrt{n}}}\right)\rightarrow Nor(0,1) \text{ en distribución cuando } n\rightarrow \infty
\end{align*}
$$

Es decir , cuando la muestra es grande (mayor de 30):

$$
\overline{X} \rightarrow N(\mu, \frac{\sigma}{\sqrt{n}})
$$

la población puede tener cualquier distribución, pero si la muestra es grande , entonces la media muestral se aproxima a una normal.

Conclusión: cuando la muestra es grande, entonces $\overline{x}$ tendrá distribución normal y en R studio se ingresara para calcular sus probabilidades: $\mu$ y $\frac{\sigma}{\sqrt{n}}$

Siendo: $\mu$ la media de la población y $\sigma$ la desviación de la población.

Recordar los casos especiales:

-   Si La población es Normal $(\mu, \sigma)$ y se conoce $\sigma$ entonces $\overline{x}$ será también normal (sin importar el tamaño de n):

$$
E(\overline{x})=\mu\\
Desviación(\overline{x})= \frac{\sigma}{\sqrt{n}}
$$

-   Si la población es Normal $(\mu, \sigma)$ y no se conoce $\sigma$ entonces $\overline{x}$ será considerada como T-student:

$$  \frac{\overline{x}-\mu}{\frac{s}{\sqrt{n}}}= T(n-1) $$

s: desviación de la muestra.

**LA PROPORCIÓN MUESTRAL (p):**

consideramos: $n$ tamaño de muestra y $\pi$ la proporción poblacional.

Si $p$ es la proporción muestral:

$$
p \rightarrow N(\pi, \sqrt{\frac{\pi*(1-\pi) }{n}})\\
\text{Su forma estandarizada será:}\\
\frac{p-\pi}{\sqrt{\frac{\pi*(1-\pi) }{n}}}=Z
$$

Para el caso de dos proporciones:

$$
p1-p2 \rightarrow N(\pi 1 - \pi 2, \sqrt{\frac{\pi 1*(1-\pi 1) }{n1}+\frac{\pi 2*(1-\pi 2) }{n2}})
$$

EJEMPLO 1:

```{r}
#De 120 alumnos se ha encontrado que 100 han aprobado el curso.
#Se seleccionará una muestra de tamaño 20 alumnos. 
#a) ¿Cuál es la probabilidad de que el porcentaje de aprobados en la muestra sea por lo menos del 75%?
#b) Calcule la probabilidad de que, en los alumnos muestreados, se tenga a lo más 3 desaprobados.

```

Solución:

Poblacion: 120 alumnos ==\> 100 aprobaron. ==\>Proporcion de aprobados : $\pi = 100/120 = 0.8333$

muestra: n= 20

¿P(p\>=0.75)?

$$
p \rightarrow N(\pi, \sqrt{\frac{\pi*(1-\pi) }{n}})\\
$$

media de p: $E(p)=\pi=0.8333$

desviación de p: $\sqrt{V(p)}=\sqrt{0.8333*0.1667/20}=0.08333$
Ahora calculamos ya, la probabilidad:

```{r}
pnorm(0.75, 0.8333, 0.08333,lower.tail =F )
```

Respuesta: 0.8413.

b\) P(en la muestra \<= 3 desaprobados)=P(X\<=3)... siendo X: \# de desaprobados en la muestra.

$$
P(x\le 3)=P(\frac{x}{n} \le \frac{3}{n})=P(p_{desap.}\le 0.15)
$$

$$
media=\pi_{desap}=0.1667\\
desv=\sqrt{0.1667*0.8333/20}=0.08333
$$

y se calcula la probabilidad:

```{r}
pnorm(0.15, 0.1667, 0.08333)
```

Respuesta: 0.42.

## calculando el tamaño de la muestra requerido para medias muestrales

**Supongamos que queremos estimar el valor esperado** $\mu$ de una variable aleatoria $X$ con varianza finita desconocida $\sigma^{2}$ de tal manera de que **estemos seguros con un** $99\%$ **de confianza** que la media muestral esté a menos de $0.1$ de la verdadera media poblacional $\mu$. Después de una encuesta piloto de tamaño $n=10$, hemos estimado que $S=6$, la desviación estándar muestral, que servira como una aproximacion a $\sigma$ . Calcule un tamaño de muestra apropiado.

## Solución

De la ley fuerte de los grandes números sabemos que $\overline{X}_{n}$ es un buen estimador para $\mu$

Además, sabemos que $$
E\left(\overline{X}_{n}\right)=\mu
$$ y $$
Var\left(\overline{X}_{n}\right)=\frac{\sigma^{2}}{n}
$$

## Formulemos lo que queremos asegurar

$$
\begin{align*}
& P\left(|\overline{X}_{n}-\mu| < 0.1\right)\geq 0.99\\
& P\left(\left|\frac{\overline{X}_{n}-\mu}{\frac{\sigma}{\sqrt{n}}}\right| < \frac{0.1}{\frac{\sigma}{\sqrt{n}}}\right)\geq 0.99\\
& \text{la varianza no es conocida, la estimamos }\\
& P\left(\left|\frac{\overline{X}_{n}-\mu}{\frac{6}{\sqrt{n}}}\right| < \frac{0.1}{\frac{6}{\sqrt{n}}}\right)\geq 0.99\\
& \text{por el Teorema Central del Límite }\\
& P\left(\left|\frac{\overline{X}_{n}-\mu}{\frac{6}{\sqrt{n}}}\right| < \frac{0.1}{\frac{6}{\sqrt{n}}}\right)\rightarrow \\
\end{align*}
$$

## Encontremos el tamaño de muestra mínimo que haga el trabajo {.scrollable}

$$
P(|Z|<\frac{0.1*\sqrt{n}}{6})=0.99
$$

$$
P(-\frac{0.1*\sqrt{n}}{6}<Z<\frac{0.1*\sqrt{n}}{6})=0.99
$$

luego de graficar la curva de normal estandar y graficar el intervalo, se tiene la siguiente propiedad:

$$
P(-a<Z<a)=2P(Z<a)-1
$$

usando simetría, se llega a tener:

$$
P(Z<\frac{0.1*\sqrt{n}}{6})=0.995
$$

```{r}
qnorm(0.995,0, 1)
```

$$
\frac{0.1*\sqrt{n}}{6}=2.575829 \rightarrow  n=23885.622
$$

El tamaño de muestra para que se cumpla todo lo mencionado debe ser 23886.

**CÓDIGO PARA CALCULAR TAMAÑO DE MUESTRA PARA VARIABLE CUANTITATIVA:**

```{r echo=TRUE}
Tamaño_muestra_media<-function (ds, nc, t){return ((qnorm((1+nc)/2)*ds/t)^2)}

desv.est=6#desviación estándar  (dato)
nc=0.96#nivel de confianza 

t=0.7 #tolerancia

Tamaño_muestra_media(desv.est,nc,t)
```

**PARA EL PROYECTO:**

*Todos usar confianza de 96%*

*Sigma se va calculando para cada columna numérica.*

*Lo único que puedes ir modificando es la Tolerancia ( mide el error)*

*La muestra debe salir para cad a columna entre 250 y 450.*

*Y de todos los n hallados , se escogera el mayor n.*

## Reflexionemos un rato

```{r,echo=FALSE}
T <- seq(from=0.01, to=1, by=0.01)
n <- ((6*qnorm(0.01, lower.tail = FALSE))/T)^2
plot(T,n, log = "y", type = "l", col = "red", ylim = c(100, 10^6), xlab = "Tolerancia", ylab = "Tamaño de muestra")
n <- ((6*qnorm(0.05, lower.tail = FALSE))/T)^2
lines(T,n, log = "y", type = "l", col = "blue")
legend("topright", legend = c(0.01, 0.05), lty = 1, col = c("red", "blue"))
title("Tamaño de muestra en función de la tolerancia\n para distintas significancias.")
```

## Para el cálculo del tamaño de la muestra para estimar la media de una variable

Para cada variable del proyecto necesitaremos decidir:

**¿cuál es el número mínimo de observaciones que tenemos que recoger para estimar su valor esperado?**

-   Necesitamos estimar la **desviación estándar** de la variable con un pre-muestreo.

-   Necesitamos decidir una tolerancia $T$

-   Necesitamos un nivel de confianza $1-\alpha$ o una significancia $\alpha$. Se fija y luego no cambiarla.

-   Usar el código anterior

Para cada variable numérica se halla el tamaño de muestra (ni) necesario, luego:

$$
n=\max_{1\leq i\leq M} n_{i}
$$

## Caso: Atención al cliente

Los tiempos de servicio para los clientes que pasan por un caja en una tienda de venta al menudeo son variables aleatorias independientes con media de $1.5$ minutos y desviación estándar de $1 min$. Calcule la probabilidad de que 100 clientes seleccionados al azar, puedan ser atendidos en menos de 2 horas de tiempo total de servicio.

## Solución: 

n=100 (muestra)

T: Tiempo de atención en caja a cada cliente.

Sea $T_{i}$ el tiempo de atención del $i$-ésimo cliente. Nos piden calcular:

$$
P(T1+T2+T3+...+T100 < 120)
$$

$$
\begin{align*}P\left(\sum_{i=1}^{100}T_{i}\leq 120\right)=&P\left(\frac{1}{100}\sum_{i=1}^{100}T_{i}\leq \frac{120}{100}\right)\\          =&P\left(\overline{T}(100)\leq \frac{6}{5}\right)\\          =&0.001349898\end{align*}
$$

Como aqui n es mas de 30 , entonces se puede usar TLC:

$$
\overline{T} \rightarrow N(\mu, \sigma / \sqrt{n})
$$

Aqui ya se tiene:

$\mu=1.5 min$ y $\sigma= 1 min$

```{r}
pnorm(1.2, 1.5, 1/10) 
```

En donde, $Z\sim N(0,1)$

## Ejercicio: Muestreo de vehículos de segunda

Una empresa dedicada a la venta de autos de segunda, tiene en su base de datos, las variables

$$
X: \text{Kilometraje del vehículo}
$$

$$
Y: \text{Antiguedad en años del vehículo.}
$$

Tomando muestras piloto de tamaño 10, han hallado que las desviaciones estándar de las variables X , Y son respectivamente: 50km y 3 años.

Si la tolerancia que han decidido es de 10km y 0.5 años, halle el tamaño de muestra necesario, con un nivel de confianza 96%.

SOLUCIÓN:

Cuando se toma muestras piloto (muestra pequeña), el objetivo es hallar un estimador (valor que se aproxime al verdadero valor de la población), que luego se podrá usar como un parámetro.

Aqui se ha calculado S (desviación muestral) , este valor se usará como $\sigma$.

Para X (kilometraje)

```{r}
Tamaño_muestra_media<-function (ds, nc, t){return ((qnorm((1+nc)/2)*ds/t)^2)}

nc=0.96 #nivel de confianza
desv.est=50 #desviación estándar
t=10 #tolerancia

Tamaño_muestra_media(desv.est,nc,t)
```

**n siempre se redondea al mayor. n=106 (para kilometraje)**

Para Antiguedad:

```{r}
Tamaño_muestra_media<-function (ds, nc, t){return ((qnorm((1+nc)/2)*ds/t)^2)}

nc=0.96 #nivel de confianza
desv.est=3 #desviación estándar
t=0.5 #tolerancia

Tamaño_muestra_media(desv.est,nc,t)
```

Para la variable Antiguedad conviene tomar 152 como tamaño de muestra.

Luego , para todo el problema se debe tomar ***el máximo de los dos tamaños:*** 152.

No olvidar que para el proyecto, se usa confianza 96% y de cada columna numerica se halla la desviación estandar con R y lo único que tu puede ir cambiando es la **Tolerancia.** Los otros dos valores son fijos.

El tamaño de muestra que debe quedar es entre 250 y 450.

**Para los que hacen encuesta o experimento** basta con que obtengan una data limpia de 500 o mas y de ahi usando el código pueden obtener un tamño de muestra que pase de 200.

## Tamaño muestral requerido para proporciones muestrales, (proviene de variables cualitativas)

Si la variable es cualitativa, por lo general una proporción (p) resulta ser conveniente para realizar alguna estimación.

El tamaño de muestra necesario se calcula a partir de la fórmula:

$$
n=(\frac{Z_{(\frac{1+\gamma}{2})}}{t})^2 *p_{o}(1-p_{o})
$$

siendo:

$$
p_{o} \text{  una proporción estimada del correspondiente parámetro}
$$

t: Tolerancia

Generalmente $p_{o}$ se halla de una muestra piloto o ya se tiene como información de algún estudio anterior.

En el caso en que no se conozca el valor de $p_{o}$ y no se ha podido tomar la muestra piloto, se puede considerar que $p_{o}=0.5$

**CÓDIGO PARA EL TAMAÑO MUESTRAL EN CASOS DE PROPORCIONES**:

```{r}
Tamaño_muestral_proporciones<-function (po, nc, t){return (po*(1-po)*((qnorm((1+nc)/2) /t)^2) )}

po=3/8 #Proporcion poblacional o proporcion estimada
nc=0.96#nivel de confianza (dato)
t=0.060 #tolerancia ( en proporciones la tolerancia no pasa de 1)

Tamaño_muestral_proporciones(po,nc,t)
```

**Continuación del Ejemplo anterior:** La misma empresa que vende autos de segunda tiene en su base de datos que de cada 20 vehículos que venden, 12 son Toyotas. Con una tolerancia de 0.08 y considerando ademas, las dos variables anteriores (kilometraje y antiguedad) ¿Cuál sería ahora, el tamaño de muestra mas adecuado para la data.?

```{r}
Tamaño_muestral<-function (po, nc, t){return (po*(1-po)*((qnorm((1+nc)/2)/t)^2) )}

po=12/20 #proporción de toyotas vendidos
nc=0.96 #nivel de confianza
t=0.08 #tolerancia

Tamaño_muestral(po,nc,t)
```

Se toma aqui una muestra de 159.

Pero para toda la data debe tomarse el mayor de: 106 , 153, 159==\> El tamaño para toda la data será del mayor de todos: 159.

**Observaciones:**

El nivel de confianza en todo un proyecto es 96%.

La desviación estandar se puede calcular para cada columna numérica.

la proporcion para las cualitativas se halla usando table.

Lo único que puedes ir cambiando es **la Tolerancia.**

A menor tolerancia, n aumenta.

A mayor tolerancia, n disminuye.

A mas confianza, n aumenta.

A menor confianza, n disminuye.

**CASO: Comparación de dos proporciones**

```{r}
#Se desea comparar las ventas de autos en un mes, entre las marcas Toyota y Nissan.
#En el mes de Febrero, los de Toyota  vendieron de sus 80 autos que disponían, la cantidad de 64 vehículos, mientras que en Nissan de los 90 que tenían disponible en dicho mes, se vendió  54. 
#¿cuál es la probabilidad de que, al tomar de sus respectivas bases de datos, muestras de 40 y 30 vehículos respectivamente,  se obtenga que el porcentaje de autos que fueron vendidos de Toyota supere al de Nissan en al menos un 5%?

```

**SOLUCIÓN:**

X: cantidad de autos vendidos, para cada marca

Toyota: N=80, X=64 ==\> $\pi= 64/80=0.8$ , n=40

Nissan: N=90, X= 54 ==\> $\pi=54/90=0.60$ , n= 30

Se pide: $P(p_T -p_N \ge 0.05)$

Para el caso de dos proporciones:

p1: proporción de Toyotas y p2: proporcion de Nissan.

$$ p1-p2 \rightarrow N(\pi 1 - \pi 2, \sqrt{\frac{\pi 1*(1-\pi 1) }{n1}+\frac{\pi 2*(1-\pi 2) }{n2}}) $$

Para usar la Normal con R, necesito lo siguiente:

$$
\pi_1 - \pi_2=0.8- 0.6= 0.2\\
Desviación= \sqrt{\frac{0.8*(0.20) }{40}+\frac{0.60*(0.40) }{30}}=0.1095
$$

```{r}
DE<- sqrt(0.8*(0.20) /40+ 0.60*(0.40)/30)
DE
```

Calculamos ya, la probabilidad pedida:

```{r}
pnorm(0.05, 0.20, 0.1095,lower.tail=F)
```

Respuesta: aproximado 0.915

# INTERVALOS DE CONFIANZA

El objetivo es hallar un intervalo donde esté ubicado el valor real de un parámetro (poblacional)

$$
A<\theta<B 
$$

con un nivel de confianza $\gamma \text{.100%}$ donde $\gamma$ es un número menor que 1 pero aproximado a 1:

0.90, 0.95, 0.96, 0.98, 0.99, etc.

**Significado de 95% de confianza:** " De 100 muestras distintas de un mismo tamaño n que se tome , 95 de ellas van a producir un intervalo para el parámetro que sea el que se menciona (de A a B) o mas pequeño.

Además el nivel de significación es $\alpha$ , siendo $\alpha + \gamma =1.$

$$
\gamma:  \text{nivel de confianza. Cerca de 1}\\
\alpha: \text{nivel de significación. Cerca de cero}
$$

Luego:

$$
P(A<\theta<B)=\gamma= 1- \alpha
$$

El error máximo (tolerancia) que se genera con dicho intervalo está dado por:

$$
E_{máx}=\frac{B-A}{2}
$$

Tener en cuenta que ahora los datos que se tienen **son de la muestra**, para luego estimar los correspondientes valores de la población.

Para variables cuantitativas se usa la media y la varianza.

Para cualitativas se usa la proporción muestral.

# INTERVALO DE CONFIANZA DE LA MEDIA

Objetivo: hallar un intervalo para $\mu=\text{media poblacional}$ a partir de datos muestrales.

## Caso 1: Cuando $\sigma$ es conocido

Hallamos un intervalo para $\mu$ *cuando* $\sigma$ *conocido* ==\> Se asume aquí que la población que la población tiene distribución normal:

$$
\begin{align*}
&\text{Fórmula a usar:}\\
&\overline{X}- z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}\leq \mu\leq \overline{X}+ z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}\\
&\text{Teniendo en cuenta que:}\\
&\text{Z crítico}=Z_{1-\frac{\alpha}{2}}=Z_{0}\\
&\text{tal que:  } P(Z< Z_{0})=1-\frac{\alpha}{2}\\
&\text{el cual se calcula usando Rstudio: ?  }qnorm(1-\frac{\alpha}{2}, 0,1)\\
\end{align*}
$$

**NOTA:**

$$
\overline{X} \text{  es la media muestral}
$$

**ERROR ESTANDAR:**

$$
\frac{\sigma}{\sqrt{n}}
$$

**MARGEN DE ERROR o ERROR MÁXIMO o Tolerancia**

$$
E=Z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}
$$

### PROBLEMA 1:

Se ha tomado una muestra de 40 cubos de concreto sometidos a fuerzas de compresión y se obtuvo como resultado una *media muestral de* $60.14$ y desviación estándar poblacional de $5.02$ $N/mm^{2}$, respectivamente. También, se determinó a través de pruebas de bondad de ajuste que podemos asumir que las fuerzas de compresión se distribuyen normalmente. Calcule el intervalo de confianza del 95% para la fuerza media de compresión del concreto.

Solución:

$$
\begin{align*}
&Datos:\\
&\text{Tamaño de muestra: }n=40\\
&\text{Media muestral :  } \overline{X}=60.14\\
&\text{Desviación poblacional :  } \sigma= 5.02\\
&\text{Nivel de confianza :  } \gamma=0.95\\
&\text{significancia:  } \alpha=0.05 \rightarrow \frac{\alpha}{2}=0.025 
\end{align*}
$$

$$
\begin{align*}
&\text{Fórmula:}\\
&\overline{X}- z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}\leq \mu\leq \overline{X}+ z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}\\
&\text{Reemplazando valores:}\\
&60.14- z_{1-0.025}\frac{5.02}{\sqrt{40}}\leq \mu\leq 60.14+ z_{1-0.025}\frac{5.02}{\sqrt{40}}\\
\end{align*}
$$

Calculando ***Z(0.975)=Zo ==\>** P(Z\<Zo)=0.975*

```{r}
qnorm(0.975,0,1)
```

Cuando se tenga: **Z(0.975)= 1.96**

$$
\begin{align*}
&IC(\mu)= \left(60.14- 1.96\frac{5.02}{\sqrt{40}}, 60.14+ 1.96\frac{5.02}{\sqrt{40}}\right)\\
&\text{usando calculadora:}\\
&IC(\mu)=\left(58.58, 61.70\right)\\
\end{align*}
$$

Con 95% de confianza se espera que la compresión promedio de los cubos de concreto, este comprendido entre 58.58 y 61.70 N/mm\^2.

&&&&&&&&&&&&&&&

hASTA AQUI EN VIERNES

&&&&&&&&&&&&&&&

```{r}
DF<-read_csv("FAMOSOS2.XLSX - Hoja1 (3).csv")
DF
```

```{r}
# para cuantitativos:
mean(DF$Edad, na.rm=TRUE)  # la media
sd(DF$Edad, na.rm=TRUE)    # desviación estandar
#para cualitativos:
table(DF$Género, useNA="always")
```

Edad promedio de cantantes

```{r}
Canto<-filter(DF, Actividad=="Canto")
Canto
```

## Código para el IC de la media con sigma conocido:

Se hará todos los cálculos en R.

**1) Aquí se ingresa los datos:**

-   Si tenemos un data frame con los n datos muestrales de una variable:

```{r}
#  Se debe calcular n y la media muestral. Además la desviación poblacional debe ser dato o debe calcularse desde la población.

n <- length(DF$Edad) 
media_muestral <- mean(DF$Edad,na.rm=TRUE )
sigma_conocida <- 5 #lo asumo como que la desviacion es 5 años

print(paste("el tamaño de muestra es:", n))
print(paste("la media muestral es:",media_muestral))
print(paste("la desviación a usar es:", sigma_conocida))

```

Si tenemos los datos ya resumidos:

```{r}

n<-40  
media_muestral <-60.14
sigma_conocida <- 5.02

print(paste("el tamaño de muestra es:", n))
print(paste("la media muestral es:",media_muestral))
print(paste("la desviación a usar es:", sigma_conocida))
```

## 2) Aquí aparecerá el I.C. de la media con sigma conocido

```{r echo=TRUE}
# Calcule el error estándar 
error_estandar <- sigma_conocida/sqrt(n) 
alpha = 0.05  # ünico dato que el alumno escribe  aqui.
z_crítico <- qnorm(1-alpha/2,0,1) 
margen_de_error <- z_crítico* error_estandar  
# Los extremos del intervalo de confianza de la media serán:
extremo_inferior <- media_muestral - margen_de_error
extremo_superior <- media_muestral + margen_de_error 
# Imprimir resultados:

print(paste("Nivel de significación:",alpha))
print(paste("Error estándar:", error_estandar))
print(paste("Z crítico:", z_crítico))
print(paste("margen de error o Tolerancia:", margen_de_error))
print(paste("IC: (",extremo_inferior,";", extremo_superior,")"))


```

Con 95% de confianza se espera que la compresión promedio de los bloques esté entre 58.58 y 61.68 N/mm\^2.

El error máximo que se está generando con el IC es 1.55569 N/mm\^2.

&&&&&&&&&&&&&&&&&&&&&&&&&&&

&&&&&&&&&&&&&&&

## Caso 2: Cuando $\sigma$ no se conoce ( S debe ser conocido)

Hallamos un intervalo para $\mu$ cuando $\sigma$ desconocido ==\> Se conoce ***S(n)*** (desviación de la muestra de tamaño n) y se usará aquí la distribución **T(n-1)**:

$$
\begin{align*}
&\text{Fórmula a usar:}\\
&\overline{X}(n)- T_{(n-1,1-\frac{\alpha}{2})}\frac{S(n)}{\sqrt{n}}\leq \mu\leq \overline{X}(n)+ T_{(n-1,1-\frac{\alpha}{2})}\frac{S(n)}{\sqrt{n}}\\&\text{Teniendo en cuenta que:}\\
&\text{T crítico}=T_{(n-1, 1-\frac{\alpha}{2})}=T_{0}\\
&\text{tal que:  } P(T(n-1)< T_{0})=1-\frac{\alpha}{2}\\
&\text{el cual se calcula usando Rstudio: ?  }qt(1-\frac{\alpha}{2}, n-1)\\
\end{align*}
$$

#### PROBLEMA 2:

Se ha tomado una muestra de 40 cubos de concreto sometidos a fuerzas de compresión y se obtuvo como resultado **una media** y **desviación estándar muestral** de $60.14$ y $5.02$ $N/mm^{2}$, respectivamente. También, se determinó a través de pruebas de bondad de ajuste que podemos asumir que las fuerzas de compresión se distribuyen normalmente. Calcule el intervalo de confianza del 95% para la fuerza media de compresión del concreto.

**Solución:**

$$
\begin{align*}
&Datos:\\
&\text{Tamaño de muestra: }n=40\\
&\text{Media muestral :  } \overline{X}=60.14\\
&\text{Desviación muestral :  } S= 5.02\\
&\text{Nivel de confianza :  } \gamma=0.95\\
&\text{significancia:  } \alpha=0.05 \rightarrow \frac{\alpha}{2}=0.025 
\end{align*}
$$

$$ \begin{align*}
 &\text{Fórmula:}\\
 &\overline{X}- T_{(n-1, 1-\frac{\alpha}{2})}\frac{S}{\sqrt{n}}\leq \mu\leq \overline{X}+ T_{(n-1,1-\frac{\alpha}{2})}\frac{S}{\sqrt{n}}\\ 
&\text{Reemplazando valores:}\\
 &60.14- T_{(39,0.975)}\frac{S}{\sqrt{n}}\leq \mu\leq 60.14+ T_{(39,0.975}\frac{S}{\sqrt{n}}\\ \end{align*} $$

Calculando el T crítico: P(T(39)\< To) = 0.975

```{r}
qt(0.975,39)
```

$$ \begin{align*} &IC(\mu)= \left(60.14- 2.022691.\frac{5.02}{\sqrt{40}}, 60.14+ 2.022691.\frac{5.02}{\sqrt{40}}\right)\\ &IC(\mu)=\left(58.5345, 61.7455\right)\\ \end{align*} $$

Con 95% de confianza se espera que la fuerz promedio de compresión de los bloques de concreto, está entre 58.5345 y 61.7455 kg/mm\^2.

## Código para el IC de la media con sigma desconocido:

1\) Ingresando datos

Si se tiene un Data Frame:

```{r}
#  Se debe calcular n , la media muestral  y la desviación muestral 

n <- length(DF$Edad) 
media_muestral <- mean(DF$Edad, na.rm=TRUE)
sd_estimada  <- sd(DF$Edad, na.rm=TRUE)

print(paste("el tamaño de muestra es:", n))
print(paste("la media muestral es:",media_muestral))
print(paste("la desviación estimada es:", sd_estimada))

```

Si se tienen los datos resumidos

```{r echo=TRUE}



#n<- 20
#media_muestral <-6
#sd_estimada <- 3


print(paste("el tamaño de muestra es:", n))
print(paste("la media muestral es:",media_muestral))
print(paste("la desviación estimada es:", sd_estimada))
```

## 2) Aquí el IC de $\mu$ con sigma desconocido.

```{r echo=TRUE}
# Calcule el error estándar
error_estandar <- sd_estimada / sqrt(n)
alpha = 0.05 # único dato que el estudiante llena aquí
grados_de_libertad = n - 1 
T_crítico = qt(1-alpha/2,grados_de_libertad)
margen_de_error <- T_crítico* error_estandar 
# Calcular los extremos del intervalo de confianza 
extremo_inferior <- media_muestral - margen_de_error 
extremo_superior <- media_muestral + margen_de_error  
# Imprimir resultados: 
print(paste("significación:",alpha))
print(paste("grados de libertad de T: ",n-1))
print(paste("T crítico:", T_crítico))
print(paste("Error estándar:", error_estandar))
print(paste("margen de error:", margen_de_error))

print(paste("IC: (",extremo_inferior,";", extremo_superior,")"))

```

"Con 95% de confianza se espera que la compresión promedio de los bloques esté entre 58.54 y 61.75 N/mm\^2."

\#######################################################################################

**INTERVALO DE CONFIANZA DE UNA PROPORCIÓN:**

Por lo general es para cualitativos.

Fórmula:

$$
p-Z_{1-\frac{\alpha}{2}}.\sqrt{\frac{p(1-p)}{n}}<\pi< p+Z_{1-\frac{\alpha}{2}}.\sqrt{\frac{p(1-p)}{n}}
$$

$$
\pi: \text{proporción poblacional de éxitos}
$$

$$
p:\text{proporción muestral de éxitos}
$$

**Código para hallar el IC de la proporción:**

**1) Aquí se ingresa los datos:**

De la data FAMOSOS 2:

¿cuál es el IC de la proporción de cantantes , con 90% de confianza?

Cuando la variable es cualitativa ==\> table:

```{r}
table(DF$Actividad)
length(DF$Actividad)
```

La proporcion de cantantes es 7/25

```{r echo=TRUE}
# Ingrese la proporción muestral
p<- 7/25

# indica el tamaño de muestra
n<- 25

# indica el nivel de confianza
nc<-0.90
print(paste("el tamaño de muestra es:", n))
print(paste("el nivel de confianza es:",nc))
print(paste("la proporción muestral es:", p))


```

#### Aquí aparecerá el I.C. de la proporción

```{r echo=TRUE}
# Calcule el error estándar  
error_estandar <-  sqrt(p*(1-p)/n) 

alpha = 1-nc
z_crítico <- qnorm(1-alpha/2,0,1) 
margen_de_error <- z_crítico* error_estandar  
# Los extremo del intervalo de confianza de la media serán: 
extremo_inferior <- p - margen_de_error 
extremo_superior <- p + margen_de_error  
# Imprimir resultados:  
print(paste("significación:",alpha)) 
print(paste("Error estándar:", error_estandar)) 
print(paste("Z crítico:", z_crítico)) 
print(paste("margen de error o Tolerancia:", margen_de_error))  
print(paste("IC: (",round(extremo_inferior, 4),";", round(extremo_superior, 4),")"))  
```

Con 90% de confianza se afirma que el porcentaje de cantantes está comprendido entre 13.23% y 42.77%.

NOTA: para redondear con una cantidad de decimales se puede usar:

***round(cálculo, cantidad de decimales)***

EJEMPLO:

```{r}
# problema 1:
# En Toyota Mitsui, se está revisando como están las ventas desde el 2020. Para ello se ha tomado una muestra de 80 registros de venta y se ha encontrado que de los vehículos Corolla se han vendido 32 unidades. Con 90% de confianza, obtenga un intervalo para el porcentaje de Corollas vendidos.

```

**Solución:**

n=80 ==\> se vendió 32 Corollas ==\> p= 32/80

nc= 0.90 ==\> IC(porcentaje de corollas vendidos.)

Usamos el código de arriba:

1\) ingreso datos:

```{r echo=TRUE}
# Ingrese la proporción muestral
p<- 32/80

# indica el tamaño de muestra
n<- 80

# indica el nivel de confianza
nc<-0.90
print(paste("el tamaño de muestra es:", n))
print(paste("el nivel de confianza es:",nc))
print(paste("la proporción muestral es:", p))
```

2\) el intervalo:

```{r echo=TRUE}
# Calcule el error estándar  
error_estandar <-  sqrt(p*(1-p)/n) 

alpha = 1-nc
z_crítico <- qnorm(1-alpha/2,0,1) 
margen_de_error <- z_crítico* error_estandar  
# Los extremo del intervalo de confianza de la media serán: 
extremo_inferior <- p - margen_de_error 
extremo_superior <- p + margen_de_error  
# Imprimir resultados:  
print(paste("significación:",alpha)) 
print(paste("Error estándar:", error_estandar)) 
print(paste("Z crítico:", z_crítico)) 
print(paste("margen de error o Tolerancia:", margen_de_error))  
print(paste("IC: (",round(extremo_inferior,3),";",round(extremo_superior, 3),")"))  
```

Con 90% de confianza se espera que el porcentaje de Corollas vendidos por Toyota, estaria entre 31% y 49\$.

**HASTA AQUI POR HOY**

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

***AQUI LA SESIÓN DE RECUPERACIÓN:***

EJEMPLOS DE IC:

```{r}
# EJEMPLO 1:
#Un fabricante produce focos que tienen un promedio de vida de distribución normal y una desviación estándar de 40 horas.
#Si una muestra de 30 focos tiene una vida promedio de 780 horas.
#A) Encuentre el intervalo de confianza del 95% para la media de la  población de todos los focos que produce la empresa.
#B) ¿Cuál es el error máximo que se está cometiendo al usar un intervalo de confianza del 95%? 

```

SOLUCIÓN:

Nivel de confianza = 0.95

Alfa=0.05

a\) Ingreso los datos:

```{r}

n<-30 
media_muestral <-780
sigma_conocida <- 40

print(paste("el tamaño de muestra es:", n))
print(paste("la media muestral es:",media_muestral))
print(paste("la desviación a usar es:", sigma_conocida))
```

El IC de la media con sigma conocido:

```{r echo=TRUE}
# Calcule el error estándar 
error_estandar <- sigma_conocida/sqrt(n) 
alpha = 0.05  # ünico dato que el alumno escribe.
z_crítico <- qnorm(1-alpha/2,0,1) 
margen_de_error <- z_crítico* error_estandar  
# Los extremos del intervalo de confianza de la media serán:
extremo_inferior <- media_muestral - margen_de_error
extremo_superior <- media_muestral + margen_de_error 
# Imprimir resultados:

print(paste("Nivel de significación:",alpha))
print(paste("Error estándar:", error_estandar))
print(paste("Z crítico:", z_crítico))
print(paste("margen de error o Tolerancia:", margen_de_error))
print(paste("IC: (",round(extremo_inferior,3),";", round(extremo_superior,3),")"))

```

Con 95% de confianza se tiene que la duración promedio de los focos que produce la empresa estará entre **765.686 horas y 794.314 horas.**

NOTAS: con 95% de confianza

$$
¿\mu>760horas? \rightarrow \text{Es seguro que si es cierto}
$$

$$
¿\mu> 796 horas?\rightarrow\text{Es seguro que no es cierto}
$$

$$
¿\mu>780horas? \rightarrow \text{Aqui no se puede afirmar ello. Hay duda.}
$$

b\) Error máximo = (794.314 -765.686) / 2 = 14.314

Tener en cuenta que en el reporte del código también se tiene dicho valor:

```         
"margen de error o Tolerancia: 14.3135531497373"
```

```{r}
#EJEMPLO 2:
#Una compañía utiliza baterías en sus juegos electrónicos que según ellos duran un promedio de 30 horas, para confirmar esto se prueba 16 baterías siendo la media muestral de 27.5 horas y su desviación estándar S=5 horas. 
#Encuentre un intervalo de confianza del 95% para la media.
#Suponga que la distribución de las duración de las baterías es aproximadamente normal.

```

**SOLUCIÓN:**

AQUI SE HALLARÁ IC PARA LA MEDIA CON SIGMA DESCONOCIDO. PERO SE CONOCE **S**.

```{r echo=TRUE}

#n<- 16
#media_muestral <- 27.5
#sd_estimada <- 5

print(paste("el tamaño de muestra es:", n))
print(paste("la media muestral es:",media_muestral))
print(paste("la desviación estimada es:", sd_estimada))
```

AQUI SALE EL IC:

```{r echo=TRUE}
# Calcule el error estándar
error_estandar <- sd_estimada / sqrt(n)
alpha = 0.05 # único dato que el estudiante llena aquí
grados_de_libertad = n - 1 
T_crítico = qt(1-alpha/2,grados_de_libertad)
margen_de_error <- T_crítico* error_estandar 
# Calcular los extremos del intervalo de confianza 
extremo_inferior <- media_muestral - margen_de_error 
extremo_superior <- media_muestral + margen_de_error  
# Imprimir resultados: 
print(paste("significación:",alpha))
print(paste("grados de libertad de T: ",n-1))
print(paste("T crítico:", T_crítico))
print(paste("Error estándar:", error_estandar))
print(paste("margen de error:", margen_de_error))

print(paste("IC: (",round(extremo_inferior, 4),";", round(extremo_superior,4),")"))

```

**INTERVALO DE CONFIANZA DE LA DIFERENCIA DE 2 PROPORCIONES:**

Ver ppt para tener la fórmula.

**CÓDIGO PARA EL IC DE LA DIFERENCIA DE PROPORCIONES:**

Aquí **ingrese datos:**

```{r echo=TRUE}
# Ingrese las proporciónes muestrales
p1<- 32/80
p2<- 28/80

# indica el tamaño de muestra
n1<- 80
n2<- 80

# indica el nivel de confianza
nc<-0.98
print(paste("el tamaño de muestra 1 es:", n1))
print(paste("el tamaño de muestra 2 es:", n2))
print(paste("el nivel de confianza es:",nc))
print(paste("la proporción muestral 1 es:", p1))
print(paste("la proporción muestral 2 es:", p2))

```

aquí el **Intervalo de la diferencia de 2 proporciones:**

```{r echo=TRUE}
# Calcule el error estándar  
error_estandar <-  sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2) 

alpha = 1-nc
z_crítico <- qnorm(1-alpha/2,0,1) 
margen_de_error <- z_crítico* error_estandar  
# Los extremo del intervalo de confianza de la media serán: 
extremo_inferior <- p1-p2 - margen_de_error 
extremo_superior <- p1-p2 + margen_de_error  
# Imprimir resultados:  
print(paste("significación:",alpha)) 
print(paste("Error estándar:", error_estandar)) 
print(paste("Z crítico:", z_crítico)) 
print(paste("margen de error o Tolerancia:", margen_de_error))  
print(paste("IC: (",extremo_inferior,";", extremo_superior,")"))  
```

**NOTA PARA DIFERENCIA DE PROPORCIONES:**

Si: $A< \pi1 - \pi 2 < B$

$$
A(+)< \pi1 - \pi2 <B(+) \rightarrow:\pi1 >\pi2
$$

$$
A(-)< \pi1 - \pi2 <B(-) \rightarrow: \pi1 < \pi2
$$

$$
A(-)< \pi1 - \pi2 <B(+) \rightarrow:\pi1 = \pi2
$$

Problema:

```{r}
# Problema 3:
# En Toyota Mitsui, se está revisando como están las ventas desde el 2020. Para ello se ha tomado una muestra de 80 registros de venta y se ha encontrado que  se ha vendido 32 unidades de Corollas y 28 RAVs. Con 98% de confianza determine un intervalo para la diferencia de porcentajes de venta de Corollas y RAVs.

```

**Solución:**

1\) Datos:

**AQUI LOS DATOS**

```{r echo=TRUE}
# Ingrese las proporciónes muestrales
p1<- 32/80  # proporción de Corollas
p2<- 28/80  # proporción de RAVs

# indica el tamaño de muestra
n1<- 80
n2<- 80

# indica el nivel de confianza
nc<-0.98
print(paste("el tamaño de muestra 1 es:", n1))
print(paste("el tamaño de muestra 2 es:", n2))
print(paste("el nivel de confianza es:",nc))
print(paste("la proporción muestral 1 es:", p1))
print(paste("la proporción muestral 2 es:", p2))

```

2\) Hallando el intervalo

```{r echo=TRUE}
# Calcule el error estándar  
error_estandar <-  sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2) 

alpha = 1-nc
z_crítico <- qnorm(1-alpha/2,0,1) 
margen_de_error <- z_crítico* error_estandar  
# Los extremo del intervalo de confianza de la media serán: 
extremo_inferior <- p1-p2 - margen_de_error 
extremo_superior <- p1-p2 + margen_de_error  
# Imprimir resultados:  
print(paste("significación:",alpha)) 
print(paste("Error estándar:", error_estandar)) 
print(paste("Z crítico:", z_crítico)) 
print(paste("margen de error o Tolerancia:", margen_de_error))  
print(paste("IC: (",round(extremo_inferior,4),";", round(extremo_superior, 4),")"))  
```

el IC de la diferencia de porcentajes es:

**-12.78% \<** PI(Corollas) - PI(RAVs) **\< +22.78%**

==\> PI(Corollas) - PI(RAVs)=0 ==\> PI(Corollas)=PI(RAVs)

Con 98% de confianza se puede afirmar que en todo Toyota , los porcentajes de ventas de Corollas y RAVs son iguales.

# CASO: ASISTENTES A TALLER

```{r}
#DF<-read_csv("Asistentestaller.csv")
#DF
```

Caso textual:

```{r}
# Considere el data.frame  "Asistentestaller.csv“.
# Cargar dicha base de datos a R, con el nombre “asistaller”.
# Eliminar todos los NA del data.frame “asistaller”. Use  𝒅𝒓𝒐𝒑_𝒏𝒂(𝒅𝒂𝒕𝒂) y tener en cuenta que con esto se elimina todas las filas que contengan a algún NA.
# Seleccionar una muestra de tamaño 100, sin reposición (sin reemplazo) y denominarla  𝑎𝑠𝑖𝑠𝑡 .
# Responder lo siguiente:
#1) Con 90% de confianza ¿ se puede afirmar que las varianzas de las edades de hombres y mujeres que asistieron al taller son iguales?
#2) Con 90% de confianza ¿se puede afirmar que la edad promedio de los hombres es mayor que la edad promedio de las mujeres que asistieron al taller?
#3) Usando 90% de confianza ¿la proporción de mujeres que está en el tercer ciclo es la misma que la proporción de hombres que está en el tercer ciclo?

```

**SOLUCIÓN:**

Cargamos la poblacion dada en el csv.

```{r}
asistaller<-read_csv("Asistentestaller.csv")
asistaller
```

Estcor==\> Estatura corregida.

Sexcor==\> Sexo corregido.

Pero esta poblacion contienen varios NA y segun las instrucciones dadas se debe limpiar esta data con DROP

DROP(asistaller) ==\> dado que piden eliminar todas las filas con NA, segun el enunciado se usa ***DROP_NA***

```{r}
BT<-drop_na(asistaller) # con esto se va a borrar todas las filas que contienen NA

BT
```

Se ha obtenido 1443 filas completas , sin NA. (pero se ha perdido varias filas)

Ahora, segun el texto, se deb sacar una muestra sin reemplazo de tamaño 100

Obteniendo una muestra sin reposición (sin reemplazo) : ***sample_n***

```{r}
#para el proyecto quitar el # y D, y seleccionar la muestra, poniendole un nombre. Luego volver a colocar numeral, para que no vuelva a ejecutar y la muestra selccionada quede fija.
#Dn=100
#Dasist<- sample_n(BT,n,replace=FALSE) # al poner FALSE será sin reemplazo#
#Dasist
```

Acabo de hallar una muestra de tamaño 100, que va a ir cambiando, para cada estudiante.

```{r}
asist
```

**Asist** *es una muestra* (va cambiando para cada estudiante)

**BT** *es una población limpia*

**Asistaller** es la poblacion original (sin elimianr NA)

**Pregunta previa:**

-   Hallar un intervalo de confianza del 95% para la EDAD promedio de los asistentes.

Solución:

Como se tiene la Data original, esta actúa como población. Y de ahí se puede hallar SIGMA.

Hallamos primero sigma de EDAD, usando l**a población limpia BT (sin NA)**

```{r}
sd(BT$Edad)
```

$$
\sigma= 1.815397
$$

Como ya conozco sigma usare el IC de Normal con sigma conocido:

Necesito $\overline{X}$ (se saca de la muestra) y el nivel de confianza

```{r}
mean(asist$Edad)
```

$$
\overline{X}=19.12
$$

Ahora se usa el **código para IC de la media, con sigma conocido.**

**1) Aquí se ingresa los datos:**

```{r echo=TRUE}

n<-100  
media_muestral <-19.12
sigma_conocida <- 1.8154

print(paste("el tamaño de muestra es:", n))
print(paste("la media muestral es:",media_muestral))
print(paste("la desviación a usar es:", sigma_conocida))
```

## 2) Aquí aparecerá el I.C. de la media con R (sigma conocido)

Nivel de confianza = 0.95 ==\> alfa = 0.05

```{r echo=TRUE}
# Calcule el error estándar 
error_estandar <- sigma_conocida / sqrt(n) 
alpha = 0.05  # ünico dato que el alumno escribe.
z_crítico <- qnorm(1-alpha/2,0,1) 
margen_de_error <- z_crítico* error_estandar  
# Los extremo del intervalo de confianza de la media serán:
extremo_inferior <- media_muestral - margen_de_error
extremo_superior <- media_muestral + margen_de_error 
# Imprimir resultados:

print(paste("significación:",alpha))
print(paste("Error estándar:", error_estandar))
print(paste("Z crítico:", z_crítico))
print(paste("margen de error o Tolerancia:", margen_de_error))

print(paste("IC: (",extremo_inferior,";", extremo_superior,")"))


```

Con 95% de confianza se espera que la edad promedio de los asistentes al taller está entre 18.7642 años y 19.4758 años.

Nota:

Como se tiene la poblacion sin NA, se puede comprobar que está bien nuestros cálculos hallando el $\mu$ verdadero:

Usando la población BT:

```{r}
mean(BT$Edad)
```

18.7642 años \< mu= 19.22592 \< 19.4758 años.

Notamos que este valor de $\mu$ si está contenido en el IC de la media que hallamos

**HASTA AQUI POR HOY SABADO.**

NOTA: Cuando la muestra es grande (mas de 30) se puede usar una aproximación de la T student a la Normal ( debido al TLC)

**PREGUNTAS:**

TRABAJANCO CON asist

```{r}
asist
```

1\) *¿Las edades de hombres y mujeres tienen igual varianza?* con nc=0.90

**SOLUCIÓN:**

se desea comparar dos varianzas ==\> se debe usar el IC con Fisher.

se necesita calcular las varianzas de hombres y mujeres:

```{r}
Masc<-filter(asist, Sexcor=="M")
Masc
Fem <- filter(asist, Sexcor=="F")
Fem
```

```{r}
var(Masc$Edad)
var(Fem$Edad)
```

**Para hallar el IC de la división de dos varianzas se debe usar el código siguiente:**

```{r}
var1=2.067603 # varianza de muestra 1 (hombres)
var2=3.028226 # varianza de muestra 2 (mujeres)
nc=0.90
n1=68
n2=32
alpha=1-nc
VC1<-qf(alpha/2, n2-1, n1-1)
VC2<-qf(1-alpha/2,n2-1,n1-1 )

extremo_inf<- (var1/var2)*VC1
extremo_sup<- (var1/var2)*VC2
extremo_inf
extremo_sup
```

Conclusión: Con 90% de confianza se tiene que la divisón de varianzas de hombres entre mujeres est´´a comprendido entre 0.3981 y 1.1077 ==\> las varianzas son iguales.

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Para este intervalo se está usando la distribución Fisher.

Tener en cuenta aquí lo siguiente:

$$
A< \frac{\sigma1^2}{\sigma2^2}<B
$$

Casos:

1\) Si A \<1 y B \<1 ==\> $\sigma 1 < \sigma 2$

2\) Si A \>1 y B\>1 ==\> $\sigma1 > \sigma 2$

3\) Si A \<1 y B \>1 ==\> $\sigma1 =\sigma 2$

2\) Con 90% de confianza ¿se puede afirmar que la edad promedio de los hombres es mayor que la edad promedio de las mujeres que asistieron al taller?

Solución:

¿Edad promedio de hombres es mayor que Edad promedio de mujeres?

Se va a comparar dos medias poblacionales y por eso se debe usar RStudio mediante: **T.Test** (para comparar dos medias poblacionales con varianzas desconocidas)

Este código **T.test** requiere saber si las varianzas son iguales o diferentes.

En la parte anterior se descubrió que las varianzas son iguales.

```{r}
t.test(Masc$Edad,Fem$Edad, var.equal = TRUE, conf.level = 0.90)
```

El intervalo es: **(-0.4636; 0.6327).**

Es decir: **-0.4636**\< **MU hombres - MU mujeres**\< **0.6327** ==\> Como el intervalo contiene al CERO, se puede afirmar con 90% de confianza que los promedios de edades de hombres y mujeres son iguales.

**NOTA:**

si se tiene el IC:

$$
C<\mu1 - \mu2<D
$$

Entonces:

1\) Si C=(-) y D=(-) ==\> $\mu1 < \mu2$

2\) SI C=(+) y D=(+) ==\> $\mu 1 > \mu 2$

3\) Si C=(-) y D=(+) ==\> $\mu 1= \mu 2$

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

3\) *Usando 90% de confianza ¿la proporción de mujeres , **que está en el tercer ciclo** es la misma que la proporción de hombres , **que está en el tercer ciclo**?*

Mi 100% lo conforman **los alumnos del ciclo 3,** por ello debo usar primero: filter.

```{r}
C3<- filter(asist, Ciclo=="3")
C3
```

```{r}
table(C3$Sexcor)
```

Al usar **filter** se observa que hay 44 personas del ciclo 3.

Se obtiene

Pfemenino= 15/44,

Pmasculino= 29/44

**otro forma (sin filter)**

```{r}
table(asist$Ciclo, asist$Sexcor)
```

Se observa de esta tabla que mi 100% será 44 alumnos del ciclo 3 y de ellos , 15 son femeninos y 29 son Masculinos.

usamos el codigo para diferencia de proporciones:

```{r echo=TRUE}
# Ingrese las proporciónes muestrales
p1<- 15/44   # proporcion de mujeres
p2<- 29/44   # proporcion de hombres


# indica el tamaño de muestra
n1<- 44
n2<- 44


# indica el nivel de confianza
nc<-0.90
print(paste("el tamaño de muestra 1 es:", n1))
print(paste("el tamaño de muestra 2 es:", n2))
print(paste("el nivel de confianza es:",nc))
print(paste("la proporción muestral 1 es:", p1))
print(paste("la proporción muestral 2 es:", p2))
```

Ahora el IC:

```{r echo=TRUE}
# Calcule el error estándar  
error_estandar <-  sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2) 

alpha = 1-nc
z_crítico <- qnorm(1-alpha/2,0,1) 
margen_de_error <- z_crítico* error_estandar  
# Los extremo del intervalo de confianza de la media serán: 
extremo_inferior <- p1-p2 - margen_de_error 
extremo_superior <- p1-p2 + margen_de_error  
# Imprimir resultados:  
print(paste("significación:",alpha)) 
print(paste("Error estándar:", error_estandar)) 
print(paste("Z crítico:", z_crítico)) 
print(paste("margen de error o Tolerancia:", margen_de_error))  
print(paste("IC: (",extremo_inferior,";", extremo_superior,")"))  
```

Conclusión: -0.4844\< PI femenino - PI masculino \< -0.1519

dado que en ambos lados se ha obtenido (-) y (-) entonces debe concluirse que:

PI femenino \< PI masculino.

Con 90% de confianza se afirma que hay mayor porcentaje de masculinos en el ciclo 3, que el porcentaje de femeninos.

**Problema:**

De una muestra de tamaño 50 se ha selecionado algunos alumnos y se ha obtenido que el IC de la edad promedio es (18.48; 20.52). Use la desviación poblacional del data frame original y halle el nivel de confianza que se ha usado.

Solución:

Hallamos la desviacion de las edades de todos los alumnos:

```{r}
sd(asistaller$Edad, na.rm= TRUE)
```

Ahora Sigma= 2.738389 de la población==\> se debe usar el IC de MU con sigma conocido

==\> con Normal

$$
\overline{X}- z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}\leq \mu\leq \overline{X}+ z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}
$$

Pero:

$$18.48<= \mu <= 20.52$$

Luego, comparando extremos

$$
 \overline{X}+ z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}=20.52
$$

$$
\overline{X}- z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}=18.48
$$

Si se suma ambos se halla la media de la muestra.

Si lo resto:

$$
2*z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}=2.04 \rightarrow 2*z_{1-\frac{\alpha}{2}}\frac{2.738389}{\sqrt{50}}=2.04
$$ Luego: Z(1- alfa/2)\* (2.738389/7.07106)=1.02 ==\> Z(1-alfa/2) = 2.63384 ==\>P(Z\<= 2.63384)= 1-alfa/2

```{r}
pnorm(2.63384,0,1)
```

1-(alfa/2) = 0.9957787 ==\> Hallo alfa= 0.0084426 ==\> nc= 1- alfa = 0.9915574 = 99.15574%

**DATOS PAREADOS:**

Halla el IC para la diferencia de medias, siempre y cuando se tenga un "Antes" y un "Después".

Este intervalo se halla con **t.test**

Ejemplo:

Se tienen las notas de 6 alumnos , en el parcial y los mismos, en el final.

¿Puede afirmarse que ha mejorado sus notas con 90% de confianza?

```{r}
Parcial<- c(14, 13, 17, 09, 12, 08)
Final<- c( 16, 10, 17, 11, 12, 06)
```

El IC se saca usando t.test y entre sus argumentos se debe colocar *paired = TRUE.* Ya no se coloca como son las varianzas.

```{r}

t.test(Parcial,Final, paired = TRUE, conf.level = 0.90)
```

Con 90% de confianza se halla que la diferencia de promedios entre el parcial y final es:

-   1.512540 \< MU (parcial) - MU (final) \< 1.845874

Como la izquierda es positiva y la derecha es positiva ==\> la diferencia puede debe ser positiva y por lo tanto, en el parcial tienen mayor nota promedio y en el final menor nota promedio.

MU (parcial) = Mu (final).

**HASTA AQUI EN MARTES.**

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

```{r}
qnorm(0.975,0,1)
```

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Consideremos el data frame: *Asistentestaller.csv.*

Lectura:

```{r}
DF<- read_csv("Asistentestaller.csv")
DF
```

La data tiene 2039 filas.

¿Tiene NA?

Aplicaré sum(complete.case) para saber cuantas filas no tienen NA

```{r}
sum(complete.cases(DF))
```

Se tiene 1443 filas sin NA. Se debe eliminar las filas que tienen NA, porque en le texto del problema 3 de la ppt, así lo pide

Eliminando todas las filas con NA:

```{r}
asistallersinNA<-drop_na(DF)  
DFL<-asistallersinNA
# se halla asi  "data frame limpio"
DFL
```

**Problema previo al 3 de ppt**

```{r}
# Considere solo una  muestra  de tamaño 50  de "Asistentestallersin NA" de la base de datos "Asistentestaller.csv"  y usando 10% de significación, ¿puede afirmarse que la edad promedio de asistentes al taller es superior a 18.5 años? 

```

**Solución.**

Seleccionando una muestra de tamaño 50:

```{r}
#n=50
#MDFL<- sample_n(DFL,n,replace=FALSE) # al poner FALSE será sin reemplazo
#MDFL   #muestra del data frame limpio
```

```{r}
MDFL  # esta es la muestra con la cual debo trabajar

```
