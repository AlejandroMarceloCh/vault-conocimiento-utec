---
curso: ACD
titulo: [2025] U2_T2 Web Scraping
slides: 30
fuente: [2025] U2_T2 Web Scraping.pdf
---

## Slide 1

Portada.

**Web Scraping**
*DS3021 Análisis Computacional de Datos*
Mg. José Espinoza Melgarejo

Fondo decorativo: silueta de persona caminando por un túnel tecnológico azul.

## Slide 2

**Objetivo de sesión** (título vertical al margen izquierdo)

> Aplicar técnicas de web scraping para el procesamiento de extracción y recolección de datos.

Foto decorativa de dos personas revisando documentos.

## Slide 3

Separador de sección.

**1. Web Scraping**

Ícono de portapapeles a la izquierda; imagen decorativa de mano robótica tocando un globo terráqueo digital.

## Slide 4

**Web Scraping — Definición**

- Se refiere netamente a la extracción de datos desde una website
- Se pueden crear procesos autónomos (bots o web crawlers) para obtener conjuntos de datos
- El proceso de web scraping consta de dos partes:
  - **Fetching** (conectar y descargar de la web)
  - **Extraction data** (parsear la data, …)

## Slide 5

**Diagrama — Figure 1.1: Web scraping – storing web content as data**

Flujo de izquierda a derecha:

- Cuatro cajas rectangulares apiladas: **Website-1**, **Website-2**, **Website-3**, **Website-4**.
- Cada website tiene flechas curvas **bidireccionales** hacia un rombo central rotulado **Scraper (Request/Response)** — la flecha de ida representa el request y la de vuelta el response desde cada sitio.
- Del rombo sale una flecha hacia la derecha etiquetada **Extract / Filter**, que apunta a un recuadro de borde punteado que agrupa tres destinos de almacenamiento: un cilindro **Database**, un stack de documentos **Docs/Files** y una nube **Cloud**.

Crédito: Imagen tomada del libro *Hands-On Web Scraping with Python - Second Edition*, Anish Chapagain.

## Slide 6

**Retos — Web Scraping**

Existen varios retos al hacer web scraping, sin embargo dos principales son:

- **Variedad:** Cada website es diferente (semi estructurado). Si bien encontramos estructuras generales, cada website es única y necesitará una personalización al momento de la extracción.
- **Durabilidad:** Las websites cambian constantemente. El web scraper que creaste puede servir una vez o varias pero no eternamente.

## Slide 7

Separador de sección.

**2. HTML y CSS**

Imagen decorativa (mano robótica / globo digital).

## Slide 8

**HTML — Hypertext markup Language**

- HTML define y contiene el contenido de una página web.
- Los datos que se pueden extraer y cualquier fuente de datos que revele información se pueden encontrar dentro de las páginas HTML dentro de un conjunto de instrucciones predefinido o elementos de marcado llamados **etiquetas (tags)**.
- Las etiquetas HTML normalmente son un marcador de posición con nombre que lleva ciertos atributos predefinidos, por ejemplo, **`<a>`, `<b>`, `<table>`, `<img>` y `<script>`**.

Foto decorativa a la izquierda.

## Slide 9

Los elementos HTML también se pueden anidar en una estructura **similar a un árbol con una jerarquía padre-hijo**, de la siguiente manera:

Bloque de código HTML mostrado en un recuadro gris:

```html
<div class="article">
  <p id="mainContent" class="content">
    <b>Paragraph Content</b>
      <img src="mylogo.png" id="pageLogo" alt="Logo"
        class="logo"/>
  </p>
  <p>
    <h3> Paragraph Title: Web Scraping</h3>
  </p>
</div>
```

Foto decorativa de laboratorio a la izquierda.

## Slide 10

**HTML — Atributos Globales**

- **id:** los valores de este atributo deben ser únicos para el elemento al que se aplican
- **class:** los valores de este atributo se usan principalmente con CSS, se pueden usar con múltiples elementos
- **style:** especifica estilos CSS en línea para un elemento
- **lang:** Esto ayuda a identificar el idioma del texto.

Foto decorativa a la derecha.

## Slide 11

**CSS**

- CSS describe **las propiedades de visualización** de los elementos HTML y la apariencia de las páginas web. CSS se utiliza para diseñar y proporcionar la apariencia y presentación deseadas de los elementos HTML.
- Al utilizar CSS, los desarrolladores/diseñadores pueden controlar el diseño y la presentación de un documento web. CSS se puede aplicar a un elemento distinto de una página o se puede incrustar en un documento independiente.
- Los detalles de estilo se pueden describir usando la etiqueta `<style>`.

## Slide 12

La etiqueta **`<style>`** puede contener detalles dirigidos a elementos repetidos y diversos en un bloque.

A la izquierda, bloque de código HTML con el bloque `<style>` **resaltado con un recuadro celeste**; el texto se recorta en el borde derecho del recuadro:

