---
curso: ACD
titulo: [2025] U1_T1 Definición de Datos
slides: 41
fuente: [2025] U1_T1 Definición de Datos.pdf
---

     Definición
     de los Datos
DS3021 Análisis Computacional de Datos




                                  Mg. José Espinoza Melgarejo
Contenido aquí

1.   Definición de los
     datos




2.   Tipos de atributos
Objetivo de la sesión
                        Introducir conceptos y tipologías sobre los
                        datos que son esenciales para el pre-
                        procesamiento de datos de manera efectiva.
1.
     Definición
     de los datos
¿Qué entendemos
  por DATOS?
                                Definición de datos

Desde una perspectiva de preprocesamiento de datos:


Definimos datos como símbolos o signos que representan una medida o modelo de la realidad. Estos
símbolos y signos son inútiles en sí mismos hasta que se utilizan con respecto a convenciones y
entendimientos de nivel superior (Higher-Level Conventions and Understandings - HLCU).


Nota: HLCU es un término utilizado en la evaluación de escritura, especialmente en pruebas
estandarizadas como el TOEFL, IELTS o AP English Language and Composition.
                      ¿Por qué esta definición?


●   Para el preprocesamiento de datos, lo primero que debe
    decidir es la HLCU que utilizará.

●   Es decir, ¿para qué HLCU está preparando sus datos?
     ○ Si los datos se preparan para la comprensión
         humana, el resultado será muy diferente que cuando
         los datos se preparan para computadoras y
         algoritmos. No solo eso, la HLCU puede ser
         diferente de un algoritmo a otro.
                                                  Pirámide DIKW
                                           Data, Information, Knowledge, and Wisdom




                     Sabiduría
    Encarnación del Conocimiento y
           apreciación del por qué.
                                       1                                               Futuro
               Conocimiento                                  Juicio
        Aplicación descriptiva de la
   Información - puede responder la
                                       2
                    pregunta cómo

                                                                      Cognición
                 Información
  Data procesada - puede responder
las preguntas: quién, cuándo, dónde
                                       3
                                                                                       Pasado
                               y qué
                                                                           Procesami
                             Data                                             ento
         Colección de símbolos - no
          puede responder ninguna      4
                          pregunta
                                                  Pirámide DIKW
                                           Data, Information, Knowledge, and Wisdom




                     Sabiduría                                           Aplicado      Mejor freno y paro el carro
    Encarnación del Conocimiento y     1
           apreciación del por qué.

               Conocimiento
        Aplicación descriptiva de la                                                   Estoy rumbo a mi trabajo, el
   Información - puede responder la
                                       2                                Contexto       semáforo que tengo al frente ha
                    pregunta cómo
                                                                                       cambiado a rojo
                 Información
  Data procesada - puede responder                                                    En la esquina de Av. La Mar y
                                       3
las preguntas: quién, cuándo, dónde                                     Significado   Av. Pardo el semáforo está en
                               y qué
                                                                                      rojo a las 10 de la mañana
                             Data
         Colección de símbolos - no
          puede responder ninguna      4                                              Rojo, 192.234.235.245, true, 10
                          pregunta                                         Raw
             Pirámide DIKW
      Data, Information, Knowledge, and Wisdom




… tiene mucho sentido, sin embargo,
no es completamente aplicable para
         análisis de datos
                                             Pirámide DDPA
                                           Data, Dataset, Pattern, and Action
                                             Actualización de Pirámide DIKW para IA



                         Acción
   La decisión es hecha, la cual es
       informada por los patrones      1
                     reconocidos                                                        Considerar la incertidumbre de los
                     Patrones                                Análisis                   patrones reconocidos y llegar a
           Tendencias y relaciones                          de riesgo                   una decisión
    interesantes y útiles dentro del
                                       2
                            dataset
                                                                                        Aplicar minería de datos para
                                                                        Minería         encontrar patrones.
                       Dataset
Colección de datos seleccionados
                                       3
 de recursos disponibles, limpios y
