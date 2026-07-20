---
curso: ACD
titulo: [2025] U1_T5 Medición de Similitud de Datos-2
slides: 48
fuente: [2025] U1_T5 Medición de Similitud de Datos-2.pdf
---

          Medición de
Similitud y Disimilitud de Datos
       DS3021 Análisis Computacional de Datos




                                         Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Comprender qué técnicas o herramientas
                     existen para determinar la similitud y
                     disimilitud de los datos.
Contenido

1.   Conceptos


     Proximidad
2.   para atributos
     Nominales

     Proximidad
3.   para atributos
     Binarios
 RECAPITULANDO          Tipos de Atributos
                         Percepción Análitica

                                Proporción
                  Numérico

                                 Intervalo
Data Attributes

                                 Ordinal                     Simétrico
                  Categórico                     Binario
                                 Nominal                     Asimétrico
                                                No Binario
1.
     Conceptos de Similitud
     y Disimilitud de Datos
                   Similitud y Disimilitud
                          de Datos

En Ciencia de Datos, la medida de similitud es una forma de medir cómo se relacionan
las muestras de datos entre sí.

Por otro lado, la medida de disimilitud sirve para indicar en qué medida son distintos
los objetos de datos.


Proximidad se refiere tanto para similitud como para disimilitud
                    Similitud de Datos


●   Es una medida numérica que indica qué tan parecidos son dos objetos de datos.
     ○ A mayor valor, mayor coincidencia entre los datos.
     ○ A menudo cae en el rango [0, 1]

●   La similitud podría usarse para identificar:
      ○ Datos duplicados que pueden tener diferencias debido a errores tipográficos.
      ○ Instancias equivalentes de diferentes conjuntos de datos. Por ejemplo, nombres
          y/o direcciones que son iguales pero tienen errores ortográficos.
      ○ Grupos de datos próximos (clusters)
                 Disimilitud de Datos

●   Medida de disimilitud es una medida numérica de cuán diferentes son dos
    objetos de datos
     ○ A menor valor, mayor coincidencia
     ○ La disimilitud mínima suele ser 0, mientras que el límite superior varía
          dependiendo de cuánta variación se observe

●   La disimilitud podría usarse para identificar
      ○ valores atípicos (outliers)
      ○ excepciones interesantes. Por ejemplo, fraude de tarjeta de crédito, límites
          a los grupos, etc.
                          Matriz de Datos

Una matriz de datos (object-by-attribute structure) es una estructura que almacena n
data objects en la forma de una matriz nxp donde p es el número de atributos.


        data object




  Por ejemplo: x11 es el valor del data object 1 de la columna 1
                    Matriz de Disimilitud

Una matriz de dismilitud (object-by-object structure) es una estructura que almacena un
conjunto de proximidades para todos los pares de n data objects. Tiene la forma de una
matriz nxn.




Por ejemplo: d(i,j) es la medida de disimilitud o diferencia entre el object i y el object j.
# TO DO




          Trabajemos
          juntos
          Ejercicios 1 - 4
2.
 Proximidad para
 Atributos Nominales
              Proximidad para Atributos
                     Nominales

●    Un atributo nominal puede tener dos o más estados.
●    ¿Cómo se calcula disimilitud entre objects descritos como atributos nominales?
       ○   La disimilitud entre dos objects i y j puede ser calculado basado en la
           proporción de mismatches (no coincidencias).




    donde m es el número de matches (1 si son iguales y 0 en caso contrario) y p es el
    total de atributos nominales de la matriz de datos.
             Proximidad para Atributos
                    Nominales
La similitud de los datos nominales pueden ser calculados como:
                      Proximidad para Atributos
                             Nominales

                                                     Entonces, la      matriz   de
                                                     disimilitud es:
 Object      Atributo
Identifier   Nominal

    1        codeA

    2         codeB

    3        codeC          d(2,1) = (1 - 0)/1 = 1
                            d(3,1) = (1 - 0)/1 = 1
    4        codeA
                            d(3,2) = (1 - 0)/1 = 1
                            d(4,1) = (1 - 1)/1 = 0
                            d(4,2) = ?
                            d(4,3) = ?
# TO DO




          Trabajemos
          juntos
          Ejercicios 5 - 7
3.
 Proximidad para
 Atributos Binarios
               Proximidad para Atributos
                       Binarios

●   Recordemos que los atributos binarios pueden ser:
     ○ Simétricos
     ○ Asimétricos

●   Tratar a los atributos binarios como numéricos (1 o 0) podría llevarnos a malos
    cálculos cuando se refiere a la proximidad de datos.
                     Proximidad para Atributos
                        Binarios Simétricos
Para binarios simétricos se debe analizar los pesos de los valores. Por ejemplo a través de
una tabla de contingencia:




Sean dos data objects i y j, se define:
 ● q: el número de atributos iguales a 1 para ambos objects.
 ● r: el número de atributos que son iguales a 1 para el objeto i pero 0 para el objeto j.
 ● s: el número de atributos iguales a 0 para el objeto i y 1 para el objeto j.
 ● t: el número de atributos que son iguales a 0 para ambos objetos.
 ● p: el número total de atributos binarios donde p = q + r + s + t.
                      Proximidad para Atributos
                         Binarios Simétricos

