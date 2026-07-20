---
curso: ML
titulo: Topic 3 - Decision Trees.pptx
slides: 43
fuente: Topic 3 - Decision Trees.pptx.pdf
---

## Slide 1

DECISION TREES

## Slide 2

Lesson Objectives

1. Understand the structure of decision trees: nodes, branches, and leaves.
2. Apply entropy and information gain to evaluate attribute splits.
3. Recognize the expressiveness and limitations of decision trees.
4. Explore ensemble methods like bagging and boosting

## Slide 3

1.

Decision Trees
*Definition and cases*

## Slide 4

Another Classification Idea

We learned about linear classification (e.g., logistic regression, linear SVM, non linear SVM), and nearest neighbors. **Any other idea?**

## Slide 5

Another Classification Idea

We learned about linear classification (e.g., logistic regression, linear SVM, non linear SVM), and nearest neighbors. **Any other idea?**

**Pick an attribute,** do a simple test

## Slide 6

Another Classification Idea

**Figura:** Panel izquierdo — gráfico de dispersión con ejes "width (cm)" (eje x, rango ~4 a 10) y "height (cm)" (eje y, rango ~4 a 10). Puntos rojos (círculos) = "oranges", puntos morados (triángulos) = "lemons". El plano está dividido por líneas negras verticales/horizontales en cuatro regiones: una línea vertical en width≈6.5cm y dos líneas horizontales (una en height≈9.5cm a la derecha de la vertical, otra en height≈6.0cm a la izquierda), formando regiones etiquetadas conceptualmente con imágenes de limón (arriba izquierda y arriba derecha) y naranja (abajo izquierda, centro derecha). Los puntos naranja se agrupan en el centro (width 6-8, height 7-8) y abajo (width 6, height 4-5); los puntos limón se agrupan en width 6-7, height 8-10.5.
Panel derecho — árbol de decisión correspondiente: nodo raíz "width > 6.5cm?" con ramas Yes/No. Rama Yes lleva a nodo "height > 9.5cm?" con ramas Yes→limón, No→naranja. Rama No lleva a nodo "height > 6.0cm?" con ramas Yes→limón, No→naranja.

## Slide 7

Another Classification Idea

We learned about linear classification (e.g., logistic regression, linear SVM, non linear SVM), and nearest neighbors. **Any other idea?**

**Pick an attribute,** do a simple test

Conditioned on a choice, pick another attribute, do another test

In the leaves, assign a class with **majority vote**

Do other branches as well

## Slide 8

Another Classification Idea

**Figura:** Izquierda, un "Test example": imagen de un limón con marcas de medición (ancho y alto) indicadas por líneas punteadas. Derecha, el mismo árbol de decisión de la slide 6 ("width > 6.5cm?" → Yes/No → "height > 9.5cm?" / "height > 6.0cm?" → Yes/No → limón/naranja), con una ruta resaltada en flechas rojas: desde la raíz toma la rama "No" (width ≤ 6.5cm) hacia "height > 6.0cm?", y de ahí la rama "No" hacia la hoja "naranja", que aparece resaltada con un recuadro morado como resultado final de la clasificación del ejemplo de prueba (aunque la imagen de prueba es un limón, el árbol lo clasifica como naranja).

## Slide 9

Decision Trees

Internal nodes **test attributes**

Branching is determined by **attribute value**

Leaf nodes are **outputs** (class assignments)

**Figura:** Árbol de decisión: nodo raíz "width > 6.5cm?" con ramas Yes/No. Rama Yes → nodo "height > 9.5cm?" con ramas Yes→limón, No→naranja. Rama No → nodo "height > 6.0cm?" con ramas Yes→limón, No→naranja.

## Slide 10

Decision Trees

**Algorithm:**

Choose an attribute on which to descend at each level

Condition on earlier (higher) choices

Generally, restrict only one dimension at a time

Declare an output value when you get to the bottom

In the orange/lemon example, we only split each dimension once, but that is not required

## Slide 11

Expressiveness

**Discrete-input, discrete-output case**

Decision trees can express any function of the input attributes

E.g., for Boolean functions, truth table row → path to leaf

