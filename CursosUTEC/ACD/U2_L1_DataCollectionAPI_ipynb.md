---
curso: ACD
titulo: U2_L1 DataCollectionAPI
slides: 0
fuente: U2_L1 DataCollectionAPI.ipynb
---

<div class="cell markdown" id="lC8u2MoaOaZs">

# **U2_L1: Data Collection via API**

**Objetivo:** Entender como usar una web API para recolectar datos.

</div>

<div class="cell markdown" id="AzV9HYd8O7hQ">

### **Paso 0:** Cargar líbrerias

</div>

<div class="cell code" execution_count="1" id="c2cJlDMsOS2c">

``` python
import requests
import json
import pandas as pd
```

</div>

<div class="cell markdown" id="pz0BhuCvPLSn">

## **Ejercicio 1**

***Random User Generator API:*** Es una gran herramienta para [generar datos de usuarios aleatorios](https://randomuser.me/). Puede usarlo para generar cualquier cantidad de usuarios aleatorios y datos asociados, y también puede especificar el género, la nacionalidad y muchos otros filtros que pueden ser realmente útiles al probar aplicaciones o, en este caso, API.

</div>

<div class="cell markdown" id="4L0stwdDgknO">

### **Paso 1:** Recolectar datos desde un Web API

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:977,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714938783697,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="zV5Fafjlgn2_" outputId="1053f643-b573-4ed3-bd20-991ef1d93d46">

``` python
#Hacemos el request al servidor
url = "https://randomuser.me/api/"
response = requests.get(url)
response
```

<div class="output execute_result" execution_count="3">

    <Response [200]>

</div>

</div>

<div class="cell markdown" id="hb3bykJuh4BF">

Información del objeto `Response`:

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:408,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714938788839,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="HH8tYFdLiB30" outputId="36c3359d-5614-4c26-ff57-72af0ab10e72">

``` python
#Revisar status code
response.status_code
```

<div class="output execute_result" execution_count="4">

    200

</div>

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:3,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714938791700,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="_b5vF58-iPE9" outputId="862bcaf3-63f1-4ba1-c25a-250ab966495c">

``` python
#Revisar HTTP headers
response.headers
```

<div class="output execute_result" execution_count="5">

    {'Date': 'Sun, 13 Apr 2025 23:08:44 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*', 'Cache-Control': 'no-cache', 'ETag': 'W/"490-hOkuvdrHHAs7SZc5PnuuGBbaheM"', 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'cf-cache-status': 'DYNAMIC', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v4?s=YW9De7HAYcyj%2BjCmIYRxmd3K9ojdhBlq0co6BjiM96FCNb0rb7E0nyLP0jd6E%2FArt5IxU5BEka3zI1oZ9A1ij1yVyuqmogUGapJscjF7RevIahndF0Xu2f09FsHjbwPg"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Server': 'cloudflare', 'CF-RAY': '92fea08729def0e0-LAX', 'alt-svc': 'h3=":443"; ma=86400', 'server-timing': 'cfL4;desc="?proto=TCP&rtt=161228&min_rtt=159017&rtt_var=48634&sent=5&recv=6&lost=0&retrans=0&sent_bytes=2846&recv_bytes=777&delivery_rate=24986&cwnd=170&unsent_bytes=0&cid=f26ca54bacb18a49&ts=262&x=0"'}

</div>

</div>

<div class="cell markdown" id="_26hFD6vilDc">

Para visualizar el contenido (los datos)

- `.text` Retorna la respuesta en formato Unicode (sistema de codificación de caracteres que permite que computadoras almacenen y intercambien datos de texto)
- `.content` Retorna la respuesta en bytes

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:161}" executionInfo="{&quot;elapsed&quot;:304,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714938795540,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="7hhdoEboikLL" outputId="23f33543-d9b9-4d7a-c33c-b356a927ef9d">

``` python
response.text
```

<div class="output execute_result" execution_count="6">

    '{"results":[{"gender":"male","name":{"title":"Mr","first":"Joël","last":"Tammer"},"location":{"street":{"number":4594,"name":"Korte Herreweg"},"city":"Landerum","state":"Noord-Holland","country":"Netherlands","postcode":"4923 LK","coordinates":{"latitude":"36.5941","longitude":"-4.7575"},"timezone":{"offset":"+4:00","description":"Abu Dhabi, Muscat, Baku, Tbilisi"}},"email":"joel.tammer@example.com","login":{"uuid":"7aa7f7a3-d718-48dc-817d-7a283654ac36","username":"lazyswan515","password":"allsop","salt":"YChIG1Vs","md5":"d6d0e8282247e0e3014e2b29d79e6d53","sha1":"a868bc146f89b72a2d90da6e2fcea7577d1de493","sha256":"da2a06d304deba3d96b8e7ccf954a405f88eab328df4254aa146c95df318c77b"},"dob":{"date":"1982-01-03T01:57:37.079Z","age":43},"registered":{"date":"2005-10-04T14:42:18.452Z","age":19},"phone":"(0467) 142790","cell":"(06) 72236242","id":{"name":"BSN","value":"75217505"},"picture":{"large":"https://randomuser.me/api/portraits/men/55.jpg","medium":"https://randomuser.me/api/portraits/med/men/55.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/55.jpg"},"nat":"NL"}],"info":{"seed":"2af098aa64646402","results":1,"page":1,"version":"1.4"}}'

</div>

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:1,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714938797788,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="JQ9VAhmIii7Q" outputId="fa92452f-6d90-4e7e-ea6f-08336ae45c62">

``` python
response.content
```

<div class="output execute_result" execution_count="7">

    b'{"results":[{"gender":"male","name":{"title":"Mr","first":"Jo\xc3\xabl","last":"Tammer"},"location":{"street":{"number":4594,"name":"Korte Herreweg"},"city":"Landerum","state":"Noord-Holland","country":"Netherlands","postcode":"4923 LK","coordinates":{"latitude":"36.5941","longitude":"-4.7575"},"timezone":{"offset":"+4:00","description":"Abu Dhabi, Muscat, Baku, Tbilisi"}},"email":"joel.tammer@example.com","login":{"uuid":"7aa7f7a3-d718-48dc-817d-7a283654ac36","username":"lazyswan515","password":"allsop","salt":"YChIG1Vs","md5":"d6d0e8282247e0e3014e2b29d79e6d53","sha1":"a868bc146f89b72a2d90da6e2fcea7577d1de493","sha256":"da2a06d304deba3d96b8e7ccf954a405f88eab328df4254aa146c95df318c77b"},"dob":{"date":"1982-01-03T01:57:37.079Z","age":43},"registered":{"date":"2005-10-04T14:42:18.452Z","age":19},"phone":"(0467) 142790","cell":"(06) 72236242","id":{"name":"BSN","value":"75217505"},"picture":{"large":"https://randomuser.me/api/portraits/men/55.jpg","medium":"https://randomuser.me/api/portraits/med/men/55.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/55.jpg"},"nat":"NL"}],"info":{"seed":"2af098aa64646402","results":1,"page":1,"version":"1.4"}}'

</div>

</div>

<div class="cell markdown" id="BexYABGyi2JC">

### **Paso 2:** Decodificar un JSON data

Dado que el contenido es de formato JSON, podemos usar la función `.json()` que convierte la respuesta del API (bytes) en una estructura de datos Python (dictionario)

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:289,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714938801689,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="glMhkjf4i5rl" outputId="6573a8ce-d04a-4c7c-912f-8584610e0bb6">

``` python
#Visualizar JSON format
data = response.json()
data
```

<div class="output execute_result" execution_count="8">

    {'results': [{'gender': 'male',
       'name': {'title': 'Mr', 'first': 'Joël', 'last': 'Tammer'},
       'location': {'street': {'number': 4594, 'name': 'Korte Herreweg'},
        'city': 'Landerum',
        'state': 'Noord-Holland',
        'country': 'Netherlands',
        'postcode': '4923 LK',
        'coordinates': {'latitude': '36.5941', 'longitude': '-4.7575'},
        'timezone': {'offset': '+4:00',
         'description': 'Abu Dhabi, Muscat, Baku, Tbilisi'}},
       'email': 'joel.tammer@example.com',
       'login': {'uuid': '7aa7f7a3-d718-48dc-817d-7a283654ac36',
        'username': 'lazyswan515',
        'password': 'allsop',
        'salt': 'YChIG1Vs',
        'md5': 'd6d0e8282247e0e3014e2b29d79e6d53',
        'sha1': 'a868bc146f89b72a2d90da6e2fcea7577d1de493',
        'sha256': 'da2a06d304deba3d96b8e7ccf954a405f88eab328df4254aa146c95df318c77b'},
       'dob': {'date': '1982-01-03T01:57:37.079Z', 'age': 43},
       'registered': {'date': '2005-10-04T14:42:18.452Z', 'age': 19},
       'phone': '(0467) 142790',
       'cell': '(06) 72236242',
       'id': {'name': 'BSN', 'value': '75217505'},
       'picture': {'large': 'https://randomuser.me/api/portraits/men/55.jpg',
        'medium': 'https://randomuser.me/api/portraits/med/men/55.jpg',
        'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/55.jpg'},
       'nat': 'NL'}],
     'info': {'seed': '2af098aa64646402',
      'results': 1,
      'page': 1,
      'version': '1.4'}}

</div>

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:288,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714938804743,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="DlVnIbfdjISv" outputId="6a046ad9-8068-4339-b045-9ebea639779e">

``` python
#Revisamos keys del dict
data.keys()
```

<div class="output execute_result" execution_count="9">

    dict_keys(['results', 'info'])

</div>

</div>

<div class="cell markdown" id="0TDnGTeQjZJy">

### **Paso 3:** Generamos un dataframe a partir del json

Para ello usamos de la librería de Pandas la función `json_normalize()` que normaliza los datos JSON semiestructurados en un dataframe.

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:165}" executionInfo="{&quot;elapsed&quot;:300,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714938808836,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="hMzuNcKTjq9U" outputId="e2c0b00e-a43f-4d2a-831b-d32b08821ad0">

``` python
#Recibe el key que convertira a dataframe
df = pd.json_normalize(data,'results')
df
```

<div class="output execute_result" execution_count="10">

      gender                    email          phone           cell nat  \
    0   male  joel.tammer@example.com  (0467) 142790  (06) 72236242  NL   

      name.title name.first name.last  location.street.number  \
    0         Mr       Joël    Tammer                    4594   

      location.street.name  ...  \
    0       Korte Herreweg  ...   

                                            login.sha256  \
    0  da2a06d304deba3d96b8e7ccf954a405f88eab328df425...   

                       dob.date dob.age           registered.date registered.age  \
    0  1982-01-03T01:57:37.079Z      43  2005-10-04T14:42:18.452Z             19   

      id.name  id.value                                   picture.large  \
    0     BSN  75217505  https://randomuser.me/api/portraits/men/55.jpg   

                                          picture.medium  \
    0  https://randomuser.me/api/portraits/med/men/55...   

                                       picture.thumbnail  
    0  https://randomuser.me/api/portraits/thumb/men/...  

    [1 rows x 34 columns]

</div>

</div>

<div class="cell markdown" id="gxaq1eLvhuhz">

## **Ejercicio 2**

En base al ejercicio anterior generemos un dataset de $`n`$ personas. Para eso generemos una función `get_dfN(n)`que reciba el número de request a la web API y retorne un dataframe.

HINT: Utilicemos ? dentro de la url

</div>

<div class="cell code" execution_count="11" id="oUV8XjQdWc0Y">

``` python
#TO DO
def get_dfN(n):
  url = "https://randomuser.me/api/?results=" + str(n)
  response = requests.get(url)
  data = response.json()
  df = pd.json_normalize(data,'results')
  return df
```

</div>

<div class="cell code" execution_count="16">

``` python
get_dfN(100)
```

<div class="output execute_result" execution_count="16">

        gender                         email         phone           cell nat  \
    0     male    floyd.stephens@example.com  011-121-5220   081-213-2699  IE   
    1   female      kelly.gordon@example.com  00-2746-2555   0455-623-422  AU   
    2     male  anthony.tremblay@example.com  D12 D37-7391   C70 F21-7461  CA   
    3     male      eino.lehtola@example.com    07-397-878  049-529-09-20  FI   
    4   female  liliana.tandstad@example.com      81218257       97765232  NO   
    ..     ...                           ...           ...            ...  ..   
    95  female  isabella.poulsen@example.com      17586722       69926536  DK   
    96    male   johan.mortensen@example.com      21765412       46666277  DK   
    97    male  frederick.watson@example.com  015396 87598   07957 401168  GB   
    98  female         jeanne.ma@example.com  X50 T73-1156   Q22 P44-2406  CA   
    99    male      nolan.clarke@example.com  01222 934071   07658 175497  GB   

       name.title name.first  name.last  location.street.number  \
    0          Mr      Floyd   Stephens                    2669   
    1        Miss      Kelly     Gordon                    4575   
    2          Mr    Anthony   Tremblay                    9877   
    3          Mr       Eino    Lehtola                    1348   
    4        Miss    Liliana   Tandstad                    5988   
    ..        ...        ...        ...                     ...   
    95        Mrs   Isabella    Poulsen                    2459   
    96         Mr      Johan  Mortensen                    9169   
    97         Mr  Frederick     Watson                    6972   
    98         Ms     Jeanne         Ma                    9811   
    99         Mr      Nolan     Clarke                    5848   

       location.street.name  ...  \
    0           Tara Street  ...   
    1           Robinson Rd  ...   
    2              Cedar St  ...   
    3         Fredrikinkatu  ...   
    4          Falsens gate  ...   
    ..                  ...  ...   
    95           Røllikevej  ...   
    96          Bekkasinvej  ...   
    97        Richmond Road  ...   
    98              Park Rd  ...   
    99          Church Road  ...   

                                             login.sha256  \
    0   8ecb09c0df2b0d933c2142b121ffd5c0ec9a7d08ca508f...   
    1   1636a529e49f8b9d346aaa6e05093811a53fd5599cbb33...   
    2   0b429d47092a484cf62e67e5a4a7479e8fea7bcd72bfc9...   
    3   d33b65b83f6c23571bfffd2e6f98edfbefa409b7d598ca...   
    4   e0caaea01d45bbaa95f45ecc2e0ce8f4577a796fda0153...   
    ..                                                ...   
    95  169faa3bcc1bcd0d851a36e7012901da16b1d3738def72...   
    96  9ecea887496d0d0a9047c172e9c21190d6d45818a3475a...   
    97  70fa54e2a4bdfec8837366f6e9b2e5b62ffc1913905403...   
    98  e89f263f862a7d797060ecfcbdd45d057b8b3ab57ac1ae...   
    99  33f43f6b5bc7da4705ef3493be5c3dbe54718bd2e7b1d2...   

                        dob.date dob.age           registered.date registered.age  \
    0   1945-06-29T19:24:57.191Z      79  2019-02-07T11:46:15.999Z              6   
    1   1994-02-25T12:32:54.312Z      31  2009-08-01T20:53:01.123Z             15   
    2   1984-04-10T19:11:13.001Z      41  2007-06-11T00:55:39.980Z             17   
    3   1961-05-05T16:04:31.826Z      63  2004-03-09T06:30:30.968Z             21   
    4   1947-06-26T06:16:30.949Z      77  2009-05-16T08:09:22.730Z             15   
    ..                       ...     ...                       ...            ...   
    95  1977-11-14T13:17:24.943Z      47  2012-04-17T15:59:42.602Z             12   
    96  1954-11-14T08:54:38.236Z      70  2017-07-28T14:56:55.998Z              7   
    97  1989-08-21T08:51:02.836Z      35  2007-08-24T13:17:04.118Z             17   
    98  1981-06-30T07:30:01.690Z      43  2003-04-16T13:08:30.913Z             21   
    99  1985-07-31T01:21:18.737Z      39  2008-01-27T22:16:15.336Z             17   

       id.name           id.value  \
    0      PPS           0665361T   
    1      TFN          150321346   
    2      SIN          150225043   
    3     HETU  NaNNA305undefined   
    4       FN        26064747842   
    ..     ...                ...   
    95     CPR        141177-1792   
    96     CPR        141154-7264   
    97    NINO      GA 05 01 33 Q   
    98     SIN          806983003   
    99    NINO      SC 63 72 15 O   

                                           picture.large  \
    0     https://randomuser.me/api/portraits/men/12.jpg   
    1   https://randomuser.me/api/portraits/women/43.jpg   
    2     https://randomuser.me/api/portraits/men/88.jpg   
    3     https://randomuser.me/api/portraits/men/84.jpg   
    4   https://randomuser.me/api/portraits/women/95.jpg   
    ..                                               ...   
    95  https://randomuser.me/api/portraits/women/24.jpg   
    96    https://randomuser.me/api/portraits/men/77.jpg   
    97    https://randomuser.me/api/portraits/men/30.jpg   
    98  https://randomuser.me/api/portraits/women/57.jpg   
    99    https://randomuser.me/api/portraits/men/13.jpg   

                                           picture.medium  \
    0   https://randomuser.me/api/portraits/med/men/12...   
    1   https://randomuser.me/api/portraits/med/women/...   
    2   https://randomuser.me/api/portraits/med/men/88...   
    3   https://randomuser.me/api/portraits/med/men/84...   
    4   https://randomuser.me/api/portraits/med/women/...   
    ..                                                ...   
    95  https://randomuser.me/api/portraits/med/women/...   
    96  https://randomuser.me/api/portraits/med/men/77...   
    97  https://randomuser.me/api/portraits/med/men/30...   
    98  https://randomuser.me/api/portraits/med/women/...   
    99  https://randomuser.me/api/portraits/med/men/13...   

                                        picture.thumbnail  
    0   https://randomuser.me/api/portraits/thumb/men/...  
    1   https://randomuser.me/api/portraits/thumb/wome...  
    2   https://randomuser.me/api/portraits/thumb/men/...  
    3   https://randomuser.me/api/portraits/thumb/men/...  
    4   https://randomuser.me/api/portraits/thumb/wome...  
    ..                                                ...  
    95  https://randomuser.me/api/portraits/thumb/wome...  
    96  https://randomuser.me/api/portraits/thumb/men/...  
    97  https://randomuser.me/api/portraits/thumb/men/...  
    98  https://randomuser.me/api/portraits/thumb/wome...  
    99  https://randomuser.me/api/portraits/thumb/men/...  

    [100 rows x 34 columns]

</div>

</div>

<div class="cell markdown" id="Ndio9DrLjLpM">

**Guardar el nuevo dataset**

</div>

<div class="cell code" execution_count="25">

``` python
pd.set_option('display.max_columns', None)
df = get_dfN(100)
df
```

<div class="output execute_result" execution_count="25">

        gender                             email           phone            cell  \
    0   female      tonkostana.zagul@example.com  (097) W95-8635  (098) Z61-1786   
    1     male           angel.doyle@example.com    031-696-6361    081-183-7995   
    2     male        santiago.armas@example.com  (663) 033 4608  (671) 177 8027   
    3     male  soncedar.kozhelyanko@example.com  (068) O26-8875  (097) A56-5646   
    4     male             hmd.khmrw@example.com    077-56786092   0962-080-9914   
    ..     ...                               ...             ...             ...   
    95  female         adrianne.paus@example.com   (0404) 092974   (06) 05206605   
    96    male            aatu.lauri@example.com      05-530-322   046-468-74-84   
    97    male           jon.roberts@example.com    07-9791-0343    0457-789-588   
    98  female           iiris.pulli@example.com      05-902-258   046-862-28-74   
    99    male        camilo.peralta@example.com  (693) 040 9635  (625) 134 0109   

       nat name.title  name.first    name.last  location.street.number  \
    0   UA         Ms  Tonkostana        Zagul                    6332   
    1   IE         Mr       Angel        Doyle                    8769   
    2   MX         Mr    Santiago        Armas                    5751   
    3   UA         Mr    Soncedar  Kozhelyanko                    4744   
    4   IR         Mr        حامد       کامروا                    2271   
    ..  ..        ...         ...          ...                     ...   
    95  NL        Mrs    Adrianne         Paus                    5064   
    96  FI         Mr        Aatu        Lauri                    1557   
    97  AU         Mr         Jon      Roberts                    8612   
    98  FI       Miss       Iiris        Pulli                     965   
    99  MX         Mr      Camilo      Peralta                    4102   

         location.street.name     location.city location.state location.country  \
    0        Voyiniv-afganciv           Popasna      Rivnenska          Ukraine   
    1             Dame Street           Dundalk        Wexford          Ireland   
    2       Retorno Chihuahua        Bellavista   Quintana Roo           Mexico   
    3              Perekopska          Mariupol       Kiyivska          Ukraine   
    4            میدان انقلاب               آمل          تهران             Iran   
    ..                    ...               ...            ...              ...   
    95   Groot Kraaivenstraat            Lieren  Noord-Brabant      Netherlands   
    96            Pyynikintie          Ylöjärvi    Päijät-Häme          Finland   
    97         Pecan Acres Ln          Bathurst       Tasmania        Australia   
    98      Itsenäisyydenkatu           Paltamo        Lapland          Finland   
    99  Ampliación Sur Zapata  Vicente Guerrero        Yucatan           Mexico   

       location.postcode location.coordinates.latitude  \
    0              33085                       81.1766   
    1              19385                       15.9932   
    2              33397                       12.2154   
    3              50850                        8.7822   
    4              98088                      -79.2273   
    ..               ...                           ...   
    95           2206 YI                        4.7818   
    96             10220                       70.0837   
    97              6516                      -24.1772   
    98             69028                       57.1958   
    99             29818                       43.1354   

       location.coordinates.longitude location.timezone.offset  \
    0                         79.1881                   -10:00   
    1                        103.2168                    -3:30   
    2                        -64.5830                    +6:00   
    3                       -160.6513                   -10:00   
    4                       -122.3973                    -6:00   
    ..                            ...                      ...   
    95                       179.7290                    +8:00   
    96                      -127.8442                    +5:45   
    97                      -135.5331                    -5:00   
    98                       -54.7193                    +5:30   
    99                      -156.5906                    -5:00   

                   location.timezone.description  \
    0                                     Hawaii   
    1                               Newfoundland   
    2                     Almaty, Dhaka, Colombo   
    3                                     Hawaii   
    4    Central Time (US & Canada), Mexico City   
    ..                                       ...   
    95      Beijing, Perth, Singapore, Hong Kong   
    96                                 Kathmandu   
    97  Eastern Time (US & Canada), Bogota, Lima   
    98       Bombay, Calcutta, Madras, New Delhi   
    99  Eastern Time (US & Canada), Bogota, Lima   

                                  login.uuid    login.username login.password  \
    0   e5e1a2ba-45d0-4832-85c4-e3045bee9d96      crazywolf288       roadkill   
    1   fb32bda7-5035-4e25-a169-66efc1a3fa59     brownzebra677         palace   
    2   af9b6a12-c5be-4f8d-a757-7a97e0c9e1b4     bigleopard787         armand   
    3   51bd8a11-8ca5-4396-8557-a1db13bbd03b     yellowlion277        vietnam   
    4   fd577cad-ef7d-4617-a867-97f2b1f8ff83     bigladybug734       mortimer   
    ..                                   ...               ...            ...   
    95  1a55187b-b3af-491e-bc44-a86be8dbb9ec       tinyswan765       porkchop   
    96  bbc41d10-24a4-47f7-b443-d51053d0ac87  silverpeacock353        tolkien   
    97  ccf9021e-b109-4a04-81f9-192fff610cba   greenostrich980        love123   
    98  5c08ecd0-2943-4dc2-afd8-03dfd1c0c2d0   ticklishlion999       overkill   
    99  09e2a5f0-7afd-4ef4-87ba-bedc857012f2    silvergoose288       lonewolf   

       login.salt                         login.md5  \
    0    v1dHnisv  e0dd68e8813893b548c56d424e49f737   
    1    xKAy38Vf  bee114aba9131aa15f9d35b5fb80f56b   
    2    IdugU2HN  2d9f230ff2c1bab6fbd5dc4cba0078f4   
    3    KE8jTf8F  2cb5257af9ffc77fef64968ab3c34dc6   
    4    dWhaZs5C  e33604a9b3c4d23a4b86b5b09b6430e8   
    ..        ...                               ...   
    95   e6DTlHro  d4cf140912b70774fcbf3ad3ca56a6ac   
    96   DgHonIhF  998895ae846f455dab9a3b5d90096843   
    97   JYFq0WGM  08ee2d72da8fc8f47e35dd5f60a642d1   
    98   bZgipa37  e1dbb82dc3d3b7a088b84bc267b5f54b   
    99   kEpkgfYL  24820ed9a32a1a64bc062a6a329e5376   

                                      login.sha1  \
    0   cbc0d05a031741ff195df65be636de4f0cd31bf4   
    1   7abe820547f4d596fac58e7069df8441e5da5470   
    2   017f7f86e12671d0c8fe5229b003932f266ea873   
    3   d3c9f710a0393a1e408005b505cbaf0bdab73424   
    4   c092c2dd71bf72e4223955b8d1491b413e3e13d9   
    ..                                       ...   
    95  5d2ccc5481747c118b71b0a2dcb068293a328ea6   
    96  77779b862d107b9e4d163c141c3bcede4abdbbdd   
    97  0fb7c361de13e689a70fe0260651e4529f907938   
    98  9e42bfbcfad85ad3aa69bb92359afb86a9c94e5a   
    99  ed3045456508cf5eb849329e7784f9025e41bbe6   

                                             login.sha256  \
    0   5b9bdcc2057a632dcc15a0e36cc620f3e99af9882d48bf...   
    1   8637f0ebe2df1dc92a899fbeda83d15510f228d4ba429f...   
    2   d85e26d39a40d5a527b2fcc66b02a28a5bf146c53033dd...   
    3   336eb623824bf85e018a8722e8ec5e0e628b05f3e36c95...   
    4   2df123b2105ed123b8ec2d617f5edc13f2c2e0fbb965a9...   
    ..                                                ...   
    95  f3ea6619856b96f440259df4333ecf61d5a75f75b392c6...   
    96  35a3e5ad082a09c364126b76d66e4fa734bd9375426590...   
    97  f69330897a2293d2a9a66ea55af590ad305dc32dff4d28...   
    98  5f8e109d98b4aa18d4cefb4548869e584abdfe1b4a61e1...   
    99  484d72fecb2cae659de0cd7f70f549b803e9a991779727...   

                        dob.date  dob.age           registered.date  \
    0   1945-08-22T02:19:07.166Z       79  2007-08-28T05:49:05.296Z   
    1   1964-10-31T05:49:39.894Z       60  2014-02-08T11:59:24.181Z   
    2   1982-05-02T18:23:51.892Z       42  2009-02-16T23:46:40.910Z   
    3   1960-09-21T01:13:34.131Z       64  2007-08-25T08:56:38.539Z   
    4   1957-03-27T16:55:28.032Z       68  2015-09-26T19:32:37.231Z   
    ..                       ...      ...                       ...   
    95  1960-09-21T16:11:33.143Z       64  2006-07-07T01:40:22.819Z   
    96  1987-02-05T09:26:16.302Z       38  2018-08-16T07:30:32.568Z   
    97  1970-03-23T12:26:50.644Z       55  2017-11-05T00:16:49.797Z   
    98  1996-06-24T03:46:32.378Z       28  2015-06-22T00:29:21.786Z   
    99  1972-05-06T20:26:38.655Z       52  2021-11-09T19:23:56.452Z   

        registered.age id.name           id.value  \
    0               17                       None   
    1               11     PPS           8443446T   
    2               16     NSS    01 98 34 4768 8   
    3               17                       None   
    4                9                       None   
    ..             ...     ...                ...   
    95              18     BSN           77601361   
    96               6    HETU  NaNNA167undefined   
    97               7     TFN          756747900   
    98               9    HETU  NaNNA850undefined   
    99               3     NSS    62 15 10 1757 4   

                                           picture.large  \
    0   https://randomuser.me/api/portraits/women/33.jpg   
    1     https://randomuser.me/api/portraits/men/56.jpg   
    2     https://randomuser.me/api/portraits/men/20.jpg   
    3     https://randomuser.me/api/portraits/men/45.jpg   
    4     https://randomuser.me/api/portraits/men/89.jpg   
    ..                                               ...   
    95  https://randomuser.me/api/portraits/women/82.jpg   
    96     https://randomuser.me/api/portraits/men/8.jpg   
    97    https://randomuser.me/api/portraits/men/52.jpg   
    98  https://randomuser.me/api/portraits/women/45.jpg   
    99    https://randomuser.me/api/portraits/men/39.jpg   

                                           picture.medium  \
    0   https://randomuser.me/api/portraits/med/women/...   
    1   https://randomuser.me/api/portraits/med/men/56...   
    2   https://randomuser.me/api/portraits/med/men/20...   
    3   https://randomuser.me/api/portraits/med/men/45...   
    4   https://randomuser.me/api/portraits/med/men/89...   
    ..                                                ...   
    95  https://randomuser.me/api/portraits/med/women/...   
    96  https://randomuser.me/api/portraits/med/men/8.jpg   
    97  https://randomuser.me/api/portraits/med/men/52...   
    98  https://randomuser.me/api/portraits/med/women/...   
    99  https://randomuser.me/api/portraits/med/men/39...   

                                        picture.thumbnail  
    0   https://randomuser.me/api/portraits/thumb/wome...  
    1   https://randomuser.me/api/portraits/thumb/men/...  
    2   https://randomuser.me/api/portraits/thumb/men/...  
    3   https://randomuser.me/api/portraits/thumb/men/...  
    4   https://randomuser.me/api/portraits/thumb/men/...  
    ..                                                ...  
    95  https://randomuser.me/api/portraits/thumb/wome...  
    96  https://randomuser.me/api/portraits/thumb/men/...  
    97  https://randomuser.me/api/portraits/thumb/men/...  
    98  https://randomuser.me/api/portraits/thumb/wome...  
    99  https://randomuser.me/api/portraits/thumb/men/...  

    [100 rows x 34 columns]

</div>

</div>

<div class="cell code" execution_count="22" id="8LlrmBMnjJCj">

``` python
df.to_csv("RandomUser.csv",index=False)
```

</div>

<div class="cell code" execution_count="20" id="RGnUp0KqjHyo" scrolled="true">

``` python
'''#Guardar el dataframe en Drive
from google.colab import drive
drive.mount('drive')'''
```

<div class="output execute_result" execution_count="20">

    "#Guardar el dataframe en Drive\nfrom google.colab import drive\ndrive.mount('drive')"

</div>

</div>

<div class="cell code" execution_count="21" id="oq7W8NdojKQa">

``` python
'''!cp RandomUser.csv "drive/My Drive/"'''
```

<div class="output execute_result" execution_count="21">

    '!cp RandomUser.csv "drive/My Drive/"'

</div>

</div>

<div class="cell markdown" id="dxXsb0yaXVcQ">

## **Ejercicio 3: TU TURNO**

<https://date.nager.at/> contiene los feriados públicos a nivel mundial. Adicionalmente, contiene Public Holiday API que provee los feriados de más de 100 países.

Extraee los feriados de Perú del año 2024 a partir de su API.

Hint: Investigue en la web de date.nager para encontrar la web API (<https://date.nager.at/swagger/index.html>).

</div>

<div class="cell code" execution_count="33" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:283,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714940573346,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="2xRm521rZb3A" outputId="e402d81f-72ac-4b07-9e9a-4951794fcad5">

``` python
#Paso 1:
url = "https://date.nager.at/api/v3/PublicHolidays/2025/PE"
response = requests.get(url)
response
```

<div class="output execute_result" execution_count="33">

    <Response [200]>

</div>

</div>

<div class="cell code" execution_count="34" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:488}" executionInfo="{&quot;elapsed&quot;:266,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1714940614999,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="u3DxZchobIcW" outputId="3c2b4313-0154-4461-abd3-d81285150f1c">

``` python
#Paso 2:
data = response.json()
#Paso 3:
df = pd.json_normalize(data)
df
```

<div class="output execute_result" execution_count="34">

              date                     localName                        name  \
    0   2025-01-01                     Año Nuevo              New Year's Day   
    1   2025-04-17                  Jueves Santo               Holy Thursday   
    2   2025-04-17                  Jueves Santo             Maundy Thursday   
    3   2025-04-18                 Viernes Santo                 Good Friday   
    4   2025-04-20                 Domingo Santo               Easter Sunday   
    5   2025-05-01               Día del Trabajo  International Workers' Day   
    6   2025-06-29  Día de San Pedro y San Pablo      St. Peter and St. Paul   
    7   2025-07-28       Día de la Independencia            Independence Day   
    8   2025-07-29       Día de la Independencia            Independence Day   
    9   2025-08-30     Día de Santa Rosa de Lima          Santa Rosa de Lima   
    10  2025-10-08            Combate de Angamos           Battle of Angamos   
    11  2025-11-01       Día de Todos los Santos              All Saints Day   
    12  2025-12-08         Inmaculada Concepción       Immaculate Conception   
    13  2025-12-25                       Navidad               Christmas Day   

       countryCode  fixed  global counties launchYear     types  
    0           PE  False    True     None       None  [Public]  
    1           PE  False    True     None       None  [Public]  
    2           PE  False    True     None       None  [Public]  
    3           PE  False    True     None       None  [Public]  
    4           PE  False    True     None       None  [Public]  
    5           PE  False    True     None       None  [Public]  
    6           PE  False    True     None       None  [Public]  
    7           PE  False    True     None       None  [Public]  
    8           PE  False    True     None       None  [Public]  
    9           PE  False    True     None       None  [Public]  
    10          PE  False    True     None       None  [Public]  
    11          PE  False    True     None       None  [Public]  
    12          PE  False    True     None       None  [Public]  
    13          PE  False    True     None       None  [Public]  

</div>

</div>

<div class="cell markdown" id="UBmmYYMSkAXq">

## **APIs con Autenticación**

Los enfoques de **autenticación** van desde lo más simple y directo, como los que usan claves API (API keys) o autenticación básica, hasta técnicas mucho más complejas y seguras, como `OAuth` (Open Authorization, protocolo de autorización que permite que una aplicación acceda a recursos protegidos de otra aplicación sin necesidad de compartir las credenciales del usuario).

Por lo general, llamar a una API sin credenciales o con las incorrectas devolverá un status code: `401 No autorizado` o `403 Prohibido`.

**API Keys** Estas claves se utilizan para identificarse como usuario o cliente de la API y para rastrear su uso de la API. Las claves API generalmente se envían como un encabezado de solicitud (request header) o como un parámetro de consulta (query).

</div>

<div class="cell markdown" id="6qEMfr2KkKL0">

## **Ejercicio 4:**

**API de la NASA:** una de las mejores colecciones de API disponibles públicamente es la proporcionada por la NASA. Se puede obtener la imagen astronómica del día o imágenes tomadas por la Cámara de imágenes policromáticas de la Tierra (EPIC), entre otras (<https://api.nasa.gov/>).

</div>

<div class="cell code" execution_count="36" id="_w_M8QHHkUsu">

``` python
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
```

</div>

<div class="cell code" execution_count="45" id="-h-zgF9mkWo8">

``` python
#Nasa otorga DEMO_KEY como key por default
api_key = "DEMO_KEY"
#Construir los párametros de consulta
query_params = {"api_key": api_key, "earth_date": "2024-12-01"}
#Hacer el request
response = requests.get(url, params=query_params)
response
```

<div class="output execute_result" execution_count="45">

    <Response [200]>

</div>

</div>

<div class="cell code" execution_count="46" id="3NvzPlVzkYIw">

``` python
#Recepcionar como dictionary
data = response.json()
data
```

<div class="output execute_result" execution_count="46">

    {'photos': [{'id': 1290897,
       'sol': 4380,
       'camera': {'id': 25,
        'name': 'MARDI',
        'rover_id': 5,
        'full_name': 'Mars Descent Imager'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/msss/04380/mrdi/4380MD0016150000303012E01_DXXX.jpg',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290896,
       'sol': 4380,
       'camera': {'id': 50,
        'name': 'MAST_LEFT',
        'rover_id': 5,
        'full_name': 'MAST_LEFT'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/msss/04380/mcam/4380ML1068000060509077C00_DXXX.jpg',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290898,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786320342EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290899,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786320303EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290900,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786320264EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290901,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786320224EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290902,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786320185EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290903,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786319986EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290904,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786319944EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290905,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786319904EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290906,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786319865EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290907,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786319644EDR_F1111548CCAM06375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290908,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786319420EDR_F1111548CCAM05375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290909,
       'sol': 4380,
       'camera': {'id': 51,
        'name': 'CHEMCAM_RMI',
        'rover_id': 5,
        'full_name': 'CHEMCAM_RMI'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ccam/CR0_786318739EDR_F1111548CCAM05375M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290911,
       'sol': 4380,
       'camera': {'id': 53,
        'name': 'FHAZ_LEFT_B',
        'rover_id': 5,
        'full_name': 'FHAZ_LEFT_B'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/fcam/FLB_786329073EDR_F1111824FHAZ00302M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290910,
       'sol': 4380,
       'camera': {'id': 54,
        'name': 'FHAZ_RIGHT_B',
        'rover_id': 5,
        'full_name': 'FHAZ_RIGHT_B'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/fcam/FRB_786329073EDR_F1111824FHAZ00302M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290912,
       'sol': 4380,
       'camera': {'id': 55,
        'name': 'NAV_LEFT_B',
        'rover_id': 5,
        'full_name': 'NAV_LEFT_B'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ncam/NLB_786330714EDR_F1111824NCAM00354M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290913,
       'sol': 4380,
       'camera': {'id': 55,
        'name': 'NAV_LEFT_B',
        'rover_id': 5,
        'full_name': 'NAV_LEFT_B'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ncam/NLB_786330682EDR_F1111824NCAM00354M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290914,
       'sol': 4380,
       'camera': {'id': 55,
        'name': 'NAV_LEFT_B',
        'rover_id': 5,
        'full_name': 'NAV_LEFT_B'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ncam/NLB_786330658EDR_F1111824NCAM00354M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290915,
       'sol': 4380,
       'camera': {'id': 55,
        'name': 'NAV_LEFT_B',
        'rover_id': 5,
        'full_name': 'NAV_LEFT_B'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ncam/NLB_786330634EDR_F1111824NCAM00354M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290916,
       'sol': 4380,
       'camera': {'id': 55,
        'name': 'NAV_LEFT_B',
        'rover_id': 5,
        'full_name': 'NAV_LEFT_B'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ncam/NLB_786330610EDR_F1111824NCAM00354M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 1290917,
       'sol': 4380,
       'camera': {'id': 55,
        'name': 'NAV_LEFT_B',
        'rover_id': 5,
        'full_name': 'NAV_LEFT_B'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/04380/opgs/edr/ncam/NLB_786330572EDR_F1111824NCAM00251M_.JPG',
       'earth_date': '2024-12-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}}]}

</div>

</div>

<div class="cell code" execution_count="47" id="pdGU07t2kbIt">

``` python
# Extraer los datos y guardarlos en un dataframe
df = pd.json_normalize(data,'photos')
df
```

<div class="output execute_result" execution_count="47">

             id   sol                                            img_src  \
    0   1290897  4380  https://mars.nasa.gov/msl-raw-images/msss/0438...   
    1   1290896  4380  https://mars.nasa.gov/msl-raw-images/msss/0438...   
    2   1290898  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    3   1290899  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    4   1290900  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    5   1290901  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    6   1290902  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    7   1290903  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    8   1290904  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    9   1290905  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    10  1290906  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    11  1290907  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    12  1290908  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    13  1290909  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    14  1290911  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    15  1290910  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    16  1290912  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    17  1290913  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    18  1290914  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    19  1290915  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    20  1290916  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   
    21  1290917  4380  https://mars.nasa.gov/msl-raw-images/proj/msl/...   

        earth_date  camera.id   camera.name  camera.rover_id     camera.full_name  \
    0   2024-12-01         25         MARDI                5  Mars Descent Imager   
    1   2024-12-01         50     MAST_LEFT                5            MAST_LEFT   
    2   2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    3   2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    4   2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    5   2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    6   2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    7   2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    8   2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    9   2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    10  2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    11  2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    12  2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    13  2024-12-01         51   CHEMCAM_RMI                5          CHEMCAM_RMI   
    14  2024-12-01         53   FHAZ_LEFT_B                5          FHAZ_LEFT_B   
    15  2024-12-01         54  FHAZ_RIGHT_B                5         FHAZ_RIGHT_B   
    16  2024-12-01         55    NAV_LEFT_B                5           NAV_LEFT_B   
    17  2024-12-01         55    NAV_LEFT_B                5           NAV_LEFT_B   
    18  2024-12-01         55    NAV_LEFT_B                5           NAV_LEFT_B   
    19  2024-12-01         55    NAV_LEFT_B                5           NAV_LEFT_B   
    20  2024-12-01         55    NAV_LEFT_B                5           NAV_LEFT_B   
    21  2024-12-01         55    NAV_LEFT_B                5           NAV_LEFT_B   

        rover.id rover.name rover.landing_date rover.launch_date rover.status  
    0          5  Curiosity         2012-08-06        2011-11-26       active  
    1          5  Curiosity         2012-08-06        2011-11-26       active  
    2          5  Curiosity         2012-08-06        2011-11-26       active  
    3          5  Curiosity         2012-08-06        2011-11-26       active  
    4          5  Curiosity         2012-08-06        2011-11-26       active  
    5          5  Curiosity         2012-08-06        2011-11-26       active  
    6          5  Curiosity         2012-08-06        2011-11-26       active  
    7          5  Curiosity         2012-08-06        2011-11-26       active  
    8          5  Curiosity         2012-08-06        2011-11-26       active  
    9          5  Curiosity         2012-08-06        2011-11-26       active  
    10         5  Curiosity         2012-08-06        2011-11-26       active  
    11         5  Curiosity         2012-08-06        2011-11-26       active  
    12         5  Curiosity         2012-08-06        2011-11-26       active  
    13         5  Curiosity         2012-08-06        2011-11-26       active  
    14         5  Curiosity         2012-08-06        2011-11-26       active  
    15         5  Curiosity         2012-08-06        2011-11-26       active  
    16         5  Curiosity         2012-08-06        2011-11-26       active  
    17         5  Curiosity         2012-08-06        2011-11-26       active  
    18         5  Curiosity         2012-08-06        2011-11-26       active  
    19         5  Curiosity         2012-08-06        2011-11-26       active  
    20         5  Curiosity         2012-08-06        2011-11-26       active  
    21         5  Curiosity         2012-08-06        2011-11-26       active  

</div>

</div>

<div class="cell code">

``` python
```

</div>
