---
curso: BIGDATA
titulo: 08 - Semana 6/Sem6_Spark
slides: 30
fuente: 08 - Semana 6/Sem6_Spark.pdf
---

Spark
Mg. Aldo Lezama Benavides


Semana 6
    Objetivo de la sesión


Comprender las diferencias entre el procesamiento in-memory de
Spark y el procesamiento basado en disco de Hadoop MapReduce.
Identificar los principales componentes del ecosistema de Spark
(Spark Core, SQL, MLlib, GraphX y Streaming) y sus funciones.
Analizar el uso de DataFrames y su rol como abstracción principal
para el procesamiento distribuido y optimizado de datos.
             Contenido de la sesión

  01.             02.           03.          04.

Definición       SPARK vs    Ecosistema de   Ejemplo
 SPARK           HADOOP         SPARK        COLAB
01.   SPARK Definición
                                 ¿QUÉ ES APACHE SPARK?
Apache Spark es un marco de código abierto que admite
diversas tareas de big data, como aprendizaje automático,
análisis exploratorio de datos y procesamiento de datos en
varios lenguajes de programación. Desarrollado inicialmente en
2009 como parte de un proyecto de investigación en la UC
Berkeley, Apache Spark se ha consolidado como un pilar
fundamental en la comunidad de big data, con el 80 % de las
empresas Fortune 500 implementando la plataforma. Apache
Spark se basa en las capacidades de su predecesor, Apache
Hadoop,    reemplazando     el   modelo    de   programación
MapReduce original de Hadoop con funciones de aprendizaje
automático más avanzadas. Si bien Apache Spark puede
utilizarse de forma independiente, algunas empresas optan por
usarlo simultáneamente con Apache Hadoop
                                                          SPARK


Apache       Spark    funciona   proporcionando    interfaces   de
programación de aplicaciones (API) para desarrolladores, ya
sea que programen en Python, Java, SQL , R o Scala, de
modo que puedan realizar sus tareas de procesamiento de
datos en un solo lugar, a la vez que permite la integración con
diferentes     bibliotecas   para   funciones     adicionales   de
manipulación de datos. En definitiva, esto crea un entorno que
promueve un procesamiento y desarrollo de aplicaciones más
rápidos, escalabilidad, acceso a la memoria y una gestión de
datos simplificada.
                                                    SPARK


Cabe destacar que, antes de Spark 2.0, la interfaz de
programación principal de Spark era el Resilient Distributed
Dataset (RDD). Tras la versión 2.0, los RDD se sustituyeron
por Dataset, que, si bien es fuertemente tipado, incorpora
optimizaciones más avanzadas. La interfaz RDD sigue siendo
compatible y se puede consultar una referencia más detallada
en la guía de programación de RDD en la pagina web de Spark.
Sin embargo, recomendamos encarecidamente el uso de
Dataset, que ofrece un mejor rendimiento que RDD.
RDD vs DATAFRAMES
               Usa DataFrame cuando:
               Tus   datos    son   estructurados   o   semi-
               estructurados (tablas, logs, JSON)
               • Haces:
               ❑ Joins
               ❑ Agregaciones
               ❑ Filtros
               • Buscas performance
               • Quieres menos código y más mantenibilidad
               Usa RDD solo cuando:
               • Tienes datos muy no estructurados
               • Necesitas control fino (ej: lógica compleja
                  por partición)
               • Estás haciendo algo muy custom (ej:
                  algoritmos no soportados)
02.   SPARK vs HADOOP
SPARK vs HADOOP
SPARK vs HADOOP
        SPARK JOB

        HDFS (disco) → Step → RAM → Step → RAM → Step → RAM → Step

        • Los datos se leen una sola vez desde disco (HDFS).
        • Luego, cada transformación (step) se ejecuta en memoria (RAM).
        • Los resultados intermedios NO se escriben al disco, se mantienen en
           memoria.
           Spark trabaja in-memory
        Características Importantes
        • La RAM es muchísimo más rápida que el disco.
        • Evitas el costo de leer/escribir en cada paso.
        • Ideal para:
        ❑ Machine Learning
        ❑ Procesamiento iterativo
        ❑ Análisis interactivo
        ❑ ETL complejos
