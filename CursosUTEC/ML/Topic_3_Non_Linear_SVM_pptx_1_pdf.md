---
curso: ML
titulo: Topic 3 - Non Linear SVM.pptx-1
slides: 36
fuente: Topic 3 - Non Linear SVM.pptx-1.pdf
---

## Slide 1

SUPPORT VECTOR MACHINE

**Figura:** Imagen decorativa de portada — silueta de un robot humanoide de pie visto desde atrás, dentro de un túnel circular futurista azul con líneas de estructura tipo red. No aporta contenido técnico.

## Slide 2

Lesson Objectives

1. Understand complexities of nonlinear input spaces
2. Learn how feature maps transform nonlinear input spaces
3. Discover the power of kernel tricks in non-linear classification
4. Explore feature mappings from different scenarios

## Slide 3

1.

Support Vector Machines

*Linear SVM*

**Figura:** Slide separadora de sección con número "1.", ícono de portapapeles/checklist, título "Support Vector Machines" y subtítulo "Linear SVM". A la derecha, imagen decorativa de una mano robótica señalando un holograma de un globo terráqueo digital.

## Slide 4

Support Vector Machines (SVM)

**Figura:** Recta numérica horizontal etiquetada "Mass (g):" con una fila de círculos grises (puntos de datos) distribuidos en dos grupos, uno a la izquierda y otro a la derecha, con una marca divisoria vertical entre ambos. Flechas apuntan desde el texto "Let's start by imagining we measured the mass of a bunch of mice…" hacia varios de los puntos centrales.

## Slide 5

Support Vector Machines (SVM)

**Figura:** Misma recta numérica "Mass (g):" ahora con dos grupos de puntos coloreados: rosa/rojo a la izquierda y verde a la derecha, separados por una línea umbral naranja vertical. Un punto rojo con borde negro y un punto verde con borde negro (los más cercanos al umbral) tienen líneas punteadas rojas y verdes respectivamente que miden su distancia al umbral. Texto: "The shortest distance between the observations and the threshold is called the **margin**."

## Slide 6

What is the "Best" Hyperplane?

Max margin classifier: Maximum distance between classes

**Figura:** Gráfico de dispersión 2D con ejes $x_1$ (horizontal) y $x_2$ (vertical). Puntos azules (clase 1) en la parte superior izquierda, puntos verdes (clase 2) en la parte inferior derecha. Una línea roja diagonal etiquetada $w*x-b=0$ representa el hiperplano separador. Dos líneas discontinuas paralelas a cada lado, etiquetadas $w*x-b=1$ y $w*x-b=-1$, delimitan la banda del margen (sombreada en amarillo claro). Se destacan con borde negro los puntos de cada clase más cercanos al hiperplano (los vectores de soporte). Se indica el vector $w$ perpendicular al hiperplano, la distancia del origen al hiperplano como $b/\|w\|$, y el ancho total del margen como $2/\|w\|$.

## Slide 7

Learning a Linear SVM

$Loss(w, b) = \frac{1}{2}\|w\|^2 + \sum_i \max(0, 1-(w^Tx^{(i)}+b)t^{(i)})$

1. **We fix $\alpha_i$ to be implicitly encoded via the hinge loss**:

hinge loss: $\max(0, 1-t^{(i)}(w^Tx^{(i)}+b))$

2. This hinge loss can be derived by **maximizing the expression over $\alpha_i \geq 0$**:

$\max_{\alpha_i \geq 0} \alpha_i[1-t^{(i)}f(x^{(i)})] = \begin{cases} 0 & \text{if } 1-t^{(i)}f(x^{(i)}) \leq 0 \\ \infty & \text{if } \alpha_i \to \infty \text{ and } 1-t^{(i)}f(x^{(i)}) > 0 \end{cases}$

But to make it **finite and differentiable**, we just directly replace that constraint with hinge loss:

$\Rightarrow \sum_i \max(0, 1-t^{(i)}f(x^{(i)}))$

## Slide 8

Real World Isn't Perfect…

**Figura:** Recta numérica "Mass (g):" con dos regiones sombreadas (rosa a la izquierda, verde a la derecha) separadas por un umbral naranja. Los puntos siguen el mismo patrón de la Slide 5, con un punto rojo y un punto verde marcados con borde negro y sus distancias medidas por líneas punteadas rojas y verdes. Texto: "So the question is 'How do we know that this **soft margin**…'"

## Slide 9

Real World Isn't Perfect…

