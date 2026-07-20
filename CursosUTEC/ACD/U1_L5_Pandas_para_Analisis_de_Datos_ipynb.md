---
curso: ACD
titulo: U1_L5 Pandas para Análisis de Datos
slides: 0
fuente: U1_L5 Pandas para Análisis de Datos.ipynb
---

<div class="cell markdown" id="JDyItWMK5ex0">

# **Laboratorio 4: Pandas para Análisis de Datos**

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:827,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672114225,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4alBWBpc5V3f">

``` python
import pandas as pd
import numpy as np
```

</div>

<div class="cell markdown" id="gTnAVYbl5lR5">

## **I. Leer Datasets**

Syntax para leer datasets:

`pd.read_csv("FILE_NAME_HERE.FORMAT")`

En este caso, estamos leyendo archivos csv, sin embargo, puede haber circunstancias en las que también tratemos con archivos excel o xlsx, simplemente podemos reemplazar `pd.read_csv` con `pd.read_excel`

</div>

<div class="cell code" execution_count="2" executionInfo="{&quot;elapsed&quot;:1517,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672161357,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="jq4dkibi5pHu">

``` python
# Usamos encoding por problemas de utf-8
df = pd.read_csv("OnlineRetail.csv", encoding = "ISO-8859-1")
```

</div>

<div class="cell markdown" id="r568TuUN7L1k">

## **II. Funciones Básicas de Pandas**

Ahora que hemos importado nuestros datos, podemos hacer uso de las funciones y sintaxis básicas de Pandas para obtener un análisis estadístico básico de nuestro conjunto de datos.

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:597}" executionInfo="{&quot;elapsed&quot;:356,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672309935,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Inj45LNfgglQ" outputId="4f96e4b5-c65f-4c7d-c2b8-c0e6c386cb1f">

``` python
df
```

<div class="output execute_result" execution_count="3">

           InvoiceNo StockCode                          Description  Quantity  \
    0         536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1         536365     71053                  WHITE METAL LANTERN         6   
    2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   
    ...          ...       ...                                  ...       ...   
    541904    581587     22613          PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899         CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254        CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255      CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138        BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID         Country  
    0        12/1/2010 8:26       2.55     17850.0  United Kingdom  
    1        12/1/2010 8:26       3.39     17850.0  United Kingdom  
    2        12/1/2010 8:26       2.75     17850.0  United Kingdom  
    3        12/1/2010 8:26       3.39     17850.0  United Kingdom  
    4        12/1/2010 8:26       3.39     17850.0  United Kingdom  
    ...                 ...        ...         ...             ...  
    541904  12/9/2011 12:50       0.85     12680.0          France  
    541905  12/9/2011 12:50       2.10     12680.0          France  
    541906  12/9/2011 12:50       4.15     12680.0          France  
    541907  12/9/2011 12:50       4.15     12680.0          France  
    541908  12/9/2011 12:50       4.95     12680.0          France  

    [541909 rows x 8 columns]

</div>

</div>

<div class="cell markdown" id="XCiYQQI68Qbu">

1.  `df.head()` - muestra una mini vista previa de sus datos para que pueda tener una idea de qué encabezados de columna y el tipo de datos dentro del archivo

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:371,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672573516,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="OfgQaJl08GC7" outputId="a6e4c030-db8f-4cc4-87ca-419dbe5ee219">

``` python
df.head()
```

<div class="output execute_result" execution_count="4">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  
    0  12/1/2010 8:26       2.55     17850.0  United Kingdom  
    1  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    2  12/1/2010 8:26       2.75     17850.0  United Kingdom  
    3  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    4  12/1/2010 8:26       3.39     17850.0  United Kingdom  

</div>

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:537}" executionInfo="{&quot;elapsed&quot;:444,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672612853,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="hN5mMhRk_oDG" outputId="76abbeeb-adbc-44e8-edfe-8557abf9c164">

``` python
df.head(10)
```

<div class="output execute_result" execution_count="5">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   
    5    536365     22752         SET 7 BABUSHKA NESTING BOXES         2   
    6    536365     21730    GLASS STAR FROSTED T-LIGHT HOLDER         6   
    7    536366     22633               HAND WARMER UNION JACK         6   
    8    536366     22632            HAND WARMER RED POLKA DOT         6   
    9    536367     84879        ASSORTED COLOUR BIRD ORNAMENT        32   

          InvoiceDate  UnitPrice  CustomerID         Country  
    0  12/1/2010 8:26       2.55     17850.0  United Kingdom  
    1  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    2  12/1/2010 8:26       2.75     17850.0  United Kingdom  
    3  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    4  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    5  12/1/2010 8:26       7.65     17850.0  United Kingdom  
    6  12/1/2010 8:26       4.25     17850.0  United Kingdom  
    7  12/1/2010 8:28       1.85     17850.0  United Kingdom  
    8  12/1/2010 8:28       1.85     17850.0  United Kingdom  
    9  12/1/2010 8:34       1.69     13047.0  United Kingdom  

</div>

</div>

<div class="cell markdown" id="ODFoo8yq_rWv">

También existe `df.tail()` para los últimos datos del dataset

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:387,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672630689,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="msLMc3km_viH" outputId="7231d537-6d9b-4ad1-9244-4a862447be77">

``` python
df.tail()
```

<div class="output execute_result" execution_count="6">

           InvoiceNo StockCode                      Description  Quantity  \
    541904    581587     22613      PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899     CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254    CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255  CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138    BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID Country  
    541904  12/9/2011 12:50       0.85     12680.0  France  
    541905  12/9/2011 12:50       2.10     12680.0  France  
    541906  12/9/2011 12:50       4.15     12680.0  France  
    541907  12/9/2011 12:50       4.15     12680.0  France  
    541908  12/9/2011 12:50       4.95     12680.0  France  

</div>

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:363}" executionInfo="{&quot;elapsed&quot;:382,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672651188,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="83PDDzI7PoM6" outputId="04b7f8b0-2b1c-48e3-da80-a2014353e989">

``` python
df.tail(10)
```

<div class="output execute_result" execution_count="7">

           InvoiceNo StockCode                      Description  Quantity  \
    541899    581587     22726       ALARM CLOCK BAKELIKE GREEN         4   
    541900    581587     22730       ALARM CLOCK BAKELIKE IVORY         4   
    541901    581587     22367  CHILDRENS APRON SPACEBOY DESIGN         8   
    541902    581587     22629              SPACEBOY LUNCH BOX         12   
    541903    581587     23256      CHILDRENS CUTLERY SPACEBOY          4   
    541904    581587     22613      PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899     CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254    CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255  CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138    BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID Country  
    541899  12/9/2011 12:50       3.75     12680.0  France  
    541900  12/9/2011 12:50       3.75     12680.0  France  
    541901  12/9/2011 12:50       1.95     12680.0  France  
    541902  12/9/2011 12:50       1.95     12680.0  France  
    541903  12/9/2011 12:50       4.15     12680.0  France  
    541904  12/9/2011 12:50       0.85     12680.0  France  
    541905  12/9/2011 12:50       2.10     12680.0  France  
    541906  12/9/2011 12:50       4.15     12680.0  France  
    541907  12/9/2011 12:50       4.15     12680.0  France  
    541908  12/9/2011 12:50       4.95     12680.0  France  

</div>

</div>

<div class="cell markdown" id="_VnX3rzO8Wt4">

1.  `df.shape`: devuelve la cantidad de filas y columnas en su conjunto de datos en una salida vectorial (cantidad de filas, cantidad de columnas)

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:395,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672705399,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KOJZkt068YHh" outputId="eff5c047-5363-4d1e-fc41-6be2380b7766">

``` python
df.shape
```

<div class="output execute_result" execution_count="8">

    (541909, 8)

</div>

</div>

<div class="cell markdown" id="Rq9bQPvk8ejD">

1.  `df.columns`: devuelve la lista de encabezados de columna y el tipo de datos de estos encabezados

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:306,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672754243,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="LVc1zXc38hT5" outputId="2127aa28-d259-4f32-9891-fa33424791a5">

``` python
df.columns
```

<div class="output execute_result" execution_count="9">

    Index(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
           'UnitPrice', 'CustomerID', 'Country'],
          dtype='object')

</div>

</div>

<div class="cell markdown" id="ATkbCRnd8ykL">

1.  `df.info()` - Devuelve información detallada sobre su conjunto de datos

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:319,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712672799435,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="qsnz0SLv8zk3" outputId="35b44d22-53b2-4151-fd06-1b71b17b2bb1">

