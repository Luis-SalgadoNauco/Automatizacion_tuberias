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

## 🛠️Trabajo realizado

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

### ¿Qué diferencias hay entre CI/CD para aplicaciones web vs pipelines de datos?

En aplicaciones web, los flujos de CI/CD suelen centrarse en:

- Pruebas unitarias y de integración del código
- Construcción del artefacto de la aplicación
- Despliegue automático a entornos de prueba o producción
- Validación de endpoints, interfaces y rendimiento

En cambio, en pipelines de datos con Apache Airflow:

- No se ejecuta el pipeline completo durante el proceso de CI
- Se valida principalmente la estructura del DAG, su sintaxis y dependencias
- Se comprueba que las tareas estén correctamente definidas
- Se evita interactuar con sistemas externos reales (APIs, bases de datos)

El objetivo del CI/CD en pipelines de datos es detectar errores de orquestación antes de que el DAG llegue a producción, reduciendo fallos durante la ejecución programada.

---

### ¿Cómo asegurar que las pruebas de DAG sean rápidas y confiables?

Para asegurar pruebas rápidas y confiables en Apache Airflow se aplican las siguientes prácticas:

- Uso de DagBag para cargar y validar DAGs sin ejecutarlos
- Evitar dependencias externas durante las pruebas
- Validar únicamente estructura, dependencias y configuración
- Mantener los tests simples, deterministas y reproducibles
- Ejecutar las pruebas en entornos aislados dentro del pipeline de CI

Estas prácticas permiten detectar errores críticos en pocos segundos y garantizar la estabilidad del entorno productivo.

---

## Estructura del proyecto

airflow_curso/
├── dags/
│   ├── mi_primer_dag.py
│   ├── pipeline_ventas_complejo.py
│   ├── pipeline_con_sensores.py
│   ├── pipeline_monitorado.py
│   └── pipeline_avanzado_complejo.py
├── tests/
│   └── dags/
│       ├── test_dag_sintaxis.py
│       └── test_pipeline_ventas.py
├── scripts/
│   └── deploy.sh
├── .github/
│   └── workflows/
│       └── ci-cd-airflow.yml
├── evidencia/
├── airflow_env/
├── airflow.cfg
├── README.md
└── README_SEMANA_4.md
