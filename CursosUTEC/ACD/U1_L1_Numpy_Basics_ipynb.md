---
curso: ACD
titulo: U1_L1 Numpy Basics
slides: 0
fuente: U1_L1 Numpy Basics.ipynb
---

<div class="cell markdown" id="u2oLWISAdcNp">

# **U1_L1: Numpy Basics**

</div>

<div class="cell markdown" id="CcdhphYgd5-c">

## **Paso 0:** Cargar la librería

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068583132,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="t4yxtWdIdXi3">

``` python
import numpy as np
```

</div>

<div class="cell markdown" id="e-iq8J6MeBED">

## **I. Inicialización**

Hay varias formas de inicializar un array NumPy. La más sencilla es pasar una lista (o cualquier otro objeto similar a un array) al método de array en NumPy.

**Syntax:** `array_nombre = np.array(listas)`

</div>

<div class="cell code" execution_count="2" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:318,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068638952,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="AQjdYFgte1aL" outputId="cfdebdaf-eddb-494e-8576-9ddaa058fcf1">

``` python
myarray_1D = np.array([1,2,3,4,5])
myarray_1D
```

<div class="output execute_result" execution_count="2">

    array([1, 2, 3, 4, 5])

</div>

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:339,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068691044,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pnR7acGKele3" outputId="a7e1b79a-2d9c-4b66-e4f9-5d56117f8254">

``` python
myarray_2D = np.array([[1,2,3,4],[5,6,7,8]])
print(myarray_2D)
```

<div class="output stream stdout">

    [[1 2 3 4]
     [5 6 7 8]]

</div>

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:371,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068784377,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="W5xDZ1Vzfa6u" outputId="68a0d378-83b0-4756-a739-63cceff12577">

``` python
tuple_to_np = np.array((1,2,3,4,5))
tuple_to_np
```

<div class="output execute_result" execution_count="4">

    array([1, 2, 3, 4, 5])

</div>

</div>

<div class="cell markdown" id="NTKtoLn7foP6">

## **II. Dimensiones**

</div>

<div class="cell markdown" id="_KcHpkVxftQY">

**ndim:** el número de dimensiones (ejes) de datos.

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:647,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068874800,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KnwpJaRpjH-a" outputId="87b14854-3e32-4cd5-b9e1-7ccd845ec648">

``` python
myarray_1D.ndim
```

<div class="output execute_result" execution_count="5">

    1

</div>

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:7,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068875281,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="suvRGbCojOkK" outputId="32076238-71e9-4ff3-b7b6-19e0e6c4d72e">

``` python
myarray_2D.ndim
```

<div class="output execute_result" execution_count="6">

    2

</div>

</div>

<div class="cell markdown" id="7KoHAtxtjnC1">

**shape**: devuelve el número de elementos a lo largo de cada dimensión como una tupla

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:311,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068896157,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Qq4G2FSrjtYo" outputId="21a78470-cfec-4147-df2f-cdf833c55f42">

``` python
myarray_1D.shape
```

<div class="output execute_result" execution_count="7">

    (5,)

</div>

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:282,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068900605,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="FhHFdo1Ij0VX" outputId="14c32021-d428-4cb8-8c05-665b5748f4ef">

``` python
myarray_2D.shape
```

<div class="output execute_result" execution_count="8">

    (2, 4)

</div>

</div>

<div class="cell markdown" id="FZzXZjXTj--E">

**size**: Devuelve el número de elementos de un array.

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:362,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068970080,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="GyVWNjXPkOmC" outputId="b2433814-dae4-4114-a6b5-41d1b7bf6e3d">

``` python
myarray_1D.size
```

<div class="output execute_result" execution_count="9">

    5

</div>

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:361,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712068973577,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="J8kxf5blkQxN" outputId="c51a25a7-167b-41c0-b14a-4c70b5586063">

``` python
myarray_2D.size
```

<div class="output execute_result" execution_count="10">

    8

</div>

</div>

<div class="cell markdown" id="OKMBrjAWkbuY">

