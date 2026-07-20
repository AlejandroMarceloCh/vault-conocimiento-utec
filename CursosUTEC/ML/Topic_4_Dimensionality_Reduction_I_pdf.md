---
curso: ML
titulo: Topic 4 - Dimensionality Reduction I
slides: 49
fuente: Topic 4 - Dimensionality Reduction I.pdf
---

## Slide 1

**DIMENSIONALITY REDUCTION**

**Figura:** Portada del deck. Fondo azul con un túnel circular futurista y la silueta de un robot humanoide caminando dentro del túnel.

## Slide 2

PROBLEMAS CON LOS ALGORITMOS DE MACHINE LEARNING (CLASIFICACIÓN)

**Figura:** Slide de título con comillas decorativas grandes de fondo sobre fondo degradado azul.

## Slide 3

### Objetivos

1. Entender la reducción de dimensionalidad y su necesidad
2. Analizar limitaciones de algoritmos en alta dimensionalidad
3. Implementar PCA como técnica de proyección
4. Aplicar SVD como método alternativo

## Slide 4

0. Aprendizaje no supervisado
*Introducción*

**Figura:** Portada de sección "0." con imagen de una mano robótica tocando una interfaz digital sobre un mapa mundial luminoso.

## Slide 5

**Figura:** Tres paneles ilustrativos que representan los tres tipos de aprendizaje automático:
- SUPERVISED LEARNING: figura de un "profesor" (muñeco blanco 3D) señalando una pizarra a un "estudiante" (otro muñeco blanco 3D).
- UNSUPERVISED LEARNING: figura de un muñeco blanco 3D sentado en una mesa leyendo un periódico, solo, sin supervisión.
- REINFORCEMENT LEARNING: un pequeño robot con ojos azules brillantes, representando un agente que actúa e interactúa con su entorno.

## Slide 6

### Aprendizaje no supervisado

**Figura:** Diagrama de flujo: "Input" → flecha hacia el bloque "Modelo" (etiquetado arriba como "Estudiante") → flecha hacia "Output". Desde "Error" sale una flecha que retroalimenta hacia el bloque "Modelo" y otra flecha hacia "Output".

Similar != Differente

## Slide 7

### Principales aplicaciones

Los principales problemas y enfoques en el aprendizaje no supervisado se dividen en tres clases.

1. **Reducción de dimensionalidad:** representar cada caso de entrada utilizando un número reducido de variables (ej. análisis de componentes principales, análisis factorial, análisis de componentes independientes).

2. **Clustering:** representar cada caso de entrada utilizando un ejemplo prototipo (por ejemplo, k-means, modelos de mezcla).

3. **Estimación de densidad:** estimar la distribución de probabilidad sobre el espacio de los datos.

## Slide 8

1. Introducción
*Motivación*

**Figura:** Portada de sección "1." con la misma imagen de mano robótica tocando una interfaz digital sobre un mapa mundial luminoso.

## Slide 9

### ¿Por qué la reducción de dimensionalidad?

A medida que los datasets crecen en tamaño y complejidad, las exigencias computacionales aumentan, se incrementa el potencial de overfitting, y disminuye la interpretabilidad del modelo.

La reducción de dimensionalidad captura la información essential dentro de los datos mientras descarta características redundantes o menos informativas.

**Figura:** A la izquierda, una superficie 3D en forma de "S" (curva tipo Swiss roll desenrollada) con eje de colores que va de azul a rojo, ejes numerados de -1 a 5 (eje horizontal) y 0 a 3 (eje vertical). A la derecha, un scatter plot 2D con puntos de colores (rojo, verde, azul, cian) formando una nube dispersa con forma irregular, ejes de -2 a 2 en ambos ejes X e Y. Entre ambas imágenes, tres flechas triples (chevrons) azules apuntando hacia la derecha.

## Slide 10

### Visualizando Tendencias de Datos

