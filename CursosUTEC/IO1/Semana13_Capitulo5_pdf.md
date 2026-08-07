---
curso: IO1
titulo: Semana13-Capitulo5
slides: 85
fuente: Semana13-Capitulo5.pdf
---

## Slide 1
Portada del capítulo "Programación entera". Diagrama decorativo: ejes X1/X2 con una pequeña región factible (triángulo) y puntos marcados Y1, Y2 en la esquina superior (valores 1, 2, 3 en el eje). Pie de página: "©Fabien Cornillier, Investigación de operaciones 1: Modelos determinísticos".

## Slide 2
Título de sección: "Problemas enteros clásicos".

## Slide 3
Título: "Problema de asignación (Assignment Problem)". Texto: tenemos n personas para hacer n tareas, cada persona hace exactamente una tarea, existe un costo $c_{ij}$ si la persona $i$ es asignada a la tarea $j$. Hallar la asignación de costo mínimo.

## Slide 4
Título: "Problema de asignación (Assignment Problem)" — formulación matemática:
$$\min \sum_{i=1}^n \sum_{j=1}^n c_{ij} x_{ij}$$
s.t. $\sum_{j=1}^n x_{ij}=1\ \forall i\in\{1,\dots,n\}$; $\sum_{i=1}^n x_{ij}=1\ \forall j\in\{1,\dots,n\}$; $x_{ij}\in\{0,1\}\ \forall (i,j)$.

## Slide 5
Título: "Problema de la mochila (0–1 Knapsack Problem)". Texto: presupuesto $b$ para invertir en $n$ proyectos potenciales, $a_i$ = monto de inversión del proyecto $i$, $c_i$ = valor esperado de la utilidad. Hallar el subconjunto de proyectos a invertir sin exceder el presupuesto maximizando la utilidad esperada total.

## Slide 6
Título: "Problema de la mochila (0–1 Knapsack Problem)" — formulación:
$$\max \sum_{i=1}^n c_i x_i \quad \text{s.t. } \sum_{i=1}^n a_i x_i \le b,\quad x_i\in\{0,1\}\ \forall i$$

## Slide 7
Título/transición: "Bin-Packing" con variantes 1D, 2D, 3D — slide de introducción a la familia de problemas de empaquetamiento (probablemente con figuras esquemáticas de cajas/contenedores; texto ancla mínimo, se asume ilustrativa).

## Slide 8
"Set covering problem" — slide de presentación del problema de cobertura de conjuntos (primera de tres variantes/ilustraciones consecutivas del mismo tema).

## Slide 9
"Set covering problem" — continuación/segunda ilustración del mismo problema (probablemente ejemplo gráfico de cobertura).

## Slide 10
"Set covering problem" — tercera ilustración/variante del mismo problema.

## Slide 11
Título: "Explosión combinatoria" — slide de transición al tema.

## Slide 12
"Explosión combinatoria — ¿Cuántas soluciones posibles?" Lista de problemas de referencia: Problema de asignación, Problema de la mochila, Covering Problem, Traveling Salesman Problem.

## Slide 13
"Explosión combinatoria — Problema de asignación": pregunta "¿Asignaciones factibles?" con un signo de interrogación gráfico (placeholder de diagrama de asignación).

## Slide 14
"Explosión combinatoria — Problema de asignación": respuesta, número de asignaciones factibles = $n!$.

## Slide 15
"Explosión combinatoria — Problema de la mochila y Covering Problem": pregunta "¿Combinaciones factibles?" (placeholder gráfico).

## Slide 16
"Explosión combinatoria — Problema de la mochila y Covering Problem": respuesta, combinaciones factibles = $2^n$.

## Slide 17
"Explosión combinatoria — TSP": pregunta "¿Ciclos factibles?" (placeholder gráfico con nodos 1,2,3).

## Slide 18
"¿Cuántos caminos posibles?" — diagrama con 3 nodos numerados (1,2,3) mostrando permutaciones de recorrido (grafo triangular).

## Slide 19
"¿Cuántos caminos posibles?" — extensión a 4 nodos (1,2,3,4), mostrando varias configuraciones de grafos completos entre los 4 puntos (varias figuras pequeñas repetidas con las mismas 4 posiciones), ejemplificando el crecimiento combinatorio de rutas.

