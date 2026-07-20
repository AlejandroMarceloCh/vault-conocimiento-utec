---
curso: ACD
titulo: U3_L3 DCNivel3_MissingValues1
slides: 0
fuente: U3_L3 DCNivel3_MissingValues1.ipynb
---

<div class="cell markdown" id="SPNbTWcJGPOj">

# **U3_L3 Data Cleaning Nivel III: Valores Faltantes - Detección**

</div>

<div class="cell markdown" id="nQMyjijVIKqG">

## **Objetivo:**

Al finalizar el laboratorio, el estudiante será capaz de detectar la presencia de valores faltantes en una dataset usando funciones de Pandas. Además, identificará el tipo de valor faltante si existiera.

</div>

<div class="cell markdown" id="pxqLXjNyHYhV">

## **Recordemos**

1.  **Missing Completely at Random (MCAR):** Los valores faltantes son completamente aleatorios y no dependen de ninguna variable observada o no observada en el dataset.
2.  **Missing at Random (MAR):** Los valores faltantes dependen de alguna variable observada, pero no de la variable con el valor faltante en sí.
3.  **Missing Not at Random (MNAR):** Los valores faltantes dependen de la variable con el valor faltante en sí.

</div>

<div class="cell code" execution_count="2" executionInfo="{&quot;elapsed&quot;:1763,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717456512878,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="sOU5mRXgOvkZ">