organizados para el siguiente paso                                             Pre-     Seleccionar los datos relevantes y
                                                                            procesami   preparación para el siguiente paso.
                             Data                                              ento
   Todos los datos posibles desde
                                       4
      todos los recursos de datos
Pirámide para Análisis de Datos
       = DIKW + DDPA
                                                 Pirámide DDVW
                                          Data, Dataset, Visualization, and Wisdom
                                          Actualización de Pirámide DIKW para Data Analytics



                    Sabiduría
   Encarnación del Conocimiento y     1
          apreciación del por qué.


              Visualización                                         Juzgar
La presentación comprensible de lo
que se ha encontrado en el dataset    2

                                                                             Analizar
                       Dataset
Colección de datos seleccionados
                                      3
 de recursos disponibles, limpios y
organizados para el siguiente paso                                                  Pre-
                                                                                 procesami
                            Data                                                    ento
    Todos los datos posibles desde
                                      4
       todos los recursos de datos
Cuando realizamos análisis de datos usamos la
tecnología para:


 1.   Explorar el dataset
 2. Testear la hipótesis
 3. Reportar los findings relevantes.



Recuerda: No es lo mismo hacer pre-procesamiento
           para ML que Data Analytics
¿Cuál es la estructura de datos
        más universal?
                           Una Tabla
                                       Data Attributes



                   Columna 1   Columna 2    .            .   .   Columna n

          Fila 1   xxx         xxx          .            .   .   xxx

          Fila 2   xxx         xxx          .            .   .   xxx
  Data
Objects   .        .           .            .            .   .   .

          .        .           .            .            .   .   .

          .        .           .            .            .   .   .

          Fila n   xxx         xxx          .            .   .   xxx

                               Data Value
    Data Objects

●   Data Objects también son llamados:
      ○ Data points,
      ○ Filas
      ○ Records,
      ○ Ejemplos,
      ○ Tuplas, y más.
●   La definición de data objects es la entidad, concepto, fenómeno o
    evento que todas las filas comparte.
                            Data Attributes

●   Las columnas de una tabla son llamadas atributos.

●   Los data attributes representan características o rasgos de
    los data objects en una tabla. Cada atributo describe algo
    sobre todos los data objects.

●   Los sustantivos: atributo, dimensión, característica y variable
    a menudo se usan indistintamente en la literatura.
      ❏ Dimensión: Comúnmente usado en data warehousing.
      ❏ Característica (feature): Usado en la literatura de
         Machine Learning
      ❏ Variable: Usado en estadística
      ❏ Atributo: Usado en data mining, data analytics y base
         de datos.
                                 Data Values


Para realizar un pre-procesamiento de datos exitoso necesitamos entender los diferentes tipos
de data values desde dos perspectivas: análitica y programación.


El tipo de los valores de datos genera el tipo de atributo es por ello que se puede encontrar
como Tipo de Datos o Tipo de Atributos en la literatura.
2.
 Tipos de Atributos
 Percepción Análitica

                        Tipos de Atributos
                         Percepción Análitica

                                Proporción
                  Numérico

                                 Intervalo
Data Attributes

                                 Ordinal                     Simétrico
                  Categórico                     Binario
                                 Nominal                     Asimétrico
                                                No Binario
Nominal
(Categórico)
                     Atributos Nominales
●   Nominal está relacionado a “nombres”.
●   Los valores de un atributo nominal son símbolos o nombres de cosas. Cada valor
    representa algún tipo de categoría, código o estado.
●   Los valores de un atributo nominal no tienen ningún orden significativo. También se
    conocen como enumeraciones.
                       Atributos Nominales


                                              Mascu   M     0       1         1
                                              lino

                                              Femen   F     1       0         2
                                              ino

                               Estado civil       Diferentes presentaciones
    Color de cabello
                                                    del atributo de género
●   Negro                  ●   Soltero                      nominal
●   Cafe                   ●   Casado
●   Rubio                  ●   Viudo
●   Rojo                   ●   Divorciado
●   Gris
●   Blanco
                        Tipos de Atributos
                         Percepción Análitica

                                Proporción
                  Numérico

                                 Intervalo
