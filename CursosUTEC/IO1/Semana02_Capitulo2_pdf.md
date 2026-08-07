---
curso: IO1
titulo: Semana02-Capitulo2
slides: 26
fuente: Semana02-Capitulo2.pdf
---

## Slide 1

Portada. "Investigación de operaciones I" / "Capítulo 2: Introducción a la programación lineal". Logo UTEC y pie de página con crédito del profesor (decorativa).

## Slide 2

**Planta de cemento: condiciones de producción**

- Una planta produce dos tipos de cemento: **cemento 1** y **cemento 2**.
- La **utilidad por tonelada** es de $50 para el cemento 1, y $70 para el cemento 2.
- Para producir una tonelada del cemento 1, se necesitan 40 minutos de **calcinación** y 20 minutos de **trituración**.
- Para producir una tonelada del cemento 2, se necesitan 30 minutos de **calcinación** y 30 minutos de **trituración**.
- El horno y el triturador son disponibles 6 horas y 8 horas por día respectivamente.

## Slide 3

**Planta de cemento: problema**

¿Cuánto cemento de cada tipo deberíamos producir cada día para **maximizar la utilidad**?

## Slide 4

**Planta de cemento: modelamiento**

- El problema se modela con un **programa lineal**.
- La respuesta del problema son dos cantidades: la cantidad de cada tipo de cemento por producir cada día.
- Denotamos por $x_1$ la cantidad de cemento 1, y por $x_2$ la cantidad 2.

## Slide 5

**Planta de cemento: programa lineal**

1. Las variables $x_1$ y $x_2$ se llaman: **variables de decisión** (o simplemente: **variables**).
2. Escribimos lo que queremos hacer, la **función objetivo**:

$$\max \quad z = 50x_1 + 70x_2$$

3. Escribimos las **restricciones**:

$$40x_1 + 30x_2 \le 360$$
$$20x_1 + 30x_2 \le 480$$
$$x_1, x_2 \ge 0$$

## Slide 6

**Planta de cemento: programa lineal**

Los valores (50, 70) de la función objetivo, (40, 30, 360) de la primera restricción y (20, 30, 480) de la segunda restricción se llaman: **parámetros**.

## Slide 7

**Programa matemático**

- De manera general, llamamos **programa matemático** un problema de optimización de una función objetivo con variables y restricciones.
- Decimos que el programa es **lineal** si la función objetivo y las restricciones son todas **combinaciones lineales** de las variables de decisión.

## Slide 8

**Forma algebraica de un programa matemático**

El problema de cemento se puede reescribir de manera más general para cualquier número de cementos y cualquier número de procesos.

- Definimos un conjunto $C$ de cementos: $C = \{1, 2, \ldots, |C|\}$.
- Definimos un conjunto $P$ de procesos: $P = \{1, 2, \ldots, |P|\}$.

## Slide 9

**Forma algebraica de un programa matemático**

- Definimos los parámetros:
  - $u_i$: Utilidad por tonelada del cemento $i \in C$.
  - $r_{ij}$: Tiempo de proceso $j \in P$ para producir una tonelada de cemento $i \in C$.
  - $R_j$: Tiempo disponible por día para el proceso $j \in P$.
- Definimos las variables de decisión:
  - $x_i$: Cantidad de cemento $i$ por producir cada día.

## Slide 10

**Forma algebraica de un programa matemático**

$$\max \quad z = \sum_{i \in C} u_i x_i$$
$$\text{s.t.} \quad \sum_{i \in C} r_{ij} x_i \le R_j \quad, \forall j \in P$$
$$x_i \ge 0 \quad, \forall i \in C.$$

Es la forma que se utiliza generalmente. Utilizaremos esa forma en las sesiones de laboratorio para resolver los problemas de optimización con Julia y JuMP.

## Slide 11

**Forma genérica de un programa matemático**

- La forma genérica de un programa lineal tiene:
  - $n$ variables **no-negativas**.
  - $m$ restricciones de igualdad o de desigualdad.
  - una función objetivo por optimizar
- El parámetro (coeficiente) de costo (o de utilidad) de la variable $x_j$ se denota por $c_j$.
- El coeficiente de la variable $x_j$ en la restricción $i$ se denota por $a_{ij}$.
- La restricción $i$ tiene un segundo término constante $b_i$.
- Las restricciones simples de **no-negatividad** no son parte de las $m$ restricciones (los algoritmos las tratan a parte).

## Slide 12

**Forma genérica de un programa matemático de maximización**

$$\max \quad z = \sum_{j=1}^{n} c_j x_j$$
$$\text{s.t.} \quad \sum_{j=1}^{n} a_{ij} x_j \le b_i \quad \forall i \in \{1, \ldots, m\}$$
$$x_j \ge 0 \quad \forall j \in \{1, \ldots, n\}$$

## Slide 13

**Forma genérica de un programa matemático de minimización**

$$\min \quad z = \sum_{j=1}^{n} c_j x_j$$
$$\text{s.t.} \quad \sum_{j=1}^{n} a_{ij} x_j \ge b_i \quad \forall i \in \{1, \ldots, m\}$$
$$x_j \ge 0 \quad \forall j \in \{1, \ldots, n\}$$

## Slide 14

**Forma genérica de un programa matemático**

