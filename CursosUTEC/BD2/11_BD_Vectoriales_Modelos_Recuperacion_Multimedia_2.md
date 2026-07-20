---
curso: BD2
titulo: 11 BD Vectoriales - Modelos Recuperación Multimedia 2
slides: 58
fuente: 11 BD Vectoriales - Modelos Recuperación Multimedia 2.pdf
---

# 11 BD Vectoriales - Modelos Recuperación Multimedia 2

## Índice

| Sección | Subtemas |
|---------|----------|
| [Modelos de Recuperación Multimedia — Búsqueda Eficiente](#modelos-de-recuperación-multimedia--búsqueda-eficiente) | Exploración secuencial, Filtrar-y-refinar, Lower Bounding Distance |
| [Índices Multidimensionales](#índices-multidimensionales) | Regiones espaciales, Índices con soporte KNN |
| [Maldición de Dimensionalidad](#maldición-de-dimensionalidad) | Distribución de distancias, Convergencia de vecindarios |
| [Modelos de Recuperación Multimedia — Descriptores Locales](#modelos-de-recuperación-multimedia--descriptores-locales) | Estrategias, SIFT, Similitud, Condiciones, Ventajas, Desventajas |
| [Índice Multidimensional con Descriptores Locales](#índice-multidimensional-con-descriptores-locales) | Un solo índice, Búsqueda |
| [Cuantización de Descriptores Locales](#cuantización-de-descriptores-locales) | Bag of Visual Words |
| [Índice Invertido con Descriptores Locales](#índice-invertido-con-descriptores-locales) | Construcción, Búsqueda |
| [Segmentación de audio con ventanas deslizantes](#segmentación-de-audio-con-ventanas-deslizantes) | — |
| [Recuperación Eficiente](#recuperación-eficiente) | Texto, Imágenes, Audio |
| [Búsqueda Aproximada](#búsqueda-aproximada) | ANN, Comparación lineal vs aproximada, Técnicas |
| [Implementaciones](#implementaciones) | PostgreSQL, Python, pgvector |
| [Glosario](#glosario) | — |

## Modelos de Recuperación Multimedia — Búsqueda Eficiente

4.
Modelos de Recuperación Multimedia
Búsqueda Eficiente

**Figura:** Slide dividida en dos zonas. en el centro un número grande «4.» con subrayado azul, un icono de portapapeles azul con viñetas y el título «Modelos de Recuperación Multimedia» en negrita; debajo, el subtítulo «Búsqueda Eficiente» en azul claro y cursiva. Líneas decorativas azules y amarillas en los bordes.

### Algoritmos de Búsqueda: exploración secuencial

- Búsqueda por rango

```
Algorithm RangeSearch(Q, r)
1.   result = [ ]
2.   for all objects Ci in the collection
3.        dist = Dist(Q, Ci)
4.        if dist < r
5.           append(result, Ci )
6.        endif
7.   endfor
8.   return result
```

$$O(N \times D^p)$$

- $N$: # de elementos en la colección
- $D$: dimensión del espacio característico
- $p$: indica el tipo de distancia (lineal, cuadrática)

**Figura:** A la izquierda, caja con el pseudocódigo del algoritmo `RangeSearch(Q, r)`; la palabra `Dist` en la línea 3 aparece resaltada en azul. A la derecha del algoritmo, la complejidad computacional $O(N \times D^p)$ en texto rojo y negrita, seguida de las definiciones de las variables $N$, $D$ y $p$.

- Búsqueda de los k vecinos más cercanos

```
Algorithm KnnSearch(Q, k)
1.   result = [ ]
2.   for all objects Ci in the collection
3.        dist = Dist(Q, Ci)
4.        append(result, {Ci , dist})
5.   endfor
6.   orderByDist(result)
7.   return result[1:k]
```

$$O(N \times D^p) + O(N \times \log N)$$

- $N$: # de elementos en la colección
- $D$: dimensión del espacio característico
- $p$: indica el tipo de distancia (lineal, cuadrática)

**Figura:** A la izquierda, caja con el pseudocódigo del algoritmo `KnnSearch(Q, k)`. A la derecha, la fórmula de complejidad $O(N \times D^p) + O(N \times \log N)$ en texto rojo, seguida de las definiciones de $N$, $D$ y $p$.

- La complejidad computacional está en función de:
  - $O(N)$: La cantidad de elementos en la colección puede ser muy grande.
  - $O(D^p)$: La función de distancia puede ser cuadrática $p \geq 1$.
- Se requiere métodos eficientes para encontrar los objetos similares a una consulta.
  - Índices y algoritmos de búsqueda

**Figura:** Texto organizado en viñetas jerárquicas. Las notaciones $O(N)$, $O(D^p)$ y la desigualdad $p \geq 1$ aparecen en tipografía matemática en negrita.

(slides 3–5)

### Algoritmos de Búsqueda: filtrar-y-refinar

- Método basado en filtrar-y-refinar
  - La verdadera distancia entre objetos puede ser:
    - Una distancia métrica.
    - Una distancia no métrica.
  - Distancia verdadera (en general) costosa de calcular.
  - Para responder una consulta se utiliza una arquitectura multi-step
    - Objetos recuperados desde el índice no son el resultado, sino sólo candidatos.

**Figura:** Texto organizado en viñetas jerárquicas (círculos para el primer nivel, cuadrados para el nivel más profundo).

- Método basado en filtrar-y-refinar
  - El conjunto de candidatos debe ser pequeño con respecto al tamaño de la BD.
    - Selectividad del filtro
  - Para los candidatos se mide la distancia verdadera con el objeto de consulta (es más cara, pero más selectiva).

$$\sigma_F = \frac{\# \text{ de candidatos}}{\# \text{ de objetos en la BD}}$$

**Figura:** Viñetas jerárquicas describiendo el tamaño del conjunto de candidatos y la medición de distancia verdadera. Junto al texto «Selectividad del filtro» aparece la fórmula $\sigma_F = \frac{\# \text{ de candidatos}}{\# \text{ de objetos en la BD}}$.

- Método basado en filtrar-y-refinar
  - Filtrado en cascada
    - Primer filtro determina candidatos con el índice
    - Filtros siguientes reducen el conjunto de candidatos
    - Paso de refinamiento determina rectitud de la respuesta

**Figura:** Viñetas jerárquicas sobre el filtrado en cascada.

- Método basado en filtrar-y-refinar

**Figura:** Diagrama de flujo del método filtrar-y-refinar. En la parte superior, la consulta $Q$ apunta hacia abajo hacia un triángulo etiquetado «INDEX». Una caja «Filter» tiene una flecha punteada hacia el índice. Debajo del índice, múltiples flechas conducen a un cilindro (base de datos) que contiene varios iconos cuadrados que representan objetos de datos. Este paso produce un subconjunto etiquetado «candidates», representado por tres iconos tipo documento. Una caja «Refine» tiene una flecha punteada hacia una flecha horizontal negra grande etiquetada «Dist» (cálculo de distancia). La flecha «Dist» apunta desde los «candidates» hacia un único icono de documento final etiquetado «The chosen ones».

- Método basado en filtrar-y-refinar

**Figura:** Diagrama de flujo con filtrado en cascada, de izquierda a derecha. En la parte superior, la consulta $Q$ apunta hacia un triángulo etiquetado «INDEX». Una caja «Filter 1» tiene flecha punteada hacia el índice. Múltiples flechas del índice conducen a un cilindro (base de datos) con iconos rectangulares de datos. Salida: grupo de tres iconos de documento etiquetados «candidates». Los candidatos fluyen hacia una flecha horizontal negra grande etiquetada «$LB$» (Lower Bound). Una caja «Filter 2» apunta con flecha punteada hacia el paso $LB$. Salida: grupo más pequeño de dos iconos de documento etiquetados «fewer candidates». Los candidatos reducidos fluyen hacia otra flecha horizontal negra grande etiquetada «Dist». Una caja «Refine» apunta con flecha punteada hacia el paso Dist. Salida final: un único icono de documento etiquetado «The chosen ones».

- Método basado en filtrar-y-refinar
  - Caso ideal para filtrar-y-refinar
    - Distancia filtro debe ser cota inferior (lower bound) de la distancia verdadera
      - Así, se garantiza que no se pierda ningún objeto relevante (no hay falsos negativos)
  - Si el filtro no es cota inferior
    - Pueden haber falsos negativos
      - No se garantiza que el resultado esté completo

**Figura:** Viñetas jerárquicas. El texto «Distancia filtro debe ser cota inferior (lower bound) de la distancia verdadera» aparece en negrita.

(slides 6–11)

### Algoritmos de Búsqueda: Lower Bounding Distance

- Dynamic Time Warping distance

https://www.cs.ucr.edu/~eamonn/tutorials.html

http://ciir.cs.umass.edu/pubfiles/mm-38.pdf

**Figura (lado izquierdo — análisis de forma de pez):** Imagen en escala de grises de un pez con contorno azul alrededor de su cuerpo. Varias líneas rectas de colores (rosa, verde, celeste y naranja) conectan puntos específicos del contorno del pez con puntos correspondientes en un gráfico de forma de onda azul debajo. El gráfico de línea azul representa el contorno del pez como una señal unidimensional (distancia desde un punto central hasta el borde, trazada sobre el ángulo). Debajo, tres siluetas negras de diferentes especies de peces (una raya, un pez triangular y un pez fusiforme estándar). Fuente: `https://www.cs.ucr.edu/~eamonn/tutorials.html`.

**Figura (lado derecho — análisis de forma de hoja):** Imagen de una hoja verde identificada como «Acer circinatum (Oregon Vine Maple)». A su derecha, un contorno simplificado de la hoja codificado por colores en segmentos rojo, azul y verde. Debajo del contorno, un gráfico de línea segmentado donde los colores (rojo, azul, verde, rojo) corresponden a diferentes partes del perímetro de la hoja; líneas grises conectan los vértices del contorno con puntos del gráfico segmentado. Debajo, tres siluetas negras de distintas formas de hojas (una hoja pinnada, una hoja ovalada serrada y una hoja tipo arce). Fuente: `http://ciir.cs.umass.edu/pubfiles/mm-38.pdf`.

- Dynamic Time Warping distance

Speech matching

**Figura:** Ilustración de «Speech matching» mediante Dynamic Time Warping. Dos formas de onda de audio apiladas verticalmente: la superior en azul y la inferior en amarillo-verdoso. Líneas discontinuas negras conectan picos y valles específicos de la forma de onda superior con características correspondientes en la inferior, mostrando cómo DTW alinea señales con variaciones temporales. Entre las dos formas de onda, etiquetas de palabras de izquierda a derecha: «doors», «and», «corners», «kid», «that's», «where», «you», «they», «get». En la parte superior derecha del área del gráfico, el texto «Dynamic Time Warping» en gris claro.

- Dynamic Time Warping distance

**Figura (gráfico izquierdo — emparejamiento euclidiano):** Dos curvas de series temporales (línea roja arriba y línea azul abajo) conectadas por líneas grises estrictamente verticales. Cada punto en el tiempo $t$ de la curva superior se empareja solo con el punto en el mismo tiempo $t$ de la curva inferior. Los picos y valles ligeramente desplazados horizontalmente producen conexiones verticales entre un pico de una curva y una pendiente o valle de la otra.

**Figura (gráfico derecho — emparejamiento Dynamic Time Warping):** Las mismas dos curvas (roja arriba, azul abajo) conectadas por líneas grises inclinadas no verticales. Los puntos se emparejan según similitud de forma en lugar de posición temporal exacta; por ejemplo, el primer pico de la curva roja se conecta con el primer pico de la curva azul aunque ocurran en posiciones horizontales distintas.

- Dynamic Time Warping distance

Warping path w

$$DTW(Q, C) = \min \left\{ \frac{\sqrt{\sum_{k=1}^{K} w_k}}{K} \right\}$$

This recursive function gives us the minimum cost path

$$M(i,j) = d(q_i, c_j) + \min\{ M(i-1,j-1), M(i-1,j), M(i,j-1) \}$$

**Figura:** Diagrama que ilustra el cálculo de DTW entre dos secuencias etiquetadas $Q$ (eje vertical, longitud $m$) y $C$ (eje horizontal, longitud $n$). Junto a cada eje se dibuja una línea ondulada que representa la serie temporal. Una matriz de puntos azules representa los puntos de alineación potenciales entre índices de $Q$ y $C$. Un camino de warping $w$ (flecha azul apuntando a segmentos negros conectados con puntas de flecha) va desde la esquina inferior izquierda $(1,1)$ hasta la esquina superior derecha $(n,m)$, marcados ambos como «End point». Un recuadro discontinuo rojo rodea el camino de warping con anotaciones «Local path», «Global path» y «Monotone-increasing».

- Dynamic Time Warping distance

$$O(N \times D^2)$$

```
Algorithm Sequential_Scan(Q)
1.   best_so_far = infinity;
2.   for all sequences in database
3.        true_dist = DTW(Ci, Q);
4.        if true_dist < best_so_far
5.            best_so_far = true_dist;
6.            index_of_best_match = i;
7.        endif
8.   endfor
```

| Secuencia $C_i$ | DTW(Q, Ci) |
|---|---|
| (forma de onda azul) | 14.1 |
| (forma de onda verde, similar a Q) | **1.7** |
| (forma de onda roja) | 12.2 |
| (forma de onda celeste) | 17.9 |
| (forma de onda azul) | 9.5 |
| (forma de onda azul) | 14.2 |
| (forma de onda roja) | 11.2 |

**Figura:** Slide con complejidad $O(N \times D^2)$ en rojo. A la izquierda, caja con el pseudocódigo `Sequential_Scan(Q)`; el término `DTW` en la línea 3 aparece resaltado en azul. A la derecha, la consulta $Q$ representada como una forma de onda verde dentada; debajo, una columna de siete formas de onda de distintos colores (azul, verde, rojo, celeste) que representan secuencias $C_i$ de la base de datos. Junto a cada secuencia, una tabla con los valores de distancia DTW calculados respecto a $Q$; el valor **1.7** aparece en negrita, indicando la coincidencia más cercana (la forma de onda verde visualmente similar a $Q$).

- Lower bounding for the Dynamic Time Warping [KR05]

The lower bound function is very fast…

The true DTW function is very slow…

$$LB\_Keogh(Q,C) \leq DTW(Q,C)$$

LB_Keogh Envelope-Based Lower Bound

$$LB\_Keogh(Q, C) = \sum_{i=1}^{n} \begin{cases} (c_i - U_i)^2 & \text{si } c_i > U_i \\ (c_i - L_i)^2 & \text{si } c_i < L_i \\ 0 & \text{en otro caso} \end{cases}$$

https://www.cs.ucr.edu/~eamonn/KAIS_2004_warping.pdf

**Figura:** En una caja naranja clara, la desigualdad $LB\_Keogh(Q,C) \leq DTW(Q,C)$; una flecha naranja apunta a $LB\_Keogh(Q,C)$ con la nota «The lower bound function is very fast…»; una flecha azul apunta a $DTW(Q,C)$ con la nota «The true DTW function is very slow…». En una caja verde clara, la fórmula de $LB\_Keogh$ como suma por tramos. Gráfico: curva azul etiquetada $Q$ y curva roja etiquetada $C$; alrededor de $Q$, dos líneas grises de frontera etiquetadas $U$ (superior) y $L$ (inferior) que forman el «envelope». Donde $C$ supera $U$ o queda por debajo de $L$, se muestran áreas sombreadas verticales entre $C$ y el límite correspondiente; cuando $C$ está dentro del envelope, la contribución es cero.

- Lower bounding for the Dynamic Time Warping

```
Algorithm Lower_Bounding_Sequential_Scan(Q)
1. best_so_far = infinity;
2. for all sequences in database
3.   LB_dist = LB_Keogh(Ci, Q);
4.     if LB_dist < best_so_far
5.        true_dist = DTW(Ci, Q);
6.        if true_dist < best_so_far
7.            best_so_far = true_dist;
8.            index_of_best_match = i;
9.        endif
10.   endif
11. endfor
```

| Secuencia $C_i$ | LB | DTW(Q, Ci) |
|---|---|---|
| (forma de onda azul) | 9.2 | 14.1 |
| (forma de onda verde, similar a Q) | 1.3 | **1.7** |
| (forma de onda roja) | 5.2 | -- |
| (forma de onda roja) | 2.5 | -- |
| (forma de onda azul) | 1.6 | 9.5 |
| (forma de onda azul) | 3.5 | -- |
| (forma de onda roja) | 5.8 | -- |

**Figura:** A la izquierda, caja con el pseudocódigo `Lower_Bounding_Sequential_Scan(Q)`; `LB_Keogh` resaltado en rojo en la línea 3 y `DTW` resaltado en azul en la línea 5. A la derecha, la consulta $Q$ como forma de onda verde; debajo, tabla con siete candidatos $C_i$ (pequeños gráficos de formas de onda en distintos colores) y sus valores de LB y DTW. El valor DTW **1.7** en negrita corresponde al mejor match. Las filas con «--» en la columna DTW (LB = 5.2, 2.5, 3.5, 5.8) indican que se omitió el cálculo costoso de DTW porque su cota inferior ya supera el `best_so_far` actual (1.7).

(slides 12–18)

## Índices Multidimensionales

**Figura (diagrama izquierdo — particionamiento espacial):** Espacio 2D delimitado por línea discontinua que contiene varios polígonos grises agrupados en tres rectángulos de delimitación mínima (MBR) etiquetados **A**, **B** y **C**. Rectángulo **A** (lado izquierdo): contiene polígonos etiquetados **1**, **4** (polígono central grande), **5** y **7**. Rectángulo **B** (parte superior derecha): contiene polígonos **2**, **11**, **10** y **3**; se solapa con A en el polígono **7**. Rectángulo **C** (parte inferior): contiene polígonos **9**, **6** y **8**; se solapa con B alrededor de **3** y **9**. Los contornos de las etiquetas de objetos usan codificación por color: azul para objetos en A, rojo para B, verde para C.

**Figura (diagrama derecho — estructura de árbol):** Representación jerárquica tipo R-tree. Nodo raíz con entradas **A**, **B**, **C** y un espacio vacío. Flecha desde A apunta a nodo hoja con punteros a polígonos **1**, **7**, **5**, **4** (contornos azules). Flecha desde B apunta a nodo hoja con punteros a **2**, **11**, **10**, **3** (contornos rojos). Flecha desde C apunta a nodo hoja con punteros a **9**, **6**, **8** y un espacio vacío (contornos verdes).

### Regiones espaciales e índices dinámicos

- Región espacial
  - Garantizan que puntos cercanos se almacenen en lo posible en la misma página de datos o subárbol.
  - Regiones de páginas jerárquicamente organizadas siempre deben estar contenidas completamente en la región de su padre.
- Índices multidimensionales son dinámicos
  - Operaciones de inserción y borrado eficientes $O(\log n)$

**Figura:** Texto en viñetas jerárquicas sobre regiones espaciales e índices dinámicos.

(slides 19–20)

### Índices Multidimensionales con soporte KNN

- R*-Tree:
  - Variante optimizada del R-Tree.
  - Mejora el rendimiento mediante técnicas como la minimización del solapamiento de nodos.
  - Soporta vectores característicos de baja dimensión.
- KD-Tree
  - Árbol binario para particionar el espacio en k dimensiones.
  - Bueno para datos de baja a moderada dimensionalidad.
- Ball Tree
  - Divide el espacio en hiperesferas (ball nodes).
  - Mejor que KD-Tree en alta dimensionalidad.

**Figura (KD-Tree — partición del espacio):** Gráfico cartesiano 2D con ejes etiquetados «x» (horizontal) e «y» (vertical). El espacio cuadrado está dividido por líneas de partición horizontales y verticales que forman regiones rectangulares. Nueve puntos rojos están distribuidos en el plano con coordenadas aproximadas: (1,10), (10,30), (25,40), (35,90), (50,50), (51,75), (55,1), (60,80) y (70,70). Cada punto tiene su etiqueta de coordenadas junto a él.

**Figura (KD-Tree — árbol binario):** Árbol binario con nodos etiquetados con coordenadas (x,y). La raíz es (51,75). El hijo izquierdo de la raíz es (25,40); el hijo derecho es (70,70). Desde (25,40), el hijo izquierdo es (1,10) y el hijo derecho es (35,90). Desde (70,70), el hijo izquierdo es (50,50) y el hijo derecho es (60,80). Desde (35,90), el hijo izquierdo es (10,30) y el hijo derecho es (55,1). Sobre el árbol aparece el texto en rojo «¿K-NN?».

**Figura (Ball Tree — 1a. A dataset):** Cuadrado con borde negro que contiene múltiples puntos negros dispersos aleatoriamente en el interior.

**Figura (Ball Tree — 1b. Root node):** Los mismos puntos negros del dataset, todos contenidos dentro de un único círculo grande (la hiperesfera raíz).

**Figura (Ball Tree — 1c. The 2 children):** El círculo raíz se divide en dos círculos hijos superpuestos parcialmente. El círculo izquierdo, etiquetado «C», contiene puntos verdes. El círculo derecho, etiquetado «B», contiene puntos rosados/magenta.

(slide 21)

## Maldición de Dimensionalidad

Los histogramas muestra la distribución de las distancias calculadas para N pares de puntos distribuidos aleatoriamente en un espacio vectorial unitario.

Se observa que a medida que crece el número de dimensiones, la mayor cantidad de distancias se concentran dentro de un rango muy pequeño.

**Figura (histogramas de distancias):** Seis histogramas dispuestos en una cuadrícula 2×3. En todos, el eje X está etiquetado «distances» y el eje Y «frequency in %».

| Dimensiones | Forma de la distribución | Rango de distancias (eje X) | Pico de frecuencia |
|---|---|---|---|
| 2 dims | Campana amplia y simétrica | 0 a ~1.4 | ~2% |
| 3 dims | Campana ligeramente más estrecha, desplazada a la derecha | 0 a ~1.7 | ~2.3% en distancia ~0.7 |
| 10 dims | Distribución notablemente más estrecha | 0 a ~3.16 | ~3.5% en distancia ~1.3 |
| 100 dims | Pico estrecho centrado alrededor de distancia 4 | 0 a 10 | >4% |
| 1000 dims | Pico muy estrecho centrado alrededor de distancia 13 | 0 a ~31.6 | >20% |
| 10000 dims | Línea casi vertical centrada alrededor de distancia 40 | 0 a 100 | ~50% |

k-nearest neighbors / Curse of Dimensionality (cornell.edu)

**Figura (gráfico izquierdo — distancias euclidianas):** Título: «10000 points from a normal distribution». Eje X: «Number of dimensions», escala logarítmica de $10^0$ (1) a $10^4$ (10 000). Eje Y: «Euclidean distance», escala logarítmica de $10^{-2}$ a $10^2$. Tres series con marcadores «x»:
- Línea azul: «Distance to nearest neighbor».
- Línea verde: «Distance to neighbor #10».
- Línea roja: «Distance to furthest neighbor».

En baja dimensionalidad (cerca de 1) hay una brecha amplia entre la distancia al vecino más cercano y la del más lejano. A medida que las dimensiones crecen hacia $10^3$, las tres líneas convergen. Una flecha negra apunta al área de convergencia en alta dimensionalidad con el texto: «Every point's neighborhood is the same!».

**Figura (gráfico derecho — ratio de páginas visitadas):** Título: «K=1». Eje X: «dimensions», escala lineal de 0 a 24. Eje Y: «ratio of visited pages», escala lineal de 0.00 a 1.00. Tres series:
- Triángulos amarillos («iDistance»): aumento rápido casi lineal, alcanzando ~0.90 a las 20 dimensiones.
- Cuadrados azul oscuro («R* Tree»): permanece en 0 hasta ~8 dimensiones, luego sube bruscamente hasta ~0.85 a las 24 dimensiones.
- Diamantes naranja («Hybrid Tree»): permanece plano en 0.00 en todo el rango de 0 a 24 dimensiones.

Kouiroukidis, Nikolaos and Georgios Evangelidis. "The Effects of Dimensionality Curse in High Dimensional kNN Search." 2011 15th Panhellenic Conference on Informatics (2011): 41-45.

(slides 22–23)

## Modelos de Recuperación Multimedia — Descriptores Locales

5.
Modelos de Recuperación Multimedia
Descriptores Locales

**Figura:** Slide dividida en dos zonas. en el centro un número grande «5.» con subrayado azul, un icono de portapapeles azul con viñetas y el título «Modelos de Recuperación Multimedia» en negrita; debajo, el subtítulo «Descriptores Locales» en azul claro y cursiva. Líneas decorativas azules y amarillas en los bordes.

### Descriptores Locales

**Figura:** Diagrama comparativo de estrategias de extracción de características («FEATURE EXTRACTION STRATEGIES»), con una imagen central etiquetada «ANY IMAGE» que muestra la fachada de un edificio de ladrillo rojo con ventanas arqueadas y hiedra verde.

**Lado izquierdo — Local Descriptors (en azul):** Cuatro lupas apuntan a regiones específicas de la imagen central (parches de ladrillo, esquina de ventana, hojas de hiedra). Cada lupa conduce a un círculo etiquetado «Local Pattern Vector» (Vector 1, Vector 2, etc.), conectados por flechas, indicando que una imagen se representa con múltiples vectores. Texto: «Extracts local patterns (e.g., SIFT, ORB, FREAK)».

**Lado derecho — Global Descriptor (en verde):** Una flecha verde apunta desde toda la imagen central hacia un único vector característico representado como una barra horizontal dividida en segmentos multicolores. Texto: «Extracts one characteristic vector (e.g., GIST, HOG, VGG-GAP)».

En la parte inferior, una llave grande agrupa ambos métodos bajo el rótulo «FEATURE EXTRACTION STRATEGIES».

(slide 25)

### Descriptores Locales: SIFT

Detección de descriptores locales invariantes a la escala y a la rotación.

Se generan una cantidad diferente de vectores característicos para cada imagen.

**Figura:** Diagrama central con dos imágenes en escala de grises de un camión de juguete y una columna central de parches SIFT.

- **Imagen A (izquierda):** Fotografía en escala de grises de un camión de juguete etiquetado «A». Cuadrados amarillos marcan puntos de interés (rueda, cabina, capó). Flechas rojas apuntan desde estos cuadrados hacia la columna central.
- **SIFT Features (centro):** Caja vertical con cuatro parches en escala de grises extraídos de las regiones de interés.
- **Imagen B (centro-derecha):** Fotografía en escala de grises del mismo camión en diferente ángulo/escenario, etiquetado «B». Cuadrados amarillos marcan los mismos puntos de interés. Flechas verdes apuntan hacia los mismos parches en la columna central.

Debajo de las imágenes:

$A = \{A_1, A_2, \ldots, A_n\}$

$A_i = [a_1, a_2, \ldots, a_D]$

$B = \{B_1, B_2, \ldots, B_m\}$

$B_i = [b_1, b_2, \ldots, b_D]$

$\delta(SIFT(A), SIFT(B))$ ? ?

- SIFT descriptor

**Figura (diagrama superior):** En la parte superior, la etiqueta «Colección» sobre una imagen de tres personas (personajes de *Seinfeld*) con elipses blancas superpuestas que resaltan puntos clave locales en rostros y ropa. Una flecha apunta hacia cuatro iconos de documento etiquetados img1, img2, img3, img4, cada uno representando los descriptores extraídos de cada imagen.

```python
import cv2

# Cargar imagen en escala de grises
image = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)
# Crear detector SIFT
sift = cv2.SIFT_create()
# Detectar keypoints y descriptores
keypoints, descriptors = sift.detectAndCompute(image, None)
# Mostrar cantidad de puntos clave y tamaño de descriptores
print(f"Número de keypoints detectados: {len(keypoints)}")
print(f"Forma del array de descriptores: {descriptors.shape}")     # (n_puntos, 128)
```

(slides 26–27)

### Descriptores Locales: Similitud

$\delta(SIFT(A), SIFT(B))$ ? ?

Para medir la similitud, se puede usar los descriptores locales de forma agregada o directamente

- Histograma de Cuantización (k-means) — Índice Multidimensionales para Descriptores Locales
- Arboles de Cuantización (Hierarchical K-Means) — Índices de Alta Dimensión para Búsqueda Aproximada
- Índice Invertido para Descriptores Locales — Búsqueda Lineal con Distancia Apropiada (DTW, ED, etc)

**Figura (diagrama inferior — forma agregada):** Flujo de creación de un descriptor de características final mediante histogramas concatenados.

1. **Imagen de entrada:** Retrato en escala de grises de un hombre, superpuesto con una cuadrícula de $4 \times 4$ (16 bloques).
2. **Extracción:** Flechas desde bloques específicos (por ejemplo, el bloque superior izquierdo y el inferior derecho) hacia cajas etiquetadas «Local Feature Extractor».
3. **Histogramas intermedios:** Cada extractor produce un histograma. El diagrama etiqueta específicamente el «1st block's Histogram» y el «Last block's Histogram».
4. **Concatenación:** Una flecha etiquetada «Histograms Concatenation» conduce desde los histogramas individuales hacia la representación final.
5. **Salida final:** Gráfico largo combinado etiquetado «Final Feature Descriptor», que representa la concatenación de todos los histogramas de bloques en un único vector grande.

(slide 28)

### Descriptores Locales: Condiciones

- Implica segmentar el problema en subespacios más pequeños.
- Los descriptores locales deben ser baja dimensión
- Se puede usar un solo índice para todos los descriptores locales, o también un índice diferente para cada descriptor local.
  - Depende la naturaleza del descriptor.
- El objeto de consulta también se le aplica extracción de descriptores locales y aplicar KNN a cada descriptor local,
- Luego se debe aplicar alguna técnica efectiva de combinación de resultados parciales para obtener el resultado final.
- El resultado no será exactamente igual a una búsqueda lineal, por eso está clasificado como método de búsqueda aproximada.

**Figura:** Viñetas jerárquicas. Los términos «baja dimensión», «Depende la naturaleza del descriptor.», «combinación de resultados parciales» y «método de búsqueda aproximada» aparecen en negrita.

(slide 29)

### Descriptores Locales: Ventajas

- Eficiencia Computacional: Son más rápidos de calcular y comparar, ya que se enfocan en regiones específicas de la imagen.
- Robustez a la Oclusión: Son útiles en escenarios donde partes de la imagen pueden estar ocultas o no estar presentes en todas las imágenes.
- Flexibilidad: Pueden adaptarse a diferentes tipos de características y pueden ser combinados para mejorar la precisión en la detección y descripción de puntos de interés.

**Figura:** Viñetas con encabezados en negrita (Eficiencia Computacional, Robustez a la Oclusión, Flexibilidad) seguidos de sus descripciones.

(slide 30)

### Descriptores Locales: Desventajas

- Alta Dimensionalidad: Los descriptores locales como SIFT generan vectores de alta dimensión, 128, lo cual sigue siendo un desafío en recursos computacionales.
- Sensibilidad al Ruido: Pueden ser sensibles al ruido en el objeto, esto puede llevar a descripciones inexactas o inconsistentes, afectando a la precisión.
- Escalabilidad: La extracción de descriptores locales puede ser costosa en términos de recursos computacionales, por lo que, escalar su uso a grandes volúmenes de datos puede ser un desafío.

Manejar y procesar grandes bases de datos de descriptores puede requerir técnicas de optimización, como los métodos de búsqueda aproximada.

**Figura:** Viñetas con encabezados en negrita (Alta Dimensionalidad, Sensibilidad al Ruido, Escalabilidad). En la parte inferior, caja resaltada con el texto sobre grandes bases de datos y métodos de búsqueda aproximada, con «grandes bases de datos» y «métodos de búsqueda aproximada» en negrita.

(slide 31)

## Índice Multidimensional con Descriptores Locales

### Indexación de Descriptores Locales: Un solo Índice

**Figura:** Diagrama de flujo de indexación con un solo índice para descriptores locales.

- **Objeto ($Obj_i$, izquierda):** Icono de imagen etiquetado $Obj_i$, representando un objeto individual de la colección.
- **Extracción de vectores (tabla central):** Flecha desde la imagen hacia una tabla vertical con descriptores $P1$, $P2$, $P3$, $P4$, $P5$, $P6$. Cada descriptor tiene una fila de tres cajas pequeñas que representan un vector característico.
- **Caja verde (izquierda):** «Se extrae los vectores característicos locales de cada objeto de la colección $Obj_i$».
- **Índice (triángulo central):** Flecha desde la tabla de descriptores hacia un triángulo grande etiquetado «INDEX».
- **Caja verde (derecha):** «Cada vector característico $P_j$ es insertado en el índice».
- **Inserción en base de datos:** Múltiples flechas descendentes desde el índice hacia un cilindro (base de datos). Junto a las flechas aparece la notación $(Obj_i, P_j)$.
- **Almacenamiento (cilindro inferior):** Contenedor cilíndrico con tarjetas rectangulares que representan entradas. Cuatro entradas resaltadas en amarillo: $(Obj_i, P1)$, $(Obj_i, P3)$, $(Obj_i, P6)$, $(Obj_i, P9)$. Esto muestra que para un solo objeto $i$ se crean múltiples entradas en el índice, una por cada descriptor local.

Barra horizontal azul en la parte inferior.

**Figura:** Diagrama de distribución de vectores característicos en MBRs (Minimum Bounding Regions).

- **$Obj_1$ (rojo, izquierda):** Cuatro flechas rojas desde la etiqueta hacia puntos rojos (vectores característicos) ubicados en diferentes regiones rectangulares.
- **$Obj_2$ (morado, derecha):** Cuatro flechas moradas hacia puntos morados en diferentes regiones.

**Regiones espaciales (MBRs):** Varios rectángulos con borde azul etiquetados $R1$ a $R9$, agrupados dentro de dos cajas grandes con borde naranja que sugieren una estructura jerárquica tipo árbol R. Dentro de cada MBR hay puntos negros pequeños (otros vectores de la base de datos).

**Distribución de vectores de $Obj_1$:**
- Un vector en $R1$.
- Un vector en una región pequeña sin etiqueta entre $R1$ y $R3$.
- Un vector en $R3$.
- Un vector en $R9$ (extremo derecho).

**Distribución de vectores de $Obj_2$:**
- Un vector en $R1$.
- Un vector en $R7$.
- Un vector en $R8$.
- Un vector en $R5$.

Caja verde inferior: «Los vectores característicos $P_j$ de cada objeto de la colección quedan ubicados en diferentes MBRs.»

(slides 33–34)

### Indexación de Descriptores Locales: Búsqueda

**Figura:** Diagrama de flujo de búsqueda con descriptores locales.

**Entrada de consulta (izquierda):**
- Tabla etiquetada «query» con seis filas (Q1 a Q6). Cada fila tiene tres cajas pequeñas que representan vectores característicos locales extraídos del objeto de consulta.
- Caja verde: «Se extrae los vectores característicos locales».
- Flecha hacia el centro.

**Filtrado e indexación (centro):**
- Triángulo etiquetado «Filter» con la palabra «INDEX» en su base.
- Cilindro debajo (base de datos) con rectángulos que representan objetos almacenados. Cuatro flechas desde el «INDEX» hacia la base de datos.

**Resultados parciales y agregación (derecha):**
- Tabla de resultados «3NN-search» con los 3 vecinos más cercanos para cada vector de consulta:

| Consulta | 1er vecino | 2do vecino | 3er vecino |
|---|---|---|---|
| Q1 | obj4 | obj2 | obj6 |
| Q2 | obj1 | obj4 | obj2 |
| Q3 | obj4 | obj8 | obj2 |
| Q4 | obj2 | obj4 | obj6 |
| Q5 | obj4 | obj3 | obj2 |
| Q6 | obj1 | obj8 | obj4 |

- Caja roja inferior: «Aplicar una estrategia para combinar todos los resultados parciales y obtener los k vecinos cercanos finales».

(slide 35)

## Cuantización de Descriptores Locales

### Bag of Visual Words: Construcción

**Figura (a) — Diagrama algorítmico (lado izquierdo):** Flujo conceptual del proceso Bag of Visual Words con tres imágenes de ejemplo:

1. **Imágenes de entrada (arriba):** Tres imágenes: un retrato (similar a la Mona Lisa), una bicicleta amarilla y un violín.
2. **Extracción de parches:** Flechas descendentes desde cada imagen hacia un conjunto de parches rectangulares pequeños recortados de esa imagen (por ejemplo, ojos y nariz del retrato; partes de ruedas y cuadro de la bicicleta).
3. **Formación del vocabulario visual (codebook):** Todos los parches de las tres imágenes se agrupan en una caja horizontal grande central que representa la colección de todas las características visuales extraídas.
4. **Generación de histogramas:** Flechas descendentes desde el pool central hacia tres histogramas individuales, cada uno correspondiente a una de las tres imágenes originales. El eje X de cada histograma muestra «palabras visuales» (parches) del pool; el eje Y representa la frecuencia (conteo) de esas palabras visuales en cada imagen. Por ejemplo, el histograma del violín tiene barras altas para parches de violín y cero para parches de bicicleta.

**Figura (b) — Diagrama de flujo (lado derecho):**

1. **Targets:** Tres cajas «Target 1», «Target 2», «Target 3» (imágenes de entrada).
2. **Extracción de características:** Cada target pasa por «SIFT feature extraction».
3. **Clustering:** Todas las características SIFT extraídas se alimentan a un único bloque «Clustering algorithm».
4. **Salida:** Generación de un «Histogram feature vector» para cada imagen.

Bag of Visual Words in a Nutshell | by Bethea Davida | TDS Archive | Medium

(slide 37)

### Bag of Visual Words: Clustering

- Clustering Algorithm

**Figura:** Diagrama de flujo de izquierda a derecha para la creación del vocabulario visual mediante K-means.

1. **Vectores de imágenes de entrada:** Cuatro columnas etiquetadas img1, img2, img3, img4. Cada columna contiene varias líneas horizontales que representan descriptores de características extraídos de esas imágenes.
2. **Proceso de clustering:** Flecha hacia una caja central titulada «Image features and K-means clustering». Círculos rodean grupos de formas similares, indicando cómo K-means particiona el espacio de características en clusters.
3. **Palabras visuales (codebook):** Flecha hacia la sección final «Visual words» con cinco palabras etiquetadas $w_1$ a $w_5$.
   - $w_1$: triángulo verde
   - $w_2$: polígono azul
   - $w_3$: diamante negro
   - $w_4$: círculo morado
   - $w_5$: estrella roja

Visualizing K-Means Clustering

(slide 38)

### Bag of Visual Words: Consulta

**Figura:** Diagrama de consulta Bag of Visual Words organizado en una cuadrícula con tres filas y dos columnas funcionales (base de datos vs. consulta).

**Fila 1 — «group image samples» / «image to compare»:**
- **Base de datos (izquierda):** Tres imágenes de muestra agrupadas: un retrato (La dama del armiño de Leonardo da Vinci), una bicicleta amarilla y un violín.
- **Consulta (derecha):** Una imagen de un violín, etiquetada como «image to compare».

**Fila 2 — «group histograms»:**
- **Histogramas de la base de datos:**
  - Bajo el retrato: histograma verde etiquetado «23%».
  - Bajo la bicicleta: histograma amarillo etiquetado «12%».
  - Bajo el violín: histograma rojo etiquetado «79%».
- **Histograma de consulta:** Bajo la imagen del violín de consulta, histograma naranja.
- El eje X de los histogramas corresponde a «palabras visuales» mostradas en la fila 3.

**Fila 3 — «vocabulary» / «result»:**
- **Vocabulario (izquierda):** Colección de parches de imagen pequeños (fragmento de ojo, nariz, sección de rueda de bicicleta, partes del cuerpo del violín) que representan las «palabras visuales» usadas para construir los histogramas.
- **Resultado (derecha):** Flecha roja descendente desde el histograma naranja de la consulta hacia la palabra «violin», etiquetada como «result».

**Figura (lado izquierdo — representación de histogramas y vectores de características):**

- **Vector $\vec{p}$:** Representa una imagen de retrato de mujer. Vector de características $[1\ 8\ 1\ 4]$ y histograma de barras verdes correspondiente. El eje horizontal del histograma muestra iconos de palabras visuales: rueda de bicicleta, parche de piel, parche oscuro/rojo y parche de ojo.
- **Vector $\vec{q}$:** Representa una imagen de bicicleta. Vector de características $[5\ 1\ 1\ 0]$ y histograma amarillo/rojo correspondiente. El eje horizontal usa los mismos iconos de palabras visuales que $\vec{p}$.

**Fórmula de similitud (parte superior derecha):**

$$\text{Similarity}(p,q) = \cos \theta = \frac{p \cdot q}{\|p\| \|q\|} = \frac{\sum_{i=1}^{n} p_i q_i}{\sqrt{\sum_{i=1}^{n} p_i^2} \sqrt{\sum_{i=1}^{n} q_i^2}}$$

**Aplicar TF-IDF (parte inferior derecha, en rojo):**

$$p_i = \frac{tf_{i,p}}{|p|} \log \frac{N}{df_i}$$

$$\log(1 + tf_{i,p})$$

lecture16_bow.ppt

(slides 39–40)

## Índice Invertido con Descriptores Locales

### Inverted Index (IVF): Construcción

**Figura:** Diagrama que ilustra la construcción de un Índice Invertido a partir de imágenes de una base de datos y sus descriptores locales (palabras visuales). La slide se divide en dos secciones principales:

**Sección izquierda — Imágenes de la base de datos:**
- **Image #1:** Fotografía del Golden Gate Bridge. Descriptores locales identificados con círculos y etiquetas: $W_{16}$, $W_{23}$, $W_{7}$.
- **Image #2:** Otra vista del Golden Gate Bridge. Descriptores identificados: $W_{62}$, $W_{7}$, $W_{91}$. El descriptor $W_{7}$ es común a Image #1 e Image #2.
- **Image #3:** Fotografía de la Ópera de Sídney. Descriptores identificados: $W_{1}$, $W_{76}$, $W_{8}$.

**Sección derecha — Tabla del Índice Invertido:**
Tabla con dos columnas: **Word #** e **Image #**.

| Word # | Image # |
|--------|---------|
| 1 | 3 |
| 2 | |
| ... | ... |
| 7 | 1, 2 |
| 8 | 3 |
| 9 | |
| 10 | |
| ... | ... |
| 91 | 2 |

La tabla demuestra el mapeo inverso: cada palabra visual (Word) apunta a las imágenes que la contienen. Por ejemplo, Word 7 aparece en las imágenes 1 y 2.

Pie de página: lecture16 (utexas.edu).

1. **Muestreo:** Se recopila todos los descriptores locales (e.g., SIFT) de un gran conjunto de imágenes de entrenamiento (base de datos).
2. **Clustering (K-Means):** Se aplica un algoritmo de clustering (e.g. K-Means) a este conjunto de descriptores. Los centroides obtenidos conforman el Vocabulario Visual.
3. **Asignación de Descriptores:** Para cada imagen de la base de datos, se toma cada descriptor local individualmente y se le asigna a la Palabra Visual (centroide) más cercano. Esta es la cuantización.
4. **Indexación:** El Índice Invertido se construye utilizando los IDs de las Palabras Visuales como claves.
    - **Posting Lists:** Para cada clave (Palabra Visual), se almacena una lista de todas las Imágenes que contienen descriptores cuantizados a ese centroide.

(slides 42–43)

### Inverted Index: Búsqueda

**Figura:** Diagrama que ilustra el proceso de búsqueda mediante un Índice Invertido. Título de la slide: **Inverted Index: Búsqueda**.

**Imagen de consulta (izquierda):**
- Fotografía del Golden Gate Bridge etiquetada como imagen de consulta nueva.
- Dos regiones locales están circuladas y etiquetadas:
  - $W_7$: ubicado en la parte superior de una torre del puente.
  - $W_{91}$: ubicado cerca de la base de la torre del puente.

**Tabla del Índice Invertido (derecha):**
Tabla con columnas **Word #** e **Image #**.

| Word # | Image # |
|--------|---------|
| 1 | |
| 2 | |
| ... | ... |
| 7 | 1, 2 |
| 8 | 3 |
| 9 | |
| 10 | |
| ... | ... |
| 91 | 2 |

**Flechas y resaltados:**
- Flecha roja conecta el descriptor $W_7$ en la imagen de consulta con la fila Word 7 de la tabla (resaltada con recuadro punteado rojo).
- Flecha naranja conecta el descriptor $W_{91}$ en la imagen de consulta con la fila Word 91 de la tabla (resaltada con recuadro punteado naranja).

Pie de página: lecture16 (utexas.edu).

1. **Consulta:** Se genera los descriptores locales y se cuantizan de la misma manera. Esto genera una lista de Palabras Visuales que contiene la imagen de consulta.
2. **Filtrado:** Se utiliza el Índice Invertido para recuperar solo las imágenes que comparten al menos una de estas Palabras Visuales.
3. **Similitud de Coseno:**
    - Para las imágenes recuperadas, se construye o se recupera su Histograma BoVW ponderado (TF-IDF).
    - Se aplica la Similitud de Coseno entre el Histograma BoVW de la consulta y los Histograma BoVW de las imágenes candidatas para determinar el ranking de similitud.

(slides 44–45)

## Segmentación de audio con ventanas deslizantes

**Figura:** Diagrama de flujo que ilustra la segmentación de una señal de audio con ventanas deslizantes para generar vectores locales.

**Capa superior — Señal de entrada:**
- Onda continua de color púrpura oscuro etiquetada **Sampled Audio Signal $s(n)$**.
- La forma de onda está superpuesta con una cuadrícula de líneas verticales que representan los pasos temporales o límites de ventana.
- Varias flechas apuntan hacia abajo indicando la selección de segmentos temporales.

**Capa media — Segmentación:**
- Tres instantáneas de la forma de onda etiquetadas **Segments of $s(n)$**: $s'_1$, $s'_2$, $s'_k$ (secuencia de 1 a $k$).
- Cada segmento representa una ventana de la señal de audio original.

**Capa de procesamiento — Extracción de características:**
- Cada segmento ($s'_1$, $s'_2$, $s'_k$) apunta a un recuadro etiquetado **Feature Extraction**.

**Capa inferior — Vectores de salida:**
- La salida de cada recuadro **Feature Extraction** es un vector: $\vec{x}^{(1)}$, $\vec{x}^{(2)}$, $\vec{x}^{(k)}$.
- Cada vector se visualiza como un arreglo horizontal de celdas con valores $x_1, x_2, \dots, x_d$, donde $d$ es la dimensionalidad del vector.

**Texto en rojo (derecha):** Se generan vectores locales más pequeños.

**Cita al pie:** At the Border of Acoustics and Linguistics: Bag-of-Audio-Words for the Recognition of Emotions in Speech

(slide 46)

## Recuperación Eficiente

### Recuperación Eficiente en Texto

**Figura:** Infografía titulada **Recuperación Eficiente en Texto** que describe el proceso completo de indexación y recuperación de documentos de texto. Dividida en dos secciones horizontales: **1) INDEXACIÓN (Offline)** y **2) RECUPERACIÓN (Online)**.

#### 1) INDEXACIÓN (Offline)

1. **Colección de documentos:** Conjunto de documentos de texto como punto de partida.
2. **Procesar texto por chunks:** Los documentos se dividen en fragmentos manejables llamados chunks (Chunk 1, Chunk 2, ..., Chunk N).
3. **Representación vectorial (TF-IDF / Bag of Words):** Cada chunk se convierte en un vector numérico basado en TF-IDF o Bag of Words. Se muestra una matriz donde las filas son chunks y las columnas contienen pesos (e.g., 0.12, 0, 0.35).
4. **Indexación (SPIMI - Memoria secundaria):** Usa Single-Pass In-Memory Indexing.
    - **Bloques (en memoria):** Los chunks se procesan en bloques en memoria.
    - **Índice parcial (en memoria):** Se crea un mapeo de «palabra» a una «lista de (documento/chunk, tf)».
    - **Escritura a disco:** Los índices parciales se escriben a disco como segmentos.
    - **Mezcla de segmentos:** Los segmentos se fusionan para formar el índice final.
5. **Índice invertido final (en disco):** Tabla persistente con estructura:

| Palabra | Lista de (documento/chunk, tf) |
|---------|-------------------------------|
| texto | (doc3/ch5, 2), (doc7/ch1, 1), ... |

Nota: IDF global almacenado por término.

#### 2) RECUPERACIÓN (Online)

1. **Consulta del usuario (query):** El usuario envía una pregunta en lenguaje natural. Ejemplo: «¿Qué es un filtro basado en el contenido?».
2. **Procesar la query:** La consulta se convierte en representación vectorial.
    - **Short Query:** Se crea un único vector (Q1).
    - **Long Query:** Se crean múltiples vectores (Q1, Q2, ..., Qk) dividiendo la consulta en chunks.
3. **Búsqueda en índice invertido (Recuperación de candidatos):** Para cada término de la consulta, el sistema:
    - Busca en el índice invertido.
    - Recupera la lista de documentos/chunks y su TF.
    - Calcula el peso TF-IDF del documento/chunk.
4. **Cálculo de similitud de coseno:**
    - Calcula similitud entre el vector de consulta ($q$) y el vector del documento/chunk candidato ($d$).
    - Fórmula: $$sim(q, d) = \frac{q \cdot d}{\|q\| \|d\|}$$
    - Componentes:
        - Producto punto: $q \cdot d = \sum_{i=1}^{|V|} q_i d_i$
        - Normas: $\|q\| = \sqrt{\sum_{i=1}^{|V|} q_i^2}$ y $\|d\| = \sqrt{\sum_{i=1}^{|V|} d_i^2}$
5. **Ranking y combinación:**
    - Los candidatos se ordenan por similitud descendente.
    - **Tabla de ranking de ejemplo:**

| Rank | Documento/Chunk | Similitud |
|------|-----------------|-----------|
| 1 | (doc3 / ch1) | 0.892 |
| 2 | (doc1 / ch2) | 0.763 |
| 3 | (doc5 / ch3) | 0.641 |
| ... | ... | ... |

    - **Para Long Queries:** Los scores de diferentes chunks de consulta se combinan (e.g., Average o Max).
    - Fórmula de score combinado: $$score(d) = \frac{1}{k} \sum_{i=1}^{k} sim(Q_i, d)$$
    - Los documentos se reordenan por este score final.

#### Notas/Definiciones al pie:
- **TF:** Frecuencia del término en el chunk/documento.
- **IDF:** $\log\left(\frac{N}{df_t}\right)$, donde $N$ es el número total de documentos y $df_t$ es el número de documentos/chunks que contienen el término $t$.
- **SPIMI:** Single-Pass In-Memory Indexing.
- **Ventaja de Similitud de Coseno:** Normaliza por la longitud del vector, permitiendo comparar consultas y documentos de diferentes tamaños.

(slide 47)

### Recuperación Eficiente en Imágenes

**Figura:** Infografía titulada **Recuperación Eficiente en Imágenes** que detalla el proceso de indexación y búsqueda de imágenes usando Bag of Visual Words. Dividida en dos secciones: **1) INDEXACIÓN (Offline)** y **2) BÚSQUEDA (Online)**.

#### 1) INDEXACIÓN (Offline)

1. **Colección de imágenes:** Tres imágenes de ejemplo: paisaje de montaña, catedral y playa.
2. **Extracción de descriptores locales (SIFT):** Las imágenes se analizan con el algoritmo **SIFT** (Scale Invariant Feature Transform). Círculos naranjas pequeños marcan puntos de interés. Se convierten en vectores verticales etiquetados «Descriptores SIFT».
3. **Aprendizaje de codewords (K-Means):**
    - Texto: «Agrupar todos los descriptores SIFT de la colección».
    - Diagrama de Voronoi con clusters de puntos de colores (azul, rojo, verde, naranja, amarillo).
    - **K centroides = Codewords (Palabras visuales):** Los centros de los clusters son las «palabras visuales».
4. **Representación de cada imagen (Histograma de cuantización):**
    - Cada imagen se transforma en un **Histograma de frecuencias de codewords** (gráfico de barras), que es un «Vector de dimensión K». Cada barra representa la frecuencia de un codeword específico en esa imagen.
5. **Indexación (Índice invertido):**
    - Texto: «Para cada codeword (centroide) se almacenan las imágenes que lo contienen y su frecuencia (tf) en el histograma».
    - Tabla **Índice invertido sobre codewords:**

| Codeword (color) | Lista (imagen, tf) |
|------------------|------------------|
| Azul | (img_2, 3), (img_5, 1), (img_9, 4), ... |
| Rojo | (img_1, 2), (img_2, 5), (img_7, 1), ... |
| Verde | (img_1, 4), (img_3, 2), (img_8, 3), ... |
| Naranja | (img_2, 1), (img_4, 2), (img_9, 3), ... |
| Amarillo | (img_3, 1), (img_6, 2), (img_10, 1), ... |

- **Resultado de indexación:** «cada imagen representada por un histograma de codewords y almacenada en un índice invertido».

#### 2) BÚSQUEDA (Online)

1. **Imagen de consulta:** El usuario proporciona una imagen (paisaje de montaña).
2. **Extracción de descriptores (SIFT):** Se extraen descriptores SIFT de la imagen de consulta.
3. **Cuantización y representación:**
    - Texto: «Asignar cada descriptor al codeword (centroide) más cercano».
    - Los descriptores se convierten en un histograma (vector de consulta $q$) de dimensión K.
4. **Búsqueda en el índice invertido (Recuperación de candidatos):**
    - Para cada codeword en la consulta con frecuencia > 0, se busca en el índice invertido y se recuperan todas las imágenes que contienen ese codeword.
    - **Conjunto de candidatos:** La unión de todas las imágenes recuperadas.
5. **Cálculo de similitud (Similitud de coseno):**
    - $q$ = vector de consulta (histograma)
    - $d$ = vector de imagen candidata (histograma)
    - Fórmula: $$sim(q, d) = \frac{q \cdot d}{\|q\| \|d\|}$$
    - Detalles matemáticos:
        - $q \cdot d = \sum_{i=1}^{K} q_i d_i$
        - $\|q\| = \sqrt{\sum_{i=1}^{K} q_i^2}$, $\|d\| = \sqrt{\sum_{i=1}^{K} d_i^2}$
6. **Ranking y resultados:**
    - Las imágenes se ordenan por similitud descendente.
    - **Tabla de ranking:**

| Rank | Imagen | Similitud |
|------|--------|-----------|
| 1 | img_2 | 0.892 |
| 2 | img_5 | 0.763 |
| 3 | img_1 | 0.641 |
| 4 | img_3 | 0.487 |
| 5 | img_7 | 0.352 |

    - Miniaturas de resultados mostradas debajo de la tabla.

#### Glosario al pie:
- **SIFT:** Scale Invariant Feature Transform (descriptores locales invariantes a escala y rotación).
- **K-Means:** Algoritmo de clustering para obtener K centroides (codewords).
- **Codeword:** Palabra visual (centroide).
- **Histograma (vector de codewords):** Distribución de frecuencias de codewords en una imagen (dimensión K).
- **Índice invertido:** Asocia cada codeword con las imágenes que lo contienen y su frecuencia (tf).

(slide 48)

### Recuperación Eficiente en Audio

**Figura:** Infografía titulada **Recuperación Eficiente en Audio** que ilustra un proceso de dos partes para indexar y buscar archivos de audio basándose en su contenido: fase de **INDEXACIÓN (Offline)** y fase de **BÚSQUEDA (Online)**.

#### 1) INDEXACIÓN (Offline)

1. **Colección de audios (Colección):** Conjunto de formas de onda de audio que representan la colección de entrada.
2. **Extracción de características (Sliding Window + MFCC):** Cada archivo de audio se procesa usando una «Sliding Window» (ventana temporal) para extraer vectores MFCC (Mel Frequency Cepstral Coefficients) de cada segmento.
3. **Aprendizaje de codewords (K-Means):** Los vectores extraídos de toda la colección se usan para aprender $K$ centroides con el algoritmo K-Means. Estos centroides se denominan **Codewords** (palabras de audio). Un diagrama de Voronoi ilustra cómo el espacio de características se particiona en $K$ regiones, cada una representada por un codeword (punto de color).
4. **Representación de cada audio (Histograma de frecuencias):** Cada archivo de audio se convierte en un **Histograma de Frecuencias de Codewords**. Los vectores MFCC de un audio se mapean a su codeword aprendido más cercano, y se cuentan sus ocurrencias. Esto produce un vector de dimensión $K$ para cada audio.
5. **Indexación (Índice invertido):** El sistema construye un **Índice Invertido**. Para cada codeword (centroide), almacena una lista de IDs de audio y su frecuencia ($tf$) dentro del histograma de ese audio. Tabla de ejemplo con puntos de colores (codewords) mapeados a listas como `(audio_12, 3), (audio_45, 1)`.

**Resumen de indexación:** Cada audio se representa por un histograma de codewords y se almacena en un índice invertido.

#### 2) BÚSQUEDA (Online)

1. **Audio de consulta (Query):** El usuario proporciona una forma de onda de audio de entrada.
2. **Extracción de características (Sliding Window + MFCC):** Idéntico al paso 2 de indexación; el audio de consulta se transforma en vectores MFCC usando ventanas deslizantes.
3. **Cuantización (Asignación a codewords):** Cada vector MFCC de la consulta se asigna a su codeword aprendido más cercano (centroide). Esto genera un histograma de codewords para la consulta (vector de dimensión $K$).
4. **Búsqueda en el índice invertido (Recuperación de candidatos):** Para cada codeword presente en la consulta (frecuencia > 0), el sistema consulta el índice invertido para recuperar todos los audios que contienen ese codeword. El resultado es un **Conjunto de candidatos**, que es la unión de todos los audios que comparten al menos un codeword con la consulta.
5. **Cálculo de similitud (Similitud de coseno):** El sistema calcula la similitud entre el vector de consulta ($q$) y cada vector de audio candidato ($d$) usando la fórmula de **Similitud de Coseno**:
    $$sim(q, d) = \frac{q \cdot d}{\|q\| \|d\|}$$
    Donde:
    - $q \cdot d = \sum_{i=1}^{K} q_i d_i$ (Producto punto)
    - $\|q\| = \sqrt{\sum_{i=1}^{K} q_i^2}$ y $\|d\| = \sqrt{\sum_{i=1}^{K} d_i^2}$ (Normas)
6. **Ranking y resultados (Orden descendente):** Los candidatos se ordenan por similitud descendente. Tabla de ejemplo:

| Rank | Audio | Similitud |
|------|-------|-----------|
| 1 | audio_12 | 0.912 |
| 2 | audio_45 | 0.784 |
| 3 | audio_7 | 0.653 |
| 4 | audio_18 | 0.512 |
| 5 | audio_3 | 0.401 |

#### Terminología/Glosario al pie:
- **Sliding Window:** ventana temporal.
- **MFCC:** Mel Frequency Cepstral Coefficients.
- **Codeword:** palabra de audio (centroide).
- **K-Means:** algoritmo de clustering usado para obtener K centroides.
- **Histograma de codewords:** distribución de frecuencias de codewords en un audio (dimensión K).
- **Índice invertido:** asocia cada codeword con los audios que lo contienen y su frecuencia ($tf$) en el histograma.

(slide 49)

## Búsqueda Aproximada

### ANN - Approximate Nearest Neighbors

**Figura:** Diagrama de flujo que ilustra dos métodos para realizar una búsqueda en una base de datos, etiquetado como **Búsqueda Exacta**.

**Colección (izquierda):** Óvalo grande que contiene un conjunto de puntos de datos. La mayoría son círculos azules pequeños, pero cuatro formas distintas están resaltadas: una **estrella**, un **cuadrado**, un **triángulo** y un **pentágono**.

**Métodos de búsqueda — dos caminos con flechas desde la colección:**

- **Camino superior:** Flecha apunta a un recuadro azul etiquetado **3NN Lineal** (búsqueda lineal de los 3 vecinos más cercanos).
- **Camino inferior:** Flecha apunta a un triángulo azul etiquetado **3NN RTree** (búsqueda usando estructura de índice R-Tree para encontrar los 3 vecinos más cercanos).

**Conjuntos de resultados (derecha):** Cada unidad de procesamiento tiene una flecha que apunta a un círculo de salida más pequeño:

- **Salida búsqueda lineal:** Círculo con tres formas: la **estrella**, el **cuadrado** y el **triángulo**.
- **Salida búsqueda RTree:** Círculo con las mismas tres formas: la **estrella**, el **cuadrado** y el **triángulo**.

**Etiqueta (derecha):** **Búsqueda Exacta** — ambos métodos recuperan exactamente los mismos tres vecinos más cercanos.

**Figura:** Diagrama de flujo que compara búsqueda lineal exacta versus búsqueda aproximada en una colección de datos.

**Camino 1 — Búsqueda Lineal:**
- Flecha conduce a un recuadro azul etiquetado **3NN Lineal**.
- Resultado en un círculo más pequeño con tres formas: **estrella**, **cuadrado** y **triángulo** (los 3 vecinos más cercanos exactos).

**Camino 2 — Búsqueda Aproximada:**
- Flecha conduce a un triángulo azul etiquetado **3NN IVF** (Inverted File Index).
- Resultado etiquetado **Búsqueda Aproximada**: contiene una **estrella**, un **triángulo** y un **pentágono naranja**.
- **Detalle clave:** El resultado difiere de la búsqueda lineal; intercambia el cuadrado azul por un pentágono naranja, demostrando que el resultado es una aproximación.

**Recuadro amarillo al pie:**
> Los métodos de búsqueda aproximada son muy eficientes al trabajar en altas dimensiones. Sacrifican precisión por eficiencia.

(slides 51–52)

### Búsqueda Lineal vs Búsqueda Aproximada

| Característica | Búsqueda Lineal | Búsqueda Aproximada |
|----------------|-----------------|----------------------|
| Definición | Compara directamente cada elemento con la consulta | Utiliza técnicas para encontrar resultados "suficientemente buenos" |
| Complejidad | O(n) | Menor complejidad comparada con la búsqueda lineal |
| Exactitud | Encuentra el resultado exacto | Sacrifica precisión por eficiencia |
| Aplicación | Eficiente en conjuntos de datos pequeños | Ideal para conjuntos de datos grandes y de alta dimensionalidad |
| Ventaja | Precisión absoluta | Maneja mejor la maldición de la dimensionalidad |
| Desventaja | Ineficiente en datos grandes y alta dimensionalidad | Pequeña pérdida de precisión |

(slide 53)

### Técnicas de Búsqueda Aproximada

- **IVF Flat:** Índice invertido con compresión plana, trabaja con descriptores globales, rápido de construir, eficiente en memoria, menos preciso que HNSW.

- **HNSW:** Algoritmo basado en grafos jerárquicos, más lento de construir, pero más preciso y rápido en la búsqueda, puede requerir más memoria.

**Investigar su funcionamiento**

**Figura (diagrama IVF Flat — arriba):**
- Dos diagramas de Voronoi lado a lado.
- Diagrama izquierdo: conjunto de «dataset points» dispersos a través de varias celdas.
- Diagrama derecho: ilustra el proceso de búsqueda. Dos «query points» (puntos rojos con flechas) están ubicados dentro de celdas específicas. Una celda está resaltada en amarillo y un cluster de tres celdas adyacentes está resaltado en naranja, mostrando cómo la búsqueda se restringe a particiones específicas (celdas) del espacio vectorial.

**Figura (diagrama HNSW — abajo):**
- Estructura jerárquica con dos planos inclinados que representan diferentes capas: **layer n** (arriba) y **layer n+1** (abajo).
- Muestra un proceso de búsqueda en grafo. Comienza en un **start vector** en la capa superior y sigue caminos (flechas verdes) para encontrar un **local minimum in layer n** más cercano a la ubicación proyectada de un **query vector** (punto rojo).
- Flecha etiquetada **descend one layer** muestra la búsqueda moviéndose de la capa superior a la capa inferior más densa (**layer n+1**).
- En la capa inferior, la búsqueda continúa desde el punto de entrada para encontrar un **local minimum in layer n+1** más preciso cerca del query vector.

(slide 54)

## Implementaciones

- **PostgreSQL**
    - PG Vector (IVF, HNSW)
        - Support kNN search

- **Python**
    - scikit-learn (LSHForest)
        - Support range and kNN search

    - Faiss (IVF, HNSW, LSH)
        - Support kNN search
        - Support GPU

(slide 55)

### PostgreSQL como Vector Database

PostgreSQL puede almacenar y gestionar vectores característicos eficientemente usando la extensión pgvector. Soporta métricas como distancia euclidiana y similitud del coseno. Además, índices de alta dimensionalidad como IVFFlat y HNSW.

```sql
CREATE EXTENSION vector;
```

| Operador | Métrica | Descripción | Rango |
|----------|---------|-------------|-------|
| `<->` | Euclidiana (L2) | Distancia línea recta | [0, ∞] |
| `<#>` | Negación Producto Punto | Opuesto del dot product | (-∞, ∞] |
| `<=>` | Coseno (Angular) | Ángulo entre vectores | [0, 1] |
| `<@` | Inclusión | Componentes dentro | bool |
| `@>` | Contenedor | Contiene componentes | bool |
| `\|\|` | Norma L2 | Magnitud del vector | [0, ∞] |

**Figura (lado izquierdo):**
- Icono de microchip etiquetado «pgvector».
- Vector de entrada representado como lista `[0.2 0.4 0.7 ... 0.1]` alimentando un proceso «Search».
- Debajo de la flecha de búsqueda, recuadro azul con diagrama de Voronoi (conjunto de celdas con puntos diamante azules), representando el particionamiento del espacio vectorial para indexación eficiente (ilustrando IVFFlat).
- Icono del elefante de PostgreSQL sobre un cilindro azul (base de datos) en la esquina inferior derecha del diagrama.

Enlace al pie: Use IVFFlat index on Azure Cosmos DB for PostgreSQL for similarity search

(slide 56)

### pgvector: Sintaxis SQL Práctica

1. **Crear tabla:**

```sql
CREATE TABLE documents (
  id SERIAL PRIMARY KEY,
  content TEXT,
  embedding vector(768)
);
```

2. **Búsqueda por similitud:**

```sql
SELECT id, content FROM documents
ORDER BY embedding <-> '[0.1, 0.2, ...]'::vector
LIMIT 10;
```

3. **Crear índice IVFFLAT:**

```sql
CREATE INDEX ON documents
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);
```

4. **Crear índice HNSW**

```sql
CREATE INDEX ON documents
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
```

(slide 57)

## Glosario

- **Selectividad del filtro ($\sigma_F$):** $\sigma_F = \frac{\# \text{ de candidatos}}{\# \text{ de objetos en la BD}}$. Mide qué tan pequeño es el conjunto de candidatos con respecto al tamaño de la base de datos.

- **R*-Tree:** Variante optimizada del R-Tree. Mejora el rendimiento mediante técnicas como la minimización del solapamiento de nodos. Soporta vectores característicos de baja dimensión.

- **KD-Tree:** Árbol binario para particionar el espacio en k dimensiones. Bueno para datos de baja a moderada dimensionalidad.

- **Ball Tree:** Divide el espacio en hiperesferas (ball nodes). Mejor que KD-Tree en alta dimensionalidad.

- **Local Descriptors:** Extraen patrones locales (e.g., SIFT, ORB, FREAK). Una imagen se representa con múltiples vectores.

- **Global Descriptor:** Extrae un único vector característico (e.g., GIST, HOG, VGG-GAP).

- **SIFT (Scale Invariant Feature Transform):** Descriptores locales invariantes a escala y rotación.

- **Vocabulario Visual:** Conjunto de centroides obtenidos mediante clustering (e.g. K-Means) sobre descriptores locales.

- **Posting Lists:** Para cada clave (Palabra Visual), lista de todas las imágenes que contienen descriptores cuantizados a ese centroide.

- **TF:** Frecuencia del término en el chunk/documento.

- **IDF:** $\log\left(\frac{N}{df_t}\right)$, donde $N$ es el número total de documentos y $df_t$ es el número de documentos/chunks que contienen el término $t$.

- **SPIMI:** Single-Pass In-Memory Indexing.

- **K-Means:** Algoritmo de clustering para obtener K centroides (codewords).

- **Codeword:** Palabra visual o de audio (centroide).

- **Histograma (vector de codewords):** Distribución de frecuencias de codewords en una imagen o audio (dimensión K).

- **Índice invertido:** Asocia cada codeword con las imágenes o audios que lo contienen y su frecuencia (tf).

- **Sliding Window:** Ventana temporal.

- **MFCC:** Mel Frequency Cepstral Coefficients.

- **IVF Flat:** Índice invertido con compresión plana, trabaja con descriptores globales, rápido de construir, eficiente en memoria, menos preciso que HNSW.

- **HNSW:** Algoritmo basado en grafos jerárquicos, más lento de construir, pero más preciso y rápido en la búsqueda, puede requerir más memoria.

