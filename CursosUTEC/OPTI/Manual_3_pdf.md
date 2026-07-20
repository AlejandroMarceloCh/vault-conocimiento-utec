---
curso: OPTI
titulo: Manual 3
slides: 17
fuente: Manual 3.pdf
---

   Módulo 3


Otros métodos de
optimización sin
restricciones
ESPECIALISTA: JULIO JOSUÉ GUTIÉRREZ ALVA

                                  1
                                UTEC / Módulo 3: Otros métodos de optimización sin restricciones / Índice




Índice

01.   Palabras clave                                                                                   3




02.   Presentación                                                                                     4




03.   Módulo 3: Otros métodos de optimización sin restricciones                                        4

        Introducción                                                                                   4
        Contenidos teóricos                                                                            4
            3.1. Métodos de Newton                                                                     4
            3.2. Aplicación a la regresión logística                                                   7
            3.3. Método de gradiente congujado                                                        10
            3.4. Métodos de Quasi-Newton                                                              13
        Resumen                                                                                       15
        Conclusiones                                                                                  15




04.   Glosario                                                                                        16




05.   Bibliografía y webgrafía                                                                        16




06.   Enlaces de interés                                                                              16




                                                2
        UTEC / Módulo 3: Otros métodos de optimización sin restricciones / Palabras clave




01.   Palabras clave

                      Newton



                      Aproximación cuadrática



                      Función logística



                      BFGS



                      Clasificación



                      Máxima Verosimilitud



                      Matriz positivo definida




                              3
                                              UTEC / Módulo 3: Otros métodos de optimización sin restricciones




Módulo 3


Otros métodos de
optimización sin
restricciones
   Introducción

Si bien el vector opuesto al gradiente nos brinda la dirección de decrecimiento máximo, puede ser que no
apunte necesariamente hacia el mínimo. Por ello, es posible que la elección de otros vectores dirección haga
que el algoritmo converja en menos iteraciones.

En este módulo veremos algunos métodos de búsqueda lineal que usan vectores dirección diferentes al vector
gradiente. Estos métodos, en general, son más rápidos que los vistos en el módulo anterior, sin embargo, su
implementación requiere del uso de la matriz Hessiana o de algunos cálculos en base al vector gradiente.

Estudiaremos el método de Newton, el cual generaliza el método visto en el Módulo 1. Aplicaremos este método
a la regresión logística. Luego estudiaremos métodos de gradiente conjugado y de Quasi-Newton.




   Contenidos teóricos

3.1. Método de Newton

El método de Newton tiene como idea el hecho de que es posible calcular una aproximación cuadrática
de una función utilizando la matriz Hessiana y que es sencillo obtener el mínimo de dicha aproximación.




                                                     4
                                                 UTEC / Módulo 3: Otros métodos de optimización sin restricciones




Aproximación cuadrática

La aproximación cuadrática de una función en un punto es la función cuadrática que se encuentra más cerca
de la función cerca del punto elegido. A continuación, la definimos.

Si                es una función de clase     (sus segundas derivadas parciales existen y son continuas). La

aproximación cuadrática de      en                    es la función




Veamos cómo calcular su mínimo.

Mínimo de la aproximación cuadrática

Podemos utilizar cálculo en varias variables para hallar el mínimo. Si hallamos el gradiente de la aproximación
cuadrática obtenemos



Y si lo igualamos a 0 obtenemos



Este es un punto crítico y, si la matriz Hessiana es positivo definida, entonces será un mínimo.

Matriz positivo definida

Recuerda que, una matriz es positivo definida si todos sus valores propios son positivos. Una forma de verificar
esto es considerando los menores de una matriz. Si la matriz es




Entonces, los menores son




     es positivo definida si




                                                        5
                                              UTEC / Módulo 3: Otros métodos de optimización sin restricciones




Idea del método

La idea del método por lo tanto consiste en elegir un punto inicial, calcular la aproximación cuadrática y
ubicar dónde ocurre el mínimo: este será el nuevo punto a considerar. El algoritmo queda entonces como
sigue.

Algoritmo

El Método de Newton consiste en considerar un punto inicial      e iterar




con una condición de parada.

La pregunta natural surge: ¿podemos asegurar que el algoritmo converja a un punto donde el gradiente es
igual a 0?

Convergencia

Si   es una función de clase      (las terceras derivadas parciales existen y son continuas), el método de
Newton es localmente convergente si         es una matriz positivo definida. Esto quiere decir que el método
converge para puntos lo suficientemente cercanos a la solución, sin embargo, no podemos garantizar que
converja para todos los puntos.

Si la matriz no es positivo definida, entonces no podemos garantizar que sea localmente convergente.
Podemos modificar el método como sigue.

Modificación de Levenberg-Marquardt

Si     no es positivo definida, podemos considerar en su lugar una matriz




de modo que, si elegimos          suficientemente grande, entonces la nueva matriz es positivo definida.
Con esta modificación tenemos




Si   es un número muy pequeño, entonces el método se aproxima al Método de Newton. Por otro lado, si
es   un número muy grande el método se aproxima al Método del Gradiente Descendiente.

