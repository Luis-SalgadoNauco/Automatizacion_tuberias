# Automatización de Tuberías – Apache Airflow  
## Semana 4 – Testing y CI/CD en DAGs de Airflow

Repositorio de trabajo semanal enfocado en la **implementación de pruebas automatizadas (testing)** y **validaciones tempranas** para DAGs de Apache Airflow, sentando las bases para integración continua (CI).

---

## Descripción general de la semana

Durante la Semana 4 se profundiza en la **calidad, validación y automatización** de pipelines de datos construidos con Apache Airflow.  
El foco principal está en asegurar que los DAGs:

- Se carguen correctamente
- No presenten errores de importación
- Cumplan una estructura mínima esperada
- Puedan validarse automáticamente antes del despliegue

Se introduce el uso de **pytest** junto con **DagBag**, permitiendo integrar testing en flujos de **CI/CD**.

---

## Objetivos de la semana

- Implementar pruebas automatizadas para DAGs de Airflow
- Detectar errores de importación antes de ejecutar pipelines
- Validar la correcta carga de DAGs
- Integrar testing como paso obligatorio previo a despliegues
- Preparar el proyecto para pipelines de CI/CD
- Mantener documentación clara y trazable del proceso

---

# Día 1 – Testing básico de DAGs en Apache Airflow

## Objetivo del día

- Comprender la importancia del testing en Airflow
- Implementar pruebas básicas para validar DAGs
- Utilizar `DagBag` para detectar errores de importación
- Ejecutar pruebas automatizadas con `pytest`
- Generar evidencia de ejecución correcta

---

## 🛠️rabajo realizado

Durante el Día 1 se realizaron las siguientes actividades:

- Activación del entorno virtual de trabajo
- Instalación de dependencias necesarias para testing
- Creación de la estructura de carpetas de pruebas
- Implementación de pruebas básicas para:
  - Verificar que los DAGs se cargan sin errores
  - Confirmar que al menos un DAG está disponible
- Ejecución de pruebas automatizadas desde consola
- Validación de resultados exitosos

---

## Evidencia de ejecución – Día 1

La ejecución de las pruebas arrojó los siguientes resultados:

- Todos los DAGs se cargaron sin errores de importación
- No se detectaron fallos de sintaxis ni configuración
- Las pruebas finalizaron en estado **PASSED**

Las evidencias correspondientes se encuentran almacenadas en la carpeta `evidencia/`.

---

## Verificación – Día 1

### ¿Por qué es importante testear DAGs en Airflow?

Porque permite detectar errores de importación, dependencias incorrectas o configuraciones inválidas **antes de ejecutar los pipelines**, evitando fallos en producción y mejorando la confiabilidad del sistema.

---

### ¿Qué es DagBag y para qué se utiliza?

`DagBag` es el componente de Apache Airflow encargado de cargar y validar los DAGs disponibles.  
Se utiliza para identificar errores de importación, problemas de sintaxis y configuraciones inválidas sin necesidad de ejecutar los flujos.

---

### ¿Qué ventaja aporta pytest en Airflow?

`pytest` permite automatizar la validación de DAGs, integrar pruebas en pipelines de CI/CD y asegurar la calidad del código mediante ejecuciones repetibles y controladas.

---

## Estructura del proyecto (Día 1)

airflow_curso/
├── dags/
│ ├── mi_primer_dag.py
│ ├── pipeline_ventas_complejo.py
│ └── otros DAGs
├── tests/
│ └── dags/
│ └── test_carga_dags.py
├── evidencia/
│ └── evidencias_dia1.png
├── airflow_env/
├── airflow.cfg
└── README.md
