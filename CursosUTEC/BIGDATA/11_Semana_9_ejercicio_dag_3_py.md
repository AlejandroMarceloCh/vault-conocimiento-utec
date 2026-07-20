---
curso: BIGDATA
titulo: 11 - Semana 9/ejercicio_dag_3
slides: 0
fuente: 11 - Semana 9/ejercicio_dag_3.py
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 11 - Semana 9/ejercicio_dag_3.py. -->

<!-- INTERPRETAR: código fuente (11 - Semana 9/ejercicio_dag_3.py). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

```py
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    }

with DAG( 
    dag_id="clase_dag_ej_03", 
    description="03. Tarea Programada",
    default_args=default_args,
    schedule="40 23 * * *",
    start_date=datetime(2026, 5, 1),
    catchup=False
) as dag:
    
    paso_01 = BashOperator(task_id='Terminado', bash_command='echo "Este Script se ejecutará a las 18:40"')
 
    paso_01

```
