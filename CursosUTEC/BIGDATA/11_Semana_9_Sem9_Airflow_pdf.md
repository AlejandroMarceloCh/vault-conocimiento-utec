---
curso: BIGDATA
titulo: 11 - Semana 9/Sem9_Airflow
slides: 41
fuente: 11 - Semana 9/Sem9_Airflow.pdf
---

Airflow
Mg. Aldo Lezama Benavides


Semana 9
      Objetivo de la sesión

•   Comprender el concepto de orquestación de datos y cómo Apache

    Airflow permite automatizar y coordinar flujos de trabajo complejos en

    entornos analíticos y de ingeniería de datos

•   Conocer la estructura y componentes de un DAG (Directed Acyclic

    Graph)    en   Airflow,   entendiendo   cómo   se   definen   las   tareas,

    dependencias y parámetros de ejecución.

•   Explorar la interfaz de usuario de Airflow, tanto en entorno local como en

    la nube (GCP), para monitorear, programar y gestionar la ejecución de

    flujos de trabajo.
                  Contenido de la sesión

    01.                 02.               03.               04.

                                                          Interfaz en
Orquestación de      Introducción a   DAG: Concepto y
                                                        Airflow Local y
     datos           Apache Airflow     Estructura
                                                            en GCP
01.   ¿Qué es la orquestación de
      datos?
                           Orquestación Flujo de Trabajo




❑ La orquestación del flujo de trabajo se refiere a la

  coordinación, gestión y automatización de múltiples tareas

  y procesos organizacionales. Se trata de garantizar que

  los diferentes sistemas, herramientas y departamentos

  trabajen en armonía para lograr el resultado deseado
Flujo Orquestado vs Flujo No Orquestado




      Flujo de trabajo orquestado   Flujo de trabajo no orquestado
02.   Introducción a Apache
      Airflow
                                     Apache Airflow

Apache Airflow es una plataforma creada por la comunidad para crear,

programar y monitorear los flujos de trabajo de manera programática. Fue

creada por Airbnb en octubre de 2014 como solución para la gestión de flujos de

trabajo dentro de la empresa.

Airflow se usa para automatizar trabajos programáticamente dividiéndolos en

subtareas. Permite su planificación y monitorización desde una herramienta

centralizada. Los casos de uso más comunes son la automatización de ingestas

de datos, acciones de mantenimiento periódicas y tareas de administración.

Para ello, permite planificar trabajos como un cron y también ejecutarlos bajo

demanda.
                  Características Apache Airflow (1)

Entre sus principales características podemos destacar:

❑ Python puro: permite utilizar las funciones estándar de Python para crear sus

  flujos de trabajo, incluidos los formatos de fecha y hora para la programación

  y bucles para generar tareas de forma dinámica.

❑ UI útil: permite supervisar, programar y administrar sus flujos de trabajo a

  través de una aplicación web sólida y moderna. Siempre te permitirá tener

  una visión completa del estado y los registros de las tareas completadas y en

  curso.

❑ Integraciones robustas: Airflow proporciona muchos operadores plug-and-play

  que están listos para ejecutar sus tareas en Google Cloud Platform, Amazon

  Web Services, Microsoft Azure y muchos otros servicios de terceros.
                  Características Apache Airflow (2)


❑ Fácil de usar: Cualquiera con conocimientos de Python puede implementar un

  flujo de trabajo. Apache Airflow no limita el alcance de sus canalizaciones;

  permite usarlo para crear modelos de aprendizaje automático, transferir

  datos, administrar su infraestructura y más.



❑ Fuente abierta: Donde quiera que el usuario desee, puede compartir los

  cambios y mejoras abriendo un PR. Es así de simple, sin barreras, sin

  procedimientos prolongados. Airflow tiene muchos usuarios activos que

  comparten voluntariamente sus experiencias.
                           Ventajas Apache Airflow (1)


❑ Descripción de los flujos de trabajo en Python con soporte para la gama

  completa de funciones.

❑ Se pueden implementar flujos de trabajo complejos y dinámicos.

❑ Numerosos operadores listos para usar listos para usar disponibles.

❑ Se pueden diseñar operadores individuales.

❑ Interfaz web gráfica para supervisar, gestionar y planificar los flujos de

  trabajo.
                          Ventajas Apache Airflow (2)


❑ El estado del flujo de trabajo se puede rastrear en vivo.