Basados en la tabla de contingencia, la disimilitud entre los objects binarios simétricos i y j
se calcula de la siguiente manera:

                                     Ejemplo

Suponga que la siguiente tabla corresponde a los records de un paciente donde:
 ● name: es el nombre del paciente
 ● gender: es el género del paciente (binario simétrico)
 ● fever, cough: Presencia de fiebre y tos respectivamente (binario asimétrico)
 ● test-1, test-2, test-3, test-4: Resultados de pruebas donde N es negativo y P es positivo
     (binario asimétrico)
Calculando la disimilitud de atributos binarios simétricos:




                                        Calculamos:
                                        d(Jack,Jim) =
                                        d(Jack,Mary) =
Calculando la disimilitud de atributos binarios simétricos:




                                        Calculamos:
                                        d(Jack,Jim) = (0 + 0) / (0 + 0 + 0 + 1) = 0
                                        d(Jack,Mary) = (0 + 1) / (0 + 0 + 1 + 0) = 1
# TO DO




          Trabajemos
          juntos
          Ejercicios 8 - 10
                    Proximidad para Atributos
                       Binarios Asimétricos

●   Para los atributos binarios asimétricos, los dos estados no son igualmente importantes,
    como los resultados positivos (1) y negativos (0) de una prueba de enfermedad.
●   Dados dos atributos binarios asimétricos, la concordancia de dos 1s (una coincidencia
    positiva) se considera más significativa que la de dos 0s (una coincidencia negativa). Por lo
    tanto, estos atributos binarios a menudo se consideran "monarios" (que tienen un estado).
●   La disimilitud basada en estos atributos se denomina disimilitud binaria asimétrica, donde
    el número de coincidencias negativas, t, se considera sin importancia y, por lo tanto, se
    ignora en el siguiente cálculo:
                 Proximidad para Atributos
                    Binarios Asimétricos

De manera complementaria, podemos medir la diferencia entre dos atributos binarios
basándonos en la noción de similitud en lugar de disimilitud. Por ejemplo, la similitud
binaria asimétrica entre los objetos i y j se puede calcular como:




  A la fórmula anterior se la conoce en la literatura como el Coeficiente de Jaccard.
                                     Ejemplo

Suponga que la siguiente tabla corresponde a los records de un paciente donde:
 ● name: es el nombre del paciente
 ● gender: es el género del paciente (binario simétrico)
 ● fever, cough: Presencia de fiebre y tos respectivamente (binario asimétrico)
 ● test-1, test-2, test-3, test-4: Resultados de pruebas donde N es negativo y P es positivo
     (binario asimétrico)
Calculando la disimilitud de atributos binarios asimétricos:
Considere Y y P como 1 y el valor N como 0


                                             Calculamos:
                                             d(Jack,Jim) =
                                             d(Jack,Mary) =
                                             d(Jim,Mary) =
Calculando la disimilitud de atributos binarios asimétricos:
Considere Y y P como 1 y el valor N como 0


                                             Calculamos:

                                             d(Jack,Jim) = (1 + 1 ) / (1 + 1 + 1) = 0.67

                                             d(Jack,Mary) = (0 + 1 ) / (2 + 0 + 1) = 0.33

                                             d(Jim,Mary) = (1 + 2 ) / (1 + 1 + 2) = 0.75



                                             Estas mediciones sugieren que es poco probable que
                                             Jim y Mary tengan una enfermedad similar porque
                                             tienen el valor de disimilitud más alto entre los tres
                                             pares.

                                             De los tres pacientes, Jack y Mary son los que tienen
                                             más probabilidades de padecer una enfermedad similar.
# TO DO




          Trabajemos
          juntos
          Ejercicio 11
3.
 Proximidad para
 Atributos Numéricos
                  Proximidad para Atributos
                         Numéricos
●   Para medir la disimilitud entre atributos numéricos se utilizan las distancias
    Euclidiana, Manhattan y Minkowski.
●   En algunos casos, los datos se normalizan antes de aplicar los cálculos de distancia.
    Esto implica transformar los datos para que se encuentren dentro de un rango más
    pequeño o común, como [−1, 1] o [0, 1].
     ○ Considere un atributo de altura, por ejemplo, que podría medirse en metros o
          pulgadas. En general, expresar un atributo en unidades más pequeñas
          conducirá a un rango más amplio para ese atributo y, por lo tanto, tenderá a
          darle a dichos atributos un mayor efecto o “peso”.
                    Proximidad para Atributos
                           Numéricos

Distancia Euclidiana:
Sean dos objects i= (xi1 , xi2 , …, xip ) y j= (xj1 , xj2, …, xjp) descritos por p atributos. La
distancia Euclidiana entre los objects i y j es definida como:




 Distancia Manhattan:
                                   Ejemplo

 Object      Atributo   Atributo
