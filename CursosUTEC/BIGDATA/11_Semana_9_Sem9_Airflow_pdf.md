---
curso: BIGDATA
titulo: 11 - Semana 9/Sem9_Airflow
slides: 41
fuente: 11 - Semana 9/Sem9_Airflow.pdf
---

## Slide 1
Portada (decorativa). Título grande: **Airflow**. Subtítulo: "Mg. Aldo Lezama Benavides". Etiqueta "Semana 9". Fondo cian con foto del edificio UTEC.

## Slide 2
**Objetivo de la sesión**

- **Comprender** el concepto de orquestación de datos y cómo Apache Airflow permite automatizar y coordinar flujos de trabajo complejos en entornos analíticos y de ingeniería de datos.
- **Conocer** la estructura y componentes de un DAG (Directed Acyclic Graph) en Airflow, entendiendo cómo se definen las tareas, dependencias y parámetros de ejecución.
- **Explorar** la interfaz de usuario de Airflow, tanto en entorno local como en la nube (GCP), para monitorear, programar y gestionar la ejecución de flujos de trabajo.

## Slide 3
**Contenido de la sesión** — índice visual de 4 bloques numerados entre corchetes:

| # | Tema |
|---|------|
| 01 | Orquestación de datos |
| 02 | Introducción a Apache Airflow |
| 03 | DAG: Concepto y Estructura |
| 04 | Interfaz en Airflow Local y en GCP |

## Slide 4
Portada de sección: **01.** con icono de portapapeles/checklist — "¿Qué es la orquestación de datos?"

## Slide 5
**Orquestación Flujo de Trabajo**

Texto: "La orquestación del flujo de trabajo se refiere a la coordinación, gestión y automatización de múltiples tareas y procesos organizacionales. Se trata de garantizar que los diferentes sistemas, herramientas y departamentos trabajen en armonía para lograr el resultado deseado."

Visual (ilustración a la derecha, título "ORQUESTACIÓN DE DATOS"): diagrama de flujo estilo infografía. Un documento → un nodo de grafo (icono de puntos conectados) → una laptop cuyo centro muestra una base de datos (cilindro azul); a la izquierda de la laptop entra un flujo binario (0110001 / 0101101 / 010010) y a la derecha sale otro flujo binario (01010001...) hacia un gráfico de barras ascendente con flecha. Arriba a la derecha, el logo de Apache Airflow (molinete de colores). Marca de agua "ChatGPT" en la esquina.

## Slide 6
**Flujo Orquestado vs Flujo No Orquestado**

Comparación de dos diagramas lado a lado:

- **1 Orchestrated** (Flujo de trabajo orquestado): un nodo teal "Orchestrator" en la cima, con flecha descendente a "Task 1" → "Task 2" → "Task 3" (cadena secuencial controlada por el orquestador).
- **2 Un-orchestrated** (Flujo de trabajo no orquestado): dos nodos "Manual" y "Manual" arriba, ambos con flechas convergiendo a un nodo "Ad-hoc", que a su vez apunta a "Task 2". Flujo desordenado, sin coordinación central.

## Slide 7
Portada de sección: **02.** con icono de checklist — "Introducción a Apache Airflow".

## Slide 8
**Apache Airflow**

"Apache Airflow es una plataforma creada por la comunidad para crear, programar y monitorear los flujos de trabajo de manera programática. Fue creada por Airbnb en octubre de 2014 como solución para la gestión de flujos de trabajo dentro de la empresa.

Airflow se usa para automatizar trabajos programáticamente dividiéndolos en subtareas. Permite su planificación y monitorización desde una herramienta centralizada. Los casos de uso más comunes son la automatización de ingestas de datos, acciones de mantenimiento periódicas y tareas de administración. Para ello, permite planificar trabajos como un cron y también ejecutarlos bajo demanda."

Visual: logo grande de Apache Airflow (molinete multicolor rojo/azul/verde/cian) con el texto "Apache Airflow".

## Slide 9
**Características Apache Airflow (1)**

Entre sus principales características podemos destacar:

- **Python puro:** permite utilizar las funciones estándar de Python para crear sus flujos de trabajo, incluidos los formatos de fecha y hora para la programación y bucles para generar tareas de forma dinámica.
- **UI útil:** permite supervisar, programar y administrar sus flujos de trabajo a través de una aplicación web sólida y moderna. Siempre te permitirá tener una visión completa del estado y los registros de las tareas completadas y en curso.
- **Integraciones robustas:** Airflow proporciona muchos operadores plug-and-play que están listos para ejecutar sus tareas en Google Cloud Platform, Amazon Web Services, Microsoft Azure y muchos otros servicios de terceros.

