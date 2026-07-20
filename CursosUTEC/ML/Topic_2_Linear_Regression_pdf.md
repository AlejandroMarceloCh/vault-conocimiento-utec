---
curso: ML
titulo: Topic 2 - Linear Regression
slides: 36
fuente: Topic 2 - Linear Regression.pdf
---

## Slide 1

**Figura:** Portada del deck. Fondo azul con un túnel/pasillo tecnológico y la silueta de una persona junto a un brazo robótico caminando por él.

LINEAR REGRESSION

## Slide 2

What should I watch?

**Figura:** Captura de pantalla de la página de IMDb de la película "The Martian" (2015). Muestra el póster "BRING HIM HOME - THE MARTIAN", la ficha (PG-13, 144 min, Adventure/Comedy/Drama, 2 October 2015 USA), la calificación 8.1/10 (271,829 users, Metascore 80/100), la sinopsis, Director: Ridley Scott, Writers: Drew Goddard (screenplay), Andy Weir (book), Stars: Matt Damon, Jessica Chastain, Kristen Wiig. Un círculo azul resalta el rating 8.1 con una flecha y el texto "Can we predict this?".

## Slide 3

How many followers will I get?

**Figura:** Captura de pantalla de un sitio de moda (estilo Chictopia) mostrando la foto de una influencer con chaqueta roja de cuero y leggings negros. Al costado se ven contadores: 282 VOTES (resaltado con un óvalo rojo), 5 COMMENTS, 67 FAVORITES, además de botones de Facebook Like, Tweet, G+1, Pinterest (2), y tags: Chic, Everyday, Winter.

## Slide 4

Predict the price of the house

**Figura:** Captura de pantalla del sitio "Nationwide House Price Index" (calculadora de precios de casas del Reino Unido). Muestra el menú superior (Why choose Nationwide?, Have your say, Corporate information, Media Policy & Legal, House Price Index, Investor relations), una foto de casas adosadas inglesas, pestañas (Headlines, House Price calculator, Report archive, Download data, Methodology) y la sección "House Price Calculator" con instrucciones: Property Value (ingresar el precio pagado o valoración reciente sin comas), Valuation Date 1 (fecha de compra o revaluación), Valuation Date 2 (fecha para la nueva estimación), Region (seleccionar región de la propiedad). Nota lateral: la calculadora ilustra movimientos generales de precios, se basa en el Nationwide House Price Index y en movimientos regionales, no en ciudades específicas.

## Slide 5

What do all these problems have in common?

**Figura:** Slide de transición con fondo degradado azul y comillas decorativas grandes de fondo, marcos punteados amarillos en las esquinas superior/inferior.

## Slide 6

1.
Regression
*Examples & Statistics*

**Figura:** Slide de sección/divisor. A la derecha, imagen de una mano robótica futurista señalando sobre un fondo de red/globo digital azul.

## Slide 7

REGRESSION aka Fitting Curves to Data

**Classification:** given point x, predict class (often binary)

**Regression:** given point x, predict a numerical value

**Figura:** Ícono de sol y nube con el texto "What will be the temperature tomorrow?" y debajo una recta numérica (escala de -50 a 230) en grados Fahrenheit, con una etiqueta señalando el valor "84°".

## Slide 8

REGRESSION aka Fitting Curves to Data

**Regression:** given point x, predict a **numerical value**

What do I need in order to predict **these outputs**?

**Figura:** A la izquierda, gráfico de dispersión titulado "Linear Regression between Sugar Levels and Blood Glucose Levels", eje X "Sugar Levels" (0 a 10), eje Y "Blood Glucose Levels" (-5 a 30), con puntos de datos (marcados como "Data", cruces azules) dispersos con tendencia creciente y una línea roja de regresión lineal ajustada ("Linear Regression"). A la derecha, tabla con dos columnas "Sugar Levels" y "Blood Glucose Levels" con los valores: 3.75→13.06, 9.51→24.62, 7.32→17.72, 5.99→13.46, 1.56→-3.49.

