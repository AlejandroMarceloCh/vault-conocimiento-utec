---
curso: ML
titulo: Topic 5 - Centroid-based
slides: 29
fuente: Topic 5 - Centroid-based.pdf
---

## Slide 1

INTRODUCCIÓN A CLUSTERING

## Slide 2

Objetivos

1. Comprender los fundamentos del aprendizaje no supervisado

2. Identificar y describir los principales métodos de clustering

3. Interpretar y evaluar resultados de agrupamiento

4. Interpretar el resultado de clustering basado en centroides

## Slide 3

1.
Aprendizaje no supervisado
*Clustering*

## Slide 4

Principales aplicaciones

Los principales problemas y enfoques en el aprendizaje no supervisado se dividen en tres clases.

1. **Reducción de dimensionalidad:** representar cada caso de entrada utilizando un número reducido de variables (ej. análisis de componentes principales, análisis factorial, análisis de componentes independientes).

2. **Clustering:** representar cada caso de entrada utilizando un ejemplo prototipo (por ejemplo, k-means, modelos de mezcla).

3. **Estimación de densidad:** estimar la distribución de probabilidad sobre el espacio de los datos.

## Slide 5

Clustering

**Figura:** Dos diagramas de dispersión lado a lado bajo el título "Clustering". A la izquierda, "Original Data": un conjunto de 9 puntos grises dispersos sin agrupar en el plano x-y. Una flecha central con la etiqueta "Clustering" apunta hacia la derecha. A la derecha, "Clustered Data": los mismos puntos ahora agrupados y coloreados en tres círculos: un grupo naranja (2 puntos) arriba a la izquierda, un grupo verde (3 puntos) arriba a la derecha, y un grupo azul (4 puntos) abajo.

## Slide 6

2.
Clustering
*Introducción y clasificación*

## Slide 7

Clustering

**Objetivo:** Agrupar **N ejemplos** en **K grupos** es uno de los problemas canónicos en el aprendizaje no supervisado.

Asumimos que los datos fueron generados a partir de distintas clases. El objetivo es agrupar juntos los datos que pertenecen a la misma clase.

¿Cuántas clases?

¿Por qué no colocar cada punto en una clase separada?

**Figura:** Diagrama de dispersión con ejes de 0 a 1 (etiquetados 0.2, 0.4, 0.6, 0.8, 1 en ambos ejes, en color rojo). Muestra cuatro nubes de puntos morados/violeta bien diferenciadas: una arriba a la izquierda (~0.2-0.4, ~0.7-0.8), una arriba a la derecha (~0.8-1, ~0.6-0.75), y dos nubes adyacentes en la parte inferior central (~0.2-0.4 y ~0.5-0.7, ambas alrededor de 0.2-0.4 en y).

## Slide 8

¿Cuál es la función objetivo que se optimiza en un clustering razonable?

## Slide 9

Clustering

Asumamos que la data $\{\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(N)}\}$ residen en un espacio euclidiano $\mathbf{x}^{(n)} \in \mathbb{R}^d$

Asumamos que los datos pertenecen a **K** clases (patrones).

¿Cómo podemos identificar las clases (a donde pertenece cada punto?)

**Figura:** Diagrama de dispersión simple dentro de un recuadro, con 9 puntos negros distribuidos sin agrupamiento visual marcado (sin ejes numerados, solo el marco del gráfico), ilustrando datos sin clases identificadas.

## Slide 10

TIPOS DE CLUSTERING

**Figura:** Tabla titulada "Clustering Algorithm Type" con tres columnas: "Clustering Algorithm Type", "Clustering Methodology" y "Algorithm(s)". Cuatro filas, cada una con una miniatura ilustrativa:
- **Centroid-based:** miniatura de un plano dividido en regiones de Voronoi coloreadas con puntos y marcas "x" (centroides). Metodología: "Cluster points based on proximity to centroid". Algoritmos: KMeans, KMeans++, KMedoids.
- **Connectivity-based:** miniatura de un dendrograma (árbol jerárquico). Metodología: "Cluster points based on proximity between clusters". Algoritmos: Hierarchical Clustering (Agglomerative and Divisive).
- **Density-based:** miniatura de tres nubes de puntos coloreadas (rojo oscuro, verde, naranja) con puntos negros de ruido dispersos. Metodología: "Cluster points based on their density instead of proximity". Algoritmos: DBSCAN, OPTICS, HDBSCAN.
- **Distribution-based:** miniatura de una nube naranja circular y una nube azul alargada diagonal. Metodología: "Cluster points based on their likelihood of belonging to the same distribution". Algoritmos: Gaussian Mixture Models (GMMs).

## Slide 11

4.
K-Means
*Clustering*

