---
curso: BIGDATA
titulo: 08 - Semana 6/Sem6_Spark
slides: 30
fuente: 08 - Semana 6/Sem6_Spark.pdf
---

## Slide 1

Portada. Título grande **Spark**. Subtítulo: Mg. Aldo Lezama Benavides. Etiqueta: Semana 6. Plantilla UTEC decorativa (fondo celeste, edificio UTEC de concreto a la derecha, logo UTEC, lema "Reinventa el mundo").

## Slide 2

**Objetivo de la sesión**

Texto dentro de un marco decorativo con corchetes:

- **Comprender** las diferencias entre el procesamiento in-memory de Spark y el procesamiento basado en disco de Hadoop MapReduce.
- **Identificar** los principales componentes del ecosistema de Spark (Spark Core, SQL, MLlib, GraphX y Streaming) y sus funciones.
- **Analizar** el uso de DataFrames y su rol como abstracción principal para el procesamiento distribuido y optimizado de datos.

## Slide 3

**Contenido de la sesión**

Cuatro bloques numerados en línea (cada uno enmarcado con corchetes decorativos):

| 01. | 02. | 03. | 04. |
|-----|-----|-----|-----|
| Definición SPARK | SPARK vs HADOOP | Ecosistema de SPARK | Ejemplo COLAB |

## Slide 4

Slide separadora de sección. Número grande **01.** junto a un icono de portapapeles/checklist y el título **SPARK Definición**. Plantilla celeste decorativa.

## Slide 5

**¿QUÉ ES APACHE SPARK?**

Columna de texto a la izquierda; a la derecha el logo de **Apache Spark** (estrella naranja + texto "Spark" en gris, marca TM).

Apache Spark es un marco de código abierto que admite diversas tareas de big data, como aprendizaje automático, análisis exploratorio de datos y procesamiento de datos en varios lenguajes de programación. Desarrollado inicialmente en 2009 como parte de un proyecto de investigación en la UC Berkeley, Apache Spark se ha consolidado como un pilar fundamental en la comunidad de big data, con el **80 % de las empresas Fortune 500** implementando la plataforma. Apache Spark se basa en las capacidades de su predecesor, Apache Hadoop, reemplazando el modelo de programación MapReduce original de Hadoop con funciones de aprendizaje automático más avanzadas. Si bien Apache Spark puede utilizarse de forma independiente, algunas empresas optan por usarlo simultáneamente con Apache Hadoop.

## Slide 6

**SPARK**

Texto a la izquierda; a la derecha un **diagrama del ecosistema Spark**: dentro de un recuadro, el logo central "Apache Spark", rodeado por cinco círculos grises con los componentes — Spark SQL, Streaming, MLlib, GraphX, SparkR. Debajo, fila de logos de los lenguajes/fuentes soportados: **Scala, Java, python, SQL (cilindro de BD), R**.

Apache Spark funciona proporcionando interfaces de programación de aplicaciones (API) para desarrolladores, ya sea que programen en **Python, Java, SQL, R o Scala**, de modo que puedan realizar sus tareas de procesamiento de datos en un solo lugar, a la vez que permite la integración con diferentes bibliotecas para funciones adicionales de manipulación de datos. En definitiva, esto crea un entorno que promueve un procesamiento y desarrollo de aplicaciones más rápidos, escalabilidad, acceso a la memoria y una gestión de datos simplificada.

## Slide 7

**SPARK**

Misma imagen del ecosistema Spark que la Slide 6 (Spark central rodeado de Spark SQL, Streaming, MLlib, GraphX, SparkR; abajo Scala/Java/python/SQL/R). Texto a la izquierda:

Cabe destacar que, antes de Spark 2.0, la interfaz de programación principal de Spark era el Resilient Distributed Dataset (RDD). Tras la versión 2.0, **los RDD se sustituyeron por Dataset**, que, si bien es fuertemente tipado, incorpora optimizaciones más avanzadas. La interfaz RDD sigue siendo compatible y se puede consultar una referencia más detallada en la guía de programación de RDD en la pagina web de Spark. Sin embargo, recomendamos encarecidamente el uso de Dataset, que ofrece un mejor rendimiento que RDD.