## Slide 20
"¿Cuántos caminos posibles?" — extensión a 5 nodos (1,2,3,4,5), con múltiples diagramas de grafos repetidos (varias copias de la figura con 5 nodos) ilustrando el conteo de ciclos; al final se muestra el resultado "12" en un caso reducido.

## Slide 21
"¿Cuántos caminos posibles?" — con 20 puntos, resultado numérico: 60 (caso simplificado mostrado con nodos 1–5) y luego menciona un caso con más nodos (7 a 12) — diagrama con nodos numerados 1 a 12 dispuestos en red, ilustrando crecimiento.

## Slide 22
Continuación: con 20 puntos el número de soluciones es 19,958,400. Con 100 puntos, se muestra un número gigantesco de más de 150 dígitos (aprox 6.08×10^157), impreso íntegramente en pantalla como cadena de dígitos.

## Slide 23
"¿Con 1000 puntos?" — se muestra un número astronómico de cientos de dígitos (aprox 4×10^2567), impreso como bloque enorme de texto numérico ocupando la slide entera, terminando en "... soluciones …".

## Slide 24
"Explosión combinatoria — TSP": fórmula general de ciclos factibles = $(n-1)!/2$.

## Slide 25
"Aplicación con 85,900 puntos": ejemplo real de VLSI (Very-large-scale integration) — creación de circuitos integrados con miles de transistores como caso de aplicación de TSP a gran escala.

## Slide 26
Tabla "Explosión combinatoria" comparando crecimiento de funciones: $\log n$, $n^{0.5}$, $n^2$, $2^n$, $n!$ para $n=10,100,1000$:

| n | log n | n^0.5 | n² | 2^n | n! |
|---|---|---|---|---|---|
| 10 | 3.32 | 3.16 | 10² | 1.02×10³ | 3.6×10⁶ |
| 100 | 6.64 | 10.00 | 10⁴ | 1.27×10³⁰ | 9.33×10¹⁵⁷ |
| 1000 | 9.97 | 31.62 | 10⁶ | 1.07×10³⁰¹ | 4.02×10²⁵⁶⁷ |

Nota: un TSP con 101 nodos tiene alrededor de 9.33×10¹⁵⁷ ciclos.

## Slide 27
"¿Un tema de potencia de computadoras?" — ejemplo: problema de mochila ($2^n$) con 438 objetos resuelto en 1 hora por fuerza bruta; pregunta cuántos objetos ($n=?$) podría resolver una computadora 1,000,000 de veces más rápida en una hora.

## Slide 28
Continuación del ejemplo anterior: respuesta, $n=458$ (solo 20 objetos más pese al enorme incremento de velocidad computacional) — ilustra que la potencia computacional no resuelve la explosión combinatoria.

## Slide 29
"¿Un tema de potencia de computadoras?" — tabla de tiempos de evaluación si se pueden evaluar mil millones de soluciones/segundo:

| n | n | n² | n³ | n⁵ | 2^n | n! |
|---|---|---|---|---|---|---|
| 10 | 0.01µs | 0.1µs | 1µs | 0.1ms | 1µs | 0.0036ms |
| 20 | 0.02µs | 0.4µs | 8µs | 3.2ms | 1ms | 77 años |
| 50 | 0.05µs | 2.5µs | 125µs | 312.5ms | 13 días | 9.64×10⁴⁷ años |
| 60 | 0.06µs | 3.6µs | 216µs | 777.6ms | 36.5 años | 2.64×10⁶⁵ años |

## Slide 30
"¿Un tema de potencia de computadoras?" — tabla de tiempos para problemas con $n$ variables binarias, comparando: evaluar mil millones de soluciones/segundo vs. evaluar un millón de millones/segundo eliminando 99.9999999% de soluciones no óptimas:

| n | Tiempo (10⁹/s) | n | Tiempo (10¹²/s, 99.9999999% podado) |
|---|---|---|---|
| 30 | 1 segundo | 70 | 1 segundo |
| 40 | 18 minutos | 80 | 20 minutos |
| 50 | 13 días | 90 | 14 días |
| 60 | 36 años | 100 | 40 años |
| 70 | 37436 años | 110 | 41161 años |