## Slide 12

K-Means

**Figura:** Diagrama de dispersión titulado "Start!" con ejes x e y de -0.5 a 1.5. Muestra tres nubes de puntos negros: una arriba a la izquierda (~0-0.3, ~0.6-1.3), una arriba a la derecha (~1-1.5, ~0.5-1.4), y una abajo a la derecha (~0.8-1.4, ~-0.5-0.2). Cerca del origen (0,0) hay tres marcadores en forma de diamante de colores distintos (verde, rojo, azul) muy cercanos entre sí, representando los centroides inicializados aleatoriamente, alejados de las nubes de datos reales.

## Slide 13

K-Means

**Inicialización**
Inicializar aleatoriamente los centros de los clusters.

**Algoritmo EM**
Paso expectation: Asignar cada punto de datos al cluster más cercano.

Paso de maximization: Mover cada centro de cluster al centroide de los datos asignados a él.

**Figura:** Mismo diagrama de dispersión que la slide anterior ("Start!", ejes -0.5 a 1.5), con las tres nubes de puntos negros y los tres centroides (diamantes verde, rojo y azul) inicializados cerca del origen, lejos de los clusters reales.

## Slide 14

K-Means

**Inicialización**
Inicializar aleatoriamente los centros de los clusters.

**Algoritmo EM**
Paso expectation: Asignar cada punto de datos al cluster más cercano.

Paso de maximization: Mover cada centro de cluster al centroide de los datos asignados a él.

**Figura:** Diagrama de dispersión con puntos negros distribuidos en cuatro nubes (arriba-izquierda, arriba-derecha muy densa, centro y abajo-centro). Se muestran cuatro marcadores triangulares de colores (azul, verde, naranja, rojo) posicionados como centroides intermedios, cada uno más cerca de su nube correspondiente que en la inicialización, mostrando un paso intermedio del algoritmo EM tras algunas iteraciones.

## Slide 15

**Figura:** Panel de 9 subgráficos (a) a (i) en una cuadrícula 3x3, mostrando la evolución iterativa de k-means sobre dos nubes de puntos (una verde/púrpura y otra roja), cada uno con ejes -2 a 2:
- (a) Datos originales en verde, con dos marcas "x" (púrpura y roja) como centroides iniciales, sin asignación de color aún.
- (b) Se traza una línea magenta divisoria (frontera de decisión); los puntos se colorean en púrpura o rojo según el centroide más cercano.
- (c) Los centroides ("x" blanca) se recalculan y mueven ligeramente, la frontera se ajusta.
- (d) Frontera magenta con mayor inclinación, separando más claramente el grupo púrpura (abajo) del rojo (arriba).
- (e) Centroides actualizados, puntos ya coloreados consistentemente (púrpura abajo, rojo arriba), sin línea divisoria dibujada.
- (f) Nueva frontera magenta con distinta inclinación, cruzando cerca del punto de contacto entre grupos.
- (g) Centroides estables, asignación de colores consolidada.
- (h) Otra línea de frontera magenta con inclinación pronunciada, similar a pasos anteriores, probando distintas orientaciones.
- (i) Estado final estable: dos clusters bien separados (púrpura y rojo), cada uno con su centroide marcado con "x" blanca, sin cambios adicionales — el algoritmo ha convergido.

## Slide 16

¿Cuál es la función objetivo que se optimiza en k-means?

## Slide 17

Objetivo de k-means

**K-means Objective:**
Find cluster centers **m** and assignments **r** to minimize the sum of squared distances of data points $\{\mathbf{x}^{(n)}\}$ to their assigned cluster centers

$$\min_{\{\mathbf{m}\},\{\mathbf{r}\}} J(\{\mathbf{m}\},\{\mathbf{r}\}) = \min_{\{\mathbf{m}\},\{\mathbf{r}\}} \sum_{n=1}^{N}\sum_{k=1}^{K} r_k^{(n)} ||\mathbf{m}_k - \mathbf{x}^{(n)}||^2$$

$$\text{s.t.} \sum_{k} r_k^{(n)} = 1, \forall n, \quad \text{where} \quad r_k^{(n)} \in \{0,1\}, \forall k,n$$

where $r_k^{(n)} = 1$ means that $\mathbf{x}^{(n)}$ is assigned to cluster $k$ (with center $\mathbf{m}_k$)

El método de optimización es una forma de descenso por coordenadas ("descenso por bloques de coordenadas").

Optimización en 2 pasos: **Expectation, Maximization**

## Slide 18

Algoritmo

1) Inicialización: Establecer las **K medias** de los clusters m₁, ..., m_K con valores aleatorios

