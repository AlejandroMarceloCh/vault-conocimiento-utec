---
curso: ACD
titulo: U1_L4 Pandas_DataStructures (original)
slides: 0
fuente: U1_L4 Pandas_DataStructures (original).ipynb
---

<div class="cell markdown" id="gIVJoAU9-YNl">

# **Laboratorio 3: Estructuras de Datos en Pandas**

</div>

<div class="cell markdown" id="FL30PHIK-hQa">

Cargamos las librerías:

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:663,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712611282623,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="e-qCQlF5-af1">

``` python
import pandas as pd
import numpy as np
```

</div>

<div class="cell markdown" id="7I8vHbg5-fL6">

## **I. Series**

En Pandas, una ***Serie*** es un array unidimensional de datos indexados.

El constructor de una Serie:

`s = pd.Series(data, index=index)`

donde `data` puede ser:

- Un `ndarray` 1D
- Una lista de Python `list`
- Un diccionario de Python `dict`
- Un valor escalar

</div>

<div class="cell markdown" id="L9gR30bUv9dS">

### Una serie a partir de **un `ndarray` 1D**

</div>

<div class="cell code" execution_count="2" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:302,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712611385656,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="9m4LbrQYwE6Y" outputId="691955a9-4421-45cb-e93f-7327d43b4050">

``` python
array1 = np.arange(1,10,2)
serie = pd.Series(array1)
serie
```

<div class="output execute_result" execution_count="2">

    0    1
    1    3
    2    5
    3    7
    4    9
    dtype: int64

</div>

</div>

<div class="cell markdown" id="6kQ1BJOpw3oI">

Si no se específica los índices, por default serán asignados desde $`0`$ hasta $`n-1`$. En caso se necesite especificar, el código sería:

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:320,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712611480782,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="FlItLPwAxY5q" outputId="d1cbf122-2e95-4d93-afdd-7fce556462e9">

``` python
serie = pd.Series(array1,index=["1st", "2nd", "3rd", "4th", "5th"])
serie
```

<div class="output execute_result" execution_count="3">

    1st    1
    2nd    3
    3rd    5
    4th    7
    5th    9
    dtype: int64

</div>

</div>

<div class="cell markdown" id="WFJI9qsG_aTR">

Como vemos en los ejemplos anteriores, la Serie tiene dos atributos: 1) un array de valores y 2)un array de índices. Sin embargo, solo los valores son de tipo: array NumPy.

Se puede acceder a los atributos de una serie:

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712611579878,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="D9DAijl0_TxF" outputId="787b31a5-a5b4-474b-8cd1-bf8f40eee560">

``` python
serie.values
```

<div class="output execute_result" execution_count="4">

    array([1, 3, 5, 7, 9])

</div>

</div>

<div class="cell markdown" id="F5KsAtN0_sIv">

Los índices también son un objeto parecidos a un array. Son del tipo `pd.Index`

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:290,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712611639753,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="7hO_2ZmbAKJm" outputId="13976f53-f1a6-4b49-d290-c393a76dd201">

``` python
serie.index
```

<div class="output execute_result" execution_count="5">

    Index(['1st', '2nd', '3rd', '4th', '5th'], dtype='object')

</div>

</div>

<div class="cell markdown" id="RUYmoQZVAzm_">

Al igual que con un array NumPy, el índice asociado puede acceder a los datos a través de la conocida notación de corchetes de Python:

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:323,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712611676545,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="0GT_h6vXyh2U" outputId="74ebee90-d786-4fe0-f850-9712517dc22e">

``` python
serie
```

<div class="output execute_result" execution_count="6">

    1st    1
    2nd    3
    3rd    5
    4th    7
    5th    9
    dtype: int64

</div>

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:293,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712611687750,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Zs1Biu1hyo9_" outputId="e6685987-8834-4917-a095-4ed34ced8097">

``` python
serie["2nd"]
```

<div class="output execute_result" execution_count="7">

    3

</div>

</div>

<div class="cell markdown" id="zIJW8uCRyzHs">

Para los índices se puede utilizar la etiqueta o la posición.

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:281,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712611727679,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="cMG6Mk05A3gQ" outputId="4ece5f9c-2c9c-44ad-d2e6-6ac0d0c93d31">

