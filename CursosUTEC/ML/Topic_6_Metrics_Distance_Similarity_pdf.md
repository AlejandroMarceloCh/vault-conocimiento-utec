---
curso: ML
titulo: Topic 6 - Metrics_ Distance & Similarity
slides: 13
fuente: Topic 6 - Metrics_ Distance & Similarity.pdf
---

## Slide 1

METRICS
Distance & Similarity

## Slide 2

Vecino más cercano

**Figura:** Gráfico de dispersión 2D (eje X e Y sin marcas numéricas, fondo gris claro). Se muestran 6 puntos de datos ("Data points", círculos rosados) etiquetados D (arriba a la izquierda), E (centro-derecha, altura media-alta), F (centro), C (abajo a la derecha) y B (abajo a la izquierda, cerca del punto de consulta). Un punto de consulta ("Query point", estrella roja) etiquetado A se ubica en la esquina inferior izquierda, muy cerca de B.

## Slide 3

Vecino más cercano

**Figura:** Dos gráficos de dispersión lado a lado con los mismos 6 puntos (A, B, C, D, E, F) pero con distinta escala en el eje Y, ilustrando cómo el escalamiento cambia cuál es el "vecino más cercano".
- Panel izquierdo: eje X de 2 a 8, eje Y ("Y axis") de 3 a 8. Puntos: D en (2, 8), E en (7, 7), F en (5, 5), C en (8, 3.5), B en (2.5, 3.2), A (estrella roja, query point) en (2, 3). Leyenda "Nearest: B", con línea punteada roja conectando A con B (el más cercano en esta escala).
- Panel derecho: mismo eje X (2 a 8), pero eje Y ("Y axis (scaled differently)") de 0.15 a 0.40. Puntos: D en (2, 0.40), E en (7, 0.35), F en (5, 0.25), C en (8, 0.175), B en (2.5, 0.16), A (estrella roja) en (2, 0.15). Leyenda "Nearest: D", con línea punteada verde conectando A verticalmente con D (ahora el más cercano al cambiar la escala del eje Y).

## Slide 4

Vecino más cercano

**Figura:** Dos paneles con los mismos 6 puntos de datos (D, E, F, C, B, A como query point) sobre fondo gris.
- Panel izquierdo: espacio "normal" (euclidiano), vacío salvo los puntos, sin líneas de distancia dibujadas.
- Panel derecho: el mismo espacio pero atravesado por una red de líneas negras que forman un laberinto/camino irregular entre los puntos, ilustrando una métrica de distancia no euclidiana (tipo distancia de camino/geodésica) donde el trayecto entre puntos depende de las paredes o rutas disponibles y no de la línea recta.

## Slide 5

Vecino más cercano

**Figura:** Dos paneles comparando el mismo conjunto de puntos (D, E, F, C, B, A) en dos "espacios" distintos.
- Panel izquierdo: espacio abstracto gris con los puntos ubicados igual que en slides anteriores.
- Panel derecho: los mismos puntos superpuestos sobre un mapa mundial real (proyección con Norteamérica, Sudamérica, Europa, África, Asia, Oceanía visibles), mostrando que las mismas posiciones relativas en el espacio abstracto corresponden a ubicaciones geográficas reales (D en Norteamérica/Ártico, E en África central, F en Sudamérica norte, C en Oceanía/Australia, B y A en la Antártida/extremo sur), para ilustrar que la métrica de distancia apropiada depende de la naturaleza real del espacio (ej. distancia geodésica/Haversine en vez de euclidiana plana).

## Slide 6

1.
Métricas
Definición

## Slide 7

Condiciones de una Métrica

**Definition 7.1.** A metric $d$ on a set $X$ is a function $d : X \times X \rightarrow \mathbb{R}$ such that for all $x, y \in X$:

(1) $d(x,y) \geq 0$ and $d(x,y) = 0$ if and only if $x = y$;

(2) $d(x,y) = d(y,x)$ (symmetry);

(3) $d(x,y) \leq d(x,z) + d(z,x)$ (triangle inequality).

