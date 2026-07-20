---
curso: OPTI
titulo: Manual 1
slides: 14
fuente: Manual 1.pdf
---

   Módulo 1


Métodos
Unidimensionales
ESPECIALISTA: JULIO JOSUÉ GUTIÉRREZ ALVA
                                                UTEC / Módulo 1: Métodos Unidimensionales / Índice




Índice

01.   Palabras clave                                                                            3




02.   Presentación                                                                              4




03.   Módulo 1: Métodos Unidimensionales                                                        5

         Introducción                                                                           5
         Contenidos teóricos                                                                    6
             1.1. Conceptos previos                                                             6
             1.2. Método de bisección                                                           8
             1.3. Método de Newton                                                              9
             1.4. Método de la secante                                                         10
         Resumen                                                                               12
         Conclusiones                                                                          12




04.   Glosario / Bibliografía y webgrafía                                                      13




                                            2
              UTEC / Módulo 1: Métodos Unidimensionales / Palabras clave




01.   Palabras clave

            Óptimo global



            Óptimo local



            Convergencia



            Condición de parada



            Función unimodal




                 3
                                                    UTEC / Módulo 1: Métodos Unidimensionales / Presentación




02.                      Presentación

La optimización de funciones es una herramienta básica en la Ciencia de Datos pues se usa continuamente
en modelos de Machine Learning. En este curso, aprenderás diferentes métodos para resolver problemas de
optimización sea con o sin restricciones.

Entre otros temas, veremos los métodos de Gradiente Descendiente, Newton, Gradiente Conjugado, Lagrange,
Kuhn-Tucker, Gradiente Proyectado; y además aplicaciones a la Regresión Lineal, Regresión Logística y Maquinas
de Soporte Vectorial.. Luego de llevar este curso podrás comprender e implementar los principales algoritmos
de optimización numérica.


         Optimización sin restricciones                          Optimización con restricciones

                Métodos Unidimensionales                                   Programación Lineal

                    Descenso Máximo                                    Multiplicadores de Lagrange

                 Gradiente Descendiente                                    Karush Kuhn Tucker

                 Newton y Quasi-Newton

                   Gradiente Conjugado




                                Regresión lineal                Regresión logística


                                          Máquinas de soporte vectorial




                                                      4
                                                                  UTEC / Módulo 1: Métodos Unidimensionales




Módulo 1


Métodos
Unidimensionales
   Introducción

En el campo de la Ciencia de Datos, utilizamos los datos disponibles para generar conocimiento, desarrollar
productos, informar decisiones entre otros. Por ejemplo, podríamos preguntarnos:

      ¿Cuál es la manera óptima de agrupar a nuestros clientes?
      ¿Qué productos son los más demandados?
      ¿Cómo podemos mejorar los procesos de una institución?

Como lo sugieren las palabras “mejor” u “óptimo” nos encontramos en el campo de la optimización.

Un problema de optimización se puede formular como encontrar el máximo o mínimo de una función




En este módulo, empezaremos con métodos para encontrar el máximo o mínimo de funciones de una sola
variable.




Estos métodos nos servirán como una guía para los métodos que aplicaremos a funciones de varias variables.
Revisaremos conceptos previos de optimización y estudiaremos los métodos de bisección, Newton y de la
secante.




                                                    5
                                                                   UTEC / Módulo 1: Métodos Unidimensionales




   Contenidos teóricos

1.1. Conceptos previos

Mínimos y máximos globales




                                                  Figura 1



El mínimo global de una función es un valor           de modo que la función siempre es mayor o igual que
dicho valor, es decir




para todo    en el dominio de   . Similarmente el máximo global de la función es un valor      de modo que




para todo   en el dominio de    .

Si bien es cierto que buscamos hallar estos puntos, muchas veces es complicado hallarlos, pero puede ser más
sencillo hallar máximos y mínimos locales.

Mínimos y máximos locales

Un mínimo local de una función es un valor         de modo que




para todo   cercano a     . Es decir, no necesariamente es un mínimo global.




                                                      6
                                                                          UTEC / Módulo 1: Métodos Unidimensionales




                                                   Figura 2

En la imagen, observamos 2 mínimos locales que ocurren en             y       .

Similarmente, podemos definir lo que es un máximo local.

Recordemos que, si la función es diferenciable, los máximos o mínimos locales se encuentran cuando
______________ , es decir, los puntos críticos de la función son candidatos a ser los máximos y mínimos locales.

Dado un punto crítico     , es decir, un punto que cumple                         , el criterio de la segunda derivada nos
dice que

      Si                , entonces   tiene un mínimo local en     .

      Si                , entonces   tiene un máximo local en         .

Resolver la ecuación




es una posibilidad para encontrar los puntos críticos, pero nos concentraremos en métodos numéricos para
hallarlos. Los métodos que veremos en esta sección son algoritmos iterativos.

Algoritmos iterativos

Un algoritmo iterativo consiste en elegir un candidato inicial  y generar una secuencia de puntos
            de modo que esta se aproxime a un punto donde se encuentra el mínimo de una función.

