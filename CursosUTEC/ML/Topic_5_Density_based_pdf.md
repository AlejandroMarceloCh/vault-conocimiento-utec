---
curso: ML
titulo: Topic 5 - Density-based
slides: 34
fuente: Topic 5 - Density-based.pdf
---

## Slide 1

CLUSTERING BASADO EN DENSIDAD

## Slide 2

Objetivos

1. Analizar las diferencias entre los enfoques basados en centroides, jerárquicos y de densidad
2. Definir el clustering basado en densidad e introducir DBSCAN
3. Interpretar visual y cuantitativamente los resultados del clustering

## Slide 3

1. Introducción
Motivación

## Slide 4

¿Cuál es la forma de un cluster?

## Slide 5

¿Cuántos clusters hay?

**Figura:** Dos gráficos de dispersión de puntos negros. A la izquierda, una nube de puntos con forma de espiral doble (dos brazos entrelazados en espiral) más un pequeño grupo disperso de puntos sueltos alrededor. A la derecha, dos formas de medialuna/creciente entrelazadas (una más grande, una más pequeña) junto con un pequeño cluster circular compacto separado y varios puntos sueltos dispersos entre las formas.

## Slide 6

Introducción

Un cluster en una región densa de puntos, separada por regiones poco densas de otras regiones densas.

Útiles cuando los clusters tienen formas irregulares, están entrelazados o hay ruido/outliers en los datos.

**Figura:** Cuatro formas de colores ilustrando tipos de clusters: una forma de "C" gris con dos puntos pequeños (morado oscuro y celeste) dentro de la abertura; dos óvalos morados unidos (forma de mancuerna); un óvalo verde y un óvalo amarillo, ambos separados, de tamaño similar.

## Slide 7

Ejemplo

**Figura:** Dos grupos de puntos negros dispersos irregularmente sobre fondo blanco. El grupo de la izquierda tiene 6 puntos agrupados de forma irregular; el grupo de la derecha tiene 7 puntos agrupados de forma irregular; un punto adicional aislado se ubica entre ambos grupos, más cerca del centro-abajo.

## Slide 8

Ejemplo

**Figura:** A la izquierda, un grupo de 5 puntos rojos rodeados por varios círculos (vecindarios epsilon) superpuestos entre sí, ilustrando cómo estos puntos están densamente conectados; un sexto punto (morado) aislado debajo, sin círculo, fuera del cluster. A la derecha, un grupo de 6 puntos morados dispersos sin círculos de vecindario dibujados (representando un cluster de baja densidad o sin conexión densa).

## Slide 9

Definición de densidad

ε-Neighborhood: Objetos dentro de un radio de ε desde un objeto

$N_{\varepsilon}(p):\{q \mid d(p,q) \le \varepsilon\}$

"Alta densidad": la ε-Neighborhood de un objeto contiene al menos **MinPts** de objetos.

ε-Neighborhood de q
Densidad de q is "bajo"
(MinPts=4)

ε-Neighborhood de p
Densidad de p is "alto"
(MinPts=4)

**Figura:** Dos círculos superpuestos (vecindarios ε) centrados respectivamente en los puntos q y p. El círculo de q contiene solo 2 puntos (q y uno más) dentro de su radio ε, mientras que el círculo de p contiene 3 puntos (p y dos más) dentro de su radio ε, ademas de un cuarto punto turquesa fuera de ambos círculos abajo a la derecha.

## Slide 10

Alcance por densidad

Directamente alcanzable por densidad

Un objeto q es directamente alcanzable por densidad desde el objeto p si p es un objeto núcleo y q está en la ε-Neighborhood de p.

- q es directamente alcanzable por densidad desde p
- p no es directamente alcanzable por densidad desde q
- El alcance por densidad es asimétrico

MinPts = 4

**Figura:** Dos círculos superpuestos (vecindarios ε) con los puntos q y p marcados dentro de la zona de intersección, más un tercer punto turquesa fuera de ambos círculos abajo a la derecha; etiqueta "MinPts = 4" debajo del diagrama.

## Slide 11

Alcance por densidad

Alcanzable por densidad (directa e indirectamente):

- Un punto p es directamente alcanzable por densidad desde p2
- p2 es directamente alcanzable por densidad desde p1
- p1 es directamente alcanzable por densidad desde q
- p <- p2 <- p1 <- q forman una cadena

