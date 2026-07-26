---
curso: ACD
titulo: [2025] U2_T4 Usando Selenium para Web Scraping
slides: 22
fuente: [2025] U2_T4 Usando Selenium para Web Scraping.pdf
---

## Slide 1

Portada (imagen de fondo decorativa: silueta caminando en un túnel de datos azul).

**Usando Selenium para Web Scraping**
DS3021 Análisis Computacional de Datos

## Slide 2

Slide de objetivo (foto decorativa de dos personas trabajando, teñida de azul).

**Objetivo de sesión**

> Al finalizar esta sesión el estudiante aplicará Selenium para extraer datos de páginas web.

## Slide 3

Slide divisoria de sección (imagen decorativa de mano robótica tocando un globo digital).

**1. Selenium**

## Slide 4

**Selenium**

Selenium es un **framework** de código abierto que integra una variedad de herramientas y bibliotecas que hacen posible actividades de automatización de navegadores, entre ellas:

- Acciones/recuperación de elementos con base en páginas web
- Pruebas de sitio
- Gestión de avisos de alerta y cookies (agregar/eliminar)
- Envío de elementos de formulario
- **Recopilación de datos (web scraping)** (resaltado en negrita)

De los componentes de Selenium, nosotros usaremos **Selenium WebDriver** (resaltado en celeste).

## Slide 5

**Ventajas y Desventajas de Selenium** — layout a dos columnas.

Columna izquierda: Selenium admite diferentes navegadores web a través de uno de sus componentes, llamado **WebDriver**. Beneficios:

- Fácil de implementar
- Soporte para varios navegadores
- Código abierto y gratuito
- Admite pruebas paralelas
- Admite múltiples sistemas operativos (SO)
- Admite múltiples lenguajes (Java, Python, Ruby, PHP y otros)
- Hay disponible una enorme colección de documentos y recursos.
- Admite servidores remotos y dispositivos en la nube

Columna derecha: Pero también existen algunas limitaciones o desventajas:

- Trabajar con múltiples pestañas y frameworks
- Baja velocidad de ejecución (dependiendo de la máquina)

## Slide 6

**Componentes de Selenium**

Figura insertada titulada "SELENIUM COMPONENTS": cuatro tarjetas de colores en fila comparando los componentes. Una flecha azul gruesa apunta hacia arriba a la tercera tarjeta (Selenium WebDriver), indicando que es el que se usará en el curso.

| Selenium IDE (verde azulado) | Selenium RC (verde) | Selenium WebDriver (naranja) ← | Selenium Grid (rojo/terracota) |
|---|---|---|---|
| • Supports only FireFox<br>• Conditional operations are not supported | • Needs separate RC server<br>• API has redundant and confusing commands<br>• No direct browser interaction<br>• Slow execution | • Direct Communication with browser<br>• No need separate server<br>• Simple commands<br>• Faster execution | • Similar architecture as RC<br>• Requires RC server to run in multiple browser and environments |

## Slide 7

Slide divisoria de sección (misma imagen decorativa de mano robótica).

**2. Selenium Web Driver**

## Slide 8

**Selenium Web Driver**

WebDriver implementa la lógica de código para navegadores seleccionados que se requiere durante la automatización.

También es el sistema central que vincula el framework de Selenium con el navegador y, a menudo, se le llama o se hace referencia como **el driver de Selenium** o solo **driver**. Para obtener información más detallada, visite este enlace:
https://www.selenium.dev/documentation/webdriver/getting_started/

## Slide 9

**Paso 1: Verificar la versión de Google Chrome**

Captura de pantalla de la página `chrome://settings` → sección "Acerca de Chrome". Se ve el menú lateral de Configuración (Tú y Google, Autocompletar y contraseñas, Privacidad y seguridad, Rendimiento, Diseño, Motor de búsqueda, Navegador predeterminado, Al iniciar, Idiomas, Descargas, Accesibilidad, Sistema, Restablecer configuración, Extensiones, y **Acerca de Chrome** seleccionado en azul). En el panel derecho, la tarjeta "Google Chrome" muestra "Actualizando Chrome — **Versión 124.0.6367.156 (Build oficial) (arm64)**", señalada por una flecha azul gruesa. Debajo: enlaces Obtener ayuda con Chrome, Informar un problema, Política de Privacidad, y "utec.edu.pe administra tu navegador". Al pie, aviso de copyright 2024 Google LLC y enlaces a Chromium / software de código abierto / Condiciones del Servicio.

## Slide 10

**Paso 2:** Visita la página https://www.selenium.dev/downloads/ y ve a la sección **Platforms supported by Selenium.** Haz click en el browser que utilices.

