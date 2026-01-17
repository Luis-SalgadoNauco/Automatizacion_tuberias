from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def saludar():
    print("¡Hola desde Airflow!")
    return "Saludo completado"

with DAG(
    dag_id='saludo_diario',
    description='DAG que saluda cada día',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['ejemplo', 'saludo']
) as dag:

    tarea_bash = BashOperator(
        task_id='tarea_bash',
        bash_command='echo "Ejecutando tarea bash a las $(date)"'
    )

    tarea_python = PythonOperator(
        task_id='tarea_python',
        python_callable=saludar
    )

    tarea_esperar = BashOperator(
        task_id='tarea_esperar',
        bash_command='sleep 5'
    )

    tarea_bash >> tarea_python >> tarea_esperar
