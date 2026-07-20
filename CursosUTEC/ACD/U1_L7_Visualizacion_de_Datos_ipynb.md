---
curso: ACD
titulo: U1_L7 Visualización de Datos
slides: 0
fuente: U1_L7 Visualización de Datos.ipynb
---

<div class="cell markdown" id="zmTInPX6trYu">

# **Laboratorio 6: Visualización de Datos**

Ser capaz de visualizar datos es **la columna vertebral** del análisis de datos. El área de la visualización de datos es muy interesante, ya que existen infinitas posibilidades de novedad y creatividad al dibujar visualizaciones que cuenten mejores historias sobre sus datos.

El objetivo de este laboratorio ***es cubrir mecanismos visuales que dan vida a los datos*** y nos permiten compararlos, analizarlos y ver patrones entre ellos. <br>

\###**¿Por qué aprender herramientas de visualización?**

Porque serás más eficaz en el preprocesamiento de los datos para obtener imágenes efectivas.

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:748,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713276872494,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="fV6m2gtZ0seF">

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

</div>

<div class="cell markdown" id="E9zCuhpwGayc">

Cargemos y entendamos la data que usaremos para este laboratorio

</div>

<div class="cell code" execution_count="2" executionInfo="{&quot;elapsed&quot;:304,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713276892313,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="LoIvxTpF71Xx">

