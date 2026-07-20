---
curso: IO1
titulo: Semana04-Capitulo2
slides: 61
fuente: Semana04-Capitulo2.pdf
---

                         Investigación de operaciones I
                         Capítulo 2: Introducción a la programación lineal




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal
                         Planta de cemento: condiciones de producción
                                   Una planta produce dos tipos de cemento: cemento 1 y
                                   cemento 2.
                                   La utilidad por tonelada es de $50 para el cemento 1, y $70
                                   para el cemento 2.
                                   Para producir una tonelada del cemento 1, se necesitan 40
                                   minutos de calcinación y 20 minutos de trituración.
                                   Para producir una tonelada del cemento 2, se necesitan 30
                                   minutos de calcinación y 30 minutos de trituración.
                                   El horno y el triturador son disponibles 6 horas y 8 horas por
                                   día respectivamente.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   2
                         Planta de cemento: problema
                         ¿Cuanto cemento de cada tipo deberíamos producir cada día para
                         maximizar la utilidad?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   3
                         Planta de cemento: modelamiento
                                   El problema se modela con un programa lineal.
                                   La respuesta del problema son dos cantidades: la cantidad de
                                   cada tipo de cemento por producir cada día.
                                   Denotamos por x1 la cantidad de cemento 1, y por x2 la
                                                                              ​                                                    ​




                                   cantidad 2.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal       4
                         Planta de cemento: programa lineal
                              1. Las variables x1 y x2 se llaman: variables de decisión (o
                                                                         ​            ​




                                 simplemente: variables).
                              2. Escribimos lo que queremos hacer, la función objetivo:
                                        max z = 50x1 + 70x2                                 ​                  ​




                              3. Escribimos las restricciones:
                                        40x1 + 30x2 ≤ 360      ​                  ​




                                                   20x1 + 30x2 ≤ 480
                                                               ​                  ​




                                                   x1 , x2 ≥ 0
                                                         ​         ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   5
                         Planta de cemento: programa lineal
                         Los valores (50, 70) de la función objetivo, (40, 30, 360) de la
                         primera restricción y (20, 30, 480) de la segunda restricción se
                         llaman: parámetros.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   6
                         Programa matemático
                                   De manera general, llamamos programa matemático un
                                   problema de optimización de una función objetivo con
                                   variables y restricciones.
                                   Decimos que el programa es lineal si la función objetivo y las
                                   restricciones son todas combinaciones lineales de las
                                   variables de decisión.



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   7
                         Forma algebraica de un programa matemático
                         El problema de cemento se puede reescribir de manera más
                         general para cualquier número de cementos y cualquier número
                         de procesos.
                                   Definimos un conjunto C de cementos: C = {1, 2, … , ∣C∣}.
                                   Definimos un conjunto P de procesos: P = {1, 2, … , ∣P ∣}.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   8
                         Forma algebraica de un programa matemático
                                   Definimos los parámetros:
                                       ui : Utilidad por tonelada del cemento i ∈ C .
                                                  ​




                                             rij : Tiempo de proceso j ∈ P para producir una tonelada
                                                      ​




                                             de cemento i ∈ C .
                                             Rj : Tiempo disponible por día para el proceso j ∈ P .
                                                          ​




                                   Definimos las variables de decisión:
                                       xi : Cantidad de cemento i por producir cada día.
                                                  ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   9
                         Forma algebraica de un programa matemático
                                                            max               z = ∑i∈C ui xi           ​       ​   ​




                                                            s.t.        ​     ∑i∈C rij xi ≤ Rj
                                                                                            ​              ​
                                                                                                                              , ∀j ∈ P    ​




                                                                              xi ≥ 0
                                                                                   ​                                          , ∀i ∈ C.
                         Es la forma que se utiliza generalmente. Utilizaremos esa forma
                         en las sesiones de laboratorio para resolver los problemas de
                         optimización con Julia y JuMP.



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal              10
                  Forma genérica de un programa matemático
                         La forma genérica de un programa lineal tiene:
                             n variables no-negativas.
                                m restricciones de igualdad o de desigualdad.
                             una función objetivo por optimizar
                         El parámetro (coeficience) de costo (o de utilidad) de la
                         variable xj se denota por cj .
                                            ​                           ​




                         El coeficiente de la variable xj en la restricción i se denota
                                                                             ​




                         por aij .   ​




                         La restricción i tiene un segundo término constante bi .                                    ​




                                    Las restricciones simples de no-negatividad no son parte de
                                    las m restricciones (los algoritmos las tratan a parte).
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   11
                         Forma genérica de un programa matemático de
                         maximización
                                                   max                z = ∑nj=1 cj xj           ​       ​   ​




                                                   s.t.         ​     ∑nj=1 aij xj ≤ bi
                                                                                    ​       ​       ​           ​   ∀i ∈ {1, … , m}   ​




                                                                      xj ≥ 0​                                       ∀j ∈ {1, … , n}




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal          12
                         Forma genérica de un programa matemático de
                         minimización
                                                    min              z = ∑nj=1 cj xj           ​       ​   ​




                                                    s.t.       ​     ∑nj=1 aij xj ≥ bi
                                                                                   ​       ​       ​           ​   ∀i ∈ {1, … , m}   ​




                                                                     xj ≥ 0​                                       ∀j ∈ {1, … , n}




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal         13
                         Forma genérica de un programa matemático
                                   Una solución que satisface todas las restricciones (como
                                   x1 = 4 y x2 = 2 en el ejemplo del cemento) se llama:
                                         ​                     ​




                                   solución factible.
                                   Si ninguna otra solución es mejor que una solución factible, es
                                   una solución óptima.
                                   A cualquier solución corresponde un valor de la función
                                   objetivo: un valor objetivo.
                                   A una solución óptima corresponde el valor óptimo de la
                                   función objetivo.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   14
                         Forma genérica de un programa matemático
                                   Si todas las variables tienen la restricción de ser enteras, el
                                   programa matemático se llama: programa lineal entero (en
                                   ingles: Integer Program).
                                   Un caso particular el cuando todas las variables son binarias
                                   (0 ó 1), se llama: programa lineal binario.
                                   Un programa que tiene a la vez variables continuas y
                                   variables enteras se llama: programa lineal mixto.
                                   Si al menos una restricción o la función objetivo no es una
                                   combinación lineal de variables, tenemos un programa no-
                                   lineal.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   15
                         Forma genérica de un programa matemático
                                   Los programas lineales enteros, binarios y mixtos son más
                                   dificíles que los programas lineales.
                                   Los programas no-lineales son aún más dificíles, excepto por
                                   unos casos específicos, como por ejemplo cuando las
                                   funciones objetivos son convexas.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   16
                         ¿Programa lineal?
                                                              max                z = x1 + x2       ​           ​




                                                              s.t.               x1   ​
                                                                                                                     ≥ x2          ​




                                                                                 x1                                  ≤ 60 − 3x2
                                                                           ​                                   ​                       ​




                                                                                      ​                                                ​




                                                                                 x1 , x2
                                                                                      ​        ​                     ≥ 0.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal           17
                         ¿Cuál es el problema con esa formulación?
                                                              max                z = x1 + x2       ​           ​




                                                              s.t.               x1   ​
                                                                                                                     > x2          ​




                                                                                 x1                                  < 60 − 3x2
                                                                           ​                                   ​                       ​




                                                                                      ​                                                ​




                                                                                 x1 , x2
                                                                                      ​        ​                     ≥ 0.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal           18
                         ¿Programa lineal?
                                                              max                z = x1 + x2       ​           ​




                                                              s.t.               x21  ​
                                                                                                                     ≥ x2          ​




                                                                                 x1                                  ≤ 60 − 3x2
                                                                           ​                                   ​                       ​




                                                                                      ​                                                ​




                                                                                 x1 , x2
                                                                                      ​        ​                     ≥ 0.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal           19
                         ¿Programa lineal?
                                                              max                z = x1 + x2       ​           ​




                                                              s.t.               ∣x1 ∣    ​
                                                                                                                     ≥ 30
                                                                                 x1                                  ≤ 60 − 3x2
                                                                           ​                                   ​                   ​




                                                                                      ​                                            ​




                                                                                 x1 , x2
                                                                                      ​        ​                     ≥ 0.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal       20

                         ¿Programa lineal?
                                                               max                z = x1 + x2       ​           ​




                                                               s.t.               x1    ​
                                                                                                                      ≥ ∣u∣
                                                                                  x1                                  ≤ v − 3x2
                                                                            ​                                   ​                  ​




                                                                                        ​                                          ​




                                                                                  x1 , x2
                                                                                        ​       ​                     ≥ 0.
                         Con parámetros u y v .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal       21
                         ¿Programa lineal?
                                                               max                z = x1 + x2       ​           ​




                                                               s.t.               x1    ​
                                                                                                                      ≥ u          ​




                                                                                  x1                                  ≤ v − 3x2
                                                                            ​                                   ​                      ​




                                                                                        ​                                              ​




                                                                                  x1 , x2
                                                                                        ​       ​                     ≥ 0.
                         Con parámetros u y v .




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal           22
                         Forma matricial clásica
                         Denotamos por:
                                   x = (x1 , x2 , … , xn )T el vector de variables,
                                                             ​           ​             ​




                                   b = (b1 , b2 , … , bm )T el vector de segundos términos de las
                                                     ​           ​                 ​




                                   restricciones,
                                   c = (c1 , c2 , … , cn )T el vector de coeficientes asociadas a las
                                                         ​           ​         ​




                                   variables de la función objetivo,
                                   A la matriz de los coefficientes aij de tamaño m × n.                            ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   23
                         Forma matricial clásica
                         Podemos escribir un programa lineal en forma matricial de dos
                         maneras:

                                                       Forma estaˊndar                                        Forma cano
                                                                                                                       ˊnica
                                                      max                cT x                                 max                  cT x
                                                                                                      ​                                             ​   ​




                                                      s.t.         ​



                                                                         Ax ≤ b             ​     ​



                                                                                                              s.t.        ​



                                                                                                                                   Ax = b   ​   ​




                                                                         x≥0                                                       x≥0
                         Esas formas matriciales se utilizan principalmente en
                         presentaciones teóricas para simplificar las notaciones.

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal                            24
                         Comentarios importantes
                                   En la realidad un programa lineal puede tener igualdades y
                                   desigualdades.
                                   Podemos siempre convertir una restricción de igualdad con
                                   dos restricciones de desigualdad.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   25
                  Comentarios importantes
                          Podemos convertir una restricción de desigualdad en una
                          restricción de igualdad con una nueva variable (lo veremos
                          más tarde).
                          También podemos convertir un programa de maximización
                          en un programa de minimización: Para minimizar una
                          función objetivo z , maximizamos la función objetivo −z
                          conservando las mismas restricciones. Si el valor óptimo del
                          programa de maximización es z ∗ entonces el valor óptimo del
                          programa de minimización es −z ∗ .
                                     Una variable sin restricción de no-negatividad (se llama:
                                     variable libre) se puede escribir como la diferencia de dos