Data Attributes

                                 Ordinal                     Simétrico
                  Categórico                     Binario
                                 Nominal                     Asimétrico
                                                No Binario
                         Atributos Binarios
●   Un atributo binario es un atributo nominal con solo dos categorías o estados: 0 o 1,
    donde:
      ○   0 normalmente significa que el atributo está ausente y
      ○   1 significa que está presente.
●   Los atributos binarios se denominan booleanos si los dos estados corresponden a
    verdadero y falso.
                          Atributos Binarios




                                         Suponga que un paciente se somete a un examen
Dado el atributo fumador que describe
                                         médico que tiene dos resultados posibles. El
un objeto paciente.
                                         atributo prueba médica es binario, donde un valor
 ●   1 indica que el paciente fuma,
                                         de
 ●   0 indica que el paciente no fuma.
                                          ●   1 significa que el resultado de la prueba para el
                                              paciente es positivo,
                                          ●   0 significa que el resultado es negativo.
           Atributos Binarios: Simétrico y
                     Asimétrico
●   Un atributo binario es simétrico si ambos estados son igualmente valiosos y tienen el
    mismo peso; es decir, no hay preferencia sobre qué resultado debe codificarse como 0 o 1
     ○   Un ejemplo de ello podría ser el atributo género que tiene los estados masculino y
         femenino.
●   Un atributo binario es asimétrico si los resultados de los estados no son igualmente
    importantes, como los resultados positivos y negativos de una prueba médica para el VIH.
     ○   Por convención, codificamos el resultado más importante, que suele ser el más raro,
         por 1 (p. ej., VIH positivo) y el otro por 0 (p. ej., VIH negativo).
Ordinal
(Categórico)
                        Atributos Ordinales
●   Un atributo ordinal es un atributo con valores posibles que tienen un orden significativo o
    una clasificación entre ellos, pero no se conoce la magnitud entre los valores sucesivos.


●   Los atributos ordinales pueden contener mayor información que un atributo nominal.
Atributos Ordinales


 Suponga que el tamaño de la bebida corresponde al tamaño de
 las bebidas disponibles en un restaurante de comida rápida.

 Este atributo nominal tiene tres valores posibles: pequeño,
 mediano y grande.

 Los valores tienen una secuencia significativa (que corresponde
 al aumento del tamaño de la bebida); sin embargo, no podemos
 decir a partir de los valores ¿cuánto más grande es un medio
 que uno grande?.
Imagen tomada de Google Images
                      Atributos Numéricos
●   Un atributo numérico es cuantitativo; es decir, es una cantidad medible, representada en
    valores enteros o reales. Los atributos numéricos pueden tener:
      ○   Una escala de intervalo o
      ○   Una escala de proporción.
Intervalo
(Numérico)
                   Atributos Intervalo

●   Estos atributos contienen más información que los atributos ordinales, ya que
    permiten la comparación de intervalos entre data objects.
●   Los datos de intervalo se miden a lo largo de una escala numérica que tiene
    intervalos iguales entre valores adyacentes.
●   Al pasar de atributos ordinales a atributos de intervalo, también pasamos de
    símbolos y categorías a números (atributos categóricos a atributos numéricos). Con
    los números viene la capacidad de saber cuánta diferencia existe entre los data
    objects.
Atributos Intervalo




                      Imagen tomada de Google Images
Proporción
(Numérico)
             Atributos Proporción (Ratio)

●   Los datos de proporción son un tipo de datos numéricos.
●   Estos datos miden variables en una escala continua, con una distancia igual entre
    valores adyacentes. Si bien comparte estas características con los datos de intervalo,
    una propiedad distintiva es que tiene un "true zero".
     ○   En otras palabras, no tienen valores negativos.
Atributos Proporción (Ratio)




                        Imagen tomada de Google Images
Tipos: Data Values

Conclusiones
 ¿Qué es un dato y cuándo adquieren valor? ¿En qué consiste la
 pirámide DIKW? ¿Cuál es la versión actualizada de dicha
 pirámide en análisis de datos?

 ¿Cuáles son los dos tipos de atributos? ¿Cómo se clasifican a la
 vez, estos tipos de atributos?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
