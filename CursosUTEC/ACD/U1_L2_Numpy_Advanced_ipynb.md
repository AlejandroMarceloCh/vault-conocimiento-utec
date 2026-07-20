---
curso: ACD
titulo: U1_L2 Numpy Advanced
slides: 0
fuente: U1_L2 Numpy Advanced.ipynb
---

<div class="cell markdown" id="mgaGV5QNPYya">

# **U1_L2 Numpy Advanced**

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:5,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161623549,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RMKyD7AePUIh">

``` python
import numpy as np
```

</div>

<div class="cell markdown" id="zVEsJBPwPhpn">

## **I. Agregando elementos a los arrays**

</div>

<div class="cell markdown" id="IjemTBlcP10y">

`np.append` para agregar elementos a nuestros dataset

**Syntax:** `np.append(ndarray, elements you want to add, axis)`

`axis = 0` es fila `axis = 1` es columna

</div>

<div class="cell markdown" id="TYfRGm1DQprN">

Agregando un elemento a un array 1D

</div>

<div class="cell code" execution_count="2" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:361,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161659310,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="VvQBeYG9Qmsa" outputId="01abe64d-0049-449f-943f-5e8c64720a98">

``` python
x = np.array([1,2,3,4])

x = np.append(x,12)

print(x)
```

<div class="output stream stdout">

    [ 1  2  3  4 12]

</div>

</div>

<div class="cell markdown" id="0kz2we6gQ_Qb">

Agregando más de 1 elemento

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:362,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161698275,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="V8MM7aecRETx" outputId="3a0b201b-7d48-46f7-8949-eada3e6a87e6">

``` python
x = np.append(x,[12,13])

print(x)
```

<div class="output stream stdout">

    [ 1  2  3  4 12 12 13]

</div>

</div>

<div class="cell markdown" id="mxio_JzvRKhQ">

Agregando nuevas filas a arrays 2D

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:374,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161746480,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="BEhftKDPRNmq" outputId="45e75f87-ecdb-41d4-ef10-b1161683f69e">

``` python
y = np.array([[1,2],[3,4]])

print(x)
print("\n")
print(y)
```

<div class="output stream stdout">

    [ 1  2  3  4 12 12 13]


    [[1 2]
     [3 4]]

</div>

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:493,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161791165,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="xjpHvffDR7To" outputId="04459122-11b5-4069-9144-e2113365fdf5">

``` python
y = np.append(y,[[11,12]],axis = 0)

print(y)
```

<div class="output stream stdout">

    [[ 1  2]
     [ 3  4]
     [11 12]]

</div>

</div>

<div class="cell markdown" id="TuqoMnw3R_Sn">

Agregar columnas extras a arrays 2D.

En este caso debemos especificar `axis=1`

</div>

<div class="cell code" id="W0ZOJHUYSHnb">

``` python
y = np.array([[1,2],[3,4]])

print(x)
print("\n")
print(y)
```

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:313,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161820147,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="1Tb2JBQnSM9n" outputId="7f76f6a9-98db-4085-88c5-9d6f82ff421d">

``` python
y = np.append(y,[[11],[12]],axis = 1)

print(y)
```

<div class="output stream stdout">

    [[ 1  2 11]
     [ 3  4 12]]

</div>

</div>

<div class="cell markdown" id="NoQ8E5DdcOsN">

## **II. Manipulación de arrays**

</div>

<div class="cell markdown" id="nkWPQjq3Xz4v">

`np.insert` Otra opción para insertar elementos. La diferencia con `np.append` es que `np.insert` inserta en alguna posición específica.

**Syntax:** `np.insert(ndarray, index, elements,axis)`

</div>

<div class="cell markdown" id="8kusntlzYcjU">

Insertar elementos en array 1D

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:420,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161909886,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="tYozLUztYU21" outputId="e181aeea-a9ed-4c9f-c73f-d272403f6f17">

``` python
x = np.array([1,2,3,4])
print(x)
```

<div class="output stream stdout">

    [1 2 3 4]

</div>

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:286,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161916274,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="vb2PGLNUYaBR" outputId="62b1f090-2f3f-46f0-d55a-4e4540db5853">

``` python
x = np.insert(x,2,[11,12,13])

print(x)
```

<div class="output stream stdout">

    [ 1  2 11 12 13  3  4]

</div>

</div>

<div class="cell markdown" id="7xmhepg6YfYQ">

Insertar elementos en filas dentro de un array 2D

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:279,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161971198,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="JZn59VMOYhjm" outputId="a7a6ca2f-04ac-4676-9ac9-f565f9c5b891">

