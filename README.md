# Automatización de Tuberías – Apache Airflow

Repositorio de trabajo semanal para el aprendizaje práctico de **Apache Airflow**, enfocado en la creación, ejecución y documentación de DAGs para la automatización de procesos de datos.

---

## Descripción general de la semana

Durante esta semana se trabajará con Apache Airflow desde un entorno Ubuntu, partiendo desde una instalación limpia hasta la construcción de workflows más completos.  
El enfoque será **práctico**, priorizando:

- Buenas prácticas de estructura de proyectos
- Versionamiento correcto con Git y GitHub
- Generación de evidencias de ejecución
- Comprensión conceptual de DAGs y orquestación

Este repositorio se utiliza como **carpeta base para toda la semana**, evitando problemas de rutas y facilitando la trazabilidad del trabajo realizado.

---

## Objetivos de la semana

- Comprender qué es Apache Airflow y para qué se utiliza
- Crear DAGs funcionales desde cero
- Ejecutar DAGs manualmente y mediante scheduler
- Analizar logs y resultados de ejecución
- Documentar correctamente cada avance
- Mantener un repositorio ordenado y versionado

---

## Día 1 – Primer DAG funcional en Apache Airflow

### Objetivo del día

- Instalar Apache Airflow en Ubuntu
- Configurar el entorno virtual y `AIRFLOW_HOME`
- Crear y ejecutar un DAG básico
- Verificar la correcta ejecución desde la UI y la consola
- Generar evidencia del trabajo realizado

---

### Trabajo realizado

Durante el Día 1 se realizaron las siguientes actividades:

- Creación de un entorno virtual en Python
- Instalación de Apache Airflow
- Inicialización y migración de la base de datos
- Configuración correcta del directorio `AIRFLOW_HOME`
- Creación del primer DAG llamado **`saludo_diario`**
- Ejecución manual del DAG desde:
  - Interfaz Web (Graph View)
  - Consola mediante `airflow dags trigger`
  - Consola mediante `airflow dags test`
- Generación de archivos de evidencia con la salida de ejecución

---

### DAG creado

**Nombre:** `saludo_diario`

**Tareas incluidas:**

1. `tarea_bash`  
   Imprime la fecha y hora de ejecución mediante un comando Bash.

2. `tarea_python`  
   Ejecuta una función Python que imprime un mensaje de saludo.

3. `tarea_esperar`  
   Simula un proceso de espera usando `sleep`.

Las tareas se ejecutan de forma **secuencial**, respetando la lógica definida en el DAG.

---

### Evidencia de ejecución – Día 1

Las evidencias del Día 1 se encuentran en la carpeta `evidencia/` e incluyen:

- `ejecucion_saludo_diario.txt`  
  Salida de la ejecución manual del DAG.

- `detalle_ejecucion_dia1.png`  
  Captura detallada de la ejecución de tareas.

- `grafico_dia1.png`  
  Visualización del DAG en **Graph View** desde la Web UI.

---

### Verificación – Día 1

**¿Qué es un DAG en Airflow?**  
Un DAG (Directed Acyclic Graph) es un grafo dirigido sin ciclos que define la estructura de un workflow, especificando tareas y sus dependencias.

**¿Para qué sirve definir dependencias entre tareas?**  
Permite controlar el orden de ejecución, asegurar que ciertas tareas solo se ejecuten cuando otras hayan finalizado correctamente y evitar ejecuciones inconsistentes.

**¿Cuál es la diferencia entre ejecutar un DAG con `trigger` y con `test`?**  
- `trigger` ejecuta el DAG completo usando el scheduler.
- `test` ejecuta el DAG de forma local y secuencial, útil para pruebas y depuración.

**¿Por qué es importante generar evidencia de ejecución?**  
Porque permite validar que el DAG funciona correctamente, facilita la auditoría del proceso y deja trazabilidad del trabajo realizado.

---

## Día 2 – DAG con dependencias complejas

### Objetivo del día

- Construir un DAG con múltiples ramas y dependencias
- Ejecutar tareas en paralelo
- Comprender el flujo visual de un DAG complejo
- Ejecutar y validar el pipeline desde la consola
- Generar evidencia de ejecución

---

### Trabajo realizado

Durante el Día 2 se realizaron las siguientes actividades:

- Creación del DAG **`pipeline_ventas_complejo`**
- Definición de tareas de:
  - Preparación de entorno
  - Extracción de datos
  - Validación
  - Transformación
  - Unión de datos (join)
  - Carga final
  - Reporte de ejecución
- Implementación de dependencias complejas con ejecución paralela
- Ejecución del DAG mediante:
  - `airflow dags test`
  - `airflow dags trigger`
- Verificación del flujo en la Web UI (Graph View)

---

### Flujo del DAG

preparar_entorno → [extraer_api, extraer_db]
extraer_api → validar_api → transformar_ventas ↘
extraer_db → validar_db → transformar_productos ↘ → join_datos → cargar_dw → enviar_reporte

---

### Evidencia de ejecución – Día 2

Las evidencias del Día 2 se encuentran en la carpeta `evidencia/`:

- `ejecucion_pipeline_ventas_complejo.txt`  
  Salida completa de la ejecución del pipeline.

- `detalle_ejecucion_dia2.png`  
  Captura del detalle de ejecución de las tareas.

- `grafico_dia2.png`  
  Visualización del DAG con dependencias complejas en **Graph View**.

---

### Verificación – Día 2

**¿Cuándo usar PythonOperator en lugar de BashOperator?**  
Se utiliza PythonOperator cuando la lógica de la tarea requiere procesamiento, validaciones o transformaciones en Python.  
BashOperator es ideal para comandos del sistema, scripts o tareas simples de infraestructura.

**¿Qué ventajas tiene definir dependencias explícitas?**  
- Permite paralelismo controlado
- Mejora la claridad del flujo
- Facilita mantenimiento y escalabilidad
- Reduce errores por ejecución fuera de orden
---

## Días restantes (planificación)

- Día 3
- Día 4
- Día 5

---

## Estructura del proyecto

```text
airflow_curso/
├── dags/
│   ├── mi_primer_dag.py
│   └── pipeline_ventas_complejo.py
├── evidencia/
│   ├── ejecucion_saludo_diario.txt
│   ├── detalle_ejecucion_dia1.png
│   ├── grafico_dia1.png
│   ├── ejecucion_pipeline_ventas_complejo.txt
│   ├── detalle_ejecucion_dia2.png
│   └── grafico_dia2.png
├── .gitignore
└── README.md
