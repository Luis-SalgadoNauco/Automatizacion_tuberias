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

### Día 1 – Testing básico de DAGs en Apache Airflow

#### Objetivo del día

- Comprender la importancia del testing en Airflow
- Implementar pruebas básicas para validar DAGs
- Utilizar `DagBag` para detectar errores de importación
- Ejecutar pruebas automatizadas con `pytest`
- Generar evidencia de ejecución correcta

---

#### Trabajo realizado

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

#### Evidencia de ejecución – Día 1

La ejecución de las pruebas arrojó los siguientes resultados:

- Todos los DAGs se cargaron sin errores de importación
- No se detectaron fallos de sintaxis ni configuración
- Las pruebas finalizaron en estado **PASSED**

Las evidencias correspondientes se encuentran almacenadas en la carpeta `evidencia/`.

---

#### Verificación – Día 1

##### ¿Qué diferencias hay entre CI/CD para aplicaciones web vs pipelines de datos?

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

##### ¿Cómo asegurar que las pruebas de DAG sean rápidas y confiables?

- Uso de `DagBag` sin ejecutar tareas
- Evitar dependencias externas
- Validar solo estructura y configuración
- Tests simples, deterministas y reproducibles
- Ejecución en entornos aislados de CI

---

### Día 2 – Monitoreo, Observabilidad y Operación Profesional

#### Objetivo del día

- Comprender la importancia del monitoreo en pipelines de datos
- Instrumentar DAGs con métricas personalizadas
- Integrar Airflow con Prometheus y Grafana
- Visualizar métricas clave del pipeline
- Configurar alertas automáticas
- Relacionar estas prácticas con escenarios profesionales reales

---

#### Trabajo realizado

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

#### Métricas implementadas

##### Métricas del DAG
- `airflow_pipeline_dag_success`
- `airflow_pipeline_dag_failure`
- `airflow_pipeline_dag_duration`

##### Métricas de extracción
- `airflow_pipeline_extract_records`
- `airflow_pipeline_extract_duration`
- `airflow_pipeline_extract_errors`

##### Métricas de transformación
- `airflow_pipeline_transform_quality`
- `airflow_pipeline_transform_output_records`
- `airflow_pipeline_transform_errors`

##### Métricas de carga
- `airflow_pipeline_load_records_loaded`
- `airflow_pipeline_load_duration`
- `airflow_pipeline_load_throughput`
- `airflow_pipeline_load_errors`

##### Métricas de SLA
- `airflow_pipeline_sla_violations`

---

#### Dashboards configurados en Grafana

Se implementó un dashboard de monitoreo con los siguientes paneles:

- Contador de ejecuciones exitosas del DAG
- Tiempo promedio de procesamiento
- Métricas de rendimiento y calidad del pipeline
- Visualización de errores por componente

Estos dashboards permiten detectar problemas operativos y analizar el comportamiento del pipeline en tiempo real.

---

#### Alertas configuradas en Prometheus

Se configuraron reglas de alerta para:

- Fallos en ejecuciones del DAG
- Violaciones de SLA

Las alertas fueron evaluadas correctamente y se encuentran en estado **OK** cuando no existen incidentes activos.

---

#### Evidencia de ejecución – Día 2

Se generaron evidencias que demuestran:

- Métricas visibles en Prometheus
- Dashboards funcionando en Grafana
- Alertas evaluadas correctamente
- Ejecución exitosa del DAG instrumentado

Las evidencias se encuentran almacenadas en la carpeta `evidencia/`.

---

#### Verificación – Día 2

##### ¿Qué métricas son más importantes para monitorear en una tubería de datos vs una aplicación web?

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

##### ¿Cómo decidir cuándo escalar de advertencia a crítica en las alertas?

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

### Día 3 – Gestión de Incidentes y Respuesta Operacional en Tuberías de Datos

#### Objetivo del día
Identificar, responder y documentar incidentes comunes en tuberías de datos mediante prácticas reales de operación on-call, utilizando runbooks automatizados, recuperación controlada y post-mortems estructurados.

---

#### Tarea 1: Tipos de Incidentes Comunes

