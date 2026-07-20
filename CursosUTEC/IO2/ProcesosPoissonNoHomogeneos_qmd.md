---
curso: IO2
titulo: ProcesosPoissonNoHomogeneos
slides: 0
fuente: ProcesosPoissonNoHomogeneos.qmd
---

---
title: "Procesos de Poisson no homogéneos, compuestos y condicionales" 
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.jpg
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
      transition: slide
editor: visual
date: "Mayo 2025"
---

## Objetivos generales: Introducción a los Procesos de Poisson No-Homogéneos

-   **Enunciar, distinguir y demostrar** la equivalencia de las dos definiciones de los procesos de Poisson no- homogéneos, la operativa y la validadora.

-   Entender las **semejanzas y las diferencias** entre los procesos de Poisson Homogéneos y los No-Homogéneos.

-   **Ejemplificar y aplicar** dicho modelo en situaciones propias de las operaciones de ingeniería industrial.

## Definición Validadora PPNH

Diremos que el proceso de conteo $\{N(t), t \geq 0\}$ es un **Proceso de Poisson No-Homogéneo** con **tasa dependiente del tiempo** $\lambda(t)$ para $t\geq 0$

$$
\begin{align*}&\text{1) }N(0) = 0\\&\text{2) }\{N(t), t \geq 0\} \text{ tiene incrementos independientes}\\&\text{3) } P(N(t+h)-N(t) = 1) = \lambda(t)h + o(h)\\&\text{4) } P(N(t+h)-N(t) \geq 2) = o(h)\end{align*}
$$

## Función de intensidad de un PPNH

Se puede probar que si definimos la función de intensidad de un PPNH con tasa de llegada $\lambda(s)$ para todo $s\geq 0$

$$
\begin{align*}&m(t)\equiv\int_{0}^{t} \lambda(s)ds\\&\text{entonces}\\&P(N(t+s)-N(t) = n) = e^{-\left[m(t+s)-m(t)\right]} \frac{\left[m(t+s)-m(t)\right]^n}{n!}\end{align*}
$$

para todo $n\geq 0$.

## Definición operativa de PPNH

Diremos que el proceso de conteo $\{N(t), t \geq 0\}$ es un **Proceso de Poisson No-Homogéneo** con tasa dependiente del tiempo $\lambda(t)$ para $t\geq 0$

$$
\begin{align*}&\text{1) }N(0) = 0\\\\&\text{2) }\{N(t), t \geq 0\} \text{ tiene incrementos independientes}\\\\&\text{3) } P\left[N(t+s)-N(t) = n\right] = e^{-\left[m(t+s)-m(t)\right]} \frac{\left[m(t+s)-m(t)\right]^n}{n!}\end{align*}
$$

para todo $n\geq 0$.

## Ejemplo:

Los clientes llegan a la cafetería de UTEC de acuerdo a un proceso de Poisson No-Homogéneo con tasa:

$$
\lambda(s)=\begin{cases}            3 &\text{ para } 0\leq s < 4\\            3s+3  &\text{ para } 4\leq s < 8\\            36-3s & \text{ para } 8\leq s \leq 12           \end{cases}
$$

donde $s$ se mide en horas a partir de la apertura que ocurre a las 7:00 AM . ¿Cuál es la probabilidad de que lleguen exactamente 25 clientes entre las 11:00 y las 11:15 AM y cuatro clientes entre las 6:45 PM y las 7:00 PM?

## Gráficamente:

```{r, echo=FALSE}
lambda <- function(s){

  return(ifelse(s<4,3,ifelse(s<8,3*s+3,ifelse(s<12,36-3*s,0))))

}
```

```{r, echo=FALSE}
t <- seq(0, 18, by=0.1)

plot(t, lambda(t), type="l")

```

## Solución:

Nos piden calcular la siguiente probabilidad:

$$
\begin{align*}&P\left[N(4.25)-N(4)=25, N(12)-N(11,75)=4\right]\\&\text{ incrementos independientes }\\=&P\left[N(4.25)-N(4)=25\right]P\left[N(12)-N(11,75)=4\right]\\\end{align*}
$$

## Cuyas funciones de intensidad son respectivamente:

$$
\begin{align*}m(4.25)-m(4)=&\int_{4}^{4.25}\lambda(s)ds\\ =&\int_{4}^{4.25}(3s+3)ds\approx 3.84\\m(12)-m(11,75)=&\int_{11.75}^{12}\lambda(s)ds\\ =&\int_{11.75}^{12}(36-3s)ds\approx 0.09\\\\\end{align*}
$$

## Finalmente:

$$
\begin{align*}&P\left[N(4.25)-N(4)=25\right]=\frac{e^{-3.84}(3.84)^{25}}{25!}\\\\&P\left[N(12)-N(11,75)=4\right]= \frac{e^{-0.09}(0.09)^{4}}{4!}\\\\& \text{ la probabilidad requerida es: }\\\\&P\left[N(4.25)-N(4)=25, N(12)-N(11,75)=4\right]\\\\=&\frac{e^{-3.84}(3.84)^{25}}{25!}\frac{e^{-0.09}(0.09)^{4}}{4!}\end{align*}
$$

## Prueba:

La prueba es similar al caso de los Procesos de Poisson Homogéneos con una pequeña diferencia:

Fije $t$ y defina:

$$P_{0}(s)\equiv P\left(N(t+s)-N(t)=0\right)$$

Al igual que en el caso homogéneo, buscamos calcular:

$$\lim_{h\rightarrow 0}\frac{P_{0}(s+h)-P_{0}(s)}{h} = P´(s)$$

en el caso que dicho límite exista.

## Entonces:

$$
\begin{align*}&P_{0}(s+h)=P\left[N(t+s+h)-N(t)=0\right]\\\\           &= P\left[0 \text{ eventos en } (t,t+s], 0 \text{ eventos en } (t+s,t+s+h]\right]\\\\          &= P\left[0 \text{ eventos en } (t,t+s]\right] P\left[0 \text{ eventos en } (t+s,t+s+h]\right]\\\\           &= P_{0}(s)\left[1-P(\text{más de 1 evento en } (t+s,t+s+h]))\right]\\\\          =& P_{0}(s)\left[1-P(N(t+s+h)-N(t+s)=1)\right.\\          \quad & - \left. P(N(t+s+h)-N(t+s)\geq 2)\right] \\\\          &= P_{0}(s)\left[1-\lambda (t+s)h+o(h)\right]\end{align*}
$$

## Continuando con la prueba

De tal manera que,

$$\frac{P_{0}(s+h)-P_{0}(s)}{h} = -\lambda (t+s)P_{0}(s)+\frac{o(h)}{h}$$

Permitiendo que $h\rightarrow 0$

$$
\begin{align*}& P_{0}'(s) = -\lambda (t+s)P_{0}(s) \\\\& \frac{P_{0}'(s)}{P_{0}(s)}=-\lambda (t+s)\\\end{align*}
$$

## Resolviendo la ecuación diferencial

Integrando a ambos lados,

$$
\begin{align*}&\log\left[P_{0}(s)\right]= -\int_{0}^{s} \lambda(t+u)du\\&\text{haciendo el cambio de variable } v=t+u\\=& -\int_{t}^{t+s} \lambda(v)dv \\\\&\text{ tomando exponenciales a ambos lados}\\&P_{0}(s)\equiv P\left[N(t+s)-N(t)=0\right]= e^{-\left[m(t+s)-m(t)\right]}\end{align*}
$$

Con un argumento inductivo similar al del caso homogéneo se termina la prueba.

## Ejemplo en Teoría de colas

Proceso de salida de un $M/G/\infty$ es un PPNH con $\lambda (t) = \lambda G(t)$.

**Prueba:**

Primero probaremos que

1.  El número de salidas en $(s,s+t]$ es una v.a. poisson con media $\lambda \int_{s}^{s+t} G(y)dy$

2.  El número de salidas en intervalos de tiempo disjuntos son independientes.

## Prueba de a)

Diremos que una llegada es del tipo I si sale en el intervalo $(s,s+t]$. Entonces una llegada que ocurre a tiempo $y$ será de tipo I con probabilidad $\quad P(s < X \leq s+t)$

$$
P(y) = \begin{cases}G(s+t-y)-G(s-y) & \text{ si } y \leq s \\ G(s+t-y) & \text{ si } s < y \leq s+t \\0 & \text{ si } y > s+t\end{cases}
$$

## 

Por la proposición vista en clase, el número de salidas será Poisson con media

$$
\lambda \int_0^{s+t}p(y)dy\\= \lambda \int_{0}^{s} \left[G(s+t-y)-G(s-y)\right]dy\\\quad + \lambda \int_{s}^{s+t} G(s+t-y)dy\\= \lambda \int_{s}^{s+t} G(y)dy
$$

## Prueba de b)

Suponga que $I_1$ e $I_2$ son dos intervalos disjuntos. Llame una llegada de tipo I si sale en $I_1$, del tipo II si sale en $I_2$ y del tipo III si no. Por bipartición de Procesos de Poisson Homogéneos, el \# de eventos tipo I y II son v.a. Poisson independientes.

Por a. y b. el proceso de salida es un proceso de Poisson no-homogéneo

## Procesos de Poisson Compuestos

Un proceso estocástico $\{X(t),t\geq 0\}$ se dice que es un **Proceso de Poisson Compuesto** si se puede escribir $\forall \quad t \geq 0$ como

$$X(t)=\sum_{i=1}^{N(t)} X_{i}$$

donde $\{N(t),t\geq 0\}$ es un proceso de Poisson y $\{X_{i},i\geq 1\}$ es una sucesión de v.a. i.i.d. e independientes de $N(t)$

## Ejemplo:

Suponga que la llegada de familias de migrantes a Lima se puede modelar mediante un Proceso de Poisson con tasa $\lambda=2$ por semana. Si el número de personas en cada familia es independiente del tamaño de las otras familias y toma valores 1,2,3,4 con probabilidades $\frac{1}{6}$, $\frac{1}{3}$ , $\frac{1}{3}$ y $\frac{1}{6}$ respectivamente, entonces

¿Cuál es el número esperado de individuos que migran a Lima durante un

período de 5 semanas?

## Solución:

Sea $N(t)\sim Poisson(2t)$ el número de familias semanales que llegan a dicha región en $(0,t]$