``` python
y = np.array([[1,2],[3,4]])
print(y)
```

<div class="output stream stdout">

    [[1 2]
     [3 4]]

</div>

</div>

<div class="cell code" execution_count="11" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:272,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712161989580,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="O_6pdQ23YpMI" outputId="d159d758-6164-41d7-98ec-07ddac2c53d1">

``` python
y = np.insert(y,1,[11,12],axis = 0)
print(y)
```

<div class="output stream stdout">

    [[ 1  2]
     [11 12]
     [ 3  4]]

</div>

</div>

<div class="cell markdown" id="-ZIznRqxYwPK">

Insertar elementos en columnas dentro de un array 2D

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:377,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162024687,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8i24P9tjY0Wx" outputId="4837f060-485b-4190-a708-2af384792e9c">

``` python
y = np.array([[1,2],[3,4]])
print(y)
```

<div class="output stream stdout">

    [[1 2]
     [3 4]]

</div>

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162026241,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pqt25aTLY2D3" outputId="d6034973-5c6f-481e-b612-946e5f36ef26">

``` python
y = np.insert(y,2,11,axis = 1)
print(y)
```

<div class="output stream stdout">

    [[ 1  2 11]
     [ 3  4 11]]

</div>

</div>

<div class="cell markdown" id="YIuf0gKGZFyK">

`np.delete()` Borrar elementos en un dataset

**Syntax:** `np.delete(ndarray,elements,axis)`

</div>

<div class="cell markdown" id="GLma8fmTZNo-">

Eliminar elementos en un array 1D

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:420,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162070185,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="f4eVOXEJZrFa" outputId="f531af06-3129-407b-9cb2-5d037239144f">

``` python
x = np.array([1,2,3,4])

print(x)
```

<div class="output stream stdout">

    [1 2 3 4]

</div>

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:289,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162081547,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="1qErKq3IZxnF" outputId="df318d9b-d0ab-43ea-8430-6ec8338d5c5a">

``` python
x = np.delete(x,[0,2])

print(x)
```

<div class="output stream stdout">

    [2 4]

</div>

</div>

<div class="cell markdown" id="QB-QfYoxZ_iQ">

Eliminar elementos en un array 2D

</div>

<div class="cell code" execution_count="16" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:391,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162132059,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="D37fTifvaEKm" outputId="9bbafe0d-3ab7-42b7-f932-7bef303aae22">

``` python
y = np.array([[1,2],[3,4]])

print("El array original:")
print(y)
print()
```

<div class="output stream stdout">

    El array original:
    [[1 2]
     [3 4]]

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:269,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162136523,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="6I1gPtl_aLLV" outputId="7ab30076-1679-44d0-8bda-0a26b7f9dc98">

``` python
y1 = np.delete(y, 0, axis = 1)

print("Después de borrar la primera columna:")
print(y1)
```

<div class="output stream stdout">

    Después de borrar la primera columna:
    [[2]
     [4]]

</div>

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:245,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162153715,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8jwAm3d7aeMw" outputId="7e246cf4-987d-4b7d-a618-d791286c9d84">

``` python
y2 = np.delete(y, 0, axis = 0)

print("Después de borrar la primera fila:")
print(y2)
```

<div class="output stream stdout">

    Después de borrar la primera fila:
    [[3 4]]

</div>

</div>

<div class="cell markdown" id="lwNXsNsiaq-_">

`np.unique`: Encuentra elementos únicos en un array

</div>

<div class="cell code" execution_count="19" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:361,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162243983,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="-dyNE6efa1Tu" outputId="f41b861c-7145-48cd-d6d4-398e3294917c">

``` python
y = np.array([[9,7,3],[8,3,5],[4,9,9]])

print(y)
```

<div class="output stream stdout">

    [[9 7 3]
     [8 3 5]
     [4 9 9]]

</div>

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:274,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162250446,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ld-A1bq_a4_Y" outputId="ec29d62b-29bd-4daf-ab7e-6bd2bdda3c74">

``` python
print(np.unique(y))
```

<div class="output stream stdout">

    [3 4 5 7 8 9]

</div>

</div>

<div class="cell markdown" id="P0cdVOJ_bOwG">

`np.sort` ordena los elementos dentro de un array

</div>

<div class="cell code" execution_count="21" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:267,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162266470,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="D2Qeyx5ibTeo" outputId="aa449d3e-1248-471c-af8a-0d4b28e88660">

``` python
x = np.array([3,2,1,4])

print(x)
```

<div class="output stream stdout">

    [3 2 1 4]

</div>

</div>

