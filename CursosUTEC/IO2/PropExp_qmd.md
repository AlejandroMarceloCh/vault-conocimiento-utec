---
curso: IO2
titulo: PropExp
slides: 0
fuente: PropExp.qmd
---

---
title: "Propiedades de la Exponencial"
author: "Prof. Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.jpg
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
    html:
      code-fold: true
      code-summary: "Show the code"
editor: source
date: "today"
---


## Objetivos generales:

-   Ilustrar con ejemplos prácticos en el contexto de la ingeniería industrial el uso del **modelo exponencial**.

-   Entender **la propiedad de pérdida de la memoria** de la variable aleatoria exponencial y su uso en el contexto de la Ingeniería Industrial.

-   Enunciar, deducir e interpretar las propiedades del **mínimo de n variables aleatorias exponenciales** independientes y de la **probabilidad del primer fallo**

-   Enunciar, aplicar y contrastar en el contexto propio de operaciones de ingeniería industrial **las propiedades débil y fuerte de pérdida de la memoria del modelo exponencial**.

-   Caracterizar la **suma determinística de variables aleatorias exponenciales independientes como una Erlang**.

## El modelo exponencial: aplicaciones

$X\sim exp(λ)$

-   El tiempo entre llegadas de clientes a una cafetería

-   El tiempo transcurrido entre pedidos en un centro de distribución.

-   El tiempo transcurrido entre dos reposiciones de inventario de un producto en particular

-   El tiempo de vida de un componente electrónico.

## Densidad exponencial

$$
f(x) = \begin{cases} \lambda e^{-\lambda x} & \text{si } x\geq 0 \\ 0 \quad & \text{si} x<0\end{cases}
$$

[Exploremos la exponencial](https://seeing-theory.brown.edu/probability-distributions/index.html#section2)

## La función de distribución acumulativa exponencial

$$
F(x)=\int_0^x\lambda e^{-\lambda t}dt=\begin{cases}1-e^{-\lambda x} & \quad \text{si } x \geq 0\\0 & \quad \text{si } x<0 \\\end{cases}
$$

La **confiabilidad** exponencial:

$$P(X > x)= e^{-\lambda x}$$

## Modelo exponencial: Esperanza y varianza {.scrollable}


\begin{align*}
E(X)=&\int_{0}^{\infty}x\lambda e^{-\lambda x}= \frac{1}{\lambda}\\\\Var(X)\equiv & E(X^{2})-E^{2}(X)=\\\\            =& \int_{0}^{\infty}x^{2}\lambda e^{-\lambda x}-\left(\int_{0}^{\infty}x\lambda e^{-\lambda x}\right)^{2}\\\\            =&\frac{1}{\lambda^{2}}
\end{align*}


**Nota:** preste atención a las unidades

## Ejemplo:

**Suponga que un fusible comienza a funcionar a tiempo cero. Se conoce que su tiempo de vida es una variable aleatoria exponencial con parámetro** $\lambda=1/hora$

1.  **Calcule la probabilidad de que el fusible funcione continuamente bien por al menos 3 horas**

2.  **Suponga que el fusible no ha fallado en las primeras tres horas después de su colocación. Calcule la probabilidad de que no falle durante la siguiente hora.**

## Solución

Sea

$$
T: \text{ el tiempo de vida del fusible en horas }\sim\exp(1/ \text{hora})
$$

La probabilidad requerida en a) es:


\begin{align*}
P(T > 3)=& e^{-3}
\end{align*}


## Continuación ejemplo

La probabilidad requerida en b) es:


\begin{align*}
P\left(T > 4\left|\right.T > 3\right)=&\frac{P\left( T > 4,  T > 3\right)}{P(T > 3)}\\\\            =&\frac{P(T>4)}{P(T>3)}\\\\
=&\frac {e^{-4}}{e^{-3}}= e^{-1}=P(T > 1)
\end{align*}


## Propiedad de pérdida de la memoria

Si $X\sim \exp(\lambda)$, entonces $X$ satisface la siguiente propiedad conocida como **la ley débil de pérdida de la memoria**:

$$
P\left(X > t+s\left|\right. X > s \right)=P\left(X > t\right) \qquad \forall \quad s,t > 0
$$

## Demostración:


\begin{align*}
P\left(X > t+s\left|\right. X > s\right)=&\frac{P(X > t+s,X > s)}{P(X > s)}\\\\            =&\frac{P(X > t+s)}{P( X > s)}\\\\            
      =&\frac {e^{-\lambda(t+s)}}{e^{-\lambda s}}=e^{-\lambda t}\\\\
      =&P(X>t)
\end{align*}



## Intuitivamente:

-   Si $X$ representa la vida útil de un componente electrónico, entonces la ecuación anterior dice que la probabilidad de que un componente que ya haya durado al menos $s$ años dure otros $t$ años adicionales es la misma que la probabilidad de que un componente dure al menos t años.

