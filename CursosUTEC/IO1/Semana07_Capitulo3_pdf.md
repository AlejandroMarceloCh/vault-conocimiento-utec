---
curso: IO1
titulo: Semana07-Capitulo3
slides: 81
fuente: Semana07-Capitulo3.pdf
---

                         Investigación de operaciones I
                         Capítulo 3: Métodos heurísticos




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos
                         Objetivo
                                   Resolver problemas complejos de decisión con algorítmos
                                   heurísticos eficientes.
                                   En particular: resolver problemas combinatorios.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   2
                         Métodos heurísticos
                                   El término viene de la palabra eurisko (εὑρίσκω): encontrar,
                                   descubrir.
                                   Son reglas prácticas de toma de decisión.
                                   Maneras prácticas de encontrar una solución a un problema.
                                   Alternativas prácticas a las técnicas matemáticas formales.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   3
                         Porqué utilizar métodos heurísticos
                                   Generalmente para resolver instancias grandes de problemas
                                   computacionalmente dificiles.
                                   Cuando obtener una solución exacta (óptima) necesitaría un
                                   tiempo de computación excesivo.
                                   Generalmente no se usa para resolver problemas
                                   polinomiales o pequeñas instancias de un problema difícil.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   4
                         Clases de problemas




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   5
                         Clase P
                         Problemas de clase P: problemas para los cuales se conoce un
                         algoritmo capaz de encontrar una solución óptima en un tiempo
                         que es función polinomial del tamaño de la instancia. Si
                         representa el tamaño de la instancia, se dice que el algoritmo es
                         de orden        .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   6
                         Clase P
                                   Ejemplo: Para el problema del camino más corto se conoce
                                   un algoritmo (Dijkstra) que necesita un tiempo del orden de
                                       (se escribe:       ), donde es el número de vértices (en
                                   este caso consideramos que representa el tamaño de la
                                   instancia). También existe un algoritmo en tiempo
                                   (escrito:         ) donde es el número de vértices y el
                                   número de arcos (en este caso consideramos que y
                                   representan juntos el tamaño de la instancia).
                                   Otros problemas de clase P: ordenar una lista de elementos,
                                   buscar un elemento en una lista, problema del arbol mínimo
                                   de recubrimiento, saber si un número es primo.
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   7
                         Clase NP
                         Problemas de clase NP (nondeterministic polynomial time):
                         problemas para los cuales existe un algorimo rápido (en tiempo
                         polinomial) para averiguar que una solución candidata (un
                         certificado) es realmente una solución del problema.
                                   Ejemplo: El problema que consiste en saber si, para un
                                   conjunto de enteros positivos o negativos, existe un
                                   subconjunto de sumatoria nula. Encontrar una solución es
                                   difícil (tenemos que generar todos los subconjuntos posibles),
                                   pero saber si una solución es factible es fácil.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   8
                         Clase NP-difícil
                         Problemas de clase NP-difícil (NP-Hard): Problemas al menos
                         tan difícil como el problema más dificil de la clase NP (problema
                         NP-completo).
                                   Ejemplos: Problema del viajante de comercio, problema 3-
                                   SAT, problema de la mochila, problema de bin-packing.
                         Para grandes instancias de esos problemas, es importante tener
                         metodos para encontrar una "buena solución" en lugar de una
                         solución óptima: métodos heurísticos.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   9
                         Clase NP-difícil




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   10
                         Espacio de búsqueda




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   11
                         Métodos heurísticos y metaheurísticos
                                   Una búsqueda exaústiva es frecuentemente la única manera
                                   de encontrar una solución óptima.
                                   Pero el espacio de búsqueda es frecuentemente demasiado
                                   grande para permitirla.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   12
                         Métodos heurísticos y metaheurísticos
                                   Necesitamos métodos imperfectos pero "inteligentes" de
                                   búsqueda:
                                         Métodos heurísticos: método de exploración que explota
                                         aspectos específicos de un problema en particular.
                                         Métodos metaheurísticos: métodos genericos de
                                         exploración que se pueden aplicar a muchos problemas
                                         distintos. Ejemplos: recocido simulado, tabu search,
                                         algoritmos evolucionarios.
                                   Esos términos son frecuentemente utilizados sin distinción en
                                   la literatura.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   13
                         Búsqueda local: algoritmo generico
                              1. Definir un espacio de búsqueda y una función objetivo
                                            .
                              2. Definir una vecindad        : la vecindad de una solución es el
                                 conjunto de soluciones obtenidas por una transformación (o
                                 movimiento), o por un conjunto de transformaciones, de
                                 cualquier solución        .
                              3. Definir un operador de selección para seleccionar una
                                 solución de la vecindad        de la solución actual .
                                 Seleccionar la solución siguiente           .
                              4. A partir de una solución inicial :


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   14
                         Ejemplos con el problema de la
                         mochila




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   15
                         Ejemplo de espacio de búsqueda y
                         representación de una solución
                                   Consideramos el problema de la mochila con 3 objetos.
                                   Podemos encodificar una solución como una serie de 3 bits (3
                                   variables binarias de decisión): por ejemplo              .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   16
                         Ejemplo de vecindad




                         Si definimos la vecindad de una solución por la transformación
                         "se cambia el valor de un bit": la vecindad de la solución      es el
                         conjunto de soluciones (vecinos)                   , y la vecindad de
                         la solución 101 es                  .
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   17
                         Ejemplos de operador de selección de la
                         solución siguiente
                                   Elegir aleatoriamente una solución de la vecindad.
                                   Elegir la mejor solución de la vecindad (best improvement).
                                   Elegir la primera solución de la vecindad que mejora la
                                   solución actual (first improvement).




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   18
                         Ejemplos con el problema del viajante
                         de comercio (TSP)




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   19
                         Ejemplo de espacio de búsqueda y
                         representación de una solución
                                   Consideramos un conjunto de ciudades               .
                                   Podemos encodificar una solución como una permutación de
                                   ciudades: por ejemplo                       .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   20

                         Ejemplos de vecindades: 2-Exchange
                                   Intercambiar la posición de dos ciudades.
                                   Por ejemplo: intercambiando las ciudades 2 y 6, obtenemos el
                                   vecino                          .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   21
                         Ejemplos de vecindades: 2-OPT
                                   Cortar el tour en 2 y reconectar los caminos con la forma
                                   alternativa.
                                   Lo mismo que tomar una fracción de la secuencia e invertirla.
                                   Por ejemplo: invertiendo la secuencia desde 2 hasta 6,
                                   obtenemos el vecino                            .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   22
                         Ejemplos de vecindades: 2-OPT




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   23
                         Ejemplos de vecindades: 2-OPT
                         ¿Cuál es la manera más rápida de evaluar un vecino con la
                         vecindad 2-OPT?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   24
                         Ejemplos de operador de selección del tour
                         siguiente
                                   Elegir aleatoriamente un tour vecino.
                                   Elegir el mejor tour de la vecindad (best improvement).
                                   Elegir el primer tour de la vecindad que mejora el tour actual
                                   (first improvement).




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   25
                         Vecindad y tiempo de computación
                                   Una vecindad grande permite la exploración de más
                                   soluciones, pero puede necesitar más tiempo de computación.
                                   El tiempo de computación depende de la manera de
                                   encodificar las soluciones, de la vecindad y del operador de
                                   selección.
                                   Hay siempre vecindades más económicas en tiempo de
                                   computación que otras.



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   26
                         Hill climbing
                         La estrategia que consiste a seleccionar cada vez una solución
                         mejor que la solución actual se llama: Hill Climbing.
                         Pseudocódigo para un problema de maximización:
                                                                                                                 ó




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos       27
                         Steepest Hill climbing
                         La estrategia que consiste a seleccionar cada vez la mejor solución
                         de la vecindad se llama: Steepest Ascent Hill Climbing.
                         Pseudocódigo para un problema de maximización:
                                                                                                                 ó




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos       28
                         Límite de las estrategias de Hill climbing y de
                         Steepest Hill Climbing
                         El problema de esas estrategias es que se terminan con un óptimo
                         local, es decir: una solución que no tiene mejor vecino.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   29
                         Óptimo local
                                   En un problema de maximización, una solución                                  es un
                                   máximo local ssi (si y solo si):


                                   En un problema de minimización, una solución                                  es un
                                   mínimo local ssi (si y solo si):


                                   Un óptimo local se refiere siempre a una vecindad específica:
                                   un óptimo local utilizando una vecindad podría no ser un
                                   óptimo local con otra vecindad.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos           30
                         Ideas para escapar un óptimo local
                                   Probabilistic Hill Climbing
                                   Hill-Climbing with Random Restarts
                                   Iterated Local Search
                                   Variable Neighborhood Search
                                   Etc.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   31
                         Probabilistic Hill Climbing
                         Para evitar la trampa del óptimo local, podemos introducir
                         aleatoriedad en el algoritmo para aceptar soluciones peores que la
                         solución actual con una cierta probabilidad.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   32
                         Hill-Climbing with Random Restarts
                         Repetir el algoritmo de Hill Climbing o Steepest Ascent Hill
                         Climbing, tomando siempre una nueva solución inicial aleatoria.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   33
                         Iterated Local Search
                                   Similar al algoritmo de Hill-Climbing with Random Restarts,
                                   pero más "inteligente".
                                   En lugar de generar aleaoriamente una solución inicial,
                                   busquamos una solución fuera del óptima local, pero "no tan
                                   lejos".
                                   Se puede hacer por ejemplo con la perturbación del óptimo
                                   local.



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   34
                         Variable Neighborhood Search
                                   Utilizar varias vecindades (por ejemplo                ).
                                   Empezar con la vecindad .
                                   Cada vez que llegamos a un óptimo local con una vecindad                      ,
                                   pasamos a la vecindad       .
                                   Cada vez que salimos de un óptimo local, volvemos a la
                                   vecindad .
                                   El algoritmo termina cuando no se puede salir del óptimo
                                   local utilizando la vecindad .


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos       35
                         Intensificación (Explotación) vs. Diversificación
                         (Exploración)
                                   En fase de intensificación, la búsqueda se limita a la
                                   exploración de vecinos de una solución ya prometedora.
                                   En fase de diversificación, intentamos visitar otras regiones
                                   del espacio de búsqueda.
                                   Con mucha intensificación: riesgo de quedarse en los mismos
                                   locales óptimos.
                                   Con mucha diversificación: riesgo de visita demasiado
                                   aleatoria del espacio de soluciones.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   36
                         Soluciones iniciales
                         Necesitamos un algoritmo para generar una solución inicial: un
                         método de construcción.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   37
                         Soluciones iniciales para el problema
                         de Bin-Packing
                         Tenemos contenedores de capacidad para empaquetar
                         objetos. Cada objeto             tiene un pesos .
                         Objetivo: Minimizar el número de contenedores para
                         empaquetar todos los objetos.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   38
                         Soluciones iniciales para el problema
                         de Bin-Packing
                         3 métodos de construcción:
                                   Next-Fit
                                   First-Fit
                                   First-Fit Decreasing



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   39
                         Soluciones iniciales para el problema
                         de Bin-Packing
                         Next-Fit
                              1. Abrir un primer contenedor (contenedor actual)
                              2. Colocar los objetos uno por uno en el contenedor actual hasta
                                 su capacidad.
                              3. Cuando no se puede colocar un objeto, cerrar el contenedor
                                 actual y abrir un nuevo contenedor.
                              4. Regresar en 2.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   40

                         Soluciones iniciales para el problema
                         de Bin-Packing
                         Next-Fit
                         Garantía: Si el valor óptimo es                                                         , la solución generada   con
                         el algoritmo Next-Fit es tal que:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos                                  41
                         Soluciones iniciales para el problema
                         de Bin-Packing
                         First-Fit
                              1. Abrir un primer contenedor (contenedor actual)
                              2. Colocar los objetos uno por uno en el primero de los
                                 contenedores abiertos que tienen la capacidad suficiente.
                              3. Cuando no se puede colocar un objeto, abrir un nuevo
                                 contenedor.
                              4. Regresar en 2.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   42
                         Soluciones iniciales para el problema
                         de Bin-Packing
                         First-Fit
                         Garantía: Si el valor óptimo es                                                         , la solución generada   con
                         el algoritmo First-Fit es tal que:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos                                  43
                         Soluciones iniciales para el problema
                         de Bin-Packing
                         First-Fit Decreasing
                              1. Ordenar los objetos en orden decreciente de pesos.
                              2. Aplicar el algoritmo First-Fit




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   44
                         Soluciones iniciales para el problema
                         de Bin-Packing
                         First-Fit Decreasing
                         Garantía: Si el valor óptimo es        , la solución generada                           con
                         el algoritmo First-Fit Decreasing es tal que:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos         45
                         Soluciones iniciales para el problema
                         de TSP




                         ¿Qué método simple podríamos utilizar para construir una
                         solución inicial?
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   46
                         Soluciones iniciales para el problema
                         de TSP
                         Nearest neighbor
                              1. Seleccionar aleatoriamente un punto inicial
                              2. Seleccionar el punto más cercano del último punto agregado
                                 (punto actual).
                              3. Volver en 2 hasta obtener un ciclo visitando todos los puntos.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   47
                         Soluciones iniciales para el problema
                         de TSP




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   48
                         Soluciones iniciales para el problema
                         de TSP
                         Farthest insertion
                              1. Seleccionar los dos puntos más alejados y conformar un ciclo
                                 (ida y vuelta) entre con esos dos puntos.
                              2. Seleccionar el punto más alejado de cualquier punto ya
                                 visitado.
                              3. Seleccionar la arista ("ruta entre dos puntos") de la solución
                                 parcial en la cual agregar el punto es más económico.
                              4. Volver en 2 hasta obtener un ciclo visitando todos los puntos.
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   49
                         Soluciones iniciales para el problema
                         de TSP




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   50
                         Soluciones iniciales para el problema
                         de TSP
                         Cheapest insertion
                              1. Seleccionar aleatoriamente un punto inicial.
                              2. Seleccionar el punto más cercano al punto y conformar un
                                 ciclo.
                              3. Seleccionar una arista        del subciclo y un punto no
                                 visitado tal que la inserción del punto sea la inserción más
                                 económica.
                              4. Volver en 3 hasta obtener un ciclo visitando todos los puntos.
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   51
                         Soluciones iniciales para el problema
                         de TSP




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   52
                         Soluciones iniciales para el problema
                         de TSP
                         Otros métodos:
                                   Convex hull insertion
                                   Greatest angle insertion
                                   etc.



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   53
                         Vecindades conexas
                         Una vecindad es conexa si desde cualquier solución existe un
                         camino hasta cualquier otra solución en un grafo donde cada
                         nodo representa una solución y cada arco representa la transición
                         desde una solución hasta otra solución.
                         En otras palabras, es una vecindad conexa si para cualquier
                         par de soluciones       existe una secuencia de movimientos
                         tal que:



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   54
                         Vecindades conexas con el problema de la mochila
                         Dar dos ejemplos de vecindades: una vecindad no conexa y una
                         vecindad conexa.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   55
                         Métodos metaheurísticos




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   56
                         Métodos métaheurísticos presentados:
                                   Recocido simulado (método de búsqueda local)
                                   Tabu Search (método de búsqueda local)
                                   GRASP (método greedy de construcción aleatorizado)




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   57
                         Métodos metaheurísticos
                         Recocido simulado




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   58
                         Recocido simulado




                         Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P., Optimization by
                         Simulated Annealing. Science, 220(4598):671–680, 1983.
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   59
                         Recocido simulado
                                   Basado en el método de Metropolis-Hastings donde un
                                   movimiento se acepta siempre cuando mejora el valor
                                   objetivo, o con una cierta probabilidad sino.
                                   La probabilidad crece con la calidad del movimiento.
                                   La probabilidad depende de una temperatura .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   60

                         Recocido simulado
                                   En un problema de minimización, si es la solución actual y
                                     un vecino de , es la diferencia entre el valor objetivo
                                        del vecino y el valor objetivo   de la solución actual:

                                   Un movimiento que malogra la solución actual será aceptado
                                   con probabilidad:        .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   61
                         Recocido simulado


                                   ¿Qué pasa cuando                                                      ?
                                   ¿Qué pasa cuando la temperatura es alta?
                                   ¿Qué pasa cuando la temperatura es baja?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   62
                         Recocido simulado
                                   Idea: Ajustar la temperatura de manera dinámica.
                                   Inicio: Temperatura alta.
                                   Luego: Disminuir la temperatura progresivamente.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   63
                         Recocido simulado
                              1.
                              2.
                              3.
                              4. Si        acceptar:      y volver en 2.
                              5. Sino, acceptar si                   y volver en 2.
                              6. Si no acceptado, volver en 2.



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   64
                         Recocido simulado
                                   Temperatura inicial alta. Si            : totalmente aleatorio.
                                   Reducir la temperatura de manera regular
                                       Cooling Schedule necesario.
                                       Si reducción demasiado rápida: parada demasiado rápida
                                       en un óptimo local.
                                       Si reducción demasiado lenta: ...algoritmo demasiado
                                       lento!
                                   Si      , ningún movimiento que empeora la solución actual
                                   se accepta.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   65
                         Recocido simulado: Cooling Schedule
                                   Predeterminado:
                                       Ajuste geométrico:             (con       )
                                       Ajuste lineal:               .
                                   Adaptativo: reaccionar a la información encontrada durante
                                   la búsqueda.
                                   Número de iteraciones a cada temperatura:
                                       Número constante (1 por ejemplo).
                                       Número dinámico.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   66
                         Recocido simulado: criterios de parada
                                   Temperatura final
                                   Número máximo de iteraciones




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   67
                         Recocido simulado: Extensiones
                                   Multistart / Iterated Local Search
                                   Múltiples recocidos




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   68
                         Recocido simulado: síntesis
                                   Método simple y robusto.
                                   Costoso en tiempo de cálculo. Lento.
                                   Necesita ajustes ("tuning") de parámetros (temperatura inicial,
                                    , etc.)




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   69
                         Métodos metaheurísticos
                         Tabu Search




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   70
                         Tabu Search
                         Glover, F., Future Paths for Integer Programming and Links to
                         Artificial Intelligence. Computers & Operations Research. 13:533–
                         549, 1986.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   71
                         Tabu Search
                                   Estrategia para evitar los óptimos locales con prohibición
                                   temporal de porciones del espacio de búsqueda.
                                   Utiliza la historía de la búsqueda sin memorizar todo.
                                   Idea simple que puede ser utilizada en muchos problemas.
                                   Muchas extensiones posibles.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   72
                         Tabu Search
                                   Idea: escapar los óptimos locales por limitación de ciclos.
                                   Utiliza memoría de corto plazo
                                             Soluciones recientes
                                             Movimientos recientes
                                             Atributos de soluciones o movimientos recientes
                                   Tabu List:
                                             Lista de soluciones prohibidas.
                                             Lista de movimientos prohibidos.
                                             Lista de atributos prohíbidos.
                                   Tamaño de la lista tabu: Tabu Tenure.
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   73
                         Atríbuto Tabu
                                   Prohibir un atríbuto: prohibir una propiedad de una
                                   solución o de un movimiento.
                                       Prohibir la asignación del valor 1 a la variable
                                       (propiedad de solución).
                                       Prohibir la presencia de una arista en una solución del
                                       TSP (propiedad de solución).
                                       Prohibir el cambio de valor de la variable (propiedad
                                       de movimiento).
                                       Prohibir agregar o remover una arista en una solución
                                       del TSP (propiedad de movimiento).

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   74
                         Ejemplo
                         En el TSP:
                                   Movimiento: intercambiar las ciudades 2 y 6
                                   Citerios posibles de prohibición:
                                       Movimientos con ciudades 2 y 6
                                       Movimientos con ciudades 2 o 6
                                       Movimientos con ciudad 2
                                       Movimientos con ciudad 6



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   75
                         Tabu Tenure
                                   Tabu Tenure: ¿Cuanto tiempo dura una prohibición?
                                   Demasiado tiempo: búsqueda demasiado limitada.
                                   Demasiado poco: riesgo de ciclos (regresar a las mismas
                                   soluciones).
                                   Tabu Tenure: puede ser estático o dinámico (puede variar en
                                   la búsqueda).



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   76
                         Extensión importante: Criterio de aspiración
                         La utilización del criterio de aspiración es una extensión del
                         método Tabu importante y fácil de implementar.
                         Consiste en autorizar un movimiento (o atríbuto) prohibido
                         cuando la solución candidata es mejor que la mejor solución
                         encontrada desde el inicio de la búsqueda (ignoramos la lista tabu
                         en este caso).




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   77
                         Métodos metaheurísticos
                         GRASP: Greedy Randomized Adaptive Search
                         Procedure




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   78
                         GRASP
                                   No es un método de búsqueda local.
                                   Es un método de construcción.
                                   En un método de construcción greedy, se elige como elemento
                                   siguiente el mejor elemento disponible.
                                   Idea: Aplicar un método de construcción de tipo greedy pero
                                   eligir aleatoriamiente el elemento siguiente entre una lista
                                   de los mejores elementos candidatos a cada iteración, en
                                   lugar de elegir sistematicamente el mejor elemento.
                                   Se restringe generalmente a uno de los     mejores elementos
                                   (Restricted Candidate List, RCL).

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   79
                         GRASP
                                   Alternativa 1: Tournament Selection, seleccionar el mejor
                                   elemento de una selección aleatoria de candidatos.
                                   Alternativa 2: Fitness-Proportionate Selection (o Roulette
                                   Selection), seleccionar un elemento aleatoriamente, cada
                                   elemento con una probabilidad de ser seleccionado
                                   proporcional a su calidad (fitness).



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   80

                         Fin del capítulo 3
                         Hemos visto:
                                   Clases de problemas de optimización (P, NP, NP-Completo, NP-
                                   Difícil).
                                   El concepto de vecindad en algoritmos de búsqueda local.
                                   Los conceptos de método de construcción y de método de
                                   mejora.
                                   Estrategias básicas para escapar un mínimo local.
                                   Métodos metaheurísticos de búsqueda local: Tabu Search y
                                   Recocido Simulado.
                                   Método metaheurístico de construcción: GRASP.
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 3: Métodos heurísticos   81

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
