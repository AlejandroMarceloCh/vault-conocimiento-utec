---
curso: ACD
titulo: U2_L2 WebParsing
slides: 0
fuente: U2_L2 WebParsing.ipynb
---

<div class="cell markdown" id="GOqghtf7G6zc">

# **U2_L2: Web Parsing**

</div>

<div class="cell markdown" id="XB5FoTcpGSvM">

**Objetivo:** Comprender el potencial de la librería Beautiful Soup para web parsing

</div>

<div class="cell code" execution_count="32" executionInfo="{&quot;elapsed&quot;:386,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715141079677,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="JO_1QZ3KFvML">

``` python
#Cargar librerias
from bs4 import BeautifulSoup as BSoup
```

</div>

<div class="cell markdown" id="9y3RPrzdayJL">

## **Parte I:** Fundamentos

</div>

<div class="cell markdown" id="wiVSjw6UJt_x">

Para este sección usaremos la página ***testHtml.html***

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:178}" executionInfo="{&quot;elapsed&quot;:7,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715137274776,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="XyQCavZxJUMh" outputId="0e873ed3-c1ea-4273-c3da-22f1bc759933">

``` python
html = open("/content/testHtml.html","r").read()
html
```

<div class="output execute_result" execution_count="5">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell markdown" id="X5oIjIAd30Ch">

Crear una sopa usando un parser por ejemplo "html.parser"

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:354,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715137570728,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="B10oDXpyKZaX" outputId="17401a6e-ce5c-4cff-af55-8a5360b380d1">

``` python
#Crea una sopa
soup = BSoup(html, "html.parser")
soup
```

<div class="output execute_result" execution_count="7">

    <html>
    <head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
                <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
                <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
                <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
                and they lived at the bottom of a well.
            </p>
    <p class="story">...</p>
    <h1>Secret agents</h1>
    <ul>
    <li data-id="10784">Jason Walters, 003: Found dead in "A View to a Kill".</li>
    <li data-id="97865">Alex Trevelyan, 006: Agent turned terrorist leader; James' nemesis in "Goldeneye".</li>
    <li data-id="45732">James Bond, 007: The main man; shaken but not stirred.</li>
    </ul>
    </body>
    </html>

</div>

</div>

<div class="cell markdown" id="gEgZTC6OKx4-">

La función `prettify()` imprime los resultados de manera más compacta

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:178}" executionInfo="{&quot;elapsed&quot;:266,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715137632086,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="BT6lAnYUKyeI" outputId="70694ad0-727e-48f8-9cce-8878214021f6">

``` python
soup.prettify()
```

<div class="output execute_result" execution_count="8">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell markdown" id="e7Utw7vGLEb8">

Desde este punto todos el contenido del HTML se puede acceder como elementos individuales.

</div>

<div class="cell markdown" id="AeFjY9RqMXz2">

### **Acceder a elementos del HTML**

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:267,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715138066992,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="merbqM6EMXOo" outputId="a20f567b-404e-4ee9-d90f-22ffe691a52c">

``` python
#Recordemos:
soup
```

<div class="output execute_result" execution_count="13">

    <html>
    <head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
                <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
                <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
                <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
                and they lived at the bottom of a well.
            </p>
    <p class="story">...</p>
    <h1>Secret agents</h1>
    <ul>
    <li data-id="10784">Jason Walters, 003: Found dead in "A View to a Kill".</li>
    <li data-id="97865">Alex Trevelyan, 006: Agent turned terrorist leader; James' nemesis in "Goldeneye".</li>
    <li data-id="45732">James Bond, 007: The main man; shaken but not stirred.</li>
    </ul>
    </body>
    </html>

</div>

</div>

<div class="cell markdown" id="x3Q-sQeZMki7">

Se puede acceder a cualquier elemento como a, p, h1, etc. Observe que solo devuelve el primer valor que encuentra.

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:7,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715137875596,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="XjaY7PjaLDWK" outputId="68231d65-b35c-49cc-a355-779c0302c069">

``` python
soup.a
```

<div class="output execute_result" execution_count="9">

    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

</div>

</div>

<div class="cell code" execution_count="11" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:289,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715137899763,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="dKqSlOx2L1WX" outputId="b29a8255-6cb4-464e-cb15-7c8cae8e60e1">

``` python
soup.h1
```

<div class="output execute_result" execution_count="11">

    <h1>Secret agents</h1>

</div>

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:401,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715138122397,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="aALAwYdcMr-b" outputId="4944958f-6fc2-4001-97a9-639ed719d0cb">

``` python
soup.p
```

<div class="output execute_result" execution_count="14">

    <p class="title"><b>The Dormouse's story</b></p>

</div>

</div>

<div class="cell markdown" id="D0faZZq1M9CG">

También se puede usar las siguientes funciones:

- **attrs**: Enlista todos los atributos de cualquier elemento encontrado.
- **has_attr()**: Recibe el nombre del atributo como argumento para comprobar si existe; devuelve una respuesta booleana (True/False)
- **get()**: Recibe el nombre del atributo como argumento y devuelve el valor del atributo proporcionado.

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:416,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715138447898,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="JHg8oj5wL4ck" outputId="af4c939f-b50a-4731-f3d8-8d14c007e35a">

``` python
soup.a.attrs
```

<div class="output execute_result" execution_count="15">

    {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:389,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715138488903,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="odpaob7EN_No" outputId="7f67d21c-d71c-4c52-ba40-d2b1753d3ae2">

``` python
soup.a.has_attr('class')
```

<div class="output execute_result" execution_count="17">

    True

</div>

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:260,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715138508629,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="p0-WguceOHzW" outputId="e73dc1fc-0b29-44f1-fc83-f6514aed0017">

``` python
soup.a.get('class')
```

<div class="output execute_result" execution_count="18">

    ['sister']

</div>

</div>

<div class="cell markdown" id="IBD-DBoxOcfk">

Se puede recuperar un valor de cadena o contenido de cualquier elemento utilizando atributos **text** y **string**, así como la función **get_text()**

</div>

<div class="cell code" execution_count="19" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}" executionInfo="{&quot;elapsed&quot;:289,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715138637935,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="oNNxHVVUOoL_" outputId="c9c91250-0b30-4742-8f90-24386556703c">

``` python
soup.a.text
```

<div class="output execute_result" execution_count="19">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell code" execution_count="20" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}" executionInfo="{&quot;elapsed&quot;:311,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715138656988,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="a91S0-cbOsHD" outputId="38031bb5-0865-49c2-f5f9-947902df4260">

``` python
soup.a.string
```

<div class="output execute_result" execution_count="20">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell code" execution_count="22" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}" executionInfo="{&quot;elapsed&quot;:292,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715138685615,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="x63rujMKOwMv" outputId="3535f5b2-c39f-48d1-c11b-6d0fe60bb20f">

``` python
soup.a.get_text()
```

<div class="output execute_result" execution_count="22">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell markdown" id="ULYr1M2kO81l">

### **Encontrar elementos en HTML**

</div>

<div class="cell markdown" id="U1HxP3GxPCD-">

**find():** Devuelve **un único resultado** según los argumentos proporcionados. En caso no hay ningún resultado, retorna None.

</div>

<div class="cell code" execution_count="23" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:272,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715139084478,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="pdY0PCgsQPpS" outputId="ca60247d-c3ac-4e9a-b1dc-86ed5ea7eaa8">

``` python
soup.find('a')
```

<div class="output execute_result" execution_count="23">

    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

</div>

</div>

<div class="cell markdown" id="cagFAWlnWNhI">

Trata de entender los siguientes líneas de código:

</div>

<div class="cell code" id="Ycsc3ZpgQagn">

``` python
soup.find('a').get('class')
soup.find('a',attrs={'class':"sister"}).get_text()
soup.find('a',string="Elsie")
soup.find('a',"sister")
soup.find('a',{'id':"link1"})
soup.find("a",attrs={'class':'sister'},text="Elsie")
soup.find('p','story')
soup.find('ul')
soup.find('ul').find('li')
soup.find('ul').find('li',attrs={'data-id':'97865'}).get_text()
```

</div>

<div class="cell markdown" id="G2az-XB8XCzC">

**find_all():** Retorna uno o más resultados dentro de una lista. En caso no hay ningún resultado, retorna una lista vacía.

</div>

<div class="cell code" execution_count="29" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:298,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715140913235,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="iL4lrxBJXVt7" outputId="2fe6dd7b-b477-4daa-f555-d268fcb97f24">

``` python
soup.find_all('a')
```

<div class="output execute_result" execution_count="29">

    [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
     <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
     <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

</div>

</div>

<div class="cell code" execution_count="30" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:288,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715140943854,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="benNwH1iXble" outputId="ae5d0c2e-d234-4b0a-95d4-59eb74d1ead0">

``` python
#Es equivalente a find_all:
soup("a")
```

<div class="output execute_result" execution_count="30">

    [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
     <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
     <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

</div>

</div>

<div class="cell markdown" id="2HyOlZOIXu-U">

Experimente con las siguientes líneas de código:

</div>

<div class="cell code" id="Idi3Thu6Xquc">

``` python
soup.find_all("a",string="Elsie")
soup.find_all(['a','title'])
soup.find_all('p','story')
soup.find_all("p",attrs={'class':["title","story"]})
```

</div>

<div class="cell markdown" id="1k0cmEaMYYde">

### **Navegar a través de DOM**

Se puede mover a través del árbol usando **next_element** or **previous_element**

</div>

<div class="cell code" execution_count="35" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:364,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715141330671,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="L2s5_iH3Y7eJ" outputId="c173d2c2-0522-42f6-da99-bcc829f12abf">

``` python
soup
```

<div class="output execute_result" execution_count="35">

    <html>
    <head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
                <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
                <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
                <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
                and they lived at the bottom of a well.
            </p>
    <p class="story">...</p>
    <h1>Secret agents</h1>
    <ul>
    <li data-id="10784">Jason Walters, 003: Found dead in "A View to a Kill".</li>
    <li data-id="97865">Alex Trevelyan, 006: Agent turned terrorist leader; James' nemesis in "Goldeneye".</li>
    <li data-id="45732">James Bond, 007: The main man; shaken but not stirred.</li>
    </ul>
    </body>
    </html>

</div>

</div>

<div class="cell code" execution_count="36" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:297,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715141380237,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="SAUu1hXFZGN6" outputId="b39f289f-83b1-4132-845e-c33cd7901212">

``` python
soup.find('p','story')
```

<div class="output execute_result" execution_count="36">

    <p class="story">Once upon a time there were three little sisters; and their names were
                <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
                <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
                <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
                and they lived at the bottom of a well.
            </p>

</div>

</div>

<div class="cell code" execution_count="34" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:35}" executionInfo="{&quot;elapsed&quot;:411,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715141319111,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="jxJUM_WrYyQ3" outputId="aafb7d1c-8177-4b52-8d0b-d1b1c3a67a3b">

``` python
soup.find('p','story').next_element
```

<div class="output execute_result" execution_count="34">

``` json
{"type":"string"}
```

</div>

</div>

<div class="cell code" execution_count="37" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:380,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715141409413,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="PHCCfQPAZN28" outputId="cf5c462f-6355-4790-ad3c-916fb0047fc9">

``` python
soup.find('p','story').next_element.next_element
```

<div class="output execute_result" execution_count="37">

    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

</div>

</div>

<div class="cell code" execution_count="39" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:295,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715141469630,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="8VUfnULmZc6S" outputId="d675ae00-f20a-4532-e76a-7cddc3a9a5c7">

``` python
soup.find('b')
```

<div class="output execute_result" execution_count="39">

    <b>The Dormouse's story</b>

</div>

</div>

<div class="cell code" execution_count="38" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:259,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1715141438004,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="tdNdgZ3cZUXX" outputId="84530fc0-fe2c-48e2-f75c-02b9bf7cd47b">

``` python
soup.find('b').previous_element
```

<div class="output execute_result" execution_count="38">

    <p class="title"><b>The Dormouse's story</b></p>

</div>

</div>

<div class="cell markdown" id="JBglwXXka8ci">

## **Parte II:** Ponerlo en Práctica

Para esta sección pondremos en práctica lo aprendido. La página que utilizaremos para parsear es <https://realpython.github.io/fake-jobs/>. Como resultado queremos obtener un dataframe que contenga tres atributos: title (job), company, location.

Recuerde los tres pasos para realizar web scraping:

1.  Inspeccionar la página
2.  Descargar el contenido de la página. Utilice lo aprendido en el laboratorio anterior.
3.  Parsear HTML.

Hint. Agregue las librerías que crea necesarias.

</div>

<div class="cell code">

``` python
```

</div>

<div class="cell code">

``` python
```

</div>
