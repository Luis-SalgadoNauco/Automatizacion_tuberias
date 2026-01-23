import os
from airflow.models import DagBag


def test_estructura_pipeline_ventas():
    dags_path = os.path.join(os.getcwd(), "dags")

    dagbag = DagBag(
        dag_folder=dags_path,
        include_examples=False
    )

    dag = dagbag.dags.get("pipeline_ventas_complejo")
    assert dag is not None, "El DAG pipeline_ventas_complejo no existe"

    task_ids = {task.task_id for task in dag.tasks}

    # 🔎 Tareas críticas que NO pueden faltar
    tareas_esperadas = {
        "preparar_entorno",
        "extraer_api_ventas",
        "extraer_db_productos",
        "validar_datos_api",
        "validar_datos_db",
        "transformar_ventas",
        "transformar_productos",
        "join_ventas_productos",
        "cargar_data_warehouse",
        "enviar_reporte_ejecucion",
    }

    faltantes = tareas_esperadas - task_ids
    assert not faltantes, f"Tareas faltantes en el DAG: {faltantes}"
