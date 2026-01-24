# Herramientas ETL y Proyecto Final  
## Semana 4 – Carrera Profesional y Próximos Pasos

Repositorio de trabajo semanal enfocado en la **consolidación de competencias profesionales en ingeniería de datos**, integrando **testing, monitoreo, observabilidad y alertas** en pipelines de Apache Airflow, alineados con prácticas reales de la industria.

---

## Descripción general de la semana

Durante la Semana 4 se aborda la transición desde el desarrollo funcional de DAGs hacia una **operación profesional y productiva de pipelines de datos**.

El foco está en comprender y aplicar prácticas clave que se esperan en entornos laborales reales:

- Validación automática de DAGs
- Calidad y confiabilidad del código
- Instrumentación de métricas
- Observabilidad del pipeline
- Monitoreo continuo y alertas
- Documentación clara y trazable

Esta semana conecta el aprendizaje técnico con una **proyección profesional**, preparando el camino hacia roles como **Data Engineer**, **Analytics Engineer** o **Platform Engineer**.

---

## Objetivos de la semana

- Comprender el rol del testing y monitoreo en pipelines productivos
- Implementar pruebas automatizadas para DAGs de Airflow
- Detectar errores de importación y configuración tempranamente
- Instrumentar DAGs con métricas personalizadas
- Integrar Airflow con Prometheus y Grafana
- Visualizar métricas operacionales del pipeline
- Configurar alertas automáticas ante fallos y violaciones de SLA
- Desarrollar criterios profesionales para operación y mantenimiento de pipelines
- Documentar el trabajo de forma clara y evaluable

---

# Día 1 – Testing básico de DAGs en Apache Airflow

## Objetivo del día

- Comprender la importancia del testing en Airflow
- Implementar pruebas básicas para validar DAGs
- Utilizar `DagBag` para detectar errores de importación
- Ejecutar pruebas automatizadas con `pytest`
- Generar evidencia de ejecución correcta

---

## rabajo realizado

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

- Pruebas unitarias y de integración
- Construcción de artefactos
- Despliegues automáticos
- Validación de interfaces y endpoints

En pipelines de datos con Apache Airflow:

- No se ejecuta el pipeline completo en CI
- Se valida estructura, sintaxis y dependencias
- Se evita interacción con sistemas externos reales
- Se prioriza la detección temprana de errores de orquestación

---

### ¿Cómo asegurar que las pruebas de DAG sean rápidas y confiables?

- Uso de `DagBag` sin ejecutar tareas
- Evitar dependencias externas
- Validar solo estructura y configuración
- Tests simples, deterministas y reproducibles
- Ejecución en entornos aislados de CI

---

# Día 2 – Monitoreo, Observabilidad y Operación Profesional

## Objetivo del día

- Comprender la importancia del monitoreo en pipelines de datos
- Instrumentar DAGs con métricas personalizadas
- Integrar Airflow con Prometheus y Grafana
- Visualizar métricas clave del pipeline
- Configurar alertas automáticas
- Relacionar estas prácticas con escenarios profesionales reales

---

## rabajo realizado

Durante el Día 2 se realizaron las siguientes actividades:

- Instrumentación de DAGs usando métricas (`Stats`)
- Exposición de métricas mediante **StatsD Exporter**
- Recolección de métricas con **Prometheus**
- Visualización de métricas en **Grafana**
- Creación de dashboards para monitorear:
  - Ejecuciones exitosas del DAG
  - Duración de tareas
  - Throughput del pipeline
  - Calidad de transformación
- Configuración de reglas de alerta en Prometheus
- Validación completa del flujo Airflow → Prometheus → Grafana

---

## Métricas implementadas

### Métricas del DAG
- `airflow_pipeline_dag_success`
- `airflow_pipeline_dag_failure`
- `airflow_pipeline_dag_duration`

### Métricas de extracción
- `airflow_pipeline_extract_records`
- `airflow_pipeline_extract_duration`
- `airflow_pipeline_extract_errors`

### Métricas de transformación
- `airflow_pipeline_transform_quality`
- `airflow_pipeline_transform_output_records`
- `airflow_pipeline_transform_errors`