## Slide 31
"¿Un tema de potencia de computadoras? — ¿Cómo resolver problemas enteros grandes?" Texto: hay que eliminar mucho más que 99.99999999999999999999% de las soluciones sin evaluarlas. Repite la tabla del millón de millones de soluciones/segundo con 99.9999999% de poda (misma tabla de la slide 30, columna derecha).

## Slide 32
Transición: "ip… mip… bip…" pregunta "¿Cómo resolver los programas lineales enteros, mixtos y binarios?" Muestra la notación general del programa entero:
$$\min_{S\subseteq N}\Big\{\sum_{j\in S} c_j : S\in\mathcal F\Big\}$$
y un ejemplo numérico: $\max\ x_1+0.64x_2$ s.t. $50x_1+31x_2\le250$, $3x_1-2x_2\ge-4$, $x_1,x_2\in\mathbb Z_+^2$.

## Slide 33
"Redondeo de solución continua" — muestra la solución LP: $(1.9637, 4.9223)$ y pregunta cuál redondeo tomar: ¿(2,5)? ¿(2,4)?, comparado con la solución entera real $(5,0)$. Nota: "y es aún peor para los problemas binarios".

## Slide 34
"Programación lineal y programación lineal entera — Conclusión": la idea básica de aplicar el simplex y redondear la solución óptima generalmente **no funciona**.

## Slide 35
"Programación lineal y programación lineal entera — Sin embargo…": el simplex (u otro método como puntos interiores) es **indispensable** para los programas lineales enteros, mixtos o binarios.

## Slide 36
Título de sección: "Relajación lineal (LP Relaxation)".

## Slide 37
"Relajación lineal (o continua) (LP Relaxation)" — formulación general (P): $\max\ c^Tx+h^Ty$ s.t. $Ax+Gy\le b$, $x\in\mathbb Z_+^n$, $y\in\mathbb R_+^p$. Nota roja: la relajación lineal $R_P$ de $P$ se obtiene suprimiendo las restricciones de integralidad (relajación LP).

## Slide 38
Comparación lado a lado: (P) problema entero original vs (R_P) relajación LP — mismas restricciones salvo que $x\in\mathbb Z_+^n$ pasa a $x\in\mathbb R_+^n$; flecha azul indica la transformación.

## Slide 39
"Ejemplo de programa entero" — gráfico 2D con la región factible entera (círculos = puntos enteros factibles) y la envolvente triangular; recta roja diagonal representa la restricción/objetivo, con la "Solución de la relajación lineal (Rp)" en el vértice superior y la "solución de (P)" (punto entero) más abajo a la derecha, formulación: $\max\ x_1+0.64x_2$ s.t. $50x_1+31x_2\le250$, $3x_1-2x_2\ge-4$, $x_1,x_2\in\mathbb Z_+^2$.

## Slide 40
"Relajación lineal (o continua) (LP Relaxation)" — enunciado formal: si $F(P)$ es el espacio de soluciones factibles de $P$, entonces $F(P)\subseteq F(R_P)$.

## Slide 41
"Límite superior de un problema P de maximización" — si $(x^*,y^*)$ es solución óptima de $P$ y $(\bar x,\bar y)$ es solución óptima de $R_P$, entonces $c^T\bar x+h^T\bar y \ge c^Tx^*+h^Ty^*$. El valor óptimo de $R_P$ es un límite superior de $P$.

## Slide 42
"Límite superior de un problema P de maximización" (continuación, sin diagrama): el valor óptimo de $R_P$ es un límite superior de $P$; cuanto más pequeño sea $F(R_P)$, más cerca del valor óptimo de $P$ está el límite obtenido.

## Slide 43
"Un mismo problema se puede formular de varias formas distintas — Una formulación puede ser mejor que otra" (slide de texto, transición).

## Slide 44
Gráfico: tres formulaciones $P_1$ (triángulo grande), $P_2$ (pentágono irregular) y $P_3$ (pentágono más ajustado, la envolvente convexa) superpuestas sobre la misma malla de puntos enteros (0–4 en ambos ejes), con los puntos factibles reales resaltados en rojo.