❑ Arquitectura modular con escalabilidad casi ilimitada.

❑ Software disponible gratuitamente.

❑ Muchos usuarios en todo el mundo y proyecto de alto nivel de la Apache

  Software Foundation.

❑ Gran comunidad disponible en la web.
03.   DAG: Concepto y Estructura
                                         Introducción a DAG



Un DAG significa Gráfico Acíclico Dirigido.

• En Airflow, representa el conjunto de tareas que conforman tu flujo de

   trabajo.

• Consiste en las tareas y las dependencias entre ellas.

• Se crea con diversos detalles sobre el DAG, incluyendo el nombre, la fecha

   de inicio, el propietario, etc.
                                           Introducción a DAG

• Un DAG (Directed Acyclic Graph) en Airflow es

  una estructura que define un flujo de trabajo

  compuesto por tareas que se ejecutan en un orden

  específico, sin ciclos.

Componentes clave de un DAG

❑ DAG: Es el contenedor del flujo de trabajo.

❑ Tareas    (Tasks):    Unidades     individuales    de

  ejecución (por ejemplo, ejecutar una función

  Python o un comando Bash).

❑ Dependencias:     Relaciones     entre   tareas   que

  indican el orden de ejecución.
                                           Introducción a DAG

• ¿Por qué es acíclico?: No puede haber ciclos: una

  tarea no puede depender de sí misma directa o

  indirectamente. Esto garantiza que el flujo tenga un

  inicio y un fin claro.

• Cómo se define: Se define como código Python

  (Workflow as Code).Puede incluir lógica condicional,

  programación, y reutilización de funciones o scripts

  externos

• Visualización:      Airflow   permite   ver   los   DAGs

  gráficamente (Graph View, Tree View).Se puede

  monitorear el estado de cada ejecución de tarea

  (éxito, fallo, en espera).
                        Código de ejemplo de un DAG
