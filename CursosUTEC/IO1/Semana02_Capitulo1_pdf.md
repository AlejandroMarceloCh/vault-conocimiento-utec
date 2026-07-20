---
curso: IO1
titulo: Semana02-Capitulo1
slides: 59
fuente: Semana02-Capitulo1.pdf
---

                         Investigación de operaciones I
                         Capítulo 1: Introducción




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción
                         Investigación de operaciones
                                   En inglés: Operations Research (US) u Operational Research
                                   (UK)
                                   Se dice también "Management Science" o "Decision Science"
                                   Es un pilar de la Ingeniería Industrial




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   2
                         Propósito
                         En investigación de operaciones, mejoramos algo!
                         La definición de INFORMS: The Science of Better




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   3
                         Temas que tienen mucho que ver con la
                         investigación de operaciones
                                   Ingeniería industrial
                                   Data mining / Data science / Big data
                                   Analísis de decisión
                                   Business analytics
                                   Teoría de grafos
                                   Programación matemática
                                   Teoría de juegos
                                   Simulación

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   4
                         Temas que tienen mucho que ver con la
                         investigación de operaciones
                                   Procesos estocásticos
                                   Supply chain management
                                   Logística
                                   Gestión de proyectos
                                   Computer Science
                                   Pronósticos


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   5
                         ¿Qué significa "optimizar"?
                         Optimizar es encontrar una solución que no podría ser mejor: una
                         solución óptima.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   6
                         A ver... ¿qué podemos optimizar?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   7
                         Problemas "fáciles" de optimización




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   8
                         Encontrar el camino más corto para ir de la
                         casa a la UTEC




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   9
                         Problema de emparejamiento máximo en un
                         grafo bipartito




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   10
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   11
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   12
                         Problema de los matrimonios estables




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   13
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   14
                         Observan las preferencias de Jeff y Britta!


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   15
                         ¿Una idea para obtener matrimonios estables?


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   16
                         Aplicaciones
                                   Vendedores / compradores: problema de eficiencia del
                                   mercado
                                   Buscardor de trabajo / Oferta de puesto
                                   Donación de riñones
                                   etc.
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   17
                         Problemas "difíciles" de optimización




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   18
                         Problema de viajante de comercio

                         Conocido en inglés como Traveling Salesman Problem
                         (TSP)




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   19
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   20

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   21
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   22
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   23
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   24
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   25
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   26
                         DNA Sequencing
                         Un reto computacional:
                                   Ensamblar los fragmentos en una única cadena de
                                   nucleótidos (superstring) tal que su tamaño sea lo más
                                   pequeño posible.
                                   Antes de los años 1990 este problema fue considerado como
                                   imposible de resolver.



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   27
                         DNA Sequencing

                         Ejemplo con cadenas de bits:
                                   Conjunto de fragmentos: {000, 001, 010, 011, 100, 101, 110,
                                   111}
                                   Fragmentos concatenados (superstring):
                                   000001010011100101110111
                                   Shortest superstring:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   28
                         DNA Sequencing

                         Ejemplo con nucleótidos:
                                   Conjunto de fragmentos: {ATC, CCA, CAG, TCC, AGT}
                                   Fragmentos concatenados (superstring): ATCCCACAGTCCAGT
                                   Shortest superstring?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   29
                         Partitioning problem
                         Tenemos un conjunto de 10 pelotas, cada con un peso:




                         Objetivo: Compartir (particionar) las 10 pelotas en 2 grupos
                         (particiones) tal que la diferencia de las sumas en cada grupo sea
                         la menor posible.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   30
                         Knapsack problem (problema de la mochila)




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   31
                         Knapsack problem (problema de la mochila)




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   32
                         ¿Donde optimizar?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   33
                         Optimización de smart grids




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   34
                         Optimización de evacuación de emergencia en
                         producción petrolera offshore




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   35
                         Optimización en radioterapia e imaginería
                         médica




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   36
                         Optimización para operaciones portuarias




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   37
                         Optimización en minería




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   38
                         Optimización en el sector Oil & Gas




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   39
                         Optimización en finanzas




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   40

                         Optimización en transporte




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   41
                         Optimización en Data Science




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   42
                         Optimización en Data Science




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   43
                         Lo que se necesita saber antes de
                         empezar el curso




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   44
                         Expresiones lineales y desigualdades
                                   Ejemplo 1:
                                   Ejemplo2:
                                   Los conocimientos básicos de matemáticas o de algebra lineal
                                   son útiles per no indispensables.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   45
                         Sumatorias
                         Si representa la cantidad de botellas de soda producidas por la
                         línea de producción , la producción total de botellas por todas las
                            líneas de producción se puede escribir como:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   46
                         Sumatorias
                                   Si tenemos que producir al menos 10000 botellas utilizando
                                   todas las líneas de producción, podemos escribir:




                                   Se utiliza frecuentemente notaciones de conjuntos para
                                   escribir una sumatoria. Si es el conjunto de líneas de
                                   producción              , podemos escribir:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   47
                         Sumatorias
                         Si   representa el conjunto de líneas de producción            ,y
                            representa el conjunto de tipos de soda           , y si
                         representa el número de botellas del soda        producidas por la
                         línea de producción        , la expresión:



                         representa la cantidad de botellas de todo tipo de soda producida
                         por todas las líneas de producción.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   48
                         Sumatorias
                                   La expresión



                                   es equivalente a la expresión



                                   Se puede también escribir de forma sintética:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   49
                         Sumatorias
                         Frecuentemente, al lugar de definir el conjunto de líneas por
                                         , con representando el número de líneas,
                         escribiremos              donde      es el número de elementos
                         en el conjunto . Se dice que    es el cardinal del conjunto .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   50
                         Conjunto de enteros no negativos:
                         Es el conjunto de números enteros desde 0 hasta                                  . Se escribe:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción                   51
                         Conjunto de enteros relativos:
                         Es el conjunto de números enteros desde                                          hasta   . Se
                         escribe:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción                  52
                         Conjunto de enteros positivos:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   53
                         Operaciones sobre conjuntos




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   54
                                   Intersección de conjuntos:


                                   Unión de conjuntos:


                                   Diferencia de conjuntos:




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   55
                         Cuantificadores




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   56
                         Cuantificador "para todo"
                                   Cada linea de producción (del conjunto ) produce al menos
                                   1000 botellas:


                                   Se lee: "la producción de la linea es mayor que 1000 botellas,
                                   para todas las líneas de ”
                                   o: “Para cualquiera línea de producción de , su producción
                                   es mayor que 1000 botellas”
                                   o: “Para cada línea de producción de , ...".


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   57
                                   Cuantificador "existe"
                                   Existe al menos una línea de producción de                             que produce
                                   1000 botellas:



                                   Cuantificador "existe uno y sólo uno"
                                   Existe una y sola una línea de producción de                           que no
                                   produce botellas:



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción                 58
                         Fin del capítulo 1




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 1: Introducción   59

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
