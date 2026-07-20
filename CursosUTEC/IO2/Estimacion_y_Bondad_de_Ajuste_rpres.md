---
curso: IO2
titulo: Estimacion y Bondad de Ajuste
slides: 0
fuente: Estimacion y Bondad de Ajuste.Rpres
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Estimacion y Bondad de Ajuste.Rpres. -->

<!-- INTERPRETAR: material de formato .rpres (Estimacion y Bondad de Ajuste.Rpres). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

Estimación y Bondad de Ajuste
========================================================
author: Claudia Antonini 
date: Noviembre 2020
autosize: true


Objetivos: Bondad de ajuste a modelos y parámetros
===========================================================
![](Logo-PNG-Negro.png)

+ Entender e interpretar el **diagrama Mc Cullen/Frey.**

+ Estimar por **máxima verosimilitud** parámetros relevantes con el fin de alimentar los modelos necesarios para la simulación.

+ Entender e interpretar **gráficos Q-Q y P-P** y **pruebas de bondad** de ajuste tales como **chi-cuadrado y Kolmogorov-Smirnov**.

+ Estructurar un análisis de datos de entrada de simulación basado en un problema planteado utilizando el **principio de parsimonia**.


¿Cómo ajustamos un modelo a un conjunto de datos?
================================================
Se requiere seguir los siguientes cuatro pasos:

>  1) Verificar que las observaciones son **independientes**

>  2) Escoger una **distribución de probabilidad** que modele lo mejor posible el conjunto de datos dado.

>  3) Encontrar **estimadores apropiados para los parámetros** de dicha distribución

>  4)  **Validar** la calidad de dicha escogencia en combinación con los estimadores encontrados.


