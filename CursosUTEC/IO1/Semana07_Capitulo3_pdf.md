---
curso: IO1
titulo: Semana07-Capitulo3
slides: 81
fuente: Semana07-Capitulo3.pdf
---

## Slide 1

Portada del capítulo. Título "Investigación de operaciones I", subtítulo "Capítulo 3: Métodos heurísticos". Logo UTEC (decorativa).

## Slide 2

**Objetivo**
- Resolver problemas complejos de decisión con algorítmos heurísticos eficientes.
- En particular: resolver problemas combinatorios.

## Slide 3

**Métodos heurísticos**
- El término viene de la palabra eurisko (εὑρίσκω): encontrar, descubrir.
- Son reglas prácticas de toma de decisión.
- Maneras prácticas de encontrar una solución a un problema.
- Alternativas prácticas a las técnicas matemáticas formales.

## Slide 4

**Porqué utilizar métodos heurísticos**
- Generalmente para resolver instancias grandes de problemas computacionalmente dificiles.
- Cuando obtener una solución exacta (óptima) necesitaría un tiempo de computación excesivo.
- Generalmente no se usa para resolver problemas polinomiales o pequeñas instancias de un problema difícil.

## Slide 5

Slide de separación de sección: "Clases de problemas". Imagen decorativa de fondo: un bloque grande de texto binario (0s y 1s) formando visualmente una silueta, con el título "TRAVELLING SALESMAN — A CEREBRAL THRILLER. COMING SOON. travellingsalesmanmovie.com @travsalemovie" (promoción de una película, imagen decorativa/artística, sin contenido técnico relevante).

## Slide 6

**Clase P**

Problemas de clase P: problemas para los cuales se conoce un algoritmo capaz de encontrar una solución óptima en un tiempo que es función polinomial del tamaño de la instancia. Si $n$ representa el tamaño de la instancia, se dice que el algoritmo es de orden $\mathcal{O}(n^c)$.

## Slide 7

**Clase P**
- Ejemplo: Para el problema del camino más corto se conoce un algoritmo (Dijkstra) que necesita un tiempo del orden de $V^2$ (se escribe: $\mathcal{O}(V^2)$), donde $V$ es el número de vértices (en este caso consideramos que $V$ representa el tamaño de la instancia). También existe un algoritmo en tiempo $VE$ (escrito: $\mathcal{O}(V \cdot E)$) donde $V$ es el número de vértices y $E$ el número de arcos (en este caso consideramos que $V$ y $E$ representan juntos el tamaño de la instancia).
- Otros problemas de clase P: ordenar una lista de elementos, buscar un elemento en una lista, problema del árbol mínimo de recubrimiento, saber si un número es primo.

## Slide 8

**Clase NP**

Problemas de clase NP (*nondeterministic polynomial time*): problemas para los cuales existe un algoritmo rápido (en tiempo polinomial) para averiguar que una solución candidata (un certificado) es realmente una solución del problema.
- Ejemplo: El problema que consiste en saber si, para un conjunto de enteros positivos o negativos, existe un subconjunto de sumatoria nula. Encontrar una solución es difícil (tenemos que generar todos los subconjuntos posibles), pero saber si una solución es factible es fácil.

## Slide 9

**Clase NP-difícil**

Problemas de clase NP-difícil (*NP-Hard*): Problemas al menos tan difícil como el problema más difícil de la clase NP (problema NP-completo).
- Ejemplos: Problema del viajante de comercio, problema 3-SAT, problema de la mochila, problema de bin-packing.

Para grandes instancias de esos problemas, es importante tener métodos para encontrar una "buena solución" en lugar de una solución óptima: métodos heurísticos.

## Slide 10

**Clase NP-difícil**

Diagrama hecho a mano (estilo boceto naranja/azul): una línea horizontal con flecha ("dificultad" creciente hacia la derecha). Sobre la línea se marcan dos puntos de corte. El primer segmento (izquierda) está anotado como "P" (llave superior) y también incluido dentro de un rango mayor "NP" (llave inferior que cubre P y un tramo adicional). En el punto donde termina NP se señala con una flecha "NP-Completo". El tramo final (a la derecha del segundo corte) está anotado como "NP-difícil" (con puntos suspensivos indicando que sigue creciendo). Ilustra la relación de contención: P ⊆ NP, con NP-Completo en la frontera de NP, y NP-difícil como región de igual o mayor dificultad que NP-Completo.

