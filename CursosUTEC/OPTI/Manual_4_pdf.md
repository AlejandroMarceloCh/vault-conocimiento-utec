---
curso: OPTI
titulo: Manual 4
slides: 26
fuente: Manual 4.pdf
---

   Módulo 4


Optimización con
restricciones
ESPECIALISTA: JULIO JOSUÉ GUTIÉRREZ ALVA

                                  1
                                              UTEC / Módulo 4: Optimización con restricciones / Índice




Índice

01.   Palabras clave                                                                                3




02.   Módulo 4: Optimización con restricciones                                                      4

        Introducción                                                                                4
        Contenidos teóricos                                                                          5
            4.1. Programación lineal                                                                 5
            4.2. Multiplicadores de Lagrange                                                        11
            4.3. Condiciones de Karush-Kuhn-Tucker                                                 15
            4.4. Convexidad                                                                        16
            4.5. Aplicación a máquinas de soporte vectorial                                        17
        Resumen                                                                                    23
        Conclusiones                                                                               23




03.   Glosario                                                                                     24




04.   Bibliografía y webgrafía                                                                     25




05.   Enlaces de interés                                                                           25




                                             2
              UTEC / Módulo 4: Optimización con restricciones / Palabras clave




01.   Palabras clave

           Simplex



           Matriz aumentada



           Solución factible



           SVM



           Restricciones



           Convexidad



           Lagrangiano




                     3
                                                                 UTEC / Módulo 4: Optimización con restricciones




Módulo 4


Optimización con
restricciones
   Introducción

En este módulo, consideraremos problemas de optimización con restricciones. A diferencia de los módulos
anteriores, exigiremos que la función sea analizada únicamente en cierta parte de su dominio. Para ello,
impondremos condiciones sobre las variables. Si, por ejemplo, restringimos los valores de una función a una
curva, el problema de hallar el mínimo con la restricción es distinto al problema sin la restricción.




                                                    Figura 1



En la imagen, podemos notar que hallar el mínimo considerando la restricción implica considerar solo los
valores de la curva negra, mientras que hallar el mínimo sin la restricción implica considerar todos los posibles
valores de la superficie anaranjada.




                                                       4
                                                                  UTEC / Módulo 4: Optimización con restricciones




En general, un problema puede tener muchas restricciones, algunas dadas por igualdades y otras por
desigualdades. Consideraremos entonces problemas del tipo




Donde el mínimo de la función     está sujeto a (sa) las restricciones.

En primer lugar, veremos problemas de programación lineal, donde las funciones involucradas son todas
lineales. Resolveremos dichos problemas con el método simplex.

Luego, veremos qué sucede si las funciones son más generales, pero consideramos solo igualdades. Para ello,
utilizaremos las condiciones de Lagrange.

Después de ello, consideraremos el caso general. Para ello, utilizaremos las condiciones de Karush-Kuhn-Tucker
(KKT).

Finalmente, estudiaremos a las máquinas de soporte vectorial (SVM por sus siglas en inglés) y plantearemos su
cálculo como un problema de optimización con restricciones.




   Contenidos teóricos

4.1. Programación lineal

Un problema de programación lineal es un problema de optimización con restricciones donde tanto la función
objetivo como las funciones que definen a las restricciones (igualdades o desigualdades) son lineales.

Ejemplo:




Las restricciones definen una región, llamada región factible. En el caso de 2 o 3 variables esta región se puede
graficar. La región factible de nuestro ejemplo se muestra a continuación:




                                                        5
                                                                 UTEC / Módulo 4: Optimización con restricciones




                                                    Figura 2

Los puntos donde es posible encontrar la solución son los vértices del polígono. Entre ellos, el que da el máximo
valor para es

Forma estándar del problema

En su forma estándar, con ayuda de variables auxiliares, el problema se puede escribir como un sistema donde
las restricciones son dadas por igualdades y por las inecuaciones

Tanto la función objetivo como las restricciones son lineales, esto es




lo cual se puede escribir como




Además, el sistema de ecuaciones lineales se puede escribir, en forma matricial como