**dtype**: esto nos proporciona el tipo de datos de los elementos del array.

</div>

<div class="cell code" execution_count="11" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:330,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069035938,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mG1oMTDMkeAO" outputId="e000082d-80c0-46a3-cfd4-33739e4cd70d">

``` python
myarray = np.array([10, 20, 30, 40, 50])
myarray
```

<div class="output execute_result" execution_count="11">

    array([10, 20, 30, 40, 50])

</div>

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:331,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069042386,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RSHMNAodkmWR" outputId="db4b400f-dd85-4992-876a-4e2357cdb971">

``` python
myarray.dtype
```

<div class="output execute_result" execution_count="12">

    dtype('int32')

</div>

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:344,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069068644,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ilCFrqGkkq8K" outputId="f0877976-58fd-4e45-c9db-d4ab4b7453bb">

``` python
(myarray / 5).dtype
```

<div class="output execute_result" execution_count="13">

    dtype('float64')

</div>

</div>

<div class="cell markdown" id="rsUPBjI7k9nd">

## **III. Arrays Especiales**

NumPy nos permite inicializar rápidamente conjuntos grandes con mucha facilidad, especialmente aquellos asociados con la computación científica.

`np.zeros` Esta función crea un nuevo array lleno de ceros de forma y tipo determinados (opcional).

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:311,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069213890,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="87Vilz1VlgsC" outputId="d428257d-47a6-4e06-9a6a-57983fa5bcf4">

``` python
zero = np.zeros((3,2))

print(zero)
```

<div class="output stream stdout">

    [[0. 0.]
     [0. 0.]
     [0. 0.]]

</div>

</div>

<div class="cell markdown" id="WCUZ9Yjhll3h">

`np.ones` Esta función crea un nuevo array lleno de unos de forma indicada.

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:304,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069238001,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pcOUj8oxllIT" outputId="79717a42-28ab-40e4-dc54-6c44b545652d">

``` python
one = np.ones((2,9))

print(one)
```

<div class="output stream stdout">

    [[1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1.]]

</div>

</div>

<div class="cell markdown" id="SAZjlDT8l6tq">

`np.eye` Esta función crea una matriz de identidad

</div>

<div class="cell code" execution_count="16" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:294,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069263708,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="wL2bzL-smBt8" outputId="c37f3745-b87a-4dba-e913-7db2d055ba78">

``` python
I_1 = np.eye(5)
print(I_1, "\n")
```

<div class="output stream stdout">

    [[1. 0. 0. 0. 0.]
     [0. 1. 0. 0. 0.]
     [0. 0. 1. 0. 0.]
     [0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 1.]] 

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:397,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069299028,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="TbraIwr4mLOo" outputId="789cde30-f919-4924-83c9-a95f2bcc0183">

``` python
I_2 = np.eye(6,4, 1)
print(I_2, "\n")
```

<div class="output stream stdout">

    [[0. 1. 0. 0.]
     [0. 0. 1. 0.]
     [0. 0. 0. 1.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]] 

</div>

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:303,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069405645,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="GT8PL8N6mV2T" outputId="fa5beba8-d665-4f6f-9765-d2d34084969f">

``` python
I_3 = np.eye(6,4, -2)
print(I_3, "\n")
```

<div class="output stream stdout">

    [[0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]
     [0. 0. 0. 1.]] 

</div>

</div>

<div class="cell markdown" id="BP2YQ3-jmu_u">

Además de estos, también podemos crear arrays igualmente espaciados. Tenemos el tipo de datos de rango en Python estándar. NumPy tiene dos métodos muy comunes que se utilizan para crear rápidamente valores espaciados de manera similar. Estos son:

`np.arange` Esta función crea un array de valores espaciados uniformemente dentro de un intervalo definido de acuerdo con el número de argumentos especificados.

**Syntax:** `np.arange(start,stop,step)`

</div>

<div class="cell code" execution_count="19" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:343,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069562931,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="sX5eOCNfnEHh" outputId="bd70e234-b36b-4d18-ec57-95ad389c4f9a">