Sea $Y_{i}$ el número de individuos de la familia $i$.

Sea $X(t)$ el número de individuos que migran hasta el instante $t$.

Claramente,

$$X(t)=\sum_{i=1}^{N(t)}Y_{i}$$

## Primero, usemos la propiedad de la torre,

$$E(X(t))=E\left[E\left(\sum_{i=1}^{N(t)}Y_{i}\Big|N(t)\right)\right]$$

En donde,

$$
E\left(\sum_{i=1}^{N(t)}Y_{i}\Big|N(t)=n\right)= nE(Y_{i})\\E\left(\sum_{i=1}^{N(t)}Y_{i}\Big|N(t)\right)= N(t)E(Y_{i})\\E(X(t))=E\left[N(t)E(Y_{i})\right]=2tE(Y_{i})\\
$$

## El valor esperado requerido es:

$$
\begin{align*} E[X(5)]=& 2(5)E[Y_{i}]\\        =& 10\left(1*\frac{1}{6}+2*\frac{1}{3}+3*\frac{1}{3}+4*\frac{1}{6}\right)\\        =& 25\end{align*}
$$

Entonces, el número esperado de individuos que migran en un periodo de 5 semanas será 25.

## Proceso de Poisson Condicional

Sea $\Lambda$ una v.a. positiva con distribución G, y sea $\{N(t),t\geq 0\}$ un proceso de conteo tal que, dado $\Lambda=\lambda, \{N(t),t\geq 0\}$ es un proceso de Poisson con parámetro $\lambda$. Entonces, por ejemplo,

$$P(N(t+s)-N(s)=n)=\int_0^{+\infty} e^{-\lambda t} \frac{(\lambda t)^n}{n!} dG(\lambda)$$

$\{N(t), t\geq 0 \}$ es un Proceso de Poisson Condicional.

Note que $\{N(t),t\geq 0\}$ no es un proceso de Poisson. De hecho, tiene incrementos estacionarios pero no son independientes. ¿Por qué?

## Ejemplo Procesos de Poisson Condicionales

En años buenos, las tormentas ocurren siguiendo un Proceso Poisson Homogéneo con tasa de 3 por año, mientras en años malos, las mismas ocurren siguiendo un Proceso de Poisson Homogéneo  con tasa de 5 por año. Suponga que las predicciones anuncian que el próximo año será un año bueno con una probabilidad del 30\%. Si $\{N(t): t\geq 0\}$ denota el número de tormentas que ocurrirán el próximo año durante el intervalo $(0,t]$.

Encuentre $P(N(t)=n)$

## Cálculo de $P(N=n)$

\begin{align*}
P(N=n)=&P(N=n|\Lambda=3)P(\Lambda=3)+P(N=n|\Lambda=5)P(\Lambda=5)\\
      =& \frac{e^{-3t}(3t)^{n}}{n!}.\frac{30}{100}+\frac{e^{-5t}(5t)^{n}}{n!}.\frac{70}{100}
\end{align*}

Por lo tanto el proceso de Poisson condicional no es un proceso de Poisson Homogéneo.


## ¿Tiene $\{N(t): t\geq 0\}$ incrementos independientes?

**Solución: **
Para ver si el PPCondicional tiene incrementos independientes tenemos que demostrar que 

\begin{align*}
&P(N(s_{1}+t_{1})-N(s_{1})=n,N(s_{2}+t_{2})-N(s_{2})=m)\\
=&P(N(s_{1}+t_{1})-N(s_{1})=n)P(N(s_{2}+t_{2})-N(s_{2})=m)
\end{align*}

## Calculemos el lado izquierdo primero:

\begin{align*}
&P\left(N(s_{1}+t_{1})-N(s_{1})=n,N(s_{2}+t_{2})-N(s_{2})=m\right)\\
=&P\left(N(s_{1}+t_{1})-N(s_{1})=n,N(s_{2}+t_{2})-N(s_{2})=m|\Lambda=3\right)P(\Lambda=3)\\
&+P\left(N(s_{1}+t_{1})-N(s_{1})=n, N(s_{2}+t_{2})-N(s_{2})=m|\Lambda=5\right)P(\Lambda=5)\\
&\text{ por la independencia de los incrementos de los PPH}\\
=&P\left(N(s_{1}+t_{1})-N(s_{1})=n|\Lambda=3\right)P\left(N(s_{2}+t_{2})-N(s_{2})=m|\Lambda=3\right)P(\Lambda=3)\\
&+P(N(s_{1}+t_{1})-N(s_{1})=n|\Lambda=5)P(N(s_{2}+t_{2})-N(s_{2})=m|\lambda=5)P(\Lambda=5)\\
&\text{por la estacionariedad de los incrementos de los PPH}\\
=&P(N(t_{1})=n|\Lambda=3)P(N(t_{2})=m|\Lambda=3)P(\Lambda=3)\\
&+P(N(t_{1})=n|\Lambda=5)P(N(t_{2})=m|\Lambda=5)P(\Lambda=5)\\
=&\frac{e^{-3t_{1}}(3t_{1})^{n}}{n!}\frac{e^{-3t_{2}}(3t_{2})^{m}}{m!}\frac{30}{100}\\
&+\frac{e^{-5t_{1}}(5t_{1})^{n}}{n!}\frac{e^{-5t_{2}}(5t_{2})^{m}}{m!}\frac{70}{100}\\
\end{align*}