Aplicaremos el Método de Newton la regresión logística.




                                                     6
                                                UTEC / Módulo 3: Otros métodos de optimización sin restricciones




3.2. Aplicación a la regresión logística

La regresión logística es un modelo que nos permite clasificar observaciones en 2 categorías.




                                                      Figura 1

Problema de clasificación

Por ejemplo, la imagen mostrada arriba corresponde a data sobre la salud de personas.


                                             tobacco             ldl        y
                                  0           12.00              5.73       1
                                   1           0.01              4.41       1
                                  2           0.08               3.48       0
                                  3            7.50              6.41       1
                                  4           13.60              3.50       1
                                  ...           ...               ...       ...


Algunas de estas personas tuvieron problemas cardiacos      y otras no los tuvieron     .
Basándonos en un modelo, quisiéramos predecir la probabilidad de que una persona tenga problemas
cardiacos.

En la figura podemos observar que los puntos rojos corresponden a               , mientras que los puntos azules
corresponden a         . Esperaríamos por lo tanto que, si los datos de una persona corresponden a puntos más
cerca del origen sea probable que        ; mientras que si, por ejemplo, corresponden a puntos ubicados en el
cuadrante superior derecho, sea más probable que              .

Como nuestro objetivo es predecir una probabilidad, será de utilidad la siguiente función que toma valores
entre 0 y 1.




                                                         7
                                                 UTEC / Módulo 3: Otros métodos de optimización sin restricciones




Función sigmoide

Utilizaremos la función sigmoide para modelar la probabilidad




                                                      Figura 2

Consideraremos un modelo con        variables predictivas.

Data

Similar a lo que teníamos para una regresión lineal, podemos almacenar la data en matrices




Donde es el número de datos. Cada columna de la matriz            corresponde a una variable, excepto la primera
columna que corresponde al intercepto.

La principal diferencia es que ahora los valores de     son solo 1 y 0.

El modelo pretende estimar, basándonos en los valores de las variables                  , la probabilidad de que
   sea 1.




                                                         8
                                                  UTEC / Módulo 3: Otros métodos de optimización sin restricciones




Modelo logístico

El modelo que consideramos es




Aquí, la probabilidad de que       condicional a haber observado la data correspondiente a los valores
           se modela como la función logística aplicada a una función lineal.

Para simplificar la notación, denotamos a esta probabilidad con                     y por lo tanto, el modelo es




Donde los parámetros del modelo son      y
Utilizando notación matricial, podemos escribir




Si conocemos los coeficientes      y    , para estimar las probabilidades calculamos la matriz

Donde la función    se aplica a todas las componentes.

La pregunta que surge es: ¿cómo sabemos que tan buenas son las probabilidades que hemos estimado?

Función objetivo

La función de máxima verosimilitud




toma valores mayores cuando el modelo es mejor. Dado que tomaremos derivadas, es conveniente aplicar el
logaritmo para convertir los productos en sumas. De modo que, nuestra función a maximizar será




Por lo tanto, deseamos minimizar       . Usaremos el método de Newton para estimar los coeficientes.

Método de Newton

El algoritmo para minimizar     es el siguiente




                                                        9
                                                   UTEC / Módulo 3: Otros métodos de optimización sin restricciones




Notamos que esto es equivalente a




y que requerimos de la matriz Hessiana de            y del gradiente. Utilizando propiedades de cálculo vectorial
obtenemos




Donde la matriz      es




3.3. Métodos de gradiente conjugado

Los métodos de gradiente conjugado son otra alternativa. Inicialmente, estos métodos nos sirven para optimizar
funciones cuadráticas, pero veremos que podemos generalizar la idea.

Direcciones conjugadas

Dada una matriz simétrica        de orden        , decimos que los vectores




son    -conjugados si para todo          tenemos




esto es,    es perpendicular a

Por ejemplo, si




Los vectores                 y                 son    -conjugados.

Si los vectores                  son   -conjugados, entonces son linealmente independientes, por lo tanto,

cualquier punto de        se puede expresar de manera única como una combinación lineal




                                                         10
                                               UTEC / Módulo 3: Otros métodos de optimización sin restricciones




Para hallar el mínimo de una función cuadrática, buscaremos expresarlo como una combinación lineal de los
vectores -conjugados.

Algoritmo de dirección conjugada

Este algoritmo sirve para minimizar una función cuadrática




donde    es una matriz simétrica positivo definida. Nota que su gradiente es




Y su matriz Hessiana es




Dado un punto inicial      y vectores   -conjugados                   realizamos, desde          hasta



1.



2.



3.

Este algoritmo es globalmente convergente y converge en n pasos. En este caso, el valor de     surge como
resultado de hallar el punto donde se minimiza la función al moverse desde el punto     en la dirección del
vector     .

Si tenemos los vectores conjugados, entonces podemos encontrar el mínimo de una función cuadrática con
   positivo definida. La pregunta que surge naturalmente es:

¿Cómo generar vectores conjugados?

