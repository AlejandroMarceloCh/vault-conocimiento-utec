---
curso: ML
titulo: Topic 3 - Linear SVM
slides: 32
fuente: Topic 3 - Linear SVM.pdf
---

## Slide 1

**SUPPORT VECTOR MACHINE**

**Figura:** Imagen decorativa de portada — silueta de una persona junto a un brazo/mano robótica, sobre un fondo de túnel circular tecnológico azul con líneas y patrones de circuito. No contiene datos técnicos.

## Slide 2

# Lesson Objectives

1. Recap on logistic regression and optimization
2. Understand the intuition and math behind linear SVM
3. Learn how soft-margin SVM handles imperfect separation
4. Implement a basic linear SVM from scratch

## Slide 3

**1.**

**Logistic Regression**
*Recap*

**Figura:** Imagen decorativa — mano robótica señalando un globo terráqueo digital, sin contenido técnico.

## Slide 4

# Logistic Regression

What is the optimization objective?

$$\max_{\mathbf{w}} L(\mathbf{w}) = \max_{\mathbf{w}} \prod_{i=1}^{N} p(t^{(i)}|\mathbf{x}^{(i)};\mathbf{w})$$

$$p(t^{(i)}|\mathbf{x}^{(i)};\mathbf{w}) = p(C=1|\mathbf{x}^{(i)};\mathbf{w})^{t^{(i)}} p(C=0|\mathbf{x}^{(i)};\mathbf{w})^{1-t^{(i)}}$$

$$= \left(1 - p(C=0|\mathbf{x}^{(i)};\mathbf{w})\right)^{t^{(i)}} p(C=0|\mathbf{x}^{(i)};\mathbf{w})^{1-t^{(i)}}$$

$$p(C=0|\mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x} + w_0) \quad \text{with} \quad \sigma(z) = \frac{1}{1+\exp(-z)}$$

x(i) = sample i from the training set

t(i) = target (ground truth) i from the training set

## Slide 5

# Decision Boundary for Logistic Regression

What is the decision boundary for logistic regression?

Decision boundary: $\mathbf{w}^T\mathbf{x} + w_0 = 0$

Logistic regression has a **linear decision boundary**

**Figura:** Gráfico con eje X de -8 a 8 y eje Y de 0 a 1.1. Dos curvas sigmoides simétricas: la curva roja p(C=0|x) va de 0 (izquierda) a 1 (derecha); la curva azul p(C=1|x) va de 1 (izquierda) a 0 (derecha). Se cruzan en x≈-1, donde p(C=0|x)=p(C=1|x)=0.5, marcado con una línea vertical punteada negra etiquetada "w x + w0=0 (decision boundary)" y una línea horizontal punteada en y=0.5.

## Slide 6

# Decision Boundary for Logistic Regression

What is the decision boundary for logistic regression?

**Figura:** Diagrama de dispersión con puntos rojos (clase 1) agrupados en la parte superior izquierda y puntos azules (clase 2) agrupados en la parte inferior derecha. Se muestran varias líneas discontinuas negras candidatas a frontera de decisión, señaladas con el texto "Many more possible classifiers". Una línea roja sólida particular se destaca cerca de los puntos azules, señalada con el texto "Line closer to the blue nodes since many of them are far away from the boundary".

## Slide 7

**Cita destacada (fondo azul degradado):**

"How can we choose the best decision boundary?"

## Slide 8

**2.**

**Support Vector Machines**
*Linear SVM*

**Figura:** Imagen decorativa — mano robótica señalando un globo terráqueo digital, sin contenido técnico (misma imagen que slide 3).

## Slide 9

# Support Vector Machines (SVM)

**Figura:** Recta numérica horizontal etiquetada "Mass (g):" con un grupo de círculos grises (puntos de datos) agrupados en dos clusters a lo largo de la línea, con flechas apuntando hacia ellos desde el texto: "Let's start by imagining we measured the mass of a bunch of mice…"

## Slide 10

# Support Vector Machines (SVM)

**Figura:** Misma recta numérica "Mass (g):" ahora con el cluster izquierdo coloreado en rojo y el cluster derecho en verde, separados por una línea vertical naranja gruesa (umbral). Una flecha señala el umbral con el texto: "Based on these observations, we can pick a threshold…"

