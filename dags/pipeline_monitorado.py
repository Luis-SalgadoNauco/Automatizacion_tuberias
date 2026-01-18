from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta
import logging
import time
import random

# -------------------------------------------------
# Configuración de logging
# -------------------------------------------------
logger = logging.getLogger("pipeline_monitorado")
logger.setLevel(logging.INFO)

# -------------------------------------------------
# Funciones del pipeline
# -------------------------------------------------
def procesar_datos_con_metricas(**context):
    """Procesa datos y registra métricas"""
    task_instance = context["task_instance"]

    logger.info(f"Iniciando procesamiento - Tarea: {task_instance.task_id}")

    # Simular procesamiento
    processing_time = random.uniform(10, 30)
    time.sleep(processing_time)

    records_processed = random.randint(1000, 5000)
    success_rate = random.uniform(0.95, 1.0)

    metricas = {
        "registros_procesados": records_processed,
        "tiempo_procesamiento": processing_time,
        "tasa_exito": success_rate,
        "timestamp": datetime.now().isoformat(),
    }

    task_instance.xcom_push(key="metricas", value=metricas)

    logger.info(f"Métricas generadas: {metricas}")
    return metricas


def validar_metricas(**context):
    """Valida métricas obtenidas del procesamiento"""
    task_instance = context["task_instance"]
    metricas = task_instance.xcom_pull(
        task_ids="procesar_datos", key="metricas"
    )

    if not metricas:
        raise ValueError("No se encontraron métricas")

    if metricas["tasa_exito"] < 0.9:
        raise ValueError(
            f"Tasa de éxito baja: {metricas['tasa_exito']:.2%}"
        )

    if metricas["tiempo_procesamiento"] > 300:
        logger.warning(
            f"Tiempo de procesamiento alto: {metricas['tiempo_procesamiento']:.1f}s"
        )

    logger.info("Validación de métricas exitosa")
    return True


def verificar_sla(**context):
    """Verifica cumplimiento del SLA"""
    dag_run = context["dag_run"]
    duration = (datetime.now() - dag_run.start_date).total_seconds()

    sla_seconds = 7200  # 2 horas

    if duration > sla_seconds:
        logger.warning(
            f"SLA violado: {duration:.1f}s > {sla_seconds}s"
        )

    return duration


def on_failure_alert(context):
    """Callback ante fallos"""
    task_instance = context["task_instance"]
    dag_id = context["dag"].dag_id
    error = str(context.get("exception", "Unknown error"))

    alert_message = f"""
🚨 ALERTA DE FALLO 🚨
DAG: {dag_id}
Tarea: {task_instance.task_id}
Error: {error}
"""

    logger.error(alert_message)


def on_success_summary(context):
    """Resumen de ejecución exitosa"""
    dag_id = context["dag"].dag_id
    start_date = context["dag_run"].start_date
    end_date = context["dag_run"].end_date

    if start_date and end_date:
        duration = (end_date - start_date).total_seconds()
        logger.info(
            f"DAG {dag_id} completado en {duration:.1f} segundos"
        )


# -------------------------------------------------
# Definición del DAG
# -------------------------------------------------
default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "on_failure_callback": on_failure_alert,
    "execution_timeout": timedelta(hours=1),
}

dag = DAG(
    dag_id="pipeline_monitorado",
    description="Pipeline ETL con monitoreo completo",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    max_active_runs=1,
    dagrun_timeout=timedelta(hours=2),
    default_args=default_args,
    on_success_callback=on_success_summary,
    sla_miss_callback=lambda context: logger.warning(
        f"SLA missing for {context['dag'].dag_id}"
    ),
)

# -------------------------------------------------
# Tareas
# -------------------------------------------------
procesar = PythonOperator(
    task_id="procesar_datos",
    python_callable=procesar_datos_con_metricas,
    provide_context=True,
    dag=dag,
)

validar = PythonOperator(
    task_id="validar_metricas",
    python_callable=validar_metricas,
    provide_context=True,
    dag=dag,
)

notificar_exito = EmailOperator(
    task_id="notificar_exito",
    to=["data-team@empresa.com"],
    subject="Pipeline ETL Completado - {{ ds }}",
    html_content="""
    <h2>Pipeline ETL Completado Exitosamente</h2>
    <p>Ejecución: {{ ds }}</p>
    <p>Duración: {{ dag_run.duration }}</p>
    <p>Próxima ejecución: {{ next_ds }}</p>
    """,
    dag=dag,
)

verificar_sla_task = PythonOperator(
    task_id="verificar_sla",
    python_callable=verificar_sla,
    provide_context=True,
    dag=dag,
)

# -------------------------------------------------
# Dependencias
# -------------------------------------------------
procesar >> validar >> notificar_exito >> verificar_sla_task
