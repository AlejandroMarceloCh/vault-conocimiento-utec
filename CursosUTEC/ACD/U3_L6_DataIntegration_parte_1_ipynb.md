---
curso: ACD
titulo: U3_L6 DataIntegration (parte 1)
slides: 0
fuente: U3_L6 DataIntegration (parte 1).ipynb
---

<div class="cell markdown" id="NDCNtQqKdX5C">

# **U3_L6 Data Integration**

## **Objetivo:**

Al finalizar el laboratorio, el estudiante será capaz de integrar datos a partir de diferentes fuentes.

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:3316,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718565240348,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RXUm6p3FdHHg">

``` python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

</div>

<div class="cell markdown" id="lk9ffhHCfcAG">

## **I. Fundamentos para Data Integration**

Se puede combinar datos en Pandas en diferentes maneras:

- `merge()`: Conecte filas en DataFrames según una o más keys. Esto resultará familiar para los usuarios de SQL u otras bases de datos relacionales, ya que implementa operaciones de **unión** a bases de datos.
- `concat()`: Concatenar o “apilar” objetos a lo largo de un eje.
- `combine_first()`: Empalma datos superpuestos para completar los valores faltantes en un objeto con valores de otro.

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:353,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567004297,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="lSUv5jlXft8R">

``` python
df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"],
                    "data1": pd.Series(range(7), dtype="Int64")})