**Figura:** Igual que la Slide 8, pero los puntos de datos aparecen atenuados/transparentes (excepto los dos marcados). Un globo de diálogo tipo cómic contiene el texto completo: "So the question is 'How do we know that this **soft margin**… …is better than this **Soft Margin**?'" — indicando que se compara un soft margin con otro.

## Slide 10

Support Vector Machines

**Figura:** Texto "Dosages measured in a bunch of patients." con flechas apuntando hacia una recta numérica etiquetada "Dosage (mg):". Los puntos muestran un patrón intercalado: rojo, rojo, rojo, rojo, luego un grupo de puntos verdes en el centro, luego rojo, rojo, rojo — es decir, los puntos verdes (una clase) están rodeados por puntos rojos (otra clase) a ambos lados, ejemplo de datos no separables linealmente en 1D.

## Slide 11

Support Vector Machines

**Figura:** Recta numérica "Dosage (mg):" con puntos rojos y verdes intercalados de la misma forma que la Slide 10 (verdes al centro, rojos rodeándolos a ambos extremos, con un punto rojo aislado a la derecha). Encima, un gráfico de dispersión con eje y "y-axis Dosage²" (el cuadrado de la dosis) muestra los mismos puntos proyectados: los rojos forman una curva ascendente en ambos extremos y los verdes se agrupan en valores bajos al centro. Una línea diagonal punteada magenta separa ambas clases en este nuevo espacio transformado. Texto: "…we could draw a line the separated the two categories of patients."

## Slide 12

Input Transformation

**Figura:** Dos paneles lado a lado. Izquierda: "Input space" — gráfico 2D con puntos azules (cuadrados) y rojos (círculos) mezclados y no separables por una línea recta (se traza una curva no lineal negra que los separa). Derecha: "Feature space" — tras aplicar la transformación $\varphi(.)$ (indicada con una flecha amarilla), los mismos puntos ahora aparecen etiquetados como $\varphi(\blacksquare)$ y $\varphi(\bullet)$ y quedan separables por una línea recta diagonal.

Mapping to a feature space can produce problems:
- High computational burden due to high dimensionality
- Many more parameters

## Slide 13

2.

Support Vector Machines

*Non Linear SVM*

**Figura:** Slide separadora de sección con número "2.", ícono de portapapeles/checklist, título "Support Vector Machines" y subtítulo "Non Linear SVM". A la derecha, la misma imagen decorativa de la mano robótica señalando el holograma del globo terráqueo digital.

## Slide 14

What if …

**Figura:** Recta numérica horizontal con eje $x_1$, con marcas en -1, 0 y 1. Puntos rojos (símbolo "-") ocupan los extremos (valores muy negativos y muy positivos de $x_1$) y puntos azules (símbolo "+") ocupan la región central alrededor de 0, no separables por un único punto de corte lineal (los rojos están a ambos lados de los azules).

## Slide 15

What if …

**Figura:** Dos paneles. Izquierda: la misma recta numérica de la Slide 14 con eje $x_1$, puntos rojos en los extremos y azules al centro. Derecha (tras una flecha celeste): gráfico de dispersión con eje x $x_1$ y eje y $x_1^2$ (dosage al cuadrado), donde los puntos ahora forman una parábola: los azules (bajos valores de $x_1^2$) quedan cerca del mínimo (centro) y los rojos (altos valores de $x_1^2$) quedan arriba, permitiendo trazar una línea horizontal que los separa.

## Slide 16

What if …

**Figura:** Gráfico de dispersión 2D con ejes $x_1$ y $x_2$. Puntos azules (símbolo "+") forman un pequeño clúster circular en el centro del plano. Puntos rojos (símbolo "-") forman un anillo/círculo grande alrededor del clúster azul, rodeándolo completamente — ejemplo clásico de datos concéntricos no separables linealmente en 2D.

## Slide 17

What if …

**Figura:** Dos paneles. Izquierda: mismo gráfico de la Slide 16 con ejes $x_1$, $x_2$ — azules en clúster central, rojos formando anillo circular alrededor. Derecha (tras flecha celeste): gráfico transformado con eje x $r = \sqrt{x_1^2+x_2^2}$ (radio) y eje y $\theta$ (ángulo). Los puntos azules quedan agrupados en valores bajos de $r$ (cerca de 1) y los puntos rojos en valores altos de $r$ (cerca de 5), separables ahora por una línea vertical entre ambos grupos, independientemente del valor de $\theta$.

## Slide 18

Support Vector Machines

Dual form of the optimization problem

$\underset{x,y}{\text{maximize}} \quad f(x,y)$
$\text{subject to} \quad g(x,y)=0.$