- p es (indirectamente) alcanzable por densidad desde q
- q no es alcanzable por densidad desde p

MinPts = 7

**Figura:** Cadena de cuatro círculos superpuestos (vecindarios ε), cada uno centrado en un punto de una secuencia q, p1, p2, p, con una flecha diagonal que atraviesa los cuatro círculos desde q hasta p, ilustrando la cadena de alcanzabilidad por densidad. Dentro de cada círculo hay varios puntos rojos (objetos de datos) agrupados densamente.

## Slide 12

Core, Border & Outlier

Dado ε y MinPts, clasifica los objetos en tres grupos exclusivos.

Un punto es **core** si tiene al menos MinPts dentro de su ε—Neighborhood.

Un punto **border** tiene menos de MinPts, pero está en la vecindad de un core.

Un punto **outlier** es un punto que no es ni un punto core ni un punto border.

ε = 1unit, MinPts = 5

**Figura:** Diagrama con un rectángulo que contiene un grupo denso de puntos azules etiquetados "Border" y "Core" (con líneas apuntando a puntos específicos dentro del cluster denso, algunos rodeados por círculos punteados de radio ε), un cluster secundario más disperso de puntos azules sin etiqueta, y un punto aislado arriba a la derecha rodeado por un círculo punteado etiquetado "Outlier".

## Slide 13

Algoritmo

```
for each o ∈ D do
    if o is not yet classified then
        if o is a core-object then
            collect all objects density-reachable from o
            and assign them to a new cluster.
        else
            assign o to NOISE
```

## Slide 14

Ejemplo

- Parameter
  - $\varepsilon$ = 2 cm
  - $MinPts$ = 3

```
for each o ∈ D do
    if o is not yet classified then
        if o is a core-object then
            collect all objects density-reachable from o
            and assign them to a new cluster.
        else
            assign o to NOISE
```

**Figura:** Grupo de 5 puntos rojos rodeados por varios círculos ε superpuestos (indicando alta densidad, candidatos a cluster), y a la derecha un grupo separado de 5 puntos morados dispersos sin círculos (sin evaluar aún).

## Slide 15

Ejemplo

- Parameter
  - $\varepsilon$ = 2 cm
  - $MinPts$ = 3

```
for each o ∈ D do
    if o is not yet classified then
        if o is a core-object then
            collect all objects density-reachable from o
            and assign them to a new cluster.
        else
            assign o to NOISE
```

**Figura:** Un punto rojo aislado con un círculo ε alrededor (evaluándose como no-core, posible ruido) en el centro; a la izquierda un grupo de 5 puntos ahora coloreados en naranja (marcados como cluster/procesados); a la derecha un grupo de 5 puntos morados sin procesar.

## Slide 16

Ejemplo

- Parameter
  - $\varepsilon$ = 2 cm
  - $MinPts$ = 3

```
for each o ∈ D do
    if o is not yet classified then
        if o is a core-object then
            collect all objects density-reachable from o
            and assign them to a new cluster.
        else
            assign o to NOISE
```

**Figura:** A la izquierda, un grupo de 5 puntos naranjas (cluster ya asignado); en el centro, un punto azul oscuro aislado (clasificado como ruido/NOISE, sin círculo); a la derecha, un grupo de 5 puntos rojos rodeados por múltiples círculos ε superpuestos (evaluándose como cluster core denso).

## Slide 17

2. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
Algoritmo y ejemplos

## Slide 18

Densidad

Número mínimo de puntos en el "vecindario":
MinPts = 2

Radio del "vecindario":
Epsilon $\sqrt{2}$ > $\sqrt{10}$

**Figura izquierda:** Cuadrícula cartesiana de 0 a 10 en ambos ejes con 8 puntos etiquetados A1, A2, A3, A4, A5, A6, A7, A8 distribuidos en distintas posiciones. Alrededor de varios puntos (A1, A2, A4/A8, A5, A7) se dibujan círculos concéntricos de dos radios distintos: círculos rojos pequeños (radio √2) y círculos celestes grandes (radio √10), mostrando cómo cambia la vecindad según el radio epsilon elegido.