**La única variable aleatoria continua con la propiedad de la pérdida de memoria es la exponencial**


## Propiedad débil de pérdida de la memoria y tiempos de espera en una parada de autobus


Amanda y Sofia quieren tomar un autobús. Los autobuses llegan a la parada acorde con un proceso de Poisson con parámetro $\lambda=\frac{1}{30}$. Es decir, los tiempos entre autobuses consecutivos tienen una distribución exponencial con parámetro $\lambda=\frac{1}{30}$  y los buses llegan, en promedio, cada 30 minutos. Amanda es desafortunada y llega a la parada justo cuando acaba de partir un autobus. Su tiempo de espera hasta que llegue el siguiente autobus es de aproximadamente 30 minutos. Sofia llega a la parada de autobuses 10 minutos después que Amanda. Increiblemente, el tiempo que Sofia va a esperar por su autobus también es exponencial con parámetro $\lambda=\frac{1}{30}$. 

## ¿Cuánto esperan en promedio Amanda y Sofia?

Observe que Sofia espera más de $t$ minutos si Amanda espera más de $t+10$ minutos dado que el bus no llega en los primeros 10 minutos y antes de que llegue Sofía a la parada. Sean $A$ y $S$ los tiempos de espera de Amanda y Sofia respectivamente. Por la ley débil de pérdida de la memoria, se tiene que:


\begin{align*}
P(S>t)=&P(A>t+10|A>10)\\
      =&\frac{P(A>t+10)}{P(A>10)}\\
      =&\frac{e^{-\frac{t+10}{30}}}{e^{-\frac{10}{30}}}\\
      =& e^{-\frac{t}{30}}=P(A>t)
\end{align*}

de donde deducimos que los tiempos de espera de Amanda, $A$, y Sofía $S$ son variables aeatorias que tienen la misma distribución.

## Simulemos la parada de autobus en R

```{r}
#| echo: true

trials <- 5000
Amanda <- numeric(trials)
Sofia <- numeric(trials)
for (i in 1:trials) {
  bus <- rexp(1,1/30)         # Tiempo de llegada del bus
  Amanda[i] <- bus            # Tiempo de espera de Amanda
  while (bus < 10) {
    bus <- bus + rexp(1,1/30) # Tiempos de llegadas de buses 
                              # hasta que llega Sofía
  }
  Sofia[i] <- bus-10          # Tiempo de espera de Sofía
}
mean(Amanda)
mean(Sofia)

```

## Miremos los histogramas de los tiempos de espera de Amanda y Sofía cuando Sofía llega la parada de autobuses 10 minutos después que Amanda

```{r}
par(mfrow=c(1,2))
hist(Amanda,xlab="",prob=T,ylab="",main="",yaxt="n")
mtext(1,text="Tiempo de espera de Amanda")
axis(2,at=c(0,.01,.02),labels=c(0,0.01, 0.02))
hist(Sofia,xlab="",prob=T,ylab="",yaxt="n",main="")
mtext(1,text="Tiempo de espera de Sofia")
axis(2,at=c(0,.01,.02),labels=c(0,0.01,0.02))

```



## Probabilidad del primer fallo entre dos exponenciales independientes

Sean $T_1$ y $T_2$ dos v.a. exponenciales independientes con parámetros $\lambda_{1}$ y $\lambda_{2}$ respectivamente. Entonces,

$$
P(T_{1} < T_{2})=\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}
$$

## Un poco de contexto:

**Supongamos que estamos monitoreando una cola** $M/M/1$**. Sea** $T_{1}$ **el tiempo de servicio del primer cliente- Se sabe que** $T_{1}\sim exp(\mu_{1})$**. Sea** $T_{2}$ **el tiempo que transcurre desde la llegada del primer cliente al sistema hasta la llegada del segundo. Se sabe que** $T_{2}\sim exp(\lambda_{2})$**. Calcule la probabilidad de que el segundo cliente no espere.**

## Solución:

Por la probabilidad del primer fallo entre dos exponenciales independientes, la probabilidad requerida es:

$$
P(T_{1} < T_{2})= \frac{\mu_{1}}{\mu_{1}+\lambda_{2}}
$$

## Demostración:


\begin{align*}
P(T_{1} < T_{2})=& \int_{0}^{\infty}P(T_{1} < T_{2}| T_{2}=x)f_{T_{2}}(x)dx\\                        =& \int_{0}^{\infty}P\left(T_{1} < x\left|\right. T_{2}=x\right)f_{T_{2}}(x)dx\\
                 & \text{ por independencia de $T_{1}$ y $T_{2}$}\\            
                =& \int_{0}^{\infty}P(T_{1} < x)f_{T_{2}}(x)dx\\           
                =& \int_{0}^{\infty}F_{T_{1}}(x)f_{T_{2}}(x)dx\\           
                =& \int_{0}^{\infty}\left(1-e^{-\lambda_{1} x}\right)\lambda_{2}e^{-\lambda_{2}x}dx\\            
                =& \frac{\lambda_1}{\lambda_1+\lambda_2}