## Calculemos ahora el lado derecho

\begin{align*}
&P\left(N(s_{1}+t_{1})-N(s_{1})=n\right)P\left(N(s_{2}+t_{2})-N(s_{2})=m\right)\\\\
=& \left[P\left(N(s_{1}+t_{1})-N(s_{1})=n|\Lambda=3\right)P(\Lambda=3)+P\left(N(s_{1}+t_{1})-N(s_{1})=n|\Lambda=5\right)P(\Lambda=5)\right]\\
&\times \left[P\left(N(s_{2}+t_{2})-N(s_{2})=m|\Lambda=3\right)P(\Lambda=3)+P\left(N(s_{2}+t_{2})-N(s_{2})=m|\Lambda=5\right)P(\Lambda=5)\right]\\\\
=&\left[\frac{e^{-3t_{1}}(3t_{1})^{n}}{n!}\frac{30}{100}+\frac{e^{-5t_{1}}(5t_{1})^{n}}{n!}\frac{70}{100}\right]\times
\left[\frac{e^{-3t_{2}}(5t_{2})^{m}}{m!}\frac{30}{100}+\frac{e^{-5t_{2}}(5t_{2})^{m}}{m!}\frac{70}{100}\right]\\
\end{align*}

Como el lado derecho no es igual al izquierdo, queda claro que **los incrementos construídos sobre intervalos de tiempos disjuntos ya no son independientes en el caso del Proceso de Poisson Condicional.**

## ¿Los incrementos de un proceso de Poisson condicional $\{N(t): t\geq 0\}$ son estacionarios?

**Solución:**

Tenemos que ver si $P(N(t+s)-N(s)=n)=P(N(t)=n) \quad \forall s,t\geq 0 \forall n\in\mathbb{N}$

Veamos,

\begin{align*}
P(N(t+s)-N(s)=n)=&P\left(N(t+s)-N(s)=n|\Lambda=3\right)P(\Lambda=3)+P\left(N(t+s)-N(s)=n|\Lambda=5\right)P(\Lambda=5)\\
                 & \text{como } \{N(t)|\Lmabda=\lambda, t\geq 0\} \text{es un proceso de PPH}\\
                 &=P\left(N(t)=n|\Lambda=3\right)P(\Lambda=3)+P\left(N(t)=n|\Lambda=5\right)P(\Lambda=5)\\
                 &=\frac{e^{3t}(3t)^{n}}{n!}\frac{30}{100}+\frac{e^{5t}(5t)^{n}}{n!}\frac{70}{100}=P(N(t)=n)
\end{align*}

Por lo tanto, **los procesos de Poisson Condicionales si tienen incrementos estacionarios.** 

## Si el año pasado ocurrieron exactamente 3 tormentas, ¿Cuál es la probabilidad de que haya sido un buen año?

**Solución:**

Nos piden calcular, $P(\Lambda=3|N(1)=3)$.

\begin{align*}
P(\Lambda=3|N(1)=3)=&\frac{P(\Lambda=3,N(1)=3)}{P(N(1)=3)}\\
                   =& \frac{P(N(1)=3|\Lambda=3)P(\Lambda=3)}{P(N(1)=3|\Lambda=3)P(\Lambda=3)+P(N(1)=3|\Lambda=5)P(\Lambda=5)}\\
                   =& \frac{\frac{e^{3t}(3t)^{n}}{n!}\frac{30}{100}}{\frac{e^{3t}(3t)^{n}}{n!}\frac{30}{100}+\frac{e^{5t}(5t)^{n}}{n!}\frac{70}{100}}
\end{align*}



## Ejemplo: Examen 2024-1

El restaurante italiano La Ruota se ha hecho muy famoso en Lima a razón de sus conocidos gnocchis alla ruota. Pasta artesanal a base de la mejor papa peruana hecha con la receta secreta de la familia Antonini y terminada de preparar dentro de una rueda gigante de queso parmesano Reggiano de unos 40 kg de peso y unos 60 cm de diámetro en cuyo interior se vierte vino blanco de la mejor calidad posible, se enciende con fuego para hacer que el queso comience a derretirse, momento en el cual se agrega la pasta de su elección, previamente cocinada dentro de una salsa a base de mantequilla, ajo, crema de leche y nuez moscada. Finalmente, raspando el fondo del queso derretido con una cuchara, se envuelve la pasta con el queso y se sirve a los comensales.  

La pasta alla ruota tiene sus orígenes en el norte de Italia, en la región de Lombardía. Se cree que los pastores de la región inventaron esta técnica mientras pastoreaban sus rebaños en los Alpes italianos. La técnica consistía en calentar el queso en una rueda y luego cocinar la pasta en el interior, de esta manera se creaba una pasta cremosa y deliciosa con un sabor a queso inigualable.

Por lo tanto, se trata una experiencia culinaria única que no se encuentra en muchos lugares. Una forma divertida y deliciosa de disfrutar de la pasta y el queso de una manera diferente. Es por esto que la familia Antonini, dueña del restaurante, no puede permitirse el lujo de quedarse sin queso parmesano.