Es decir, el problema se puede escribir como




Donde la notación          indica que todas las componentes del vector      son no negativas.




                                                        6
                                                                 UTEC / Módulo 4: Optimización con restricciones




Además, asumimos que es una matriz          de rango (es decir, no hay ecuaciones redundantes) y que
     (cambiando de signo a toda una ecuación de ser necesario).

Veamos un ejemplo.

Ejemplo: Convirtamos el siguiente problema a su forma estándar




En primer lugar, convertimos el problema a un problema de minimización. Minimizaremos                    . Luego,
agregaremos una variable auxiliar a la inecuación. Notemos que se cumple




Por lo tanto, el problema quedaría como




Soluciones básicas

El sistema         es tal que el rango de la matriz      es   . Por lo tanto, debe existir un conjunto de
columnas que sean linealmente independientes. Si estas columnas fuesen las m primeras, luego de realizar
reducción gaussiana a la matriz aumentada       , llegaríamos a la siguiente matriz escalonada reducida.




En esta matriz hay     pivotes iguales a 1, es decir, un pivote por fila. Estos pivotes corresponden a las
primeras columnas de la matriz . Las siguientes             columnas pueden tener entradas diferentes de 0 y
la última columna corresponde a la transformación de la columna       luego de hacer las operaciones entre filas.

Por lo tanto, una solución del sistema de ecuaciones sería




A esta solución le llamaremos solución básica. Esta solución corresponde a la base dada por las primeras
columnas.




                                                       7
                                                                UTEC / Módulo 4: Optimización con restricciones




Si elegimos otro conjunto de    columnas (que sea linealmente independiente), encontraríamos otra solución
básica donde no necesariamente los ceros se encuentren en las últimas posiciones, sino que sería un vector
con           ceros y    entradas que pueden ser distintas de cero. Estas últimas están en las posiciones que
corresponden a las columnas elegidas.

Soluciones factibles

Una solución del sistema de ecuaciones lineales se llama factible si todas sus entradas son no negativas. Una
solución básica puede ser o no factible.

Si el problema de programación lineal tiene solución, entonces debe existir una solución básica factible.

Matriz de coeficientes canónica

Si al reordenar las columnas de la matriz     obtenemos una matriz del tipo            , es decir, si podemos
construir la matriz identidad con  de las columnas de , entonces decimos que está en forma canónica. Las
columnas que tienen los pivotes son la base respecto de la cual la matriz es canónica.

Ejemplo:




Es canónica con respecto a las columnas 3, 4 y 5. La matriz




Es canónica con respecto a las columnas 3, 1 y 4

Matriz aumentada canónica

Una matriz aumentada         es canónica si la matriz      es canónica. Luego de reordenar las columnas, una
matriz aumentada canónica tiene la siguiente forma




En el caso que se muestra la base corresponde a las primeras        columnas, pero la base podría consistir de
otras columnas.

Cambio de la base

Supongamos que, tenemos una solución básica factible correspondiente a las columnas




                                                       8
                                                               UTEC / Módulo 4: Optimización con restricciones




Es decir, que es una combinación lineal de las columnas de la base. Si quisiéramos agregar a la columna
   a la base deberíamos quitar alguna de las columnas. Observando la matriz




Podemos expresar a la columna       como una combinación lineal de las columnas               . Los coeficientes
son las entradas de la columna, esto es

Al multiplicar por un número    a la ecuación obtenemos

Podemos obtener, por lo tanto




Para eliminar alguna de las     columnas originales, algunos de los coeficientes deben ser 0. Por ello,

para algún             . Esto dará lugar a una nueva solución básica. Para que sea una solución básica factible

elegimos




Supongamos que la columna a eliminarse es la , entonces la nueva solución básica es




                                                       9
                                                                UTEC / Módulo 4: Optimización con restricciones




Donde entrada tiene entrada 0 y la de la columna entrada . Para ordenar esta solución podemos pivotear
la matriz respecto de la entrada de la fila y columna .

Cambio en la función objetivo

El valor de la función en la solución básica original es




Al evaluar la función en la nueva solución      obtenemos