$\min_{w,b} \frac{1}{2}\|w\|^2$
$s.t. \forall i \quad (w^Tx^{(i)}+b)t^{(i)} \geq 1,$

$J(w, b; \alpha) = \frac{1}{2}\|w\|^2 + \sum_{i=1}^{N} \alpha_i[1-(w^Tx^{(i)}+b)t^{(i)}]$

## Slide 19

Support Vector Machines

Dual form of the optimization problem

$\max_{\alpha_i \geq 0} \min_{w,b} J(w,b;\alpha) = \max_{\alpha_i \geq 0} \min_{w,b} \frac{1}{2}\|w\|^2 + \sum_{i=1}^{N} \alpha_i[1-(w^Tx^{(i)}+b)t^{(i)}]$

$\frac{\partial J(w,b;\alpha)}{\partial w} = w - \sum_{i=1}^{N} \alpha_i x^{(i)} t^{(i)} = 0 \qquad w = \sum_{i=1}^{N} \alpha_i t^{(i)} x^{(i)}$

$\frac{\partial J(w,b;\alpha)}{\partial b} = -\sum_{i=1}^{N} \alpha_i t^{(i)} = 0$

Then substitute back to get final optimization:

$L = \max_{\alpha_i \geq 0}\{\sum_{i=1}^{N} \alpha_i - \frac{1}{2}\sum_{i,j=1}^{N} t^{(i)}t^{(j)}\alpha_i\alpha_j(x^{(i)^T} \cdot x^{(j)})\}$

## Slide 20

Support Vector Machines

Dual form of the optimization problem

$L = \max_{\alpha_i \geq 0}\{\sum_{i=1}^{N} \alpha_i - \frac{1}{2}\sum_{i,j=1}^{N} t^{(i)}t^{(j)}\alpha_i\alpha_j(x^{(i)^T} \cdot x^{(j)})\}$

But why are we doing this????
(why not just solve the original problem????)

Because this will let us solve the problem by computing the just the inner products of $x^i$, $x^j$ (which will be very important later on when we want to solve non-linearly separable classification problems)

## Slide 21

# Support Vector Machines

So we used a **Support Vector Machine** with a **Polynomial Kernel** to compute the relationships between the observations in a higher dimension…

**Figura:** Recta numérica horizontal "Dosage (mg):" con puntos rojos y verdes (dos clases) ubicados en distintas dosis. Sobre ella, un eje vertical etiquetado "y-axis / Dosage²". Flechas punteadas grises salen de los puntos sobre la recta y ascienden hacia arriba y a la derecha, elevando cada punto a una nueva posición según su dosis al cuadrado: los puntos rojos (clase negativa, dosis bajas y una dosis alta) se proyectan más alto y a la derecha, formando un arco; los puntos verdes (clase positiva, dosis intermedias) se proyectan formando una curva ascendente más baja. Una flecha punteada negra grande conecta dos de los puntos rojos elevados mostrando el arco que los separaría de los verdes, ilustrando cómo el kernel polinomial separa las clases al llevarlas a una dimensión superior.

## Slide 22

# Support Vector Machines

$(a \times b + r)^d = (a \times b)^d = a^d b^d = (a^d) \cdot (b^d)$

When **r = 0**, the **Polynomial Kernel** simplifies to a single term…

…and that gives us a **Dot Product** with a single coordinate.

**Figura:** Recta numérica horizontal "Dosage (mg):" con un punto rojo y un punto verde muy cercanos entre sí cerca del origen, y marcas de graduación vacías a la derecha (sin otros puntos resaltados).

## Slide 23

# Support Vector Machines

When **r = 0**… $(a \times b + r)^d = (a \times b)^d = a^d b^d = (a^d) \cdot (b^d)$ (en gris, atenuado)

When **d = 2** we get… $a^2b^2 = (a^2) \cdot (b^2)$ (el término $(a^2)\cdot(b^2)$ resaltado con un recuadro rojo)

…which is equal to the **Dot Product** of **a²** and **b²**.

**Figura:** Misma recta numérica "Dosage (mg):" con un punto rojo y un punto verde cercanos al origen; una flecha curva negra conecta la fórmula "When d = 2" con el término encuadrado en rojo, y otra flecha señala desde el recuadro hacia el texto de la explicación del producto punto.

## Slide 24

# Support Vector Machines

When **r = 0**… $(a \times b + r)^d = (a \times b)^d = a^d b^d = (a^d) \cdot (b^d)$