**Figura:** Grilla de 8 scatter plots que muestran distintos algoritmos de reducción de dimensionalidad aplicados a un dataset en forma de "S" 3D (mostrado como referencia a la izquierda, con ejes -1 a 1, 0 a 1, y -2 a 2, coloreado con gradiente arcoíris). Los 8 paneles, cada uno titulado con el nombre del algoritmo y su tiempo de cómputo:
- LLE (0.18 sec): forma de arco/parábola invertida coloreada en gradiente arcoíris.
- LTSA (0.53 sec): bandas verticales de colores.
- Hessian LLE (0.34 sec): bandas verticales de colores.
- Modified LLE (0.27 sec): bandas verticales de colores.
- Isomap (0.44 sec): bandas verticales con dispersión, colores arcoíris.
- MDS (3.6 sec): forma de "S" o espiral, coloreada en gradiente arcoíris.
- SE (0.21 sec): forma de arco similar a una parábola delgada coloreada en gradiente arcoíris.
- t-SNE (26 sec): nube densa de puntos con agrupaciones de color, forma irregular.

## Slide 11

### Mejorar la Generalización

**Figura:** Tres diagramas que ilustran el efecto de la dimensionalidad sobre la generalización mediante puntos rojos (datos) y una curva/forma azul que los conecta:
1. En 2D: un cuadrado con esquinas redondeadas (curva azul) pasando por 8 puntos rojos dispuestos en cuadrado, con un punto rojo central.
2. En 3D (representado con ejes de perspectiva): una forma estrellada azul irregular dentro de un cubo alámbrico, pasando por puntos rojos distribuidos en las aristas y vértices del cubo.
3. En muchas dimensiones (representado radialmente): una maraña densa de curvas azules en forma de estrella múltiple, rodeada de muchos puntos rojos dispersos y líneas grises radiales que salen del centro en todas direcciones.

## Slide 12

### La Maldición de la Dimensionalidad

Richard Bellman (fotografía en blanco y negro de un hombre con traje).

**Figura:** Secuencia de figuras geométricas mostrando cómo crece la distancia máxima entre dos puntos según la dimensión: un segmento de línea (d = 1), un cuadrado con su diagonal marcada en rojo (d = √2), un cubo con su diagonal marcada en rojo (d = √3), puntos suspensivos, y la fórmula general (d = √n).

En n dimensiones la distancia máxima entre dos puntos crece lentamente

A medida que la dimensión aumenta, el volumen del espacio crece exponencialmente. Esto hace que los datos sean cada vez más dispersos.

## Slide 13

### ... ¿por qué es útil?

Compresión

Eliminación de redundancia

Visualización

Reducción de la complejidad temporal del procesamiento posterior

Regularización implícita

Maldición de la dimensionalidad

## Slide 14

2. Principal Component Analysis (PCA)

**Figura:** Portada de sección "2." con la misma imagen de mano robótica tocando una interfaz digital sobre un mapa mundial luminoso.

## Slide 15

### Principal Component Analysis (PCA)

**¿Qué es PCA?** Técnica no supervisada para extraer la estructura de varianza de datasets de alta dimensionalidad.

**Figura:** Nube de puntos amarillos con forma alargada diagonal (de esquina inferior izquierda a superior derecha), con dos flechas negras partiendo de un punto central: una apuntando hacia arriba-izquierda (dirección de menor varianza) y otra apuntando hacia arriba-derecha siguiendo el eje principal de la nube (dirección de mayor varianza).

PCA es una **proyección ortogonal** o transformación de los datos en un subespacio de manera que la **varianza** de los datos proyectados se **maximiza**.

## Slide 16

### Principal Component Analysis (PCA)

Intrínsecamente de menor dimensionalidad que la dimensión del espacio ambiente.

Si rotamos los datos, nuevamente solo una coordenada es más importante.

