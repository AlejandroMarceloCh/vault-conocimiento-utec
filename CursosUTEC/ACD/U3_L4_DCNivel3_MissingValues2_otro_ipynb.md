---
curso: ACD
titulo: U3_L4 DCNivel3_MissingValues2 (otro)
slides: 0
fuente: U3_L4 DCNivel3_MissingValues2 (otro).ipynb
---

<div class="cell markdown" id="yAA5zxoqMIpw">

# **U3_L4 Data Cleaning Nivel III: Valores Faltantes - Manejo**

## **Objetivo:**

Al finalizar el laboratorio, el estudiante será capaz de manejar la presencia de valores faltantes en una dataset dependiendo su tipología.

</div>

<div class="cell code" execution_count="1" id="CxlHQwhkLx6H">

``` python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

</div>

<div class="cell markdown" id="gvY9Nw8eNlsw">

## **Estrategia 1: Ignorar los valores faltantes**

</div>

<div class="cell markdown" id="yWDRj7xWPChN">

### **Ejercicio 1**

En base al dataset `Airdata.csv` (utilizado en la sesión anterior), construya una visualización cuyo objetivo sea mostrar el promedio de la contaminación en el sector A de la ciudad durante el día (es decir por cada hora)

</div>

<div class="cell code" execution_count="2" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:400}" executionInfo="{&quot;elapsed&quot;:436,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717470733252,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="vKmfU4GyOlN6" outputId="09c8b879-8eed-4901-9ea1-1aec4017fdc9">

``` python
#Read Data y Data Cleaning Nivel I y II
df = pd.read_csv("Airdata.csv")
df.DateTime = pd.to_datetime(df.DateTime)
df['Month'] = df.DateTime.dt.month
df['Day'] = df.DateTime.dt.day
df['Hour'] = df.DateTime.dt.hour
df['Weekday'] = df.DateTime.dt.day_name()
df
```

<div class="output execute_result" execution_count="2">

                    DateTime  Temperature  Humidity  Wind_Speed  Wind_Direction  \
    0    2020-01-01 00:00:00        17.48        74        0.37          358.05   
    1    2020-01-01 01:00:00        14.31        85        2.93          277.27   
    2    2020-01-01 02:00:00        18.24        62        1.16             NaN   
    3    2020-01-01 03:00:00        22.62        82        1.53          221.01   
    4    2020-01-01 04:00:00        13.83        79        1.03          121.29   
    ...                  ...          ...       ...         ...             ...   
    8995 2021-01-09 19:00:00        15.51        71         NaN          289.36   
    8996 2021-01-09 20:00:00        20.84        64        1.15          145.90   
    8997 2021-01-09 21:00:00        22.94        79        4.60          174.88   
    8998 2021-01-09 22:00:00        11.58        67        0.78            9.96   
    8999 2021-01-09 23:00:00        19.01        60        4.33          144.48   

          NO2_Location_A  NO2_Location_B  NO2_Location_C  Month  Day  Hour  \
    0              27.63           58.46           79.20      1    1     0   
    1              17.16           23.62           45.44      1    1     1   
    2              15.90           30.74           32.23      1    1     2   
    3              31.85           33.31           99.11      1    1     3   
    4               8.97           42.21           63.61      1    1     4   
    ...              ...             ...             ...    ...  ...   ...   
    8995           19.50           41.17           32.42      1    9    19   
    8996           25.98           12.41           78.80      1    9    20   
    8997           17.33           20.19          128.40      1    9    21   
    8998           18.20           47.76           46.54      1    9    22   
    8999           21.13           19.62           46.43      1    9    23   

            Weekday  
    0     Wednesday  
    1     Wednesday  
    2     Wednesday  
    3     Wednesday  
    4     Wednesday  
    ...         ...  
    8995   Saturday  
    8996   Saturday  
    8997   Saturday  
    8998   Saturday  
    8999   Saturday  

    [9000 rows x 12 columns]

</div>

</div>

<div class="cell code" execution_count="3">

``` python
df.isnull().sum()
```

<div class="output execute_result" execution_count="3">

    DateTime            0
    Temperature         0
    Humidity            0
    Wind_Speed        300
    Wind_Direction    500
    NO2_Location_A    120
    NO2_Location_B    580
    NO2_Location_C    132
    Month               0
    Day                 0
    Hour                0
    Weekday             0
    dtype: int64

</div>

</div>

<div class="cell markdown" id="XqNux4m0P5ys">

Dado que según nuestro diagnostico la presencia de los datos faltantes en **NO2_Location_A** son de tipo MCAR y nuestro objetivo es calcular el promedio, podriamos usar la función `mean()` que **ignora la existencia de atributos con datos faltantes**.

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:453}" executionInfo="{&quot;elapsed&quot;:1247,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717471084321,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="-vlKxJWpPjZ-" outputId="0c847de8-f9af-4997-876a-77136b72785d">

``` python
df.groupby('Hour').NO2_Location_A.mean().plot.bar()
plt.grid()
plt.show()
```

<div class="output display_data">

![](a38f070800913bec6cec3855a3c5cfccd1cc0162.png)

</div>

</div>

<div class="cell code" execution_count="5">

``` python
120/9000*100
```

<div class="output execute_result" execution_count="5">

    1.3333333333333335

</div>

</div>

<div class="cell markdown" id="7i9IfvHTQjWr">

### **Ejercicio 2**

Desarrolle una visualización para comparar los promedios de NO2 por hora en las ubicaciones A y B.

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:453}" executionInfo="{&quot;elapsed&quot;:821,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717471217573,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Z-AThgl1PjCP" outputId="1e974f5b-8ea3-4df2-82ca-6280a65cd111">

``` python
df.groupby('Hour')[['NO2_Location_A','NO2_Location_B']].mean().plot.bar()
plt.show()
```

<div class="output display_data">

![](5209a221c265b868b9a4a856976ab6f9014fcd4a.png)

</div>

</div>

<div class="cell markdown" id="Jmss6yelQyLW">

Dado que los valores faltantes en `NO2_Location_A` son de tipo **MCAR** y en `NO2_Location_B` son de tipo **MAR** se puede manejar los valores faltantes tal como estan.

</div>

<div class="cell markdown" id="biNBpeAtQ71m">

## **Estrategia 2 y 3: Eliminar filas y columnas con valores faltantes**

En pandas se puede utilizar la función `dropna()` que filtra los índices (filas y columnas) en función si existe un valor faltante y los elimina.

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:283,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472020354,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="3ydLcfs-RP1g" outputId="35ec3cbe-b545-4c1e-c26b-d190e17abeff">

``` python
data = pd.Series([1, np.nan, 'hello', None])
data
```

<div class="output execute_result" execution_count="7">

    0        1
    1      NaN
    2    hello
    3     None
    dtype: object

</div>

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472030819,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mbVPKNrlT2fX" outputId="50aa2702-a015-4401-a4f3-07a789f18e0e">

``` python
 data.dropna()