**Figura:** Tabla de verdad a la izquierda con columnas A, B, A xor B: filas (F,F,F), (F,T,T), (T,F,T), (T,T,F). A la derecha, árbol de decisión equivalente: nodo raíz "A" con ramas F/T. Rama F → nodo "B" con ramas F→F (rojo), T→T (verde). Rama T → nodo "B" con ramas F→T (verde), T→F (rojo). El árbol reproduce exactamente la tabla de verdad de XOR.

## Slide 12

"HOW DO WE CONSTRUCT A USEFUL DECISION TREE?"

## Slide 13

2.

Decision Trees
*Training*

## Slide 14

Learning Decision Trees

Learning the simplest (smallest) decision tree is an NP complete problem (check: Hyafil & Rivest'76)

Resort to a **greedy heuristic**

- Start from an empty decision tree
- Split on next best attribute
- Recurse

What is **best** attribute?

We use **information theory** to guide us

## Slide 15

Choosing a good attribute

Which attribute is better to split on, $X_1$ or $X_2$?

**Figura:** Dos mini-árboles de una sola división. Izquierda: nodo $X_1$ con ramas t/f; rama t → conteos Y=t:4, Y=f:0; rama f → conteos Y=t:1, Y=f:3. Derecha: nodo $X_2$ con ramas t/f; rama t → conteos Y=t:3, Y=f:1; rama f → conteos Y=t:2, Y=f:2. A la derecha, tabla de datos con columnas $X_1$, $X_2$, Y y 8 filas: (T,T,T), (T,F,T), (T,T,T), (T,F,T), (F,T,T), (F,F,F), (F,T,F), (F,F,F) — celdas de Y coloreadas verde para T y rojo para F.

**Idea:** Use counts at leaves to define probability distributions, so we can measure uncertainty

## Slide 16

We Flip Two Different Coins

Sequence 1:
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 ... ?

Sequence 2:
0 1 0 1 0 1 1 1 0 1 0 0 1 1 0 1 0 1 ... ?

**Figura:** Dos pares de barras comparando conteos de 0s y 1s. Izquierda ("Sequence 1"): barra para "0" con valor 16, barra para "1" con valor 2. Derecha ("Sequence 2", etiquetado "versus"): barra para "0" con valor 8, barra para "1" con valor 10. Ilustra que la Secuencia 1 tiene una distribución muy sesgada (poca incertidumbre) mientras la Secuencia 2 tiene una distribución casi uniforme (alta incertidumbre).

## Slide 17

Quantifying Uncertainty

How surprised are we by a new value in the sequence?

$H(X) = -\sum_{x \in X} p(x) \log_2 p(x)$

**Figura:** Gráfico de la función de entropía H(X) (eje y "entropy", rango 0 a 1.0) en función de la probabilidad p de cara (eje x "probability p of heads", rango 0 a 1.0), para una variable Bernoulli de dos resultados. La curva es una forma de campana simétrica que empieza en 0 (p=0), sube hasta un máximo de 1.0 en p=0.5, y vuelve a bajar a 0 en p=1.0.

## Slide 18

Entropy

**High Entropy**

- Variable has a uniform like distribution
- Flat histogram
- Values sampled from it are less predictable

**Low Entropy**

- Distribution of variable has many peaks and valleys
- Histogram has many lows and highs
- Values sampled from it are more predictable

## Slide 19

Entropy of a Joint Distribution

Example: $X = \{\text{Raining}, \text{Not raining}\}$, $Y = \{\text{Cloudy}, \text{Not cloudy}\}$

**Figura:** Tabla de probabilidad conjunta con filas "Raining"/"Not Raining" y columnas "Cloudy"/"Not Cloudy": Raining∩Cloudy=24/100, Raining∩Not Cloudy=1/100, Not Raining∩Cloudy=25/100, Not Raining∩Not Cloudy=50/100.

$H(X,Y) = -\sum_{x \in X}\sum_{y \in Y} p(x,y) \log_2 p(x,y)$

$= -\frac{24}{100}\log_2\frac{24}{100} - \frac{1}{100}\log_2\frac{1}{100} - \frac{25}{100}\log_2\frac{25}{100} - \frac{50}{100}\log_2\frac{50}{100}$

$\approx 1.56 \text{ bits}$

## Slide 20

Specific Conditional Entropy

Example: $X = \{\text{Raining}, \text{Not raining}\}$, $Y = \{\text{Cloudy}, \text{Not cloudy}\}$

**Figura:** Misma tabla de probabilidad conjunta de la slide 19: Raining∩Cloudy=24/100, Raining∩Not Cloudy=1/100, Not Raining∩Cloudy=25/100, Not Raining∩Not Cloudy=50/100.

What is the entropy of cloudiness Y, given that it is raining?

$H(Y|X=x) = -\sum_{y \in Y} p(y|x)\log_2 p(y|x)$

$= -\frac{24}{25}\log_2\frac{24}{25} - \frac{1}{25}\log_2\frac{1}{25}$

$\approx 0.24 \text{ bits}$

## Slide 21

# Conditional Entropy

Example: $X = \{\text{Raining}, \text{Not raining}\}$, $Y = \{\text{Cloudy}, \text{Not cloudy}\}$

**Figura:** Tabla de contingencia 2x2 con columnas "Cloudy" y "Not Cloudy", y filas "Raining" y "Not Raining". Valores: Raining-Cloudy = 24/100, Raining-Not Cloudy = 1/100, Not Raining-Cloudy = 25/100, Not Raining-Not Cloudy = 50/100.

The expected conditional entropy:

$$H(Y|X) = \sum_{x \in X} p(x) H(Y|X=x)$$

$$= -\sum_{x \in X} \sum_{y \in Y} p(x,y) \log_2 p(y|x)$$

## Slide 22

# Conditional Entropy

Example: $X = \{\text{Raining}, \text{Not raining}\}$, $Y = \{\text{Cloudy}, \text{Not cloudy}\}$

**Figura:** Misma tabla de contingencia 2x2 que la slide anterior: Raining-Cloudy = 24/100, Raining-Not Cloudy = 1/100, Not Raining-Cloudy = 25/100, Not Raining-Not Cloudy = 50/100.

What is the entropy of cloudiness, given the knowledge of whether or not it is raining?

$$H(Y|X) = \sum_{x \in X} p(x) H(Y|X=x)$$

$$= \frac{1}{4} H(\text{cloudy}|\text{is raining}) + \frac{3}{4} H(\text{cloudy}|\text{not raining})$$

$$\approx 0.75 \text{ bits}$$

## Slide 23

# Conditional Entropy

### Properties

- H is always non-negative
- Chain rule: $H(X, Y) = H(X|Y) + H(Y) = H(Y|X) + H(X)$
- If X and Y independent, then X doesn't tell us anything about Y : $H(Y|X) = H(Y)$
- But Y tells us everything about Y : $H(Y|Y) = 0$
- By knowing X, we can only decrease uncertainty about Y: $H(Y|X) \leq H(Y)$

## Slide 24

# Alternatives to Entropy

**Gini index?** $Gini = 1 - \sum_{i=1}^{C} (p_i)^2$

**Figura:** Dos gráficos de línea lado a lado, ambos con eje X "P(X)" de 0.0 a 1.0 y eje Y de 0.0 a 1.0. Gráfico izquierdo: curva roja "Gini" (pico ~0.5 en P(X)=0.5) y curva azul "Entropy" (pico ~1.0 en P(X)=0.5), ambas en forma de arco simétrico, la de Entropy siempre por encima de Gini. Gráfico derecho: curva roja "Gini x 2" y curva azul "Entropy", ambas casi superpuestas en forma de arco con pico ~1.0 en P(X)=0.5, mostrando que Gini x 2 aproxima bastante bien a Entropy.

## Slide 25

# Information Gain

Example: $X = \{\text{Raining}, \text{Not raining}\}$, $Y = \{\text{Cloudy}, \text{Not cloudy}\}$

**Figura:** Tabla de contingencia 2x2 igual a las anteriores: Raining-Cloudy = 24/100, Raining-Not Cloudy = 1/100, Not Raining-Cloudy = 25/100, Not Raining-Not Cloudy = 50/100.

How much information about cloudiness do we get by discovering whether it is raining?

$$IG(Y|X) = H(Y) - H(Y|X)$$

$$\approx 0.25 \text{ bits}$$

## Slide 26

# Information Gain

Example: $X = \{\text{Raining}, \text{Not raining}\}$, $Y = \{\text{Cloudy}, \text{Not cloudy}\}$

**Figura:** Misma tabla de contingencia 2x2: Raining-Cloudy = 24/100, Raining-Not Cloudy = 1/100, Not Raining-Cloudy = 25/100, Not Raining-Not Cloudy = 50/100.

- Also called information gain in Y due to X
- If X is completely uninformative about Y: $IG(Y|X) = 0$
- If X is completely informative about Y: $IG(Y|X) = H(Y)$
- How can we use this to construct our decision tree?

## Slide 27

# Constructing Decision Trees

**Figura:** Diagrama compuesto en dos partes. Izquierda: gráfico de dispersión con eje X "width (cm)" (4 a 10) y eje Y "height (cm)" (4 a 10), puntos rojos "oranges" y triángulos azules "lemons", con líneas negras de separación (una vertical cerca de width=6.5 y una horizontal cerca de height=6.0 y otra cerca de height=9.5) dividiendo el plano en regiones; se muestran íconos de limón y naranja en cada región correspondiente. Derecha: árbol de decisión con nodo raíz "width > 6.5cm?" que se ramifica en "Yes"→"height > 9.5cm?" y "No"→"height > 6.0cm?"; cada uno de estos nodos se ramifica en "Yes"/"No" terminando en íconos de limón u naranja.

We can use the *information gain* to automate the process.

At each level, one must choose:
1. Which variable to split.
2. Possibly where to split it.

Choose them based on how much information we would gain from the decision! (choose attribute that gives the highest gain)

## Slide 28

# Decision Tree Construction Algorithm

Simple, greedy, recursive approach, builds up tree node-by-node

1. pick an attribute to split at a non-terminal node
2. split examples into groups based on attribute value
3. for each group:
   - if no examples – return majority from parent
   - else if all examples in same class – return class
   - else loop to step 1

## Slide 29

# What Makes a Good Tree?

**Not too small:**

Need to handle important but possibly subtle distinctions in data

**Not too big:**

- Computational efficiency
- Avoid overfitting training examples

**Occam's Razor:** find the simplest hypothesis (smallest tree) that fits the observations

**Inductive bias:** small trees with informative nodes near the root

## Slide 30

# Multi-class Decision Trees

Can directly handle multi class problems

**Figura:** Gráfico de dispersión cuadrado particionado en 6 regiones poligonales de distintos colores (magenta, rojo, naranja, verde, amarillo, morado), cada región con puntos de dispersión de un color más oscuro correspondiente a su clase, ilustrando cómo un árbol de decisión divide el espacio de atributos en regiones para clasificación multiclase mediante fronteras lineales por partes (axis-aligned/piecewise).

## Slide 31

# Comparison to k-NN

**K-Nearest Neighbors**
- Decision boundaries: piece-wise linear
- Test complexity: non-parametric, few parameters besides (all?) training examples

**Decision Trees**
- Decision boundaries: axis aligned, tree structured
- Test complexity: attributes and splits

## Slide 32

# Applications of Decision Trees

Can express any Boolean function, but most useful when function depends critically on few attributes

Bad on: parity, majority functions; also not well-suited to continuous attributes

**Practical Applications**

- Flight simulator: 20 state variables; 90K examples based on expert pilot's actions; autopilot tree
- Yahoo Ranking Challenge
- Random Forests: Microsoft Kinect Pose Estimation

## Slide 33

# 3. Ensembles
### Decision Trees

**Figura:** Imagen decorativa de portada de sección: mano robótica tocando una interfaz digital con un globo terráqueo/red neuronal proyectada, sobre fondo azul oscuro con líneas de datos punteadas decorativas.

## Slide 34

# Ensemble Types

**Figura:** Diagrama con dos esquemas de ensamblado. Izquierdo, titulado "Bagging" / "Parallel": un dataset original (ícono verde) se ramifica en 3 datasets bootstrap (íconos morados), cada uno alimenta un modelo/robot independiente en paralelo, y las 3 salidas convergen en un ícono de bombilla (resultado combinado). Derecho, titulado "Boosting" / "Sequential": un dataset original (ícono verde) alimenta un primer dataset (morado) y modelo/robot; su salida retroalimenta secuencialmente al siguiente dataset (celeste) y modelo, y así sucesivamente hasta un tercer dataset (naranja) y modelo; las salidas de los 3 modelos convergen en un ícono de bombilla.

## Slide 35

# Bagging: Random Forest

**Figura:** Diagrama de flujo de Random Forest. Arriba, una tabla "Training data" con columnas Class, A, B, C y filas 1-5 (valores a1-a5, b1-b5, c1-c5). Esta tabla se muestra "Bootstrap" en 4 (…N) submuestras con reemplazo, cada una una tabla similar con filas repetidas/reordenadas. Cada submuestra alimenta un árbol de decisión individual ("Ensemble of trees": DT 1, DT 2, DT 3, …, DT N), representados como árboles binarios pequeños con nodos de colores (rojo, azul, verde, amarillo) representando clases. Cada árbol produce una predicción de clase (Class 1, Class 2, Class 1, Class 1) que se combinan mediante "Majority vote: Class 1" al final.

## Slide 36

# Bagging: XGBoost

**Figura:** Diagrama de flujo del algoritmo de boosting tipo XGBoost. "Training data" en la parte superior se distribuye a tres (o n) conjuntos $f(L_1)$, $f(L_2)$, $f(L_n)$, cada uno representado como una nube de puntos verdes y amarillos de distintos tamaños (pesos de las muestras). Debajo, sección "Building T CART trees": cada conjunto entrena un árbol CART pequeño (nodos amarillos conectados). Debajo, sección "Weighting increase": los puntos mal clasificados aumentan de tamaño/peso (flechas rojas indican que el peso se transmite/incrementa de un modelo al siguiente, y de vuelta con "Weighting increase" señalado por flecha roja hacia el segundo conjunto). Sección "Prediction": cada modelo produce $\hat{y}_L^{(1)}$, $\hat{y}_L^{(2)}$, ..., $\hat{y}_L^{(N)}$. Etiquetas laterales "Training" y "Testing" indican las fases. Todas las predicciones convergen en un cuadro final "Average aggregation of predictors".

## Slide 37

# 4. Decision Trees
### Example

**Figura:** Imagen decorativa de portada de sección: mano robótica tocando una interfaz digital con un globo terráqueo/red neuronal proyectada, sobre fondo azul oscuro con líneas de datos punteadas decorativas (misma imagen que la slide 33).

## Slide 38

# Example

**Figura:** Tabla de ejemplos de entrenamiento con columnas: Example (x1-x12), Input Attributes (Alt, Bar, Fri, Hun, Pat, Price, Rain, Res, Type, Est), y Goal (WillWait). Datos completos:
- x1: Alt=Yes, Bar=No, Fri=No, Hun=Yes, Pat=Some, Price=$$$, Rain=No, Res=Yes, Type=French, Est=0–10 → y1=Yes
- x2: Alt=Yes, Bar=No, Fri=No, Hun=Yes, Pat=Full, Price=$, Rain=No, Res=No, Type=Thai, Est=30–60 → y2=No
- x3: Alt=No, Bar=Yes, Fri=No, Hun=No, Pat=Some, Price=$, Rain=No, Res=No, Type=Burger, Est=0–10 → y3=Yes
- x4: Alt=Yes, Bar=No, Fri=Yes, Hun=Yes, Pat=Full, Price=$, Rain=Yes, Res=No, Type=Thai, Est=10–30 → y4=Yes
- x5: Alt=Yes, Bar=No, Fri=Yes, Hun=No, Pat=Full, Price=$$$, Rain=No, Res=Yes, Type=French, Est=>60 → y5=No
- x6: Alt=No, Bar=Yes, Fri=No, Hun=Yes, Pat=Some, Price=$$, Rain=Yes, Res=Yes, Type=Italian, Est=0–10 → y6=Yes
- x7: Alt=No, Bar=Yes, Fri=No, Hun=No, Pat=None, Price=$, Rain=Yes, Res=No, Type=Burger, Est=0–10 → y7=No
- x8: Alt=No, Bar=No, Fri=No, Hun=Yes, Pat=Some, Price=$$, Rain=Yes, Res=Yes, Type=Thai, Est=0–10 → y8=Yes
- x9: Alt=No, Bar=Yes, Fri=Yes, Hun=No, Pat=Full, Price=$, Rain=Yes, Res=No, Type=Burger, Est=>60 → y9=No
- x10: Alt=Yes, Bar=Yes, Fri=Yes, Hun=Yes, Pat=Full, Price=$$$, Rain=No, Res=Yes, Type=Italian, Est=10–30 → y10=No
- x11: Alt=No, Bar=No, Fri=No, Hun=No, Pat=None, Price=$, Rain=No, Res=No, Type=Thai, Est=0–10 → y11=No
- x12: Alt=Yes, Bar=Yes, Fri=Yes, Hun=Yes, Pat=Full, Price=$, Rain=No, Res=No, Type=Burger, Est=30–60 → y12=Yes

## Slide 39

# Attribute Selection

**Figura:** Dos árboles parciales comparando el split por atributo "Type?" (izquierda) versus "Patrons?" (derecha), ambos partiendo del conjunto completo de ejemplos {1,3,4,6,8,12} (positivos, verde) y {2,5,7,9,10,11} (negativos, rojo).

Izquierda — split por "Type?": ramas French→{1(+); 5(−)}, Italian→{6(+); 10(−)}, Thai→{4,8(+); 2,11(−)}, Burger→{3,12(+); 7,9(−)}. Cada rama queda con ejemplos mixtos (positivos y negativos), es decir no separa bien las clases.

Derecha — split por "Patrons?": ramas None→{7,11(−)} termina en hoja "No"; Some→{1,3,6,8(+)} termina en hoja "Yes"; Full→{4,12(+); 2,5,9,10(−)} continúa con un nodo "Hungry?" que se ramifica en No→{5,9(−)} y Yes→{4,12(+); 2,10(−)}.

## Slide 40

# Attribute Selection

**Figura:** Mismo diagrama que la slide anterior (splits por "Type?" a la izquierda y por "Patrons?"/"Hungry?" a la derecha con los mismos grupos de ejemplos), agregando debajo las fórmulas de Information Gain calculadas para cada atributo.

$$IG(Y) = H(Y) - H(Y|X)$$

$$IG(type) = 1 - \left[\frac{2}{12}H(Y|\text{Fr.}) + \frac{2}{12}H(Y|\text{It.}) + \frac{4}{12}H(Y|\text{Thai}) + \frac{4}{12}H(Y|\text{Bur.})\right] = 0$$

$$IG(Patrons) = 1 - \left[\frac{2}{12}H(0,1) + \frac{4}{12}H(1,0) + \frac{6}{12}H\left(\frac{2}{6}, \frac{4}{6}\right)\right] \approx 0.541$$

## Slide 41

# Final Takeaways

1. Decision Trees are interpretable and flexible models that recursively split data based on feature values.

2. The quality of splits is guided by metrics like entropy, Gini index, and information gain.

3. Although decision trees can model complex interactions, they are prone to overfitting.

4. Ensembles such as Random Forests and XGBoost significantly improve performance and generalization.

## Slide 42

# Further Reading and Resources

- Bishop, "Pattern Recognition and Machine Learning", Chapter 14.
- Hal Daumé III, "A Course in Machine Learning", Chapter 6.
- Mitchell, "Machine Learning", Chapter 3.

## Slide 43

**Figura:** Fotografía de fondo (decorativa, con overlay azul) que muestra a dos personas con bata de laboratorio y lentes de protección observando de cerca un equipo mecánico/electrónico de laboratorio (rieles metálicos con cableado y componentes). No contiene texto ni datos.
