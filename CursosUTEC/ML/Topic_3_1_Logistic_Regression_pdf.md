---
curso: ML
titulo: Topic 3.1 - Logistic Regression
slides: 46
fuente: Topic 3.1 - Logistic Regression.pdf
---

## Slide 1

LOGISTIC REGRESSION

**Figura:** Imagen de portada decorativa: silueta de un robot humanoide caminando dentro de un túnel digital azul, con marcas de escala tipo regla en la parte inferior. No aporta contenido técnico.

## Slide 2

Lesson Objectives

1. Learn how logistic regression models the probability of binary outcomes.

2. Derive the logistic regression model using likelihood.

3. Interpret model coefficients and evaluate classification performance.

## Slide 3

1. Classification Task
Introduction

**Figura:** Imagen decorativa de portada de sección: mano robótica señalando sobre un mapa digital del mundo, con marcas de escala tipo regla al costado.

## Slide 4

Classification Task

Grasshoppers | Katydids

**Figura:** Gráfico de dispersión con eje X "Abdomen Length" (1 a 10) y eje Y "Antenna Length" (1 a 10). Puntos morados (Grasshoppers) ubicados en la zona de abdomen corto (1-3) con antena de longitud variable (1-6), agrupados en la esquina inferior izquierda. Puntos rojos con patrón rayado (Katydids) ubicados en la zona de abdomen largo (6-9) con antena de longitud media-alta (5-10), agrupados en la esquina superior derecha. A los costados se muestran ilustraciones de saltamontes (grasshoppers, izquierda) y katydids (derecha) con flechas que conectan cada ilustración a su punto correspondiente en el gráfico.

## Slide 5

Classification Task

With a lot of data, we can build a histogram

**Figura:** Mismo gráfico de dispersión Abdomen Length (eje X, 1-10) vs Antenna Length (eje Y, 1-10), ahora con muchos más puntos: morados (Grasshoppers) concentrados en abdomen 1-4, antena 1-7; rojos rayados (Katydids) concentrados en abdomen 6-10, antena 4-10. A la derecha, un histograma horizontal de "Antenna Length" que muestra la distribución de frecuencias de cada clase (rojo arriba, morado/azul abajo), con leyenda "Katydids" (rojo) y "Grasshoppers" (morado).

## Slide 6

Classification Task

We can leave the histograms as they are, or we can summarize them with two normal distributions.

**Figura:** Arriba, un histograma de barras con dos distribuciones superpuestas: barras rojas (a la izquierda) y barras moradas/azules (a la derecha), con cierto solapamiento en el centro.

Let us us two normal distributions for ease of visualization in the following slides…

**Figura:** Abajo, dos curvas de densidad normal (campanas de Gauss) suavizadas: una roja centrada más a la izquierda y una morada centrada más a la derecha, con una zona de solapamiento entre ambas.

## Slide 7

Classification Task

We want to classify an insect we have found. Its antennae are 3 units long. **How can we classify it?**

**Figura:** Dos curvas de densidad normal superpuestas (roja a la izquierda, morada a la derecha) sobre un eje horizontal, con una flecha vertical señalando el punto "3" en el eje. Debajo, ilustración de un saltamontes con la etiqueta "Antennae length is 3".

## Slide 8

Classification Task

We want to classify an insect we have found. Its antennae are 3 units long. **How can we classify it?**

**Figura:** Mismas dos curvas de densidad normal (roja y morada) con flecha señalando el punto "3", e ilustración del insecto con "Antennae length is 3".

We can just ask ourselves, give the distributions of antennae lengths we have seen, is it more probable that our insect is a **Grasshopper** or a **Katydid**.

## Slide 9

Classification Task

We want to classify an insect we have found. Its antennae are 3 units long. **How can we classify it?**

**Figura:** Mismas dos curvas de densidad normal (roja y morada) con flecha señalando el punto "3" e ilustración del insecto con "Antennae length is 3".

There is a formal way to discuss the most probable classification…

$p(c_i | d)$ = probability of class $c_i$, given that we have observed $d$

## Slide 10

Classification Task

$p(c_i | d)$ = probability of class $c_i$, given that we have observed $d$

