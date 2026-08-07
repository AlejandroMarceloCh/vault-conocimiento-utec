---
curso: IO1
titulo: Semana14-Capitulo5
slides: 126
fuente: Semana14-Capitulo5.pdf
---

## Slide 1
Portada del capítulo: "Programación entera". Diagrama en el plano X1-X2: región factible poligonal (verde/gris) con dos subregiones marcadas Y1 (triángulo superior) e Y2 (rectángulo/región inferior), puntos enteros marcados con círculos amarillos rellenos dentro de la región factible y círculos vacíos fuera. Una línea roja diagonal representa una restricción/curva de nivel que corta la región cerca de x1≈2.6. Un punto rojo marca la solución óptima continua en (≈2.6, 2). Créditos: "©Fabien Cornillier, Investigación de operaciones 1: Modelos determinísticos" (decorativa/pie de página, se repite en varias slides).

## Slide 2
Portada de sección: "Problemas enteros clásicos" (texto negro + subtítulo rojo manuscrito "clásicos"). Sin contenido adicional.

## Slide 3
Texto: "Problema de asignación (Assignment Problem)". Definición: n personas para hacer n tareas, costo c_ij, hallar asignación de costo mínimo. Sin elementos visuales adicionales (solo texto).

## Slide 4
Formulación matemática del problema de asignación:
$$\min \sum_{i=1}^n\sum_{j=1}^n c_{ij}x_{ij}$$
$$\text{s.t.} \sum_{j=1}^n x_{ij}=1 \quad \forall i\in\{1,...,n\}$$
$$\sum_{i=1}^n x_{ij}=1 \quad \forall j\in\{1,...,n\}$$
$$x_{ij}\in\{0,1\}\quad \forall (i,j)\in\{1,...,n\}^2$$

## Slide 5
Texto: "Problema de la mochila (0-1 Knapsack Problem)". Definición: presupuesto b, n proyectos, monto de inversión a_i, utilidad esperada c_i; hallar subconjunto que maximiza utilidad sin exceder presupuesto.

## Slide 6
Formulación matemática del problema de la mochila:
$$\max \sum_{i=1}^n c_i x_i$$
$$\text{s.t.} \sum_{i=1}^n a_i x_i \le b$$
$$x_i \in \{0,1\}\quad \forall i\in\{1,...,n\}$$

## Slide 7
Título "Bin-Packing 1D" (subtítulo rojo "1D"). Gráfico de barras (19 contenedores/bins numerados 1-19) cada uno de altura hasta 80, subdividido en segmentos con números (objetos empaquetados dentro de cada bin) que suman aproximadamente la capacidad de cada bin (ej. bin 1: 79 = 8+45+26; bin 6: 80 = 3+14+63). Ilustra el problema de empaquetado de objetos 1D en contenedores de capacidad fija.

## Slide 8
Título "2D" (rojo, manuscrito). Captura de una herramienta de optimización de corte/empaquetado 2D: un rectángulo grande contiene 40 piezas rectangulares numeradas (1-40) de distintos tamaños, acomodadas sin solaparse (packing). A la izquierda, panel de estadísticas de la herramienta: TYPE 1, FinEff, Max 95.61, Aver 95.24, Min 94.74, Time 13048/5.0, Iter 595, RAND 5, Eff 95.12, Sort 40/0, PACKING Rand 1, Eff 91.78/94.79, Best 4/0, Sort 12/0. Ilustra bin-packing 2D.

## Slide 9
Título "3D" (rojo, manuscrito). Captura de una herramienta de empaquetado 3D: contenedor tipo caja/container visto en perspectiva isométrica con 20 cajas numeradas (1-20) de distintos colores y tamaños acomodadas dentro sin solaparse. Ilustra bin-packing 3D.

## Slide 10
Título "Set covering problem" (rojo, manuscrito, esquina superior derecha). Diagrama de puntos: conjunto de ~25 puntos dispersos, algunos resaltados en azul (subconjunto seleccionado) y otros en blanco (no seleccionados/cubiertos). Ilustra el concepto base del problema de cobertura de conjuntos (selección de puntos "centro").

## Slide 11
Mismo tema "Set covering problem". Ahora se añaden círculos naranjas translúcidos (áreas de cobertura) centrados en los puntos azules, que se solapan entre sí, cubriendo el conjunto de puntos blancos. Ilustra visualmente cómo un conjunto de centros (azules) con radio de cobertura cubre todos los puntos del plano.

## Slide 12
Continuación "Set covering problem": variante del diagrama anterior con puntos grises adicionales (posiblemente puntos no cubiertos) y círculos naranjas de cobertura reubicados; menos puntos azules (centros) que en la slide 11, mostrando una solución de cobertura distinta/optimizada.

## Slide 13
Portada de subsección: "Explosión combinatoria" (rojo manuscrito) + "combinatoria" en negro. Sin más contenido.

## Slide 14
Título "Explosión combinatoria" con lista de los 4 problemas clásicos vistos: Problema de asignación, Problema de la mochila, Covering Problem, Traveling Salesman Problem. Anotación manuscrita roja con flecha: "¿Cuántas soluciones posibles?".

## Slide 15
"Explosión combinatoria — Problema de asignación". Gran signo de interrogación rojo (manuscrito) centrado, con texto "Asignaciones factibles" debajo — plantea la pregunta antes de dar la respuesta (slide siguiente).

## Slide 16
Misma cabecera "Explosión combinatoria — Problema de asignación". Respuesta mostrada en rojo grande: **n!** — "Asignaciones factibles" = n! (factorial).

## Slide 17
"Explosión combinatoria — Problema de la mochila y Covering Problem". Signo de interrogación rojo grande, "Combinaciones factibles" debajo (pregunta).

