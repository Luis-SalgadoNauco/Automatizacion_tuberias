from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# ======================
# Funciones del pipeline
# ======================

def extraer_ventas():
    """Simular extracción de datos de ventas"""
    print("Extrayendo datos de ventas...")
    return {"registros": 1000}

def validar_datos(ventas):
    """Validar calidad de datos"""
    print(f"Validando {ventas['registros']} registros...")
    return {"validos": 950, "errores": 50}

def transformar_datos(datos):
    """Aplicar transformaciones de negocio"""
    print(f"Transformando {datos['validos']} registros válidos...")
    return {"transformados": datos['validos']}

def cargar_data_warehouse(transformados):
    """Cargar a data warehouse"""
    print(f"Cargando {transformados['transformados']} registros...")
    return {"cargados": transformados['transformados']}

def enviar_reporte(resultado):
    """Enviar reporte de ejecución"""
    print(f"Pipeline completado: {resultado['cargados']} registros procesados")

# ==========
# Definir DAG
# ==========

dag = DAG(
    dag_id='pipeline_ventas_complejo',
    description='Pipeline ETL de ventas con dependencias complejas',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args={
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    },
    tags=['ventas', 'etl', 'dia2']
)

# ====================
# Tareas del pipeline
# ====================

# Preparación
preparar_entorno = BashOperator(
    task_id='preparar_entorno',
    bash_command='mkdir -p /tmp/etl_ventas',
    dag=dag
)

# Extracción (paralelo)
extraer_api = PythonOperator(
    task_id='extraer_api_ventas',
    python_callable=extraer_ventas,
    dag=dag
)

extraer_db = PythonOperator(
    task_id='extraer_db_productos',
    python_callable=lambda: {"productos": 500},
    dag=dag
)

# Validación
validar_api = PythonOperator(
    task_id='validar_datos_api',
    python_callable=lambda: validar_datos({"registros": 1000}),
    dag=dag
)

validar_db = PythonOperator(
    task_id='validar_datos_db',
    python_callable=lambda: {"productos_validos": 480},
    dag=dag
)

# Transformación
transformar_ventas = PythonOperator(
    task_id='transformar_ventas',
    python_callable=lambda: transformar_datos({"validos": 950}),
    dag=dag
)

transformar_productos = PythonOperator(
    task_id='transformar_productos',
    python_callable=lambda: {"productos_transformados": 480},
    dag=dag
)

# Join
join_datos = PythonOperator(
    task_id='join_ventas_productos',
    python_callable=lambda: {"registros_completos": 920},
    dag=dag
)

# Carga
cargar_dw = PythonOperator(
    task_id='cargar_data_warehouse',
    python_callable=lambda: cargar_data_warehouse({"transformados": 920}),
    dag=dag
)

# Reporte
reporte_final = PythonOperator(
    task_id='enviar_reporte_ejecucion',
    python_callable=lambda: enviar_reporte({"cargados": 920}),
    dag=dag
)

# =====================
# Dependencias complejas
# =====================

preparar_entorno >> [extraer_api, extraer_db]

extraer_api >> validar_api >> transformar_ventas
extraer_db >> validar_db >> transformar_productos

[transformar_ventas, transformar_productos] >> join_datos

join_datos >> cargar_dw >> reporte_final