P(**Grasshopper** | **3**) = 10 / (10 + 2) = 0.833
P(**Katydid** | **3**) = 2 / (10 + 2) = 0.166

**Figura:** Dos curvas de densidad normal (roja izquierda, morada derecha) con una línea vertical en el punto "3" del eje horizontal. Se marcan los valores de altura de cada curva en ese punto: la curva morada alcanza el valor 10 y la curva roja alcanza el valor 2, indicados con flechas verticales a la derecha del gráfico. Debajo, ilustración del insecto con "Antennae length is 3".

## Slide 11

Classification Task

$p(c_i | d)$ = probability of class $c_i$, given that we have observed $d$

P(**Grasshopper** | **7**) = 3 / (3 + 9) = 0.250
P(**Katydid** | **7**) = 9 / (3 + 9) = 0.750

**Figura:** Dos curvas de densidad normal (roja izquierda, morada derecha) con línea vertical en el punto "7". En ese punto, la curva roja alcanza el valor 9 y la curva morada alcanza el valor 3, indicados con flechas verticales a la derecha. Debajo, ilustración de un insecto con "Antennae length is 7".

## Slide 12

Classification Task

$p(c_i | d)$ = probability of class $c_i$, given que we have observed $d$

P(**Grasshopper** | **5**) = 6 / (6 + 6) = 0.500
P(**Katydid** | **5**) = 6 / (6 + 6) = 0.500

**Figura:** Dos curvas de densidad normal (roja izquierda, morada derecha) que se cruzan justo en el punto "5" del eje horizontal, donde ambas alcanzan el mismo valor de altura (6 y 6), marcado con flechas verticales a la derecha. Debajo, ilustración de un insecto con "Antennae length is 5".

## Slide 13

2. Logistic Regression
Formalization

**Figura:** Imagen decorativa de portada de sección: mano robótica señalando sobre un mapa digital del mundo, con marcas de escala tipo regla al costado (misma imagen de fondo que la slide 3).

## Slide 14

Logistic Regression

An alternative: replace the $sign(\cdot)$ with the **sigmoid** or **logistic** function

We assumed a particular functional form: sigmoid applied to a linear function of the data

$y(\mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x} + w_0)$

where the sigmoid is defined a

$\sigma(z) = \dfrac{1}{1+\exp(-z)}$

**Figura:** Gráfico de la función sigmoide: eje Y "y" de 0 a 1, eje X "z" centrado en 0. Curva en forma de S que parte cerca de 0 para z negativo, cruza y=0.5 en z=0, y se acerca a 1 para z positivo.

The output is a smooth function of the inputs and the weights. It can be seen as a **smoothed and differentiable** alternative to $sign(\cdot)$

## Slide 15

Logistic Regression

We assumed a particular functional form: sigmoid applied to a linear function of the data

$y(\mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x} + w_0)$

where the sigmoid is defined a

$\sigma(z) = \dfrac{1}{1+\exp(-z)}$

➔ One parameter per data dimension (feature) and the bias

➔ Features can be discrete or continuous

➔ Output of the model: value y ∈ [0, 1]

➔ Allows for gradient-based learning of the parameter

## Slide 16

Shape of the Logistic Function

Let's look at how modifying **w** changes the shape of the function

**1D example**

$y = \sigma(w_1 x + w_0)$

**Figura:** Tres gráficos de la función sigmoide en 1D con distintos parámetros, eje X de -6 a 6 y eje Y de 0 a 1:
- $w_0 = 0, w_1 = 1$: curva en S centrada en x=0, con pendiente pronunciada (transición rápida).
- $w_0 = 0, w_1 = 0.5$: curva en S centrada en x=0, con pendiente más suave (transición gradual, más extendida).
- $w_0 = -2, w_1 = 1$: curva en S desplazada hacia la derecha, centrada aproximadamente en x=2, con pendiente similar a la primera.

## Slide 17

Probabilistic Interpretation

If we have a value between 0 and 1, let's use it to model class probability

$p(C=0|\mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x} + w_0)$ with $\sigma(z) = \dfrac{1}{1+\exp(-z)}$

Substituting we have