## Slide 18
Misma cabecera. Respuesta: **2ⁿ** en rojo grande — "Combinaciones factibles" = 2 elevado a n.

## Slide 19
"Explosión combinatoria — TSP". Signo de interrogación rojo grande, "Ciclos factibles" debajo (pregunta).

## Slide 20
Diagrama con 3 nodos numerados (1, 2, 3) dispersos, sin conexiones. Anotación roja manuscrita con flecha: "¿Cuántos caminos posibles?". Introduce el conteo de ciclos en TSP con n=3.

## Slide 21
Igual que la slide 20 pero con 4 nodos (1,2,3,4) dispersos, misma pregunta "¿Cuántos caminos posibles?" (sin responder aún).

## Slide 22
Con n=4 nodos: se muestran 3 grafos distintos, cada uno con las 4 aristas de un ciclo hamiltoniano distinto sobre los mismos 4 nodos (cada grafo dibuja un ciclo diferente que pasa por 1,2,3,4). Anotación roja "3" indicando que hay 3 ciclos posibles distintos con 4 nodos.

## Slide 23
5 nodos (1,2,3,4,5) dispersos sin conexiones. Pregunta "¿Cuántos caminos posibles?" (aún sin responder).

## Slide 24
Con n=5 nodos: cuadrícula de 12 grafos pequeños, cada uno mostrando un ciclo hamiltoniano distinto sobre los 5 nodos (1,2,3,4,5) con conexiones distintas entre sí. Anotación roja "12" — hay 12 ciclos hamiltonianos distintos con 5 nodos ((5-1)!/2 = 12).

## Slide 25
6 nodos (1,2,3,4,5,6) dispersos. Pregunta "¿Cuántos caminos posibles?". Anotación roja "60" ya visible como respuesta ((6-1)!/2 = 60).

## Slide 26
12 nodos numerados (1 a 12) dispersos aleatoriamente en el plano. Pregunta "¿Cuántos caminos posibles?". Respuesta roja grande: **19,958,400** (=(12-1)!/2).

## Slide 27
"20 puntos" — ~20 puntos dispersos grises en el plano. Anotación "20 puntos" con flecha. Número gigante rojo: **6,082,255,020,4416,000** (≈6.08×10^15, factorial de ciclos con 20 nodos) — nota: el texto extraído tiene el número mal formateado en el OCR (posible salto de coma), se transcribe tal como aparece renderizado en la slide.

## Slide 28
"¿Con 100 puntos?" — solo texto, gran número (soluciones) escrito en gris/negro ocupando casi toda la slide: una cifra de aproximadamente 156 dígitos representando el número de ciclos factibles con 100 nodos, terminando en "...soluciones ..." (rojo). Ilustra la explosión combinatoria extrema.

## Slide 29
"¿Con 1000 puntos?" con anotación roja "Exactamente…". Bloque de texto denso (~20 líneas) con un número astronómico de cientos de dígitos que representa las soluciones factibles con 1000 nodos, terminando en muchos ceros y "...soluciones ..." en rojo. Tamaño de fuente pequeño para caber el número completo.

## Slide 30
"Explosión combinatoria — TSP". Fórmula roja grande: **(n-1)!/2** — "Ciclos factibles", resumiendo la fórmula general derivada en las slides anteriores (20-29).

## Slide 31
"Aplicación con 85,900 puntos" con anotación manuscrita roja y flecha. Imagen técnica: patrón denso de líneas azules horizontales tipo circuito impreso/VLSI (textura de rayado denso simulando un layout de circuito). Texto explicativo: "Very-large-scale integration (integración a muy gran escala): creación de circuitos integrados con miles de transistores". Ilustra aplicación real de TSP a gran escala (ruteo de VLSI).

## Slide 32
Bloque de texto gris denso ocupando casi toda la slide (columnas de dígitos ilegibles a simple vista, representando una cifra combinatoria enorme para el caso de 85,900 puntos), con un recuadro rojo resaltando una porción del número. Etiqueta roja "soluciones …" en la esquina inferior derecha. Continuación de la slide 31 (cifra de soluciones para VLSI).

## Slide 33
Título "Explosión combinatoria". Tabla con columnas n, log n, n^0.5, n², 2ⁿ, n!:

| n | log n | n^0.5 | n² | 2ⁿ | n! |
|---|---|---|---|---|---|
| 10 | 3.32 | 3.16 | 10² | 1.02×10³ | 3.6×10⁶ |
| 100 | 6.64 | 10.00 | 10⁴ | 1.27×10³⁰ | 9.33×10¹⁵⁷ |
| 1000 | 9.97 | 31.62 | 10⁶ | 1.07×10³⁰¹ | 4.02×10²⁵⁶⁷ |

Texto: "Un TSP con 101 nodos tiene alrededor de 9.33×10¹⁵⁷ ciclos". Compara crecimiento de distintas funciones para mostrar la explosión combinatoria de n!.

## Slide 34
"¿Un tema de potencia de computadoras?" Texto: problema de mochila (2ⁿ) con 438 objetos, computadora resuelve por fuerza bruta en 1 hora. Pregunta: "Una computadora 1,000,000 veces más rápida podrá resolver un problema con n = ? en una hora" (con "?" en rojo, sin respuesta aún).

## Slide 35
Misma pregunta que la 34, pero ahora con la respuesta: **n = 458** en negrita — muestra que aumentar la velocidad computacional 1 millón de veces solo permite crecer n de 438 a 458, ilustrando lo inútil de la fuerza bruta ante el crecimiento exponencial.

