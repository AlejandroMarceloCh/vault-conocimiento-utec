---
curso: CLOUD
titulo: 1. Almacenamiento y Bases de Datos - Taller 1 - V1.00
slides: 19
fuente: 1. Almacenamiento y Bases de Datos - Taller 1 - V1.00.pdf
---

## Slide 1

Portada. "CS2032 - Cloud Computing (Ciclo 2024-1) / Almacenamiento y Bases de Datos" con subtítulo "Semana 5 - Taller 1: Servicio de almacenamiento S3". "Elaborado por: Geraldo Colchado". Logo UTEC (decorativo) arriba a la derecha, franja naranja decorativa al pie.

## Slide 2

Slide de contenido (barra lateral naranja "Contenido / Servicio de Almacenamiento S3", panel derecho blanco con lista numerada). Índice del taller, con el ítem 1 en negrita/subrayado indicando la sección actual:
1. **Objetivo del taller 1** (resaltado)
2. Ejercicio 1: Crear un bucket
3. Ejercicio 2: Crear directorios y archivos
4. Ejercicio 3: Crear enlaces públicos
5. Ejercicio 4: Implementar página web
6. Cierre

## Slide 3

Título: "Objetivo del taller 1: Servicio de Almacenamiento S3". Lista con viñetas:
- Entender qué es un bucket
- Crear directorios, subdirectorios y archivos
- Crear enlaces públicos
- Implementar página web

## Slide 4

Slide de contenido (mismo layout que slide 2), ahora resaltando el ítem 2 en negrita/subrayado:
1. Objetivo del taller 1
2. **Ejercicio 1: Crear un bucket** (resaltado)
3. Ejercicio 2: Crear directorios y archivos
4. Ejercicio 3: Crear enlaces públicos
5. Ejercicio 4: Implementar página web
6. Cierre

## Slide 5

Título: "Ejercicio 1: Crear un bucket (nombre único a nivel mundial)".

Texto: "Creación de un bucket" — "Cada objeto en S3 se almacena en un bucket. Para subir archivos y carpetas a S3, tendrá que crear un bucket donde se almacenarán los objetos." (frase resaltada en amarillo: "bucket donde se almacenarán los objetos"). Botón naranja "Crear bucket".

Captura de pantalla de la consola AWS S3, sección "Configuración general":
- Campo "Nombre del bucket": `gcolchado` (resaltado en amarillo)
- Texto de ayuda: el nombre debe ser único en todo el mundo y no debe contener espacios ni mayúsculas
- "Región de AWS": EE. UU. Este (Norte de Virginia) us-east-1
- Sección "Propiedad de objetos": dos opciones radio — "ACL deshabilitadas (recomendado)" (no seleccionada) y "ACL habilitadas" (seleccionada, marcada con flecha roja), con su descripción de cada opción.

## Slide 6

Continuación de "Ejercicio 1: Crear un bucket (nombre único a nivel mundial)".

Captura de pantalla de la consola AWS S3, sección "Configuración de bloqueo de acceso público para este bucket": texto explicativo sobre ACLs/políticas de bucket y el bloqueo de acceso público. Checkbox "Bloquear todo el acceso público" (NO marcado), y sus 4 sub-opciones (ninguna marcada):
- Bloquear el acceso público a buckets y objetos concedido a través de nuevas ACL
- Bloquear el acceso público a buckets y objetos concedido a través de cualquier ACL
- Bloquear el acceso público a buckets y objetos concedido a través de políticas de bucket y puntos de acceso públicas nuevas
- Bloquear el acceso público y entre cuentas a buckets y objetos concedido a través de cualquier política de bucket y puntos de acceso pública

Recuadro de advertencia (icono ⚠️) a la derecha: "Desactivar el bloqueo de todo acceso público puede provocar que este bucket y los objetos que contiene se vuelvan públicos", con checkbox marcado "Reconozco que la configuración actual puede provocar que este bucket y los objetos que contiene se vuelvan públicos". Botones "Cancelar" y "Crear bucket" (naranja, señalado con flecha roja).

## Slide 7

Continuación de "Ejercicio 1: Crear un bucket (nombre único a nivel mundial)".

Captura de pantalla de la consola AWS S3 mostrando la lista de buckets creados. Tabla:

| Nombre | Región de AWS | Acceso | Fecha de creación |
|---|---|---|---|
| gcolchado (resaltado) | EE. UU. Este (Norte de Virginia) us-east-1 | Los objetos pueden ser públicos (resaltado) | 11 Sep 2022 9:40:06 PM -05 |

Encabezado "Buckets (1)" con botones "Copiar ARN", "Vaciar", "Eliminar", "Crear bucket" y campo de búsqueda "Buscar buckets por nombre".

## Slide 8

Slide de contenido, ahora resaltando el ítem 3:
1. Objetivo del taller 1
2. Ejercicio 1: Crear un bucket
3. **Ejercicio 2: Crear directorios y archivos** (resaltado)
4. Ejercicio 3: Crear enlaces públicos
5. Ejercicio 4: Implementar página web
6. Cierre

## Slide 9

Título: "Ejercicio 2: Crear directorios y archivos".

- Instrucción: "Crear la siguiente estructura de directorios"

Diagrama/tabla de estructura de carpetas (con iconos de carpeta):