**Figura:** Dos diagramas con nubes de puntos amarillos y ejes negros en forma de "V":
- Izquierda: nube de puntos aplanada horizontalmente sobre un plano, con un eje vertical corto y un eje horizontal largo saliendo del mismo origen (perspectiva 3D).
- Derecha: la misma nube de puntos rotada, ahora alargada diagonalmente, con dos flechas negras (una hacia arriba-izquierda, otra siguiendo la diagonal principal hacia arriba-derecha).

¿Podemos **transformar** las **features** de manera que solo necesitemos **preservar** una **dimensión**?

## Slide 17

### PCA: Intuición

Los datos de entrenamiento tienen N vectores, $\{x_n\}_{n=1}^{N}$, de dimensionalidad D, entonces $x_i \in \mathbb{R}^D$

**El objetivo es reducir la dimensionalidad:**

- Proyectar linealmente a un espacio de dimensión mucho menor, M << D

$$\mathbf{x} \approx U\mathbf{z} + \mathbf{a}$$

- donde U es una matriz D × M y z un vector de M dimensiones

Buscar direcciones ortogonales en el espacio con la varianza más alta proyectar datos en este subespacio

**Figura:** Scatter plot con ejes $x_1$ (horizontal) y $x_2$ (vertical), puntos marcados con "×" formando una nube alargada en diagonal. Dos flechas parten de un punto dentro de la nube: $u_1$ apuntando en la dirección principal de la nube (diagonal ascendente), y $u_2$ apuntando perpendicular a $u_1$ (diagonal hacia arriba-izquierda, de menor varianza).

## Slide 18

### Encontrando Componentes Principales

Para encontrar las direcciones de los componentes principales, centramos los datos (restamos la media muestral de cada variable)

Calculamos la matriz de covarianza empírica

$$C = \frac{1}{N}\sum_{n=1}^{N}(\mathbf{x}^{(n)} - \bar{\mathbf{x}})(\mathbf{x}^{(n)} - \bar{\mathbf{x}})^T$$

con $\bar{\mathbf{x}}$ la media

¿Cuál es la dimensionalidad de C?

Ensamblamos estos eigenvectores en una matriz U (D × M)

Ahora podemos expresar vectores de D dimensiones x proyectándose a z de M dimensiones

$$\mathbf{z} = U^T\mathbf{x}$$

## Slide 19

### PCA Standard

**Algoritmo:** para encontrar M componentes subyacentes a datos de D dimensiones

1. Seleccionar los M eigenvectores principales de C (matriz de covarianza)

$$C = \frac{1}{N}\sum_{n=1}^{N}(\mathbf{x}^{(n)} - \bar{\mathbf{x}})(\mathbf{x}^{(n)} - \bar{\mathbf{x}})^T = U\Sigma U^T \approx U_{1:M}\Sigma_{1:M}U_{1:M}^T$$

donde U es ortogonal, las columnas son eigenvectores de longitud unitaria

$$U^TU = UU^T = 1$$

y Σ es una matriz con eigenvalores en la diagonal, representan la varianza en la dirección de cada eigenvector

2. Proyectar cada vector de entrada x en este subespacio, p.ej

$$z_j = \mathbf{u}_j^T\mathbf{x}; \qquad \mathbf{z} = U_{1:M}^T\mathbf{x}$$

## Slide 20

### Dos Derivaciones de PCA

**Dos vistas/derivaciones**

Maximizar la varianza (dispersión de puntos verdes)

Minimizar el error (distancia rojo-verde por punto de datos)

**Figura:** Scatter plot con ejes $x_1$ (horizontal) y $x_2$ (vertical). Una línea diagonal magenta representa la dirección del componente principal $u_1$ (con flecha indicando su dirección). Puntos rojos representan datos originales $\mathbf{x}_n$, cada uno conectado por un segmento azul a su proyección ortogonal sobre la línea magenta, representada como un punto verde $\tilde{\mathbf{x}}_n$.

