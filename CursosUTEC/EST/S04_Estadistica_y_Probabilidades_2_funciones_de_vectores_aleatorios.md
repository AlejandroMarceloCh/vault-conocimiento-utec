---
curso: EST
titulo: S04_Estadística y Probabilidades 2_ funciones de vectores aleatorios
slides: 36
fuente: S04_Estadística y Probabilidades 2_ funciones de vectores aleatorios.pdf
---

# S04_Estadística y Probabilidades 2_ funciones de vectores aleatorios

## Índice

Capítulo de Estadística y Probabilidades 2. Contenido transcrito de las diapositivas (fórmulas en LaTeX, figuras descritas).

# Tema 4: Funciones de vectores aleatorios

**Semana 3 — Estadística y probabilidades II (UTEC)**

---

## Slide 1 — Portada

**ESTADÍSTICA Y PROBABILIDADES 2**

**Tema 4:**

**Funciones de vectores aleatorios**

**Semana 3**

**Figura:** Portada con logo UTEC y fotografía de edificio moderno (fachada de concreto con líneas geométricas).

---

## Slide 2 — Función de distribución bivariados

**Función de distribución bivariados**

Hasta el tema anterior, solo se generaba una variable aleatoria, lo que implicaba que solo estábamos interesados en una característica $X$.

Pero es muy frecuente, que dado un experimento aleatorio, estemos interesados en dos características $X$ e $Y$ o tal vez en más.

En esta unidad veremos el cálculo de probabilidades cuando tenemos dos variables aleatorias $X$ e $Y$, lo que genera un vector aleatorio denotado $(X; Y)$.

---

## Slide 3 — Distribución de probabilidad - Caso discreto

**Distribución de probabilidad - Caso discreto**

Si $X_1$ y $X_2$ son dos variables aleatorias discretas entonces su **función de probabilidad conjunta** (o bivariada) está dada por:

$$p(x_1, x_2) = P(X_1 = x_1, X_2 = x_2), \quad -\infty < x_1 < \infty, \quad -\infty < x_2 < \infty$$

**PROPIEDADES:**

1) $p(x_1, x_2) \geq 0$ para todo $x_1, x_2$
2) $\sum_{x_1, x_2} p(x_1, x_2) = 1$

La **función de distribución conjunta** de las variables discretas $X_1$ y $X_2$ se puede obtener a partir de

$$F(x_1, x_2) = P(X_1 \leq x_1, X_2 \leq x_2), \quad -\infty < x_1 < \infty, \quad -\infty < x_2 < \infty$$

---

## Slide 4 — Actividad de clase: Ejemplo 1 (Parte I)

**Actividad de clase**

**Ejemplo 1:** COMPUCENTRO es una empresa dedicada a la venta de computadoras y accesorios. Dos clientes acaban de realizar compras y para hacer el pago, tienen tres cajas disponibles a los cuales acuden de forma independiente, eligiendo cada uno una caja al azar. Sea $X_1$ el número de clientes que eligen la caja 1 y $X_2$ el número de clientes que eligen la caja 2.

a) Determine la función de probabilidad conjunta expresándola en una tabla de doble entrada.

b) Calcule $F(2, 1.8)$

---

## Slide 5 — Actividad de clase: Ejemplo 1 (Parte II - Solución)

**Actividad de clase**

(Continuación Ejemplo 1 - Solución en desarrollo)

Esta slide contiene el espacio para desarrollar la solución del Ejemplo 1 con la tabla de doble entrada y el cálculo de $F(2, 1.8)$.

---

## Slide 6 — Distribución conjunta - Caso continuo

**Distribución conjunta - Caso continuo**

Si $X_1$ y $X_2$ son dos variables aleatorias continuas, su **función de distribución conjunta** está definida por:

$$F(x_1, x_2) = \int_{-\infty}^{x_1} \int_{-\infty}^{x_2} f(u, v) \, dv \, du, \quad -\infty < x_1 < \infty, \quad -\infty < x_2 < \infty$$

siempre que exista una función no negativa $f(x_1, x_2)$, que se denominará **función de densidad de probabilidad conjunta**.

**PROPIEDADES:**