## Slide 11

Slide de separación de sección: "Espacio de búsqueda". Solo título, sin contenido adicional.

## Slide 12

**Métodos heurísticos y metaheurísticos**
- Una búsqueda exaústiva es frecuentemente la única manera de encontrar una solución óptima.
- Pero el espacio de búsqueda es frecuentemente demasiado grande para permitirla.

## Slide 13

**Métodos heurísticos y metaheurísticos**
- Necesitamos métodos imperfectos pero "inteligentes" de búsqueda:
  - Métodos **heurísticos**: método de exploración que explota aspectos específicos de un problema en particular.
  - Métodos **metaheurísticos**: métodos genericos de exploración que se pueden aplicar a muchos problemas distintos. Ejemplos: recocido simulado, tabu search, algoritmos evolucionarios.
- Esos términos son frecuentemente utilizados sin distinción en la literatura.

## Slide 14

**Búsqueda local: algoritmo generico**
1. Definir un espacio de búsqueda $S$ y una función objetivo $f: S \to \mathbb{R}$.
2. Definir una vecindad $V(x)$: la vecindad de una solución es el conjunto de soluciones obtenidas por una **transformación** (o **movimiento**), o por un conjunto de transformaciones, de cualquier solución $x \in S$.
3. Definir un operador de selección $U$ para seleccionar una solución de la vecindad $V(x)$ de la solución actual $x$. Seleccionar la solución siguiente $U(V(x))$.
4. A partir de una solución inicial $x_0$:

$$x_0 \to x_1 = U(V(x_0)) \to x_2 = U(V(x_1)) \to \ldots$$

## Slide 15

Slide de separación de sección: "Ejemplos con el problema de la mochila". Solo título.

## Slide 16

**Ejemplo de espacio de búsqueda y representación de una solución**
- Consideramos el problema de la mochila con 3 objetos.
- Podemos encodificar una solución como una serie de 3 bits (3 variables binarias de decisión): por ejemplo $000, 001$ o $101$.

Diagrama: un cubo (hipercubo binario de 3 bits) dibujado en perspectiva. Los 8 vértices están etiquetados con las 8 combinaciones de 3 bits: 000, 001, 010, 011, 100, 101, 110, 111. Las aristas del cubo conectan nodos que difieren en un solo bit, representando el espacio de búsqueda completo del problema de mochila de 3 objetos.

## Slide 17

**Ejemplo de vecindad**

Mismo diagrama de cubo binario que en la slide 16, con los 8 vértices (000 a 111) conectados por aristas.

Texto: Si definimos la vecindad de una solución por la transformación "se cambia el valor de un bit": la vecindad de la solución 000 es el conjunto de soluciones (vecinos) $\{001, 010, 100\}$, y la vecindad de la solución 101 es $\{001, 111, 100\}$.

## Slide 18

**Ejemplos de operador de selección de la solución siguiente**
- Elegir aleatoriamente una solución de la vecindad.
- Elegir la mejor solución de la vecindad (*best improvement*).
- Elegir la primera solución de la vecindad que mejora la solución actual (*first improvement*).

## Slide 19

Slide de separación de sección: "Ejemplos con el problema del viajante de comercio (TSP)". Solo título.

## Slide 20

**Ejemplo de espacio de búsqueda y representación de una solución**
- Consideramos un conjunto de ciudades $\{0, 1, 2, \ldots, 9\}$.
- Podemos encodificar una solución como una permutación de ciudades: por ejemplo $(0,1,2,3,4,5,6,7,8,9)$.

## Slide 21

**Ejemplos de vecindades: 2-Exchange**
- Intercambiar la posición de dos ciudades.
- Por ejemplo: intercambiando las ciudades 2 y 6, obtenemos el vecino $(0,1,6,3,4,5,2,7,8,9)$.

Par de diagramas TSP lado a lado (dos recuadros con nodos numerados 0-9 conectados por flechas formando un tour cerrado):
- Izquierda: tour original con longitud L=4.77807. Se resaltan en azul las aristas que involucran a los nodos 2 y 6 (aristas 1→6, 6→2/3, 4→5, etc., cruzándose en el centro del recuadro).
- Derecha: tour resultante tras el intercambio 2↔6, con longitud L=4.25869 (menor, mejora). Las aristas modificadas se resaltan en rojo: ahora 1→6 pasa a 6→3 y luego a 2, sin el cruce anterior.

