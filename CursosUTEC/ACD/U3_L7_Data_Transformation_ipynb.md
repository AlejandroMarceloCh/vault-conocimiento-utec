---
curso: ACD
titulo: U3_L7 Data Transformation
slides: 0
fuente: U3_L7 Data Transformation.ipynb
---

<div class="cell markdown" id="3UvfhoPN-Z06">

# **U3_L7 Data Transformation**

## **Objetivo:**

Al finalizar el laboratorio, el estudiante será capaz de transformar los datos a partir de diferentes técnicas.

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:3900,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718590668003,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="yT-2gj7s-TS8">

``` python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

</div>

<div class="cell markdown" id="z-5gJmxG_9Bs">

## **I. Codificación Binaria**

Es la única opción de transformar atributos nominales a numéricos.

</div>

<div class="cell markdown" id="nxHSB3FzDPLZ">

**Contexto:** Usaremos el dataset preprocesado sobre *The World Happiness Report* que incluye datos de 2010 a 2019.

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:226}" executionInfo="{&quot;elapsed&quot;:361,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592087788,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pMsPe4I3_I0A" outputId="96bc1df2-f79e-4419-f3c9-e5c7a87b7e8e">

``` python
report_df = pd.read_csv('WH Report_preprocessed.csv')
report_df.head()
```

<div class="output execute_result" execution_count="9">

``` json
{"summary":"{\n  \"name\": \"report_df\",\n  \"rows\": 1220,\n  \"fields\": [\n    {\n      \"column\": \"Name\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 122,\n        \"samples\": [\n          \"Burkina Faso\",\n          \"Haiti\",\n          \"Hungary\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Continent\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Asia\",\n          \"Europe\",\n          \"North America\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2,\n        \"min\": 2010,\n        \"max\": 2019,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          2018,\n          2011,\n          2015\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"population\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 173313056.1025001,\n        \"min\": 318041.0,\n        \"max\": 1397715000.0,\n        \"num_unique_values\": 1220,\n        \"samples\": [\n          59539717.0,\n          50339443.0,\n          2897584.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Life_Ladder\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.152958028337429,\n        \"min\": 2.375,\n        \"max\": 7.858,\n        \"num_unique_values\": 1045,\n        \"samples\": [\n          5.683,\n          6.25,\n          6.155\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Log_GDP_per_capita\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.1621518123850239,\n        \"min\": 6.885,\n        \"max\": 11.648,\n        \"num_unique_values\": 1011,\n        \"samples\": [\n          9.81,\n          9.867,\n          10.867\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Social_support\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.1190888233101127,\n        \"min\": 0.303,\n        \"max\": 0.987,\n        \"num_unique_values\": 408,\n        \"samples\": [\n          0.877,\n          0.933,\n          0.542\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Healthy_life_expectancy_at_birth\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7.148289559556728,\n        \"min\": 32.3,\n        \"max\": 77.1,\n        \"num_unique_values\": 564,\n        \"samples\": [\n          52.04,\n          51.58,\n          67.28\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Freedom_to_make_life_choices\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.1368902458737292,\n        \"min\": 0.304,\n        \"max\": 0.985,\n        \"num_unique_values\": 482,\n        \"samples\": [\n          0.947,\n          0.98,\n          0.912\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Generosity\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.16634883158364563,\n        \"min\": -0.335,\n        \"max\": 0.698,\n        \"num_unique_values\": 542,\n        \"samples\": [\n          0.212,\n          0.0712499999999999,\n          -0.152\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Perceptions_of_corruption\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.1929678596471981,\n        \"min\": 0.047,\n        \"max\": 0.983,\n        \"num_unique_values\": 521,\n        \"samples\": [\n          0.519,\n          0.664,\n          0.7929999999999999\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Positive_affect\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.10879542097062088,\n        \"min\": 0.322,\n        \"max\": 0.944,\n        \"num_unique_values\": 409,\n        \"samples\": [\n          0.8029999999999999,\n          0.623,\n          0.6559999999999999\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Negative_affect\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.08284900996343249,\n        \"min\": 0.095,\n        \"max\": 0.591,\n        \"num_unique_values\": 351,\n        \"samples\": [\n          0.263,\n          0.382,\n          0.2685\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"report_df"}
```

</div>

</div>

<div class="cell markdown" id="S6-5dp7U_J1Y">

**Objetivo Análitico:** Realizar un agrupamiento de los países en base al continente al que pertenecen para analizar sus indicadores durante el año 2019.

Dado que se realizará un agrupamiento se necesita que los atributos sean *númericos*. Desarrolle los siguientes ejercicios:

</div>

<div class="cell markdown" id="o7LASCUjDI20">

### **Ejercicio 1:**

Crea un subdataframe que sólo contenga los datos del año 2019 donde el índice sea el país.

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:510}" executionInfo="{&quot;elapsed&quot;:336,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592094684,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="zwLJvqPe_aP1" outputId="dcbc94c2-d454-4909-87be-561b9ebfb569">

``` python
BM = report_df.year == 2019
report2019_df = report_df[BM]
report2019_df.set_index('Name',inplace=True)
report2019_df
```

<div class="output execute_result" execution_count="10">

``` json
{"summary":"{\n  \"name\": \"report2019_df\",\n  \"rows\": 122,\n  \"fields\": [\n    {\n      \"column\": \"Name\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 122,\n        \"samples\": [\n          \"Burkina Faso\",\n          \"Haiti\",\n          \"Hungary\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Continent\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Asia\",\n          \"Europe\",\n          \"North America\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 2019,\n        \"max\": 2019,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          2019\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"population\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 180149284.2086378,\n        \"min\": 361313.0,\n        \"max\": 1397715000.0,\n        \"num_unique_values\": 122,\n        \"samples\": [\n          20321378.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Life_Ladder\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.1689108313738141,\n        \"min\": 2.375,\n        \"max\": 7.78,\n        \"num_unique_values\": 121,\n        \"samples\": [\n          4.768\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Log_GDP_per_capita\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.1550621542609445,\n        \"min\": 6.966,\n        \"max\": 11.648,\n        \"num_unique_values\": 122,\n        \"samples\": [\n          7.691\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Social_support\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.12466174393002386,\n        \"min\": 0.42,\n        \"max\": 0.982,\n        \"num_unique_values\": 97,\n        \"samples\": [\n          0.922\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Healthy_life_expectancy_at_birth\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 6.396878313752248,\n        \"min\": 48.7,\n        \"max\": 77.1,\n        \"num_unique_values\": 93,\n        \"samples\": [\n          55.7\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Freedom_to_make_life_choices\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.11820594159389439,\n        \"min\": 0.385,\n        \"max\": 0.97,\n        \"num_unique_values\": 107,\n        \"samples\": [\n          0.7290000000000001\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Generosity\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.16123115780914002,\n        \"min\": -0.292,\n        \"max\": 0.561,\n        \"num_unique_values\": 111,\n        \"samples\": [\n          0.111\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Perceptions_of_corruption\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.19265009561781338,\n        \"min\": 0.07,\n        \"max\": 0.963,\n        \"num_unique_values\": 108,\n        \"samples\": [\n          0.8740000000000001\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Positive_affect\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.11278810194754327,\n        \"min\": 0.322,\n        \"max\": 0.8909999999999999,\n        \"num_unique_values\": 102,\n        \"samples\": [\n          0.784\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Negative_affect\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.0893885115009108,\n        \"min\": 0.138,\n        \"max\": 0.502,\n        \"num_unique_values\": 107,\n        \"samples\": [\n          0.195\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"report2019_df"}
```

</div>

</div>

<div class="cell markdown" id="Ol7YSm8eDoTV">

### **Ejercicio 2:**

Dado que el atributo `Continent` que es de tipo nominal la única opción que tenemos es realizar codificación binaria para convertirlo a un atributo numérico y con ello se considere como hiperparámetro dentro de un algoritmo de agrupamiento.

La función `get_dummies()` de Pandas convierte la variable categórica en variables dummies(fictisias).

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:238}" executionInfo="{&quot;elapsed&quot;:418,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592188837,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="fidUdPsx_geg" outputId="4f1fea45-b9fe-4ea7-ebcd-9473b87843ff">

``` python
bc_Continent = pd.get_dummies(report2019_df.Continent, dtype=int)
bc_Continent.head(5)
```

<div class="output execute_result" execution_count="12">

``` json
{"summary":"{\n  \"name\": \"bc_Continent\",\n  \"rows\": 122,\n  \"fields\": [\n    {\n      \"column\": \"Name\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 122,\n        \"samples\": [\n          \"Burkina Faso\",\n          \"Haiti\",\n          \"Hungary\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Africa\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Antarctica\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Asia\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Europe\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"North America\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Oceania\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"South America\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"bc_Continent"}
```

</div>

</div>

<div class="cell markdown" id="8Ek6tnCRFBDX">

### **Clustering**

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:1104,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592232907,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pIpW8wWkFDPu" outputId="db21a60e-b5dd-4c21-8c70-bea812e8a17b">

``` python
from sklearn.cluster import KMeans
dimensions = ['Life_Ladder', 'Log_GDP_per_capita', 'Social_support',
              'Healthy_life_expectancy_at_birth', 'Freedom_to_make_life_choices',
              'Generosity', 'Perceptions_of_corruption', 'Positive_affect', 'Negative_affect']
Xs = report2019_df[dimensions]
Xs = (Xs - Xs.min())/(Xs.max()-Xs.min())
Xs = Xs.join(bc_Continent/7)
kmeans = KMeans(n_clusters=3)
kmeans.fit(Xs)

for i in range(3):
    BM = kmeans.labels_==i
    print('Cluster {}: {}'.format(i,Xs[BM].index.values))
```

<div class="output stream stdout">

    Cluster 0: ['Afghanistan' 'Algeria' 'Bangladesh' 'Benin' 'Burkina Faso' 'Cambodia'
     'Cameroon' 'Chad' 'Ethiopia' 'Gabon' 'Ghana' 'Guinea' 'Haiti' 'India'
     'Iraq' 'Jordan' 'Kenya' 'Lebanon' 'Liberia' 'Madagascar' 'Malawi' 'Mali'
     'Mauritania' 'Morocco' 'Myanmar' 'Nepal' 'Niger' 'Nigeria' 'Pakistan'
     'Rwanda' 'Senegal' 'Sierra Leone' 'Tanzania' 'Togo' 'Tunisia' 'Uganda'
     'Zambia' 'Zimbabwe']
    Cluster 1: ['Albania' 'Argentina' 'Armenia' 'Azerbaijan' 'Belarus' 'Belgium'
     'Bolivia' 'Bosnia and Herzegovina' 'Botswana' 'Brazil' 'Bulgaria' 'Chile'
     'China' 'Colombia' 'Costa Rica' 'Croatia' 'Cyprus' 'Czech Republic'
     'Dominican Republic' 'Ecuador' 'El Salvador' 'Georgia' 'Greece'
     'Guatemala' 'Honduras' 'Hungary' 'Indonesia' 'Israel' 'Italy' 'Japan'
     'Kazakhstan' 'Kuwait' 'Latvia' 'Libya' 'Lithuania' 'Malaysia' 'Malta'
     'Mexico' 'Moldova' 'Mongolia' 'Montenegro' 'Nicaragua' 'Panama'
     'Paraguay' 'Peru' 'Philippines' 'Poland' 'Portugal' 'Romania'
     'Saudi Arabia' 'Serbia' 'Slovenia' 'South Africa' 'Spain' 'Sri Lanka'
     'Tajikistan' 'Thailand' 'Turkey' 'Turkmenistan' 'Ukraine' 'Vietnam']
    Cluster 2: ['Australia' 'Austria' 'Bahrain' 'Canada' 'Denmark' 'Estonia' 'Finland'
     'France' 'Germany' 'Iceland' 'Ireland' 'Luxembourg' 'Netherlands'
     'New Zealand' 'Norway' 'Singapore' 'Sweden' 'Switzerland'
     'United Arab Emirates' 'United Kingdom' 'United States' 'Uruguay'
     'Uzbekistan']

</div>

<div class="output stream stderr">

    /usr/local/lib/python3.10/dist-packages/sklearn/cluster/_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(

</div>

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:586}" executionInfo="{&quot;elapsed&quot;:1585,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592284471,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="nrPO1lAfFPYf" outputId="79fcbbac-afc4-4017-86bd-3c85893c49b1">

``` python
#Visualización de Clusters
clusters = ['Cluster {}'.format(i) for i in range(3)]

Centroids = pd.DataFrame(0.0, index =  clusters,
                        columns = Xs.columns)
for i,clst in enumerate(clusters):
    BM = kmeans.labels_==i
    Centroids.loc[clst] = Xs[BM].mean(axis=0)

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
sns.heatmap(Centroids[dimensions], linewidths=.5,
            annot=True, cmap='binary')
plt.subplot(1,2,2)
sns.heatmap(Centroids[bc_Continent.columns],
            linewidths=.5, annot=True, cmap='binary')
plt.show()
```

<div class="output display_data">

![](ef932b6f2777e99d96d818dd81770b90e4befc98.png)

</div>

</div>

<div class="cell markdown" id="-6CgplZ2Fn2Y">

## **II. Discretización de Atributos Numéricos**

Pasar de datos numéricos a datos categóricos.

</div>

<div class="cell markdown" id="1Ym5yu2_Fyr8">

### **Ejercicio 3:**

Para este ejercicio utilizaremos un dataset de Adultos (trabajado en laboratorios anteriores).

1.  Realice el análisis univariado de `hoursPerWeek` en base a un histograma.
2.  Analice la relación entre las horas que trabaja una persona, su ingreso salarial y su género. ¿Existe alguna relación? Escoga la herramienta gráfica adecuada.

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:617}" executionInfo="{&quot;elapsed&quot;:834,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592502068,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="er3MICghF2eJ" outputId="5f3fcf46-7a70-4d23-f7a5-d34136aec7b3">

``` python
adult_df = pd.read_csv('adult.csv')
adult_df
```

<div class="output execute_result" execution_count="15">

``` json
{"summary":"{\n  \"name\": \"adult_df\",\n  \"rows\": 32561,\n  \"fields\": [\n    {\n      \"column\": \"age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 13,\n        \"min\": 17,\n        \"max\": 90,\n        \"num_unique_values\": 73,\n        \"samples\": [\n          28,\n          73,\n          35\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"workclass\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 8,\n        \"samples\": [\n          \"Self-emp-not-inc\",\n          \"Self-emp-inc\",\n          \"State-gov\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"fnlwgt\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 105549,\n        \"min\": 12285,\n        \"max\": 1484705,\n        \"num_unique_values\": 21648,\n        \"samples\": [\n          128485,\n          469907,\n          235951\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 16,\n        \"samples\": [\n          \"Bachelors\",\n          \"HS-grad\",\n          \"Some-college\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education-num\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2,\n        \"min\": 1,\n        \"max\": 16,\n        \"num_unique_values\": 16,\n        \"samples\": [\n          13,\n          9,\n          10\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"marital-status\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Never-married\",\n          \"Married-civ-spouse\",\n          \"Married-AF-spouse\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"occupation\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 14,\n        \"samples\": [\n          \"Machine-op-inspct\",\n          \"Protective-serv\",\n          \"Adm-clerical\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"relationship\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Not-in-family\",\n          \"Husband\",\n          \"Other-relative\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"race\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"Black\",\n          \"Other\",\n          \"Asian-Pac-Islander\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"sex\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Female\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capitalGain\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7385,\n        \"min\": 0,\n        \"max\": 99999,\n        \"num_unique_values\": 119,\n        \"samples\": [\n          3781,\n          15831\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capitalLoss\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 402,\n        \"min\": 0,\n        \"max\": 4356,\n        \"num_unique_values\": 92,\n        \"samples\": [\n          419,\n          2051\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hoursPerWeek\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 12,\n        \"min\": 1,\n        \"max\": 99,\n        \"num_unique_values\": 94,\n        \"samples\": [\n          6,\n          22\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"nativeCountry\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 41,\n        \"samples\": [\n          \"El-Salvador\",\n          \"Italy\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"income\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \">50K\",\n          \"<=50K\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"adult_df"}
```

</div>

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:372,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592587255,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="h3N6nYx7GWCt" outputId="5e78f9a8-6e8b-453c-ce03-4082d0e41447">

``` python
adult_df.hoursPerWeek.plot.hist()
plt.show()
```

<div class="output display_data">

![](af0308ed92f7bc7fd5041db24ecb2ab4a7a3be96.png)

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:449}" executionInfo="{&quot;elapsed&quot;:1347,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592551018,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2WZKU6NTGMa3" outputId="59ddfb9b-ce8d-496d-b733-f6e2c557eaa7">

``` python
sns.boxplot(data=adult_df, y='sex', x='hoursPerWeek',hue='income')
plt.show()
```

<div class="output display_data">

![](dee975173f018b8116f06f4f654d4b2577a499a9.png)

</div>

</div>

<div class="cell markdown" id="gF_qLC25HbOx">

### **Ejercicio 4:**

Para mejorar el gráfico del ánalisis multivariado, discretize `hoursPerWeek` y vuelva a graficar en base a las tres variables. Considere 40 como su threshold.

</div>

<div class="cell code" execution_count="19" executionInfo="{&quot;elapsed&quot;:357,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592977510,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="HqEFs8lcH4fZ">

``` python
adult_df['discretized_hoursPerWeek']=adult_df.hoursPerWeek.apply(lambda v: '>40' if v>40 else ('40' if v==40 else '<40'))
```

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:876,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718592986782,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="J23etNZNH80c" outputId="9c447a44-e4cd-4f8a-cba3-72cf16bdd8a9">

``` python
adult_df.groupby(['sex','income']).discretized_hoursPerWeek.value_counts().unstack()[['<40','40', '>40']].plot.barh()
plt.show()
```

<div class="output display_data">

![](afd811cf733b0fe8facc78cc607f01ff5006b2fb.png)

</div>

</div>

<div class="cell markdown" id="vWRIB_v3sYtV">

### **Tipos de Discretización**

- Equal width (Igual ancho)
- Equal frequency (Igual Frequency)
- Ad hoc

Nota: En el ejemplo anterior hemos usado el tipo **ad hoc.**

</div>

<div class="cell markdown" id="krXkpCu35Uaq">

**Equal Width (Igual Ancho):**

Este enfoque se asegura que los puntos de corte conduzcan a ***intervalos iguales*** del atributo numérico.

Para este propósito usaremos la función de Pandas `cut()` que crea $`n`$ bins de igual ancho.

Para ilustrar este tipo, usaremos el atributo `age`.

</div>

<div class="cell markdown" id="Vl3conF_It4U">

### **Ejercicio 5:**

Discretiza el atributo `age`en 5 intervalos **iguales**.

</div>

<div class="cell code" execution_count="21" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:336,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593208068,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="e1NgQQRHIzSr" outputId="00754065-31d7-45d8-beb1-96cfe88fb1d1">

``` python
adult_df.age
```

<div class="output execute_result" execution_count="21">

    0        39
    1        50
    2        38
    3        53
    4        28
             ..
    32556    27
    32557    40
    32558    58
    32559    22
    32560    52
    Name: age, Length: 32561, dtype: int64

</div>

</div>

<div class="cell code" execution_count="22" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:439,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593218666,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="YVumvAkxI1d_" outputId="04049d7b-2bf3-4cff-e273-3fb7f350c984">

``` python
#Se mapea cada dato dentro de 5 bins del mismo ancho.
pd.cut(adult_df.age, bins = 5)
```

<div class="output execute_result" execution_count="22">

    0          (31.6, 46.2]
    1          (46.2, 60.8]
    2          (31.6, 46.2]
    3          (46.2, 60.8]
    4        (16.927, 31.6]
                  ...      
    32556    (16.927, 31.6]
    32557      (31.6, 46.2]
    32558      (46.2, 60.8]
    32559    (16.927, 31.6]
    32560      (46.2, 60.8]
    Name: age, Length: 32561, dtype: category
    Categories (5, interval[float64, right]): [(16.927, 31.6] < (31.6, 46.2] < (46.2, 60.8] <
                                               (60.8, 75.4] < (75.4, 90.0]]

</div>

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:468,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593229132,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="JTjvS3-GI4aS" outputId="7f17b368-744b-4b89-ebc9-2a2f7e529029">

``` python
#Contemos cuantos valores existen dentro cada bin
bins = pd.cut(adult_df.age, bins = 5).value_counts()
bins
```

<div class="output execute_result" execution_count="23">

    age
    (31.6, 46.2]      12211
    (16.927, 31.6]    11460
    (46.2, 60.8]       6558
    (60.8, 75.4]       2091
    (75.4, 90.0]        241
    Name: count, dtype: int64

</div>

</div>

<div class="cell code" execution_count="24" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:316,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593238792,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="WNXRvPc-I61v" outputId="413d40be-2188-4074-d07e-ab9fd18a7c33">

``` python
#Ordenamos los rangos de menor a mayor para mejor ilustración
bins = bins.sort_index()
bins
```

<div class="output execute_result" execution_count="24">

    age
    (16.927, 31.6]    11460
    (31.6, 46.2]      12211
    (46.2, 60.8]       6558
    (60.8, 75.4]       2091
    (75.4, 90.0]        241
    Name: count, dtype: int64

</div>

</div>

<div class="cell code" execution_count="25" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:535}" executionInfo="{&quot;elapsed&quot;:1132,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593255226,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="C_yCW_ZJI89r" outputId="a94bc087-f2b5-4035-e44e-c1a9a12a1ead">

``` python
#Graficar usando Bar Plot
bins.plot.bar()
plt.show()
```

<div class="output display_data">

![](31c28023aa1391e926b1f39720eb91527e14e50e.png)

</div>

</div>

<div class="cell markdown" id="7FCyHCIVAD7M">

**Equal Frequency (Igual Frecuencia):**

El enfoque de igual frecuencia tiene como objetivo tener ***un número igual*** de datos en cada bin.

Para este próposito usaremos la función `qcut()`.

</div>

<div class="cell markdown" id="DJRFA0JIJeEz">

### **Ejercicio 6:**

Discretiza el atributo `age`en 5 grupos (bins) de igual frecuencia.

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:404,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593435743,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RnmzX89zJqHj" outputId="744008ec-a775-48f3-d8d4-f682a3f2c7a6">

``` python
#Cada dato es mapeado equitativamente a un bin
pd.qcut(adult_df.age,q=5)
```

<div class="output execute_result" execution_count="26">

    0          (33.0, 41.0]
    1          (41.0, 50.0]
    2          (33.0, 41.0]
    3          (50.0, 90.0]
    4          (26.0, 33.0]
                  ...      
    32556      (26.0, 33.0]
    32557      (33.0, 41.0]
    32558      (50.0, 90.0]
    32559    (16.999, 26.0]
    32560      (50.0, 90.0]
    Name: age, Length: 32561, dtype: category
    Categories (5, interval[float64, right]): [(16.999, 26.0] < (26.0, 33.0] < (33.0, 41.0] <
                                               (41.0, 50.0] < (50.0, 90.0]]

</div>

</div>

<div class="cell code" execution_count="27" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:382,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593443229,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="gE0ELQmSJs3V" outputId="9c00c6c0-f1b8-438b-a7e4-8fb94b903188">

``` python
# Contamos cuantos datos hay por bin
bins = pd.qcut(adult_df.age,q=5,duplicates='drop').value_counts()
bins
```

<div class="output execute_result" execution_count="27">

    age
    (16.999, 26.0]    7196
    (33.0, 41.0]      6763
    (50.0, 90.0]      6460
    (41.0, 50.0]      6175
    (26.0, 33.0]      5967
    Name: count, dtype: int64

</div>

</div>

<div class="cell code" execution_count="28" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:356,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593451021,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="5IY2amVGJupY" outputId="1896e178-e4e0-402b-a616-8f044634a126">

``` python
#ordenamos los bins
bins = bins.sort_index()
bins
```

<div class="output execute_result" execution_count="28">

    age
    (16.999, 26.0]    7196
    (26.0, 33.0]      5967
    (33.0, 41.0]      6763
    (41.0, 50.0]      6175
    (50.0, 90.0]      6460
    Name: count, dtype: int64

</div>

</div>

<div class="cell code" execution_count="29" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:535}" executionInfo="{&quot;elapsed&quot;:535,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593466258,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4Epdu3xmJwtb" outputId="b0681b38-2e69-43c6-9a55-294fbcba84b6">

``` python
#Graficamos usando Bar Plot
bins.plot.bar()
plt.show()
```

<div class="output display_data">

![](8d164b53402edef5d1696269fd5684e1d64da402.png)

</div>

</div>

<div class="cell markdown" id="zFibx0oIYzVJ">

## **III. Construcción de Atributos (*Attribute Construction*)**

El uso de la construcción de atributos requiere tener una comprensión profunda del entorno del que se han recopilado los datos.

</div>

<div class="cell markdown" id="zMlg79LJJ78x">

### **Ejercicio 7:**

¿Sabes qué es el Índice de Masa Corporal (IMC)? El IMC es el resultado de la construcción de atributos por parte de investigadores y médicos, que buscaban un índice de salud que tuviera en cuenta tanto el peso como la altura de las personas.

Para este ejercicio utilizaremos el dataset 500_Person_Gender_Height_Weight_Index.csv y **categorizaremos** la columna `Index`

- 0: Extremely Weak
- 1: Weak
- 2: Normal
- 3: Overweight
- 4: Obesity
- 5: Extreme Obesity

Y renombre la columna `Index` como `Condition`.

</div>

<div class="cell code" execution_count="30" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:378,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593668661,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="N8Oq1YnYKdSA" outputId="527cb69f-5188-48b0-969d-5d63e4e83a41">

``` python
df = pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
df
```

<div class="output execute_result" execution_count="30">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 500,\n  \"fields\": [\n    {\n      \"column\": \"Gender\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Female\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Height\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 16,\n        \"min\": 140,\n        \"max\": 199,\n        \"num_unique_values\": 60,\n        \"samples\": [\n          174,\n          147\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Weight\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 32,\n        \"min\": 50,\n        \"max\": 160,\n        \"num_unique_values\": 110,\n        \"samples\": [\n          124,\n          80\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Index\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 0,\n        \"max\": 5,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          4,\n          2\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell code" execution_count="31" executionInfo="{&quot;elapsed&quot;:343,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593685311,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2FDMNhlMKnHT">

``` python
df.Index = df.Index.replace({0:'Extremely Weak', 1: 'Weak',2: 'Normal',3:'Overweight', 4:'Obesity',5:'Extreme Obesity'})
```

</div>

<div class="cell code" execution_count="32" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:471,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593691585,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="eCosyNGpKobi" outputId="e8879101-0864-429c-da95-1ba36745595d">

``` python
df.columns = ['Gender', 'Height', 'Weight', 'Condition']
df
```

<div class="output execute_result" execution_count="32">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 500,\n  \"fields\": [\n    {\n      \"column\": \"Gender\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Female\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Height\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 16,\n        \"min\": 140,\n        \"max\": 199,\n        \"num_unique_values\": 60,\n        \"samples\": [\n          174,\n          147\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Weight\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 32,\n        \"min\": 50,\n        \"max\": 160,\n        \"num_unique_values\": 110,\n        \"samples\": [\n          124,\n          80\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Condition\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Obesity\",\n          \"Normal\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell markdown" id="l8L5aFlpKyej">

### **Ejercicio 8:**

Analiza visualmente la relación entre todas las variables del dataset.

</div>

<div class="cell code" execution_count="33" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:449}" executionInfo="{&quot;elapsed&quot;:2482,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593775271,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="kUldS3i2K6Dt" outputId="09f4476c-f89c-4054-bb08-f633742a76bc">

``` python
sns.scatterplot(data = df, x='Height',y='Weight', hue='Condition',style='Gender')
plt.legend(bbox_to_anchor=(1.05, 1))
plt.show()
```

<div class="output display_data">

![](30fe8a77935ff973e3a7ff7d4318bac301a1d34a.png)

</div>

</div>

<div class="cell markdown" id="70bCNcUQK_DS">

### **Ejercicio 9:**

Nuestra observación del gráfico anterior es obvia. Los dos atributos `Height` y `Weight` juntos pueden determinar la salud de una persona. Esto es lo que los investigadores y los médicos deben haber visto antes de llegar a la fórmula del IMC. El IMC es una función que tiene en cuenta tanto el peso como la altura para crear un índice de salud. La fórmula es la siguiente:

``` math
 IMC = \frac{Weight(kg)}{Height(m)^2}
```

Construye una nueva columna `IMC` dentro del dataset

</div>

<div class="cell code" execution_count="34" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:332,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593826550,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Az8uCI1NLHKA" outputId="e7e3a5db-adfe-461c-dd61-e8e2d660fe47">

``` python
df['IMC'] = df.apply(lambda r:r.Weight/((r.Height/100)**2),axis=1)
df
```

<div class="output execute_result" execution_count="34">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 500,\n  \"fields\": [\n    {\n      \"column\": \"Gender\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Female\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Height\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 16,\n        \"min\": 140,\n        \"max\": 199,\n        \"num_unique_values\": 60,\n        \"samples\": [\n          174,\n          147\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Weight\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 32,\n        \"min\": 50,\n        \"max\": 160,\n        \"num_unique_values\": 110,\n        \"samples\": [\n          124,\n          80\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Condition\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Obesity\",\n          \"Normal\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"IMC\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 13.965620181356998,\n        \"min\": 12.753800632588511,\n        \"max\": 78.85340210275739,\n        \"num_unique_values\": 476,\n        \"samples\": [\n          21.936347412254616,\n          62.07148363016755\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell markdown" id="IDGNExGhLL_Z">

### **Ejercicio 10:**

Analice visualmente la variación del atributo IMC. ¿Qué herramienta visual es la mejor?

</div>

<div class="cell code" execution_count="35" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:449}" executionInfo="{&quot;elapsed&quot;:460,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593881092,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Yqny0cwVLU7i" outputId="2ee70e3f-ae81-4a50-b260-e7c0b7bf2200">

``` python
sns.histplot(data=df, x= 'IMC')
plt.show()
```

<div class="output display_data">

![](d9572f777cffee99fcdff7d1ee8d711f145467d6.png)

</div>

</div>

<div class="cell code" execution_count="36" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:449}" executionInfo="{&quot;elapsed&quot;:5,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1718593898294,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="j6ydOoKHLZnX" outputId="2d053304-157d-4b52-c91a-8e1c44caae70">

``` python
sns.boxplot(data=df, x= 'IMC')
plt.show()
```

<div class="output display_data">

![](227976779979afa2444a35e0e8a979bd9e55ebab.png)

</div>

</div>
