---
curso: ACD
titulo: U3_L9 Geospatial Data Analysis
slides: 0
fuente: U3_L9 Geospatial Data Analysis.ipynb
---

<div class="cell markdown" id="zSWAQXWtca33">

# **Laboratorio 9: Geospatial Data Analysis**

**Objetivo de la Sesión:**

- Al finalizar la sesión, el estudiante obtendrá un panorama de las técnicas computacionales de pre-procesamiento (utilizando Python) que se pueden realizar para el análisis de datos geo-espaciales.

</div>

<div class="cell markdown" id="ufCrSFVT27zf">

\##**Instalar Paquetes**

</div>

<div class="cell code" execution_count="2" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:10560,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719846783634,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="D7JUDqc3BqBd" outputId="fecb398e-df67-4130-9845-6ecd3c4a2dc9">

``` python
pip install mapclassify
```

<div class="output stream stdout">

    Collecting mapclassify
      Downloading mapclassify-2.6.1-py3-none-any.whl (38 kB)
    Requirement already satisfied: networkx>=2.7 in /usr/local/lib/python3.10/dist-packages (from mapclassify) (3.3)
    Requirement already satisfied: numpy>=1.23 in /usr/local/lib/python3.10/dist-packages (from mapclassify) (1.25.2)
    Requirement already satisfied: pandas!=1.5.0,>=1.4 in /usr/local/lib/python3.10/dist-packages (from mapclassify) (2.0.3)
    Requirement already satisfied: scikit-learn>=1.0 in /usr/local/lib/python3.10/dist-packages (from mapclassify) (1.2.2)
    Requirement already satisfied: scipy>=1.8 in /usr/local/lib/python3.10/dist-packages (from mapclassify) (1.11.4)
    Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas!=1.5.0,>=1.4->mapclassify) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas!=1.5.0,>=1.4->mapclassify) (2023.4)
    Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas!=1.5.0,>=1.4->mapclassify) (2024.1)
    Requirement already satisfied: joblib>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from scikit-learn>=1.0->mapclassify) (1.4.2)
    Requirement already satisfied: threadpoolctl>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from scikit-learn>=1.0->mapclassify) (3.5.0)
    Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas!=1.5.0,>=1.4->mapclassify) (1.16.0)
    Installing collected packages: mapclassify
    Successfully installed mapclassify-2.6.1

</div>

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:449014,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719847344494,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="nt6nMvJcCyrj" outputId="b45046a3-016a-471a-8651-f1cbc302a716">

``` python
pip install pyrosm
```

<div class="output stream stdout">

    Collecting pyrosm
      Downloading pyrosm-0.6.2.tar.gz (2.5 MB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 24.9 MB/s eta 0:00:00
    ents to build wheel ... etadata (pyproject.toml) ...  pyrosm)
      Downloading python_rapidjson-1.18-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 67.1 MB/s eta 0:00:00
    ent already satisfied: setuptools>=18.0 in /usr/local/lib/python3.10/dist-packages (from pyrosm) (67.7.2)
    Requirement already satisfied: geopandas>=0.12.0 in /usr/local/lib/python3.10/dist-packages (from pyrosm) (0.13.2)
    Requirement already satisfied: shapely>=2.0.1 in /usr/local/lib/python3.10/dist-packages (from pyrosm) (2.0.4)
    Collecting cykhash (from pyrosm)
      Downloading cykhash-2.0.1.tar.gz (44 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.9/44.9 kB 5.6 MB/s eta 0:00:00
    ents to build wheel ... etadata (pyproject.toml) ...  pyrosm)
      Using cached pyrobuf-0.9.3-cp310-cp310-linux_x86_64.whl
    Requirement already satisfied: fiona>=1.8.19 in /usr/local/lib/python3.10/dist-packages (from geopandas>=0.12.0->pyrosm) (1.9.6)
    Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from geopandas>=0.12.0->pyrosm) (24.1)
    Requirement already satisfied: pandas>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from geopandas>=0.12.0->pyrosm) (2.0.3)
    Requirement already satisfied: pyproj>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from geopandas>=0.12.0->pyrosm) (3.6.1)
    Requirement already satisfied: numpy<3,>=1.14 in /usr/local/lib/python3.10/dist-packages (from shapely>=2.0.1->pyrosm) (1.25.2)
    Requirement already satisfied: jinja2>=2.8 in /usr/local/lib/python3.10/dist-packages (from pyrobuf->pyrosm) (3.1.4)
    Requirement already satisfied: cython>=0.23 in /usr/local/lib/python3.10/dist-packages (from pyrobuf->pyrosm) (3.0.10)
    Requirement already satisfied: attrs>=19.2.0 in /usr/local/lib/python3.10/dist-packages (from fiona>=1.8.19->geopandas>=0.12.0->pyrosm) (23.2.0)
    Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from fiona>=1.8.19->geopandas>=0.12.0->pyrosm) (2024.6.2)
    Requirement already satisfied: click~=8.0 in /usr/local/lib/python3.10/dist-packages (from fiona>=1.8.19->geopandas>=0.12.0->pyrosm) (8.1.7)
    Requirement already satisfied: click-plugins>=1.0 in /usr/local/lib/python3.10/dist-packages (from fiona>=1.8.19->geopandas>=0.12.0->pyrosm) (1.1.1)
    Requirement already satisfied: cligj>=0.5 in /usr/local/lib/python3.10/dist-packages (from fiona>=1.8.19->geopandas>=0.12.0->pyrosm) (0.7.2)
    Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from fiona>=1.8.19->geopandas>=0.12.0->pyrosm) (1.16.0)
    Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2>=2.8->pyrobuf->pyrosm) (2.1.5)
    Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.0->geopandas>=0.12.0->pyrosm) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.0->geopandas>=0.12.0->pyrosm) (2023.4)
    Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.0->geopandas>=0.12.0->pyrosm) (2024.1)
    Building wheels for collected packages: pyrosm, cykhash
      Building wheel for pyrosm (pyproject.toml) ... : filename=pyrosm-0.6.2-cp310-cp310-linux_x86_64.whl size=7461330 sha256=db606c1c895bca538f3665ab37ea7a1e6d138f885edbb75a85072889d826b4bb
      Stored in directory: /root/.cache/pip/wheels/18/21/22/b07b96a708420e351c553188667cfd6ebc7e78a011a8708cf4
      Building wheel for cykhash (pyproject.toml) ... e=cykhash-2.0.1-cp310-cp310-linux_x86_64.whl size=3366530 sha256=4498bd3ed05daf8fbcf3045457ff9086e48bd78e2d44711c0e38ab3a18ed174c
      Stored in directory: /root/.cache/pip/wheels/ed/de/7a/4386df8e70276a0d2ec5e990db76b6c89889dc41cd627e1c14
    Successfully built pyrosm cykhash
    Installing collected packages: cykhash, python-rapidjson, pyrobuf, pyrosm
    Successfully installed cykhash-2.0.1 pyrobuf-0.9.3 pyrosm-0.6.2 python-rapidjson-1.18