```

<div class="output execute_result" execution_count="8">

    0        1
    2    hello
    dtype: object

</div>

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:17,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472053211,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="qdRaL8huT6xy" outputId="f05c33aa-73f9-4558-c356-977093cd4dfb">

``` python
df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])
df
```

<div class="output execute_result" execution_count="9">

         0    1  2
    0  1.0  NaN  2
    1  2.0  3.0  5
    2  NaN  4.0  6

</div>

</div>

<div class="cell markdown" id="sNzHwen9T-yR">

No se puede eliminar un dato solo, en cambio solo se eliminar la fila entera o columna.

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:81}" executionInfo="{&quot;elapsed&quot;:266,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472110378,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="TieOGmM2UI-o" outputId="211ca8d5-dbac-4ba0-f25f-340dd6046cde">

``` python
df.dropna()
```

<div class="output execute_result" execution_count="10">

         0    1  2
    1  2.0  3.0  5

</div>

</div>

<div class="cell code" execution_count="11" id="eb8m1EFpUQM4">

``` python
df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])
df
```

<div class="output execute_result" execution_count="11">

         0    1  2
    0  1.0  NaN  2
    1  2.0  3.0  5
    2  NaN  4.0  6

</div>

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:6,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472147074,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="S75zcuTIURr6" outputId="c1987158-92d0-41bf-c965-76f6b2f9c621">

``` python
df.dropna(axis='columns')
```

<div class="output execute_result" execution_count="12">

       2
    0  2
    1  5
    2  6

</div>

</div>

<div class="cell markdown" id="l8_ZncKaUhSd">

El valor predeterminado es **how='any'**, de modo que se elimina cualquier fila o columna que contenga **algún** valor nulo. También puede especificar **how='all'**, que solo eliminará filas/columnas que todos sus valores sean nulos.

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:303,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472277502,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="3G6ML545UuYK" outputId="7ff8e710-1e82-4830-9e2c-9f6b78017e11">

``` python
df[3] = np.nan
df
```

<div class="output execute_result" execution_count="13">

         0    1  2   3
    0  1.0  NaN  2 NaN
    1  2.0  3.0  5 NaN
    2  NaN  4.0  6 NaN

</div>

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:250,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472289727,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="BNqBXzJIUzsd" outputId="aeefc682-9f48-420d-9193-877e24c32269">

``` python
df.dropna(axis='columns', how='all')
```

<div class="output execute_result" execution_count="14">

         0    1  2
    0  1.0  NaN  2
    1  2.0  3.0  5
    2  NaN  4.0  6

</div>

</div>

<div class="cell markdown" id="K661PG9FVEj3">

Para un control más detallado, el parámetro **thresh** le permite especificar un número mínimo de **valores no nulos** para la fila/columna que se mantendrá:

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:329,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472375241,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="MbHf0v0oVBwr" outputId="c8e76396-370b-42a0-e242-79c7f4a9924c">

``` python
df[3] = np.nan
df
```

<div class="output execute_result" execution_count="15">

         0    1  2   3
    0  1.0  NaN  2 NaN
    1  2.0  3.0  5 NaN
    2  NaN  4.0  6 NaN

</div>

</div>

<div class="cell code" execution_count="16" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:81}" executionInfo="{&quot;elapsed&quot;:291,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472392501,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aNbVvNG6VMX4" outputId="0ccfa346-2227-4d95-83b7-7138f07de164">

``` python
df.dropna(axis='rows', thresh=3)
```

<div class="output execute_result" execution_count="16">

         0    1  2   3
    1  2.0  3.0  5 NaN

</div>

</div>

<div class="cell markdown" id="MddslSMIW3bo">

### **Ejercicio 3**

A partir del siguiente dataframe df2 elimine las filas dodne al menos un elemento esta faltando.

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:363}" executionInfo="{&quot;elapsed&quot;:284,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472862017,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="nQR5cofuW_hv" outputId="ad68f0fe-3028-4fac-a9fc-3250b64dbd0a">

``` python
df2 =  pd.DataFrame([
                       ('Lewis' ,67,'H1',21),
                       ('Phylis',70,'F3',19),
                       ('Mary',73,'F3',21),
                       ('Steve',pd.NA,'P2',23),
                       ('Edick',67,'H1',21),
                       (pd.NA,78,'F3',pd.NA),
                       ('Carolin',78,pd.NA,pd.NA),
                       (pd.NA,76,'F3',23),
                       ('Euge',67,pd.NA,pd.NA),
                       ('Francis',89,'F3',20)
                   ],
    columns = ('name','marks','department','age') )