Durante la operación de una tubería de datos, los incidentes más frecuentes se agrupan en las siguientes categorías:

##### 1. Fallos de conectividad
- APIs caídas o no disponibles
- Bases de datos inaccesibles
- Timeouts de red
- Límites de rate limit alcanzados
- Problemas de autenticación o credenciales vencidas

##### 2. Problemas de datos
- Datos corruptos o con formato inválido
- Cambios inesperados en esquemas
- Volúmenes de datos que exceden la capacidad del sistema

##### 3. Problemas de recursos
- Uso excesivo de memoria o CPU
- Disco lleno o límites de almacenamiento alcanzados
- Contención de recursos entre múltiples pipelines

##### 4. Errores lógicos
- Errores en el código de transformación
- Dependencias circulares en DAGs
- Configuraciones incorrectas

---

#### Tarea 2: Estrategias de Recuperación – Runbook de Incidentes

Se implementó un **runbook automatizado** para manejar incidentes de forma estructurada.

##### Paso 1: Detección automática
Las alertas disparan el runbook cuando se cumplen condiciones como:
- Pipeline caído
- Violaciones de SLA
- Alta tasa de errores
- Datos desactualizados

##### Paso 2: Diagnóstico rápido
El diagnóstico se realiza según el tipo de incidente:
- Verificación del scheduler de Airflow
- Revisión de conectividad a la base de datos
- Análisis de uso de CPU y memoria

##### Paso 3: Recuperación automática
Dependiendo del diagnóstico, se ejecutan acciones como:
- Reinicio de servicios
- Escalado de recursos
- Rollback a checkpoints de datos
- Renovación de credenciales

Si la recuperación automática falla, el incidente se escala según su severidad.

---

#### Simulación de Incidente

Se simuló un incidente de tipo **`pipeline_down`**, ejecutando automáticamente:

- Verificación del scheduler de Airflow
- Chequeo de conectividad a base de datos
- Reinicio de servicios afectados
- Validación de recuperación del pipeline

Resultado:
- Incidente resuelto automáticamente
- Severidad: **CRITICAL**
- Todos los pasos del runbook ejecutados con éxito

---

#### Tarea 3: Post-Mortem y Mejora Continua

Se generó un **post-mortem automático** en formato Markdown como evidencia del incidente.

#### Contenido del post-mortem
- Executive Summary
- Timeline del incidente
- Impacto en usuarios y negocio
- Análisis de causa raíz
- Pasos de resolución
- Lecciones aprendidas
- Acciones correctivas
- Medidas de prevención

#### Evidencia
- Archivo generado: `post_mortem_pipeline_down.md`
- Incluido en el repositorio como documentación formal del incidente

---

#### Preguntas de verificación (Cierre del día)

**1. ¿Cuál es la diferencia entre un incidente de datos y uno de infraestructura?**
Un incidente de datos afecta la calidad, integridad o frescura de la información, mientras que uno de infraestructura impacta la disponibilidad o rendimiento de los sistemas.

**2. ¿Por qué es clave contar con runbooks automatizados?**
Porque reducen el MTTR, evitan errores humanos, estandarizan la respuesta y previenen escaladas innecesarias.

**3. ¿Qué valor aporta un post-mortem en una organización de datos?**
Permite aprender del incidente, identificar causas raíz, definir acciones correctivas y mejorar la resiliencia del sistema a futuro.

---

### Día 4 – Escalado, Versionado y Deploy sin Tiempo de Inactividad

#### Objetivo del día
Comprender e implementar estrategias de escalado y versionado en tuberías de datos, junto con técnicas de despliegue sin tiempo de inactividad, asegurando continuidad operativa, compatibilidad de datos y alta disponibilidad en entornos productivos.

---

#### Contenidos abordados

##### 1. Estrategias de Escalado

**Escalado vertical**
- Incremento de CPU, memoria o disco en una misma máquina.
- Implementación simple.
- Limitado por el hardware.
- Puede requerir tiempo de inactividad.

**Escalado horizontal**
- Uso de múltiples instancias en paralelo.
- Mayor complejidad de coordinación.
- Teóricamente ilimitado.
- Permite actualizaciones sin downtime.