\end{align*}


## Mínimo de dos exponenciales independientes

Sean $T_1$ y $T_2$ dos v.a. exponenciales independientes con parámetros $\lambda_{1}$ y $\lambda_{2}$ respectivamente. Entonces,

$$T=\min{(T_1,T_2)} \sim exp(\lambda_1+ \lambda_2)$$

## Un poco de contexto:

**Supongamos que tenemos dos componentes conectados en serie. Ambos tiempos de vida exponenciales e independientes con parámetros** $\lambda_{1}$ **y** $\lambda_{2}$**. Calcule la distribución del tiempo de vida del sistema completo.**

## Solución:

Sea $T_{i}:$ el tiempo de vida del componente $i$ para $i=1,2$.

Sea $T:$ el tiempo de vida del sistema

Observe que el sistema mientras ambos componentes estén funcionando.


\begin{align*}
P(T > t)=& P(\min{(T_{1},T_{2})} > t)\\         
         & \text{ como $\min{(T_{1},T_{2})}\sim exp(\lambda_{1}+\lambda_{2})$ }\\            =& e^{-(\lambda_{1}+\lambda_{2})t}
\end{align*}


En consecuencia, $T\sim exp(\lambda_{1}+\lambda_{2})$

## Demostración:

Sea $T=\min{(T_{1},T_{2})}$, entonces calculemos su confiabilidad:


\begin{align*}
P(T > t)=& P(\min{(T_{1},T_{2})} > t)\\        
        =& P(T_{1} > t,T_{2} > t)\\        
         & \text{ por independencia de $T_{1}$ y $T_{2}$ }\\        
        =& P(T_{1} > t)P(T_{2} > t)\\        =& e^{-\lambda_{1}t}e^{-\lambda_{2}t}\\         =& e^{-(\lambda_{1}+\lambda_{2})t}
\end{align*}


## Propiedad fuerte de pérdida de la memoria

Sean $T_{1}$ y $T_{2}$ dos v.a. exponenciales independientes con parámetros $\lambda_{1}$ y $\lambda_{2}$ respectivamente. Entonces,

$$
P\left(T_{2} > T_{1}+t\left|\right. T_{2} > T_{1}\right)=P\left(T_{2} > t\right)
$$

Observe que también puede escribirse de la siguiente manera:


\begin{align*}
P\left(T_{2}-T_{1} > t\left|\right.T_{2} > T_{1}\right)=&P\left(T_{2} > t\right)
\end{align*}


## Observaciones importantes:

Esto significa que la variable aleatoria

$$
T_{2} - T_{1}\left| \right. T_{2} > T_{1}  \sim exp(\lambda_{2})
$$

y además

$$
T_{2}-T_{1}\left|\right. T_{2} > T_{1}
$$

es una variable aleatoria independiente de $T_{1}$

## Demostración

Primero observemos que:


\begin{align*}
P\left(T_{2}-T_{1} > t\left|\right. T_{2} > T_{1}\right)
=&\frac{P(T_{2}-T_{1} > t, T_{2}-T_{1} > 0)}{P(T_{2} > T_{1})}\\
 &\text{ pues $\{T_{2}-T_{1} > t\} \subset  \{T_{2}-T_{1} > 0\}$ }\\                         =&\frac{P(T_{2}-T_{1} > t)}{P(T_{2} > T_{1})}\\       
 &\text{ por la probabilidad del primer fallo}\\      
=&\frac{P(T_{2}-T_{1} > t)}{\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}}\\
\end{align*}


## Continuación de la demostración:

Basta con calcular:


\begin{align*}
&P\left(T_{2}-T_{1} > t\right)\\
&= \int_{0}^{\infty}P\left(T_{2}-T_{1} > t\left|\right. T_{1}=x\right)f_{T_{1}}(x)dx\\
&= \int_{0}^{\infty}P\left(T_{2}-x > t\left|\right.T_{1}=x\right)f_{T_{1}}(x)dx\\&\text{ pues $T_{1}$ y $T_{2}$ son independientes}\\
&= \int_{0}^{\infty}P\left(T_{2} > t+x\right)f_{T_{1}}(x)dx\\
&= \int_{0}^{\infty}e^{-\lambda_{2}(t+x)}\lambda_{1}e^{-\lambda_{1}x}dx\\
&=\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}e^{-\lambda_{2}t}
\end{align*}


## Finalmente,


\begin{align*}
P\left(T_{2}-T_{1} > t\left|\right. T_2 > T_1\right)=&\frac{P\left(T_{2}-T_{1} > t\right)}{\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}}\\
                      =&\frac{\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}e^{-\lambda_{2}t}}{\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}}=e^{-\lambda_{2}t}\\