``` python
df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 541909 entries, 0 to 541908
    Data columns (total 8 columns):
     #   Column       Non-Null Count   Dtype  
    ---  ------       --------------   -----  
     0   InvoiceNo    541909 non-null  object 
     1   StockCode    541909 non-null  object 
     2   Description  540455 non-null  object 
     3   Quantity     541909 non-null  int64  
     4   InvoiceDate  541909 non-null  object 
     5   UnitPrice    541909 non-null  float64
     6   CustomerID   406829 non-null  float64
     7   Country      541909 non-null  object 
    dtypes: float64(2), int64(1), object(5)
    memory usage: 33.1+ MB

</div>

</div>

<div class="cell markdown" id="6jA0iKY684qP">

1.  `df.describe()` - Devuelve información estadística detallada sobre su conjunto de datos numéricos

</div>

<div class="cell code" execution_count="11" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:300}" executionInfo="{&quot;elapsed&quot;:335,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712673008943,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="awLTuTVG88Im" outputId="56284a7b-af8c-415c-a75d-fe9c3649329c">

``` python
df.describe()
```

<div class="output execute_result" execution_count="11">

                Quantity      UnitPrice     CustomerID
    count  541909.000000  541909.000000  406829.000000
    mean        9.552250       4.611114   15287.690570
    std       218.081158      96.759853    1713.600303
    min    -80995.000000  -11062.060000   12346.000000
    25%         1.000000       1.250000   13953.000000
    50%         3.000000       2.080000   15152.000000
    75%        10.000000       4.130000   16791.000000
    max     80995.000000   38970.000000   18287.000000

</div>

</div>

<div class="cell markdown" id="F0ep5HPN-asu">

## **III. Encontrar datos**

Similar a las listas en Python, podemos usar métodos de indexación para encontrar filas y columnas específicas del dataframe. Pandas accede a estos índices a través de esta sintaxis:

`df.iloc[row,column]`

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:288,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712673954982,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_r1opTmD_E9H" outputId="f70f3b36-fa9b-4ed3-9f8e-3c15798e59f7">

``` python
df.head()
```

<div class="output execute_result" execution_count="12">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  
    0  12/1/2010 8:26       2.55     17850.0  United Kingdom  
    1  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    2  12/1/2010 8:26       2.75     17850.0  United Kingdom  
    3  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    4  12/1/2010 8:26       3.39     17850.0  United Kingdom  

</div>

</div>

<div class="cell markdown" id="ScPoyWpw_B4O">

Devuelve la tercera fila del dataframe

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:269,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674003511,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="EBEQItpC-tiZ" outputId="54466ac8-e5ae-4272-a6b1-23ebcda19954">

``` python
#tu código
df.iloc[2]
```

<div class="output execute_result" execution_count="13">

    InvoiceNo                              536365
    StockCode                              84406B
    Description    CREAM CUPID HEARTS COAT HANGER
    Quantity                                    8
    InvoiceDate                    12/1/2010 8:26
    UnitPrice                                2.75
    CustomerID                            17850.0
    Country                        United Kingdom
    Name: 2, dtype: object

</div>

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:418,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674026468,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="GaL6K4BpU4zh" outputId="e37fe21e-1545-4f4f-cb13-e7c63172f2df">

``` python
df.iloc[2,:]
```

<div class="output execute_result" execution_count="14">

    InvoiceNo                              536365
    StockCode                              84406B
    Description    CREAM CUPID HEARTS COAT HANGER
    Quantity                                    8
    InvoiceDate                    12/1/2010 8:26
    UnitPrice                                2.75
    CustomerID                            17850.0
    Country                        United Kingdom
    Name: 2, dtype: object

</div>

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:81}" executionInfo="{&quot;elapsed&quot;:467,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674040750,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="MJkVrM5RU94e" outputId="5f9fb71d-007d-43f9-da1a-b083a92fb876">

``` python
df.iloc[2:3,:]
```

<div class="output execute_result" execution_count="15">

      InvoiceNo StockCode                     Description  Quantity  \
    2    536365    84406B  CREAM CUPID HEARTS COAT HANGER         8   

          InvoiceDate  UnitPrice  CustomerID         Country  
    2  12/1/2010 8:26       2.75     17850.0  United Kingdom  

</div>

</div>

<div class="cell markdown" id="hGXbZSTM_RdJ">

Devuelve la última fila del dataframe

</div>

<div class="cell code" execution_count="16" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:396,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674163116,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="3JIHli7wjiy8" outputId="e74535dd-19f3-4f26-f660-a49074e3619a">

``` python
df.tail()
```

<div class="output execute_result" execution_count="16">

           InvoiceNo StockCode                      Description  Quantity  \
    541904    581587     22613      PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899     CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254    CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255  CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138    BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID Country  
    541904  12/9/2011 12:50       0.85     12680.0  France  
    541905  12/9/2011 12:50       2.10     12680.0  France  
    541906  12/9/2011 12:50       4.15     12680.0  France  
    541907  12/9/2011 12:50       4.15     12680.0  France  
    541908  12/9/2011 12:50       4.95     12680.0  France  

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:310,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674186187,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Vj1K7aeG_f5N" outputId="4b33afad-8615-4f31-ac23-94cbfb1ddc19">

``` python
#tu código
df.iloc[-1]
```

<div class="output execute_result" execution_count="17">

    InvoiceNo                             581587
    StockCode                              22138
    Description    BAKING SET 9 PIECE RETROSPOT 
    Quantity                                   3
    InvoiceDate                  12/9/2011 12:50
    UnitPrice                               4.95
    CustomerID                           12680.0
    Country                               France
    Name: 541908, dtype: object

</div>

</div>

<div class="cell markdown" id="QZx28QOn_6fr">

Devuelve las tres últimas columnas del dataframe

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:451,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674250851,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="G4w-v_qT_5_K" outputId="da38fb72-fb23-45b6-8321-04b8ec29c71e">

``` python
#tu código
df.iloc[:,-3:]
```

<div class="output execute_result" execution_count="18">

            UnitPrice  CustomerID         Country
    0            2.55     17850.0  United Kingdom
    1            3.39     17850.0  United Kingdom
    2            2.75     17850.0  United Kingdom
    3            3.39     17850.0  United Kingdom
    4            3.39     17850.0  United Kingdom
    ...           ...         ...             ...
    541904       0.85     12680.0          France
    541905       2.10     12680.0          France
    541906       4.15     12680.0          France
    541907       4.15     12680.0          France
    541908       4.95     12680.0          France

    [541909 rows x 3 columns]

</div>

</div>

<div class="cell markdown" id="B1fSoGOmAfaj">

## **IV. Describir datos específicos**

Podemos hacer uso de las funciones básicas anteriores para profundizar más en nuestro conjunto de datos. Podemos obtener información sobre solo algunos tipos de datos que estamos interesados ​​en usar:

`df.describe(include=['OBJECT_TYPE1','OBJECT_TYPE2'])`

Además, podemos obtener la frecuencia de ciertos valores usando:

`df.value_counts(Normalize=False)`

</div>

<div class="cell markdown" id="MP-4AgvhBEvq">

Información estadística sobre los tipos de datos `object` y `bool` dentro del conjunto de datos.

</div>

<div class="cell code" execution_count="19" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:312,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674306447,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="iUdhE7N2kIPC" outputId="e4e1df1f-d53c-49a7-97de-b896aed175f8">

``` python
df.head()
```

<div class="output execute_result" execution_count="19">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  
    0  12/1/2010 8:26       2.55     17850.0  United Kingdom  
    1  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    2  12/1/2010 8:26       2.75     17850.0  United Kingdom  
    3  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    4  12/1/2010 8:26       3.39     17850.0  United Kingdom  

</div>

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:300}" executionInfo="{&quot;elapsed&quot;:541,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674309286,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="JWx1d2MZkeVy" outputId="35f99642-ed84-4175-e969-d954077ed5df">

``` python
df.describe()
```

<div class="output execute_result" execution_count="20">

                Quantity      UnitPrice     CustomerID
    count  541909.000000  541909.000000  406829.000000
    mean        9.552250       4.611114   15287.690570
    std       218.081158      96.759853    1713.600303
    min    -80995.000000  -11062.060000   12346.000000
    25%         1.000000       1.250000   13953.000000
    50%         3.000000       2.080000   15152.000000
    75%        10.000000       4.130000   16791.000000
    max     80995.000000   38970.000000   18287.000000

</div>

</div>

<div class="cell code" execution_count="21" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:175}" executionInfo="{&quot;elapsed&quot;:746,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674324778,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2TSUOzeWA-IW" outputId="2c071c94-1fd7-46bd-8b03-3e39f1519338">

``` python
df.describe(include=['object','bool'])
```

<div class="output execute_result" execution_count="21">

           InvoiceNo StockCode                         Description  \
    count     541909    541909                              540455   
    unique     25900      4070                                4223   
    top       573585    85123A  WHITE HANGING HEART T-LIGHT HOLDER   
    freq        1114      2313                                2369   

                 InvoiceDate         Country  
    count             541909          541909  
    unique             23260              38  
    top     10/31/2011 14:41  United Kingdom  
    freq                1114          495478  

</div>

</div>

<div class="cell markdown" id="dY8ctG4_BiVi">

Se puede revisar la frecuencia de la columna `CustomerID`

</div>

<div class="cell code" execution_count="22" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674452272,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="TmRymtV_IbJr" outputId="ae1d0adc-424c-4642-ee56-7f2144892cb8">

``` python
df.head()
```

<div class="output execute_result" execution_count="22">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  
    0  12/1/2010 8:26       2.55     17850.0  United Kingdom  
    1  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    2  12/1/2010 8:26       2.75     17850.0  United Kingdom  
    3  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    4  12/1/2010 8:26       3.39     17850.0  United Kingdom  

</div>

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:285,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674450103,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mM5cTYHsIdgu" outputId="4c0a0c5a-23ff-4b8f-d46b-7acba78fe45f">

``` python
df['CustomerID'].value_counts()
```

<div class="output execute_result" execution_count="23">

    CustomerID
    17841.0    7983
    14911.0    5903
    14096.0    5128
    12748.0    4642
    14606.0    2782
               ... 
    15070.0       1
    15753.0       1
    17065.0       1
    16881.0       1
    16995.0       1
    Name: count, Length: 4372, dtype: int64

</div>

</div>

<div class="cell markdown" id="BkoYg_v3JCFl">

\## **V. Asignación de Datos**

Pandas también permite la asignación de datos a través de métodos de llamada simples. Esto permite la creación de nuevas columnas y algunos cambios en los datos. Podemos hacer esto asignando una constante o iteración de variables.

Podemos hacer que toda la columna `Quantity` sea cero a través de este código simple:

</div>

<div class="cell code" execution_count="24" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:402,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674563451,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aJp-YXGnlvvp" outputId="1e6a9f3c-d6d6-4aec-d5bb-7799c0e302fe">

``` python
df.head()
```

<div class="output execute_result" execution_count="24">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  
    0  12/1/2010 8:26       2.55     17850.0  United Kingdom  
    1  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    2  12/1/2010 8:26       2.75     17850.0  United Kingdom  
    3  12/1/2010 8:26       3.39     17850.0  United Kingdom  
    4  12/1/2010 8:26       3.39     17850.0  United Kingdom  

</div>

</div>

<div class="cell code" execution_count="25" executionInfo="{&quot;elapsed&quot;:2,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674638641,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pEKfRA4rJmDT">

``` python
df["TotalPrice"]=df["Quantity"]*df["UnitPrice"]
```

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:315,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674640376,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="dmlCUTfRJrz9" outputId="dfbcc338-8a3d-4f6e-e81e-456d5b83c9b0">

``` python
df.head()
```

<div class="output execute_result" execution_count="26">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    0  12/1/2010 8:26       2.55     17850.0  United Kingdom       15.30  
    1  12/1/2010 8:26       3.39     17850.0  United Kingdom       20.34  
    2  12/1/2010 8:26       2.75     17850.0  United Kingdom       22.00  
    3  12/1/2010 8:26       3.39     17850.0  United Kingdom       20.34  
    4  12/1/2010 8:26       3.39     17850.0  United Kingdom       20.34  

</div>

</div>

<div class="cell markdown" id="cnC6uGx-egJ6">

## **VI. Manejo de Datos Faltantes**

Si faltan entradas en un conjunto de datos, los valores se dan como `NaN`, que significa "No es un número". Estos valores `NaN` siempre serán de tipo `float64` debido a razones técnicas.

Para detectar datos faltantes podemos usar el método `isna()`

</div>

<div class="cell markdown" id="QNum0Po2hpQw">

Pandas nos permite acceder a datos faltantes. Para acceder a las entradas de `NaN` podemos usar `pd.isnull()` o `pd.notnull()`. Adicionalmente podemos usar el método `isna()`

</div>

<div class="cell code" execution_count="27" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:286,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674741412,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="X18EgAGnfyxJ" outputId="22aeac56-84ec-4743-e554-1ff8ba443fd4">

``` python
pd.isnull(df)
```

<div class="output execute_result" execution_count="27">

            InvoiceNo  StockCode  Description  Quantity  InvoiceDate  UnitPrice  \
    0           False      False        False     False        False      False   
    1           False      False        False     False        False      False   
    2           False      False        False     False        False      False   
    3           False      False        False     False        False      False   
    4           False      False        False     False        False      False   
    ...           ...        ...          ...       ...          ...        ...   
    541904      False      False        False     False        False      False   
    541905      False      False        False     False        False      False   
    541906      False      False        False     False        False      False   
    541907      False      False        False     False        False      False   
    541908      False      False        False     False        False      False   

            CustomerID  Country  TotalPrice  
    0            False    False       False  
    1            False    False       False  
    2            False    False       False  
    3            False    False       False  
    4            False    False       False  
    ...            ...      ...         ...  
    541904       False    False       False  
    541905       False    False       False  
    541906       False    False       False  
    541907       False    False       False  
    541908       False    False       False  

    [541909 rows x 9 columns]

</div>

</div>

<div class="cell code" execution_count="28" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:392,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674806603,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="LLgBqRt-iIGQ" outputId="2342f179-824f-44cc-a3e9-17c10fae85c8">

``` python
df.isna()
```

<div class="output execute_result" execution_count="28">

            InvoiceNo  StockCode  Description  Quantity  InvoiceDate  UnitPrice  \
    0           False      False        False     False        False      False   
    1           False      False        False     False        False      False   
    2           False      False        False     False        False      False   
    3           False      False        False     False        False      False   
    4           False      False        False     False        False      False   
    ...           ...        ...          ...       ...          ...        ...   
    541904      False      False        False     False        False      False   
    541905      False      False        False     False        False      False   
    541906      False      False        False     False        False      False   
    541907      False      False        False     False        False      False   
    541908      False      False        False     False        False      False   

            CustomerID  Country  TotalPrice  
    0            False    False       False  
    1            False    False       False  
    2            False    False       False  
    3            False    False       False  
    4            False    False       False  
    ...            ...      ...         ...  
    541904       False    False       False  
    541905       False    False       False  
    541906       False    False       False  
    541907       False    False       False  
    541908       False    False       False  

    [541909 rows x 9 columns]

</div>

</div>

<div class="cell code" execution_count="29" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:288,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712674846454,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Jft6EpE1gD-r" outputId="82e2cc11-f37f-45d4-f542-9f9e3c1da421">

``` python
pd.notnull(df)
```

<div class="output execute_result" execution_count="29">

            InvoiceNo  StockCode  Description  Quantity  InvoiceDate  UnitPrice  \
    0            True       True         True      True         True       True   
    1            True       True         True      True         True       True   
    2            True       True         True      True         True       True   
    3            True       True         True      True         True       True   
    4            True       True         True      True         True       True   
    ...           ...        ...          ...       ...          ...        ...   
    541904       True       True         True      True         True       True   
    541905       True       True         True      True         True       True   
    541906       True       True         True      True         True       True   
    541907       True       True         True      True         True       True   
    541908       True       True         True      True         True       True   

            CustomerID  Country  TotalPrice  
    0             True     True        True  
    1             True     True        True  
    2             True     True        True  
    3             True     True        True  
    4             True     True        True  
    ...            ...      ...         ...  
    541904        True     True        True  
    541905        True     True        True  
    541906        True     True        True  
    541907        True     True        True  
    541908        True     True        True  

    [541909 rows x 9 columns]

</div>

</div>

<div class="cell code" execution_count="30" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:370,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675007234,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Tb3ntaD8iM99" outputId="30c956f2-a008-43f1-c74d-d91d58f1db3b">

``` python
#Indica las columnas donde existen valores nulos
df.isna().any()
```

<div class="output execute_result" execution_count="30">

    InvoiceNo      False
    StockCode      False
    Description     True
    Quantity       False
    InvoiceDate    False
    UnitPrice      False
    CustomerID      True
    Country        False
    TotalPrice     False
    dtype: bool

</div>

</div>

<div class="cell markdown" id="-UzyvG50gjKS">

Imprime las filas que tienen `NaN` en una columna específica `UnitPrice`

</div>

<div class="cell code" execution_count="31" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:273,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675306677,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="9VMJwjCjnupn" outputId="0dfc5a7e-74a5-45f9-e476-397577cd8710">

``` python
#tu turno
df[df['Description'].isna()]
```

<div class="output execute_result" execution_count="31">

           InvoiceNo StockCode Description  Quantity      InvoiceDate  UnitPrice  \
    622       536414     22139         NaN        56  12/1/2010 11:52        0.0   
    1970      536545     21134         NaN         1  12/1/2010 14:32        0.0   
    1971      536546     22145         NaN         1  12/1/2010 14:33        0.0   
    1972      536547     37509         NaN         1  12/1/2010 14:33        0.0   
    1987      536549    85226A         NaN         1  12/1/2010 14:34        0.0   
    ...          ...       ...         ...       ...              ...        ...   
    535322    581199     84581         NaN        -2  12/7/2011 18:26        0.0   
    535326    581203     23406         NaN        15  12/7/2011 18:31        0.0   
    535332    581209     21620         NaN         6  12/7/2011 18:35        0.0   
    536981    581234     72817         NaN        27  12/8/2011 10:33        0.0   
    538554    581408     85175         NaN        20  12/8/2011 14:06        0.0   

            CustomerID         Country  TotalPrice  
    622            NaN  United Kingdom         0.0  
    1970           NaN  United Kingdom         0.0  
    1971           NaN  United Kingdom         0.0  
    1972           NaN  United Kingdom         0.0  
    1987           NaN  United Kingdom         0.0  
    ...            ...             ...         ...  
    535322         NaN  United Kingdom        -0.0  
    535326         NaN  United Kingdom         0.0  
    535332         NaN  United Kingdom         0.0  
    536981         NaN  United Kingdom         0.0  
    538554         NaN  United Kingdom         0.0  

    [1454 rows x 9 columns]

</div>

</div>

<div class="cell code" execution_count="32" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:309,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675360295,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="fYHOilkaZ2Ne" outputId="3c121fd5-b4a4-46fe-ff8d-a1609c94df5e">

``` python
pd.isnull(df['Description'])
```

<div class="output execute_result" execution_count="32">

    0         False
    1         False
    2         False
    3         False
    4         False
              ...  
    541904    False
    541905    False
    541906    False
    541907    False
    541908    False
    Name: Description, Length: 541909, dtype: bool

</div>

</div>

<div class="cell markdown" id="vrdc5Uo5gt8R">

Imprime filas que no tienen entradas `NaN` en una columna específica `CustomerID`

</div>

<div class="cell code" execution_count="33" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:270,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675511747,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="xAqG5dLQg44K" outputId="1588be11-c208-4cc9-e6e2-f707281cc3a5">

``` python
#tu turno
pd.notnull(df['CustomerID'])
```

<div class="output execute_result" execution_count="33">

    0         True
    1         True
    2         True
    3         True
    4         True
              ... 
    541904    True
    541905    True
    541906    True
    541907    True
    541908    True
    Name: CustomerID, Length: 541909, dtype: bool

</div>

</div>

<div class="cell code" execution_count="34" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:597}" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675527381,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="czjMvc1_apLS" outputId="faaa4cb1-8533-4d88-a61a-b5cc53279149">

``` python
df[pd.notnull(df['CustomerID'])]
```

<div class="output execute_result" execution_count="34">

           InvoiceNo StockCode                          Description  Quantity  \
    0         536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1         536365     71053                  WHITE METAL LANTERN         6   
    2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   
    ...          ...       ...                                  ...       ...   
    541904    581587     22613          PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899         CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254        CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255      CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138        BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    0        12/1/2010 8:26       2.55     17850.0  United Kingdom       15.30  
    1        12/1/2010 8:26       3.39     17850.0  United Kingdom       20.34  
    2        12/1/2010 8:26       2.75     17850.0  United Kingdom       22.00  
    3        12/1/2010 8:26       3.39     17850.0  United Kingdom       20.34  
    4        12/1/2010 8:26       3.39     17850.0  United Kingdom       20.34  
    ...                 ...        ...         ...             ...         ...  
    541904  12/9/2011 12:50       0.85     12680.0          France       10.20  
    541905  12/9/2011 12:50       2.10     12680.0          France       12.60  
    541906  12/9/2011 12:50       4.15     12680.0          France       16.60  
    541907  12/9/2011 12:50       4.15     12680.0          France       16.60  
    541908  12/9/2011 12:50       4.95     12680.0          France       14.85  

    [406829 rows x 9 columns]

</div>

</div>

<div class="cell markdown" id="Sci3XPTliexC">

También podemos reemplazar estos valores nulos con lo que queramos usando `fillna()`. Por ejemplo, podemos reemplazar los valores nulos en `UnitPrice` por el valor 0

</div>

<div class="cell code" execution_count="35" executionInfo="{&quot;elapsed&quot;:350,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675560483,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="YS0aXi17inOR">

``` python
df['UnitPrice'] = df['UnitPrice'].fillna(0)
```

</div>

<div class="cell code" execution_count="36" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:453,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675565235,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="48Vp55gKiuus" outputId="ca0a6d68-4956-4e6a-ae2a-a21e8877541d">

``` python
#Verificamos
df.isna().any()
```

<div class="output execute_result" execution_count="36">

    InvoiceNo      False
    StockCode      False
    Description     True
    Quantity       False
    InvoiceDate    False
    UnitPrice      False
    CustomerID      True
    Country        False
    TotalPrice     False
    dtype: bool

</div>

</div>

<div class="cell markdown" id="W_LNESlUgLeW">

Si necesitamos reemplazar otros valores que representan valores nulos pero que no se muestran en las entradas de `NaN`, podemos usar `replace()`. Por ejemplo, podemos reemplazar los valores nulos en la columna `StockCode` por el valor "MISSING"

</div>

<div class="cell code" execution_count="37" executionInfo="{&quot;elapsed&quot;:381,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675643333,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="0smy-lUgjVZE">

``` python
df['StockCode'] = df['StockCode'].replace(np.nan, "MISSING")
```

</div>

<div class="cell code" execution_count="38" id="TF0jO19OjtD_">

``` python
#Verificamos
df.isna().any()
```

<div class="output execute_result" execution_count="38">

    InvoiceNo      False
    StockCode      False
    Description     True
    Quantity       False
    InvoiceDate    False
    UnitPrice      False
    CustomerID      True
    Country        False
    TotalPrice     False
    dtype: bool

</div>

</div>

<div class="cell code" execution_count="39" id="EMbsOG8nkZ-e">

``` python
# TODO: Reemplaza los  espacios nulos del atributo Quantity
```

</div>

<div class="cell markdown" id="uU45-G03KNyW">

## **VII. Manipulación de Datos**

Podemos cambiar ciertas características de nuestro conjunto de datos de lo que era originalmente a través de Pandas. Estas son algunas de las formas en que podemos hacerlo:

1.  Cambiar los tipos de datos
2.  Ordenar los tipos de datos

</div>

<div class="cell markdown" id="rKIZaIPUKfpL">

### **Cambiar de tipos de datos**

Si tenemos ciertos datos que no están en nuestro tipo de datos deseado, simplemente podemos reasignarlos como se muestra a continuación.

Hacemos uso de nuestra función básica de pandas, `df.info()`, para ver los cambios realizados.

</div>

<div class="cell code" execution_count="40" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:471,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675695245,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ifxpwFJOKuqg" outputId="87d65218-8bd8-4c31-fcaa-dfea6ce3ba54">

``` python
df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 541909 entries, 0 to 541908
    Data columns (total 9 columns):
     #   Column       Non-Null Count   Dtype  
    ---  ------       --------------   -----  
     0   InvoiceNo    541909 non-null  object 
     1   StockCode    541909 non-null  object 
     2   Description  540455 non-null  object 
     3   Quantity     541909 non-null  int64  
     4   InvoiceDate  541909 non-null  object 
     5   UnitPrice    541909 non-null  float64
     6   CustomerID   406829 non-null  float64
     7   Country      541909 non-null  object 
     8   TotalPrice   541909 non-null  float64
    dtypes: float64(3), int64(1), object(5)
    memory usage: 37.2+ MB