$p(C=0|\mathbf{x}) = \dfrac{1}{1+\exp(-\mathbf{w}^T\mathbf{x} - w_0)}$

Suppose we have two classes, how can I compute p(C = 1|x)?
Use the marginalization property of probability

$p(C=1|\mathbf{x}) + p(C=0|\mathbf{x}) = 1$

Thus

$p(C=1|\mathbf{x}) = 1 - \dfrac{1}{1+\exp(-\mathbf{w}^T\mathbf{x} - w_0)} = \dfrac{\exp(-\mathbf{w}^T\mathbf{x} - w_0)}{1+\exp(-\mathbf{w}^T\mathbf{x} - w_0)}$

## Slide 18

Decision Boundary for Logistic Regression

What is the **decision boundary** for logistic regression?

$p(C=1|\mathbf{x}, \mathbf{w}) = p(C=0|\mathbf{x}, \mathbf{w}) = 0.5$

$p(C=0|\mathbf{x}, \mathbf{w}) = \sigma(\mathbf{w}^T\mathbf{x} + w_0) = 0.5$, where $\sigma(z) = \dfrac{1}{1+\exp(-z)}$

Decision boundary: $\mathbf{w}^T\mathbf{x} + w_0 = 0$

Logistic regression has a **linear decision boundary**

**Figura:** Gráfico con eje X de -8 a 8 y eje Y de 0 a 1.1. Dos curvas sigmoides: una roja etiquetada p(C=0|x) que crece de 0 a 1 de izquierda a derecha, y una azul etiquetada p(C=1|x) que decrece de 1 a 0. Ambas curvas se cruzan en el punto donde p(C=0|x) = p(C=1|x) = 0.5, marcado con una línea horizontal punteada en y=0.5 y una línea vertical discontinua etiquetada "w x + w0=0 (decision boundary)" señalada con una flecha.

## Slide 19

How does decision boundary look like?

https://ml-visualizer.herokuapp.com/

## Slide 20

Logistic Regression vs Least Squares Regression

If the right answer is 1 and the model says 1.5, it loses, so it changes the boundary to avoid being "too correct" (tilts away from outliers)

**Figura:** Dos gráficos de dispersión lado a lado, eje X de -4 a 8/9 y eje Y de -8 a 4, con dos clases de puntos: cruces rojas (clase 1) agrupadas en la zona superior izquierda, y círculos azules (clase 2) agrupados en el centro.
- Gráfico izquierdo: una línea verde (logistic regression) y una línea magenta (least squares regression) casi superpuestas, ambas separando razonablemente las dos clases.
- Gráfico derecho: se añade un grupo adicional de círculos azules atípicos (outliers) en la esquina inferior derecha (x≈7-9, y≈-5 a -7). La línea verde (logistic regression) mantiene su posición casi sin cambios, mientras que la línea magenta (least squares regression) se inclina notablemente hacia esos outliers, degradando la separación entre clases.

## Slide 21

# Example

**Problem:** Given the number of hours a student spent learning, will (s)he pass the exam?

Training data (top row: x(i), bottom row: t(i))

**Figura:** Tabla de datos de entrenamiento con dos filas. Fila "Hours": 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50. Fila "Pass": 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1.

Learn **w** for our model, i.e., logistic regression (**coming up**)

**Figura:** Gráfico "Probability of passing exam versus hours of studying". Eje X: horas de estudio (1 a 5.5). Eje Y: "Probability of passing exam" (0.00 a 1.00). Puntos negros en y=0 e y=1 muestran los datos de entrenamiento (fallar/aprobar). Una curva sigmoide azul asciende de cerca de 0 (pocas horas) a cerca de 1 (muchas horas), pasando por 0.5 alrededor de 2.7-3 horas. Junto al gráfico, una tabla "Hours of study" vs "Probability of passing exam": 1 → 0.07, 2 → 0.26, 3 → 0.61, 4 → 0.87, 5 → 0.97.

## Slide 22

# Learning?

➔ When we have a d-dim input x ∈ $\mathbb{R}^d$

➔ How should we learn the weights w = $(w_0, w_1, \cdots, w_d)$?

➔ We have a probabilistic model