Por lo tanto, si la expresión                                    es negativa, entonces el valor de     decrece.

Por lo tanto, deseamos elegir     de modo que              .

Estamos listos para enunciar el método Simplex.

Método simplex

  1.   Empezamos con una solución básica factible respecto a las columnas           .
  2.   Si todos los valores  son no negativos hemos encontrado la solución, de lo contrario elegimos tal
       que           .
  3.   Si todos los valores       para todo , entonces el problema es no acotado y no tiene solución. De
       lo contrario hallamos




       (la columna que saldrá de la base).
  4.   Pivoteamos la matriz aumentada respecto de la entrada
  5.   Repetimos desde el paso 2.

Notemos que, el método requiere empezar con una solución básica factible. Sin embargo, es posible que no sea
obvio saber cuáles de las columnas elegir para tener esta solución inicial. Por ello podemos requerir de algunas
variables auxiliares.

Método simplex en 2 pasos

Dado el problema estándar




                                                           10
                                                              UTEC / Módulo 4: Optimización con restricciones




Donde       tiene rango     y          , es posible que la matriz no sea canónica respecto de ninguna base.
Para poder aplicar el Método Simplex, usaremos variables auxiliares: una variable por ecuación, de modo que,
la matriz identidad aparezca en las últimas      columnas.

Ejemplo: En el siguiente problema




La matriz aumentada es




La cual no es canónica. Para convertirla en canónica, agregamos 2 variables   y     y convertimos al sistema
de ecuaciones en




De modo que, la matriz aumentada se convierte en




Que ya es canónica. Lógicamente, estos 2 problemas no son equivalentes, pero, si este último sistema tiene
soluciones básicas factibles donde las variables y  son iguales a cero, entonces tendremos una solución
básica factible para el sistema original.

Por lo tanto, antes de empezar con el Método Simplex, podemos resolver el problema auxiliar




En cuya solución debemos tener                  . Luego de aplicar el método simplex a este problema,

consideraremos la matriz obtenida y la base obtenida. Luego eliminaremos las columnas correspondientes a
   y    , y aplicaremos el método simplex al problema original.

4.2. Multiplicadores de Lagrange

En esa sección, consideraremos funciones que no necesariamente son lineales, pero restricciones únicamente
dadas por igualdades. Por ejemplo, consideremos el problema de hallar el máximo y el mínimo de




                                                     11
                                                              UTEC / Módulo 4: Optimización con restricciones




restringida a




Podemos graficar la restricción en el dominio de




                                                   Figura 3

¿Qué punto              nos daría el máximo valor de f restringido a   ?, ¿qué punto nos daría el mínimo?

Para ello, podemos observar las curvas de nivel de f que son circunferencias con ecuaciones




                                                   Figura 4

Podemos ubicar el valor máximo y el valor mínimo que puede tomar            de modo que la curva de nivel
intersecte a la elipse.




                                                   Figura 5



                                                      12
                                                                UTEC / Módulo 4: Optimización con restricciones




El valor máximo ocurre en los puntos          y        . El valor mínimo ocurre en los puntos        y        .

Si tuviésemos solo una restricción, el problema sería de la forma



Sujeto a



La idea para resolver este problema es encontrar los conjuntos de nivel de              que sean tangentes a




En los puntos de tangencia,                   es paralelo a                 . Es decir, si                    ,
entonces existe un      tal que




En dos dimensiones tendríamos el siguiente gráfico




                                                   Figura 6

Problema con varias restricciones

Sean                           funciones de clase          . El problema consiste en hallar el mínimo de




sujeto a las restricciones




                                                      13
                                                             UTEC / Módulo 4: Optimización con restricciones




Condiciones de primer orden

Si el problema con varias restricciones tiene solución en un punto     tal que                          son
vectores linealmente independientes, entonces existen              tales que




Esta condición es la condición de primer orden de Lagrange. Cuando resolvamos el sistema de ecuaciones
resultante (note que es una igualdad de vectores) entonces habremos hallado a un candidato para ser mínimo.

