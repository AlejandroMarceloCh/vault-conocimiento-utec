---
curso: ACD
titulo: [2025] U3_T3 Data Cleaning Nivel 3 Outliers
slides: 20
fuente: [2025] U3_T3 Data Cleaning Nivel 3 Outliers.pdf
---

Data Cleaning Nivel 3: Outliers

       DS3021 Análisis Computacional de Datos




                                         Mg. José Espinoza Melgarejo
RECAPITULANDO
                            Data Cleaning Nivel 3
      El objetivo de este nivel es asegurarse que los datos sean correctos y apropiados.

      Los tres usuales problemas relacionados a los datos registrados son:
       ● Valores Faltantes
       ● Outliers
       ● Errores
Data Cleaning Nivel 3

      Outliers
Objetivo de sesión
                     Identificar   y   tratar   de   manera
                     computacional la presencia de outliers
                     en un conjunto de datos.
1.
     Outliers
     Definición
                                   Outliers


Los outliers (valores atípicos) son datos cuyos
valores son demasiado diferentes al resto de la
población.
¿Por qué es importante detectar y
      manejar los outliers?

  1. Los outliers pueden ser errores en la data y deben
     detectarse y eliminarse.
  2. Los outliers que no son errores pueden sesgar los
     resultados de las herramientas analíticas que son sensibles
     a la existencia de outliers.
  3. Los outliers pueden ser entradas fraudulentas.
2.
 Outliers
 Detección
                                   Detección de Outliers
Las herramientas que utilizamos para detectar outliers dependen de la cantidad de atributos involucrados.




            1                               Detección de Outliers UNIVARIADOS




                        2                                Detección de Outliers BIVARIADOS




                                     3                               Detección de Outliers MULTIVARIADOS
U3_L5 DCNivel3_Outliers
Detección de Outliers
     Univariados
                            Detección de Outliers
                                 Univariados

                                                         Outliers

●   Los outliers univariados son valores muy grandes
    o pequeños que ocurren en una sola variable en
    un conjunto de datos.
●   Estos valores se consideran extremos y suelen ser
    diferentes del resto de valores de la variable.
●   Es importante identificarlos y abordarlos antes de
    realizar cualquier análisis o modelado adicional.
                                 Detección de Outliers
                                      Univariados

Existen dos métodos principales para identificar outliers univariados:

  1.   Métodos estadísticos: Como el rango intercuartil (IQR), la
       puntuación Z y la medida de asimetría.

  1.   Visualización de datos: Los histogramas y boxplots son
       gráficos muy útiles que muestran la distribución de un
       conjunto de datos. La forma de la distribución puede indicar
       dónde se encuentran los valores atípicos.
Detección de Outliers
      Bivariado
Detección de Outliers
     Bivariados

                ●   Los outliers bivariados suelen ser valores grandes o
     Outliers
                    pequeños     que    ocurren     en    dos    variables
                    simultáneamente.
                ●   Individualmente, los valores de cada variable pueden
                    o no ser outliers; sin embargo, en conjunto, son
                    outliers.
                ●   Para identificarlos utilizaremos scatterplot o boxplots
                    dependiendo de las variables.
Detección de Outliers
    Multivariado
                       Detección de Outliers
                           Multivariado


●   Los outliers multivariados son valores
    extremos que ocurren en tres o más
    variables simultáneamente.

●   La mejor manera de realizar la detección de
    outliers multivariados es mediante el análisis
    de agrupamiento (clustering).
3.
 Outliers
 Manejo
                Outliers
                Manejo

1.   No hacer nada
2.   Reemplazarlos por:
        a. Medidas estadísticas: La media, la mediana o los
           percentiles del conjunto de datos.
        b. Interpolación: Estimar el valor de un outlier utilizando los
           puntos de datos vecinos del outlier.
        c. Métodos basados ​en modelos: El uso de un modelo de
           ML para predecir el valor de reemplazo de los valores
           atípicos.
3.   Desarrollar una transformación logarítmica
4.   Eliminarlos
Cierre de la Sesión

●   ¿Qué son los outliers?
●   ¿Cómo los identificamos y manejamos?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