## Slide 11

# Support Vector Machines (SVM)

**Figura:** Recta numérica "Mass (g):" con fondo sombreado en rosa (zona "not obese"/clase roja, izquierda) y verde (zona clase verde, derecha), separadas por una línea vertical naranja. Los puntos originales están en rosa/verde clarito, y aparece un nuevo punto negro justo a la derecha del umbral, dentro de la zona verde pero muy cerca de la frontera. Texto: "However, what if get a new observation here?" y "But that doesn't make sense, because it is much closer to the observations that are **not obese**."

## Slide 12

# Support Vector Machines (SVM)

**Figura:** Arriba, la misma recta numérica con fondos rosa/verde y línea naranja de umbral; el punto nuevo ahora aparece coloreado en verde justo al lado del umbral, con flecha y texto: "So this threshold is pretty lame." Abajo, una segunda recta numérica "Mass (g):" muestra los mismos puntos ahora coloreados completamente en rojo (izquierda) y verde (derecha), sin sombreado de fondo, representando los datos de entrenamiento originales sin el punto ambiguo.

## Slide 13

# Support Vector Machines (SVM)

**Figura:** Recta numérica "Mass (g):" con fondo rosa/verde. El punto más a la derecha del cluster rojo y el punto más a la izquierda del cluster verde están resaltados con contorno negro grueso (rojo sólido y verde sólido respectivamente). Una línea vertical naranja marca el punto medio entre ambos, señalada con flecha y texto: "…and use the midpoint between them as the threshold."

## Slide 14

# Support Vector Machines (SVM)

**Figura:** Misma configuración que la slide anterior (puntos límite resaltados rojo y verde, línea naranja de umbral en el punto medio), pero ahora se añaden marcas de distancia: un segmento punteado rojo desde el punto rojo límite hasta el umbral, y un segmento punteado verde desde el punto verde límite hasta el umbral, ambos etiquetados con flechas hacia el texto: "The shortest distance between the observations and the threshold is called the **margin**."

## Slide 15

# Max Margin Classification?

- Instead of fitting all the points, **focus on the boundary points**
- Aim: learn a boundary that leads to the **largest margin** (buffer) from points on **both sides**
- **Why:** intuition; theoretical support; and works well in practice
- Subset of vectors that support (determine boundary) are called the **support vectors**

**Figura:** Diagrama de dispersión 2D con puntos rojos agrupados arriba a la izquierda y puntos azules agrupados abajo a la derecha. Una línea discontinua negra diagonal separa ambas clases. Se destacan dos puntos (uno rojo, uno azul) más cercanos a la frontera, unidos por segmentos verdes en zigzag etiquetados "D" y "D", representando la distancia (margen) desde cada clase hasta la línea de decisión.

## Slide 16

# Support Vector Machines (SVM)

- **Supervised learning** once again!
- We are given **training** data {(x(i),t(i))}Ni=1
- We will look at classification, so t(i) will represent the **class label**
- We will focus on **binary classification** (two classes)
- We will consider a **linear classifier** first (next class **non-linear decision boundaries**)
- **Tiny change** from before: instead of using t = 1 and t = 0 for positive and negative class, we will use t = 1 for the positive and t = −1 for the negative class

## Slide 17

# What is the "Best" Hyperplane?

**Max margin classifier:** Maximum distance between classes

**Figura:** Gráfico 2D con ejes x1 (horizontal) y x2 (vertical). Puntos azules agrupados arriba a la izquierda, puntos verdes agrupados abajo a la derecha. Una franja amarilla diagonal representa el margen entre dos líneas discontinuas paralelas: la superior etiquetada $w*x-b=1$ (en azul), la inferior etiquetada $w*x-b=-1$ (en verde), y la línea roja central etiquetada $w*x-b=0$ (el hiperplano de decisión). Se marcan con contorno negro los puntos soporte (uno azul y uno verde) que tocan las líneas del margen. Un vector $w$ perpendicular al hiperplano se dibuja desde el origen. Se indica la distancia entre las líneas de margen como $\frac{2}{\|w\|}$, y la distancia del origen al hiperplano central como $\frac{b}{\|w\|}$.

## Slide 18

# Distance between hyperplanes

