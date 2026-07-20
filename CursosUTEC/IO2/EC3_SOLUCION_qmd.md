---
curso: IO2
titulo: EC3 SOLUCIÓN
slides: 0
fuente: EC3 SOLUCIÓN.qmd
---

---
title: "EC3 SOLUCIONES"
format: html
editor: visual
---

### EC3 2026-1 A

En el puerto del Callao, los buques arriban siguiendo un proceso de Poisson homogéneo con una tasa promedio de cinco buques por día. Aunque las llegadas se programan con anticipación, el número efectivo de embarcaciones que arriba es aleatorio debido a la incertidumbre propia de las condiciones marítimas. El puerto está preparado para recibir dos tipos de embarcaciones: buques de carga seca y químicos. Estos últimos son atendidos en un almacenamiento especializado administrado por DQM. La probabilidad de que un buque sea de carga seca es de 0.75

```{r}
ls = 0.75
lq = 1 - ls
```

#### Pregunta 1:

Calcule la probabilidad de que ocho buques químicos hayan llegado en 2 días, dado que en este mismo periodo llegaron 15 buques en total.

Se tiene el siguiente PPH.

$$
\begin{align*}
&\{N(t) ;t\geq0\} \sim PPH(5)
&\\&N(t):\text{# buques que llegan la puerto del callao hasta tiempo "t".} 
\end{align*}
$$

Por bifuración tenemos que:

$$
\begin{align*}
&\{N_1(t) ;t\geq0\} \sim PPH(5*0.75)
&\\&N_1(t):\text{# buques de carga seca que llegan la puerto del callao hasta tiempo "t".} \\\\&\{N_2(t) ;t\geq0\} \sim PPH(5*0.25)
&\\&N_2(t):\text{# buques químicos que llegan la puerto del callao hasta tiempo "t".}
\end{align*}
$$

donde $N(t) = N_1(t) + N_2(t)$ y $N_1(t) \perp N_2(t)$

Debemos resolver:

$$
\begin{align*}
P(N_2(2)=8 |N(2)=15) &= \frac{P(N_2(2)=8 ,N(2)=15)}{P(N(2)=15)}
\\\\&= \frac{P(N_2(2)=8,N_1(2)+N_2(2)=15)}{P(N(2)=15)}\\\\
&=\frac{P(N_2(2)=8,N_1(2)=7)}{P(N(2)=15)}\\\\&=\frac{P(N_2(2)=8)P(N_1(2)=7)}{P(N(2)=15)}\\\\&=\frac{\frac{e^{-(5*0.25*2)}(5*0.25*2)^8}{8!}\frac{e^{-(5*0.75*2)}(5*0.75*2)^7}{7!}}{\frac{e^{-(5*2)}(5*2)^{15}}{15!}}
\end{align*}
$$

```{r}
(dpois(8,5*0.25*2)*dpois(7,5*0.75*2))/dpois(15,5*2)

```

#### Pregunta 2:

Dado que en un periodo de tres días llegaron 15 buques de carga seca, calcule el tiempo esperado de llegada del décimo buque de carga seca.

El problema nos pide:

$$
\begin{align*}
E[S_{1_{10}}|N_1(3)=15]
\end{align*}
$$

donde k = 10 y n = 15. Dado que k\<n, la esperanza se calcula como:

$$
E[S_{1_{10}}|N_1(3)=15] = \frac{(10)(3)}{15+1}
$$

```{r}
(10*3)/(15+1)
```

### EC2 2026-1 B

Un hospital de emergencias viene enfrentando reclamos debido al aumento de las colas y tiempos de espera en la sala de atención. Esta situación ha generado preocupación tanto en los pacientes como en el personal médico, ya que la alta demanda de servicios está ocasionando congestión en distintas áreas del hospital. Los pacientes se clasifican en dos grupos según la gravedad de su condición: emergencia y urgencia. Los pacientes de emergencia llegan siguiendo un proceso de Poisson homogéneo con una tasa de 3 pacientes por hora, mientras que los pacientes de urgencia llegan también bajo un proceso de Poisson homogéneo con una tasa de 7 pacientes por hora. El hospital busca analizar el comportamiento de las llegadas de pacientes a la sala de atención. Asuma que el hospital atiende las 24 horas y que a las 00:00 horas no se tienen pacientes.

#### Pregunta 1:

Calcule la probabilidad de que, entre las 3:00 a. m. y las 6:00 a. m., lleguen en total 35 pacientes, y que, entre las 3:00 a. m. y las 8:30 a. m., arriben en total 60 pacientes.

Se tiene los siguientes PPH.

$$
\begin{align*}
&\{N_1(t) ;t\geq0\} \sim PPH(3)
&\\&N_1(t):\text{# pacientes de emergencia que llegan al hospital hasta tiempo "t".} \\\\&\{N_2(t) ;t\geq0\} \sim PPH(7)
&\\&N_2(t):\text{#  pacientes de urgencia que llegan al hospital hasta tiempo "t".}
\end{align*}
$$

Por superposición tenemos que:

$$
\begin{align*}
&\{N(t) ;t\geq0\} \sim PPH(3+7)
&\\&N(t):\text{# de pacientes que llegan al hospital hasta tiempo "t".} 
\end{align*}
$$

donde $N(t) = N_1(t) + N_2(t)$ y $N_1(t) \perp N_2(t)$

Tomando las 3:00 am como posición inicial (s=0)

Debemos resolver:

$$
\begin{align*}
P(N(3)-N(0)=35,N(5.5)-N(0) =60) &
\end{align*}
$$

Debemos disjuntizar los intervalos de tiempo para poder usar independencia de los incrementos.

$$
\begin{align*}
P(N(3)-N(0)=35,N(5.5)-N(0) =60) &= P(N(3)-N(0)=35,N(5.5)-N(3) =25)\\
&=P(N(3)-N(0)=35)P(N(5.5)-N(3) =25) \\
&=P(N(3)=35)P(N(2.5)=25) \text{ por estacionareidad }\\
&=\frac{e^{-10*3}(10*3)^35}{35!}\frac{e^{-10*2.5}(10*2.5)^25}{25!}
\end{align*}
$$

```{r}
dpois(35,10*3)*dpois(25,10*2.5)
```

#### Pregunta 2:

Dado que en un periodo de 5 horas llegaron 50 pacientes en total, calcule el tiempo esperado de llegada del paciente número 80.

El problema nos pide:

$$ \begin{align*} E[S_{80}|N(5)=50]  \end{align*} $$

donde k = 80 y n = 50. Dado que k\>n, la esperanza se calcula como:

$$ \begin{align*} E[S_{80}|N(5)=50] &=5+\frac{80-50}{10} \end{align*}  $$

```{r}
5 + (80-50)/10
```