``` python
#Cargar el dataset
df = pd.read_csv('adult.csv')
```

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:330}" executionInfo="{&quot;elapsed&quot;:804,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713276904529,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="FqoAf8iMQs58" outputId="a0840b15-fd82-4231-c9be-2984a2ed640a">

``` python
df.head()
```

<div class="output execute_result" execution_count="3">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 32561,\n  \"fields\": [\n    {\n      \"column\": \"age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 13,\n        \"min\": 17,\n        \"max\": 90,\n        \"num_unique_values\": 73,\n        \"samples\": [\n          28,\n          73,\n          35\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"workclass\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 8,\n        \"samples\": [\n          \"Self-emp-not-inc\",\n          \"Self-emp-inc\",\n          \"State-gov\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"fnlwgt\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 105549,\n        \"min\": 12285,\n        \"max\": 1484705,\n        \"num_unique_values\": 21648,\n        \"samples\": [\n          128485,\n          469907,\n          235951\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 16,\n        \"samples\": [\n          \"Bachelors\",\n          \"HS-grad\",\n          \"Some-college\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education-num\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2,\n        \"min\": 1,\n        \"max\": 16,\n        \"num_unique_values\": 16,\n        \"samples\": [\n          13,\n          9,\n          10\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"marital-status\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Never-married\",\n          \"Married-civ-spouse\",\n          \"Married-AF-spouse\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"occupation\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 14,\n        \"samples\": [\n          \"Machine-op-inspct\",\n          \"Protective-serv\",\n          \"Adm-clerical\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"relationship\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Not-in-family\",\n          \"Husband\",\n          \"Other-relative\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"race\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"Black\",\n          \"Other\",\n          \"Asian-Pac-Islander\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"sex\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Female\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capitalGain\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7385,\n        \"min\": 0,\n        \"max\": 99999,\n        \"num_unique_values\": 119,\n        \"samples\": [\n          3781,\n          15831\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capitalLoss\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 402,\n        \"min\": 0,\n        \"max\": 4356,\n        \"num_unique_values\": 92,\n        \"samples\": [\n          419,\n          2051\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hoursPerWeek\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 12,\n        \"min\": 1,\n        \"max\": 99,\n        \"num_unique_values\": 94,\n        \"samples\": [\n          6,\n          22\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"nativeCountry\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 41,\n        \"samples\": [\n          \"El-Salvador\",\n          \"Italy\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"income\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \">50K\",\n          \"<=50K\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:308,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713276978163,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="s3P78s-i75Hu" outputId="a2387b9a-2dbc-4598-bfdf-ab86c92ca159">

``` python
df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 32561 entries, 0 to 32560
    Data columns (total 15 columns):
     #   Column          Non-Null Count  Dtype 
    ---  ------          --------------  ----- 
     0   age             32561 non-null  int64 
     1   workclass       30725 non-null  object
     2   fnlwgt          32561 non-null  int64 
     3   education       32561 non-null  object
     4   education-num   32561 non-null  int64 
     5   marital-status  32561 non-null  object
     6   occupation      30718 non-null  object
     7   relationship    32561 non-null  object
     8   race            32561 non-null  object
     9   sex             32561 non-null  object
     10  capitalGain     32561 non-null  int64 
     11  capitalLoss     32561 non-null  int64 
     12  hoursPerWeek    32561 non-null  int64 
     13  nativeCountry   31978 non-null  object
     14  income          32561 non-null  object
    dtypes: int64(6), object(9)
    memory usage: 3.7+ MB

</div>

</div>

<div class="cell markdown" id="J-WL3ijexPxW">

## **I. Comprender la población**

Para visualizar las variaciones en los valores de un dataset se puede utilizar:

- Histograma
- Boxplot
- Bar Chart

</div>

<div class="cell markdown" id="MMpB76CL3e3y">

### **Ejemplo para Atributos Numéricos**

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:2549,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713277129292,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="K1vYu2LFtn0B" outputId="e2e87e4f-bfc5-4e26-b44f-de8d96aa0fb2">

``` python
numerical_attributes = ['age', 'fnlwgt', 'education-num', 'capitalGain', 'capitalLoss',
       'hoursPerWeek']

for att in numerical_attributes:
    plt.subplot(2,1,1)
    df[att].plot.hist()
    plt.subplot(2,1,2)
    df[att].plot.box(vert=False)
    plt.tight_layout()
    plt.show()
```

<div class="output display_data">

![](8bad28d1e9ec9765ab4b027ca39439983fc8b0ca.png)

</div>

<div class="output display_data">

![](028915dd3b0eb715e7012ab1890fd715b95962f2.png)

</div>

<div class="output display_data">

![](fd15f0d0cea8ad2cf09a50af3425b5c783dcc0a7.png)

</div>

<div class="output display_data">

![](da8e0ffbf0f314be9bf8ff316e232d9364d6ff36.png)

</div>

<div class="output display_data">

![](305f97d326bdc50fb6f81b9dd3e55ed5569ced48.png)

</div>

<div class="output display_data">

![](ed6c45d0d9216314013dcf2db8808b623477957f.png)

</div>

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713277849038,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="No-ursT8SabF" outputId="c4e77a81-630f-4d32-ffd1-441a2190fd24">

``` python
set(zip(df.education,df["education-num"]))
```

<div class="output execute_result" execution_count="9">

    {('10th', 6),
     ('11th', 7),
     ('12th', 8),
     ('1st-4th', 2),
     ('5th-6th', 3),
     ('7th-8th', 4),
     ('9th', 5),
     ('Assoc-acdm', 12),
     ('Assoc-voc', 11),
     ('Bachelors', 13),
     ('Doctorate', 16),
     ('HS-grad', 9),
     ('Masters', 14),
     ('Preschool', 1),
     ('Prof-school', 15),
     ('Some-college', 10)}

</div>

</div>

<div class="cell markdown" id="Vlz5AQds4NM7">

### **Ejemplo para Atributos Categóricos**

</div>

<div class="cell markdown" id="VhjhMcxF4R1p">

Crea diagrama de barras para los atributos categóricos.

Hint: Empecemos con un sólo atributo

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:306,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713278203804,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Vz2q9dYh9IGE" outputId="fb94aac4-70d8-4006-ccc9-f69e8a32a3f4">

``` python
df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 32561 entries, 0 to 32560
    Data columns (total 15 columns):
     #   Column          Non-Null Count  Dtype 
    ---  ------          --------------  ----- 
     0   age             32561 non-null  int64 
     1   workclass       30725 non-null  object
     2   fnlwgt          32561 non-null  int64 
     3   education       32561 non-null  object
     4   education-num   32561 non-null  int64 
     5   marital-status  32561 non-null  object
     6   occupation      30718 non-null  object
     7   relationship    32561 non-null  object
     8   race            32561 non-null  object
     9   sex             32561 non-null  object
     10  capitalGain     32561 non-null  int64 
     11  capitalLoss     32561 non-null  int64 
     12  hoursPerWeek    32561 non-null  int64 
     13  nativeCountry   31978 non-null  object
     14  income          32561 non-null  object
    dtypes: int64(6), object(9)
    memory usage: 3.7+ MB

</div>

</div>

<div class="cell code" execution_count="11" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:4543,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713278217983,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pRpNrnZv4XZx" outputId="600140e9-a625-41b9-8079-81b9960223d1">

``` python
#TO DO
categorical_attributes = ['workclass', 'education', 'marital-status',
                          'occupation', 'relationship', 'race',
                         'sex','nativeCountry','income']

for att in categorical_attributes:
    df[att].value_counts().plot.barh()
    plt.title(att)
    plt.tight_layout()
    plt.show()
```

<div class="output display_data">

![](515a8afc403546b530d3038b8903f4bbb3223545.png)

</div>

<div class="output display_data">

![](3433ba10e81c431e95f2889a5b65d9481b711022.png)

</div>

<div class="output display_data">

![](9e3547d05bc18007c85386a6943c6f6505311736.png)

</div>

<div class="output display_data">

![](6a29ecca9ae38f6bee0c2affdfe7a8f90fed9916.png)

</div>

<div class="output display_data">

![](58f3fc00065fc09801be45041d1861fe31398aa8.png)

</div>

<div class="output display_data">

![](3a8c06b3fe6560d8ad0ab108e9d0ea60f26176b5.png)

</div>

<div class="output display_data">

![](9f5e08c44bd246df84442272dd5de20d19643485.png)

</div>

<div class="output display_data">

![](7bfe68c51e37ecdd0a6e6fd242d90673454f714e.png)

</div>

<div class="output display_data">

![](9adc428c4a2f581b28a93a8dd397a6bbdfb80f23.png)

</div>

</div>

<div class="cell markdown" id="bKKgOsiH-kSl">

## **II. Comparación de poblaciones**

Para la compatación de poblaciones es útil usar diferentes herramientas de visualizaciones donde cada una resume o sintetiza las características esenciales del dataset.

</div>

<div class="cell markdown" id="ktfHg7k6C9N9">

### **Ejemplo de Comparación usando Boxplots**

</div>

<div class="cell markdown" id="FdyrLUjPIk-p">

Recordemos que necesitamos para construir un boxplot:

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:330}" executionInfo="{&quot;elapsed&quot;:297,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713278577788,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="OoDpPPH5JiXy" outputId="53abe25d-8a5b-45da-b4e2-baff490d5b2c">

``` python
df.head()
```

<div class="output execute_result" execution_count="12">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 32561,\n  \"fields\": [\n    {\n      \"column\": \"age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 13,\n        \"min\": 17,\n        \"max\": 90,\n        \"num_unique_values\": 73,\n        \"samples\": [\n          28,\n          73,\n          35\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"workclass\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 8,\n        \"samples\": [\n          \"Self-emp-not-inc\",\n          \"Self-emp-inc\",\n          \"State-gov\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"fnlwgt\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 105549,\n        \"min\": 12285,\n        \"max\": 1484705,\n        \"num_unique_values\": 21648,\n        \"samples\": [\n          128485,\n          469907,\n          235951\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 16,\n        \"samples\": [\n          \"Bachelors\",\n          \"HS-grad\",\n          \"Some-college\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education-num\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2,\n        \"min\": 1,\n        \"max\": 16,\n        \"num_unique_values\": 16,\n        \"samples\": [\n          13,\n          9,\n          10\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"marital-status\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Never-married\",\n          \"Married-civ-spouse\",\n          \"Married-AF-spouse\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"occupation\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 14,\n        \"samples\": [\n          \"Machine-op-inspct\",\n          \"Protective-serv\",\n          \"Adm-clerical\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"relationship\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Not-in-family\",\n          \"Husband\",\n          \"Other-relative\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"race\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"Black\",\n          \"Other\",\n          \"Asian-Pac-Islander\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"sex\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Female\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capitalGain\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7385,\n        \"min\": 0,\n        \"max\": 99999,\n        \"num_unique_values\": 119,\n        \"samples\": [\n          3781,\n          15831\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capitalLoss\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 402,\n        \"min\": 0,\n        \"max\": 4356,\n        \"num_unique_values\": 92,\n        \"samples\": [\n          419,\n          2051\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hoursPerWeek\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 12,\n        \"min\": 1,\n        \"max\": 99,\n        \"num_unique_values\": 94,\n        \"samples\": [\n          6,\n          22\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"nativeCountry\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 41,\n        \"samples\": [\n          \"El-Salvador\",\n          \"Italy\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"income\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \">50K\",\n          \"<=50K\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:300,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713278586784,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="fCtpOU47Im-_" outputId="3270983f-9e5d-4583-b3a8-f8a552b6966e">

``` python
plt.boxplot(df["education-num"], vert=False)
plt.show()
```

<div class="output display_data">

![](14d9bd330f377f57fecb3dc8ee367d55ee655d48.png)

</div>

</div>

<div class="cell markdown" id="5TiflNdTIiZG">

**TO DO:** Necesitamos comparar los atributos de educación en base a sus ingresos. Tal como la imagen:

</div>

<div class="cell markdown" id="3b-ZX2csEl_V">

![ComparaciónBoxplot.png](data:image/png;base64,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SFsu5dLtbXf//Z7mwOwy3c7s7JnnvGc/J9nur/ObOed5P+8zs/M8854zOw7esnU2AgQIECBAgAABAgQIECBAgACBZgR2aOg0M1cCJUCAAAECBAgQIECAAAECBAj0Aho6EoEAAQIECBAgQIAAAQIECBAg0JiAhk5jEyZcAgQIECBAgAABAgQIECBAgICGjhwgQIAAAQIECBAgQIAAAQIECDQmoKHT2IQJlwABAgQIECBAgAABAgQIECCgoSMHCBAgQIAAAQIECBAgQIAAAQKNCWjoNDZhwiVAgAABAgQIECBAgAABAgQIaOjIAQIECBAgQIAAAQIECBAgQIBAYwIaOo1NmHAJECBAgAABAgQIECBAgAABAho6coAAAQIECBAgQIAAAQIECBAg0JiAhk5jEyZcAgQIECBAgAABAgQIECBAgICGjhwgQIAAAQIECBAgQIAAAQIECDQmoKHT2IQJlwABAgQIECBAgAABAgQIECCgoSMHCBAgQIAAAQIECBAgQIAAAQKNCWjoNDZhwiVAgAABAgQIECBAgAABAgQIaOjIAQIECBAgQIAAAQIECBAgQIBAYwIaOo1NmHAJECBAgAABAgQIECBAgAABAho6coAAAQIECBAgQIAAAQIECBAg0JiAhk5jEyZcAgQIECBAgAABAgQIECBAgICGjhwgQIAAAQIECBAgQIAAAQIECDQmoKHT2IQJlwABAgQIECBAgAABAgQIECCgoSMHCBAgQIAAAQIECBAgQIAAAQKNCWjoNDZhwiVAgAABAgQIECBAgAABAgQIaOjIAQIECBAgQIAAAQIECBAgQIBAYwIaOo1NmHAJECBAgAABAgQIECBAgAABAho6M86BAwcOdPv37+8OHjzY7dixo/8z4+EaGgECBAgQIECAAAECBAgQKBFI3T3U3rt27ep27tw5ehwaOqMT1xwgiXTTTTd11113Xd/U2bNnT5ekshEgQIAAAQIECBAgQIAAAQLHViCLKVKDp+4+6aSTutTgWVgx5qahM6Zu0b6zMufmm2/urrrqqu5DH/pQ98UvfrFPpnQIx06ooiE7LAECBAgQIECAAAECBAgQKBHIgorU4Wno3OUud+nue9/7dne/+9273bt3j7pSR0OnZLrHPWiS6Ktf/Wr3vve9r3vNa17TfeADH3DK1bjk9k6AAAECBAgQIECAAAECx7HAcMrV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O876yW7nt35/t+OOp3XdnpNmhfGVr3yl++xnP9tdeuml3Ste8Ypu586d3YUXXtidd955fT6ffPLJsxqvwRCYkkBl/a2hM6VMOEaxVCbUMRqC3RAgQIAAAQIERhX40pe+1H3qU5/qGzove9kxU6GlAAAb7UlEQVTLuhtuuKH72Z/92e6cc87R0BlVfjs733Hzvm7nvs91u6++otv735f0B933ned1N592Zndg7926g7v3bieQLR3luuuu66666qruPe95T/fa1762O/HEEzV0tmTvMAQq628NnRnmX2VCzZDTkAgQIECAAIEZCnz+85/vPvrRj3aXXHJJ96pXvar7whe+0D3kIQ/pzjjjjO6ud71rd9JJ81rBMcMpPOKQdh+4sTvxwJe7U2/6TPdd13+4v+9H73Cf7po9p3c37Dy5u3nnCUd8fGu/vP7667trr722u/LKK/tVOqeddlp30UUXdeeff353j3vcw4qz1iZUvE0JVNbfGjpNpcpqwVYm1GoRuhcBAgQIECBAoFYgp6dcdtllfUPnjW98Y/eJT3yiu9vd7tbl1JQTTjih27VrV22Ajr6RwN7dB7u7nnig+77TdnSP+I5b5/KtH9vf/cfVB7vP37Cz23fzjo32P7UHHzhwoLvpppu6nEp49dVXd2eddVb3tKc9rW/onHrqqRqUU5sw8cxKoLL+1tCZVSrdOpjKhJohpyERIECAAAECMxS45pprug9+8IP9KSp/93d/13384x/v9uzZ0zdycv0RW9sCe/fs6L5p747uAfe8Q3fBGaf0g3nbldd2l/3f9d0X9h3s9t10sO0B3kb0O3bs6K+fk4bOYx/72O7ss8/u7nznO/enYN3GQ9xMgMCGApX1t4bOhpM3xYdXJtQUPcREgAABAgQIEDhcINccSVMnp129//3v70+5OuWUU7q9e/d2u3fv7oviwx/j/9sR2LXjYLdnx/7uLifs775578194J/et7v74o27upsO7ur2H5zXCp1hZtKMTGMyp1mdeeaZ/d/5f03KQcjfBI69QGX9raFz7OezfI+VCVU+eAEQIECAAAECBFYQGN4vfe5zn+s++clPdrkGSRo6uXZOGjpZ6WBrWeCWFTgH9nc79t/Q7bz5un4gB3af1B3cdWLX7cwpWPOc35wqmAZOGpNW5rScv2JvSWD49yTXZHvuc5/bh/6c5zyn/5a5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raHTdOosD74yoZZH5FYCBAgQIECAAAECBAgQIDA/gcr6W0NnfvnUVSbUDDkNiQABAgQIECBAgAABAgQILBWorL81dJZOSds3ViZU23KiJ0CAAAECBAgQIECAAAECqwtU1t8aOqvPUzP3rEyoZpAESoAAAQIECBAgQIAAAQIENhSorL81dDacvCk+vDKhpughJgIECBAgQIAAAQIECBAgMIZAZf2toTPGjBbvszKhiofu8AQIECBAgAABAgQIECBAYGsClfW3hs7Wpnl7B6pMqO2N0pEIECBAgAABAgQIECBAgECtQGX9raFTO/ejHL0yoUYZkJ0SIECAAAECBAgQIECAAIEJClTW3xo6E0yITUOqTKhNY/d4AgQIECBAgAABAgQIECDQikBl/a2h00qWrBFnZUKtEaa7EiBAgAABAgQIECBAgACBpgUq628NnaZTZ3nwlQm1PCK3EiBAgAABAgQIECBAgACB+QlU1t8aOvPLp64yoWbIaUgECBAgQIAAAQIECBAgQGCpQGX9raGzdEravrEyodqWEz0BAgQIECBAgAABAgQIEFhdoLL+1tBZfZ6auWdlQjWDJFACBAgQIECAAAECBAgQILChQGX9raGz4eRN8eGVCTVFDzERIECAAAECBAgQIECAAIExBCrrbw2dMWa0eJ+VCVU8dIcnQIAAAQIECBAgQIAAAQJbE6isvzV0tjbN2ztQZUJtb5SORIAAAQIECBAgQIAAAQIEagUq628Nndq5H+XolQk1yoDslAABAgQIECBAgAABAgQITFCgsv7W0JlgQmwaUmVCbRq7xxMgQIAAAQIECBAgQIAAgVYEKutvDZ1WsmSNOCsTao0w3ZUAAQIECBAgQIAAAQIECDQtUFl/a+g0nTrLg69MqOURuZUAAQIECBAgQIAAAQIECMxPoLL+1tCZXz51lQk1Q05DIkCAAAECBAgQIECAAAECSwUq628NnaVT0vaNlQnVtpzoCRAgQIAAAQIECBAgQIDA6gKV9beGzurz1Mw9KxOqGSSBEiBAgAABAgQIECBAgACBDQUq628NnQ0nb4oPr0yoKXqIiQABAgQIECBAgAABAgQIjCFQWX9r6Iwxo8X7rEyo4qE7PAECBAgQIECAAAECBAgQ2JpAZf2tobO1ad7egSoTanujdCQCBAgQIECAAAECBAgQIFArUFl/a+jUzv0o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Nm3alJYsWZK23nrrtHz58rTjjjum+93vfmn77bdPy5YtS0uXLq29bGcQL1Danxi45ZZbcrvvtNNOaeXKlen+979/2m677eILaQnmFWB93bhxY7rjjjtyO956663pzjvvzOvy5s2b87rMervDDjukXXbZJa/PrNdbbbXVvPP2A7ECtB/r6apVqxLtWrbTtDcTbbjtttvmtmU7zbrL/53iBe66667cdrRZabv169fn9ZL2Y/u622675TZbsWJF3rdWlZr2Z/vMPNasWZP306zztH3ZPz/gAQ/IMeD+uUqwmffqtC/rNdto1mvalN85/mKeZZu9zTbb5HW5HH8RI7S5x1/NtOdsc63TzrPNk/fZX9900035GJwYoF057mIbznEY67ZT8wLTal+26fSf2N6zvS7bat5jon1Zp1mf2e5zPEYfa8jrswmd5uPXJSiQBa677rp0wQUXpF/84hfpN7/5TeL/dO456GRDwwaHDc8jH/nIdOihh6aHPvShaeedd3ZHM5D4Ke1/3nnnpXPOOScfTO63337p4IMPTk984hPTgx70oIHUdNjV4ICBg0PWYdrxkksuSb/73e9yZ4GDDNZlDhBZj5/61KemfffdN9EBpIPg1F0BOnb8XHvttelnP/tZ+vnPf55+9atfpeuvvz53AEm6kxTYfffd0yMe8YjEuvvYxz42/5+/OcUKcKKEbeyvf/3rdOGFF6Yrrrgid+BIzLC+7rXXXukZz3hG3t7uvffeed86s8Sj7c88fvnLX+b2Zx9N4o7986Mf/ej0lKc8JT384Q+3IzgTsMH/L7R9aVMScldffXX66U9/mi699NK8vb7hhhvyyTU6mHT8ONZ64AMfmB71qEfl4y9iZK7EX4NVXdSzXmg7z4d21VVXpR/84AeJ4y9igPX5CU94Qt4ePOYxj0m77rrrfLPw71MQmFb7lhOk7KM5DmNbzb6bxA7rPAk6knUcf7HdZ73mJDnr+lAnEzpDbVnr1TkBNjxf//rX88EmZwo40ORMEZ1AzgTREeSMHwcVBx10UNp///1zp4GDSDoMdho616RjFYj25WzgZZddlr7xjW/kgwoOLJkOOeSQdPjhh6fnPe95uZM41gz9UIhA6Riw7tKWJHIuuuiixIEi6zIHGHyG9ZiOP53+I488Mh1wwAFpjz32yAnbkIK70LEEysgMDva/853v5MQ7Cfey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)

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:210,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693515675156,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_CxyE3rjDk7P" outputId="02f9bb0d-a944-49ec-f288-f39ccb9560d8">

``` python
#Asegurarnos de tener la lista de Ingresos (no repetidos)
income_list = df.income.unique()
income_list
```

<div class="output execute_result" execution_count="31">

    array(['<=50K', '>50K'], dtype=object)

</div>

</div>

<div class="cell code" id="kHnqcnmlD1vD">

``` python
#Cree un dictionary vacío donde sus indíces sean los posibles ingresos
#y su contenido sea los datos que corresponden al ingreso
dataForBox_dic= {}
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:240,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693515680088,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="tnO31P15Ft4O" outputId="833f324a-5da3-4981-8a94-d956ba73e0e3">

``` python
#Usemos un Boolean Mask para extraer los datos específicos
df.income == "<=50K"
```

<div class="output execute_result" execution_count="33">

    0         True
    1         True
    2         True
    3         True
    4         True
             ...  
    32556     True
    32557    False
    32558     True
    32559     True
    32560    False
    Name: income, Length: 32561, dtype: bool

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:226,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693515681435,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2FWF6UVCF4JR" outputId="6ce3f0d5-c5e4-4062-f63d-0e6053cc230f">

``` python
BM = df.income == "<=50K"
BM
```

<div class="output execute_result" execution_count="34">

    0         True
    1         True
    2         True
    3         True
    4         True
             ...  
    32556     True
    32557    False
    32558     True
    32559     True
    32560    False
    Name: income, Length: 32561, dtype: bool

</div>

</div>

<div class="cell code" id="9O3dq-QZD_8b">

``` python
# Filtrar por cada ingreso y agregarlo al dict
for poss in income_list:
    BM = df.income == poss
    dataForBox_dic[poss] = df[BM]['education-num']
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:250,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693515685561,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="t2HsuYVx-jqU" outputId="dafd3273-0ab7-47a0-8800-fd8d90b10430">

``` python
#Dibujar el boxplot en base a box_sr
#Analiza que nos dice el gráfico
plt.boxplot(dataForBox_dic.values(),vert=False)
plt.yticks([1,2],income_list)
plt.show()
```

<div class="output display_data">

![](744be4f84bda981be4deff5d20eb9ae77fb2c3a1.png)

</div>

</div>

<div class="cell markdown" id="2mvFbPHkK7fR">

### **Ejemplo de Comparación usando Histogramas**

</div>

<div class="cell markdown" id="D0k7sMt4LBrT">

**TO DO:** Realicemos el mismo análisis que en el ejercicio anterior pero esta vez usemos Histogramas.

Hint: usemos como tipo de histograma a `histtype='step'`

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:272,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693515834699,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="lzT2zoyJZy5r" outputId="6eb66eb9-bad4-4d65-e992-ac09f5dd6eed">

``` python
#Para cada ingreso dibujar un histograma
for poss in income_list:
    BM = df.income == poss
    plt.hist(df[BM]['education-num'],
             histtype='step',label=poss)
plt.legend()
plt.show()
```

<div class="output display_data">

![](7d2a73ca2b5ccc9ca2e23e5e0ad920b01f5dcced.png)

</div>

</div>

<div class="cell markdown" id="GRDbzpoyaSJm">

**TO DO:** Une en una sola figura el análisis de educación e ingresos usando Histogramas y Boxplots

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:477}" executionInfo="{&quot;elapsed&quot;:505,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693515934983,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="VDB3fFxXafy2" outputId="6dc81127-1418-4af4-b53b-2bc90d54c11c">

``` python
income_list = df.income.unique()

dataForBox_dic= {}

for poss in income_list:
    BM = df.income == poss
    dataForBox_dic[poss] = df[BM]['education-num']

plt.subplot(2,1,1)
plt.boxplot(dataForBox_dic.values(),vert=False)
plt.yticks([1,2],income_list)
plt.show()

plt.subplot(2,1,2)

for poss in income_list:
    BM = df.income == poss
    plt.hist(df[BM]['education-num'],
             histtype='step',label=poss)
plt.legend()
plt.tight_layout()
plt.show()
```

<div class="output display_data">

![](d36d5766dccfef688bd8eecb2cbcb72c7bbc2a29.png)

</div>

<div class="output display_data">

![](2abac50b0605fb82fd4f8466d62792b4462754af.png)

</div>

</div>

<div class="cell markdown" id="9YFrDiXGb4xN">

### **Ejemplo de Comparación usando Diagramas de Barras**

</div>

<div class="cell markdown" id="zGJvD5BWb-Uq">

**TO DO:** Crea una visualización que usa diagrama de barras para comparar el atributo categórico raza en base a sus ingresos.

</div>

<div class="cell markdown" id="r10mpxoFcouO">

**Primera manera:** Colocar un histograma después del otro

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:524,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693516446230,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="J5D5KgixceRN" outputId="9d3e4e57-bbf5-4d31-e3e2-7488a5631f19">

``` python
income_list = df.income.unique()

for i,poss in enumerate(income_list):
    plt.subplot(2,1,i+1)
    BM = df.income == poss
    df[BM].race.value_counts().plot.barh()
    plt.xlim([0,22000])
    plt.ylabel(poss)
```

<div class="output display_data">

![](da891aaf8d8adb2693d3b2c4920130e1e046962d.png)

</div>

</div>

<div class="cell markdown" id="NtFsTWclcsiY">

**Segunda manera:** Mezclar ambos histogramas en uno solo. Note los labels de `income,race`

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:647,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693516499862,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="YSKAIrqGct8D" outputId="e576e229-b73d-4a12-e6e9-4f0b1b6053b3">

``` python
df.groupby(['income','race']).size().plot.barh()
plt.show()
```

<div class="output display_data">

![](ec5e2cf0760dd3dc8b99f3a005b44bb02cc5cd13.png)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:1485,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693516562995,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Xf03hcdOc_I-" outputId="464cb1e1-d76b-4de6-9199-731623d65509">

``` python
df.groupby(['race','income']).size().plot.barh()
plt.show()
```

<div class="output display_data">

![](300a5a5672cb0f751005fd8e042ad59d628dbc7b.png)

</div>

</div>

<div class="cell markdown" id="b5FGHRC9cxz5">

**Tercera manera:** Mezcla de dos histogramas usando leyendas con el uso de diferentes colores.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:917,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693516548077,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="QW3EtpXIc44t" outputId="78cdbf21-e597-40d4-b36a-08548f9e9d21">

``` python
df.groupby(['income','race']).size().unstack().plot.barh()
plt.show()
```

<div class="output display_data">

![](2d6b62ceadae31e2b2cfe99a3f84883b8bef0006.png)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:515,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693516578594,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="csxqCi3PdA0k" outputId="b2efdbcd-ca43-409d-9b00-520bf40815a3">

``` python
df.groupby(['race','income']).size().unstack().plot.barh()
plt.legend(loc=4)
plt.show()
```

<div class="output display_data">

![](4cb8fac9835df4c803b879fee5b519eea112f8bf.png)

</div>

</div>

<div class="cell markdown" id="-uOA_XL4c1-C">

**Cuarta manera:** Usaremos un **stacked bar chart**

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:567,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693516621021,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KRrsdOLfdEol" outputId="ec03b01a-6144-4a79-9af2-429f56e414bc">

``` python
df.groupby(['race','income']).size().unstack().plot.barh(stacked=True)
plt.legend(loc=4)
plt.show()
```

<div class="output display_data">

![](b37ad6b8360cca9a69a2aff979258f5cf0a5c84c.png)

</div>

</div>

<div class="cell markdown" id="i3irjlcAgbPD">

## **III. Investigar la relación entre dos atributos**

Las herramientas que usamos para investigar la realción entre dos atributos depende siempre del tipo de atributos. Pueden ser:

- numérico-numérico
- categórico-categórico
- categórico-numérico

</div>

<div class="cell markdown" id="cu9yaE18g6r8">

### **Visualización para dos atributos numéricos**

Para esta sección, utilizaremos otro dataset

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:487}" executionInfo="{&quot;elapsed&quot;:455,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693518006511,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="GMlIpvN5hgAJ" outputId="97d3cd7b-11ab-4ec1-fa11-32d6b8ce8303">

``` python
uni_df = pd.read_csv('Universities_imputed_reduced.csv')
uni_df.head()
```

<div class="output execute_result" execution_count="46">

                            College Name State Public/Private  num_appli_rec  \
    0          Alaska Pacific University    AK        Private            193   
    1  University of Alaska at Fairbanks    AK         Public           1852   
    2     University of Alaska Southeast    AK         Public            146   
    3  University of Alaska at Anchorage    AK         Public           2065   
    4        Alabama Agri. & Mech. Univ.    AL         Public           2817   

       num_appl_accepted  num_new_stud_enrolled  in-state tuition  \
    0                146                     55              7560   
    1               1427                    928              1742   
    2                117                     89              1742   
    3               1598                   1162              1742   
    4               1920                    984              1700   

       out-of-state tuition  % fac. w/PHD  stud./fac. ratio  Graduation rate  
    0                  7560            76              11.9               15  
    1                  5226            67              10.0               60  
    2                  5226            39               9.5               39  
    3                  5226            48              13.7               60  
    4                  3400            53              14.3               40  

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:231,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693518016063,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="UR6i5Rslihbg" outputId="1f363b91-a461-445c-aed5-ad34079f8e8f">

``` python
uni_df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1302 entries, 0 to 1301
    Data columns (total 11 columns):
     #   Column                 Non-Null Count  Dtype  
    ---  ------                 --------------  -----  
     0   College Name           1302 non-null   object 
     1   State                  1302 non-null   object 
     2   Public/Private         1302 non-null   object 
     3   num_appli_rec          1302 non-null   int64  
     4   num_appl_accepted      1302 non-null   int64  
     5   num_new_stud_enrolled  1302 non-null   int64  
     6   in-state tuition       1302 non-null   int64  
     7   out-of-state tuition   1302 non-null   int64  
     8   % fac. w/PHD           1302 non-null   int64  
     9   stud./fac. ratio       1302 non-null   float64
     10  Graduation rate        1302 non-null   int64  
    dtypes: float64(1), int64(7), object(3)
    memory usage: 112.0+ KB

</div>

</div>

<div class="cell markdown" id="N_qYhxhOiolm">

Usamos la función `pairplot()` de la líbreria `Seaborn` para dibujar scatter plots para cada par de atributos numéricos

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:23492,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693518201330,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="EWzUgZq7jDUK" outputId="49a3b6ac-2d7f-48c5-d6d9-98fef950999a">

``` python
import seaborn as sns
sns.pairplot(uni_df)
```

<div class="output execute_result" execution_count="48">

    <seaborn.axisgrid.PairGrid at 0x7a54a68e0460>

</div>

<div class="output display_data">

![](7dfc416727a226f5ce455988e977894dcf806321.png)

</div>

</div>

<div class="cell markdown" id="Aejky_BNjUFI">

### **Visualización para dos atributos categóricos**

La mejor herramienta para examinar la relación entre dos atributos categóricos es la tabla de contingencia (contingency table) coloreado (mapa de calor).

Recuerde que esta tabla es una matriz que muestra la frencuencia de los data objects en todas sus posibles combinaciones de valores con respecto a ambos atributos.

</div>

<div class="cell markdown" id="jcFMwBeRkhhk">

**TO DO:** Encontrar la relación entre ingresos y género del dataset `adult.csv`

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:143}" executionInfo="{&quot;elapsed&quot;:240,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693518571345,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="P7syfF_hjiLi" outputId="1fcc4a1a-0400-4a99-af99-ee62e77bfda7">

``` python
c_tbl = pd.crosstab(df.income,df.sex)
c_tbl
```

<div class="output execute_result" execution_count="50">

    sex     Female   Male
    income               
    <=50K     9592  15128
    >50K      1179   6662

</div>

</div>

<div class="cell markdown" id="F6n3tgABkvZ9">

La tabla de contingencia nos puede ayudar para crear un mapa de calor:

</div>

<div class="cell code" id="W_zxnA10lJUf">

``` python
#Primero, crear una tabla de probabilidades
#en base a la tabla de contingencia
prob_tbl = c_tbl/ c_tbl.sum()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:449}" executionInfo="{&quot;elapsed&quot;:938,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693518755668,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="uGXAq1x6jnWc" outputId="6dd4aa1d-bf7b-44f5-a5f9-e59e807a6502">

``` python
#Usamos heatmap() de Seaborn para crear una tabla de contingencia coloreada
sns.heatmap(prob_tbl, annot=True, center=0.5 ,cmap="Greys")
plt.show()
```

<div class="output display_data">

![](140b5ef394f5de38551e7eead37b665d39c85d16.png)

</div>

</div>

<div class="cell markdown" id="e8ict86GlfrY">

En el ejemplo anterior el atributo `sex` es binario. Para atributos **no binarios** también funciona. Por ejemplo, utilizemos el atributo `race`

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:574}" executionInfo="{&quot;elapsed&quot;:1213,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693518877840,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="TwPDgMPzjoM7" outputId="26fcaf9b-fae9-4963-d812-8812f7638881">

``` python
c_tbl = pd.crosstab(df.occupation,df.race)
prob_tbl = c_tbl/ c_tbl.sum()
sns.heatmap(prob_tbl, annot=True, center=0.5 ,cmap="Greys")
plt.show()
```

<div class="output display_data">

![](269a8725151d59083c062b651fd0f5b96a411ea5.png)

</div>

</div>

<div class="cell markdown" id="boL388RimMrm">

### **Visualización entre un atributo numérico y un atributo categórico**

</div>

<div class="cell markdown" id="kJj95VBbmX9X">

**TO DO:** Visualizar la relación entre los atributos `race` y `age` del dataset

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:220,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693519105796,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="cCbJXJSRmitB" outputId="7d142d45-e791-466f-96b8-5256a56365f1">

``` python
#Transformar age en un atributo categorico
#A este proceso se denomina Discretizar
age_discretized = pd.cut(df.age, bins = 5)
age_discretized
```

<div class="output execute_result" execution_count="55">

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

<div class="cell code" id="3cGf5WO9jrNw">

``` python
#Creamos la tabla de contingencia entre attr. categóricos
c_tbl = pd.crosstab(age_discretized,df.race)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:574}" executionInfo="{&quot;elapsed&quot;:636,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693519208837,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="vBQEBoSFnBGx" outputId="32a8a89f-043f-40cd-b6d2-b6b927594ec7">

``` python
#Crear el heatmap en base a c_tbl
prob_tbl = c_tbl/ c_tbl.sum()
sns.heatmap(prob_tbl, annot=True, center=0.5 ,cmap="Greys")
plt.show()
```

<div class="output display_data">

![](b367e688e33e0c2812d0836777b8981a206346d3.png)

</div>

</div>

<div class="cell markdown" id="cLmFIoWcnLKr">

**TO DO:** Visualizar la relación entre atributos `education` y `age`

</div>

<div class="cell markdown" id="_Z5bMyPCngdm">

En esta ocasión el atributo categórico `education` tiene dos características:

1.  Es ordinal
2.  Se puede discretizar realizando algunas suposiciones (`education-num`)

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:229,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693519471682,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="b03dOMszoELx" outputId="218527f6-c1f1-4119-b46f-962a4ccdc7e5">

``` python
#1. Analizamos la relación entre education y education-num
#Como se ve hay una relación entre los atributos
df.groupby(['education','education-num']).size()
```

<div class="output execute_result" execution_count="59">

    education     education-num
    10th          6                  933
    11th          7                 1175
    12th          8                  433
    1st-4th       2                  168
    5th-6th       3                  333
    7th-8th       4                  646
    9th           5                  514
    Assoc-acdm    12                1067
    Assoc-voc     11                1382
    Bachelors     13                5355
    Doctorate     16                 413
    HS-grad       9                10501
    Masters       14                1723
    Preschool     1                   51
    Prof-school   15                 576
    Some-college  10                7291
    dtype: int64

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:449}" executionInfo="{&quot;elapsed&quot;:584,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693519601863,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="6bdGefOwofia" outputId="e48a0241-eb7a-415c-8b31-55bdfb9dd192">

``` python
#Podemos visualizar age y su versión númerica de education
df.plot.scatter(x='age',y='education-num')
plt.show()
```

<div class="output display_data">

![](b5de47a2937e163b4bd6ad857c6c36239bb95dfc.png)

</div>

</div>

<div class="cell markdown" id="4Rqk6dr1pC4U">

Como se observa en el gráfico anterior, estos atributos no estan relacionados. Por lo que ahora realizaremos el análisis al revés. Es decir, discreticemos `age` y con eso creamos una tabla de contingencia. De esa manera, podremos analizar si llegamos a la misma conclusión

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:535}" executionInfo="{&quot;elapsed&quot;:1291,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693519862512,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aipMTzPhj-yO" outputId="c6201c6e-c08e-4335-9303-a97c7d403b6f">

``` python
age_discretized = pd.cut(df['age'], bins = 5)
c_tbl = pd.crosstab(df.education,age_discretized)
prob_tbl = c_tbl/ c_tbl.sum()
sns.heatmap(prob_tbl, annot=True, center=0.5 ,cmap="Greys")
plt.show()
```

<div class="output display_data">

![](17686a9d08d0448b209536a8257f7d5770252850.png)

</div>

</div>

<div class="cell markdown" id="zGYKPCSIpyGT">

## **IV. Agregando dimensiones visuales**

Las visualizaciones que hemos creado hasta ahora tienen **sólo dos dimensiones**. <br>

Cuando los elementos visuales se utilizan como herramientas de exploración para detectar patrones en los datos, **poder agregar dimensiones a los elementos visuales** podría ser justo lo que necesita un analista de datos. Hay muchas formas de agregar dimensiones a un objeto visual, como usar ***color, tamaño, tono, estilos de línea*** y más. <br>

En este laboratorio cubriremos los tres enfoques más aplicados agregando dimensiones usando: **color, tamaño y tiempo.**

</div>

<div class="cell markdown" id="K_QV6DmQ0P87">

Para esta sección, utilizaremos un nuevo dataset `WH Report_preprocessed.csv`. Este dataset ha sido tomado del *The World Happiness Report* que incluye datos de 2010 a 2019.

Para este laboratorio nos enfocaremos en los siguientes atributos:

- `Healthy_life_expectancy_at_birth` : Esperanza de vida saludable al nacer
- `Log_GDP_per_capita`: PBI per capita (Log)
- `year` : año del reporte
- `Continent` : continente
- `Population` : población

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:226}" executionInfo="{&quot;elapsed&quot;:338,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693522794681,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mRn8gHNM0cW8" outputId="73fbfa6f-2dd3-4e6c-92ae-564b36963c89">

``` python
country_df = pd.read_csv('WH Report_preprocessed.csv')
country_df.head()
```

<div class="output execute_result" execution_count="63">

              Name Continent  year  population  Life_Ladder  Log_GDP_per_capita  \
    0  Afghanistan      Asia  2010  29185507.0        4.758               7.647   
    1  Afghanistan      Asia  2011  30117413.0        3.832               7.620   
    2  Afghanistan      Asia  2012  31161376.0        3.783               7.705   
    3  Afghanistan      Asia  2013  32269589.0        3.572               7.725   
    4  Afghanistan      Asia  2014  33370794.0        3.131               7.718   

       Social_support  Healthy_life_expectancy_at_birth  \
    0           0.539                             51.60   
    1           0.521                             51.92   
    2           0.521                             52.24   
    3           0.484                             52.56   
    4           0.526                             52.88   

       Freedom_to_make_life_choices  Generosity  Perceptions_of_corruption  \
    0                         0.600       0.121                      0.707   
    1                         0.496       0.162                      0.731   
    2                         0.531       0.236                      0.776   
    3                         0.578       0.061                      0.823   
    4                         0.509       0.104                      0.871   

       Positive_affect  Negative_affect  
    0            0.618            0.275  
    1            0.611            0.267  
    2            0.710            0.268  
    3            0.621            0.273  
    4            0.532            0.375  

</div>

</div>

<div class="cell markdown" id="FIFkjSEGJlSo">

### **Visualizando tres dimensiones**

</div>

<div class="cell markdown" id="YWv-dorcH853">

**TO DO:** Analicemos visualmente los atributos de `Healthy_life_expectancy_at_birth`, `Log_GDP_per_capita` y `year`

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:696}" executionInfo="{&quot;elapsed&quot;:2154,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693527483929,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="MbNOyg4NqITV" outputId="abd3d7ed-6a8f-4a06-9959-5490c05c6fef">

``` python

plt.figure(figsize=(15,8))

year_poss = country_df.year.unique()

for i,yr in enumerate(year_poss):
    BM = country_df.year == yr
    X= country_df[BM].Healthy_life_expectancy_at_birth
    Y= country_df[BM].Log_GDP_per_capita

    plt.subplot(2,5,i+1)
    plt.scatter(X,Y)
    plt.title(yr)
    plt.xlim([30,80])
    plt.ylim([6,12])

plt.show()
plt.tight_layout()
```

<div class="output display_data">

![](aef9fdd13734f078e3304ad9f16b2d4fc09e8823.png)

</div>

<div class="output display_data">

    <Figure size 640x480 with 0 Axes>

</div>

</div>

<div class="cell markdown" id="HbqPx96wIyUp">

**TO DO:** Podemos mejorar el gráfico anterior utilizando un sólo gráfico y un slide bar para los años y ver la evolución.

</div>

<div class="cell markdown" id="kHZgpyYXJyiA">

***Paso 1:*** Crear una función que devuelva el scatterplot relevante al año.

</div>

<div class="cell code" id="TyRxbvhqqIwh">

``` python
def plotyear(year):
    BM = country_df.year == year
    X= country_df[BM].Healthy_life_expectancy_at_birth
    Y= country_df[BM].Log_GDP_per_capita

    plt.scatter(X,Y)
    plt.xlabel('Healthy_life_expectancy_at_birth')
    plt.ylabel('Log_GDP_per_capita')
    plt.xlim([30,80])
    plt.ylim([6,12])
    plt.show()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:455}" executionInfo="{&quot;elapsed&quot;:747,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693528121149,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="x72EVRq1qKnW" outputId="3101e562-ba0c-4eb8-bc55-ec3d23ec0604">

``` python
plotyear(2018)
```

<div class="output display_data">

![](f612f69e91a145c9cc5c6e70fa380d0e74eb8865.png)

</div>

</div>

<div class="cell markdown" id="cq4K7QPTJJoE">

***Paso 2:*** Crear un slide bar para ver la evolución en los años

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:505,&quot;referenced_widgets&quot;:[&quot;013c6f2f66344aa683de53055147ab95&quot;,&quot;4194e8936e4a44eb844c4dd2bd4bce08&quot;,&quot;3bfffcf7c2d346299a72d3d288baee63&quot;,&quot;224cb6a50bd6488d99b5a02f7e2baa9b&quot;,&quot;8aabad4a9b3e44b8af98c726d03be9cd&quot;,&quot;efca9a02325e4b1fa4b870aa08af7a96&quot;,&quot;3dbb4dc4474648d3a36662cc2a1bde36&quot;]}" executionInfo="{&quot;elapsed&quot;:316,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693528194002,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="w8SUcc5zqMg0" outputId="5406de48-b0c3-4a32-fd99-a4757ce04261">

``` python
from ipywidgets import interact, widgets

interact(plotyear,year=widgets.IntSlider(min=2010,max=2019,step=1,value=2010))
```

<div class="output display_data">

``` json
{"model_id":"013c6f2f66344aa683de53055147ab95","version_major":2,"version_minor":0}
```

</div>

<div class="output execute_result" execution_count="68">

    <function __main__.plotyear(year)>

</div>

</div>

<div class="cell markdown" id="0ikvhmwDJ078">

### **Visualizando cuatro dimensiones**

</div>

<div class="cell markdown" id="jcRWEUShJ-NL">

**TO DO:** Usemos colores para incluir una cuarta dimensión, `Continent`

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:505,&quot;referenced_widgets&quot;:[&quot;ceb85c417c5448319021e404dbc8d55a&quot;,&quot;7da56f3cdfcc47c9afd49892f5bea677&quot;,&quot;33d9a8f1f4a24cc89c439426b86cc45e&quot;,&quot;8a101601af4246d08ccda1b8c43c4260&quot;,&quot;a9813bbd9a5d4597933dd2c16c215324&quot;,&quot;d33e046d68424566a47434ee92517949&quot;,&quot;91428286b1c44518aa2073c3cd493846&quot;]}" executionInfo="{&quot;elapsed&quot;:897,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693528391569,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="UCmLo5rBqQYJ" outputId="43e36db3-c068-4df8-b9fe-5c3cc32c58f2">

``` python
Continent_poss = country_df.Continent.unique()
colors_dic={'Asia':'b', 'Europe':'g', 'Africa':'r', 'South America':'c',
            'Oceania':'m', 'North America':'y', 'Antarctica':'k'}

def plotyear(year):
    for continent in Continent_poss:
        BM1 = (country_df.year == year)
        BM2 = (country_df.Continent ==continent)
        BM = BM1 & BM2
        X = country_df[BM].Healthy_life_expectancy_at_birth
        Y= country_df[BM].Log_GDP_per_capita
        plt.scatter(X,Y,c=colors_dic[continent], marker='o',
                    linewidths=0.5,edgecolors='w',label=cotinent)

    plt.xlabel('Healthy_life_expectancy_at_birth')
    plt.ylabel('Log_GDP_per_capita')
    plt.xlim([30,80])
    plt.ylim([6,12])
    plt.legend(ncol=1)
    plt.show()

interact(plotyear,year=widgets.IntSlider(min=2010,max=2019,step=1,value=2010))
```

<div class="output display_data">

``` json
{"model_id":"ceb85c417c5448319021e404dbc8d55a","version_major":2,"version_minor":0}
```

</div>

<div class="output execute_result" execution_count="69">

    <function __main__.plotyear(year)>

</div>

</div>

<div class="cell markdown" id="PFoqAfQiKUUi">

### **Visualizando cinco dimensiones**

</div>

<div class="cell markdown" id="5FtAj5sJKV6X">

**TO DO:** Utilicemos markers para representar `population`

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:505,&quot;referenced_widgets&quot;:[&quot;38c14db4884b4573bce51753133b34fd&quot;,&quot;810d958bb22f4bc18209e856d9bdcd15&quot;,&quot;1b06d8a3f25f4049aec2010e6fd502ee&quot;,&quot;d236a8d59c1c4843b190867f1bcbabc7&quot;,&quot;162c0492b2c44b57a60f1ca357f24de9&quot;,&quot;62a2ac72f4774b13a73a807f7338a143&quot;,&quot;b7419b7f266446b9a09664d2d78dee43&quot;]}" executionInfo="{&quot;elapsed&quot;:879,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1693528475505,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="6bOsOgmvqTTB" outputId="c4f4b63a-497b-4e68-dbc5-262ad9c074f5">

``` python
Continent_poss = country_df.Continent.unique()
colors_dic={'Asia':'b', 'Europe':'g', 'Africa':'r', 'South America':'c',
            'Oceania':'m', 'North America':'y', 'Antarctica':'k'}
country_df.sort_values(['population'],inplace = True, ascending=False)

def plotyear(year):
    for cotinent in Continent_poss:
        BM1 = (country_df.year == year)
        BM2 = (country_df.Continent ==cotinent)
        BM = BM1 & BM2
        # para bajar la escala uniformemente
        size = country_df[BM].population/200000
        X = country_df[BM].Healthy_life_expectancy_at_birth
        Y= country_df[BM].Log_GDP_per_capita
        plt.scatter(X,Y,c=colors_dic[cotinent], marker='o', s=size,
                    linewidths=0.5,edgecolors='w',label=cotinent)

    plt.xlabel('Healthy_life_expectancy_at_birth')
    plt.ylabel('Log_GDP_per_capita')
    plt.xlim([30,80])
    plt.ylim([6,12])
    #Para escalar los markers en la legenda
    plt.legend(markerscale=0.5)
    plt.show()

interact(plotyear,year=widgets.IntSlider(min=2010,max=2019,step=1,value=2010))
```

<div class="output display_data">

``` json
{"model_id":"38c14db4884b4573bce51753133b34fd","version_major":2,"version_minor":0}
```

</div>

<div class="output execute_result" execution_count="70">

    <function __main__.plotyear(year)>

</div>

</div>