A **hyperplane** is a set

$$\{x : a^Tx = b\},$$

where $a \in \mathbf{R}^n$ is nonzero and $b \in \mathbf{R}$. The vector $a$ is referred to as the normal vector of the hyperplane, since, if $x_0$ is any point such that $a^Tx_0 = b$, the hyperplane can be expressed as

$$\{x : a^T(x - x_0) = 0\}.$$

The Euclidean projection of a point $x_0$ onto the hyperplane $\{x : a^Tx = b\}$ is

$$x^\star = x_0 + (b - a^Tx_0)a/\|a\|^2.$$

## Slide 19

# Distance between hyperplanes

Consider two parallel hyperplanes $H_1 = \{x : a^Tx = b_1\}$ and $H_2 = \{x : a^Tx = b_2\}$. The distance between the hyperplanes can be computed by projecting any point $x_0$ in the former hyperplane onto the latter hyperplane. In particular, the projection of $x_0 \in H_1$ onto $H_2$ is

$$x_1 = x_0 + (b_2 - a^Tx_0)a/\|a\|^2 = x_0 + (b_2 - b_1)a/\|a\|^2.$$

Hence the distance between the two hyperplanes is

$$\|x_1 - x_0\| = \|(b_2 - b_1)a/\|a\|^2\| = \frac{|b_2 - b_1|}{\|a\|}.$$

## Slide 20

# Learning a Margin-Based Classifier

We can search for the optimal parameters (**w** and **b**) by finding a solution that:

1. Correctly classifies the training examples: {(x(i),t(i))}Ni=1
2. Maximizes the margin (same as minimizing wTw)

**Figura:** Diagrama con tres líneas paralelas diagonales: la roja superior etiquetada "wTx+b=+1" con el texto "Predict class +1"; la línea negra central etiquetada "wTx+b=0"; la línea azul inferior etiquetada "wTx+b=-1" con el texto "Predict class -1".

$$\min_{\mathbf{w},b} \frac{1}{2}\|\mathbf{w}\|^2$$

$$s.t. \, \forall i \quad (\mathbf{w}^T\mathbf{x}^{(i)} + b)t^{(i)} \geq 1,$$

Can optimize via projective **gradient descent**, etc.

## Slide 21

# Learning a Linear SVM

$\text{Loss}(w, b) = \frac{1}{2}\|w\|^2 + \sum_i \max(0, 1 - (w^T x^{(i)} + b)t^{(i)})$

1. **We fix $\alpha_i$ to be implicitly encoded via the hinge loss:**

hinge loss: $\max(0, 1 - t^{(i)}(w^T x^{(i)} + b))$

2. This hinge loss can be derived by **maximizing the expression over $\alpha_i \geq 0$:**

$\max_{\alpha_i \geq 0} \alpha_i[1 - t^{(i)} f(x^{(i)})] = \begin{cases} 0 & \text{if } 1 - t^{(i)} f(x^{(i)}) \leq 0 \\ \infty & \text{if } \alpha_i \to \infty \text{ and } 1 - t^{(i)} f(x^{(i)}) > 0 \end{cases}$

But to make it **finite and differentiable**, we just directly replace that constraint with hinge loss:

$\Rightarrow \sum_i \max(0, 1 - t^{(i)} f(x^{(i)}))$

## Slide 22

# Real World Isn't Perfect…

**Figura:** Recta numérica "Mass (g):" con marcas de escala. A la izquierda hay 5 puntos rosados (clase "not obese") agrupados, luego un espacio, y a la derecha 6 puntos verdes (clase "obese") agrupados. Entre ambos grupos hay un punto rojo (resaltado) que está clasificado como "not obese" pero posicionado mucho más cerca del grupo de puntos verdes ("obese"). Una flecha señala ese punto rojo con el texto: "…and we had an outlier observation that was classified as **not obese**, but was much closer to the **obese** observations."

## Slide 23

# Real World Isn't Perfect…

