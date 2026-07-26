---
curso: ACD
titulo: [2025] U2_T3 Scraping usando Scrapy-2
slides: 28
fuente: [2025] U2_T3 Scraping usando Scrapy-2.pdf
---

## Slide 1

Portada. Título **Scraping usando Scrapy**, subtítulo *DS3021 Análisis Computacional de Datos*. Imagen de fondo decorativa (silueta con equipo, túnel tecnológico azul).

## Slide 2

**Objetivo de sesión**

> Al finalizar esta sesión el estudiante aplicará el framework Scrapy para extraer datos de páginas web.

Foto de dos personas trabajando con tinte azul: decorativa.

## Slide 3

Slide separadora: **U2_L4: Crawler usando Scrapy**. Fondo con foto de laboratorio: decorativa.

## Slide 4

Slide separadora: **Parte I: Configuración y creación de proyecto**. Imagen de mano robótica y globo terráqueo: decorativa.

## Slide 5

**Paso 0: Instalar Scrapy**

Scrapy es uno de los pocos frameworks de web scraping de código abierto escritos en Python que permite una adaptación dinámica, un alcance basado en proyectos y extensibilidad modular para tareas de rastreo web. Para ello, creamos una carpeta de proyecto, luego en la terminal creamos y activamos un entorno virtual e instalamos scrapy.

Enlace: https://scrapy.org/

**Captura de terminal PowerShell (Windows, `D:\bookScrapy`):**

```powershell
PS D:\bookScrapy> python --version
Python 3.10.0
PS D:\bookScrapy> python -m venv venv
PS D:\bookScrapy> .\venv\Scripts\activate
(venv) PS D:\bookScrapy> pip install scrapy
Collecting scrapy
  Using cached Scrapy-2.12.0-py2.py3-none-any.whl (311 kB)
Collecting cssselect>=0.9.1
  Using cached cssselect-1.3.0-py2.py3-none-any.whl (18 kB)
Collecting parsel>=1.5.0
  Using cached parsel-1.10.0-py2.py3-none-any.whl (17 kB)
Collecting PyDispatcher>=2.0.5
```

## Slide 6

**Paso 1:** Para crear un proyecto `scrapy startproject [projectname]`

Captura de terminal con dos flechas azules apuntando al comando (`scrapy startproject books`) y una tercera flecha, rotulada "Ubicación donde fue creado:", que apunta a la ruta de salida:

```powershell
PS D:\bookScrapy> scrapy startproject books
New Scrapy project 'books', using template directory 'C:\Users\JOSE\anaconda3\Lib\site-packages\scrapy\templates\project', created in:
    D:\bookScrapy\books

You can start your first spider with:
    cd books
    scrapy genspider example example.com
```

## Slide 7

**Paso 2:** Dentro de la carpeta **Bookscrapy**, Scrapy crea la sub-carpeta **books** y el archivo de configuración (por default) **scrapy.cfg**

Captura del explorador de VS Code (árbol de archivos) con dos flechas azules: una apunta a la carpeta `books`, otra a `scrapy.cfg`.

```
BOOKSCRAPY
└── books
    └── books
        ├── __pycache__/
        ├── spiders/
        ├── __init__.py
        ├── items.py
        ├── middlewares.py
        ├── pipelines.py
        └── settings.py
    ├── scrapy.cfg
    └── venv/
```

## Slide 8

**Otros archivos creados:**

- **items.py:** Un elemento es como un diccionario de Python que contiene claves y valores (columna y valor). Detalle: https://docs.scrapy.org/en/latest/topics/items.html
- **pipelines.py:** Después de recopilar datos, los elementos extraídos se envían a un pipeline para realizar acciones adicionales, como limpiar y enviar. Detalle: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
- **settings.py:** Las configuraciones relacionadas con el proyecto se pueden controlar y agregar. Detalle: https://docs.scrapy.org/en/latest/topics/settings.html
- **middlewares.py:** Podemos especificar algunos hooks o extensiones que pueden realizar tareas adicionales con spiders (procesamiento de entradas y salidas). Detalle: https://docs.scrapy.org/en/latest/topics/spider-middleware.html