## Slide 21

Dos Derivaciones de PCA

**Varianza acumulada**

¿Qué significa cada punto del gráfico?

- PC1 solo → explica ~73% de la varianza
- PC1 + PC2 → explica ~96% de la varianza ← línea verde
- PC1 + PC2 + PC3 → explica ~99% de la varianza
- PC1 + PC2 + PC3 + PC4 → explica 100% de la varianza

**Varianza acumulada**

PC1 captura: 73%
PC2 captura: 23% → acumulado = 73+23 = 96%
PC3 captura: 3% → acumulado = 96+3 = 99%
PC4 captura: 1% → acumulado = 99+1 = 100%

**Figura:** gráfico de línea "Varianza acumulada por componentes". Eje X = "Número de componentes" (1.0 a 4.0), eje Y = "Varianza acumulada" (0.75 a 1.00). Curva azul con puntos en (1, ~0.73), (2, ~0.96), (3, ~0.995), (4, 1.00). Línea roja horizontal punteada en 0.95 etiquetada "95% varianza". Línea verde vertical punteada en x=2 etiquetada "M=2 componentes".

## Slide 22

Dos Derivaciones de PCA

¿Qué nos dice el gráfico concretamente?

Con solo 2 componentes principales en lugar de las 4 features originales:

- Se conserva el 96% de la información
- Se reduce la dimensionalidad a la mitad
- Se pierde solo el 4% de información

¿Qué significan las líneas del gráfico?

Línea roja horizontal — umbral del 95% de varianza. Es el criterio mínimo aceptable de información a conservar.

Línea verde vertical — indica que con M=2 componentes ya se supera ese umbral del 95%.

**Figura:** mismo gráfico de la slide anterior, "Varianza acumulada por componentes", repetido como referencia para la explicación de las líneas roja y verde.

## Slide 23

PCA: Minimizando el Error de Reconstrucción

Podemos pensar en PCA como la proyección de los datos en un subespacio de menor dimensión

Una derivación es que queremos encontrar la proyección tal que la mejor reconstrucción lineal de los datos esté lo más cerca posible de los datos originales

$J(\mathbf{u}, \mathbf{z}, \mathbf{b}) = \sum_n ||\mathbf{x}^{(n)} - \tilde{\mathbf{x}}^{(n)}||^2$     donde     $\tilde{\mathbf{x}}^{(n)} = \sum_{j=1}^{M} z_j^{(n)} \mathbf{u}_j + \sum_{j=M+1}^{D} b_j \mathbf{u}_j$

El objetivo se minimiza cuando los primeros M componentes son los eigenvectores con los eigenvalores máximos

$z_j^{(n)} = \mathbf{u}_j^T \mathbf{x}^{(n)}; \quad b_j = \bar{\mathbf{x}}^T \mathbf{u}_j$

## Slide 24

Aplicando PCA a rostros

Ejecutar PCA en 2429 imágenes en escala de grises de 19x19 (datos CBCL)

**Comprime los datos:** se pueden obtener buenas reconstrucciones con solo 3 componentes

**Figura:** fila de 12 miniaturas en escala de grises de rostros parciales (ojos, nariz, boca) — reconstrucciones/componentes de rostros obtenidos del análisis PCA sobre el dataset CBCL.

**PCA pre-procesamiento:** se puede aplicar un clasificador a la representación latente

PCA con 3 componentes obtiene 79% de accuracy en discriminación rostro/no-rostro en datos de prueba vs. 76.8% para NN con 84 neuronas

¡También puede ser bueno para visualización!

## Slide 25

Ventajas y Desventajas

**Ventajas**
- Reducción de Dimensionalidad
- Independencia de Features
- Reducción de Ruido
- Visualización
- Previene Overfitting
- Elimina Features Correlacionadas
- Acelera los Algoritmos de Machine Learning