Identifier    Num 1     Num 2
                                    Calculando la disimilitud d(2,1) es:
    1          45         15
                                    d(2,1) = sqrt( (22 – 45)2 + (19 – 15)2 )
    2          22         19        d(2,1) = sqrt( 529 – 16 )
                                    d(2,1) = sqrt( 513 )
    3          64          14
                                    d(2,1) = 22.64
    4          28         12
# TO DO




          Trabajemos
          juntos
          Ejercicio 12
4.
 Proximidad para
 Atributos Ordinales
                 Proximidad para Atributos
                         Ordinales

●   Los valores de un atributo ordinal tienen un orden o clasificación significativa,
    pero se desconoce la magnitud entre valores sucesivos.

●   Los atributos ordinales también se pueden obtener a partir de la discretización de
    atributos numéricos dividiendo el rango de valores en un número finito de
    categorías.
      ○ Estas categorías están organizadas en rangos. Es decir, el rango de un
          atributo numérico se puede asignar a un atributo ordinal f que tiene estados
          Mf .
                     Proximidad para Atributos
                             Ordinales
Suponga que f es un atributo ordinal que describe n objects. La disimilitud con respecto al
atributo involucra los siguientes pasos:

 1. Determinar el número de estados posibles M de un atributo ordinal f. Se denota como
    Mf. Por ejemplo, el atributo class(o) cuenta con 3 posibles estados (First, Second, Third).
    Por lo tanto Mf = 3.
 2. Reemplazar cada valor del atributo ordinal por su rank (numérico). Por ejemplo: First = 1,
    Second = 2 y Third = 3. De tal manera que el rankeo es rif = {1, …, Mf} = {1, 2, 3}
 3. Dado que cada atributo ordinal puede tener diferentes estados, se debe mapear el
    rango a cada atributo entre [0, 1] tal que cada atributo tiene el mismo peso. Se
    normaliza de la siguiente manera:

                                                            zif: representa el valor f para el i-ésimo object



 1.   Luego se calcula la disimilitud como para atributos numéricos
                               Ejemplo
                         1.   Dado que tiene tres atributos (excelente, requiere
 Object      Atributo         mejora, bueno). Entonces, Mf = 3.
Identifier   Ordinal
                         2. Reemplazar por su rank (numérico), entonces:
    1        excelente         ● Excelente : 3
                               ● Bueno : 2
    2        requiere          ● Requiere Mejora : 1
              mejora
                         3. Normalizar usando:
    3         bueno

    4        excelente

                              Requiere Mejora (1) = (1 – 1) / (3 – 1) = 0

                              Bueno (2) = (2 – 1) / (3 – 1) = 0.5

                              Excelente (3) = (3 – 1) / (3 – 1) = 1
                                   Ejemplo (cont)

 Object      Atributo       Valor
Identifier   Ordinal     normalizado

    1        excelente        1

    2        requiere        0
              mejora                    Encontrar d(i,j) usando distancia Euclidiana

    3         bueno          0.5
                                              d(2,1) = sqrt( (0 – 1)2 ) = 1
    4        excelente        1               d(3,1) = sqrt( (0.5 – 1)2 ) = 0.5
                                              d(4,1) = sqrt( (1 – 1)2 ) = 0

                                   Ejemplo (cont)

 Object      Atributo       Valor
Identifier   Ordinal     normalizado

    1        excelente        1

    2        requiere        0
              mejora                    Encontrar d(i,j) usando distancia Euclidiana

    3         bueno          0.5

    4        excelente        1
# TO DO




          Trabajemos
          juntos
          Ejercicio 13
5.
 Proximidad para
 Atributos Mixtos
                  Proximidad para Atributos
                           Mixtos

En las secciones anteriores hemos revisado como calcular la disimilitud entre objetos de
diferentes tipos. Sin embargo, en muchas bases de datos reales, los objetos se describen
mediante una combinación de tipos de atributos.

Entonces,

    ¿Cómo podemos calcular la disimilitud entre objetos con tipos de atributos mixtos?
                  Proximidad para Atributos
                           Mixtos

●   Un enfoque es agrupar cada tipo de atributo, realizando análisis de datos separados.
    Por ejemplo, como en minería (agrupamiento) para cada tipo. Esto es factible si estos
    análisis derivan resultados compatibles. Sin embargo, en aplicaciones reales, es poco
    probable que se pueda realizar un análisis por separado por tipo de atributo generará
    resultados compatibles.

●   Un enfoque más preferible es procesar todos los tipos de atributos juntos, realizando
    una análisis único. Una de esas técnicas combina los diferentes atributos en una sola
    matriz de disimilitud, reuniendo todos los atributos significativos en una escala común
    del intervalo [0, 1].
                    Proximidad para Atributos
                             Mixtos
Supongamos que el conjunto de datos contiene p atributos de tipo mixto. La disimilitud d(i, j)
entre los objetos i y j se define como:




                                                                              Solo numérico cambia
                                               Ejemplo

 Object      Atributo   Atributo    Atributo
Identifier   Nominal    Ordinal      Num

    1        codeA      excelente     45

    2        codeB      requiere      22
                         mejora

    3        codeC       bueno        64

    4        codeA      excelente     28




                                                 Resultado:
# TO DO




          Trabajemos
          juntos
          Ejercicio 14

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