Para poder saber si dicho candidato es un mínimo local debemos considerar las condiciones de segundo
orden. Para ello necesitamos las siguientes definiciones.

Espacio tangente y espacio normal

Dadas las restricciones




Decimos que un punto      es regular si




son vectores linealmente independientes.

Definimos entonces al espacio normal como




Es decir, el espacio generado por los vectores gradientes. Definimos además al espacio tangente como el
espacio de todos los vectores perpendiculares al espacio normal, es decir




Función Lagrangiana

La función Lagrangiana es




Notemos que es una función de             variables.




                                                       14
                                                                      UTEC / Módulo 4: Optimización con restricciones




Las condiciones de primer orden de Lagrange indican que si existe un mínimo local en                , entonces existen

multiplicadores     de modo que la derivada del Lagrangiano es igual a cero




Matriz Hessiana respecto a



Donde es la matriz Hessiana de         y        es la matriz Hessiana de     . Ahora si estamos listos para determinar
si un punto será un mínimo local.

Condiciones de segundo orden

Sean                    tales que      es un punto regular. Si se cumplen

  1.

  2.   Para todo                       se cumple

Entonces      tiene un mínimo local sujeto a las restricciones en el punto         .

4.3. Condiciones de Karush-Kuhn-Tucker

Consideraremos ahora problemas que pueden tener inecuaciones




En esta sección estudiaremos condiciones análogas a las de Lagrange para resolver estos problemas. Estas
condiciones son las de Karush-Kuhn-Tucker.

Restricciones activas

Las restricciones dadas por inecuaciones pueden ser activas o inactivas

Decimos que                es activa en        si               , de lo contrario decimos que es inactiva. Sea      el

conjunto de restricciones activas en       .




                                                           15
                                                                     UTEC / Módulo 4: Optimización con restricciones




Punto regular

Un punto         es regular si



Son linealmente independientes.

Condiciones de primer orden

Si        es un mínimo local del problema y es un punto regular, entonces existen        y    tales que

     1.

     2.

     3.

De modo que, en las condiciones inactivas tenemos                .

4.4. Convexidad

Los métodos de optimización que hemos visto en módulos anteriores convergen a puntos donde se anula el
gradiente, pero no podemos garantizar que sean mínimos locales o globales.

Similarmente, con las condiciones de Lagrange o Karush-Kuhn-Tucker, hemos visto cómo poder obtener
mínimos locales para problemas con restricciones, pero no mínimos globales.

Veremos que, si podemos garantizar la convexidad de la función objetivo y sus restricciones (si las hubiere)
entonces podremos garantizar que hemos obtenido mínimos globales.

En esta sección veremos qué significa que una función sea convexa, cómo verificarlo y cuál es su importancia.

Conjuntos convexos

            es un conjunto convexo si para cualquier par de punto                   se cumple que




Es decir, el segmento de recta que une a los puntos          y       debe pertenecer al conjunto       . En la figura

observamos subconjuntos de          . El conjunto de lado izquierdo es convexo y el del lado derecho no lo es.




                                                        16
                                                                UTEC / Módulo 4: Optimización con restricciones




                                                   Figura 7

Función convexa

                  es una función convexa si el conjunto       es convexo y además




Condición para convexidad

Si    es una función de clase   tal que su matriz Hessiana es positivo semi-definida (tiene todos sus valores
propios no negativos), entonces   es convexa.

Importancia

  •   Si    es convexa y     es un mínimo local, entonces es un mínimo global.
  •   Si    es convexa y               , entonces    es un mínimo global.

En un problema con restricciones




  •   Si               y            son funciones convexas y si     cumple las condiciones de Kuhn Tucker de

      primer orden, entonces       es un mínimo global.

4.5. Aplicación a máquinas de soporte vectorial

Veremos una aplicación de las técnicas estudiadas en este modulo a las máquinas de soporte vectorial (SVM).
Similar a las regresiones logísticas, las SVM nos permiten clasificar data en dos categorías.




                                                      17
                                                               UTEC / Módulo 4: Optimización con restricciones