```html
<html>
<head>
<style>
a{color:blue;}
h1{color:black; text-decoration:underline;}
#idOne{color:red;}
.classOne{color:orange;}
</style>
</head>
<body>
<h1> Welcome to Web Scraping </h1>Links:<a href="https://www.go…
<a class='classOne' href="https://www.yahoo.com"> Yahoo </a>
<a id='idOne' href="https://www.wikipedia.org"> Wikipedia </a>
</body>
</html>
```

A la derecha, captura del render (**Figure 1.4: Output of the HTML code using CSS**): el título "Welcome to Web Scraping" en negro y **subrayado** (por `h1`), y la línea "Links:" con tres enlaces — **Google** en azul (regla `a`), **Yahoo** en naranja (clase `.classOne`) y **Wikipedia** en rojo (id `#idOne`).

Referencias: https://www.w3.org/Style/CSS/ · https://www.w3schools.com/css/

## Slide 13

Separador de sección.

**3. Búsqueda y Procesamiento de Documentos en la Web**

## Slide 14

**DOM — The Document Object Model**

- Un árbol de elementos para lenguajes de marcado como HTML.
- Entender este árbol es elemental para el proceso de extracción de datos.
- Los **selectores XPath y CSS** se utilizan para navegar a lo largo del DOM y se utilizan para buscar el contenido deseado en los nodos o elementos encontrados.

**Diagrama (Figure 3.1: HTML DOM tree structure)** — árbol de cajas conectadas de izquierda a derecha:

- `Web Document` → `<html> Root`
- `<html> Root` se ramifica en `<head> Element` y `<body> Element`
- `<head> Element` → `<title> Element` → `<style> Element`
- `<body> Element` → `<h1> Element` y `<a> Element`
- `<h1> Element` → `Text: Welcome to..`
- `<a> Element` → `Text: Google` y `Attribute: href`

## Slide 15

**XPath**

- XPath es como **una ruta** (las expresiones se crean utilizando y representando elementos HTML y nodos XML) que identifica nodos en los documentos.
- Las expresiones XPath también se identifican como:
  - Absolutas
  - Relativas

## Slide 16

**XPath — Absolutas**

- Esta expresión representa una *ruta completa desde el elemento raíz hasta el elemento deseado o de destino.*
- En un documento HTML, comienza con **/html** y tiene el aspecto **`/html/body/div[1]/div/div[2]/div/span/p[1]`**.
- Los elementos individuales, como **div** y **p**, generalmente se identifican por su posición y se representan mediante un número de índice, como **[1]** o **[2]**.

Foto decorativa a la izquierda.

## Slide 17

**XPath — Relativas**

- Esta expresión es algo más corta y más legible en comparación con una ruta absoluta y, a menudo, se prefiere a las expresiones absolutas.
- Comienza con ciertos elementos elegidos o seleccionados y termina con el elemento deseado, por ejemplo, **`//*[@id="answer"]/div/span/p[@class="text"]`**.

Foto decorativa a la derecha.

## Slide 18

**CSS selectors**

- Los selectores CSS son patrones definidos que utiliza CSS para seleccionar elementos.
- De manera similar a las expresiones XPath, que se utilizan para buscar e identificar elementos, **los selectores CSS se utilizan para seleccionar o buscar elementos HTML y definir un estilo para ellos.**

Foto decorativa de laboratorio a la izquierda.

## Slide 19

Separador de sección.

**4. Pasos para hacer web scraping**

## Slide 20

**Pasos para hacer Web Scraping**

Diagrama de tres flechas tipo *chevron* encadenadas horizontalmente:

1. **1. Inspeccionar la página** (chevron celeste)
2. **2. Descargar el contenido de la página** (chevron gris)
3. **3. Parsear HTML** (chevron celeste)

## Slide 21

Chevron activo: **1. Inspeccionar la página**

> El primer paso consiste en entender la estructura de la página web que se desea extraer los datos.

Paso numerado con círculo verde **1**:

**Explora la página web**
Interactúa con la página web para observar sus características

## Slide 22

Paso numerado con círculo azul oscuro **2**:

**Descifra la información de la URL**

Una URL contiene mucha información relevante para un programador (no tanto para el usuario)

Primer ejemplo, con dos llaves/subrayados celestes que anotan tramos de la URL:

```
https://realpython.github.io/fake-jobs/ | jobs/senior-python-developer-0.html
        ^ URL Base                        ^ Ubicación específica del sitio
```

Segundo ejemplo, con un subrayado celeste bajo el tramo tras el `?`:

```
https://au.indeed.com/jobs?q=software+developer&l=Australia
                          ^ Parámetros de consulta
```

- Empieza con el símbolo `?`
- Cada parámetro tiene la forma `key=value`
- Los parámetros están separados por el símbolo `&`

## Slide 23

Paso numerado con círculo rojo **3**:

**Inspecciona el código de la página web**

Utiliza las herramientas del explorador para inspeccionar el código