➔ Let's use maximum likelihood

## Slide 23

# Conditional Likelihood

Assume t ∈ {0, 1}, we can write the probability distribution of each of our training points $p(t^{(1)}, \cdots, t^{(N)}|x^{(1)}, \cdots, x^{(N)}; w)$

Assuming that the training examples are sampled **IID**: independent and identically distributed, we can write the *likelihood function*:

$$L(\mathbf{w}) = p(t^{(1)}, \cdots, t^{(N)}|\mathbf{x}^{(1)}, \cdots \mathbf{x}^{(N)}; \mathbf{w}) = \prod_{i=1}^{N} p(t^{(i)}|\mathbf{x}^{(i)}; \mathbf{w})$$

We can write each probability as (will be useful later):

$$p(t^{(i)}|\mathbf{x}^{(i)}; \mathbf{w}) = p(C=1|\mathbf{x}^{(i)}; \mathbf{w})^{t^{(i)}} p(C=0|\mathbf{x}^{(i)}; \mathbf{w})^{1-t^{(i)}}$$

$$= \left(1 - p(C=0|\mathbf{x}^{(i)}; \mathbf{w})\right)^{t^{(i)}} p(C=0|\mathbf{x}^{(i)}; \mathbf{w})^{1-t^{(i)}}$$

## Slide 24

# Conditional Likelihood

$$p(t^{(i)}|\mathbf{x}^{(i)}; \mathbf{w}) = p(C=1|\mathbf{x}^{(i)}; \mathbf{w})^{t^{(i)}} p(C=0|\mathbf{x}^{(i)}; \mathbf{w})^{1-t^{(i)}}$$

$$= \left(1 - p(C=0|\mathbf{x}^{(i)}; \mathbf{w})\right)^{t^{(i)}} p(C=0|\mathbf{x}^{(i)}; \mathbf{w})^{1-t^{(i)}}$$

We can learn the model by **maximizing the likelihood**

$$\max_{\mathbf{w}} L(\mathbf{w}) = \max_{\mathbf{w}} \prod_{i=1}^{N} p(t^{(i)}|\mathbf{x}^{(i)}; \mathbf{w})$$

Easier to maximize the log likelihood ***log(L(w))***

## Slide 25

# Loss Function

$$L(\mathbf{w}) = \prod_{i=1}^{N} p(t^{(i)}|\mathbf{x}^{(i)}) \quad \text{(likelihood)}$$

$$= \prod_{i=1}^{N} \left(1 - p(C=0|\mathbf{x}^{(i)})\right)^{t^{(i)}} p(C=0|\mathbf{x}^{(i)})^{1-t^{(i)}}$$

We can convert the maximization problem into minimization so that we can write the **loss function**:

$$\ell_{log}(\mathbf{w}) = -\log L(\mathbf{w})$$

$$= -\sum_{i=1}^{N} \log p(t^{(i)}|\mathbf{x}^{(i)}; \mathbf{w})$$

$$= -\sum_{i=1}^{N} t^{(i)} \log(1 - p(C=0|\mathbf{x}^{(i)}, \mathbf{w})) - \sum_{i=1}^{N} (1-t^{(i)}) \log p(C=0|\mathbf{x}^{(i)}; \mathbf{w})$$

## Slide 26

# Gradient Descent

$$\min_{\mathbf{w}} \ell(\mathbf{w}) = \min_{\mathbf{w}} \left\{ -\sum_{i=1}^{N} t^{(i)} \log(1 - p(C=0|\mathbf{x}^{(i)}, \mathbf{w})) - \sum_{i=1}^{N} (1-t^{(i)}) \log p(C=0|\mathbf{x}^{(i)}, \mathbf{w}) \right\}$$

Gradient descent: iterate and at each iteration compute steepest direction towards optimum, move in that direction, step-size λ

$$w_j^{(t+1)} \leftarrow w_j^{(t)} - \lambda \frac{\partial \ell(\mathbf{w})}{\partial w_j}$$

You can write this in vector form