©Fabien Cornillier | Investigación devariables
                                      operaciones 1: Modelosno-negativas.
                                                             determinísticos | Capítulo 2: Introducción a la programación lineal   26
                         Terminología
                         En las restricciones de un programa lineal:
                                   la parte izquierda, función de las variables (Ax), se denota
                                   frecuentemente por LHS (Left Hand Side).
                                   la parte derecha constante (b) se denota por RHS (Right Hand
                                   Side).




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   27
                         Resolución gráfica de programas lineales con
                         dos variables
                                                                max z = x1                       ​       + 2x2              ​




                                                                s.t.    x1                       ​
                                                                                                         + x2           ​
                                                                                                                                       ≤6
                                                                                                           x2                          ≤3
                                                                                      ​              ​      ​                      ​        ​




                                                                                                                        ​




                                                                                                           x1 , x2      ​          ​   ≥0
                                   ¿Este problema está escrito en forma canónica o estándar?
                                   ¿Cómo se puede escribir en forma canónica matricial?



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal                28
                         Resolución gráfica




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   29
                         Casos especiales
                                   Sin la restricción x1 + x2 ≤ 6, tendríamos un espacio factible
                                                                                  ​            ​




                                   no acotado.
                                   ¿Tendríamos una solución óptima?
                                   ¿Se podría tener un programa lineal con espacio factible no
                                   acotado y un valor óptimo finito?
                                   ¿Se podría tener un programa lineal con espacio factible
                                   vacío?


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   30
                         Casos especiales
                                   ¿Se podría tener un programa lineal con múltiples soluciones
                                   óptimas?
                                   En el caso de tener múltiples soluciones óptimas, ¿cuantas
                                   tendríamos?
                                   Si existe al menos una solución óptima, ¿siempre existe una
                                   solución óptima que corresponde a una esquina (o punto
                                   extremo) del espacio factible?