When **d = 1** we get… $a^1b^1 = (a) \cdot (b)$ (en gris, atenuado)

When **d = 2** we get… $a^2b^2 = (a^2) \cdot (b^2)$ (en gris, atenuado)

When **d = 3** we get… $a^3b^3 = (a^3) \cdot (b^3)$

So, setting **r = 0** seems silly because no matter what values we use for **d**, the **Dot Products** leave the data in the original dimension…

**Figura:** Misma recta numérica "Dosage (mg):" con un punto rojo y un punto verde cercanos al origen; flechas curvas negras conectan las fórmulas de "r = 0" y "d = 3" con el texto explicativo, formando una V que converge en la frase sobre los productos punto.

## Slide 25

# Support Vector Machines

$a^1b^1 + a^2b^2 = (a, a^2) \cdot (b, b^2)$

Now we can plot the transformed data on **x/y-axes**…

**Figura:** Eje vertical "y-axis / Dosage²" y eje horizontal "Dosage (mg):". Los puntos originales (rosados/verdes claros, atenuados) están sobre el eje horizontal. Puntos rojos (clase negativa) y verdes (clase positiva) más oscuros/saturados aparecen elevados en el plano x/y siguiendo una trayectoria curva ascendente: los rojos correspondientes a dosis bajas y a una dosis alta se ubican en distintas alturas, mientras los verdes (dosis intermedias) forman una curva ascendente suave más a la derecha, mostrando la transformación a 2 dimensiones mediante el mapeo $(a, a^2)$.

## Slide 26

# Support Vector Machines

$a^1b^1 + a^2b^2 + a^3b^3 = (a, a^2, a^3) \cdot (b, b^2, b^3)$

…and we can plot the transformed data on **x/y/z-axes**…

**Figura:** Sistema de ejes 3D con "y-axis" vertical y "z-axis" en diagonal, más el eje horizontal "Dosage (mg):". Los puntos originales atenuados están en la base. Puntos rojos y verdes aparecen elevados en el espacio tridimensional siguiendo la transformación $(a, a^2, a^3)$: los rojos (algunos de mayor tamaño) se agrupan hacia la izquierda a media altura, uno rojo aislado arriba a la derecha, y los verdes forman una diagonal ascendente hacia la derecha sobre el eje z, ilustrando el mapeo a 3 dimensiones.

## Slide 27

# Support Vector Machines

$a^1b^1 + a^2b^2 + a^3b^3 + \cdots + a^{\infty}b^{\infty} = (a, a^2, a^3, \ldots, a^{\infty}) \cdot (b, b^2, b^3, \ldots, b^{\infty})$

**Series de Taylor**

$f(x) = f(a) + \dfrac{f'(a)}{1!}(x-a) + \dfrac{f''(a)}{2!}(x-a)^2 + \dfrac{f'''(a)}{3!}(x-a)^3 + \cdots + \dfrac{f^{\infty}(a)}{\infty!}(x-a)^{\infty}$

**Series de Taylor con e^x**

$e^x = e^a + \dfrac{e^a}{1!}(x-a) + \dfrac{e^a}{2!}(x-a)^2 + \dfrac{e^a}{3!}(x-a)^3 + \cdots + \dfrac{e^a}{\infty!}(x-a)^{\infty}$

(en esta fórmula, cada término "$-a$" está resaltado en color rojo)

## Slide 28

# Support Vector Machines

$e^x = e^a + \dfrac{e^a}{1!}(x-a) + \dfrac{e^a}{2!}(x-a)^2 + \dfrac{e^a}{3!}(x-a)^3 + \cdots + \dfrac{e^a}{\infty!}(x-a)^{\infty}$ (con los términos "$-a$" en rojo)

$e^x = e^0 + \dfrac{e^0}{1!}(x-0) + \dfrac{e^0}{2!}(x-0)^2 + \dfrac{e^0}{3!}(x-0)^3 + \cdots + \dfrac{e^0}{\infty!}(x-0)^{\infty}$ (con los términos "0" en rojo)

$e^x = 1 + \dfrac{1}{1!}x + \dfrac{1}{2!}x^2 + \dfrac{1}{3!}x^3 + \cdots + \dfrac{1}{\infty!}x^{\infty}$

$e^{ab} = 1 + \dfrac{1}{1!}ab + \dfrac{1}{2!}(ab)^2 + \dfrac{1}{3!}(ab)^3 + \cdots + \dfrac{1}{\infty!}(ab)^{\infty}$

