---
curso: BIGDATA
titulo: 07 - Semana 5/Sem5_Modin en el Ecosistema Big Data
slides: 22
fuente: 07 - Semana 5/Sem5_Modin en el Ecosistema Big Data.pdf
---

## Slide 1

Portada. Título: **Modin en el Ecosistema Big Data**. Autor: Mg. Aldo Lezama Benavides. Etiqueta: "Semana 5". Fondo cian con foto decorativa del edificio de UTEC y logo UTEC (chrome decorativo).

## Slide 2

**Objetivo de la sesión**

Lista de objetivos (dentro de un recuadro con esquinas tipo corchete):

- **Comprender** qué es Modin y su rol en el ecosistema Big Data
- **Analizar** cómo Modin permite manejar y procesar grandes volúmenes de datos en Python
- **Reconocer** las funciones de Pandas que Modin paraleliza para mejorar rendimiento.
- **Identificar** las ventajas de usar Modin sobre Pandas tradicional en proyectos de Big Data.

## Slide 3

**Contenido de la sesión**

Índice visual en 4 columnas numeradas (cada una enmarcada entre corchetes blancos):

- **01.** Modin en Big Data
- **02.** Funciones paralelizadas
- **03.** Pandas vs Dask vs Modin
- **04.** Modin en GColab

## Slide 4

Slide separador de sección. Número grande **01.** entre corchetes, con ícono de portapapeles/checklist y el título **Modin en Big Data**.

## Slide 5

**Modin en el ecosistema Big Data**

Texto (columna izquierda):

El análisis de datos en Python a menudo comienza con **Pandas**, una librería que ha simplificado enormemente la manipulación de datos tabulares. Su API intuitiva ha hecho de la limpieza, transformación y análisis de datos una tarea accesible. Sin embargo, Pandas tiene una limitación fundamental: es una librería **in-memory** y de **un solo hilo**. Esto significa que solo puede procesar datos que caben por completo en la memoria RAM de tu máquina, y solo puede utilizar un único núcleo de tu procesador para realizar sus cálculos. Cuando trabajas con un dataset de 10 GB en una máquina con 8 GB de RAM, Pandas simplemente fallará. Y si la operación es muy pesada, como un groupby complejo en un dataset de 100 GB, te verás atrapado en una espera interminable.

Visual (columna derecha): logo de **pandas** rodeado (a modo de nube de etiquetas) de nombres de métodos dispersos: `df.rename`, `df.describe`, `df.drop`, `df.groupby`, `pd.merge`, `df.pivot`, `pd.join`. Sugiere el abanico de operaciones que ofrece la API de Pandas.

## Slide 6

**¡El Cuello de Botella de Pandas: Cuando tus Datos Crecen**

Texto (columna izquierda):

**1. Limitación de Memoria (In-Memory)**
Pandas debe cargar todo el conjunto de datos en la memoria RAM de tu computadora para poder procesarlo. Si tu archivo es más grande que la memoria disponible, Pandas no puede funcionar y generará un error (*MemoryError*).

**2. Limitación de Procesamiento (Un Solo Hilo)**
Pandas utiliza un solo núcleo de tu CPU para ejecutar las operaciones. Aunque tu máquina tenga 8, 16 o más núcleos, solo uno se usa para el trabajo de Pandas. Esto hace que las operaciones complejas y los datasets grandes sean extremadamente lentos.

Visual (columna derecha): ilustración caricaturesca de un panda sudando y esforzándose por sostener/empujar un monitor azul con la etiqueta "RAM"; a un lado una torre con las etiquetas "PANDAS LIBRARY" y "MEMORY LIMIT" (con ícono de advertencia). Metáfora del panda que no da abasto con la memoria.

## Slide 7

**Pandas vs Modin**

Diagrama comparativo de dos bloques (contenedores tipo "Memory"):

- **Izquierda (Pandas):** un recuadro "Memory" contiene "pandas DataFrame". Debajo hay 4 cajas "CPU": solo **una** está resaltada en verde (activa) y las otras 3 en rojo (inactivas). Una flecha desde una caja roja etiquetada **"Idle cores"** (núcleos ociosos) apunta hacia arriba a los CPUs no usados. Solo 1 núcleo trabaja.
- **Derecha (Modin):** recuadro "Memory" con "Modin DataFrame". Las **4** cajas "CPU" están en verde (todas activas), con flechas bidireccionales, y una caja verde etiquetada **"Full Utilization!"** apunta a todos los núcleos. Todos los núcleos trabajan.

Texto inferior:

Podemos observar que Pandas Dataframe solo utiliza un núcleo de la CPU, mientras que la función Modin utiliza todos los núcleos. Modin es una biblioteca de código abierto, por lo que el código fuente y diversas pruebas de rendimiento que demuestran su eficiencia en comparación con Pandas están disponibles en GitHub. Según el repositorio de Modin en GitHub, **Modin cubre el 90,8 % de las API de Pandas Dataframe** y el 88,05 % de las API de Pandas Series. Por lo tanto, podemos ver que la cobertura de API de la función Modin es bastante alta, lo que la convierte en una herramienta muy fácil y fiable para escalar y paralelizar el flujo de trabajo de Pandas.

