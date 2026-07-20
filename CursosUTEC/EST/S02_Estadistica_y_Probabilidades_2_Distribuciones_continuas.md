---
curso: EST
titulo: S02_Estadística y Probabilidades 2_ Distribuciones continuas
slides: 26
fuente: S02_Estadística y Probabilidades 2_ Distribuciones continuas.pdf
---

# S02_Estadística y Probabilidades 2_ Distribuciones continuas

## Índice

Capítulo de Estadística y Probabilidades 2. Contenido transcrito de las diapositivas (fórmulas en LaTeX, figuras descritas).

# S02 — Estadística y Probabilidades II: Distribuciones Continuas

## Slide 1 — Portada

**Tema:** Distribuciones Continuas

**Sesión:** 1.2

**Curso:** Estadística y probabilidades II

**Institución:** UTEC (Universidad de Ingeniería y Tecnología)

---

## Slide 2 — Distribuciones Continuas: Definición

**DISTRIBUCIONES CONTINUAS**

Una variable aleatoria continua es aquella que adopta todos los valores de un intervalo.

Siendo más rigurosos, una variable aleatoria continua es una función:

$$X: \Omega \to I \subset \mathbb{R}$$

Tal que cualquier valor de $I$ es obtenido a partir de algún $\omega \in \Omega$.

**Diagrama:** Se muestra el espacio muestral $\Omega$ (conjunto gris) con un elemento $\omega$, conectado mediante la función $X$ (flecha roja) hacia el intervalo $I$ en los reales, donde se mapea a $X(\omega) = x_0 \in I$.

---

## Slide 3 — Distribución Normal

**DISTRIBUCIONES CONTINUAS**

**Normal**

**Variable aleatoria:** $X \sim N(\mu, \sigma^2)$

**Rango:** $-\infty < X < \infty$

**Parámetros:**
- $\mu = E(X)$ → Media de X
- $\sigma^2 = V(X)$ → Varianza de X

Necesariamente se debe indicar en el texto que la variable es Normal.

**Función de densidad:**

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

**Probabilidad:** Se calcula con R-Studio.

**Figura:** Campana de Gauss simétrica centrada en $\mu$, con puntos de inflexión en $\mu - \sigma$ y $\mu + \sigma$.

---

## Slide 4 — Normal con R

**Normal con R**

**Cálculo de una probabilidad acumulada**

- Si se desea: $P(X < k) = P(X \leq k) = ??$ 
  ```
  pnorm(k, μ, σ, Lower.Tail = T)
  ```

- Si se desea: $P(X > k) = P(X \geq k) = ??$ 
  ```
  pnorm(k, μ, σ, Lower.Tail = F)
  ```

**Cálculo de la inversa acumulada (¿k = ??)**

- Si $P(X < k) = P(X \leq k) = p$
  ```
  qnorm(p, μ, σ)
  ```

**Tener en cuenta lo siguiente:**

- $P(X \geq k) = P(X > k) = 1 - P(x \leq k)$

- $P(a \leq X \leq b) = P(a < X < b) = P(X \leq b) - P(X \leq a)$

---

## Slide 5 — Normal Estándar

**DISTRIBUCIONES CONTINUAS**

**Normal estándar**

La Normal estándar es una variable Normal, **denotada por z**, que tiene media 0 y desviación 1.

Si $X \sim N(\mu, \sigma^2)$ tiene media $\mu$ y desviación $\sigma$, entonces, se obtiene una normal estándar, haciendo la sustitución:

$$z = \frac{X - \mu}{\sigma}$$

La normal estándar tiene media $\mu_z = 0$ y desviación $\sigma_z = 1$

**Figura:** Campana de Gauss estándar centrada en 0, con área sombreada entre $-1$ y $1$ indicando 68.26% de la distribución. Marcas de eje en $-3, -2, -1, 0, 1, 2, 3$.

---

## Slide 6 — Actividad de Clase: Ejemplo 1

**Actividad de clase**

**Ejemplo 1:** La cantidad de dinero destinada al ahorro mensual de los clientes de un banco, es una variable aleatoria con distribución normal, siendo su media 400 soles y su desviación estándar igual a 80 soles.

a. Calcule la probabilidad de que un cliente ahorre más de 360 soles mensuales.

b. Sabiendo que un cliente ahorró más de 360 soles, calcule la probabilidad de que sea no más de 500 soles.

**Código R mostrado:**

