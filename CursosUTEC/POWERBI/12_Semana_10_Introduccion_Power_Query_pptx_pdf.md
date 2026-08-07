---
curso: POWERBI
titulo: 12 - Semana 10/Introducción Power Query__pptx
slides: 15
fuente: 12 - Semana 10/Introducción Power Query__pptx.pdf
---

## Slide 1

Portada del capítulo. Título: "Introducción Power Query". Fondo degradado turquesa/celeste con textura de hexágonos, foto decorativa de un edificio (torre UTEC) a la derecha. Elementos decorativos: logo UTEC, lema "Reinventa el mundo", cruz amarilla decorativa. Sin contenido técnico adicional.

## Slide 2

Título: "Objetivo de sesión aquí". Texto dentro de un recuadro con esquinas en forma de corchete decorativo:

"Es una herramienta fundamental para la automatización, transformación y limpieza de datos dentro del entorno de Excel y Power BI. El curso tiene como propósito proporcionar una comprensión sólida de los conceptos básicos de Power Query, permitiendo a los usuarios importar datos desde diversas fuentes, realizar transformaciones eficientes, combinar tablas y preparar conjuntos de datos listos para el análisis."

## Slide 3

Título: "Contenido de sesión aquí". Diagrama de 3 bloques numerados (01, 02, 03), cada uno dentro de un marco tipo corchete:
- **01** — ¿Qué es Power Query?
- **02** — Proceso ETL
- **03** — Ejercicios

## Slide 4

Slide separadora de sección "01." con ícono de portapapeles/checklist y texto "¿Qué es Power Query?". Solo título de sección, sin contenido adicional.

## Slide 5

Título: "Power Query".

Texto: "Power Query es un motor de preparación de datos el cual permite: adecuar, limpiar, formatear, consolidar, crear, refinar y hasta resumir datos de forma veloz, intuitiva y coherente sin apenas código.
Existen dos grandes versiones de Power Query:
- Power Query de Escritorio (Desktop)
- Power Query en la Nube (Online) – Flujos de datos"

**Diagrama de flujo** (lado derecho): tres íconos de fuentes de datos en la parte superior — archivo CSV, base de datos (cilindros), archivo XLS — cada uno con una flecha que baja y converge hacia un recuadro central etiquetado "power query" (ícono verde de engranajes/flujo). Desde ese recuadro, una flecha baja hacia dos íconos de destino: Power BI y Excel (ícono verde con "X"). El diagrama ilustra el flujo: fuentes de datos → motor Power Query → herramientas de consumo (Power BI / Excel).

## Slide 6

Título: "Power Query".

Texto: "Power query de escritorio se encuentra en:" — seguido de 3 logos: Excel (ícono verde "X"), Power BI, y Microsoft SQL Server.

Texto: "Power query en la nube se encuentra en:" — seguido de 5 logos: Power BI, PowerApps, Power Automate, Azure Data Factory, Fabric Data Factory.

## Slide 7

Título: "Proceso ETL".

Texto: "El proceso ETL hace parte de la integración de datos, en otras palabras, es una pieza importante en la orquestación y automatización del movimiento y transformación de datos estructurados y no estructurados, las letras ETL significan:
a. Extracción
b. Transformación
c. Carga

Las siglas derivan del inglés: **Extract, Transform** and **Load**. Este proceso consiste en llevar datos de múltiples orígenes, para luego hacer la limpieza necesaria, y finalmente dejarlos en el destino listos para el consumo, con un contexto que los dota del significado adecuados para proporcionar información significativa a los analistas, científicos de datos y responsables de decisiones empresariales."

## Slide 8

Título: "¿Cómo ir al editor de Power Query?"

Texto: "Existen dos caminos bien definidos para ir al Editor de Power Query en escritorio, la primera es ir a secas, para ello:
1. Abrimos un archivo en blanco de Power BI.
2. Vamos a la pestaña Inicio, grupo Datos externos, desplegamos las opciones de Editar consultas y pulsamos clic en Editar Consultas:"

**Captura de pantalla**: ventana "Sin título - Editor de Power Query" vacía (sin consultas cargadas). Se ve la cinta de opciones con pestañas Archivo, Inicio, Transformar, Agregar columna, Vista, Herramientas, Ayuda, y los grupos de botones: Cerrar y aplicar, Nuevo origen/Orígenes recientes/Especificar datos, Configuración de origen de datos, Administrar parámetros, Consulta (Propiedades/Editor avanzado/Administrar), Administrar columnas (Elegir/Quitar columnas), Reducir filas/Ordenar, Transformar (Dividir columna/Agrupar por/Tipo de datos/Reemplazar valores), Combinar, Conclusiones de IA (Text Analytics/Visión/Azure Machine Learning). Panel izquierdo "Consultas [0]" vacío, área central de datos vacía.