1) $F(-\infty, -\infty) = F(-\infty, x_2) = F(x_1, -\infty) = 0$
2) $F(\infty, \infty) = 1$
3) $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x_1, x_2) \, dx_1 \, dx_2 = 1$

---

## Slide 7 — Actividad de clase: Ejemplo 2 (Parte I)

**Actividad de clase**

**Ejemplo 2:** La distribución Uniforme en su forma bivariada tiene la siguiente función de densidad de probabilidad conjunta, cuando el punto $(x, y)$ está en un rectángulo:

$$f(x, y) = \begin{cases} k, & 0 \leq x \leq 2, \, 1 \leq y \leq 4 \\ 0, & en \, otros \, puntos \end{cases}$$

Siendo $k$ un valor específico.

a) Calcule el valor de $k$.
b) Calcule $F(1.3, 1.5)$.
c) Calcule $P(0.5 \leq x \leq 1.5, \, y \geq 2)$
d) Calcule $P(2x + y \geq 2)$

---

## Slide 8 — Actividad de clase: Ejemplo 2 (Parte II - Solución)

**Actividad de clase**

(Continuación Ejemplo 2 - Solución en desarrollo)

Siendo $k$ un valor específico.

a) Calcule el valor de $k$.
b) Calcule $F(1.3, 1.5)$.
c) Calcule $P(0.5 \leq x \leq 1.5, \, y \geq 2)$
d) Calcule $P(2x + y \geq 2)$

---

## Slide 9 — Actividad de clase: Para el alumno

**Actividad de clase**

**Para el alumno:** La distribución Uniforme en su forma bivariada tiene la siguiente función de densidad de probabilidad conjunta, cuando el punto $(x, y)$ está en un rectángulo:

$$f(x, y) = \begin{cases} k, & en \, triángulo \, ABC \\ 0, & en \, otros \, puntos \end{cases}$$

Siendo $k$ un valor específico y $A(1;1)$, $B(5;1)$, $C(1; 7)$.

a) Calcule el valor de $k$.
b) Calcule $F(3; 4)$.
c) Calcule $P(y > 3)$
d) Calcule $P(y \geq x)$

---

## Slide 10 — Esperanza de una función de 2 variables aleatorias

**Esperanza de una función de 2 variables aleatorias**

**Esperanza:**
Sea $g(x, y)$ una función de dos variables aleatorias.

- **Para el caso discreto:**
$$E(g(x, y)) = \sum_x \sum_y g(x, y) \cdot p(x, y)$$

- **Para el caso continuo:**
$$E(g(x, y)) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \cdot f(x, y) \, dx \, dy$$

---

## Slide 11 — Actividad de clase: Ejemplo 3

**Actividad de clase**

**Ejemplo 3:** Del ejemplo 1 determine la esperanza de la suma de $x$ e $y$.

---

## Slide 12 — Actividad de clase: Ejemplo 4

**Actividad de clase**

**Ejemplo 4:** Del ejemplo 2 calcule la esperanza del producto de $x$ e $y$.

---

## Slide 13 — Actividad de clase: Ejemplo 5

**Actividad de clase**

**Ejemplo 5:** Extrayendo mineral de una mina, se ha deducido en un laboratorio que una muestra de ello siempre puede contener hasta 2 tipos de impurezas A y B. Luego de realizar varias observaciones se ha obtenido la siguiente función de densidad

$$f(x, y) = \begin{cases} k(1 - x), & 0 \leq x \leq 1, \, 0 \leq y \leq 1 \\ 0, & en \, otros \, puntos \end{cases}$$

siendo $x$ la proporción total de impurezas que está presente en una muestra del mineral e $y$ representa la proporción de impurezas de tipo B que se encuentra entre toda la impureza hallada en la muestra del mineral.

Calcule el esperado de la proporción de impureza del tipo A en toda la muestra.

**Figura:** Fotografía de fluorita (mineral de fluoruro de calcio) mostrando cristales azules y verdes sobre matriz blanca y dorada.

---

## Slide 14 — Solución: Ejemplo 5

**solución**

**Ejemplo 5:** Extrayendo mineral de una mina, se ha deducido en un laboratorio que una muestra de ello siempre puede contener hasta 2 tipos de impurezas A y B. Luego de realizar varias observaciones se ha obtenido la siguiente función de densidad

