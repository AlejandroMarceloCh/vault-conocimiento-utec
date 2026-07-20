---
curso: ACD
titulo: U1_L6 Matplotlib para Análisis de Datos
slides: 0
fuente: U1_L6 Matplotlib para Análisis de Datos.ipynb
---

<div class="cell markdown" id="7KXnS5_YUthp">

# **Laboratorio: Matplotlib para Análisis de Datos**

**Objetivo:** Aprender métodos sobre la librería Matplotlib para análisis de Datos.

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:769,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713215775086,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="PncIkoa1erBd">

``` python
#Importar librerías
import pandas as pd
import numpy as np
#Librería para visualización
import matplotlib.pyplot as plt
```

</div>

<div class="cell markdown" id="5gJL6XrZgE7y">

## **I. Plotting**

Dibujamos a partir de un conjunto de datos.

</div>

<div class="cell code" execution_count="2" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:296,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713215814454,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aUQPQ8Ebf22_" outputId="9f9b9a10-6de2-4ca5-f054-038636b7bb83">

``` python
data = np.arange(10)
data
plt.plot(data)
#comando para mostrar
plt.show()
```

<div class="output display_data">

![](d13981ba9e304bb8a65e679aa6b79078fc37fe97.png)

</div>

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:291,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713215895622,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_DrPFj5vn-LT" outputId="b0bd22f1-8d12-4616-95f9-12f3dbe79f4e">

``` python
data
```

<div class="output execute_result" execution_count="3">

    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

</div>

</div>

<div class="cell markdown" id="Xco7kiAIolKY">

### **Propiedades de Plot**

Matplotlib es excelente para permitirnos modificar los gráficos para que satisfagan las necesidades. Lo primero que necesita antes de modificar un objeto visual es saber el nombre de la parte del objeto visual que desea modificar.

</div>

<div class="cell markdown" id="G2kme_PutHMP">