## Slide 8

**RDD vs DATAFRAMES**

A la izquierda, **infografía tipo "ring de boxeo"** ("RDD vs DataFrame — The New Champion in Spark"): a la izquierda RDD ("The Old Champion") caído/noqueado en rojo, con lista de contras (Low-level API, More Code, No Optimizer, Harder to Use, Legacy) y bocadillo "Too Low-level... Too Slow...". A la derecha DataFrame ("The New Champion") en azul, victorioso con trofeo "WINNER", lista de pros (High-level API, Less Code, Catalyst Optimizer, Easy to Use, Industry Standard). Franja inferior "Why DataFrame Wins?" con iconos: Better Performance, Automatic Optimization, Less Code/More Productivity, Seamless SQL Integration, Widely Adopted in Industry. Cartel final: WINNER DataFrame.

Texto a la derecha:

**Usa DataFrame cuando:**
- Tus datos son estructurados o semi-estructurados (tablas, logs, JSON)
- Haces:
  - Joins
  - Agregaciones
  - Filtros
- Buscas performance
- Quieres menos código y más mantenibilidad

**Usa RDD solo cuando:**
- Tienes datos muy no estructurados
- Necesitas control fino (ej: lógica compleja por partición)
- Estás haciendo algo muy custom (ej: algoritmos no soportados)

## Slide 9

Slide separadora de sección. Número grande **02.** junto al icono de portapapeles y el título **SPARK vs HADOOP**. Plantilla celeste.

## Slide 10

**SPARK vs HADOOP**

**Diagrama comparativo de flujo** (solo la figura, sin texto explicativo):

- Fila superior (logo **Spark**), caja gris "Spark Job" que dispara flechas punteadas a cada paso. Flujo: **HDFS (Hard Disk)** → Step → **RAM (Memory)** → Step → RAM (Memory) → Step → RAM (Memory) → Step. Los intermedios usan RAM (chips de memoria).
- Línea roja separadora.
- Fila inferior (logo **hadoop**, el elefante amarillo), caja gris "Hadoop Job". Flujo: **HDFS (Hard Disk)** → Step → **HDFS (Hard Disk)** → Step → HDFS (Hard Disk) → Step → HDFS (Hard Disk) → Step. Cada intermedio es un disco duro (todo pasa por disco).

## Slide 11

**SPARK vs HADOOP**

Reutiliza el diagrama de la Slide 10, con el bloque **Spark Job resaltado** (recuadro naranja/amarillo alrededor de la fila Spark). A la derecha, panel de texto:

**SPARK JOB**

`HDFS (disco) → Step → RAM → Step → RAM → Step → RAM → Step` (banner naranja)

- Los datos se leen una sola vez desde disco (HDFS).
- Luego, cada transformación (step) se ejecuta en memoria (RAM).
- Los resultados intermedios NO se escriben al disco, se mantienen en memoria. Spark trabaja **in-memory**.

**Características Importantes**
- La RAM es muchísimo más rápida que el disco.
- Evitas el costo de leer/escribir en cada paso.
- Ideal para:
  - Machine Learning
  - Procesamiento iterativo
  - Análisis interactivo
  - ETL complejos

## Slide 12

**SPARK vs HADOOP**

Mismo diagrama, ahora con el bloque **Hadoop Job resaltado** (recuadro naranja alrededor de la fila Hadoop). A la derecha:

**HADOOP JOB**

`HDFS → Step → HDFS → Step → HDFS → Step → HDFS → Step` (banner naranja)

- Cada etapa del proceso:
  1. Lee datos desde disco (HDFS)
  2. Procesa
  3. Escribe nuevamente al disco
- Hadoop MapReduce trabaja **disk-based**.

**Características Importantes**
- Mucho I/O (lectura/escritura en disco).
- Cada paso es más lento.
- Pero es:
  - Muy robusto
  - Escalable
  - Bueno para procesos batch pesados

## Slide 13

**SPARK vs HADOOP**

Tabla comparativa (cabecera azul):