$$f(x, y) = \begin{cases} k(1 - x), & 0 \leq x \leq 1, \, 0 \leq y \leq 1 \\ 0, & en \, otros \, puntos \end{cases}$$

siendo $x$ la proporción total de impurezas que está presente en una muestra del mineral e $y$ representa la proporción de impurezas de tipo B que se encuentra entre toda la impureza hallada en la muestra del mineral.

Calcule el esperado de la proporción de impureza del tipo A en toda la muestra.

---

## Slide 15 — Distribuciones de probabilidad marginal y condicional. Caso discreto

**Distribuciones de probabilidad marginal y condicional. Caso discreto.**

**Función de probabilidad marginal**

Si $X$, $Y$ son dos variables aleatorias discretas con función de probabilidad conjunta (o bivariada) dada por:

$$p(x, y) = P(X = x, Y = y), \quad -\infty < x < \infty, \quad -\infty < y < \infty$$

Entonces se definen a sus funciones de probabilidad marginal de $X$ e $Y$ respectivamente, mediante

$$p_X(x) = \sum_Y P(X = x, Y = y), \quad -\infty < x < \infty$$

$$p_Y(x) = \sum_X P(X = x, Y = y), \quad -\infty < y < \infty$$

---

## Slide 16 — Distribuciones de probabilidad marginal y condicional. Caso continuo

**Distribuciones de probabilidad marginal y condicional. Caso continuo.**

**Función de densidad marginal**

Si $X$, $Y$ son dos variables aleatorias discretas con función de densidad conjunta (o bivariada) dada por:

$$f(x, y), \quad -\infty < x < \infty, \quad -\infty < y < \infty$$

Entonces se definen a sus funciones de densidad marginal de $X$ e $Y$ respectivamente, mediante

$$f_X(x) = \int_{-\infty}^{\infty} f(x, y) \, dy, \quad -\infty < y < \infty$$

$$f_Y(x) = \int_{-\infty}^{\infty} f(x, y) \, dx, \quad -\infty < x < \infty$$

---

## Slide 17 — Actividad de clase: Ejemplo 6

**Actividad de clase**

**Ejemplo 6:** La función de probabilidad conjunta para dos variables aleatorias está dada por:

| $X$ \ $Y$ | 1   | 2   |
|-----------|-----|-----|
| 0         | 0.1 | 0.1 |
| 1         | 0.2 | 0.2 |
| 2         | 0.3 | 0.1 |

Obtenga a partir de ello la distribución marginal para $X$ e $Y$, luego calcule sus valores esperados respectivos.

---

## Slide 18 — Solución: Ejemplo 6

**solución**

**Ejemplo 6:** La función de probabilidad conjunta para dos variables aleatorias está dada por:

| $X$ \ $Y$ | 1   | 2   |
|-----------|-----|-----|
| 0         | 0.1 | 0.1 |
| 1         | 0.2 | 0.2 |
| 2         | 0.3 | 0.1 |

Obtenga a partir de ello la distribución marginal para $X$ e $Y$, luego calcule sus valores esperados respectivos.

---

## Slide 19 — Actividad de clase: Ejemplo 7

**Actividad de clase**

**Ejemplo 7:** Dada la siguiente función de densidad conjunta para dos variables aleatorias continuas

$$f(x, y) = \begin{cases} kx, & 0 \leq x \leq 2, \, 0 \leq y \leq 1 \\ 0, & en \, otros \, puntos \end{cases}$$

Obtenga las respectivas funciones de densidad marginales y luego calcule sus esperados.

---

## Slide 20 — Solución: Ejemplo 7

**solución**

(Solución del Ejemplo 7 en desarrollo)

---

**Fin del Tema 4 - Slides 1-20**

---

# S04 — Estadística y Probabilidades 2: Funciones de Vectores Aleatorios
## Slides 21–36

---

## Slide 21 — Función de probabilidad discreta condicional

**Definición:** La función de probabilidad condicional de dos variables aleatorias $X$ e $Y$ se define como:

$$p(x | y = y_o) = P(X = x | Y = y_o) = \frac{P(x, y_o)}{P(y_o)} = \frac{p(x, y_o)}{p_Y(y_o)}$$

