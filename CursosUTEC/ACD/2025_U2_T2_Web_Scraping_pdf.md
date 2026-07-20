---
curso: ACD
titulo: [2025] U2_T2 Web Scraping
slides: 30
fuente: [2025] U2_T2 Web Scraping.pdf
---

  Web Scraping

DS3021 Análisis Computacional de Datos




                                  Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Aplicar técnicas de web scraping para el
                     procesamiento     de    extracción    y
                     recolección de datos.
1.
     Web Scraping
                          Web Scraping
                           Definición

●   Se refiere netamente a la extracción de datos desde una website
●   Se pueden crear procesos autónomos (bots o web crawlers) para
    obtener conjuntos de datos
●   El proceso de web scraping consta de dos partes:
     ○   Fetching (conectar y descargar de la web)
     ○   Extraction data (parsear la data, …)
Imagen Tomada del Libro Hands-On Web Scraping with Python - Second Edition
                                                         Anish Chapagain
                                Retos
                             Web Scraping


Existen varios retos al hacer web scraping, sin embargo dos principales son:
 ●   Variedad: Cada website es diferente (semi estructurado). Si bien
     encontramos estructuras generales, cada website es única y necesitará
     una personalización al momento de la extracción.
 ●   Durabilidad: Las websites cambian constantemente. El web scraper
     que creaste puede servir una vez o varias pero no eternamente.
2.
 HTML y CSS
                   HTML
              Hypertext markup
                 Language


●   HTML define y contiene el contenido de una
    página web.
●   Los datos que se pueden extraer y cualquier
    fuente de datos que revele información se
    pueden encontrar dentro de las páginas
    HTML dentro de un conjunto de
    instrucciones predefinido o elementos de
    marcado llamados etiquetas (tags).
●   Las etiquetas HTML normalmente son un
    marcador de posición con nombre que lleva
    ciertos atributos predefinidos, por ejemplo,
    <a>, <b>, <table>, <img> y <script>.
Los elementos HTML también se pueden anidar en una estructura
similar a un árbol con una jerarquía padre-hijo, de la siguiente
manera:
                HTML
          Atributos Globales

●   id: los valores de este atributo deben ser únicos para
    el elemento al que se aplican
●   class: los valores de este atributo se usan
    principalmente con CSS, se pueden usar con
    múltiples elementos
●   style: especifica estilos CSS en línea para un
    elemento
●   lang: Esto ayuda a identificar el idioma del texto.
                                       CSS

●   CSS describe las propiedades de visualización de los elementos HTML y la apariencia de
    las páginas web. CSS se utiliza para diseñar y proporcionar la apariencia y presentación
    deseadas de los elementos HTML.
●   Al utilizar CSS, los desarrolladores/diseñadores pueden controlar el diseño y la
    presentación de un documento web. CSS se puede aplicar a un elemento distinto de una
    página o se puede incrustar en un documento independiente.
●   Los detalles de estilo se pueden describir usando la etiqueta <style>.
La etiqueta <style> puede contener detalles dirigidos a
elementos repetidos y diversos en un bloque.




                                                          Revisar: https://www.w3.org/Style/CSS/
                                                                https://www.w3schools.com/css/
3.
 Búsqueda y
 Procesamiento de
 Documentos en la Web
                                    DOM
                           The Document Object Model

●   Un árbol de elementos para lenguajes de
    marcado como HTML.
●   Entender este árbol es elemental para el
    proceso de extracción de datos.
●   Los selectores XPath y CSS se utilizan
    para navegar a lo largo del DOM y se
    utilizan para buscar el contenido deseado
    en los nodos o elementos encontrados.
                                     XPath


●   XPath es como una ruta (las expresiones se crean utilizando y representando elementos
    HTML y nodos XML) que identifica nodos en los documentos.
●   Las expresiones XPath también se identifican como:
     ○   Absolutas
     ○   Relativas
                         XPath
                        Absolutas

