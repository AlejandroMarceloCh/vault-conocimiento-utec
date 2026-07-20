---
curso: ACD
titulo: U2_L3 Web_Crawler
slides: 0
fuente: U2_L3 Web_Crawler.ipynb
---

<div class="cell markdown" id="SpsVBGpnB-NL">

# **U2_L3: Web Crawler**

***Web crawler*** es el término utilizado para representar los algoritmos que rastrean los sitios y páginas web.

**Objetivo:** Construir un web crawler para extraer datos de un página web

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:1966,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715696800188,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8wL73iBoBgqm">

``` python
#Cargar librerias
from bs4 import BeautifulSoup as BSoup
import requests
import pandas as pd
```

</div>

<div class="cell markdown" id="Ijd3VjEVF7aY">

**Contexto:**\
Para este laboratorio utilizaremos la siguiente página web como source: <https://quotes.toscrape.com/> . El objetivo es obtener un dataset (dataframe) que contenga los siguientes atributos:

- Quote
- Author
- Tags

El dataset debe ser completado con todos los quotes de la página. Note que la página web tiene varias páginas.

</div>

<div class="cell markdown" id="Gxo6_W96JJ_N">

## **Ejercicio1:**

Cargue la página principal y cree el objeto Soup

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:1142,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715271439591,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Sna1u-u7I-_l" outputId="b7142d76-bc36-479d-ff0f-d1f7a84a6373">

``` python
# Descargar la página
#TO DO
url = " https://quotes.toscrape.com/"
page = requests.get(url)
page
```

<div class="output execute_result" execution_count="3">

    <Response [200]>

</div>

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:618,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715696938297,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="I2c2lENuf7uA" outputId="569535d7-ff9f-4388-e17e-fa8130a9b36f">

``` python
# Descargar la página
#TO DO
url = "https://www.sbs.com.pe/"
page = requests.get(url)
page
```

<div class="output execute_result" execution_count="7">

    <Response [200]>

</div>

</div>

<div class="cell code" id="2Cq84ywbJU4Z">

``` python
#TO DO
# Crear la sopa
soup = BSoup(page.content,'html.parser')
```

</div>

<div class="cell markdown" id="n66Nu5nAJ0lx">

## **Ejercicio 2:**

Encuentre la primera quote, identifique su:

- Quote : string
- Author : string
- Tags : string list

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:585,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715271909556,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="QWcrbBZdJ6LU" outputId="e6a43612-6d2e-46f6-def8-dc582fbe6118">

``` python
fstquote = soup.find('div','quote')
fstquote
```