df2
```

<div class="output execute_result" execution_count="17">

          name marks department   age
    0    Lewis    67         H1    21
    1   Phylis    70         F3    19
    2     Mary    73         F3    21
    3    Steve  <NA>         P2    23
    4    Edick    67         H1    21
    5     <NA>    78         F3  <NA>
    6  Carolin    78       <NA>  <NA>
    7     <NA>    76         F3    23
    8     Euge    67       <NA>  <NA>
    9  Francis    89         F3    20

</div>

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:255,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472910894,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="JOi75nXtXGSi" outputId="bd2559a6-7792-49dc-bde9-40ce8d63e145">

``` python
df2.dropna()
```

<div class="output execute_result" execution_count="18">

          name marks department age
    0    Lewis    67         H1  21
    1   Phylis    70         F3  19
    2     Mary    73         F3  21
    4    Edick    67         H1  21
    9  Francis    89         F3  20

</div>

</div>

<div class="cell markdown" id="t0C_de1aXTMy">

### **Ejercicio 4**

Elimina las filas donde todos los elementas estan faltando

</div>

<div class="cell code" execution_count="19" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:20,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717472963796,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="0OdpDLSDXZDR" outputId="d2cedcf2-1fce-468f-c4c1-c3dfebbef262">

``` python
df3=df.copy()
df3.dropna(how='all')
```

<div class="output execute_result" execution_count="19">

         0    1  2   3
    0  1.0  NaN  2 NaN
    1  2.0  3.0  5 NaN
    2  NaN  4.0  6 NaN

</div>

</div>

<div class="cell markdown" id="EyoaGgyqXf8-">

### **Ejercicio 5**

Que permanezca solo las filas con al menos 2 valores no vacíos.

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:253,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717473034828,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="jEna4kWuXqqf" outputId="054e6643-c747-4bfe-cbba-af7c265dfea2">

``` python
df4=df.copy()
df4.dropna(thresh=2)
```

<div class="output execute_result" execution_count="20">

         0    1  2   3
    0  1.0  NaN  2 NaN
    1  2.0  3.0  5 NaN
    2  NaN  4.0  6 NaN

</div>

</div>

<div class="cell markdown" id="21bNl7VLkisw">

## **Estrategia 4: Estimar e imputar un valor**

</div>

<div class="cell markdown">

### **Ejercicio 6**

Construya una visutalización que analize la tendencia y la comparación de `NO2` cada primer día del mes en la ubicación A.

</div>

<div class="cell code" execution_count="21">

``` python
#Read Data y Data Cleaning Nivel I y II
air_df = pd.read_csv("Airdata.csv")
air_df.DateTime = pd.to_datetime(air_df.DateTime)
air_df['Month'] = air_df.DateTime.dt.month
air_df['Day'] = air_df.DateTime.dt.day
air_df['Hour'] = air_df.DateTime.dt.hour
air_df['Weekday'] = air_df.DateTime.dt.day_name()
air_df
```

<div class="output execute_result" execution_count="21">

                    DateTime  Temperature  Humidity  Wind_Speed  Wind_Direction  \
    0    2020-01-01 00:00:00        17.48        74        0.37          358.05   
    1    2020-01-01 01:00:00        14.31        85        2.93          277.27   
    2    2020-01-01 02:00:00        18.24        62        1.16             NaN   
    3    2020-01-01 03:00:00        22.62        82        1.53          221.01   
    4    2020-01-01 04:00:00        13.83        79        1.03          121.29   
    ...                  ...          ...       ...         ...             ...   
    8995 2021-01-09 19:00:00        15.51        71         NaN          289.36   
    8996 2021-01-09 20:00:00        20.84        64        1.15          145.90   
    8997 2021-01-09 21:00:00        22.94        79        4.60          174.88   
    8998 2021-01-09 22:00:00        11.58        67        0.78            9.96   
    8999 2021-01-09 23:00:00        19.01        60        4.33          144.48   

          NO2_Location_A  NO2_Location_B  NO2_Location_C  Month  Day  Hour  \
    0              27.63           58.46           79.20      1    1     0   
    1              17.16           23.62           45.44      1    1     1   
    2              15.90           30.74           32.23      1    1     2   
    3              31.85           33.31           99.11      1    1     3   
    4               8.97           42.21           63.61      1    1     4   
    ...              ...             ...             ...    ...  ...   ...   
    8995           19.50           41.17           32.42      1    9    19   
    8996           25.98           12.41           78.80      1    9    20   
    8997           17.33           20.19          128.40      1    9    21   
    8998           18.20           47.76           46.54      1    9    22   
    8999           21.13           19.62           46.43      1    9    23   

            Weekday  
    0     Wednesday  
    1     Wednesday  
    2     Wednesday  
    3     Wednesday  
    4     Wednesday  
    ...         ...  
    8995   Saturday  
    8996   Saturday  
    8997   Saturday  
    8998   Saturday  
    8999   Saturday  

    [9000 rows x 12 columns]

</div>

</div>

<div class="cell code" execution_count="22">

``` python
air_df.isnull().sum()
```

<div class="output execute_result" execution_count="22">

    DateTime            0
    Temperature         0
    Humidity            0
    Wind_Speed        300
    Wind_Direction    500
    NO2_Location_A    120
    NO2_Location_B    580
    NO2_Location_C    132
    Month               0
    Day                 0
    Hour                0
    Weekday             0
    dtype: int64

</div>

</div>

<div class="cell code" execution_count="23" id="3iuVAu9Jwgor">

``` python
month_pos = air_df.Month.unique()
hour_pos = air_df.Hour.unique()
plt.figure(figsize=(13,4))