``` python
# numpy.arange(stop)
print(np.arange(5))
```

<div class="output stream stdout">

    [0 1 2 3 4]

</div>

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:333,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069597760,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="krHpMDHXnGZw" outputId="bec06bf5-2af7-4f85-a10d-c5d8283ef8bd">

``` python
# numpy.arange(start, stop)
print(np.arange(1, 10))
```

<div class="output stream stdout">

    [1 2 3 4 5 6 7 8 9]

</div>

</div>

<div class="cell code" execution_count="21" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:265,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069646747,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="7HRnIdXunKSz" outputId="9fea41f0-6520-4c96-f961-cebcca05d5e9">

``` python
# numpy.arange(start, stop, step)
print(np.arange(1, 10, 2))
```

<div class="output stream stdout">

    [1 3 5 7 9]

</div>

</div>

<div class="cell markdown" id="zEkUNw3DnOkZ">

`np.linspace` Similar a `np.arange`, esta función crea un array de valores espaciados uniformemente. Sin embargo, la diferencia es que puede especificar el número de elementos en lugar de un intervalo o paso.

**Syntax:** np.linspace(start(inclusive),stop(inclusive), number of evenly spaced numbers)

</div>

<div class="cell code" execution_count="22" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:324,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069730419,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KIM1WbPxnPdq" outputId="69d8f20f-da7d-4ef4-ecb7-d46121079dfd">

``` python
print(np.linspace(0, 10, 2))
```

<div class="output stream stdout">

    [ 0. 10.]

</div>

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:312,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069763907,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="UpexizQ7nWiF" outputId="35067868-1d07-49af-8ee2-70f02bff1303">

``` python
print(np.linspace(0, 10, 5))
```

<div class="output stream stdout">

    [ 0.   2.5  5.   7.5 10. ]

</div>

</div>

<div class="cell code" execution_count="24" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:421,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069853480,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="uR6Wtn9tnZ_i" outputId="680a0ec5-144c-48ae-e423-6784b68af4f1">

``` python
#Por default, imprime 50 valores
print(np.linspace(0, 10, ))
```

<div class="output stream stdout">

    [ 0.          0.20408163  0.40816327  0.6122449   0.81632653  1.02040816
      1.2244898   1.42857143  1.63265306  1.83673469  2.04081633  2.24489796
      2.44897959  2.65306122  2.85714286  3.06122449  3.26530612  3.46938776
      3.67346939  3.87755102  4.08163265  4.28571429  4.48979592  4.69387755
      4.89795918  5.10204082  5.30612245  5.51020408  5.71428571  5.91836735
      6.12244898  6.32653061  6.53061224  6.73469388  6.93877551  7.14285714
      7.34693878  7.55102041  7.75510204  7.95918367  8.16326531  8.36734694
      8.57142857  8.7755102   8.97959184  9.18367347  9.3877551   9.59183673
      9.79591837 10.        ]

</div>

</div>

<div class="cell markdown" id="aBXVSY1soFSN">

## **IV. Array Slicing**

El corte de arrays (array slicing) es similar al corte de listas en Python. La indexación de arrays también comienza desde 0. Sin embargo, dado que los arrays pueden ser multidimensionales, debemos especificar el segmento para cada dimensión.

**Syntax:** `nameofarray[start_row:end_row, start_col:end_col`

</div>

<div class="cell code" execution_count="25" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:336,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712069933203,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="nv2DMw-noKAZ" outputId="d1765f49-85b2-484f-bc5f-d361febba732">

``` python
myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(myArray)
```

<div class="output stream stdout">

    [[1 2 3]
     [4 5 6]
     [7 8 9]]

</div>

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:300,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070181917,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Scuk9Q6AoNGp" outputId="9a630ac7-8147-4c13-ddf2-1bdc3ba7c17c">

``` python
#Devuelve el elemento en la fila 1 y columna 2
myArray[0:2, 1:2]
```

<div class="output execute_result" execution_count="26">

    array([[2],
           [5]])

</div>

</div>

<div class="cell markdown" id="FoKx2Ts7oJeE">

