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

## 📘 Día 3 – Operadores, Sensores y Operadores Personalizados

### Objetivo del día

- Conocer los operadores más comunes de Apache Airflow
- Comprender el uso de sensores para esperar condiciones externas
- Crear y utilizar un operador personalizado
- Construir un DAG que combine sensores, operadores estándar y personalizados
- Verificar la ejecución correcta desde la UI y la consola
- Generar evidencia gráfica de la ejecución

---

### Trabajo realizado

Durante el Día 3 se realizaron las siguientes actividades:

- Revisión de operadores comunes:
  - `BashOperator`
  - `PythonOperator`
- Introducción y uso de sensores:
  - `FileSensor` para esperar la llegada de archivos
- Creación de un operador personalizado para validación de datos
- Construcción del DAG **`pipeline_con_sensores`**
- Ejecución manual del DAG desde la consola
- Monitoreo del flujo de tareas desde la Web UI
- Análisis de estados y resolución de errores durante la ejecución
- Generación de evidencia visual del DAG ejecutado correctamente

---

### DAG creado

**Nombre:** `pipeline_con_sensores`

**Descripción:**  
Pipeline que espera la llegada de un archivo de ventas, valida su calidad, procesa la información, genera un reporte y finalmente limpia los archivos temporales.

---

### Tareas incluidas

1. **`esperar_archivo_datos`** (`FileSensor`)  
   Espera la existencia del archivo `/tmp/datos_ventas.csv` antes de continuar el flujo.

2. **`validar_datos_ventas`** (Operador personalizado)  
   Lee el archivo CSV y valida la calidad de los datos según un umbral definido.

3. **`procesar_datos_ventas`** (`PythonOperator`)  
   Simula el procesamiento de los datos de ventas.

4. **`generar_reporte`** (`PythonOperator`)  
   Simula la generación de un reporte ejecutivo.

5. **`limpiar_archivos`** (`BashOperator`)  
   Elimina el archivo temporal utilizado en el proceso.

El flujo del DAG es **secuencial**:

## 📘 Día 3 – Operadores, Sensores y Operadores Personalizados

### Objetivo del día

- Conocer los operadores más comunes de Apache Airflow
- Comprender el uso de sensores para esperar condiciones externas
- Crear y utilizar un operador personalizado
- Construir un DAG que combine sensores, operadores estándar y personalizados
- Verificar la ejecución correcta desde la UI y la consola
- Generar evidencia gráfica de la ejecución

---

### Trabajo realizado

Durante el Día 3 se realizaron las siguientes actividades:

- Revisión de operadores comunes:
  - `BashOperator`
  - `PythonOperator`
- Introducción y uso de sensores:
  - `FileSensor` para esperar la llegada de archivos
- Creación de un operador personalizado para validación de datos
- Construcción del DAG **`pipeline_con_sensores`**
- Ejecución manual del DAG desde la consola
- Monitoreo del flujo de tareas desde la Web UI
- Análisis de estados y resolución de errores durante la ejecución
- Generación de evidencia visual del DAG ejecutado correctamente

---

### DAG creado

**Nombre:** `pipeline_con_sensores`

**Descripción:**  
Pipeline que espera la llegada de un archivo de ventas, valida su calidad, procesa la información, genera un reporte y finalmente limpia los archivos temporales.

---

### Tareas incluidas

1. **`esperar_archivo_datos`** (`FileSensor`)  
   Espera la existencia del archivo `/tmp/datos_ventas.csv` antes de continuar el flujo.

2. **`validar_datos_ventas`** (Operador personalizado)  
   Lee el archivo CSV y valida la calidad de los datos según un umbral definido.

3. **`procesar_datos_ventas`** (`PythonOperator`)  
   Simula el procesamiento de los datos de ventas.

4. **`generar_reporte`** (`PythonOperator`)  
   Simula la generación de un reporte ejecutivo.

5. **`limpiar_archivos`** (`BashOperator`)  
   Elimina el archivo temporal utilizado en el proceso.

El flujo del DAG es **secuencial**:

esperar_archivo_datos → validar_datos_ventas → procesar_datos_ventas → generar_reporte → limpiar_archivos

### Evidencia de ejecución

