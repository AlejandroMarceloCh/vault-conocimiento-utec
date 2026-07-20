---
curso: ML
titulo: Topic 3 - Nearest Neighbors.pptx
slides: 36
fuente: Topic 3 - Nearest Neighbors.pptx.pdf
---

## Slide 1

GENERALIZATION & NEAREST NEIGHBORS

## Slide 2

Lesson Objectives

1. Extend classification to multiclass escenarios.
2. Understand the intuition behind instance-based learning.
3. Identify the differences between linear classifiers and k-NN, including their assumptions and use cases.
4. Visualize and interpret decision boundaries formed by nearest neighbor models.

## Slide 3

1.
Support Vector
Multi-class

## Slide 4

Discriminant Functions for +2 classes

First idea: Use $K - 1$ classifiers, each solving a two class problem of separating point in a class $C_k$ from points not in the class.

Known as **1 vs all** or **1 vs the rest** classifier

PROBLEM: More than one good answer for green region!

**Figura:** Diagrama con dos rectas rojas que se cruzan formando cuatro regiones. La región superior (triángulo verde) queda marcada con un signo de interrogación "?", indicando ambigüedad. Las regiones están etiquetadas $\mathcal{R}_1$, $\mathcal{R}_2$, $\mathcal{R}_3$. Flechas indican el lado "$\mathcal{C}_1$" vs "not $\mathcal{C}_1$" para una recta, y "$\mathcal{C}_2$" vs "not $\mathcal{C}_2$" para la otra.

## Slide 5

Discriminant Functions for +2 classes

Another idea: Introduce $K(K-1)/2$ two-way classifiers, one for each possible pair of classes.

Each point is classified according to majority vote amongst the disc. func.

Known as the **1 vs 1 classifier**

PROBLEM: Two-way preferences need not be transitive

**Figura:** Diagrama con tres rectas (dos continuas rojas y una discontinua roja) que se cruzan formando una región central verde marcada con "?". Regiones etiquetadas $\mathcal{R}_1$, $\mathcal{R}_2$, $\mathcal{R}_3$. Flechas indican pares de preferencia: $\mathcal{C}_1$ vs $\mathcal{C}_3$, $\mathcal{C}_1$ vs $\mathcal{C}_2$, $\mathcal{C}_3$ vs $\mathcal{C}_2$.

## Slide 6

K-Class Discriminant

We can avoid these problems by considering a single K-class discriminant comprising K functions of the form

$y_k(\mathbf{x}) = \mathbf{w}_k^T \mathbf{x} + w_{k,0}$

and then assigning a point x to class $C_k$ if

$\forall j \neq k \quad y_k(\mathbf{x}) > y_j(\mathbf{x})$

Note that $\mathbf{w}^T_k$ is now a vector, not the k-th coordinate

## Slide 7

K-Class Discriminant

The decision boundary between class $C_j$ and class $C_k$ is given by $y_j(x) = y_k(x)$, and thus it's a *(D − 1)* dimensional hyperplane defined as

$(\mathbf{w}_k - \mathbf{w}_j)^T \mathbf{x} + (w_{k0} - w_{j0}) = 0$

What about the binary case? Is this different?

What is the shape of the overall decision boundary?

## Slide 8

K-Class Discriminant

The decision regions of such a discriminant are always **singly connected** and **convex**

Consider 2 points $\mathbf{x}_A$ and $\mathbf{x}_B$ that lie inside decision region $R_k$

Any convex combination $\hat{\mathbf{x}}$ of those points also will be in $R_k$

$\hat{\mathbf{x}} = \lambda \mathbf{x}_A + (1-\lambda)\mathbf{x}_B$

**Figura:** Diagrama con tres rectas rojas que parten de un punto común, dividiendo el plano en tres regiones etiquetadas $\mathcal{R}_i$, $\mathcal{R}_j$, $\mathcal{R}_k$. Dentro de $\mathcal{R}_k$ se dibujan dos puntos $\mathbf{x}_A$ y $\mathbf{x}_B$ unidos por un segmento morado, con un punto intermedio $\hat{\mathbf{x}}$ sobre el segmento, ilustrando que la combinación convexa permanece dentro de la región.

## Slide 9

Example

**Figura:** Gráfico de dispersión titulado "Decision surface" con ejes de -2 a 3 (eje x) y de -3 a 4 (eje y). Muestra tres regiones de fondo coloreadas: azul (class 1, esquina superior izquierda), rojo (class 2, parte inferior central), y dorado/amarillo (class 3, derecha). Puntos de datos superpuestos: puntos azules (class 1) agrupados en la región azul, puntos rojos (class 2) en la región roja/central, puntos verde-oliva (class 3) dispersos en la región dorada y también mezclados en la zona central. Varias líneas discontinuas (roja, morada, verde, amarilla) representan los límites de decisión par a par entre clases, mostrando cómo se cruzan sin definir un límite único y consistente.