## Slide 9

REGRESSION aka Fitting Curves to Data

**Regression:** given point x, predict a **numerical value**

What do I need in order to predict **these outputs**?

**Figura:** Igual que en el slide 8 (gráfico de dispersión "Linear Regression between Sugar Levels and Blood Glucose Levels" con línea roja de ajuste), pero ahora la tabla de la derecha está encabezada explícitamente como "Input (x)" sobre "Sugar Levels" y "Output (y)" sobre "Blood Glucose Levels", con los mismos valores. Debajo de la tabla aparece la fórmula del modelo: $f(x) = mx + b$.

## Slide 10

REGRESSION aka Fitting Curves to Data

**Regression:** given point x, predict a **numerical value**

What do I need in order to predict **these outputs**?

**Figura:** Mismo gráfico de dispersión y tabla que el slide anterior (Input (x) = Sugar Levels, Output (y) = Blood Glucose Levels), con la fórmula $f(x) = mx + b$ y debajo la etiqueta "Model".

## Slide 11

REGRESSION aka Fitting Curves to Data

**Regression:** given point x, predict a **numerical value**

What do I need in order to predict **these outputs**?

Error?

**Figura:** Mismo gráfico de dispersión con la línea de regresión roja y la misma tabla Input (x)/Output (y). A la izquierda del gráfico se agrega el texto "Error?" como pregunta abierta. Debajo de la tabla: $f(x) = mx + b$, etiqueta "Model".

## Slide 12

REGRESSION aka Fitting Curves to Data

**Regression:** given point x, predict a **numerical value**

What do I need in order to predict **these outputs**?

Error

**Mean Squared Error**

$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \tilde{y}_i)^2$$

**Mean Absolute Error**

$$MAE = \frac{1}{N}\sum_{i=1}^{N}|y_i - \hat{y}_i|$$

**Figura:** Mismo gráfico de dispersión "Linear Regression between Sugar Levels and Blood Glucose Levels" con línea roja de regresión, y la misma tabla Input (x)/Output (y) a la derecha. Debajo: $f(x) = mx + b$, etiqueta "Model".

## Slide 13

REGRESSION aka Fitting Curves to Data

What do I need in order to predict **these outputs**?

**Least Squares Regression:** y = mx + b

$$m = \frac{N\sum(xy) - \sum x \sum y}{N\sum(x^2) - (\sum x)^2}$$

$$b = \frac{\sum y - m\sum x}{N}$$

**y = mx + b**

## Slide 14

Loss Function vs Metrics

*Simply put, loss function is for machines, and metric is for humans.*

Loss function is what the machine tries to minimize in order to optimize the machine learning model.

Metrics are utilized by people to evaluate the performance of machine learning models and has nothing to do with the optimization process.

**Can they be used interchangeably?**

A **loss function** can be used as a metric, but the opposite isn't always true.

This is due to an important characteristic of loss functions: they must be differentiable.

## Slide 15

Condition of a Metric

**Definition 7.1.** A metric $d$ on a set $X$ is a function $d: X \times X \to \mathbb{R}$ such that for all $x, y \in X$:

(1) $d(x,y) \geq 0$ and $d(x,y) = 0$ if and only if $x = y$;

(2) $d(x,y) = d(y,x)$ (symmetry);

(3) $d(x,y) \leq d(x,z) + d(z,x)$ (triangle inequality).

A metric space $(X,d)$ is a set $X$ with a metric $d$ defined on $X$.

*Metric spaces by UCDavis*

## Slide 16

Metrics for Regression

$$MAPE = \frac{1}{n}\sum_{i=1}^{n}\left|\frac{\widehat{y}_i - y_i}{y_i}\right| \times 100$$

$$RMSE = \sqrt{\frac{1}{n}\sum_{j=1}^{n}(y_j - \hat{y}_j)}$$

**R2 Squared** = $1 - \dfrac{SSr}{SSm}$