## Slide 45
"Envolvente convexa de P" — mismo gráfico de $P_1,P_2,P_3$; a la derecha, relación $F(R_{P_3})\subseteq F(R_{P_1})$ y $F(R_{P_3})\subseteq F(R_{P_2})$; conclusión: la formulación $P_3$ es mejor que $P_1$ y $P_2$; $P_3$ es la envolvente convexa de $P$.

## Slide 46
"Envolvente convexa de P" — mismo gráfico; texto: la envolvente convexa $P_3$ es la formulación **ideal** de $P$; un punto extremo (y entero) de $P_3$ es solución óptima de $P$; si resolvemos la relajación lineal de $P_3$ obtenemos una solución óptima entera de $P$.

## Slide 47
"Envolvente convexa de P" — mismo gráfico; pregunta: ¿podríamos determinar la envolvente convexa de $P$ y resolver su relajación lineal para tener la solución óptima del problema entero?

## Slide 48
"¿Porqué no determinar la envolvente convexa de P y resolver su relajación lineal?" Respuesta: identificar todas las restricciones que configuren la envolvente convexa de $P$ es un problema generalmente mucho más difícil que el mismo problema $P$.

## Slide 49
Título de sección: "Algoritmo de Branch & Bound — Divide y vencerás".

## Slide 50
"Idea general" — diagrama hexagonal amarillo/verde dividido en $X_1$ (amarillo) y $X_2$ (verde): queremos resolver $z^*=\max\{cx\mid x\in X\}$; particionamos $X$ en $\{X_1,X_2\}$; entonces $z^*=\max\{z_1^*,z_2^*\}$.

## Slide 51
"Idea general" — mismo diagrama pero solo con $X_1$ (amarillo) resaltado, mostrando $z_1^*>z_2^*$: si $z_1^*>z_2^*$ es inútil explorar $X_2$; no hay solución óptima en $X_2$.

## Slide 52
"Idea general" — mismo diagrama; añade pregunta: ¿cómo saber que es inútil explorar $X_2$ sin calcular $z_2^*$?

## Slide 53
"Idea general" — mismo diagrama; añade: podemos determinar un límite superior de $z_2^*$. ¿Cómo?

## Slide 54
Gráfico de región factible verde ($X$) en el plano $X_1,X_2$ con puntos enteros (círculos amarillos rellenos = factibles, blancos = no) y una recta roja con flecha indicando la dirección de la "función objetivo".

## Slide 55
Mismo gráfico de $X$; se añade una línea punteada horizontal y anotación "ramificación sobre la variable x₂" con "solución continua" marcada en un vértice de la región (intersección de la recta roja con el borde).

## Slide 56
El polígono $X$ se divide en $Y_1$ (triángulo verde superior, franja sobre $x_2\ge$ línea punteada) e $Y_2$ (región verde inferior); anotación "resolución del problema relajado sobre Y₂"; la "solución continua" marcada en el vértice del pentágono derecho.

## Slide 57
Mismo diagrama $Y_1$/$Y_2$; ahora la "solución continua" se marca en el punto (2, 2), sobre el borde de $Y_2$, con la línea punteada horizontal desplazada.

## Slide 58
Mismo diagrama; se añade una línea punteada vertical y anotación "ramificación sobre la variable x₁", indicando la siguiente ramificación sobre $Y_2$ (o similar) en el punto marcado en rojo.

## Slide 59
Mismo diagrama con $Y_1$/$Y_2$; ahora $Y_2$ se reduce a un rectángulo (recortado por la línea vertical punteada) y se muestra la nueva región sombreada más clara a la derecha de la línea vertical.

## Slide 60
Mismo diagrama; anotación "ahora tenemos que averiguar si una mejor solución entera existe sobre Y₁"; "primera solución entera" marcada en punto azul (2,2); "Y₂" es el rectángulo recortado.

## Slide 61
Mismo diagrama; anotación "solución continua" en el punto rojo (1,3) sobre el borde de $Y_1$; "primera solución entera" reemplazada por rótulo "solución continua" apuntando a un punto distinto.

## Slide 62
Mismo diagrama; anotación "ramificación sobre la variable x₁" con línea punteada vertical adicional sobre $Y_1$ (triángulo superior), mostrando la siguiente subdivisión.

