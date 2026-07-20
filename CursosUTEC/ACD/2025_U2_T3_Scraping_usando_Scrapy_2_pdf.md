---
curso: ACD
titulo: [2025] U2_T3 Scraping usando Scrapy-2
slides: 28
fuente: [2025] U2_T3 Scraping usando Scrapy-2.pdf
---

Scraping usando Scrapy

   DS3021 Análisis Computacional de Datos




                                     Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Al finalizar esta sesión el estudiante
                     aplicará   el   framework   Scrapy   para
                     extraer datos de páginas web.
U2_L4: Crawler usando
       Scrapy
Parte I: Configuración y
creación de proyecto
                    Paso 0: Instalar Scrapy

Scrapy es uno de los pocos frameworks de web scraping de código abierto escritos en
Python que permite una adaptación dinámica, un alcance basado en proyectos y
extensibilidad modular para tareas de rastreo web. Para ello, creamos una carpeta de
proyecto, luego en la terminal creamos y activamos un entorno virtual e instalamos scrapy.




                                                                          https://scrapy.org/
  Paso 1: Para crear un proyecto scrapy startproject [projectname]



Ubicación donde fue
creado:
Paso 2: Dentro de la carpeta Bookscrapy, Scrapy crea la sub-carpeta
books y el archivo de configuración (por default) scrapy.cfg
Otros archivos creados:

 ●    items.py: Un elemento es como un diccionario de Python que contiene
      claves y valores (columna y valor). Para obtener más detalles, visite
      https://docs.scrapy.org/en/latest/topics/items.html.

 ●    pipelines.py: Después de recopilar datos, los elementos extraídos se
      envían a un pipeline para realizar acciones adicionales, como limpiar y
      enviar.       Para       obtener         más        detalles,    visite
      https://docs.scrapy.org/en/latest/topics/item-pipeline.html.

 ●    settings.py: Las configuraciones relacionadas con el proyecto se
      pueden controlar y agregar. Para obtener más detalles, visite
      https://docs.scrapy.org/en/latest/topics/settings.html.

 ●    middlewares.py: Podemos especificar algunos hooks o extensiones
      que pueden realizar tareas adicionales con spiders (procesamiento de
      entradas      y     salidas).     Visite     para     mayor      detalle
      https://docs.scrapy.org/en/latest/topics/spider-middleware.html.
Paso 3: Creación de un SPIDER


Spider
 ●   Es una clase en Python que contiene código utilizado para la lógica de
     recolección de datos y scraping.
 ●   Pueden existir múltiples clases de spiders dirigidas a actividades de
     scraping específicas.
 ●   Comandos como scrapy list y scrapy list spider enumeran los spiders de
     un proyecto.
 ●   Visite                 para                    mayor                 detalle
     https://docs.scrapy.org/en/latest/intro/tutorial.html?highlight=Spider#our-
     first-spider
  A

  1.   Asegurate estar en el folder books de bookScrapy
  2.   Usamos el siguiente comando: scrapy genspider
       booklist books.toscrape.com                        B

       Este comando crea un spider booklist.py dentro
       de la subcarpeta bookScrapy\books\spiders, que
       contiene un código por default con
       books.toscrape.com configurado para el
       argumento allowed_domains.



Paso 3: Creación de un SPIDER
         Un spider está formado por:
SPIDER    ● name: Nombre único que identifica al Spider.
          ● start_urls: Lista inicial de requests
          ● parse(): Método que extrae los datos como dicts y
               también encuentra nuevas URL para seguir creando
               nuevas solicitudes (requests) a partir de ellas.


         Run a Spider:

         Aseguráte estar en top level directory y ejecuta en la terminal:
                              scrapy crawl name
         E.g. scrapy crawl booklist
Parte II: Scraping usando
Scrapy
U2_L4: Scraping usando Scrapy

Para el desarrollo de un crawler con Scrapy se seguirá los siguientes
pasos:

  1.   Buscaremos en el sitio http://books.toscrape.com todos los
       detalles de un libro en todas las páginas del sitio.
  2.   Para cada libro, se extraerá campos como: título, precio,
       calificación, URL e imagen.
  3.   Después de recopilar la URL del libro en el paso 2, a través de
       la url y extraerá campos: categoría, UPC y Num_review
       (número de reseñas).
  4.   Repetiremos los pasos 2 y 3 para todos los libros y
       analizaremos todas las páginas disponibles.
  5.   Exportamos todos los datos recopilados a archivos JSON y CSV.
                               Creando un item

Un item normalmente se entiende como el
nombre de una columna o la clave para un objeto
de un diccionario que se utiliza para recopilar
valores para implementar en el spider.

El archivo items.py contiene       una clase
predeterminada BooksItem que       implementa
scrapy.Item.
Creando un item   B   Define cada dato que se necesita extraer
                      dentro de BooksItem


A
                        Implementar un spider

Con la planificación y recopilación de items, implementaremos el spider para usar items.py y
continuaremos con la implementación del código dentro de la función parse(self, response)

               A
Para extraer los datos de cada libro utilizaremos xpath
"//article[@class='product_pod']"
Implementar un spider
                            Exportar los datos


Los comandos para exportar los datos son:
                      scrapy crawl booklist –o bookRecords.csv
                     scrapy crawl booklist –o bookRecords.json


Estos comandos ejecutan el spider booklist y exportan los datos extraídos como
columnas o BooksItem a CSV y JSON. Estos archivos estarán disponibles en la carpeta
del proyecto.

                         Deploying a web crawler
El deployed crawler se beneficia de múltiples características del servidor (como tener acceso en cualquier momento y
lugar, velocidad y amplio almacenamiento), así como de su naturaleza dinámica.

Podemos elegir cualquier plataforma en la nube, servidor web o servicio basado en Internet para cargar nuestro
código y ejecutarlo. La mayoría de estos servicios no son 100% gratuitos; tenemos que pagar una determinada
cantidad por la configuración y los servicios deseados.

Scrapy, desde el principio, ha sido famoso por su arquitectura. Existían y siguen existiendo múltiples plataformas
basadas en web que permiten a los usuarios ejecutar sus proyectos basados en Scrapy. Uno de ellos es Scrapinghub
(ahora Zyte). Zyte Scrapy Cloud (https://www.zyte.com/scrapy-cloud/) proporciona muchas infraestructuras
adicionales gratuitas para Scrapy y otros proyectos.
                  Deploying a web crawler

1. Crea una cuenta en https://app.zyte.com/.
2. Una vez registrado y logueado, se mostrará un dashboard.
                         Deploying a web crawler



3. Click en Create Project con el nombre de
BooksToScrape.
4. Una vez que el proyecto ha sido creado, Zyte te
enviará a la sección Deploy
                         Deploying a web crawler



5. Instala shub usando la API Key (ve la imagen      A
de tu plataforma)
6. En el top-level directory, ejecuta shub deploy
XXXXX.
Una vez ejecutado, se podrá ver el historial en la
plataforma Zyte y también se crearán dos
archivos nuevos en tu Proyecto: scrapinghub.yml
y setup.py
    Deploying a web crawler

                          C
B
                          Deploying a web crawler

7. Ir a la sección Dashboard, se podrá
observar nuestro spider Booklist. Al
hacer click en el spider, se puede
observar sus detalles.
8. Al ejecutar el spider, se puede observar los items que está extrayendo en la sección Running
Una vez terminado el
crawler, se podrá ver los
items y por lo tanto,
descargar, publicar, etc.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
