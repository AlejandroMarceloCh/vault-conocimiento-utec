---
curso: IO1
titulo: Proyecto_IO1_2025_1_con_instrucciones
slides: 5
fuente: Proyecto_IO1_2025_1_con_instrucciones.pdf
---

Recolección de pedidos en un almacén:
Selección de órdenes y pasillos
En empresas de comercio electrónico y distribución a gran escala, cada orden
generada por un cliente está asociada a un plazo de entrega definido por los
compromisos de servicio. Desde su creación hasta su entrega final, una orden atraviesa
múltiples procesos logísticos. En este proyecto, nos enfocamos específicamente en el
proceso de recolección (picking) dentro del almacén. Las órdenes que aún no han sido
atendidas y permanecen pendientes de recolección conforman el backlog, un conjunto
dinámico que se actualiza constantemente a medida que ingresan nuevas órdenes y se
atienden otras.

Para organizar la recolección de manera eficiente, las órdenes del backlog se agrupan
en un wave, es decir, un subconjunto de órdenes que se recolectan conjuntamente. Al
definir el wave, se diseña un recorrido único en el almacén que permite recolectar, en
un solo trayecto, todos los ítems solicitados. Esto reduce los desplazamientos
innecesarios entre pasillos y mejora la eficiencia operativa.


Datos
     Conjunto de órdenes: O = {1, 2, 3, . . . , |O|}

     Conjunto de ítems: I = {1, 2, 3, . . . , |I|}

     Conjunto de pasillos: P = {1, 2, 3, . . . , |P |}

     roi : Cantidad de unidades del ítem i ∈ I requeridas por la orden o ∈ O.

     upi : Cantidad de unidades del ítem i ∈ I disponibles en el pasillo p ∈ P .

     LB, U B: Límites inferior y superior para el número total de unidades en el wave.


Consideraciones
     Cada wave está definido por un subconjunto Ow ⊆ O de órdenes y un subconjunto
     Pw ⊆ P de pasillos donde se recolectan los productos pedidos en Ow .

     En un wave, la demanda total del ítem i ∈ I corresponde al número de unidades
     requeridas de ese ítem en todas las órdenes seleccionadas Ow .

     Para cada ítem i ∈ I, la cantidad total de unidades recolectadas desde todos los
     pasillos de Pw debe ser igual a la demanda total de ese ítem en Ow .
     La cantidad recolectada del ítem i ∈ I en un pasillo p ∈ P no puede ser mayor que
     la cantidad disponible de ese ítem en dicho pasillo.

     La cantidad total de unidades recolectadas en un wave debe estar dentro del
     rango definido por LB y U B.

     La demanda total del ítem i ∈ I en un wave no puede superar la cantidad total
     disponible de ese ítem en todos los pasillos del almacén.


Objetivo
Maximizar el promedio de unidades recolectadas en un wave por pasillo visitado, es
decir, maximizar:
                                       ∑∑
                                                roi · xo
                                      o∈O i∈I
                                           ∑
                                                yp
                                          p∈P


donde:

     xo = 1 si la orden o ∈ O es seleccionada en el wave, 0 en caso contrario.

     yp = 1 si el pasillo p ∈ P es visitado, 0 en caso contrario.



           Instancia   Valor Objetivo                 Instancia   Valor Objetivo

               1            15.00                          11         16.85
               2             2.00                          12         11.25
               3            12.00                          13        117.38
               4             3.50                          14        181.64
               5            117.88                         15        149.33
               6            691.00                         16         85.00
               7            392.25                         17         36.50
               8            162.94                         18        117.20
               9             4.42                          19        202.00
               10           16.58                          20         5.00

                Cuadro 1: Mejor valor objetivo encontrado por instancia
Trabajo solicitado
Desarrollar e implementar un método heurístico utilizando el Tabu Search para construir
un único wave que maximice el promedio de unidades recolectadas por pasillo visitado.
Se permite complementar el método heurístico con técnicas exactas (por ejemplo:
programación lineal entera) si se considera que pueden mejorar la calidad o eficiencia
de la solución.


Sistema de evaluación
El trabajo se evalúa sobre 5 criterios:

     Presentación del informe: 10 %

     Presentación oral y preguntas:

         • Planteamiento del algoritmo de generación de solución(es) inicial(es): 15 %
         • Definición, caracterización y planteamiento de la(s) vecindad(es): 30 %
         • Planteamiento del método metaheurístico Tabu Search: 30 %
         • Utilización de los conceptos vistos en sesiones teóricas y de práctica: 15 %