```r
pnorm(360, 400, 80, lower.tail = FALSE)
[1] 0.6914625
```

```r
(pnorm(500, 400, 80) - pnorm(360, 400, 80)) / pnorm(360, 400, 80, lower.tail = F)
[1] 0.8472082
```

---

## Slide 7 — Actividad de Clase: Ejemplo 2

**Actividad de clase**

**Ejemplo 2:** La cantidad de dinero destinada al ahorro mensual de los clientes de un banco, es una variable aleatoria con distribución normal, siendo su media 400 soles y su desviación estándar igual a 80 soles.

a. ¿Cuál es el ahorro mínimo mensual para estar en el 25% de los clientes que más ahorran?

b. ¿Cuál es el ahorro máximo mensual para estar en el primer decil de los clientes que menos ahorran?

**Código R mostrado:**

```r
qnorm(0.25, 400, 80, Lower.tail = F)
[1] 453.9592
```

```r
qnorm(0.1, 400, 80)
[1] 297.4759
```

---

## Slide 8 — Actividad de Clase: Ejemplo 3

**Actividad de clase**

**Ejemplo 3:** La cantidad de dinero destinada al ahorro mensual de los clientes de un banco, es una variable aleatoria con distribución normal, siendo su media 400 soles y su desviación estándar igual a 80 soles.

Si se elige al azar a 2000 clientes, ¿qué cantidad de clientes se espera que ahorren más de S/ 500?

**Código R mostrado:**

```r
pnorm(500, 400, 80, lower.tail = F)
[1] 0.1056498
```

---

## Slide 9 — Actividad de Clase: Ejemplo 4

**Actividad de clase**

**Ejemplo 4:** Se ha observado que, en una marca de vehículos, la distancia de frenado se comporta como una variable normal. El 62% de las veces esta distancia no supera los 30 metros, mientras que el 55% de las veces la distancia de frenado supera a 20 metros.

¿Con que probabilidad esta distancia no excede los 10 metros?

**Código R mostrado:**

```r
> qnorm(0.62, 0, 1)
[1] 0.3054808
```

```r
{r}
qnorm(0.55, 0, 1, Lower.tail=F)
[1] -0.1256613
```

---

## Slide 10 — Propiedad Reproductiva de la Normal

**Propiedad reproductiva de la normal**

**Teorema:**

1) La suma y diferencia de 2 variables normales, produce otra normal:

$$x \sim N(\mu_x; \sigma^2_x)$$
$$y \sim N(\mu_y; \sigma^2_y)$$

Entonces:

$$x \pm y \sim N(\mu_x \pm \mu_y; \sigma^2_x + \sigma^2_y)$$

donde $\sigma^2 = \sigma^2_x + \sigma^2_y$ (la varianza de la suma/diferencia)

2) En general:

$$x \sim N(\mu_x; \sigma^2_x)$$
$$y \sim N(\mu_y; \sigma^2_y)$$

Entonces:

$$ax + by \sim N(a.\mu_x + b.\mu_y; a^2.\sigma^2_x + b^2.\sigma^2_y)$$

---

## Slide 11 — Actividad de Clase: Ejemplo 5

**Actividad de clase**

**Ejemplo 5:** Una fábrica de puertas, las realiza de distintos tamaños. Se sabe que el largo de las puertas producidas tiene distribución normal con media $2.4 \, m$ y desviación $24 \, cm$, mientras que el ancho es también normal con media $1.2 \, m$ y desviación $18 \, cm$. ¿Cuál es la probabilidad de que el perímetro de una puerta supere los $7 \, m$?

**Código R mostrado:**

```r
{r}
pnorm(3.5, 3.6, 0.30, lower.tail = F)
[1] 0.6305587
```

---

## Slide 12 — Chi Cuadrado

**DISTRIBUCIONES CONTINUAS**

**Chi cuadrado**

Se genera mediante la suma de los cuadrados de $n$ variables normales estándar, que sean independientes.

$$z_1^2 + z_2^2 + z_3^2 + \cdots + z_n^2 = \chi^2(n)$$

$n$: grados de libertad.

**Esperado:** $E(\chi^2(n)) = n$

**Varianza:** $V(\chi^2(n)) = 2n$

**Figura:** Distribución chi-cuadrado para muestras pequeñas (etiqueta "PARA MUESTRAS PEQUEÑAS"), mostrando la curva de densidad asimétrica hacia la derecha, con área sombreada en la cola izquierda.