**Desventajas**
- Estandarización de Datos
- Pérdida de Interpretabilidad
- Suposición de Linealidad
- Sensibilidad a la Escala
- Los Outliers Impactan los Resultados
- Complejidad $O(d^2n + n^3)$

## Slide 26

3. Singular Value Decomposition (SVD)

**Figura:** imagen decorativa de portada de sección — mano robótica señalando una representación digital de un cerebro/globo terráqueo sobre fondo azul oscuro, con líneas de datos y marcadores de medida punteados en amarillo y celeste.

## Slide 27

Singular Value Decomposition (SVD)

Multiplicar una matriz por un vector no es más que rotar y escalar el vector

$A * \vec{v} = \begin{pmatrix} 3 & \frac{2}{3} \\ 2 & \frac{1}{3} \end{pmatrix} * \begin{pmatrix} 2 \\ 6 \end{pmatrix} = \begin{pmatrix} 10 \\ 6 \end{pmatrix} = 2\sqrt{34} \begin{pmatrix} 0.86 \\ 0.51 \end{pmatrix}$

**Figura:** diagrama vectorial en el plano. Vector negro $\vec{v}$ apunta desde el origen hasta (2, 6). Vector rojo $\sigma\vec{u}$ apunta desde el origen hasta (10, 6), representando el resultado de $A\vec{v}$. Líneas punteadas grises marcan las proyecciones en los ejes (valores 2, 10 en el eje horizontal; 6 en el eje vertical). Ilustra que multiplicar por A rota y escala $\vec{v}$ hacia $\sigma\vec{u}$.

## Slide 28

Singular Value Decomposition (SVD)

**Figura:** diagrama de la factorización SVD de una matriz de "feature face". $M \in \mathbb{R}^{nd}$ (matriz gris rotulada "feature face") = $U \in \mathbb{R}^{nn}$ (matriz de columnas discontinuas, con una columna resaltada en rojo y una flecha señalando "Eigenface") $\times$ $\Sigma \in \mathbb{R}^{nd}$ (matriz diagonal amarilla con valores $\sigma_1, \sigma_2, \ldots, \sigma_d$ en la diagonal y ceros fuera de ella, recuadro naranja punteado resaltando la diagonal) $\times$ $V^T \in \mathbb{R}^{dd}$ (matriz gris de filas discontinuas).

## Slide 29

Singular Value Decomposition (SVD)

**Figura izquierda:** imagen "TrainingFace" — rostro en escala de grises de baja resolución (aprox. 38×48 píxeles, ejes numerados de 0 a 40).

**Figura derecha:** descomposición de esa cara de entrenamiento como suma ponderada de "Eigenfaces", con flechas indicando que $\sigma_i$ (coeficiente escalar) y $\vec{u}_i$ (eigenface/vector singular izquierdo) se combinan. Se muestran 12 eigenfaces en una grilla de 3 filas × 4 columnas, cada una con su coeficiente $\sigma_i$ encima:
Fila 1: -2.076 * , -1.046 * , 2.127 * , 0.037 *
Fila 2: -0.758 * , -0.517 * , 0.856 * , 1.052 *
Fila 3: 0.458 * , 0.013 * , -0.040 * , 0.639 *
El signo "=" con doble barra indica que TrainingFace es igual a la suma ponderada (con los coeficientes $\sigma_i$) de las 12 eigenfaces mostradas.

## Slide 30

SVD: Algoritmo

1. Evaluar los n eigenvectores $\mathbf{v}_i$ y eigenvalores $\lambda_i$ of $A^TA$
2. Hacer una matriz $V$ a partir de los vectores normalizados $\mathbf{v}_i$. Las columnas son llamadas "vectores singulares derechos"

$V = \begin{pmatrix} \vdots & \cdots & \vdots \\ \mathbf{v}_1 & \cdots & \mathbf{v}_n \\ \vdots & \cdots & \vdots \end{pmatrix}$