**Figura:** Misma recta numérica "Mass (g):". Se muestran dos regiones sombreadas: una rosada (izquierda, zona "not obese") y una verde (derecha, zona "obese"), separadas por una línea vertical naranja gruesa (el hiperplano/frontera). El punto outlier (rojo, con borde negro) queda justo a la izquierda de la línea naranja, dentro de un recuadro punteado verde junto con los puntos verdes ("obese"). Debajo se marcan dos distancias con corchetes: una roja pequeña (margen hacia el punto rojo) y una verde (margen hacia los puntos verdes agrupados), con una flecha que apunta a ese conjunto y el texto: "In this case, the **Maximum Margin Classifier** would be super close to the **obese** observations…"

## Slide 24

# Real World Isn't Perfect…

**Figura:** Misma recta numérica "Mass (g):". Ahora todos los puntos a la izquierda de la línea naranja (incluido el outlier) están en rojo, y todos los de la derecha en verde, con las dos regiones sombreadas (rosada y verde) separadas exactamente por la línea vertical naranja gruesa, que pasa justo pegada al punto outlier. Una flecha señala la línea naranja con el texto: "So **Maximal Margin Classifiers** are *super sensitive to outliers* in the training data and that makes them pretty lame."

## Slide 25

# Real World Isn't Perfect…

**Figura:** Misma recta numérica "Mass (g):" con las dos regiones sombreadas (rosada y verde) separadas por la línea naranja gruesa. Se resaltan con borde negro dos puntos: uno rojo (el outlier, a la izquierda de la línea naranja, dentro de la región rosada) y uno verde (a la derecha de la línea naranja, dentro de la región verde, el más cercano al límite). Debajo, dos corchetes punteados miden distancias: uno rojo (margen del punto rojo a la línea naranja) y uno verde (margen del punto verde a la línea naranja). Dos flechas convergen señalando ambos corchetes, con el texto: "So the question is 'How do we know that this **soft margin**…"

## Slide 26

# Real World Isn't Perfect…

**Figura:** Idéntica a la slide 25 (misma recta, mismas dos regiones sombreadas, mismos dos puntos resaltados con borde negro —uno rojo y uno verde— y los mismos dos corchetes punteados de margen), pero ahora el texto de la slide anterior aparece atenuado (gris) y se agrega, en un globo de diálogo, la continuación: "…is better than this **Soft Margin**?"

## Slide 27

# Real World Isn't Perfect…

**Introduce slack variables ξi**

$\min \frac{1}{2}\|\mathbf{w}\|^2 + \lambda \sum_{i=1}^{N} \xi_i$

s.t. $\xi_i \geq 0; \quad \forall i \quad t^{(i)}(\mathbf{w}^T \mathbf{x}^{(i)} + b) \geq 1 - \xi_i$

- Example lies on wrong side of hyperplane $\xi_i > 1$
- Therefore $\sum \xi_i$ upper bounds the number of training errors
- λ trades off training error vs model complexity
- This is known as the soft-margin extension

**Figura:** Gráfico de dispersión 2D con dos clases de puntos (rojos y azules) y tres rectas paralelas discontinuas etiquetadas "+1 plane" (roja), la frontera de decisión central (negra, sin etiqueta directa pero entre ambas) y "-1 plane" (azul). Varios puntos rojos y azules caen del lado incorrecto o dentro del margen; se marcan dos segmentos de distancia perpendiculares a las líneas, etiquetados $\varepsilon_k$ (para un punto azul mal ubicado, en el lado de "+1 plane") y $\varepsilon_j$ (para un punto rojo mal ubicado, cerca de "-1 plane"), representando las variables de holgura (slack) de esos dos ejemplos.

## Slide 28

# How does decision boundary look like?

https://ml-visualizer.herokuapp.com/

## Slide 29

4.
**Support Vector Machines**
*Hands-on Activity*

## Slide 30

# Implement Linear SVM

Notebook in canvas

## Slide 31

# Further Reading and Resources

- Bishop, "Pattern Recognition and Machine Learning", Chapter 7.
- Shalev-Shwartz, "Understanding Machine Learning", Chapter 15.
- Cristianini, "An Introduction to Support Vector Machines".

## Slide 32

**Figura:** Imagen de fondo con tono azul superpuesto mostrando a dos personas con bata de laboratorio y lentes de protección observando de cerca un equipo/mecanismo con brazos metálicos articulados (aparenta ser un robot o dispositivo mecánico de laboratorio). No hay texto de contenido en esta slide (solo elementos decorativos de marca).