=&P\left(T_{2} > t\right)
\end{align*}


como queríamos demostrar.

## Supongamos que Sofía llega un tiempo exponencial después que Amanda

```{r}
#| echo: true

trials <- 5000
Amanda <- numeric(trials)
Sofia <- numeric(trials)
for (i in 1:trials) {
  s <- rexp(1, 1/10)          # Tiempo entre las llegadas de Amanda y Sofia
  bus <- rexp(1,1/30)         # Tiempo de llegada del bus
  Amanda[i] <- bus            # Tiempo de espera de Amanda
  while (bus < s) {
    bus <- bus + rexp(1,1/30) # Tiempos de llegadas de buses 
                              # hasta que llega Sofía
  }
  Sofia[i] <- bus-s           # Tiempo de espera de Sofía
}
mean(Amanda)
mean(Sofia)
```
## Miremos los histogramas

```{r}
par(mfrow=c(1,2))
hist(Amanda,xlab="",prob=T,ylab="",main="",yaxt="n")
mtext(1,text="Amanda")
axis(2,at=c(0,.01,.02),labels=c(0,0.01, 0.02))
hist(Sofia,xlab="",prob=T,ylab="",yaxt="n",main="")
mtext(1,text="Sofia")
axis(2,at=c(0,.01,.02),labels=c(0,0.01,0.02))
```
## ¿Qué sucede si Sofía llega una cantidad aleatoria de tiempo después que Amanda?

```{r}
#| echo: true

trials <- 5000
Amanda <- numeric(trials)
Sofia <- numeric(trials)
for (i in 1:trials) {
  s <- rnorm(1,30, 2)           # Tiempo entre las llegadas de Amanda y Sofia
  bus <- rexp(1,1/30)           # Tiempo de llegada del bus
  Amanda[i] <- bus              # Tiempo de espera de Amanda
  while (bus < s) {
    bus <- bus + rexp(1, 1/30)   # Tiempos de llegadas de buses 
                                # hasta que llega Sofía
  }
  Sofia[i] <- bus-s             # Tiempo de espera de Sofía
}
mean(Amanda)
mean(Sofia)
```
```{r}

par(mfrow=c(1,2))
hist(Amanda,xlab="",prob=T,ylab="",main="",yaxt="n")
mtext(1,text="Amanda")
axis(2,at=c(0,.01,.02),labels=c(0,0.01, 0.02))
hist(Sofia,xlab="",prob=T,ylab="",yaxt="n",main="")
mtext(1,text="Sofia")
axis(2,at=c(0,.01,.02),labels=c(0,0.01,0.02))

```

## Ejemplo:

**Considere un sistema de n componentes conectados en paralelo. Sea** $T_{i}=$ **el tiempo de vida del** $i$**-ésimo componente. Asuma que** $\{T_i, i=1,2, \ldots , n\}$ **son v.a. independientes e idénticamente distribuidas (iid)** $exp(\lambda)$**. Calcule el tiempo esperado de vida del sistema.**

## Solución:

Definamos las siguientes variables aleatorias:


\begin{align*}
&Z_{1}= \text{tiempo que 1er componente falle}\\
&Z_{2}= \text{tiempo que 2ndo componente falle}\\\\
&\vdots\\&Z_{n}= \text{tiempo que $n$-ésimo componente falle}\\\\
& \text{ Observe que:}\\&Z_{1}=min\{T_{1},T_{2},\ldots,T_{n}\}\sim \exp(n\lambda)\\
&Z_{n}=max\{T_{1},T_{2},\ldots,T_{n}\}
\end{align*}


La esperanza requerida es: $E(Z_{n})$.

## Continuando con el ejemplo:

Observemos que:


\begin{align*}
&E\left(Z_{1}\right)=\frac{1}{n\lambda}\\&Z_{2}-Z_{1} \sim exp((n-1)\lambda)\\
&E\left(Z_{2}-Z_{1}\right)=\frac{1}{(n-1)\lambda}\\
&E\left(Z_{2}-Z_{1}\right)=E(Z_{2})-E(Z_{1})\\&E\left(Z_{2}\right)= \frac{1}{(n-1)\lambda}+\frac{1}{n\lambda}
\end{align*}


pues $Z_{2}-Z_{1}$= es el mínimo de $n-1$ exponenciales independientes.

## Continuación del ejemplo

Análogamente,


\begin{align*}
&E\left(Z_{3}-Z_{2}\right)=\frac{1}{(n-2)\lambda}\\
&E\left(Z_{3}-Z_{2}\right)=E\left(Z_{3}\right)-E\left(Z_{2}\right)\\ &E\left(Z_{3}\right)=E\left(Z_{2}\right)+\frac{1}{(n-2)\lambda}\\
&E\left(Z_{3}\right)=\frac{1}{(n-2)\lambda}+ \frac{1}{(n-1)\lambda}+\frac{1}{n\lambda}\\
& \vdots\\
&\text{ un argumento inductivo permite concluir que}\\
&E\left(Z_{n}\right)=\sum_{k=1}^n \frac{1}{k\lambda}
\end{align*}