## Slide 63
Mismo diagrama; anotación "el límite superior no permite podar Y₁" y "solución continua" — indica que el bounding no permite descartar la rama $Y_1$ todavía.

## Slide 64
Mismo diagrama; anotación "segunda solución entera" (punto azul en (1,3)) y "solución sobre Y₂ mejor que solución sobre Y₁ (solo un poquito…)" — comparación de las dos soluciones enteras encontradas.

## Slide 65
"Problema original X" — formulación explícita del ejemplo numérico usado en el resto del capítulo:
$$\max\ -x_1+2x_2 \quad \text{s.t. } -4x_1+6x_2\le 9,\ x_1+x_2\le 4,\ (x_1,x_2)\in\mathbb Z_+^2$$

## Slide 66
"Inicialización" — mismo problema (X); inicializa el algoritmo B&B con $Z^*=+\infty$ y lista de subproblemas activos: {X}.

## Slide 67
"Resolución de la relajación LP de X" — mismo problema; $Z^*=+\infty$, subproblemas activos {X} resaltado en verde; Solución LP: $(1.5, 2.5)$, $Z^*(LP(X))=3.5$.

## Slide 68
"Ramificación de X sobre x₂" — dos nuevos subproblemas creados: $x_2\le\lfloor x_2^*\rfloor=2$ (Y1) y $x_2\ge\lceil x_2^*\rceil=3$ (Y2); recuerda solución LP $(1.5,2.5)$, $Z^*(LP(X))=3.5$.

## Slide 69
"Resolución de la relajación LP de Y₁" — problema (Y1) con la restricción adicional $x_2\le2$; $Z^*=+\infty$; subproblemas activos {X, Y1, Y2} (X e Y1 en amarillo); Solución LP: $(0.75, 2.0)$, $Z^*(LP(Y_1))=3.25$.

## Slide 70
"Resolución de la relajación LP de Y₂" — problema (Y2) con $x_2\ge3$; subproblemas activos {X (amarillo), Y1 (amarillo), Y2 (gris=descartado)}; Solución LP: **No factible**.

## Slide 71
"Ramificación de Y₁ sobre x₁" — dos nuevos subproblemas: $x_1\le\lfloor x_1^*\rfloor=0$ (Y1,1) y $x_1\ge\lceil x_1^*\rceil=1$ (Y1,2); recuerda Solución LP de Y1 $(0.75,2.0)$, $Z^*(LP(Y_1))=3.25$.

## Slide 72
"Resolución de la relajación LP de Y₁,₁" — problema (Y1,1) con $x_1\le0$ además de restricciones previas; subproblemas activos {X, Y1 amarillos, Y2 gris, Y1,1 y Y1,2 amarillos}; Solución LP: $(0, 1.5)$, $Z^*(LP(Y_{1,1}))=3.0$.

## Slide 73
"Resolución de la relajación LP de Y₁,₂" — problema (Y1,2) con $x_1\ge1$; Solución LP: $(1.0, 2.0)$, $Z^*(LP(Y_{1,2}))=3.0$; subproblemas activos igual que la anterior.

## Slide 74
"Eliminación de Y₁,₁" — $Z^*=3.0$ (actualizado con la solución entera $(1,2)$ hallada en Y1,2); nota roja: relajación $Z^*(LP(Y_{1,1}))=3.0$ no mejor que $Z^*$, por lo tanto se descarta (poda) Y1,1; subproblemas activos: X, Y1 en amarillo, Y2/Y1,1/Y1,2 en gris.

## Slide 75
"Eliminación de Y₁" — $Z^*=3.0$; mejor solución entera de Y1 = 3.0; todos los subproblemas (X amarillo, resto gris) quedan resueltos/descartados dentro de la rama Y1.

## Slide 76
"Eliminación de X" — $Z^*=3.0$; mejor solución entera de X = 3.0; todos los subproblemas (X, Y1, Y2, Y1,1, Y1,2) en gris = cerrados; fin del algoritmo, óptimo global = 3.0.