<div class="cell code" execution_count="22" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:278,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162273617,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aFqxmUVgbcWp" outputId="30c0ceb1-278e-4b5c-c82a-6d1e8a5b60cd">

``` python
#Cuando lo usas como función (), el array original no cambia
sort = np.sort(x)
print(sort)
print(x)
```

<div class="output stream stdout">

    [1 2 3 4]
    [3 2 1 4]

</div>

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:362,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162326864,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="TXQEW_UIbj3V" outputId="65f3bde3-ddca-4257-9d18-c84b53cb5dad">

``` python
#Cuando lo usas cómo método, el array original se modifica
x.sort()
print(x)
```

<div class="output stream stdout">

    [1 2 3 4]

</div>

</div>

<div class="cell markdown" id="R6u53Xj8bs-Y">

Ordenar por filas o columnas

</div>

<div class="cell code" execution_count="24" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:306,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162392821,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="eOwhqNQ8bwgc" outputId="a82243cd-d9d3-4fb3-8478-9675129ead90">

``` python
y = np.array([[2,7,3],[8,3,5],[4,0,9]])

print("Array Original:\n", y, "\n")
```

<div class="output stream stdout">

    Array Original:
     [[2 7 3]
     [8 3 5]
     [4 0 9]] 

</div>

</div>

<div class="cell code" execution_count="25" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:263,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162425321,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="K6kFHg9hb2qP" outputId="7345eeb4-5e1a-4414-9dd3-4bd3434185fa">

``` python
# Ordena elementos por filas
y = np.sort(y,axis = 1)
print("Filas Ordenadas:\n", y, "\n")
```

<div class="output stream stdout">

    Filas Ordenadas:
     [[2 3 7]
     [3 5 8]
     [0 4 9]] 

</div>

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:300,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162462929,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="QFoR-AiWb9y8" outputId="a8e8354f-b3cd-4aa0-9c5a-a3e69887d67e">

``` python
# Ordena elementos por columnas
y = np.sort(y,axis = 0)
print("Columnas ordenadas:\n", y, "\n")
```

<div class="output stream stdout">

    Columnas ordenadas:
     [[0 3 7]
     [2 4 8]
     [3 5 9]] 

</div>

</div>

<div class="cell markdown" id="R4q7kbdebs_9">

## **III. Matemáticas II**

Al realizar análisis de datos, a menudo necesitamos encontrar la media, la desviación estándar y los valores mínimos/máximos.

</div>

<div class="cell code" execution_count="27" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:316,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162525108,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ByC87PjHcsaW" outputId="43f5d6ac-848c-4d09-be0c-629a2319a4fe">

``` python
y = np.array([[2,7,3],[8,3,5],[4,0,9]])

print(y)
```

<div class="output stream stdout">

    [[2 7 3]
     [8 3 5]
     [4 0 9]]

</div>

</div>

<div class="cell markdown" id="NVvJUrNwcwHk">

`.mean` Encuentra el promedio de los elementos en un array

</div>

<div class="cell code" id="vYmLm2cpc3KE">

``` python
y.mean()
```

</div>

<div class="cell code" id="x6m99kzBc8Qp">

``` python
#Promedio en base a las filas
y.mean(axis=1)
```

</div>

<div class="cell code" id="C5pnc4A_dEgi">

``` python
#Promeido en base a columnas
y.mean(axis=0)
```

</div>

<div class="cell markdown" id="nxRkf_SLdMrY">

`np.sum` Suma los elementos de una matrix.

</div>

<div class="cell code" id="Ic0U_JeUdTHq">

``` python
y = np.array([[2,7,3],[8,3,5],[4,0,9]])

print(y)
```

</div>

<div class="cell code" id="TMDctRK4dWH3">

``` python
#Suma de todos los elementos
np.sum(y)
```

</div>

<div class="cell code" id="ZG4fF3L2dbDP">

``` python
#Suma por filas
np.sum(y,axis=1)
```

</div>

<div class="cell code" id="Y3E-T9M2djZ2">

``` python
#Suma por columnas
np.sum(y,axis=0)
```

</div>

<div class="cell markdown" id="1ua9Lt3ZdoX3">

`np.std` Encuentra la desviación estándar de todos los elementos en una matrix.

</div>

<div class="cell code" id="2SjI6hqtdvYx">

``` python
y = np.array([[2,7,3],[8,3,5],[4,0,9]])

print(y)
```

</div>

<div class="cell code" id="6Bd7FNiCdxTL">

``` python
np.std(y)
```

</div>

<div class="cell code" id="UatRuEcQdzDf">

``` python
np.std(y,axis=0)
```

</div>

<div class="cell code" id="34gYQFrbd2J3">