3. Hacer una matriz diagonal de las raíces cuadradas de los eigenvalores

$\Sigma = \begin{pmatrix} \sigma_1 & & \\ & \ddots & \\ & & \sigma_n \end{pmatrix}$     $\sigma_i = \sqrt{\lambda_i}$  and  $\sigma_1 \geq \sigma_2 \geq \sigma_3 \ldots$

4. Encontrar $U$: $A = U\Sigma V^T \Rightarrow U\Sigma = AV \Rightarrow U = AV\Sigma^{-1}$. Las columnas se llaman "vectores singulares izquierdos".

## Slide 31

Ejemplo 1: imágenes [original]

**Figura:** grilla de 4 filas × 8 columnas (32 fotografías) de un mismo niño en distintas poses y expresiones faciales (serio, sonriendo, guiñando el ojo), en escala de grises, ilustrando el dataset original de imágenes antes de aplicar SVD/compresión.

## Slide 32

Ejemplo 1: imágenes [compresión]

**Figura:** la misma grilla de 4 filas × 8 columnas (32 fotografías) del niño, pero visiblemente más borrosa/con menor detalle, mostrando el resultado de la compresión de las imágenes mediante SVD (reconstrucción con menos componentes/valores singulares).

## Slide 33

Ventajas y Desventajas

**Ventajas**
- Reducción de Dimensionalidad
- Reducción de Ruido
- Estabilidad Numérica

**Desventajas**
- Complejidad Computacional $O(n^3)$
- Altos Requerimientos de Memoria
- Sensibilidad a Valores Faltantes

## Slide 34

4. PCA con SVD — Ejemplo

**Figura:** imagen decorativa de portada de sección — mano robótica señalando una representación digital de un cerebro/globo terráqueo sobre fondo azul oscuro, con líneas de datos y marcadores de medida punteados en amarillo y celeste (misma imagen decorativa que en la slide 26).

## Slide 35

Ejemplo PCA

$A = U\Sigma V^T$

$A = \begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix}$

$A^TA = \begin{bmatrix} 4 & 3 \\ 0 & -5 \end{bmatrix} \begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix} = \begin{bmatrix} 25 & -15 \\ -15 & 25 \end{bmatrix}$

**Figura:** desarrollo manuscrito del ejemplo numérico de PCA vía SVD, mostrando la matriz $A$ y el cálculo paso a paso de $A^TA$.

## Slide 36

Ejemplo PCA

$A = U\Sigma V^T$

$A^TA = \begin{bmatrix} 25 & -15 \\ -15 & 25 \end{bmatrix}$

$A^TA - \lambda I = \begin{bmatrix} 25-\lambda & -15 \\ -15 & 25-\lambda \end{bmatrix}$

$\det(A^TA - \lambda I) = ((25-\lambda)(25-\lambda)) - (-15 \times -15)$

$= (625 - 25\lambda - 25\lambda + \lambda^2) - (225)$

$= \lambda^2 - 50\lambda + 400$

**Figura:** desarrollo manuscrito continuando el ejemplo: planteamiento del polinomio característico de $A^TA$ para hallar los eigenvalores.

## Slide 37

Ejemplo PCA

$A = U\Sigma V^T$

$\lambda^2 - 50\lambda + 400 = 0$

$\lambda^2 - 40\lambda - 10\lambda + 400 = 0$

$\lambda(\lambda - 40) - 10(\lambda - 40) = 0$

$(\lambda - 10)(\lambda - 40)$

Two Eigen Values: 10, 40

**Figura:** desarrollo manuscrito de la factorización del polinomio característico, obteniendo los dos eigenvalores 10 y 40 (subrayados como resultado final).

## Slide 38

Ejemplo PCA

$A = U\Sigma V^T$

$A^TA - 10I = \begin{bmatrix} 25-10 & -15 \\ -15 & 25-10 \end{bmatrix} = \begin{bmatrix} 15 & -15 \\ -15 & 15 \end{bmatrix}$