**Recuperación de elementos desde filas:** Para recuperar todos los elementos de la primera fila, especifique el parámetro de fila como 0 y deje el parámetro de columna vacío.

**Syntax:** `myArray[0,:]`

</div>

<div class="cell code" execution_count="27" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:278,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070260992,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="kzb6bPi4oRCe" outputId="d616b78d-537d-4606-93a4-83e2a7ecb567">

``` python
myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(myArray[0,:])
```

<div class="output stream stdout">

    [1 2 3]

</div>

</div>

<div class="cell markdown" id="BvJiqNyVoXVn">

**Recuperación de elementos desde columnas:** En este ejemplo, estamos recuperando elementos de la segunda columna. Por lo tanto, necesitaríamos especificar el parámetro de columna y dejar vacío el parámetro de fila.

**Syntax:** `myArray[:,1]`

</div>

<div class="cell code" execution_count="28" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:382,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070290306,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="1hv9wWH4obH5" outputId="3cfef8cf-f8bc-4e21-e61b-800c431e03d3">

``` python
myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(myArray[:,1])
```

<div class="output stream stdout">

    [2 5 8]

</div>

</div>

<div class="cell markdown" id="VHOMO549osxU">

**Recuperación de elementos desde filas y columnas:** Supongamos que queremos recuperar un sub-array que consta de las 2 primeras filas y las 3 columnas. Podemos especificar los parámetros de la siguiente manera.

</div>

<div class="cell code" execution_count="29" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070312793,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="WP-TxfcHoV-C" outputId="fbed58c9-b89e-4a3f-97bb-284d2fbea72c">

``` python
myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(myArray)
```

<div class="output stream stdout">

    [[1 2 3]
     [4 5 6]
     [7 8 9]]

</div>

</div>

<div class="cell code" execution_count="30" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:837,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070319593,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="C0WQoymmowLb" outputId="3481f156-d49f-44b8-a58c-b23ec8664fea">

``` python
myArray_new = myArray[:2,:]

print(myArray_new)
print(myArray_new.shape)
```

<div class="output stream stdout">

    [[1 2 3]
     [4 5 6]]
    (2, 3)

</div>

</div>

<div class="cell code" execution_count="31" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:338,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070545907,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="94IUnEyOWRQi" outputId="7ebd0424-3a1d-4bfe-efc9-a982ed175226">

``` python
myArray_new2 = myArray[1:3,1:3]
myArray_new2
```

<div class="output execute_result" execution_count="31">

    array([[5, 6],
           [8, 9]])

</div>

</div>

<div class="cell code" execution_count="32" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:331,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070578420,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="638yOw2AW2-G" outputId="b9ba2b1a-194d-49bf-ae35-2931498454c2">

``` python
myArray_new3 = myArray[1:,1:]
myArray_new3
```

<div class="output execute_result" execution_count="32">

    array([[5, 6],
           [8, 9]])

</div>

</div>

<div class="cell markdown" id="amQEZIm_o0xr">

**Revertir el orden de los elementos del array:** El corte también se puede usar para invertir el orden de los elementos en las matrices. Primero creemos una matriz para trabajar usando `np.arange` y luego usemos la siguiente sintaxis: `myArray[::-1]`

</div>

<div class="cell code" execution_count="33" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:296,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070648940,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8GxvKn0Wo3ba" outputId="9f1364ae-a197-4e77-91ff-03097febee43">

``` python
myArray = np.arange(8)

print("El array original: \n", myArray, "\n")

print("El array revertido: \n", myArray[::-1], "\n")
```

<div class="output stream stdout">

    El array original: 
     [0 1 2 3 4 5 6 7] 

    El array revertido: 
     [7 6 5 4 3 2 1 0] 

</div>

</div>

<div class="cell markdown" id="0IDVuUK5o51q">

**Remodelar (reshape) los arrays:** Puede haber varias razones para remodelar arrays. Una de estas razones podría ser cuando desea agregar un array a otro: deben ser del mismo tamaño. Recuerda que la forma de un array es el número de elementos en cada dimensión.