Escoger una distribución de probabilidad
====================================================
El paquete [´fitdistrplus´](http://cran.r-project.org/package=fitdistrplus)  provee lo que necesitamos para este fin. Para instalarlo recuerde hacer uso del comando ´install.packages("")´:

```{r}
# install.packages("fitdistrplus")
```

¿Cómo usamos el paquete ´fitdistrplus´
==================================================
Para ilustrar dicho paquete haremos uso del conjunto de datos llamado groundbeef el cual está incluído en el paquete. Dicho conjunto de datos contiene información de las raciones de hamburguesas de carne en gramos consumidas por niños menores de 5 años en Francia.


```{r}
library(fitdistrplus)
require(utils)
try(data(package = "fitdistrplus") ) # muestra datasets en fitdistrplus package
data(groundbeef)    # carga dataset 'groundbeef'
```


Visualización de los datos
==================================

> - **Histogramas** a través de ´hist´ ayuda a visualizar la **función de densidad empírica** de los datos.

> - La función ´plotdist´ permite visualizar la **función de distribución empírica** de los datos. 

Uso de la función ´plotdist´
=============================================

```{r}
plotdist(groundbeef$serving, histo = TRUE, demp = TRUE)
```

Skewness como medida de simetría
==============================================
El estadístico **skewness** como **medida de simetría** y su **estimador insesgado**:


$$
\begin{align*}
sk(X)=&\frac{E[(X-E(X))^{3}]}{(Var(X))^{3/2}} \\\\
\widehat{sk}=&\frac{\sqrt{n(n-1)}}{n-2}\frac{m_{3}}{m_{2}^{\frac{3}{2}}}
\end{align*}
$$


en donde $m_{k}=\frac{1}{n}\sum_{i=1}^{n}(x_{i}-\bar{x})^{k}$ para $k=2,3$

Un skewness distinto de cero significa falta de simetría en la función de densidad empírica. **La función de densidad de la normal tiene skewness igual a cero.**

La curtosis como medida del peso de las colas
=======================================================
El estadístico **curtosis (Kurtosis)** como **medida del peso de las colas de la función de densidad** y su **estimador insesgado**:


$$
\begin{align*}
&kr(X)=\frac{E[(X-E(X))^{4}]}{(Var(X))^{2}} \\\\
&\widehat{kr}=\frac{n-1}{(n-2)(n-3)}\left[\frac{(n+1)m_{4}}{m_{2}^{2}}-3(n-1)\right]+3
\end{align*}
$$

en donde $m_{k}=\frac{1}{n}\sum_{i=1}^{n}(x_{i}-\bar{x})^{k}$ para $k=2,4$

Observaciones:
===========================================================

> - **La normal es mesocúrtica pues tiene curtosis igual a 3.**

> - Si una densidad tiene curtosis **menor que 3** se denomina **platicúrtica**, es decir, tiene **colas menos pesadas que la normal**

> - Si una densidad tiene curtosis **mayor que 3** es **leptocúrtica**, es decir, tiene **colas más pesadas que la normal**. 


Gráfico de Mc Cullen y Frey: skewness al cuadrado vs curtosis
===============================================================

```{r}
descdist(groundbeef$serving, boot = 1000)
```

Observaciones
=====================================

> - **La normal, la uniforme, la logística y la exponencial** como tienen skewness y curtosis únicas independientemente de sus parámetros son representadas con puntos.

> - **La gamma, la lognormal** tienen skewness y curtosis a lo largo de una recta. La **weibull** se parece.

> - Las skewness y las curtosis de la **beta** viven en un área.

Mas observaciones:
=====================================================

> - La función ´descdist´ provee estadísticos descriptivos clásicos como **el mínimo, el máximo, la mediana, la media, la desviación estándar, la skewness y la curtosis**. Por descarte, se entregan los estimadores insesgados de los últimos tres. Sin embargo, cambiando el **argumento ´method´** from "unbiased" to "sample" se puede eliminar esa corrección. 

> - El **argumento lógico ´discrete´** cuando se puede igualar a TRUE para considerar distribuciones discretas

Advertencias:
=============================================================

> - Ambos estadísticos de la skewness y la curtosis son **insesgados**, pero tienen una **varianza grande**.

> - Un procedimiento de bootstrap no paramétrico puede ser utilizado usando el argumento ´boot´. El mismo toma tantas **muestras con reemplazamiento como indique el argumento ´boot´** y lo reporta en el gráfico de Mc. Cullen y Frey con puntos naranjas.


Estimación por el método de los momentos:
=========================================================

Sean $\mu_{j}$ y $m_{j}$ los momentos de orden $j$ poblacionales y muestrales respectivamente de una variable poblacional de interés. Recordemos que 

$$
\mu_{j}(\Theta_{1}, \Theta_{2}, \cdots, \Theta_{k})=m_{j} \text{ para } j=1,2,\cdots k
$$

La soluciones $\hat{\theta_{1}}, \hat{\theta_{2}}, \cdots, \hat{\theta_{k}}$ de este sistema de $k$ ecuaciones con $k$ incógnitas son conocidos como los **estimadores del método de los momentos** o MOM.


Ejemplo:
================================================================

**Sea $0.2; 0.9; 0.05; 0.47; 0.56; 0.8; 0.35$ una muestra aleatoria simple de una variable poblacional $Y$ cuya densidad viene dada por $f(y)=(\Theta+1)y^{\Theta}$ para $0\leq y \leq 1$.**

a) Detemine el estimador de $\Theta$ por MOM.

b) Determine el estimador MOM de $P(Y > 0.8)$

Solución parte a)
==============================================================

$$
\begin{align*}
&\mu_{1}=E(Y)=\int_{0}^{1}y(1+\Theta)y^{\Theta}dy=\frac{\Theta+1}{\Theta+2}\\
&m_{1}=\overline{Y}\equiv \frac{\sum_{i=1}Y_{i}}{n}\\
&\text{ finalmente el estimador de }\Theta\\
& \frac{\hat{\Theta}+1}{\hat{\Theta}+2}=\overline{Y}\\
& \hat{\Theta}=\frac{2\overline{Y}-1}{1-\overline{Y}}
\end{align*}
$$

El estimado puntual 
===========================================================
Evaluando en la muestra dada, obtenemos un **estimado** para $\Theta$,