</div>

</div>

<div class="cell markdown" id="YTXAiDVk3I38">

## **Importar librerías**

</div>

<div class="cell code" execution_count="4" executionInfo="{&quot;elapsed&quot;:352,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848039662,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="qSq7l3vE3hDB">

``` python
import pandas as pd
import matplotlib.pyplot as plt
```

</div>

<div class="cell code" execution_count="5" executionInfo="{&quot;elapsed&quot;:7001,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848086031,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="hkDEkND9cNqA">

``` python
import geopandas as gpd
import folium
from pyrosm import OSM, get_data
import mapclassify
```

</div>

<div class="cell markdown" id="JoCKuJKAcrZ4">

## **Datos Geoesopaciales**

Datos espaciales, datos geoespaciales, datos SIG o geodatos, son nombres de **datos numéricos** que identifican la ubicación geográfica de un objeto físico como un edificio, una calle, un pueblo, una ciudad, un país, etc. según un sistema de coordenadas geográficas.

</div>

<div class="cell markdown" id="VcO_0PhM_wcj">

## **Paso 1:** Leer la data

</div>

<div class="cell markdown" id="Eih0-XNo-mJn">

Para este laboratorio vamos a trabajar con datos geo-espaciales de la ciudad de Helsinki (Capital de Finlandia)

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:603}" executionInfo="{&quot;elapsed&quot;:1345,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848177203,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="keCWqAGJ8mYY" outputId="23df0ee8-b847-4b49-e88d-861e3af2fb38">

``` python
# Leer el archivo usando Geopandas
df = gpd.read_file("buildings.geojson")
df.head()
```

<div class="output execute_result" execution_count="6">

``` json
{"type":"dataframe","variable_name":"df"}
```

</div>

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:329,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848465357,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="4VZmEn02_bLj" outputId="afd2b4a5-2a76-4471-a140-59818c5205cf">

``` python
df.info()
```

<div class="output stream stdout">

    <class 'geopandas.geodataframe.GeoDataFrame'>
    RangeIndex: 486 entries, 0 to 485
    Data columns (total 34 columns):
     #   Column              Non-Null Count  Dtype   
    ---  ------              --------------  -----   
     0   addr:city           86 non-null     object  
     1   addr:country        57 non-null     object  
     2   addr:housenumber    88 non-null     object  
     3   addr:housename      4 non-null      object  
     4   addr:postcode       54 non-null     object  
     5   addr:street         89 non-null     object  
     6   email               2 non-null      object  
     7   name                81 non-null     object  
     8   opening_hours       8 non-null      object  
     9   operator            7 non-null      object  
     10  phone               8 non-null      object  
     11  ref                 1 non-null      object  
     12  url                 8 non-null      object  
     13  website             20 non-null     object  
     14  building            486 non-null    object  
     15  amenity             26 non-null     object  
     16  building:levels     162 non-null    object  
     17  building:material   2 non-null      object  
     18  building:min_level  4 non-null      object  
     19  height              17 non-null     object  
     20  landuse             2 non-null      object  
     21  office              5 non-null      object  
     22  shop                5 non-null      object  
     23  source              3 non-null      object  
     24  start_date          87 non-null     object  
     25  wikipedia           47 non-null     object  
     26  id                  486 non-null    int64   
     27  timestamp           486 non-null    int64   
     28  version             486 non-null    int64   
     29  tags                181 non-null    object  
     30  osm_type            486 non-null    object  
     31  internet_access     1 non-null      object  
     32  changeset           66 non-null     float64 
     33  geometry            486 non-null    geometry
    dtypes: float64(1), geometry(1), int64(3), object(29)
    memory usage: 129.2+ KB

</div>

</div>

<div class="cell markdown" id="eUU5_cCW_1DS">

## **Paso 2:** Análisis Exploratorio

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:300}" executionInfo="{&quot;elapsed&quot;:355,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848502155,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="07CDoRW2_5Gh" outputId="fd595481-b934-478b-a4b5-f19fd91c7f1d">

``` python
#Para los datos cuantitativos
df.describe()
```

<div class="output execute_result" execution_count="8">

``` json
{"summary":"{\n  \"name\": \"df\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"id\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 345428668.40283257,\n        \"min\": 486.0,\n        \"max\": 1042028875.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          140077980.7962963,\n          122869920.5,\n          486.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"timestamp\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 652775783.1743208,\n        \"min\": 486.0,\n        \"max\": 1555840214.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          1455829086.5432098,\n          1493288033.0,\n          486.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"version\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 169.4081302990349,\n        \"min\": 1.0,\n        \"max\": 486.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          4.849794238683128,\n          3.0,\n          486.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"changeset\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 23.33452377915607,\n        \"min\": 0.0,\n        \"max\": 66.0,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0.0,\n          66.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>

<div class="cell markdown" id="yKHahH2CD7DV">

De manera similar a un Pandas DataFrame, un GeoDataFrame también tiene un plot de atributos, que utiliza el atributo de geometría dentro del dataframe para dibujar un mapa:

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:448}" executionInfo="{&quot;elapsed&quot;:1145,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848558668,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Pgx4hIJ1AOnz" outputId="86514eba-d013-4998-84e4-ac8c48257835">

``` python
#Como es un data geospacial podemos dibujarla
df.plot()
```

<div class="output execute_result" execution_count="9">

    <Axes: >

</div>

<div class="output display_data">

![](022f9b780b53d6a9d02b9f14b5fbfc4de61108df.png)

</div>

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:886}" executionInfo="{&quot;elapsed&quot;:1173,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848612238,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="CWH1SCe5A9ms" outputId="8d0c7d1a-5da6-47fe-846e-0be85a0508fd">

``` python
#También podemos usar un mapa interactivo con la función explore()
df.explore()
```

<div class="output execute_result" execution_count="10">

    <folium.folium.Map at 0x7d696f8909d0>

</div>

</div>

<div class="cell markdown" id="ziOE3sKdCXwa">

## **Paso 3:** Extraer datos desde OpenStreetMap

</div>

<div class="cell markdown" id="eXhPgHKkFVS4">

OpenStreetMap (OSM) es probablemente la base de datos espaciales más conocida y utilizada del mundo. Se puede recuperar datos de OSM usando la librería `pyrosm`. Con [Pyrosm](https://pyrosm.readthedocs.io/en/latest/installation.html) se puede descargar y extraer datos fácilmente desde cualquier parte del mundo en función de archivos OSM. Con pyrosm puede extraer datos de OSM de 654 regiones del mundo (que cubren todos los países y muchas regiones urbanas; consulte los documentos para obtener más información).

</div>

<div class="cell code" execution_count="11" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:2868,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848809133,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="YsQLLiYtCm55" outputId="e1498900-cc31-45f5-953e-1fef44706ed9">

``` python
# Descargar datos para Helsinki
fp = get_data("helsinki")

# Inicializar el objeto reader OpenStreetMap (OSM) para Helsinki
osm = OSM(fp)
```

<div class="output stream stdout">

    Downloaded Protobuf data 'Helsinki.osm.pbf' (39.44 MB) to:
    '/tmp/pyrosm/Helsinki.osm.pbf'

</div>

</div>

<div class="cell markdown" id="MKV9KpgoHdX0">

OSM es una “base de datos del mundo”, por lo que contiene mucha información sobre diferentes cosas. Con pyrosm puedes extraer fácilmente información sobre:

- street networks –\> `osm.get_network()`
- buildings –\> `osm.get_buildings()`
- Points of Interest (POI) –\> `osm.get_pois()`
- landuse –\> `osm.get_landuse()`
- natural elements –\> `osm.get_natural()`
- boundaries –\> `osm.get_boundaries()`

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:51803,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848908365,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="7skOY6GpEqqM" outputId="6340e29b-31c5-4939-a5be-4766ed7d20d7">

``` python
#Get los edificios de Helkinki
buildings = osm.get_buildings()
buildings
```

<div class="output execute_result" execution_count="12">

``` json
{"type":"dataframe","variable_name":"buildings"}
```

</div>

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:334,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848939788,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="e7O_SiWJE740" outputId="548d0820-4126-42d2-9d77-d09db8b8a8dd">

``` python
len(buildings)
```

<div class="output execute_result" execution_count="13">

    163554

</div>

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:325,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719848952198,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="joBujeTO_EUS" outputId="4fbc3614-5819-42ec-f572-e79069ae92ab">

``` python
buildings.info()
```

<div class="output stream stdout">

    <class 'geopandas.geodataframe.GeoDataFrame'>
    RangeIndex: 163554 entries, 0 to 163553
    Data columns (total 40 columns):
     #   Column              Non-Null Count   Dtype   
    ---  ------              --------------   -----   
     0   addr:city           51898 non-null   object  
     1   addr:country        9207 non-null    object  
     2   addr:full           4 non-null       object  
     3   addr:housenumber    116984 non-null  object  
     4   addr:housename      612 non-null     object  
     5   addr:postcode       51437 non-null   object  
     6   addr:place          301 non-null     object  
     7   addr:street         117222 non-null  object  
     8   email               112 non-null     object  
     9   name                3809 non-null    object  
     10  opening_hours       444 non-null     object  
     11  operator            1467 non-null    object  
     12  phone               328 non-null     object  
     13  ref                 1052 non-null    object  
     14  url                 39 non-null      object  
     15  visible             163107 non-null  object  
     16  website             933 non-null     object  
     17  building            163554 non-null  object  
     18  amenity             2621 non-null    object  
     19  building:flats      14036 non-null   object  
     20  building:levels     73994 non-null   object  
     21  building:material   12855 non-null   object  
     22  building:min_level  228 non-null     object  
     23  building:use        28725 non-null   object  
     24  craft               10 non-null      object  
     25  height              1245 non-null    object  
     26  internet_access     51 non-null      object  
     27  landuse             27 non-null      object  
     28  office              102 non-null     object  
     29  shop                343 non-null     object  
     30  source              17373 non-null   object  
     31  start_date          43163 non-null   object  
     32  wikipedia           492 non-null     object  
     33  id                  163554 non-null  int64   
     34  timestamp           163554 non-null  uint32  
     35  version             163554 non-null  int32   
     36  tags                73808 non-null   object  
     37  osm_type            163554 non-null  object  
     38  geometry            163554 non-null  geometry
     39  changeset           447 non-null     float64 
    dtypes: float64(1), geometry(1), int32(1), int64(1), object(35), uint32(1)
    memory usage: 48.7+ MB

</div>

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:447}" executionInfo="{&quot;elapsed&quot;:42397,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849021811,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="FWpfoBVOE-7E" outputId="efb4d13f-401e-4632-dd9f-3d80f9960d73">

``` python
buildings.plot()
```

<div class="output execute_result" execution_count="15">

    <Axes: >

</div>

<div class="output display_data">

![](3aedfe05963c5c896ed162a3dadac231311ddaee.png)

</div>

</div>

<div class="cell markdown" id="XxLVNmLpILlF">

## **Paso 4:** Reproyectar datos

Como podemos ver en los mapas anteriores, las coordenadas en los ejes $`x`$ y $`y`$ sugieren que nuestras geometrías están representadas en grados decimales (WGS84). En muchos casos, deseas reproyectar tus datos a otro Coordinate Reference System(CRS).

</div>

<div class="cell code" execution_count="16" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:334,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849076835,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="KhGMjAezIcy5" outputId="682cd886-bd94-4740-e1a7-e8dd52c4bded">

``` python
buildings.crs
```

<div class="output execute_result" execution_count="16">

    <Geographic 2D CRS: EPSG:4326>
    Name: WGS 84
    Axis Info [ellipsoidal]:
    - Lat[north]: Geodetic latitude (degree)
    - Lon[east]: Geodetic longitude (degree)
    Area of Use:
    - name: World.
    - bounds: (-180.0, -90.0, 180.0, 90.0)
    Datum: World Geodetic System 1984 ensemble
    - Ellipsoid: WGS 84
    - Prime Meridian: Greenwich

</div>

</div>

<div class="cell markdown" id="YZTB42MnI1ss">

Como resultado, obtenemos información sobre el CRS y podemos ver que los datos están efectivamente en WGS84. También podemos ver que el código EPSG para CRS es 4326. Podemos reproyectar fácilmente nuestros datos usando un método `to_crs()`. La forma más sencilla de utilizar este método es especificar el CRS de destino como un código EPSG. Reproyectemos nuestros datos en EPSG 3067, que es el sistema de referencia de coordenadas proyectadas más utilizado en Finlandia, EUREF-FIN:

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:1244,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849185213,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Nyd2sKH7JCEt" outputId="4a72874e-b9c4-4d93-adda-dd76fc63a51e">

``` python
projected = buildings.to_crs(epsg=3067)
projected.crs
```

<div class="output execute_result" execution_count="17">

    <Projected CRS: EPSG:3067>
    Name: ETRS89 / TM35FIN(E,N)
    Axis Info [cartesian]:
    - E[east]: Easting (metre)
    - N[north]: Northing (metre)
    Area of Use:
    - name: Finland - onshore and offshore.
    - bounds: (19.08, 58.84, 31.59, 70.09)
    Coordinate Operation:
    - name: TM35FIN
    - method: Transverse Mercator
    Datum: European Terrestrial Reference System 1989 ensemble
    - Ellipsoid: GRS 1980
    - Prime Meridian: Greenwich

</div>

</div>

<div class="cell markdown" id="2jE3z36jJJGb">

Como podemos ver, ahora tenemos como resultado un CRS Proyectado. Para confirmar la diferencia, echemos un vistazo a la geometría de la primera fila en el GeoDataFrame de nuestros edificios originales y el GeoDataFrame proyectado. Para seleccionar una fila específica en los datos, podemos usar la indexación loc:

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:363,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849288818,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="SIEqMLEEJNcU" outputId="07ab8a5c-3c8d-4ebd-fbd9-d919b29f687b">

``` python
orig_geom = buildings.loc[0, "geometry"]
projected_geom = projected.loc[0, "geometry"]

print("Orig:\n", orig_geom, "\n")
print("Proj:\n", projected_geom)
```

<div class="output stream stdout">

    Orig:
     POLYGON ((24.8212890625 60.18717956542969, 24.82163429260254 60.1871223449707, 24.821828842163086 60.18709182739258, 24.821863174438477 60.18708801269531, 24.821863174438477 60.18709182739258, 24.82186508178711 60.18709945678711, 24.821922302246094 60.187095642089844, 24.821918487548828 60.187076568603516, 24.82199478149414 60.18706512451172, 24.822052001953125 60.18705749511719, 24.822471618652344 60.186988830566406, 24.822540283203125 60.18697738647461, 24.822486877441406 60.18689727783203, 24.82246208190918 60.1869010925293, 24.82244300842285 60.1869010925293, 24.822397232055664 60.1867790222168, 24.822132110595703 60.186798095703125, 24.82210922241211 60.18677520751953, 24.822084426879883 60.18675231933594, 24.822336196899414 60.18671417236328, 24.822330474853516 60.18670654296875, 24.82231330871582 60.186676025390625, 24.822303771972656 60.18666076660156, 24.822324752807617 60.1866569519043, 24.822345733642578 60.18665313720703, 24.82227897644043 60.18658447265625, 24.8222713470459 60.18658447265625, 24.82178497314453 60.18669509887695, 24.821781158447266 60.18668746948242, 24.821718215942383 60.18669128417969, 24.821720123291016 60.18669891357422, 24.82172393798828 60.18670654296875, 24.821138381958008 60.18675994873047, 24.821134567260742 60.18674850463867, 24.821073532104492 60.18675231933594, 24.821075439453125 60.18675994873047, 24.821077346801758 60.186767578125, 24.82049560546875 60.18681716918945, 24.820491790771484 60.186805725097656, 24.8204288482666 60.18680953979492, 24.820430755615234 60.18681716918945, 24.820432662963867 60.186824798583984, 24.820301055908203 60.18683624267578, 24.8203182220459 60.18688201904297, 24.820335388183594 60.1868782043457, 24.820371627807617 60.18696975708008, 24.82046890258789 60.18696212768555, 24.820472717285156 60.18696975708008, 24.820476531982422 60.186981201171875, 24.82048225402832 60.18699645996094, 24.820587158203125 60.18729019165039, 24.820615768432617 60.187339782714844, 24.820627212524414 60.18735885620117, 24.82099723815918 60.18729782104492, 24.82096290588379 60.18724822998047, 24.820955276489258 60.187232971191406, 24.821231842041016 60.18718719482422, 24.82123374938965 60.18719482421875, 24.82123565673828 60.18720245361328, 24.821292877197266 60.18720245361328, 24.8212890625 60.18717956542969)) 

    Proj:
     POLYGON ((379178.4051288579 6674250.751009551, 379197.3351398305 6674243.74889214, 379208.00926063093 6674239.995392478, 379209.8987020246 6674239.50788623, 379209.9127169722 6674239.932577282, 379210.04649441945 6674240.778469689, 379213.2049064009 6674240.249088939, 379212.9233383157 6674238.132612863, 379217.11120112345 6674236.718957369, 379220.2556036689 6674235.764891688, 379243.26789921254 6674227.352855992, 379247.03279294586 6674225.953189976, 379243.7776207354 6674217.132358954, 379242.4169049042 6674217.602403701, 379241.3594228062 6674217.637291449, 379238.3730985978 6674204.130907569, 379223.74410963 6674206.739345694, 379222.39104735025 6674204.233071027, 379220.9322346567 6674201.73028622, 379234.750941884 6674197.022804302, 379234.40567169024 6674196.18388904, 379233.3418362572 6674192.817761255, 379232.75704340386 6674191.136441988, 379233.90627024893 6674190.673371745, 379235.05549737276 6674190.210301863, 379231.1020625926 6674182.687977893, 379230.6790657032 6674182.701934218, 379204.11946245626 6674195.907790471, 379203.8799339208 6674195.065388155, 379200.40423695924 6674195.605246403, 379200.53801744245 6674196.451138461, 379200.7775466889 6674197.293540565, 379168.50893907587 6674204.310774196, 379168.2553830737 6674203.043683191, 379164.88544616086 6674203.580084404, 379165.0192347403 6674204.425975255, 379165.1530232731 6674205.271866113, 379133.0820144729 6674211.857740588, 379132.82844644994 6674210.590651899, 379129.3527718721 6674211.130577879, 379129.48656855914 6674211.976467525, 379129.6203651993 6674212.822357175, 379122.3658017857 6674214.337386081, 379123.4858351627 6674219.402246008, 379124.4235441736 6674218.946125542, 379126.7693487059 6674229.072354845, 379132.1344446501 6674228.044879792, 379132.37398829375 6674228.887277596, 379132.6275556979 6674230.154366266, 379133.0008946265 6674231.842653879, 379139.8968094382 6674264.351799969, 379141.66531191854 6674269.820405816, 379142.36990701203 6674271.922910208, 379162.66043377033 6674264.45052919, 379160.5747199351 6674258.992386935, 379160.09564852784 6674257.307587779, 379175.2607487645 6674251.705111446, 379175.3945340362 6674252.5510026775, 379175.5283192608 6674253.396893911, 379178.7007351967 6674253.2921741875, 379178.4051288579 6674250.751009551))

</div>

</div>

<div class="cell markdown" id="MDFtGhbfJVJu">

Como podemos ver las coordenadas que forman nuestro Polígono han cambiado de grados decimales a metros. Veamos qué pasa si simplemente llamamos a las geometrías:

</div>

<div class="cell code" execution_count="19" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:121}" executionInfo="{&quot;elapsed&quot;:342,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849318552,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="-TsU5SjxJUpO" outputId="12ee2e35-af18-4a07-a290-18223691f8ad">

``` python
orig_geom
```

<div class="output execute_result" execution_count="19">

![](82b156ed19f69fe47a10a540c74b3765e9496334.svg)

</div>

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:121}" executionInfo="{&quot;elapsed&quot;:367,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849323595,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="qgnq3xOGJYFy" outputId="8af22303-4628-4337-8e2d-5c129fe505e3">

``` python
projected_geom
```

<div class="output execute_result" execution_count="20">

![](8a53adcbd50f20eb1630c75dd31eae720cbe9007.svg)

</div>

</div>

<div class="cell markdown" id="ffbnsZYwJlPQ">

Se puede ver fácilmente la diferencia en la forma de las dos geometrías. Las variables `orig_geom` y `projected_geom` contienen una geometría Shapely que es `Polygon` en este caso. Podemos confirmar esto comprobando el tipo:

</div>

<div class="cell code" execution_count="21" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:323,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849360308,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="B3mctjEfJyD0" outputId="1165dd3c-fb78-43b4-cdf2-1abb19f5c4ac">

``` python
type(orig_geom)
```

<div class="output execute_result" execution_count="21">

    shapely.geometry.polygon.Polygon

</div>

</div>

<div class="cell markdown" id="ldLpBOwgJ28C">

## **Paso 5:** Calcular el área

Se puede calcular el área de las geometrías

</div>

<div class="cell code" execution_count="22" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:352,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849370169,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="vj9H80BRKBOb" outputId="18889161-640b-4304-b76c-89a9737ea62c">

``` python
projected["building_area"] = projected.area
projected["building_area"].describe()
```

<div class="output execute_result" execution_count="22">

    count    163554.000000
    mean        285.943613
    std         936.377117
    min           0.000000
    25%          65.546590
    50%         141.169011
    75%         258.873781
    max       84216.701096
    Name: building_area, dtype: float64

</div>

</div>

<div class="cell markdown" id="6JmaOk1_KNeQ">

## **Paso 6:** Spatial Join

Una funcionalidad SIG comúnmente necesaria es poder fusionar información entre dos capas utilizando la ubicación como clave. Por lo tanto, es un enfoque algo similar a la unión de tablas, pero debido a que la operación se basa en geometrías, se llama unión espacial.

A continuación, leeremos todos los restaurantes de OSM para la región de Helsinki y combinaremos la data de los restaurantes con el edificio subyacente (los restaurantes normalmente se encuentran dentro de los edificios). Usaremos nuevamente pyrosm para leer los datos, pero esta vez usaremos la función `get_pois()`.

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:408}" executionInfo="{&quot;elapsed&quot;:2184,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849505336,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="llNXsNFxKrty" outputId="c9340be0-4afe-4a98-eefb-678bf564741a">

``` python
# Leer Points of Interest (POI) usando el mismo OSM reader object que inicializamos antes
restaurants = osm.get_pois(custom_filter={"amenity": ["restaurant"]})
restaurants.plot()
```

<div class="output execute_result" execution_count="23">

    <Axes: >

</div>

<div class="output display_data">

![](8c44fbc6103d75d80f20902a8c520bb0cf6e8c0d.png)

</div>

</div>

<div class="cell code" execution_count="24" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:324,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849537090,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Xn_LbhCyLBse" outputId="005bcf12-435e-49ba-d1b3-b1fe8a8bb075">

``` python
restaurants.info()
```

<div class="output stream stdout">

    <class 'geopandas.geodataframe.GeoDataFrame'>
    RangeIndex: 1641 entries, 0 to 1640
    Data columns (total 38 columns):
     #   Column            Non-Null Count  Dtype   
    ---  ------            --------------  -----   
     0   changeset         1566 non-null   float64 
     1   lat               1563 non-null   float32 
     2   lon               1563 non-null   float32 
     3   version           1641 non-null   int32   
     4   timestamp         1641 non-null   uint32  
     5   id                1641 non-null   int64   
     6   tags              1540 non-null   object  
     7   visible           1638 non-null   object  
     8   addr:city         1096 non-null   object  
     9   addr:country      358 non-null    object  
     10  addr:housenumber  1197 non-null   object  
     11  addr:housename    111 non-null    object  
     12  addr:postcode     1065 non-null   object  
     13  addr:place        5 non-null      object  
     14  addr:street       1224 non-null   object  
     15  email             213 non-null    object  
     16  name              1621 non-null   object  
     17  opening_hours     1009 non-null   object  
     18  operator          72 non-null     object  
     19  phone             613 non-null    object  
     20  ref               2 non-null      object  
     21  url               26 non-null     object  
     22  website           1007 non-null   object  
     23  amenity           1641 non-null   object  
     24  bar               17 non-null     object  
     25  cafe              1 non-null      object  
     26  drinking_water    1 non-null      object  
     27  internet_access   15 non-null     object  
     28  office            3 non-null      object  
     29  pub               2 non-null      object  
     30  restaurant        1 non-null      object  
     31  source            49 non-null     object  
     32  start_date        34 non-null     object  
     33  wikipedia         16 non-null     object  
     34  geometry          1641 non-null   geometry
     35  osm_type          1641 non-null   object  
     36  building          45 non-null     object  
     37  building:levels   14 non-null     object  
    dtypes: float32(2), float64(1), geometry(1), int32(1), int64(1), object(31), uint32(1)
    memory usage: 461.7+ KB

</div>

</div>

<div class="cell markdown" id="hFCVmBWSLLpd">

Unir los datos de buildings a restaurantes

</div>

<div class="cell code" execution_count="25" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:819}" executionInfo="{&quot;elapsed&quot;:950,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849577146,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="uKVynK76LQvx" outputId="f6d974fa-9a4a-40de-ead5-a47e8922d4d4">

``` python
# Unir info desde edificios a restaurantes
join = gpd.sjoin(restaurants, buildings)

# Imprimir nombre de columnas
print(join.columns)

# Mostrar filas
join
```

<div class="output stream stdout">

    Index(['changeset_left', 'lat', 'lon', 'version_left', 'timestamp_left',
           'id_left', 'tags_left', 'visible_left', 'addr:city_left',
           'addr:country_left', 'addr:housenumber_left', 'addr:housename_left',
           'addr:postcode_left', 'addr:place_left', 'addr:street_left',
           'email_left', 'name_left', 'opening_hours_left', 'operator_left',
           'phone_left', 'ref_left', 'url_left', 'website_left', 'amenity_left',
           'bar', 'cafe', 'drinking_water', 'internet_access_left', 'office_left',
           'pub', 'restaurant', 'source_left', 'start_date_left', 'wikipedia_left',
           'geometry', 'osm_type_left', 'building_left', 'building:levels_left',
           'index_right', 'addr:city_right', 'addr:country_right', 'addr:full',
           'addr:housenumber_right', 'addr:housename_right', 'addr:postcode_right',
           'addr:place_right', 'addr:street_right', 'email_right', 'name_right',
           'opening_hours_right', 'operator_right', 'phone_right', 'ref_right',
           'url_right', 'visible_right', 'website_right', 'building_right',
           'amenity_right', 'building:flats', 'building:levels_right',
           'building:material', 'building:min_level', 'building:use', 'craft',
           'height', 'internet_access_right', 'landuse', 'office_right', 'shop',
           'source_right', 'start_date_right', 'wikipedia_right', 'id_right',
           'timestamp_right', 'version_right', 'tags_right', 'osm_type_right',
           'changeset_right'],
          dtype='object')

</div>

<div class="output execute_result" execution_count="25">

``` json
{"type":"dataframe","variable_name":"join"}
```

</div>

</div>

<div class="cell code" execution_count="26" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:408}" executionInfo="{&quot;elapsed&quot;:949,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849587784,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="BGwzBECdLeWl" outputId="db581227-57ff-43e2-fb33-76c04802dad9">

``` python
#Visualizar los datos
join.plot()
```

<div class="output execute_result" execution_count="26">

    <Axes: >

</div>

<div class="output display_data">

![](72dfe35b98fbd290addb8f6f913082e0f8e58399.png)

</div>

</div>

<div class="cell markdown" id="0e29Jw7TLvRJ">

Un truco útil y eficaz para la unión espacial es utilizarla para seleccionar datos. Podemos, por ejemplo. seleccione todos los edificios que se cruzan con restaurantes realizando la unión espacial al revés, es decir, usando los edificios como el GeoDataFrame izquierdo y los restaurantes como el GeoDataFrame derecho:

</div>

<div class="cell code" execution_count="27" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:464}" executionInfo="{&quot;elapsed&quot;:1275,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849614042,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="fiupfuqRLuk2" outputId="5a8a0433-f27f-4d4e-9106-df1e0283a9ad">

``` python
# Merge information from restaurants to buildings (conducts selection at the same time)
join2 = gpd.sjoin(buildings, restaurants, how="inner", op="intersects")
join2.plot()
```

<div class="output stream stderr">

    /usr/local/lib/python3.10/dist-packages/IPython/core/interactiveshell.py:3473: FutureWarning: The `op` parameter is deprecated and will be removed in a future release. Please use the `predicate` parameter instead.
      if (await self.run_code(code, result,  async_=asy)):

</div>

<div class="output execute_result" execution_count="27">

    <Axes: >

</div>

<div class="output display_data">

![](33847b365b94b8f3d68dbf1fcb26315599b34280.png)

</div>

</div>

<div class="cell markdown" id="BtCK2XfNL7r6">

Como podemos ver (aunque las geometrías de los edificios pequeños son un poco poco visibles), el resultado final es una capa de edificios que se cruzan con los restaurantes.

</div>

<div class="cell markdown" id="sIrsFoBdMDDA">

## **Paso 7:** Plotting data con Matplotlib

Hasta ahora, no hemos hecho ningún esfuerzo para que nuestros mapas sean visualmente atractivos. A continuación veamos cómo podemos ajustar la apariencia de nuestro mapa y cómo podemos visualizar muchas capas una encima de la otra. Comencemos visualizando los edificios que seleccionamos anteriormente y ajustemos un poco los colores y el tamaño de las figuras. Podemos ajustar el color de los polígonos con el parámetro `facecolor` y el tamaño de la figura con el parámetro `figsize` que acepta una tupla de ancho y alto como argumento:

</div>

<div class="cell code" execution_count="28" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:678}" executionInfo="{&quot;elapsed&quot;:937,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849669471,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mwliJl5CMCet" outputId="b3680d85-1653-4134-a261-0f4709459d3e">

``` python
ax = join2.plot(facecolor="red", figsize=(12,12))
```

<div class="output display_data">

![](3bf061e95abd241478b126d1a088e48d1fd47cee.png)

</div>

</div>

<div class="cell code" execution_count="29" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:334,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849699401,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="MIdZZeelMY3y" outputId="25e2e095-73f2-46c6-d1cf-3d6f33d3b6b5">

``` python
join2.columns
```

<div class="output execute_result" execution_count="29">

    Index(['addr:city_left', 'addr:country_left', 'addr:full',
           'addr:housenumber_left', 'addr:housename_left', 'addr:postcode_left',
           'addr:place_left', 'addr:street_left', 'email_left', 'name_left',
           'opening_hours_left', 'operator_left', 'phone_left', 'ref_left',
           'url_left', 'visible_left', 'website_left', 'building_left',
           'amenity_left', 'building:flats', 'building:levels_left',
           'building:material', 'building:min_level', 'building:use', 'craft',
           'height', 'internet_access_left', 'landuse', 'office_left', 'shop',
           'source_left', 'start_date_left', 'wikipedia_left', 'id_left',
           'timestamp_left', 'version_left', 'tags_left', 'osm_type_left',
           'geometry', 'changeset_left', 'index_right', 'changeset_right', 'lat',
           'lon', 'version_right', 'timestamp_right', 'id_right', 'tags_right',
           'visible_right', 'addr:city_right', 'addr:country_right',
           'addr:housenumber_right', 'addr:housename_right', 'addr:postcode_right',
           'addr:place_right', 'addr:street_right', 'email_right', 'name_right',
           'opening_hours_right', 'operator_right', 'phone_right', 'ref_right',
           'url_right', 'website_right', 'amenity_right', 'bar', 'cafe',
           'drinking_water', 'internet_access_right', 'office_right', 'pub',
           'restaurant', 'source_right', 'start_date_right', 'wikipedia_right',
           'osm_type_right', 'building_right', 'building:levels_right'],
          dtype='object')

</div>

</div>

<div class="cell markdown" id="ou_7NI5XMfub">

Coloreemos nuestros edificios según el tipo de edificio. Por lo tanto, cada categoría de tipo de edificio recibirá un color diferente.

Usamos el parámetro `column` para especificar el atributo que se usa para colorear cada edificio (puede ser categórico o continuo). Usamos `cmap` para especificar el mapa de colores y agregamos la leyenda especificando `legend=True`.

</div>

<div class="cell code" execution_count="30" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:823}" executionInfo="{&quot;elapsed&quot;:1851,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849729430,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="-mGIsY_ZkPXM" outputId="7fe4efc3-d7b2-4708-bd83-85da62a2e8ed">

``` python
ax = join2.plot(column="building_left", cmap="RdYlBu", figsize=(12,12), legend=True)
```

<div class="output display_data">

![](43beb768322b28f990975b35c2387a4693176f30.png)

</div>

</div>

<div class="cell markdown" id="ruCE5a-hk3Gd">

Para una mejor visualización se puede hacer zoom in al mapa usando `set_xlim()` y `set_ylim()`

</div>

<div class="cell code" execution_count="31" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:1000}" executionInfo="{&quot;elapsed&quot;:1983,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849772155,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="1VcuLkvXk3Od" outputId="fa31b8e7-5077-49ce-b132-9c156d6d363b">

``` python
# Zoom into city center by specifying X and Y coordinate extent
# These values should be given in the units that our data is presented (here decimal degrees)
xmin, xmax = 24.92, 24.98
ymin, ymax = 60.15, 60.18

# Plot the map again
ax = join2.plot(column="building_left", cmap="RdYlBu", figsize=(12,12), legend=True)

# Control and set the x and y limits for the axis
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
```

<div class="output execute_result" execution_count="31">

    (60.15, 60.18)

</div>

<div class="output display_data">

![](27bf61d30d492ff7a20975c147e8612582ccf505.png)

</div>

</div>

<div class="cell markdown" id="3ZxNgPFQlMNB">

También usando OSM se puede obtener las calles

</div>

<div class="cell code" execution_count="32" executionInfo="{&quot;elapsed&quot;:31108,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849866758,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="MK4LISorlQE3">

``` python
#Obtener las calles
roads = osm.get_network()
```

</div>

<div class="cell markdown" id="2Vdq4A6hlUnN">

Ahora podemos continuar y agregar las calles como una capa a nuestra visualización con color de línea gris:

</div>

<div class="cell code" execution_count="33" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:990}" executionInfo="{&quot;elapsed&quot;:61417,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719849947059,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="SS1q159OlibU" outputId="a9780a23-e022-4ecf-fa7b-9ef3e665bdf2">

``` python
# Zoom into city center by specifying X and Y coordinate extent
# These values should be given in the units that our data is presented (here decimal degrees)
xmin, xmax = 24.92, 24.98
ymin, ymax = 60.15, 60.18

# Plot the map again
ax = join2.plot(column="building_left", cmap="RdYlBu", figsize=(12,12), legend=True)

# Plot the roads into the same axis
ax = roads.plot(ax=ax, edgecolor="gray", linewidth=0.75)

# Control and set the x and y limits for the axis
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])

plt.show()
```

<div class="output display_data">

![](2eabc9304e6ff885d3ae1360c3193e0608f3e00d.png)

</div>

</div>
