---
curso: ACD
titulo: [2025] U2_T4 Usando Selenium para Web Scraping
slides: 22
fuente: [2025] U2_T4 Usando Selenium para Web Scraping.pdf
---

 Usando Selenium
para Web Scraping
 DS3021 Análisis Computacional de Datos




                                   Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Al finalizar esta sesión el estudiante
                     aplicará Selenium para extraer datos de
                     páginas web.
1.
     Selenium
                      Selenium

Selenium es un framework de código abierto que integra una
variedad de herramientas y bibliotecas que hacen posible
actividades de automatización de navegadores, entre ellas:
  ● Acciones/recuperación de elementos con base en páginas
      web
  ● Pruebas de sitio
  ● Gestión de avisos de alerta y cookies (agregar/eliminar)
  ● Envío de elementos de formulario
  ● Recopilación de datos (web scraping)
De los componentes de Selenium, nosotros usaremos Selenium
WebDriver.
                       Ventajas y Desventajas de Selenium

Selenium admite diferentes navegadores web a través de      Pero también    existen   algunas   limitaciones   o
uno de sus componentes, llamado WebDriver. Hay muchos       desventajas:
beneficios que hacen que Selenium sea popular, los cuales
son:                                                         ●   Trabajar con múltiples pestañas y frameworks
                                                             ●   Baja velocidad de ejecución (dependiendo de la
  ●   Fácil de implementar                                       máquina)
  ●   Soporte para varios navegadores
  ●   Código abierto y gratuito
  ●   Admite pruebas paralelas
  ●   Admite múltiples sistemas operativos (SO)
  ●   Admite múltiples lenguajes (Java, Python, Ruby, PHP
      y otros)
  ●   Hay disponible una enorme colección de documentos
      y recursos.
  ●   Admite servidores remotos y dispositivos en la nube
Componentes de Selenium
2.
 Selenium
 Web Driver
             Selenium Web Driver

WebDriver implementa la lógica de código para navegadores
seleccionados que se requiere durante la automatización.

También es el sistema central que vincula el framework de Selenium
con el navegador y, a menudo, se le llama o se hace referencia como
el driver de Selenium o solo driver. Para obtener información más
detallada, visite este enlace:
https://www.selenium.dev/documentation/webdriver/getting_started/
.
Paso 1: Verificar la versión de Google Chrome
Paso 2: Visita la página https://www.selenium.dev/downloads/ y ve a la sección
Platforms supported by Selenium. Haz click en el browser que utilices.

                                             Creamos una carpeta de proyecto y luego, en la
                                             terminal, creamos y activamos un entorno virtual.




                                             Si la versión de GoogleChrome es mayor 114.0… es
                                             mejor seguir los siguientes pasos:

                                             1. pip uninstall selenium
                                             2. pip install -U selenium==4.11.2
                                             3. pip show selenium (double check)
                                             4. pip install webdriver_manager
U2_L5: Web Scraping usando
        Selenium
https://www.saucedemo.com/

                             Ejercicio

                             Utilizaremos Selenium para completar   de   manera
                             automática el form de la página web.
 Interacciones con los elementos web - Selenium:
 https://www.selenium.dev/documentation/webdriver/elements/interactions/

selenium.webdriver proporciona varios tipos de localizadores de elementos para identificar elementos HTML y atributos
asociados con ellos. Estos localizadores se proporcionan como argumentos para los métodos del controlador:

  ●   find_element(): Devuelve un solo elemento
  ●   find_elements(): Devuelve múltiples o listas de elementos


  ●   By.ID: Busca elementos con el atributo id, por ejemplo,     ●   By.CLASS_NAME: Busca elementos con el atributo de clase,
      driver.find_element(By.ID,"numb1").                             por ejemplo, driver.find_element(By.CLASS_NAME,"email").
  ●   By.NAME: Busca elementos con el atributo nombre, por        ●   By.CSS_SELECTOR: Busca elementos utilizando expresiones
      ejemplo, driver.find_element(By.NAME,"first_name").             de          selector        CSS,        por         ejemplo,
  ●   By.TAG_NAME: Busca elementos con un nombre de                   driver.find_element(By.CSS_SELECTOR,".completed > h2").
      etiqueta,      por      ejemplo,    driver.find_element     ●   By.LINK_TEXT: Busca elementos de los enlaces disponibles y
      (By.TAG_NAME,"h2").                                             aquellos que coincidan con la cadena completa proporcionada.
  ●   By.XPATH: Busca elementos proporcionando expresiones        ●   By.PARTIAL_LINK_TEXT: Busca elementos de los enlaces
      XPath,                     por                  ejemplo,        disponibles y aquellos que coincidan con una parte o porción
      driver.find_element(By.XPATH,"[id='demo’]”).                    de la cadena proporcionada.
Script para configurar el navegador web - Selenium:
Definimos el usuario y contraseña de la página y con find_element(), agregamos sus identificadores en código
HTML inspeccionado la página web para acceder a esta.
Ejecutamos el script anterior y nos llevará al contenido de la página. A continuación, elegiremos dos
productos del catálogo para añadir al carrito de compra.
Usamos nuevamente find_element(), para hacer clic en los botones de agregar producto al carrito y luego para
entrar a la sección donde se encuentra el carrito y darle clic. Si en caso no nos permite hacer esto último,
agregamos option.add_argument("--incognito") para que no se muestre la ventana de cambiar la contraseña.
Al ejecutar el script anterior, se deberían mostrar los productos que fueron agregados al carrito para,
posteriormente, darle clic al botón de chequeo y llevarnos a un apartado con datos personales a completar. Si
en caso no se observe el botón del carrito, cambiar el tamaño de página a 1366×768, 1440×900 o
1280×800.
Completamos los datos personales con valores apropiados identificando el código HTML para cada casilla al
inspeccionar la página web.
Si volvemos a ejecutar el script, veremos que se muestran los datos personales completos y lo que haremos a
continuación será darle clic al botón continuar desde nuestro script.

Completamos el código con los botones para continuar, finalizar y regresar, luego de explorar la página web y
finalmente se nos mostrará una pantalla en donde se da por finalizado el pedido de compra.
Ejercicio


 Utilizaremos la página https://quotes.toscrape.com para hacer web scraping.
 Desarrolle un código basado en driver Selenium que:
  1. Haga log in en la página usando test como palabra clave para ambos campos.
  2. Extraiga todos las citas de los páginas de la web. Recuerde que cada cita, tiene un autor
       y una lista de tags.
  3. Termine con log out.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