$$\nabla \ell(\mathbf{w}) = \left[\frac{\partial \ell(\mathbf{w})}{\partial w_0}, \cdots, \frac{\partial \ell(\mathbf{w})}{\partial w_k}\right]^T, \quad \text{and} \quad \Delta(\mathbf{w}) = -\lambda \nabla \ell(\mathbf{w})$$

But where is **w**?

$$p(C=0|\mathbf{x}) = \frac{1}{1+\exp(-\mathbf{w}^T\mathbf{x}-w_0)}, \quad p(C=1|\mathbf{x}) = \frac{\exp(-\mathbf{w}^T\mathbf{x}-w_0)}{1+\exp(-\mathbf{w}^T\mathbf{x}-w_0)}$$

## Slide 27

# Compute the Updates

The loss is

$$\ell_{log-loss}(\mathbf{w}) = -\sum_{i=1}^{N} t^{(i)} \log p(C=1|\mathbf{x}^{(i)}, \mathbf{w}) - \sum_{i=1}^{N} (1-t^{(i)}) \log p(C=0|\mathbf{x}^{(i)}, \mathbf{w})$$

where the probabilities are

$$p(C=0|\mathbf{x}, \mathbf{w}) = \frac{1}{1+\exp(-z)} \qquad p(C=1|\mathbf{x}, \mathbf{w}) = \frac{\exp(-z)}{1+\exp(-z)}$$

$$z = \mathbf{w}^T\mathbf{x} + w_0$$

**We can simplify**

$$\ell(\mathbf{w})_{log-loss} = \sum_i t^{(i)} \log(1+\exp(-z^{(i)})) + \sum_i t^{(i)} z^{(i)} + \sum_i (1-t^{(i)}) \log(1+\exp(-z^{(i)}))$$

$$= \sum_i \log(1+\exp(-z^{(i)})) + \sum_i t^{(i)} z^{(i)}$$

## Slide 28

# Updates

$$\ell(\mathbf{w}) = \sum_i t^{(i)} z^{(i)} + \sum_i \log(1+\exp(-z^{(i)}))$$

Now it's easy to take derivatives

Remember **z = w$^T$x + w$_0$**

$$\frac{\partial \ell}{\partial w_j} = \sum_i \left(t^{(i)} x_j^{(i)} - x_j^{(i)} \cdot \frac{\exp(-z^{(i)})}{1+\exp(-z^{(i)})}\right)$$

What's $x_j^{(i)}$? The j-th dimension of the i-th training example $x^{(i)}$, and simplifying

$$\frac{\partial \ell}{\partial w_j} = \sum_i x_j^{(i)} \left(t^{(i)} - p(C=1|\mathbf{x}^{(i)}; \mathbf{w})\right)$$

*j* for the weight that we are updating and *i* for the training example

## Slide 29

# Gradient Descent

Putting it all together (plugging the update into gradient descent).

Gradient descent for logistic regression:

$$w_j^{(t+1)} \leftarrow w_j^{(t)} - \lambda \sum_i x_j^{(i)} \left(t^{(i)} - p(C=1|\mathbf{x}^{(i)}; \mathbf{w})\right)$$

where:

$$p(C=1|\mathbf{x}^{(i)}; \mathbf{w}) = \frac{\exp(-\mathbf{w}^T\mathbf{x}-w_0)}{1+\exp(-\mathbf{w}^T\mathbf{x}-w_0)} = \frac{1}{1+\exp(\mathbf{w}^T\mathbf{x}+w_0)}$$

This is all there is to learning in logistic regression.

## Slide 30

# Regularization?

$$L(\mathbf{w}) + \lambda\|\mathbf{w}\|^2$$

(la llave roja debajo señala este término como "Cross Entropy Loss")

Cross Entropy Loss

$$L(\mathbf{w}) + \lambda R(\mathbf{w})$$

(la llave roja debajo de R(w) indica las opciones de término de regularización)

L1
L2
ElasticNet

## Slide 31

# 3. Classification Metrics

How good are our results?

**Figura:** Diapositiva de portada de sección con fondo dividido: a la izquierda el número "3." y el título "Classification / Metrics" (con ícono de clipboard); a la derecha una imagen decorativa de una mano robótica tocando una proyección holográfica de un globo terráqueo digital, sobre fondo azul oscuro con líneas de datos y elementos gráficos decorativos (líneas punteadas naranjas y celestes).