©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   31
                         Casos especiales
                                   En un problema real como la optimización de un plan de
                                   producción, el espacio factible normalmente no es vacío:
                                   existe al menos el plan de producción actual no optimizado. Si
                                   el espacio factible es vacío, el problema es sobre-restringido.
                                   Si el valor objetivo es infinito en un problema real, hay un
                                   error en el programa matemático: inversión de signo,
                                   inversión de la dirección de una desigualdad, falta de
                                   restricción, etc.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   32
                         Ejercicio: Problema de la dieta
                                   Una granja necesita al menos 800kg por día de un alimento
                                   constituido de una mezcla de maíz y de soya.
                                   Se necesita al menos 30% de proteinas y un máximo de 5%
                                   de fibras.
                                   Los costos y los nutrientes del maíz y del soya son los
                                   siguientes:
                                     Cereal Proteinas (%) Fibras (%) Costo ($/kg)
                                     Maíz                                                9                             2           0.30
                                     Soya                                             60                               6           0.90

©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal          33
                         Ejercicio: Problema de la dieta
                                   Se busca la mezcla de menos costo.
                                   Formular el problema con un programa lineal:
                                      i. Determinar las variables de decisión.
                                     ii. Escribir la función objetivo
                                    iii. Escribir las restricciones.
                                   Escribir el problema en forma canónica.
                                   Escribir el problema de forma algebraica con un número
                                   indeterminado de cereales y de nutrientes.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   34
                         Ejercicio: Problema de la mochila
                         Formular el problema de la mochila con un número
                         indeterminado de objetos y escribir el programa en forma
                         algebraica.
                                   Identificar el (los) conjunto(s) necesario(s) y elegir una
                                   notación.
                                   Identificar los parámetros necesarios y elegir una notación.
                                   Identificar las variables de decisión necesarias y elegir una
                                   notación.
                                   Escribir la función objetivo.
                                   Escribir las restricciones.