</div>

<div class="cell code" execution_count="34" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:321,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070705982,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Xthy_poao81P" outputId="30a0f98b-5ae9-4dec-bc08-a650e8728b55">

``` python
myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Array Original: \n", myArray, "\n")
```

<div class="output stream stdout">

    Array Original: 
     [[1 2 3]
     [4 5 6]
     [7 8 9]] 

</div>

</div>

<div class="cell code" execution_count="35" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:342,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070727302,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="xdcteSrzpAkv" outputId="124a122c-5501-47ae-dd1c-4b0ce61ae309">

``` python
myArray_reshaped = myArray.reshape(1,9)

print("Array remodelado: \n", myArray_reshaped, "\n")
print("Su forma: ", myArray_reshaped.shape)
```

<div class="output stream stdout">

    Array remodelado: 
     [[1 2 3 4 5 6 7 8 9]] 

    Su forma:  (1, 9)

</div>

</div>

<div class="cell markdown" id="D6UgJMoApCrX">

`.reshape` tiene una función especial en la que detecta automáticamente el número de columna. Esto significa que en realidad no tenemos que especificar un número de columna, simplemente podemos reemplazar el número de columna con -1.

</div>

<div class="cell code" execution_count="36" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070799877,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="q0XQ6aMeXxz7" outputId="6a56e192-0658-45f9-cf47-669328027adb">

``` python
myArray
```

<div class="output execute_result" execution_count="36">

    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])

</div>

</div>

<div class="cell code" execution_count="37" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:315,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070777698,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="yRRuEdoBpE3c" outputId="7cdb22f7-62df-4883-cc34-a71f2f604d39">

``` python
myArray_reshaped = myArray.reshape(1,-1)

print("Array remodelado: \n", myArray_reshaped, "\n")
print("Su forma: ", myArray_reshaped.shape, "\n")
```

<div class="output stream stdout">

    Array remodelado: 
     [[1 2 3 4 5 6 7 8 9]] 

    Su forma:  (1, 9) 

</div>

</div>

<div class="cell code" execution_count="38" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:335,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070908746,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="z4ppVY9VpG3f" outputId="3eea84b1-361e-4d31-d868-b3144cc21f13">

``` python
print("usando reshape con el número automático de columna -1:")
print(myArray_reshaped.reshape(3,-1))
```

<div class="output stream stdout">

    usando reshape con el número automático de columna -1:
    [[1 2 3]
     [4 5 6]
     [7 8 9]]

</div>

</div>

<div class="cell markdown" id="stzjLQU1pkkk">

## **V. Funciones en NumPy**

NumPy viene con una variedad de funciones integradas. Estas funciones realizan operaciones matemáticas y cálculos científicos complejos muy rápidamente.

También podemos realizar estas operaciones a lo largo de un eje particular en lugar de en toda la matriz. Entonces, si desea tomar la suma de elementos a lo largo de las filas o solo a lo largo de las columnas, eso también es posible, recuerde que la dimensión más externa es el eje 0, la siguiente el eje 1, y así sucesivamente. Al igual que con Python estándar, podemos usar indexación negativa. La dimensión más interna será el eje = -1 y así sucesivamente.

</div>

<div class="cell code" execution_count="39" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:295,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070932801,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="rLgOSNUxp_a2" outputId="a8b23758-8260-4c6a-a093-33d2a51fdd85">

``` python
x = np.array([[1,2],[3,4]])
print(x)
```

<div class="output stream stdout">

    [[1 2]
     [3 4]]

</div>

</div>

<div class="cell code" execution_count="40" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070934945,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Umby19E4qBmw" outputId="a5840538-99d7-4d47-ca67-75759094e975">

``` python
y = np.ones((2,2))
print(y)
```

<div class="output stream stdout">

    [[1. 1.]
     [1. 1.]]

</div>

</div>

<div class="cell markdown" id="aW9xFZznqEy-">

**Suma de arrays**

</div>