</div>

</div>

<div class="cell code" execution_count="41" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:597}" executionInfo="{&quot;elapsed&quot;:278,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675734866,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="SDiHeCqrbbsG" outputId="889dd969-8aa5-4c1b-edf5-d0fb5514c3d6">

``` python
df
```

<div class="output execute_result" execution_count="41">

           InvoiceNo StockCode                          Description  Quantity  \
    0         536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1         536365     71053                  WHITE METAL LANTERN         6   
    2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   
    ...          ...       ...                                  ...       ...   
    541904    581587     22613          PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899         CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254        CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255      CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138        BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    0        12/1/2010 8:26       2.55     17850.0  United Kingdom       15.30  
    1        12/1/2010 8:26       3.39     17850.0  United Kingdom       20.34  
    2        12/1/2010 8:26       2.75     17850.0  United Kingdom       22.00  
    3        12/1/2010 8:26       3.39     17850.0  United Kingdom       20.34  
    4        12/1/2010 8:26       3.39     17850.0  United Kingdom       20.34  
    ...                 ...        ...         ...             ...         ...  
    541904  12/9/2011 12:50       0.85     12680.0          France       10.20  
    541905  12/9/2011 12:50       2.10     12680.0          France       12.60  
    541906  12/9/2011 12:50       4.15     12680.0          France       16.60  
    541907  12/9/2011 12:50       4.15     12680.0          France       16.60  
    541908  12/9/2011 12:50       4.95     12680.0          France       14.85  

    [541909 rows x 9 columns]

</div>

</div>

<div class="cell code" execution_count="42" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:300}" executionInfo="{&quot;elapsed&quot;:258,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675850872,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_jraoB2Db1xk" outputId="6db30d38-8fb2-43b8-8ac8-83bf8d2f4248">

``` python
df.describe()
```

<div class="output execute_result" execution_count="42">

                Quantity      UnitPrice     CustomerID     TotalPrice
    count  541909.000000  541909.000000  406829.000000  541909.000000
    mean        9.552250       4.611114   15287.690570      17.987795
    std       218.081158      96.759853    1713.600303     378.810824
    min    -80995.000000  -11062.060000   12346.000000 -168469.600000
    25%         1.000000       1.250000   13953.000000       3.400000
    50%         3.000000       2.080000   15152.000000       9.750000
    75%        10.000000       4.130000   16791.000000      17.400000
    max     80995.000000   38970.000000   18287.000000  168469.600000

</div>

</div>

<div class="cell code" execution_count="43" executionInfo="{&quot;elapsed&quot;:422,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675978595,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="rwVEhGKkLCdk">

``` python
df['CustomerID'] = df['CustomerID'].fillna(0)
df['CustomerID'] = df['CustomerID'].astype('int')
```

</div>

<div class="cell code" execution_count="44" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:273,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712675992914,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="0S_VYIehLCW3" outputId="b75c8a4f-adb9-4c2b-d55a-0af978608b02">

``` python
df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 541909 entries, 0 to 541908
    Data columns (total 9 columns):
     #   Column       Non-Null Count   Dtype  
    ---  ------       --------------   -----  
     0   InvoiceNo    541909 non-null  object 
     1   StockCode    541909 non-null  object 
     2   Description  540455 non-null  object 
     3   Quantity     541909 non-null  int64  
     4   InvoiceDate  541909 non-null  object 
     5   UnitPrice    541909 non-null  float64
     6   CustomerID   541909 non-null  int32  
     7   Country      541909 non-null  object 
     8   TotalPrice   541909 non-null  float64
    dtypes: float64(2), int32(1), int64(1), object(5)
    memory usage: 35.1+ MB

</div>

</div>

<div class="cell markdown" id="lcMmB5jJlm5Z">

### **Cambiar de tipos de datos**

Podemos realizar cambios en el orden del conjunto de datos de acuerdo con ciertas reglas.

</div>

<div class="cell code" execution_count="45" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676054070,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="dPfdQAu7cpHc" outputId="c467e6e6-ec7f-43d8-96c1-15e7e89591d1">

``` python
df.head()
```

<div class="output execute_result" execution_count="45">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    0  12/1/2010 8:26       2.55       17850  United Kingdom       15.30  
    1  12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    2  12/1/2010 8:26       2.75       17850  United Kingdom       22.00  
    3  12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    4  12/1/2010 8:26       3.39       17850  United Kingdom       20.34  

</div>

</div>

<div class="cell code" execution_count="46" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:340,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676068444,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="j-NAE3ZDlyAJ" outputId="6115039e-00ee-40db-ef2a-a0c19b13674a">

``` python
#ascending=False si queremos ordenar de manera descendente
df.sort_values(by='Quantity', ascending=False).head()
```

<div class="output execute_result" execution_count="46">

           InvoiceNo StockCode                        Description  Quantity  \
    540421    581483     23843        PAPER CRAFT , LITTLE BIRDIE     80995   
    61619     541431     23166     MEDIUM CERAMIC TOP STORAGE JAR     74215   
    502122    578841     84826     ASSTD DESIGN 3D PAPER STICKERS     12540   
    74614     542504     37413                                NaN      5568   
    421632    573008     84077  WORLD WAR 2 GLIDERS ASSTD DESIGNS      4800   

                 InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    540421    12/9/2011 9:15       2.08       16446  United Kingdom    168469.6  
    61619    1/18/2011 10:01       1.04       12346  United Kingdom     77183.6  
    502122  11/25/2011 15:57       0.00       13256  United Kingdom         0.0  
    74614    1/28/2011 12:03       0.00           0  United Kingdom         0.0  
    421632  10/27/2011 12:26       0.21       12901  United Kingdom      1008.0  

</div>

</div>

<div class="cell code" execution_count="47" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676112217,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8jYKFlnTmMKp" outputId="e437704c-a6f3-4598-91c1-c1216de47178">

``` python
#Por default es de manera ascendente
df.sort_values(by='Quantity').head()
```

<div class="output execute_result" execution_count="47">

           InvoiceNo StockCode                          Description  Quantity  \
    540422   C581484     23843          PAPER CRAFT , LITTLE BIRDIE    -80995   
    61624    C541433     23166       MEDIUM CERAMIC TOP STORAGE JAR    -74215   
    225529    556690     23005         printing smudges/thrown away     -9600   
    225530    556691     23005         printing smudges/thrown away     -9600   
    4287     C536757     84347  ROTATING SILVER ANGELS T-LIGHT HLDR     -9360   

                InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    540422   12/9/2011 9:27       2.08       16446  United Kingdom   -168469.6  
    61624   1/18/2011 10:17       1.04       12346  United Kingdom    -77183.6  
    225529  6/14/2011 10:37       0.00           0  United Kingdom        -0.0  
    225530  6/14/2011 10:37       0.00           0  United Kingdom        -0.0  
    4287    12/2/2010 14:23       0.03       15838  United Kingdom      -280.8  

</div>

</div>

<div class="cell code" execution_count="48" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:277,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676171798,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="DYJ9_PHjmbga" outputId="7aa0bb4f-0648-4961-f15f-bd7d225f1311">

``` python
#Podemos ordenar para diversas columnas
df.sort_values(by=['Quantity', 'UnitPrice'], ascending=[False, True]).head()
```

<div class="output execute_result" execution_count="48">

           InvoiceNo StockCode                        Description  Quantity  \
    540421    581483     23843        PAPER CRAFT , LITTLE BIRDIE     80995   
    61619     541431     23166     MEDIUM CERAMIC TOP STORAGE JAR     74215   
    502122    578841     84826     ASSTD DESIGN 3D PAPER STICKERS     12540   
    74614     542504     37413                                NaN      5568   
    421632    573008     84077  WORLD WAR 2 GLIDERS ASSTD DESIGNS      4800   

                 InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    540421    12/9/2011 9:15       2.08       16446  United Kingdom    168469.6  
    61619    1/18/2011 10:01       1.04       12346  United Kingdom     77183.6  
    502122  11/25/2011 15:57       0.00       13256  United Kingdom         0.0  
    74614    1/28/2011 12:03       0.00           0  United Kingdom         0.0  
    421632  10/27/2011 12:26       0.21       12901  United Kingdom      1008.0  

</div>

</div>

<div class="cell markdown" id="qLtg6fj_m1UA">

## **VIII. Eliminar Datos**

En Pandas, es posible que haya datos que deban eliminarse pero que no sean entradas de `NaN`, por lo tanto, no podemos utilizar funciones de eliminación de `NaN` preexistentes. Para eliminar dichas entradas, podemos usar `DataFrame.drop()`

</div>

<div class="cell markdown" id="rku4FZ52oXkn">

**Eliminar columna**

`axis = 0` para eliminar filas y `axis = 1` para eliminar columnas

</div>

<div class="cell code" execution_count="49" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:283,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676464109,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KS11eQBPoO94" outputId="d26cdee4-a816-4a99-a2ca-6d2bbf5be3be">

``` python
df.head()
```

<div class="output execute_result" execution_count="49">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    0  12/1/2010 8:26       2.55       17850  United Kingdom       15.30  
    1  12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    2  12/1/2010 8:26       2.75       17850  United Kingdom       22.00  
    3  12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    4  12/1/2010 8:26       3.39       17850  United Kingdom       20.34  

</div>

</div>

<div class="cell code" execution_count="50" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:597}" executionInfo="{&quot;elapsed&quot;:356,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676522076,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="hz5j22sCocQG" outputId="e5af4855-60c5-401e-eee0-bf4d858092e1">

``` python
df1 = df.drop('StockCode', axis=1)
df1
```

<div class="output execute_result" execution_count="50">

           InvoiceNo                          Description  Quantity  \
    0         536365   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1         536365                  WHITE METAL LANTERN         6   
    2         536365       CREAM CUPID HEARTS COAT HANGER         8   
    3         536365  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4         536365       RED WOOLLY HOTTIE WHITE HEART.         6   
    ...          ...                                  ...       ...   
    541904    581587          PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587         CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587        CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587      CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587        BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    0        12/1/2010 8:26       2.55       17850  United Kingdom       15.30  
    1        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    2        12/1/2010 8:26       2.75       17850  United Kingdom       22.00  
    3        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    4        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    ...                 ...        ...         ...             ...         ...  
    541904  12/9/2011 12:50       0.85       12680          France       10.20  
    541905  12/9/2011 12:50       2.10       12680          France       12.60  
    541906  12/9/2011 12:50       4.15       12680          France       16.60  
    541907  12/9/2011 12:50       4.15       12680          France       16.60  
    541908  12/9/2011 12:50       4.95       12680          France       14.85  

    [541909 rows x 8 columns]

</div>

</div>

<div class="cell markdown" id="9eQOkai_oqBn">

Elimina una fila si tiene un valor específico

</div>

<div class="cell code" execution_count="51" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:597}" executionInfo="{&quot;elapsed&quot;:310,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676550677,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="3GoI0U08ovzY" outputId="63f50cd6-c025-4e6e-dcd8-48577c0c9636">

``` python
df[df.InvoiceNo!= '536365']
```

<div class="output execute_result" execution_count="51">

           InvoiceNo StockCode                      Description  Quantity  \
    7         536366     22633           HAND WARMER UNION JACK         6   
    8         536366     22632        HAND WARMER RED POLKA DOT         6   
    9         536367     84879    ASSORTED COLOUR BIRD ORNAMENT        32   
    10        536367     22745       POPPY'S PLAYHOUSE BEDROOM          6   
    11        536367     22748        POPPY'S PLAYHOUSE KITCHEN         6   
    ...          ...       ...                              ...       ...   
    541904    581587     22613      PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899     CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254    CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255  CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138    BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    7        12/1/2010 8:28       1.85       17850  United Kingdom       11.10  
    8        12/1/2010 8:28       1.85       17850  United Kingdom       11.10  
    9        12/1/2010 8:34       1.69       13047  United Kingdom       54.08  
    10       12/1/2010 8:34       2.10       13047  United Kingdom       12.60  
    11       12/1/2010 8:34       2.10       13047  United Kingdom       12.60  
    ...                 ...        ...         ...             ...         ...  
    541904  12/9/2011 12:50       0.85       12680          France       10.20  
    541905  12/9/2011 12:50       2.10       12680          France       12.60  
    541906  12/9/2011 12:50       4.15       12680          France       16.60  
    541907  12/9/2011 12:50       4.15       12680          France       16.60  
    541908  12/9/2011 12:50       4.95       12680          France       14.85  

    [541902 rows x 9 columns]

</div>

</div>

<div class="cell markdown" id="2MqPtkGUpBR3">

También se puede borrar a partir de índices

</div>

<div class="cell code" execution_count="52" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:597}" executionInfo="{&quot;elapsed&quot;:284,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676563701,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="PUNdJaeto9jH" outputId="139e1a59-b03c-4676-f4ba-6570778a42ab">

``` python
df.drop(df.index[0])
```

<div class="output execute_result" execution_count="52">

           InvoiceNo StockCode                          Description  Quantity  \
    1         536365     71053                  WHITE METAL LANTERN         6   
    2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   
    5         536365     22752         SET 7 BABUSHKA NESTING BOXES         2   
    ...          ...       ...                                  ...       ...   
    541904    581587     22613          PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899         CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254        CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255      CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138        BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    1        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    2        12/1/2010 8:26       2.75       17850  United Kingdom       22.00  
    3        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    4        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    5        12/1/2010 8:26       7.65       17850  United Kingdom       15.30  
    ...                 ...        ...         ...             ...         ...  
    541904  12/9/2011 12:50       0.85       12680          France       10.20  
    541905  12/9/2011 12:50       2.10       12680          France       12.60  
    541906  12/9/2011 12:50       4.15       12680          France       16.60  
    541907  12/9/2011 12:50       4.15       12680          France       16.60  
    541908  12/9/2011 12:50       4.95       12680          France       14.85  

    [541908 rows x 9 columns]

</div>

</div>

<div class="cell code" execution_count="53" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:337,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676571916,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="0dLMmNNhpIVs" outputId="561d6aef-de5b-45d3-ebfa-dd74480a746b">

``` python
#Quedarse con las últimas cinco filas
df.drop(df.index[:-5])
```

<div class="output execute_result" execution_count="53">

           InvoiceNo StockCode                      Description  Quantity  \
    541904    581587     22613      PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899     CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254    CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255  CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138    BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID Country  TotalPrice  
    541904  12/9/2011 12:50       0.85       12680  France       10.20  
    541905  12/9/2011 12:50       2.10       12680  France       12.60  
    541906  12/9/2011 12:50       4.15       12680  France       16.60  
    541907  12/9/2011 12:50       4.15       12680  France       16.60  
    541908  12/9/2011 12:50       4.95       12680  France       14.85  

</div>

</div>

<div class="cell markdown" id="pIWxdLtgpvIB">

## **IX. Renombrar Datos**

Hay escenarios en los que los datos se nos presentan con nombres o encabezados que no se ajustan o describen con precisión los datos, por lo que podemos usar las funciones de Pandas para cambiar el nombre a uno más apropiado.

Esta función es `rename()`, que le permite cambiar los nombres de los índices y/o los nombres de las columnas.

</div>

<div class="cell code" execution_count="54" id="Tp69RIfAp7sR">

``` python
df.head()
```

<div class="output execute_result" execution_count="54">

      InvoiceNo StockCode                          Description  Quantity  \
    0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1    536365     71053                  WHITE METAL LANTERN         6   
    2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    0  12/1/2010 8:26       2.55       17850  United Kingdom       15.30  
    1  12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    2  12/1/2010 8:26       2.75       17850  United Kingdom       22.00  
    3  12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    4  12/1/2010 8:26       3.39       17850  United Kingdom       20.34  

</div>

</div>

<div class="cell code" execution_count="55" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:597}" executionInfo="{&quot;elapsed&quot;:667,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676601322,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="58b4DbRCqSH5" outputId="392cc305-a045-4916-df91-bb8d998bfa4f">

``` python
df = df.rename(columns={'Description': 'Product'})
df
```

<div class="output execute_result" execution_count="55">

           InvoiceNo StockCode                              Product  Quantity  \
    0         536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    1         536365     71053                  WHITE METAL LANTERN         6   
    2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   
    ...          ...       ...                                  ...       ...   
    541904    581587     22613          PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899         CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254        CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255      CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138        BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    0        12/1/2010 8:26       2.55       17850  United Kingdom       15.30  
    1        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    2        12/1/2010 8:26       2.75       17850  United Kingdom       22.00  
    3        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    4        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    ...                 ...        ...         ...             ...         ...  
    541904  12/9/2011 12:50       0.85       12680          France       10.20  
    541905  12/9/2011 12:50       2.10       12680          France       12.60  
    541906  12/9/2011 12:50       4.15       12680          France       16.60  
    541907  12/9/2011 12:50       4.15       12680          France       16.60  
    541908  12/9/2011 12:50       4.95       12680          France       14.85  

    [541909 rows x 9 columns]

</div>

</div>

<div class="cell markdown" id="uoekKW4Fqu_l">

`rename()` permite también cambiar index

</div>

<div class="cell code" execution_count="56" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:597}" executionInfo="{&quot;elapsed&quot;:432,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676627294,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KKjre5aPq0T6" outputId="e0070df9-15f5-49f1-b985-0af78e637a8e">

``` python
df=df.rename(index={0:'item 1', 1: 'item 2'})
df
```

<div class="output execute_result" execution_count="56">

           InvoiceNo StockCode                              Product  Quantity  \
    item 1    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    item 2    536365     71053                  WHITE METAL LANTERN         6   
    2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   
    ...          ...       ...                                  ...       ...   
    541904    581587     22613          PACK OF 20 SPACEBOY NAPKINS        12   
    541905    581587     22899         CHILDREN'S APRON DOLLY GIRL          6   
    541906    581587     23254        CHILDRENS CUTLERY DOLLY GIRL          4   
    541907    581587     23255      CHILDRENS CUTLERY CIRCUS PARADE         4   
    541908    581587     22138        BAKING SET 9 PIECE RETROSPOT          3   

                InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    item 1   12/1/2010 8:26       2.55       17850  United Kingdom       15.30  
    item 2   12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    2        12/1/2010 8:26       2.75       17850  United Kingdom       22.00  
    3        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    4        12/1/2010 8:26       3.39       17850  United Kingdom       20.34  
    ...                 ...        ...         ...             ...         ...  
    541904  12/9/2011 12:50       0.85       12680          France       10.20  
    541905  12/9/2011 12:50       2.10       12680          France       12.60  
    541906  12/9/2011 12:50       4.15       12680          France       16.60  
    541907  12/9/2011 12:50       4.15       12680          France       16.60  
    541908  12/9/2011 12:50       4.95       12680          France       14.85  

    [541909 rows x 9 columns]

</div>

</div>

<div class="cell markdown" id="XiAy4_4Brj2k">

## **X. Usando Pandas con otras funciones**

Ahora que estamos familiarizados con la funcionalidad y la sintaxis básicas de Pandas, exploremos cómo podemos combinar esto con otras modificaciones populares que se usan comúnmente en Python para crear estructuras de datos más sólidas y apropiadas para el análisis de datos.

</div>

<div class="cell markdown" id="uYMmNcHXr3I1">

**Usando funciones numpy**

</div>

<div class="cell code" execution_count="66" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:5685,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676685889,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="tqGM8Dlrr8aT" outputId="ba279203-d9fb-4497-cb92-b189921a68f3">

``` python
df['Quantity']
```

<div class="output execute_result" execution_count="66">

    item 1     6
    item 2     6
    2          8
    3          6
    4          6
              ..
    541904    12
    541905     6
    541906     4
    541907     4
    541908     3
    Name: Quantity, Length: 541909, dtype: int64

</div>

</div>

<div class="cell code" execution_count="67">

``` python
np.max(df['Quantity'])
```

<div class="output execute_result" execution_count="67">

    80995

</div>

</div>

<div class="cell markdown" id="iQq6K6Q7sIcY">

**Usando funciones lambda**

</div>

<div class="cell code" execution_count="58" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:299,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676751604,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="HDesEg5-sbGH" outputId="7f6eea2d-caa4-40a4-d534-5b1c54461bfe">

``` python
df['UnitPrice']=df['UnitPrice'].apply(lambda x: 1000 * x)
df['UnitPrice'].head()
```

<div class="output execute_result" execution_count="58">

    item 1    2550.0
    item 2    3390.0
    2         2750.0
    3         3390.0
    4         3390.0
    Name: UnitPrice, dtype: float64

</div>

</div>

<div class="cell markdown" id="3P7E9-7ptOKZ">

## **XI. Clasificación de datos**

Clasificar sus datos para una comprensión más refinada y precisa de los datos es un factor importante del análisis de datos, por lo tanto, podemos utilizar Pandas para llevar a cabo tales operaciones al organizar y resumir nuestros datos.

</div>

<div class="cell markdown" id="3T2r1FoYuL1K">

**Función Groupby** Podemos clasificar nuestros datos usando la función `groupby`

`df.groupby(by=grouping_columns)[columns_to_show].function()`

</div>

<div class="cell code" execution_count="59" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:447,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676885668,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="uxZ56QWuuC8i" outputId="5f09ac2c-9316-4035-9d2a-d658adf90407">

``` python
df.head()
```

<div class="output execute_result" execution_count="59">

           InvoiceNo StockCode                              Product  Quantity  \
    item 1    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    item 2    536365     71053                  WHITE METAL LANTERN         6   
    2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

               InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    item 1  12/1/2010 8:26     2550.0       17850  United Kingdom       15.30  
    item 2  12/1/2010 8:26     3390.0       17850  United Kingdom       20.34  
    2       12/1/2010 8:26     2750.0       17850  United Kingdom       22.00  
    3       12/1/2010 8:26     3390.0       17850  United Kingdom       20.34  
    4       12/1/2010 8:26     3390.0       17850  United Kingdom       20.34  

</div>

</div>

<div class="cell code" execution_count="60" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:300,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676908897,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Mn0yj-dpumiB" outputId="83d927f6-4270-495d-8e22-02042b40fd25">

``` python
df.groupby(['InvoiceDate'])['UnitPrice']
```

<div class="output execute_result" execution_count="60">

    <pandas.core.groupby.generic.SeriesGroupBy object at 0x000001ADAAE60B00>

</div>

</div>

<div class="cell markdown" id="pc-OhAORuw97">

Usando la función `groupby` y `describe` podemos obtener información estadística del conjunto de datos por `UnitPrice` y `InvoiceDate`

</div>

<div class="cell code" execution_count="61" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:37936,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712676979704,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Jy2Gbb4CucQF" outputId="28abcb1d-de46-4b66-aaa6-dd9ae5afeaf0">

``` python
print(df.groupby(['InvoiceDate'])['UnitPrice'].describe())
```

<div class="output stream stdout">

                     count         mean           std     min     25%     50%  \
    InvoiceDate                                                                 
    1/10/2011 10:04    1.0     0.000000           NaN     0.0     0.0     0.0   
    1/10/2011 10:07    1.0  3750.000000           NaN  3750.0  3750.0  3750.0   
    1/10/2011 10:08    1.0     0.000000           NaN     0.0     0.0     0.0   
    1/10/2011 10:32   23.0  1922.608696   1512.530142   210.0   850.0  1250.0   
    1/10/2011 10:35   17.0  3134.117647   5330.147816   190.0   190.0   850.0   
    ...                ...          ...           ...     ...     ...     ...   
    9/9/2011 8:48     16.0  5059.375000   2824.253220   850.0  3450.0  4950.0   
    9/9/2011 9:03     14.0  2797.857143   1637.935749   420.0  1025.0  3350.0   
    9/9/2011 9:13     45.0  3730.666667   3175.272644   420.0  1450.0  2950.0   
    9/9/2011 9:38     14.0  5026.428571  11656.627436   420.0  1050.0  1670.0   
    9/9/2011 9:52     37.0  2308.648649   2006.384479   390.0   830.0  1250.0   

                        75%      max  
    InvoiceDate                       
    1/10/2011 10:04     0.0      0.0  
    1/10/2011 10:07  3750.0   3750.0  
    1/10/2011 10:08     0.0      0.0  
    1/10/2011 10:32  2750.0   5950.0  
    1/10/2011 10:35  1650.0  18000.0  
    ...                 ...      ...  
    9/9/2011 8:48    8500.0   8950.0  
    9/9/2011 9:03    3750.0   5450.0  
    9/9/2011 9:13    4250.0  15000.0  
    9/9/2011 9:38    2737.5  45330.0  
    9/9/2011 9:52    3750.0   5950.0  

    [23260 rows x 8 columns]

</div>

</div>

<div class="cell markdown" id="BQqfLSZRu-_e">

**Función Pivot_table**

Para resumir datos, podemos emplear métodos similares a los de la función de Excel, tablas dinámicas, para evitar mostrar grandes cantidades de datos.

`df.pivot_table([rows_to_be_displayed'],                [columns_to_be_displayed], aggfunc=function)`

</div>

<div class="cell markdown" id="bzI93X5Wvyth">

¿Podemos crear una tabla dinámica que muestre los precios promedio y la cantidad neta de pedidos fallidos y exitosos en fechas específicas?

</div>

<div class="cell code" execution_count="62" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:293}" executionInfo="{&quot;elapsed&quot;:417,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1712677184201,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="hLVrVWHAwMFt" outputId="943fc92b-5ece-460b-b885-2133270ecbaf">

``` python
df.head()
```

<div class="output execute_result" execution_count="62">

           InvoiceNo StockCode                              Product  Quantity  \
    item 1    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   
    item 2    536365     71053                  WHITE METAL LANTERN         6   
    2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
    3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
    4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

               InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice  
    item 1  12/1/2010 8:26     2550.0       17850  United Kingdom       15.30  
    item 2  12/1/2010 8:26     3390.0       17850  United Kingdom       20.34  
    2       12/1/2010 8:26     2750.0       17850  United Kingdom       22.00  
    3       12/1/2010 8:26     3390.0       17850  United Kingdom       20.34  
    4       12/1/2010 8:26     3390.0       17850  United Kingdom       20.34  

</div>

</div>

<div class="cell code" execution_count="63" id="NdB2BukJwJYz">

``` python
df.pivot_table(index = 'Country', columns='Product', values='Quantity', aggfunc='sum')
```

<div class="output execute_result" execution_count="63">

    Product                4 PURPLE FLOCK DINNER CANDLES  \
    Country                                                
    Australia                                        NaN   
    Austria                                          NaN   
    Bahrain                                          NaN   
    Belgium                                          NaN   
    Brazil                                           NaN   
    Canada                                           NaN   
    Channel Islands                                  NaN   
    Cyprus                                           NaN   
    Czech Republic                                   NaN   
    Denmark                                          NaN   
    EIRE                                             6.0   
    European Community                               NaN   
    Finland                                          NaN   
    France                                           NaN   
    Germany                                          NaN   
    Greece                                           NaN   
    Hong Kong                                        NaN   
    Iceland                                          NaN   
    Israel                                           NaN   
    Italy                                            NaN   
    Japan                                            NaN   
    Lebanon                                          NaN   
    Lithuania                                        NaN   
    Malta                                            NaN   
    Netherlands                                      NaN   
    Norway                                           NaN   
    Poland                                           NaN   
    Portugal                                         NaN   
    RSA                                              NaN   
    Saudi Arabia                                     NaN   
    Singapore                                        NaN   
    Spain                                            NaN   
    Sweden                                           NaN   
    Switzerland                                      NaN   
    USA                                              NaN   
    United Arab Emirates                             NaN   
    United Kingdom                                 138.0   
    Unspecified                                      NaN   

    Product                50'S CHRISTMAS GIFT BAG LARGE   DOLLY GIRL BEAKER  \
    Country                                                                    
    Australia                                        NaN               200.0   
    Austria                                          NaN                12.0   
    Bahrain                                          NaN                 NaN   
    Belgium                                          NaN                60.0   
    Brazil                                           NaN                 NaN   
    Canada                                           NaN                 NaN   
    Channel Islands                                  NaN                 NaN   
    Cyprus                                           NaN                12.0   
    Czech Republic                                   NaN                 NaN   
    Denmark                                          NaN                 NaN   
    EIRE                                            48.0                24.0   
    European Community                               NaN                 NaN   
    Finland                                          NaN                 NaN   
    France                                          12.0               120.0   
    Germany                                         60.0                84.0   
    Greece                                           NaN                 NaN   
    Hong Kong                                        NaN                 NaN   
    Iceland                                          NaN                 NaN   
    Israel                                           NaN                12.0   
    Italy                                            NaN                 NaN   
    Japan                                            NaN                 NaN   
    Lebanon                                          NaN                 NaN   
    Lithuania                                        NaN                 NaN   
    Malta                                            NaN                 NaN   
    Netherlands                                      NaN              1201.0   
    Norway                                           NaN                12.0   
    Poland                                           NaN                 NaN   
    Portugal                                        56.0                 NaN   
    RSA                                              NaN                 NaN   
    Saudi Arabia                                     NaN                 NaN   
    Singapore                                        NaN                 NaN   
    Spain                                           12.0                 NaN   
    Sweden                                           NaN                 NaN   
    Switzerland                                      NaN                 NaN   
    USA                                              NaN                 NaN   
    United Arab Emirates                             NaN                 NaN   
    United Kingdom                                1725.0               711.0   
    Unspecified                                      NaN                 NaN   

    Product                I LOVE LONDON MINI BACKPACK  \
    Country                                              
    Australia                                      4.0   
    Austria                                        NaN   
    Bahrain                                        NaN   
    Belgium                                        4.0   
    Brazil                                         NaN   
    Canada                                         NaN   
    Channel Islands                                NaN   
    Cyprus                                         4.0   
    Czech Republic                                 NaN   
    Denmark                                        NaN   
    EIRE                                           NaN   
    European Community                             NaN   
    Finland                                        NaN   
    France                                        19.0   
    Germany                                        8.0   
    Greece                                         NaN   
    Hong Kong                                      4.0   
    Iceland                                        NaN   
    Israel                                         NaN   
    Italy                                          NaN   
    Japan                                         40.0   
    Lebanon                                        NaN   
    Lithuania                                      NaN   
    Malta                                          NaN   
    Netherlands                                  100.0   
    Norway                                         NaN   
    Poland                                         NaN   
    Portugal                                       NaN   
    RSA                                            NaN   
    Saudi Arabia                                   NaN   
    Singapore                                      NaN   
    Spain                                          NaN   
    Sweden                                         NaN   
    Switzerland                                    NaN   
    USA                                            NaN   
    United Arab Emirates                           NaN   
    United Kingdom                               206.0   
    Unspecified                                    NaN   

    Product                I LOVE LONDON MINI RUCKSACK   NINE DRAWER OFFICE TIDY  \
    Country                                                                        
    Australia                                      NaN                       NaN   
    Austria                                        NaN                       NaN   
    Bahrain                                        NaN                       NaN   
    Belgium                                        NaN                       NaN   
    Brazil                                         NaN                       NaN   
    Canada                                         NaN                       NaN   
    Channel Islands                                NaN                       NaN   
    Cyprus                                         NaN                       4.0   
    Czech Republic                                 NaN                       NaN   
    Denmark                                        NaN                       NaN   
    EIRE                                           NaN                       2.0   
    European Community                             NaN                       NaN   
    Finland                                        NaN                       2.0   
    France                                         NaN                       2.0   
    Germany                                        NaN                       NaN   
    Greece                                         NaN                       NaN   
    Hong Kong                                      NaN                       NaN   
    Iceland                                        NaN                       NaN   
    Israel                                         NaN                       NaN   
    Italy                                          NaN                       NaN   
    Japan                                          NaN                       NaN   
    Lebanon                                        NaN                       NaN   
    Lithuania                                      NaN                       NaN   
    Malta                                          NaN                       NaN   
    Netherlands                                    1.0                       NaN   
    Norway                                         NaN                       NaN   
    Poland                                         NaN                       NaN   
    Portugal                                       NaN                       1.0   
    RSA                                            NaN                       NaN   
    Saudi Arabia                                   NaN                       NaN   
    Singapore                                      NaN                       NaN   
    Spain                                          NaN                       NaN   
    Sweden                                         NaN                       NaN   
    Switzerland                                    NaN                       NaN   
    USA                                            NaN                       NaN   
    United Arab Emirates                           NaN                       NaN   
    United Kingdom                                 NaN                      48.0   
    Unspecified                                    NaN                       NaN   

    Product                OVAL WALL MIRROR DIAMANTE    RED SPOT GIFT BAG LARGE  \
    Country                                                                       
    Australia                                     NaN                       NaN   
    Austria                                       NaN                       NaN   
    Bahrain                                       NaN                       NaN   
    Belgium                                       NaN                       NaN   
    Brazil                                        NaN                       NaN   
    Canada                                        NaN                       NaN   
    Channel Islands                               NaN                       NaN   
    Cyprus                                        NaN                       NaN   
    Czech Republic                                NaN                       NaN   
    Denmark                                       NaN                       NaN   
    EIRE                                          7.0                      48.0   
    European Community                            NaN                       NaN   
    Finland                                       NaN                       NaN   
    France                                        NaN                       NaN   
    Germany                                       NaN                      48.0   
    Greece                                        NaN                       NaN   
    Hong Kong                                     NaN                       NaN   
    Iceland                                       NaN                       NaN   
    Israel                                        NaN                       NaN   
    Italy                                         NaN                       NaN   
    Japan                                         NaN                       NaN   
    Lebanon                                       NaN                       NaN   
    Lithuania                                     NaN                       NaN   
    Malta                                         NaN                       NaN   
    Netherlands                                   NaN                       NaN   
    Norway                                        2.0                       NaN   
    Poland                                        NaN                       NaN   
    Portugal                                      NaN                      24.0   
    RSA                                           NaN                       NaN   
    Saudi Arabia                                  NaN                       NaN   
    Singapore                                     NaN                       NaN   
    Spain                                         NaN                      12.0   
    Sweden                                        NaN                       NaN   
    Switzerland                                   NaN                      12.0   
    USA                                           NaN                       NaN   
    United Arab Emirates                          NaN                       NaN   
    United Kingdom                              224.0                    1583.0   
    Unspecified                                   NaN                       NaN   

    Product                SET 2 TEA TOWELS I LOVE LONDON   \
    Country                                                  
    Australia                                          NaN   
    Austria                                            NaN   
    Bahrain                                            NaN   
    Belgium                                            NaN   
    Brazil                                             NaN   
    Canada                                             NaN   
    Channel Islands                                    NaN   
    Cyprus                                             6.0   
    Czech Republic                                     NaN   
    Denmark                                            NaN   
    EIRE                                               NaN   
    European Community                                 NaN   
    Finland                                            NaN   
    France                                           132.0   
    Germany                                           48.0   
    Greece                                             NaN   
    Hong Kong                                          6.0   
    Iceland                                            NaN   
    Israel                                             NaN   
    Italy                                              NaN   
    Japan                                              NaN   
    Lebanon                                            NaN   
    Lithuania                                          NaN   
    Malta                                              NaN   
    Netherlands                                        NaN   
    Norway                                             NaN   
    Poland                                             NaN   
    Portugal                                           NaN   
    RSA                                                NaN   
    Saudi Arabia                                       NaN   
    Singapore                                          NaN   
    Spain                                              8.0   
    Sweden                                             NaN   
    Switzerland                                        NaN   
    USA                                                3.0   
    United Arab Emirates                               NaN   
    United Kingdom                                  2578.0   
    Unspecified                                        NaN   

    Product                SPACEBOY BABY GIFT SET  ...  wrongly coded 20713  \
    Country                                        ...                        
    Australia                                 NaN  ...                  NaN   
    Austria                                   6.0  ...                  NaN   
    Bahrain                                   NaN  ...                  NaN   
    Belgium                                  10.0  ...                  NaN   
    Brazil                                    NaN  ...                  NaN   
    Canada                                    NaN  ...                  NaN   
    Channel Islands                           3.0  ...                  NaN   
    Cyprus                                    NaN  ...                  NaN   
    Czech Republic                            NaN  ...                  NaN   
    Denmark                                  24.0  ...                  NaN   
    EIRE                                     54.0  ...                  NaN   
    European Community                        NaN  ...                  NaN   
    Finland                                   NaN  ...                  NaN   
    France                                   86.0  ...                  NaN   
    Germany                                  12.0  ...                  NaN   
    Greece                                    NaN  ...                  NaN   
    Hong Kong                                 NaN  ...                  NaN   
    Iceland                                   NaN  ...                  NaN   
    Israel                                    NaN  ...                  NaN   
    Italy                                     NaN  ...                  NaN   
    Japan                                     NaN  ...                  NaN   
    Lebanon                                   NaN  ...                  NaN   
    Lithuania                                 NaN  ...                  NaN   
    Malta                                     NaN  ...                  NaN   
    Netherlands                              39.0  ...                  NaN   
    Norway                                    NaN  ...                  NaN   
    Poland                                    NaN  ...                  NaN   
    Portugal                                  NaN  ...                  NaN   
    RSA                                       NaN  ...                  NaN   
    Saudi Arabia                              NaN  ...                  NaN   
    Singapore                                 NaN  ...                  NaN   
    Spain                                     6.0  ...                  NaN   
    Sweden                                    NaN  ...                  NaN   
    Switzerland                              22.0  ...                  NaN   
    USA                                       NaN  ...                  NaN   
    United Arab Emirates                      6.0  ...                  NaN   
    United Kingdom                          223.0  ...               -200.0   
    Unspecified                               2.0  ...                  NaN   

    Product               wrongly coded 23343  wrongly coded-23343  \
    Country                                                          
    Australia                             NaN                  NaN   
    Austria                               NaN                  NaN   
    Bahrain                               NaN                  NaN   
    Belgium                               NaN                  NaN   
    Brazil                                NaN                  NaN   
    Canada                                NaN                  NaN   
    Channel Islands                       NaN                  NaN   
    Cyprus                                NaN                  NaN   
    Czech Republic                        NaN                  NaN   
    Denmark                               NaN                  NaN   
    EIRE                                  NaN                  NaN   
    European Community                    NaN                  NaN   
    Finland                               NaN                  NaN   
    France                                NaN                  NaN   
    Germany                               NaN                  NaN   
    Greece                                NaN                  NaN   
    Hong Kong                             NaN                  NaN   
    Iceland                               NaN                  NaN   
    Israel                                NaN                  NaN   
    Italy                                 NaN                  NaN   
    Japan                                 NaN                  NaN   
    Lebanon                               NaN                  NaN   
    Lithuania                             NaN                  NaN   
    Malta                                 NaN                  NaN   
    Netherlands                           NaN                  NaN   
    Norway                                NaN                  NaN   
    Poland                                NaN                  NaN   
    Portugal                              NaN                  NaN   
    RSA                                   NaN                  NaN   
    Saudi Arabia                          NaN                  NaN   
    Singapore                             NaN                  NaN   
    Spain                                 NaN                  NaN   
    Sweden                                NaN                  NaN   
    Switzerland                           NaN                  NaN   
    USA                                   NaN                  NaN   
    United Arab Emirates                  NaN                  NaN   
    United Kingdom                     1000.0               -800.0   
    Unspecified                           NaN                  NaN   

    Product               wrongly marked  wrongly marked 23343  \
    Country                                                      
    Australia                        NaN                   NaN   
    Austria                          NaN                   NaN   
    Bahrain                          NaN                   NaN   
    Belgium                          NaN                   NaN   
    Brazil                           NaN                   NaN   
    Canada                           NaN                   NaN   
    Channel Islands                  NaN                   NaN   
    Cyprus                           NaN                   NaN   
    Czech Republic                   NaN                   NaN   
    Denmark                          NaN                   NaN   
    EIRE                             NaN                   NaN   
    European Community               NaN                   NaN   
    Finland                          NaN                   NaN   
    France                           NaN                   NaN   
    Germany                          NaN                   NaN   
    Greece                           NaN                   NaN   
    Hong Kong                        NaN                   NaN   
    Iceland                          NaN                   NaN   
    Israel                           NaN                   NaN   
    Italy                            NaN                   NaN   
    Japan                            NaN                   NaN   
    Lebanon                          NaN                   NaN   
    Lithuania                        NaN                   NaN   
    Malta                            NaN                   NaN   
    Netherlands                      NaN                   NaN   
    Norway                           NaN                   NaN   
    Poland                           NaN                   NaN   
    Portugal                         NaN                   NaN   
    RSA                              NaN                   NaN   
    Saudi Arabia                     NaN                   NaN   
    Singapore                        NaN                   NaN   
    Spain                            NaN                   NaN   
    Sweden                           NaN                   NaN   
    Switzerland                      NaN                   NaN   
    USA                              NaN                   NaN   
    United Arab Emirates             NaN                   NaN   
    United Kingdom                  48.0                 200.0   
    Unspecified                      NaN                   NaN   

    Product               wrongly marked carton 22804  \
    Country                                             
    Australia                                     NaN   
    Austria                                       NaN   
    Bahrain                                       NaN   
    Belgium                                       NaN   
    Brazil                                        NaN   
    Canada                                        NaN   
    Channel Islands                               NaN   
    Cyprus                                        NaN   
    Czech Republic                                NaN   
    Denmark                                       NaN   
    EIRE                                          NaN   
    European Community                            NaN   
    Finland                                       NaN   
    France                                        NaN   
    Germany                                       NaN   
    Greece                                        NaN   
    Hong Kong                                     NaN   
    Iceland                                       NaN   
    Israel                                        NaN   
    Italy                                         NaN   
    Japan                                         NaN   
    Lebanon                                       NaN   
    Lithuania                                     NaN   
    Malta                                         NaN   
    Netherlands                                   NaN   
    Norway                                        NaN   
    Poland                                        NaN   
    Portugal                                      NaN   
    RSA                                           NaN   
    Saudi Arabia                                  NaN   
    Singapore                                     NaN   
    Spain                                         NaN   
    Sweden                                        NaN   
    Switzerland                                   NaN   
    USA                                           NaN   
    United Arab Emirates                          NaN   
    United Kingdom                             -256.0   
    Unspecified                                   NaN   

    Product               wrongly marked. 23343 in box  \
    Country                                              
    Australia                                      NaN   
    Austria                                        NaN   
    Bahrain                                        NaN   
    Belgium                                        NaN   
    Brazil                                         NaN   
    Canada                                         NaN   
    Channel Islands                                NaN   
    Cyprus                                         NaN   
    Czech Republic                                 NaN   
    Denmark                                        NaN   
    EIRE                                           NaN   
    European Community                             NaN   
    Finland                                        NaN   
    France                                         NaN   
    Germany                                        NaN   
    Greece                                         NaN   
    Hong Kong                                      NaN   
    Iceland                                        NaN   
    Israel                                         NaN   
    Italy                                          NaN   
    Japan                                          NaN   
    Lebanon                                        NaN   
    Lithuania                                      NaN   
    Malta                                          NaN   
    Netherlands                                    NaN   
    Norway                                         NaN   
    Poland                                         NaN   
    Portugal                                       NaN   
    RSA                                            NaN   
    Saudi Arabia                                   NaN   
    Singapore                                      NaN   
    Spain                                          NaN   
    Sweden                                         NaN   
    Switzerland                                    NaN   
    USA                                            NaN   
    United Arab Emirates                           NaN   
    United Kingdom                             -3100.0   
    Unspecified                                    NaN   

    Product               wrongly sold (22719) barcode  wrongly sold as sets  \
    Country                                                                    
    Australia                                      NaN                   NaN   
    Austria                                        NaN                   NaN   
    Bahrain                                        NaN                   NaN   
    Belgium                                        NaN                   NaN   
    Brazil                                         NaN                   NaN   
    Canada                                         NaN                   NaN   
    Channel Islands                                NaN                   NaN   
    Cyprus                                         NaN                   NaN   
    Czech Republic                                 NaN                   NaN   
    Denmark                                        NaN                   NaN   
    EIRE                                           NaN                   NaN   
    European Community                             NaN                   NaN   
    Finland                                        NaN                   NaN   
    France                                         NaN                   NaN   
    Germany                                        NaN                   NaN   
    Greece                                         NaN                   NaN   
    Hong Kong                                      NaN                   NaN   
    Iceland                                        NaN                   NaN   
    Israel                                         NaN                   NaN   
    Italy                                          NaN                   NaN   
    Japan                                          NaN                   NaN   
    Lebanon                                        NaN                   NaN   
    Lithuania                                      NaN                   NaN   
    Malta                                          NaN                   NaN   
    Netherlands                                    NaN                   NaN   
    Norway                                         NaN                   NaN   
    Poland                                         NaN                   NaN   
    Portugal                                       NaN                   NaN   
    RSA                                            NaN                   NaN   
    Saudi Arabia                                   NaN                   NaN   
    Singapore                                      NaN                   NaN   
    Spain                                          NaN                   NaN   
    Sweden                                         NaN                   NaN   
    Switzerland                                    NaN                   NaN   
    USA                                            NaN                   NaN   
    United Arab Emirates                           NaN                   NaN   
    United Kingdom                               170.0                -600.0   
    Unspecified                                    NaN                   NaN   

    Product               wrongly sold sets  
    Country                                  
    Australia                           NaN  
    Austria                             NaN  
    Bahrain                             NaN  
    Belgium                             NaN  
    Brazil                              NaN  
    Canada                              NaN  
    Channel Islands                     NaN  
    Cyprus                              NaN  
    Czech Republic                      NaN  
    Denmark                             NaN  
    EIRE                                NaN  
    European Community                  NaN  
    Finland                             NaN  
    France                              NaN  
    Germany                             NaN  
    Greece                              NaN  
    Hong Kong                           NaN  
    Iceland                             NaN  
    Israel                              NaN  
    Italy                               NaN  
    Japan                               NaN  
    Lebanon                             NaN  
    Lithuania                           NaN  
    Malta                               NaN  
    Netherlands                         NaN  
    Norway                              NaN  
    Poland                              NaN  
    Portugal                            NaN  
    RSA                                 NaN  
    Saudi Arabia                        NaN  
    Singapore                           NaN  
    Spain                               NaN  
    Sweden                              NaN  
    Switzerland                         NaN  
    USA                                 NaN  
    United Arab Emirates                NaN  
    United Kingdom                   -975.0  
    Unspecified                         NaN  

    [38 rows x 4223 columns]

</div>

</div>