$$p(y | x = x_o) = P(Y = y | X = x_o) = \frac{P(x_o, y)}{P(x_o)} = \frac{p(x_o, y)}{p_X(x_o)}$$

---

## Slide 22 — Función de distribución condicional

**Denotamos:**

$$p(X \le x | Y = y_o) = F(x|y_o)$$

$$p(Y \le y | X = x_o) = F(y|x_o)$$

**Función de densidad condicional:**

$$f(x | y = y_o) = \frac{f(x, y)}{f_Y(y_o)}$$

$$f(y | x = x_o) = \frac{f(x, y)}{f_X(x_o)}$$

---

## Slide 23 — Actividad de clase: Ejemplo 8

**Ejemplo 8:** Dada la función de probabilidad conjunta para dos variables aleatorias definida mediante:

| $X \backslash Y$ | 1   | 2   |
|------------------|-----|-----|
| 0                | 0.1 | 0.1 |
| 1                | 0.2 | 0.2 |
| 2                | 0.3 | 0.1 |

**Preguntas:**
- Halle la distribución de probabilidades condicional de $Y$ dado que $X = 2$.
- Obtenga también la distribución de probabilidades condicional de $X$ dado que $Y = 1$.

---

## Slide 24 — PROBLEMA

La función de probabilidad conjunta de 2 variables aleatorias está determinada por:

$$p(0,1) = \frac{p(0,2)}{2} = \frac{p(1,1)}{2} = \frac{p(2,2)}{3}$$

$$p(1,2) = p(2,1) = 0$$

**Preguntas:**
1. Calcule las distribuciones marginales para $X$ y para $Y$.
2. Halle la Distribución condicional de $X$ dado $Y=1$.
3. Halle la Distribución condicional de $Y$ dado $X=2$.
4. Calcule la esperanza de $x + y$.

---

## Slide 25 — Actividad de clase: Ejemplo 9

**Ejemplo 9:** Sean $X, Y$ dos variables aleatorias continuas con función de densidad conjunta:

$$f(x, y) = \begin{cases}
k, & 0 \le x \le y \le 2 \\
0, & \text{en otros puntos}
\end{cases}$$

**Pregunta:** Obtenga la densidad condicional de $X$ dado que $Y = y_o$.

---

## Slide 26 — Variables aleatorias independientes: Definición

**Definición:**

Si $F_X(x)$ y $F_Y(y)$ son las funciones de distribución de las variables aleatorias $X$ , $Y$ respectivamente y $F(x, y)$ es la función de distribución conjunta, entonces $X$ y $Y$ son **independientes** si y solo si:

$$F(x, y) = F_X(x) \cdot F_Y(y)$$

Para todo par de números reales $x, y$.

Si no son independientes se llamarán **dependientes**.

---

## Slide 27 — Variables aleatorias independientes: Teorema

**Teorema:**

- Si $X, Y$ son variables aleatorias **discretas**: Serán independientes si solo si
  $$p(x, y) = p_X(x) \cdot p_Y(y)$$
  para todo par de reales $(x, y)$.

- Si $X, Y$ son variables aleatorias **continuas**: Serán independientes si solo si
  $$f(x, y) = f_X(x) \cdot f_Y(y)$$
  para todo par de reales $(x, y)$.

---

## Slide 28 — Variables aleatorias independientes: Teorema del valor esperado

**Teorema del valor esperado de variables aleatorias independientes:**

- Si $X, Y$ son variables aleatorias independientes se cumple que:
  $$E(X \cdot Y) = E(X) \cdot E(Y)$$

- En general, si $m(X)$ y $n(Y)$ son funciones de variables aleatorias independientes $X, Y$ entonces se cumple que:
  $$E(m(X) \cdot n(Y)) = E(m(X)) \cdot E(n(Y))$$

---

## Slide 29 — Actividad de clase: Ejemplo 8 (Dos monedas)

**Ejemplo 8:** Se lanzan dos monedas y se declaran las variables:
- $X$: # de caras que se obtiene en la moneda 1.
- $Y$: # de sellos que se obtiene en la moneda 2.