Visual (recuadro derecho, título "APACHE AIRFLOW"): infografía de 6 iconos — logo Python (".ES PYTHON PURO"), molinete Airflow (centro), eslabones de cadena ("INTEGRACIÓN ROBUSTA"), pulgar arriba ("FÁCIL DE USAR"), monitor con dashboard ("U ÚTIL"), candado abierto ("FUENTE ABIERTA").

## Slide 10
**Características Apache Airflow (2)**

- **Fácil de usar:** Cualquiera con conocimientos de Python puede implementar un flujo de trabajo. Apache Airflow no limita el alcance de sus canalizaciones; permite usarlo para crear modelos de aprendizaje automático, transferir datos, administrar su infraestructura y más.
- **Fuente abierta:** Donde quiera que el usuario desee, puede compartir los cambios y mejoras abriendo un PR. Es así de simple, sin barreras, sin procedimientos prolongados. Airflow tiene muchos usuarios activos que comparten voluntariamente sus experiencias.

Visual: misma infografía de 6 iconos "APACHE AIRFLOW" que la slide 9.

## Slide 11
**Ventajas Apache Airflow (1)**

- Descripción de los flujos de trabajo en Python con soporte para la gama completa de funciones.
- Se pueden implementar flujos de trabajo complejos y dinámicos.
- Numerosos operadores listos para usar disponibles.
- Se pueden diseñar operadores individuales.
- Interfaz web gráfica para supervisar, gestionar y planificar los flujos de trabajo.

Visual (rueda "Ventajas"): diagrama radial con el logo Apache Airflow + "itop Consulting" al centro, rodeado de 8 iconos circulares azules con etiquetas: Gran comunidad disponible, Software disponible, Muchos usuarios en todo el mundo, Interfaz web gráfica, Descripción de los flujos de trabajo en Python, Diseñar operadores individuales, Flujos de trabajo complejos y dinámicos, Numerosos operadores listos.

## Slide 12
**Ventajas Apache Airflow (2)**

- El estado del flujo de trabajo se puede rastrear en vivo.
- Arquitectura modular con escalabilidad casi ilimitada.
- Software disponible gratuitamente.
- Muchos usuarios en todo el mundo y proyecto de alto nivel de la Apache Software Foundation.
- Gran comunidad disponible en la web.

Visual: misma rueda radial "Ventajas" con logo Airflow + itop al centro y los 8 iconos que en la slide 11.

## Slide 13
Portada de sección: **03.** con icono de checklist — "DAG: Concepto y Estructura".

## Slide 14
**Introducción a DAG**

Un DAG significa Gráfico Acíclico Dirigido.

- En Airflow, representa el conjunto de tareas que conforman tu flujo de trabajo.
- Consiste en las tareas y las dependencias entre ellas.
- Se crea con diversos detalles sobre el DAG, incluyendo el nombre, la fecha de inicio, el propietario, etc.

Visual (recuadro derecho, título "Directed Acyclic Graph"): grafo dirigido con 5 nodos azules numerados. Aristas: 1 → 2, 1 → 3, 2 → 4, 2 → 5. Los nodos 4 y 5 son terminales; ninguna arista regresa (acíclico).

## Slide 15
**Introducción a DAG**

- Un DAG (Directed Acyclic Graph) en Airflow es una estructura que define un flujo de trabajo compuesto por tareas que se ejecutan en un orden específico, sin ciclos.

**Componentes clave de un DAG**
- **DAG:** Es el contenedor del flujo de trabajo.
- **Tareas (Tasks):** Unidades individuales de ejecución (por ejemplo, ejecutar una función Python o un comando Bash).
- **Dependencias:** Relaciones entre tareas que indican el orden de ejecución.

Visual (captura de la UI de Airflow): pantalla del DAG `latest_only_with_trigger`, Run 2024-03-24 09:00:00 CET, con pestañas Details / Graph / Gantt / Code / Audit Log. A la izquierda un panel "Duration" con gráfico de barras verdes de duración por ejecución y una cuadrícula de estados (latest_only, task1..task4) en verde/rosado. A la derecha el Graph View con cajas: `latest_only` (success, LatestOnlyOperator) → `task1` (skipped, EmptyOperator) → `task2` (success) y `task4` (success); `task3` (skipped). Códigos de color: verde=success, rosado=skipped; leyenda "deferred/failed" arriba a la derecha.

## Slide 16
**Introducción a DAG**

