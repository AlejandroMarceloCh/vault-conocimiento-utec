---
curso: BIGDATA
titulo: 06 - Semana 4/W4 L4 Dask Array
slides: 0
fuente: 06 - Semana 4/W4 L4 Dask Array.ipynb
---

<div class="cell markdown" id="JlVE2hDgkg0i">

# Array con **Dask**

</div>

<div class="cell markdown" id="W1T4Xn23knoA">

Curso: Big Data - UTEC

</div>

<div class="cell markdown" id="IjAtYAVhknwl">

Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="8lUpYbiukw1U">

``` python
import dask.array as da
import numpy as np
```

</div>

<div class="cell code" id="Wsz-SXummj-1">

``` python
np.zeros([10, 10])
```

</div>

<div class="cell code" id="FBFBowvqmkB8">

``` python
da.zeros([10, 10],chunks=(5,5))
```

</div>

<div class="cell code" id="WQaG8kybmkFF">

``` python
np.eye(10)
```

</div>

<div class="cell code" id="--DMLvB_mpdZ">

``` python
mat1 = da.eye(10,chunks=(5))
```

</div>

<div class="cell code" id="ZW8yQcfmmpg1">

``` python
print(mat1.blocks[0, 0].compute())
```

</div>

<div class="cell code" id="-nBW-LgDmpjm">

``` python
print(mat1.blocks[0, 1].compute())
```

</div>

<div class="cell code" id="nCs069jNmpl0">

``` python
print(mat1.blocks[1, 0].compute())
```

</div>

<div class="cell code" id="XHBcg1obmvGU">

``` python
print(mat1.blocks[1, 1].compute())
```

</div>

<div class="cell code" id="LCOWIxflkw4Y">

``` python
# Convertir Numpy as Dask array
x = np.arange(12).reshape(3,4)
dx = da.from_array(x, chunks=(2,2))
```

</div>

<div class="cell code" id="pDb8f3dLkw7S">

``` python
# Aleatorios
a = da.random.random((6,6), chunks=(3,3))
b = da.random.random((6,6), chunks=(3,3))
```

</div>

<div class="cell code" id="ZD3np8Fskw94">

``` python
# Identidad
I = da.eye(5, chunks=(2))
```

</div>

<div class="cell code" id="ls63VDiXkxAu">

``` python
res1 = dx + 5
res1.compute()
```

</div>

<div class="cell code" id="krLwa9IekxDO">

``` python
res2 = dx - 3
res2.compute()
```

</div>

<div class="cell code" id="zKa0V9XHkxF0">

``` python
res3 = dx * 2
res3.compute()
```

</div>

<div class="cell code" id="0nu2D76YkxIe">

``` python
res4 = dx / 2
res4.compute()
```

</div>

<div class="cell code" id="yAUuRd0WkxKs">

``` python
res5 = dx ** 2
res5.compute()
```

</div>

<div class="cell code" id="xKAWQNqxlKZr">

``` python
da.sqrt(dx)
```

</div>

<div class="cell code" id="gj95ys-nlKc1">

``` python
dx.sum().compute()
```

</div>

<div class="cell code" id="PG6BK5p8lKff">

``` python
dx.mean().compute()
```

</div>

<div class="cell code" id="A37rrh4GlKiE">

``` python
dx.std().compute()
```

</div>

<div class="cell code" id="QfnKnKl6l4mB">

``` python
dx.var().compute()
```

</div>

<div class="cell code" id="MY_rtUKQlKkj">

``` python
dx.min().compute()
```

</div>

<div class="cell code" id="S1ckjCPLl8iI">

``` python
dx.max().compute()
```

</div>

<div class="cell code" id="XZy8BiG_l8lE">

``` python
da.percentile(a, [25, 50, 75]).compute()
```

</div>

<div class="cell code" id="jbznsSoul8n4">

``` python
dx[0, :].compute()
```

</div>

<div class="cell code" id="BuZvBCKkl8qt">

``` python
dx[:, 1].compute()
```

</div>

<div class="cell code" id="xQE16eykmFiQ">

``` python
dx[1:3, 2:4].compute()
```

</div>

<div class="cell code" id="w-boxJm8mFk9">

``` python
# Producto matricial
matmul = da.matmul(a, b)
print(matmul.compute())
```

</div>

<div class="cell code" id="boSqbORumFnt">

``` python
# Producto interno
dot = da.dot(dx, dx.T)
print(dot.compute())
```

</div>

<div class="cell code" id="pQFPXOabmFqS">

``` python
# Transpuesta
print(dx.T.compute())
```

</div>