## Continuación del caso


En el restaurante la Ruota se ha estimado que las ruedas de queso parmesano reggiano tienen una demanda promedio de 14 unidades por año y la misma cumple con las suposiciones de un modelo de Poisson homogéneo. El inventario de las ruedas de queso parmesano es manejado siguiendo una política que depende de los siguientes procesos:

\begin{align*}
&I(t)= \text{ número de ruedas de queso parmesano en inventario a tiempo } t\\
&IQ(t)= \text{ ruedas de queso parmesano ordenadas pero todavía en tránsito a tiempo } t\\
& \text{Finalmente, la posición de inventario a tiempo } t \text{ se define como:}\\
& IP(t)≡I(t)+IQ(t)\\
\end{align*}


## Continuación del caso 

Como política de inventario, la familia Antonini ha decidido, con base en su conocimiento previo, que cada vez que $IP(t)\leq 3$, se ordenen 4 ruedas de queso parmesano. Esta política toma en cuenta tanto la demanda como el tiempo que el proveedor actual tarda exactamenteen traer las ruedas de queso al restaurante que es 45 días además de la capacidad limitada de la refrigeradora.
 
Cada rueda de Parmigiano Reggiano DOC de 40kg tiene un costo de \S 4760 soles. Los expertos en queso parmesano recomiendan que lo guardes en el refrigerador ya sea antes o después de abierto, porque así te puede durar hasta 8 semanas e incluso en los mejores casos hasta 6 meses de ser conservado a una temperatura estable entre los 4°C y lo 8°C. Es por esto que el costo de mantener una rueda de queso parmesano en inventario por un mes es de alrededor de \S 30. 


## Pregunta 1A)

 Al abrir el restaurante La Ruota, la Chef Claudia quiso tomar la precaución de arrancar con 10 ruedas de queso parmesano en la refrigeradora. ¿Cuál es la probabilidad de que en menos de dos meses el restaurante La Ruota tenga que hacer un pedido para reabastecerce de ruedas de queso parmesano?

## Solución 1A)

Sea $D(t)$ el número de ruedas de queso parmesano que el restaurante consume en el intervalo $(0,t]$ con $t$. Sabemos que $D(t)∼Poisson(14t)$ con el tiempo medido en años. Como el inventario en estos momentos es de 10 ruedas de queso parmesano, podemos asumir que no hay ruedas de queso parmesano en tránsito. Por lo tanto, la probabilidad requerida es:

\begin{align*}
P\left(D\left(\frac{2}{12}\right)\geq 7\right)&=\sum_{k=7}^{\infty}e^{14\frac{2}{12}}\frac{[14\frac{2}{12}]^{k}}{k!}
\end{align*}

Haciendo el cálculo en R:

```{r, echo=TRUE}
ppois(6,lambda =7/3, lower.tail=FALSE)
```

## Pregunta 1B)

Al abrir el restaurante La Ruota, la Chef Claudia tomó el riesgo y la precaución de arrancar con 10 ruedas de queso parmesano en la refrigeradora para asegurar tener suficiente mientras aprende más de la demanda real del restaurante.
¿Cuál es la probabilidad de que no se le malogre ninguna rueda de queso parmesano? Puede asumir que las condiciones de frío son impecables tanto en el traslado de la ruedas desde su lugar de origen en Italia hasta el restaurante y también en la refrigeradora del restaurante La Ruota.

## Solución 1B)

\begin{align*}
P\left(D\left(\frac{1}{2}\right)\geq 10\right)&=\sum_{k=10}^{\infty}e^{14.\frac{1}{2}}\frac{[14.\frac{1}{2}]^{k}}{k!}
\end{align*}

```{r, echo=TRUE}
ppois(9,lambda =7, lower.tail=FALSE)
```

## Pregunta 2A)

Si en 6 meses a partir de ahora que se cuenta con 10 ruedas de queso parmesano en stock, el restaurante ha consumido exactamente 7 ruedas de queso parmesano y emite una orden de reabastecimiento, pero esta vez con un proveedor nuevo que ofrece un  tiempo de reabastecimiento de exactamente 1 mes. Calcule la probabilidad de que el restaurante no se quede sin ruedas de queso parmesano antes de ser reabastecido. 

## Solución 2A)

Sea $S_{k}=$ el momento en el tiempo desde que abre el restaurante con 10 ruedas de queso hasta que se acabe la késima rueda de queso parmesano. 

\begin{align*}
&P\left(S_{10}>\frac{1}{12} \right|\left.D\left(\frac{1}{2}\right)=7\right)=P\left(S_{3}>\frac{1}{12}\right)\\
&\text{ en vista que podemos reiniciar el reloj después de consumir la séptima rueda }\\
&\text{ porque el tiempo hasta que se consuma la proxima rueda es exponencial(14)}\\
& \text{ y la misma satisface la propiedad de pérdida de la memoria }\\
&=P\left(D\left(\frac{1}{12}\right)\leq 2\right)\\
&=\sum_{k=0}^{2}e^{14\frac{1}{12}}\frac{[14\frac{1}{12}]^{k}}{k!}
\end{align*}

Calculando la cuenta en R:

```{r, echo=TRUE}
ppois(2,lambda =7/6)
```