Franja lateral con foto de estudiantes: decorativa.

## Slide 9

**Paso 3: Creación de un SPIDER**

**Spider**
- Es una clase en Python que contiene código utilizado para la lógica de recolección de datos y scraping.
- Pueden existir múltiples clases de spiders dirigidas a actividades de scraping específicas.
- Comandos como **scrapy list** y **scrapy list spider** enumeran los spiders de un proyecto.
- Visite para mayor detalle https://docs.scrapy.org/en/latest/intro/tutorial.html?highlight=Spider#our-first-spider

A la derecha, un ícono/ilustración de araña azul (decorativo temático).

## Slide 10

**Paso 3: Creación de un SPIDER**

1. Asegúrate estar en el folder **books** de **bookScrapy**
2. Usamos el siguiente comando: **scrapy genspider booklist books.toscrape.com**

Este comando crea un spider **booklist.py** dentro de la subcarpeta **bookScrapy\books\spiders**, que contiene un código por default con **books.toscrape.com** configurado para el argumento **allowed_domains**.

**Callout A** — captura de terminal, con el prompt resaltado en rojo (`(venv) PS D:\bookScrapy\books>`) para enfatizar el directorio correcto:

```powershell
(venv) PS D:\bookScrapy\books> scrapy genspider booklist books.toscrape.com
Created spider 'booklist' using template 'basic' in module:
  books.spiders.booklist
```

**Callout B** — captura de VS Code: árbol `books/spiders/booklist.py` seleccionado y el editor con el código generado por defecto:

```python
import scrapy


class BooklistSpider(scrapy.Spider):
    name = "booklist"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
```

## Slide 11

**SPIDER**

Un spider está formado por:
- **name**: Nombre único que identifica al Spider.
- **start_urls**: Lista inicial de requests
- **parse()**: Método que extrae los datos como dicts y también encuentra nuevas URL para seguir creando nuevas solicitudes (requests) a partir de ellas.

**Run a Spider:**
Asegúrate estar en top level directory y ejecuta en la terminal:
`scrapy crawl name` — E.g. **scrapy crawl booklist**

A la izquierda, misma captura de VS Code que la slide 10 (árbol BOOKSCRAPY + `booklist.py` con `import scrapy`, clase `BooklistSpider`, name/allowed_domains/start_urls y `def parse(self, response): pass`).

## Slide 12

Slide separadora: **Parte II: Scraping usando Scrapy**. Foto de laboratorio con pipeta: decorativa.

## Slide 13

**U2_L4: Scraping usando Scrapy**

Para el desarrollo de un crawler con Scrapy se seguirá los siguientes pasos:

1. Buscaremos en el sitio http://books.toscrape.com todos los detalles de un libro en todas las páginas del sitio.
2. Para cada libro, se extraerá campos como: **título, precio, calificación, URL e imagen**.
3. Después de recopilar la URL del libro en el paso 2, a través de la url y extraerá campos: **categoría, UPC y Num_review (número de reseñas)**.
4. Repetiremos los pasos 2 y 3 para todos los libros y analizaremos todas las páginas disponibles.
5. Exportamos todos los datos recopilados a archivos JSON y CSV.

Foto lateral de expositor frente a pizarra: decorativa.

## Slide 14

**Creando un item**

Un **item** normalmente se entiende como *el nombre de una columna* o la clave para un objeto de un diccionario que se utiliza para recopilar valores para implementar en el spider.

El archivo **items.py** contiene una clase predeterminada **BooksItem** que implementa **scrapy.Item**.

Captura de VS Code de `books > items.py` con el contenido por defecto:

```python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
```

## Slide 15

**Creando un item**

**Callout A** (izquierda): la misma captura de `items.py` por defecto de la slide 14.

**Callout B** (derecha): "Define cada dato que se necesita extraer dentro de **BooksItem**". Captura de VS Code `books > items.py > BooksItem`:

```python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    num_review = scrapy.Field()
    upc = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    stock = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    pass
```

## Slide 16

**Implementar un spider**

Con la planificación y recopilación de **items**, implementaremos el spider para usar **items.py** y continuaremos con la implementación del código dentro de la función **parse(self, response)**