## Slide 10

What do we know about hyperparameters?

## Slide 11

Use of Validation Set

Tuning hyper-parameters

→ **Never use test data for tuning the hyper-parameters**
→ We can divide the set of training examples into two disjoint sets: **training** and **validation**
→ Use the first set (i.e., training) to estimate the weights **w** for different values of α
→ Use the second set (i.e., validation) to estimate the best α, by evaluating
→ how well the classifier does on this second set
→ This tests how well it generalizes to unseen data

## Slide 12

Cross-Validation

**Figura:** Diagrama de bloques que ilustra el proceso de validación cruzada. Fila superior: bloque "All Data" completo. Segunda fila: el mismo bloque dividido en "Training data" (verde, mayor parte) y "Test data" (azul, menor parte a la derecha). Debajo, la porción de Training data se subdivide en 5 folds (Fold 1 a Fold 5). Se muestran 5 splits (Split 1 a Split 5): en cada split, un fold distinto se marca en azul (usado como validación) mientras los otros cuatro permanecen en verde (usados como entrenamiento) — Split 1 marca Fold 1, Split 2 marca Fold 2, y así sucesivamente hasta Split 5 marca Fold 5. Una llave agrupa los 5 splits bajo la etiqueta "Finding Parameters". Al final, un bloque naranja "Test data" bajo la etiqueta "Final evaluation".

## Slide 13

2.
Nearest Neighbors
Instance-based Learning

## Slide 14

Classification: Oranges and Lemons

Can construct simple linear decision boundary:

$y = sign(w_0 + w_1 x_1 + w_2 x_2)$

**Figura:** Gráfico de dispersión con eje x "width (cm)" (rango 4 a 10) y eje y "height (cm)" (rango 4 a 10). Puntos rojos circulares etiquetados "oranges" agrupados principalmente en la zona central-inferior derecha, y puntos triangulares azules etiquetados "lemons" agrupados en la zona superior izquierda. Una línea diagonal negra recta separa aproximadamente ambas nubes de puntos, actuando como frontera de decisión lineal. A la derecha, una fotografía de una naranja con flechas de doble punta indicando su ancho y su alto (dimensiones medidas).

## Slide 15

What is the meaning of "linear" classification?

**Classification is intrinsically non-linear**

It puts non-identical things in the same class, so a difference in the input vector sometimes causes zero change in the answer

**Linear classification** means that the part that adapts is linear

$z(x) = \mathbf{w}^T\mathbf{x} + w_0$

The adaptive part is followed by a non-linearity to make the **decision**

$y(\mathbf{x}) = f(z(\mathbf{x}))$

What functions *f()* have we seen so far in class?

## Slide 16

Classification as induction

**Figura:** Mismo gráfico de dispersión "oranges vs lemons" (width cm vs height cm) que en la slide 14, pero sin la línea de frontera lineal. Se añade una estrella blanca en la posición aproximada (6, 6.5) representando una nueva instancia de consulta, con un círculo morado con signo de interrogación "?" apuntando hacia la estrella mediante una flecha, ilustrando la pregunta de a qué clase pertenece el nuevo punto (inducción/clasificación por instancia).

## Slide 17

Instance-based Learning

Alternative to parametric models are **non-parametric** models

These are typically simple methods for approximating discrete-valued or real-valued target functions (they work for **classification** or regression problems)

**Learning** amounts to simply **storing** training data

Test instances classified using **similar** training instances

Embodies often sensible underlying **assumptions**:

1. Output varies smoothly with input
2. Data occupies subspace of high-dimensional input space

## Slide 18

Nearest Neighbors

Training example in Euclidean space: $\mathbf{x} \in \Re^d$

**Idea:** The value of the target function for a new query is estimated from the known value(s) of the **nearest training example(s)**

$||\mathbf{x}^{(a)} - \mathbf{x}^{(b)}||_2 = \sqrt{\sum_{j=1}^{d}(x_j^{(a)} - x_j^{(b)})^2}$

**Algorithm:**
1. Find example $(\mathbf{x}^*, t^*)$ (from the stored training set) closest to the test instance $\mathbf{x}$. That is:

$\mathbf{x}^* = \underset{\mathbf{x}^{(i)} \in \text{train. set}}{\text{argmin}} \; \text{distance}(\mathbf{x}^{(i)}, \mathbf{x})$

2. Output $y = t^*$

## Slide 19

Decision Boundaries

Nearest neighbor algorithm does not explicitly compute **decision boundaries**, but these can be inferred

