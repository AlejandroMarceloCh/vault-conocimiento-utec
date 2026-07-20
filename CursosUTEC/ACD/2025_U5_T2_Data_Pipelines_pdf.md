---
curso: ACD
titulo: [2025] U5_T2 Data Pipelines
slides: 21
fuente: [2025] U5_T2 Data Pipelines.pdf
---

 Data Pipelines

DS3021 Análisis Computacional de Datos




                                  Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Explicar conceptos fundamentales de
                     Data Pipelines.
1.
     Data Pipelines
     Introducción
        “Data is new oil”



Al igual que el petróleo, el valor de los datos
logra su potencial después de que se refinan y
se entregan al consumidor. También como el
petróleo, se necesitan oleoductos eficientes para
entregar datos a través de cada etapa de su
cadena de valor.
                        Data Engineering
                            LifeCycle
   Data Pipeline

                                                                                Analytics
                        Ingestion   Transformation    Serving
                                                                                Machine
 Generation                                                                     Learning
                                       Storage
                                                                           Reverse ETL




                               Corriente subterráneas

Security      Data           DataOps           Data             Orchestration       Software
           Management                       Architecture                           Engineering
                               Data Pipelines



Los data pipelines son la combinación de
arquitectura,   sistemas   y   procesos    que
mueven los datos a través de las etapas del
ciclo de vida de la ingeniería de datos.
                                       Data Pipelines
                                          Ejemplo




APIs de ingesta para obtener los     Después,    una    tecnología   de   Por último, la pipeline termina con
datos, los cuales son el punto de    procesamiento, que puede ser         el resultado almacenado de forma
partida, y podría enviar los datos   streaming o batch, leerá los datos   persistente en una base de datos
a un topic de Apache Kafka. Kafka    de nuestro buffer. Por ejemplo,      como HBase o en un sistema de
actúa aquí como un buffer para el    Apache Spark realizará analítica     ficheros distribuido como HDFS.
siguiente paso.                      sobre estos datos.
                       Data Pipelines
                    ¿Por qué construirlos?


Dashboards, campañas de
marketing, modelos
predictivos




                                  Data Pipelines
2.
 Data Pipelines
 Una infraestructura
 moderna de datos
Antes de decidir en productos para el
diseño de la construcción de pipelines
   es importante entender con qué
              contamos.
1   2   3   4   5
    La   mayoría de las organizaciones tienen
    docenas, sino cientos, de fuentes de datos que
    alimentan   sus   esfuerzos   analíticos.   Sin
1   embargo hay puntos a considerar:
  Propios de la organización


                                            Es común que un equipo de análisis utilize
                                            datos de sistemas de origen creados y
                                            propiedad de la organización, así como de
                                            herramientas y proveedores de terceros.


                                            Por ejemplo, una empresa de e-commerce
                                            puede almacenar datos de su carrito de
                                            compras en una base de datos PostgreSQL
                                            detrás de su aplicación web. También
                                            pueden usar una herramienta de análisis web
                                            de terceros, como Google Analytics, para
                                            rastrear el uso en su sitio web.

Un pipeline simple con datos de múltiples
fuentes cargadas en un bucket S3 y luego
     en una base de datos Redshift.
 Interfaces de Ingestión y   “El término data ingestion se refiere a extraer datos de un
   Estructuras de datos      recurso y cargarlo dentro de otro recurso”



Independientemente de quién sea el propietario de los datos de
origen, lo primero que examinará un ingeniero de datos al crear una
nueva ingestión de datos es: ¿cómo los obtiene? y ¿en qué forma?,
¿cuál es la interfaz? Algunos de los más comunes incluyen los
siguientes:

 ●   Una base de datos detrás de una aplicación, como una base de datos
     Postgres, Oracle o MySQL
 ●   Una capa de abstracción sobre un sistema como una API REST
 ●   Una plataforma de procesamiento de flujo (stream) como Apache
     Kafka
 ●   Un sistema de archivos de red compartido o depósito de
     almacenamiento en la nube que contiene registros, archivos CSV y
     otros archivos planos
 ●   Un datawarehouse o un data lake
Interfaces de Ingestión y
  Estructuras de datos




Además de la interfaz, la estructura de los datos variará. Estos son algunos ejemplos
comunes:
 ● JSON de una API REST
 ● Datos estructurados de una base de datos
 ● JSON dentro de columnas de una tabla de base de datos
 ● Log data semiestructurados
 ● CSV, formato de ancho fijo (FWF) y otros formatos de archivo sin formato
 ● JSON en archivos sin formato
 ● Stream output de Kafka
    Volumen de datos




●   Aunque tanto los ingenieros de datos como los gerentes de contratación
    disfrutan alardeando sobre los conjuntos de datos a escala de petabytes, la
    realidad es que la mayoría de las organizaciones valoran los conjuntos de
    datos pequeños tanto como los grandes.


●   Además, es común ingerir y modelar conjuntos de datos pequeños y grandes.
    Aunque las decisiones de diseño en cada paso de un pipeline deben tener en
    cuenta el volumen de datos, un gran volumen no significa un gran valor.
Limpieza y validez de datos




Es importante comprender las limitaciones y deficiencias de
los datos de origen y abordarlas en las secciones
correspondientes de sus pipelines.


Hay momentos en los que es mejor esperar para limpiar los
datos hasta más adelante en un pipeline. Por ejemplo, los
pipelines modernos tienden a seguir un ELT en lugar de ETL
para el almacenamiento de datos.

Use la herramienta correcta para el trabajo correcto en
lugar de apresurar los procesos de limpieza y validación.
Latencia y Ancho de Banda




La necesidad de extraer con frecuencia grandes volúmenes de
datos de los sistemas de origen es un caso de uso común en un
data pipeline moderna. Sin embargo, hacerlo presenta desafíos.

Los pasos de extracción de datos en los pipelines deben lidiar
con:
 ● los límites de velocidad de la API,
 ● los tiempos de espera de conexión,
 ● las descargas lentas y
 ● los propietarios del sistema de origen que no están
     contentos debido a la presión ejercida sobre sus sistemas.
3.
 Data Pipelines
 Patrones Comunes de
 Data Pipelines
 ETL y ELT
     ETL                      ELT



¿De qué trata?



Ejemplos para Ciencia de Datos (2)


Una ventaja contra      ETL    o     ELT
(respectivamente)

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