<div class="cell code" execution_count="41" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:391,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070938369,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8PNitkItqHEl" outputId="37185123-671c-4f12-8e98-7b1b28f1e4e1">

``` python
#Método 1: Usando el operador +
print(x + y)
```

<div class="output stream stdout">

    [[2. 3.]
     [4. 5.]]

</div>

</div>

<div class="cell code" execution_count="42" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:295,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070941874,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="h9TSvK1ZqJey" outputId="6db736c8-46be-441c-9ecf-e9ba6d48de68">

``` python
#Método 2: Usar `np.add`
print(np.add(x,y))
```

<div class="output stream stdout">

    [[2. 3.]
     [4. 5.]]

</div>

</div>

<div class="cell markdown" id="Zvl_NeI2qN_E">

**Resta, multiplicación y división de arrays**

</div>

<div class="cell code" execution_count="43" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:297,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070950776,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="q1C4_fXGqOnj" outputId="5c60ab3e-6ec2-4ef7-99de-fcde733c99f5">

``` python
print(x)
print()
print(y)
```

<div class="output stream stdout">

    [[1 2]
     [3 4]]

    [[1. 1.]
     [1. 1.]]

</div>

</div>

<div class="cell code" execution_count="44" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:318,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070955892,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="rOk865hNqSXv" outputId="2cca46fc-e15e-49b3-e93f-a9fd70e6c237">

``` python
print(np.subtract(x,y))
```

<div class="output stream stdout">

    [[0. 1.]
     [2. 3.]]

</div>

</div>

<div class="cell code" execution_count="45" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:456,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070960017,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="prNaVh-RqUYI" outputId="2b213b90-8367-475a-d913-0428b525d347">

``` python
print(np.multiply(x,y))
```

<div class="output stream stdout">

    [[1. 2.]
     [3. 4.]]

</div>

</div>

<div class="cell code" execution_count="46" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:311,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712070970576,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="o6FOYoCjqWTV" outputId="31f81043-1c80-4d51-a7d0-cec490f1da36">

``` python
print(np.divide(x,y))
```

<div class="output stream stdout">

    [[1. 2.]
     [3. 4.]]

</div>

</div>

<div class="cell markdown" id="bVD0SEbOqkJ2">

Puede consultar la documentación para obtener [la lista completa de funciones](https://numpy.org/doc/stable/reference/routines)en NumPy.

</div>

<div class="cell markdown" id="9LUKv4XftCbb">

## **EJERCICIOS**

1.  Crea un arreglo NumPy con 10 elementos enteros aleatorios entre 1 y 100
2.  Reshape un arreglo NumPy de 1D con 20 elementos en un arreglo 2D de 4x5.
3.  Crea una matriz NumPy 5x5 con valores enteros aleatorios entre 1 y 100. Extrae la submatriz central de 3x3.
4.  Crea un arreglo NumPy de 1D con 15 elementos aleatorios entre 1 y 50. Utiliza slicing para obtener los elementos en las posiciones pares y luego realiza una operación para duplicar su valor.
5.  Crea un arreglo NumPy de 1D con 15 elementos. Agregue un nuevo eje para convertir este en un array de 2D con shape (15, 1).
6.  Crea un arreglo NumPy de 2D con shape (2, 3) y expanda sus dimensiones para crear un arreglo de 3D con shape (1, 2, 3).
7.  Crea una matriz NumPy 6x6 con valores enteros consecutivos empezando desde 1. Luego, realiza un slicing para obtener la submatriz de 4x4 en la esquina inferior derecha.
8.  Crea un arreglo NumPy de 1D con 10 elementos aleatorios entre 1 y 100. Luego, calcula la suma, el promedio, el mínimo y el máximo de los elementos.
9.  Crea dos arreglos NumPy de 1D con 5 elementos cada uno, con valores aleatorios entre 1 y 10. Luego, realiza una suma y una multiplicación elemento por elemento entre los dos arreglos.
10. Utiliza np.arange para crear un arreglo NumPy con los números del 20 al 10 en intervalos de -1.

</div>

<div class="cell code">

``` python
```

</div>