Izquierda: captura de la sección "Platforms Supported by Selenium" del sitio de Selenium, con un control "+ − Browsers" y la lista de navegadores con su logo y nota:
- **Firefox** — GeckoDriver is implemented and supported by Mozilla, refer to their documentation for supported versions.
- **Internet Explorer** — Only version 11 is supported, and it requires additional configuration.
- **Safari** — SafariDriver is supported directly by Apple, for more information, check their documentation.
- **Opera** — OperaDriver is supported by Opera Software, refer to their documentation for supported versions.
- **Chrome** — ChromeDriver is supported by the Chromium project, please refer to their documentation for any compatibility information.
- **Edge** — Microsoft is implementing and maintaining the Microsoft Edge WebDriver, please refer to their documentation for any compatibility information.

Derecha: Creamos una carpeta de proyecto y luego, en la terminal, creamos y activamos un entorno virtual. Captura de terminal PowerShell:

```powershell
PS D:\storeSelenium2> python -m venv venv
PS D:\storeSelenium2> .\venv\Scripts\activate
```

Si la versión de GoogleChrome es mayor **114.0…** es mejor seguir los siguientes pasos:

1. `pip uninstall selenium`
2. `pip install -U selenium==4.11.2`
3. `pip show selenium` (double check)
4. `pip install webdriver_manager`

## Slide 11

Slide divisoria con foto decorativa (dos estudiantes en laboratorio, teñida de azul).

**U2_L5: Web Scraping usando Selenium**

## Slide 12

https://www.saucedemo.com/

Izquierda: captura de la página de login de **Swag Labs** (saucedemo). Formulario con campos `Username` y `Password` y botón verde **Login**. Debajo, panel negro con:

- **Accepted usernames are:** standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user
- **Password for all users:** secret_sauce

Derecha: **Ejercicio** — Utilizaremos Selenium para completar de manera automática el form de la página web.

## Slide 13

*Interacciones con los elementos web* - Selenium: https://www.selenium.dev/documentation/webdriver/elements/interactions/

**selenium.webdriver** proporciona varios tipos de localizadores de elementos para identificar elementos HTML y atributos asociados con ellos. Estos localizadores se proporcionan como argumentos para los métodos del controlador:

- **find_element():** Devuelve un solo elemento
- **find_elements():** Devuelve múltiples o listas de elementos

Dos columnas de localizadores:

- **By.ID:** Busca elementos con el atributo **id**, por ejemplo, `driver.find_element(By.ID,"numb1")`.
- **By.NAME:** Busca elementos con el atributo **nombre**, por ejemplo, `driver.find_element(By.NAME,"first_name")`.
- **By.TAG_NAME:** Busca elementos con un nombre de etiqueta, por ejemplo, `driver.find_element(By.TAG_NAME,"h2")`.
- **By.XPATH:** Busca elementos proporcionando expresiones XPath, por ejemplo, `driver.find_element(By.XPATH,"[id='demo']")`.
- **By.CLASS_NAME:** Busca elementos con el atributo de clase, por ejemplo, `driver.find_element(By.CLASS_NAME,"email")`.
- **By.CSS_SELECTOR:** Busca elementos utilizando expresiones de selector CSS, por ejemplo, `driver.find_element(By.CSS_SELECTOR,".completed > h2")`.
- **By.LINK_TEXT:** Busca elementos de los enlaces disponibles y aquellos que coincidan con la cadena completa proporcionada.
- **By.PARTIAL_LINK_TEXT:** Busca elementos de los enlaces disponibles y aquellos que coincidan con una parte o porción de la cadena proporcionada.

## Slide 14

*Script para configurar el navegador web* - Selenium:

Captura de VS Code (tema oscuro). Explorador lateral: proyecto `STORESELENIUM` con carpeta `venv` y archivo `main.py`. Editor con `main.py` (líneas 1-24); el bloque de configuración del navegador está recuadrado en blanco:

```python
from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

USER = "standard_user"
PASSWORD = "secret_sauce"

# Configuración de navegador
def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--incognito")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()
```

## Slide 15

Definimos el usuario y contraseña de la página y con **find_element()**, agregamos sus identificadores en código HTML inspeccionado la página web para acceder a esta.

Captura de VS Code con `main.py`. Hay dos recuadros blancos: uno sobre las líneas 8-9 (`USER` / `PASSWORD`) y otro sobre el bloque de login (líneas 21-27), añadido tras `driver.get(...)` y `time.sleep(5)`:

```python
#Login
user_input = driver.find_element(By.ID, "user-name")
user_input.send_keys(USER)
pass_input = driver.find_element(By.ID, "password")
pass_input.send_keys(PASSWORD)
button = driver.find_element(By.ID, "login-button")
button.click()
```

## Slide 16

Ejecutamos el script anterior y nos llevará al contenido de la página. A continuación, elegiremos dos productos del catálogo para añadir al carrito de compra.

Captura del catálogo de Swag Labs con 6 productos en dos columnas, cada uno con foto, nombre, descripción, precio y botón "Add to cart":

