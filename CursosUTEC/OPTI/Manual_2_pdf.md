---
curso: OPTI
titulo: Manual 2 
slides: 19
fuente: Manual 2 .pdf
---

   Módulo 2


Métodos
Gradientes
ESPECIALISTA: JULIO JOSUÉ GUTIÉRREZ ALVA

                                  1
                                                     UTEC / Módulo 2: Métodos Gradientes / Índice




Índice

01.   Palabras clave                                                                           3




02.   Módulo 2: Métodos Gradientes                                                             4

        Introducción                                                                           4
        Contenidos teóricos                                                                    4
            2.1. Dirección de crecimiento máximo                                               4
            2.2. Método del descenso máximo                                                    6
            2.3. Método del gradiente descendiente                                             9
            2.4. Aplicación a la regresión lineal                                              11
        Resumen                                                                               16
        Conclusiones                                                                          16




03.   Glosario                                                                                17




04.   Bibliografía y webgrafía                                                                18




05.   Enlaces de interés                                                                      18




                                            2
                           UTEC / Módulo 2: Métodos Gradientes / Palabras clave




01.   Palabras clave

           Gradiente



           Curvas de nivel



           Optimización sin restricciones



           Función objetivo



           Regresión lineal



           Tamaño de peso




                       3
                                                                            UTEC / Módulo 2: Métodos Gradientes




Módulo 2


Métodos
Gradientes
   Introducción

En el Módulo 1, vimos cómo optimizar funciones de una variable, pero generalmente los problemas más
interesantes generan funciones de varias variables. Esto sucede, por ejemplo, en el área de Machine Learning
donde muchos de los modelos a construir tienen su formulación como problemas de optimización en varias
variables.

En este módulo, veremos algunos métodos para optimizar dichas funciones. Empezaremos con conceptos
de cálculo en varias variables que serán necesarios para entender los métodos que desarrollaremos. Luego,
estudiaremos los métodos de descenso máximo y gradiente descendiente. Finalmente, aplicaremos estos
métodos para estimar los parámetros de modelos de regresión lineal.




   Contenidos teóricos

2.1. Dirección de crecimiento máximo

Conjuntos de nivel

Sea                      y sea          . El conjunto de nivel de valor es el conjunto de todos los puntos
                   tales que                       , es decir, es el conjunto de puntos que se encuentra al mismo
nivel luego de aplicar la función   .




                                                         4
                                                                      UTEC / Módulo 2: Métodos Gradientes




Ejemplo: Los siguientes son conjuntos de nivel de la función                 .




                                                  Figura 1

Son circunferencias que corresponden a las ecuaciones

Derivada direccional

Si deseamos saber cómo cambian los valores de la función si nos movemos en cierta dirección, podemos usar
la derivada direccional. Sea un vector unitario. La derivada direccional




mide la razón de cambio instantáneo en la dirección de   .




                                                  Figura 2

El siguiente teorema nos permite calcular las derivadas direccionales fácilmente si conocemos el vector
gradiente.




                                                     5
                                                                            UTEC / Módulo 2: Métodos Gradientes




Teorema: Si                     es diferenciable en    , entonces las derivadas direccionales de   en     existen
para todo vector unitario           y se cumple

Dirección de máximo crecimiento

El siguiente teorema nos indica cuáles son las direcciones de máximo crecimiento y máximo decrecimiento
instantáneo.

Teorema: Sea                     diferenciable en      . Si           , entonces

  •          es la dirección de máximo crecimiento en y
  •            es la dirección de máximo decrecimiento en        .

Esta idea es fundamental pues nos indica en qué dirección debemos movernos (con un paso pequeño) para
lograr que el crecimiento o decrecimiento de la función sean máximos.

Vector gradiente y curvas de nivel

El vector gradiente, si es distinto de 0, será perpendicular a las curvas de nivel. Esto quiere decir que forma un
ángulo recto con la recta tangente (o con el plano tangente en más dimensiones).




                                                      Figura 3

2.2. Método del descenso máximo

Algoritmos de búsqueda lineal

