---
curso: BIGDATA
titulo: 06 - Semana 4/W4 L6 Cluster_en_Dask_Funciones_y_Grafos
slides: 0
fuente: 06 - Semana 4/W4 L6 Cluster_en_Dask_Funciones_y_Grafos.ipynb
---

<div class="cell markdown" id="veB-ayKgZZih">

# Creación de un Cluster Local

</div>

<div class="cell markdown" id="Col9-up_aNgP">

Curso: Big Data - UTEC

Docente: Aldo Lezama Benavides

</div>

<div class="cell code">

``` python
!pip install "dask[distributed]" --upgrade
```

</div>

<div class="cell code" id="433H89LaUBXI">

``` python
from dask.distributed import Client, LocalCluster
```

</div>

<div class="cell code" id="eqZI9PY_URLX">

``` python
# Crear un cluster local con todos los núcleos disponibles
cluster = LocalCluster()

# Conectar un cliente al cluster
client = Client(cluster)

# Ver estado del cluster
client
```

</div>

<div class="cell code" id="I00TMydaURO1">

``` python
from dask.distributed import Client, LocalCluster

# Crear un cluster local con todos los núcleos disponibles
cluster = LocalCluster(n_workers=2, memory_limit='2GB')

# Conectar un cliente al cluster
client = Client(cluster)

# Ver estado del cluster
client
```

</div>

<div class="cell markdown" id="OPsPKLpyW2Jr">

## Funciones en paralelo

`@dask.delayed`convierte funciones normales de Python en tareas diferidas (lazy) que Dask puede optimizar, paralelizar y ejecutar eficientemente.

</div>

<div class="cell code" id="7J6k4dGgVGa9">

``` python
from dask import delayed

@delayed
def add(x, y):
    return x + y

a = add(1, 2)
b = add(a, 3)
result = b.compute()
```

</div>

<div class="cell markdown" id="mUVDVt1VVbXS">

## Grafo de Tareas con **visualize**

</div>

<div class="cell code" id="E2z3QvmKVGj5">

``` python
import dask
import time

@dask.delayed
def add(x, y):
    time.sleep(1)
    return x + y

@dask.delayed
def double(x):
    time.sleep(1)
    return x * 2

a = add(1, 2)
b = double(a)
c = add(b, 3)

# Visualizar el grafo de tareas
c.visualize(filename="proceso", format="png")
```

</div>

<div class="cell markdown" id="vMqDxvAoXYyz">

**Análisis:**

Este grafo representa un flujo secuencial de 3 tareas dependientes entre sí

`a = add(1, 2)`

Crea una tarea para sumar 1 + 2.

Esta es la primera tarea del grafo.

`b = double(a)`

Toma el resultado de a y lo multiplica por 2.

Esta tarea depende de a.

`c = add(b, 3)`

Suma el resultado de b con 3.

Esta tarea depende de b

</div>

<div class="cell markdown" id="6YBGLAxKY7EE">

## Grafo de Tareas que comparten procesos con **visualize**

</div>

<div class="cell code" id="g6ja8TLAWX0A">

``` python
import dask
from dask import delayed

@delayed
def inc(x):
    return x + 1

@delayed
def double(x):
    return x * 2

@delayed
def add(x, y):
    return x + y

shared = inc(1)

# Dos pipelines que lo usan
a = double(shared)
b = add(shared, 3)

final = add(a, b)

# Visualizar grafo
final.visualize(filename="proceso_final", format="png")
```

</div>

<div class="cell markdown" id="zD18yJ1hYaLF">

**Análisis:**

Este grafo representa un flujo con bifurcación y tareas compartidas, lo cual permite ejecución paralela parcial y evita recomputación.

Es un ejemplo claro de reutilización de resultados intermedios, algo común en ciencia de datos y pipelines.

Muestra cómo Dask optimiza automáticamente sin que el usuario tenga que preocuparse por duplicación.

En flujos más grandes, esta deduplicación puede ahorrar tiempo de cómputo y memoria.

</div>

<div class="cell markdown" id="HvB_8QlQZBGJ">

## Modulo de **Machine Learning con Dask**

</div>

<div class="cell code" id="wor-dOe7U484">

``` python
pip install dask-ml
```

</div>

<div class="cell code" id="SZlsdZ0VURR0">

``` python
import pkgutil
import dask_ml
for module_info in pkgutil.walk_packages(dask_ml.__path__, prefix='dask_ml.'):
    print(module_info.name)
```

</div>