**Callout A** — captura de `books > spiders > booklist.py` con el esqueleto aún vacío:

```python
import scrapy


class BooklistSpider(scrapy.Spider):
    name = "booklist"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
```

## Slide 17

Para extraer los datos de cada libro utilizaremos xpath **"//article[@class='product_pod']"**

Tres capturas lado a lado:

1. **Navegador con books.toscrape.com** y DevTools resaltando un producto: banner amarillo "Warning! This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning."; tooltip de inspección `article.product_pod  152.99 × 370`. Se ven tres tarjetas de libro: "A Light in the Attic" (★★★☆☆ aprox., £51.77, In stock), "Tipping the Velvet" (★☆☆☆☆, £53.74, In stock), "Soumission" (★☆☆☆☆, £50.10, In stock), cada una con botón "Add to basket".
2. **Panel HTML de DevTools**: jerarquía `div.col-sm-8 col-md-9` → `div.page-header action` → `div#messages` → `div#promotions` → `form.form-horizontal` → `section` → `div.alert alert-warning` → `div` → `ol.row` → lista de `<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">`, con el primero expandido y resaltado mostrando `<article class="product_pod">…</article>`.
3. **VS Code** (`books > books > spiders > booklist.py > BooklistSpider > parse`), con una flecha señalando el import de items y otra señalando el xpath:

```python
import scrapy
from books.items import BooksItem


class BooklistSpider(scrapy.Spider):
    name = "booklist"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        #Extraer la lista de libros de una página
        books = response.xpath('//article[@class="product_pod"]')
        print("Hay libros", len(books), "en la pagina")
```

## Slide 18

**Implementar un spider**

Captura completa del método `parse`:

```python
def parse(self, response):

    books = response.xpath('//article[@class="product_pod"]')
    print("Hay",len(books),"libros en la pagina")

    for book in books:
        title = book.xpath('.//h3/a/@title').get()
        price = book.xpath('.//p[@class="price_color"]/text()').get()
        availability = book.xpath('.//p[@class="instock availability"]/text()').getall()
        rating_class = book.xpath('.//p[contains(@class,"star-rating")]/@class').get()

        # Limpieza del texto
        availability = ''.join([text.strip() for text in availability if text.strip() != ''])
        rating = rating_class.split()[-1] if rating_class else 'Unknown'

        yield {
            'title': title,
            'price': price,
            'availability': availability,
            'rating': rating
        }

    next_page = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
    if next_page:
        next_page_url = response.urljoin(next_page)
        yield scrapy.Request(url=next_page_url, callback=self.parse)
```

## Slide 19

**Exportar los datos**

Los comandos para exportar los datos son:

```
scrapy crawl booklist –o bookRecords.csv
scrapy crawl booklist –o bookRecords.json
```

Estos comandos ejecutan el spider **booklist** y exportan los datos extraídos como columnas o **BooksItem** a CSV y JSON. Estos archivos estarán disponibles en la carpeta del proyecto.

## Slide 20

Slide sin texto propio (solo captura). Muestra VS Code con el explorador BOOKSCRAPY (books, spiders, `booklist.py`, `items.py`, `middlewares.py`, `pipelines.py`, `settings.py`, `bookRecords.csv`, `scrapy.cfg`) y una flecha azul grande apuntando a **bookRecords.csv**. A la derecha, el archivo CSV abierto en el editor, líneas 485–513, con filas del tipo:

