import os
from airflow.models import DagBag

def test_estructura_pipeline_ventas():
    dags_path = os.path.join(os.getcwd(), "dags")

    dagbag = DagBag(
        dag_folder=dags_path,
        include_examples=False
    )

    # ⚠️ NUNCA get_dag() en CI
    dag = dagbag.dags.get("pipeline_ventas_complejo")

    assert dag is not None, "El DAG pipeline_ventas_complejo no existe"

    task_ids = [task.task_id for task in dag.tasks]

    assert "extraer_datos" in task_ids
    assert "transformar_datos" in task_ids
    assert "cargar_datos" in task_ids