**Aplicación en Airflow**
- Uso de ejecutores distribuidos (CeleryExecutor).
- Workers independientes para ejecución paralela de tareas.
- Redis como broker de mensajes.

Archivo asociado:
- `semana_4/dia_4/escalado/docker-compose.scale.yml`

---

##### 2. Versionado de Datos y Esquemas

Se implementó un gestor de versionado de datos que permite:

- Validar datos contra múltiples versiones de esquema.
- Mantener compatibilidad hacia atrás.
- Realizar upgrades progresivos entre versiones.
- Detectar errores de esquema antes de procesar datos.

Versiones de esquema:
- **v1**: id, name, created_at
- **v2**: agrega email y updated_at
- **v3**: agrega phone

Archivo asociado:
- `semana_4/dia_4/versionado/data_version_manager.py`

Evidencia de ejecución:
- Validación correcta de datos legacy.
- Upgrade exitoso hasta versión 3.
- Validación posterior sin errores.

---

##### 3. Deploy sin Tiempo de Inactividad (Zero Downtime)

Se implementó una estrategia de despliegue tipo **blue-green**, que permite actualizar servicios sin interrumpir la operación.

Flujo del deploy:
1. Verificación de compatibilidad de datos.
2. Preparación de nueva versión (green).
3. Health checks.
4. Ejecución de smoke tests.
5. Cambio de tráfico a nueva versión.
6. Eliminación de versión anterior (blue).

Archivo asociado:
- `semana_4/dia_4/deploy/deploy-zero-downtime.sh`

Evidencia generada:
- `evidencia_semana4/deploy_zero_downtime_dia4.txt`

---

#### Evidencias del Día 4

- `evidencia_semana4/deploy_zero_downtime_dia4.txt`
- Ejecución exitosa del gestor de versionado de datos.
- Validación y upgrade de esquemas sin errores.

---

#### Preguntas de verificación

**¿En qué situaciones preferirías escalar horizontalmente vs verticalmente?**

El escalado horizontal es preferible cuando:
- Se requiere alta disponibilidad y tolerancia a fallos.
- El volumen de datos y la concurrencia crecen de forma impredecible.
- Se necesita procesar múltiples tareas en paralelo (por ejemplo, múltiples DAGs o tareas simultáneas en Airflow).
- Se busca evitar tiempos de inactividad durante ampliaciones de capacidad.

El escalado vertical es más adecuado cuando:
- La carga es predecible y estable.
- Se prioriza una implementación simple y rápida.
- No se requiere alta tolerancia a fallos.
- El sistema aún no ha alcanzado los límites físicos del hardware.

---

**¿Cómo asegurar compatibilidad hacia atrás cuando cambias esquemas de datos?**

La compatibilidad hacia atrás se asegura mediante:
- Versionado explícito de esquemas de datos.
- Adición de nuevos campos como opcionales, evitando eliminar o renombrar campos existentes.
- Uso de valores por defecto o `null` para campos nuevos al procesar datos antiguos.
- Implementación de funciones de migración progresiva que permitan actualizar datos de versiones anteriores.
- Validaciones automáticas del esquema antes de procesar o desplegar cambios.

Estas prácticas permiten que sistemas antiguos sigan funcionando mientras se introducen nuevas versiones del esquema sin interrumpir las operaciones.

---

### Día 5 – Documentación Técnica y Comunicación Ejecutiva

#### Objetivo del día
Aprender a tratar la documentación y la comunicación como un **producto profesional**, orientado a distintos públicos (técnico, negocio y ejecutivo), y no solo como un complemento del código.

---

#### Contenidos abordados

##### 1. Documentación técnica como producto
La documentación deja de ser un requisito secundario y pasa a ser la **puerta de entrada** del proyecto.

Se trabajó el concepto de README como:
- Punto inicial para nuevos usuarios o stakeholders
- Guía rápida de uso y contexto
- Referencia técnica viva del sistema

Estructura recomendada de un README profesional:
- Propósito del negocio
- Arquitectura de alto nivel
- Quick Start
- Guía de desarrollo
- Troubleshooting común

