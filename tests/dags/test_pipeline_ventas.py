from airflow.models import DagBag

def test_estructura_pipeline_ventas():
    dagbag = DagBag(include_examples=False)
    dag = dagbag.get_dag("pipeline_ventas_complejo")

    assert dag is not None, "DAG pipeline_ventas_complejo no encontrado"

    task_ids = [t.task_id for t in dag.tasks]

    # Verificar tareas de extracción
    assert "extraer_api_ventas" in task_ids
    assert "extraer_db_productos" in task_ids

    # Verificar validaciones
    assert "validar_datos_api" in task_ids
    assert "validar_datos_db" in task_ids

    # Verificar transformación
    assert "transformar_ventas" in task_ids