SSr = Squared sum error of regression line

SSm = Squared sum error of mean line

## Slide 17

2.
Linear Regression
*Machine Learning*

**Figura:** Slide de sección/divisor. A la derecha, misma imagen de la mano robótica futurista señalando sobre un fondo de red/globo digital azul del slide 6.

## Slide 18

REGRESSION aka Fitting Curves to Data

**Regression:** given point x, predict a **numerical value**

What do I need in order to predict **these outputs**?

Error

MSE?

MAE?

**Figura:** Mismo gráfico de dispersión "Linear Regression between Sugar Levels and Blood Glucose Levels" con línea roja de ajuste y la misma tabla Input (x)/Output (y). Debajo: $f(x) = ax + b \Rightarrow h(x) = wx + b$, etiqueta "Model".

## Slide 19

Regression

**Figura:** Diagrama de flujo. "Input" (izquierda) apunta con una flecha hacia un recuadro "Model" etiquetado arriba como "Student"; de "Model" sale una flecha hacia "Output"; de "Output" baja una flecha hacia un recuadro "Ground Truth" etiquetado abajo como "Teacher"; de la comparación entre Output y Ground Truth surge "Error", que retroalimenta con una flecha de vuelta hacia "Model". Debajo del diagrama, la pregunta: "How do we learn from the error?"

## Slide 20

Regression

**Figura:** Mismo diagrama de flujo que el slide 19 (Input → Model [Student] → Output → comparación con Ground Truth [Teacher] → Error → retroalimentación a Model). Debajo del diagrama, dos preguntas: "How do we learn from the error?" y "How do we define our objective?"

## Slide 21

# Regression

**Figura:** Diagrama de flujo. Un bloque "Model" (etiquetado arriba como "Student") recibe una flecha desde "Input" y emite una flecha hacia "Output". Desde "Output" sale una flecha diagonal hacia un bloque "Ground Truth" (etiquetado abajo como "Teacher"). Desde "Ground Truth" sale una flecha hacia la etiqueta "Error", y desde "Error" una flecha regresa hacia el bloque "Model", cerrando el ciclo de retroalimentación.

A la izquierda del diagrama:
How do we learn from the error?

How do we define our objective?

Minimize the error

Gradient Descent

## Slide 22

# Gradient Descent - Optimization

$\nabla_{\mathbf{x}} f(\mathbf{x}) = \left[\dfrac{\partial f(\mathbf{x})}{\partial x_1}, \dfrac{\partial f(\mathbf{x})}{\partial x_2}, \ldots, \dfrac{\partial f(\mathbf{x})}{\partial x_n}\right]^T$

$x_1 = x_1 - \alpha \dfrac{\partial f(x)}{\partial x_1}$   $x_2 = x_2 - \alpha \dfrac{\partial f(x)}{\partial x_2}$

**Figura:** Gráfico 2D de una función f(x) vs x, en el rango x de -1 a 2 y f(x) de -1 a 2. La curva muestra dos valles: un "local minimum" señalado con una flecha alrededor de x=-0.3, f(x)≈-0.2, y un "global minimum" señalado con una flecha alrededor de x=1.1, f(x)=-1.

**Figura:** Superficie 3D en forma de silla de montar (paraboloide hiperbólico) con ejes x, y (de -1 a 1) y eje vertical de -1 a 1. Se señala con una flecha un "saddle point" ubicado en el centro de la superficie, marcado con un punto rojo.

## Slide 23

# Gradient Descent

**Figura:** Recuadro naranja con pseudocódigo titulado "Algorithm 1 Gradient Descent":
1: procedure GD($\mathcal{D}$, $\boldsymbol{\theta}^{(0)}$)
2:     $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta}^{(0)}$
3:     while not converged do
4:         $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \gamma \nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta})$
5:     return $\boldsymbol{\theta}$