---

##### 2. Código autodocumentado (Docstrings)
Se revisó el uso de docstrings con estilo profesional (Google / NumPy Style) para:
- Explicar **qué hace** el código, no solo **cómo**
- Facilitar mantenimiento y escalabilidad
- Permitir generación automática de documentación

Aspectos clave:
- Descripción clara de la función
- Argumentos y tipos esperados
- Valor de retorno
- Posibles errores

---

##### 3. Storytelling para presentaciones ejecutivas
Se trabajó la diferencia entre:
- Explicar implementación técnica
- Comunicar **valor de negocio**

Framework utilizado: **SCQA**
- Situación
- Complicación
- Pregunta
- Respuesta

El foco estuvo en presentar soluciones en términos de:
- Ahorro de costos
- Reducción de tiempos
- Mitigación de riesgos
- Impacto estratégico

---

##### 4. Jerarquía visual en presentaciones
Buenas prácticas aplicadas:
- Cada slide comunica una idea principal
- Títulos con conclusiones, no genéricos
- Visuales simples y orientados a impacto
- Evitar sobrecarga de texto y gráficos

Se reforzó que una presentación **acompaña al mensaje**, no lo reemplaza.

---

##### 5. Comunicación según audiencia
Se analizó cómo traducir un mismo concepto técnico a distintos públicos:

- Técnicos: precisión y detalle
- Negocio: impacto operativo
- Ejecutivos: valor estratégico y riesgo

Ejemplos trabajados:
- Refactorización
- Rendimiento / latencia
- Deuda técnica

---

#### Ejercicio práctico del día

#### Documentación técnica del pipeline ETL
Se documentó el pipeline completo considerando:
- Arquitectura general
- Flujo de datos
- Decisiones arquitectónicas
- Escalabilidad, fiabilidad y mantenibilidad
- Métricas de éxito
- Manual operativo
- Recuperación ante desastres

---

#### Presentación ejecutiva automatizada
Se implementó un script en Python que:
- Toma un resumen ejecutivo estructurado
- Genera automáticamente una presentación `.pptx`
- Produce slides orientadas a negocio y dirección

El resultado es una **presentación ejecutiva reutilizable**, generada desde código.

---

#### Guía de adopción para usuarios de negocio
Se creó documentación orientada a usuarios no técnicos:
- Explicación del sistema en lenguaje simple
- Uso de dashboards
- Preguntas frecuentes
- Canales de soporte

---

#### Preguntas de verificación

**¿Cómo adaptarías una presentación técnica para diferentes audiencias?**
Adaptando el lenguaje, el nivel de detalle y el foco del mensaje:
- Técnicos: implementación y decisiones técnicas
- Negocio: impacto operativo y eficiencia
- Ejecutivos: valor estratégico, riesgos y retorno

**¿Qué elementos son más importantes en la documentación: código comentado, README o diagramas?**  
Todos son importantes, pero cumplen roles distintos:
- README: contexto y punto de entrada
- Código comentado: mantenibilidad
- Diagramas: entendimiento rápido del sistema
La documentación efectiva combina los tres.

---

## Estructura del proyecto

```text
airflow_curso/
├── README_SEMANA_4.md
├── runbook.py
├── post_mortem_pipeline_down.md
├── dags/
│   └── pipeline_monitoring_demo.py
├── test/
│   └── dags/
│       ├── test_dag_sintaxis.py
│       └── test_pipeline_ventas.py
├── semana_4/
│   └── dia_4/
│       ├── escalado/
│       │   └── docker-compose.scale.yml
│       ├── versionado/
│       │   └── data_version_manager.py
│       ├── deploy/
│       │   └── deploy-zero-downtime.sh
│       └── presentacion/
│           ├── generar_presentacion_ejecutiva.py
│           └── presentacion_ejecutiva_dia4.pptx
├── evidencia_semana4/
│   ├── alertas_canalizacion_dia2.png
│   ├── DashBoard_dia2.png
│   ├── Diagrama_ejecucion_dia2.png
│   └── deploy_zero_downtime_dia4.txt
└── .gitignore