## Slide 32

# How good are our results?

$$Error(x) = Bias^2 + Variance + Error\ Irreductible$$

**Figura:** Cuatro diagramas de "diana" (blanco de tiro) en cuadrícula 2x2, cada uno ilustrando una combinación de sesgo (bias) y varianza:
- Arriba-izquierda: puntos muy agrupados en el centro (bias bajo, varianza baja) — etiqueta "Bias: Low/High, Variance: Low/High".
- Arriba-derecha: puntos dispersos pero centrados alrededor del blanco (bias bajo, varianza alta) — misma etiqueta genérica.
- Abajo-izquierda: puntos agrupados pero lejos del centro, en la parte superior del blanco (bias alto, varianza baja).
- Abajo-derecha: puntos dispersos y lejos del centro, en la parte superior (bias alto, varianza alta).
Cada diana tiene anillos concéntricos celestes/blancos con un círculo rojo central representando el valor objetivo verdadero.

## Slide 33

# Confusion Matrix

**Figura:** Diagrama con dos partes. Izquierda "Predictions": dos grupos de íconos de sobres de correo. Grupo "0 - Not Spam" (12 sobres, la mayoría en verde/oliva = predicciones correctas, uno en gris = incorrecta). Grupo "1 - Spam" (4 sobres: 2 grises/incorrectos, 1 verde/correcto, 1 gris/incorrecto). Leyenda: verde = "Correct predictions", gris = "Incorrect predictions". Derecha "Confusion Matrix": tabla 2x2 con eje "Prediction" (0, 1) en columnas y "Actual" (0, 1) en filas: TN=14 (verde), FP=3 (gris), FN=2 (gris), TP=1 (verde). Flechas conectan los sobres de cada grupo hacia las celdas correspondientes de la matriz.

## Slide 34

# Generalization?

**Figura:** Tres gráficos de dispersión 2D (ejes X1, X2) con dos clases de puntos (círculos rojos y cruces verdes) y una frontera de decisión (línea punteada negra):
- Izquierda "Underfitting (high bias)": frontera es una línea recta que separa mal las clases, dejando puntos rojos y verdes mezclados en ambos lados.
- Centro "Good compromise": frontera curva que separa razonablemente bien las dos clases.
- Derecha "Overfitting (high variance)": frontera muy sinuosa e irregular que rodea puntos individuales, ajustándose excesivamente al ruido de los datos.

## Slide 35

# Accuracy

$$\frac{\text{Num. of correct predictions}}{\text{Total num. of predictions}}$$

**Figura:** Fórmula de accuracy aplicada al ejemplo: (TN=14 + TP=1) dividido entre (TN=14 + TP=1 + FN=2 + FP=3), igual a 75%. Los recuadros TN y TP están en verde/oliva, FN y FP en gris.

## Slide 36

# Accuracy

**Figura:** Representación visual de la matriz de confusión como un área proporcional (tipo mosaico): un gran cuadrado verde/oliva grande etiquetado "TN 14" ocupa la mayor parte del área; a su derecha un rectángulo gris pequeño "FP 3"; debajo, un rectángulo gris "FN 2" y un rectángulo verde/oliva pequeño "TP 1". El tamaño de cada bloque es proporcional al valor numérico, ilustrando visualmente el peso de cada categoría dentro del total.

## Slide 37

# Precision

$$\frac{\text{True Positives (TP)}}{\text{True Positives (TP) + False Positives (FP)}}$$

**Figura:** Izquierda, matriz de confusión reducida a la columna de predicción "1": FP=3 (gris) arriba, TP=1 (verde) abajo, con ejes "Prediction" (0,1) y "Actual" (0,1). Una flecha lleva a la fórmula: TP=1 dividido entre (TP=1 + FP=3), igual a 25%.

## Slide 38

# Recall

$$\frac{\text{True Positives (TP)}}{\text{True Positives (TP) + False Negatives (FN)}}$$