``` python
serie[1]
```

<div class="output execute_result" execution_count="8">

    3

</div>

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:353,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712611831979,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="3qzJUbPoA5aW" outputId="2857b708-5f77-4844-9c54-4dbc8320097b">

``` python
serie[1:3]
```

<div class="output execute_result" execution_count="9">

    2nd    3
    3rd    5
    dtype: int64

</div>

</div>

<div class="cell markdown" id="HdA8zqnABzjg">

La diferencia entre *un array Numpy* de una dimensión y *Series* es la presencia del índice:

- Mientras que el array NumPy tiene **un índice entero** definido implícitamente que se usa para acceder a los valores
- Series tiene **un índice definido explícitamente** asociado con los valores. Donde no necesariamente tiene que ser entero

</div>

<div class="cell markdown" id="SRWNoRuALXau">

Incluso los índices no necesitan ser consecutivos

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:320,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612007771,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="nb_dYzXmLVwM" outputId="ddd1998a-ad9b-464c-ea3a-65867d2d7eb5">

``` python
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                index=[2, 5, 3, 7])
data
```

<div class="output execute_result" execution_count="10">

    2    0.25
    5    0.50
    3    0.75
    7    1.00
    dtype: float64

</div>

</div>

<div class="cell code" execution_count="11" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:305,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612065685,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="zA3Yr2gsLffZ" outputId="34ca9f93-4ecc-43bb-b64e-263b53fe72d6">

``` python
data[3]
```

<div class="output execute_result" execution_count="11">

    0.75

</div>

</div>

<div class="cell markdown" id="UhJ4xY-bzeqt">

### Una serie a partir de **una lista**

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:296,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612188606,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="o5eQY7wy-U9f" outputId="9976e7df-115d-4082-92ad-81ae36dc2b9b">

``` python
#Una serie puede ser creada a partir de una lista
serie = pd.Series([0.25, 0.5, 0.75, 1.0])
serie
```

<div class="output execute_result" execution_count="12">

    0    0.25
    1    0.50
    2    0.75
    3    1.00
    dtype: float64

</div>

</div>

<div class="cell markdown" id="Yq6jp0hZLrY0">

### Una serie a partir de **un diccionario**

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:261,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612232457,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="jV_TdPIiMuU4" outputId="f7764367-41b1-4c68-f406-73f9cbcd8c1f">

``` python
#Creamos un diccionario
population_dict = {'California': 38332521,
                  'Texas': 26448193,
                  'New York': 19651127,
                  'Florida': 19552860,
                  'Illinois': 12882135}
#Creamos una Serie en base al diccionario
population = pd.Series(population_dict)
population
```

<div class="output execute_result" execution_count="13">

    California    38332521
    Texas         26448193
    New York      19651127
    Florida       19552860
    Illinois      12882135
    dtype: int64

</div>

</div>

<div class="cell markdown" id="S-GraX7G0DIG">

Podemos acceder a través de la etiqueta (index):

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:269,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612260190,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="VOE_4Q0NNr-l" outputId="e9cd415d-cf23-40d1-f05f-5b45b0ec0875">

``` python
population['Texas']
```

<div class="output execute_result" execution_count="14">

    26448193

</div>

</div>

<div class="cell markdown" id="z5bv4wdYN0rm">

Sin embargo, a diferencia de un diccionario, la serie también admite operaciones de un array como por ejemplo *slicing*.

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:293,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612329006,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="K0RiECGINziM" outputId="82bf15f7-feb1-4600-fe0d-15b186ff56b2">

``` python
population['Texas':'Florida']
```

<div class="output execute_result" execution_count="15">

    Texas       26448193
    New York    19651127
    Florida     19552860
    dtype: int64

</div>

</div>

<div class="cell code" execution_count="16" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:327,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612369072,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8lFdbqne1UOz" outputId="30939415-3805-49f8-c30d-188081a9d98f">

``` python
population[["Texas", "Florida", "Illinois"]]
```

<div class="output execute_result" execution_count="16">

    Texas       26448193
    Florida     19552860
    Illinois    12882135
    dtype: int64

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:315,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612388381,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2N3o_v8JDUTE" outputId="dde96748-723b-4c41-977e-9835dba2b263">