●   Esta expresión representa una ruta completa desde el elemento
    raíz hasta el elemento deseado o de destino.
●   En un documento HTML, comienza con /html y tiene el aspecto
    /html/body/div[1]/div/div[2]/div/span/p[1].
●   Los elementos individuales, como div y p, generalmente se
    identifican por su posición y se representan mediante un número
    de índice, como [1] o [2].
                    XPath
                   Relativas

●   Esta expresión es algo más corta y más legible en
    comparación con una ruta absoluta y, a menudo, se
    prefiere a las expresiones absolutas.
●   Comienza    con   ciertos   elementos   elegidos   o
    seleccionados y termina con el elemento deseado,
    por                                        ejemplo,
    //*[@id="answer"]/div/span/p[@class="text"].
           CSS selectors

●   Los selectores CSS son patrones definidos que
    utiliza CSS para seleccionar elementos.
●   De manera similar a las expresiones XPath, que
    se utilizan para buscar e identificar elementos,
    los selectores CSS se utilizan para seleccionar
    o buscar elementos HTML y definir un estilo
    para ellos.
4.
 Pasos para hacer web
 scraping
        Pasos para hacer Web Scraping



                   2. Descargar el
1. Inspeccionar
                    contenido de     3. Parsear HTML
la página
                      la página

1. Inspeccionar    El primer paso consiste en entender la estructura de la
la página          página web que se desea extraer los datos.




                  Explora la página web

                  Interactúa con la página web para observar sus características
Descifra la información de la URL

Una URL contiene mucha información relevante para un
programador (no tanto para el usuario)

https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html

             URL Base                      Ubicación específica del sitio



 https://au.indeed.com/jobs?q=software+developer&l=Australia

                                  Parámetros de consulta
                    ●   Empieza con el símbolo ?
                    ●   Cada parámetro tiene la forma key=value
                    ●   Los parámetros están separados por el símbolo &
Inspecciona el código de la
página web

Utiliza las herramientas del
explorador para inspeccionar el
código

MAC: Cmd + Alt + I
Windows/Linux: Ctrl + Shift + I
                          2. Descargar el
   1. Inspeccionar
                           contenido de
   la página
                             la página



Para el paso 2 usaremos la librería requests. Sin embargo es importante tener en cuenta:



    Websites Estáticas                      Websites Escondidas     Websites Dinámicas



   El servidor que aloja la             Cierta información de la   Es    posible   que   el
   website        devuelve              website está escondida     servidor no devuelva
   documentos HTML que                  y       se     necesita    ningún HTML. En su
   ya contienen todos los               autenticación para la      lugar, se podría recibir
   datos que podrá ver                  extracción.                código        JavaScript
   como usuario.                                                   como respuesta el cual
                                                                   tiene otro proceso de
                                                                   scraping.
                     2. Descargar el
1. Inspeccionar
                      contenido de      3. Parsear HTML
la página
                        la página




       Scraping HTML Websites
                                                               Scraping Java Script
        (estáticas y dinámicas)
                                                          ●   Usaremos la librería
   ●    Usaremos las librerías Scrapy
                                                              Selenium
        y Beautiful Soup.
5.
 Beautiful Soup
                               Beautiful Soup

●   Librería para trabajar con documentos HTML y XML. Genera un árbol que se utiliza
    para recorrer, buscar e identificar elementos. Y así poder extraer datos de la web.
●   Tiene las siguientes características:
      ○ Puede analizar documentos con etiquetas rotas, incompletas, mal escritas o
          faltantes.
      ○ A diferencia de otros analizadores, permite manejar atributos duplicados y de
          valores múltiples.
      ○ También se pueden analizar porciones o secciones específicas seleccionadas
          del contenido, ahorrando memoria y tiempo.
      ○ La codificación basada en documentos se maneja automáticamente. Los
          detalles de codificación también se pueden proporcionar al constructor de
          Beautiful Soup.
U2_L2: Web Parsing usando
         Python
U2_L3: Web Crawler

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