## Slide 36
"¿Un tema de potencia de computadoras?" Tabla con columnas n, n, n², n³, n⁵, 2ⁿ, n! (tiempos si se evalúan mil millones de soluciones/segundo):

| n | n | n² | n³ | n⁵ | 2ⁿ | n! |
|---|---|---|---|---|---|---|
| 10 | 0.01µs | 0.1µs | 1µs | 0.1ms | 1µs | 0.0036ms |
| 20 | 0.02µs | 0.4µs | 8µs | 3.2ms | 1ms | 77 años |
| 50 | 0.05µs | 2.5µs | 125µs | 312.5ms | 13 días | 9.64×10⁴⁷ años |
| 60 | 0.06µs | 3.6µs | 216µs | 777.6ms | 36.5 años | 2.64×10⁶⁵ años |

Muestra cómo n! y 2ⁿ crecen inmanejablemente incluso con hardware muy rápido.

## Slide 37
Dos tablas lado a lado bajo "¿Un tema de potencia de computadoras?": izquierda "Problema con n variables binarias — si evaluamos mil millones de soluciones/segundo" (n=30→1 seg, 40→18 min, 50→13 días, 60→36 años, 70→37436 años); derecha "si evaluamos un millón de millones de soluciones/segundo y eliminamos 99.9999999% de soluciones no óptimas" (n=70→1 seg, 80→20 min, 90→14 días, 100→40 años, 110→41161 años). Compara fuerza bruta vs poda agresiva.

## Slide 38
Repite la tabla derecha de la slide 37 (millón de millones de soluciones/seg, eliminando 99.9999999% de soluciones no óptimas: n=70→1seg...110→41161 años). Pregunta manuscrita roja: "¿Cómo resolver problemas enteros grandes?" con texto: "Tenemos que eliminar mucho más que 99.99999999999999999999% de las soluciones sin evaluarlas" — plantea la necesidad de algoritmos de poda tipo Branch & Bound.

## Slide 39
Imagen decorativa de un satélite tipo Sputnik en el espacio, con la Tierra al fondo, y textos manuscritos "ip... mip... bip..." (juego de palabras con IP/MIP/BIP — Integer/Mixed/Binary Programming — simulando el sonido de un satélite emitiendo señales). Pie: "¿Cómo resolver los programas lineales enteros, mixtos y binarios?" — transición hacia los métodos de resolución.

## Slide 40
"Ejemplo de programa entero". Formulación:
$$\max x_1+0.64x_2$$
$$\text{s.t. } 50x_1+31x_2\le 250$$
$$3x_1-2x_2\ge -4$$
$$x_1,x_2\in\mathbb{Z}_+^2$$
Gráfico: retícula de puntos enteros (círculos blancos) en el primer cuadrante, con una línea roja diagonal (curva de nivel de la función objetivo) que toca dos puntos enteros marcados en negro (uno arriba cerca del eje Y, otro abajo cerca del eje X), representando las dos soluciones óptimas alternativas sobre la retícula entera. También se dibuja la región factible en negro (polígono triangular irregular).

## Slide 41
Título "Redondeo de solución continua". Formulación repetida (max x1+0.64x2, s.t. 50x1+31x2≤250, 3x1-2x2≥-4). Texto: "Solución LP: (1.9637, 4.9223)"; "Redondeo: ¿cuál? ¿(2,5)? ¿(2,4)?"; "Solución entera: (5,0)". Nota roja manuscrita: "...y es aún peor para los problemas binarios". Gráfico: retícula de puntos enteros con línea roja diagonal; recuadro gris "solución LP" con flecha apuntando al punto óptimo continuo (arriba, cerca del vértice); recuadro gris "solución entera" con flecha apuntando al punto óptimo entero real (5,0) en el eje X — muestra que redondear la solución LP da un resultado muy distinto (y peor) que la verdadera solución entera óptima.

## Slide 42
Título "Programación lineal y programación lineal entera". Subtítulo rojo "Conclusión". Texto: "La idea básica que consiste en aplicar el simplex y redondear la solución óptima generalmente **no funciona**."

## Slide 43
Mismo título. Subtítulo rojo "Sin embargo…". Texto: "El simplex (u otro método como puntos interiores) es **indispensable** para los programas lineales enteros, mixtos o binarios." — transición hacia el uso de LP como subrutina (relajación).

## Slide 44
Portada de sección: "Relajación lineal" con subtítulo rojo manuscrito "(LP Relaxation)". Sin más contenido.

## Slide 45
Título "Relajación lineal (o continua) (LP Relaxation)". Formulación del problema (P) en rojo:
$$\max c^Tx+h^Ty$$
$$\text{s.t. } Ax+Gy\le b,\; x\in\mathbb{Z}_+^n,\; y\in\mathbb{R}_+^p$$
Anotación roja manuscrita con flecha señalando las restricciones de integralidad: "La relajación lineal R_P de P se obtiene por la supresión de las restricciones de integralidad (relajación LP)".

## Slide 46
Misma cabecera. Comparación lado a lado: (P) problema entero original (x∈Z_+^n, y∈R_+^p) a la izquierda, flecha azul hacia (R_P) relajación LP a la derecha (misma función objetivo y restricciones pero x∈R_+^n en vez de Z_+^n). Etiquetas rojas "problema entero original" / "relajación LP" debajo de cada formulación.

## Slide 47
Retoma "Ejemplo de programa entero" (mismo enunciado de knapsack 2D: max x1+0.64x2, s.t. 50x1+31x2≤250, 3x1-2x2≥-4). Gráfico con retícula de puntos enteros, línea roja diagonal; recuadro "Solución de la relajación lineal (Rp)" con flecha al punto óptimo continuo (arriba); recuadro "solución de (P)" con flecha al punto óptimo entero real (abajo, en el eje X) — repite la comparación LP vs entero de la slide 41 en este contexto de relajación.