©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   35
                         Ejercicio: Problema de particionamiento
                                   S es un conjunto de números enteros de N∗
                                   Queremos partir el conjunto S en dos subconjuntos S1 y S2                                       ​       ​




                                   Denotamos por s1 y s2 las sumas de los números en S1 y S2
                                                                              ​         ​                                              ​       ​




                                   Escribir un programa lineal para minimizar la diferencia
                                   entre s1 y s2      ​          ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal                   36
                         Ejercicio: Problema de particionamiento
                                   S es un conjunto de números enteros de N∗
                                   Queremos partir el conjunto S en n subconjuntos
                                   S1 , S2 , … , Sn
                                         ​        ​                     ​




                                   Denotamos por s1 , … , sn las sumas de los números en
                                                                              ​                  ​




                                   S1 , … , Sn
                                         ​                   ​




                                   Escribir un programa lineal para minimizar la diferencia
                                   entre max{s1 , … , sn } y min{s1 , … , sn }
                                                                    ​                  ​                          ​                ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal       37
                         Variables binarias y restricciones
                         lógicas




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   38
                         Consideramos el caso de una empresa que tiene un conjunto P =
                         {1, 2, … , ∣P ∣} de proyectos en los cuales tiene la oportunidad de
                         invertir.
                         Asociamos a cada proyecto i ∈ P la variable binaria xi siguiente:                                         ​




                                               xi = {
                                                      1 si se invierte en el proyecto i ∈ P
                                                      0 caso contrario
                                                     ​              ​                                                                  ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal           39
                         Caso 1
                         No se puede invertir en más de N proyectos.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   40

                         Caso 2
                         Se debe invertir en un mínimo de N proyectos.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   41
                         Caso 3
                         Si se invierte en el proyecto 1, entonces se invierte también en el
                         proyecto 2.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   42
                         Caso 4
                         Los proyectos 1 y 2 son incompatibles. Si se invierte en uno, no se
                         puede invertir en el otro.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   43
                         Caso 5
                         Se debe invertir al menos en uno de los proyectos 1 y 2.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   44
                         Caso 6
                         Si se invierte en el proyecto 1, entonces se debe también invertir
                         en los proyectos 2 y 3.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   45
                         Caso 7
                         Si se invierte en el proyecto 1, entonces se debe también invertir
                         en al menos uno de los proyectos 2 y 3.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   46
                         Caso 8
                         Si se invierte en al menos en uno de los proyectos 1 y 2, entonces
                         se debe invertir también en el proyecto 3.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   47
                         Caso 9
                         Si se invierte en los dos proyectos 1 y 2, entoncés se debe invertir
                         en el proyecto 3.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   48
                         Método del Big-M




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   49
                         El método del big-M consiste en utilizar un valor suficientemente
                         grande en una restricción para que en ciertas condiciones esa
                         restricción sea satisfecha para cualquier valor que las variables de
                         decisión podrían tomar.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   50
                         Ejemplo
                         Consideramos un problema de location-transportation que
                         consiste en elegir en un conjunto W de almacenes aquellos que
                         debemos abrir para abastecer un conjunto S de tiendas, además
                         de decidir de las cantidades de productos que se enviarán desde
                         cada almacén hasta cada tienda.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   51
                         Objetivo
                         Minimizar el costo total calculado como la sumatoria de los costos
                         fijos fi de apertura de un almacén i y los costos variables vij de
                                         ​                                                                                         ​




                         transporte de cada unidad de producto desde el almacén i hasta la
                         tienda j . Definimos también qi como la capacidad de cada               ​




                         almacén i y dj como la demanda de cada tienda j .
                                                           ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal       52
                         Variables de decisión
                         Denotamos por xij la variable de decisión que corresponde a la
                                                                      ​




                         cantidad de productos enviados desde el almacén i ∈ W hasta la
                         tienda j ∈ S , y por yi la variable de decisión binaria que toma el
                                                                            ​




                         valor 1 si se abre el almacén i ∈ W y el valor 0 en el caso
                         contrario.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   53
                         Pregunta
                         ¿Cómo garantizar que ningún producto sea enviado a una tienda
                         desde un almacén cerrado?
                         Traducción: ¿Cómo garantizar que las variables xij sean nulas si                                          ​




                         y i = 0?
                              ​




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal       54
                         Podemos utilizar un valor M grande y plantear la restricción
                         siguiente:
                                                                   xij ≤ M yi ,
                                                                          ​                   ​       ∀i ∈ W , j ∈ S.
                         Si sabemos por ejemplo que ninguna tienda necesita más de d
                         unidades del producto, un buen valor de M podría ser d.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   55
                         Peligro con el big-M
                         Podríamos pensar que cualquier valor grande de M es adecuada
                         y, por ejemplo, fijar M = 1000000000000000...000, pero
                         "mezclar" coeficientes mayores en muchos órdenes de magnitud
                         que cualquier de los otros genera generalmente importantes
                         problemas númericos (en el capítulo 6, veremos por ejemplo que
                         genera a una pésima relajación lineal).
                         Por esa razón, el valor del big-M debería ser suficientemente
                         grande para que las restricciones sean válidas, no más grande.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   56
                         Ejemplo de modelo mejorado
                         Si sabemos por ejemplo que cualquier tienda j nunca necesita
                         más de dj unidades del producto, podríamos plantear las
                                                ​




                         restricciones siguientes:
                                                                    xij ≤ dj yi ,
                                                                           ​            ​    ​         ∀i ∈ W , j ∈ S.
                         Importante: Se puede ver que el big-M no tiene que ser único,
                         sino que es frecuentement preferible tener varios big-Ms cuando
                         se puede. Aquí, tenemos un Mj = qj distinto para cada tienda. Es          ​            ​




                         mejor que tener un único valor de M para todas las tiendas.


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   57
                         Aún mejor
                         Si sabemos además que el stock de producto del almacén i es
                         limitado a hi unidades, podríamos plantear las restricciones
                                                       ​




                         siguientes:
                                                           xij ≤ min{qi , dj } yi ,
                                                               ​                        ​       ​        ​        ∀i ∈ W , j ∈ S.




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal    58
                         Activar / desactivar restricciones con el big-M
                         Consideramos una variable binaria δ .
                         ¿Cómo formular que la restricción:
                                                                                        ∑ a i xi ≤ b
                                                                                                 ​     ​    ​




                                                                                         i∈N

                         sea satisfecha si δ = 1?




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   59
                         Disyunción lógica con el big-M
                         ¿Cómo formular que de las dos restricciones siguientes:
                                                                              (1)                  ∑ a i xi ≤ b
                                                                                                            ​        ​       ​




                                                                                                   i∈N

                         y
                                                                              (2)                  ∑ c i xi ≤ d
                                                                                                            ​    ​       ​




                                                                                                   i∈N

                         al menos una sea satisfecha?


©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a la programación lineal   60

                         Fín del
                         capítulo 2




©Fabien Cornillier | Investigación de operaciones 1: Modelos determinísticos | Capítulo 2: Introducción a
la programación lineal                                                                         61

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