``` python
population[1]
```

<div class="output execute_result" execution_count="17">

    26448193

</div>

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:294,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612410021,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="YCAYUkGi1qKR" outputId="45d7de11-b3b0-4e2c-a826-1a30d85ea0c7">

``` python
population
```

<div class="output execute_result" execution_count="18">

    California    38332521
    Texas         26448193
    New York      19651127
    Florida       19552860
    Illinois      12882135
    dtype: int64

</div>

</div>

<div class="cell code" execution_count="19" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:296,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612437218,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="7A8TFNlI1xMX" outputId="6059989a-1cef-404f-865b-d05250cedd67">

``` python
population[population > 20000000]
```

<div class="output execute_result" execution_count="19">

    California    38332521
    Texas         26448193
    dtype: int64

</div>

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:314,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612594450,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="3vr8EqYvqkeB" outputId="c9e62c38-10ae-4473-bb32-72825d50f05f">

``` python
ma_15=population[population > 15000000 ]
final=ma_15[ma_15<20000000]
final
```

<div class="output execute_result" execution_count="20">

    New York    19651127
    Florida     19552860
    dtype: int64

</div>

</div>

<div class="cell code" execution_count="21" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:287,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612640708,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RqizKWsmqvzn" outputId="db3e1875-1e90-4623-be7f-b24a0c246bbd">

``` python
population[(population < 20000000) & (population > 15000000)]
```

<div class="output execute_result" execution_count="21">

    New York    19651127
    Florida     19552860
    dtype: int64

</div>

</div>

<div class="cell markdown" id="xY82K9s10SDN">

### Una serie a partir de **un escalar**

</div>

<div class="cell code" execution_count="22" executionInfo="{&quot;elapsed&quot;:423,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612681760,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="bnrN0KKIOv55">

``` python
#Cuando los datos es un escalar y debe estar ubicado en índices específicos
serie = pd.Series(5, index=[100, 200, 300])
```

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:363,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612683869,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="J5QFzLN1Dia8" outputId="3a939a91-090d-4333-e4a3-1c160f001f88">

``` python
serie
```

<div class="output execute_result" execution_count="23">

    100    5
    200    5
    300    5
    dtype: int64

</div>

</div>

<div class="cell markdown" id="roVc1BgQPtd5">

## **II. DataFrame**

Si una Serie es análoga a un array unidimensional con índices flexibles, un DataFrame es análoga a un array bidimensional con índices de fila flexibles y nombres de columna flexibles.

</div>

<div class="cell markdown" id="4yZ7zv3_5YDt">

El constructor de un DataFrame:

`df = pd.DataFrame(data, index=index, columns=columns)`

Un DataFrame es la estructura de datos más utilizada en Pandas. El constructor de la clase `DataFrame()` acepta muchos tipos diferentes de argumentos:

- Un ndarray bidimensional
- Un diccionario de diccionarios
- Una lista de diccionarios
- Un diccionario de series

</div>

<div class="cell markdown" id="R4pGiKvl6TPB">

### Un dataframe a partir de un **ndarray bidimensional**

</div>

<div class="cell code" execution_count="24" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:273,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712612880556,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aeilharD6gcC" outputId="8b6f6ffd-78e1-4f5c-8a6b-861742420d58">

``` python
array = np.array([[25,85],[28,90],[18,98],[45,70]])
array
```

<div class="output execute_result" execution_count="24">

    array([[25, 85],
           [28, 90],
           [18, 98],
           [45, 70]])

</div>

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613038671,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="7lxJBYfS61gr" outputId="d473c69c-00cf-4bfe-ed40-9e7705c89775">

``` python
df = pd.DataFrame(array,index=["Jose", "Maria", "Juan", "Rosa"], columns=["Edad", "Puntaje"])
df
```

<div class="output execute_result" execution_count="26">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 4,\n  \"fields\": [\n    {\n      \"column\": \"Edad\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 11,\n        \"min\": 18,\n        \"max\": 45,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          28,\n          45,\n          25\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Puntaje\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 11,\n        \"min\": 70,\n        \"max\": 98,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          90,\n          70,\n          85\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell markdown" id="hWIVyovC7Mif">