## Continuando con el ejemplo:

Lo que no queda claro es:

-   ¿Por qué $Z_{1},Z_{2}-Z_{1},Z_{3}-Z_{2},\ldots Z_{n}-Z_{n-1}$ son independientes?

La propiedad fuerte de pérdida de la memoria dice que

$$
P\left(Z_{2}-Z_{1} > x\left|\right. Z_{2} > Z_{1}\right) = P\left(Z_{2} > x\right)
$$

es decir que $Z_{2}-Z_{1}\left|\right. Z_{2} > Z_{1} \sim exp((n-1)\lambda)$ por lo que es independiente de $Z_{1}$

## Suma de exponenciales i.i.d.

Si $T_{1}, T_{2}, \cdots, T_{n}$ es una sucesión i.i.d. de variables aleatorias exponenciales parámetro $\lambda,$ entonces

$$
S_{n}=\sum_{k=1}^{n}T_{k} \sim Erlang(n,\lambda)=\Gamma(n,\lambda)
$$

## Ejemplo:

Los tiempos entre dos nacimientos sucesivos en un hospital de maternidad son iid $\sim\exp\left(1/\text{día}\right)$.

**¿Cuál es la probabilidad de que el décimo nacimiento en un año calendario tenga lugar después del 15 de enero?**

Sea

$T_{k}:\quad$ el tiempo transcurrido entre el nacimiento $k-1$ y el $k$

$$
S_{10}=\sum_{k=1}^{10}T_{k}
$$

es **el tiempo desde que abre el hospital de maternidad hasta que ocurre el décimo nacimiento**.

## Función de densidad de la Erlang

Diremos que $S_{n}\sim Erlan(n, \lambda)$ si su **función de densidad** viene dada por:

$$
f_{S_{n}}(t) = \begin{cases}\frac{\lambda e^{-\lambda t}(\lambda t)^{n-1}}{(n-1)!} & \text{si } t> 0 \\ 0 & \text{si } t\leq 0\end{cases}
$$

## Función de distribución de la Erlang

Diremos que $S_{n}\sim Erlan(n, \lambda)$ si su **función de distribución acumulada** viene dada por:

$$
P\left(S_{n} \leq t\right) = 1-\sum_{r=0}^{n-1} e^{-\lambda t} \frac{(\lambda t)^r}{r!}
$$

## Terminando de caracterizar a la Erlang

Su **esperanza, varianza y función generadora de momentos** vienen dadas por:


\begin{align*}
&E(S_{n}) = \frac{n}{\lambda}\\&Var(S_{n})=\frac{n}{\lambda^2}\\
&\Phi_{S_{n}}(t)= E\left(e^{S_{n}t}\right)  =\left(\frac{\lambda}{\lambda - t}\right)^n
\end{align*}


## La suma de exponenciales independientes se distribuye Erlang

Calculemos la función generadora de momentos de $S_{n}$


\begin{align*}
\Phi_{S_{n}}(t)&=E\left(e^{tS_{n}}\right)=E\left(e^{t\sum_{k=1}^n T_k}\right)\\                                    &=E\left(\prod_{k=1}^n e^{tT_k}\right)=\prod_{k=1}^n E\left(e^{tT_k}\right)\\ 
               &\text{ por independencia de $T_{1}, T_{2},\cdots T_{n}$}\\
               &=\prod_{k=1}^n \left(\frac{\lambda}{\lambda - t}\right)\\                                          &=\left(\frac{\lambda}{\lambda - t}\right)^n 
\end{align*}


## Solución del ejemplo de la maternidad:

La probabilidad requerida se puede calcular como:


\begin{align*}
P\left(\sum_{k=1}^{10} T_{k} > 15\right)=& P\left(S_{10}>15\right)\\\\
                                        =& 1-\left(1-\sum_{k=0}^{9} e^{-15} \frac{15^k}{k!}\right)\\\\
                                        =& \sum_{k=0}^{9} \frac{e^{-15} 15^k}{k!}
\end{align*}


## Suma de un número aleatorio de exponenciales i.i.d.

Sea


\begin{align*}
&\{T_n,n \geq1\} \text{ una sucesión i.i.d de v.a. $exp(\lambda)$ }\\
& N\sim Geo(p)\\&\text{ y entonces}\\ 
&S_{N}=\sum_{k=1}^{N} T_k \sim \exp(\lambda p )
\end{align*}


## Un poco de contexto: {.scrollable}

**Un refrigerador está sujeto a una serie de fallos eléctricos. Los tiempos entre dos fallos eléctricos consecutivos son v.a. i.i.d.** $exp (\lambda)$ **con media 10 hr. Cada fallo eléctrico tiene una probabilidad de 0.3 de malograr el refrigerador. Calcule la distribución del tiempo de vida útil de la refrigerador.**

