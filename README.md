# Día 1 – Primer DAG en Apache Airflow

## Objetivo
Crear y ejecutar un DAG básico en Apache Airflow utilizando operadores Bash y Python.

## Estructura del proyecto
airflow_curso/
├── dags/
│ └── mi_primer_dag.py
├── evidencia/
│ └── ejecucion_saludo_diario.txt
│ └── detalle_ejecucion_dia1
│ └── ejecucion_saludo_diario.txt
├── README.md

markdown
Copiar código

## DAG creado
**Nombre:** `saludo_diario`

### Tareas
1. `tarea_bash`: imprime la fecha de ejecución
2. `tarea_python`: ejecuta una función Python de saludo
3. `tarea_esperar`: simula procesamiento con `sleep`

## Ejecución
El DAG fue ejecutado manualmente utilizando los siguientes comandos:

```bash
airflow dags trigger saludo_diario
airflow dags test saludo_diario 2024-01-01