for month in month_pos:
    #Seleccionamos los primeros días de cada mes
    firstList = (air_df.Month == month) & (air_df.Day ==1)
    #nuevo subdf
    tmp_df = air_df[firstList]
    plt.plot(tmp_df['NO2_Location_A'].values,label=month)
plt.legend(ncol=6)
plt.xticks(hour_pos)
plt.xlim(-1,24)
plt.show()
```

<div class="output display_data">

![](9f39aa2045a7cd1e495743b61ee80936f807041a.png)

</div>

</div>

<div class="cell markdown" id="QmDCY3EV5sRj">

En el diagrama anterior vemos que los gráficos de líneas están cortados en el medio debido a la existencia de valores faltantes. Si la figura satisface nuestra necesidad analítica, entonces hemos terminado y no hay necesidad de hacer nada más.

**Sin embargo**, si deseamos lidiar con los valores faltantes y eliminar los puntos vacíos en los gráficos de líneas, necesitaríamos usar la interpolación ya que los valores faltantes son del tipo MCAR y los datos son series temporales.

La función `interpolate()` con el método `linear` imputa los valores faltantes con el promedio de los datos previos y posteriores (como si fueran unidos por una regla).

</div>

<div class="cell code" execution_count="24" id="aKCQv8dfwny1">

``` python
NO2_Location_A_noMV = air_df.NO2_Location_A.interpolate(method='linear')

month_pos = air_df.Month.unique()
hour_pos = air_df.Hour.unique()
plt.figure(figsize=(13,4))

for month in month_pos:
    #Seleccionamos los primeros días de cada mes
    firstList = (air_df.Month == month) & (air_df.Day ==1)
    #Dibujamos
    plt.plot(NO2_Location_A_noMV[firstList].values, label=month)
plt.legend(ncol=6)
plt.xticks(hour_pos)
plt.xlim(-1,24)
plt.show()
```

<div class="output display_data">

![](aea433c461f81c7b3b139d014952bf72a26eeb1f.png)

</div>

</div>

<div class="cell code">

``` python
```

</div>