**Figura derecha:** Imagen satelital de una zona urbana/rural con puntos de colores superpuestos (turquesa, azul, amarillo, negro, magenta/rosa, rojo) agrupados en distintas áreas del mapa: un cluster denso turquesa en el centro urbano, un cluster magenta a la derecha, puntos azules y amarillos dispersos en los bordes, ilustrando clusters de densidad geográfica reales.

## Slide 19

Ventajas

Resistente al Ruido

Puede manejar clusters de diferentes formas y tamaños

**Figura izquierda:** Nube de puntos morados formando las letras "UTEC" (con relleno de puntos), acompañada de puntos sueltos dispersos alrededor como ruido, todos del mismo color morado (sin clusterizar).

**Figura derecha:** La misma nube de puntos con forma "UTEC", pero ahora coloreada por cluster: cada trazo de letra tiene un color distinto (morado, rojo, verde claro, amarillo, celeste, granate), y los puntos sueltos de ruido permanecen en color oscuro/morado, mostrando el resultado de DBSCAN separando correctamente formas irregulares y ruido.

## Slide 20

Ventajas

Resistente al Ruido
Puede manejar clusters de diferentes formas y tamaños

**Figura izquierda:** La misma nube de puntos con forma "UTEC" coloreada por cluster (morado, rojo, granate, amarillo, verde claro, celeste), con puntos de ruido en color oscuro disperso alrededor.

**Figura derecha:** Mapa titulado "Mendoza: clusters de actividad identificados", con calles trazadas en negro sobre fondo gris claro y numerosas elipses/contornos de colores marcando clusters de actividad por categoría, según leyenda: banca (celeste), culto (azul), educación (verde claro), entretenimiento (verde oscuro), gastronomía (rosa), gobierno y serv. públicos (rojo), retail (naranja), salud (naranja oscuro/marrón), servicios (lila). Los clusters de retail y servicios se concentran densamente en el centro de la ciudad, con clusters aislados de otras categorías dispersos en distintas zonas del mapa.

## Slide 21

# Limitaciones

No puede manejar densidades variables

Sensible a los parámetros - es difícil determinar el conjunto correcto de parámetros

**Figura:** Cuatro paneles con resultados de DBSCAN sobre el mismo dataset (una elipse con puntos dispersos tipo diamante verde, un grupo denso rojo, un cluster verde-oliva grande con forma circular irregular y dos sub-clusters pequeños dentro de él) bajo distintos parámetros. Izquierda superior: nube elíptica de puntos verdes dispersos conectada a un grupo pequeño rojo y a un cluster grande verde-oliva con tres sub-clusters densos (dos pequeños círculos oscuros dentro). Debajo, panel etiquetado "(MinPts=4, Eps=9.92)": mismo patrón de puntos coloreado igual (verde disperso, rojo, verde-oliva con dos sub-clusters oscuros). A la derecha, panel superior con la misma elipse de puntos ahora en color lila disperso, unida a un cluster grande rojo (denso) y uno pequeño verde-oliva; debajo panel etiquetado "(MinPts=4, Eps=9.75)": puntos lila dispersos, cluster rojo denso grande y un pequeño cluster verde-oliva. Ilustra cómo, con densidades variables en el mismo dataset, distintos valores de Eps producen agrupamientos muy distintos (fusiona o separa clusters de forma inconsistente).

## Slide 22

# Limitaciones

**Figura:** Figure 8. Resultados de DBSCAN para el dataset DS1 con MinPts=4 y Eps en (a) 0.5 y (b) 0.4. Ambos paneles muestran dos elipses alargadas rojas/anaranjadas en la parte superior (conectadas por un puente de puntos), un círculo grande de puntos en el centro-inferior, y dos clusters pequeños circulares a la derecha (uno naranja oscuro, uno celeste). En (a) el círculo central se colorea casi todo de un mismo tono (naranja/salmón), indicando que DBSCAN lo trata como un solo cluster grande; en (b), con Eps más chico, el mismo círculo se fragmenta en múltiples colores (subclusters azul marino, rojo, verde, lila, etc.), evidenciando sobre-segmentación cuando se ajusta Eps para separar mejor las elipses de arriba.