**Figura:** Gráfico 3D de una superficie convexa tipo "tazón" (paraboloide) con ejes numerados aproximadamente de -10 a 10, y un trazo de puntos/estrellas en magenta que desciende desde la parte alta de la superficie hasta el mínimo en el centro, ilustrando la trayectoria del descenso de gradiente.

$\nabla_{\mathbf{x}} f(\mathbf{x}) = \left[\dfrac{\partial f(\mathbf{x})}{\partial x_1}, \dfrac{\partial f(\mathbf{x})}{\partial x_2}, \ldots, \dfrac{\partial f(\mathbf{x})}{\partial x_n}\right]^T$

$x_1 = x_1 - \alpha \dfrac{\partial f(x)}{\partial x_1}$   $x_2 = x_2 - \alpha \dfrac{\partial f(x)}{\partial x_2}$

## Slide 24

# Stochastic Gradient Descent

**Figura:** Recuadro naranja con pseudocódigo titulado "Algorithm 1 Stochastic Gradient Descent (SGD)":
1: procedure SGD($\mathcal{D}$, $\boldsymbol{\theta}^{(0)}$)
2:     $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta}^{(0)}$
3:     while not converged do
4:         for $i \in$ shuffle($\{1, 2, \ldots, N\}$) do
5:             $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \gamma \nabla_{\boldsymbol{\theta}} J^{(i)}(\boldsymbol{\theta})$
6:     return $\boldsymbol{\theta}$

**Figura:** Gráfico de contorno 2D con ejes $\theta_0$ (horizontal, de -1000 a 2000) y $\theta_1$ (vertical, de -0.5 a 0.5), mostrando líneas de nivel elípticas concéntricas de distintos colores. Una trayectoria en magenta con marcadores en forma de estrella y rombo zigzaguea de manera errática desde la esquina superior derecha hacia el centro de las elipses, ilustrando el camino ruidoso característico del SGD.

$\nabla_{\mathbf{x}} f(\mathbf{x}) = \left[\dfrac{\partial f(\mathbf{x})}{\partial x_1}, \dfrac{\partial f(\mathbf{x})}{\partial x_2}, \ldots, \dfrac{\partial f(\mathbf{x})}{\partial x_n}\right]^T$

$x_1 = x_1 - \alpha \dfrac{\partial f(x)}{\partial x_1}$   $x_2 = x_2 - \alpha \dfrac{\partial f(x)}{\partial x_2}$

## Slide 25

# Linear Regression

Model Prediction / Output → $f(x) = y' = wx + b$

$y$   ← Ground Truth / Label

Minimize the error (MSE, MAE)

Loss = MSE = 1/n $\sum(f(x) - y)^2$

$w = w - \alpha \dfrac{\partial Loss}{\partial w}$

$b = b - \alpha \dfrac{\partial Loss}{\partial b}$

## Slide 26

# Linear Regression

Minimize the error (MSE, MAE)

Loss = MSE = 1/2n $\sum(f(x) - y)^2$

$w = w - \alpha \dfrac{\partial Loss}{\partial w} = w - \alpha \dfrac{1}{n}\sum(f(x)-y)x$

$b = b - \alpha \dfrac{\partial Loss}{\partial b} = b - \alpha \dfrac{1}{n}\sum(f(x)-y)$

## Slide 27

# Linear Regression

$L = xw + \boxed{b}$   $L = x\boxed{w} + b$   $L = x\boxed{w} + \boxed{b}$

**Figura:** Tres gráficos de dispersión idénticos en sus datos (puntos azules, eje x de -10.0 a 10.0, eje y de -20 a 20), cada uno con una recta de regresión azul distinta superpuesta, ilustrando el efecto de actualizar solo $b$ (primer gráfico, recta con pendiente similar a los datos pero desplazada), solo $w$ (segundo gráfico, recta con distinta pendiente) o ambos $w$ y $b$ (tercer gráfico, recta con pendiente e intercepto distintos), en relación al ajuste de la recta a la nube de puntos.