## Slide 48
Título "Relajación lineal (o continua) (LP Relaxation)". Texto/teorema: "Si F(P) es el espacio de soluciones factibles de P, entonces: F(P) ⊆ F(R_P)." (solo texto, sin gráfico).

## Slide 49
Título rojo "Límite superior de un problema P de maximización". Teorema: "Si (x*,y*) es una solución óptima de P y (x̄,ȳ) es una solución óptima de R_P, entonces: c^Tx̄+h^Tȳ ≥ c^Tx*+h^Ty*." Conclusión: "El valor óptimo de R_P es un límite superior de P."

## Slide 50
Mismo título rojo "Límite superior de un problema P de maximización". Texto: "El valor óptimo de R_P es un límite superior de P. Cuanto más pequeño sea F(R_P), el límite superior obtenido resolviendo R_p está más cerca del valor óptimo de P." (solo texto).

## Slide 51
Texto centrado: "Un mismo problema se puede formular de varias formas distintas". Subtítulo rojo manuscrito: "Una formulación puede ser mejor que otra". Sin gráficos.

## Slide 52
Sin título visible (continuación conceptual). Gráfico en el plano con retícula de puntos enteros (círculos blancos, algunos en rojo relleno formando un pentágono irregular). Se dibujan 3 polígonos superpuestos: P1 (triángulo grande, rotado), P2 (rectángulo/polígono mediano) y P3 (pentágono pequeño formado exactamente por los puntos rojos, ajustado a la envolvente de los puntos enteros factibles). Ilustra 3 formulaciones distintas (P1, P2, P3) de la misma región factible entera.

## Slide 53
Título rojo "Envolvente convexa de P". Mismo gráfico de la slide 52 (P1, P2, P3 superpuestos con puntos rojos). A la derecha: fórmula F(R_P3) ⊆ F(R_P1) y F(R_P3) ⊆ F(R_P2), con flecha azul hacia abajo señalando la conclusión: "La formulación P3 es mejor que las formulaciones P1 y P2." y "P3 es la envolvente convexa de P".

## Slide 54
Mismo título y gráfico (P1, P2, P3). Texto a la derecha: "La envolvente convexa P3 es la formulación ideal de P"; "Un punto extremo (y entero) de P3 es solución óptima de P"; en negrita: "Si resolvemos la relajación lineal de P3 obtenemos una solución óptima entera de P".

## Slide 55
Mismo gráfico (P1, P2, P3, puntos rojos). Pregunta a la derecha: "¿Podríamos determinar la envolvente convexa de P y resolver su relajación lineal para tener la solución óptima del problema entero?" — plantea la idea antes de refutarla.

## Slide 56
Título rojo "¿Porqué no determinar la envolvente convexa de P y resolver su relajación lineal?". Texto: "Identificar todas las restricciones que configuren la envolvente convexa de P es un problema generalmente mucho más difícil que el mismo problema P" — explica por qué el enfoque de la envolvente convexa no es práctico, motivando Branch & Bound.

## Slide 57
Portada de sección: "Algoritmo de Branch & Bound" con subtítulo rojo manuscrito "Divide y vencerás". Sin más contenido.

## Slide 58
Título "Idea general". Bullets: "Queremos resolver z* = max{cx | x∈X}"; "Particionamos X en {X1,X2}"; "Entonces z* = max{z1*, z2*}". Diagrama: hexágono dividido en dos regiones (X1 amarilla, X2 verde) por una línea diagonal, con etiquetas z1* y z2* marcando cada subregión mediante líneas discontinuas — ilustra la partición del espacio de soluciones.

## Slide 59
Mismo título "Idea general" y mismo diagrama (ahora solo la región X1 amarilla se muestra completa, X2 removida/oculta). Bullets adicionales: "Si z1* > z2* es inútil explorar X2"; "No hay solución óptima en X2." Fórmula en el diagrama: z1* > z2*.

## Slide 60
Mismo título y diagrama (X1 amarilla). Bullets iguales a la slide 59 más uno nuevo: "¿Cómo saber que es inútil explorar X2 sin calcular z2*?" — plantea la necesidad de un límite superior (bounding) sin resolver X2 directamente.

## Slide 61
Mismo título y diagrama de las slides 59-60 (X1 amarilla, X2 verde, z1*>z2*). Bullets iguales más uno nuevo final: "Podemos determinar un límite superior de z2*. ¿Cómo?" — cierra la idea de bounding antes de pasar al ejemplo gráfico con B&B sobre el ejemplo de knapsack.

## Slide 62
Sin título. Gráfico X1-X2 con región factible verde (polígono irregular), retícula de puntos enteros (amarillos dentro, blancos fuera). Línea roja diagonal "función objetivo" con flecha indicando dirección de crecimiento (hacia arriba-derecha). Introduce el ejemplo gráfico de Branch & Bound sobre el problema entero de las slides 1/40/47.

## Slide 63
Mismo gráfico. Anotaciones rojas: "ramificación sobre la variable x2" (flecha a línea discontinua horizontal en x2≈2.6) y "solución continua" (flecha al punto rojo, intersección de la línea objetivo con el borde de la región, arriba a la derecha) — muestra el primer paso de ramificación de B&B sobre x2.

## Slide 64
Región dividida en dos subregiones: Y1 (triángulo verde oscuro, arriba, x2≥3) e Y2 (pentágono verde claro/oscuro, abajo, x2≤2), separadas por la línea discontinua horizontal. Anotaciones: "ramificación sobre la variable x2" y "resolución del problema relajado sobre Y2" (apunta a la región Y2). Punto rojo en el borde de Y1/línea objetivo.