$\begin{bmatrix} 15 & -15 \\ -15 & 15 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = 0$

**Figura:** desarrollo manuscrito calculando el eigenvector correspondiente al eigenvalor $\lambda=10$: se sustituye $\lambda=10$ en $A^TA - \lambda I$ y se plantea el sistema homogéneo para hallar $v_1, v_2$.

## Slide 39

Ejemplo PCA

$A = U\Sigma V^T$

$\begin{bmatrix} 15 & -15 \\ -15 & 15 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = 0$

Row 1 + Row 2:

$\begin{bmatrix} 15 & -15 \\ 0 & 0 \end{bmatrix}$

Row 1 × 1/15:

$\begin{bmatrix} 1 & -1 \\ 0 & 0 \end{bmatrix}$

$\begin{bmatrix} 1 & -1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

Solve:

$1v_1 - 1v_2 = 0$

$1v_1 = v_2$

$\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ for $v_2 = 1$

**Figura:** desarrollo manuscrito de la reducción por filas del sistema homogéneo hasta obtener la relación $v_1 = v_2$ y el vector solución $[1, 1]^T$.

## Slide 40

Ejemplo PCA

$A = U\Sigma V^T$

$\begin{bmatrix} 1 & -1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

Solve:

$1v_1 - 1v_2 = 0$

$1v_1 = v_2$

$\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ for $v_2 = 1$

$\sqrt{(1)^2 + (1)^2} = \sqrt{2}$

Convert to Unit Vector

$\begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix}$ = EigenVector of EigenValue 10

**Figura:** desarrollo manuscrito final: normalización del vector $[1,1]^T$ (magnitud $\sqrt{2}$) para obtener el eigenvector unitario $[1/\sqrt{2}, 1/\sqrt{2}]^T$ correspondiente al eigenvalor 10.

## Slide 41

**Ejemplo PCA**

$A = U \Sigma V^T$

$A^TA - 40I = \begin{bmatrix} 25-40 & -15 \\ -15 & 25-40 \end{bmatrix} = \begin{bmatrix} -15 & -15 \\ -15 & -15 \end{bmatrix}$

Row 1 + (-1)(Row 2)

$\begin{bmatrix} -15 & -15 \\ 0 & 0 \end{bmatrix}$

$-\frac{1}{15}$ Row 1

$\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$

$\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

$1v_1 + 1v_2 = 0$

$v_1 = -v_2$

$\begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} -1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix}$ = Eigenvector for Eigenvalue 40

## Slide 42

**Ejemplo PCA**

$A = U \Sigma V^T$

Eigenvectors & Eigenvalues are

$\begin{bmatrix} -1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix} = V$

$\begin{bmatrix} \sqrt{40} & 0 \\ 0 & \sqrt{10} \end{bmatrix} = \Sigma$

## Slide 43

**Ejemplo PCA**

$A = U \Sigma V^T$

$A = U \Sigma V^T$

$AV\Sigma^T = U$

$AV = \begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix} \begin{bmatrix} -1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}$

$= \begin{bmatrix} -4/\sqrt{2} & 4/\sqrt{2} \\ -8/\sqrt{2} & -2/\sqrt{2} \end{bmatrix}$

## Slide 44

**Ejemplo PCA**

$A = U \Sigma V^T$

$AV = \begin{bmatrix} -4/\sqrt{2} & 4/\sqrt{2} \\ -8/\sqrt{2} & -2/\sqrt{2} \end{bmatrix}$

$= \begin{bmatrix} -4/\sqrt{2} \times \frac{1}{2\sqrt{10}} & 4/\sqrt{2} \times \frac{1}{\sqrt{10}} \\ -8/\sqrt{2} \times \frac{1}{2\sqrt{10}} & -2/\sqrt{2} \times \frac{1}{\sqrt{10}} \end{bmatrix}$