``` python
np.std(y,axis=1)
```

</div>

<div class="cell markdown" id="1xJjlswkd5Tc">

`.min` y `.max` encuentran el mínimo y el máximo de una matriz entero

</div>

<div class="cell code" id="sP7RKGVheA1v">

``` python
y = np.array([[2,7,3],[8,3,5],[4,0,9]])

print(y)
```

</div>

<div class="cell code" id="awGsBRyveB1S">

``` python
np.min(y)
```

</div>

<div class="cell code" id="Tb0hmtTReEBo">

``` python
np.min(y,axis=1)
```

</div>

<div class="cell code" id="Hgo8AJL8eGPk">

``` python
np.min(y,axis=0)
```

</div>

<div class="cell code" id="qeV08Dj7eIor">

``` python
np.max(y)
```

</div>

<div class="cell code" id="dyUB1_HHeKjV">

``` python
np.max(y,axis=1)
```

</div>

<div class="cell code" id="DBZ53JaGeMMC">

``` python
np.max(y,axis=0)
```

</div>

<div class="cell markdown" id="4GFucLJweYUX">

## **Análisis de Datos**

</div>

<div class="cell markdown" id="cRQFs8AEefn1">

`np.where` Permite seleccionar elementos desde un array bajo ciertas condiciones. Retorna el indíce de los elementos que encuentra

</div>

<div class="cell code" execution_count="28" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:261,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162586795,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mAm4_WxheN7f" outputId="c94f5903-ca9b-4b52-c37e-24decac22b7a">

``` python
x = np.ones(10)
y = np.arange(10)

print("Array X:\n", x, "\n")
print("Array Y:\n", y, "\n")
```

<div class="output stream stdout">

    Array X:
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.] 

    Array Y:
     [0 1 2 3 4 5 6 7 8 9] 

</div>

</div>

<div class="cell code" execution_count="29" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:297,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162613072,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="05OuOUWYj28t" outputId="e6637217-a170-40a0-e70c-150368a4ce57">

``` python
print("1. Los índices de elementos comunes entre x & y:")
print(np.where(x == y), "\n")
```

<div class="output stream stdout">

    1. Los índices de elementos comunes entre x & y:
    (array([1]),) 

</div>

</div>

<div class="cell code" execution_count="30" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:319,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162651038,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="FeZgWcoQj4HJ" outputId="04aa1501-f6a0-42ee-f838-2c0443cdf2cd">

``` python
print("2. Los índices de los elementos de x que son mayores o iguales a y:")
print(np.where(x >= y), "\n")
```

<div class="output stream stdout">

    2. Los índices de los elementos de x que son mayores o iguales a y:
    (array([0, 1]),) 

</div>

</div>

<div class="cell code" execution_count="31" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:290,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162703734,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="0hxKbCJ7j5Hy" outputId="c489a002-6bae-438c-d81a-e95daacedeca">

``` python
print("3. Los índices de elementos que cumplan:")
print(np.where(2*x < y), "\n")
```

<div class="output stream stdout">

    3. Los índices de elementos que cumplan:
    (array([3, 4, 5, 6, 7, 8, 9]),) 

</div>

</div>

<div class="cell code" execution_count="32" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:312,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162757050,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KPlKRUsNj6GA" outputId="a4f04489-7e97-4962-a467-7b9050bb4b69">

``` python
print("4. Los índices de elementos en y que son mayores a 5:")
print(np.where(y > 5), "\n")
```

<div class="output stream stdout">

    4. Los índices de elementos en y que son mayores a 5:
    (array([6, 7, 8, 9]),) 

</div>

</div>

<div class="cell markdown" id="mjeB9vmqkrwg">

***Boolean indexing*** Los operadores binarios como $`=, <, >`$ pueden ser usado para comparar arrays. Retornan valores booleanos.

</div>

<div class="cell code" execution_count="33" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:1109,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162778219,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8QLAbQolk5zs" outputId="9b63b448-5d3e-4c72-e81d-7955b7b8dcc3">

``` python
x = np.ones(10)
y = np.arange(10)

print("Array A:\n", x, "\n")
print("Array B:\n", y, "\n")
```

<div class="output stream stdout">

    Array A:
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.] 

    Array B:
     [0 1 2 3 4 5 6 7 8 9] 

</div>

</div>

<div class="cell code" execution_count="34" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:1237,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712162782347,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Q7MevowFk8Ed" outputId="15865d48-cc3f-4834-f353-3b0694e88f72">

``` python
print(y > 3, "\n")
```

<div class="output stream stdout">

    [False False False False  True  True  True  True  True  True] 

</div>

</div>