**Decision boundaries: Voronoi diagram** visualization

- show how input space divided into classes
- each line segment is equidistant between two points of opposite classes

**Figura:** Diagrama de Voronoi en un plano con ejes $x_1$ (horizontal) y $x_2$ (vertical). Puntos rojos y negros dispersos en el plano, cada uno rodeado por una celda poligonal (región de Voronoi) delimitada por líneas negras que representan la equidistancia entre puntos vecinos de clases opuestas. Las celdas correspondientes a puntos rojos están sombreadas en gris; las celdas de puntos negros quedan en blanco.

## Slide 20

Decision Boundaries

**Figura:** Panel izquierdo: gráfico de dispersión "oranges vs lemons" (width cm vs height cm, ejes de 4 a 10) con el diagrama de Voronoi superpuesto (líneas delgadas grises) y una frontera de decisión gruesa en negro (zigzag) que separa la región de las lemons (triángulos azules, arriba) de la región de las oranges (círculos rojos, abajo), siguiendo los bordes de las celdas de Voronoi entre puntos de clases opuestas. Panel derecho: gráfico 3D con ejes $x_1$, $x_3$ (y un tercer eje implícito) mostrando un poliedro de Voronoi en 3D: una celda central roja/rosada rodeada de puntos negros (otra clase) y una envolvente gris translúcida, ilustrando cómo el diagrama de Voronoi se extiende a espacios de mayor dimensión.

## Slide 21

# Use Cases

Nearest Neighbor approaches can work with **multi-modal data**

**Figura:** Diagrama de dispersión 2D con cuadrados rojos y círculos azules agrupados en dos regiones (una arriba, otra abajo), cada una con un punto de consulta marcado con "?" ubicado en zona mixta entre ambas clases, ilustrando un caso de clasificación con datos no linealmente separables.

**Figura:** Diagrama titulado "1 NN" con puntos rojos (arriba, dispersos) y puntos azules (abajo, dispersos), con una región sombreada azul alrededor de una "noisy sample" (muestra ruidosa) rodeada de puntos rojos. Texto: "every example in the blue shaded area will be misclassified as the blue class" (todo ejemplo en el área sombreada azul será clasificado incorrectamente como clase azul).

## Slide 22

# k-Nearest Neighbors

**Figura:** Dos diagramas lado a lado. Izquierda "1 NN": región sombreada azul alrededor de una "noisy sample" (muestra ruidosa) situada entre puntos rojos, con leyenda "every example in the blue shaded area will be misclassified as the blue class" (será clasificado incorrectamente como clase azul). Derecha "3 NN": la misma región ahora aparece corregida, con leyenda "every example in the blue shaded area will be classified correctly as the red class" (será clasificado correctamente como clase roja), mostrando cómo aumentar k corrige el error de clasificación causado por ruido.

- Nearest neighbors **sensitive to mis-labeled** data ("class noise"). Solution?
- **Smooth** by having k nearest neighbors **vote**

## Slide 23

# k-Nearest Neighbors

- Nearest neighbors **sensitive to mis-labeled** data ("class noise"). Solution?
- **Smooth** by having k nearest neighbors **vote**

**Figura:** Recuadro con el algoritmo kNN:

Algorithm (kNN):
1. Find k examples $\{\mathbf{x}^{(i)}, t^{(i)}\}$ closest to the test instance $\mathbf{x}$
2. Classification output is majority class

$y = \arg\max_{t^{(z)}} \sum_{r=1}^{k} \delta(t^{(z)}, t^{(r)})$

How do we **choose k**?

## Slide 24

# How do we choose k?

- Larger $k$ may lead to better performance
- But if we set $k$ too large we may end up looking at samples that are not neighbors (are far away from the query)
- We can use cross-validation to find $k$
- Rule of thumb is $k < sqrt(n)$, where n is the number of training examples

## Slide 25

# Issues & (Fixes?)

If some attributes (coordinates of x) have larger **ranges**, they are treated as more important

- Normalize scale
  - Simple option: Linearly scale the range of each feature to be, e.g., in range [0,1]
  - Linearly scale each dimension to have 0 mean and variance 1 (compute mean μ and variance σ² for an attribute $x_j$ and scale: $(x_j - m)/\sigma$)

- be careful: sometimes scale matters

## Slide 26

# Issues & (Fixes?)

**Irrelevant, correlated** attributes add noise to distance measure

- eliminate some attributes
- or vary and possibly adapt weight of attributes

**Non-metric** attributes (symbols)

- hot-encoding
- hamming distance

## Slide 27

# Issues & (Fixes?)

**Expensive at test time:** To find one nearest neighbor of a query point x, we must compute the distance to all N training examples. Complexity: $O(kdN)$ for kNN

