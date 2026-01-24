from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.stats import Stats   # 👈 CAMBIO 1
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

def extract_with_metrics(**context):
    records = 1000
    duration = 45.2  # segundos

    Stats.gauge('pipeline.extract.records', records)
    Stats.timing('pipeline.extract.duration', duration * 1000)  # 👈 CAMBIO 2

    logger.info(
        "Extract completed",
        extra={"records": records, "duration": duration}
    )

    return {'records': records}


def transform_with_metrics(**context):
    ti = context['task_instance']
    input_data = ti.xcom_pull(task_ids='extract')

    output_records = input_data['records'] * 0.95
    quality_score = 0.98

    Stats.gauge('pipeline.transform.quality', quality_score)
    Stats.gauge('pipeline.transform.output_records', output_records)

    return {'output_records': output_records}


def load_with_metrics(**context):
    ti = context['task_instance']
    transform_data = ti.xcom_pull(task_ids='transform')

    records_loaded = transform_data['output_records']
    load_time = 12.5

    Stats.gauge('pipeline.load.records_loaded', records_loaded)
    Stats.timing('pipeline.load.duration', load_time * 1000)

    throughput = records_loaded / load_time
    Stats.gauge('pipeline.load.throughput', throughput)


def dag_success_callback(context):
    dag_run = context['dag_run']
    duration = (dag_run.end_date - dag_run.start_date).total_seconds()

    Stats.timing('pipeline.dag.duration', duration * 1000)
    Stats.incr('pipeline.dag.success')


def dag_failure_callback(context):
    Stats.incr('pipeline.dag.failure')


dag = DAG(
    'pipeline_monitoring_demo',
    description='Pipeline con métricas y monitoreo completos',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args={
        'retries': 2,
        'retry_delay': timedelta(minutes=5),
        'execution_timeout': timedelta(hours=2),
        'sla': timedelta(hours=1),
    },
    on_success_callback=dag_success_callback,
    on_failure_callback=dag_failure_callback,
    tags=['monitoring', 'production']
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_with_metrics,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform_with_metrics,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load_with_metrics,
    dag=dag
)

extract_task >> transform_task >> load_task