$\hat{\theta}=\frac{2\overline{Y}-1}{1-\overline{Y}}= \frac{2(0.4757)-1}{1-0.4757}= -0.0926$

Solución parte b)
=======================================================

La función de distribución acumulada de $Y$ viene dada por:

$$
\begin{align*}
F_{Y}(y)\equiv& P(Y\leq y)=\int_{0}^{y}(\Theta +1)t^{\Theta}dt=y^{\Theta+1}\\
P(Y > 0.8)=&1-F_{Y}(0.8)\\
=&1-(0.8)^{\hat{\Theta}+1}\\
=& 1-(0.8)^{-0.0926+1}=0.1832976
\end{align*}
$$

```{r}
1-(0.8)^(1-0.0926)
```

Estimación de parámetros por máxima verosimilitud
=======================================================
Una vez seleccionadas una o más densidades paramétricas $f(.|\theta)$ con $\theta \in \mathbb{R}^{d}$ que podrían ajustarse al conjunto de datos, una a la vez, usando la función ´fitdist´ y bajo la suposición de que **los datos son independientes e idénticamente distribuidos**, los parámetros son estimados, por defecto, **maximizando la función de verosimilitud**:


$$
L(\theta)=\prod_{i=1}^{n}f(x_{i}|\theta)
$$

Ejemplo: estimemos el parámetro de la exponencial
==================================================
Recordemos que la **función densidad de la exponencial parámetro $\lambda$** viene dada por:

>
$$
f(x|\lambda)=\begin{cases}
      \lambda e^{-\lambda x} & \text{ cuando } x > 0\\
      0                      & \text{ fuera }
     \end{cases}
$$

Por lo tanto, su **función de verosimilitud** vendía dada por:

>
$$
\begin{align*}
L(\lambda)=&\prod_{i=1}^{n}\lambda e^{-\lambda x_{i}}\\
          =& \lambda^{n}\exp\left(-\lambda\sum_{i=1}^{n}x_{i}\right)
\end{align*}
$$

Es más fácil maximizar la log-verosimilitud
=============================================
La **función de log-verosimilitud** de la exponencial parámetro $\lambda$ es:

>
$$
\begin{align*}
l(\lambda)=\log(L(\lambda)) =& \log\left[\lambda^{n}\exp\left(-\lambda\sum_{i=1}^{n}x_{i}\right)\right]\\
                 =& n\log(\lambda)-\lambda \sum_{i=1}^{n}x_{i}\\
\end{align*}
$$


Maximicemos la log-verosimilitud:
=====================================================

$$
\begin{align*}
\frac{d}{d\lambda}\log(L(\lambda))=&  \frac{n}{\lambda}- \sum_{i=1}^{n}x_{i}=0\\
\widehat{\lambda}=& \frac{1}{\bar{x}(n)}=MLE(\lambda)\\
\frac{d^{2}}{d\lambda^{2}}\log(L(\lambda))=&-\frac{n}{\lambda} < 0

\end{align*}
$$

Observe que es un **máximo** pues la segunda derivada es siempre negativa.

Ejemplo: estimemos el parámetro de la geométrica
==================================================
Recordemos que la función de probabilidad de masa de una geométrica parámetro $p$ viene dada por:

$$
P(X=x|p)=(1-p)^{x}p
$$

Por lo tanto, su **función de verosimilitud** vendía dada por:

>
$$
\begin{align*}
L(p)=&\prod_{i=1}^{n}(1-p)^{x_{i}}p\\
          =& p^{n}(1-p)^{\sum_{i=1}^{n}x_{i}}
\end{align*}
$$

La **función de log-verosimilitud** de la exponencial parámetro $\lambda$ es:

>
$$
\begin{align*}
l(p)=\log(L(p)) =& \log\left[ p^{n}(1-p)^{\sum_{i=1}^{n}x_{i}}\right]\\
                 =& n\log(p)+ \sum_{i=1}^{n}x_{i}log(1-p)\\
