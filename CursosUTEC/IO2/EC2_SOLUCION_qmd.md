---
curso: IO2
titulo: EC2 SOLUCIÓN
slides: 0
fuente: EC2 SOLUCIÓN.qmd
---

---
title: "EC2 SOLUCIONES"
format: html
editor: visual
---

### EC2 2026-1 A

En la clase de IO2 del día viernes a las 4:00 p.m., los alumnos presentarán un quiz sobre propiedades de la exponencial; en esta ocasión, la profesora llegó con anticipación al salón con la intención de comenzar puntualmente y disponer de tiempo suficiente al final para que los estudiantes resolvieran el examen sin contratiempos, pero al momento de iniciar la clase observó que aún no había llegado ningún alumno. Se sabe que los estudiantes se clasifican en tres grupos según la distancia a la que viven (cerca, a distancia intermedia y lejos), y que el tiempo entre llegadas de los alumnos de cada grupo sigue una distribución exponencial con medias de 2, 4 y 10 minutos, respectivamente.

#### Pregunta 1:

Calcule la probabilidad de que el tiempo hasta que llegue el primer alumno (ya sea de cualquier grupo) sea a lo sumo de 5 minutos.

**Solución:**

Se tiene que:

$$
\begin{align*}
&T_1 : \text{Tiempo entre llegadas de alumnos que viven cerca}\\ &T_1 \sim \exp(\frac{1}{2})\\\\&T_2 : \text{Tiempo entre llegadas de alumnos que viven a distancia intermedia}\\ &T_2 \sim \exp(\frac{1}{4})\\\\&T_3 : \text{Tiempo entre llegadas de alumnos que viven lejos }\\ &T_3 \sim \exp(\frac{1}{10})\\\\
\end{align*}
$$

Por lo que el tiempo hasta que llegue el primer alumno será

$$
\begin{align*}
&T: \text{Tiempo hasta que llegue el primer alumno}\\
&T=\min(T_1,T_2,T_3) \sim \exp(\frac{1}{2}+\frac{1}{4}+\frac{1}{10})\\&\text{por la propiedad del mínimo de n exponenciales independientes}
\end{align*}
$$

Ahora nos piden calcular:

$$
\begin{align*}
P(T\leq5)&=1-e^{-(\frac{1}{2}+\frac{1}{4}+\frac{1}{10})(5)}\\&=0.9857
\end{align*}
$$

```{r}
pexp(5,(1/2 + 1/4 + 1/10))
```

#### Pregunta 2:

Ahora asuma que el tiempo entre llegadas de cualquier alumno se distribuye exponencialmente con media de 5 minutos. Calcule la probabilidad de que el tiempo hasta que lleguen exactamente cuatro alumnos sea mayor a 30 minutos

**Solución:**

Tenemos que

$$
\begin{align*}
&T: \text{Tiempo entre llegadas de alumnos}\\
&T\sim \exp(\frac{1}{5})
\end{align*}
$$

El tiempo hasta que lleguen exactamente 4 alumnos se expresa como:

$$
\begin{align*}
&S_4: \text{Tiempo hasta que lleguen exactamente 4 alumnos}\\&S_4 = T_1 + T_2 + T_3+T_4\\
&S_4\sim Erlang(4,\frac{1}{5})\\&\text{Por la suma de n exponenciales i.i.d.}
\end{align*}
$$

Nos piden calcular

$$
\begin{align*}
P(S_4>30) &= 1-P(S_4 \leq 30)\\
&=1-\bigg[1-\sum_{r=0}^{4-1}e^{-\frac{30}{5}}\frac{(\frac{30}{5})^r}{r!}\bigg]\\
&=\sum_{r=0}^{3}e^{-\frac{30}{5}}\frac{(\frac{30}{5})^r}{r!}\\
&=e^{-\frac{30}{5}}\frac{(\frac{30}{5})^0}{0!}+e^{-\frac{30}{5}}\frac{(\frac{30}{5})^1}{1!}+e^{-\frac{30}{5}}\frac{(\frac{30}{5})^2}{2!}+e^{-\frac{30}{5}}\frac{(\frac{30}{5})^3}{3!}\\&=0.1512
\end{align*}
$$

```{r}
sum(exp(-30/5) * (30/5)^(0:3) / factorial(0:3))

```

### EC2 2026-1 B

Los alumnos de la UTEC han desarrollado un robot capaz de servir bebidas; sin embargo, al tratarse de un prototipo, presenta fallas de manera recurrente que obligan a enviarlo al taller para su reparación. Cada vez que el robot falla, es llevado al taller, donde existe una probabilidad de 0.7 de que la reparación sea exitosa; en caso de que en alguna de estas ocasiones no logren repararlo, el proyecto se dará por finalizado. Además, el tiempo de funcionamiento del robot entre fallas sigue una distribución exponencial con una media de 4 días, siendo independiente tanto de los tiempos de funcionamiento anteriores como del número de reparaciones realizadas.

#### Pregunta 1:

Calcule la probabilidad de que el tiempo hasta que se de por finalizado el proyecto se mayor a 30 días.

Se tienen las siguientes variables

$$
\begin{align*}
&T_i :\text{Tiempo de vida del robot antes de que falle por i-ésima vez }\\
&T_i\sim\exp(\frac{1}{4})\\\\&N:\text{Número de veces que el robot será llevado al taller hasta que no pueda ser reparado más}\\&N\sim geo(0.3)\\\\
&S_N:\text{Tiempo hasta que el proyecto se de por finalizado}\\
&S_N = \sum_{i=1}^NT_i\\&S_N \sim \exp(\frac{0.3}{4})\\&\text{Por la propiedad de la suma de un numero aleatorio geométricamente distribuido de exponenciales i.i.d.}
\end{align*}
$$

El problema nos pide:

$$
P(S_N>30)=e^{(-\frac{0.3}{4})(30)}
$$

```{r}
1-pexp(30,0.3/4)

```

#### Pregunta 2:

Calcule la probabilidad de que el tiempo hasta que el robot sea llevado por tercera vez al taller se a lo sumo de 20 días.

Tenemos que:

$$
\begin{align*}
&S_3: \text{Tiempo hasta que el robot sea llevado al taller por tercera vez}\\
&S_3= T_1+T_2+T_3\\
&S_3 \sim Erlang(3,\frac{1}{4})\\&\text{Por la suma de n exponenciales i.i.d}
\end{align*}
$$

Nos piden:

$$
\begin{align*}
P(S_3\leq20)&=1-\sum_{r=0}^{3-1}e^{-\frac{20}{4}} \frac{(\frac{20}{4})^r}{r!}
\\&=1-\big[e^{-\frac{20}{4}} \frac{(\frac{20}{4})^0}{0!}+e^{-\frac{20}{4}} \frac{(\frac{20}{4})^1}{1!}+e^{-\frac{20}{4}} \frac{(\frac{20}{4})^2}{2!}\big]\\
&=1-\big[e^{-\frac{20}{4}} +e^{-\frac{20}{4}} \frac{20}{4}+e^{-\frac{20}{4}} \frac{(\frac{20}{4})^2}{2}\big]\\&=0.12465
\end{align*}
$$

```{r}
sum(exp(-20/4) * (20/4)^(0:2) / factorial(0:2))
```
