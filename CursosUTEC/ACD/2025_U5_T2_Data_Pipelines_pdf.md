---
curso: ACD
titulo: [2025] U5_T2 Data Pipelines
slides: 21
fuente: [2025] U5_T2 Data Pipelines.pdf
---

## Slide 1

Portada (decorativa: túnel de datos azul con silueta caminando).

**Data Pipelines**
DS3021 Análisis Computacional de Datos

## Slide 2

Slide de objetivo. Foto decorativa de dos personas revisando documentos, con overlay azul.

**Objetivo de sesión**

> Explicar conceptos fundamentales de Data Pipelines.

## Slide 3

Separador de sección (imagen decorativa: mano robótica tocando un globo digital).

**1. Data Pipelines — Introducción**

## Slide 4

**"Data is new oil"**

Al igual que el petróleo, el valor de los datos logra su potencial después de que se refinan y se entregan al consumidor. También como el petróleo, se necesitan oleoductos eficientes para entregar datos a través de cada etapa de su cadena de valor.

**Visual:** ilustración en blanco y negro de un campo petrolero — cinco torres de perforación sobre un corte transversal del subsuelo (negro sólido). La torre central perfora hasta un yacimiento con forma de mancha blanca irregular rotulado **DATA**: la analogía es que los datos son el "crudo" que hay que extraer.

## Slide 5

**Data Engineering LifeCycle**

**Diagrama de flujo:**

- Caja amarilla **Generation** (izquierda) → flecha → contenedor redondeado grande = el pipeline.
- Dentro del contenedor, fila superior de tres bloques encadenados por flechas: **Ingestion** (verde) → **Transformation** (guinda) → **Serving** (azul).
- Debajo de esos tres, ocupando todo el ancho, bloque gris **Storage** (el almacenamiento sostiene las tres etapas).
- Una estrella gris etiquetada **Data Pipeline** (texto azul) señala el bloque de ingesta/el contenedor: el data pipeline es Ingestion + Transformation + Serving sobre Storage.
- Del contenedor salen tres flechas hacia cajas grises de salida: **Analytics**, **Machine Learning**, **Reverse ETL**.

Debajo, separado por una línea azul, la banda **Corriente subterráneas** (undercurrents) con seis elementos transversales alternando color azul/amarillo: **Security · Data Management · DataOps · Data Architecture · Orchestration · Software Engineering**.

## Slide 6

**Data Pipelines**

Los **data pipelines** son la combinación de arquitectura, sistemas y procesos que **mueven los datos** a través de las etapas del ciclo de vida de la ingeniería de datos.

**Visual:** icono de una tubería serpenteante negra que zigzaguea de arriba a la derecha hacia abajo a la izquierda, con segmentos grises punteados (flujo) y un círculo amarillo con una cruz (una válvula/unión) en el centro del recorrido.

## Slide 7

**Data Pipelines — Ejemplo**

**Diagrama (estilo boceto, tres bloques encadenados por flechas amarillas):**

1. Bloque morado sin título de cabecera, dos filas: **BUFFER** con el logo de Apache Kafka (tres nodos conectados), y **CACHE** con el logo de Redis. Una flecha amarilla gruesa entra desde arriba (la ingesta).
2. → Bloque azul **PROCESAMIENTO**, dos filas: **BATCH** con el logo de Apache Spark, y **STREAM** con el logo de Apache Storm.
3. → Bloque rojo **ALMACENAMIENTO**, dos filas: **BD SQL** con icono de cilindro de base de datos, y **NoSQL** con el logo de Hadoop (elefante amarillo). Marca de agua "AprenderBigData.com".

Pie del diagrama: "Ejemplo esquemático de una pipeline de datos".

Tres columnas de texto bajo el diagrama:

- APIs de ingesta para obtener los datos, los cuales son el punto de partida, y podría enviar los datos a un topic de Apache Kafka. Kafka actúa aquí como un buffer para el siguiente paso.
- Después, una tecnología de procesamiento, que puede ser streaming o batch, leerá los datos de nuestro buffer. Por ejemplo, Apache Spark realizará analítica sobre estos datos.
- Por último, la pipeline termina con el resultado almacenado de forma persistente en una base de datos como HBase o en un sistema de ficheros distribuido como HDFS.

## Slide 8

**Data Pipelines — ¿Por qué construirlos?**

**Visual:** metáfora del iceberg. Foto de un iceberg; la punta visible sobre el agua está etiquetada con un cuadro de texto: "Dashboards, campañas de marketing, modelos predictivos". La masa sumergida, mucho mayor, está etiquetada "Data Pipelines" — es decir, lo que se ve es una fracción del trabajo real de datos.

## Slide 9

Separador de sección (misma imagen decorativa de mano robótica).

**2. Data Pipelines — Una infraestructura moderna de datos**

## Slide 10

Slide de cita, fondo azul degradado con comillas grandes decorativas.

> Antes de decidir en productos para el diseño de la construcción de pipelines es importante entender con qué contamos.

## Slide 11

**Visual:** cinco barras/píldoras diagonales azules en escalera (de azul oscuro a azul claro, de izquierda a derecha), cada una con un círculo numerado en su base. Es el índice de los cinco componentes:

1. Diversidad de Recursos de Datos
2. Herramientas de Ingesta de Datos
3. Plataformas de orquestación de workflow
4. Warehouses y Data Lakes en Nube
5. Frameworks y herramientas de modelado

Sin texto adicional.