#### **Agregar el título al gráfico**

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:452}" executionInfo="{&quot;elapsed&quot;:701,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216126426,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="6cBsDM9xqyKE" outputId="ede9ff17-c413-4899-cb56-8e04e969d563">

``` python
#configura el límite de ejes x, y
plt.axis([0,5,0,20])
#agrega el título al gráfico
plt.title('My first plot')
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()
```

<div class="output display_data">

![](15c18b65eb1cff73db7fde0b7713f09894b05ab9.png)

</div>

</div>

<div class="cell markdown" id="7yFs3SOcT0TW">

Se puede cambiar la fuente y el tamaño de letra

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:484}" executionInfo="{&quot;elapsed&quot;:996,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216220640,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="g8SIeipNwvsl" outputId="b5d5e864-1b3e-426f-b637-0a23deae66c1">

``` python
plt.axis([0,5,0,20])
#Cambiar font size para el título
plt.title('My first plot',fontsize=40,fontname='Sans')
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()
```

<div class="output display_data">

![](c8860958bc1e206ccb622ce6b5089b5cf7088a9b.png)

</div>

</div>

<div class="cell markdown" id="KoJ8YrAfvQgt">

#### **Agregar etiquetas a los ejes**

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}" executionInfo="{&quot;elapsed&quot;:803,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216241984,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="iJLduMl-vf2P" outputId="e69da69a-cd36-480f-e2e3-e07eacd14ebe">

``` python
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting')
plt.ylabel('Square values')
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()
```

<div class="output display_data">

![](b73d47a67eb6e27758fc25e3b174a22377f0cc26.png)

</div>

</div>

<div class="cell markdown" id="1wULtI6DT6a-">

Se puede cambiar los colores de las etiquetas de los ejes

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}" executionInfo="{&quot;elapsed&quot;:1008,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216295694,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="ywj2_9Gpx-WV" outputId="5df8b023-2918-4b03-ff9e-d8511c8bbeed">

``` python
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting',color='green')
plt.ylabel('Square values',color='blue')
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()
```

<div class="output display_data">

![](2c385c23ca35b9101300d2fd2ed2721babb2005c.png)

</div>

</div>

<div class="cell markdown" id="_9n-dgRPUV1_">

#### **Modificar los makers**

- Markers: <https://matplotlib.org/stable/api/markers_api.html>
- Colors: <https://matplotlib.org/stable/api/markers_api.html>

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}" executionInfo="{&quot;elapsed&quot;:828,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216458163,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4cTIhMU_VD-W" outputId="eba22787-ea47-4ccd-cbcf-cc0a6b63f83a">

``` python
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting',color='green')
plt.ylabel('Square values',color='blue')
#El tercer párametro es para marker otra manera marker = 'o'
plt.plot([1,2,3,4],[1,4,9,16],'rv')
plt.show()
```

<div class="output display_data">

![](7ba09dd71f877b16c97c2395906a1d8412a43975.png)

</div>

</div>

<div class="cell markdown" id="3h8zhnioUSXf">

#### **Agregar etiquetas a los datos**

</div>

<div class="cell code" execution_count="11" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}" executionInfo="{&quot;elapsed&quot;:297,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216500548,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="53F_bL64XVUa" outputId="a3609073-5932-4374-8d21-9f0d4e58d563">

``` python
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting',color='green')
plt.ylabel('Square values',color='blue')
#Agregar etiquetas en la posición correcta
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()
```

<div class="output display_data">

![](e617f9331eea053bc2310d0d250dd154013ce4b6.png)

</div>

</div>

<div class="cell markdown" id="8t3ZH0WsX6LQ">

#### **Agregar expresiones matemáticas**

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}" executionInfo="{&quot;elapsed&quot;:842,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216591212,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="r5Ck9FXJX9Be" outputId="b7fd6ada-a8ba-461c-8f22-5789ab9d31c6">

``` python
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting',color='green')
plt.ylabel('Square values',color='blue')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
#Agregar expresión matemática
plt.text(1.1,12,r'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()
```

<div class="output display_data">

![](74b6f591724b2c43d9ab34a8a529c18943cac9b7.png)

</div>

</div>

<div class="cell markdown" id="-lZ_oQGbrp8o">

#### **Agregar una grilla**

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}" executionInfo="{&quot;elapsed&quot;:710,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216673555,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8MINZP9YYiHu" outputId="4e63c951-9ac9-4c98-f76b-0be1067f2002">

``` python
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting',color='green')
plt.ylabel('Square values',color='blue')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
#agregar la grilla
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()
```

<div class="output display_data">

![](451455754f6bc546d43827cbdb93fad64e72494f.png)

</div>

</div>

<div class="cell markdown" id="1gn6kID6Y04w">

#### **Agregar una leyenda**

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}" executionInfo="{&quot;elapsed&quot;:762,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216706782,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_7ewvcXPY3_M" outputId="f3e83253-2425-4ff7-ff27-a491682bc98f">

``` python
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting',color='green')
plt.ylabel('Square values',color='blue')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.legend(['First series'])
plt.show()
```

<div class="output display_data">

![](fbd82cf8f80d7eddfd8f8aef33fa4ad94e2bedbb.png)

</div>

</div>

<div class="cell markdown" id="Q0BrT3gFZT7B">

Para más de una serie:

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}" executionInfo="{&quot;elapsed&quot;:875,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216764106,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="s5dio3McZb_k" outputId="af371776-8dec-42cd-af00-f9c2b1190fc5">

``` python
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')

plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.grid(True)

plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'b*')


plt.legend(['First series','Second series','Third series'],loc=2)
plt.show()
```

<div class="output display_data">

![](5bd1ef6108a2790c8be8ecc9803bc5500e46147a.png)

</div>

</div>

<div class="cell markdown" id="DsNslvtJbTH6">

## **II. Principales Gráficos en Matplotlib**

Dibujar imágenes con Matplotlib es fácil. Todo lo que necesita es la entrada correcta y una comprensión correcta de los datos. Los cinco elementos visuales principales que utilizamos en Matplotlib para dibujar son:

- Histogramas
- Boxplots (diagramas de caja)
- Gráfico de barras (bar charts)
- Diagrama de líneas (line plots)
- Scatterplots (diagramas de dispersión)

</div>

<div class="cell markdown" id="DG70hsMXbrJj">

Para esta parte usaremos un dataset

</div>

<div class="cell code" execution_count="16" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:330}" executionInfo="{&quot;elapsed&quot;:334,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216918173,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="o5YCDbrdbz1v" outputId="05025345-5869-4e22-f92f-3fc00190bc05">

``` python
df = pd.read_csv('adult.csv')
df.head()
```

<div class="output execute_result" execution_count="16">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 32561,\n  \"fields\": [\n    {\n      \"column\": \"age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 13,\n        \"min\": 17,\n        \"max\": 90,\n        \"num_unique_values\": 73,\n        \"samples\": [\n          28,\n          73,\n          35\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"workclass\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 8,\n        \"samples\": [\n          \"Self-emp-not-inc\",\n          \"Self-emp-inc\",\n          \"State-gov\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"fnlwgt\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 105549,\n        \"min\": 12285,\n        \"max\": 1484705,\n        \"num_unique_values\": 21648,\n        \"samples\": [\n          128485,\n          469907,\n          235951\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 16,\n        \"samples\": [\n          \"Bachelors\",\n          \"HS-grad\",\n          \"Some-college\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education-num\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2,\n        \"min\": 1,\n        \"max\": 16,\n        \"num_unique_values\": 16,\n        \"samples\": [\n          13,\n          9,\n          10\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"marital-status\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Never-married\",\n          \"Married-civ-spouse\",\n          \"Married-AF-spouse\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"occupation\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 14,\n        \"samples\": [\n          \"Machine-op-inspct\",\n          \"Protective-serv\",\n          \"Adm-clerical\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"relationship\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Not-in-family\",\n          \"Husband\",\n          \"Other-relative\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"race\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"Black\",\n          \"Other\",\n          \"Asian-Pac-Islander\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"sex\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Female\",\n          \"Male\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capitalGain\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7385,\n        \"min\": 0,\n        \"max\": 99999,\n        \"num_unique_values\": 119,\n        \"samples\": [\n          3781,\n          15831\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"capitalLoss\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 402,\n        \"min\": 0,\n        \"max\": 4356,\n        \"num_unique_values\": 92,\n        \"samples\": [\n          419,\n          2051\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"hoursPerWeek\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 12,\n        \"min\": 1,\n        \"max\": 99,\n        \"num_unique_values\": 94,\n        \"samples\": [\n          6,\n          22\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"nativeCountry\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 41,\n        \"samples\": [\n          \"El-Salvador\",\n          \"Italy\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"income\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \">50K\",\n          \"<=50K\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:294,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713216928035,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="gQrGTRR2b0g8" outputId="25bdb562-3a2e-4af7-9fcf-f288686682c2">

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

<div class="cell markdown" id="MGe22C-TbdIx">

### **Resumen de atributos numéricos usando histogramas o boxplots**

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:786,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713217112223,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="3QNJsD_4b6VK" outputId="403f1219-46cc-42e6-c5ff-06e519e2aeae">

``` python
#Histograma
plt.hist(df.age)
plt.show()
```

<div class="output display_data">

![](0997f7d9f4219251063e2c9a931181a0f0c020d5.png)

</div>

</div>

<div class="cell code" execution_count="19" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:311,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713217229660,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="SBu7FXRAcBBZ" outputId="5be1f23e-e6a1-457a-cb15-f2423d31ec75">

``` python
#Boxplot
plt.boxplot(df.age, vert=False)
plt.show()
```

<div class="output display_data">

![](31730ec20c20ad946519ad39ef482d33f836b0c6.png)

</div>

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:936,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713217590745,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="nE78WC1mcBuA" outputId="a554a41d-3494-4f9c-a340-634104083bbe">

``` python
#Tu turno de los otros atributos numéricos
plt.hist(df.hoursPerWeek)
plt.show()
```

<div class="output display_data">

![](27c5dff1439c542f0bd62b9973a925c243f17774.png)

</div>

</div>

<div class="cell markdown" id="3hpE3AHscMvT">

### **Observar tendencias en los datos usando un Diagrama de Línea (*line plot*)**

Para revisar tendencias, usaremos los siguientes datasets: a) Amazon_Stock.csv y b) Apple_Stock.csv. Estos datasets contienen precios de acciones (stock prices) de Amazon y Apple desde 2000 al 2020.