Figure 9. Resultados de DBSCAN para el dataset DS2 con MinPts=4 y Eps en (a) 5.0, (b) 3.5 y (c) 3.0. Tres paneles muestran un patrón en forma de "reloj de arena"/diamante doble (dos triángulos que se tocan en un punto central). En (a) con Eps=5.0 todo el patrón se colorea casi uniformemente en dos tonos (rojo y salmón), fusionando estructuras. En (b) con Eps=3.5 aparece un cluster azul marino dominante que cubre gran parte de un triángulo y fragmentos de otros colores en los bordes. En (c) con Eps=3.0 el resultado se fragmenta mucho más, con muchos colores pequeños dispersos (verde, rojo, celeste, blanco, naranja, lila) indicando sobre-segmentación severa. Ilustra la alta sensibilidad de DBSCAN al parámetro Eps.

## Slide 23

# 3. OPTICS (Ordering Points To Identify the Clustering Structure)

*Intuición*

## Slide 24

# DBSCAN vs OPTICS

**Figura:** Dos scatter plots lado a lado con ejes "Dim. 1" (horizontal, 0 a 1) y "Dim. 2" (vertical, 0 a 1). Izquierda: todos los puntos en negro, sin clasificar, mostrando tres agrupaciones visuales naturales — una nube pequeña arriba al centro (~x=0.4-0.5, y=0.8-0.9), una nube grande abajo a la izquierda (~x=0.2-0.5, y=0.1-0.5) y otra nube grande abajo a la derecha (~x=0.7-0.95, y=0.15-0.5) — más puntos de ruido dispersos. Derecha: los mismos datos coloreados por cluster: verde (grupo superior), lila/morado (grupo derecho), rojo (grupo inferior central) y puntos grises (ruido/no asignados), mostrando el resultado de un algoritmo de clustering density-based sobre el mismo dataset.

## Slide 25

# Algoritmo

**Figura:** Tres paneles apilados. Arriba a la izquierda: mismo scatter en negro (Dim.1 vs Dim.2) con las tres nubes de puntos sin clasificar. Arriba a la derecha: mismo scatter donde cada nube se conecta mediante un árbol de líneas (estructura tipo árbol/grafo) — un cluster verde arriba, uno rojo/magenta a la izquierda-centro y uno morado/azul a la derecha, con líneas finas violetas conectando los nodos entre clusters (representando el orden/alcanzabilidad entre puntos). Abajo: un gráfico de barras (reachability plot) con eje Y de 0 a 0.25 (doble escala, izquierda y derecha) mostrando "valles" de distinta altura y color — morado, luego rojo, luego un pico angosto naranja, luego verde, terminando en otro pico naranja — con líneas discontinuas de color (morada, roja y verde) que conectan cada valle del gráfico de barras con su correspondiente cluster en el scatter de arriba, ilustrando cómo el reachability plot de OPTICS revela la estructura jerárquica de clusters mediante valles de baja distancia de alcanzabilidad.

## Slide 26

# Algoritmo

1. Comenzamos eligiendo un punto que aún no hayamos visitado. **Calculamos su Distancia Central.**

2. **Preparar la Lista de Prioridad.** Identificamos a todos sus vecinos. Guardamos estos vecinos en la Lista de Prioridad.

3. **Explorar la Zona Densa.** Siempre elegimos y procesamos el punto que esté de primero en la Lista de Prioridad.

4. **Registrar y Repetir.** Registramos el punto y su Distancia de Alcanzabilidad a la Lista de Salida Final.

## Slide 27

# DBSCAN vs OPTICS

**Figura:** Dos scatter plots (Eje X e Y de 0 a 1, sin etiqueta explícita de ejes salvo marcas numéricas) mostrando el mismo dataset de tres nubes (verde arriba-izquierda, morado a la derecha, rojo/magenta en el centro-abajo) más puntos grises de ruido. Izquierda: clasificación con más puntos grises (no asignados) alrededor de los tres clusters coloreados. Derecha: clasificación alternativa donde casi todos los puntos grises pasaron a formar parte del cluster rojo (que ahora es mucho más grande y disperso), y quedan solo un par de puntos verdes sueltos fuera del cluster verde principal — comparando cómo dos corridas/algoritmos (probablemente DBSCAN vs OPTICS con distinto criterio de corte) asignan de forma distinta los puntos de borde/ruido.

## Slide 28

# 4. HDBSCAN (Hierarchical DBSCAN)

*Intuición*

## Slide 29

# Algoritmo