SPARK vs HADOOP
        HADOOP JOB

        HDFS → Step → HDFS → Step → HDFS → Step → HDFS → Step

        • Cada etapa del proceso:
        1. Lee datos desde disco (HDFS)
        2. Procesa
        3. Escribe nuevamente al disco
           Hadoop MapReduce trabaja disk-based.
        Características Importantes
        • Mucho I/O (lectura/escritura en disco).
        • Cada paso es más lento.
        • Pero es:
        ❑ Muy robusto
        ❑ Escalable
        ❑ Bueno para procesos batch pesados
                SPARK vs HADOOP


   Aspecto                Spark                Hadoop (MapReduce)



Procesamiento      En memoria (RAM)              En disco (HDFS)


  Velocidad              Muy alta                    Más lento


Uso de disco               Bajo                         Alto


  Ideal para     Iteraciones, ML, análisis        Batch tradicional


 Arquitectura      DAG (más flexible)        Secuencial (map → reduce)
03.   Ecosistema SPARK
                      ECOSISTEMA DE APACHE SPARK


Los componentes principales del ecosistema de Apache Spark

incluyen

• Spark Core

• MLlib

• Spark SQL

• GraphX

• Spark Streaming
                                              SPARK CORE

Todas las funcionalidades que ofrece Apache Spark se basan en Spark
Core . Proporciona velocidad gracias a su capacidad de computación en
memoria.


Por lo tanto, Spark Core es la base del procesamiento paralelo y
distribuido de grandes conjuntos de datos. Las características clave de
Apache Spark Core son:


• Se encarga de las funcionalidades esenciales de entrada/salida.
• Importante en la programación y en la observación del papel del
  clúster Spark .
• Despacho de tareas.
• Recuperación de fallas.
• Supera el inconveniente de MapReduce mediante el uso de cálculos
  en memoria.
                                                 SPARK SQL


Spark SQL es un módulo de Spark para el procesamiento de
datos   estructurados.   Proporciona   una      abstracción   de
programación llamada DataFrames y también puede funcionar
como un motor de consultas SQL distribuido. Permite que las
consultas de Hadoop Hive sin modificar se ejecuten hasta 100
veces más rápido en implementaciones y datos existentes.
Además, ofrece una potente integración con el resto del
ecosistema Spark (por ejemplo, integrando el procesamiento de
consultas SQL con el aprendizaje automático).
                           ARQUITECTURA DE SPARK SQL
La capa inferior de la arquitectura de Spark SQL es el acceso (y
almacenamiento) flexible de datos, que funciona con múltiples
formatos. Los datos se obtienen de diversos formatos de
entrada: JSON, JDBC o CSV. La API DataSource se utiliza para
leer y almacenar datos estructurados y semiestructurados en
Spark SQL. A continuación, la API DataSource recupera los
datos, que luego se convierten a una API DataFrame (un
DataFrame es una colección distribuida de datos organizada en
columnas con nombre). La API DataFrame es equivalente a una
tabla relacional en SQL, que convierte los datos leídos a través
de la API DataSource en columnas tabulares para realizar
operaciones SQL. Mediante los lenguajes específicos de
dominio (DSL) de DataFrame, Spark SQL o HQL, el DataFrame
se procesa para obtener los resultados deseados.
                                         ARQUITECTURA DE SPARK SQL
                                                                     Spark SQL y HQL
DataFrame DSL
                                                                     Escribir consultas tipo SQL:
Es programación usando código (Python, Scala).
                                                                     SELECT * FROM tabla WHERE ventas > 1000
Usa operaciones como:
                                                                     Ideal para gente de negocio o analistas
•   Select
                                                                     Dos formas de hacer lo mismo:
•   Filter
                                                                     Código (DataFrame)
•   groupBy
                                                                     SQL (más declarativo)
Es más flexible y programático.




DataFrame API                                                        Data Source API
Aquí todo se convierte en DataFrames, que son:                       Esta capa permite que Spark lea datos desde
•   Tablas distribuidas                                              múltiples fuentes.
•   Con esquema (columnas)                                           Es como un adaptador universal.
•   Optimizadas para procesamiento                                   Permite conectar con:
•   Spark convierte todo (SQL o código) en un                        •   ArchivosBases de datos
    plan lógico                                                      •   Sistemas externos
•   Luego lo optimiza (Catalyst Optimizer)
                         SPARK STRUCTURED STREAMING
                             (antes Spark Streaming)
Spark Streaming es una extensión de la API principal de Spark
que permite el procesamiento de flujos de datos en tiempo real,
escalable, de alto rendimiento y tolerante a fallos. Los datos
pueden ingerirse desde diversas fuentes, como Kafka, Kinesis o
sockets TCP, y procesarse mediante algoritmos complejos
expresados ​con funciones de alto nivel como map, reduce, joiny.