| Producto | Precio |
|---|---|
| Sauce Labs Backpack | $29.99 |
| Sauce Labs Bike Light | $9.99 |
| **Sauce Labs Bolt T-Shirt** (recuadrado en rojo) | $15.99 |
| Sauce Labs Fleece Jacket | $49.99 |
| Sauce Labs Onesie | $7.99 |
| **Test.allTheThings() T-Shirt (Red)** (recuadrado en rojo) | $15.99 |

Los dos recuadros rojos marcan los productos elegidos para el carrito.

## Slide 17

Usamos nuevamente **find_element()**, para hacer clic en los botones de agregar producto al carrito y luego para entrar a la sección donde se encuentra el carrito y darle clic. Si en caso no nos permite hacer esto último, agregamos **option.add_argument("--incognito")** para que no se muestre la ventana de cambiar la contraseña.

Captura de código con el bloque nuevo (#Compras / #Carrito) recuadrado en blanco:

```python
#Login
user_input = driver.find_element(By.ID, "user-name")
user_input.send_keys(USER)
pass_input = driver.find_element(By.ID, "password")
pass_input.send_keys(PASSWORD)
button = driver.find_element(By.ID, "login-button")
button.click()
#Compras
time.sleep(5)
button_1 = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
button_2 = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
button_1.click()
button_2.click()
#Carrito
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[1]/div[1]/div[3]/a").click()
time.sleep(5)
driver.find_element(By.NAME,"checkout").click()

time.sleep(5)
driver.quit()

if __name__ == "__main__":
    main()
```

## Slide 18

Al ejecutar el script anterior, se deberían mostrar los productos que fueron agregados al carrito para, posteriormente, darle clic al botón de chequeo y llevarnos a un apartado con datos personales a completar. Si en caso no se observe el botón del carrito, **cambiar el tamaño de página a 1366×768, 1440×900 o 1280×800**.

Dos capturas lado a lado:
- Izquierda: página "Your Cart" de Swag Labs con columnas QTY / Description y dos ítems: **Test.allTheThings() T-Shirt (Red)** $15.99 y **Sauce Labs Bolt T-Shirt** $15.99, cada uno con botón "Remove". Abajo: botón "← Continue Shopping" y botón verde **Checkout**.
- Derecha: pantalla "Your Information" con tres campos vacíos (First Name, Last Name, Zip/Postal Code), botón "← Cancel" y botón verde **Continue**.

## Slide 19

Completamos los datos personales con valores apropiados identificando el código HTML para cada casilla al inspeccionar la página web.

Captura de código con el bloque `#Pagar` recuadrado en blanco:

```python
#Compras
time.sleep(5)
button_1 = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
button_2 = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
button_1.click()
button_2.click()
#Carrito
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[1]/div[1]/div[3]/a").click()
time.sleep(5)
driver.find_element(By.NAME,"checkout").click()
#Pagar
time.sleep(5)
driver.find_element(By.ID,"first-name").send_keys("José")
driver.find_element(By.ID,"last-name").send_keys("Espinoza")
driver.find_element(By.ID,"postal-code").send_keys("15001")

time.sleep(5)
driver.quit()

if __name__ == "__main__":
    main()
```

## Slide 20

Si volvemos a ejecutar el script, veremos que se muestran los datos personales completos y lo que haremos a continuación será darle clic al botón continuar desde nuestro script.

Captura de la pantalla "Checkout: Your Information" de Swag Labs con el carrito mostrando 2 ítems (badge rojo). Los tres campos ya rellenados automáticamente: **José**, **Espinoza**, **15001**. Abajo: botón "← Cancel" y botón verde **Continue**.

## Slide 21

Completamos el código con los botones para continuar, finalizar y regresar, luego de explorar la página web y finalmente se nos mostrará una pantalla en donde se da por finalizado el pedido de compra.

Captura de código:

```python
#Continuar, finalizar y regresar
driver.find_element(By.ID,"continue").click()
time.sleep(5)
driver.find_element(By.ID,"finish").click()
time.sleep(5)
driver.find_element(By.ID,"back-to-products").click()

time.sleep(5)
driver.quit()

if __name__ == "__main__":
    main()
```

Debajo, captura de la pantalla "Checkout: Complete!" de Swag Labs: ícono de check verde en círculo, título **"Thank you for your order!"**, texto "Your order has been dispatched, and will arrive just as fast as the pony can get there!" y botón verde **Back Home**.

## Slide 22

**Ejercicio**

Utilizaremos la página https://quotes.toscrape.com para hacer web scraping. Desarrolle un código basado en driver Selenium que:

1. Haga ***log in*** en la página usando ***test*** como palabra clave para ambos campos.
2. Extraiga todos las citas de los páginas de la web. Recuerde que cada cita, tiene un autor y una lista de tags.
3. Termine con ***log out.***