**Figura:** Dos scatter plots con ejes X e Y de 0.5 a 2.5 (aprox.), mostrando una nube de puntos azules claros dispersos a la izquierda y un pequeño grupo de puntos marcados con "X" a la derecha-centro. Izquierda: un círculo azul oscuro centrado en un punto (marcado con un punto azul sólido) con una flecha horizontal etiquetada "core distance" que indica el radio hasta llegar al k-ésimo vecino más cercano (que incluye las X cercanas). Derecha: tres círculos concéntricos/superpuestos de distinto color (verde arriba, azul-lila en el centro, rojo abajo), cada uno centrado en un punto de color correspondiente (verde, azul oscuro, rojo) con su propia flecha "core distance", mostrando que cada punto tiene su propia distancia núcleo (core distance) según su densidad local, y estos círculos se superponen sobre el mismo conjunto de puntos X.

## Slide 30

# Algoritmo

**Figura:** Dos scatter plots idénticos en configuración a la slide anterior (tres círculos: verde, azul-lila, rojo, cada uno con su "core distance"). Izquierda: se dibuja una flecha bidireccional etiquetada "d_reach(•,•)" desde el punto verde hasta un punto dentro del círculo azul, ilustrando la distancia de alcanzabilidad entre dos puntos. Derecha: se dibuja una línea diagonal amarilla/dorada entre el punto verde y el punto rojo, etiquetada "d(•,•) = d_reach(•,•)", indicando que cuando la distancia real entre dos puntos ya es mayor que ambas core distances, la distancia de alcanzabilidad es igual a la distancia euclidiana real.

Fórmula: $d_{\text{mreach-}k}(a,b) = \max\{\text{core}_k(a), \text{core}_k(b), d(a,b)\}$

## Slide 31

# Algoritmo

**Figura:** Un grafo/árbol (Árbol de Mínimo Recubrimiento, MST) con nodos grises circulares conectados por aristas coloreadas según una escala de color lateral etiquetada "Mutual reachability distance" que va de 0.16 (morado oscuro) a 0.80 (amarillo). El grafo muestra dos ramificaciones densas arriba (una a la izquierda, otra a la derecha, con muchas aristas cortas moradas/azules indicando puntos muy cercanos) conectadas por aristas largas amarillas/verdes (alta distancia de alcanzabilidad) a un nodo central, el cual se conecta hacia abajo con una estructura en forma de espiral/serpentina de nodos con aristas de tonos azul-verdosos intermedios. Ilustra cómo se construye la jerarquía de clusters de HDBSCAN a partir del MST ponderado por distancia mutua de alcanzabilidad.

## Slide 32

# Algoritmo

1. Re-define la Distancia (La Dureza del Enlace). Calcula la Distancia Mutua de Alcanzabilidad.

2. Crea un Árbol de Mínimo Recubrimiento (MST). Construye la Jerarquía de Clusters.

3. Extrae los Clusters Estables. Mide la Persistencia. Selecciona los Mejores Grupos.

## Slide 33

# DBSCAN vs OPTICS vs HDBSCAN

**Figura:** Tres paneles comparativos sobre el mismo dataset sintético (dos nubes elípticas magenta/rosa arriba a la izquierda, un grupo gris pequeño al centro, una forma de "S"/espiral turquesa arriba a la derecha, un patrón de anillos concéntricos abajo a la izquierda —anillo exterior + círculo interior denso—, y una nube difusa celeste/azul abajo a la derecha, más puntos de ruido dispersos en azul oscuro). Panel (a) DBSCAN, score 0.6935: anillos coloreados naranja (exterior) y rojo (interior), nube difusa celeste abajo a la derecha. Panel (b) OPTICS, score 0.7492: mismos anillos ahora coloreados azul (exterior) y verde (interior), nube difusa celeste. Panel (c) HDBSCAN*, score 0.7546: anillos coloreados azul (exterior) y naranja (interior), nube difusa en amarillo pálido; además el grupo gris pequeño del centro-superior aparece separado en un color distinto (verde claro) en (c), a diferencia de (a) y (b) donde queda mezclado/gris. Los números (0.6935, 0.7492, 0.7546) son puntajes de calidad de clustering, mostrando que HDBSCAN* obtiene el mejor desempeño de los tres métodos en este dataset.

## Slide 34

(Slide de cierre de sección, solo imagen decorativa de fondo con dos personas en laboratorio observando un equipo con brazos robóticos; sin texto ni contenido académico visible.)