Si hemos generado el vector     , consideraremos cómo hallar un vector conjugado

Es decir, usando el gradiente                   . Si recordamos la definición, debemos tener                 y

de aquí se deduce




                                                      11
                                                UTEC / Módulo 3: Otros métodos de optimización sin restricciones




Ahora que sabemos obtener los vectores conjugados sobre la marcha, nuestro algoritmo queda de la siguiente
manera.

Algoritmo del gradiente conjugado

Dado un punto inicial     , inicializamos      y realizamos

  1.

  2.

  3.

  4.

  5.

  6.

  7.              y, si             regresamos al paso 2.

Caso de una función no cuadrática

Si la función a optimizar no es cuadrática tomaremos 2 medidas para que el algoritmo solo utilice a la función
y su gradiente (y no al Hessiano).

  1.      será obtenido mediante un algoritmo de optimización unidimensional.
       Será el punto que minimiza a




  2.   La fórmula para      cambia para usar únicamente el gradiente.

Existen diferentes posibles fórmulas para     . Cada una de ellas brinda un algoritmo distinto. Mencionaremos
tres de ellas:

  •    Fórmula de Hesteness-Stiefel




                                                      12
                                                UTEC / Módulo 3: Otros métodos de optimización sin restricciones




  •     Fórmula de Polak-Ribiere




  •     Fórmula de Fletcher-Reeves




3.4. Métodos de Quasi-Newton

Recordemos el método de Newton donde iteramos de acuerdo a la fórmula




Si bien es bastante efectivo cuando converge, en cada paso debemos calcular la inversa del Hessiano lo cual
es costoso.

Idea

En los métodos de Quasi-Newton aproximamos a




por una matriz      de modo que el algoritmo se convierte en




Donde hemos agregado también un tamaño de paso . Una forma de garantizar que el valor de la función vaya
disminuyendo (si elegimos el apropiado) es que sea una matriz positivo definida.

También podemos denotar a los métodos como

donde

Diferentes formas de calcular la matriz     dan lugar a diferentes algoritmos. Mencionaremos dos de ellos.

Algoritmo SRS

Dado un punto inicial     , inicializamos       y realizamos




                                                       13
                                                   UTEC / Módulo 3: Otros métodos de optimización sin restricciones




  1.         una matriz simétrica positivo definida (la identidad por ejemplo).

  2.

  3.

  4.   Calculamos

         •

         •

         •



  5.                 , de no cumplirse la condición de parada regresamos al paso 2.

Algoritmo BFGS

En el Algoritmo BFGS actualizamos la matriz         de acuerdo a la siguiente ecuación




                                                          14
                                              UTEC / Módulo 3: Otros métodos de optimización sin restricciones




   Resumen

En este módulo, estudiamos nuevos métodos de búsqueda lineal que usan direcciones de movimiento diferentes
a la dirección opuesta al gradiente, aunque guardan cierta relación con dicha dirección. Estos métodos son
generalmente más rápidos que el método de gradiente descendiente. Sin embargo, deben almacenar más
información pues requieren el uso del Hessiano o de otras matrices.

También estudiamos al modelo de regresión logística que nos permite predecir clases y mostramos como el
método de Newton se puede aplicar para encontrar los parámetros del modelo.




   Conclusiones

           El método de Newton requiere menos iteraciones para converger, pero es solo localmente
           convergente.

           Podemos agregar un tamaño de paso y considerar la modificación de Levenberg-Marquardt.

           Podemos estimar los coeficientes de una regresión logística con el método de Newton.

           Los métodos de gradiente conjugado pueden encontrar el mínimo de una función cuadrática de
           variables a lo mas en pasos, pero también se puede adaptar a funciones generales.

           Los métodos de Quasi-Newton evitan el uso de la matriz Hessiana al considerar aproximaciones
           de esta.




                                                    15
UTEC / Módulo 3: Otros métodos de optimización sin restricciones / Glosario / Bibliografía y webgrafía / Enlaces de interés




04.                         Glosario

            Matriz positivo-definida: es una matriz cuadrada cuyos valores propios son todos positivos.

            Valor propio:       es un valor propio de una matriz cuadrada          si existe un vector           tal que



            Función de clase           : es una función que tiene derivadas parciales continuas de orden           .



            Función sigmoide o logística: es la función



            Modelo de clasificación: es un modelo que tiene por objetivo diferenciar entre dos (o más)
            clases basándose en variables predictivas.




05.                         Bibliografía y webgrafía

            Chong, E. K., & Zak, S. H. (2004). An introduction to optimization. John Wiley & Sons.

            James, G., Witten, D., Hastie, T., & Tibshirani, R. (2017). An introduction to statistical learning: With
            applications in R (1st ed.). New York, NY: Springer. Disponible en https://www.statlearning.com/




06.                         Enlaces de interés

            Enlace: https://www.csie.ntu.edu.tw/~r97002/temp/num_optimization.pdf
            Descripción: libro de Nocedal y Wright donde se estudian a más profundidad los temas vistos en
            el módulo.



                                                            16