Sea $N$ **el número de fallas eléctricas que el refrigerador resiste antes de malograrse**, entonces

$$P(N=k)=(0.7)^{k-1}(0.3) \text{ para }  k \geq 1$$

Sea $T_{i}$ = tiempo en horas entre la $i$-ésimo y la $(i-1)$-ésima falla eléctrica.

$$
T_{i} \sim \exp\left(\frac{1}{10}\right)
$$

## El tiempo de vida útil de la máquina:

Sea $T$ = **tiempo de vida útil del refrigerador en horas**

Observe que:

$$T=\sum_{i=1}^{N}T_{i}$$

Nos piden hallar la distribución del tiempo de vida útil de la máquina. Es decir, nos piden hallar

$$
\text{¿ }P(T\leq t)=\text{ ?}
$$

## Intentemos responder algunas preguntas:

¿Qué nos detiene de saber calcular $\Phi_{T}(t)$?

$$
\begin{align*}\Phi_{T}(t)=&E\left(e^{tT}\right)\\=&E\left(e^{t\sum_{i=1}^{N} T_i}\right)\\\end{align*}
$$

¿Será verdad que si $T_{1}, T_{2}, \cdots, T_{n}\sim \exp(\lambda)$ son independientes, entonces

$$
\text{ ¿ }E\left(e^{t\sum_{i=1}^{N} T_i}\Big|N=n\right)=\left(\frac{\lambda}{\lambda - t}\right)^n \text{ ?}
$$

## Más preguntas:

¿Es

$$E\left(e^{t\sum_{i=1}^{N} T_i}\Big|N=n\right)$$

una variable aleatoria?

¿Es

$$
E\left(e^{t\sum_{i=1}^{N} T_i}\Big|N\right)
$$

una variable aleatoria?

## Más preguntas:

Y si las pensamos así:

¿Es

$$
E\left(e^{t\sum_{i=1}^{N} T_i}\Big|N=n\right)= \left(\frac{\lambda}{\lambda - t}\right)^n
$$

una variable aleatoria?

¿Es

$$E\left(e^{t\sum_{i=1}^{N} T_i}\Big|N\right)=\left(\frac{\lambda}{\lambda - t}\right)^N$$

una variable aleatoria?

## y más preguntas:

Si efectivamente

$$
E\left(e^{t\sum_{i=1}^{N} T_i}\Big|N\right)=\left(\frac{\lambda}{\lambda - t}\right)^N
$$

¿cómo calcularíamos

$$
E\left[E\left(e^{t\sum_{i=1}^{N} T_i}\Big|N\right)\right]=E\left[\left(\frac{\lambda}{\lambda - t}\right)^N\right] ?
$$

## Observe que:

el valor esperado

$$
E\left(e^{t\sum_{i=1}^{N} T_i}\Big|N=n\right)=\left(\frac{\lambda}{\lambda - t}\right)^{n}
$$

se calculó con respecto a la densidad del vector aleatorio $(T_{1},T_{2},\cdots, T_{N})\Big|N=n$ cuya densidad es $Erlang(n,\lambda)$

## Observe también que:

el valor esperado

$$
E\left[E\left(e^{t\sum_{i=1}^{N} T_i}\Big|N\right)\right]=E\left[\left(\frac{\lambda}{\lambda - t}\right)^{N}\right]
$$

se debe calcular con respecto a la función de probabilidad de masa de la variable aleatoria $N\sim Geo(p)$.

## Finalmente: {.scrollable}


\begin{align*}
\Phi_{T}(t)=&E\left(e^{tT}\right)\\=&E\left(e^{t\sum_{i=1}^{N} T_i}\right)\\
           =&E\left[E\left(e^{t\sum_{i=1}^N X_i}|N\right)\right]\\
           =&E\left[\left(\frac{\lambda}{\lambda - t}\right)^N\right]\\
           =&\sum_{n=1}^{+\infty}\left(\frac{\lambda}{\lambda - t}\right)^n P(N=n)\\
           =&\sum_{n=1}^{+\infty}\left(\frac{\lambda}{\lambda - t}\right)^n (1-p)^{n-1} p\\
           =&\frac{\lambda p}{\lambda p-t}
\end{align*}


en donde nuevamente estaríamos invocando la serie geométrica

$$
\sum_{n=1}^{\infty}r^{n}=\frac{r}{1-r}$ cuando $|r| < 1$ con $r=\frac{\lambda(1-p)}{\lambda-t}
$$

## Propiedad Torre de la Esperanza Condicional

La usamos aquí:

$$
E\left(e^{t\sum_{i=1}^{N} T_i}\right)\\=E\left[E\left(e^{t\sum_{i=1}^N X_i}|N\right)\right]
$$