## Pregunta 2B)

Si en 6 meses a partir de ahora que se cuenta con 10 ruedas de queso parmesano en stock, el restaurante ha consumido exactamente 7 ruedas de queso parmesano y emite una orden de reabastecimiento, pero esta vez con un proveedor nuevo que ofrece un  tiempo de reabastecimiento de exactamente 1 mes. Calcule tiempo esperado hasta que el restaurante se acabe la décima rueda de queso parmesano.  

## Solución 2B)

Sea $S_{k}=$ el momento en el tiempo desde que abre el restaurante con 10 ruedas de queso hasta que se acaba la késima rueda de queso parmesano. 

\begin{align*}
E\left(S_{10}\left|D\left(\frac{1}{2}\right)=7\right.\right)&= \frac{1}{2}+E\left(S_{3}\right)\\
            &= \frac{1}{2}+\frac{3}{14}= 0.7142857
\end{align*}


Calculando la cuenta en R:

```{r, echo=TRUE}
1/2 +3/14
```

## Pregunta 3A)

Si en sus primeros 6 meses de funcionamiento, el restaurante ha consumido exactamente 7 ruedas de queso parmesano de las 10 con las que comenzó y emite una orden de reabastecimiento, pero esta vez, con un proveedor nuevo que ofrece un tiempo de reabastecimiento aleatorio distribuido exponencialmente con una media de 1 mes. ¿cuál es la probabilidad de que se quede sin ruedas de queso parmesano antes que se pueda reabastecer?

## Solución 3A)

Como una vez emitida la orden de reabastecimiento, la misma tarda un tiempo en años $T\sim exp(12)$ en entrar al inventario, la probabilidad requerida es la probabilidad de que el restaurante consuma las 3 ruedas de queso parmesano que le quedan en inventario antes de ser reabastecido. Es decir la probabilidad requerida es:

\begin{align*}
P\left(S_{3}<T\right)&=\int_{0}^{\infty}P\left(S_{3}< T\right|\left.T=t\right)f_{T}(t)dt\\
&= \int_{0}^{\infty}P\left(S_{3}< t\right|\left.T=t\right)12e^{-12t}dt\\
& \text{ como } T \text{ y } S_{3} \text{ son v.a. independientes }\\
&= \int_{0}^{\infty}P\left(S_{3}< t\right)12e^{-12t}dt\\
&= \int_{0}^{\infty}P\left(D(t)\geq 3\right)12e^{-12t}dt\\
&= \int_{0}^{\infty}\sum_{k=3}^{\infty}e^{-14t}\frac{[14t]^{k}}{k!}12e^{-12t}dt= 0.156122
\end{align*}

## Calculando la integral en R,

```{r, echo=TRUE}
integrand <- function(t) {dexp(t, rate = 12)*ppois(2, lambda=14*t, lower.tail = FALSE)}
integrate(integrand,lower=0,upper=Inf)
```
O también:

```{r, echo=TRUE}
integrand <- function(t) {dexp(t, rate = 1)*ppois(2, lambda = (7*t)/6, lower.tail = FALSE)}
integrate(integrand,lower=0,upper=Inf)
```

## Pregunta 3B)

Si en sus primeros 6 meses de funcionamiento, el restaurante ha consumido exactamente 7 ruedas de queso parmesano de las 10 con las que comenzó y emite una orden de reabastecimiento, pero esta vez, con un proveedor nuevo que ofrece un tiempo de reabastecimiento aleatorio que varía uniformemente entre 15 y 45 días. ¿cuál es la probabilidad de que se quede sin ruedas de queso parmesano antes que se pueda reabastecer?

## Solución 3B) 

Como una vez emitida la orden de reabastecimiento, la misma tarda un tiempo en años $T\sim Unif\left(\frac{1}{24}, \frac{3}{24}\right)$ en entrar al inventario, la probabilidad requerida es la probabilidad de que el restaurante consuma las 3 ruedas de queso parmesano que le quedan en inventario antes de ser reabastecido. Es decir la probabilidad requerida es:

\begin{align*}
P\left(S_{3}<T\right)&=\int_{\frac{1}{24}}^{\frac{3}{24}}P\left(S_{3}< T\right|\left.T=t\right)f_{T}(t)dt\\
&= \int_{\frac{1}{24}}^{\frac{3}{24}}P\left(S_{3}< t\right|\left.T=t\right)\frac{1}{\frac{3}{24}-\frac{1}{24}}dt\\
& \text{ como } T \text{ y } S_{3} \text{ son v.a. independientes }\\
&= \int_{\frac{1}{24}}^{\frac{3}{24}}P\left(S_{3}< t\right)12dt\\
&=12 \int_{\frac{1}{24}}^{\frac{3}{24}}P\left(D(t)\geq 3\right)dt\\
&=12\int_{\frac{1}{24}}^{\frac{3}{24}}\sum_{k=3}^{\infty}e^{-14t}\frac{[14t]^{k}}{k!}dt=0.1218846 
\end{align*}

## Calculando la integral en R,

```{r, echo=TRUE}
integrand <- function(t) {dunif(t, min = 1/24,max =3/24 )*ppois(2, 14*t, lower.tail = FALSE)}
integrate(integrand,lower=1/24,upper=3/24)
```