| Aspecto | Spark | Hadoop (MapReduce) |
|---------|-------|--------------------|
| Procesamiento | En memoria (RAM) | En disco (HDFS) |
| Velocidad | Muy alta | Más lento |
| Uso de disco | Bajo | Alto |
| Ideal para | Iteraciones, ML, análisis | Batch tradicional |
| Arquitectura | DAG (más flexible) | Secuencial (map → reduce) |

## Slide 14

Slide separadora de sección. Número grande **03.** junto al icono de portapapeles y el título **Ecosistema SPARK**. Plantilla celeste.

## Slide 15

**ECOSISTEMA DE APACHE SPARK**

Texto a la izquierda; a la derecha **diagrama de capas del ecosistema** (estilo oficial Spark, color naranja): cuatro bloques superiores en forma de flecha hacia abajo — **MLlib** (Machine Learning), **Streaming** (Real-time analytics), **SQL** (Interactive Queries), **GraphX** (Graph processing) — todos apoyados sobre la base **Apache Spark Core**; y debajo del Core, cuatro cajas de lenguajes: **R, Python, Scala, Java**.

Los componentes principales del ecosistema de Apache Spark incluyen:
- Spark Core
- MLlib
- Spark SQL
- GraphX
- Spark Streaming

## Slide 16

**SPARK CORE**

Texto a la izquierda; a la derecha logo estilizado de Spark (llama/remolino naranja-rojo + texto "Spark").

Todas las funcionalidades que ofrece Apache Spark se basan en Spark Core. Proporciona velocidad gracias a su capacidad de computación en memoria.

Por lo tanto, Spark Core es la base del procesamiento paralelo y distribuido de grandes conjuntos de datos. Las características clave de Apache Spark Core son:
- Se encarga de las funcionalidades esenciales de entrada/salida.
- Importante en la programación y en la observación del papel del clúster Spark.
- Despacho de tareas.
- Recuperación de fallas.
- Supera el inconveniente de MapReduce mediante el uso de cálculos en memoria.

## Slide 17

**SPARK SQL**

Texto a la izquierda; a la derecha logo "Spark SQL".

Spark SQL es un módulo de Spark para el procesamiento de datos estructurados. Proporciona una abstracción de programación llamada DataFrames y también puede funcionar como un motor de consultas SQL distribuido. Permite que las consultas de Hadoop Hive sin modificar se ejecuten hasta 100 veces más rápido en implementaciones y datos existentes. Además, ofrece una potente integración con el resto del ecosistema Spark (por ejemplo, integrando el procesamiento de consultas SQL con el aprendizaje automático).

## Slide 18

**ARQUITECTURA DE SPARK SQL**

Texto a la izquierda; a la derecha **diagrama de arquitectura por capas** ("Architecture of Spark SQL"):
- Capa superior (azul), dos bloques: **Dataframe DSL** | **Spark SQL and HQL**
- **Data Frame API** (banda naranja)
- **Data Source API** (banda roja/rosa)
- Capa inferior: tres cilindros de fuentes de datos — **CSV**, **JSON**, **JDBC**

La capa inferior de la arquitectura de **Spark SQL** es el acceso (y almacenamiento) flexible de datos, que funciona con múltiples formatos. Los datos se obtienen de diversos formatos de entrada: JSON, JDBC o CSV. La API DataSource se utiliza para leer y almacenar datos estructurados y semiestructurados en Spark SQL. A continuación, la API DataSource recupera los datos, que luego se convierten a una API DataFrame (un DataFrame es una colección distribuida de datos organizada en columnas con nombre). La API DataFrame es equivalente a una tabla relacional en SQL, que convierte los datos leídos a través de la API DataSource en columnas tabulares para realizar operaciones SQL. Mediante los lenguajes específicos de dominio (DSL) de DataFrame, Spark SQL o HQL, el DataFrame se procesa para obtener los resultados deseados.

## Slide 19

**ARQUITECTURA DE SPARK SQL**

El mismo diagrama de capas (Dataframe DSL / Spark SQL and HQL → Data Frame API → Data Source API → cilindros CSV, JSON, JDBC) en el centro, rodeado de cuatro recuadros amarillos explicando cada capa:

**DataFrame DSL**
Es programación usando código (Python, Scala). Usa operaciones como:
- Select
- Filter
- groupBy