- Una solución que satisface **todas** las restricciones (como $x_1 = 4$ y $x_2 = 2$ en el ejemplo del cemento) se llama: *solución* **factible**.
- Si ninguna otra solución es mejor que una solución factible, es una *solución* **óptima**.
- A cualquier solución corresponde un valor de la función objetivo: un *valor* **objetivo**.
- A una solución óptima corresponde el *valor* **óptimo** de la función objetivo.

## Slide 15

**Forma genérica de un programa matemático**

- Si todas las variables tienen la restricción de ser enteras, el programa matemático se llama: **programa lineal entero** (en inglés: *Integer Program*).
- Un caso particular es cuando todas las variables son binarias (0 ó 1), se llama: **programa lineal binario**.
- Un programa que tiene a la vez variables continuas y variables enteras se llama: **programa lineal mixto**.
- Si al menos una restricción o la función objetivo no es una combinación lineal de variables, tenemos un **programa no-lineal**.

## Slide 16

**Forma genérica de un programa matemático**

- Los programas lineales enteros, binarios y mixtos son más difíciles que los programas lineales.
- Los programas no-lineales son aún más difíciles, excepto por unos casos específicos, como por ejemplo cuando las funciones objetivos son convexas.

## Slide 17

**¿Programa lineal?**

$$\max \quad z = x_1 + x_2$$
$$\text{s.t.} \quad x_1 \ge x_2$$
$$x_1 \le 60 - 3x_2$$
$$x_1, x_2 \ge 0.$$

(Slide de pregunta/ejercicio: evaluar si esta formulación es un programa lineal — es un caso válido, sirve de referencia base para las variaciones de las slides siguientes.)

## Slide 18

**¿Cuál es el problema con esa formulación?**

$$\max \quad z = x_1 + x_2$$
$$\text{s.t.} \quad x_1 > x_2$$
$$x_1 < 60 - 3x_2$$
$$x_1, x_2 \ge 0.$$

Variante del ejemplo con desigualdades **estrictas** ($>$, $<$) en vez de $\ge$/$\le$ — el problema es que las desigualdades estrictas no definen una región factible cerrada válida para programación lineal (no hay óptimo garantizado alcanzable en el borde).

## Slide 19

**¿Programa lineal?**

$$\max \quad z = x_1 + x_2$$
$$\text{s.t.} \quad x_1^2 \ge x_2$$
$$x_1 \le 60 - 3x_2$$
$$x_1, x_2 \ge 0.$$

Variante con $x_1^2$ (término cuadrático) — rompe la linealidad de la restricción.

## Slide 20

**¿Programa lineal?**

$$\max \quad z = x_1 + x_2$$
$$\text{s.t.} \quad |x_1| \ge 30$$
$$x_1 \le 60 - 3x_2$$
$$x_1, x_2 \ge 0.$$

Variante con valor absoluto $|x_1|$ — no es una combinación lineal.

## Slide 21

**¿Programa lineal?**

$$\max \quad z = x_1 + x_2$$
$$\text{s.t.} \quad x_1 \ge |u|$$
$$x_1 \le v - 3x_2$$
$$x_1, x_2 \ge 0.$$

Con **parámetros** $u$ y $v$. Nota: el valor absoluto está sobre el parámetro $u$ (no sobre la variable), lo cual es distinto al caso de la slide 20.

## Slide 22

**¿Programa lineal?**

$$\max \quad z = x_1 + x_2$$
$$\text{s.t.} \quad x_1 \ge \sqrt{u}$$
$$x_1 \le v - 3x_2$$
$$x_1, x_2 \ge 0.$$

Con **parámetros** $u$ y $v$. Variante con raíz cuadrada sobre el parámetro $u$.

## Slide 23

**Forma matricial clásica**

Denotamos por:

- $x = (x_1, x_2, \ldots, x_n)^T$ el vector de variables,
- $b = (b_1, b_2, \ldots, b_m)^T$ el vector de segundos términos de las restricciones,
- $c = (c_1, c_2, \ldots, c_n)^T$ el vector de coeficientes asociadas a las variables de la función objetivo,
- $A$ la matriz de los coeficientes $a_{ij}$ de tamaño $m \times n$.

## Slide 24

**Forma matricial clásica**

Podemos escribir un programa lineal en forma matricial de dos maneras. Tabla comparativa:

| Forma estándar | Forma canónica |
|---|---|
| max $c^T x$ | max $c^T x$ |
| s.t. $Ax \le b$ | s.t. $Ax = b$ |
| $x \ge 0$ | $x \ge 0$ |

Esas formas matriciales se utilizan principalmente en presentaciones teóricas para simplificar las notaciones.

## Slide 25

**Comentarios importantes**

- En la realidad un programa lineal puede tener igualdades y desigualdades.
- Podemos siempre convertir una restricción de igualdad con dos restricciones de desigualdad.

## Slide 26

**Comentarios importantes**

- Podemos convertir una restricción de desigualdad en una restricción de igualdad con una nueva variable (lo veremos más tarde).
- También podemos convertir un programa de maximización en un programa de minimización: Para minimizar una función objetivo $z$, maximizamos la función objetivo $-z$ conservando las mismas restricciones. Si el valor óptimo del programa de maximización es $z^*$ entonces el valor óptimo del programa de minimización es $-z^*$.
- Una variable sin restricción de no-negatividad (se llama: variable **libre**) se puede escribir como la diferencia de dos variables no-negativas.