</div>

<div class="cell code" execution_count="21" executionInfo="{&quot;elapsed&quot;:243,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713217708282,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="qDfJyGSLcL2s">

``` python
amz_df = pd.read_csv('Amazon Stock.csv')
apl_df = pd.read_csv('Apple Stock.csv')
```

</div>

<div class="cell code" execution_count="22" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:272,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713217838528,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="EGGmyWAicZhS" outputId="580e6189-2ff2-43a2-babf-2e84ddca280e">

``` python
#Tu turno: Explora los datasets
amz_df.head()
```

<div class="output execute_result" execution_count="22">

``` json
{"summary":"{\n  \"name\": \"amz_df\",\n  \"rows\": 5284,\n  \"fields\": [\n    {\n      \"column\": \"Date\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 5284,\n        \"samples\": [\n          \"4/15/2010\",\n          \"7/23/2012\",\n          \"2/27/2001\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Open\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 718.025336630988,\n        \"min\": 5.909999847,\n        \"max\": 3547.0,\n        \"num_unique_values\": 4743,\n        \"samples\": [\n          190.7899933,\n          611.7999878,\n          83.87000275\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"High\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 725.8863130955956,\n        \"min\": 6.099999905,\n        \"max\": 3552.25,\n        \"num_unique_values\": 4725,\n        \"samples\": [\n          1163.189941,\n          259.6799927,\n          83.25\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Low\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 708.750466266107,\n        \"min\": 5.510000229,\n        \"max\": 3486.689941,\n        \"num_unique_values\": 4720,\n        \"samples\": [\n          166.9700012,\n          18.85000038,\n          12.5\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Close\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 717.5844492406999,\n        \"min\": 5.96999979,\n        \"max\": 3531.449951,\n        \"num_unique_values\": 4799,\n        \"samples\": [\n          807.6400146,\n          14.31000042,\n          834.0900269\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Volume\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 5111533,\n        \"min\": 881300,\n        \"max\": 104329200,\n        \"num_unique_values\": 5151,\n        \"samples\": [\n          6289700,\n          4027100,\n          4299200\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Dividends\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 0,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Stock Splits\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 0,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"amz_df"}
```