Es más flexible y programático.

**Spark SQL y HQL**
Escribir consultas tipo SQL:
`SELECT * FROM tabla WHERE ventas > 1000`
Ideal para gente de negocio o analistas. Dos formas de hacer lo mismo: Código (DataFrame) / SQL (más declarativo).

**DataFrame API**
Aquí todo se convierte en DataFrames, que son:
- Tablas distribuidas
- Con esquema (columnas)
- Optimizadas para procesamiento
- Spark convierte todo (SQL o código) en un plan lógico
- Luego lo optimiza (Catalyst Optimizer)

**Data Source API**
Esta capa permite que Spark lea datos desde múltiples fuentes. Es como un adaptador universal. Permite conectar con:
- Archivos / Bases de datos
- Sistemas externos

## Slide 20

**SPARK STRUCTURED STREAMING (antes Spark Streaming)**

Texto a la izquierda; a la derecha **diagrama de flujo "Spark Streaming"**: a la izquierda las fuentes de entrada con sus logos — **Kafka, Flume, HDFC/S3, Kinesis (amazon), Twitter** — que fluyen (flechas) hacia el núcleo hexagonal **Spark Streaming**, y de ahí (flechas) hacia las salidas: **HDFC, Databases, Dashboards**.

Spark Streaming es una extensión de la API principal de Spark que permite el procesamiento de flujos de datos en tiempo real, escalable, de alto rendimiento y tolerante a fallos. Los datos pueden ingerirse desde diversas fuentes, como Kafka, Kinesis o sockets TCP, y procesarse mediante algoritmos complejos expresados con funciones de alto nivel como map, reduce, join, y.

Finalmente, los datos procesados pueden enviarse a sistemas de archivos, bases de datos y paneles de control en tiempo real. De hecho, se pueden aplicar los algoritmos de aprendizaje automático y procesamiento de grafos de Spark a los flujos de datos.

## Slide 21

**SPARK STRUCTURED STREAMING (antes Spark Streaming)**

Texto a la izquierda; a la derecha **diagrama de micro-batches**: `input data stream` (flecha verde) → caja **Spark Streaming** → `batches of input data` (flecha verde con cajitas) → caja **Spark Engine** → `batches of processed data` (flecha azul con cajitas).

Structured Streaming proporciona una abstracción de alto nivel basada en DataFrames/Datasets, donde un flujo de datos se modela como una tabla infinita. Los datos pueden leerse desde fuentes como Kafka o Kinesis y procesarse usando operaciones declarativas (SQL o DataFrame API). Internamente, el sistema ejecuta el procesamiento como micro-batches optimizados o en modo continuo.

## Slide 22

**SPARK STRUCTURED STREAMING (antes Spark Streaming)**

Tabla comparativa (cabecera azul):

| Característica | Spark Streaming | Structured Streaming |
|---------------|-----------------|----------------------|
| API | DStreams | DataFrames |
| Base | RDD | DataFrame |
| Optimización | Limitada | Automática |
| SQL | No natural | Nativo |
| Estado | Complejo | Avanzado |
| Facilidad | Media | Alta |
| Uso actual | Legacy | Recomendado |

## Slide 23

**SPARK MLLIB**

Texto a la izquierda; a la derecha logo "Spark MLlib".

MLlib en Spark es una biblioteca de aprendizaje automático escalable que combina algoritmos de alta calidad con alta velocidad.

Su objetivo es hacer que el aprendizaje automático sea escalable y sencillo. Contiene bibliotecas con implementaciones de diversos algoritmos, como clustering, regresión, clasificación y filtrado colaborativo. También incluye primitivas de bajo nivel, como el algoritmo genérico de optimización de descenso de gradiente.

## Slide 24

**SPARK MLLIB**

Texto a la izquierda; a la derecha logo "Spark MLlib".

En la versión 2.0 de Spark, la API basada en RDD del paquete spark.mllib entró en modo de mantenimiento. En esta versión, la API basada en DataFrame se convirtió en la principal API de aprendizaje automático para Spark. Por lo tanto, MLlib no añadirá nuevas funcionalidades a la API basada en RDD.