- *MAC:* Cmd + Alt + I
- *Windows/Linux:* Ctrl + Shift + I

**Captura de pantalla** del sitio de práctica "Fake Python — Fake Jobs for Your Web Scraping" con las DevTools de Chrome abiertas al costado:

- Panel izquierdo: listado de ofertas en tarjetas — "Senior Python Developer / Payne, Roberts and Davis / Stewartbury, AA / 2021-04-08" con botones **Learn** y **Apply**; luego "Energy engineer / Vasquez-Davidson / Christopherville, AA / 2021-04-08"; luego "Legal executive / Jackson, Chambers and Levy / Port Ericaburgh, AA". Sobre la lista, un tooltip de selección azul indica `div#ResultsContainer.columns.is-multiline  480 × 261.80`.
- Panel derecho: pestaña **Elements** (junto a Console, Sources, Network) con el árbol DOM expandido y la línea `<div id="ResultsContainer" class="columns is-multiline">` resaltada en azul. Se ven anidados `<section class="section">`, `<div class="container">`, `<div class="column is-half">`, `<div class="card">`, `<div class="card-content">`, `<div class="media">`, `<div class="media-content">`, `<h2 class="title is-5">Senior Python Developer</h2>`, `<h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>`, `<div class="content">`, `<p class="location">Stewartbury, AA</p>` y `<p class="is-small has-text-grey"><time datetime="2021-04-08">2021-04-08</time></p>`.
- Abajo, breadcrumb del DOM (`body > section.section > div.container > div#ResultsContainer.columns.is-multiline`) y la barra de pestañas **Styles / Computed / Layout / Event Listeners / DOM Breakpoints / Properties**.

## Slide 24

Chevrons: **1. Inspeccionar la página** → **2. Descargar el contenido de la página** (activo)

Para el paso 2 usaremos la librería **requests**. Sin embargo es importante tener en cuenta:

Tres cajas con borde celeste, en columnas:

| Websites Estáticas | Websites Escondidas | Websites Dinámicas |
|---|---|---|
| El servidor que aloja la website devuelve documentos HTML que ya contienen **todos los datos** que podrá ver como usuario. | Cierta información de la website está escondida y se **necesita autenticación** para la extracción. | Es posible que el servidor no devuelva ningún HTML. En su lugar, se podría recibir **código JavaScript** como respuesta el cual tiene otro proceso de scraping. |

## Slide 25

Chevrons: **1. Inspeccionar la página** → **2. Descargar el contenido de la página** → **3. Parsear HTML** (activo)

Dos tarjetas grises:

- **Scraping HTML Websites (estáticas y dinámicas)**
  - Usaremos las librerías Scrapy y Beautiful Soup.
  - Ícono de un archivo con etiqueta roja "HTML" y llaves `{ }`.
- **Scraping Java Script**
  - Usaremos la librería Selenium
  - Logo amarillo de **JS**.

## Slide 26

Separador de sección.

**5. Beautiful Soup**

## Slide 27

**Beautiful Soup**

- Librería para trabajar con documentos HTML y XML. **Genera un árbol que se utiliza para recorrer, buscar e identificar elementos. Y así poder extraer datos de la web.**
- Tiene las siguientes características:
  - Puede analizar documentos con etiquetas rotas, incompletas, mal escritas o faltantes.
  - A diferencia de otros analizadores, permite manejar atributos duplicados y de valores múltiples.
  - También se pueden analizar porciones o secciones específicas seleccionadas del contenido, ahorrando memoria y tiempo.
  - La codificación basada en documentos se maneja automáticamente. Los detalles de codificación también se pueden proporcionar al constructor de Beautiful Soup.

## Slide 28

Portada de laboratorio.

**U2_L2: Web Parsing usando Python**

Foto decorativa de estudiantes en laboratorio.

## Slide 29

Slide sin título: ejemplo HTML ("The Dormouse's story") y su árbol DOM equivalente.

A la izquierda, código HTML (coloreado tipo editor); el texto se recorta ligeramente en el borde derecho:

```html
<html>
  <head><title>The Dormouse's story</title></head>
  <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
      <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
      <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
      and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
    <h1>Secret agents</h1>
    <ul>
      <li data-id="10784">Jason Walters, 003: Found dead in "A View to a Kill".</li>
      <li data-id="97865">Alex Trevelyan, 006: Agent turned terrorist leader; James' nemesis in…
      <li data-id="45732">James Bond, 007: The main man; shaken but not stirred.</li>
    </ul>
  </body>
</html>
```

A la derecha, el **árbol** dibujado con conectores verdes, con raíz **BODY** y sus hijos en orden:

- `P.title`
  - `B`
- `P.story`
  - `A.sister`
  - `A.sister`
  - `A.sister`
- `P.story`
- `H1`
- `UL`
  - `LI`
  - `LI`
  - `LI`

## Slide 30

Portada de laboratorio.

**U2_L3: Web Crawler**

Foto decorativa de estudiantes en laboratorio (misma que la slide 28).