## Slide 77
Slide de resumen con fragmentos superpuestos del ejemplo de la mochila 0-1 (4 variables binarias): $5x_1+7x_2+4x_3+3x_4\le14$, $x_i\in\{0,1\}$, $x_1+x_2+x_3\le2$, $x_1+x_2+x_4\le2$; y también recuerda el problema (X) de asignación anterior — parece un slide compuesto/transición mezclando fragmentos de distintas fórmulas del capítulo (posible slide de resumen o error de composición del PDF original).

## Slide 78
Slide similar: repite formulación (X) $\max\ x_1+2x_2$ s.t. $4x_1+6x_2\le9$, $x_1+x_2\le4$, $(x_1,x_2)\in\mathbb Z_+^2$; junto con inicialización $Z^*=+\infty$, subproblemas activos {X} — resumen/recordatorio del ejemplo de mochila con las restricciones $x_i\in\{0,1\}$.

## Slide 79
Slide similar: formulación (X) con Solución LP: $(1.5, 2.5)$, $Z^*(LP(X)):3.5$; identifica un conjunto $C\subseteq\{1,\dots,n\}$ tal que $\sum_i w_ix_i>W$ — mezcla de fórmulas de mochila y del ejemplo (X), aparenta ser un slide de transición/resumen del capítulo con fragmentos superpuestos de distintas fórmulas (cobertura, mochila, B&B).

## Slide 80
Slide similar de resumen: "Ramificación de X sobre x₂" con los dos subproblemas $x_2\le\lfloor x_2^*\rfloor=2$ (Y1) y $x_2\ge\lceil x_2^*\rceil=3$ (Y2); Solución LP $(1.5,2.5)$, $Z^*(LP(X))=3.5$; superpuesto con restricción de cobertura $|C|\ge1$ y descartes por infactibilidad — slide de repaso condensado del proceso de B&B aplicado al ejemplo mochila con las anotaciones "Descartado por infactibilidad" y "Descartado por límite superior (bounding)".

## Slide 81
"Resolución de la relajación LP de Y₁,₂" — problema (Y1,2) con $x_1\ge1$ además de $x_2\le2$, $-4x_1+6x_2\le9$, $x_1+x_2\le4$; $Z^*=3.0$; subproblemas activos: X, Y1, Y1,1 en amarillo, Y2/Y1,2 en gris; Solución LP: $(1.0, 2.0)$, $Z^*(LP(Y_{1,2}))=3.0$.

## Slide 82
"Eliminación de Y₁,₁" — mismo problema (Y1,1) con $x_1\le0$; $Z^*=3.0$; nota roja: "Relajación $Z^*(LP(Y1,1))$ no mejor que $Z^*$"; Solución LP $(0,1.5)$, $Z^*(LP(Y_{1,1}))=3.0$; subproblemas activos: X y Y1 amarillos, resto gris.

## Slide 83
"Eliminación de Y₁" — $Z^*=3.0$; mejor solución entera de Y1 = 3.0; subproblemas activos: X amarillo, Y1/Y2/Y1,1/Y1,2 gris (cerrados).

## Slide 84
"Eliminación de X" — $Z^*=3.0$; mejor solución entera de X = 3.0; todos los subproblemas (X, Y1, Y2, Y1,1, Y1,2) en gris = cerrados; fin del algoritmo.

## Slide 85
Diagrama de árbol de Branch & Bound completo (resumen final): nodo raíz (X) con Solución LP $(1.5,2.5)$, $Z^*(LP(X))=3.5$, que se ramifica en $x_2\le\lfloor x_2^*\rfloor=2$ (rama izquierda, Solución LP $(0.75,2.0)$, $Z^*(LP(Y_1))=3.25$) y $x_2\ge\lceil x_2^*\rceil=3$ (rama derecha, marcada con X naranja "Descartado por infactibilidad", No factible). La rama izquierda se subdivide en $x_1\le\lfloor x_1^*\rfloor=0$ (marcada con X naranja "Descartado por límite superior (bounding)", Solución LP $(0,1.5)$, $Z^*(LP(Y_{1,1}))=3.0$) y $x_1\ge\lceil x_1^*\rceil=1$ (Solución LP $(1.0,2.0)$, $Z^*(LP(Y_{1,2}))=3.0$, hoja final con solución entera óptima). Árbol completo que resume visualmente todo el proceso de Branch & Bound desarrollado en las slides 65-84.
