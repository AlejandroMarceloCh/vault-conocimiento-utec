---
curso: IO1
titulo: Semana10-Capitulo4A
slides: 47
fuente: Semana10-Capitulo4A.pdf
---

                         Investigación de operaciones I
                         Capítulo 4: Programación Lineal




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal
                         Objetivos del capítulo
                                   Presentar de manera intuitiva los fundamentos teóricos de la
                                   programación lineal.
                                   Resolver problemas lineales de optimización con el método
                                   simplex.
                                   Presentar aspectos teóricos y prácticos de la dualidad.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   2
                         Parte 1: Apectos teóricos de la
                         programación lineal




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   3
                         La collección de combinaciones
                                   Combinaciones lineales
                                   Combinaciones afines
                                   Combinaciones cónicas
                                   Combinaciones convexas




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   4
                         Combinaciones lineales
                         Nos damos:
                                   un espacio vectorial E , por ejemplo Rn .
                                   un conjunto x1 , … , xm de vectores de E .
                                                                      ​                       ​




                                   un conjunto α1 , … , αm de escalares en R.
                                                                          ​                       ​




                         Llamamos:
                                                                              α 1 x1 + … + α m xm
                                                                                    ​     ​                      ​       ​




                         una combinación lineal de los vectores x1 , … , xm .                                        ​       ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal                   5
                         Combinaciones afines
                         Una combinación lineal α1 x1 + … + αm xm de vectores           ​     ​                  ​   ​




                         x1 , … , xm se llama combinación afín si ∑m
                               ​                    ​




                                                                   i=1 αi = 1.                                           ​   ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal                   6
                         Combinaciones cónicas
                         Una combinación lineal α1 x1 + … + αm xm de vectores           ​     ​                  ​   ​




                         x1 , … , xm se llama combinación cónica si αi ≥ 0, ∀i ∈
                               ​                    ​                                                                    ​




                         {1, … , m}.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal               7
                         Combinaciones convexas
                         Una combinación lineal α1 x1 + … + αm xm de vectores           ​     ​                  ​   ​




                                                                      m
                         x1 , … , xm se llama combinación convexa si ∑i=1 αi = 1 y
                                   ​                ​                                                                    ​   ​




                         αi ≥ 0, ∀i ∈ {1, … , m}.
                               ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal                   8
                         Conjunto convexo (espacio convexo)
                         X ⊆ Rn es convexo si y sólo si para cualqiuer par de vectores
                         x1 , x2 ∈ X tenemos αx1 + (1 − α)x2 ∈ X para todo α ∈ [0, 1].
                               ​       ​                                            ​                            ​




                         Dicho de otra manera:
                                   Un espacio X es convexo si para cualquier par de puntos A y
                                   B de X , el segmento [A, B] está incluido en X .
                                   Un espacio X es convexo si todas la combinaciones convexas
                                   de cualquier conjunto de puntos de X pertenecen a X .


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal       9
                         Pregunta
                         ¿La combinación convexa de un número finito de elementos de un
                         conjunto convexo S pertenece siempre a S ?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   10
                         Identifica los objetos convexos:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   11
                         ¿El conjunto de puntos (en azul) es convexo?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   12
                         ¿El conjunto de puntos (en azul) es convexo?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   13
                         Envolvente convexa (envoltura convexa)
                         La envolvente convexa de X ⊆ Rn , denotada conv(X), es el
                         conjunto de todas las combinaciones convexas de X .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   14
                         ¿Identifica la envolvente convexa de los puntos
                         en azul?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   15
                         ¿Identifica la envolvente convexa de los puntos
                         en azul?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   16
                         Envolvente convexa:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   17
                         Intersección de conjuntos convexos
                         Resultado importante:
                         La intersección de conjuntos convexos es un conjunto convexo
                         o un conjunto vacío.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   18
                         Hiperplano
                                   Definición wikipedia: Un hiperplano e un análogo de muchas
                                   dimensiones al plano (de dos dimensiones) en el espacio
                                   tridimensional.
                                   ¿Cómo representar matematicamente un hiperplano en
                                   dimensión n?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   19
                         Hiperplano
                         Un hiperplano es un conjunto de puntos {x ∣ α1 x1 + ⋯ +                                 ​   ​




                         αn xn = b} en Rn donde α es un vector no nulo.
                                ​     ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal           20

                         Semiespacio (cerrado)
                                   Definición wikipedia: Cada una de las dos partes en que un
                                   espacio queda dividido por un (hiper)plano contenido en él.
                                   ¿Cómo representar matematicamente un semiespacio en
                                   dimensión n?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   21
                         Semiespacio
                         Un semiespacio es un conjunto de puntos {x ∣ α1 x1 + ⋯ +                                ​   ​




                         αn xn ≤ b} en Rn donde α es un vector no nulo.
                                ​     ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal           22
                         Pregunta
                         ¿Un semiespacio es convexo?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   23
                         Pregunta
                         ¿Un hiperplano es convexo?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   24
                         Poliedros convexos y politopos convexos
                                   La intersección de un número finito de semiespacios es un
                                   poliedro convexos.
                                   Un poliedro convexo acotado es un politopo convexo.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   25
                         Pregunta
                         ¿La región factible de un programa lineal es convexa?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   26
                         Puntos extremos
                                   Un punto x de un conjunto convexo P es un punto extremo si
                                   no se puede escribir como combinación convexa de dos otros
                                   puntos de P .
                                   Matematicamente: x ∈ P es un punto extremo si no existe
                                   dos puntos x1 =  x y x2 =
                                                             x de P distintos de x y un escalar
                                                                    ​                     ​




                                   α ∈ [0, 1] tal que x = αx1 + (1 − α)x2 .                       ​              ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal       27
                         ¿Puntos extremos?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   28
                         ¿Puntos extremos?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   29
                         Politopos convexos y puntos extremos
                         Cada punto de un politopo convexo es combinación convexa de
                         sus puntos extremos.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   30
                         Puntos extremos y programación lineal
                         Si todas las variable son no-negativas y si la región factible es no
                         vacía, entonces existe un punto extremo.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   31
                         Puntos extremos y programación lineal
                         Si una solución óptima existe, entonces existe un punto extremo
                         óptimo.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   32
                         Puntos extremos y programación lineal
                         Si un programa lineal tiene una única solución óptima, esa
                         solución es un punto extremo.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   33
                         Puntos extremos y programación lineal
                         Si un programa lineal tiene una infinidad de soluciones óptimas,
                         todas esas soluciones son combinaciones convexas de puntos
                         extremos óptimos.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   34
                         Puntos extremos y programación lineal
                              1. Si un programa lineal tiene una solución óptima, al menos un
                                 punto extremo corresponde a una solución óptima.
                              2. Podriamos identificar todos los puntos extremos resolviendo
                                 todas las combinaciones de sistemas de n ecuaciones
                                 (hiperplanos) con n variables.
                              3. Si la solución de un sistema de ecuaciones corresponde a una
                                 solución factible, es un punto extremo.



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   35
                         Número de puntos extremos potenciales:
                         Explosión combinatoria
                              1. En un programa lineal con n variabes y m restricciones,
                                 existen m + n restricciones incluyendo las restricciones de
                                 no-negatividad.
                              2. m + n restricciones son m + n hiperplanos.
                              3. En dimensión n un punto corresponde a la intersección de n
                                 hiperplanos linealmente independientes.
                              4. ¿De cuántas maneras podemos seleccionar n hiperplanos
                                 entre m + n?
                                                                                                                 (m+n)!
                                   Número potencial de puntos extremos:                                           m!n!
                                                                                                                          ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal                36
                         Puntos extremos y programación lineal
                         Si la solución de un programa lineal que corresponde a un punto
                         extremo es mejor que las soluciones que corresponden a sus
                         puntos extremos adyacentes, entonces es una solución óptima.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   37
                         Método Simplex




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   38
                         Historia de la programación lineal
                                   En el fin del siglo XVIII Fourier inventó un método para
                                   resolver sistemas de inecuaciones, conocido ahora como el
                                   método de eliminación de Fourier-Motzkin. Ese método es
                                   bastante ineficiente.
                                   En 1930, Kantorovich y Koopmans (Premio Nobel de
                                   Economía, 1975) muestran que la programación lineal tiene
                                   un gran potencial práctico, en particular para resolver
                                   problema de alocación de recursos.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   39
                         Historia de la programación lineal
                                   En 1947, George Dantzig inventó el primer algoritmo práctico
                                   para resolver programas lineales: el método Simplex.
                                   En 1979, Khachiyan demuestra que se puede resolver
                                   programas lineales en tiempo polinomial con el método
                                   elipsoidal. Es una ruptura teorica, pero en práctica el
                                   algoritmo es lento.
                                   En 1984, Karmarkar propone otro método en tiempo
                                   polinomial, el método del punto interior, eficiente también en
                                   práctica.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   40

                         Explicación intuitiva del método simplex
                                   Se inicia el algoritmo en cualquier punto extremo.
                                   A cada iteración, consideramos los puntos adyacentes del
                                   punto actual y seleccionamos uno que mejora la solución
                                   actual.
                                   Iterar hasta que ningún punto adyacente mejore la solución
                                   actual.



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   41
                         Explicación intuitiva del método simplex




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   42
                         ¿Qué tiene que ver la convexidad con eso?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   43
                         Método simplex y convexidad




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   44
                         Método simplex y convexidad




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   45
                         Método de puntos interiores y convexidad




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   46
                         Método de puntos interiores y convexidad




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 4: Programación Lineal   47

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