## Slide 8

**Modin en el ecosistema Big Data**

Visual (izquierda): diagrama de la arquitectura por capas de Modin, apilada de arriba a abajo con etiquetas laterales:
- **APIs:** fila con logos `pandas` (+ íconos de gráficos), `SQLite (Experimental)` y `MODIN API (Coming Soon™)`.
- **Query Compiler:** franja "MODIN Query Compiler".
- **Middle Layer:** bloque grande "MODIN DataFrame" y a la derecha un recuadro verde "??? Bring your Distributed DataFrame".
- **Execution:** fila con logos `RAY`, `DASK`, `python` y "??? Bring your backend".

Texto (derecha):

El funcionamiento de Modin es tres capas clave:

**Capa del Usuario (API de Pandas):** En la parte superior, los usuarios escriben su código de análisis de datos usando la sintaxis de Pandas, la cual ya les es familiar. La única diferencia es que importan Modin en lugar de Pandas (`import modin.pandas as pd`)

**Capa de Optimización (Modin Engine):** Esta capa intermedia toma los comandos del usuario y los divide en tareas más pequeñas y eficientes. Modin es el "cerebro" que decide cómo paralelizar las operaciones para que puedan ejecutarse en múltiples núcleos

**Capa del Motor (Backend):** En la base, el motor de cómputo distribuido (como Dask o Ray) ejecuta las tareas en paralelo. Esta capa es la que realmente realiza el trabajo pesado, distribuyendo el cómputo para procesar grandes volúmenes de datos de manera eficiente

## Slide 9

**Backends en Modin**

Texto superior: Modin puede ejecutar su motor de paralelización sobre diferentes backends¹, siendo los más comunes Ray, Dask y Unidist. Cada uno es un sistema distribuido con filosofías distintas:

Tres columnas con logo, comando de instalación y descripción:

| Backend | Instalación | Descripción |
|---------|-------------|-------------|
| **RAY** | `pip install "modin[ray]"` | Ray es un marco unificado para escalar aplicaciones de IA y Python. Ray consta de un entorno de ejecución distribuido y un conjunto de bibliotecas de IA para simplificar el procesamiento de aprendizaje automático. |
| **dask** | `pip install "modin[dask]"` | Dask es un framework de computación distribuida en Python. Nació en el mundo de ciencia de datos para escalar librerías como NumPy, Pandas y Scikit-learn. Orientado a colecciones (arrays, dataframes, bags) con una interfaz muy parecida a pandas/numpy. |
| **UNIDIST** | `pip install "modin[mpi]"` | Unidist es un marco que tiene como objetivo proporcionar una API unificada para la ejecución distribuida al admitir varios backends de ejecución de alto rendimiento. No es un motor en sí, sino una abstracción que permite a Modin (y otras librerías) trabajar de manera unificada sobre Ray, Dask o Multiprocessing. |

Nota al pie: ¹ un backend es el motor de ejecución que hace el "trabajo pesado" detrás de una librería o aplicación.
Enlace: https://www.youtube.com/watch?v=rXy2uSD2c-w

## Slide 10

**Código de ejemplo**

Dos bloques de código Python lado a lado. "Primero, con **Pandas**" vs "Ahora con **Modin**" (idéntico salvo el import):

```python
# Pandas
import pandas as pd
import time
t_inicio = time.time()
df_pandas = pd.read_csv("big_data.csv")
t_fin = time.time()
print(f"Tiempo de carga con Pandas: {t_fin - t_inicio:.2f} segundos")
```

```python
# Modin
import modin.pandas as pd
import time
t_inicio = time.time()
df_modin = pd.read_csv("big_data.csv")
t_fin = time.time()
print(f"Tiempo de carga con Modin: {t_fin - t_inicio:.2f} segundos")
```

Texto inferior: En un dataset grande (por ejemplo, de 10 GB), el tiempo de carga con Pandas podría ser de 150 segundos, mientras que con Modin podría reducirse a 30 segundos o menos.

## Slide 11

Slide separador de sección. Número grande **02.** entre corchetes, ícono de portapapeles y título **Funciones paralelizadas**.

## Slide 12

**Cargar datos: read_csv**

Dos bloques de código Python idénticos salvo el import, etiquetados "Pandas" y "Modin":

```python
# Pandas
import pandas as pd
df = pd.read_csv("ventas.csv")
ventas_cols = df.filter(like="ventas", axis=1)
print(ventas_cols.head())
```

```python
# Modin
import modin.pandas as pd
df = pd.read_csv("ventas.csv")
ventas_cols = df.filter(like="ventas", axis=1)
print(ventas_cols.head())
```