``` python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

</div>

<div class="cell markdown" id="aIM-mAfxMfHS">

## **I. Identificar Valores Faltantes**

Pandas ofrece varias funciones para detectar la presencia de valores faltantes un dataset:

- `isna()` y `isnull()`: Estas funciones devuelven un DataFrame del mismo tamaño (shape) que el original, donde cada elemento es un valor booleano que responde a la pregunta si es un valor faltante (True) o no (False).
- `notna()` y `notnull()`: Estas funciones devuelven lo opuesto a `isna()` y `isnull()`.
- `info()`: este método proporciona un resumen conciso del DataFrame, incluido el recuento de valores no nulos para cada columna. Al comparar este recuento con el número total de filas, puede identificar rápidamente las columnas con valores faltantes.

</div>

<div class="cell markdown" id="UHPu6q95PbgY">

### **Ejemplo 1:**

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:294,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717386822567,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="9fA5mlV9F7dE" outputId="cc8dff96-27f3-4003-9fc4-c66189a45ca4">

``` python
data = pd.Series([1, np.nan, 'hello', None])
data
```

<div class="output execute_result" execution_count="3">

    0        1
    1      NaN
    2    hello
    3     None
    dtype: object

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717386837361,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mxWH1KlrO1Lv" outputId="fa8dd03c-47ad-492d-fe8e-829dc7779627">

``` python
data.isnull()
```

<div class="output execute_result" execution_count="4">

    0    False
    1     True
    2    False
    3     True
    dtype: bool

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:336,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717386858142,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="R8VdQXzyO7XU" outputId="dda4bd4f-ea8b-4d98-94ef-2cc0db155d2f">

``` python
data.isna()
```

<div class="output execute_result" execution_count="5">

    0    False
    1     True
    2    False
    3     True
    dtype: bool

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:310,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717386946615,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="1D2Quj1ZPQ7y" outputId="f94cf258-da91-40ca-95e3-ffa58c51c81c">

``` python
data.notna()
```

<div class="output execute_result" execution_count="6">

    0     True
    1    False
    2     True
    3    False
    dtype: bool

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:273,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717386956280,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="lScu_puaPTi9" outputId="66774ff8-f4e7-42af-f0fa-f99262fa1110">

``` python
data.info()
```

<div class="output stream stdout">

    <class 'pandas.core.series.Series'>
    RangeIndex: 4 entries, 0 to 3
    Series name: None
    Non-Null Count  Dtype 
    --------------  ----- 
    2 non-null      object
    dtypes: object(1)
    memory usage: 160.0+ bytes

</div>

</div>

<div class="cell markdown" id="Ufse0y27Ph5O">

### **Ejemplo 2:**

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}" executionInfo="{&quot;elapsed&quot;:20,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717387046449,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="yfgZhwGVPg_p" outputId="5c641765-3ca5-4eba-b2bd-fb323d74fb24">

``` python
df = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],[np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
df
```

<div class="output execute_result" execution_count="8">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 4,\n  \"fields\": [\n    {\n      \"column\": 0,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.0,\n        \"min\": 1.0,\n        \"max\": 1.0,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          1.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 1,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.0,\n        \"min\": 6.5,\n        \"max\": 6.5,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          6.5\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 2,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.0,\n        \"min\": 3.0,\n        \"max\": 3.0,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          3.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}" executionInfo="{&quot;elapsed&quot;:264,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717387061275,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="wSer8iXhPr1t" outputId="4bf788a4-957e-489a-fc27-ad0c53d056bf">

``` python
df.isnull()
```

<div class="output execute_result" execution_count="9">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 4,\n  \"fields\": [\n    {\n      \"column\": 0,\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          true,\n          false\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 1,\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          true,\n          false\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 2,\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          true,\n          false\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}" executionInfo="{&quot;elapsed&quot;:267,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717387070573,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ued4iPDaPvo6" outputId="2825eb82-40d5-40e5-a33a-0bf28773c9fc">

``` python
df.notnull()
```

<div class="output execute_result" execution_count="10">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 4,\n  \"fields\": [\n    {\n      \"column\": 0,\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          false,\n          true\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 1,\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          false,\n          true\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 2,\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          false,\n          true\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:299,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717387082183,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="naAAWhyIPxOv" outputId="9961d495-4e5b-4892-94f9-b8db0650a607">

``` python
df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4 entries, 0 to 3
    Data columns (total 3 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   0       2 non-null      float64
     1   1       2 non-null      float64
     2   2       2 non-null      float64
    dtypes: float64(3)
    memory usage: 224.0 bytes

</div>

</div>

<div class="cell markdown" id="L4q-2LkVQL7Z">

## **II. Tipos de Valores Faltantes**

**Contexto:**

Para esta sección utilizaremos el dataset `Airdata.csv` que contiene un conjunto de datos sobre **la calidad del aire** recogidos a partir de tres sensores ubicados en tres ubicaciones A, B y C durante al año 2020. El dataset tiene datos generales por cada día del año como: el timestamp, la temperatura, humedad, la velocidad y dirección del viento. En cuanto a los sensores, los datos son acerca de el dióxido de nitrógeno (NO2) que es un contaminante atmosférico.

</div>

<div class="cell markdown" id="Md7aJlynQwz1">

### **Ejercicio 1:**

Cargar el dataset `Airdata.csv`y construya una función `print_MVs(df)` que imprima el número de valores faltantes existentes por cada columna en el dataframe `df`.

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:462,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717456519733,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="xn_FQSoqRd86" outputId="1c9dac15-1a37-4d66-c69e-1586a542417f">

``` python
df = pd.read_csv("Airdata.csv")
df.head()
```

<div class="output execute_result" execution_count="3">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 8784,\n  \"fields\": [\n    {\n      \"column\": \"DateTime\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 8784,\n        \"samples\": [\n          \"9/23/2020 1:00\",\n          \"3/3/2020 0:00\",\n          \"9/29/2020 11:00\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Temperature\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7.363943394853997,\n        \"min\": -2.7894714,\n        \"max\": 33.87053,\n        \"num_unique_values\": 2810,\n        \"samples\": [\n          15.310529,\n          32.68053,\n          26.06053\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Humidity\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 14,\n        \"min\": 20,\n        \"max\": 98,\n        \"num_unique_values\": 79,\n        \"samples\": [\n          95,\n          87,\n          75\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Wind_Speed\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 8.443103411224255,\n        \"min\": 0.0,\n        \"max\": 65.44677,\n        \"num_unique_values\": 1774,\n        \"samples\": [\n          17.174677,\n          23.241617,\n          10.446206\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Wind_Direction\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 91.96162685537111,\n        \"min\": 1.2188721,\n        \"max\": 360.0,\n        \"num_unique_values\": 3072,\n        \"samples\": [\n          113.35556,\n          91.08092,\n          267.63376\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NO2_Location_A\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15.597173171007618,\n        \"min\": -0.46,\n        \"max\": 116.6,\n        \"num_unique_values\": 2807,\n        \"samples\": [\n          42.22,\n          50.03,\n          38.33\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NO2_Location_B\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 20.630746311298815,\n        \"min\": 0.43,\n        \"max\": 151.85,\n        \"num_unique_values\": 2910,\n        \"samples\": [\n          57.25,\n          13.73,\n          10.5\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NO2_Location_C\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 26.735531203921493,\n        \"min\": 0.15,\n        \"max\": 168.28,\n        \"num_unique_values\": 3773,\n        \"samples\": [\n          47.98,\n          58.16,\n          14.35\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell code" id="YCP2rLFbSxyr">

``` python
def print_MVs(df):
  for col in df.columns:
    n = sum(df[col].isna())
    print('{}:{}'.format(col,n))
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:291,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717387902958,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RoUJbv7wS7JI" outputId="e74601f7-08f3-4082-f8cb-db66430ad098">

``` python
print_MVs(df)
```

<div class="output stream stdout">

    DateTime:0
    Temperature:0
    Humidity:0
    Wind_Speed:0
    Wind_Direction:0
    NO2_Location_A:120
    NO2_Location_B:580
    NO2_Location_C:132

</div>

</div>

<div class="cell markdown" id="4R0eQdw5S-NO">

### **Ejercicio 2:**

Realice un Data Cleaning Nivel II para enriquecer los datos de tal manera que tengamos las siguientes columnas: Month, Day, Hour y WeekDay.

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:400}" executionInfo="{&quot;elapsed&quot;:540,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717456526815,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="hcyB-fx_YLZZ" outputId="9844cb3f-f523-44dc-bc1d-4059cd2e571c">

``` python
df.DateTime = pd.to_datetime(df.DateTime)
df['Month'] = df.DateTime.dt.month
df['Day'] = df.DateTime.dt.day
df['Hour'] = df.DateTime.dt.hour
df['Weekday'] = df.DateTime.dt.day_name()

df.head()
```

<div class="output execute_result" execution_count="4">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 8784,\n  \"fields\": [\n    {\n      \"column\": \"DateTime\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": \"2020-01-01 00:00:00\",\n        \"max\": \"2020-12-31 23:00:00\",\n        \"num_unique_values\": 8784,\n        \"samples\": [\n          \"2020-09-23 01:00:00\",\n          \"2020-03-03 00:00:00\",\n          \"2020-09-29 11:00:00\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Temperature\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7.363943394853997,\n        \"min\": -2.7894714,\n        \"max\": 33.87053,\n        \"num_unique_values\": 2810,\n        \"samples\": [\n          15.310529,\n          32.68053,\n          26.06053\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Humidity\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 14,\n        \"min\": 20,\n        \"max\": 98,\n        \"num_unique_values\": 79,\n        \"samples\": [\n          95,\n          87,\n          75\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Wind_Speed\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 8.443103411224255,\n        \"min\": 0.0,\n        \"max\": 65.44677,\n        \"num_unique_values\": 1774,\n        \"samples\": [\n          17.174677,\n          23.241617,\n          10.446206\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Wind_Direction\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 91.96162685537111,\n        \"min\": 1.2188721,\n        \"max\": 360.0,\n        \"num_unique_values\": 3072,\n        \"samples\": [\n          113.35556,\n          91.08092,\n          267.63376\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NO2_Location_A\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15.597173171007618,\n        \"min\": -0.46,\n        \"max\": 116.6,\n        \"num_unique_values\": 2807,\n        \"samples\": [\n          42.22,\n          50.03,\n          38.33\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NO2_Location_B\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 20.630746311298815,\n        \"min\": 0.43,\n        \"max\": 151.85,\n        \"num_unique_values\": 2910,\n        \"samples\": [\n          57.25,\n          13.73,\n          10.5\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NO2_Location_C\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 26.735531203921493,\n        \"min\": 0.15,\n        \"max\": 168.28,\n        \"num_unique_values\": 3773,\n        \"samples\": [\n          47.98,\n          58.16,\n          14.35\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Month\",\n      \"properties\": {\n        \"dtype\": \"int32\",\n        \"num_unique_values\": 12,\n        \"samples\": [\n          11,\n          10,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Day\",\n      \"properties\": {\n        \"dtype\": \"int32\",\n        \"num_unique_values\": 31,\n        \"samples\": [\n          28,\n          16,\n          24\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Hour\",\n      \"properties\": {\n        \"dtype\": \"int32\",\n        \"num_unique_values\": 24,\n        \"samples\": [\n          8,\n          16,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Weekday\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Wednesday\",\n          \"Thursday\",\n          \"Monday\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell markdown" id="AETKqxqwY7Ld">

### **Ejercicio 3:**

Construya una visualización para realizar un análisis univariado sobre la temperatura.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:452}" executionInfo="{&quot;elapsed&quot;:297,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717389870067,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="v2Nwt7C3VVDS" outputId="ec0ea720-d65d-4c68-bcb1-2275befb0aa7">

``` python
plt.boxplot(df.Temperature,vert=False)
plt.title('Temperatura')
plt.show()
```

<div class="output display_data">

![](00d128eeefb0fbe7336ac723a688604252f5a6a4.png)

</div>

</div>

<div class="cell markdown" id="uqg59a4sZskv">

### **Ejercicio 4:**

**¿Cómo cambia la temperatura si divimos el dataset en base a la identificación de los valores faltantes?** Para contestar en esta pregunta nos enfocaremos en los datos faltantes identificados en el atributo `NO2_Location_A`.

1.  Tenga en cuenta dos poblaciones: a) SIN Valores Faltantes y b) CON Valores Faltantes.
2.  Construya una visualización a través de boxplots para estas poblaciones con respecto a la **Temperatura**. Coloque como xlabel, el nombre de la variable Temperature.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:5,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717392243331,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2_ooK7ugdTVB" outputId="8b162353-3f97-4b7a-df58-7a39d450f9b6">

``` python
#Detectamos que datos son MV
isMV = df.NO2_Location_A.isna()
isMV
```

<div class="output execute_result" execution_count="34">

    0       False
    1       False
    2        True
    3       False
    4       False
            ...  
    8779    False
    8780    False
    8781    False
    8782    False
    8783    False
    Name: NO2_Location_A, Length: 8784, dtype: bool

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:344,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717392246759,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ZGpde5NGdPsh" outputId="4de0edb2-6bfe-4cfd-93ce-2bee57960703">

``` python
#Creamos una serie con dos indices para la visualización: True y False
box_sr = pd.Series('',index = isMV.unique())
box_sr
```

<div class="output execute_result" execution_count="35">

    False    
    True     
    dtype: object

</div>

</div>

<div class="cell code" id="LexaP0TRdndE">

``` python
#Agrega respectivamente a la serie box_sr
for poss in isMV.unique():
    # Filtra a los indices que son iguales a poss
    BM = isMV == poss
    # Agrega a box_sr
    box_sr[poss] = df[BM].Temperature
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:317,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717392250920,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="hCZZy8nkdzjz" outputId="a6bf832c-ce03-44e2-b4ee-67742a575d9d">

``` python
# Creo la visualización
labels = ['CON Valores Faltantes','SIN Valores Faltantes']
plt.boxplot(box_sr,vert=False)
plt.yticks([1,2],labels)
plt.xlabel('Temperature')
plt.show()
```

<div class="output display_data">

![](8551f68c85031061eeb5e365a978e2bf7844b3da.png)

</div>

</div>

<div class="cell markdown" id="XucoAJ26fl2d">

**VISUALMENTE:** Observando el gráfico, podemos ver que el atributo `Temperature` no tiene cambios significativos entre ambas poblaciones. Por lo tanto, un cambio en `Temperature` no podría haber causado o influido la aparición de valores faltantes en `NO2_Location_A`.

</div>

<div class="cell markdown" id="iqD9Ib2WndRM">

### **Ejercicio 5:**

Construya una visualización para todos los atributos númericos del dataset. Encapsule su código en una función `analyze_numMV(numAtrList,df,attr)` donde `numAttrList = ['Temperature', 'Humidity', 'Wind_Speed', 'Wind_Direction']` y `attr =  NO2_Location_A`

</div>

<div class="cell code" execution_count="5" executionInfo="{&quot;elapsed&quot;:438,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717456532316,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_6Ej9_CyokYz">

``` python
def analyze_numMV(numAtrList,df,attr):
  isMV = df[attr].isna()

  for atributo in numAtrList:
    print('Diagnóstico para datos faltantes en {}:'.format(atributo))

    labelsDic = {True:'CON Valores Faltantes',False:'SIN Valores Faltantes'}
    #Método Visual
    labels=[]
    box_sr = pd.Series('',index = isMV.unique())
    for poss in isMV.unique():
      # Filtra a los indices que son iguales a poss
      BM = isMV == poss
      # Agrega a box_sr
      box_sr[poss] = df[BM][atributo].dropna()
      labels.append(labelsDic[poss])
    plt.boxplot(box_sr,vert=False)
    plt.yticks([1,2],labels)
    plt.xlabel(atributo)
    plt.show()
  print('- - - - - - - - - - - - - - - - - - - - - - - ')
```

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:1070,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717456538112,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="czLdPQyMoc8C" outputId="5f3f4b01-d830-4ca8-a3b5-d2289f0c9720">

``` python
numAtrList = ['Temperature', 'Humidity', 'Wind_Speed', 'Wind_Direction']
analyze_numMV(numAtrList,df,'NO2_Location_A')
```

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Temperature:

</div>

<div class="output display_data">

![](7386ea208724bb443dfb0fbd6f00ff61dbe74597.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Humidity:

</div>

<div class="output display_data">

![](420bc5435ae79fb2e9b4bca236f7650f360ff4cc.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Wind_Speed:

</div>

<div class="output display_data">

![](c260686f372313a43926b67721a20283d21ecf9f.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Wind_Direction:

</div>

<div class="output display_data">

![](6ec66e435a0f85ddcd7ef45e6fc80f8873b992e0.png)

</div>

<div class="output stream stdout">

    - - - - - - - - - - - - - - - - - - - - - - - 

</div>

</div>

<div class="cell markdown" id="jCvM2701pqBY">

**VISUALMENTE:** Observando los gráficos, podemos ver que el atributos no tienen cambios significativos entre ambas poblaciones. Por lo tanto, podriamos decir que el tipo de valores faltantes en `NO2_Location_A` son **MCAR**.

</div>

<div class="cell markdown" id="lleA_IZbkK0m">

### **Ejercicio 6:**

Siguiendo la línea del ejercicio anterior (`NO2_Location_A`), **¿Cómo cambia la distribución de los registros durante la semana ?**

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:283,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717392625184,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="j44VWGTjky8k" outputId="8e0ee8e7-d1f9-4cf9-d1e1-a29caf16288a">

``` python
#Detectar que datos son faltantes
isMV = df.NO2_Location_A.isna()
isMV
```

<div class="output execute_result" execution_count="40">

    0       False
    1       False
    2        True
    3       False
    4       False
            ...  
    8779    False
    8780    False
    8781    False
    8782    False
    8783    False
    Name: NO2_Location_A, Length: 8784, dtype: bool

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:477}" executionInfo="{&quot;elapsed&quot;:789,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717392651969,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ZwmZvZt7k91P" outputId="55361066-c866-43cc-b0bb-9f10bd4d2bc6">

``` python
# Creo la visualización
labels = ['SIN Valores Faltantes','CON Valores Faltantes']
plt.figure(figsize=(10,4))
for i,poss in enumerate(isMV.unique()):
    plt.subplot(1,2,i+1)
    BM = isMV == poss
    df[BM].Weekday.value_counts().plot.bar()
    plt.title(labels[i])
plt.show()
```

<div class="output display_data">

![](38a93520953c5291b22fdacda3aa7d4bad644eed.png)

</div>

</div>

<div class="cell markdown" id="WlV_vz4ylJd7">

**VISUALMENTE:** Al observar el gráfico, podemos ver que los valores faltantes podrían haber ocurrido al azar y no tenemos una tendencia significativa para creer que existe una razón sistemática para que los valores faltantes ocurran debido a un cambio en el valor de `df.Weekday`.

</div>

<div class="cell markdown" id="HwspX_oPqTej">

### **Ejercicio 7:**

Similar al Ejercicio 5, construya una función `analyze_categMV(categAtrList,df,attr)` para los atributos categóricos del dataset.

</div>

<div class="cell code" execution_count="7" executionInfo="{&quot;elapsed&quot;:587,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717456546066,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="orNAOrNmncw7">

``` python
def analyze_categMV(categAtrList,df,attr):

  isMV = df[attr].isna()
  for atributo in categAtrList:
    print('Diagnóstico para datos faltantes en {}:'.format(atributo))
    labelsDic = {True:'CON Valores Faltantes',False:'SIN Valores Faltantes'}
    plt.figure(figsize=(10,4))
    for i,poss in enumerate(isMV.unique()):
      plt.subplot(1,2,i+1)
      BM = isMV == poss
      df[BM][atributo].value_counts().plot.bar()
      plt.title(labelsDic[i])
    plt.show()
```

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:2321,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717456549685,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="UYrpbFPFrgtx" outputId="9eabeddc-288d-4411-ae42-bb24e201b6dc">

``` python
categAtrList = ['Month', 'Day','Hour', 'Weekday']
analyze_categMV(categAtrList,df,'NO2_Location_A')
```

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Month:

</div>

<div class="output display_data">

![](554bb8980d88574c158dcb8335dd2774ac03a1fd.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Day:

</div>

<div class="output display_data">

![](54617c462673ee5735a9d9400838ca5836cb6a52.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Hour:

</div>

<div class="output display_data">

![](27a6a06900b70843d7007878181ebf0af6f8c293.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Weekday:

</div>

<div class="output display_data">

![](38a93520953c5291b22fdacda3aa7d4bad644eed.png)

</div>

</div>

<div class="cell markdown" id="Vh1gNC8qsapx">

Basado en todos resultados, vemos que ninguno de los atributos en el dataset (weekday, day, month, hour) podría haber influido en la tendencia de los valores faltantes. Por lo tanto, los valores faltantes en `NO2_Location_A` son del **tipo MCAR**.

</div>

<div class="cell markdown" id="fZ4kRtaQmaj1">

### **Bonus:**

Para identificar **MCAR** o **MAR**, se puede crear una variable indicadora de **falta o inexistencia** y luego realizar pruebas estadísticas para verificar si esta variable indicadora es independiente de otras variables en el conjunto de datos. La prueba estadística es el *chi-square test of independence* que calcula un p-value, la probalidad que tenemos de que los datos que tenemos sucedan si la hipótesis es cierta. Usando ese p-value, podemos decidir si tenemos alguna evidencia para sospechar una razón sistemática para los valores faltantes.

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:430,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717457404967,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="BzNim7HdlrN0" outputId="ab94f5f2-4332-449d-e42c-9537a74aace3">

``` python
from scipy.stats import chi2_contingency
isMV = df.NO2_Location_B.isna()
chi2, p, _, _ = chi2_contingency(pd.crosstab(isMV,df.Month))
if p < 0.05:
    print("Hipotesis MCAR es rechazada, es MAR ")
else:
    print("Hipotesis MCAR NO es rechazada")
```

<div class="output stream stdout">

    Hipotesis MCAR es rechazada,posiblemente MAR 

</div>

</div>

<div class="cell markdown" id="SGOHfq7kKFh2">

### **Ejercicio 8:**

Detecte el tipo de los datos faltantes para `NO2_Location_B`. Utilice las funciones realizadas en los ejercicios anteriores.

</div>

<div class="cell code" execution_count="18" executionInfo="{&quot;elapsed&quot;:429,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717457686510,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="d_jiiCfncqpe">

``` python
def analyze_numMV(numAtrList,df,attr):
  isMV = df[attr].isna()

  for atributo in numAtrList:
    print('Diagnóstico para datos faltantes en {}:'.format(atributo))

    labelsDic = {True:'CON Valores Faltantes',False:'SIN Valores Faltantes'}
    #Método Visual
    labels=[]
    box_sr = pd.Series('',index = isMV.unique())
    for poss in isMV.unique():
      # Filtra a los indices que son iguales a poss
      BM = isMV == poss
      # Agrega a box_sr
      box_sr[poss] = df[BM][atributo].dropna()
      labels.append(labelsDic[poss])

    chi2, p, _, _ = chi2_contingency(pd.crosstab(isMV,df[atributo]))
    if p < 0.05:
      print("Hipotesis MCAR es rechazada, es MAR ")
    else:
      print("Hipotesis MCAR NO es rechazada")

    plt.boxplot(box_sr,vert=False)
    plt.yticks([1,2],labels)
    plt.xlabel(atributo)
    plt.show()



  print('- - - - - - - - - - - - - - - - - - - - - - - ')
```

</div>

<div class="cell code" execution_count="21" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:2346,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717457723975,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="O5Y1be4vKvsy" outputId="47dc9532-8fa2-4ce4-b596-d59203acc50f">

``` python
#TO DO
numAtrList = ['Temperature', 'Humidity', 'Wind_Speed', 'Wind_Direction']
analyze_numMV(numAtrList,df,'NO2_Location_B')
```

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Temperature:
    Hipotesis MCAR NO es rechazada

</div>

<div class="output display_data">

![](425c3e483c5e34517084d83c7452f17113e3986d.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Humidity:
    Hipotesis MCAR NO es rechazada

</div>

<div class="output display_data">

![](1ef1b2816618e374c5b5b7a4c9485613bb086ba8.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Wind_Speed:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](7a969128601bf784cb8be8bfcf00cee604af37fb.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Wind_Direction:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](70d79f8444acba3bb24c622aacf21222c05fd824.png)

</div>

<div class="output stream stdout">

    - - - - - - - - - - - - - - - - - - - - - - - 

</div>

</div>

<div class="cell markdown" id="zpTbmzRhZbmQ">

**VISUALMENTE:** Al observar el gráfico, podemos ver que existen atributos como Wind_Speed y Wind_Direction que tienen una relación con la presencia de los valores faltantes.

</div>

<div class="cell code" execution_count="22" executionInfo="{&quot;elapsed&quot;:391,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717457814082,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4UUXLDz8dYjI">

``` python
def analyze_categMV(categAtrList,df,attr):

  isMV = df[attr].isna()
  for atributo in categAtrList:
    print('Diagnóstico para datos faltantes en {}:'.format(atributo))
    labelsDic = {True:'CON Valores Faltantes',False:'SIN Valores Faltantes'}
    plt.figure(figsize=(10,4))
    for i,poss in enumerate(isMV.unique()):
      plt.subplot(1,2,i+1)
      BM = isMV == poss
      df[BM][atributo].value_counts().plot.bar()
      plt.title(labelsDic[i])

    chi2, p, _, _ = chi2_contingency(pd.crosstab(isMV,df[atributo]))
    if p < 0.05:
      print("Hipotesis MCAR es rechazada, es MAR ")
    else:
      print("Hipotesis MCAR NO es rechazada")

    plt.show()
```

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:2853,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717457819790,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="SD476QsKY-vb" outputId="f1fc8e78-6156-4bdc-9b6c-f4d4f2aa8baf">

``` python
categAtrList = ['Month', 'Day','Hour', 'Weekday']
analyze_categMV(categAtrList,df,'NO2_Location_B')
```

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Month:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](8807bbe06fe630d5d062de6edd7680546d282a1d.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Day:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](c6d30c0b3f903feed073bef3bd3290bad0bf3b66.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Hour:
    Hipotesis MCAR NO es rechazada

</div>

<div class="output display_data">

![](9203f15c32112be869dd91ccdff06f83b3ce63aa.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Weekday:
    Hipotesis MCAR NO es rechazada

</div>

<div class="output display_data">

![](353d5bfed66edbf87badbe1b0b2eb7932289252c.png)

</div>

</div>

<div class="cell markdown" id="TvIYwYpsdvW0">

Poniendo todo en contexto, existe una relación fuerte entre Wind_speed con otros atributos. Por lo tanto es **MAR.**

</div>

<div class="cell code" execution_count="25" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:449}" executionInfo="{&quot;elapsed&quot;:1263,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717458231124,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="WxgTYKPVeSQ1" outputId="cf20bca9-cf19-4679-b679-8d22b34a0b43">

``` python
speed_discretized = pd.cut(df.Wind_Speed, bins=5)
contigencia_tbl = pd.crosstab(speed_discretized, df.Month)
probability_tbl = contigencia_tbl / contigencia_tbl.sum()
sns.heatmap(probability_tbl,annot=True, center=0.5)
plt.show()
```

<div class="output display_data">

![](866ea7a122ce77d4270ed21c4b27700a6771cbed.png)

</div>

</div>

<div class="cell markdown" id="MTxmuUP5KcEE">

### **Ejercicio 9:**

Detecte el tipos de los datos faltantes para `NO2_Location_C`.

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:4615,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717458259784,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="VdoiS-9RKE7E" outputId="b3698789-2a92-406f-db4b-565f1342781c">

``` python
#TO DO
numAtrList = ['Temperature', 'Humidity', 'Wind_Speed', 'Wind_Direction']
analyze_numMV(numAtrList,df,'NO2_Location_C')
```

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Temperature:
    Hipotesis MCAR NO es rechazada

</div>

<div class="output display_data">

![](06f3f2406eb2243e982c1b8cd5754b60d0ffc8a3.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Humidity:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](351904067e7cb41c5a3efceecf51b9ad6bd6dabc.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Wind_Speed:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](2ede91bf1448c9e73455bcdad9f0e546ace319ee.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Wind_Direction:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](74f85cf5408d018dd2f6edff423a5a9a0c96d59f.png)

</div>

<div class="output stream stdout">

    - - - - - - - - - - - - - - - - - - - - - - - 

</div>

</div>

<div class="cell code" execution_count="27" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:3383,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717458269621,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RVHCDuQXZDE-" outputId="110b5639-d693-4135-ae5b-cd028f5205a2">

``` python
categAtrList = ['Month', 'Day','Hour', 'Weekday']
analyze_categMV(categAtrList,df,'NO2_Location_C')
```

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Month:
    Hipotesis MCAR NO es rechazada

</div>

<div class="output display_data">

![](27810658a977535372f762dee9dfacb69e10e2f3.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Day:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](9e6e5c07d5fdd31b6bf7c3337241cf438b97b5c0.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Hour:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](012d52578fc97004a53a6af7af30b0d230927a41.png)

</div>

<div class="output stream stdout">

    Diagnóstico para datos faltantes en Weekday:
    Hipotesis MCAR es rechazada, es MAR 

</div>

<div class="output display_data">

![](23388a46719bd5b3997eaa18194d72c0ff27f067.png)

</div>

</div>

<div class="cell markdown" id="jkV7LD1zfr2k">

**VISUALMENTE:** Al observar los gráficos, el diagnóstico basado en Hour y day muestran patrones significativos . Los valores faltantes ocurren solo cuando el valor del atributo de hora es 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 y 20, o cuando el valor del atributo de día es 25, 26, 27, 28 y 29. De estos informes, podemos deducir que los valores faltantes ocurren de manera predecible el último sábado de cada mes de 10 a.m. a 8 p.m. Ese es el patrón que vemos en los datos, **pero ¿por qué?**

Después de informar a la autoridad local de la ubicación C, resultó que un grupo de empleados de la planta de energía en la ubicación C había estado aprovechando los recursos de la planta de energía para participar en la extracción de varias criptomonedas. Este abuso de recursos se había producido recién el último sábado del mes, ya que la central en cuestión tenía un día libre completo para realizar mantenimiento regular y preventivo. Como este grupo de empleados había estado bajo mucho estrés para cubrir sus huellas y evitar ser atrapados, decidieron alterar el sensor que se había instalado para regular la contaminación del aire de la planta de energía. Lo que no sabían es que la manipulación de la recopilación de datos deja una marca en el conjunto de datos que no se oculta fácilmente a los ojos de un analista de datos de alta calidad como usted.

Este último dato y el diagnóstico nos llevan a la conclusión de que el valor faltante en **NO2_Location_C** es un valor **MNAR**.

</div>