```
//books.toscrape.com/../media/cache/8b/10/8b120daec94d1ea9c6fc36dd3ec1c1fe.jpg,0,£46.33,Two,,Unreasonab…
…media/cache/98/c2/98c2e95c5fd1a4e7cd5f2b63c52826cb.jpg,0,£37.33,Three,,Under the Tusc…
…media/cache/1d/1f/1d1fbd89f0290275b9166877663ee9f5.jpg,0,£53.63,Two,,32 Yolks
…£25.37,Five,,What Happened…  …£12.08,Three,,You Are a B…  …£22.14,Two,,Wildlife of New…
…£44.48,Five,,"""Most Blesse…  …£56.91,Four,,Between the…  …£55.06,Four,,Being Morta…
…£19.22,Two,,Brazen: The…  …£11.45,Three,,Brilliant Bea…  …£55.65,Five,,Future Sho…
…£37.51,Four,,Death by Leisu…  …£28.41,One,,Diary of a Citi…  …£43.64,One,,Ender's Game
…£52.86,Two,,Heaven is for R…  …£32.38,One,,Playing from…  …£34.41,Two,,Raymie Nighti…
…£51.74,One,,"Rich Dad, Poo…  …£52.87,Three,,"Shrunken T…  …£40.20,Four,,Sister Dear,7f…
…£20.90,Three,,"Sit, Stay, L…  …£20.90,Two,,Steal Like an A…  …£20.12,Five,,Team of I…
…£33.17,Four,,The 7 Habits o…  …£52.30,Five,,The Bachelor G…  …£39.55,One,,The Faith of…
…£32.34,Two,,The Art Book,4b8fa5…
```

Es decir: columnas con URL de imagen, num_review (0), precio en £, rating textual (One…Five), y título.

## Slide 21

**Deploying a web crawler**

El deployed crawler se beneficia de múltiples características del servidor (como tener acceso en cualquier momento y lugar, velocidad y amplio almacenamiento), así como de su naturaleza dinámica.

Podemos elegir cualquier plataforma en la nube, servidor web o servicio basado en Internet para cargar nuestro código y ejecutarlo. La mayoría de estos servicios no son 100% gratuitos; tenemos que pagar una determinada cantidad por la configuración y los servicios deseados.