---

## Slide 13 — Chi con R

**Chi con R**

**Cálculo de una probabilidad acumulada**

- $P(X(gl) < k) = P(X(gl) \leq k) = ??$ 
  ```
  pchisq(k, gl, Lower.Tail = T)
  ```

- $P(X(gl) > k) = P(X(gl) \geq k) = ??$ 
  ```
  pchisq(k, gl, Lower.Tail = F)
  ```

**Cálculo de la inversa acumulada (k = ??)**

- $P(X(gl) < k) = P(X(gl) \leq k) = p$ 
  ```
  qchisq(p, gl, Lower.Tail = T)
  ```

**PROPIEDADES**

1) Si $z$ es normal estándar: $z^2 = \chi^2(1)$

2) $\chi^2(n) + \chi^2(m) = \chi^2(n + m)$

---

## Slide 14 — Actividad de Clase: Ejemplo 6

**Actividad de clase**

**Ejemplo 6:**

Sea la variable $z_1$ una normal con media 2 y varianza 1.

Calcule $P((z_1 - 6)(z_1 + 2) + 10 > 0)$

**Código R mostrado:**

```r
{r}
pchisq(6, 1, lower.tail = F)
[1] 0.01430588
```

---

## Slide 15 — Actividad de Clase: Ejemplo 7

**Actividad de clase**

**Ejemplo 7:**

Sean las variables $z \sim N(0; 1)$ y $z_1$ una normal con media 2 y varianza 1.

Calcular el valor de $k$, si $P(z^2 + z_1^2 < 4(z_1 + k)) = 0.80$

**Código R mostrado:**

```r
{r}
qchisq(0.80, 2)
[1] 3.218876
```

---

## Slide 16 — Actividad de Clase: Ejemplo 8

**Actividad de clase**

**Ejemplo 8:**

Sean las variables normales estándar $z_1, z_2, z_3, z_4$.

Calcule $E((z_1^2 + z_2^2 + z_3^2 + z_4^2)^2)$

**Esperado y Varianza (mostrados abajo):**

$$E(F(m; n)) = \frac{n}{n-2}, \quad n > 2$$

$$V(F(m; n)) = \frac{2n^2(n + m - 2)}{m(n-2)^2(n-4)}, \quad n > 4$$

---

## Slide 17 — T Student

**DISTRIBUCIONES CONTINUAS**

**PARA MUESTRAS PEQUEÑAS**

**T Student**

Se genera mediante una normal estándar, dividida entre la raíz cuadrada de una chi-cuadrada.

Sean las variables independientes:
- $z$: normal estándar
- $\chi^2(n)$: chi cuadrado con $n$ grados de libertad

Entonces:

$$T(n) = \frac{z}{\sqrt{\frac{\chi^2(n)}{n}}}$$

**Esperado:** $E(T(n)) = 0$

**Varianza:** $V(T(n)) = \frac{n}{n-2}, \quad n > 2$

**Figura:** Función de densidad de la distribución t de Student con $df = 3$, campana simétrica centrada en 0, con colas más pesadas que la normal estándar.

---

## Slide 18 — T Student con R

**T Student con R**

Si se desea: $P(t(gl) \leq k)$
```
pt(k, gl, Lower.Tail = T)
```

Si se desea: $P(t(gl) \geq k)$:
```
pt(k, gl, Lower.Tail = F)
```

Si se desea k, tal que: $P(t(gl) \leq k) = p$
```
qt(p, gl)
```

---

## Slide 19 — Actividad de Clase: Ejemplo 9

**Actividad de clase**

**Ejemplo 9:**

Sean las variables normales estándar $z_1, z_2, z_3, z_4, z_5$.

Calcule $P(\sqrt{z_2^2 + z_3^2 + z_4^2 + z_5^2} > 2z_1)$

**Código R mostrado:**

```r
{r}
pt(1, 4)
[1] 0.8130495
```

---

## Slide 20 — Actividad de Clase: Ejemplo 10

**Actividad de clase**

**Ejemplo 10:**

Sean las variables normales estándar $z_2, z_3, z_4$ y la variable normal $z_1$ con media 1 y varianza 4

Calcule $P(z_1^2 - z_2^2 - z_3^2 - z_4^2 + 1 < 2z_1)$

**Código R mostrado:**

```r
{r}
pf(0.75, 1, 3)
[1] 0.5498151
```