Los métodos de búsqueda lineal tienen la siguiente estructura.




                                                          6
                                                                         UTEC / Módulo 2: Métodos Gradientes




donde:

      : punto inicial
      : dirección de búsqueda en la iteración   .
      : longitud del paso en la iteración .

Los algoritmos deben incluir una condición de parada.

Empezamos en un punto         y luego en cada paso elegimos una dirección y la multiplicamos por un escalar
  . La idea es que luego de varias iteraciones el algoritmo se aproxime al punto mínimo.




                                                    Figura 4

Una visualización muy útil

Es conveniente observar qué sucede con los valores de nuestra función mientras el algoritmo itera. Si deseamos
encontrar el mínimo de una función entonces el valor de la función debe decrecer eventualmente mientras
aumenta la cantidad de iteraciones.




                                                    Figura 5




                                                        7
                                                                        UTEC / Módulo 2: Métodos Gradientes




Método del descenso máximo

Dado que la dirección opuesta al gradiente es la de máximo decrecimiento, surge naturalmente la idea de
encontrar dicha dirección en cada iteración y movernos en esa dirección. A su vez, es natural querer obtener
el máximo decrecimiento posible, de ese modo, seleccionaremos      para lograr dicho decrecimiento. Esto da
lugar al algoritmo de Descenso Máximo

Algoritmo



donde:




                                                 Figura 6

Criterios de parada absolutos

Para decidir cuándo parar el algoritmo necesitamos una condición de parada. Algunas condiciones son
absolutas. Por ejemplo, podemos considerar que el algoritmo se detiene cuando la distancia entre un punto y
el siguiente es menor que un valor dado




También podríamos considerar como condición el hecho de que el valor de la función se estabiliza




                                                     8
                                                                           UTEC / Módulo 2: Métodos Gradientes




Criterios de parada relativos

Podemos considerar las versiones relativas de las condiciones de parada.




Estas condiciones se podrían utilizar cuando deseamos considerar cambios porcentuales, es decir considerar
la escala de la variable o del valor de la función.

Algoritmos globalmente convergentes

Decimos que un algoritmo es globalmente convergente si para cualquier punto inicial el algoritmo converge a
un punto que cumple las condiciones necesarias para ser un mínimo. Es decir, cuando el algoritmo converge
hacia un punto donde el gradiente es igual a 0.

El algoritmo del Descenso Máximo es globalmente convergente, es decir, que sin importar el punto inicial
elegido, este converge hacia un punto donde el gradiente es igual a 0.

No todos los algoritmos son globalmente convergentes.

Algoritmos localmente convergentes

Decimos que un algoritmo es localmente convergente si converge a un punto que cumple las condiciones
necesarias para ser mínimo si el punto inicial es lo suficientemente cercano a dicha solución. La distancia
requerida para que el algoritmo converja depende del algoritmo en sí.

2.3. Método del gradiente descendiente

Hallar en cada paso puede ser un proceso costoso pues implica utilizar un método de optimización
unidimensional. Es preferible modificar el algoritmo eligiendo un tamaño de paso constante




donde:



  : constante.




                                                     9
                                                                          UTEC / Módulo 2: Métodos Gradientes




A diferencia del método de descenso máximo consideramos fijo. Esto trae un nuevo reto pues debemos
elegir correctamente el valor de dicha variable. Si elegimos un valor muy grande es posible que el algoritmo no
converja. Por el contrario, si elegimos un valor muy pequeño es posible que converja muy lentamente.




                                                   Figura 7




                                                   Figura 8

Convergencia del método

Bajo ciertas condiciones podemos concluir que el Método del gradiente descendiente es globalmente
convergente.

Teorema: Si            es una función con matriz Hessiana     de modo que el máximo valor propio
del Hessiano siempre es menor que , entonces el Método del gradiente descendiente es globalmente
convergente para




                                                      10
                                                                           UTEC / Módulo 2: Métodos Gradientes




En el caso en que es una función cuadrática podemos ser un poco más precisos: el algoritmo es globalmente
convergente si y solo si




2.4. Aplicación a la regresión lineal