## Slide 65
Mismo diagrama con Y1/Y2. Anotación "solución continua" ahora apunta a un nuevo punto rojo (intersección de la línea objetivo con el borde de Y2, en x2=2) — resultado de resolver la relajación LP sobre Y2.

## Slide 66
Mismo diagrama Y1/Y2. Nueva anotación roja "ramificación sobre la variable x1" con flecha a una línea discontinua vertical (en x1≈2.6) — segunda ramificación, ahora sobre x1 dentro de la región relajada.

## Slide 67
Mismo diagrama, ahora con una subregión rectangular verde oscuro más pequeña delimitada además por la línea discontinua vertical (x1≤2), y región clara (x1≥3, vacía/descartada) a la derecha. Punto rojo en la esquina (2,2) — solución continua tras ramificar sobre x1.

## Slide 68
Texto rojo "ahora tenemos que averiguar si una mejor solución entera existe sobre Y1" (a la izquierda). Diagrama: mismo Y1 (triángulo)/Y2 (rectángulo verde), con un punto azul relleno en (2,2) marcado como "primera solución entera" (anotación roja con flecha) — se ha encontrado la primera solución entera factible.

## Slide 69
Mismo diagrama y punto azul (2,2). Anotación "solución continua" ahora señala el punto rojo en la parte superior (intersección con Y1, arriba, cerca de x2=3) — se continúa evaluando la rama Y1 para ver si mejora la solución entera encontrada.

## Slide 70
Mismo diagrama. Nueva anotación roja "ramificación sobre la variable x1" con flecha a línea discontinua vertical en la parte superior (sobre Y1) — se ramifica nuevamente sobre x1 dentro de la subregión Y1 para verificar si existe mejor solución entera.

## Slide 71
Mismo diagrama Y1(triángulo)/Y2(rectángulo verde), punto azul en (2,2). Anotaciones: "solución continua" (apunta al punto rojo arriba, en la intersección con Y1 tras la ramificación x1) y "ramificación sobre la variable x1" (línea discontinua vertical arriba); a la izquierda, texto rojo "el límite superior no permite podar Y1" — el límite superior de Y1 sigue siendo mejor que la solución entera actual, por lo que no se poda.

## Slide 72
Mismo diagrama. Punto azul ahora también en (1,3) marcado "segunda solución entera" (anotación roja con flecha) — nueva solución entera encontrada al explorar Y1. Texto izquierdo: "solución sobre Y2 mejor que solución sobre Y1 (solo un poquito…)" — compara el valor de la 2ª solución entera (Y1) con la 1ª (Y2), casi empatadas.

## Slide 73
Título "Problema original X". Formulación:
$$\max -x_1+2x_2$$
$$\text{s.t. } -4x_1+6x_2\le 9,\; x_1+x_2\le 4,\; (x_1,x_2)\in\mathbb{Z}_+^2$$
Nota: función objetivo distinta a la de las slides 1-72 (nuevo ejemplo numérico para desarrollar el algoritmo Branch & Bound paso a paso con tablas).

## Slide 74
Título "Inicialización". Misma formulación (X). A la derecha: "Z*=+∞"; "Subproblemas activos: X" — estado inicial del algoritmo B&B antes de resolver nada.

## Slide 75
Título "Resolución de la relajación LP de X". Misma formulación. A la derecha: Z*=+∞, Subproblemas activos: recuadro verde "X". Abajo: "Solución LP: (1.5, 2.5)"; "Z*(LP(X)): 3.5" — primer bound superior calculado.

## Slide 76
Título "Ramificación de X sobre x2". Misma formulación (X). A la derecha: "Dos nuevos subproblemas: x2 ≤ ⌊x2*⌋=2 (Y1); x2 ≥ ⌈x2*⌉=3 (Y2)". Abajo: Solución LP: (1.5,2.5), Z*(LP(X)):3.5 — se ramifica sobre x2.

## Slide 77
Título "Resolución de la relajación LP de Y1". Formulación (Y1) añade x2≤2. A la derecha: Z*=+∞; Subproblemas activos (recuadro amarillo): X, Y1, Y2. Abajo: "Solución LP: (0.75, 2.0)"; "Z*(LP(Y1)): 3.25".

## Slide 78
Título "Resolución de la relajación LP de Y2". Formulación (Y2) añade x2≥3. A la derecha: Z*=+∞; Subproblemas activos: X (amarillo), Y1 (amarillo), Y2 (gris, indicando resuelto/descartado). Abajo: "Solución LP: No factible" — Y2 se elimina por infactibilidad.

## Slide 79
Título "Ramificación de Y1 sobre x1". Formulación (Y1) con x2≤2. A la derecha: "Dos nuevos subproblemas: x1≤⌊x1*⌋=0 (Y1,1); x1≥⌈x1*⌉=1 (Y1,2)". Abajo: Solución LP: (0.75,2.0), Z*(LP(Y1)):3.25.

## Slide 80
Título "Resolución de la relajación LP de Y1,1". Formulación (Y1,1) añade x1≤0. A la derecha: Z*=+∞; Subproblemas activos (recuadro amarillo): X, Y1, gris: Y2, amarillo: Y1,1, Y1,2. Abajo: "Solución LP: (0, 1.5)"; "Z*(LP(Y1,1)): 3.0".

## Slide 81
Título "Resolución de la relajación LP de Y1,2". Formulación (Y1,2) añade x1≥1. A la derecha: Z*=3.0 (ya hay solución entera); Subproblemas activos (recuadro amarillo): X, Y1, gris Y2, amarillo Y1,1, gris Y1,2. Abajo: "Solución LP: (1.0, 2.0)"; "Z*(LP(Y1,2)): 3.0".