## Slide 22

**Ejemplos de vecindades: 2-OPT**
- Cortar el tour en 2 y reconectar los caminos con la forma alternativa.
- Lo mismo que tomar una fracción de la secuencia e invertirla.
- Por ejemplo: invirtiendo la secuencia desde 2 hasta 6, obtenemos el vecino $(0,1,6,5,4,3,2,7,8,9)$.

Par de diagramas TSP lado a lado similares a la slide 21:
- Izquierda: tour original, L=4.77807, con las aristas 1→7 y 6→2 resaltadas en azul (cruzándose).
- Derecha: tour tras invertir el segmento 2-6, L=4.29529 (menor), con la arista 7→2 resaltada en rojo, ya sin cruce.

## Slide 23

**Ejemplos de vecindades: 2-OPT** (continuación, otro ejemplo)

Par de diagramas TSP lado a lado con 10 nodos (0,1,2,3,4,5,6,7,8,9) en disposición circular/irregular:
- Izquierda: tour con cruce entre las aristas 3→9 y 8→4 (resaltadas en azul), L=2.38194.
- Derecha: tour corregido tras 2-OPT, sin cruce, con las aristas 3→8 y 4→9 resaltadas en rojo, L=2.09523 (mejora, tour más corto).

## Slide 24

**Ejemplos de vecindades: 2-OPT**

¿Cuál es la manera más rápida de evaluar un vecino con la vecindad 2-OPT? (pregunta abierta para reflexión, sin respuesta desarrollada en la slide).

## Slide 25

**Ejemplos de operador de selección del tour siguiente**
- Elegir aleatoriamente un tour vecino.
- Elegir el mejor tour de la vecindad (*best improvement*).
- Elegir el primer tour de la vecindad que mejora el tour actual (*first improvement*).

## Slide 26

**Vecindad y tiempo de computación**
- Una vecindad grande permite la exploración de más soluciones, pero puede necesitar más tiempo de computación.
- El tiempo de computación depende de la manera de encodificar las soluciones, de la vecindad y del operador de selección.
- Hay siempre vecindades más económicas en tiempo de computación que otras.

## Slide 27

**Hill climbing**

La estrategia que consiste a seleccionar cada vez una solución mejor que la solución actual se llama: Hill Climbing.

Pseudocódigo para un problema de maximización:
```
x ← alguna solución inicial
REPEAT
    x' ← selectFrom(V(x))
    IF f(x') > f(x) THEN
        x ← x'
UNTIL f(x') <= f(x)
RETURN x
```

## Slide 28

**Steepest Hill climbing**

La estrategia que consiste a seleccionar cada vez la mejor solución de la vecindad se llama: Steepest Ascent Hill Climbing.

Pseudocódigo para un problema de maximización:
```
x ← alguna solución inicial
REPEAT
    x' ← best(V(x))
    IF f(x') > f(x) THEN
        x ← x'
UNTIL f(x') <= f(x)
RETURN x
```

(Diferencia clave respecto a la slide 27: aquí `x' ← best(V(x))` en vez de `selectFrom(V(x))` — se toma el mejor vecino en cada iteración, no uno arbitrario.)

## Slide 29

**Límite de las estrategias de Hill climbing y de Steepest Hill Climbing**

El problema de esas estrategias es que se terminan con un óptimo local, es decir: una solución que no tiene mejor vecino.

Gráfico de una función $f()$ en el eje vertical vs. una variable en el eje horizontal, mostrando una curva con dos picos: un pico alto a la izquierda (el óptimo global, más alto) y un pico más bajo a la derecha (óptimo local). Una trayectoria de puntos con flechas asciende por la pendiente del pico de la derecha (el más bajo) hasta detenerse en su cima, con un globo de diálogo tipo cómic que dice "I'm at the top of the world!" — ilustrando humorísticamente cómo el algoritmo Hill Climbing queda atrapado en el óptimo local sin darse cuenta de que existe un óptimo global mejor a la izquierda.

## Slide 30