La regresión lineal es un modelo estadístico y de Machine Learning que probablemente sea uno de los más
clásicos y más usados. Nos sirve para hacer predicciones y entender las relaciones que hay entre variables. Se
basa en encontrar una relación lineal entre variables.

Ilustraremos el concepto con el siguiente gráfico. Si observamos la siguiente data, nos podríamos preguntar

¿Cuál es la mejor función lineal                que relaciona a las variables    e   ?




                                                    Figura 9

Si logramos encontrar dicha ecuación, por ejemplo, si la ecuación resulta ser




entonces podemos utilizar dicha ecuación para predecir los valores de         para valores de      no vistos con
anterioridad. Por ejemplo, para          podríamos predecir el valor            . Para conocer la validez de esta
predicción requerimos un análisis estadístico, pero con la ecuación de la recta ya podemos tener al menos una
idea de dicho valor.

Si bien es cierto que no existe una recta que pase por todos los puntos, la idea es que la “mejor” recta pase lo
más cerca posible de la mayor cantidad de puntos posibles. Para ello, debemos tener una manera de medir el
error general de nuestra recta.

Si tenemos      datos observados, es decir, parejas de valores                  , donde             , entonces
definimos




                                                       11
                                                                          UTEC / Módulo 2: Métodos Gradientes




  •      : valor observado

  •      : valor predicho, donde




                                                  Figura 10

Entonces podemos definir el residuo (o error) en la observación   como




Gráficamente, fijado el valor       , el residuo es la distancia entre el punto observado y el punto predicho.
Nuestra función objetivo será la suma de los residuos cuadráticos, es decir




Expresado en términos de los coeficientes tenemos




Para encontrar la función    debemos encontrar los valores de      y      que minimizan la función objetivo.

Regresión lineal múltiple

Podemos generalizar el proceso a varias variables. En este caso tenemos      variables           y buscamos
una función




Supongamos además que tenemos          observaciones para estas variables.




                                                      12
                                                                                 UTEC / Módulo 2: Métodos Gradientes




Ejemplo: La siguiente tabla muestra el caso con 2 variables y 10 observaciones.


                                                 x1               x2              y
                                    0          1283.0            1015.0         2290.5
                                    1          1901.0            1129.0         3400.0
                                    2          174.0             333.0          507.4
                                    3          337.0             515.0           851.7
                                    4          326.0             624.0          400.0
                                    5          236.0             671.0          1002.3
                                    6          680.0             1841.0         2103.5
                                    7          168.0             375.0          520.0
                                    8          1175.0            3134.0         4009.1
                                    9          309.0             787.0          1010.4


En este caso la función sería de la forma                                  .Si agregamos una columna inicial que sea
constante igual a 1 podemos ver la data como


                                          x0              x1              x2          y
                                0          1            1283.0       1015.0      2290.5
                                1          1            1901.0         1129.0    3400.0
                                2          1            174.0          333.0      507.4
                                3          1            337.0          515.0      851.7
                                4          1            326.0          624.0     400.0
                                5          1            236.0          671.0     1002.3
                                6          1            680.0        1841.0      2103.5
                                7          1            168.0          375.0     520.0
                                8          1            1175.0       3134.0      4009.1
                                9          1            309.0          787.0     1010.4


Y buscamos una función de la forma

Podemos recopilar la información en 2 matrices: la matriz         que es de orden                 y la matriz   que
es de orden




                                                          13
                                                                             UTEC / Módulo 2: Métodos Gradientes




Además, podemos crear una matriz de coeficientes




de ese modo podemos predecir los valores para          usando el producto de matrices     .

Función objetivo

En este caso los valores predichos se calculan en un vector




Nuestra función objetivo será la suma de los errores cuadráticos, es decir




Expresado en términos de los coeficientes tenemos




Esta es una función cuadrática de         variables:

Método del gradiente descendiente

Para este caso, dada nuestra función



el gradiente se puede calcular como



y por lo tanto el algoritmo es




                                                         14
                                                                         UTEC / Módulo 2: Métodos Gradientes