</div>

</div>

<div class="cell code" execution_count="24" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:337,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713217883791,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="MICD3uIyviYF" outputId="79fdc9de-4b0a-44cb-b77c-246365526e2b">

``` python
apl_df.head()
```

<div class="output execute_result" execution_count="24">

``` json
{"summary":"{\n  \"name\": \"apl_df\",\n  \"rows\": 5284,\n  \"fields\": [\n    {\n      \"column\": \"Date\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 5284,\n        \"samples\": [\n          \"4/15/2010\",\n          \"7/23/2012\",\n          \"2/27/2001\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Open\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 23.590563029517863,\n        \"min\": 0.199805337,\n        \"max\": 137.8440254,\n        \"num_unique_values\": 5279,\n        \"samples\": [\n          0.726654845,\n          2.029125475,\n          0.378384902\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"High\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 23.876358253912343,\n        \"min\": 0.202882078,\n        \"max\": 138.5829115,\n        \"num_unique_values\": 5279,\n        \"samples\": [\n          0.759460732,\n          2.058658598,\n          0.385921756\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Low\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 23.3016784771454,\n        \"min\": 0.195652658,\n        \"max\": 134.1395542,\n        \"num_unique_values\": 5272,\n        \"samples\": [\n          0.711394065,\n          40.08258052,\n          27.98442895\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Close\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 23.601325557300786,\n        \"min\": 0.201805368,\n        \"max\": 136.4860535,\n        \"num_unique_values\": 4884,\n        \"samples\": [\n          1.881156921,\n          0.332547396,\n          2.141102791\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Volume\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 391178719,\n        \"min\": 39340000,\n        \"max\": 7421640800,\n        \"num_unique_values\": 5254,\n        \"samples\": [\n          755445600,\n          168249600,\n          195804000\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Dividends\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.012153631832398712,\n        \"min\": 0.0,\n        \"max\": 0.205,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          0.1925,\n          0.094643,\n          0.1425\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Stock Splits\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 7,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2,\n          4,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"apl_df"}
```

