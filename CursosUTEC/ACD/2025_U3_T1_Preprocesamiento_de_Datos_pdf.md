---
curso: ACD
titulo: [2025] U3_T1 Preprocesamiento de Datos
slides: 19
fuente: [2025] U3_T1 Preprocesamiento de Datos.pdf
---

Preprocesamiento de Datos

     DS3021 Análisis Computacional de Datos




                                       Mg. José Espinoza Melgarejo
 Una baja calidad de datos
origina una baja calidad de
                 resultados
Objetivo de sesión
                     Comprender e identificar la importancia
                     de realizar el preprocesamiento de datos
                     en Ciencia de Datos.
1.
     Preprocesamiento de
     Datos
                Preprocesamiento de Datos
El preprocesamiento de datos se puede definir como el proceso de conversión de datos sin
procesar (raw data) a un formato que sea comprensible y utilizable para un análisis posterior. Es
un paso importante en la etapa de Preparación de Datos (ciclo de vida Ciencia de Datos).
Garantiza que el resultado del análisis sea preciso, completo y coherente.
                                         ¿Por qué es importante el
                                        Preprocesamiento de Datos?
                                                       Accuracy (precisión)
                                                       El   preprocesamiento     de   datos
                                                       garantizará que los datos de entrada
                                                       sean precisos y confiables al
                                                       garantizar que no existan errores de
                                                       entrada manual, duplicados, etc




                                                                               Consistent (consistencia)
Completeness (integridad)                                                      El   preprocesamiento     de   datos
Garantiza que se manejen los valores                                           garantiza que los datos de entrada
faltantes y que los datos estén                                                sean consistentes, es decir, los
completos para su posterior análisis.                                          mismos      datos   guardados       en
                                                                               diferentes lugares deben coincidir.




                                                                                      Interpretability (interpretabilidad)
                                                                                      Los datos sin procesar generalmente
                Trustable (confiable)
                                                                                      no    se   pueden     utilizar   y  el
                Si los datos provienen de datos
                                                                                      preprocesamiento de datos los
                confiables o no.
                                                                                      convierte      en     un       formato
                                                                                      interpretable.
2.
 Técnicas de
 Preprocesamiento
   Técnicas de Preprocesamiento

                Limpieza de los datos. Remover   ruido   y   corregir
Data Cleaning
                inconsistencias en los datos.
     Técnicas de Preprocesamiento
                   Mezcla data de diferentes recursos dentro de un
Data Integration   almacenamiento coherente de datos (por ejemplo data
                   warehouse, etc)
    Técnicas de Preprocesamiento

                 Reducir el tamaño de los datos. Por ejemplo, agregar,
Data Reduction
                 eliminar características redundantes, etc.
      Técnicas de Preprocesamiento


     Data
                      Normalización puede ser aplicada.
Transformation




-2, 32, 100, 59, 48                          -0.02, 0.32, 1.00, 0.59, 0.48
     Técnicas de Preprocesamiento

                   Limpieza de los datos. Remover      ruido   y   corregir
 Data Cleaning
                   inconsistencias en los datos.


                   Mezcla data de diferentes recursos dentro de un
Data Integration   almacenamiento coherente de datos (por ejemplo data
                   warehouse, etc)



                   Reducir el tamaño de los datos. Por ejemplo, agregar,
Data Reduction
                   eliminar características redundantes, etc.




     Data
                   Normalización puede ser aplicada.
Transformation
2.
 Data Cleaning
                                 Data Cleaning
Los datos del mundo real tienden a ser incompletos, ruidosos e inconsistentes. Las rutinas de
data cleaning (limpieza de datos) intentan completar los valores faltantes, suavizar el ruido
mientras identifican los valores atípicos y corrigen las inconsistencias en los datos.
                                             Pasos Data Cleaning
                                                             Nivel 1: Limpiar cómo luce la tabla
                                                             Se realiza la limpieza en base a las siguientes 3
                                                             características:
                                                                 ●      Estructura de datos estándar
                                                                 ●      Las columnas tienen nombres
                                                                        codificables e intuitivos
                                                                 ●      Cada fila tiene un identificador único




                                                                   Nivel 3: Evaluar y corregir valores
Nivel 2: Reestructuración y                                        Este nivel de limpieza tiene que ver con la
                                                                   exactitud y existencia de los valores
reformulación de la tabla                                          registrados en el dataset. En este nivel de
Este nivel de limpieza tiene que ver con el tipo                   limpieza, desea asegurarse de que los valores
de estructura de datos y formato en el que                         registrados sean correctos y se presenten de la
necesita que esté el dataset para que se                           manera que mejor respalde los objetivos
puedan realizar el análisis que se tiene en                        analíticos. Aquí se evalúa la presencia de:
mente.                                                                 ●      valores faltantes
                                                                       ●      outliers
                                                                       ●      coherencia
U3_L1 DataCleaning_Nivel1
U3_L2 DataCleaning_Nivel2
Una respuesta para
analizar los discursos es
analizar la frecuencia de
las palabras:
  ● voto (vote)
  ● impuestos (tax)
  ● campaña
       (campaign)
  ● economía
       (economy)

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