## Slide 82
Título "Eliminación de Y1,1". Misma formulación (Y1,1). Anotación roja manuscrita: "Relajación Z*(LP(Y1,1)) no mejor que Z*" con flechas señalando Z*=3.0 y la solución LP (0,1.5), Z*(LP(Y1,1))=3.0. Subproblemas activos: X, Y1 (amarillos), Y2/Y1,1/Y1,2 (grises) — Y1,1 se elimina por bounding (no mejora Z*).

## Slide 83
Título "Eliminación de Y1". Texto: "Mejor solución entera de Y1 = 3.0". A la derecha: Z*=3.0; Subproblemas activos: X (amarillo), Y1/Y2/Y1,1/Y1,2 (todos grises, ya resueltos/eliminados) — se cierra la rama Y1.

## Slide 84
Título "Eliminación de X". Texto: "Mejor solución entera de X = 3.0". A la derecha: Z*=3.0; Subproblemas activos: todos grises (X, Y1, Y2, Y1,1, Y1,2) — el algoritmo termina, la solución óptima entera del problema X es Z*=3.0.

## Slide 85
Título "Enumeración implícita". Definición formal: "Para resolver z*=max{cx|x∈X}: particionamos el espacio factible X en {Y1,...,Yn}; para cada parte Yi calculamos un límite superior z*_LP(Yi) del valor óptimo z*(Yi); si z*_LP(Yi) es menor que la mejor solución ya encontrada, podamos Yi; sino, particionamos recursivamente Yi." (solo texto, resumen del método).

## Slide 86
Título "Algoritmo". Texto: "A cada paso del algoritmo, tenemos que mantener: una lista de subproblemas activos (no resueltos o no eliminados); el valor Z* de la mejor solución encontrada; el valor inicial de Z* es -∞ o cᵀx para un valor x factible conocido" (solo texto).

## Slide 87
Título "Algoritmo". Lista numerada (1-5) con el pseudocódigo completo de Branch & Bound: (1) elegir subproblema activo Yi de la lista, sino terminar; (2) resolver relajación lineal de Yi, si no factible eliminar y volver a 1; (3) si Z_LP(Yi)≤Z* eliminar Yi y volver a 1; (4) si LP(Yi) es solución entera mejor que Z*, actualizar Z*←Z_LP(Yi) y volver a 1; (5) si Z_LP(Yi) no es solución entera, resolver Yi directamente o particionar y agregar a la lista, volver a 1. Anotación roja manuscrita junto al paso 4: "hubiera sido eliminado antes si fuera una solución entera no mejor".

## Slide 88
Portada de subsección: "Estrategias de recorrido" con subtítulo "Ejemplo simplificado". Sin más contenido.

## Slide 89
Título "Breadth-First" (recuadro izquierdo). Árbol binario de búsqueda con nodos etiquetados A-Q: raíz A (60.75, solución fraccional) se ramifica en B (60.0, fraccional) y C (57.3, fraccional); B→D(55.5,fraccional)/E(57,fraccional); C→F(55.7,fraccional)/G(55.5,solución entera); D→H(55.5,fraccional)/I(55.2,fraccional); E→J(No factible)/K(55.8,solución entera); F→L(55.2,solución entera)/M(No factible); H→N(55.2,entera)/O(54.9,entera); I→P(54.9,fraccional)/Q(54.9,entera). Ilustra el árbol completo de B&B para el recorrido en anchura.

## Slide 90
Mismo árbol y título "Breadth-First" (repetición de la slide 89, sin números de orden todavía) — transición antes de mostrar la numeración.

## Slide 91
Mismo árbol "Breadth-First". Ahora cada nodo tiene un círculo de color con número indicando orden de exploración: verde = explorado/activo (A=1, B=2, C=3, D=4, E=5, F=6, G=7, J=8, K=9) y rojo = podado/descartado sin numerar (H, I, L, M, N, O, P, Q, y su continuación). Muestra el recorrido nivel por nivel (BFS): se exploran todos los nodos del nivel 1, luego nivel 2, etc.; los rojos se podan por bounding/infactibilidad sin explorarlos más.

## Slide 92
Título "Best-First". Mismo árbol base A-Q, sin números de orden aún (recién presentado el criterio).

## Slide 93
Mismo árbol "Best-First" con numeración de orden en círculos verdes/rojos: A=1, B=2, C=3, D=4, E=5, F=6, G=7, J=8, K=9 (idéntica secuencia que Breadth-First en este ejemplo simplificado, ya que en el primer nivel best-first coincide con breadth-first al tener pocos nodos con bounds similares).

## Slide 94
Título "Depth-First". Mismo árbol base, sin números de orden aún.

## Slide 95
Mismo árbol "Depth-First" con numeración de orden en círculos verdes/rojos: A=1, B=2, D=3, H=4, N=5, O=6, I=7, P(rojo, no numerado), Q(rojo), J=9, K=10, E=8, C=11, F=12, L(rojo), M(rojo), G=13 — recorre primero en profundidad una rama completa (A→B→D→H→N→O...) antes de retroceder, a diferencia de BFS/Best-First que exploran por niveles.

## Slide 96
Portada de subsección: "Otra idea: algoritmo de plano de corte" (rojo manuscrito) con subtítulo "Acercándonos a la envolvente convexa". Sin más contenido.

## Slide 97
Título "Restricción válida". Definición formal: "Se dice de una restricción πᵀx≤π0 que es válida para el programa P cuando está satisfecha por cualquier solución del espacio factible de P": C={πᵀx≤π0} válida para P ⟺ [x'∈F(P) ⟹ πᵀx'≤π0].