El motivo de este cambio es que MLlib es más fácil de usar que RDD. Entre las ventajas de usar DataFrames se encuentran la compatibilidad con fuentes de datos de Spark, consultas SQL de DataFrame, optimizaciones de Tungsten y Catalyst, y API uniformes en diferentes lenguajes. MLlib también utiliza el paquete de álgebra lineal Breeze. Breeze es una colección de bibliotecas para computación numérica y aprendizaje automático.

## Slide 25

**SPARK GRAPHX**

Texto a la izquierda; a la derecha logo "Spark GraphX" (con un pequeño grafo de nodos coloreados + tabla junto al texto "GraphX").

GraphX en Spark es una API para grafos y ejecución paralela de grafos. Es un motor de análisis de grafos de red y un almacén de datos. También permite la agrupación, clasificación, recorrido, búsqueda y búsqueda de rutas en grafos.

Además, GraphX extiende Spark RDD al introducir una nueva abstracción de grafo: un multigrafo dirigido con propiedades asociadas a cada vértice y arista.

GraphX también optimiza la forma en que podemos representar vértices y aristas cuando son tipos de datos primitivos. Para admitir el cálculo de grafos, admite operadores fundamentales (por ejemplo, subgrafo, unión de vértices y agregación de mensajes), así como una variante optimizada de la API Pregel.

## Slide 26

**SPARKR**

Texto a la izquierda; a la derecha logo "Apache Spark R" (estrella Spark + R azul).

SparkR fue la versión 1.4 de Apache Spark. El componente clave de SparkR es SparkR DataFrame. Los DataFrames son una estructura de datos fundamental para el procesamiento de datos en R. El concepto de DataFrames se extiende a otros lenguajes con bibliotecas como Pandas, etc.

R también proporciona herramientas de software para la manipulación, el cálculo y la visualización gráfica de datos. Por lo tanto, la idea principal detrás de SparkR era explorar diferentes técnicas para integrar la usabilidad de R con la escalabilidad de Spark. Es un paquete de R que proporciona una interfaz ligera para usar Apache Spark desde R.

## Slide 27

Slide separadora de sección. Número grande **04.** junto al icono de portapapeles y el título **Ejemplo en COLAB**. Plantilla celeste.

## Slide 28

**SPARKR**

**Captura de pantalla de Google Colab** (notebook "Intro a Spark.ipynb", con barra de menú Archivo/Editar/Ver/Insertar/Entorno de ejecución/Herramientas/Ayuda, botones +Código +Texto, Ejecutar todo, Compartir). Dos celdas ejecutadas:

Celda [1]:
```
!pip install pyspark
```
Salida:
```
Requirement already satisfied: pyspark in /usr/local/lib/python3.12/dist-packages (4.0.2)
Requirement already satisfied: py4j<0.10.9.10,>=0.10.9.7 in /usr/local/lib/python3.12/dist-packages (from pyspark) (0.10.9.9)
```

Celda [7]:
```
!pyspark --version
```
Salida:
```
WARNING: Using incubator modules: jdk.incubator.vector
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 4.0.2
      /_/

Using Scala version 2.13.16, OpenJDK 64-Bit Server VM, 17.0.18
Branch HEAD
Compiled by user runner on 2026-02-02T08:08:13Z
Revision 7cc3b9bcdaab8c923f23cdbc9ce922530e1becf1
Url https://github.com/apache/spark
Type --help for more information.
```

## Slide 29

**Conclusiones**

Tres puntos numerados (01, 02, 03) con corchetes decorativos:

01. Spark ofrece un rendimiento superior frente a Hadoop MapReduce al ejecutar operaciones en memoria, reduciendo significativamente el costo de I/O.

02. El ecosistema de Spark integra múltiples capacidades (SQL, machine learning, streaming y grafos) en una sola plataforma unificada.

03. La evolución de RDD hacia DataFrames/Datasets responde a la necesidad de mayor optimización, facilidad de uso y compatibilidad entre lenguajes.

## Slide 30

Cierre. Logo UTEC (Universidad de Ingeniería y Tecnología) centrado sobre fondo celeste decorativo. Sin contenido de texto.