Aplicaremos este algoritmo para hallar los coeficientes , pero debemos tener una consideración antes de
aplicar el algoritmo: Es conveniente estandarizar nuestras variables, es decir, restarle a cada una su media y
dividir entre su desviación estándar.




Esto se realiza para lograr que el método converja más rápido. Luego de estandarizar las variables tendríamos




donde calculamos los coeficientes           . No es necesario estimar el intercepto pues este será igual a 0.

Luego de haber obtenido los coeficientes     podemos hallar los coeficientes originales utilizando




Y, finalmente, hallar el intercepto como




                                                      15
                                                                          UTEC / Módulo 2: Métodos Gradientes




   Resumen

Los métodos que hemos visto en este tema se basan en moverse en la dirección opuesta al gradiente (la
dirección de máximo decrecimiento).

El método de descenso máximo busca el mínimo valor que puede tomar la función en dicha dirección y, si bien
es cierto que es globalmente convergente, la búsqueda de este punto mínimo hace que no sea tan eficiente.

El método del gradiente descendiente considera un tamaño de paso constante, sin embargo, vimos que este
tamaño de paso debe ser elegido correctamente.

Finalmente, vimos una aplicación a la regresión lineal. Convertimos el problema en un problema de optimización
donde la función objetivo tiene por variables a los parámetros que deseamos estimar. Luego, aplicamos el
método del gradiente descendiente para hallar los coeficientes.

En el siguiente módulo veremos más métodos de optimización.




   Conclusiones


           La dirección de decrecimiento máximo es la dirección opuesta al gradiente.

           El método del gradiente descendiente simplifica al método de descenso máximo pues el valor de
           es constante.

           Debemos tener cuidado al elegir el valor de: no puede ser muy pequeño ni muy grande.

           Una regresión lineal se puede ajustar utilizando el método del gradiente descendiente. Es conveniente
           estandarizar las variables antes de aplicarlo.




                                                      16
                                                      UTEC / Módulo 2: Métodos Gradientes / Glosario




03.             Glosario

  Conjunto de nivel: es un conjunto de puntos donde los valores de una función permanecen
  constantes.

  Dirección de máximo decrecimiento: de una función en un punto, es la dirección donde el
  cambio instantáneo es lo más negativo posible. Es la dirección opuesta al gradiente de la función
  evaluado en el punto.

  Globalmente convergente: un algoritmo es globalmente convergente si converge para todo
  punto inicial.

  Gradiente: para una función                , es el vector

  Matriz Hessiana: para una función                 , es una matriz         ,

  que contiene en sus entradas a las derivadas parciales de segundo orden.

  Parámetros: son variables que al tomar valores específicos definen a una función.



  Residuo: es la diferencia entre el valor observado y el valor predicho.



  Tamaño de paso: para un algoritmo de búsqueda lineal, es el valor por el cual multiplicamos al
  vector que define la dirección.




                                             17
                       UTEC / Módulo 2: Métodos Gradientes / Bibliografía y webgrafía / Enlaces de interés




04.              Bibliografía y webgrafía

  Chong, E. K., & Zak, S. H. (2004). An introduction to optimization. John Wiley & Sons.

  Hastie, T., Tibshirani, R., & Friedman, J. (2017). The elements of statistical learning: Data mining,
  inference, and prediction, second edition (2nd ed.). New York, NY: Springer.

  James, G., Witten, D., Hastie, T., & Tibshirani, R. (2017). An introduction to statistical learning: With
  applications in R (1st ed.). New York, NY: Springer. Disponible en https://www.statlearning.com/




05.              Enlaces de interés

  Enlace: https://arxiv.org/abs/1609.04747
  Descripción: el artículo del link nos brinda una reseña de diferentes variaciones del método del
  gradiente descendiente.

  Enlace: https://www.youtube.com/watch?v=GCvWD9zIF-s
  Descripción: este video nos muestra animaciones del método del gradiente descendiente en 3D.

  Enlace: https://www.youtube.com/watch?v=qg4PchTECck
  Descripción: el video explica dónde se usa el método del gradiente descendiente y menciona
  algunas de sus variaciones.




                                               18