Y se enuncia formalmente así:

$$E(X)=E[E(X|Y)]$$

Yo prefiero recordarla así:

$$E_{X}(X)=E_{Y}\left[E_{X|Y}\left(X|Y\right)\right]$$

## Volviendo al tiempo de vida útil de la máquina:

Sabemos que $T\sim\exp(\lambda p)$. Es decir,

$$T \sim exp ((0.3)(0.1)) = exp (0.03)$$

**El tiempo de vida útil está exponencialmente distribuido con media de 33.33 hr.**

## ¿Qué aprendimos hoy?

## Material complementario no evaluado

-   Definir y utilizar la **función generadora de momentos** como herramienta para caracterizar la suma de variables aleatorias independientes.

## Función generadora de momentos

Se define por:


\begin{align*}
\Phi(t)=& \text{E}(e^{tX})\\\\
       =&\begin{cases}\int_{\mathbb{R}} e^{tx}f_{X}(x)dx & \text{ $X$ continua}\\\\
       \sum_{k\geq 0}e^{tk}P(X=k) & \text{ $X$ discreta }
         \end{cases}
\end{align*}


## ¿Para qué sirve la función generadora de momentos?

-   Para **caracterizar una variable aleatoria** dada.

-   Para **obtener los momentos de orden** $k$ **de una variable aleatoria** dada. Es decir, para calcular $E(X^{k})$ para $k=1,2,\cdots$

-   Para **caracterizar la distribución de la suma de variables aleatorias independientes e idénticamente distribuidas**.

## Función generadora exponencial:

Si $X\sim \exp(\lambda)$ entonces su **función generadora de momentos** se calcula así:


\begin{align*}
\Phi(t)=& \text{E}(e^{tx})\\=& \int_{0}^{\infty} e^{tx}\lambda e^{-\lambda x}dx\\
       =& \lambda \int_{0}^{\infty}e^{-(\lambda-t) x}dx\\
       =& \frac{\lambda}{\lambda - t}
\end{align*}


siempre que $t < \lambda$.

**La función generadora de momentos caracteriza a la variable aleatoria.**

## Función generadora de la geométrica

Si $X\sim Geo(p)$, su **función generadora de momentos** viene dada por:

$$
\begin{align*}\Phi(t)=& \text{E}(e^{tx})= \sum_{k=1}^{\infty}e^{tk}P(X=k)\\=& \sum_{k=1}^{\infty}e^{tk}(1-p)^{k-1}p\\=&\frac{p}{1-p}\sum_{k=1}^{\infty}\left(e^{t}(1-p)\right)^{k}\\=& \frac{pe^{t}}{1-e^{t}(1-p)}\\\end{align*}
$$

en donde usamos que $\sum_{k=1}^{\infty}r^{k}=\frac{r}{1-r}$ siempre que $|r| < 1$.

## Función generadora de momento de la geométrica:

$$
\begin{align*}\Phi(t)=& \frac{pe^{t}}{1-e^{t}(1-p)}\\\end{align*}
$$

Siempre que $\quad e^{t}(1-p) < 1\quad$. Es decir, siempre que:

$$t < -ln(1-p)$$

## Función generadora de la Poisson {.scrollable}

Si $X\sim Poison(\lambda)$, su **función generadora de momentos** viene dada por:


\begin{align*}\Phi(t)=& \text{E}(e^{tx})= \sum_{k=0}^{\infty}e^{tk}P(X=k)\\
                     =& \sum_{k=0}^{\infty}e^{tk}e^{-\lambda}\frac{\lambda^{k}}{k!}\\
                     =& e^{-\lambda}\sum_{k=0}^{\infty}\frac{\left(e^{t}\lambda\right)^{k}}{k!}=e^{-\lambda\left(1-e^{t}\right)}\\
\end{align*}


En donde hemos usado que:

$$\sum_{k=0}^{\infty}\frac{z^{k}}{k!}=e^{z}\quad \forall z\in \mathbb{R}$$

## ¿Cómo genera momentos?

Recordemos la expansión en series de Taylor de la función exponencial:


\begin{align*}
&e^{x}=\sum_{k=0}^{\infty}\frac{x^{k}}{k!}\\
&e^{tX}=\sum_{k=0}^{\infty}\frac{(tX)^{k}}{k!}
\end{align*}


## Continuando con los momentos: {.scrollable}

Entonces:


\begin{align*}
\Phi(t)=&E\left(e^{tX}\right)\\       
       =&E\left(\sum_{k=0}^{\infty}\frac{(tX)^{k}}{k!}\right)\\                                            =&\sum_{k=0}^{\infty}t^{k}\frac{E\left[X^{k}\right]}{k!}\\
        &\frac{d\Phi(t)}{dt}=\sum_{k=1}^{\infty}kt^{k-1}\frac{E\left[X^{k}\right]}{k!}\\
        &\frac{d\Phi(t)}{dt}\Big|_{t=0}=E(X)\\
