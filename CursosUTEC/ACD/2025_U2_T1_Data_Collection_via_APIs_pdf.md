---
curso: ACD
titulo: [2025] U2_T1 Data Collection via APIs
slides: 9
fuente: [2025] U2_T1 Data Collection via APIs.pdf
---

## Slide 1

Portada.

**Data Collection vía APIs**
DS3021 Análisis Computacional de Datos

Fondo decorativo: túnel digital azul con silueta de una persona caminando. Separador de guiones amarillos bajo el título. Chrome institucional ignorado.

## Slide 2

**Objetivo de sesión** (título rotado 90° en el margen izquierdo)

> Aplicar diferentes herramientas computacionales para la recolección de datos a través de APIs.

Banda vertical izquierda con foto decorativa (dos personas revisando documentos, teñida de azul).

## Slide 3

**¿Cómo recolectamos los datos?**

Tabla de dos columnas con cabecera negra y un emoji por fila indicando el nivel de esfuerzo:

| Métodos | Esfuerzo | Emoji |
|---|---|---|
| Descargar | Baja | 🙂 (cara sonriente) |
| API (*Application Program Interface*) | Media | 😐 (cara neutra) |
| *Scrape* | Alto | 😲 (cara de asombro/boca abierta) |

La progresión visual de los emojis refuerza el aumento de esfuerzo de arriba hacia abajo.

## Slide 4

Slide divisoria de sección.

**1.**
**Data Collection via APIs**

Icono de portapapeles/checklist azul junto al título. Imagen decorativa a la derecha: mano robótica tocando un globo terráqueo digital.

## Slide 5

**API — *Application Programming Interface***

> Una API actúa como una capa de comunicación (una interfaz) que permite que diferentes sistemas se comuniquen entre sí **sin tener que entender exactamente lo que hacen los demás.** (última parte resaltada en celeste)

Imagen a la derecha: un mesero de esmoquin y guantes blancos sosteniendo una bandeja con campana/cloche plateada cerrada — metáfora de la API que sirve el resultado sin exponer cómo se preparó.

## Slide 6

**A web API**

Ilustración a la izquierda: una nube azul con dos flechas blancas horizontales apuntando en direcciones opuestas (izquierda y derecha) — intercambio bidireccional de datos — con el rótulo "Web API" debajo.

> Una API web es un servicio disponible en la web que **proporciona acceso a recursos como datos sin procesar** (resaltado en celeste), información filtrada y contenido integrado y dinámico, normalmente en un formato intercambiable y listo para usar, como **JSON**, **CSV o XML**.

## Slide 7

Diagrama de árbol simple:

- Nodo raíz (caja celeste): **Recolectar datos vía APIs**
- Dos flechas descendentes hacia dos cajas grises:
  - **Sin Autenticación** (izquierda)
  - **Con Autenticación** (derecha)

## Slide 8

Diagrama cliente–servidor sin título. Al centro arriba, icono de globo terráqueo con un rack de servidores rotulado **Web Server**. Debajo, dos flechas gruesas celestes:

- Flecha hacia arriba (hacia el servidor): **Page Request**
- Flecha hacia abajo (desde el servidor): **Page Content**

Caja izquierda (asociada al request) — componentes de una petición:
- ***Endpoint***: URL de los datos.
- ***Método*** (GET, PUT, POST o DELETE).
- ***Headers***, proporcionan información como claves de autenticación.
- ***Data/body***: GET no tiene esta sección

Caja derecha (asociada a la respuesta) — códigos de estado HTTP:
- **1xx:** Brinda información
- **2xx:** Exitoso
- **3xx:** Proporcionar información sobre redireccionamientos
- **4xx:** Error del lado del cliente (nuestro error)
- **5xx:** Error del lado del servidor

## Slide 9

**Beneficios de web APIs**

Infografía en zigzag: cinco iconos circulares azules (lupa, diana, cohete, calendario, cadena/enlace) conectados por una cinta gris en S descendente; cada icono se enlaza con líneas amarillas a un bloque de texto alternando derecha/izquierda.

- **Integración**: Las API devuelven datos en un formato estándar, como JSON, que se pueden guardar y procesar.
- **Multiplataforma**: Cada API requiere una URL con argumentos compatibles o necesarios que deben ejecutarse o cargarse en el navegador web. Las dependencias de la máquina, el sistema operativo y el navegador web no son factores a considerar.
- **Automatización**: Ejecutar API y recopilar resultados es parte de la automatización, ya que las API contienen código preconfigurado, como llamadas a sus procesos o procedimientos internos, y dependencias necesarias, que funcionan como automatización.
- **Tiempo**: Las API son fáciles de procesar, llamar y cargar en el navegador. Estas actividades toman menos tiempo en comparación con las configuraciones de máquinas completas o virtuales.
- **Seguridad**: El procesamiento de API mediante una suscripción y claves de API se considera seguro. Sin embargo esta seguridad se puede eludir con encabezados y servidores proxy HTTP.