### Métricas de carga
- `airflow_pipeline_load_records_loaded`
- `airflow_pipeline_load_duration`
- `airflow_pipeline_load_throughput`
- `airflow_pipeline_load_errors`

### Métricas de SLA
- `airflow_pipeline_sla_violations`

---

## Dashboards configurados en Grafana

Se implementó un dashboard de monitoreo con los siguientes paneles:

- Contador de ejecuciones exitosas del DAG
- Tiempo promedio de procesamiento
- Métricas de rendimiento y calidad del pipeline
- Visualización de errores por componente

Estos dashboards permiten detectar problemas operativos y analizar el comportamiento del pipeline en tiempo real.

---

## Alertas configuradas en Prometheus

Se configuraron reglas de alerta para:

- Fallos en ejecuciones del DAG
- Violaciones de SLA

Las alertas fueron evaluadas correctamente y se encuentran en estado **OK** cuando no existen incidentes activos.

---

## Evidencia de ejecución – Día 2

Se generaron evidencias que demuestran:

- Métricas visibles en Prometheus
- Dashboards funcionando en Grafana
- Alertas evaluadas correctamente
- Ejecución exitosa del DAG instrumentado

Las evidencias se encuentran almacenadas en la carpeta `evidencia/`.

---

## Verificación – Día 2

### ¿Qué métricas son más importantes para monitorear en una tubería de datos vs una aplicación web?

Aunque tanto las aplicaciones web como las tuberías de datos utilizan principios similares de observabilidad, las métricas prioritarias difieren debido a la naturaleza de cada sistema.

**En una tubería de datos (Data Pipeline):**
- **Éxito / fallo de ejecuciones** del DAG (success / failure)
- **Duración total del pipeline** y de cada etapa (extract, transform, load)
- **Cumplimiento de SLA** y retrasos en la ejecución
- **Calidad de los datos** (registros procesados, pérdidas, scores de calidad)
- **Throughput** (registros procesados por unidad de tiempo)
- **Frescura de los datos** (data freshness)

Estas métricas permiten detectar:
- Bloqueos operativos
- Degradación del rendimiento
- Problemas de calidad silenciosos
- Impacto directo en consumidores downstream

**En una aplicación web:**
- Latencia de requests (p50, p95, p99)
- Tasa de errores HTTP (4xx / 5xx)
- Disponibilidad del servicio (uptime)
- Uso de recursos (CPU, memoria)
- Tráfico y concurrencia

Aquí el foco está en la **experiencia del usuario en tiempo real**, mientras que en pipelines de datos el foco es la **confiabilidad, completitud y puntualidad**.

---

### ¿Cómo decidir cuándo escalar de advertencia a crítica en las alertas?

La severidad de una alerta debe definirse según el **impacto en el negocio** y no solo por la existencia de un error técnico.

**Advertencia (Warning):**
- Fallos intermitentes
- Retrasos leves en la ejecución
- Degradación gradual del rendimiento
- Métricas fuera de lo normal pero recuperables automáticamente

Ejemplos:
- Un DAG falla una vez pero se recupera en el retry
- Aumento leve en la duración del pipeline
- Métricas de calidad cercanas al umbral mínimo

**Crítica (Critical):**
- Fallos persistentes
- Incumplimiento de SLA
- Bloqueo completo del pipeline
- Datos desactualizados que impactan decisiones del negocio

Ejemplos:
- Varias ejecuciones fallidas consecutivas
- SLA violado por más de un período definido
- Pipeline detenido sin generación de datos
- Datos con más de 24 horas de atraso

Una buena práctica es:
- Comenzar con alertas **warning**
- Escalar a **critical** solo si la condición persiste en el tiempo
- Evitar alertas ruidosas que no requieren acción inmediata

Este enfoque reduce la fatiga de alertas y garantiza que las alertas críticas representen incidentes reales que requieren intervención humana.
---

## Estructura del proyecto
airflow_curso/
├── dags/
├── tests/
├── scripts/
├── evidencia/
├── airflow_env/
├── airflow.cfg
├── README.md
└── README_SEMANA_4.md