- **¿Por qué es acíclico?:** No puede haber ciclos: una tarea no puede depender de sí misma directa o indirectamente. Esto garantiza que el flujo tenga un inicio y un fin claro.
- **Cómo se define:** Se define como código Python (Workflow as Code). Puede incluir lógica condicional, programación, y reutilización de funciones o scripts externos.
- **Visualización:** Airflow permite ver los DAGs gráficamente (Graph View, Tree View). Se puede monitorear el estado de cada ejecución de tarea (éxito, fallo, en espera).

Visual: la misma captura de la UI de Airflow (DAG `latest_only_with_trigger`, Graph View con task1..task4) que la slide 15.

## Slide 17
**Código de ejemplo de un DAG**

Definición simple de un DAG:

```python
etl_dag = DAG( dag_id='etl_pipeline', default_args={"start_date": "2025-10-06"} )
```

**DAG** — Es una clase de Airflow que define un flujo de tareas (tasks) y sus dependencias. El DAG organiza cómo y cuándo se ejecutan esas tareas.

**dag_id='etl_pipeline'** — Este es el identificador único del DAG dentro de Airflow. En este caso, el DAG se llama "etl_pipeline", lo que sugiere que está diseñado para un pipeline ETL (extracción, transformación y carga de datos).

**default_args={"start_date": "2025-10-06"}** — Define argumentos por defecto que usarán las tareas dentro del DAG.
- start_date indica la fecha de inicio desde la cual Airflow comenzará a programar ejecuciones.
- A partir de esta fecha, Airflow puede decidir cuándo correr el flujo (por ejemplo, diariamente o semanalmente, según la configuración del DAG).

(En la slide las partes del código están resaltadas con color: `DAG` en azul, `dag_id` en rojo, `default_args` en morado.)

## Slide 18
**Estructura de un DAG**

Bloque de código (imports):

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
```

"Se cargan los módulos de Airflow y Python necesarios para definir tareas, operadores y el DAG."

## Slide 19
**Estructura de un DAG**

Bloque de código (argumentos por defecto):

```python
default_args = {
    'owner': 'aldo',
    'retries': 2,
    'retry_delay': timedelta(minutes=3),
    ...
}
```

"Se definen parámetros comunes a todas las tareas: reintentos, alertas, tiempo de espera, etc."

## Slide 20
**Estructura de un DAG**

Bloque de código (definición del DAG con context manager):

```python
with DAG(
    dag_id='dag_proceso_etl_complejo',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='0 6 * * *',  # Todos los días a las 6am
    catchup=False
) as dag:
```

## Slide 21
**Estructura de un DAG**

Repite el mismo bloque de código de la slide 20:

```python
with DAG(
    dag_id='dag_proceso_etl_complejo',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='0 6 * * *',  # Todos los días a las 6am
    catchup=False
) as dag:
```

## Slide 22
**Estructura de un DAG**

Texto centrado (sin bloque de código):

"Cada bloque representa una tarea. Pueden ser funciones en Python (PythonOperator), comandos de consola (BashOperator), o nodos simbólicos (DummyOperator)."

## Slide 23
**Estructura de un DAG**

Bloque de código (dependencias en paralelo):

```python
validar >> [transformar_cliente, transformar_producto]
```

"Las tareas transformar_cliente y transformar_producto se ejecutan en paralelo, luego del proceso de validar."

## Slide 24
**Estructura de un DAG**

Bloque de código (flujo completo con inicio y fin):

```python
inicio >> extraer >> validar
[transformar_1, transformar_2] >> modelo >> fin
```

"El DAG tiene un inicio simbólico, tareas intermedias, y un final. Esto ayuda a visualizar y controlar mejor el flujo."

## Slide 25
**Ejemplos DAGs**

Bloque de código completo (DAG básico de saludo):

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def saludar():
    print("Hola desde Airflow")

with DAG(
    dag_id='dag_saludo_basico',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['basico']
) as dag:
    tarea = PythonOperator(
        task_id='saludar',
        python_callable=saludar
    )
```

Notas (recuadro naranja):
- Se crea un DAG que se ejecuta diariamente (@daily).
- La tarea saludar imprime un mensaje en los logs.
- Es un ejemplo ideal para testear si Airflow está funcionando.

## Slide 26
**Ejemplos DAGs**

Bloque de código completo (pipeline ETL secuencial):

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extraer():
    print("Extrayendo datos...")
def transformar():
    print("Transformando datos...")
def cargar():
    print("Cargando datos...")