## Slide 13

**Fusionar: merge**

Dos bloques de código Python idénticos salvo el import ("Pandas" vs "Modin"):

```python
# Pandas
import pandas as pd
client = pd.read_csv("clientes.csv")
orden = pd.read_csv("ordenes.csv")
merged = pd.merge(client, orden, on="cliente_id", how="inner")
```

```python
# Modin
import modin.pandas as pd
client = pd.read_csv("clientes.csv")
orden = pd.read_csv("ordenes.csv")
merged = pd.merge(client, orden, on="cliente_id", how="inner")
```

## Slide 14

**Filtrar: filter**

Dos bloques de código Python idénticos salvo el import ("Pandas" vs "Modin"):

```python
# Pandas
import pandas as pd
df = pd.read_csv("ventas.csv")
ventas_cols = df.filter(like="ventas", axis=1)
print(ventas_cols.head())
```

```python
# Modin
import modin.pandas as pd
df = pd.read_csv("ventas.csv")
ventas_cols = df.filter(like="ventas", axis=1)
print(ventas_cols.head())
```

## Slide 15

**Aplicar función: apply**

Dos bloques de código Python idénticos salvo el import ("Pandas" vs "Modin"):

```python
# Pandas
import pandas as pd
df = pd.read_csv("ventas.csv")
df["con_igv"] = df["monto"].apply(lambda x: round(x * 2, 2))
print(df[["monto", "con_igv"]].head())
```

```python
# Modin
import modin.pandas as pd
df = pd.read_csv("ventas.csv")
df["con_igv"] = df["monto"].apply(lambda x: round(x * 2, 2))
print(df[["monto", "con_igv"]].head())
```

## Slide 16

**Compatibilidad**

Tabla de tres columnas clasificando funciones de Pandas según su soporte en Modin:

| Altamente compatibles (soporte completo o casi completo) | Parcialmente compatibles (soporte completo o casi completo) | No compatibles |
|---|---|---|
| `read_csv()`, `read_excel()`, `read_parquet()`, `groupby()`, `merge()`, `join()`, `concat()`, `apply()`, `map()`, `filter()`, `loc[]`, `iloc[]`, `describe()`, `value_counts()`, `dropna()`, `fillna()`, `to_csv()`, `to_parquet()` | `datetime`, `rolling()`, `resample()`, `pivot_table()` | Funciones muy específicas del API de Pandas que tienen poca demanda o que son difíciles de paralelizar. Algunas integraciones con librerías externas (como plotting directo con `df.plot()`) |

Nota inferior: Estas operaciones están paralelizadas por defecto y tienen mejoras de rendimiento significativas.

## Slide 17

Slide separador de sección. Número grande **03.** entre corchetes, ícono de portapapeles y título **Pandas vs Dask vs Modin**.

## Slide 18

**Comparativa de Librerías para Manipulación de Datos en Python**

Tabla comparativa (encabezados con emoji: 🐼 Pandas, Dask, ⚡ Modin):

| Característica | Pandas | Dask | Modin |
|---|---|---|---|
| Escalabilidad | Memoria local (RAM) | Escala a múltiples núcleos y clústeres | Escala automáticamente en múltiples núcleos |
| Interfaz API | pandas | Subconjunto compatible con pandas | Compatible con pandas (sin cambiar código) |
| Tamaño de datos soportado | Memoria limitada | Datos que exceden la RAM | Datos más grandes que RAM |
| Paralelismo | No | Sí (por bloques) | Sí (automático con Ray o Dask) |
| Facilidad de uso | Muy alta | Media | Muy alta (usa código pandas) |
| Ecosistema | Muy maduro | Integración con herramientas Big Data | En crecimiento |

## Slide 19

Slide separador de sección. Número grande **04.** entre corchetes, ícono de portapapeles y título **Laboratorio**.

## Slide 20

**Modin en GColab**

Visual: logos combinados **MODIN** + **Google Colab** (logo Modin, un signo "+" y el logo de Google Colab).

Texto grande: ¡¡¡¡¡¡¡¡ Ejecutemos nuestro script !!!!!!!!

## Slide 21

**Conclusiones**

Tres puntos numerados (01, 02, 03), cada uno enmarcado entre corchetes:

**01.** Modin facilita la paralelización automática de muchas operaciones de Pandas, permitiendo trabajar con grandes volúmenes de datos sin cambiar el código.

**02.** No todas las funciones de Pandas están completamente soportadas o paralelizadas en Modin, pero cubre la mayoría de las operaciones comunes usadas en análisis de datos.

**03.** Elegir entre Pandas, Modin y Dask depende del tamaño del dataset, recursos computacionales disponibles y la complejidad de las operaciones a realizar.

## Slide 22

Slide de cierre. Solo el logo UTEC (Universidad de Ingeniería y Tecnología) centrado sobre fondo cian con patrones geométricos. Decorativa.