Finalmente, los datos procesados ​pueden enviarse a sistemas
de archivos, bases de datos y paneles de control en tiempo real.
De hecho, se pueden aplicar los algoritmos de aprendizaje
automático y procesamiento de grafos de Spark a los flujos de
datos.

                        SPARK STRUCTURED STREAMING
                            (antes Spark Streaming)


Structured Streaming proporciona una abstracción de
alto nivel basada en DataFrames/Datasets, donde un
flujo de datos se modela como una tabla infinita. Los
datos pueden leerse desde fuentes como Kafka o
Kinesis y procesarse usando operaciones declarativas
(SQL o DataFrame API). Internamente, el sistema
ejecuta   el   procesamiento   como    micro-batches
optimizados o en modo continuo
SPARK STRUCTURED STREAMING
    (antes Spark Streaming)

Característica   Spark Streaming   Structured Streaming

     API            DStreams           DataFrames

    Base              RDD               DataFrame

Optimización        Limitada            Automática

    SQL             No natural            Nativo

   Estado           Complejo            Avanzado

  Facilidad           Media                Alta

 Uso actual          Legacy           Recomendado
                                                SPARK MLLIB

MLlib en Spark es una biblioteca de aprendizaje automático
escalable que combina algoritmos de alta calidad con alta
velocidad.
Su objetivo es hacer que el aprendizaje automático sea
escalable y sencillo. Contiene bibliotecas con implementaciones
de diversos algoritmos, como clustering, regresión, clasificación
y filtrado colaborativo. También incluye primitivas de bajo nivel,
como el algoritmo genérico de optimización de descenso de
gradiente.
                                               SPARK MLLIB

En la versión 2.0 de Spark, la API basada en RDD del paquete
spark.mllib entró en modo de mantenimiento. En esta versión, la API
basada en DataFrame se convirtió en la principal API de aprendizaje
automático para Spark . Por lo tanto, MLlib no añadirá nuevas
funcionalidades a la API basada en RDD.
El motivo de este cambio es que MLlib es más fácil de usar que RDD.
Entre las ventajas de usar DataFrames se encuentran la compatibilidad
con fuentes de datos de Spark, consultas SQL de DataFrame,
optimizaciones de Tungsten y Catalyst , y API uniformes en diferentes
lenguajes. MLlib también utiliza el paquete de álgebra lineal Breeze .
Breeze es una colección de bibliotecas para computación numérica y
aprendizaje automático.
                                            SPARK GRAPHX

GraphX ​en Spark es una API para grafos y ejecución paralela de
grafos. Es un motor de análisis de grafos de red y un almacén de
datos. También permite la agrupación, clasificación, recorrido,
búsqueda y búsqueda de rutas en grafos.


Además, GraphX ​extiende Spark RDD al introducir una nueva
abstracción de grafo: un multigrafo dirigido con propiedades
asociadas a cada vértice y arista.


GraphX ​también optimiza la forma en que podemos representar
vértices y aristas cuando son tipos de datos primitivos. Para
admitir el cálculo de grafos, admite operadores fundamentales
(por ejemplo, subgrafo, unión de vértices y agregación de
mensajes), así como una variante optimizada de la API Pregel .
                                                      SPARKR

SparkR fue la versión 1.4 de Apache Spark. El componente
clave de SparkR es SparkR DataFrame. Los DataFrames son
una estructura de datos fundamental para el procesamiento de
datos en R. El concepto de DataFrames se extiende a otros
lenguajes con bibliotecas como Pandas, etc.


R también proporciona herramientas de software para la
manipulación, el cálculo y la visualización gráfica de datos. Por
lo tanto, la idea principal detrás de SparkR era explorar
diferentes técnicas para integrar la usabilidad de R con la
escalabilidad de Spark. Es un paquete de R que proporciona
una interfaz ligera para usar Apache Spark desde R.
04.   Ejemplo en COLAB
SPARKR
                     Conclusiones

01.   Spark ofrece un rendimiento superior frente a Hadoop MapReduce al ejecutar
      operaciones en memoria, reduciendo significativamente el costo de I/O.




02.   El ecosistema de Spark integra múltiples capacidades (SQL, machine learning,
      streaming y grafos) en una sola plataforma unificada.




03.   La evolución de RDD hacia DataFrames/Datasets responde a la necesidad de mayor
      optimización, facilidad de uso y compatibilidad entre lenguajes.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