df2 = pd.DataFrame({"key": ["a", "b", "d"],
                    "data2": pd.Series(range(3), dtype="Int64")})
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:269}" executionInfo="{&quot;elapsed&quot;:373,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567013629,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ca7DhJRvk3eJ" outputId="946f372e-bae4-415a-acc7-66420402c53f">

``` python
df1
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:378,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567019926,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2ueptPqDk5hF" outputId="ef4c1a33-ccbc-43ea-b090-75a72f0ac2de">

``` python
df2
```

</div>

<div class="cell markdown" id="l9A6JJgBlB3M">

### **Ejemplo 1:**

Ejemplo *many-to-one join*. Combine los dataframes `df1`y `df2`.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:238}" executionInfo="{&quot;elapsed&quot;:476,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567424974,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="wrrl8wLemG0f" outputId="e42084b8-2941-4e5c-da4f-f9f7d4a27417">

``` python
pd.merge(df1,df2,on='key')
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:238}" executionInfo="{&quot;elapsed&quot;:204,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567448699,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_8868HuHlPkB" outputId="61b3a176-6632-4d02-c241-4832ee291e62">

``` python
#No es necesario especificar el nom columna
#Usa la columna en común
pd.merge(df1,df2)
```

</div>

<div class="cell markdown" id="6wrqQtD0mmsW">

### **Ejemplo 2:**

Si el nombre de las columnas son diferentes para los dataset, se puede especificar el nombre de las columnas que se usará para hacer la combinación.

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:404,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567520766,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="VznTP0C1mrWB">

``` python
df3 = pd.DataFrame({"lkey": ["b", "b", "a", "c", "a", "a", "b"],
                   "data1": pd.Series(range(7), dtype="Int64")})

df4 = pd.DataFrame({"rkey": ["a", "b", "d"],
                   "data2": pd.Series(range(3), dtype="Int64")})
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:269}" executionInfo="{&quot;elapsed&quot;:347,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567525473,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ZA_cKGo_m08B" outputId="a17b1285-5c8e-434a-d681-edbb181d2791">

``` python
df3
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:399,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567531917,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="OB4ZRRV2m2Th" outputId="a6d839e6-93ca-4b53-ff51-7509f4c66e02">

``` python
df4
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:238}" executionInfo="{&quot;elapsed&quot;:295,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567585135,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="qPPRhrGSm4ya" outputId="4e58585d-dd35-4c2e-c232-fa359dc01c65">

``` python
pd.merge(df3, df4, left_on="lkey", right_on="rkey")
```

</div>

<div class="cell markdown" id="PfbIHRfoneeY">

### **Ejemplo 3:**

De forma predeterminada, `pandas.merge()` realiza una unión interna (inner); las keys del resultado son la intersección o el conjunto común que se encuentra en ambas tablas. Otras opciones posibles son "left", "right" y "outer". En detalle:

- `how="inner"` Utilice sólo las combinaciones de keys observadas en ambas tablas.
- `how="left"` Utilice todas las combinaciones de keys que se encuentran en la tabla de la izquierda
- `how="right"` Utilice todas las combinaciones de keys que se encuentran en la tabla de la derecha
- `how="outer"` Utilice todas las combinaciones de keys observadas en ambas tablas juntas

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:300}" executionInfo="{&quot;elapsed&quot;:455,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718567715414,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="53G5-meiniRT" outputId="63179ba2-0317-4456-c35a-9f593a9deda3">

``` python
pd.merge(df1, df2, how="outer")
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:300}" executionInfo="{&quot;elapsed&quot;:365,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718569416527,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="OZzp5fMmuBy5" outputId="350f0727-f096-4ff9-86e7-77d8960a6b0c">

``` python
pd.merge(df3, df4, left_on="lkey", right_on="rkey", how="outer")
```

</div>

<div class="cell markdown" id="-YjuDX96vQzY">

### **Ejemplo 4:**

Concatenemos dos dataframes(uno a lado del otro). Se puede usar el atributo `keys`para crear un index jerarquico donde el primer nivel puede ser usado para identificar cada uno de los objetos DataFrame concatenados.

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:393,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718570227165,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="qEv2e846vVrS">

``` python
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=["a", "b", "c"],
                  columns=["one", "two"])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=["a", "c"],
                  columns=["three", "four"])
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718570228823,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="R4gLraNrvvTM" outputId="f1452ccd-9fc7-4418-907d-772677c75b57">

``` python
df1
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:125}" executionInfo="{&quot;elapsed&quot;:431,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718570231456,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="wvDpxptHvw3M" outputId="7ba98650-656f-477b-aa74-ea8ce8bd3c65">

``` python
df2
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}" executionInfo="{&quot;elapsed&quot;:323,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718570243308,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KmoDb6dHvyPN" outputId="70e7b4ae-c87a-4b11-951b-d4597404c6f3">

``` python
pd.concat([df1, df2], axis="columns", keys=["level1", "level2"])
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}" executionInfo="{&quot;elapsed&quot;:7,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718570246293,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="SMssM8R3wTwh" outputId="20c71dca-0e87-4b54-cc8e-ca5f21e7ee81">

``` python
pd.concat([df2, df1], axis="columns", keys=["level2", "level1"])
```

</div>

<div class="cell markdown" id="PARJ6XfuxWpM">

En este caso, puedes pasar `ignore_index=True`, que descarta los índices de cada DataFrame y concatena los datos en las columnas únicamente, asignando un nuevo índice predeterminado:

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:335,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718570313617,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="sjT7T7r2xbis" outputId="e1da74b8-c408-458a-905c-b05227c1a86a">

``` python
pd.concat([df1, df2], ignore_index=True)
```

</div>

<div class="cell markdown" id="0vVbGjhmC-ys">

### **Ejemplo 5:**

Con DataFrames, `combine_first` "parchea" los datos faltantes en el objeto que llama con datos del objeto que se pasa como párametro.

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:328,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718574989066,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="-u9QeioTDFky">

``` python
df1 = pd.DataFrame({"a": [1., np.nan, 5., np.nan],
                    "b": [np.nan, 2., np.nan, 6.],
                    "c": range(2, 18, 4)})
df2 = pd.DataFrame({"a": [5., 4., np.nan, 3., 7.],
                    "b": [np.nan, 3., 4., 6., 8.]})
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}" executionInfo="{&quot;elapsed&quot;:12,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718574994189,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Kd9-25oiDUZw" outputId="4304ec4f-69c5-49ea-c3f0-3f0b59aa9b4b">

``` python
df1
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:307,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718574999725,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="cLUbae9hDVs3" outputId="24966aad-0a71-474c-9334-dd8c44dd132a">

``` python
df2
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:342,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718575014609,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="CtJfyyYoDY9J" outputId="8ccc10d0-ebfc-431b-9550-139b9aac15af">

``` python
df1.combine_first(df2)
```

</div>

<div class="cell markdown" id="yHN7VKfafioR">

## **II. Desafíos de Data Integration**

</div>

<div class="cell markdown" id="iXrvUNxlpRn_">

### **Ejercicio 1:**

En este ejercicio usaremos dos fuentes de datos:

1.  El primero se obtuvo de un proveedor de electricidad local que mantiene el consumo de electricidad para los años 2016 y 2017 (`Electricity Data 2016_2017.csv`)
2.  El segundo se obtuvo de una estación meteorológica local e incluye datos de temperatura deñ año 2016 (`Temperature 2016.csv`).

El objetivo análitico es llegar a una visualización que pueda responder ***si la cantidad de consumo de electricidad se ve afectada por el clima, y en ese caso ¿cómo se ve afectada?***.

Para realizar la visualización se debe integrar ambos datasets, con ese próposito realice los siguientes pasos:

1.  Revise las características de cada dataset y elimine los datos del año que no tienen en común.\
2.  Agregue una nueva columna "Hour" en `electric_df` que tenga un patrón similar al otro dataset.
3.  Cree una nueva estructura de datos cuya definición del objeto de datos sea el consumo de electricidad por hora.
4.  Limpie el dataset `temp_df` a nivel II.
5.  Integrar los datasets
6.  Realizar la visualización adecuada

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:325,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718575207016,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="53GKgTGYd8Vr">

``` python
electric_df = pd.read_csv('Electricity Data 2016_2017.csv')
temp_df = pd.read_csv('Temperature 2016.csv')
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:13,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718575209747,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2H946lEnfUNb" outputId="7362800a-d5a4-4f0c-db5b-911ce955b1a8">

``` python
electric_df
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:356,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718575217704,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="dpiNAW2pfYGX" outputId="abaa1f5b-29b3-45ec-e69b-4249bc31602f">

``` python
temp_df
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:341,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718575342156,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4RZB75RoEP5z" outputId="6a8e7758-5bd6-49aa-ae1a-c4c98ee37440">

``` python
#Eliminar el año 2017 antes de la unión
BM = electric_df.Date.str.contains('2017')
dropping_index = electric_df[BM].index
electric_df.drop(index = dropping_index,inplace=True)
electric_df
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:334,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718575489567,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="QRTrYnFEFBb4" outputId="17403f9a-fe7e-4f77-c6ac-373673ad6392">

``` python
#Agregar una nueva columna Hour en formato similar temp_df
#Solo se queda con la hora
electric_df['Hour'] = electric_df.Time.apply(lambda v: '{}:00'.format(v.split(':')[0]))
electric_df
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:335,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718575947717,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="lhcVhrAjG5s_" outputId="09485bde-7c2c-4b7b-e956-7f4bbb23aab5">

``` python
integrate_sr = electric_df.groupby(['Date','Hour']).Consumption.sum()
integrate_sr
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:379,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718576012125,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="xDDsgcIYHMb5" outputId="8a102603-45a3-4641-bd1c-1e1896e5c908">

``` python
temp_df
```

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:332,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718576016857,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="EH56M6rKHLbp">

``` python
def unpackTimestamp(r):
    ts = r.Timestamp
    date,time = ts.split('T')
    hour = time.split(':')[0]
    year,month,day = date.split('-')

    r['Hour'] = '{}:00'.format(int(hour))
    r['Date'] = '{}/{}/{}'.format(
        int(month),int(day),year)
    return(r)
```

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:11674,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718576036810,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="GmfePQHbHQZJ">

``` python
temp_df = temp_df.apply(unpackTimestamp,axis=1)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:455}" executionInfo="{&quot;elapsed&quot;:325,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718576080668,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="yxzilt7NHUFe" outputId="3e8927fc-cbbd-49b6-9f9a-23986eebdbdc">

``` python
temp_df = temp_df.set_index(['Date','Hour']).drop(columns=['Timestamp'])
temp_df
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:363,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718576220929,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ckaifwVdHxvb" outputId="c7722098-ec92-4734-c699-7bc478fc69f7">

``` python
#Integrar ambos dataset
integrate_df =temp_df.join(integrate_sr)
integrate_df.reset_index(inplace=True)
integrate_df
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:311}" executionInfo="{&quot;elapsed&quot;:4751,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718576318532,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="XI-HH404ITTj" outputId="6dc1c2c3-20fd-448f-b147-8cd61756cab8">

``` python
#Visualización
days = integrate_df.Date.unique()

max_temp, min_temp = integrate_df.temp.max(), integrate_df.temp.min()
green =0.1

plt.figure(figsize=(20,5))

for d in days:
    BM = integrate_df.Date == d
    wdf = integrate_df[BM]

    average_temp = wdf.temp.mean()
    red = (average_temp - min_temp)/ (max_temp - min_temp)
    blue = 1-red
    clr = [red,green,blue]
    plt.plot(wdf.index,wdf.Consumption,c = clr)
BM = (integrate_df.Hour =='0:00') & (integrate_df.Date.str.contains('/28/'))
plt.xticks(integrate_df[BM].index,integrate_df[BM].Date,rotation=90)
plt.grid()
plt.margins(y=0,x=0)
plt.show()
```

</div>

<div class="cell markdown" id="KkHq6iXYIdhL">

### **Contexto**

Suponga que nos contratan para descubrir qué hace que una canción llegue al top 10 de Billboard (<https://www.billboard.com/charts/hot-100>) y permanezca allí durante al menos 5 semanas. Será neceseraio realizar un gráfico que clasifique las canciones populares según las ventas, la reproducción en la radio y la transmisión.

Para este ejercicio es necesario integrar datos desde tres recursos: billboardHot100_1999-2019.csv, songAttributes_1999-2019.csv, and artistDf.csv obtenidos de <https://www.kaggle.com/danield2255/data-on-songs-from-billboard-19992019>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:521}" executionInfo="{&quot;elapsed&quot;:5421,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718578984176,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="w5Uk45PSKHck" outputId="25e2689b-b4a5-4152-b090-8f82652f43c8">

``` python
billboard_df = pd.read_csv('billboardHot100_1999-2019.csv')
billboard_df.head()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:540}" executionInfo="{&quot;elapsed&quot;:1169,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718579091136,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2H87VMcFSlGF" outputId="d35761e7-74ba-4034-8507-add264d6159a">

``` python
songAttribute_df = pd.read_csv('songAttributes_1999-2019.csv')
songAttribute_df.head()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:241}" executionInfo="{&quot;elapsed&quot;:500,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718579127582,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="GK2eXgMaTA4U" outputId="0985af9c-8250-491b-b386-d6aec3d96d6d">

``` python
artist_df = pd.read_csv('artistDf.csv')
artist_df.head()
```

</div>

<div class="cell markdown" id="dNgTrAYYTHxr">

### **Ejercicio 2:**

Verique que si el dataset `billboard_df` tiende objecto de datos duplicados. En ese caso, eliminelos. *Hint*. Primero, cuente cuántas entradas existen según `Artists`, `Name` y `Week`. En base a ello, elimine.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:4135,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718578313157,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8C0pOT9YP615" outputId="867ba76d-ae80-4192-9d5d-3c87c838b4ba">

``` python
wsr = billboard_df.apply(lambda r: '{}-{}-{}'
                         .format(r.Artists,r.Name,r.Week),axis=1)
wsr.value_counts()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:323}" executionInfo="{&quot;elapsed&quot;:382,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718579386723,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Al3mdN5qQRYC" outputId="79eb6a6c-1db3-465b-debf-f0d8ef79d911">

``` python
billboard_df.query("Artists == '50 Cent' and Name=='Outta Control' \
                   and Week== '2005-09-14'")
```

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:450,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718579392032,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_PTxggnRQYzj">

``` python
billboard_df.drop(index = 67647,inplace=True)
```

</div>

<div class="cell markdown" id="uiej6XrgUcZY">

### **Ejercicio 3:**

Elimine los duplicados de los datasets `songAttributes_df` y `artist_df`.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:3719,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718579606684,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="svUInyYtU4lv" outputId="77013d2f-0dfd-40eb-cd2a-e152a7dbedb8">

``` python
songAttribute_df = pd.read_csv('songAttributes_1999-2019.csv')
wsr = songAttribute_df.apply(
    lambda r: '{}---{}'.format(r.Artist,r.Name),axis=1)
wsr.value_counts()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:355,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718579622080,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="W-1pA-XxU-G0" outputId="dccc5d02-4fd5-4655-92cf-b7239c4ed2d2">

``` python
songAttribute_df.query("Artist == 'Jose Feliciano' and Name == 'Light My Fire'")
```

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:926059,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718580743957,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="AQ7DDO6kVOtE">

``` python
doFrequencies = wsr.value_counts()
BM = doFrequencies>1

for i,v in doFrequencies[BM].items():
    [name,artist] = i.split('---')
    BM = ((songAttribute_df.Name == name) &
          (songAttribute_df.Artist == artist))
    wdf = songAttribute_df[BM]

    dropping_index = wdf.index[1:]
    songAttribute_df.drop(index = dropping_index,
                          inplace=True)
```

</div>

<div class="cell code">

``` python
# Otra forma
songAttribute_df['wsr'] = songAttribute_df['Name'] + '---' + songAttribute_df['Artist']

doFrequencies = songAttribute_df['wsr'].value_counts()
BM = doFrequencies > 1

songAttribute_df = songAttribute_df.drop_duplicates(subset='wsr', keep='first')
songAttribute_df.drop(columns='wsr', inplace=True)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2598,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718580979032,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="UO-ZhJpHV5jM" outputId="86a0740b-23a3-4142-824f-927a6d39d648">

``` python
wsr = songAttribute_df.apply(
    lambda r: '{}---{}'.format(r.Artist,r.Name),axis=1)
wsr.value_counts()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:332,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718580984358,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_v3TjLg0V_53" outputId="ad0990ad-b204-44ac-f9a6-4bf3235ed801">

``` python
artist_df.Artist.value_counts()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:147}" executionInfo="{&quot;elapsed&quot;:420,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718580991248,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="S9v_fxNbWDL0" outputId="7a46afbe-fc7f-4867-f343-89f645378c89">

``` python
artist_df.query("Artist == 'Reba McEntire'")
```

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:348,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718580995010,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2rWUBXyrWG0m">

``` python
artist_df.drop(index = 716, inplace=True)
```

</div>

<div class="cell markdown" id="MEAfNkStWI8A">

### **Ejercicio 4:**

Crea una DataFrame para que soporte la integración de datos.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:109}" executionInfo="{&quot;elapsed&quot;:344,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718580999144,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ePnXpLsEWWmO" outputId="6c1a3b9d-912d-4093-ab39-81a9c16a601d">

``` python
songIntegrate_df = pd.DataFrame(
    columns = ['Name', 'Artists', 'Top_song', 'First_date_on_Billboard',
               'Acousticness', 'Danceability', 'Duration', 'Energy',
               'Explicit', 'Instrumentalness', 'Liveness', 'Loudness',
               'Mode', 'Speechiness', 'Tempo', 'TimeSignature', 'Valence',
               'Artists_n_followers', 'n_male_artists', 'n_female_artists',
               'n_bands', 'artist_average_years_after_first_album',
               'artist_average_number_albums'])
songIntegrate_df
```

</div>

<div class="cell markdown" id="nVTZPQJqWZn8">

### **Ejercicio 5:**

Llenar `songIntegrate_df` a partir del dataset `billboard_df`.

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:119806,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718587915709,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="srvJ6eE6XNxg">

``` python
SongNames = billboard_df.Name.unique()

for i, song in enumerate(SongNames):
    BM = billboard_df.Name == song
    wdf = billboard_df[BM]

    Artists = wdf.Artists.unique()
    for artist in Artists:
        BM = wdf.Artists == artist
        wdf2 = wdf[BM]

        topsong = False

        BM = wdf2['Weekly.rank'] <=10
        if(len(wdf2[BM])>=5):
            topsong = True

        first_date_on_billboard = wdf2.Week.iloc[-1]
        dic_append = {'Name':song,'Artists':artist,
                      'Top_song':topsong,
                      'First_date_on_Billboard':
                      first_date_on_billboard}

        songIntegrate_df.loc[len(songIntegrate_df.index)] = dic_append
        #songIntegrate_df = pd.concat([songIntegrate_df, pd.DataFrame.from_dict(dic_append)], ignore_index=True)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:377}" executionInfo="{&quot;elapsed&quot;:338,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718588129319,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="DsjJSVC7XTG0" outputId="5adf6099-b18c-4ac5-9530-02209093840a">

``` python
songIntegrate_df.head()
```

</div>

<div class="cell markdown" id="BACjzCiRXYKr">

### **Ejercicio 6:**

Llenar `songIntegrate_df` a partir del dataset `songAttribute_df`. Revise todas las situaciones que existen.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:504}" executionInfo="{&quot;elapsed&quot;:327,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718588161267,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="lusuq1Dz1gbC" outputId="c6176f16-1463-4913-c691-200105f1ea7d">

``` python
songAttribute_df.head()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:687188,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718588881975,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="9BgWJQUXXeUJ" outputId="6ae5a4f4-cc91-4eec-def7-c1118ffe3056">

``` python
adding_columns = ['Acousticness','Danceability','Duration','Energy','Explicit','Instrumentalness',
                  'Liveness','Loudness','Mode','Speechiness','Tempo','TimeSignature', 'Valence']
template = 'Index= {} - The song {} by {} was integrated using sitution {}.'
for i, row in songIntegrate_df.iterrows():
    filled = False
    Artists = row.Artists.split(',')
    Artists = list(map(str.strip,Artists))
    # Situation 1
    BM = songAttribute_df.Name == row.Name
    if(sum(BM) == 1):
        for col in adding_columns:
            songIntegrate_df.loc[i,col]= songAttribute_df[BM][col].values[0]
        filled = True
        print(template.format(i,row.Name,row.Artists,1))
    # Situation 2
    elif(sum(BM) > 1):
        wdf = songAttribute_df[BM]
        if(len(Artists)==1):
            BM2 = wdf.Artist.str.contains(Artists[0])
            if(sum(BM2)==1):
                for col in adding_columns:
                    songIntegrate_df.loc[i,col]= wdf[BM2][col].values[0]
                filled = True
                print(template.format(i,row.Name,row.Artists,2))
    # Situation 3
    if((not filled) and len(Artists)>1):
        BM2= (songAttribute_df.Name.str.contains(row.Name)&songAttribute_df.Artist.isin(Artists))
        if(sum(BM2)==1):
            for col in adding_columns:
                songIntegrate_df.loc[i,col]= songAttribute_df[BM2][col].values[0]
            filled = True
            print(template.format(i,row.Name,row.Artists,3))
    if(not filled):
        # Situation 4
        BM2 = songAttribute_df.Name.str.contains(row.Name)
        if(sum(BM2)==1):
            for artist in Artists:
                if(artist == songAttribute_df[BM2].Artist.iloc[0]):
                    for col in adding_columns:
                        songIntegrate_df.loc[i,col]= songAttribute_df[BM2][col].values[0]
                    filled = True
                    print(template.format(i,row.Name,row.Artists,4))
        # Situation 5
        if(sum(BM2)>1):
            wdf2 = songAttribute_df[BM2]
            BM3 = wdf2.Artist.isin(Artists)
            if(sum(BM3)>0):
                wdf3 = wdf2[BM3]
                for i3, row3 in wdf3.iterrows():
                    if(row3.Name == row.Name):
                        for col in adding_columns:
                            songIntegrate_df.loc[i,col]= row3[col]
                        filled = True
                        print(template.format(i,row.Name,row.Artists,5))
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:377}" executionInfo="{&quot;elapsed&quot;:352,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718588901048,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pIBtk__1Xwh0" outputId="48f45953-0311-4b01-eb69-360388fd2833">

``` python
songIntegrate_df.head()
```

</div>

<div class="cell markdown" id="2z5U5tzPX678">

### **Ejercicio 7:**

Realizar la limpieza de datos de `songIntegrate_df` a nivel III en base a eliminar los datos faltantes.

Hint. Puede eliminar en base a un atributo. Por ejemplo, Acousticness.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:319,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718588910315,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="cjZzJj25X1AO" outputId="b5c057b7-66c4-44b0-babf-e7386f131a89">

``` python
songIntegrate_df.info()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:365,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589067892,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="eLMpFYFrYM-R" outputId="94dd3d6f-fc6f-485c-e412-0a7baaf7f95a">

``` python
B_MV = songIntegrate_df.Acousticness.isna()
B_MV.rename('Missing Values',inplace=True)
contigency_table = pd.crosstab(songIntegrate_df.Top_song,B_MV)
contigency_table
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:336,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589073658,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="5ydv79dLYkFe" outputId="034a963f-6ba5-494b-c112-3727340373e7">

``` python
from scipy.stats import chi2_contingency
p_value = chi2_contingency(contigency_table)[1]
p_value
```

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:334,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589078704,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="t-7jsWBwYz8f">

``` python
#Observando p_value, podemos concluir que no hay suficiente evidencia para
#rechazar la hipotesis que MV no tienen relación con las canciones sean top o no
dropping_index = songIntegrate_df[B_MV].index
songIntegrate_df.drop(index = dropping_index,inplace=True)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:502,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718589081854,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8MSAk_uIY2hG" outputId="b86263da-71f0-4544-d8dc-c871ed8747de">

``` python
songIntegrate_df.info()
```

</div>