\end{align*}
$$

Maximicemos la log-verosimilitud:
=====================================================

$$
\begin{align*}
\frac{d}{dp}\log(L(p))=& \frac{n}{p}- \frac{\sum_{i=1}^{n}x_{i}}{1-p}=0\\
\widehat{p}=& \frac{1}{\bar{x}(n)+1}=MLE(p)\\
\frac{d^{2}}{dp^{2}}\log(L(p))=&-\frac{n}{p^{2}}-\frac{\sum_{i=1}^{n}x_{i}}{(1-p)^{2}} < 0
\end{align*}
$$

Observe que es un **máximo** pues la segunda derivada es siempre negativa.

¿Por qué estimar parámetros por máxima verosimilitud?
======================================================

> - Para la mayoría de las distribuciones el $MLE(\theta)$ es **único**

> - Los MLE **no son necesariamente insesgados** pero

>
$$
\lim_{n\rightarrow \infty}E(\hat{\theta}(n))=\theta
$$

> -  MLE son **invariantes**. Es decir, si $\Phi=h(\theta)$, entonces el $MLE(\Phi)=MLE(h(\theta))$.

> - MLE son **fuertemente consistentes**. Es decir,

>
$$
\lim_{n\rightarrow\infty}\hat{\theta}(n)=\theta \text{ con prob 1}
$$

El mejor estimador asintóticamente normal
==================================================================

Es decir,

$$
\frac{\hat{\theta}(n)-\theta}{\sqrt{\delta(\hat{\theta}(n))/n}}\rightarrow N(0,1)
$$

en distribución donde $\delta(\hat{\theta})\equiv -\frac{n}{E\left(\frac{d^{2}l(\theta)}{d^{2}}\right)}$

Intervalo de confianza para MLE
=========================================

Entonces, para $n$ grande, un aproximado para el $100(1-\alpha)\% $ intervalo de confianza para $\theta$ es

>
$$
\hat{\theta}(n)\pm z_{1-\alpha/2}\sqrt{\frac{\delta(\hat{\theta})}{n}}
$$

Ejemplo
====================================================
Construya un intervalo de confianza del 90\% para el parámetro $p$ de la distribución geométrica.

Es fácil ver que:

>
$$
E\left(\frac{d^{2}l(p)}{dp^{2}}\right)= -\frac{n}{p^{2}}-\frac{\sum_{i=1}^{n}x_{i}}{(1-p)^{2}}=-\frac{n}{p^{2}(1-p)}
$$

por lo tanto, $\hat{\theta}(n)=p^{2}(1-p)$.

El intervalo de confianza deseado vendría dado por:

>
$$
\hat{p}\pm 1.645\sqrt{\frac{\hat{p}^{2}(1-\hat{p})}{n}}
$$

¿Cómo lo hacemos en R? summary de la función fitdist
====================================================

```{r}
fw <- fitdist(data=groundbeef$serving, distr = "weibull", method="mle")
summary(fw)
```

¿Qué reporta el summary de la función fitdist?
===================================================

> - Los estimados de los parámetros

> - Los estimados de los errores estándar
 
> - La función de log-verosimilitud

> - Los criterios de información Akaike y Bayesiano AIC y BIC respectivamente

> - La matriz de correlaciones de los estimadores de los parámetros.


¿Cómo lo hacemos en R? plot de la función fitdist
====================================================

```{r, echo=FALSE}
fw <- fitdist(data=groundbeef$serving, distr = "weibull", method="mle")
#plot(fw)
```

```{r, echo=FALSE}
plot(fw)
```



¿Qué reporta plot de la función fitdist?
===================================================

> - El gráfico de la densidad teórica y el histograma de la densidad empírica

> - Las funciones de distribución empíricas y teóricas

> - El Q-Q plot representa los cuantiles empíricos (eje y) versus los cuantiles teóricos (eje x)

> - Los valores de la función de distribución empírica (eje y) versus los valores de la teórica (eje x)





¿Qué aprendimos hoy?
=================================================================