Las evidencias del Día 3 se encuentran en la carpeta `evidencia/` e incluyen:

- `detalle_ejecucion_dia3.png` – Detalle de ejecución de tareas
- `grafico_dia3.png` – Vista gráfica del DAG ejecutado correctamente

---

### Aprendizajes clave

- Los sensores permiten sincronizar los DAGs con eventos externos.
- Un DAG no debe ejecutar tareas si no se cumplen las condiciones previas.
- Los operadores personalizados mejoran la reutilización y limpieza del código.
- Airflow gestiona estados de tareas de forma independiente al resultado del scheduler.
- La Web UI es clave para depurar y entender la ejecución de pipelines.

---

### Verificación – Día 3

**¿En qué situaciones usarías un sensor en lugar de ejecutar tareas inmediatamente?**  
Se utiliza un sensor cuando una tarea depende de un evento externo, como la llegada de un archivo, la disponibilidad de un servicio o la finalización de otro proceso. Esto evita fallos prematuros y permite que el flujo se ejecute solo cuando las condiciones son correctas.

**¿Cuáles son las ventajas de crear operadores personalizados?**  
Permiten encapsular lógica reutilizable, mantener los DAGs más ordenados, estandarizar procesos, facilitar el mantenimiento y escalar soluciones de orquestación de forma más profesional.
---

## Día 4 – Monitoreo, métricas y alertas en Airflow

### Objetivo
Implementar un DAG con monitoreo completo, métricas, validaciones, alertas y control de SLA utilizando Apache Airflow.

---

### Actividades realizadas

- Creación del DAG `pipeline_monitorado`
- Configuración de parámetros de monitoreo:
  - Reintentos automáticos
  - Timeout de ejecución
  - Callbacks de éxito y fallo
- Implementación de métricas:
  - Tiempo de procesamiento
  - Registros procesados
  - Tasa de éxito
- Uso de XCom para compartir métricas entre tareas
- Validación de umbrales de calidad
- Notificación de éxito mediante `EmailOperator`
- Verificación de SLA al final del pipeline

---

### Ejecución y monitoreo

- Las tareas `procesar_datos` y `validar_metricas` se ejecutaron correctamente.
- La tarea `notificar_exito` intentó enviar un correo electrónico.
- Debido a que el entorno local no tiene SMTP configurado, el envío de correo no se completó automáticamente.
- La tarea fue marcada manualmente como exitosa para continuar el flujo.
- El DAG finalizó exitosamente y permitió validar el monitoreo completo.

---

### Evidencias generadas

- `detalle_ejecucion_dia4.png`  
  Vista detallada de la ejecución del DAG.

- `grafico_intento_aviso_dia4.png`  
  Evidencia del intento de notificación por correo electrónico.

- `grafico_completado_dia4.png`  
  Ejecución final del DAG completado correctamente.

---

### Pregunta de verificación

**¿Qué métricas son más importantes para monitorear en una tubería de datos y cómo elegir el tipo de alerta?**

Las métricas más importantes son el estado de las tareas, tiempo de ejecución, volumen de datos procesados, tasa de éxito y cumplimiento de SLA.  
Las alertas por correo se usan para notificaciones formales, Slack para alertas operativas en tiempo real y SMS para incidentes críticos.

---

## Días restantes (planificación)

- Día 5

---

## Estructura del proyecto

```text
airflow_curso/
├── dags/
│   ├── mi_primer_dag.py
│   ├── pipeline_ventas_complejo.py
│   ├── pipeline_con_sensores.py
│   └── pipeline_monitorado.py
├── evidencia/
│   ├── ejecucion_saludo_diario.txt
│   ├── detalle_ejecucion_dia1.png
│   ├── grafico_dia1.png
│   ├── ejecucion_pipeline_ventas_complejo.txt
│   ├── detalle_ejecucion_dia2.png
│   ├── grafico_dia2.png
│   ├── detalle_ejecucion_dia3.png
│   ├── grafico_dia3.png
│   ├── detalle_ejecucion_dia4.png
│   ├── grafico_intento_aviso_dia4.png
│   └── grafico_completado_dia4.png
├── .gitignore
└── README.md
```
