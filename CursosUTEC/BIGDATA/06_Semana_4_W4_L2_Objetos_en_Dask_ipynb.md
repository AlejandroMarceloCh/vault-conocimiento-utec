---
curso: BIGDATA
titulo: 06 - Semana 4/W4 L2 Objetos en Dask
slides: 0
fuente: 06 - Semana 4/W4 L2 Objetos en Dask.ipynb
---

<div id="0c4f3ada-38f1-4273-a438-3193c7cb8506" class="cell markdown">

# Dask

- Curso Big Data
- Universidad UTEC
- Docente: Mg. Aldo Lezama Benavides

En este notebook aprenderemos los **tipos principales de objetos en Dask** y cómo usarlos:

1.  Dask Array (`dask.array`) → similar a NumPy\
2.  Dask DataFrame (`dask.dataframe`) → similar a pandas\
3.  Dask Bag (`dask.bag`) → similar a listas de Python

Dask permite trabajar con **datasets más grandes que la memoria RAM** y distribuir cálculos en paralelo.

</div>

<div id="97e15db8-ec59-4154-979f-56aa800c960c" class="cell markdown">

## 1. Dask Array

- Es equivalente a **NumPy arrays**, pero dividido en bloques (*chunks*).
- Ideal para cálculos numéricos grandes (álgebra lineal, estadísticas).

</div>

<div id="cf219bea-12b3-4b5f-813d-062939f3ad19" class="cell code">

``` python
import dask.array as da
import numpy as np

# Crear un Dask array grande (10000x10000) en bloques de 1000x1000
x = da.random.random((10000, 10000), chunks=(1000, 1000))
x
```

</div>

<div id="43b8238c-42a4-4770-8c3a-bf2d124fe3d5" class="cell code">

``` python
# Operaciones: lazy (no se ejecutan hasta .compute())
y = x + x.T
z = y.mean()

print(z)          # objeto pendiente
print(z.compute()) # se ejecuta el cálculo
```

</div>

<div id="97522899-d0c3-4535-8e44-68902c1bc372" class="cell markdown">

## 2. Dask DataFrame

- Es equivalente a **pandas DataFrame**, pero particionado.
- Ideal para procesar datos tabulares que no caben en memoria.

</div>

<div id="70226fe0-c336-42ff-aef9-c4a8b4d64606" class="cell code">

``` python
import pandas as pd
import dask.dataframe as dd

# Crear un DataFrame de pandas
pdf = pd.DataFrame({
    "a": range(1, 1000001),
    "b": range(1000000, 0, -1)
})

# Convertirlo a Dask DataFrame con 10 particiones
ddf = dd.from_pandas(pdf, npartitions=10)
ddf
```

</div>

<div id="aa361b6b-0f72-49b6-be61-c8bd85390173" class="cell code">

``` python
# Operaciones (lazy)
media = ddf["a"].mean()
print(media)

# Ejecutar
print(media.compute())
```

</div>

<div id="6246d71e-dceb-4582-a1aa-ccf31c2bf914" class="cell markdown">

## 3. Dask Bag

- Es equivalente a una **lista de Python** o a un `map/filter` de Spark.
- Ideal para datos **semi-estructurados** (ej. JSON, logs, texto).

</div>

<div id="1ec41994-ac99-460f-a1fd-3b14275d6b76" class="cell code">

``` python
import dask.bag as db

# Crear un Dask Bag a partir de una lista
b = db.from_sequence([1, 2, 3, 4, 5], npartitions=2)
b
```

</div>

<div id="7cd5401a-c31f-40ae-b443-8f0bb59ac6a7" class="cell code">

``` python
# Operaciones lazy
mapped = b.map(lambda x: x**2).filter(lambda x: x % 2 == 0)
print(mapped)

# Ejecutar
print(mapped.compute())
```

</div>

<div id="43b0b82f-3c76-46a1-b6dc-ca01bf6cefd3" class="cell markdown">

## Resumen

- **Dask Array** → NumPy paralelo (álgebra, estadísticas).\
- **Dask DataFrame** → pandas paralelo (datos tabulares grandes).\
- **Dask Bag** → listas/colecciones paralelas (texto, JSON, logs).

Todos comparten la idea de **operaciones lazy**: se construye un grafo de tareas y se ejecuta al llamar `.compute()`.

</div>

<div id="edee5a08-3e9d-479b-9594-cbd584a2b388" class="cell code">

``` python
```

</div>