Se puede acceder a los tres elementos de un dataframe de manera individual:

</div>

<div class="cell code" execution_count="27" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:404,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613093879,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="SzlPqtM77QCP" outputId="7be2cb1d-ba1e-4bdf-dd14-12d78ce8b3f9">

``` python
df.values
```

<div class="output execute_result" execution_count="27">

    array([[25, 85],
           [28, 90],
           [18, 98],
           [45, 70]])

</div>

</div>

<div class="cell code" execution_count="28" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:306,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613109708,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="q0k1tB0a7Tfp" outputId="08f916d2-1b53-4bdf-873b-d50a5b57f2d8">

``` python
df.index
```

<div class="output execute_result" execution_count="28">

    Index(['Jose', 'Maria', 'Juan', 'Rosa'], dtype='object')

</div>

</div>

<div class="cell code" execution_count="29" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:324,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613164571,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="5GTQ42nc7VQS" outputId="39ce4a6a-6499-4af3-e4c6-b6f30c7ea05e">

``` python
df.columns
```

<div class="output execute_result" execution_count="29">

    Index(['Edad', 'Puntaje'], dtype='object')

</div>

</div>

<div class="cell markdown" id="80EQkZrb7Zav">

### Un dataframe a partir de un **diccionario de diccionarios**

</div>

<div class="cell code" execution_count="30" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613193972,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Hd7OSB737owl" outputId="d455c5e0-fd4f-4ece-d332-8ed421140e80">

``` python
my_dict = {
    "nombre" : {"J":"Jose", "M":"Maria", "Ju":"Juan", "R":"Rosa"},
    "edad": {"J":25, "M":28, "Ju":18, "R":45},
    "puntaje": {"J":85, "M":90, "Ju":98, "R":70}
}
my_dict
```

<div class="output execute_result" execution_count="30">

    {'nombre': {'J': 'Jose', 'M': 'Maria', 'Ju': 'Juan', 'R': 'Rosa'},
     'edad': {'J': 25, 'M': 28, 'Ju': 18, 'R': 45},
     'puntaje': {'J': 85, 'M': 90, 'Ju': 98, 'R': 70}}

</div>

</div>