$e^{ab} = \left(1, \sqrt{\dfrac{1}{1!}}a, \sqrt{\dfrac{1}{2!}}a^2, \sqrt{\dfrac{1}{3!}}a^3, \ldots, \sqrt{\dfrac{1}{\infty!}}a^{\infty}\right) \cdot \left(1, \sqrt{\dfrac{1}{1!}}b, \sqrt{\dfrac{1}{2!}}b^2, \sqrt{\dfrac{1}{3!}}b^3, \ldots, \sqrt{\dfrac{1}{\infty!}}b^{\infty}\right)$

## Slide 29

# Non-linear Decision Boundaries

$\ell = \displaystyle\sum_{i=1}^{N} \alpha_i - \dfrac{1}{2}\displaystyle\sum_{i,j=1}^{N} t^{(i)}t^{(j)}\alpha_i\alpha_j(\mathbf{x}^{(i)T} \cdot \mathbf{x}^{(j)})$

$y = \text{sign}\left[b + \mathbf{x} \cdot \left(\displaystyle\sum_{i=1}^{N} \alpha_i t^{(i)}\mathbf{x}^{(i)}\right)\right]$

- How to form non-linear decision boundaries in input space?

  1. Map data into feature space x → φ(x)
  2. Replace dot products between inputs with feature points x₍ᵢ₎ᵀ x₍ⱼ₎ → φ(x₍ᵢ₎)ᵀ φ(x₍ⱼ₎)
  3. Find linear decision boundary in feature space

- Problem: what is a good feature function φ(x)?

## Slide 30

# Input Transformation

Mapping to a feature space can produce problems:

- High computational burden due to high dimensionality
- Many more parameters

SVM solves these two issues simultaneously:

- "Kernel trick" produces efficient classification
- Dual formulation only assigns parameters to samples, not features

## Slide 31

# Classification with Non-linear SVMs

**Kernel trick:**

$K(\mathbf{x}^{(i)}, \mathbf{x}^{(j)}) = \phi(\mathbf{x}^{(i)})^T \phi(\mathbf{x}^{(j)})$

**Non-linear SVM using kernel function K():**

$\ell = \displaystyle\sum_{i=1}^{N} \alpha_i - \dfrac{1}{2}\displaystyle\sum_{i,j=1}^{N} t^{(i)}t^{(j)}\alpha_i\alpha_j K(\mathbf{x}^{(i)}, \mathbf{x}^{(j)})$

**Final decision function:**

$y = \text{sign}\left[b + \displaystyle\sum_{i=1}^{N} t^{(i)}\alpha_i K(\mathbf{x}, \mathbf{x}^{(i)})\right]$

## Slide 32

# Kernels

**Examples of kernels: kernels measure similarity**

Polynomial

$K(\mathbf{x}^{(i)}, \mathbf{x}^{(j)}) = (\mathbf{x}^{(i)T}\mathbf{x}^{(j)} + 1)^d$

where **d** is the degree of the polynomial, e.g., d = 2 for quadratic

Gaussian

$K(\mathbf{x}^{(i)}, \mathbf{x}^{(j)}) = \exp\left(-\dfrac{\|\mathbf{x}^{(i)} - \mathbf{x}^{(j)}\|^2}{2\sigma^2}\right)$

Sigmoid

$K(\mathbf{x}^{(i)}, \mathbf{x}^{(j)}) = \tanh(\beta(\mathbf{x}^{(i)T}\mathbf{x}^{(j)}) + a)$

**Why is this useful?**

1. Rewrite training examples using more complex features
2. Dataset not linearly separable in original space may be linearly separable in higher dimensional space

## Slide 33

How does decision boundary look like?

https://ml-visualizer.herokuapp.com/

## Slide 34

# Final Takeaways

1. Kernels allow very flexible hypotheses. Poly-time exact optimization methods rather than approximate methods

2. Soft-margin extension permits misclassified examples

3. Excellent results (1.1% error rate on handwritten digits vs. LeNet's 0.9%)

4. SVM must choose kernel parameters. Very large problems computationally intractable

## Slide 35

# Further Reading and Resources

- Bishop, "Pattern Recognition and Machine Learning", Chapter 7.

- Shalev-Shwartz, "Understanding Machine Learning", Chapter 15.

- Cristianini, "An Introduction to Support Vector Machines".

## Slide 36

**Figura:** Slide de cierre con fotografía de fondo (dos personas con bata de laboratorio y lentes de protección observando un equipo mecánico/robótico con rieles y engranajes), con overlay de color azul degradado. No contiene texto propio de contenido (solo elementos decorativos institucionales).