Definición simple de un DAG


               etl_dag = DAG ( dag_id='etl_pipeline’, default_args={"start_date": "2025-10-06"} )


DAG
Es una clase de Airflow que define un flujo de tareas (tasks) y sus dependencias.
El DAG organiza cómo y cuándo se ejecutan esas tareas.
dag_id='etl_pipeline’
Este es el identificador único del DAG dentro de Airflow.En este caso, el DAG se llama "etl_pipeline", lo que sugiere
que está diseñado para un pipeline ETL (extracción, transformación y carga de datos).
default_args={"start_date": "2025-10-06"}
Define argumentos por defecto que usarán las tareas dentro del DAG.
• start_date indica la fecha de inicio desde la cual Airflow comenzará a programar ejecuciones.
• A partir de esta fecha, Airflow puede decidir cuándo correr el flujo (por ejemplo, diariamente o semanalmente,
  según la configuración del DAG).
                       Estructura de un DAG

         from airflow import DAG
                                             from airflow import DAG
         from airflow.operators.python    import PythonOperator
                             from airflow.operators.python import PythonOperator
                                  from airflow.operators.bash import BashOperator
         from airflow.operators.bash    import BashOperator
                             from airflow.operators.dummy import DummyOperator
         from airflow.operators.dummy import DummyOperator




Se cargan los módulos de Airflow y Python necesarios para definir tareas, operadores y el DAG
                        Estructura de un DAG

         default_args = {
             'owner': 'aldo',
                                                from airflow import DAG
             'retries': 2,       from airflow.operators.python import PythonOperator
                                   from airflow.operators.bash import BashOperator
             'retry_delay': timedelta(minutes=3),
                                from airflow.operators.dummy import DummyOperator

             ...
         }



Se definen parámetros comunes a todas las tareas: reintentos, alertas, tiempo de espera, etc.
             Estructura de un DAG

with DAG(
  dag_id='dag_proceso_etl_complejo',
  default_args=default_args,        from airflow import DAG
                     from airflow.operators.python import PythonOperator
  start_date=datetime(2023,
                       from      1, 1),
                            airflow.operators.bash import BashOperator
                    from airflow.operators.dummy import DummyOperator
  schedule_interval='0 6 * * *', # Todos los días a las 6am
  catchup=False
) as dag:

             Estructura de un DAG

with DAG(
  dag_id='dag_proceso_etl_complejo',
  default_args=default_args,        from airflow import DAG
                     from airflow.operators.python import PythonOperator
  start_date=datetime(2023,
                       from      1, 1),
                            airflow.operators.bash import BashOperator
                    from airflow.operators.dummy import DummyOperator
  schedule_interval='0 6 * * *', # Todos los días a las 6am
  catchup=False
) as dag:
Estructura de un DAG


        Cada bloque representa una tarea.

 Pueden ser funciones en Python (PythonOperator)

      comandos de consola (BashOperator),

      o nodos simbólicos (DummyOperator).
            Estructura de un DAG

validar >> [transformar_cliente, transformar_producto]


                                    from airflow import DAG
                     from airflow.operators.python import PythonOperator
                       from airflow.operators.bash import BashOperator
                    from airflow.operators.dummy import DummyOperator




 Las tareas transformar_cliente y transformar_producto se ejecutan en
 paralelo, luego del proceso de validar
             Estructura de un DAG

inicio >> extraer >> validar
[transformar_1, transformar_2] >> modelo >> fin
                                      from airflow import DAG
                       from airflow.operators.python import PythonOperator
                         from airflow.operators.bash import BashOperator
                      from airflow.operators.dummy import DummyOperator




 El DAG tiene un inicio simbólico, tareas intermedias, y un final. Esto ayuda a
 visualizar y controlar mejor el flujo.
                                     Ejemplos DAGs

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
def saludar():
  print("Hola desde Airflow")
                                                      •   Se crea un DAG que se ejecuta diariamente (@daily)
with DAG(
  dag_id='dag_saludo_basico',                         •   La tarea saludar imprime un mensaje en los logs.

  start_date=datetime(2025, 1, 1),                    •   Es un ejemplo ideal para testear si Airflow está

  schedule_interval='@daily',                             funcionando.

  catchup=False,
  tags=['basico']
) as dag:
  tarea = PythonOperator(
      task_id='saludar',
      python_callable=saludar
  )
                                        Ejemplos DAGs
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
def extraer():
  print("Extrayendo datos...")
def transformar():
  print("Transformando datos...")                                           •   t1 → t2 → t3: simula un pipeline ETL.
def cargar():
                                                                            •   Cada función representa una fase del proceso.
  print("Cargando datos...")
                                                                            •   Muestra cómo Airflow gestiona tareas secuenciales
with DAG(
                                                                                automáticamente
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
04.   Interfaz
Interfaz Usuario - Local
Interfaz Usuario - Local

              Estadísticas del resultado de las
          1   ejecuciones de los DAGS: Fallos,
              Ejecutando y Activos.
Interfaz Usuario - Local


              Indicadores   de   salud      para
              componentes del sistema como
          2   MetaDatabase, Scheduler, Triggerer
              y Dag Processor
Interfaz Usuario - Local




            Historial de DAG e instancias de
            tarea, que muestra recuentos y
        3   tasas de éxito/fracaso durante un
            rango de tiempo seleccionable
Interfaz Usuario - Local




                               Eventos de activos recientes,
                           4   incluidas materializaciones y DAG
                               activados
                         Interfaz Usuario - Local


    La vista de lista de DAG en la barra
    de navegación principal. Muestra
    todos los DAG disponibles en su
5   entorno, con un resumen claro de
    su estado, ejecuciones recientes y
    configuración..
                  Interfaz Usuario - Local

    La vista de lista de DAG en la barra
    de navegación principal. Muestra
    todos los DAG disponibles en su
6   entorno, con un resumen claro de
    su estado, ejecuciones recientes y
    configuración.
Interfaz Usuario - GCP
Interfaz Usuario - GCP
Interfaz Usuario - GCP
Interfaz Usuario - GCP
Interfaz Usuario - GCP
                     Conclusiones
      Apache Airflow es una herramienta clave para la orquestación de datos, ya que
01.   permite automatizar pipelines complejos utilizando código Python y facilita la
      integración con múltiples plataformas (AWS, GCP, Azure).


      Los DAGs representan la base de Airflow, al permitir definir flujos de trabajo
02.   reproducibles, escalables y fácilmente monitorizables mediante dependencias
      entre tareas


      La interfaz de Airflow ofrece una supervisión completa del estado de las
03.   ejecuciones, lo que ayuda a garantizar la confiabilidad y trazabilidad de los
      procesos ETL o de análisis de datos.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
