---
curso: BIGDATA
titulo: 11 - Semana 9/ejercicio_dag_1
slides: 0
fuente: 11 - Semana 9/ejercicio_dag_1.py
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 11 - Semana 9/ejercicio_dag_1.py. -->

<!-- INTERPRETAR: código fuente (11 - Semana 9/ejercicio_dag_1.py). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

```py
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

from airflow import DAG

default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5)
    }

with DAG(dag_id="clase_dag_ej_01", description="1. Un DAG básico",
    schedule=timedelta(days=1),
    default_args=default_args,
    start_date=datetime(2021, 1, 1),
    catchup=False
) as dag:
    
	print_hello = BashOperator(task_id='print_hello', bash_command='echo "hello"')

print_hello

```
