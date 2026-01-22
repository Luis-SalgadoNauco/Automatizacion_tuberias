from airflow.models import DagBag

def test_carga_dags_sin_errores():
    """
    Verifica que todos los DAGs se cargan sin errores de importación
    """
    dagbag = DagBag(include_examples=False)

    assert len(dagbag.import_errors) == 0, (
        f"Errores de importación encontrados: {dagbag.import_errors}"
    )

    assert len(dagbag.dags) > 0, "No se cargó ningún DAG"
