---
curso: ACD
titulo: U3_L5 DCNivel3_Outliers
slides: 0
fuente: U3_L5 DCNivel3_Outliers.ipynb
---

<div class="cell markdown" id="TueFxURvmu2Q">

# **U3_L5 Data Cleaning Nivel III: Outliers**

## **Objetivo:**

Al finalizar el laboratorio, el estudiante será capaz de manejar la presencia de outliers (valores atípicos) en una dataset.

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:503,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958911310,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="QC5iyRbUmreW">

``` python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

</div>

<div class="cell markdown" id="1tfdNGJrs_Bv">

Para este laboratorio utilizaremos data pública de Kaggle <https://www.kaggle.com/datasets/thomasnibb/amsterdam-house-price-prediction> sobre los precios de bienes raíces en la ciudad Amsterdam durante el año 2021.

</div>

<div class="cell markdown" id="ZdBfUgm8tWWL">

## **Paso 0: Cargar la data**

</div>

<div class="cell code" execution_count="2" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:450,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958914037,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aKnEurL0tZVV" outputId="8d280135-f506-4395-8ea4-f3919c070cee">

``` python
house_df = pd.read_csv("HousingPrices-Amsterdam-August-2021.csv")
house_df
```

<div class="output execute_result" execution_count="2">

         Unnamed: 0                                 Address      Zip     Price  \
    0             1            Blasiusstraat 8 2, Amsterdam  1091 CR  685000.0   
    1             2  Kromme Leimuidenstraat 13 H, Amsterdam  1059 EL  475000.0   
    2             3              Zaaiersweg 11 A, Amsterdam  1097 SM  850000.0   
    3             4            Tenerifestraat 40, Amsterdam  1060 TH  580000.0   
    4             5              Winterjanpad 21, Amsterdam  1036 KN  720000.0   
    ..          ...                                     ...      ...       ...   
    919         920                     Ringdijk, Amsterdam  1097 AE  750000.0   
    920         921         Kleine Beerstraat 31, Amsterdam  1033 CP  350000.0   
    921         922       Stuyvesantstraat 33 II, Amsterdam  1058 AK  350000.0   
    922         923   John Blankensteinstraat 51, Amsterdam  1095 MB  599000.0   
    923         924      S. F. van Ossstraat 334, Amsterdam  1068 JS  300000.0   

         Area  Room       Lon        Lat  
    0      64     3  4.907736  52.356157  
    1      60     3  4.850476  52.348586  
    2     109     4  4.944774  52.343782  
    3     128     6  4.789928  52.343712  
    4     138     5  4.902503  52.410538  
    ..    ...   ...       ...        ...  
    919   117     1  4.927757  52.354173  
    920    72     3  4.890612  52.414587  
    921    51     3  4.856935  52.363256  
    922   113     4  4.965731  52.375268  
    923    79     4  4.810678  52.355493  

    [924 rows x 8 columns]

</div>

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:479,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958917082,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="dlXSxlT8t4ez" outputId="eda9ae32-553d-40ed-f531-5039cc0f5ccf">

``` python
house_df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 924 entries, 0 to 923
    Data columns (total 8 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   Unnamed: 0  924 non-null    int64  
     1   Address     924 non-null    object 
     2   Zip         924 non-null    object 
     3   Price       920 non-null    float64
     4   Area        924 non-null    int64  
     5   Room        924 non-null    int64  
     6   Lon         924 non-null    float64
     7   Lat         924 non-null    float64
    dtypes: float64(3), int64(3), object(2)
    memory usage: 57.9+ KB

</div>

</div>

<div class="cell code" execution_count="4">

``` python
house_df.isnull().sum()
```

<div class="output execute_result" execution_count="4">

    Unnamed: 0    0
    Address       0
    Zip           0
    Price         4
    Area          0
    Room          0
    Lon           0
    Lat           0
    dtype: int64

</div>

</div>

<div class="cell markdown" id="56LariSn-svi">

## **I. Detección de Outliers**

</div>

<div class="cell markdown" id="uiItV90xnMx8">

### **A. Detección de Outliers Univariados**

</div>

<div class="cell markdown" id="7gqy71Q2uIiZ">

#### **Ejercicio 1:**

Crea un sub-dataframe que incluya los atributos `Price`, `Area` y `Room`. Para tener una idea general, obtén su resumen estadístico y observa cuáles son las características del dataset.

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:584,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958926609,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="VacQMqLKuvYW" outputId="99f063a8-b78d-486f-a8eb-fe79a35f17a7">

``` python
df = house_df[['Price','Area','Room']]
df.head()
```

<div class="output execute_result" execution_count="5">

          Price  Area  Room
    0  685000.0    64     3
    1  475000.0    60     3
    2  850000.0   109     4
    3  580000.0   128     6
    4  720000.0   138     5

</div>

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:300}" executionInfo="{&quot;elapsed&quot;:432,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958929940,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="3Ol-4MoUu605" outputId="f546bb8f-98cc-4af4-86d9-e57e5f3c6d52">

``` python
df.describe()
```

<div class="output execute_result" execution_count="6">

                  Price        Area        Room
    count  9.200000e+02  924.000000  924.000000
    mean   6.220654e+05   95.952381    3.571429
    std    5.389942e+05   57.447436    1.592332
    min    1.750000e+05   21.000000    1.000000
    25%    3.500000e+05   60.750000    3.000000
    50%    4.670000e+05   83.000000    3.000000
    75%    7.000000e+05  113.000000    4.000000
    max    5.950000e+06  623.000000   14.000000

</div>

</div>

<div class="cell markdown" id="RKjTu_bzvw2q">

#### **Ejercicio 2:**

Utilizando los métodos de vizualización detecte los outliers con respecto al atributo **Price** univariados a través de la función `histplot` y `boxplot` de **Seaborn**. Utilicemos como titulo "Análisis de Outliers de Precios" para los gráficos.

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:450}" executionInfo="{&quot;elapsed&quot;:1389,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958999359,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="wPe9bwsXwBrA" outputId="e4921887-9228-41e2-9b39-076a806f810b">

``` python
plt.figure(figsize = (40,18))
ax = sns.histplot(data= df, x= 'Price')
ax.set_xlabel('Precio en millones', fontsize = 30)
ax.set_ylabel('Frecuencia', fontsize = 30)
ax.set_title('Análisis de Outliers de Precios',fontsize = 40)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.show()
```

<div class="output display_data">

![](23b6263e203c9a5166af6d21d00f15d70bbebf9b.png)

</div>

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:468}" executionInfo="{&quot;elapsed&quot;:1103,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717959010617,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mpclSTf2xCG-" outputId="13696292-ac1d-47bb-d0c3-950790eb2e76">

``` python
plt.figure(figsize = (40,18))
ax = sns.boxplot(data= df, x= 'Price')
ax.set_xlabel('Precio en millones', fontsize = 30)
ax.set_title('Análisis de Outliers de Precios', fontsize = 40)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.show()
```

<div class="output display_data">

![](3e818c91a76566bf345cc9304742d877219667cb.png)

</div>

</div>

<div class="cell markdown" id="fJ-sXaHoyag5">

#### **Ejercicio 3:**

Nosotros no necesitabamos usar un boxplot para encontrar los outliers podriamos usar métodos estadísticos. Por ejemplo, un boxplot usa las siguientes formulas para calcular "the upper cap" y "the lower cap" del boxplot, donde $`Q1`$ y $`Q3`$ son el primer y el tercer quartil de la data:

``` math
 UpperCap = Q3 + 1.5* IQR 
```
``` math
 LowerCap = Q1 - 1.5 * IQR 
```
``` math
 IQR = Q3 -Q1 
```

Cualquier elemento mayor a "the upper cap" y menor a "the lower cap" es marcado como **outlier**.

Implemente el código para encontrar **los Precios outliers** en base al $`IQR`$.

Hint: Utiliza la función `quantile()` de Pandas.

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:499,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717959266173,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="teLJvF4kycm_" outputId="de8d8742-51d1-47ce-f492-bd94b62cd758">

``` python
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
```

<div class="output stream stdout">

    350000.0

</div>

</div>

<div class="cell code" execution_count="10">

``` python
'''D4 = df['Price'].quantile(0.40)
D4'''
```

<div class="output execute_result" execution_count="10">

    "D4 = df['Price'].quantile(0.40)\nD4"

</div>

</div>

<div class="cell code" execution_count="11" executionInfo="{&quot;elapsed&quot;:586,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717959273363,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="WAS-XPzRRs8Z">

``` python
uppercap = Q3 + 1.5 * IQR
lowercap = Q1 - 1.5 * IQR
```

</div>

<div class="cell code" execution_count="12">

``` python
df['Price']
```

<div class="output execute_result" execution_count="12">

    0      685000.0
    1      475000.0
    2      850000.0
    3      580000.0
    4      720000.0
             ...   
    919    750000.0
    920    350000.0
    921    350000.0
    922    599000.0
    923    300000.0
    Name: Price, Length: 924, dtype: float64

</div>

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:5,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958163033,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Qu1HIEuM0ejM" outputId="40179bbe-23f8-421f-f244-aeea6e8e08c7">

``` python
BM = (df['Price'] > uppercap) | (df['Price'] < lowercap)
BM
```

<div class="output execute_result" execution_count="13">

    0      False
    1      False
    2      False
    3      False
    4      False
           ...  
    919    False
    920    False
    921    False
    922    False
    923    False
    Name: Price, Length: 924, dtype: bool

</div>

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717959297114,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="rQFbCvER04hL" outputId="e22c9b95-cb8d-4137-eb55-3a6612e603b5">

``` python
#Outliers:
price_outliers = df[BM]['Price']
price_outliers
```

<div class="output execute_result" execution_count="14">

    20     1625000.0
    28     1650000.0
    31     1950000.0
    33     3925000.0
    57     1295000.0
             ...    
    885    1450000.0
    902    1300000.0
    906    1250000.0
    910    1698000.0
    917    1500000.0
    Name: Price, Length: 71, dtype: float64

</div>

</div>

<div class="cell code">

``` python
```

</div>

<div class="cell code">

``` python
```

</div>

<div class="cell markdown" id="yu1eahvy1uY5">

### **B. Detección de Outliers Bivariado**

</div>

<div class="cell markdown" id="v3NlerBL3_Vu">

#### **Ejercicio 4:**

Analice a través de un `scatterplot` (Seaborn) la relación entre `Price` y `Area` en la ciudad de Amnsterdan. Observe la presencia de los **outliers bivariados**.

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:452}" executionInfo="{&quot;elapsed&quot;:1738,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717959584049,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="clJlTPXp11fS" outputId="3d9d9186-8ccf-499c-cf7a-f1617c15e6d1">

``` python
plt.figure(figsize = (40,18))
ax = sns.scatterplot(data= df, x= 'Price', y = 'Area', s = 200)
ax.set_xlabel('Precio en millones', fontsize = 30)
ax.set_ylabel('Area',  fontsize = 30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
ax.set_title('Análisis de Outliers Bivariado entre Precios y Áreas', fontsize = 40)
plt.show()
```

<div class="output display_data">

![](bfa6ed66d85f73ba8d8a64a393921459be4b184b.png)

</div>

</div>

<div class="cell markdown" id="7KTNKOgw5lxS">

#### **Ejercicio 5:**

En el caso de los outliers bivariados, la única manera de obtener los outliers es utilizando los gráficos como apoyo para realizar *el Boolean mask*. En báse al gráfico del Ejercicio anterior, implemente:

1.  El código para encontrar los outliers bivariados `biv_outliers` entre **Price** y **Area**.
2.  El código para visualizar el gráfico anterior donde los outliers son pintados de otro color. Hint: párametro `hue = atributo`

</div>

<div class="cell code" execution_count="16">

``` python
df
```

<div class="output execute_result" execution_count="16">

            Price  Area  Room
    0    685000.0    64     3
    1    475000.0    60     3
    2    850000.0   109     4
    3    580000.0   128     6
    4    720000.0   138     5
    ..        ...   ...   ...
    919  750000.0   117     1
    920  350000.0    72     3
    921  350000.0    51     3
    922  599000.0   113     4
    923  300000.0    79     4

    [924 rows x 3 columns]

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:477,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717959660184,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="9dDk_dnI6JTU" outputId="113b65e9-8dd9-4a77-c3b5-b57cbcea22ee">

``` python
BM = (df.Price > 3000000.0) & (df.Area > 100)
BM
```

<div class="output execute_result" execution_count="17">

    0      False
    1      False
    2      False
    3      False
    4      False
           ...  
    919    False
    920    False
    921    False
    922    False
    923    False
    Length: 924, dtype: bool

</div>

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:332}" executionInfo="{&quot;elapsed&quot;:5,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717959692453,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RWlSjhEK6t17" outputId="f91920c8-2b57-4aac-eaf4-be2febc295ee">

``` python
biv_outliers = df[BM]
biv_outliers
```

<div class="output execute_result" execution_count="18">

             Price  Area  Room
    33   3925000.0   319     7
    103  4550000.0   497    13
    179  4495000.0   178     5
    195  5950000.0   394    10
    276  3500000.0   374     7
    301  3680000.0   374     4
    305  4900000.0   623    13
    334  3500000.0   348     8
    837  5850000.0   480    14

</div>

</div>

<div class="cell code" execution_count="19">

``` python
len(biv_outliers)
```

<div class="output execute_result" execution_count="19">

    9

</div>

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:431,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717960245670,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="xiQ1xMHmaN0n" outputId="f093731d-0244-4cb4-debe-2fa1bbb04041">

``` python
biv_outliers.index
```

<div class="output execute_result" execution_count="20">

    Index([33, 103, 179, 195, 276, 301, 305, 334, 837], dtype='int64')

</div>

</div>

<div class="cell code" execution_count="21" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:548,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717960303199,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="frc75y08ZGO8" outputId="53827592-db70-4d6e-dd26-95295f21784e">

``` python
df["outlier"] = [True if idx in biv_outliers.index else False for idx in df.index]
```

<div class="output stream stderr">

    C:\Users\JOSÉ\AppData\Local\Temp\ipykernel_2352\614871412.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      df["outlier"] = [True if idx in biv_outliers.index else False for idx in df.index]

</div>

</div>

<div class="cell code" execution_count="22" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:8,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717960330623,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="AlxtFWhQajdy" outputId="bf20eecc-baff-4f34-a8cf-5f87ac9135a5">

``` python
df
```

<div class="output execute_result" execution_count="22">

            Price  Area  Room  outlier
    0    685000.0    64     3    False
    1    475000.0    60     3    False
    2    850000.0   109     4    False
    3    580000.0   128     6    False
    4    720000.0   138     5    False
    ..        ...   ...   ...      ...
    919  750000.0   117     1    False
    920  350000.0    72     3    False
    921  350000.0    51     3    False
    922  599000.0   113     4    False
    923  300000.0    79     4    False

    [924 rows x 4 columns]

</div>

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:452}" executionInfo="{&quot;elapsed&quot;:2072,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717960377409,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="APXHwufXYfkg" outputId="2378c2b0-4c22-404c-cb7f-11847cc570f8">

``` python
plt.figure(figsize = (40,18))
ax = sns.scatterplot(data= df, x= 'Price', y = 'Area', s = 200, hue = 'outlier')
ax.set_xlabel('Precio en millones', fontsize = 30)
ax.set_ylabel('Area',  fontsize = 30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
ax.set_title('Análisis de Outliers Bivariado entre Precios y Áreas', fontsize = 40)
plt.show()
```

<div class="output display_data">

![](3ec7ff9daa70b66ae8e23bbcfc7180adc135f40c.png)

</div>

</div>

<div class="cell code">

``` python
#?sns.scatterplot
```

</div>

<div class="cell code">

``` python
```

</div>

<div class="cell markdown" id="pcWpgA3T47TA">

#### **Ejercicio 6:**

Detecte la presencia de outliers entre la relación de Precios y Habitaciones del dataset.

</div>

<div class="cell code" execution_count="24" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:458}" executionInfo="{&quot;elapsed&quot;:1179,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717960399123,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="BVt1xhir5IfC" outputId="0e20e45c-2f49-4b8f-86f5-3b3461b265c5">

``` python
plt.figure(figsize = (40,18))
ax = sns.boxplot(data= df,x = 'Room', y= 'Price')
ax.set_xlabel('Room', fontsize = 30)
ax.set_ylabel('Price',  fontsize = 30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
ax.set_title('Análisis de Outliers Bivariado entre Precios y Habitaciones', fontsize = 40)
plt.show()
```

<div class="output display_data">

![](26493927542559c1e73330155aee28dff6d64adc.png)

</div>

</div>

<div class="cell markdown" id="BHOB0YpUdcH4">

### **C. Detección de Outliers Multivariado**

</div>

<div class="cell markdown" id="CrX5YP0sdgCY">

#### **Ejercicio 7:**

Detectemos la presencia de Outliers entre **Precio**, **Area** y **Room** utilizando clustering (K-means).

</div>

<div class="cell code" execution_count="25" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717960685880,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="01q6JpF-b1Zc" outputId="72636bf9-cb1d-47ed-8141-ec61ee4f6c1e">

``` python
house_df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 924 entries, 0 to 923
    Data columns (total 8 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   Unnamed: 0  924 non-null    int64  
     1   Address     924 non-null    object 
     2   Zip         924 non-null    object 
     3   Price       920 non-null    float64
     4   Area        924 non-null    int64  
     5   Room        924 non-null    int64  
     6   Lon         924 non-null    float64
     7   Lat         924 non-null    float64
    dtypes: float64(3), int64(3), object(2)
    memory usage: 57.9+ KB

</div>

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:578,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717961238014,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="BicyrkPKbzI7" outputId="a0316b18-d117-423e-de23-57b417bcf8c7">

``` python
#Creamos XS con los atributos para el clustering
dimensions = ['Price', 'Area', 'Room']
Xs = house_df[dimensions]
Xs
```

<div class="output execute_result" execution_count="26">

            Price  Area  Room
    0    685000.0    64     3
    1    475000.0    60     3
    2    850000.0   109     4
    3    580000.0   128     6
    4    720000.0   138     5
    ..        ...   ...   ...
    919  750000.0   117     1
    920  350000.0    72     3
    921  350000.0    51     3
    922  599000.0   113     4
    923  300000.0    79     4

    [924 rows x 3 columns]

</div>

</div>

<div class="cell code" execution_count="31">

``` python
Xs.describe()
```

<div class="output execute_result" execution_count="31">

                  Price        Area        Room
    count  9.240000e+02  924.000000  924.000000
    mean   6.246755e+05   95.952381    3.571429
    std    5.392813e+05   57.447436    1.592332
    min    1.750000e+05   21.000000    1.000000
    25%    3.500000e+05   60.750000    3.000000
    50%    4.690000e+05   83.000000    3.000000
    75%    7.000000e+05  113.000000    4.000000
    max    5.950000e+06  623.000000   14.000000

</div>

</div>

<div class="cell code" execution_count="27" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:490,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717961285736,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="eo4w6d0KeKqW" outputId="245e1603-1d14-4399-d457-0ab6a6d64c0d">

``` python
#Verificamos la presencia de Valores Faltantes
Xs.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 924 entries, 0 to 923
    Data columns (total 3 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   Price   920 non-null    float64
     1   Area    924 non-null    int64  
     2   Room    924 non-null    int64  
    dtypes: float64(1), int64(2)
    memory usage: 21.8 KB

</div>

</div>

<div class="cell code" execution_count="28" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:606}" executionInfo="{&quot;elapsed&quot;:1096,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717961291957,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2ypI2QdBcOuy" outputId="dc81bd08-3725-41dc-863e-fbeebd425c57">

``` python
plt.figure(figsize=(4,7))
sns.heatmap(Xs.isna())
plt.show()
```

<div class="output display_data">

![](2d4b045cf9de8458c23292bfe2e51ad15b1b494b.png)

</div>

</div>

<div class="cell code" execution_count="30" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717961310064,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="dUQSnN9TcTDH">

``` python
#Manejamos la presencia de Valores Faltantes
Q3 = Xs.quantile(0.75)
Q1 = Xs.quantile(0.25)
IQR = Q3 - Q1
Xs = Xs.fillna(Q3+IQR*1.5)
Xs.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 924 entries, 0 to 923
    Data columns (total 3 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   Price   924 non-null    float64
     1   Area    924 non-null    int64  
     2   Room    924 non-null    int64  
    dtypes: float64(1), int64(2)
    memory usage: 21.8 KB

</div>

</div>

<div class="cell code" execution_count="32" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:638,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717961360126,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="7PBhmT9QcWFn" outputId="26ce0149-61fe-4bc9-9a6c-e3e131df0599">

``` python
#Estandarizamos el dataset
Xs = (Xs - Xs.min())/(Xs.max()-Xs.min())
Xs
```

<div class="output execute_result" execution_count="32">

            Price      Area      Room
    0    0.088312  0.071429  0.153846
    1    0.051948  0.064784  0.153846
    2    0.116883  0.146179  0.230769
    3    0.070130  0.177741  0.384615
    4    0.094372  0.194352  0.307692
    ..        ...       ...       ...
    919  0.099567  0.159468  0.000000
    920  0.030303  0.084718  0.153846
    921  0.030303  0.049834  0.153846
    922  0.073420  0.152824  0.230769
    923  0.021645  0.096346  0.230769

    [924 rows x 3 columns]

</div>

</div>

<div class="cell code" execution_count="33">

``` python
Xs.describe()
```

<div class="output execute_result" execution_count="33">

                Price        Area        Room
    count  924.000000  924.000000  924.000000
    mean     0.077866    0.124506    0.197802
    std      0.093382    0.095428    0.122487
    min      0.000000    0.000000    0.000000
    25%      0.030303    0.066030    0.153846
    50%      0.050909    0.102990    0.153846
    75%      0.090909    0.152824    0.230769
    max      1.000000    1.000000    1.000000

</div>

</div>

<div class="cell code" execution_count="34" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:490,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717961388670,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="zwTZoU4ucYFL" outputId="69b3ea3f-1115-4a80-f594-9fb9d14aa552">

``` python
#Aplicamos K-means
from sklearn.cluster import KMeans
for k in range(2,8):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(Xs)
    print('k={}'.format(k))
    for i in range(k):
        BM = kmeans.labels_==i
        print('Cluster {}: {}'.format(i,Xs[BM].index.values))
    print('--------- Divider ----------')
```

<div class="output stream stderr">

    C:\Users\Anaconda3\Lib\site-packages\joblib\externals\loky\backend\context.py:136: UserWarning: Could not find the number of physical cores for the following reason:
    [WinError 2] El sistema no puede encontrar el archivo especificado
    Returning the number of logical cores instead. You can silence this warning by setting LOKY_MAX_CPU_COUNT to the number of cores you want to use.
      warnings.warn(
      File "C:\Users\Anaconda3\Lib\site-packages\joblib\externals\loky\backend\context.py", line 257, in _count_physical_cores
        cpu_info = subprocess.run(
            "wmic CPU Get NumberOfCores /Format:csv".split(),
            capture_output=True,
            text=True,
        )
      File "C:\Users\Anaconda3\Lib\subprocess.py", line 554, in run
        with Popen(*popenargs, **kwargs) as process:
             ~~~~~^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Anaconda3\Lib\subprocess.py", line 1039, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
        ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                            pass_fds, cwd, env,
                            ^^^^^^^^^^^^^^^^^^^
        ...<5 lines>...
                            gid, gids, uid, umask,
                            ^^^^^^^^^^^^^^^^^^^^^^
                            start_new_session, process_group)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Anaconda3\Lib\subprocess.py", line 1554, in _execute_child
        hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
                                 # no special security
                                 ^^^^^^^^^^^^^^^^^^^^^
        ...<4 lines>...
                                 cwd,
                                 ^^^^
                                 startupinfo)
                                 ^^^^^^^^^^^^

</div>

<div class="output stream stdout">

    k=2
    Cluster 0: [  0   1   2   5   6   7   8   9  10  11  12  13  14  15  17  18  19  21
      22  23  24  25  26  27  29  30  32  34  35  36  37  38  40  41  42  43
      44  45  46  47  48  49  50  51  52  54  55  56  58  59  60  61  62  64
      65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82
      83  84  85  86  87  89  90  91  92  93  94  95  96  97  98  99 100 101
     102 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120
     121 122 124 126 127 128 129 130 131 132 133 135 136 138 139 140 141 143
     144 145 146 147 148 149 150 152 153 154 155 159 160 161 163 164 165 166
     168 169 170 172 173 174 175 176 178 181 183 185 186 187 188 189 190 191
     192 194 196 197 198 199 200 203 204 205 206 207 210 211 213 214 215 216
     219 221 222 223 224 225 226 227 228 229 230 232 236 237 238 239 240 242
     243 245 247 248 249 250 251 252 254 256 258 259 266 267 268 269 272 275
     277 278 282 283 285 289 290 291 293 294 297 298 299 300 303 307 310 311
     312 313 314 315 316 317 318 319 322 323 324 325 326 329 330 331 332 333
     335 337 338 339 340 341 343 345 347 348 349 350 351 353 354 355 356 357
     358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375
     376 377 378 379 380 381 382 383 385 386 387 388 389 390 391 392 393 395
     396 397 398 399 400 401 402 403 404 405 407 408 409 410 411 412 413 414
     415 416 417 418 419 420 421 422 424 425 426 427 428 429 430 431 432 433
     434 435 436 437 438 439 440 441 442 443 444 445 446 447 449 450 451 452
     455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 472 473
     474 475 476 477 479 480 481 482 483 485 486 487 488 489 490 492 493 494
     495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512
     513 514 515 516 517 518 519 520 521 522 523 524 525 526 528 529 530 531
     532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549
     550 551 552 553 554 555 556 557 558 559 560 561 563 564 565 566 567 568
     569 570 571 573 574 576 577 578 579 580 581 583 584 585 586 587 588 589
     590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607
     608 609 610 611 612 614 615 616 618 620 621 623 624 625 626 627 628 629
     630 631 632 633 634 636 637 638 639 640 642 644 645 646 648 649 650 651
     652 653 655 656 657 658 659 660 661 662 665 666 667 668 669 670 671 673
     674 675 676 677 678 679 680 681 682 683 684 686 687 688 689 690 691 693
     694 695 696 697 698 699 701 703 704 705 706 707 708 709 710 711 712 713
     714 715 716 717 718 719 720 721 722 723 724 727 729 731 732 733 734 735
     736 738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 756
     757 758 759 760 761 762 763 764 767 768 770 771 772 773 774 775 776 777
     778 779 780 781 782 783 784 785 787 788 790 791 792 793 794 796 798 799
     800 802 803 804 805 806 809 810 811 813 816 817 818 819 820 821 823 824
     825 826 827 828 830 831 832 833 834 835 836 838 839 840 841 842 843 845
     846 848 850 851 852 853 854 855 857 859 860 861 862 863 864 865 866 867
     868 869 870 871 872 873 874 875 876 877 878 879 880 881 882 883 884 886
     887 888 889 890 891 892 893 894 895 896 897 898 899 900 901 903 904 905
     907 908 909 911 912 913 914 915 916 918 919 920 921 922 923]
    Cluster 1: [  3   4  16  20  28  31  33  39  53  57  63  88 103 123 125 134 137 142
     151 156 157 158 162 167 171 177 179 180 182 184 193 195 201 202 208 209
     212 217 218 220 231 233 234 235 241 244 246 253 255 257 260 261 262 263
     264 265 270 271 273 274 276 279 280 281 284 286 287 288 292 295 296 301
     302 304 305 306 308 309 320 321 327 328 334 336 342 344 346 352 384 394
     406 423 448 453 454 471 478 484 491 527 562 572 575 582 613 617 619 622
     635 641 643 647 654 663 664 672 685 692 700 702 725 726 728 730 737 754
     755 765 766 769 786 789 795 797 801 807 808 812 814 815 822 829 837 844
     847 849 856 858 885 902 906 910 917]
    --------- Divider ----------
    k=3
    Cluster 0: [  0   1   5   6   7   8   9  10  11  12  13  14  17  18  19  21  22  23
      25  27  29  30  32  34  35  36  37  38  40  41  42  43  44  45  46  47
      48  49  50  51  52  54  55  56  58  59  60  61  62  64  65  66  67  68
      69  70  71  72  73  74  75  76  78  79  80  81  82  83  84  85  86  87
      89  91  92  93  94  95  96  97  98  99 100 101 102 104 105 106 107 108
     109 110 111 112 113 114 115 117 118 119 120 121 122 124 126 127 128 129
     130 131 132 135 138 139 140 141 143 144 145 146 147 148 149 150 152 153
     154 159 160 161 163 164 165 166 168 169 170 175 176 178 181 183 185 186
     187 188 190 191 192 194 196 197 198 199 203 204 205 206 210 211 213 214
     215 216 219 221 223 224 225 226 227 228 229 230 232 236 237 238 240 242
     243 247 248 249 250 251 252 254 256 258 266 268 269 272 275 277 278 283
     285 290 291 297 299 300 303 307 310 311 313 314 315 317 318 319 322 324
     325 326 330 331 332 335 337 338 339 340 341 343 347 348 349 350 351 353
     354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371
     372 373 374 376 377 378 379 380 381 382 383 385 386 387 388 389 390 391
     392 393 395 396 397 398 399 400 401 402 403 404 405 407 408 409 410 411
     412 413 414 415 416 417 418 419 420 421 422 424 425 426 427 428 429 430
     431 432 433 434 435 436 437 438 440 441 442 443 444 445 446 447 449 450
     451 452 455 456 458 459 460 461 462 463 464 465 466 467 468 469 470 473
     474 475 476 477 479 480 481 482 485 486 487 488 490 492 494 495 496 497
     498 499 500 501 502 503 504 505 506 508 509 510 511 512 513 514 515 516
     517 518 519 520 521 522 523 524 525 526 528 529 530 531 532 533 534 535
     536 537 538 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554
     555 556 558 560 561 563 564 565 566 567 568 569 570 573 574 576 577 578
     579 580 581 583 584 585 586 587 588 589 590 591 592 593 594 595 596 599
     600 601 602 603 604 605 606 607 608 609 610 611 612 614 615 616 618 620
     621 623 624 625 626 628 632 633 636 637 638 639 640 642 644 645 646 648
     649 650 651 652 653 655 656 658 659 660 661 662 665 667 668 669 670 671
     674 675 676 677 678 679 680 681 682 683 684 686 687 688 689 690 691 693
     694 695 696 697 698 699 701 703 704 705 707 708 709 710 711 712 713 716
     717 718 719 720 721 722 724 727 729 731 732 734 735 736 738 739 741 742
     743 744 745 746 747 748 749 750 751 752 753 756 757 758 759 760 761 762
     763 768 770 771 773 774 775 776 777 778 780 781 782 783 784 785 787 790
     791 792 793 794 796 798 799 800 803 804 805 806 810 811 813 816 817 818
     820 821 823 824 825 826 827 828 831 832 833 834 835 838 839 840 841 842
     843 845 846 848 850 851 852 853 854 855 857 859 860 861 862 864 865 866
     867 868 869 870 871 872 873 874 875 876 877 878 880 881 882 883 884 886
     888 889 890 891 892 893 894 895 896 897 898 899 900 901 903 904 905 907
     908 909 911 912 915 916 918 919 920 921 922 923]
    Cluster 1: [ 33 103 179 195 231 261 264 276 295 301 305 308 321 334 837]
    Cluster 2: [  2   3   4  15  16  20  24  26  28  31  39  53  57  63  77  88  90 116
     123 125 133 134 136 137 142 151 155 156 157 158 162 167 171 172 173 174
     177 180 182 184 189 193 200 201 202 207 208 209 212 217 218 220 222 233
     234 235 239 241 244 245 246 253 255 257 259 260 262 263 265 267 270 271
     273 274 279 280 281 282 284 286 287 288 289 292 293 294 296 298 302 304
     306 309 312 316 320 323 327 328 329 333 336 342 344 345 346 352 375 384
     394 406 423 439 448 453 454 457 471 472 478 483 484 489 491 493 507 527
     539 557 559 562 571 572 575 582 597 598 613 617 619 622 627 629 630 631
     634 635 641 643 647 654 657 663 664 666 672 673 685 692 700 702 706 714
     715 723 725 726 728 730 733 737 740 754 755 764 765 766 767 769 772 779
     786 788 789 795 797 801 802 807 808 809 812 814 815 819 822 829 830 836
     844 847 849 856 858 863 879 885 887 902 906 910 913 914 917]
    --------- Divider ----------
    k=4
    Cluster 0: [  2   4  15  16  22  24  26  30  42  44  49  51  55  56  59  60  61  63
      71  73  74  75  77  81  84  90 113 116 120 126 130 133 136 137 140 141
     143 145 149 150 152 155 163 164 165 168 170 171 172 173 174 178 181 183
     185 186 187 189 193 194 196 200 202 207 208 211 213 215 216 222 225 229
     234 235 238 239 242 243 244 245 251 256 259 267 270 275 282 283 289 290
     291 293 294 297 298 300 303 306 307 309 312 314 315 316 317 318 319 322
     323 329 330 331 333 335 336 339 340 342 345 346 353 356 358 363 372 373
     375 377 384 387 388 392 394 400 405 406 408 410 420 421 423 426 436 439
     441 443 444 448 451 453 457 465 470 471 472 479 482 483 485 486 489 491
     493 495 502 503 505 507 517 524 532 535 539 542 547 548 549 550 552 553
     555 557 559 560 561 564 566 571 572 573 578 582 596 597 598 599 602 606
     607 609 610 611 617 623 627 629 630 631 632 633 634 646 651 652 657 661
     662 666 668 673 676 677 679 681 684 688 691 694 700 703 704 706 714 715
     717 720 723 727 730 731 733 736 740 742 743 744 748 750 754 756 757 762
     763 764 765 767 769 771 772 774 779 785 788 789 790 792 793 795 797 799
     800 802 806 809 810 813 815 817 818 819 822 829 830 833 836 841 842 844
     845 846 848 851 852 856 858 860 862 863 865 869 870 874 879 884 887 888
     891 896 897 904 908 909 911 912 913 914 915 916 922 923]
    Cluster 1: [  3  20  28  31  39  53  57  88 123 125 134 142 151 156 157 158 162 167
     177 180 182 184 201 209 212 217 218 220 231 233 241 246 253 255 257 260
     261 262 263 265 271 273 274 279 280 281 284 286 287 288 292 296 302 304
     320 327 328 344 352 454 478 484 527 562 575 613 619 622 635 641 643 647
     654 663 664 672 685 692 702 725 726 728 737 755 766 786 801 807 808 812
     814 847 849 885 902 906 910 917]
    Cluster 2: [ 33 103 179 195 264 276 295 301 305 308 321 334 837]
    Cluster 3: [  0   1   5   6   7   8   9  10  11  12  13  14  17  18  19  21  23  25
      27  29  32  34  35  36  37  38  40  41  43  45  46  47  48  50  52  54
      58  62  64  65  66  67  68  69  70  72  76  78  79  80  82  83  85  86
      87  89  91  92  93  94  95  96  97  98  99 100 101 102 104 105 106 107
     108 109 110 111 112 114 115 117 118 119 121 122 124 127 128 129 131 132
     135 138 139 144 146 147 148 153 154 159 160 161 166 169 175 176 188 190
     191 192 197 198 199 203 204 205 206 210 214 219 221 223 224 226 227 228
     230 232 236 237 240 247 248 249 250 252 254 258 266 268 269 272 277 278
     285 299 310 311 313 324 325 326 332 337 338 341 343 347 348 349 350 351
     354 355 357 359 360 361 362 364 365 366 367 368 369 370 371 374 376 378
     379 380 381 382 383 385 386 389 390 391 393 395 396 397 398 399 401 402
     403 404 407 409 411 412 413 414 415 416 417 418 419 422 424 425 427 428
     429 430 431 432 433 434 435 437 438 440 442 445 446 447 449 450 452 455
     456 458 459 460 461 462 463 464 466 467 468 469 473 474 475 476 477 480
     481 487 488 490 492 494 496 497 498 499 500 501 504 506 508 509 510 511
     512 513 514 515 516 518 519 520 521 522 523 525 526 528 529 530 531 533
     534 536 537 538 540 541 543 544 545 546 551 554 556 558 563 565 567 568
     569 570 574 576 577 579 580 581 583 584 585 586 587 588 589 590 591 592
     593 594 595 600 601 603 604 605 608 612 614 615 616 618 620 621 624 625
     626 628 636 637 638 639 640 642 644 645 648 649 650 653 655 656 658 659
     660 665 667 669 670 671 674 675 678 680 682 683 686 687 689 690 693 695
     696 697 698 699 701 705 707 708 709 710 711 712 713 716 718 719 721 722
     724 729 732 734 735 738 739 741 745 746 747 749 751 752 753 758 759 760
     761 768 770 773 775 776 777 778 780 781 782 783 784 787 791 794 796 798
     803 804 805 811 816 820 821 823 824 825 826 827 828 831 832 834 835 838
     839 840 843 850 853 854 855 857 859 861 864 866 867 868 871 872 873 875
     876 877 878 880 881 882 883 886 889 890 892 893 894 895 898 899 900 901
     903 905 907 918 919 920 921]
    --------- Divider ----------
    k=5
    Cluster 0: [  5   7   9  13  29  35  36  38  62  65  68  78  80  82  83  85  86  91
      92  93  94  99 104 108 115 121 124 128 131 132 138 144 146 147 153 154
     159 166 169 176 188 190 192 210 219 221 226 227 230 232 236 247 248 258
     268 269 272 285 299 310 324 326 347 350 354 362 365 368 370 371 376 378
     381 382 389 391 393 399 401 409 416 425 428 429 430 431 432 433 435 437
     446 449 450 452 455 459 460 461 462 469 473 474 476 481 487 490 494 496
     499 500 508 509 510 513 514 515 516 518 519 521 522 529 530 533 534 537
     538 540 545 563 565 567 568 570 580 585 588 590 591 600 608 615 620 621
     628 640 650 658 665 667 669 670 674 687 689 690 696 697 699 701 705 712
     721 729 732 734 735 738 739 746 747 770 778 780 782 787 798 803 821 823
     825 826 827 832 835 843 853 854 859 866 867 868 877 878 881 882 886 898
     900 918 919]
    Cluster 1: [  2   3   4  15  16  22  24  26  42  44  49  51  55  56  59  60  61  63
      71  74  75  77  81  84  90 113 116 120 130 133 136 137 140 141 145 149
     150 152 155 163 164 168 170 171 173 178 181 183 185 186 187 189 193 196
     200 202 207 208 211 215 216 222 229 234 235 239 244 245 246 251 259 267
     270 275 282 286 290 293 294 297 298 303 306 309 312 316 322 323 329 330
     331 333 335 336 339 340 342 345 353 356 358 373 375 377 388 392 394 400
     405 406 408 410 420 421 423 426 436 439 443 444 448 451 453 457 465 470
     471 472 479 482 483 485 486 489 491 493 495 502 503 505 507 517 524 527
     532 535 539 548 550 552 553 555 557 559 560 561 564 566 571 572 573 582
     596 597 598 599 602 607 609 611 617 623 627 629 630 631 632 634 651 652
     657 661 662 666 668 673 677 679 681 684 688 691 692 694 700 704 706 714
     715 717 720 723 730 733 736 740 743 744 748 750 754 756 757 762 763 764
     765 767 771 772 774 779 788 790 795 797 799 800 801 802 806 807 809 810
     814 815 817 818 819 822 830 833 836 841 842 844 845 846 848 851 852 856
     858 860 862 863 865 869 879 884 887 888 896 897 904 908 909 911 912 913
     914 915 916 922 923]
    Cluster 2: [ 33 103 179 195 264 276 295 301 305 308 321 334 837]
    Cluster 3: [ 20  28  31  39  53  57  88 123 125 134 142 151 156 157 158 162 167 177
     180 182 184 201 209 212 217 218 220 231 233 241 253 255 257 260 261 262
     263 265 271 273 274 279 280 281 284 287 288 292 296 302 304 320 327 328
     344 346 352 384 454 478 484 562 575 613 619 622 635 641 643 647 654 663
     664 672 685 702 725 726 728 737 755 766 769 786 789 808 812 829 847 849
     885 902 906 910 917]
    Cluster 4: [  0   1   6   8  10  11  12  14  17  18  19  21  23  25  27  30  32  34
      37  40  41  43  45  46  47  48  50  52  54  58  64  66  67  69  70  72
      73  76  79  87  89  95  96  97  98 100 101 102 105 106 107 109 110 111
     112 114 117 118 119 122 126 127 129 135 139 143 148 160 161 165 172 174
     175 191 194 197 198 199 203 204 205 206 213 214 223 224 225 228 237 238
     240 242 243 249 250 252 254 256 266 277 278 283 289 291 300 307 311 313
     314 315 317 318 319 325 332 337 338 341 343 348 349 351 355 357 359 360
     361 363 364 366 367 369 372 374 379 380 383 385 386 387 390 395 396 397
     398 402 403 404 407 411 412 413 414 415 417 418 419 422 424 427 434 438
     440 441 442 445 447 456 458 463 464 466 467 468 475 477 480 488 492 497
     498 501 504 506 511 512 520 523 525 526 528 531 536 541 542 543 544 546
     547 549 551 554 556 558 569 574 576 577 578 579 581 583 584 586 587 589
     592 593 594 595 601 603 604 605 606 610 612 614 616 618 624 625 626 633
     636 637 638 639 642 644 645 646 648 649 653 655 656 659 660 671 675 676
     678 680 682 683 686 693 695 698 703 707 708 709 710 711 713 716 718 719
     722 724 727 731 741 742 745 749 751 752 753 758 759 760 761 768 773 775
     776 777 781 783 784 785 791 792 793 794 796 804 805 811 813 816 820 824
     828 831 834 838 839 840 850 855 857 861 864 870 871 872 873 874 875 876
     880 883 889 890 891 892 893 894 895 899 901 903 905 907 920 921]
    --------- Divider ----------
    k=6
    Cluster 0: [  5   7   9  13  29  35  36  38  62  65  68  78  80  82  83  85  86  87
      91  92  93  94  99 104 108 115 121 124 128 131 132 138 144 146 147 153
     154 159 166 169 176 188 190 192 210 219 221 226 227 230 232 236 247 248
     258 268 269 272 285 299 310 324 326 347 350 354 362 365 368 370 371 376
     378 381 382 389 391 393 399 401 409 416 425 428 429 430 431 432 433 435
     437 446 449 450 452 455 459 460 461 462 469 473 474 476 481 487 490 494
     496 499 500 508 509 510 513 514 515 516 518 519 521 522 529 530 533 534
     537 538 540 545 563 565 567 568 570 580 585 588 590 591 600 608 615 620
     621 628 640 650 658 665 667 669 670 674 687 689 690 696 697 699 701 705
     712 721 729 732 734 735 738 739 746 747 770 778 780 782 787 798 803 821
     823 825 826 827 832 835 843 853 854 859 866 867 868 877 878 881 882 886
     898 900 918 919]
    Cluster 1: [ 28  33 156 179 209 217 231 253 261 263 264 274 276 292 295 301 304 308
     321 334 575 613 685 755 906 917]
    Cluster 2: [ 20  31  53  57  73  88 123 125 136 137 155 157 165 171 172 174 177 180
     184 193 198 200 201 202 218 220 233 238 239 241 243 255 257 259 260 262
     279 280 281 283 287 288 289 291 314 316 317 320 327 344 345 346 352 384
     439 610 629 630 631 641 646 663 664 666 702 714 723 737 742 769 785 789
     829 847 849 856 885 902 910]
    Cluster 3: [103 195 305 837]
    Cluster 4: [  3   4  15  16  24  26  39  63  77  90 116 133 134 142 151 158 162 167
     182 207 208 212 222 234 235 244 246 265 267 270 271 273 282 284 286 293
     294 296 302 306 309 312 323 328 333 336 342 375 394 406 423 448 453 454
     457 471 472 478 484 489 491 493 507 527 539 557 559 562 571 572 582 597
     598 617 619 622 635 643 647 654 657 672 673 692 700 706 715 725 726 728
     730 733 754 764 765 766 767 779 786 788 795 797 801 802 807 808 809 812
     814 815 819 822 830 836 844 858 863 887 914]
    Cluster 5: [  0   1   2   6   8  10  11  12  14  17  18  19  21  22  23  25  27  30
      32  34  37  40  41  42  43  44  45  46  47  48  49  50  51  52  54  55
      56  58  59  60  61  64  66  67  69  70  71  72  74  75  76  79  81  84
      89  95  96  97  98 100 101 102 105 106 107 109 110 111 112 113 114 117
     118 119 120 122 126 127 129 130 135 139 140 141 143 145 148 149 150 152
     160 161 163 164 168 170 173 175 178 181 183 185 186 187 189 191 194 196
     197 199 203 204 205 206 211 213 214 215 216 223 224 225 228 229 237 240
     242 245 249 250 251 252 254 256 266 275 277 278 290 297 298 300 303 307
     311 313 315 318 319 322 325 329 330 331 332 335 337 338 339 340 341 343
     348 349 351 353 355 356 357 358 359 360 361 363 364 366 367 369 372 373
     374 377 379 380 383 385 386 387 388 390 392 395 396 397 398 400 402 403
     404 405 407 408 410 411 412 413 414 415 417 418 419 420 421 422 424 426
     427 434 436 438 440 441 442 443 444 445 447 451 456 458 463 464 465 466
     467 468 470 475 477 479 480 482 483 485 486 488 492 495 497 498 501 502
     503 504 505 506 511 512 517 520 523 524 525 526 528 531 532 535 536 541
     542 543 544 546 547 548 549 550 551 552 553 554 555 556 558 560 561 564
     566 569 573 574 576 577 578 579 581 583 584 586 587 589 592 593 594 595
     596 599 601 602 603 604 605 606 607 609 611 612 614 616 618 623 624 625
     626 627 632 633 634 636 637 638 639 642 644 645 648 649 651 652 653 655
     656 659 660 661 662 668 671 675 676 677 678 679 680 681 682 683 684 686
     688 691 693 694 695 698 703 704 707 708 709 710 711 713 716 717 718 719
     720 722 724 727 731 736 740 741 743 744 745 748 749 750 751 752 753 756
     757 758 759 760 761 762 763 768 771 772 773 774 775 776 777 781 783 784
     790 791 792 793 794 796 799 800 804 805 806 810 811 813 816 817 818 820
     824 828 831 833 834 838 839 840 841 842 845 846 848 850 851 852 855 857
     860 861 862 864 865 869 870 871 872 873 874 875 876 879 880 883 884 888
     889 890 891 892 893 894 895 896 897 899 901 903 904 905 907 908 909 911
     912 913 915 916 920 921 922 923]
    --------- Divider ----------
    k=7
    Cluster 0: [ 31  73 136 137 143 155 165 171 172 173 174 177 184 193 198 200 202 203
     213 225 238 239 242 243 256 259 283 287 288 289 291 300 314 316 317 318
     319 345 346 363 384 439 594 610 629 630 631 646 663 666 676 703 714 723
     727 731 742 769 785 789 792 793 829 856 891]
    Cluster 1: [ 33 103 179 195 264 276 295 301 305 308 334 837]
    Cluster 2: [  2  15  22  24  42  44  49  51  55  56  59  60  61  71  74  75  77  81
      84 113 116 120 130 140 141 145 149 150 152 163 164 168 170 178 181 183
     185 186 187 189 196 211 215 216 229 245 251 275 282 290 294 297 298 303
     322 329 330 331 333 335 339 340 353 356 358 373 375 377 388 392 400 405
     408 410 420 421 426 436 443 444 451 457 465 470 479 482 483 485 486 493
     495 502 503 505 507 517 524 532 535 539 548 550 552 553 555 557 560 561
     564 566 571 573 578 596 597 599 602 607 609 611 623 627 632 634 651 652
     657 661 662 668 673 677 679 681 684 688 691 694 704 717 720 736 740 743
     744 748 750 756 757 762 763 764 767 771 772 774 790 799 800 802 806 810
     817 818 833 841 842 845 846 848 851 852 860 862 865 869 879 884 887 888
     896 897 904 908 909 911 912 913 915 916 922 923]
    Cluster 3: [  5   7   9  13  29  35  36  38  62  65  68  78  80  82  83  85  86  91
      92  93  94  99 104 108 115 121 124 128 131 132 138 144 146 147 153 154
     159 166 169 176 188 190 192 210 219 221 226 227 230 232 236 247 248 258
     268 269 272 285 299 324 326 347 350 354 362 365 368 370 371 376 378 381
     382 389 391 393 399 401 409 416 425 428 429 430 431 432 433 435 437 446
     449 450 452 455 459 460 461 462 469 473 474 476 481 487 490 494 496 499
     500 508 509 510 513 514 515 516 518 519 521 522 529 530 533 534 537 538
     540 545 563 565 567 568 570 580 585 588 590 591 600 608 615 620 621 628
     640 650 658 665 667 669 670 674 687 689 690 696 697 699 701 705 712 721
     729 732 734 735 738 739 746 747 770 778 780 782 787 798 803 821 823 825
     826 827 832 835 843 853 854 859 866 867 868 877 878 881 882 886 898 900
     918 919]
    Cluster 4: [ 20  28  88 142 156 157 158 162 182 209 217 220 231 233 253 257 261 263
     265 271 274 279 280 281 284 292 304 320 321 328 575 613 619 664 685 755
     766 786 808 885 906 910 917]
    Cluster 5: [  0   1   6   8  10  11  12  14  17  18  19  21  23  25  27  30  32  34
      37  40  41  43  45  46  47  48  50  52  54  58  64  66  67  69  70  72
      76  79  87  89  95  96  97  98 100 101 102 105 106 107 109 110 111 112
     114 117 118 119 122 126 127 129 135 139 148 160 161 175 191 194 197 199
     204 205 206 214 223 224 228 237 240 249 250 252 254 266 277 278 307 310
     311 313 315 325 332 337 338 341 343 348 349 351 355 357 359 360 361 364
     366 367 369 372 374 379 380 383 385 386 387 390 395 396 397 398 402 403
     404 407 411 412 413 414 415 417 418 419 422 424 427 434 438 440 441 442
     445 447 456 458 463 464 466 467 468 475 477 480 488 492 497 498 501 504
     506 511 512 520 523 525 526 528 531 536 541 542 543 544 546 547 549 551
     554 556 558 569 574 576 577 579 581 583 584 586 587 589 592 593 595 601
     603 604 605 606 612 614 616 618 624 625 626 633 636 637 638 639 642 644
     645 648 649 653 655 656 659 660 671 675 678 680 682 683 686 693 695 698
     707 708 709 710 711 713 716 718 719 722 724 741 745 749 751 752 753 758
     759 760 761 768 773 775 776 777 781 783 784 791 794 796 804 805 811 813
     816 820 824 828 831 834 838 839 840 850 855 857 861 864 870 871 872 873
     874 875 876 880 883 889 890 892 893 894 895 899 901 903 905 907 920 921]
    Cluster 6: [  3   4  16  26  39  53  57  63  90 123 125 133 134 151 167 180 201 207
     208 212 218 222 234 235 241 244 246 255 260 262 267 270 273 286 293 296
     302 306 309 312 323 327 336 342 344 352 394 406 423 448 453 454 471 472
     478 484 489 491 527 559 562 572 582 598 617 622 635 641 643 647 654 672
     692 700 702 706 715 725 726 728 730 733 737 754 765 779 788 795 797 801
     807 809 812 814 815 819 822 830 836 844 847 849 858 863 902 914]
    --------- Divider ----------

</div>

<div class="output stream stderr">

    C:\Users\Anaconda3\Lib\site-packages\sklearn\cluster\_kmeans.py:1419: UserWarning: KMeans is known to have a memory leak on Windows with MKL, when there are less chunks than available threads. You can avoid it by setting the environment variable OMP_NUM_THREADS=4.
      warnings.warn(
    C:\Users\Anaconda3\Lib\site-packages\sklearn\cluster\_kmeans.py:1419: UserWarning: KMeans is known to have a memory leak on Windows with MKL, when there are less chunks than available threads. You can avoid it by setting the environment variable OMP_NUM_THREADS=4.
      warnings.warn(
    C:\Users\Anaconda3\Lib\site-packages\sklearn\cluster\_kmeans.py:1419: UserWarning: KMeans is known to have a memory leak on Windows with MKL, when there are less chunks than available threads. You can avoid it by setting the environment variable OMP_NUM_THREADS=4.
      warnings.warn(
    C:\Users\Anaconda3\Lib\site-packages\sklearn\cluster\_kmeans.py:1419: UserWarning: KMeans is known to have a memory leak on Windows with MKL, when there are less chunks than available threads. You can avoid it by setting the environment variable OMP_NUM_THREADS=4.
      warnings.warn(
    C:\Users\Anaconda3\Lib\site-packages\sklearn\cluster\_kmeans.py:1419: UserWarning: KMeans is known to have a memory leak on Windows with MKL, when there are less chunks than available threads. You can avoid it by setting the environment variable OMP_NUM_THREADS=4.
      warnings.warn(
    C:\Users\Anaconda3\Lib\site-packages\sklearn\cluster\_kmeans.py:1419: UserWarning: KMeans is known to have a memory leak on Windows with MKL, when there are less chunks than available threads. You can avoid it by setting the environment variable OMP_NUM_THREADS=4.
      warnings.warn(

</div>

</div>

<div class="cell code" execution_count="54">

``` python
# Distancias de Mahalanobis
from scipy.spatial.distance import mahalanobis
import scipy as sp
X = Xs
Sx = X.cov().values
IC = np.linalg.pinv(Sx)
media = X.mean().values
```

</div>

<div class="cell code" execution_count="55">

``` python
def mahalanobisR(X,media,IC):
    m = []
    for i in range(X.shape[0]):
        m.append(mahalanobis(X.iloc[i,:],media,IC)**2)
    return(m)

Xs["distMaha"] = pd.DataFrame(mahalanobisR(X,media,IC),columns=["distMaha"])
Xs
```

<div class="output execute_result" execution_count="55">

            Price      Area      Room   distMaha
    0    0.088312  0.071429  0.153846   1.476266
    1    0.051948  0.064784  0.153846   0.690917
    2    0.116883  0.146179  0.230769   0.268207
    3    0.070130  0.177741  0.384615   4.136965
    4    0.094372  0.194352  0.307692   1.280838
    ..        ...       ...       ...        ...
    919  0.099567  0.159468  0.000000  11.390329
    920  0.030303  0.084718  0.153846   0.266978
    921  0.030303  0.049834  0.153846   0.950932
    922  0.073420  0.152824  0.230769   0.365722
    923  0.021645  0.096346  0.230769   1.094673

    [924 rows x 4 columns]

</div>

</div>

<div class="cell code" execution_count="56">

``` python
Xs['index'] = Xs.index
Xs = Xs.reset_index(drop=True)
Xs
```

<div class="output execute_result" execution_count="56">

            Price      Area      Room   distMaha  index
    0    0.088312  0.071429  0.153846   1.476266      0
    1    0.051948  0.064784  0.153846   0.690917      1
    2    0.116883  0.146179  0.230769   0.268207      2
    3    0.070130  0.177741  0.384615   4.136965      3
    4    0.094372  0.194352  0.307692   1.280838      4
    ..        ...       ...       ...        ...    ...
    919  0.099567  0.159468  0.000000  11.390329    919
    920  0.030303  0.084718  0.153846   0.266978    920
    921  0.030303  0.049834  0.153846   0.950932    921
    922  0.073420  0.152824  0.230769   0.365722    922
    923  0.021645  0.096346  0.230769   1.094673    923

    [924 rows x 5 columns]

</div>

</div>

<div class="cell code" execution_count="58">

``` python
plt.scatter(Xs['index'],Xs['distMaha'])
plt.xlabel('Índice')
plt.ylabel('Distancia de Mahalanobis')
plt.show()
```

<div class="output display_data">

![](44ebf5e8d7e2ef16a4dde30a1ccc691679ba6671.png)

</div>

</div>

<div class="cell code" execution_count="61">

``` python
Xs_elim = Xs[Xs['distMaha'] > 30]
Xs_elim
```

<div class="output execute_result" execution_count="61">

            Price      Area      Room    distMaha  index
    33   0.649351  0.495017  0.461538   42.685042     33
    103  0.757576  0.790698  0.923077   56.660730    103
    179  0.748052  0.260797  0.307692  118.929576    179
    195  1.000000  0.619601  0.692308  128.346523    195
    243  0.125368  0.393688  0.000000   73.078783    243
    276  0.575758  0.586379  0.461538   36.193781    276
    301  0.606926  0.586379  0.230769   66.499127    301
    305  0.818182  1.000000  0.923077   91.091286    305
    308  0.263203  0.740864  1.000000   79.509492    308
    321  0.181818  0.573090  0.846154   49.757484    321
    837  0.982684  0.762458  1.000000  110.245198    837

</div>

</div>

<div class="cell markdown" id="xS7DEnLh_GTs">

## **II. Manejo de Outliers**

</div>

<div class="cell markdown" id="2J7WfEeOfCD9">

### **A. Outliers Univariados**

</div>

<div class="cell markdown" id="361XMb3H_Qex">

#### **Ejercicio 8:**

Compare la visualización del histograma de Precios con outliers y sin outliers. ¿en qué escenarios sería mejor usar uno u otro?.

Hint. Utilice un subplot para una mejor comparación.

</div>

<div class="cell code" execution_count="35" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:7,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717961763467,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KsUzaxUggAcO" outputId="332ac39b-5ec5-404d-ba0a-6499357d2a70">

``` python
df = house_df[['Price','Area','Room']]
df.shape
```

<div class="output execute_result" execution_count="35">

    (924, 3)

</div>

</div>

<div class="cell code" execution_count="37">

``` python
df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 924 entries, 0 to 923
    Data columns (total 3 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   Price   920 non-null    float64
     1   Area    924 non-null    int64  
     2   Room    924 non-null    int64  
    dtypes: float64(1), int64(2)
    memory usage: 21.8 KB

</div>

</div>

<div class="cell code" execution_count="36" executionInfo="{&quot;elapsed&quot;:487,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717961793222,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ZHw81xWkffFc">

``` python
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
outliers = df['Price'][(df['Price'] < (Q1 - 1.5 * IQR)) |(df['Price'] > (Q3 + 1.5 * IQR))]
outliers
```

<div class="output execute_result" execution_count="36">

    20     1625000.0
    28     1650000.0
    31     1950000.0
    33     3925000.0
    57     1295000.0
             ...    
    885    1450000.0
    902    1300000.0
    906    1250000.0
    910    1698000.0
    917    1500000.0
    Name: Price, Length: 71, dtype: float64

</div>

</div>

<div class="cell code" execution_count="38" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:10,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717961798241,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Np-T1fObDX19" outputId="3d773773-13d6-433a-faf6-8c0e8b5a3369">

``` python
df_no_outliers = df.drop(outliers.index, axis = 0)
df_no_outliers.shape
```

<div class="output execute_result" execution_count="38">

    (853, 3)

</div>

</div>

<div class="cell code" execution_count="39" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:487}" executionInfo="{&quot;elapsed&quot;:2981,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717962006174,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="3-pVVpV6BX8u" outputId="765afaaf-c4cb-4359-cc42-491cfecb8825">

``` python
#Visualización CON OUTLIERS
plt.subplot(1,2,1)
ax = sns.histplot(data= df, x= 'Price')
ax.set_xlabel('Precio en millones')
ax.set_ylabel('Frecuencia')
ax.set_title('Análisis de Precios CON Outliers')
#plt.xticks(fontsize = 30)
#plt.yticks(fontsize = 30)

#Visualización SIN OUTLIERS
plt.subplot(1,2,2)
ax = sns.histplot(data= df_no_outliers, x= 'Price')
ax.set_xlabel('Precio en millones')
ax.set_ylabel('Frecuencia')
ax.set_title('Análisis de Precios SIN Outliers')
#plt.xticks(fontsize = 30)
#plt.yticks(fontsize = 30)

plt.tight_layout()
plt.show()
```

<div class="output display_data">

![](7e51ccfe5c1bff292b19ac4d3a947328b52759f1.png)

</div>

</div>

<div class="cell code" execution_count="40">

``` python
#Visualización CON OUTLIERS
plt.subplot(1,2,1)
ax = sns.boxplot(data= df, x= 'Price')
ax.set_xlabel('Precio en millones')
ax.set_ylabel('Frecuencia')
ax.set_title('Análisis de Precios CON Outliers')
#plt.xticks(fontsize = 30)
#plt.yticks(fontsize = 30)

#Visualización SIN OUTLIERS
plt.subplot(1,2,2)
ax = sns.boxplot(data= df_no_outliers, x= 'Price')
ax.set_xlabel('Precio en millones')
ax.set_ylabel('Frecuencia')
ax.set_title('Análisis de Precios SIN Outliers')
#plt.xticks(fontsize = 30)
#plt.yticks(fontsize = 30)

plt.tight_layout()
plt.show()
```

<div class="output display_data">

![](8750e1464545705c8e19f5b7a7388f62a78751df.png)

</div>

</div>

<div class="cell markdown" id="MADKwBwfCydi">

#### **Ejercicio 9:**

Se puede reemplazar los valores de outliers con "the upper cap" o "the lower cap" sólo si el outlier is **univariado**. En esencia se reemplaza:

- Los outliers univariados que son mucho **más pequeños** que el resto de los datos con el límite inferior del atributo $`LowerCap = Q1-1.5*IQR`$
- Los outliers univariados que son mucho **más grandes** que el resto de los datos con el límite superior del atributo $`UpperCap = Q3+1.5*IQR`$.

Recordemos: $`IQR = Q3 -Q1`$

En nuestro contexto, reemplace los outliers detectados en el atributo **Price** de nuestro dataset (Ejercicio 1).

</div>

<div class="cell code" execution_count="41" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:484,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717957537233,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pYL5dR1tC2B5" outputId="42a57355-7903-46b0-dd73-324017af9cb9">

``` python
#Calcula IQR usando el método quantile de Pandas
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
```

<div class="output stream stdout">

    350000.0

</div>

</div>

<div class="cell code" execution_count="42" executionInfo="{&quot;elapsed&quot;:462,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958203951,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="xCfU_bpmSY4Z">

``` python
uppercap = Q3 + 1.5 * IQR
lowercap = Q1 - 1.5 * IQR
```

</div>

<div class="cell code" execution_count="50" executionInfo="{&quot;elapsed&quot;:6,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958371568,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="l7aifOt5SqeX">

``` python
BM_upp = df['Price'] > uppercap
df.loc[df[BM_upp].index,'Price'] = uppercap
df.loc[df[BM_upp].index,'Price']
```

<div class="output execute_result" execution_count="50">

    Series([], Name: Price, dtype: float64)

</div>

</div>

<div class="cell code" execution_count="48" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958373382,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="N40pYvqnSdm7">

``` python
BM_low = (df['Price'] < lowercap)
df.loc[df[BM_low].index,'Price'] = lowercap
df.loc[df[BM_low].index,'Price']
```

<div class="output execute_result" execution_count="48">

    Series([], Name: Price, dtype: float64)

</div>

</div>

<div class="cell code" execution_count="51" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:450}" executionInfo="{&quot;elapsed&quot;:1279,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1717958410254,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="uV_BVU_rTHch" outputId="e6067ffb-0af1-4bf5-a0a6-5b385b0e658a">

``` python
plt.figure(figsize = (40,18))
ax = sns.histplot(data= df, x= 'Price')
ax.set_xlabel('Precios en Millones', fontsize = 30)
ax.set_title('Análisis de Precios con reemplazo de outliers', fontsize = 40)
ax.set_ylabel('Count',  fontsize = 30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.show()
```

<div class="output display_data">

![](08f991e37cca6843c420de19feb54d1151b32a94.png)

</div>

</div>

<div class="cell code" execution_count="52">

``` python
plt.figure(figsize = (40,18))
ax = sns.boxplot(data= df, x= 'Price')
ax.set_xlabel('Precios en Millones', fontsize = 30)
ax.set_title('Análisis de Precios con reemplazo de outliers', fontsize = 40)
ax.set_ylabel('Count',  fontsize = 30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.show()
```

<div class="output display_data">

![](df058342e82f77e4951e2c5a7605757d01f3740b.png)

</div>

</div>

<div class="cell code">

``` python
```

</div>