**Óptimo local**
- En un problema de maximización, una solución $x$ es un máximo local ssi (si y solo si):
$$f(x') \le f(x), \quad \forall x' \in V(x)$$
- En un problema de minimización, una solución $x$ es un mínimo local ssi (si y solo si):
$$f(x') \ge f(x), \quad \forall x' \in V(x)$$
- Un óptimo local se refiere siempre a una vecindad específica: un óptimo local utilizando una vecindad podría no ser un óptimo local con otra vecindad.

## Slide 31

**Ideas para escapar un óptimo local**
- Probabilistic Hill Climbing
- Hill-Climbing with Random Restarts
- Iterated Local Search
- Variable Neighborhood Search
- Etc.

## Slide 32

**Probabilistic Hill Climbing**

Para evitar la trampa del óptimo local, podemos introducir aleatoriedad en el algoritmo para aceptar soluciones peores que la solución actual con una cierta probabilidad.

## Slide 33

**Hill-Climbing with Random Restarts**

Repetir el algoritmo de Hill Climbing o Steepest Ascent Hill Climbing, tomando siempre una nueva solución inicial aleatoria.

## Slide 34

**Iterated Local Search**
- Similar al algoritmo de *Hill-Climbing with Random Restarts*, pero más "inteligente".
- En lugar de generar aleaoriamente una solución inicial, busquamos una solución fuera del óptima local, pero "no tan lejos".
- Se puede hacer por ejemplo con la **perturbación** del óptimo local.

## Slide 35

**Variable Neighborhood Search**
- Utilizar **varias vecindades** (por ejemplo $V_1, V_2, \ldots, V_n$).
- Empezar con la vecindad $V_1$.
- Cada vez que llegamos a un óptimo local con una vecindad $V_i$, pasamos a la vecindad $V_{i+1}$.
- Cada vez que salimos de un óptimo local, volvemos a la vecindad $V_1$.
- El algoritmo termina cuando no se puede salir del óptimo local utilizando la vecindad $V_n$.

## Slide 36

**Intensificación (Explotación) vs. Diversificación (Exploración)**
- En **fase de intensificación**, la búsqueda se limita a la exploración de vecinos de una solución ya prometedora.
- En **fase de diversificación**, intentamos visitar otras regiones del espacio de búsqueda.
- Con mucha intensificación: riesgo de quedarse en los mismos locales óptimos.
- Con mucha diversificación: riesgo de visita demasiado aleatoria del espacio de soluciones.

## Slide 37

**Soluciones iniciales**

Necesitamos un algoritmo para generar una solución inicial: un **método de construcción**.

## Slide 38

**Soluciones iniciales para el problema de Bin-Packing**

Tenemos contenedores de capacidad $W$ para empaquetar $N$ objetos. Cada objeto $i \in \{1, \ldots, N\}$ tiene un peso $w_i$.

**Objetivo:** Minimizar el número de contenedores para empaquetar todos los objetos.

## Slide 39

**Soluciones iniciales para el problema de Bin-Packing**

3 métodos de construcción:
- Next-Fit
- First-Fit
- First-Fit Decreasing

## Slide 40

**Soluciones iniciales para el problema de Bin-Packing — Next-Fit**
1. Abrir un primer contenedor (contenedor actual)
2. Colocar los objetos uno por uno en el contenedor actual hasta su capacidad.
3. Cuando no se puede colocar un objeto, cerrar el contenedor actual y abrir un nuevo contenedor.
4. Regresar en 2.

## Slide 41

**Soluciones iniciales para el problema de Bin-Packing — Next-Fit**

**Garantía:** Si el valor óptimo es $f(x^*)$, la solución generada $\hat{x}$ con el algoritmo Next-Fit es tal que:
$$f(\hat{x}) \le 2f(x^*) - 1$$

## Slide 42

**Soluciones iniciales para el problema de Bin-Packing — First-Fit**
1. Abrir un primer contenedor (contenedor actual)
2. Colocar los objetos uno por uno en el primero de los contenedores abiertos que tienen la capacidad suficiente.
3. Cuando no se puede colocar un objeto, abrir un nuevo contenedor.
4. Regresar en 2.

## Slide 43

**Soluciones iniciales para el problema de Bin-Packing — First-Fit**

**Garantía:** Si el valor óptimo es $f(x^*)$, la solución generada $\hat{x}$ con el algoritmo First-Fit es tal que:
$$f(\hat{x}) \le \lceil (17/10) f(x^*) \rceil$$

## Slide 44

**Soluciones iniciales para el problema de Bin-Packing — First-Fit Decreasing**
1. Ordenar los objetos en orden decreciente de pesos.
2. Aplicar el algoritmo First-Fit

## Slide 45

**Soluciones iniciales para el problema de Bin-Packing — First-Fit Decreasing**

**Garantía:** Si el valor óptimo es $f(x^*)$, la solución generada $\hat{x}$ con el algoritmo First-Fit Decreasing es tal que:
$$f(\hat{x}) \le \frac{3}{2} f(x^*)$$

## Slide 46

**Soluciones iniciales para el problema de TSP**

Diagrama: un recuadro con 12 puntos naranjas dispersos sin conectar (nube de puntos representando ciudades sin ruta definida aún).

Pregunta: ¿Qué método simple podríamos utilizar para construir una solución inicial?

## Slide 47

**Soluciones iniciales para el problema de TSP — Nearest neighbor**
1. Seleccionar aleatoriamente un punto inicial
2. Seleccionar el punto más cercano del último punto agregado (punto actual).
3. Volver en 2 hasta obtener un ciclo visitando todos los puntos.

## Slide 48

**Soluciones iniciales para el problema de TSP**

Diagrama: tour construido con el método Nearest Neighbor sobre 10 puntos. Un punto de partida (verde) en la parte superior derecha conecta con flechas dirigidas a los demás puntos (naranjas) formando un ciclo cerrado que recorre todos los nodos y regresa al punto verde inicial. Ilustra el resultado del algoritmo de la slide 47 aplicado al conjunto de puntos de la slide 46.

## Slide 49

**Soluciones iniciales para el problema de TSP — Farthest insertion**
1. Seleccionar los dos puntos más alejados y conformar un ciclo (ida y vuelta) entre esos dos puntos.
2. Seleccionar el punto $k$ más alejado de cualquier punto ya visitado.
3. Seleccionar la arista ("ruta entre dos puntos") de la solución parcial en la cual agregar el punto $k$ es más económico.
4. Volver en 2 hasta obtener un ciclo visitando todos los puntos.

## Slide 50

**Soluciones iniciales para el problema de TSP**

Diagrama: recuadro con los mismos 12 puntos naranjas dispersos sin conectar (idéntico al de la slide 46), presumiblemente como base para ilustrar el método Farthest insertion (sin tour dibujado aún en esta slide).

## Slide 51

**Soluciones iniciales para el problema de TSP — Cheapest insertion**
1. Seleccionar aleatoriamente un punto $i$ inicial.
2. Seleccionar el punto $j$ más cercano al punto $i$ y conformar un ciclo.
3. Seleccionar una arista $(i,j)$ del subciclo y un punto $k$ no visitado tal que la inserción del punto $k$ sea la inserción más económica.
4. Volver en 3 hasta obtener un ciclo visitando todos los puntos.

## Slide 52

**Soluciones iniciales para el problema de TSP**

Diagrama: recuadro con los mismos 12 puntos naranjas dispersos sin conectar (idéntico a las slides 46 y 50), como base ilustrativa para el método Cheapest insertion (sin tour dibujado en esta slide).

## Slide 53

**Soluciones iniciales para el problema de TSP**

Otros métodos:
- **Convex hull** insertion
- **Greatest angle** insertion
- etc.

## Slide 54

**Vecindades conexas**

Una vecindad $V$ es conexa si desde **cualquier** solución $x$ existe un camino hasta **cualquier** otra solución en un grafo donde cada nodo representa una solución y cada arco representa la transición desde una solución hasta otra solución.

En otras palabras, $V$ es una vecindad conexa si para **cualquier par de soluciones** $(x, x')$ existe una secuencia de movimientos tal que:
$$x = x_0 \to x_1 \in V(x_0) \to x_2 \in V(x_1) \to \cdots \to x_n \in V(x_{n-1}) = x'$$

## Slide 55

**Vecindades conexas con el problema de la mochila**

Dar dos ejemplos de vecindades: una **vecindad no conexa** y una **vecindad conexa**. (Pregunta abierta para reflexión, sin desarrollo adicional en la slide.)

## Slide 56

Slide de separación de sección: "Métodos metaheurísticos". Solo título.

## Slide 57

**Métodos métaheurísticos presentados:**
- **Recocido simulado** (método de **búsqueda local**)
- **Tabu Search** (método de **búsqueda local**)
- **GRASP** (método **greedy** de construcción aleatorizado)

## Slide 58

Slide de separación de subsección: "Métodos metaheurísticos — Recocido simulado". Solo título y subtítulo.

## Slide 59

**Recocido simulado**

Imagen: cuatro paneles (a, b, c, d) mostrando trayectorias de búsqueda del algoritmo de recocido simulado sobre un espacio 2D (ejes de 0.0 a 1.0), típicamente aplicado a un problema tipo TSP/layout de circuitos. El panel (a) muestra una trayectoria muy errática con muchos cruces y zigzags (alta temperatura, exploración amplia/aleatoria). Los paneles (b) y (c) muestran trayectorias progresivamente menos caóticas, con menos cruces. El panel (d) muestra una trayectoria mucho más ordenada y suave, con líneas que forman contornos más regulares (baja temperatura, solución refinada) — ilustra la evolución del algoritmo a medida que la temperatura disminuye, pasando de exploración aleatoria a convergencia hacia una buena solución.

Referencia bibliográfica: Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P., Optimization by Simulated Annealing. *Science*, 220(4598):671–680, 1983.

## Slide 60

**Recocido simulado**
- Basado en el método de Metropolis-Hastings donde un movimiento se acepta siempre cuando mejora el valor objetivo, o con una cierta probabilidad sino.
- La probabilidad crece con la calidad del movimiento.
- La probabilidad depende de una **temperatura** $t$.

## Slide 61

**Recocido simulado**
- En un problema de **minimización**, si $s$ es la solución actual y $n$ un vecino de $s$, $\Delta$ es la diferencia entre el valor objetivo $f(n)$ del vecino y el valor objetivo $f(s)$ de la solución actual: $\Delta = f(n) - f(s)$
- Un movimiento que malogra la solución actual será aceptado con probabilidad: $exp(\frac{-\Delta}{t})$.

## Slide 62

**Recocido simulado**

$$\text{Prob(aceptacion)} = \begin{cases} 1 & \text{if } \Delta \le 0 \\ e^{-\Delta/t} & \text{if } \Delta > 0 \end{cases}$$

- ¿Qué pasa cuando $\Delta \to +\infty$?
- ¿Qué pasa cuando la temperatura $t$ es alta?
- ¿Qué pasa cuando la temperatura $t$ es baja?

(Preguntas de reflexión, sin respuesta desarrollada en la slide.)

## Slide 63

**Recocido simulado**
- Idea: Ajustar la temperatura de manera dinámica.
- Inicio: Temperatura alta.
- Luego: Disminuir la temperatura progresivamente.

## Slide 64

**Recocido simulado**

Pseudocódigo:
1. $s \leftarrow solucionInicial$
2. $n \leftarrow random(V(s))$
3. $\Delta \leftarrow f(n) - f(s)$
4. Si $\Delta < 0$ acceptar: $s \leftarrow n$ y volver en 2.
5. Sino, acceptar si $rand(0,1) < e^{-\Delta/t}$ y volver en 2.
6. Si $n$ no acceptado, volver en 2.

## Slide 65

**Recocido simulado**
- Temperatura inicial $t_0$ alta. Si $t \to +\infty$: totalmente aleatorio.
- Reducir la temperatura de manera regular
  - Cooling Schedule necesario.
  - Si reducción demasiado rápida: parada demasiado rápida en un óptimo local.
  - Si reducción demasiado lenta: ...algoritmo demasiado lento!
- Si $t = 0$, ningún movimiento que empeora la solución actual se accepta.

## Slide 66

**Recocido simulado: Cooling Schedule**
- Predeterminado:
  - Ajuste geométrico: $t_{k+1} \leftarrow \alpha t_k$ (con $\alpha \to 1$)
  - Ajuste lineal: $t_{k+1} \leftarrow t_k - \alpha$.
- Adaptativo: reaccionar a la información encontrada durante la búsqueda.
- Número de iteraciones a cada temperatura:
  - Número constante (1 por ejemplo).
  - Número dinámico.

## Slide 67

**Recocido simulado: criterios de parada**
- Temperatura final
- Número máximo de iteraciones

## Slide 68

**Recocido simulado: Extensiones**
- Multistart / Iterated Local Search
- Múltiples recocidos

## Slide 69

**Recocido simulado: síntesis**
- Método simple y robusto.
- Costoso en tiempo de cálculo. Lento.
- Necesita ajustes ("*tuning*") de parámetros (temperatura inicial, $\alpha$, etc.)

## Slide 70

Slide de separación de subsección: "Métodos metaheurísticos — Tabu Search". Solo título y subtítulo.

## Slide 71

**Tabu Search**

Referencia bibliográfica: Glover, F., Future Paths for Integer Programming and Links to Artificial Intelligence. *Computers & Operations Research*. 13:533–549, 1986.

## Slide 72

**Tabu Search**
- Estrategia para evitar los óptimos locales con prohibición temporal de porciones del espacio de búsqueda.
- Utiliza la historía de la búsqueda sin memorizar todo.
- Idea simple que puede ser utilizada en muchos problemas.
- Muchas extensiones posibles.

## Slide 73

**Tabu Search**
- **Idea**: escapar los óptimos locales por limitación de ciclos.
- Utiliza memoría de corto plazo
  - Soluciones recientes
  - Movimientos recientes
  - Atributos de soluciones o movimientos recientes
- **Tabu List**:
  - Lista de **soluciones prohibidas**.
  - Lista de **movimientos prohibidos**.
  - Lista de **atributos prohíbidos**.
- Tamaño de la lista tabu: **Tabu Tenure**.

## Slide 74

**Atríbuto Tabu**
- Prohibir un atríbuto: prohibir una **propiedad de una solución** o de un **movimiento**.
  - Prohibir la asignación del valor 1 a la variable $x_i$ (propiedad de solución).
  - Prohibir la presencia de una arista en una solución del TSP (propiedad de solución).
  - Prohibir el cambio de valor de la variable $x_i$ (propiedad de movimiento).
  - Prohibir agregar o remover una arista en una solución del TSP (propiedad de movimiento).

## Slide 75

**Ejemplo**

En el TSP:
- Movimiento: intercambiar las ciudades 2 y 6
- Citerios posibles de prohibición:
  - Movimientos con ciudades 2 y 6
  - Movimientos con ciudades 2 o 6
  - Movimientos con ciudad 2
  - Movimientos con ciudad 6

## Slide 76

**Tabu Tenure**
- *Tabu Tenure*: ¿Cuánto tiempo dura una prohibición?
- Demasiado tiempo: búsqueda demasiado limitada.
- Demasiado poco: riesgo de ciclos (regresar a las mismas soluciones).
- *Tabu Tenure*: puede ser **estático** o **dinámico** (puede variar en la búsqueda).

## Slide 77

**Extensión importante: Criterio de aspiración**

La utilización del **criterio de aspiración** es una extensión del método Tabu importante y fácil de implementar.
Consiste en autorizar un movimiento (o atríbuto) prohibido cuando la solución candidata es mejor que la mejor solución encontrada desde el inicio de la búsqueda (ignoramos la lista tabu en este caso).

## Slide 78

Slide de separación de subsección: "Métodos metaheurísticos — GRASP: Greedy Randomized Adaptive Search Procedure".

## Slide 79

**GRASP**
- **No es** un método de búsqueda local.
- **Es** un método de construcción.
- En un método de construcción greedy, se elige como elemento siguiente el mejor elemento disponible.
- **Idea**: Aplicar un método de construcción de tipo greedy pero elegir **aleatoriamiente el elemento siguiente entre una lista de los mejores elementos candidatos** a cada iteración, en lugar de elegir sistematicamente el mejor elemento.
- Se restringe generalmente a uno de los $p\%$ mejores elementos (*Restricted Candidate List*, RCL).

## Slide 80

**GRASP**
- Alternativa 1: **Tournament Selection**, seleccionar el mejor elemento de una selección aleatoria de $t$ candidatos.
- Alternativa 2: **Fitness-Proportionate Selection** (o **Roulette Selection**), seleccionar un elemento aleatoriamente, cada elemento con una probabilidad de ser seleccionado proporcional a su calidad (*fitness*).

## Slide 81

**Fin del capítulo 3**

Hemos visto:
- Clases de problemas de optimización (P, NP, NP-Completo, NP-Difícil).
- El concepto de vecindad en algoritmos de búsqueda local.
- Los conceptos de método de construcción y de método de mejora.
- Estrategias básicas para escapar un mínimo local.
- Métodos metaheurísticos de búsqueda local: Tabu Search y Recocido Simulado.
- Método metaheurístico de construcción: GRASP.
