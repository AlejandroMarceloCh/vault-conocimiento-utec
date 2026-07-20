---
curso: BIGDATA
titulo: 11 - Semana 9/ejercicio_dag_4
slides: 0
fuente: 11 - Semana 9/ejercicio_dag_4.py
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 11 - Semana 9/ejercicio_dag_4.py. -->

<!-- INTERPRETAR: código fuente (11 - Semana 9/ejercicio_dag_4.py). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

```py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

import pandas as pd

default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Función Python
def calcular_promedio():

    # Ruta del archivo en GCS montado por Composer
    ruta = "/home/airflow/gcs/data/Iris.csv"

    # Leer CSV
    df = pd.read_csv(ruta)

    # Calcular promedio
    promedio = df["SepalLengthCm"].mean()

    print(f"Promedio de sepal_length: {promedio}")

# DAG
with DAG(
    dag_id="clase_dag_ej_04",
    description="04. Leer y Procesar un CSV con PythonOperator",
    default_args=default_args,
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["gcp", "pandas"],
) as dag:

    tarea_promedio = PythonOperator(
        task_id="calcular_promedio",
        python_callable=calcular_promedio
    )

    tarea_promedio

```
