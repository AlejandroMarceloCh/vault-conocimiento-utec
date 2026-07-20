---
curso: ACD
titulo: [2025] U3_T2 Data Cleaning Nivel 3 Detectar
slides: 35
fuente: [2025] U3_T2 Data Cleaning Nivel 3 Detectar.pdf
---

Data Cleaning Nivel 3: Detectar

       DS3021 Análisis Computacional de Datos




                                         Mg. José Espinoza Melgarejo
¿Qué sabemos de esta marca?
Sabían que ….


En abril de 2018, Samsung Securities (la rama de negociación de acciones
de la corporación Samsung) distribuyó accidentalmente acciones por valor de
alrededor de 105 mil millones de dólares a sus empleados, 30 veces
más acciones que el número real de acciones en circulación totales.
                                      ¿Qué sucedió?

●   Un empleado cometió un “typo” (typographical error). Se
    refiere a un error involuntario al escribir, como una letra
    mal col) y en lugar de escribir “won” (moneda coreana)
    escribió “acciones”.
●   Como resultado, se emitieron 2800 millones de
    acciones (por un valor de 105 mil millones de dólares)
    como pago a los empleados.
●   La empresa tardó 37 minutos en darse cuenta de lo
    sucedido y evitar que los empleados vendieran “acciones
    fantasmas”. Sin embargo, durante ese periodo, 16
    empleados vendieron 5 millones de acciones por un
    valor de alrededor 187 millones de dólares.
¿Cuáles fueron las consecuencias?


         ●   Las acciones cayeron casi un 12%, eliminando alrededor de
             300 millones de dólares de su valor de mercado.
         ●   Pérdida de relaciones con clientes importantes, incluido el
             fondo de pensiones más grande de Corea del Sur, debido a
             “preocupaciones” por medidas de seguridad deficientes.
         ●   Los reguladores financieros le prohibieron aceptar nuevos
             clientes durante seis meses.
         ●   El codirector ejecutivo Koo Sung-Hoon renunció.
¿Cómo se hubiese evitado?
RECAPITULANDO      Técnicas de Preprocesamiento

                                Limpieza de los datos. Remover      ruido   y   corregir
                Data Cleaning
                                inconsistencias en los datos.


                                Mezcla data de diferentes recursos dentro de un
            Data Integration    almacenamiento coherente de datos (por ejemplo, data
                                warehouse, etc.).



                                Reducir el tamaño de los datos. Por ejemplo, agregar,
            Data Reduction
                                eliminar características redundantes, etc.




                 Data
                                Normalización puede ser aplicada.
            Transformation
RECAP                                         Pasos Data Cleaning
                                                              Nivel 1: Limpiar cómo luce la tabla
                                                              Se realiza la limpieza en base a las siguientes 3
                                                              características:
                                                                  ●      Estructura de datos estándar
                                                                  ●      Las columnas tienen nombres
                                                                         codificables e intuitivos
                                                                  ●      Cada fila tiene un identificador único




                                                                    Nivel 3: Evaluar y corregir valores
 Nivel 2: Reestructuración y                                        Este nivel de limpieza tiene que ver con la
 reformulación de la tabla                                          exactitud y existencia de los valores
 Este nivel de limpieza tiene que ver con el tipo                   registrados en el dataset. En este nivel de
 de estructura de datos y formato en el que                         limpieza, desea asegurarse de que los valores
 necesita que esté el dataset para que se                           registrados sean correctos y se presenten de la
 puedan realizar el análisis que se tiene en                        manera que mejor respalde los objetivos
 mente.                                                             analíticos. Aquí se evalúa la presencia de:
                                                                        ●      valores faltantes
                                                                        ●      outliers
Objetivo de sesión
                     Identificar y reconocer la importancia del
                     proceso de limpieza de datos a nivel III.
                     Especialmente centrado en el primer
                     factor, los datos faltantes.
                      Data Cleaning Nivel 3
El objetivo de este nivel es asegurarse que los datos sean correctos y apropiados.

Los tres usuales problemas relacionados a los datos registrados son:
 ● Valores Faltantes
 ● Outliers
 ● Errores
1.
     Valores Faltantes
     Definición
Los valores faltantes en un dataset son como las piezas de un
rompecabezas que se pierden.




                Nuestro objetivo es encontrar esas piezas faltantes y decidir
                                                       qué hacer con ellas.
            Valores Faltantes

En el contexto de un dataframe, son celdas vacías. En Python,
los valores faltantes se representan vía NaN (Not a Number).




Ejemplo de dataset con valores      Ejemplo de dataframe en Python
          faltantes                      con valores faltantes
    Problemas asociados a Valores Faltantes


●   Los valores faltantes pueden hacer que si usamos la data para la fase de
    modelamiento, el modelo esté sesgado si no se manejan con cuidado.
●   Hay una pérdida de poder estadístico cuando nos faltan valores. Significa que
    influye negativamente en la probabilidad de que la prueba de hipótesis rechace la
    hipótesis nula cuando no es válida.
●   Se hacen inferencias incorrectas, análisis, etc.
2.
 Valores Faltantes
 Diagnóstico
        Tipos de Valores Faltantes


1             Missing Completely at Random (MCAR)




    2                           Missing at Random (MAR)




          3                                Missing not at Random (MNAR)
     Tipo 1: Missing Completely at Random (MCAR)

Los valores faltantes son completamente aleatorios y no dependen de ninguna variable
observada o no observada en el dataset.


Ejemplo:                       Impacto:                      Efecto si lo
                                                             ignoramos:




Un sensor de temperatura       No introduce sesgo, pero      No hay ningún efecto sobre
que ocasionalmente falla sin   reduce la cantidad de datos   las inferencias (estimaciones
ningún patrón identificable    disponible.                   imparciales), aunque podría
                                                             reducir el poder estadístico.
                   Tipo 2: Missing at Random (MAR)

Los valores faltantes dependen de alguna variable observada, pero no de la variable con el
valor faltante en sí.


Ejemplo:                         Impacto:                        Efecto si lo
                                                                 ignoramos:




                                 Introduce sesgo si no se
Los    ingresos    de    los     maneja adecuadamente, pero
encuestados pueden faltar        puede ser corregido si la        Las inferencias y predicciones
más frecuentemente para los      variable asociada está bien      están sesgadas.
encuestados más jóvenes.         entendida.
             Tipo 3: Missing Not at Random (MNAR)

Los valores faltantes dependen de la variable con el valor faltante en sí.



Ejemplo:                            Impacto:                           Efecto si lo
                                                                       ignoramos:




Las personas con ingresos
muy altos pueden no querer
revelar sus ingresos, lo que        Introduce sesgo significativo y     Las inferencias y predicciones
lleva a una falta de datos en       es el más difícil de tratar.        están sesgadas.
esa variable específica.
TU TURNO

Ingresa al enlace https://www.menti.com/ y responde a la
pregunta planteada por el docente.
U3_L3
DCNivel3_MissingValues1
Cierre de la Sesión

●   ¿Cuál es el objetivo principal del Nivel 3 de
    la Limpieza de Datos?
●   ¿Cuáles son los tipos de valores faltantes?
3.
 Valores Faltantes
 Manejo
Objetivo de sesión
                     Identificar las estrategias para manejar los
                     datos faltantes en datasets teniendo en
                     consideración su tipología.
Una vez detectado la presencia de
datos faltantes en nuestro dataset




                     ¿Qué hacemos?
                           Estrategias generales

                                       Ignorar   los   valores
                                       faltantes




Eliminar     filas   con                               Eliminar columnas con
valores faltantes                                      valores faltantes




           Estimar e imputar un
           valor
    Estrategia 1: Ignorar
    los valores faltantes

●   Se utiliza esta estrategia en los casos en los que
    compartirá estos datos con otras personas y no será
    necesariamente usted quien los utilizará para análisis.
    De esta manera, les permitirá decidir cómo deben
    abordar los valores faltantes en función de sus
    necesidades analíticas.

●   En segundo lugar, si tanto los objetivos de análisis de
    datos como las herramientas de análisis de datos que
    utilizará pueden manejar sin problemas los valores
    faltantes, mantenerlo como está es el mejor enfoque.
       Estrategia 2: Eliminar filas con
              valores faltantes

Este enfoque debe seleccionarse con mucho cuidado porque puede ir en
contra de los dos objetivos de abordar con éxito los valores faltantes:
  ● no introducir sesgos en el conjunto de datos y
  ● no eliminar información valiosa del dataset.

Por ejemplo, cuando los valores faltantes en un conjunto de datos son del tipo
MNAR o MAR, debemos abstenernos de eliminar las filas con valores
faltantes. Esto se debe a que hacerlo significa que se elimina una parte
significativamente distinta de la población del conjunto de datos.

Incluso si los valores faltantes son del tipo MCAR, primero deberíamos
intentar encontrar otras formas de lidiar con los valores faltantes antes de
eliminar las filas.
Estrategia 3: Eliminar columnas
      con valores faltantes
Cuando la mayoría de los valores faltantes en un dataset provienen de
uno o dos atributos, podríamos considerar eliminar los atributos como
una forma de lidiar con los valores faltantes.

Por supuesto, si el atributo es un atributo clave sin el cual no se puede
continuar con el proyecto, enfrentar demasiados valores faltantes en el
atributo clave significa que el proyecto no es factible.

Sin embargo, si los atributos no son absolutamente esenciales para el
proyecto, eliminar los atributos con demasiados valores faltantes podría
ser el enfoque correcto.

TIP: Cuando el número de valores faltantes en un atributo es lo
suficientemente grande (aprox > 25%), estimar e ingresar valores faltantes
deja de tener sentido y dejar de lado el atributo es mejor que estimar los
valores faltantes.
        Estrategia 4: Estimar e imputar un valor

En este enfoque, usamos nuestro conocimiento, comprensión y herramientas analíticas para
completar los valores faltantes.

El término imputación captura la esencia de lo que esto le hace a un dataset: asignamos valor en
lugar de valor faltante sabiendo que esto podría causar sesgo en nuestro análisis.
Si los valores faltantes son del tipo MCAR o MAR y la analítica que hemos elegido no puede
procesar el dataset con valores faltantes, imputar los valores faltantes podría ser el mejor enfoque.
          Estrategia 4: Estimar e imputar un valor

Existen cuatro métodos generales para estimar el reemplazo de los valores faltantes:

  ●   Imputar con la tendencia central general (media, mediana o moda). Esto es mejor para
      los valores faltantes de MCAR.
  ●   Imputar la tendencia central de un grupo de datos más relevante a los valores
      faltantes. Esto es mejor para los valores faltantes de MAR.
  ●   Análisis de regresión. No es ideal, pero si tenemos que proceder con un conjunto de
      datos al que le faltan valores MNAR, este método es mejor para dicho conjunto de datos.
  ●   Interpolación. Cuando el conjunto de datos es un conjunto de datos de series temporales
      y los valores faltantes son del tipo MCAR.
TU TURNO
Ingresa al enlace https://www.menti.com/ y responde a la
pregunta planteada por el docente.
U3_L4
DCNivel3_MissingValues2

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