</div>

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:301,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713217860103,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4DypZWp1vdK3" outputId="363f4173-3f33-4cb2-bfbe-3f2beb98c32a">

``` python
amz_df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5284 entries, 0 to 5283
    Data columns (total 8 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   Date          5284 non-null   object 
     1   Open          5284 non-null   float64
     2   High          5284 non-null   float64
     3   Low           5284 non-null   float64
     4   Close         5284 non-null   float64
     5   Volume        5284 non-null   int64  
     6   Dividends     5284 non-null   int64  
     7   Stock Splits  5284 non-null   int64  
    dtypes: float64(4), int64(3), object(1)
    memory usage: 330.4+ KB

</div>

</div>

<div class="cell code" execution_count="25" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:353,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713217944591,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="nK4O1gqRvx9L" outputId="709b82a4-6d95-47d4-c328-2c55eb0fc72d">

``` python
apl_df.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5284 entries, 0 to 5283
    Data columns (total 8 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   Date          5284 non-null   object 
     1   Open          5284 non-null   float64
     2   High          5284 non-null   float64
     3   Low           5284 non-null   float64
     4   Close         5284 non-null   float64
     5   Volume        5284 non-null   int64  
     6   Dividends     5284 non-null   float64
     7   Stock Splits  5284 non-null   int64  
    dtypes: float64(5), int64(2), object(1)
    memory usage: 330.4+ KB

</div>

</div>

<div class="cell markdown" id="HdrEskDZcdUQ">

Revisar la tendencia en los precios para cerrar (closing prices) de las acciones:

</div>

<div class="cell code" execution_count="27" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:270,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713218073153,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_KAX-YF7wRWw" outputId="d4226cb6-5246-4c20-f64c-de3c25caa349">

``` python
amz_df.Close
```

<div class="output execute_result" execution_count="27">

    0         89.375000
    1         81.937500
    2         69.750000
    3         65.562500
    4         69.562500
               ...     
    5279    3172.689941
    5280    3283.959961
    5281    3322.000000
    5282    3285.850098
    5283    3256.929932
    Name: Close, Length: 5284, dtype: float64

</div>

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:795,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713218033669,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="dukOdgLEchLw" outputId="a51128b5-c495-4c36-c517-f79494f27625">

``` python
#Tendencia en Amazon
plt.plot(amz_df.Close)
plt.show()
```

<div class="output display_data">

![](1f4ceaf61e971ea75f31eb3274d3854424d92ca9.png)

</div>

</div>

<div class="cell code" execution_count="28" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:311,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713218251073,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="hustHJP6cot7" outputId="92d10f82-4cd6-42e8-c089-900c43d0712c">

``` python
#Tendencia en Apple
plt.plot(apl_df.Close)
plt.show()
```

<div class="output display_data">

![](506725343eda10ce71b7b0d9ad0ca6c9be7a78e3.png)

</div>

</div>

<div class="cell code" execution_count="29" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:284,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713218297652,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="njBCEnescubY" outputId="b2e16ef1-6460-45e5-fd46-51cf57e51b63">

``` python
#Tendencias juntas
plt.plot(amz_df.Close)
plt.plot(apl_df.Close)
plt.show()
```

<div class="output display_data">

![](59d4188d95a47bd77560fb03ec4e937a523970cd.png)

</div>

</div>

<div class="cell markdown" id="VDFyW-7ic1ze">

### **Relacionar dos atributos numéricos usando scatterplot**

¿Cómo mostramos la relación entre los precios de las acciones de Amazon y Apple entre los años 2000 y 2020?

</div>

<div class="cell code" execution_count="30" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:818,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713218361714,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="rYScQZVMdGQJ" outputId="fcfb65e3-89f4-417d-bc10-88ffb2d706ff">

``` python
plt.scatter(apl_df.Close,amz_df.Close)
plt.show()
```

<div class="output display_data">

![](ed5787b59a3abb8dd89903985f839354b5596df4.png)

</div>

</div>

<div class="cell markdown" id="OOfMl5nKdH3L">

**Tu Turno:**

- Titular al gráfico como: Tendencias entre acciones de Amazon y Apple
- Agregar una etiqueta a los ejes (si corresponde)
- Agregar leyendas.
- 

Tip: Para agregar leyendas debemos hacer dos pasos:

1.  Agregar la etiqueta relevante para cada segmento de la data
2.  Después de ejecutar los gráficos, se ejecuta `plt.legend()`

</div>

<div class="cell code" execution_count="31" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}" executionInfo="{&quot;elapsed&quot;:665,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713219129494,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="i8YqTwPdY2u1" outputId="7ff7ec7a-e912-4a2e-a793-c0a8bb9a8169">

``` python
#Tu Turno
plt.title('Tendencias entre acciones de Amazon y Apple')
plt.plot(amz_df.Close)
plt.plot(apl_df.Close)
plt.xlabel('Years', color='black')
plt.ylabel('Close', color='black')
plt.grid(True)
plt.legend(['Amazon','Apple'],loc=2)
plt.show()
```

<div class="output display_data">

![](d14edd5b320af0ae9857803c27ec81756431e88c.png)

</div>

</div>

<div class="cell markdown" id="1gnWUonJY7tF">

### **Modificar *ticks***

Ejemplo de agregar xticks

</div>

<div class="cell code" execution_count="33" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:493}" executionInfo="{&quot;elapsed&quot;:864,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713219404879,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4wJsP23PZCMm" outputId="9ba01f4e-1c75-4be4-aae0-dfd041580d92">

``` python
# TO DO
plt.title('Tendencias entre acciones de Amazon y Apple')
plt.plot(amz_df.Close)
plt.plot(apl_df.Close)
plt.xlabel('Years', color='black')
plt.ylabel('Close', color='black')
plt.grid(True)
plt.legend(['Amazon','Apple'],loc=2)
plt.xticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500], rotation=90)
plt.show()
```

<div class="output display_data">

![](2401f26e24fd32c3fa9db71a0afc19f16e3074b8.png)

</div>

</div>

<div class="cell markdown" id="gQUIxjCSZQD9">

¿Qué tal si queremos volver a representar estos números enteros que representan días de negociación con las fechas reales?

</div>

<div class="cell code" execution_count="38" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:538}" executionInfo="{&quot;elapsed&quot;:734,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713219982434,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="v3HoXPZkZPC2" outputId="bdd04575-2613-4d86-c8fd-d9e3d9437ca7">

``` python
#Tu turno
#Primer Paso: crear array del tamaño de amz_df con intervalos de 250plt.title('Tendencias entre acciones de Amazon y Apple')
plt.title('Tendencias entre acciones de Amazon y Apple')
plt.plot(amz_df.Close)
plt.plot(apl_df.Close)
plt.xlabel('Date', color='black')
plt.ylabel('Close Price', color='black')
#plt.grid(True)
plt.legend(['Amazon','Apple'],loc=2)
plt.xticks(np.arange(0,len(amz_df),250),
           amz_df.Date[0:len(amz_df):250], rotation=90)
plt.show()
```

<div class="output display_data">

![](c38ddca15fde4beb90c46ab954257bd52fb9fbf7.png)

</div>

</div>

<div class="cell code" execution_count="35" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:268,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713219777062,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="wOAjP-Vr2ylE" outputId="954f5fea-9086-40a6-9b51-64fe13dbc66b">

``` python
np.arange(0,len(amz_df),250)
```

<div class="output execute_result" execution_count="35">

    array([   0,  250,  500,  750, 1000, 1250, 1500, 1750, 2000, 2250, 2500,
           2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250])

</div>

</div>

<div class="cell code" execution_count="36" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:4,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713219802882,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aSH8lB5B24zg" outputId="1a0706b1-b4a3-4968-e080-30172b25152a">

``` python
amz_df.Date[0:len(amz_df):250]
```

<div class="output execute_result" execution_count="36">

    0         1/3/2000
    250     12/28/2000
    500       1/2/2002
    750     12/30/2002
    1000    12/26/2003
    1250    12/23/2004
    1500    12/20/2005
    1750    12/18/2006
    2000    12/17/2007
    2250    12/12/2008
    2500    12/10/2009
    2750     12/8/2010
    3000     12/5/2011
    3250     12/4/2012
    3500     12/2/2013
    3750    11/28/2014
    4000    11/25/2015
    4250    11/22/2016
    4500    11/20/2017
    4750    11/16/2018
    5000    11/15/2019
    5250    11/12/2020
    Name: Date, dtype: object

</div>

</div>

<div class="cell markdown" id="2E_7FBPwgRrd">

## **III. Figuras y Subplots**

Dibujar un **subplot** puede ser una herramienta de preprocesamiento y análisis de datos muy útil. Usamos subplots cuando queremos poblar más de un objeto visual y organizarlos uno al lado del otro de una manera específica.

</div>

<div class="cell code" execution_count="39" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:435}" executionInfo="{&quot;elapsed&quot;:1090,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713220014812,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="o-S_jkMwgWkJ" outputId="f50c951c-a5fc-46de-a258-bf13ba9cf86b">

``` python
#1. Crea una figura
fig = plt.figure()
#2. Puedes crear subplots con add_subplot
#add_subplot(2,2,a) es que la figura 2x2 y es el c subplot
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
```

<div class="output display_data">

![](a13f1b530cec4bcca5c1cb69dfd2012ea687cd1d.png)

</div>

</div>

<div class="cell markdown" id="qkRTblsSioPu">

Podemos crear diferentes tipos de plots

</div>

<div class="cell code" execution_count="40" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" executionInfo="{&quot;elapsed&quot;:1056,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713220089740,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="nLMNTP5jipyZ" outputId="4944e57c-98f7-48ab-bc7f-0d33a96de725">

``` python
ax1.hist(np.random.standard_normal(100), bins=20, color="black", alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.standard_normal(30))
ax3.plot(np.random.standard_normal(50).cumsum(), color="black",linestyle="dashed")
fig
```

<div class="output execute_result" execution_count="40">

![](c470cd5a96372fd44938110d9752b4f7370be88f.png)

</div>

</div>

<div class="cell markdown" id="DBhZhHTNbk1R">

**Tu turno:** Reutilicemos el dataframe basado en adult.csv para realizar un gráfico donde se analice el atributo `age` a través de dos gráficos:

- Histograma
- Boxplot El gráfico debe tener tamaño 2x1.

**Tip:** La función `plt.tight_layout()` se utiliza mejor una vez que haya terminado con todos los elementos visuales y esté a punto de mostrar los subplots completos. Esta función garantiza que cada objeto visual se ajuste a sus propios límites y no haya superposiciones.

</div>

<div class="cell code" execution_count="42" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:266}" executionInfo="{&quot;elapsed&quot;:1224,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1713220734532,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="uTTtIGWxjAcf" outputId="04b69d46-5c75-44fb-a15a-b30830a889e6">

``` python
#Tu turno
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 2)
ax2 = fig.add_subplot(2, 2, 1)
ax1.hist(df.age,bins=20, color="orange", alpha=0.3)
ax2.boxplot(df.age,vert=False)
plt.tight_layout()
```

<div class="output display_data">

![](53e91bbfdd20c54c2880240e73cfcce875fd347c.png)

</div>

</div>
