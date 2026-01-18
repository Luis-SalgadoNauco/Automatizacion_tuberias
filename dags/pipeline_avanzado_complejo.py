from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
import random

# --------------------------------------------------
# Funciones de negocio
# --------------------------------------------------

def validar_calidad_datos(**context):
    """Simula validación de calidad de datos"""
    calidad = random.choice(['alta', 'media', 'baja'])
    context['task_instance'].xcom_push(key='calidad', value=calidad)
    print(f"Calidad de datos detectada: {calidad}")
    return calidad


def decidir_procesamiento(**context):
    """Decide la ruta según la calidad de los datos"""
    calidad = context['task_instance'].xcom_pull(
        task_ids='validar_calidad',
        key='calidad'
    )

    if calidad == 'alta':
        return 'procesamiento_rapido'
    elif calidad == 'media':
        return 'procesamiento_completo'
    else:
        return 'procesamiento_pesado.paso1'


def procesamiento_rapido():
    print("🚀 Procesamiento rápido para datos de alta calidad")
    return "Procesado rápido"


def procesamiento_completo():
    print("🧠 Procesamiento completo con validaciones adicionales")
    return "Procesado completo"


# --------------------------------------------------
# Definición del DAG
# --------------------------------------------------

default_args = {
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(hours=1)
}

dag = DAG(
    dag_id='pipeline_avanzado_complejo',
    description='Pipeline con branching, TaskGroups y buenas prácticas',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args=default_args
)

# --------------------------------------------------
# Tareas del DAG
# --------------------------------------------------

inicio = DummyOperator(
    task_id='inicio',
    dag=dag
)

validar = PythonOperator(
    task_id='validar_calidad',
    python_callable=validar_calidad_datos,
    provide_context=True,
    dag=dag
)

decidir = BranchPythonOperator(
    task_id='decidir_ruta',
    python_callable=decidir_procesamiento,
    provide_context=True,
    dag=dag
)

ruta_rapida = PythonOperator(
    task_id='procesamiento_rapido',
    python_callable=procesamiento_rapido,
    dag=dag
)

ruta_completa = PythonOperator(
    task_id='procesamiento_completo',
    python_callable=procesamiento_completo,
    dag=dag
)

# --------------------------------------------------
# TaskGroup: procesamiento pesado
# --------------------------------------------------

with TaskGroup('procesamiento_pesado', dag=dag) as procesamiento_group:
    paso1 = PythonOperator(
        task_id='paso1',
        python_callable=lambda: print("Paso 1"),
        dag=dag
    )

    paso2 = PythonOperator(
        task_id='paso2',
        python_callable=lambda: print("Paso 2"),
        dag=dag
    )

    paso3 = PythonOperator(
        task_id='paso3',
        python_callable=lambda: print("Paso 3"),
        dag=dag
    )

    paso1 >> paso2 >> paso3

union = DummyOperator(
    task_id='union_rutas',
    trigger_rule='none_failed_min_one_success',
    dag=dag
)

fin = DummyOperator(
    task_id='fin',
    dag=dag
)

# --------------------------------------------------
# Dependencias
# --------------------------------------------------

inicio >> validar >> decidir

decidir >> ruta_rapida
decidir >> ruta_completa
decidir >> procesamiento_group

[ruta_rapida, ruta_completa, procesamiento_group] >> union >> fin