## Slide 98
Título "Plano de corte". Definición: "Sea P' el problema P al cual se agrega una restricción C válida para P. La restricción C es un plano de corte para P si F(R_P')⊂F(R_P)." (solo texto).

## Slide 99
Título "Corte válido". Definición: "Un plano de corte C={πᵀx≤π0} es un corte válido para x̄∈R_p si πᵀx̄>π0." (solo texto).

## Slide 100
Título "Algoritmo del plano de corte" (negro, con "plano de corte" en negrita). Sin más contenido (portada de la sección del algoritmo).

## Slide 101
Portada: "Ejemplo: Problema de la mochila". Sin más contenido.

## Slide 102
Título "Problema de la mochila". Formulación:
$$\max 8x_1+11x_2+6x_3+4x_4$$
$$\text{s.t. } 5x_1+7x_2+4x_3+3x_4\le 14,\; x_i\in\{0,1\}\;\forall i=\{1,...,4\}$$
Texto: "Averiguar que las restricciones siguientes son planos de corte:" x1+x2+x3≤2; x1+x2+x4≤2.

## Slide 103
Mismo título "Problema de la mochila". Definiciones formales: "Definición: Un conjunto C⊂{1,...,n} tal que Σ_{i∈C} wᵢ>W es una cobertura."; "Definición: Sea una cobertura C. Si para cualquier elemento j∈C el conjunto C\{j} no es una cobertura, C es una cobertura mínima."; "Proposición: Sea C una cobertura mínima, la restricción Σ_{i∈C}xᵢ≤|C|-1 es un corte válido." Anotación roja manuscrita: "Se tiene que remover cualquier elemento de C para satisfacer la restricción de capacidad".

## Slide 104
Título "Ejercicio". Texto: "Consideramos el problema de mochila siguiente:" X={x∈B⁷: 11x1+6x2+6x3+5x4+5x5+4x6+x7≤19}. Lista: "1. Identificar unas coberturas; 2. Identificar coberturas mínimas; 3. Escribir los cortes válidos correspondientes (las restricciones de corte)".

## Slide 105
Mismo enunciado del ejercicio. Ahora con la solución a la derecha: "Some cover inequalities for X are:" x1+x2+x3≤2; x1+x2+x6≤2; x1+x5+x6≤2; x3+x4+x5+x6≤3 — cuatro restricciones de corte derivadas de coberturas mínimas del problema.

## Slide 106
Título "Estrategia". Lista numerada (1-4): "1. Resolver R_P y obtener la solución continua x̄; 2. Si x̄∈Zⁿ, tenemos la solución óptima del programa entero, se termina el algoritmo; 3. Determinar un corte válido C para x̄ y P; 4. Agregar la restricción C al programa P y volver al paso 1." Anotación roja manuscrita con círculo alrededor del paso 3 y flecha: "problema de separación: paso más importante".

## Slide 107
Texto centrado (solo texto, sin título de sección visible): "Algoritmo de plano de corte cuando un problema se formula con un número exponencial de restricciones" — transición hacia el ejemplo del TSP.

## Slide 108
Portada: "Ejemplo: TSP". Sin más contenido.

## Slide 109
Título "Problema del viajante de comercio (Traveling Salesman Problem – TSP)". Diagrama: grafo completo K5 con 5 nodos numerados 1-5 (nodos 1,3 arriba; 2,4 abajo; 5 a la derecha), todas las aristas dibujadas entre cada par de nodos. Anotación roja manuscrita "Grafo" señalando el diagrama. Texto a la derecha: "Objetivo: Hallar el ciclo hamiltoniano más corto… …el tour (o un tour) de menos costo que pasa por cada nodo exactamente una vez".

## Slide 110
Continuación del grafo TSP: ahora solo se muestran resaltadas en azul las aristas de un tour específico (1-3, 3-5, 5-4, 4-2, 2-1), formando un ciclo hamiltoniano (pentágono irregular: 1→3→5→4→2→1). Texto: "Para determinar las aristas que utilizar en el tour, definimos las variables binarias xᵢⱼ: xᵢⱼ=1 si se utiliza la arista (i,j), xᵢⱼ=0 sino". Valores manuscritos rojos de ejemplo: x1,2=1; x1,3=1; x1,4=0; x1,5=0; x2,3=…

## Slide 111
Sin título de sección visible. Fórmula manuscrita roja "Costo de cada arista" con flecha a c_ij en min Σ_{ij∈E} c_ij x_ij; anotación roja "Minimizar el costo total de las aristas seleccionadas" con flecha a la fórmula completa. Debajo, grafo pequeño con nodos 1,3 (arriba), 2,4,5 (abajo/derecha) y solo 3 aristas dibujadas (1-2, 2-3, 4-5, faltando conexión con nodo 3 y 5 completa) — pregunta roja "¿Esa solución es factible? ¿Porqué?" — introduce que solo minimizar costo de aristas no garantiza un tour válido (puede dar componentes desconectados).

## Slide 112
Fórmula completa: min Σc_ij x_ij s.r. Σ_{ij∈δ(i)} x_ij=2 ∀i∈V; x_ij∈{0,1} ∀ij∈E. Anotaciones rojas: "Minimizar el costo total de las aristas seleccionadas" (flecha a la función objetivo) y "De tal manera que cada nodo tenga 2 aristas adyacentes" (flecha a la restricción de grado 2). Primer intento de formulación del TSP (solo restricción de grado, sin eliminación de subciclos).

## Slide 113
Mismo modelo. Grafo con nodos 1,2,3,4,5 y aristas resaltadas en azul formando un pentágono (ciclo válido). Anotaciones rojas "Nodo 1" y "Nodo 4" señalando esos nodos específicos, con recuadro rojo resaltando la restricción de grado. Verifica que cada nodo tenga exactamente 2 aristas en la solución.