Empezaremos estudiando cómo encontrar un hiperplano que separe a dos conjuntos de puntos en el espacio
    y luego veremos cómo encontrar el hiperplano que separe a estos conjuntos de modo que el margen sea
el máximo posible.

El caso del separador de máximo margen corresponde a un caso básico de máquinas de soporte vectorial. Para
poder entrenar estos modelos veremos cómo plantear el problema como un problema de optimización con
restricciones y construiremos el problema dual.

Hiperplanos

Un hiperplano en      es la generalización de una recta o un plano. Está definido por una ecuación lineal



El vector




es el vector normal al hiperplano    .

Data separable por un hiperplano

Dadas observaciones que pertenecen a dos clases: 1 o -1, estas son separables por un hiperplano si las
observaciones de una clase quedan a un lado del hiperplano y las de la otra clase, al otro lado. Notemos que
pueden existir infinitos hiperplanos que separen a una data.

En la figura mostramos data separable por una recta.




                                                   Figura 8




                                                       18
                                                                      UTEC / Módulo 4: Optimización con restricciones




La data que da lugar a la gráfica es de la forma


                                                   x1            x2              y
                                  0          -0.117655        -0.657773          -1
                                   1        -1.332025         -0.494892          -1
                                   2        0.983396          0.156848           1
                                   3        0.510020          0.918294           1
                                  4         -0.240129         0.798667           1


Donde el color rojo corresponde a           y el azul,           .

¿Cómo hallar rectas que separen a los puntos?

La ecuación de una recta en      puede ser escrita como sigue



Si definimos la función



deseamos




Por lo tanto, todas las observaciones quedan correctamente clasificadas si el producto                    es siempre
positivo.

Caso de varias variables

En el caso de varias variables la data se puede almacenar en las matrices




Donde cada                  . Podemos definir




                                                         19
                                                               UTEC / Módulo 4: Optimización con restricciones




La observación      está clasificada incorrectamente si



donde      representa el vector determinado por la fila de la matriz     . Si   el conjunto de observaciones
clasificadas incorrectamente, entonces deseamos minimizar




donde la suma se da sobre las observaciones incorrectamente clasificadas. Podemos expresar esta cantidad
en términos de los coeficientes




El mínimo de esta función es 0 si podemos separar a la data perfectamente. Para aplicar el método de gradiente
descendiente, podemos hallar las derivadas parciales




Usaremos una variación de este método.

Gradiente estocástico

Para calcular el gradiente de la función necesitamos de toda la data, sin embargo, podemos aproximar el
gradiente con un subconjunto aleatorio de la data. En particular podríamos considerar un solo punto y, en caso
de tener una observación mal clasificada considerar las aproximaciones




y si está bien clasificada




Consideraremos estas aproximaciones en lugar del vector gradiente. Para aplicar el método, en cada iteración
elegiremos una fila de la data aleatoria y realizaremos un paso en la dirección (considerando un tamaño de
paso). Repetiremos este proceso hasta alcanzar la convergencia.




                                                          20

                                                                 UTEC / Módulo 4: Optimización con restricciones




Hiperplano de máximo margen

En la figura, los puntos negros son los más cercanos de cada una de las clases a la recta. Esta distancia es el
margen de la recta.

Consideraremos ahora el problema de obtener el hiperplano de modo que el margen sea máximo. Formularemos
este problema como un problema de optimización con restricciones.




                                                   Figura 9

Distancia de un punto a un hiperplano

La distancia dirigida de un punto    al hiperplano de ecuación                   es




Máximo margen

Buscamos un hiperplano de modo que las distancias de todos los puntos hacia la recta tengan un valor mayor
o igual que




Por lo tanto, el problema de optimización para hallar el máximo margen es




                                                      21
                                                                 UTEC / Módulo 4: Optimización con restricciones




Dado que, podemos reescalar el vector       podemos asumir                  y por lo tanto podemos convertir el
problema en




El cual es equivalente a




Este es el problema de optimización con restricciones que debemos resolver para hallar los coeficientes del
hiperplano. Sin embargo, podemos usar el problema dual que nos brinda una forma un poco más sencilla.

Problema dual

Dado el problema