Para poder generar esta sucesión se requiere de la función      y en algunos casos de sus derivadas                y     .

En muchos casos no podemos garantizar que los algoritmos converjan al mínimo global, sino únicamente a
un punto donde se cumple                . Dependerá de las características de la función que este punto sea un
mínimo local o global. Una de las condiciones que podemos imponer a la función para garantizar que hemos
encontrado un mínimo global es que la función sea unimodal.



                                                       7
                                                                     UTEC / Módulo 1: Métodos Unidimensionales




Función unimodal

Una función es unimodal si existe un valor         tal que

           es decreciente si         y

           es creciente si      .

Por ejemplo, la función de la Figura 1 es unimodal.

Esto implica que la función tiene un único mínimo local que también es mínimo global. De esta manera, si nuestro
algoritmo converge hacia un punto crítico, entonces, para las funciones unimodales, podemos garantizar que
también es un mínimo global. Empecemos entonces a estudiar estos métodos.

1.2. Método de bisección

Sea                     una función unimodal con solo un mínimo en el intervalo                      . Además,
supongamos que          existe.

Definamos




Y notemos que:

      Si                 , entonces el mínimo debe estar en

      Si                 , entonces el mínimo debe estar en

      Si                 , entonces el mínimo es      .




                                                          Figura 3



                                                             8
                                                                             UTEC / Módulo 1: Métodos Unidimensionales




Luego de analizar el signo de la derivada en el punto                podemos elegir uno de los intervalos

o            y reiniciar el proceso. El nuevo intervalo a analizar tiene la mitad de la longitud del intervalo original

y por lo tanto nos aproximamos más a la solución.

Condición de parada

El proceso continúa y lo detenemos cuando la longitud del intervalo sea menor que cierto valor prefijado             . El
valor elegido será el punto medio de dicho intervalo.

     Algoritmo

1.    Inicializamos          y      y

2.    Elegimos

        Si                    , entonces

        Si                    , entonces

        Si                    , entonces el algoritmo termina.

3.                    si                     terminamos el algoritmo, de lo contrario, repetimos desde el paso 2.

1.3. Método de Newton

Sea                           unimodal de modo que existen           y    . Además, supongamos que                  para

todo                       . Definimos un valor inicial    y luego definimos




                                                           Figura 5



                                                                 9
                                                                      UTEC / Módulo 1: Métodos Unidimensionales




Condición de parada

El algoritmo se detiene cuando la diferencia entre dos de los valores es menor a cierto valor establecido      ,

es decir,                      .

     Algoritmo

1.    Inicializamos        y

2.    Elegimos

3.                    si                terminamos el algoritmo, de lo contrario, repetimos desde el paso 2.

1.4. Método de la Secante

Sea                        unimodal de modo que existe        . En el Método de Newton consideramos




Podemos aproximar la derivada de una función con la pendiente de la recta secante, es decir




                                                    Figura 6




                                                         10
                                                                   UTEC / Módulo 1: Métodos Unidimensionales




Por lo tanto, podemos aproximar la segunda derivada por




Con lo cual nuestro algoritmo es




Este algoritmo ya no usa la segunda derivada, pero a cambio utiliza dos puntos para calcular el siguiente. Por
lo tanto, requiere de dos puntos iniciales  y       .

     Algoritmo

1.    Inicializamos        ,   y

2.    Elegimos

3.                    si              terminamos el algoritmo, de lo contrario, repetimos desde el paso 2.




                                                      11
                                                                 UTEC / Módulo 1: Métodos Unidimensionales




  Resumen

En esta sección, hemos analizado algunos conceptos teóricos y los métodos de bisección, Newton y de la
secante. Estos métodos nos permiten hallar el mínimo de una función en el caso sea unimodal.




  Conclusiones

          Los métodos de bisección, Newton y de la secante nos permiten hallar los mínimos de funciones
          unimodales.

          Los métodos de bisección y de la secante utilizan sólo la primera derivada de la función, mientras
          que el método de Newton utiliza también la segunda derivada.

          Los algoritmos requieren una condición de parada para saber cuándo detenerse y dar como
          respuesta al valor aproximado donde ocurre el mínimo.




                                                    12
                        UTEC / Módulo 1: Métodos Unidimensionales / Glosario / Bibliografía y webgrafía




04.             Glosario

  Aproximación cuadrática:
  La aproximación cuadrática en un punto es aquella función cuadrática que mejor aproxima la
  función.

  Condición de parada:
  Es una condición que utilizamos para detener un algoritmo.

  Función unimodal:
  Es una función decreciente hasta cierto punto y creciente a partir de ese punto. Tiene un único
  mínimo local y global.

  Mínimo local:
  Es un mínimo si consideramos únicamente puntos cercanos.

  Punto crítico:
  Para funciones diferenciables, es un punto donde la derivada es igual a 0..




05.             Bibliografía y webgrafía

  Chong, E. K., & Zak, S. H. (2004). An introduction to optimization. John Wiley & Sons.




                                            13