A metric space $(X, d)$ is a set $X$ with a metric $d$ defined on $X$.

*Metric spaces by UCDavis*

## Slide 8

Ejemplos de Distancias

**Figura:** Tres diagramas de cuadrícula 3x3 con un punto naranja en el centro (o esquina inferior izquierda en el primero) mostrando cómo se calcula cada distancia:
- **Euclidean Distance**: cuadrícula con una flecha diagonal desde el punto naranja (esquina inferior izquierda) hasta la esquina superior derecha de la cuadrícula. Fórmula: $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$.
- **Manhattan Distance**: cuadrícula con el punto naranja en el centro y flechas en las 8 direcciones (horizontal, vertical, diagonal) con valores mostrados en cada celda: 2,1,2 (fila superior), 1,(centro),1 (fila media), 2,1,2 (fila inferior) — el costo de moverse diagonalmente es la suma de los pasos horizontal+vertical. Fórmula: $|x_1-x_2|+|y_1-y_2|$.
- **Chebyshev Distance**: cuadrícula con el punto naranja en el centro y flechas en las 8 direcciones, todas las celdas adyacentes marcadas con valor 1 (mismo costo en cualquier dirección, incluida la diagonal). Fórmula: $\max(|x_1-x_2|, |y_1-y_2|)$.

- Uso: Espacios isotrópicos, misma escala
  Ejemplo: Puntos en un plano 2D/3D
- Uso: Navegación en cuadrículas, más robusta a outliers
  Ejemplo: Calles de ciudad
- Uso: Movimiento en cualquier dirección con mismo costo
  Ejemplo: Movimientos del rey en ajedrez

## Slide 9

Ejemplos de Distancias

**Figura:** Fila superior de 5 diagramas, cada uno con un punto verde (origen) y un punto azul (destino) sobre ejes cartesianos, conectados por una línea roja que ilustra el trayecto de cada métrica:
- **Euclidean**: línea recta diagonal directa entre los dos puntos.
- **Manhattan**: trayecto en forma de "L" (horizontal luego vertical) entre los dos puntos.
- **Chebyshev**: línea vertical recta desde el punto verde hacia abajo (solo se muestra el componente vertical, el mayor de los dos ejes).
- **Minkowski**: múltiples trayectorias desde el punto verde hasta el azul etiquetadas con distintos valores de $p$: $p=1$ (forma de L, arriba), $p=1{,}3$, $p=2$ (diagonal recta), $p=\infty$ (etiqueta cerca del punto verde, abajo a la izquierda), mostrando cómo la forma de la trayectoria varía según el parámetro $p$.
- **Cosine**: dos puntos (verde y azul) con líneas rojas desde el origen de los ejes hacia cada uno, formando un ángulo $\theta$ entre ellas, con la etiqueta $\cos(\theta)$ marcando el ángulo.

Fila inferior de 5 diagramas:
- **Haversine**: una esfera (globo) con un punto verde y un punto azul sobre su superficie, conectados por una línea roja curva que sigue la superficie esférica (distancia geodésica), con líneas de latitud/longitud dibujadas sobre la esfera.
- **Hamming**: dos secuencias binarias de 5 bits una encima de otra: fila superior "1 0 0 1 1", fila inferior "1 1 0 1 0", con líneas rojas verticales conectando las posiciones donde los bits difieren (posición 2 y posición 4).
- **Jaccard**: diagrama de Venn con un círculo verde (x) y un círculo azul (y) superpuestos, la intersección resaltada en rojo oscuro y etiquetada "x∩y"; debajo, ambos círculos coloreados enteramente en rojo etiquetados "x∪y" (unión), representando la fórmula intersección sobre unión.
- **Sörensen-Dice**: similar al de Jaccard, diagrama de Venn con círculo verde y azul, intersección "x∩y" resaltada en rojo, con un "2" al lado; debajo, dos círculos rojos separados unidos por un signo "+", representando 2×intersección sobre la suma de los tamaños de los conjuntos.
- **Dynamic Time Warping**: dos series temporales (curvas) una en verde y otra en azul, con múltiples líneas verticales negras conectando puntos correspondientes entre ambas curvas en distintos instantes de tiempo, mostrando el alineamiento no lineal entre las dos secuencias.