<div class="output execute_result" execution_count="12">

    <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
    <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
    <span>by <small class="author" itemprop="author">Albert Einstein</small>
    <a href="/author/Albert-Einstein">(about)</a>
    </span>
    <div class="tags">
                Tags:
                <meta class="keywords" content="change,deep-thoughts,thinking,world" itemprop="keywords"/>
    <a class="tag" href="/tag/change/page/1/">change</a>
    <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
    <a class="tag" href="/tag/thinking/page/1/">thinking</a>
    <a class="tag" href="/tag/world/page/1/">world</a>
    </div>
    </div>

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}" executionInfo="{&quot;elapsed&quot;:471,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715271934171,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="tIGLD2jtK1j2" outputId="d2808e98-6be1-44a2-83f8-61352bbada4a">

``` python
fstquote.find('span').text
```

<div class="output execute_result" execution_count="15">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}" executionInfo="{&quot;elapsed&quot;:933,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715272031853,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="BxZLOV_7LPVn" outputId="5a5d6d2f-1f7a-4182-85d2-d4b2871793f1">

``` python
fstquote.find('small','author').text
```

<div class="output execute_result" execution_count="19">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:450,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715272153461,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="-sYyvHOJLnKt" outputId="8e796bd7-1905-4e2f-b808-ed14c991aa76">

``` python
[ elem.text for elem in fstquote.find_all('a','tag')]
```

<div class="output execute_result" execution_count="21">

    ['change', 'deep-thoughts', 'thinking', 'world']

</div>

</div>

<div class="cell markdown" id="3D_BuyfQMGaL">

## **Ejercicio 3:**

Implemente una función `webScraping(url)` que reciba la url principal y retorne el dataframe.

</div>

<div class="cell code" id="joZ60yXlNT7r">

``` python
def webScraping(url):

  #Request the page
  page = requests.get(url)
  page

  if page.status_code != 200:
    print("ERROR")
    return

  #Build the soup
  soup = BSoup(page.content,'html.parser')

  #Get all quotes
  quoteElemList = soup.find_all('div','quote')

  #Get data for each quote
  quoteList = []
  for i in range(len(quoteElemList)):
    elem = {}
    elem['quote'] = quoteElemList[i].find('span').text
    elem['author'] = quoteElemList[i].find('small','author').text
    elem['tagList'] = [elem.text for elem in quoteElemList[i].find_all('a','tag')]
    quoteList.append(elem)

  return pd.DataFrame(quoteList)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:363}" executionInfo="{&quot;elapsed&quot;:1205,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715273376005,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="RmYkeK-jQQZx" outputId="b7a8ba46-9ccb-4b9e-bcc9-743b711f7df5">

``` python
url = " https://quotes.toscrape.com/"
webScraping(url)
```

<div class="output execute_result" execution_count="27">

``` json
{"summary":"{\n  \"name\": \"webScraping(url)\",\n  \"rows\": 10,\n  \"fields\": [\n    {\n      \"column\": \"quote\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 10,\n        \"samples\": [\n          \"\\u201cA woman is like a tea bag; you never know how strong it is until it's in hot water.\\u201d\",\n          \"\\u201cIt is our choices, Harry, that show what we truly are, far more than our abilities.\\u201d\",\n          \"\\u201cTry not to become a man of success. Rather become a man of value.\\u201d\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"author\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 8,\n        \"samples\": [\n          \"J.K. Rowling\",\n          \"Thomas A. Edison\",\n          \"Albert Einstein\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"tagList\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>

<div class="cell markdown" id="JbohKYy1Vb7p">

## **Ejercicio 4:**

Implemente su primer web crawler `webCrawler(urlInicial)` que empiece en la urlInicial y se mueva a través de las siguientes páginas, hasta llegar a la página final. La función debe retornar el dataset (dataframe) completo.

*Hint:* Inspecciona el código del botton Next

</div>

<div class="cell code" id="JH2azYeuWQzE">

``` python
def webCrawler(urlInicial):

  nextpage = True
  quoteList = []
  url = urlInicial

  while(nextpage):

    #Request the page
    page = requests.get(url)
    #Build the soup
    soup = BSoup(page.content,'html.parser')

    #Get all quotes
    quoteElemList = soup.find_all('div','quote')
    #Get data for each quote
    for i in range(len(quoteElemList)):
      elem = {}
      elem['quote'] = quoteElemList[i].find('span').text
      elem['author'] = quoteElemList[i].find('small','author').text
      elem['tagList'] = [elem.text for elem in quoteElemList[i].find_all('a','tag')]
      quoteList.append(elem)

    #Get nextPage
    if soup.find('li','next'):
      txtNext = soup.find('li','next').find('a').get('href')
      url = urlInicial + txtNext[1:]
    else:
      nextpage = False

  #Dataframe
  return pd.DataFrame(quoteList)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:8674,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715282617725,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="NOG3YgdGnnCL" outputId="9b803740-ff30-499d-c69c-6e64f979f103">

``` python
url = " https://quotes.toscrape.com/"
webCrawler(url)
```

<div class="output execute_result" execution_count="55">

``` json
{"summary":"{\n  \"name\": \"#https://quotes\",\n  \"rows\": 100,\n  \"fields\": [\n    {\n      \"column\": \"quote\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 100,\n        \"samples\": [\n          \"\\u201cI declare after all there is no enjoyment like reading! How much sooner one tires of any thing than of a book! -- When I have a house of my own, I shall be miserable if I have not an excellent library.\\u201d\",\n          \"\\u201cIf I were not a physicist, I would probably be a musician. I often think in music. I live my daydreams in music. I see my life in terms of music.\\u201d\",\n          \"\\u201cIf I had a flower for every time I thought of you...I could walk through my garden forever.\\u201d\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"author\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 50,\n        \"samples\": [\n          \"Mark Twain\",\n          \"J.D. Salinger\",\n          \"Stephenie Meyer\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"tagList\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>