## Slide 9

Título: "Transformación".

Texto: "incluye muchas funciones de transformación que se pueden usar a través de la interfaz gráfica del editor de Power Query. Estas transformaciones pueden ser tan sencillas como quitar una columna o filtrar filas, o tan habituales como usar la primera fila como encabezado de tabla. También hay opciones de transformación avanzadas, como combinar, anexar, agrupar (por), dinamizar y anular la dinamización.

Todas estas transformaciones son posibles al elegir la opción de transformación en el menú y aplicar las opciones necesarias para esa transformación. En la siguiente ilustración se muestran algunas de las transformaciones disponibles en el editor de Power Query."

**Captura de pantalla**: tres franjas de cinta de opciones de Power Query (en inglés) mostrando grupos de comandos de transformación:
- Fila 1: Table (Group By, Use First Row as Headers, Reverse Rows, Count Rows, Transpose), Any Column (Detect Data Type, Rename, Data Type, Replace Values, Fill, Pivot Column, Unpivot Columns, Move, Convert to List), Text Column (Split Column, Format), Number Column (Statistics, Standard, Scientific, Trigonometry, Rounding, Information), Date & Time Column (Date, Time, Duration), Structured Column (Expand, Aggregate, Extract Values), Scripts (Run R script, Run Python script).
- Fila 2: Close (Close & Apply), New Query (New Source, Recent Sources, Enter Data), Data Sources, Parameters, Query (Refresh Preview, Properties, Advanced Editor, Manage), Manage Columns (Choose/Remove Columns), Reduce Rows (Keep/Remove Rows), Sort, Transform (Split Column, Group By, Data Type, Use First Row as Headers, Replace Values), Combine (Merge/Append Queries, Combine Files), AI Insights (Text Analytics, Vision, Azure Machine Learning).
- Fila 3: General (Column From Examples, Custom Column, Invoke Custom Function, Duplicate Column), From Text (Conditional Column, Merge Columns, Format, Extract, Parse), From Number (Statistics, Standard, Scientific, Trigonometry, Rounding, Information), From Date & Time (Date, Time, Duration), AI Insights (Text Analytics, Vision, Azure Machine Learning).

## Slide 10

Título: "Transformación" (misma serie de slides de UI anotada).

**Captura de pantalla anotada**: ventana "Sin título - Editor de Power Query" con un recuadro azul resaltando toda la cinta de opciones superior (pestañas Archivo, Inicio, Transformar, Agregar columna, Vista, Herramientas, Ayuda y sus botones), rotulada con la etiqueta azul **"Cinta de Opciones"** debajo. Panel izquierdo "Consultas [0]" vacío, sin resaltar.

## Slide 11

Título: "Transformación" (misma captura base).

**Captura de pantalla anotada**: recuadro azul resaltando el panel izquierdo "Consultas [0]" (que muestra 3 líneas placeholder simulando consultas listadas), rotulado con la etiqueta azul **"Panel de consultas"**.

## Slide 12

Título: "Transformación" (misma captura base).

**Captura de pantalla anotada**: recuadro azul resaltando el área central grande de la ventana (debajo de la cinta, a la derecha del panel de consultas), rotulada con la etiqueta azul **"Visualización de los datos"**.

## Slide 13

Título: "Transformación" (misma captura base).

**Captura de pantalla anotada**: recuadro azul resaltando el panel derecho de la ventana, rotulado con la etiqueta azul **"Propiedades"**.

## Slide 14

Título: "Conclusiones aquí". Cuatro bloques numerados (01-04), cada uno con marco tipo corchete azul:

- **01**: "Power Query es una herramienta poderosa y accesible que permite a los usuarios de Excel y Power BI automatizar tareas repetitivas de manipulación de datos, sin necesidad de conocimientos avanzados en programación."
- **02**: "La transformación y limpieza de datos se vuelve más eficiente, lo que permite dedicar menos tiempo a tareas manuales y más tiempo al análisis y toma de decisiones basada en información confiable."
- **03**: "Los conocimientos adquiridos permiten trabajar con múltiples fuentes de datos, combinarlas, filtrarlas y estructurarlas de manera flexible, resolviendo problemas comunes en el manejo de bases de datos empresariales, financieras, académicas, entre otras."
- **04**: "Este curso sienta las bases para continuar explorando herramientas avanzadas, como Power BI, DAX y modelos de datos más complejos, formando un ecosistema sólido para la inteligencia de negocios y la analítica de datos moderna."

## Slide 15

Slide de cierre — decorativa. Fondo degradado celeste/turquesa con textura hexagonal, logo grande UTEC centrado (isotipo + "Universidad de Ingeniería y Tecnología"), cruz amarilla decorativa. Sin contenido textual adicional (slide de cierre/contraportada).