## Slide 114
Texto en post-it rojo: "En un circuito cada nodo es de grado 2 (cada nodo tiene 2 aristas incidentes)". Debajo, pregunta: "Si cada nodo es de grado 2, ¿tenemos un circuito???" — plantea la falla lógica de la primera formulación (grado 2 no implica un único ciclo).

## Slide 115
Título "Cada nodo tiene 2 aristas incidentes, pero…". Diagrama: dos triángulos separados, nodos {1,2,3} formando un triángulo (grado 2 cada uno) y nodos {4,5,6} formando otro triángulo — cada nodo tiene grado 2 pero la solución consta de dos subciclos separados en vez de un único tour de 6 nodos. Anotación roja "No es una solución factible" señalando el grafo. Etiqueta "Subciclos".

## Slide 116
Título "Eliminar las soluciones con subciclos: añadir nuevas restricciones" (rojo manuscrito para la segunda parte). Mismo diagrama de dos triángulos {1,2,3} y {4,5,6}.

## Slide 117
Título "Eliminar los subciclos es impedir cualquier ciclo para cada subconjunto de puntos del grafo". A la derecha, ejemplo con el subconjunto {1,2,3} (triángulo) resaltado con un óvalo rojo. Fórmula: x1,2+x1,3+x2,3=3 → flecha azul hacia abajo → "añadir la restricción" x1,2+x1,3+x2,3<3. Anotación roja: "Ejemplo, para el subconjunto {1,2,3} rechazamos cada solución que contiene 3 o más aristas".

## Slide 118
Mismo esquema, ahora con el subconjunto {4,5,6} resaltado con óvalo rojo. Fórmula: x4,5+x4,6+x5,6=3 → "añadir la restricción" x4,5+x4,6+x5,6<3. Anotación: "Ejemplo, para el subconjunto {4,5,6} rechazamos cada solución que contiene 3 o más aristas adyacentes".

## Slide 119
Título "Segundo intento: Costo de cada arista". Formulación completa con restricción de eliminación de subciclos añadida:
$$\min \sum_{ij\in E} c_{ij}x_{ij}$$
$$\text{s.r. } \sum_{ij\in\delta(i)} x_{ij}=2\;\forall i\in V,\quad \sum_{ij\in E(S)} x_{ij}\le |S|-1\;\forall S\subset V,\quad x_{ij}\in\{0,1\}\;\forall ij\in E$$
Anotaciones rojas: "Minimizar el costo total de las aristas seleccionadas"; "De tal manera que cada nodo tenga 2 aristas adyacentes"; "Restricciones de eliminación de subciclos". Pequeño diagrama de los dos triángulos {1,2,3}/{4,5,6} abajo a la izquierda.

## Slide 120
Título "Problema del viajante de comercio (Traveling Salesman Problem – TSP)". Formulación completa alternativa (formulación clásica de asignación con eliminación implícita, sin subtour aún):
$$\min \sum_{i=1}^n\sum_{j=1}^n c_{ij}x_{ij}$$
$$\text{s.t. } \sum_{j:j\ne i} x_{ij}=1\;\forall i,\quad \sum_{i:i\ne j} x_{ij}=1\;\forall j,\quad x_{ij}\in\{0,1\}\;\forall(i,j)$$
Recapitula la formulación básica de asignación del TSP antes de agregar restricciones de eliminación de subciclos.

## Slide 121
Sin título de sección. Formulación completa del "Segundo intento" (min Σc_ij x_ij, restricción de grado=2, restricción de eliminación de subciclos Σx_ij≤|S|-1, x_ij binaria). Preguntas rojas manuscritas: "¿Cuántas variables?" (flecha a x_ij en la función objetivo), "¿Cuántas restricciones de grado?" (flecha a la restricción de grado), "¿Cuántas restricciones de eliminación de subciclos?" (flecha a la restricción de subciclos) — plantea las 3 preguntas antes de responderlas.

## Slide 122
Misma formulación. Respuesta roja a la derecha: "n(n-1)/2 variables" — responde solo la primera pregunta (número de variables xᵢⱼ, combinaciones de pares de nodos).

## Slide 123
Misma formulación. Respuestas rojas: "n(n-1)/2 variables" y "n restricciones de grado" (una por cada nodo i∈V).

## Slide 124
Misma formulación. Respuestas rojas completas: "n(n-1)/2 variables"; "n restricciones de grado"; "2^(n-1) restricciones de eliminación de subciclos" — cierra las 3 preguntas, mostrando que las restricciones de subciclos crecen exponencialmente con n (2^(n-1) subconjuntos posibles de V).

## Slide 125
Misma formulación (min Σc_ij x_ij, restricciones de grado y subciclos). A la derecha: "Con n=100:" seguido de "4950 variables"; "100 restricciones de grado"; "~6.338×10²⁹ restricciones de eliminación de subciclos" — instancia numérica que muestra la explosión combinatoria real de las restricciones de subciclos incluso para un TSP de tamaño moderado (n=100).

## Slide 126
Misma formulación. A la derecha: "Con n=267:" "~1.1857×10⁸⁰ restricciones de eliminación de subciclos"; comparación: "Número estimado de átomos en la parte visible del universo: 10⁸⁰" — cierre dramático del capítulo mostrando que el número de restricciones de subciclos de un TSP de 267 nodos es comparable al número de átomos del universo observable, justificando la necesidad de los algoritmos de plano de corte y branch & bound vistos en el capítulo (no se puede enumerar todas las restricciones de antemano).