2) Repetir hasta convergencia (hasta que los centroides no cambien):
   a) **Expectation:** Cada punto x^(n) es asignado al centroide más cercano

   $$\hat{k}^n = \arg\min_{k} d(\mathbf{m}_k, \mathbf{x}^{(n)})$$

   (con, por ejemplo, distancia euclidiana) y clusters de 1 a k

   a) **Maximization:** Los centroides se actualizan para que coincidan con el centroide de los nuevos puntos asignados a los clusters.

   $$\mathbf{m}_k = \frac{\sum_n r_k^{(n)} \mathbf{x}^{(n)}}{\sum_n r_k^{(n)}}$$

## Slide 19

Test de convergencia

Si las asignaciones no cambian en el paso de asignación, hemos convergido (al menos a un mínimo local).

**Figura:** Gráfico de línea con eje y "J" (de 0 a 1000) y eje x de 1 a 4 (pasos, marcados en intervalos de 0.5). Una curva verde desciende desde un valor alto (~1050) en el paso 0.5 (marcador círculo púrpura), cae abruptamente hasta ~300 en el paso 1 (círculo rojo), sigue bajando a ~150 en el paso 1.5 (círculo púrpura), y luego se estabiliza cerca de 0 desde el paso 2 en adelante (alternando círculos rojos y púrpuras en los pasos 2, 2.5, 3, 3.5, 4), indicando convergencia.

Función de costo de K-means después de cada paso **E (azul)** y paso **M (rojo)**. El algoritmo ha convergido después del tercer paso M.

## Slide 20

Limitaciones

El objetivo **J** es no convexo (por lo que el descenso por coordenadas en **J** no garantiza converger al mínimo global).

**Figura:** Dos diagramas lado a lado. A la izquierda, "A bad local optimum": una curva azul con múltiples valles de distinta profundidad; los valles poco profundos están etiquetados "Local Optima" (rellenos de rojo, indicando puntos de bajo costo pero no óptimos) y el valle más profundo está etiquetado "Global Optimum". A la derecha, un diagrama esquemático: a la izquierda tres nubes de puntos negros encerradas en óvalos azules (datos sin clasificar), con dos flechas que apuntan a dos resultados posibles: arriba, "GLOBAL OPTIMUM", donde los puntos se agrupan correctamente en dos colores (azul oscuro y rojo, con marcas "x" como centroides) según sus nubes naturales; abajo, "LOCAL OPTIMA", con dos ejemplos donde la asignación de colores (azul, rojo, verde) no corresponde a las nubes naturales de datos, mostrando un agrupamiento subóptimo.

Nada impide que k-means se quede atascado en mínimos locales. Podríamos intentar con muchos puntos de inicio aleatorios.

## Slide 21

Aplicaciones: Vector Quantization

**Figura:** Cuadrícula de 2 filas × 4 columnas con imágenes de niños (fotografías) cuantizadas con distinto número de colores/clusters K. Columnas etiquetadas $K=2$, $K=3$, $K=10$, "Original image". Fila superior: niño sonriendo asomado en un inflable amarillo, junto a otra figura de fondo; a medida que K aumenta la imagen recupera más colores y detalle, hasta acercarse a la imagen original a la derecha. Fila inferior: niño con cascos/orejeras rojas en un asiento con cinturón de seguridad, mismo patrón de cuantización progresiva de K=2 a K=10 comparado con la imagen original.

## Slide 22

Aplicaciones: Vector Quantization

**Figura:** Tres imágenes fotográficas segmentadas mediante superpíxeles (teselado tipo mosaico con celdas irregulares delimitadas por líneas negras, y una línea diagonal blanca que atraviesa cada imagen dividiéndola en dos mitades comparativas). Imagen 1: rostro de una mujer con velo/red sobre la cara. Imagen 2: un pez payaso (clownfish) entre una anémona verde. Imagen 3: un árbol sin hojas junto a construcciones de piedra tipo iglú/muros de adobe en un paisaje campestre.

## Slide 23

5.

Limitaciones
*K-means++ & K-medoids*

## Slide 24

Inicialización

K-Means ++

**Figura (izquierda):** Diagrama titulado "Nine Data Items in Two-Dimension into Three Clusters", plano cartesiano con ejes X (0-9) e Y (0-8) y grilla. Nueve puntos rojos distribuidos en el plano. Se marca "first initial mean" en el punto (3,6), rodeado con un círculo. Desde ahí, líneas punteadas conectan a otros puntos indicando distancias; se señala con flecha azul el punto (3,7) como "Least likely third mean (smallest distance^2)". Se marca "second initial mean" en el punto (4,3), también rodeado con un círculo, con líneas punteadas hacia varios puntos y una flecha azul señalando el punto (8,4) como "Most likely third mean (largest distance^2)".

