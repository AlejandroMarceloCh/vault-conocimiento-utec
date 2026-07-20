---
curso: BIGDATA
titulo: 06 - Semana 4/W4 L3 Dask vs Numpy
slides: 0
fuente: 06 - Semana 4/W4 L3 Dask vs Numpy.ipynb
---

<div id="3f0357be-7a7a-4489-ab03-74856c3c18c5" class="cell markdown">

# Comparación de rendimiento: NumPy vs Dask

- Curso Big Data
- Universidad UTEC
- Docente: Mg. Aldo Lezama Benavides

En este notebook vamos a comparar el rendimiento de **NumPy** y **Dask** en operaciones numéricas.

## Objetivos

1.  Entender cómo se comporta NumPy vs Dask en operaciones grandes.
2.  Medir tiempos con `%%timeit`.
3.  Ver cuándo conviene usar Dask.

------------------------------------------------------------------------

</div>

<div id="77b8e866-561b-4400-99b6-e453bbf5f452" class="cell code">

``` python
import numpy as np
import dask.array as da
import time
```

</div>

<div id="ec58c751-7ce5-4943-ab05-86ad414809d3" class="cell code">

``` python
# Arrays de tamaño 10,000 x 10,000

# NumPy: se crea en RAM de golpe
np_array = np.random.random((10000, 10000))

# Dask: se crea en chunks (bloques) de 1000x1000
dask_array = da.random.random((10000, 10000), chunks=(1000, 1000))
```

</div>

<div id="c64211b6-3b23-4a4e-b721-28ffaaf334bf" class="cell markdown">

# Suma de todos los elementos

</div>

<div id="5f11b6a3-6c27-4377-95f8-151a01d99b86" class="cell code">

``` python
%%timeit
np_array.sum()
```

</div>

<div id="f82f9458-0ad0-4c39-87c7-0f5d194f6189" class="cell code">

``` python
%%timeit
dask_array.sum().compute()
```

</div>

<div id="b0772c38-f7aa-455a-a4b8-4e5c41422e20" class="cell markdown">

# Media de todos los elementos

</div>

<div id="bcfd1b94-da62-4205-8c00-18277bf45021" class="cell code">

``` python
%%timeit
np_array.mean()
```

</div>

<div id="ff5e3e25-d22e-4184-a461-ca1ed33696f1" class="cell code">

``` python
%%timeit
dask_array.mean().compute()
```

</div>

<div id="ce6c87b7-cd18-4f73-861f-6e6758d6c553" class="cell markdown">

# Multiplicación de matrices

</div>

<div id="f907389d-3d7b-4447-b39b-d88b0de6655a" class="cell code">

``` python
%%timeit
A_np = np.random.random((5000, 2000))
B_np = np.random.random((2000, 1000))
A_np.dot(B_np)
```

</div>

<div id="d290c031-c7a1-4b4a-b2d7-131bed87f65e" class="cell code">

``` python
%%timeit
A_da = da.random.random((5000, 2000), chunks=(1000, 1000))
B_da = da.random.random((2000, 1000), chunks=(1000, 1000))
(A_da.dot(B_da)).compute()
```

</div>

<div id="09153f0c-9e68-4633-bf3e-01aa1400abbe" class="cell markdown">

### Comentarios:

- **NumPy** suele ser más rápido cuando los datos **entran en memoria** (RAM suficiente).
- **Dask** es más lento en pequeños datasets, porque tiene overhead de paralelización.
- **Dask gana ventaja** cuando:
  - El dataset no cabe en memoria (divide en chunks).
  - Hay varios núcleos que pueden trabajar en paralelo.
  - Escalamos a un clúster distribuido.

En laptops con 4-8 núcleos y RAM limitada, Dask puede ser más eficiente en datasets grandes.

</div>

<div id="befc20d0-cdda-47b2-8219-7ec276e8b8be" class="cell code">

``` python
```

</div>

<div id="6a3ee0a6-82a2-4754-a100-dacb6063422b" class="cell code">

``` python
```

</div>

<div id="9e3976c9-376c-4f98-879d-754edc8748d8" class="cell code">

``` python
```

</div>