<div class="cell code" execution_count="31" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}" executionInfo="{&quot;elapsed&quot;:286,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613197623,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="XWLzsWfs9GIy" outputId="9d3de678-a3ef-4bb0-f382-3a4698406c37">

``` python
df = pd.DataFrame(my_dict)
df
```

<div class="output execute_result" execution_count="31">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 4,\n  \"fields\": [\n    {\n      \"column\": \"nombre\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"Maria\",\n          \"Rosa\",\n          \"Jose\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"edad\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 11,\n        \"min\": 18,\n        \"max\": 45,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          28,\n          45,\n          25\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"puntaje\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 11,\n        \"min\": 70,\n        \"max\": 98,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          90,\n          70,\n          85\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell markdown" id="4N2SyWRW9a0S">

### Un dataframe a partir de una **lista de diccionarios**

</div>

<div class="cell code" execution_count="32" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:312,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613332706,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="-dKiH7ftSaWk" outputId="aaa8bb8b-fc48-4008-ab68-c7ac8871182e">

``` python
#Construcción a partir de una lista de diccionarios
data = [{'a': i, 'b': 2 * i} for i in range(3)]
pd.DataFrame(data)
```

<div class="output execute_result" execution_count="32">

``` json
{"summary":"{\n  \"name\": \"pd\",\n  \"rows\": 3,\n  \"fields\": [\n    {\n      \"column\": \"a\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 0,\n        \"max\": 2,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          0,\n          1,\n          2\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"b\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2,\n        \"min\": 0,\n        \"max\": 4,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          0,\n          2,\n          4\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>

<div class="cell markdown" id="B3Zog5LJ-HeI">

También se puede crear un DataFrame en base a dos series (previamente diccionarios)

</div>

<div class="cell code" execution_count="33" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:733,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613506544,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="BJTpuiEs-M1y" outputId="c6691d63-a45c-4c3b-b99d-9a76bbf7bbac">

``` python
#Primera Serie
population
```

<div class="output execute_result" execution_count="33">

    California    38332521
    Texas         26448193
    New York      19651127
    Florida       19552860
    Illinois      12882135
    dtype: int64

</div>

</div>

<div class="cell code" execution_count="34" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:322,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613513724,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="wWS1HjbaPvlu" outputId="f13aa70e-bb49-46ae-fea5-574b2c13428a">

``` python
#Segunda Serie
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
            'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
area
```

<div class="output execute_result" execution_count="34">

    California    423967
    Texas         695662
    New York      141297
    Florida       170312
    Illinois      149995
    dtype: int64

</div>

</div>

<div class="cell code" execution_count="35" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:286,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613536356,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mJPbNUqnPlHe" outputId="66c59379-eb9b-4147-f262-3f88dde98652">

``` python
#Construimos un DataFrame en base a dos Series (previamentes diccionarios)
states = pd.DataFrame({'population': population,
                        'area': area})
states
```

<div class="output execute_result" execution_count="35">

``` json
{"summary":"{\n  \"name\": \"states\",\n  \"rows\": 5,\n  \"fields\": [\n    {\n      \"column\": \"population\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 9640385,\n        \"min\": 12882135,\n        \"max\": 38332521,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          26448193,\n          12882135,\n          19651127\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"area\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 242437,\n        \"min\": 141297,\n        \"max\": 695662,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          695662,\n          149995,\n          141297\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"states"}
```

</div>

</div>

<div class="cell markdown" id="TRl4YukIW-6q">

## **III. Index**

Es una estructura interesante en sí misma y se puede considerar como *un array inmutable* o como un conjunto ordenado (técnicamente, un conjunto múltiple, ya que los objetos Index pueden contener valores repetidos).

</div>

<div class="cell code" execution_count="36" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:307,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613654250,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="bZW7g25HXDJj" outputId="69ccedbe-4cc5-42e4-ca4a-519ec8c6e288">

``` python
ind = pd.Index([2, 3, 5, 7, 11])
ind
```

<div class="output execute_result" execution_count="36">

    Index([2, 3, 5, 7, 11], dtype='int64')

</div>

</div>

<div class="cell markdown" id="rrLhTT9uYDXc">

El objeto Index en muchos sentidos funciona como un array. Por ejemplo, podemos usar la notación de indexación estándar de Python para recuperar valores o slices:

</div>

<div class="cell code" execution_count="37" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:290,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613672635,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4fAvfwMCYIHF" outputId="5ea04477-068b-449e-f2bc-b997e1e1c9e4">

``` python
ind[2]
```

<div class="output execute_result" execution_count="37">

    5

</div>

</div>

<div class="cell code" execution_count="38" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:288,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613677316,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Q4JMD2XCYKPg" outputId="a9725012-7f8a-4dfa-dba3-7ee321e0eed1">

``` python
ind[::2]
```

<div class="output execute_result" execution_count="38">

    Index([2, 5, 11], dtype='int64')

</div>

</div>

<div class="cell markdown" id="SUE9vR3TYRDc">

El objeto Index también tiene atributos similarea a los arrays en NumPy

</div>

<div class="cell code" execution_count="39" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:288,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613708470,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="a5GixJj0YWRz" outputId="0d36a6db-d06a-4f31-a8a0-0fa1013960e6">

``` python
print(ind.size, ind.shape, ind.ndim, ind.dtype)
```

<div class="output stream stdout">

    5 (5,) 1 int64

</div>

</div>

<div class="cell markdown" id="H6OhmEBVYr4V">

Una diferencia entre los objetos Index y los arrays en NumPy es que **los índices son inmutables**, es decir, no se pueden modificar por los medios normales.

</div>

<div class="cell code" execution_count="40" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:269}" executionInfo="{&quot;elapsed&quot;:16,&quot;status&quot;:&quot;error&quot;,&quot;timestamp&quot;:1712613756657,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="i3FlI9GXYwGq" outputId="108c839d-00f3-4a0e-ec3e-a5dd6134488f">

``` python
ind[1] = 0
```

<div class="output error" ename="TypeError" evalue="Index does not support mutable operations">

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-40-906a9fa1424c> in <cell line: 1>()
    ----> 1 ind[1] = 0

    /usr/local/lib/python3.10/dist-packages/pandas/core/indexes/base.py in __setitem__(self, key, value)
       5155     @final
       5156     def __setitem__(self, key, value):
    -> 5157         raise TypeError("Index does not support mutable operations")
       5158 
       5159     def __getitem__(self, key):

    TypeError: Index does not support mutable operations

</div>

</div>

<div class="cell markdown" id="Kv1RfJ4bY2Ft">

El objeto Index también puede ser visto como un conjunto ordenado. Por lo tanto soporta operaciones de conjunto

</div>

<div class="cell code" execution_count="41" executionInfo="{&quot;elapsed&quot;:322,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613783645,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="t4wWB-kWYyOH">

``` python
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
```

</div>

<div class="cell code" execution_count="42" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:267,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613785680,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="UJY6noRrZErC" outputId="243a7606-41db-4e48-9e36-e4f2eb933895">

``` python
#Intersección
indA.intersection(indB)
```

<div class="output execute_result" execution_count="42">

    Index([3, 5, 7], dtype='int64')

</div>

</div>

<div class="cell code" execution_count="43" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712613788145,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="5DrJ6G6YZOGN" outputId="2971c041-5284-42b9-d979-b2bedafa6973">

``` python
#Unión
indA.union(indB)
```

<div class="output execute_result" execution_count="43">

    Index([1, 2, 3, 5, 7, 9, 11], dtype='int64')

</div>

</div>

<div class="cell markdown" id="sTi7XqxcZaSo">

## **Tu Turno**

![image.png](data:image/png;base64,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)

</div>

<div class="cell markdown" id="mUEv8qt6COXj">

1.  Crea una serie de Pandas con los siguientes datos: \[10, 20, 30, 40, 50\] y etiquetas \['A', 'B', 'C', 'D', 'E'\].

2.  Crea un DataFrame de Pandas con los siguientes datos:\
    Nombre Edad Ciudad\
    0 Ana 25 Madrid\
    1 Juan 30 Barcelona\
    2 María 35 Valencia\
    3 Pedro 40 Sevilla

3.  Crea una serie de Pandas con los siguientes datos: \[100, 200, 300, 400, 500\] y los índices \['A', 'B', 'C', 'D', 'E'\].

4.  Crea un DataFrame con los siguientes datos y configura la columna 'ID' como index:\
    Name Age Gender\
    ID\
    101 Alice 25 Female\
    102 Bob 30 Male\
    103 Charlie 35 Male\
    104 David 40 Male

5.  Crea una serie de Pandas con fechas como índice y números aleatorios como valores, que cubra un rango de 10 días a partir del '2022-01-01'.

6.  Crea una serie de Pandas con los datos {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5} y cambia el nombre del índice a {'AA', 'BB' , 'CC', 'DD', 'EE'}.

7.  Crea una serie de Pandas con los siguientes datos: \[15, 25, 35, 45, 55\] y etiquetas \['X', 'Y', 'Z', 'W', 'V'\].

8.  Crea un DataFrame de Pandas con los siguientes datos:\
    Producto Precio Stock\
    0 Laptop 1200 15\
    1 Mouse 25 100\
    2 Teclado 50 75\
    3 Monitor 300 90

9.  Crea una serie de Pandas con los siguientes datos: \[150, 250, 350, 450, 550\] y los índices \['P', 'Q', 'R', 'S', 'T'\].

10. Crea un DataFrame con los siguientes datos y configura la columna 'ID' como index:\
    Nombre Edad Ciudad\
    DNI\
    45145 Luis 28 Lima\
    67890 Carla 35 Arequipa\
    24680 José 40 Trujillo

11. Crea una serie de Pandas con fechas como índice y números aleatorios como valores, que cubra un rango de 15 días a partir del '2023-05-01'.

12. Crea una serie de Pandas con los datos {'G': 10, 'H': 20, 'I': 30, 'J': 40, 'K': 50} y cambia el nombre del índice a {'GG', 'HH' , 'II', 'JJ'}.

</div>