**Figura (derecha):** Panel titulado "k-means iteration: 1" con dos subgráficos de dispersión: "Initialization #1" (SSE: 6735.8) e "Initialization #2" (SSE: 5238.5). Ambos muestran tres nubes de puntos coloreadas (naranja arriba, roja/naranja abajo a la izquierda, azul abajo a la derecha) en ejes de -10 a 15 aproximadamente, con centroides marcados con "X" negra en distintas posiciones según la inicialización, y leyenda "centroid" en el segundo panel.

## Slide 25

Maximización

**Figura (izquierda, "K-Means"):** Serie de 7 subgráficos ("Iteration: 1" a "Iteration: 7") mostrando la evolución de un clustering K-Means sobre un mismo conjunto de datos en dos dimensiones (ejes aproximadamente 0-10 en X, -10 a 2 en Y). Los puntos están coloreados según su asignación a 3 clusters (leyenda 0=morado, 1=naranja, 2=amarillo) y los centroides se muestran como puntos negros grandes que se desplazan iteración a iteración hasta estabilizarse.

**Figura (derecha, "K-Means++"):** Serie de 4 subgráficos ("Iteration: 1" a "Iteration: 4") sobre el mismo dataset, mostrando que con inicialización K-Means++ el algoritmo converge en muchas menos iteraciones (los clusters ya se ven casi correctamente formados desde la Iteración 1).

## Slide 26

Maximización

**Figura:** Comparación esquemática entre "K-Means Clustering" (izquierda) y "K-Medoids Clustering" (derecha), cada una encerrada en un óvalo rojo punteado con puntos azules ("Data Point") representando datos. En K-Means se marca el centro con una estrella verde ("Cluster Mean"), ubicada en una posición calculada (promedio) que no necesariamente coincide con un dato real. En K-Medoids se marca el centro con un rombo/diamante amarillo con un punto azul dentro ("Cluster Medoid"), indicando que el medoide es un punto de dato real (no un promedio).

## Slide 27

Maximización

**Figura:** Dos gráficos de dispersión lado a lado con ejes X (-6 a 12) e Y (-4 a 6), mostrando el mismo conjunto de datos con tres grupos de puntos: cuadrados azules, triángulos cian y círculos rojos, distribuidos en tres regiones (izquierda, centro, derecha). El gráfico izquierdo muestra el agrupamiento original/base; el gráfico derecho muestra el resultado tras aplicar el algoritmo de clustering, donde se observa un leve solapamiento entre los cuadrados azules y los triángulos cian en la región central-izquierda, evidenciando una diferencia en la asignación de puntos frente al agrupamiento original.

## Slide 28

Maximización

**Figura:** Dos gráficos de dispersión en R, titulados "Kmedoids Cluster" (izquierda) y "Kmeans Cluster" (derecha), con ejes X (-5 a 5 aprox.) e Y (-10 a 5 aprox.). Los puntos están representados como círculos vacíos (azules y negros) agrupados en dos clusters. En cada gráfico se dibuja un círculo grande alrededor de cada cluster indicando su dispersión, con una cruz marcando el centro: en "Kmedoids Cluster" el centro está representado por un punto sólido (medoide, un dato real); en "Kmeans Cluster" el centro está representado igualmente con un punto sólido pero corresponde a la media calculada del cluster. Se observa que la posición y tamaño de los clusters difiere levemente entre ambos métodos.

## Slide 29

Resumen K-Means

**Figura:** Diagrama de flujo tipo infografía dividido en dos filas.

Fila superior, cuatro etapas conectadas por flechas naranjas:
1. "Intuition" → nube de puntos azules dispersos etiquetada "Raw Data".
2. "Initialization" → los mismos puntos azules con tres marcas "X" naranjas superpuestas, etiquetada "Centroids".
3. "Assignment" → puntos verdes con flechas naranjas convergiendo hacia un punto naranja central (el centroide atrayendo a los puntos asignados).
4. "Convergence" → puntos morados con un punto naranja central, representando el resultado final estable.

Fila inferior, conexión "Mathematics" ——— "Code":
- Bajo "Mathematics": texto "minimize **WCSS (Inertia)**" con un pequeño diagrama de puntos verdes con un centro naranja y dos flechas hacia una versión más compacta/ordenada de los mismos puntos.
- Bajo "Code": bloque de código de fondo gris:
```
kmeans = KMeans
n_clusters = 3)
kmeans.fit(X)
labels = kmeans.label_
```
- A la derecha, "Visualization": gráfico de línea descendente titulado "Elbow Method", con 4 puntos morados conectados mostrando una curva decreciente típica del método del codo (eje Y sin etiqueta numérica, disminuye y luego se aplana).