Scrapy, desde el principio, ha sido famoso por su arquitectura. Existían y siguen existiendo múltiples plataformas basadas en web que permiten a los usuarios ejecutar sus proyectos basados en Scrapy. Uno de ellos es Scrapinghub (ahora Zyte). Zyte Scrapy Cloud (https://www.zyte.com/scrapy-cloud/) proporciona muchas infraestructuras adicionales gratuitas para Scrapy y otros proyectos.

Banda superior con foto de equipo de trabajo: decorativa.

## Slide 22

**Deploying a web crawler**

1. Crea una cuenta en https://app.zyte.com/
2. Una vez registrado y logueado, se mostrará un dashboard.

Captura del dashboard de Zyte: barra superior oscura con logo "zyte", buscador y "Welcome back, Yamilet Serrano Ll..."; menú lateral con **Dashboard** y sección TOOLS (Zyte API, Scrapy Cloud). Área central "Tools" con tres tarjetas:

| Tarjeta | Descripción | Acción |
|---|---|---|
| Zyte API | Return HTML efficiently from any website using a single API. | Try free with $5 credit |
| Scrapy Cloud | Deploy, run and scale your web spiders | Create your first project |
| Smart Proxy Management | Make site bans a thing of the past with Zyte API Proxy Mode. | Try free with $5 credit |

## Slide 23

**Deploying a web crawler**

3. Click en **Create Project** con el nombre de **BooksToScrape**.
4. Una vez que el proyecto ha sido creado, Zyte te enviará a la sección **Deploy**

Captura del formulario "Start A Project": campo **Project Name** con el valor `BooksToScrape`; sección **What To Deploy** con dos opciones — "Your Own Code · Deploy your own web scraping code to the cloud." (botón en estado **Selected**) y "Zyte's AI-Powered Spiders · Use our no-code solution for web scraping." (etiqueta NEW, botón Select). Abajo botón morado **Create project**.

## Slide 24

**Deploying a web crawler**

5. Instala shub usando la API Key (ve la imagen de tu plataforma)
6. En el top-level directory, ejecuta *shub deploy XXXXX*.
Una vez ejecutado, se podrá ver el historial en la plataforma Zyte y también se crearán dos archivos nuevos en tu Proyecto: **scrapinghub.yml** y **setup.py**

**Callout A** — captura del panel "Command Line — Deploy code from your own computer", con pestañas SCRAPY / CUSTOM IMAGE:

```bash
$ pip install shub
$ shub login
API key:
348d196eeb5c44ee8ee17d0990398bf1
$ shub deploy 752022
```

Debajo: "Don't have a project yet? **Clone a public repository**". A la derecha, separador "OR".

## Slide 25

**Deploying a web crawler**

**Callout B** — captura de la pantalla "Deploy Your Code" de Zyte: aviso "…deploying your own code will overwrite your existing spiders and you will not be able to use them again". Panel izquierdo Command Line (mismos comandos: `pip install shub`, `shub login`, API key `348d196eeb5c44ee8ee17d0990398bf1`, `shub deploy 752022`), separador OR, panel derecho **Github** ("Deploy your code directly to Zyte from Github", "Your account is not connected yet", botón **Connect to Github**, enlace Learn more).
Debajo, **Current Deploy**: fila `1` · versión `1716152688` · "yserrano08 deployed 12 seconds ago from Command line" · **1 SPIDERS** · badge verde **SUCCESS**. Y **Deploys History** con la misma fila.

**Callout C** — explorador de VS Code con dos flechas azules apuntando a los archivos nuevos **scrapinghub.yml** y **setup.py**. Árbol: BOOKSCRAPY → books (→ `__pycache__`, spiders [`__pycache__`, `__init__.py`, `booklist.py`], `__init__.py`, `items.py`, `middlewares.py`, `pipelines.py`, `settings.py`), `build/`, `project.egg-info/`, `bookRecords.csv`, `scrapinghub.yml`, `scrapy.cfg`, `setup.py`.

## Slide 26

**Deploying a web crawler**

7. Ir a la sección Dashboard, se podrá observar nuestro spider **Booklist**. Al hacer click en el spider, se puede observar sus detalles.

Captura de la vista "Booklist Spider" en Zyte, con pestañas Details / Settings / Raw Settings y botones **Watch** y **Run** (morado). Tabla **Spider Details**:

| Campo | Valor |
|---|---|
| Name | booklist |
| Type | manual |
| Version | 1716152688 |
| Tags | No tags (botón Edit) |
| Default job units | 1 |
| Total Jobs | 0 |

Debajo, sección **Next (0)** con tabla de columnas Job, Spider, Units, Priority, Added, Wait Time, Wait Reason — "No results found" y botones Cancel/Edit. A la derecha, medidor circular **0 / 1** con "Units Breakdown · Default Group" y leyenda: This Project 0, Others 0, Free 1. Abajo empieza la sección **Running (0)**.

## Slide 27

8. Al ejecutar el spider, se puede observar los items que está extrayendo en la sección **Running**

Captura de la tabla **Running (1)** de Zyte, con checkbox "Show Only Jobs With Comments (0)":

| Job | Spider | Items | Requests | Errors | Logs | Runtime | Started |
|---|---|---|---|---|---|---|---|
| 1/1 | booklist (1716152688) | 258 | 275 | 0 | 319 | 00:01:37 | 2024-05-19 2… |

Botón **Stop** debajo.

## Slide 28

Una vez terminado el crawler, se podrá ver los items y por lo tanto, descargar, publicar, etc.

Captura de la vista **Job 1** en Zyte (proyecto BooksToScrape, "0 spiders, 0 members"; menú lateral: JOBS → Dashboard, Periodic Jobs; SPIDERS → Dashboard, Code & Deploys, Settings; PROJECT → Usage Stats, Activity, Members, Settings; ADDONS → Addons Setup). Pestañas: Job, **Items 1000**, Requests 1051, Log 1168, Stats 24, Console. Botones Watch, **Clone this Job**, **Stop this Job**, y en Job Items: **Download**, **Publish**, **Samples**, filtros (Choose field…, Choose Action…, All Items, Clear, Update, Add Filter, "Show Scraped Fields").

**Item 0** — 2024-05-19 21:15:41 UTC:

| Campo | Valor |
|---|---|
| category | Poetry |
| image | http://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg |
| num_review | 0 |
| price | £51.77 |
| rating | Three |
| title | A Light in the Attic |
| upc | a897fe39b1053632 |
| url | catalogue/a-light-in-the-attic_1000/index.html |

**Item 1** — 2024-05-19 21:15:41 UTC (parcialmente visible): category = Default, image = http://books.toscrape.com/media/cache/66/88/66883b91f68O4b2323c8369131cb7dd1.jpg
