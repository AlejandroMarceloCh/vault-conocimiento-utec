---
curso: ACD
titulo: U1_L8 Similitud y Disimilitud de Datos
slides: 0
fuente: U1_L8 Similitud y Disimilitud de Datos.ipynb
---

<div class="cell markdown" id="VJ3fDhYerjgV">

\#**Laboratorio 8: Similitud y Disimilitud de Datos**

**Objetivo de la Sesión:** Comprender qué técnicas o herramientas existen para determinar la similitud y disimilitud de los datos.

</div>

<div class="cell code" execution_count="2" id="cwM8d8p0mgvd">

``` python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
```

</div>

<div class="cell markdown" id="U2_yDc3eryS4">

## **Ejercicio 0:** Cargar el dataset

Para este laboratorio usaremos el dataset **Titanic** de la librería Seaborn. Recuerde que el dataframe es **la matriz de datos.**

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:444}" executionInfo="{&quot;elapsed&quot;:385,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533289518,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="WdCS671vnv8m" outputId="ed790606-845a-4644-c286-ddba693abb3b">

``` python
df = sns.load_dataset('titanic')
df
```

<div class="output execute_result" execution_count="4">

         survived  pclass     sex   age  sibsp  parch     fare embarked   class  \
    0           0       3    male  22.0      1      0   7.2500        S   Third   
    1           1       1  female  38.0      1      0  71.2833        C   First   
    2           1       3  female  26.0      0      0   7.9250        S   Third   
    3           1       1  female  35.0      1      0  53.1000        S   First   
    4           0       3    male  35.0      0      0   8.0500        S   Third   
    ..        ...     ...     ...   ...    ...    ...      ...      ...     ...   
    886         0       2    male  27.0      0      0  13.0000        S  Second   
    887         1       1  female  19.0      0      0  30.0000        S   First   
    888         0       3  female   NaN      1      2  23.4500        S   Third   
    889         1       1    male  26.0      0      0  30.0000        C   First   
    890         0       3    male  32.0      0      0   7.7500        Q   Third   

           who  adult_male deck  embark_town alive  alone  
    0      man        True  NaN  Southampton    no  False  
    1    woman       False    C    Cherbourg   yes  False  
    2    woman       False  NaN  Southampton   yes   True  
    3    woman       False    C  Southampton   yes  False  
    4      man        True  NaN  Southampton    no   True  
    ..     ...         ...  ...          ...   ...    ...  
    886    man        True  NaN  Southampton    no   True  
    887  woman       False    B  Southampton   yes   True  
    888  woman       False  NaN  Southampton    no  False  
    889    man        True    C    Cherbourg   yes   True  
    890    man        True  NaN   Queenstown    no   True  

    [891 rows x 15 columns]

</div>

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:262,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694125921944,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="yAzzxojlMHCp" outputId="74269f85-4538-4099-84ea-7f59b9940140">

``` python
df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 15 columns):
     #   Column       Non-Null Count  Dtype   
    ---  ------       --------------  -----   
     0   survived     891 non-null    int64   
     1   pclass       891 non-null    int64   
     2   sex          891 non-null    object  
     3   age          714 non-null    float64 
     4   sibsp        891 non-null    int64   
     5   parch        891 non-null    int64   
     6   fare         891 non-null    float64 
     7   embarked     889 non-null    object  
     8   class        891 non-null    category
     9   who          891 non-null    object  
     10  adult_male   891 non-null    bool    
     11  deck         203 non-null    category
     12  embark_town  889 non-null    object  
     13  alive        891 non-null    object  
     14  alone        891 non-null    bool    
    dtypes: bool(2), category(2), float64(2), int64(4), object(5)
    memory usage: 80.7+ KB

</div>

</div>

<div class="cell markdown" id="Y-EecuwG0R_o">

## **Ejercicio 1:** Sub DataFrame

Para nuestro análisis de similitud y disimilitud consideremos una muestra aleatoria sin la presencia de valores `NaN`.

1.  Cree un subdataframe `dfSample` que sea una muestra (2%) del dataset original.
2.  Eliminar las columnas con valores `NaN`
3.  Resetee los indexes
4.  Elimine la columna `index` producto del paso anterior

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:634}" executionInfo="{&quot;elapsed&quot;:241,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533293620,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2GlpamKi4Lbu" outputId="bebdfe42-7b90-41c6-fbc5-b0bf246ab2a3">

``` python
dfSample = df.sample(frac=0.02, random_state=1)
dfSample
```

<div class="output execute_result" execution_count="7">

         survived  pclass     sex   age  sibsp  parch     fare embarked   class  \
    862         1       1  female  48.0      0      0  25.9292        S   First   
    223         0       3    male   NaN      0      0   7.8958        S   Third   
    84          1       2  female  17.0      0      0  10.5000        S  Second   
    680         0       3  female   NaN      0      0   8.1375        Q   Third   
    535         1       2  female   7.0      0      2  26.2500        S  Second   
    623         0       3    male  21.0      0      0   7.8542        S   Third   
    148         0       2    male  36.5      0      2  26.0000        S  Second   
    3           1       1  female  35.0      1      0  53.1000        S   First   
    34          0       1    male  28.0      1      0  82.1708        C   First   
    241         1       3  female   NaN      1      0  15.5000        Q   Third   
    794         0       3    male  25.0      0      0   7.8958        S   Third   
    2           1       3  female  26.0      0      0   7.9250        S   Third   
    6           0       1    male  54.0      0      0  51.8625        S   First   
    17          1       2    male   NaN      0      0  13.0000        S  Second   
    368         1       3  female   NaN      0      0   7.7500        Q   Third   
    430         1       1    male  28.0      0      0  26.5500        S   First   
    819         0       3    male  10.0      3      2  27.9000        S   Third   
    743         0       3    male  24.0      1      0  16.1000        S   Third   

           who  adult_male deck  embark_town alive  alone  
    862  woman       False    D  Southampton   yes   True  
    223    man        True  NaN  Southampton    no   True  
    84   woman       False  NaN  Southampton   yes   True  
    680  woman       False  NaN   Queenstown    no   True  
    535  child       False  NaN  Southampton   yes  False  
    623    man        True  NaN  Southampton    no   True  
    148    man        True    F  Southampton    no  False  
    3    woman       False    C  Southampton   yes  False  
    34     man        True  NaN    Cherbourg    no  False  
    241  woman       False  NaN   Queenstown   yes  False  
    794    man        True  NaN  Southampton    no   True  
    2    woman       False  NaN  Southampton   yes   True  
    6      man        True    E  Southampton    no   True  
    17     man        True  NaN  Southampton   yes   True  
    368  woman       False  NaN   Queenstown   yes   True  
    430    man        True    C  Southampton   yes   True  
    819  child       False  NaN  Southampton    no  False  
    743    man        True  NaN  Southampton    no  False  

</div>

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:226}" executionInfo="{&quot;elapsed&quot;:262,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533296466,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="M-YDhXDUyL9a" outputId="44935749-25bc-47cb-ae23-2035144e2c82">

``` python
dfSample = dfSample.dropna()
dfSample
```

<div class="output execute_result" execution_count="8">

         survived  pclass     sex   age  sibsp  parch     fare embarked   class  \
    862         1       1  female  48.0      0      0  25.9292        S   First   
    148         0       2    male  36.5      0      2  26.0000        S  Second   
    3           1       1  female  35.0      1      0  53.1000        S   First   
    6           0       1    male  54.0      0      0  51.8625        S   First   
    430         1       1    male  28.0      0      0  26.5500        S   First   

           who  adult_male deck  embark_town alive  alone  
    862  woman       False    D  Southampton   yes   True  
    148    man        True    F  Southampton    no  False  
    3    woman       False    C  Southampton   yes  False  
    6      man        True    E  Southampton    no   True  
    430    man        True    C  Southampton   yes   True  

</div>

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:226}" executionInfo="{&quot;elapsed&quot;:256,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533298132,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="VLKV752TCKkE" outputId="3425b732-4051-4be4-a28c-e94306a6fcc4">

``` python
dfSample = dfSample.reset_index()
dfSample
```

<div class="output execute_result" execution_count="9">

       index  survived  pclass     sex   age  sibsp  parch     fare embarked  \
    0    862         1       1  female  48.0      0      0  25.9292        S   
    1    148         0       2    male  36.5      0      2  26.0000        S   
    2      3         1       1  female  35.0      1      0  53.1000        S   
    3      6         0       1    male  54.0      0      0  51.8625        S   
    4    430         1       1    male  28.0      0      0  26.5500        S   

        class    who  adult_male deck  embark_town alive  alone  
    0   First  woman       False    D  Southampton   yes   True  
    1  Second    man        True    F  Southampton    no  False  
    2   First  woman       False    C  Southampton   yes  False  
    3   First    man        True    E  Southampton    no   True  
    4   First    man        True    C  Southampton   yes   True  

</div>

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:226}" executionInfo="{&quot;elapsed&quot;:268,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533299863,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Qoy-N8LwSzk2" outputId="a62eedb1-d1a3-4242-d7fa-63524638595f">

``` python
dfSample = dfSample.drop(columns=['index'])
dfSample
```

<div class="output execute_result" execution_count="10">

       survived  pclass     sex   age  sibsp  parch     fare embarked   class  \
    0         1       1  female  48.0      0      0  25.9292        S   First   
    1         0       2    male  36.5      0      2  26.0000        S  Second   
    2         1       1  female  35.0      1      0  53.1000        S   First   
    3         0       1    male  54.0      0      0  51.8625        S   First   
    4         1       1    male  28.0      0      0  26.5500        S   First   

         who  adult_male deck  embark_town alive  alone  
    0  woman       False    D  Southampton   yes   True  
    1    man        True    F  Southampton    no  False  
    2  woman       False    C  Southampton   yes  False  
    3    man        True    E  Southampton    no   True  
    4    man        True    C  Southampton   yes   True  

</div>

</div>

<div class="cell markdown" id="D5eG7g_kz_XL">

## **Ejercicio 2:** Tipos de Datos

Observe la matriz de datos y determine cuáles son nominales, binarios, numéricos y ordinales.

Renombre las columnas del dataframe `dfSample` como `NombreColumna(t)` donde `t` puede ser:

- `(n)`: nominal no binario
- `(b)`: nominal binario
- `(num)`: numérico
- `(o)`: ordinal

***Por ejemplo:*** la columna `survived` debe ser renombrada como `survived(b)` debido a que es de tipo binario

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:226}" executionInfo="{&quot;elapsed&quot;:271,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533302009,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="6idBJiD8KeZ9" outputId="f5941c3d-ce23-4f40-b485-07969815a015">

``` python
dfSample.rename(columns = {'survived':'survived(b)',
                     'pclass': 'pclass(o)',
                     'sex': 'sex(b)',
                     'age': 'age(num)',
                     'sibsp': 'sibsp(num)',
                     'parch': 'parch(num)',
                     'fare': 'fare(num)',
                     'embarked': 'embarked(n)',
                     'class': 'class(o)',
                     'who': 'who(b)',
                     'adult_male': 'adult_male(b)',
                     'deck': 'deck(n)',
                     'embark_town': 'embark_town(n)',
                     'alive': 'alive(b)',
                     'alone': 'alone(b)'}, inplace = True)
dfSample
```

<div class="output execute_result" execution_count="12">

       survived(b)  pclass(o)  sex(b)  age(num)  sibsp(num)  parch(num)  \
    0            1          1  female      48.0           0           0   
    1            0          2    male      36.5           0           2   
    2            1          1  female      35.0           1           0   
    3            0          1    male      54.0           0           0   
    4            1          1    male      28.0           0           0   

       fare(num) embarked(n) class(o) who(b)  adult_male(b) deck(n)  \
    0    25.9292           S    First  woman          False       D   
    1    26.0000           S   Second    man           True       F   
    2    53.1000           S    First  woman          False       C   
    3    51.8625           S    First    man           True       E   
    4    26.5500           S    First    man           True       C   

      embark_town(n) alive(b)  alone(b)  
    0    Southampton      yes      True  
    1    Southampton       no     False  
    2    Southampton      yes     False  
    3    Southampton       no      True  
    4    Southampton      yes      True  

</div>

</div>

<div class="cell markdown" id="AwVsKK9FOfBO">

## **Ejercicio 3:** SubListas de Columnas

A partir de los nombres de las columnas, construya una variable para cada tipo. Por ejemplo:

`ordinalCols = ['pclass(o)', 'class(o)']`

El resto se deberá nombrar como `nominalCols`, `binarioCols`, `numCols`

*Hint*: Podrian usar listas por comprensión

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141187821,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="lhwLBTamOUwD" outputId="be9c7bc5-dff4-407b-c5cf-700c05c41596">

``` python
dfSample.columns
```

<div class="output execute_result" execution_count="14">

    Index(['survived(b)', 'pclass(o)', 'sex(b)', 'age(num)', 'sibsp(num)',
           'parch(num)', 'fare(num)', 'embarked(n)', 'class(o)', 'who(b)',
           'adult_male(b)', 'deck(n)', 'embark_town(n)', 'alive(b)', 'alone(b)'],
          dtype='object')

</div>

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:237,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533305367,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Yjal8ndBNRwZ" outputId="bea51cdc-43ce-49a8-a43b-039df8d4196f">

``` python
ordinalCols = [i for i in dfSample.columns if '(o)' in i]
ordinalCols
```

<div class="output execute_result" execution_count="15">

    ['pclass(o)', 'class(o)']

</div>

</div>

<div class="cell code" execution_count="16" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533306083,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ACpXlJWBM6ia" outputId="e2eb9b00-772e-450c-f6cc-864b3a09fc7c">

``` python
nominalCols = [i for i in dfSample.columns if '(n)' in i]
nominalCols
```

<div class="output execute_result" execution_count="16">

    ['embarked(n)', 'deck(n)', 'embark_town(n)']

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533306856,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="X2B2HhYZNZXA" outputId="36a1bda4-4bf5-48a8-8246-91d42258a22c">

``` python
binarioCols = [i for i in dfSample.columns if '(b)' in i]
binarioCols
```

<div class="output execute_result" execution_count="17">

    ['survived(b)', 'sex(b)', 'who(b)', 'adult_male(b)', 'alive(b)', 'alone(b)']

</div>

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533307809,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="AXWUjzMDMvjl" outputId="61440c2d-4eca-4665-8fed-dde9e65d5309">

``` python
numCols = [i for i in dfSample.columns if '(num)' in i]
numCols
```

<div class="output execute_result" execution_count="18">

    ['age(num)', 'sibsp(num)', 'parch(num)', 'fare(num)']

</div>

</div>

<div class="cell markdown" id="GajI2SN59ubq">

## **Ejercicio 4:** Crear una matriz de disimilitud

Implemente una función `set_Matriz(n)` donde $`n`$ es el tamaño de la matriz que será llamada `M` como un array bidimensional de $`nxn`$ donde todos sus valores sean zeros.

*Hint:* Recuerde los métodos en NumPy

</div>

<div class="cell code" execution_count="20" id="yv9_-3tX-Yv_">

``` python
def set_Matriz(n):
  return np.zeros((n, n), dtype=float)
```

</div>

<div class="cell code" execution_count="21" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:6,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141195514,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="LMzg_-LNWmYc" outputId="a9254945-2315-4725-9240-9fa67872ea34">

``` python
dM = set_Matriz(9)
dM
```

<div class="output execute_result" execution_count="21">

    array([[0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 0.]])

</div>

</div>

<div class="cell markdown" id="TpbwlEi-_XyW">

## **I. Proximidad para Atributos nominales**

Para calcular la disimilitud de dos objetos $`i`$ y $`j`$ se sigue:

``` math
 d(i,j) =  \frac{p - m}{p}
```

donde $`m`$ es el número de coincidencias (1 si son iguales, 0 en caso contrario) y $`p`$ es el número total de **atributos Nominales** de la matriz de datos.

</div>

<div class="cell markdown" id="499GPql6oKai">

## **Ejercicio 5:**

Calcule la matriz de disimilitud para los **atributos nominales** de la data.<br>

Hints:

- Extraiga en un subdataframe los atributos nominales.
- Cree una función `disimilitudNominal(df)` que reciba el dataframe de atributos nominales y devuelva la matriz de disimilitud `disM`
- Visualice su matriz de dismilitud

</div>

<div class="cell code" execution_count="24" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:313,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141199951,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="9q5ooKt9Peu7" outputId="0efaff1e-8d9e-453d-8d4f-244527ed0dc4">

``` python
nominalCols
```

<div class="output execute_result" execution_count="24">

    ['embarked(n)', 'deck(n)', 'embark_town(n)']

</div>

</div>

<div class="cell code" execution_count="25" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:221,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533313721,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="6JAqz4tEQSS2" outputId="efcf894c-6579-4d6a-ac60-656b8aefe00c">

``` python
dfNominal = dfSample[nominalCols]
dfNominal
```

<div class="output execute_result" execution_count="25">

      embarked(n) deck(n) embark_town(n)
    0           S       D    Southampton
    1           S       F    Southampton
    2           S       C    Southampton
    3           S       E    Southampton
    4           S       C    Southampton

</div>

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:452,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141202706,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Ng5YKGEM0Bq7" outputId="b1d4eff4-88ea-4ab2-f71f-252d38233dbc">

``` python
dfNominal.shape
```

<div class="output execute_result" execution_count="26">

    (5, 3)

</div>

</div>

<div class="cell code" execution_count="27" id="oI8qzyWyo21h">

``` python
#Input: df - El dataframe
def disimilitudNominal(df):
  (n,p) = df.shape
  disM = set_Matriz(n)

  #Calculando m: número de matches de atributos nominales
  for i in range(n):
    for j in range(i):
      if i!=j:
        m = sum(df.iloc[i]==df.iloc[j])
        disM[i,j] = (p-m)/p

  return disM
```

</div>

<div class="cell code" execution_count="28" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:312,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141206797,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="NOuvhj8cwFFC" outputId="b865097b-e72e-43fc-e20e-4c1be642fbfe">

``` python
disMN = disimilitudNominal(dfNominal)
disMN
```

<div class="output execute_result" execution_count="28">

    array([[0.        , 0.        , 0.        , 0.        , 0.        ],
           [0.33333333, 0.        , 0.        , 0.        , 0.        ],
           [0.33333333, 0.33333333, 0.        , 0.        , 0.        ],
           [0.33333333, 0.33333333, 0.33333333, 0.        , 0.        ],
           [0.33333333, 0.33333333, 0.        , 0.33333333, 0.        ]])

</div>

</div>

<div class="cell code" execution_count="29" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:448}" executionInfo="{&quot;elapsed&quot;:1729,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141287019,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_2RATHPUr2lh" outputId="29a4e542-e9d3-4e88-ff92-21e7e3db3d91">

``` python
sns.heatmap(disMN, annot=True)
```

<div class="output execute_result" execution_count="29">

    <Axes: >

</div>

<div class="output display_data">

![](40ed3270dfd19cc535682531aa48797355cfdd2f.png)

</div>

</div>

<div class="cell markdown" id="EyyJnctL0YIp">

## **Ejercicio 6:**

Cree una función `similitudNominal(dM)` que calcule la matriz de similitud para los **atributos nominales**. Recuerde que la similitud se calcula:

``` math
 sim(i,j) = 1 - d(i,j) = \frac{m}{p} 
```

</div>

<div class="cell code" execution_count="31" id="TIFzkIJH1NoG">

``` python
# Input: disM - matriz de disimilitud
def similitudNominal(disM):
  (n,_) = disM.shape
  simM = set_Matriz(n)

  for i in range(n):
    for j in range(i):
      if i!=j:
        simM[i,j] = 1 - disM[i,j]

  return simM
```

</div>

<div class="cell code" execution_count="32" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141356375,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="gchmyafPvuhp" outputId="928143e1-e8c0-44e6-ff1b-0253e32a9325">

``` python
simMN = similitudNominal(disMN)
simMN
```

<div class="output execute_result" execution_count="32">

    array([[0.        , 0.        , 0.        , 0.        , 0.        ],
           [0.66666667, 0.        , 0.        , 0.        , 0.        ],
           [0.66666667, 0.66666667, 0.        , 0.        , 0.        ],
           [0.66666667, 0.66666667, 0.66666667, 0.        , 0.        ],
           [0.66666667, 0.66666667, 1.        , 0.66666667, 0.        ]])

</div>

</div>

<div class="cell markdown" id="6tIRBBgqT5sT">

## **Ejercicio 7:**

A partir de una matriz de **similitud y disimilitud**, implemente:

1.  Una función `getDifferentObjects()` que retorne una lista de data objects que son 100% diferentes.
2.  Una función `getIdenticalObjetcs()` que retorne una lista de data objects iguales.

*Hint:* Utilice la función `np.argwhere(condicion)`. Identifique qué párametros deberían recibir las funciones. Adicionalmente, recuerde las funciones de Pandas vistas en los laboratorios anteriores.

</div>

<div class="cell code" execution_count="34" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:275,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141360660,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="HMkcHMW34MOh" outputId="d4d4eba9-791e-4645-a0e3-fcc49ee21ebc">

``` python
dfNominal
```

<div class="output execute_result" execution_count="34">

      embarked(n) deck(n) embark_town(n)
    0           S       D    Southampton
    1           S       F    Southampton
    2           S       C    Southampton
    3           S       E    Southampton
    4           S       C    Southampton

</div>

</div>

<div class="cell code" execution_count="35" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141364113,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="rhrFVLmx5GS8" outputId="a025b8cf-2a0e-488c-dea5-5033aed7fd00">

``` python
disMN
```

<div class="output execute_result" execution_count="35">

    array([[0.        , 0.        , 0.        , 0.        , 0.        ],
           [0.33333333, 0.        , 0.        , 0.        , 0.        ],
           [0.33333333, 0.33333333, 0.        , 0.        , 0.        ],
           [0.33333333, 0.33333333, 0.33333333, 0.        , 0.        ],
           [0.33333333, 0.33333333, 0.        , 0.33333333, 0.        ]])

</div>

</div>

<div class="cell code" execution_count="36" id="-5g1_a2432fU">

``` python
def getDifferentObjects(disM,df):
  idxArray =  np.argwhere(disM == 1)
  (n,_) = idxArray.shape
  if n== 0:
    print("No existe ningún data object diferente")
  else:
    resA = np.unique(idxArray)
    return df[df.index.isin(resA)]
```

</div>

<div class="cell code" execution_count="37" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:6,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141393857,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="799Q7Glaohq2" outputId="1a7f20fa-3fef-4e05-e969-ba04d3c5b5eb">

``` python
getDifferentObjects(disMN,dfNominal)
```

<div class="output stream stdout">

    No existe ningún data object diferente

</div>

</div>

<div class="cell code" execution_count="38" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:299,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141398053,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="lBXu3DnA7yDM" outputId="b7418fb5-89b6-4ea3-b5fc-67dd12009207">

``` python
simMN
```

<div class="output execute_result" execution_count="38">

    array([[0.        , 0.        , 0.        , 0.        , 0.        ],
           [0.66666667, 0.        , 0.        , 0.        , 0.        ],
           [0.66666667, 0.66666667, 0.        , 0.        , 0.        ],
           [0.66666667, 0.66666667, 0.66666667, 0.        , 0.        ],
           [0.66666667, 0.66666667, 1.        , 0.66666667, 0.        ]])

</div>

</div>

<div class="cell code" execution_count="39" id="o01Ndfa44Cba">

``` python
def getIdenticalObjects(simM,df):
  idxArray =  np.argwhere(simM == 1)
  (n,_) = idxArray.shape
  if n== 0:
    print("No existe ningún data object idéntico")
  else:
    resA = np.unique(idxArray)
    return df[df.index.isin(resA)]

```

</div>

<div class="cell code" execution_count="40" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:112}" executionInfo="{&quot;elapsed&quot;:10,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141405407,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="JFqT59G-4YbQ" outputId="0b6ced29-bd73-46ee-e671-bd74b0d78bb2">

``` python
idemDf = getIdenticalObjects(simMN,dfNominal)
idemDf
```

<div class="output execute_result" execution_count="40">

      embarked(n) deck(n) embark_town(n)
    2           S       C    Southampton
    4           S       C    Southampton

</div>

</div>

<div class="cell markdown" id="sRxR-Ym9PNu7">

## **II. Proximidad para Atributos Binarios**

Sean dos data objects $`i`$ y $`j`$, se define:

- $`q`$: el número de atributos iguales a 1 para ambos objects $`i`$ y $`j`$.
- $`r`$: el número de atributos que son iguales a 1 para el objeto $`i`$ pero 0 para el objeto $`j`$.
- $`s`$: el número de atributos iguales a 0 para el objeto $`i`$ y 1 para el objeto $`j`$.
- $`t`$: el número de atributos que son iguales a 0 para los objetos $`i`$ y $`j`$.
- $`p`$: el número total de **atributos binarios** donde $`p=q+r+s+t`$

</div>

<div class="cell markdown" id="R0nO5IyGPruN">

### **A. Binarios Simétricos**

La disimilitud entre dos data objects ***Binarios Simétricos*** $`i`$ y $`j`$ se calcula:
``` math
 d(i,j) = \frac{r+s}{q+r+s+t} 
```

</div>

<div class="cell markdown" id="SI7-WvcyRQe7">

## **Ejercicio 8:**

Cree una variable `binarioSimetrico` que contenga a las columnas binarias simétricas

</div>

<div class="cell code" execution_count="44" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:226}" executionInfo="{&quot;elapsed&quot;:319,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141413861,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="oamOKHDxQ0Md" outputId="d55e654b-1dcd-4742-98c9-9e236e85608f">

``` python
dfSample
```

<div class="output execute_result" execution_count="44">

       survived(b)  pclass(o)  sex(b)  age(num)  sibsp(num)  parch(num)  \
    0            1          1  female      48.0           0           0   
    1            0          2    male      36.5           0           2   
    2            1          1  female      35.0           1           0   
    3            0          1    male      54.0           0           0   
    4            1          1    male      28.0           0           0   

       fare(num) embarked(n) class(o) who(b)  adult_male(b) deck(n)  \
    0    25.9292           S    First  woman          False       D   
    1    26.0000           S   Second    man           True       F   
    2    53.1000           S    First  woman          False       C   
    3    51.8625           S    First    man           True       E   
    4    26.5500           S    First    man           True       C   

      embark_town(n) alive(b)  alone(b)  
    0    Southampton      yes      True  
    1    Southampton       no     False  
    2    Southampton      yes     False  
    3    Southampton       no      True  
    4    Southampton      yes      True  

</div>

</div>

<div class="cell code" execution_count="45" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:5,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141415919,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="DyYk_dfqQo2p" outputId="9995442c-f97c-4381-d047-2ca999caa32a">

``` python
binarioCols
```

<div class="output execute_result" execution_count="45">

    ['survived(b)', 'sex(b)', 'who(b)', 'adult_male(b)', 'alive(b)', 'alone(b)']

</div>

</div>

<div class="cell code" execution_count="46" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:225,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533338801,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8mtx_z2xRV0i" outputId="202f2dc0-f777-4d33-f973-38ebee7f5446">

``` python
binarioSimetricoCols = ['sex(b)','who(b)']
binarioSimetricoCols
```

<div class="output execute_result" execution_count="46">

    ['sex(b)', 'who(b)']

</div>

</div>

<div class="cell markdown" id="ARx0mjUTQMWL">

## **Ejercicio 9:**

Implemente una función `dBin` que calcule la disimilitud binaria simétrica para dos objetos $`i`$ y $`j`$.

Hints:

- Extraiga en un subdataframe los atributos binarios simétricos.

</div>

<div class="cell code" execution_count="48" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:216,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533341325,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="xxWxI9KgQwiG" outputId="b566fc20-e712-48d2-d789-dbe96b26dbb7">

``` python
dfBinSimetrico = dfSample[binarioSimetricoCols]
dfBinSimetrico
```

<div class="output execute_result" execution_count="48">

       sex(b) who(b)
    0  female  woman
    1    male    man
    2  female  woman
    3    male    man
    4    male    man

</div>

</div>

<div class="cell code" execution_count="49" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:6,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141422422,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="72tN4P3wSkDm" outputId="79a7c231-1373-4c0b-ef90-488382274c56">

``` python
dfBinSimetrico.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Data columns (total 2 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   sex(b)  5 non-null      object
     1   who(b)  5 non-null      object
    dtypes: object(2)
    memory usage: 212.0+ bytes

</div>

</div>

<div class="cell code" execution_count="50" id="5IVAEa68SpMA">

``` python
dfBinariosSim_bool = dfBinSimetrico.copy()
dfBinariosSim_bool['sex(b)'] = dfBinariosSim_bool['sex(b)'].replace({"female": True, "male": False})
dfBinariosSim_bool['who(b)'] = dfBinariosSim_bool['who(b)'].replace({"woman": True, "man": False})
```

<div class="output stream stderr">

    C:\Users\jespinozame\AppData\Local\Temp\ipykernel_70612\633483803.py:2: FutureWarning: Downcasting behavior in `replace` is deprecated and will be removed in a future version. To retain the old behavior, explicitly call `result.infer_objects(copy=False)`. To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`
      dfBinariosSim_bool['sex(b)'] = dfBinariosSim_bool['sex(b)'].replace({"female": True, "male": False})
    C:\Users\jespinozame\AppData\Local\Temp\ipykernel_70612\633483803.py:3: FutureWarning: Downcasting behavior in `replace` is deprecated and will be removed in a future version. To retain the old behavior, explicitly call `result.infer_objects(copy=False)`. To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`
      dfBinariosSim_bool['who(b)'] = dfBinariosSim_bool['who(b)'].replace({"woman": True, "man": False})

</div>

</div>

<div class="cell code" execution_count="51" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:316,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141426902,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="WRtKik43TpkD" outputId="0a8826e9-5579-4fbf-b2dc-ccd3a8bb093a">

``` python
dfBinariosSim_bool
```

<div class="output execute_result" execution_count="51">

       sex(b)  who(b)
    0    True    True
    1   False   False
    2    True    True
    3   False   False
    4   False   False

</div>

</div>

<div class="cell code" execution_count="52" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:406,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141428827,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="nML7IAP0TrgV" outputId="372cc8db-4596-48fe-d329-4e8262291019">

``` python
dfBinariosSim_bool.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Data columns (total 2 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   sex(b)  5 non-null      bool 
     1   who(b)  5 non-null      bool 
    dtypes: bool(2)
    memory usage: 142.0 bytes

</div>

</div>

<div class="cell code" execution_count="53" id="0DLYJbUJUl_H">

``` python
def disBinSimetrico(i,j,df):

  q = len([col for col in df.columns if df.iloc[i][col] == df.iloc[j][col] == True])
  r = len([col for col in df.columns if df.iloc[i][col] == True and df.iloc[j][col] == False])
  s = len([col for col in df.columns if df.iloc[i][col] == False and df.iloc[j][col] == True])
  t = len([col for col in df.columns if df.iloc[i][col] == False and df.iloc[j][col] == False])

  d = (r+s)/(q+r+s+t)
  return (q,r,s,t,d)
```

</div>

<div class="cell code" execution_count="54" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:305,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141433922,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="OupYf9PcU100" outputId="b6934676-c724-4366-e85e-c7bfc7133261">

``` python
disBinSimetrico(0,1,dfBinariosSim_bool)
```

<div class="output execute_result" execution_count="54">

    (0, 2, 0, 0, 1.0)

</div>

</div>

<div class="cell markdown" id="tSqDoqVnx-tl">

## **Ejercicio 10:**

Calcule la matriz de disimilitud para los **atributos binarios simétricos** de la data.<br>

Hints:

- Cree una función `disimilitudBinarioSimetrico(df)` que reciba el dataframe de atributos binarios y devuelva la matriz de disimilitud `disM`
- Use la función del ejercicio anterior
- Visualice su matriz de disimilitud

</div>

<div class="cell code" execution_count="56">

``` python
def disBinSimetrico2(i,j,df):

  q = len([col for col in df.columns if df.iloc[i][col] == df.iloc[j][col] == True])
  r = len([col for col in df.columns if df.iloc[i][col] == True and df.iloc[j][col] == False])
  s = len([col for col in df.columns if df.iloc[i][col] == False and df.iloc[j][col] == True])
  t = len([col for col in df.columns if df.iloc[i][col] == False and df.iloc[j][col] == False])

  d = (r+s)/(q+r+s+t)
  return d
```

</div>

<div class="cell code" execution_count="57" id="6IKeIw4aVKxQ">

``` python
def disimilitudBinarioSimetrico(df):
  (n,_) = df.shape
  disM = set_Matriz(n)

  for i in range(n):
    for j in range(i):
      disM[i,j] = disBinSimetrico2(i,j,df)

  return disM
```

</div>

<div class="cell code" execution_count="58" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:275,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141452799,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="sztaHxhyWSHi" outputId="a0c153f9-d2ce-40b3-a947-b2c3b2f74e81">

``` python
disBSM = disimilitudBinarioSimetrico(dfBinariosSim_bool)
disBSM
```

<div class="output execute_result" execution_count="58">

    array([[0., 0., 0., 0., 0.],
           [1., 0., 0., 0., 0.],
           [0., 1., 0., 0., 0.],
           [1., 0., 1., 0., 0.],
           [1., 0., 1., 0., 0.]])

</div>

</div>

<div class="cell code" execution_count="59" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:453}" executionInfo="{&quot;elapsed&quot;:942,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694141607912,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="1KC-OcgOWzzO" outputId="47a060a1-9c20-4dde-d18b-422ae8398854">

``` python
sns.heatmap(disBSM, annot = True)
```

<div class="output execute_result" execution_count="59">

    <Axes: >

</div>

<div class="output display_data">

![](36b509a387bf76162145c951b38727c12d13c9c0.png)

</div>

</div>

<div class="cell markdown" id="p6v-DramXBXa">

### **B. Binarios Asimétricos**

La disimilitud entre dos data objects ***Binarios Asimétricos*** $`i`$ y $`j`$ se calcula:
``` math
 d(i,j) = \frac{r+s}{q+r+s} 
```

</div>

<div class="cell markdown" id="Bj0H0SyexxaH">

## **Ejercicio 11:**

Calcule la matriz de disimilitud para los **atributos binarios asimétricos** de la data.<br>

Hints:

- Cree una función `disimilitudBinarioAsimetrico(df)` que reciba el dataframe de atributos binarios y devuelva la matriz de disimilitud.
- Visualice su matriz de disimilitud

</div>

<div class="cell code" execution_count="62" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:378,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694142843112,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="e7ODcNOhxw1Y" outputId="d5d73752-67b2-4e8a-ffae-8b5c7e9882db">

``` python
binarioCols
```

<div class="output execute_result" execution_count="62">

    ['survived(b)', 'sex(b)', 'who(b)', 'adult_male(b)', 'alive(b)', 'alone(b)']

</div>

</div>

<div class="cell code" execution_count="63" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:206,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533361707,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="jctrbMcztTs_" outputId="e03d3243-413f-4ee9-c255-815d74e0072d">

``` python
binarioAsimetricoCols = ['survived(b)','adult_male(b)', 'alive(b)', 'alone(b)']
binarioAsimetricoCols
```

<div class="output execute_result" execution_count="63">

    ['survived(b)', 'adult_male(b)', 'alive(b)', 'alone(b)']

</div>

</div>

<div class="cell code" execution_count="64" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533362876,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="lKBkyRKkypmX" outputId="ae2c487c-5483-4196-95e2-d9a8ed13614d">

``` python
dfBinAsimetrico = dfSample[binarioAsimetricoCols]
dfBinAsimetrico
```

<div class="output execute_result" execution_count="64">

       survived(b)  adult_male(b) alive(b)  alone(b)
    0            1          False      yes      True
    1            0           True       no     False
    2            1          False      yes     False
    3            0           True       no      True
    4            1           True      yes      True

</div>

</div>

<div class="cell code" execution_count="65" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694143143464,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ATZf9jKjzL3Y" outputId="f84c64a1-6929-40f2-a1cf-2ac541d31c5e">

``` python
dfBinAsimetrico.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Data columns (total 4 columns):
     #   Column         Non-Null Count  Dtype 
    ---  ------         --------------  ----- 
     0   survived(b)    5 non-null      int64 
     1   adult_male(b)  5 non-null      bool  
     2   alive(b)       5 non-null      object
     3   alone(b)       5 non-null      bool  
    dtypes: bool(2), int64(1), object(1)
    memory usage: 222.0+ bytes

</div>

</div>

<div class="cell code" execution_count="66" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:210,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533365616,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RSujK3tIzPah" outputId="32aaf52f-4621-446a-a4e6-7e4bc385f61c">

``` python
dfBinariosAsim_bool = dfBinAsimetrico.copy()
dfBinariosAsim_bool['survived(b)'] = dfBinariosAsim_bool['survived(b)'].replace({1: True, 0: False})
dfBinariosAsim_bool['alive(b)'] = dfBinariosAsim_bool['alive(b)'].replace({"yes": True, "no": False})
dfBinariosAsim_bool
```

<div class="output stream stderr">

    C:\Users\jespinozame\AppData\Local\Temp\ipykernel_70612\1257835014.py:2: FutureWarning: Downcasting behavior in `replace` is deprecated and will be removed in a future version. To retain the old behavior, explicitly call `result.infer_objects(copy=False)`. To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`
      dfBinariosAsim_bool['survived(b)'] = dfBinariosAsim_bool['survived(b)'].replace({1: True, 0: False})
    C:\Users\jespinozame\AppData\Local\Temp\ipykernel_70612\1257835014.py:3: FutureWarning: Downcasting behavior in `replace` is deprecated and will be removed in a future version. To retain the old behavior, explicitly call `result.infer_objects(copy=False)`. To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`
      dfBinariosAsim_bool['alive(b)'] = dfBinariosAsim_bool['alive(b)'].replace({"yes": True, "no": False})

</div>

<div class="output execute_result" execution_count="66">

       survived(b)  adult_male(b)  alive(b)  alone(b)
    0         True          False      True      True
    1        False           True     False     False
    2         True          False      True     False
    3        False           True     False      True
    4         True           True      True      True

</div>

</div>

<div class="cell code" execution_count="67" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:7,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694143246457,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="iA6ysvfwzjqI" outputId="d2c826c0-775c-4c22-802d-3c7e6d0c0ad8">

``` python
dfBinariosAsim_bool.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Data columns (total 4 columns):
     #   Column         Non-Null Count  Dtype
    ---  ------         --------------  -----
     0   survived(b)    5 non-null      bool 
     1   adult_male(b)  5 non-null      bool 
     2   alive(b)       5 non-null      bool 
     3   alone(b)       5 non-null      bool 
    dtypes: bool(4)
    memory usage: 152.0 bytes

</div>

</div>

<div class="cell code" execution_count="68" id="QJudEQLtyeqL">

``` python
def disBinAsimetrico(i,j,df):

  q = len([col for col in df.columns if df.iloc[i][col] == df.iloc[j][col] == True])
  r = len([col for col in df.columns if df.iloc[i][col] == True and df.iloc[j][col] == False])
  s = len([col for col in df.columns if df.iloc[i][col] == False and df.iloc[j][col] == True])

  d = (r+s)/(q+r+s)
  return d
```

</div>

<div class="cell code" execution_count="69" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:202,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533370047,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aeOgU5gYynrD" outputId="81c8edf4-12d6-404f-bf6e-a3a5d573fef2">

``` python
disBinAsimetrico(0,1,dfBinariosAsim_bool)
```

<div class="output execute_result" execution_count="69">

    1.0

</div>

</div>

<div class="cell code" execution_count="70" id="GNEbUU0KyWZC">

``` python
def disimilitudBinarioAsimetrico(df):
  (n,_) = df.shape
  disM = set_Matriz(n)

  for i in range(n):
    for j in range(i):
      disM[i,j] = disBinAsimetrico(i,j,df)

  return disM
```

</div>

<div class="cell code" execution_count="71" id="7cha5FYxzuOJ">

``` python
disBAsimM = disimilitudBinarioAsimetrico(dfBinariosAsim_bool)
```

</div>

<div class="cell code" execution_count="72" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:453}" executionInfo="{&quot;elapsed&quot;:464,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694143328610,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="95dpf1ZBz3dl" outputId="0b58ecb3-0cb1-49f0-9863-beaa42893481">

``` python
sns.heatmap(disBAsimM, annot=True)
```

<div class="output execute_result" execution_count="72">

    <Axes: >

</div>

<div class="output display_data">

![](17ff4c560f85f97ecea058274285463ec82be3e1.png)

</div>

</div>

<div class="cell markdown" id="kWLsQNFZ0DFA">

=======

</div>

<div class="cell markdown" id="B3OZO8BEik3V">

## **III. Proximidad para Atributos Númericos**

Para medir la disimilitud entre atributos numéricos se utilizan las distancias ***Euclideana***, Manhattan y Minkowski.

En este laboratorio utilizaremos la distancia Euclideana se calcula:

Sean dos objects $`i= (x_{i1} , x_{i2} , …, x_{ip} )`$ y $`j= (x_{j1} , x_{j2} , …, x_{jp})`$ descritos por $`p`$ atributos. La distancia Euclideana entre los objects $`i`$ y $`j`$ es definida como:
``` math
 d(i,j) = \sqrt{ (x_{i1}-x_{j1})^2 + (x_{i2}-x_{j2})^2 + \ldots + (x_{ip}-x_{jp})^2 }
```

</div>

<div class="cell markdown" id="bfL0q_vzjzg8">

## **Ejercicio 12:**

Calcule la matriz de disimilitud para los **atributos numéricos** de la data.<br>

Hints:

- Cree una función `disimilitudNumerico(df)` que reciba el dataframe de atributos numéricos y devuelva la matriz de disimilitud.

</div>

<div class="cell code" execution_count="76" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:216,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694460511924,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_ZMIUJoIj-C4" outputId="f7f8b008-beb2-449f-b82a-5696698dbbe4">

``` python
numCols
```

<div class="output execute_result" execution_count="76">

    ['age(num)', 'sibsp(num)', 'parch(num)', 'fare(num)']

</div>

</div>

<div class="cell code" execution_count="77" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:227,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694460514785,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="F25qhNYPkHJv" outputId="71a5e83d-6d6b-4b47-cfe8-4aa4d7089ca5">

``` python
dfNum = dfSample[numCols]
dfNum
```

<div class="output execute_result" execution_count="77">

       age(num)  sibsp(num)  parch(num)  fare(num)
    0      48.0           0           0    25.9292
    1      36.5           0           2    26.0000
    2      35.0           1           0    53.1000
    3      54.0           0           0    51.8625
    4      28.0           0           0    26.5500

</div>

</div>

<div class="cell code" execution_count="78" id="wEpXW4P-sMEH">

``` python
import math
```

</div>

<div class="cell code" execution_count="79" id="8q5jWeOYkfWO">

``` python
def disimilitudNumerico(df):
  (n,p) = df.shape
  disM = set_Matriz(n)

  for i in range(n):
    for j in range(i):
        sum = 0
        for k in range(p):
          sum = sum + pow((df.iloc[i][k] - df.iloc[j][k]),2)
        disM[i,j] = math.sqrt(sum)

  return disM
```

</div>

<div class="cell code" execution_count="80" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:216,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694460398215,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="38wct2EVk1BJ" outputId="372f6ddc-7554-4219-a66f-104c2b18336d">

``` python
disM = disimilitudNumerico(dfNum)
disM
```

<div class="output stream stderr">

    C:\Users\jespinozame\AppData\Local\Temp\ipykernel_70612\2271620387.py:9: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
      sum = sum + pow((df.iloc[i][k] - df.iloc[j][k]),2)

</div>

<div class="output execute_result" execution_count="80">

    array([[ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ],
           [11.67283225,  0.        ,  0.        ,  0.        ,  0.        ],
           [30.1372257 , 27.23343533,  0.        ,  0.        ,  0.        ],
           [26.61834046, 31.29087577, 19.06649958,  0.        ,  0.        ],
           [20.0096325 ,  8.74942855, 27.47548908, 36.28667326,  0.        ]])

</div>

</div>

<div class="cell markdown" id="MhDSuOeTXvrx">

## **IV. Proximidad para Atributos Ordinales**

Suponga que $`f`$ es un atributo ordinal que describe $`n`$ objects. La disimilitud con respecto al atributo involucra los siguientes pasos:

1.  Determinar el número de estados posibles $`M`$ de un atributo ordinal $`f`$. Se denota como $`M_f`$. Por ejemplo, el atributo `class(o)` cuenta con 3 posibles estados (First, Second, Third). Por lo tanto $`M_f = 3`$.
2.  Reemplazar cada valor del atributo ordinal por su rank (numérico). Por ejemplo: First = 1, Second = 2 y Third = 3. De tal manera que el rankeo es $`r_{if} = \{1, \ldots, M_f\} = \{1, 2, 3\}`$
3.  Dado que cada atributo ordinal puede tener diferentes estados, se debe mapear el rango a cada atributo entre $`[0.0,1.0]`$ tal que cada atributo tiene el mismo peso. Se normaliza de la siguiente manera:

``` math
 z_{if} = \frac{r_{if}-1}{M_f -1}
```

</div>

<div class="cell markdown" id="WO0pnaC86FnD">

## **Ejercicio 13:**

Calcule la matriz de disimilitud para los **atributos ordinales** de la data.<br>

Hints:

- Cree una función `disimilitudOrdinales(df)` que reciba el dataframe de atributos ordinales y devuelva la matriz de disimilitud.

</div>

<div class="cell code" execution_count="83" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:221,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694460607850,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="dFi9ImMK2kOP" outputId="47aa913a-5e2a-4b80-efa5-13a98ddc1875">

``` python
ordinalCols
```

<div class="output execute_result" execution_count="83">

    ['pclass(o)', 'class(o)']

</div>

</div>

<div class="cell code" execution_count="84" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:225,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533387222,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="y_ddCdmS6H4Z" outputId="fa5d12a0-e043-42e0-b3db-87d4cc88d0af">

``` python
df_Ordinales = dfSample[ordinalCols]
df_Ordinales
```

<div class="output execute_result" execution_count="84">

       pclass(o) class(o)
    0          1    First
    1          2   Second
    2          1    First
    3          1    First
    4          1    First

</div>

</div>

<div class="cell code" execution_count="85" id="BmquJ79vEevP">

``` python
def disimilitudOrdinales(df):
  (n,_) = df.shape
  disM = set_Matriz(n)

  dfNorm = pd.DataFrame(columns = df.columns)
  dfNorm = df.copy()

  #Para cada atributo
  for column in df.columns:
    #Paso 1: establecer los estados
    M = df[column].unique()

    #Paso 2: asignar su rank
    RankList = list(enumerate(M,start=1))

    #Paso 3: normalizar
    NormalizeDict = {}
    for (i,value) in RankList:
      z = (i-1)/(len(M)-1)
      #NormalizeList.append((value,z))
      NormalizeDict[value] = z

    #Set the dfNorm
    dfNorm=dfNorm.replace({column: NormalizeDict})

  #Calcular la proximidad numérica
  disM = disimilitudNumerico(dfNorm)
  return disM
```

</div>

<div class="cell code" execution_count="86" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:199,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694533391942,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ZRD0vRWJFemt" outputId="06e24e39-7966-4d88-a538-a752cd9c0d9d">

``` python
disM = disimilitudOrdinales(df_Ordinales)
disM
```

<div class="output stream stderr">

    C:\Users\jespinozame\AppData\Local\Temp\ipykernel_70612\3680630790.py:24: FutureWarning: The behavior of Series.replace (and DataFrame.replace) with CategoricalDtype is deprecated. In a future version, replace will only be used for cases that preserve the categories. To change the categories, use ser.cat.rename_categories instead.
      dfNorm=dfNorm.replace({column: NormalizeDict})
    C:\Users\jespinozame\AppData\Local\Temp\ipykernel_70612\2271620387.py:9: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
      sum = sum + pow((df.iloc[i][k] - df.iloc[j][k]),2)

</div>

<div class="output execute_result" execution_count="86">

    array([[0.        , 0.        , 0.        , 0.        , 0.        ],
           [1.41421356, 0.        , 0.        , 0.        , 0.        ],
           [0.        , 1.41421356, 0.        , 0.        , 0.        ],
           [0.        , 1.41421356, 0.        , 0.        , 0.        ],
           [0.        , 1.41421356, 0.        , 0.        , 0.        ]])

</div>

</div>

<div class="cell code" execution_count="87" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:293,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694472403775,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pwEovuGdbOZd" outputId="dfe1d366-939d-4915-8361-2c5e74348d7f">

``` python
df_Ordinales
```

<div class="output execute_result" execution_count="87">

       pclass(o) class(o)
    0          1    First
    1          2   Second
    2          1    First
    3          1    First
    4          1    First

</div>

</div>

<div class="cell markdown" id="xUuoMoeK9-eD">

## **V. Proximidad para Atributos Mixtos**

Supongamos que el conjunto de datos contiene $`p`$ atributos de tipo mixto. La disimilitud $`d(i, j)`$ entre los objetos $`i`$ y $`j`$ se define como:

``` math
 d(i,j) = \frac{\sum_{f=1}^{p}\delta_{ij}^{(f)}d_{ij}^{(f)}}{\sum_{f=1}^{p}\delta_{ij}^{(f)}} 
```

donde:

- $`\delta_{ij}^{(f)} = 0`$ si $`x_{if}`$ o $`x_{jf}`$ no existe o si $`x_{if} = x_{jf} = 0`$ y el atributo $`f`$ es binario asimétrico.
- $`\delta_{ij}^{(f)} = 1`$, en caso contrario.

La contribución del atributo $`f`$ para la disimilitud entre $`i`$ y $`j`$ ($`d_{ij}^{(f)}`$) es calculado dependiendo su tipo:

- Si $`f`$ es numérico:
  ``` math
   d_{ij}^{(f)} = \frac{|x_{if} - x_{jf}|}{max_h x_{hf} - min_h x_{hf}} 
  ```
  donde $`h`$ es para todo object del atributo $`f`$.
- Si $`f`$ es nominal o binario:
  ``` math
   d_{ij}^{(f)} = 0 \text{ si } x_{if} = x_{jf}; \text{ en caso contrario } d_{ij}^{(f)} = 1
  ```
- Si $`f`$ es ordinal: Calcula los ranks $`r_{if}`$ y $`z_{if} = \frac{r_{if}-1}{M_f -1}`$ y trata a $`z_{if}`$ como numérico.

</div>

<div class="cell markdown" id="7PviwbWtIB-o">

Por ejemplo, recordando nuestro ejemplo en los slides:

``` math
 d(2,1) = \frac{\delta_{21}^{(Nom)}d_{21}^{(Nom)} + \delta_{21}^{(Ord)}d_{21}^{(Ord)} + \delta_{21}^{(Num)}d_{21}^{(Num)}}{ \delta_{21}^{(Nom)} + \delta_{21}^{(Ord)} + \delta_{21}^{(Num)}}
```
``` math
 d(2,1) = \frac{(1)(1) + (1)(1) + (1)(\frac{|45-22|}{64-22})}{ 1 + 1 + 1}
```
``` math
 d(2,1) = \frac{1 + 1 + 0.55 }{3} = 0.85
```

</div>

<div class="cell markdown" id="NmRsLarGL3na">

## **Ejercicio 14:**

Calcule la matriz de disimilitud para los **todos los atributos** de la data.<br>

Hints:

- Cree una función `disimilitudMixto(df)` que reciba el dataframe de atributos y devuelva la matriz de disimilitud.

</div>

<div class="cell code" execution_count="91" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:226}" executionInfo="{&quot;elapsed&quot;:213,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694537590867,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="luametmdT5IZ" outputId="5a228a32-e4e0-4655-ac96-f4229c2853a4">

``` python
dfSample
```

<div class="output execute_result" execution_count="91">

       survived(b)  pclass(o)  sex(b)  age(num)  sibsp(num)  parch(num)  \
    0            1          1  female      48.0           0           0   
    1            0          2    male      36.5           0           2   
    2            1          1  female      35.0           1           0   
    3            0          1    male      54.0           0           0   
    4            1          1    male      28.0           0           0   

       fare(num) embarked(n) class(o) who(b)  adult_male(b) deck(n)  \
    0    25.9292           S    First  woman          False       D   
    1    26.0000           S   Second    man           True       F   
    2    53.1000           S    First  woman          False       C   
    3    51.8625           S    First    man           True       E   
    4    26.5500           S    First    man           True       C   

      embark_town(n) alive(b)  alone(b)  
    0    Southampton      yes      True  
    1    Southampton       no     False  
    2    Southampton      yes     False  
    3    Southampton       no      True  
    4    Southampton      yes      True  

</div>

</div>

<div class="cell code" execution_count="92" id="0xSXp7-tT61m">

``` python
dfSample.rename(columns={'survived(b)':'survived(ba)',
                         'adult_male(b)': 'adult_male(ba)',
                         'alive(b)': 'alive(ba)',
                         'alone(b)': 'alone(ba)',
                         'sex(b)': 'sex(bs)',
                         'who(b)': 'who(bs)'}, inplace=True)
```

</div>

<div class="cell code" execution_count="93" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:226}" executionInfo="{&quot;elapsed&quot;:225,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694537918525,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="7Nl6JlaQVJh0" outputId="5de75fe9-eb74-4382-acb3-8d84b7c90b4a">

``` python
dfSample
```

<div class="output execute_result" execution_count="93">

       survived(ba)  pclass(o) sex(bs)  age(num)  sibsp(num)  parch(num)  \
    0             1          1  female      48.0           0           0   
    1             0          2    male      36.5           0           2   
    2             1          1  female      35.0           1           0   
    3             0          1    male      54.0           0           0   
    4             1          1    male      28.0           0           0   

       fare(num) embarked(n) class(o) who(bs)  adult_male(ba) deck(n)  \
    0    25.9292           S    First   woman           False       D   
    1    26.0000           S   Second     man            True       F   
    2    53.1000           S    First   woman           False       C   
    3    51.8625           S    First     man            True       E   
    4    26.5500           S    First     man            True       C   

      embark_town(n) alive(ba)  alone(ba)  
    0    Southampton       yes       True  
    1    Southampton        no      False  
    2    Southampton       yes      False  
    3    Southampton        no       True  
    4    Southampton       yes       True  

</div>

</div>

<div class="cell code" execution_count="94" id="WGMDkuo_N5vs">

``` python
from sqlalchemy import Null
def productSum(col,i,j,df):

  #Reconer el tipo de la columna
  f = ""
  if '(o)' in col:
    f = "Ordinal"
  elif '(n)' in col:
    f = "Nominal"
  elif '(bs)' in col:
    f = "BinarioSimetrico"
  elif '(ba)' in col:
    f = "BinarioAsimetrico"
  elif '(num)' in col:
    f = "Numerico"
  else:
      print("No se encuentra el tipo")
      return

  #Calcular delta
  delta= 0
  if f != "BinarioAsimetrico" or df.iloc[i][j] != Null:
    delta = 1

  #Calcular d
  d = 0
  if f == "Numerico":
    d = (abs(df.iloc[i][col] - df.iloc[j][col]))/(df[col].max() - df[col].min())
  elif f == "Nominal" or f=="BinarioSimetrico" or f=="BinarioAsimetrico":
    if df.iloc[i][col] != df.iloc[j][col]:
      d = 1
  elif f == "Ordinal":
    rank_mapping = {val: k for k, val in enumerate(df[col].sort_values().unique())}
    mapped_i = rank_mapping[df.iloc[i][col]]
    mapped_j = rank_mapping[df.iloc[j][col]] 
    a = abs((mapped_i - mapped_j) / (len(rank_mapping) - 1))
    b = (max(rank_mapping.values()) - min(rank_mapping.values())) / (len(rank_mapping) - 1)
    d = a / b

  return(delta,d)
```

</div>

<div class="cell code" execution_count="99" id="JNpnvA_nHbtH">

``` python
def disimilitudMixto(df):

  #Calcular los tipos de columnas
  ordinalCols = [col for col in df.columns if '(o)' in col]
  nominalCols = [col for col in df.columns if '(n)' in col]
  binarioCols = [col for col in df.columns if '(b)' in col]
  numCols = [col for col in df.columns if '(num)' in col]

  #Set up
  (n,p) = df.shape
  disM = set_Matriz(n)

  for i in range(n):
    for j in range(i):
      sum_denominador = 0
      sum_numerador = 0
      for f in df.columns:
        (delta,d) = productSum(f,i,j,df)
        sum_numerador = sum_numerador + (delta*d)
        sum_denominador = sum_denominador + delta

      #Calcular d(i,j)
      disM[i][j] = sum_numerador / sum_denominador

  return disM
```

</div>

<div class="cell code" execution_count="100">

``` python
dfSample
```

<div class="output execute_result" execution_count="100">

       survived(ba)  pclass(o) sex(bs)  age(num)  sibsp(num)  parch(num)  \
    0             1          1  female      48.0           0           0   
    1             0          2    male      36.5           0           2   
    2             1          1  female      35.0           1           0   
    3             0          1    male      54.0           0           0   
    4             1          1    male      28.0           0           0   

       fare(num) embarked(n) class(o) who(bs)  adult_male(ba) deck(n)  \
    0    25.9292           S    First   woman           False       D   
    1    26.0000           S   Second     man            True       F   
    2    53.1000           S    First   woman           False       C   
    3    51.8625           S    First     man            True       E   
    4    26.5500           S    First     man            True       C   

      embark_town(n) alive(ba)  alone(ba)  
    0    Southampton       yes       True  
    1    Southampton        no      False  
    2    Southampton       yes      False  
    3    Southampton        no       True  
    4    Southampton       yes       True  

</div>

</div>

<div class="cell code" execution_count="101" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:308,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1694538285419,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="NebbSBGmMPjv" outputId="b3c435a1-52c4-488f-d440-91c6c1238e63">

``` python
disM = disimilitudMixto(dfSample)
disM
```

<div class="output stream stderr">

    C:\Users\jespinozame\AppData\Local\Temp\ipykernel_70612\862420579.py:22: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
      if f != "BinarioAsimetrico" or df.iloc[i][j] != Null:

</div>

<div class="output execute_result" execution_count="101">

    array([[0.        , 0.        , 0.        , 0.        , 0.        ],
           [0.69632756, 0.        , 0.        , 0.        , 0.        ],
           [0.3       , 0.73700577, 0.        , 0.        , 0.        ],
           [0.47901493, 0.44166173, 0.58508763, 0.        , 0.        ],
           [0.31947192, 0.48981103, 0.41642551, 0.32877378, 0.        ]])

</div>

</div>

<div class="cell code">

``` python
```

</div>