**Figura:** Izquierda, matriz de confusión reducida a la fila "Actual=1": FN=2 (gris) a la izquierda, TP=1 (verde) a la derecha, con ejes "Prediction" (0,1) y "Actual" (0,1). Una flecha lleva a la fórmula: TP=1 dividido entre (TP=1 + FN=2), igual a 33%.

## Slide 39

# Precision vs Recall

**Figura:** Dos matrices de confusión comparativas.
"Scenario A — High Precision, Low Recall": TN=14, FP=1, FN=4, TP=1. Un óvalo celeste resalta FN=4 con nota "More spam emails went undetected". Debajo: Precision: 50%, Recall: 20%.
"Scenario B — High Recall, Low Precision": TN=14, FP=4, FN=1, TP=1. Un óvalo celeste resalta FP=4 con nota "More non-spam emails flagged as spam". Debajo: Precision: 20%, Recall: 50%.

## Slide 40

# F1 score

$$\frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 \times 25\% \times 33\%}{25\% + 33\%} = 28\%$$

**Figura:** Recta horizontal etiquetada "F1" con un marcador (bloque verde/oliva) situado ligeramente a la izquierda del centro. Extremo izquierdo etiquetado "High Precision / Low Recall", extremo derecho etiquetado "Low Precision / High Recall". El marcador F1 se ubica más cerca del extremo izquierdo, indicando la posición del score calculado (28%) en el espectro precision-recall.

## Slide 41

4.

Logistic Regression
*Hands-on Activity*

## Slide 42

# Implement Logistic Regression

**Problem:** Given the number of hours a student spent learning, will (s)he pass the exam?

Training data (top row: $x^{(i)}$, bottom row: $t^{(i)}$)

| Hours | 0.50 | 0.75 | 1.00 | 1.25 | 1.50 | 1.75 | 1.75 | 2.00 | 2.25 | 2.50 | 2.75 | 3.00 | 3.25 | 3.50 | 4.00 | 4.25 | 4.50 | 4.75 | 5.00 | 5.50 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |

Learn **w** para nuestro modelo, i.e., logistic regression (**coming up**)

**Figura:** Gráfico de dispersión titulado "Probability of passing exam versus hours of studying". Eje X: horas de estudio (0 a aprox. 5.5). Eje Y: "Probability of passing exam" (0.00 a 1.00). Puntos negros en y=0 e y=1 representan los datos de entrenamiento (fail/pass). Curva azul en forma de S (sigmoide) ajustada sobre los puntos, que sube suavemente desde cerca de 0 (pocas horas) hasta cerca de 1 (muchas horas), cruzando aproximadamente 0.5 alrededor de 2.5-3 horas.

Tabla anexa "Hours of study" vs "Probability of passing exam":
| Hours of study | Probability of passing exam |
|---|---|
| 1 | 0.07 |
| 2 | 0.26 |
| 3 | 0.61 |
| 4 | 0.87 |
| 5 | 0.97 |

## Slide 43

# Logistic Regression

**Advantages**

➔ Easily extended to multiple classes (thoughts?)
➔ Natural probabilistic view of class predictions
➔ Quick to train
➔ Fast at classification
➔ Good accuracy for many simple data sets
➔ Resistant to overfitting
➔ Can interpret model coefficients as indicators of feature importance

**Less good:**

➔ Linear decision boundary (too simple for more complex problems?)

## Slide 44

# Final Takeaways

1. Logistic regression models probabilities using the sigmoid function and produce a linear decision boundary

2. It's based on maximizing the likelihood of the observed data

3. Interpretable, fast to train, resistant to overfitting, and widely used in real-world applications

4. Model predictions are evaluated using accuracy, precision, recall and f1 score

## Slide 45

# Further Reading and Resources

- Bishop, "Pattern Recognition and Machine Learning", Chapter 4.

- Murphy, "Machine Learning: A Probabilistic Perspective", Chapter 8.

- Mitchell, "Machine Learning", Chapter 6.

## Slide 46

**Figura:** Fotografía de fondo (con overlay azul) de dos estudiantes con bata de laboratorio y lentes de protección observando un equipo/mecanismo con rieles y componentes electrónicos, en un laboratorio. Sin texto adicional en la slide (slide de cierre/transición).