\end{align*}


## Un argumento inductivo demuestra que:

La función generadora de momentos permite **calcular los momentos de orden** $k$ de una variable aleatoria dada, utilizando la siguiente fórmula:

$$\frac{d^{k}\Phi(t)}{dt^{k}}\Big|_{t=0}=E\left(X^{k}\right)$$

## Generando el primer momento de la exponencial

Sabemos que si $X\sim \exp(\lambda)$, entonces su función generadora de momentos es:


\begin{align*}
&\Phi(t)=\frac{\lambda}{\lambda - t}\\&\frac{d\Phi(t)}{dt}=\frac{d}{dt}\left(\frac{\lambda}{\lambda -t}\right)= \frac{\lambda}{(\lambda -t)^{2}}\\&\frac{d\Phi(t)}{dt}\Big|_{t=0}=\frac{\lambda}{(\lambda -t)^{2}}\Big|_{t=0}=\frac{1}{\lambda}=E(X)
\end{align*}


## La función generadora de una suma es:


\begin{align*}
\Phi_{S_{n}}(t)&=E\left(e^{tS_{n}}\right)=E\left(e^{t\sum_{k=1}^n T_k}\right)\\                                    &=E\left(\prod_{k=1}^n e^{tT_k}\right)=\prod_{k=1}^n E\left(e^{tT_k}\right)\\
               &\text{ por independencia de $T_{1}, T_{2},\cdots T_{n}$}\\&=\prod_{k=1}^n \Phi_{T_{k}}(t)\\
               & \text{ como son indénticamente distribuídas }\\
               &=\left(\Phi_{T}(t)\right)^n
\end{align*}


el producto de las funciones generadoras de los sumandos

## ¿Qué aprendimos hoy?

## Función de riesgo

Sea $X$ una variable aleatoria continua con función de densidad $f$. **La función de riesgo**, $r$ de $X$ está definida como:

$$r(x)=\frac{f(x)}{P(X>x)}$$

## Intuitivamente:

Recordar que


\begin{align*}
f(x)\equiv   & \lim_{\Delta x \rightarrow  0} \frac{P(x < X \leq x+ \Delta x)}{\Delta x}\\
r(x)\Delta x=& \frac{f(x) \Delta x}{P(X > x)}\\\\
\approx      & \frac{P(x < X \leq x+ \Delta x)}{P(X > x)}\\\\           
            =& P\left(X \in (x,x+ \Delta x] \left| X > x \right.\right)
\end{align*}


## Intuitivamente:

Por lo tanto, $r(x) \Delta x$ es la probabilidad condicional de que una máquina con vida útil $X$ falle en el intervalo $(x,x+ \Delta x]$ dado que ha durado más que $x$ unidades de tiempo.

## La función de riesgo de la exponencial

Si $X\sim exp(\lambda)$, su **función de riesgo** es:


\begin{align*}r(x)=&\frac{f(x)}{P(X>x)}\\
=&\frac{\lambda e^{-\lambda x}}{e^{-\lambda x}}\\    
=&\lambda
\end{align*}


La v.a. exponencial tiene una **función de riesgo constante**.

## Intuitivamente:

-   El hecho de que la función de riesgo de la exponencial sea constante es compatible con la propiedad de pérdida de la memoria.

-   La propiedad de pérdida de la memoria especifica que la probabilidad de que la máquina falle en $(x,x+ \Delta x]$ dado que la máquina sigue funcionando a tiempo $x$, es independiente de $x$.

## La función de riesgo caracteriza a la variable aleatoria:

$$P(X > x)=exp\left(-\int_0^xr(u)du\right)$$

## Demostración:

Sea $H(x)\equiv P(X > x) = 1-F(x)$ de la siguiente manera:


\begin{align*} 
&H(x)=P(X>x)=1-F(x)\\ 
&H'(x)=-f(x)=-r(x)H(x)\\
&\frac{H'(x)}{H(x)}=-r(x)\\
&\text{ integrando a ambos lados }\\
&\log(H(x)) =-\int_0^x r(u)du\\
& \text{ tomando exponenciales a ambos lados}\\
&H(x)= P(X > x)= exp\left(-\int_0^x r(u)du\right)
\end {align*}


como queríamos demostrar.

## En el caso exponencial

Como en el caso de $X\sim exp(\lambda)$, tenemos que su función de riesgo es constante. Es decir, $r(x)=\lambda$. Por lo tanto,


\begin{align*}
P(X > x)=& exp\left(-\int_0^x r(u)du\right)\\        
=& exp\left(-\int_0^x \lambda du\right)\\        
=& exp(-\lambda x)
\end{align*}


que coincide con la confiabilidad de una variable aleatoria $X\sim exp(\lambda)$. **Hemos caracterizado la variable aleatoria exponencial con la función riesgo.**
