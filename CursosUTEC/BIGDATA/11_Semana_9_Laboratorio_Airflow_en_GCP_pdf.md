---
curso: BIGDATA
titulo: 11 - Semana 9/Laboratorio Airflow en GCP
slides: 2
fuente: 11 - Semana 9/Laboratorio Airflow en GCP.pdf
---

Laboratorio
Mg. Aldo Lezama Benavides


Semana 9
                    Recomendaciones a usar en Airflow

• Usar nombres de archivo simples y sin espacios: ejercicio_dag_01.py

• Guardar siempre los DAGs dentro de: gs://BUCKET/dags/

• Utilizar dag_id únicos y sin caracteres especiales: dag_id=“proceso_diario_01“

• Mantener task_id únicos dentro del DAG: task_id="cargar_clientes“

• Usar imports compatibles con la versión de Airflow/Composer: from airflow.operators.bash import BashOperator

• Definir siempre un start_date fijo: start_date=datetime(2026,1,1)

• Configurar catchup=False para evitar ejecuciones históricas masivas: catchup=False

• No repetir parámetros

• Mantener una indentación consistente (4 espacios)

• Separar scripts externos en carpetas como: dags/scripts/

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