el problema dual corresponde a



y es equivalente al original en el caso en que la función  sea convexa, las restricciones lineales y exista algún
punto en la región factible. Este es el caso que tenemos para nuestro problema de optimización.

Problema dual para SVM

Luego de operar según la definición de un problema dual podemos llegar a




                                                       22
                                                                UTEC / Módulo 4: Optimización con restricciones




Este problema es un problema en las variables     y luego de resolverlo debemos ser capaces de hallar     . La
fórmula que los relaciona es




Los vectores son aquellos tales que         . En este caso se cumple la igualdad                       . Y con
esta igualdad podemos hallar    .




   Resumen

En este módulo, hemos estudiado cómo resolver problemas de optimización con restricciones. Empezamos
con el método simplex para el caso de programación lineal. Además de este método existen otros métodos que
se pueden aplicar a dichos problemas.

Luego las condiciones de Lagrange para problemas con restricciones dadas por igualdades; y las condiciones
de Karush-Kuhn-Tucker para restricciones dadas por una mezcla de igualdades y desigualdades.

Definimos también lo que es la convexidad de una función y cómo el saber que una función es convexa
nos permite asegurar la existencia de un mínimo si encontramos un punto donde el gradiente se anule.
Similarmente, podemos garantizar que un punto que cumpla las condiciones de Karush-Kuhn-Tucker es un
mínimo si la función objetivo y sus restricciones son convexas.

Finalmente, describimos el problema de optimización que determina a los coeficientes de un hiperplano de
máximo margen y su problema dual. Este modelo corresponde a máquinas de soporte vectorial (SVM).




   Conclusiones


          El método simplex nos permite resolver problemas de programación lineal.

          Las condiciones de Lagrange nos permiten analizar problemas con restricciones dadas por
          igualdades.

          Las condiciones de Karush-Kuhn-Tucker nos permiten analizar problemas con restricciones dadas
          por igualdades y desigualdades.

          El estudio de la convexidad de las funciones nos permite analizar la existencia de mínimos globales.

          Para estimar los coeficientes del hiperplano de máximo margen podemos considerar un problema
          de optimización con restricciones.



                                                     23
                                          UTEC / Módulo 4: Optimización con restricciones / Glosario




03.            Glosario

  Región factible: es el conjunto de puntos que satisfacen las restricciones de un problema.

  Espacio generado: el espacio generado por un conjunto de vectores                  se denota por
                y es el espacio de todas las posibles combinaciones lineales.

  Vectores linealmente independientes: un conjunto de vectores                      es linealmente
  independiente si ninguno de ellos es una combinación lineal de los otros.

  Rango de una matriz: luego de aplicar reducción Gaussiana, es el número de pivotes. Este
  número brinda la cantidad de columnas (o filas) linealmente independientes que tiene la matriz.

  Hiperplano: es la generalización de un plano a más dimensiones. Se define por una ecuación
  lineal en varias variables.




                                           24
            UTEC / Módulo 4: Optimización con restricciones / Bibliografía y webgrafía / Enlaces de interés




04.              Bibliografía y webgrafía

  Chong, E. K., & Zak, S. H. (2004). An introduction to optimization. John Wiley & Sons.

  Hastie, T., Tibshirani, R., & Friedman, J. (2017). The elements of statistical learning: Data mining,
  inference, and prediction, second edition (2nd ed.). New York, NY: Springer.

  James, G., Witten, D., Hastie, T., & Tibshirani, R. (2017). An introduction to statistical learning: With
  applications in R (1st ed.). New York, NY: Springer. Disponible en https://www.statlearning.com/




05.              Enlaces de interés

  Enlace: https://es.wikipedia.org/wiki/George_Dantzig
  Descripción: artículo George Dantzing, creador del método simplex.

  Enlace: https://youtu.be/uh1Dk68cfWs
  Descripción: video que explica visualmente las condiciones de KKT y la idea del problema dual de
  un problema de optimización con restricciones.

  Enlace: https://youtu.be/_YPScrckx28
  Descripción: video que explica brevemente los modelos de SVM.




                                               25