## Slide 12

Retoma la píldora diagonal **1 — Diversidad de Recursos de Datos** (misma gráfica que la slide anterior, aislada a la izquierda).

La mayoría de las organizaciones tienen docenas, sino cientos, de fuentes de datos que alimentan sus esfuerzos analíticos. Sin embargo hay puntos a considerar:

## Slide 13

**Propios de la organización**

Es común que un equipo de análisis utilice datos de sistemas de origen creados y propiedad de la organización, así como de herramientas y proveedores de terceros.

**Por ejemplo,** una empresa de e-commerce puede almacenar datos de su carrito de compras en una base de datos PostgreSQL detrás de su aplicación web. También pueden usar una herramienta de análisis web de terceros, como Google Analytics, para rastrear el uso en su sitio web.

**Diagrama de arquitectura (izquierda):** dos fuentes — cilindro azul **Postgres DB** (arriba) y caja **Google analytics REST API** (abajo) — convergen con flechas en un icono de bucket (S3), y de ahí una flecha al logo de **Amazon Redshift**.

Pie: "Un *pipeline* simple con datos de múltiples fuentes cargadas en un *bucket* S3 y luego en una base de datos Redshift."

## Slide 14

**Interfaces de Ingestión y Estructuras de datos**

> "El término **data ingestion** se refiere a extraer datos de un recurso y cargarlo dentro de otro recurso"

Independientemente de quién sea el propietario de los datos de origen, lo primero que examinará un ingeniero de datos al crear una nueva ingestión de datos es: ¿cómo los obtiene? y ¿en qué forma?, ¿cuál es la **interfaz**? Algunos de los más comunes incluyen los siguientes:

- Una base de datos detrás de una aplicación, como una base de datos Postgres, Oracle o MySQL
- Una capa de abstracción sobre un sistema como una API REST
- Una plataforma de procesamiento de flujo (stream) como Apache Kafka
- Un sistema de archivos de red compartido o depósito de almacenamiento en la nube que contiene registros, archivos CSV y otros archivos planos
- Un datawarehouse o un data lake

**Visual:** icono decorativo de una gota de agua celeste con un circuito/red de nodos conectados sobre ella (flujo de datos).

## Slide 15

**Interfaces de Ingestión y Estructuras de datos**

Además de la interfaz, la estructura de los datos variará. Estos son algunos ejemplos comunes:

- JSON de una API REST
- Datos estructurados de una base de datos
- JSON dentro de columnas de una tabla de base de datos
- Log data semiestructurados
- CSV, formato de ancho fijo (FWF) y otros formatos de archivo sin formato
- JSON en archivos sin formato
- Stream output de Kafka

Sin gráfico.

## Slide 16

**Volumen de datos**

- Aunque tanto los ingenieros de datos como los gerentes de contratación disfrutan alardeando sobre los conjuntos de datos a escala de petabytes, la realidad es que **la mayoría de las organizaciones valoran los conjuntos de datos pequeños tanto como los grandes.** (resaltado en celeste)
- Además, es común ingerir y modelar conjuntos de datos pequeños y grandes. Aunque las decisiones de diseño en cada paso de un pipeline deben tener en cuenta el volumen de datos, **un gran volumen no significa un gran valor**. (resaltado en celeste)

## Slide 17

**Limpieza y validez de datos**

Es importante **comprender las limitaciones y deficiencias** de los datos de origen y abordarlas en las secciones correspondientes de sus pipelines.

Hay momentos en los que es mejor esperar para limpiar los datos hasta más adelante en un pipeline. Por ejemplo, los pipelines modernos tienden a seguir un ELT en lugar de ETL para el almacenamiento de datos.

*Use la herramienta correcta para el trabajo correcto en lugar de apresurar los procesos de limpieza y validación.* (destacado en celeste)

**Visual:** icono lineal de un documento con líneas de texto siendo barrido por una escoba (limpieza de datos).

## Slide 18

**Latencia y Ancho de Banda**

La necesidad de extraer con frecuencia grandes volúmenes de datos de los sistemas de origen es un caso de uso común en un data pipeline moderna. Sin embargo, hacerlo presenta desafíos.

Los pasos de extracción de datos en los pipelines deben lidiar con:

- los límites de velocidad de la API,
- los tiempos de espera de conexión,
- las descargas lentas y
- los propietarios del sistema de origen que no están contentos debido a la presión ejercida sobre sus sistemas.

**Visual:** icono lineal de un cronómetro con las letras **MS** (milisegundos) en la esfera.

## Slide 19

Separador de sección (misma imagen decorativa de mano robótica).

**3. Data Pipelines — Patrones Comunes de Data Pipelines · ETL y ELT**

## Slide 20

Slide de actividad/comparación en formato de matriz vacía (para completar en clase).

Dos encabezados de columna en cajas celestes: **ETL** y **ELT**. Tres filas grises de preguntas que abarcan ambas columnas:

| | ETL | ELT |
|---|---|---|
| ¿De qué trata? | | |
| Ejemplos para Ciencia de Datos (2) | | |
| Una ventaja contra ETL o ELT (respectivamente) | | |

**Visual:** icono decorativo a la derecha — cuatro personas en círculo punteado alrededor de dos globos de diálogo (discusión grupal).

## Slide 21

Slide de cierre sin texto. Foto decorativa de dos estudiantes con lentes de seguridad y batas trabajando en un equipo de laboratorio, con overlay azul.