## Slide 10

Ejemplos de Distancia

**Figura:** Dos elementos gráficos lado a lado.
- Izquierda: gráfico titulado "KL Divergence Between Two Gaussians", eje X ("$x$") de -4 a 6, eje Y ("Probability Density") de 0.00 a 0.40. Dos curvas gaussianas superpuestas: $P(x)$ en rojo centrada cerca de 0, y $Q(x)$ en azul centrada cerca de 1. El área bajo $P(x)$ que no se solapa con $Q(x)$ está sombreada en rosa claro y etiquetada "KL Divergence (P||Q)"; el área bajo $Q(x)$ que no se solapa con $P(x)$ está sombreada en azul claro y etiquetada "KL Divergence (Q||P)".
- Derecha: un cubo (hipercubo binario) con 8 vértices etiquetados en binario de 3 bits: 100, 101, 000, 001, 110, 111, 010, 011, conectados por aristas azules formando la estructura del cubo. Se muestra un camino resaltado en rojo con tres pasos etiquetados: "Paso 1" (de 100 a 110, hacia abajo), "Paso 2" (de 110 a 111, hacia la derecha) y "Paso 3" (de 111 a 011, diagonal hacia abajo), ilustrando un recorrido de distancia (tipo Hamming) sobre el cubo de bits.

## Slide 11

Ejemplos de Distancia

**Figura:** Dos diagramas lado a lado.
- Izquierda ("Longest Common Subsequence (LCS)"): "String 1" = A G G T A B (letras en recuadros individuales); "String 2" = G X T X A Y B (letras en recuadros individuales); debajo, "LCS = G T A B" (la subsecuencia común más larga entre ambas cadenas, resaltada en recuadros).
- Derecha ("Edit Distance"): fila superior "STR 1" = GEEXSFRGEEKKS y "STR 2" = GEEKSFORGEEKS (letras en recuadros, STR1 en amarillo, STR2 en verde). Debajo se muestra el proceso de edición paso a paso: STR1 se descompone en tres segmentos con operaciones marcadas — "Replace X TO K" (sobre el segmento GEEKSF), "Insert O Between F & R" (inserción de una O), "Remove K" (sobre el segmento RGEEKS) — que al aplicarse producen STR2 = GEEKSFORGEEKS. Texto al pie: "Minimum Number Of Edits To Convert Str1 To Str 2 = 3".

Longest Common Subsequence (LCS)
Edit Distance

## Slide 12

Ejercicio

Sistema de Recomendación Musical

Una plataforma de streaming musical quiere recomendar canciones similares. Para cada canción tienen las siguientes características:

- Tempo: 60-200 BPM (beats por minuto)
- Energía: 0.0 - 1.0 (normalizado)
- Valencia emocional: -1.0 (triste) a +1.0 (alegre)
- Popularidad: 0-100
- Duración: 30-600 segundos
- Género: Rock, Pop, Jazz, Clásica, Electrónica (categórico)
- Tonalidad: C, C#, D, D#, E, F, F#, G, G#, A, A#, B (12 notas)
- Hora del día preferida: 0-23 horas (cuándo se escucha más)
- ¿Qué tipo de distancia sería más apropiada y por qué?
- Dos canciones tienen exactamente las mismas características excepto que una es muy popular (95/100) y otra no (15/100). ¿En qué escenarios querrías que se consideren "similares" y en cuáles no?

## Slide 13

**Figura:** Fotografía de dos personas (una mujer y un hombre) con bata de laboratorio y lentes de protección, observando de cerca un dispositivo mecánico/robótico alargado con múltiples componentes metálicos y cables, en un laboratorio. La imagen tiene una superposición de color azul (tratamiento gráfico de la plantilla). Es una transición sin texto de contenido adicional.