## Pregunta 4A)

Suponga que en estos momentos que $I(t)=1$ e $IQ(t)=4$. Asuma que el restaurante ordenó una reposición de inventario cuando se percató que estaba abriendo una de las 3 ruedas de parmesano que quedaban en inventario. Sin embargo, no recuerda cuando eso ocurrió. Asumiendo que el restaurante solicitó la reposición de inventario al proveedor que ofrece un leadtime exponencialmente distribuido con media de 1 mes. Calcule la probabilidad de que la reposición ocurra antes de se termine la rueda de queso parmesano en uso. 

## Solución 4A)

Por la Propiedad fuerte de pérdida de la memoria, aunque no sepamos cuándo se hizo la orden de reposición, si sabemos que el tiempo que queda hasta que la reposición ocurra, $T_{R}$ es una variable aleatoria exponencial con tasa $12$ por año. Igualmente, el tiempo $T_{Q}$ desde que se abre la última rueda de parmesano que aún queda en inventario hasta que se acaba, también, por la propiedad fuerte de pérdida de la memoria es una variable aleatoria exponencial con tasa $14$ por año independientemente de que sepamos cuando se abrió. Por lo tanto, la probabilidad requerida es:

\begin{align*}
P\left(T_{R} < T_{Q}\right)&= \frac{12}{12+14}=\frac{6}{13}=0.4615385\\
& \text{ por la propiedad del primer fallo}\\
& \text{ y el hecho que } T_{R} \text{ y } T_{Q} \text{ son v.a. independientes}\\
\end{align*}

```{r, echo=TRUE}
6/13

```


## Pregunta 4B)


Suponga que en estos momentos que $I(t)=1$ e $IQ(t)=4$. Asuma que el restaurante ordenó una reposición de inventario cuando se percató que estaba abriendo una de las 3 ruedas de parmesano que quedaban en inventario. Sin embargo, no recuerda cuando eso ocurrió. Asumiendo que el restaurante solicitó la reposición de inventario al proveedor que ofrece un leadtime exponencialmente distribuido con media de 1 mes. Calcule el valor esperado del tiempo mínimo entre el tiempo de reposición y el tiempo hasta que se termine la rueda de parmesano que está en uso actualmente.

## Solución 4B)

Por la Propiedad fuerte de pérdida de la memoria, aunque no sepamos cuándo se hizo la orden de reposición, si sabemos que el tiempo que queda hasta que la reposición ocurra, $T_{R}$ es una variable aleatoria exponencial con tasa $12$ por año. Igualmente, el tiempo $T_{Q}$ desde que se abre la última rueda de parmesano que aún queda en inventario hasta que se acaba, también, por la propiedad fuerte de pérdida de la memoria es una variable aleatoria exponencial con tasa $14$ por año independientemente de que sepamos cuando se abrió. El valor esperado requerido es

\begin{align*}
E\left(\min{(T_{R},T_{Q})}\right)&=\frac{1}{12+14}=0.03846154 \text{ años.}\\ 
\end{align*}

```{r}
1/(12+14)
```


En vista que $\min{(T_{R},T_{Q})}\sim exp(12+14)$ siempre que $T_{R}$ y $T_{Q}$ sean variables aleatorias independientes como es el caso. 

## Pregunta 5A)

El restaurante La Ruota abre de lunes a domingo entre las 7:00 PM a 1:00 AM. Se conoce que los comensales llegan al restaurante en grupos de tamaño 1, 2, 4 y 6 personas con probabilidades respectivas de $\frac{1}{8}$, $\frac{1}{2}$, $\frac{1}{8}$ y $\frac{1}{4}$ siguiendo un Proceso de Poisson con una taza de llegada que comienza en 10 grupos por hora a las 7:00 PM y aumenta linealmente hasta 15 grupos por hora a las 9:00 PM, momento en el cual la tasa se llegada se mantiene constante hasta las 11:00PM. A las 11:00 PM la tasa de llegada de clientes comienza a descender de manera lineal desde 15 grupos por hora hasta 3 grupos por hora a la 1:00 AM. Dado que se conoce que entre las 8:00 PM y las 11:00 han llegado 15 grupos, calcule la probabilidad de que al menos 10 de esos grupos hayan llegado antes de las 10:00.

## Solución 5A) 

Claramente, la llegada de grupos al restaurante sigue un Proceso de Poisson no homogéneo. Es decir, definamos $N(t+s)-N(s)$ como el número de grupos que llegan al restaurante en un intervalo arbitrario $(s,s+t]$. Por lo que sabemos que 

$$
P\left(N(t+s)-N(s)=k\right)=e^{-[m(t+s)-m(s)]}\frac{\left[m(t+s)-m(s)\right]^{k}}{k!} \text{ para } k=0,1,\dots
$$
en donde $m(t)\equiv \int_{0}^{t}\lambda(u)du$

En este caso, la probabilidad requerida es:

\begin{align*}
P\left[N(3)-N(1)\geq 10\left|\right.N(4)-N(1)=15\right]&=\frac{P\left[N(3)-N(1)\geq 10 \text{ , } N(4)-N(1)=15\right]}{P\left[N(4)-N(1)=15\right]}\\\\
& \text{ disjuntizando para lograr independencia de los incrementos}\\\\
&= \frac{\sum_{k=10}^{15}P\left[N(3)-N(1)=k \text{ , }N(4)-N(3)=15-k\right]}{P\left[N(4)-N(1)=15\right]}\\
&= \frac{\sum_{k=10}^{15}P\left[N(3)-N(1)=k\right] P\left[N(4)-N(3)=15-k\right]}{P\left[N(4)-N(1)=15\right]}
\end{align*}


## Calculemos las intensidades:

\begin{align*}
&m(3)-m(1)=\int_{1}^{3}\lambda(u)du=\int_{1}^{2}\left(10+\frac{5}{2}u\right)du+\int_{2}^{3}15du=13.75+15=28.75\\
&m(4)-m(3)=\int_{3}^{4}\lambda(u)du=\int_{3}^{4}15du=15\\
&m(4)-m(1)=\int_{1}^{4}\lambda(u)du=\int_{1}^{2}\left(10+\frac{5}{2}u\right)du+\int_{2}^{4}15du=13.75+30=43.75
\end{align*}

## Calculando las integrales en R obtenemos:

```{r, echo=TRUE}
integrand <- function(u) {10+5*u/2}
integrate(integrand,lower=1,upper=2)
```

## Continuación solución 5A)

Finalmente, la probabilidad requerida viende dada por:

\begin{align*}
P\left[N(3)-N(1)\geq 10\left|\right.N(4)-N(1)=15\right]&=\frac{P\left[N(3)-N(1)\geq 10 \text{ , } N(4)-N(1)=15\right]}{P\left[N(4)-N(1)=15\right]}\\\\
& \text{ disjuntizando para lograr independencia de los incrementos}\\\\
&= \frac{\sum_{k=10}^{15}P\left[N(3)-N(1)=k \text{ , }N(4)-N(3)=15-k\right]}{P\left[N(4)-N(1)=15\right]}\\
&= \frac{\sum_{k=10}^{15}P\left[N(3)-N(1)=k\right] P\left[N(4)-N(3)=15-k\right]}{P\left[N(4)-N(1)=15\right]}\\
&=\frac{\sum_{k=10}^{15}\frac{e^{-28.75}(28.75)^{k}}{k!}\frac{e^{-15}(15)^{15-k}}{(15-k)!}}{\frac{e^{-43.75}(43.75)^{15}}{15!}}\\
\end{align*}

## Pregunta 5B)

El restaurante La Ruota abre de lunes a domingo entre las 7:00 PM a 1:00 AM. Se conoce que los comensales llegan al restaurante en grupos de tamaño 1, 2, 4 y 6 personas con probabilidades respectivas de $\frac{1}{8}$, $\frac{1}{2}$, $\frac{1}{8}$ y $\frac{1}{4}$ siguiendo un Proceso de Poisson con una taza de llegada que comienza en 10 grupos por hora a las 7:00 PM y aumenta linealmente hasta 15 grupos por hora a las 9:00 PM, momento en el cual la tasa se llegada se mantiene constante hasta las 11:00PM. A las 11:00 PM la tasa de llegada de clientes comienza a descender de manera lineal desde 15 grupos por hora hasta 3 grupos por hora a la 1:00 AM. Calcule el valor esperado del número de comensales que llegará al restaurante entre las 9:00 PM y las 11:00 PM en un día cualquiera. 

## Solución 5B)

Sea $X_{i}$ el tamaño del grupo $i$ que llega al restaurante entre las 9:00 PM y las 11:00 PM en un día cualquiera. 

Si $N(t)$ es el número de comensales que llegan al restaurante en cualquier intervalo contenido en el horario de 9:00 PM y las 11:00 PM en un día cualquiera, sabemos que $\{N(t),t\geq 0\}\sim PPH(15/\text{hora})$

Por lo tanto, el valor esperado requerido viene dado por

\begin{align*}
E\left(\sum_{i=1}^{N(2)}X_{i}\right)&=E\left[E\left(\sum_{i=1}^{N(2)}X_{i}\left|\right.N(2)\right)\right]\\
&\text{ Por la propiedad torre de la esperanza condicional }\\
&\text{ Comencemos por calcular }\\
E\left(\sum_{i=1}^{N(2)}X_{i}\left|\right.N(2)=n\right)&=E\left(\sum_{i=1}^{n}X_{i}\left|\right.N(2)\right)\\
&\text{ como } X_{i} \text{ y } N(2) \text{ son v.a. independientes }\\
&= E\left(\sum_{i=1}^{n}X_{i}\right)\\
&= nE(X_{i})=n\left(1\frac{1}{8}+2\frac{1}{2}+4\frac{1}{8}+6\frac{1}{4}\right)=\frac{25}{8}n\\
&\text{Finalmente,}\\
E\left(\sum_{i=1}^{N(2)}X_{i}\right)&=E\left[E\left(\sum_{i=1}^{N(2)}X_{i}\left|\right.N(2)\right)\right]\\
&= E\left[\frac{25}{8}N(2)\right]=\frac{25}{8}15(2)=93.75 \text{ comensales.}
\end{align*}

```{r, echo=TRUE}
(25*15*2)/8
```




## ¿Qué aprendimos hoy?