- Use subset of dimensions
- Presort training examples into fast data structures (e.g., kd-trees)
- Compute only an approximate distance (e.g., LSH)
- Remove redundant data (e.g., condensing)

## Slide 28

# Remove Redundancy

If all Voronoi neighbors have the same class, a sample is useless, remove it

**Figura:** Dos diagramas de teselación de Voronoi lado a lado con puntos rojos y verdes. Izquierda: diagrama original con una flecha roja etiquetada "remove" (eliminar) señalando un punto rojo rodeado por celdas cuyos vecinos de Voronoi son todos de la misma clase (rojo), por lo que es redundante. Derecha: el mismo diagrama después de eliminar ese punto redundante, con las celdas de Voronoi simplificadas/fusionadas, mostrando el resultado de la condensación.

## Slide 29

# Multi-class K-NN

Can directly handle multi class problems

**Figura:** Dos diagramas de teselación de Voronoi (ejes de 0.0 a 1.0 en ambos ejes) sobre el mismo conjunto de puntos negros dispersos. Izquierda: diagrama de líneas mostrando solo las fronteras de las celdas de Voronoi (sin color, solo el trazado de líneas). Derecha: el mismo diagrama coloreado por regiones (colores: morado, dorado/amarillo, verde, celeste, magenta, azul, naranja, rojo, lima), ilustrando cómo kNN particiona el espacio en regiones de decisión para múltiples clases.

## Slide 30

# Example: Digit Classification

Decent performance when lots of data

**Figura:** Tira de imágenes de dígitos manuscritos (0 al 9) en fondo negro con trazos blancos (estilo MNIST), seguida de una tabla titulada "Test Error Rate (%)" con los siguientes métodos y sus tasas de error:

| Método | Test Error Rate (%) |
|---|---|
| Linear classifier (1-layer NN) | 12.0 |
| K-nearest-neighbors, Euclidean | 5.0 |
| K-nearest-neighbors, Euclidean, deskewed | 2.4 |
| K-NN, Tangent Distance, 16x16 | 1.1 |
| K-NN, shape context matching | 0.67 |
| 1000 RBF + linear classifier | 3.6 |
| SVM deg 4 polynomial | 1.1 |
| 2-layer NN, 300 hidden units | 4.7 |
| 2-layer NN, 300 HU, [deskewing] | 1.6 |
| LeNet-5, [distortions] | 0.8 |
| Boosted LeNet-4, [distortions] | 0.7 |

## Slide 31

# Summary

Naturally **forms complex decision boundaries**; adapts to data density

If we have lots of samples, kNN typically works well

**Problems**

- Sensitive to class noise
- Sensitive to scales of attributes
- Distances are less meaningful in high dimensions
- Scales linearly with number of examples

What kind of decision boundaries do we expect to find?

## Slide 32

# 3. Nearest Neighbors
### Hands-on Activity

**Figura:** Imagen decorativa de fondo azul con una mano robótica extendiendo el dedo índice hacia un globo terráqueo digital/holograma con líneas de datos, sin texto adicional relevante más allá del título y subtítulo de sección.

## Slide 33

# Home Exercise

**Figura:** Diagrama de dispersión titulado con leyenda "fraud" (0 = azul, 1 = naranja). Eje X: "dist_from_home" (de 0 a 140+). Eje Y: "purchase_price_ratio" (de 0 a 8). Los puntos naranjas (fraud=1) se concentran mayormente en valores bajos de dist_from_home (0-30) con purchase_price_ratio alto (4-8.5), aunque hay algunos casos naranjas dispersos con distancias mayores (110, 145) y ratios más bajos. Los puntos azules (fraud=0) se concentran en dist_from_home bajo (0-80) con purchase_price_ratio bajo (0-3), y algunos pocos en distancias mayores (115, 145) con ratio bajo (~0.5).

## Slide 34

# Final Takeaways

1. KNN is a simple yet powerful non-parametric method.
2. Choosing k carefully and normalizing features are essential for good performance.
3. k-NN is computationally intensive during inference but can be optimized with data structures.
4. In high-dimensional spaces, distance metrics become less meaningful, use feature selection or dimensionality reduction.

## Slide 35

# Further Reading and Resources

- Bishop, "Pattern Recognition and Machine Learning", Chapter 2.
- Hal Daumé III, "A Course in Machine Learning", Chapter 3.
- Hastie, "The Elements of Statistical Learning".

## Slide 36

**Figura:** Imagen de cierre con fondo azul, fotografía en tono azul superpuesto de dos personas (con lentes de seguridad y bata blanca de laboratorio) observando un equipo/maquinaria con rieles y cables en un laboratorio. Sin texto adicional visible más allá de los logos institucionales.