## Slide 28

# Multidimensional Linear Regression

Imagine now we want to predict the median house price from these **multi-dimensional** observations

Each house is a data point **n**, with observations indexed by **j**:

$\mathbf{x}^{(n)} = \left(x_1^{(n)}, \cdots, x_j^{(n)}, \cdots, x_d^{(n)}\right)$

We can incorporate the bias $w_0$ into $w$, by using $x_0 = 1$, then

$y(\mathbf{x}) = w_0 + \sum_{j=1}^{d} w_j x_j = \mathbf{w}^T\mathbf{x}$

We can then solve for w = $(w_0, w_1, \cdots, w_d)$. How?

## Slide 29

# Multidimensional Linear Regression

Imagine now we want to predict the median house price from these **multi-dimensional** observations

Each house is a data point **n**, with observations indexed by **j**:

$\mathbf{x}^{(n)} = \left(x_1^{(n)}, \cdots, x_j^{(n)}, \cdots, x_d^{(n)}\right)$

We can incorporate the bias $w_0$ into $w$, by using $x_0 = 1$, then

$y(\mathbf{x}) = w_0 + \sum_{j=1}^{d} w_j x_j = \mathbf{w}^T\mathbf{x}$

We can then solve for w = $(w_0, w_1, \cdots, w_d)$. How?

We can use gradient descent to solve for each **coefficient**, or compute **w** analytically (how does the solution change?)

## Slide 30

# Multidimensional Linear Regression

Imagine now we want to predict the median house price from these **multi-dimensional** observations

Each house is a data point **n**, with observations indexed by **j**:

$\mathbf{x}^{(n)} = \left(x_1^{(n)}, \cdots, x_j^{(n)}, \cdots, x_d^{(n)}\right)$

We can use gradient descent to solve for each **coefficient**, or compute **w** analytically (how does the solution change?)

$\vec{\beta} = (X^T X)^{-1} X^T \vec{y}$

$\begin{bmatrix}\beta_0 \\ \beta_1\end{bmatrix} = \begin{bmatrix} N & \sum X_i \\ \sum X_i & \sum x_i^2 \end{bmatrix}^{-1} \begin{bmatrix} \sum y \\ \sum X_i y_i \end{bmatrix}$

## Slide 31

3.

Linear Regression
*Example*

**Figura:** Imagen decorativa de fondo (mano robótica tocando un holograma de una red/globo digital) sin contenido textual adicional relevante.

## Slide 32

Home Exercise

https://www.mladdict.com/linear-regression-simulator

## Slide 33

# Home Exercise

**Figura:** Gráfico de dispersión titulado "Linear Regression between Sugar Levels and Blood Glucose Levels". Eje x "Sugar Levels" de 0 a 10, eje y "Blood Glucose Levels" de -5 a 30. Puntos azules marcados con "x" (leyenda "Data") dispersos con tendencia creciente, y una línea roja de regresión lineal ajustada (leyenda "Linear Regression") que cruza el eje y cerca de 0 y sube hasta aproximadamente 23 en x=10.

Tabla "Sugar Levels" / "Blood Glucose Levels":
3.75 / 13.06
9.51 / 24.62
7.32 / 17.72
5.99 / 13.46
1.56 / -3.49

$f(x) = wx + b$        $w = 0$        $b = 0$
                        $a = 0.1$

## Slide 34

# Home Exercise

$f(x) = wx + b$        $w = 0$        $b = 0$
                        $a = 0.1$

Tabla "Sugar Levels" / "Blood Glucose Levels":
3.75 / 13.06
9.51 / 24.62
7.32 / 17.72
5.99 / 13.46
1.56 / -3.49

## Slide 35

More Exercises?

MACHINE LEARNING WORKOUT: Chapter 5

## Slide 36

**Figura:** Imagen decorativa de fondo (dos personas con bata de laboratorio y lentes de protección observando un dispositivo mecánico/robótico) sin contenido textual adicional relevante.