**Pregunta:** Determinar si ambas variables son dependientes o independientes.

---

## Slide 30 — Actividad de clase: Ejemplo 9 (Continuas)

**Ejemplo 9:** Sean las variables aleatorias continuas con función de densidad:

$$f(x, y) = \begin{cases}
6xy^2, & 0 \le x \le 1, 0 \le y \le 1 \\
0, & \text{en otros casos}
\end{cases}$$

**Pregunta:** ¿son estas variables independientes?

---

## Slide 31 — Valores esperados condicionales: Definición

**Definición:**

Dado que ya se conoce como determinar la función de probabilidad condicional $p(x|y)$ y también la densidad condicional $f(x|y)$, entonces se define al valor esperado condicional de $g(X)$ dado $Y = y$ mediante:

- $E(g(X) | Y = y) = \sum_x g(x) \cdot p(x|y)$ para el caso discreto.

- $E(g(X) | Y = y) = \int_{-\infty}^{\infty} g(x) \cdot f(x|y) dx$ para el caso continuo.

---

## Slide 32 — Valores esperados condicionales (Continuación)

En general el valor esperado condicional de $X$, dado $Y = y$ es una función de $y$, ya que solo dependerá de los valores que tome esta variable, luego si $y$ va tomando todos sus valores posibles, se podrá considerar que:

$$E(X | Y) = h(Y) \text{ es una función de la variable aleatoria } Y$$

Hallando el valor esperado de $h(Y)$:

$$E(h(Y)) = \int_{-\infty}^{\infty} h(y) \cdot f(y) dy$$

$$E(E(X|Y)) = \int_{-\infty}^{\infty} E(X|Y = y) \cdot f(y) dy = \int_{-\infty}^{\infty} \left(\int_{-\infty}^{\infty} x \cdot f(x|y) dx\right) \cdot f(y) dy$$

$$= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x \cdot f(x|y) \cdot f(y) \cdot dxdy = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x \cdot \frac{f(x,y)}{f(y)} \cdot f(y) \cdot dxdy$$

$$= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x \cdot f(x, y) \cdot dxdy = E(X)$$

**Resultado:**
$$E(E(X|Y)) = E(X)$$

---

## Slide 33 — Actividad de clase: Ejemplo 12

**Ejemplo 12:** Una máquina expendedora de café contiene al inicio del día una cantidad $Y$ que no pasa de 4 galones. En el transcurso del día se ha vendido una cantidad de $X$ galones. La distribución conjunta es:

$$f(x, y) = \begin{cases}
\frac{1}{8}, & 0 \le x \le y \le 4 \\
0, & \text{en otros casos}
\end{cases}$$

**Pregunta:** Halle la cantidad esperada condicional de las ventas, dado una cantidad inicial de $y$ galones.

---

## Slide 34 — Bibliografía complementaria

**Referencias:**

- **Estadística matemática con aplicaciones.** Wackerly, D; Mendenhall, W; Scheaffer, R. Cengage learning

- **Estadística para todos. Análisis de datos.** Eva Romero Ramos. Editorial Pirámide. Madrid, España.

**Figura:** Portadas de dos libros de referencia. Izquierda: "Estadística Matemática con Aplicaciones" (séptima edición) de Wackerly, Mendenhall, Scheaffer. Derecha: "Estadística para Todos" de Eva Romero Ramos, Editorial Pirámide.

---

## Slide 35 — Analítica descriptiva (Contexto general)

**Figura:** Diagrama de complejidad y niveles de análitica. Muestra la progresión desde "Información" (nivel más bajo, analítica descriptiva), pasando por "Optimización" (analítica prescriptiva) y diversos niveles de complejidad. Incluye subsecciones de:
- Analítica descriptiva: "¿Qué ha pasado?"
- Analítica diagnóstica: "¿Por qué ha pasado?"
- Analítica prescriptiva: "¿Qué se debe hacer?"
- Analítica predictiva: "¿Qué va a pasar?"

También presenta gráficos de distribuciones continuas y series de tiempo para ilustrar conceptos de modelado estadístico.

---

## Slide 36 — Página en blanco (Cierre)

Página en blanco con marca de agua "Alfredo Calderón" en esquina inferior derecha.