Presentación del informe
Presentación clara y precisa del proyecto. Lógica justificada de los algoritmos
planteados. Reconocimiento de las potencialidades y limitaciones de los algoritmos
planteados. Los algoritmos planteados demuestran claramente la creatividad del
trabajo, la búsqueda de métodos más sofisticados a través de un pensamiento lógico
profundizado y de una revisión de la literatura científica relacionada al proyecto o a las
técnicas de resolución de problemas similares. Código claro, estructurado, con
comentarios adecuados. Resultados correctamente analizados.


Presentación oral y preguntas
Planteamiento del algoritmo de generación de solución(es) inicial(es)

Planteamiento, exposición y explicación sintética, precisa y clara del algoritmo de
generación de soluciones iniciales, reconociendo potencialidades y limitaciones del
trabajo realizado. Se demuestra creatividad e investigación para alinearse al objetivo.
En el caso de que las soluciones iniciales no sean factibles, se justifica y se explica
cómo se toma en cuenta en los otros pasos (vecindad, método metaheurístico).
Definición, caracterización y planteamiento de la(s) vecindad(es)

Planteamiento, exposición y explicación sintética, precisa y clara de la(s) vecindad(es)
planteada(s), reconociendo potencialidades y limitaciones del trabajo realizado. Se
demuestra creatividad e investigación para alinearse al objetivo.

Planteamiento del método Tabu Search

Planteamiento, exposición y explicación sintética, precisa y clara de un algoritmo de
tabu search, reconociendo potencialidades y limitaciones del trabajo realizado. Se
demuestra creatividad e investigación para alinearse al objetivo.

Utilización de los conceptos vistos en clase

Demuestra un excelente dominio de los conceptos vistos en teoría y práctica, relaciona
de manera precisa y clara, con un vocabulario preciso y adaptado esos conceptos con
el trabajo realizado.


Informe

General
      La entrega final consiste en un archivo PDF describiendo los algoritmos y
      presentando las ideas implementadas y los resultados obtenidos.

      Describir el aporte y el porcentaje de participación de cada integrante del grupo.

      La nota final individual por integrante estará en función a la calidad del trabajo y el
      desempeño personal durante la presentación final.

      Revisar eventuales recursos publicados en Canvas.

El proyecto debe ser desarrollado solamente por los integrantes del grupo. El diseño,
código y resultados deben ser de creación exclusiva de los integrantes del grupo.
Cualquier situación de plagio será sancionada con un cero (0) para todos los
integrantes de los grupos involucrados, además de ser debidamente reportada.


Código C++ o Julia
      El diseño de los algoritmos debe satisfacer los siguientes criterios:

         • Descomposición en funciones cortas y específicas (∼ 15 líneas max). Toda
           la lógica está contenida en funciones. Todas las variables utilizadas en las
           funciones son declaradas localmente.
         • Reproducibilidad:
            ◦ En el caso de programar en C++, sólo se pueden utilizar librerías
              estándares ISO C++11, C++14, C++17 o C++20 compatibles tanto con
              Windows, Linux y MacOS. El archivo entregado debe contener todos los
              archivos del código fuente para permitir la compilación sin instalar
              ninguna otra librería no estándar.
            ◦ En el caso de programar en Julia, el archivo entregado debe contener
              todos los archivos del código fuente para permitir su ejecución sin
              ninguna modificación.
        • Documentación: Explicaciones claras y precisas donde se necesitan (no
          comentar todas las líneas del código).
        • Legibilidad de las funciones y estructura (convenciones, indentación, etc).
          Los nombres de las funciones y variables tienen un significado real y conciso.


Exposición oral
La exposición del trabajo es una evaluación en dos pasos con aproximadamente 10
minutos de exposición y 15 minutos de preguntas.
En la exposición, se debe explicar de manera sintética, clara y precisa:

     No se debe presentar el problema

     Concentrarse en la presentación de las ideas implementadas en los algoritmos:
     conceptos, fundamentos, descubrimientos y limitaciones.

     Análisis y discusión del desempeño de los algoritmos: calidad de soluciones,
     eficiencia de ejecución, oportunidades de mejora.


Criterios de evaluación
     Resultados concretos expresados en gráficas, tablas, diagramas u otros.

     Profundidad de análisis de soluciones y algoritmos.

     Participación individual en el desarrollo del proyecto, explicación y justificación
     de la lógica utilizada para resolver el problema.

     Dominio individual de los conceptos desarrollados en las sesiones de teoría y de
     laboratorio, con la terminología específica adquirida en el curso.


Fecha de entrega del informe
Último día de la semana 14 (viernes 11:59 pm)