---

## Slide 21 — DISTRIBUCIONES CONTINUAS: F de Fisher

**Tema:** PARA MUESTRAS PEQUEÑAS

**Distribución: F de Fisher**

Se genera dividiendo dos chi cuadrados independientes.

Sean las variables independientes:
- $\chi^2(m)$: chi cuadrado con $m$ grados de libertad
- $\chi^2(n)$: chi cuadrado con $n$ grados de libertad

**Entonces:**

$$F(m; n) = \frac{\frac{\chi^2(m)}{m}}{\frac{\chi^2(n)}{n}}$$

**Esperado:**

$$E(F(m; n)) = \frac{n}{n-2} \quad n > 2$$

**Varianza:**

$$V(F(m; n)) = \frac{2n^2(n+m-2)}{m(n-2)^2(n-4)} \quad n > 4$$

---

## Slide 22 — Fisher con R

### Funciones R para cálculo de probabilidades

**Si se desea:** $P(F(m, n) \leq k)$

```r
pf(k, m, n, lower.tail = T)
```

**Si se desea:** $P(F(m, n) \geq q)$

```r
pf(k, m, n, lower.tail = F)
```

### Función para calcular cuantiles

Para calcular $k$, tal que $P(F(m, n) \leq k) = p$

```r
qf(p, m, n)
```

---

## Slide 23 — Actividad de clase: Ejemplo 11

Sean las variables normales estándar $z_2, z_3, z_4$ y la variable normal $z_1$ con media 2 y varianza 9.

**Calcule:**
$$P(z_1^2 - z_2^2 - z_3^2 - z_4^2 + 4 < 4z_1)$$

**Solución en R:**

```r
pf(1/3, 1, 3)
```

**Resultado:**
```
[1] 0.3958187
```

---

## Slide 24 — Actividad de clase: Ejemplo 12

Sean las variables $z_1, z_2, z_3, z_4, z_5 \sim N(0; 1)$.

**Calcular el valor de $k$, si:**
$$P(kz_1^2 + kz_2^2 < z_3^2 + z_4^2 + z_5^2) = 0.5$$

**Solución en R:**

```r
qf(0.5, 3, 2, lower.tail = F)
```

**Resultado:**
```
[1] 1.134943
```

---

## Slide 25 — Bibliografía complementaria

### Referencias bibliográficas

**Libro 1: Probabilidad e Inferencia estadística**

- **Autores:** Rufino Moya C.; Gregorio Saravia A.
- **Editorial:** Editorial San Marcos
- **Ubicación:** Lima, Perú

**Figura:** Portada con fondo marrón oscuro. Contiene gráficos matemáticos en la portada: fórmulas de probabilidad, campana de Gauss y gráficos estadísticos. Título en letras grandes doradas: "PROBABILIDAD E INFERENCIA ESTADISTICA".

**Libro 2: Estadística para todos. Análisis de datos**

- **Subtítulo:** Análisis de datos: estadística descriptiva, teoría de la probabilidad e inferencia
- **Autor:** Eva Romero Ramos
- **Editorial:** Editorial Pirámide
- **Ubicación:** Madrid, España

**Figura:** Portada azul marino con título blanco de tipografía clara. Contiene un gráfico abstracto en la mitad inferior: líneas amarillas/doradas que forman una estructura piramidal sobre fondo púrpura. El logo "PIRÁMIDE" aparece en la parte inferior.

---

## Slide 26 — ¿Qué es la Ciencia de Datos?

Al estudiar la carrera de Ciencia de Datos en UTEC te convertirás en el profesional capaz de descifrar grandes volúmenes de información, predecir escenarios, tomar decisiones y crear soluciones a partir de ellos. Serás el responsable de encontrar y extraer tendencias a partir de grandes conjuntos de datos usando, por ejemplo, algoritmos de inteligencia artificial.

Aprenderás bajo una malla curricular de estándar internacional y nuestros convenios internacionales con las instituciones más top del mundo te llevarán a compartir tus conocimientos y tu ingenio.

La Ciencia de Datos es una profesión que las empresas están demandando cada vez más, especialmente en tiempos de transformación digital. Esta carrera en UTEC, primera de su tipo en el Perú, te llevará a dominar la relación entre las matemáticas, la estadística y la computación. Con tus conocimientos en análisis y procesamiento de datos, podrás ser el líder de los nuevos retos que el mundo afronta.