with DAG(
    dag_id='dag_etl_simple',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['etl']
) as dag:
    t1 = PythonOperator(task_id='extraer', python_callable=extraer)
    t2 = PythonOperator(task_id='transformar', python_callable=transformar)
    t3 = PythonOperator(task_id='cargar', python_callable=cargar)
    t1 >> t2 >> t3
```

Notas (recuadro naranja):
- t1 → t2 → t3: simula un pipeline ETL.
- Cada función representa una fase del proceso.
- Muestra cómo Airflow gestiona tareas secuenciales automáticamente.

## Slide 27
Portada de sección: **04.** con icono de checklist — "Interfaz".

## Slide 28
**Interfaz Usuario - Local**

Captura de pantalla de la UI de Airflow (versión moderna), página "Welcome". Barra lateral izquierda con navegación: Home, Dags, Assets, Browse, Admin, Security, Docs, User (logo Airflow arriba).
- **Stats:** píldoras "0 Failed dags", "0 Running dags", "0 Active dags".
- **Health:** etiquetas verdes MetaDatabase, Scheduler, Triggerer, Dag Processor (todas OK).
- **History:** selector "Last 24 hours" | rango 2025-07-30 07:37:13 – 2025-07-31 07:37:13.
- **Dag Runs (9):** Queued 0 (0.00%), Running 0 (0.00%), Success 9 (100.00%, barra verde llena), Failed 0 (0.00%).
- **Task Instances (9):** Success 9 (100.00%).
- Panel derecho **Asset Events (0):** "No Asset Events found."

## Slide 29
**Interfaz Usuario - Local**

Misma captura de la UI de Airflow que la slide 28, con una anotación numerada:

> **1** — Estadísticas del resultado de las ejecuciones de los DAGS: Fallos, Ejecutando y Activos.

Se resalta con recuadro naranja la sección **Stats** (Failed / Running / Active dags).

## Slide 30
**Interfaz Usuario - Local**

Misma captura, anotación:

> **2** — Indicadores de salud para componentes del sistema como MetaDatabase, Scheduler, Triggerer y Dag Processor.

Se resalta con recuadro naranja la sección **Health** (MetaDatabase, Scheduler, Triggerer, Dag Processor).

## Slide 31
**Interfaz Usuario - Local**

Misma captura, anotación:

> **3** — Historial de DAG e instancias de tarea, que muestra recuentos y tasas de éxito/fracaso durante un rango de tiempo seleccionable.

Se resalta con recuadro naranja la sección **History** (selector "Last 24 hours" y rango de fechas).

## Slide 32
**Interfaz Usuario - Local**

Misma captura, anotación:

> **4** — Eventos de activos recientes, incluidas materializaciones y DAG activados.

Se resalta con recuadro naranja el panel **Asset Events** ("No Asset Events found.").

## Slide 33
**Interfaz Usuario - Local**

Captura de la vista **Dags** (pestañas Dags / Runs / Task Instances), con buscador "Search Dags", filtro "by tag" y contador "82 D..." DAGs. Se resalta el ítem **Dags** de la barra lateral con anotación:

> **5** — La vista de lista de DAG en la barra de navegación principal. Muestra todos los DAG disponibles en su entorno, con un resumen claro de su estado, ejecuciones recientes y configuración.

Tabla de DAGs (columnas Dag / Schedule / Next Dag Run / Last Dag Run / Tags) con filas como: asset1_producer, asset2_producer, asset_alias_example_alias_consumer (Asset; tags asset-alias, consumer), asset_alias_example_alias_consumer_with_no_taskflow, asset_alias_example_alias_producer (tags producer, asset-alias), asset_alias_example_alias_producer_with_no_taskflow, asset_consumes_1 (schedule s3://dag1/output_1.txt; tags consumes, asset-scheduled), asset_consumes_1_and_2 (0 of 2 assets updated), asset_consumes_1_never_scheduled (0 of 2 assets updated). Cada fila con toggle de activación y botón de ejecutar (▷).

## Slide 34
**Interfaz Usuario - Local**

Captura de la vista Dags filtrada por la búsqueda "hello" → "1 Dag". Anotación:

> **6** — La vista de lista de DAG en la barra de navegación principal. Muestra todos los DAG disponibles en su entorno, con un resumen claro de su estado, ejecuciones recientes y configuración.

Fila del DAG **hello_airflow** (tags demo, ejemplo):
- Schedule: `0 0 * * *`
- Latest Run: 2025-07-30, 23:48:22 (check verde = success)
- Next Run: 2025-07-31, 19:00:00
- A la derecha, mini gráfico de barras verdes de historial de ejecuciones.

## Slide 35
**Interfaz Usuario - GCP**

Captura de la consola de **Google Cloud** (proyecto "ProyBigData-UTEC2026"), sección Solutions → categoría **Analytics** ("Collect, store, process and analyse large amounts of data"). Tabla Name / Description de productos:

| Producto | Descripción |
|---|---|
| BigQuery | Data warehouse/analytics |
| Pub/Sub | Global real-time messaging |
| Dataflow | Streaming analytics service |
| **Composer** | **Managed workflow orchestration service** |
| Dataproc | Managed Apache Spark and Apache Hadoop |
| Alteryx Designer Cloud | Visual data wrangling |
| Data Fusion | Data pipeline management |
| Looker | Enterprise BI and Analytics |
| Healthcare | Healthcare data storage and processing |
| Financial Services | Revenue growth through the cloud |
| Elastic Cloud | Data power to uncover actionable intelligence |
| Databricks | Platform for data, analytics and AI workloads |
| Earth Engine | Planetary-scale platform for Earth science |
| Managed service for A… (Kafka) | An Apache Kafka service for all use cases |
| Confluent Cloud | Managed data-streaming platform built on Apache Kafka and Apache Flink |

(Cloud Composer = el servicio de orquestación gestionado que corre Airflow; BigQuery y Dataproc aparecen "pinned".)

## Slide 36
**Interfaz Usuario - GCP**

Captura de Google Cloud → **Composer / Environments**. Estado inicial (sin entornos): tarjeta central "Cloud Composer — Environments" con texto "With Composer, you can easily create and manage Airflow environments. Get started by creating your first environment." y botones **Create environment** ▾ y **Learn more**.

## Slide 37
**Interfaz Usuario - GCP**

Captura de Google Cloud → **Environments** con un entorno ya creado. Barra de acciones: Create / Refresh / Delete. Banner informativo "Join Airflow community on 7–9 October during the Airflow Summit 2025... Register here". Tabla de entornos (columnas State, Name, Location, Composer version, Airflow version, Creation time, Update time, Airflow webserver, DAG list, Logs, DAGs folder, Labels):

- **composer-aldo** | State ✓ (verde) | Location us-central1 | Composer version 3 | Airflow version 2.10.5-build.15 | Creation 06/10/2025 16:58 | Update 06/10/2025 17:22 | Airflow webserver: link "Airflow" | DAG list: DAGs | Logs | DAGs folder: DAGs | Labels: None.

## Slide 38
**Interfaz Usuario - GCP**

Misma captura que la slide 37 (lista de Environments con el entorno **composer-aldo**, Composer v3, Airflow 2.10.5-build.15, us-central1, State OK).

## Slide 39
**Interfaz Usuario - GCP**

Captura de la **UI de Airflow clásica** dentro de Cloud Composer (entorno composer-aldo). Menú superior: DAGs, Cluster Activity, Datasets, Browse, Admin, Docs, Composer; reloj 22:42 UTC.
- Filtros: All (1), Active (1), Paused (0), Running (0), Failed (0), buscador "Search DAGs", toggle Auto-refresh.
- Tabla de DAGs (DAG / Owner / Runs / Schedule / Last Run / Next Run / Recent Tasks / Actions / Links):
  - **airflow_monitoring** | Owner: airflow | Runs: círculo con "2" (verde) | Schedule: `*/10 * * * *` | Last Run: 2025-10-06, 22:20:00 | Next Run: 2025-10-06, 22:30:00 | Recent Tasks: un círculo verde "1" | Actions: ejecutar / trigger / borrar.
- Pie: "Version: 2.10.5+composer — Environment Name: composer-aldo". "Showing 1-1 of 1 DAGs".

## Slide 40
**Conclusiones**

- **01.** Apache Airflow es una herramienta clave para la orquestación de datos, ya que permite automatizar pipelines complejos utilizando código Python y facilita la integración con múltiples plataformas (AWS, GCP, Azure).
- **02.** Los DAGs representan la base de Airflow, al permitir definir flujos de trabajo reproducibles, escalables y fácilmente monitorizables mediante dependencias entre tareas.
- **03.** La interfaz de Airflow ofrece una supervisión completa del estado de las ejecuciones, lo que ayuda a garantizar la confiabilidad y trazabilidad de los procesos ETL o de análisis de datos.

## Slide 41
Cierre (decorativa). Logo UTEC — "Universidad de Ingeniería y Tecnología" sobre fondo cian. Sin contenido textual adicional.