| Carpeta | Tipo |
|---|---|
| documentos/ | Carpeta |
| imágenes/ | Carpeta |
| &nbsp;&nbsp;productos/ (sangrado, dentro de imágenes) | Carpeta |
| &nbsp;&nbsp;publicidad/ (sangrado, dentro de imágenes) | Carpeta |
| videos/ | Carpeta |

- Instrucción: "En directorio 'documentos' subir un archivo en formato pdf"

## Slide 10

Slide de contenido, ahora resaltando el ítem 4:
1. Objetivo del taller 1
2. Ejercicio 1: Crear un bucket
3. Ejercicio 2: Crear directorios y archivos
4. **Ejercicio 3: Crear enlaces públicos** (resaltado)
5. Ejercicio 4: Implementar página web
6. Cierre

## Slide 11

Título: "Ejercicio 3: Crear enlaces públicos". Solo texto, sin imagen:
- Crear un enlace público al archivo pdf en directorio "documentos".
- Obtener el enlace público y acceder por el navegador

## Slide 12

Continuación de "Ejercicio 3: Crear enlaces públicos".

Captura de pantalla de la consola AWS S3, dentro del bucket `gcolchado > documentos/`. Se muestra la pestaña "Objetos" con 1 objeto:

| ✓ | Nombre | Tipo | Última modificación | Tamaño | Clase de almacenamiento |
|---|---|---|---|---|---|
| ✓ | CS2032 - Cloud Computing - 2022.2.pdf | pdf | 11 Sep 2022 9:46:47 PM -05 | 4.1 MB | Estándar |

El archivo está seleccionado (checkbox marcado, señalado con flecha roja). Al costado, un menú desplegable "Acciones" abierto mostrando opciones: Iniciar restauración (deshabilitado), Consultar con S3 Select, Editar acciones, Cambiar el nombre del objeto, Editar clase de almacenamiento, Editar cifrado del lado del servidor, Editar metadatos, Editar etiquetas, y **"Hacer público mediante ACL"** (resaltada con flecha roja, es la opción que se va a elegir).

## Slide 13

Continuación de "Ejercicio 3: Crear enlaces públicos".

Captura de pantalla similar a la anterior (bucket `documentos/`, mismo archivo pdf seleccionado), pero ahora mostrando el botón "Copiar URL" en la barra de herramientas (Copiar URI de S3, Copiar URL, Descargar, Abrir, Eliminar, Acciones, Crear carpeta, Cargar), señalado con flecha roja para indicar que se debe copiar la URL del objeto ya hecho público.

## Slide 14

Continuación de "Ejercicio 3: Crear enlaces públicos".

Muestra el enlace público resultante, con partes resaltadas en amarillo (nombre del bucket, "s3", nombre del directorio y nombre del archivo):

```
https://gcolchado.s3.amazonaws.com/documentos/CS2032+-+Cloud+Computing+-+2022.2.pdf
```

## Slide 15

Slide de contenido, ahora resaltando el ítem 5:
1. Objetivo del taller 1
2. Ejercicio 1: Crear un bucket
3. Ejercicio 2: Crear directorios y archivos
4. Ejercicio 3: Crear enlaces públicos
5. **Ejercicio 4: Implementar página web** (resaltado)
6. Cierre

## Slide 16

Título: "Ejercicio 4: Implementar página web".

Instrucciones (viñetas):
- Cree un nuevo bucket "gcolchado-miweb" (resaltado en amarillo)
- Suba o cargue la web simple o la web plantilla con index.html en la raíz
- Luego marque todos los directorios y archivos y "Hacer público"
- Configure "Alojamiento de sitios web estáticos" (Pestaña "Propiedades") con index.html
- Visualice la página web por el navegador. Ejemplo:

Captura de pantalla superior derecha: encabezado del bucket "gcolchado-miweb" con pestañas Objetos / **Propiedades** (marcada con check) / Permisos.

Captura de pantalla central derecha: sección "Alojamiento de sitios web estáticos" con:
- Radio buttons: "Desactivar" (no seleccionado) / "Habilitar" (seleccionado)
- "Tipo de alojamiento": radio "Alojar un sitio web estático" (seleccionado)
- Campo "Documento de índice": `index.html`

Al pie, el enlace público resultante (bucket y dominio resaltados en amarillo):

```
http://gcolchado-miweb.s3-website-us-east-1.amazonaws.com
```

## Slide 17

Slide de contenido, ahora resaltando el ítem 6:
1. Objetivo del taller 1
2. Ejercicio 1: Crear un bucket
3. Ejercicio 2: Crear directorios y archivos
4. Ejercicio 3: Crear enlaces públicos
5. Ejercicio 4: Implementar página web
6. **Cierre** (resaltado)

## Slide 18

Título: "Cierre: Servicio de Almacenamiento S3 - Qué aprendimos?". Lista con viñetas (recapitulación de objetivos):
- Qué es un bucket?
- Crear directorios, subdirectorios y archivos
- Crear enlaces públicos
- Implementar página web

## Slide 19

Slide de cierre/agradecimiento: "Gracias" y "Elaborado por docente: Geraldo Colchado". Franja naranja decorativa al pie. Slide decorativa/de cierre, sin contenido técnico adicional.