$AV = \begin{bmatrix} -2/2\sqrt{5} & 4/2\sqrt{5} \\ -4/2\sqrt{5} & -2/2\sqrt{5} \end{bmatrix} = \begin{bmatrix} -1/\sqrt{5} & 2/\sqrt{5} \\ -2/\sqrt{5} & -1/\sqrt{5} \end{bmatrix}$

## Slide 45

**Ejemplo PCA**

$AV\Sigma^T = \begin{bmatrix} -1/\sqrt{5} & 2/\sqrt{5} \\ -2/\sqrt{5} & -1/\sqrt{5} \end{bmatrix} \begin{bmatrix} \sqrt{40} & 0 \\ 0 & \sqrt{10} \end{bmatrix}$

$= \begin{bmatrix} -1/\sqrt{5} \times \sqrt{40} & 2/\sqrt{5} \times \sqrt{10} \\ -2/\sqrt{5} \times \sqrt{40} & -1/\sqrt{5} \times \sqrt{10} \end{bmatrix}$

$= \begin{bmatrix} -\sqrt{\frac{40}{5}} & 2\sqrt{\frac{10}{5}} \\ -2\sqrt{\frac{40}{5}} & -\sqrt{\frac{10}{5}} \end{bmatrix}$

$= \begin{bmatrix} -2\sqrt{2} & 2\sqrt{2} \\ -4\sqrt{2} & -\sqrt{2} \end{bmatrix}$

## Slide 46

**Ejemplo PCA**

$A = U \Sigma V^T$

$U = \begin{bmatrix} -2\sqrt{2} & 2\sqrt{2} \\ -4\sqrt{2} & -\sqrt{2} \end{bmatrix}$

$= \begin{bmatrix} -\frac{2\sqrt{2}}{\sqrt{40}} & \frac{2\sqrt{2}}{\sqrt{10}} \\ -\frac{4\sqrt{2}}{\sqrt{40}} & -\frac{\sqrt{2}}{\sqrt{10}} \end{bmatrix} = \begin{bmatrix} -2\sqrt{\frac{2}{40}} & 2\sqrt{\frac{2}{10}} \\ -4\sqrt{\frac{2}{40}} & -\sqrt{\frac{2}{10}} \end{bmatrix}$

$= \begin{bmatrix} -2/\sqrt{20} & 2/\sqrt{5} \\ -4/\sqrt{20} & -1/\sqrt{5} \end{bmatrix}$

$U = \begin{bmatrix} -1/\sqrt{5} & 2/\sqrt{5} \\ -2/\sqrt{5} & -1/\sqrt{5} \end{bmatrix}$

## Slide 47

**Ejemplo PCA**

$A = U \Sigma V^T$

$\begin{bmatrix} 4 & 0 \\ 3 & -5 \end{bmatrix} = \begin{bmatrix} -1/\sqrt{5} & 2/\sqrt{5} \\ -2/\sqrt{5} & -1/\sqrt{5} \end{bmatrix} \begin{bmatrix} \sqrt{40} & 0 \\ 0 & \sqrt{10} \end{bmatrix} \begin{bmatrix} -1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}$

## Slide 48

**Final Takeaways**

1. PCA reduce dimensionalidad maximizando varianza, facilitando visualización y reduciendo complejidad computacional

2. SVD ofrece mayor estabilidad numérica para PCA en datasets grandes o con ruido

3. Ambos métodos mejoran eficiencia, previenen overfitting y eliminan redundancia

4. Limitaciones: pérdida de interpretabilidad, suposición de linealidad y sensibilidad a outliers

## Slide 49

(Sin texto ni contenido académico visible.)

**Figura:** Fotografía decorativa con overlay azul de dos personas con bata de laboratorio y lentes de protección examinando un equipo/maquinaria con componentes electrónicos y cables, en un laboratorio.
