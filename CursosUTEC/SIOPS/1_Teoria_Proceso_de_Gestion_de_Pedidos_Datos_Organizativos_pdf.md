---
curso: SIOPS
titulo: 1. Teoria - Proceso de Gestión de Pedidos - Datos Organizativos
slides: 33
fuente: 1. Teoria - Proceso de Gestión de Pedidos - Datos Organizativos.pdf
---

## Slide 1

Portada. Título "Proceso de Gestión de Pedidos (Datos Organizativos)". Profesor: Carlos Villanueva Q. Logo UTEC arriba a la derecha (decorativa). Crédito: Adaptado de Magal and Word | Integrated Business Processes with ERP Systems © 2011, traducido por Grandón, Pinto y Soto (2017).

## Slide 2

"Objetivos de Aprendizaje":
1. Describir los niveles organizativos clave asociados al proceso de Gestión de Pedidos.
2. Identificar Datos Maestros de Clientes en un Sistema empresarial (S/4HANA).

## Slide 3

Slide "Agenda" con estructura tipo árbol (llaves `{` que agrupan ítems), dividida en dos bloques numerados:

**1. Datos Organizativos** (agrupa 7 ítems):
1) Mandante
2) Sociedad
3) Centro
4) Almacén
5) Área de ventas — con sub-lista (agrupada con llave aparte): Organización de ventas / Canal de distribución / Sector (división)
6) Puesto de expedición
7) Área de Control de Créditos

**2. Datos Maestros** (agrupa 6 ítems):
1) Maestro de Materiales
2) Maestro de Cliente
3) Registro de Información (INFO) Cliente-Material
4) Condiciones de Precio
5) Condiciones de Mensajes
6) Registro Maestro Gestión de Créditos

Esta misma slide de "Agenda" se repite como separador de sección en varias slides posteriores (6, 9, 12, 16, 19, 23, 30), resaltando cada vez en un recuadro/flecha rosado el ítem que se va a tratar a continuación.

## Slide 4

Diagrama "Proceso básico de gestión de pedidos": flujo horizontal de 3 iconos de personas conectadas por flechas, cada una con dos cajas de proceso debajo:

`[Persona 1 - Ventas] → [Persona 2 - Almacén] → [Persona 3 - Contabilidad]`

- **Ventas**: "Recibe pedido de cliente" → "Crea pedido de cliente"
- **Almacén**: "Prepara despacho (tomar y embalar)" → "Envía despacho (despacha)"
- **Contabilidad**: "Crea y envía factura" → "Recibe pago"

Cada persona tiene un ícono representativo (mujer con orden de compra "PURCHASE ORDER", hombre con caja "Almacén", hombre con factura "INVOICE").

## Slide 5

Slide "Datos Organizativos": lista de dos columnas con checkmarks (✔) indicando lo ya visto en una sesión teórica previa:
- Columna izquierda: Mandante ✔, Sociedad ✔, Centro ✔, Almacén ✔
- Columna derecha (sin check, se verán en este capítulo): Área de ventas (con sub-bullets: Organización de ventas, Canal de distribución, Sector (división)), Cadena de distribución, Puesto de Expedición, Área de control de créditos

## Slide 6

Slide "Agenda" (repetición de slide 3), con el ítem "Organización de ventas" resaltado en un recuadro rosado dentro de la sub-lista de Área de ventas.

## Slide 7

"Organización de ventas": bullets:
- Responsable de:
  - Vender y Distribuir bienes y servicios
  - Negociar condiciones de ventas
  - Responsable de los clientes con respecto a las obligaciones y derechos de recurso en caso de disputas
- Utilizada para dividir el mercado basado en **áreas geográficas**.
- Nivel de agregación más alto en reportes relacionados con ventas.
- Una sociedad tiene al menos una Organización de Ventas.
- Una Organización de Ventas pertenece solo a una sociedad.

## Slide 8

Diagrama "Organización de ventas de GBI" — jerarquía de 3 niveles en cajas azules conectadas por líneas verticales/horizontales:

```
Mandante:            [Mandante]
                         |
        ┌────────────────┴────────────────┐
Sociedad: [US00 Empresa EE.UU.]      [DE00 Empresa Alemana]
              |                              |
      ┌───────┴───────┐              ┌───────┴───────┐
Org.  [UE00 EE.UU. Este] [UW00 EE.UU. Oeste] [DN00 Alemania Norte] [DS00 Alemania Sur]
Ventas
```

Filas etiquetadas a la izquierda: Mandante / Sociedad / Organización de ventas.

## Slide 9

Slide "Agenda" (repetición), con "Canal de distribución" resaltado en rosado dentro de la sub-lista de Área de ventas.

## Slide 10

"Canal de distribución": bullets:
- Medio por el cual la empresa distribuye sus productos y servicios a sus clientes
- Se usa para:
  - Diferenciar estrategias o enfoques de distribución
  - Diferenciar precios, responsabilidades
  - **Tipos de canales**: mayoristas, ventas al detalle, en línea.
  - Estadísticas y reportes al nivel del canal de distribución
- Una organización de ventas debe tener al menos un canal de distribución

## Slide 11

Diagrama "Canales de distribución de GBI US" — jerarquía de 4 niveles en cajas azules:

```
Mandante:  [Mandante]
              |
     ┌────────┴────────┐
Sociedad: [US00 EE.UU.]        [DE00 Alemania]
              |                       |
     ┌────────┴────────┐      ┌───────┴───────┐
Org.Ventas: [UE00 Este] [UW00 Oeste]  [DN00 Norte] [DS00 Sur]
                |            |              |            |
Canal:   [WH Mayorista] [WH Mayorista]  [WH Mayorista] [WH Mayorista]
                          [IN Ventas por Internet]  [IN Ventas por Internet]
```

Muestra que UW00 (Oeste) tiene dos canales (WH y IN), igual que DN00 (Norte); mientras que UE00 y DS00 solo tienen canal WH Mayorista.

## Slide 12

Slide "Agenda" (repetición), con "Sector (división)" resaltado en rosado dentro de la sub-lista de Área de ventas.

## Slide 13

"Sectores": bullets:
- Unidad utilizada por las empresas para **combinar materiales** y servicios con características similares.
  - Asociados con una **línea de producto**
  - Diferentes estrategias de venta, acuerdos de precio
  - Estadísticas y reportes a nivel de sector
- Una organización de venta tiene al menos un sector.
- Un producto o material se asocia solo a un sector
- Un sector puede ser asignado a múltiples organizaciones de venta.

## Slide 14

Diagrama "Sectores de GBI EE.UU." — jerarquía de 4 niveles:

```
Mandante: [Empresa global GBI]
              |
Sociedad: [US00 Empresa EE.UU.]
              |
     ┌────────┴────────┐
Org.Ventas: [UE00 EE.UU. Este]        [UW00 EE.UU. Oeste]
                |    |                     |    |
Sector:    [BI Sector    [AS Sector   [BI Sector   [AS Sector
            bicicletas]  Accesorios]  bicicletas]  Accesorios]
```

Cada organización de ventas (Este y Oeste) se ramifica en dos sectores: BI (bicicletas) y AS (accesorios).

## Slide 15

Diagrama "Sectores de GBI Alemania" — misma estructura jerárquica que GBI EE.UU. pero para la sociedad alemana:

```
Mandante: [Empresa global GBI]
              |
Sociedad: [DE00 Empresa Alemania]
              |
     ┌────────┴────────┐
Org.Ventas: [DN00 Alemania Norte]     [DS00 Alemania Sur]
                |    |                     |    |
Sector:    [BI sector    [AS sector   [BI sector   [AS sector
            bicicletas]  accesorios]  bicicletas]  accesorios]
```

## Slide 16

Slide "Agenda" (repetición), con las 3 sub-opciones (Organización de ventas, Canal de distribución, Sector (división)) agrupadas dentro de un recuadro rosado en forma de bocadillo/flecha apuntando hacia "Área de ventas", indicando que se completó el bloque de las 3 sub-categorías y se pasa a tratar "Área de ventas" como combinación de las tres.

## Slide 17

"Área de ventas": bullets:
- Combinación única de: Organización de Venta / Canal de distribución / Sector
- Recuadro de texto a la derecha: "Determina qué productos serán vendidos a través de qué canal y quién es responsable de esa venta"
- Puede ser asignada solo a una sociedad.
- Todos los documentos asociados con el proceso de gestión de pedidos, tales como ofertas y listas de embalaje, pertenecen a un área de ventas.

## Slide 18

Diagrama "Áreas de ventas de GBI" — jerarquía de 4 niveles (Mandante/Sociedad/Organización de ventas/Canal de Distribución/Sector) con un óvalo de resaltado que encierra la combinación UE00 + WH + BI, y una lista de texto arriba a la izquierda enumerando las 6 combinaciones posibles (áreas de venta) que resultan del cruce Org.Ventas × Canal × Sector:

- UE00 + WH + BI
- UE00 + WH + AS
- UW00 + WH + BI
- UW00 + WH + AS
- UW00 + IN + BI
- UW00 + IN + AS

Estructura del diagrama:
```
Mandante: [GBI]
              |
     ┌────────┴────────┐
Sociedad: [US00 GBI EE.UU.]    [DE00 GBI Alemania]
              |
     ┌────────┴────────┐
Org.Ventas: [UE00 EE.UU. Este]        [UW00 EE.UU. Oeste]
                |                       |          |
Canal:     [WH Mayorista]        [WH Mayorista] [IN Ventas por Internet]
             |      |               |    |          |     |
Sector: [BI bicic] [AS access]  [BI bicic][AS access][BI bicic][AS access]
```
El óvalo resalta la rama UE00 → WH Mayorista → BI Sector bicicletas, ilustrando una de las 6 combinaciones (áreas de venta).

## Slide 19

Slide "Agenda" (repetición), con el ítem "Centro" resaltado en rosado en la lista principal de Datos Organizativos.

## Slide 20

"Centro": bullets:
- En el proceso de gestión de pedidos un centro suministrador es una instalación desde la cual la empresa entrega sus productos y servicios a sus clientes.
- Un centro se puede asignar a más de un canal de distribución.
- A la inversa, una cadena de distribución puede estar asociada a más de un centro.

## Slide 21

Diagrama "Centros": muestra relación muchos-a-muchos entre canales de distribución y centros mediante líneas cruzadas:

```
[Canal de distribución 1]   [Canal de distribución 2]   [Canal de distribución 3]
        \                    /        \                    /
         \                  /          \                  /
        [Centro 1]      [Centro 2]              [Centro 3]
```

Canal 1 conecta solo a Centro 1; Canal 2 conecta a Centro 1 y Centro 2 (líneas cruzadas); Canal 3 conecta a Centro 2 y Centro 3. Ilustra que un centro puede recibir de más de un canal y un canal puede repartir a más de un centro.

## Slide 22

"Cadena de distribución": texto:
- Una única combinación de organización de ventas y canal de distribución
  - Algunos datos maestros son mantenidos a este nivel
  - Maestro de material
  - Condiciones de precio

## Slide 23

Slide "Agenda" (repetición), con el ítem "Puesto de expedición" resaltado en rosado en la lista principal de Datos Organizativos.

## Slide 24

"Puesto de expedición": bullets:
- Un lugar en un centro desde el cual se despachan las entregas de salida.
  - Muelle de carga
  - Sala de correo
  - Estación de tren
  - Se asocia también a un grupo de empleados que maneja entregas especiales o rápidas
- Un centro debe tener al menos un punto de expedición
- Un centro puede tener más de un puesto de expedición
- Un punto de expedición se asocia a uno o más centros

## Slide 25

Diagrama "Puestos de expedición compartidos": dos ejemplos lado a lado.

Ejemplo izquierdo: una caja "Instalación de almacenamiento (centro)" con ícono de puerta "EXIT" etiquetado "Puesto de expedición" apuntando hacia ella, y debajo (mismo contorno) otra sección "Oficina (centro)" sin puesto de expedición propio.

Ejemplo derecho: dos cajas separadas, "Instalación de almacenamiento (centro)" arriba y "Fábrica (centro)" abajo, sin conexión entre ellas.

Texto explicativo debajo: "Todos los despachos se envían desde un puesto de expedición, el cual es una instalación de almacenamiento ubicada en la oficina."

## Slide 26

Diagrama "Puestos de expedición múltiples": tres cajas verticales "Instalación de almacenamiento #1/#2/#3 (centro)". Un "Puesto de expedición regular" (con ícono EXIT) tiene flechas hacia Instalación #1 e Instalación #3. La Instalación #3 tiene además su propio ícono EXIT que conecta a un "Puesto de expedición rápido".

Texto explicativo: "El puesto de expedición rápido se usa en todos los centros en la medida que se necesite. La instalación 2 usa los puestos de expedición localizados en las otras dos instalaciones."

## Slide 27

"Puesto de expedición. Ejemplo 1": fotografía en blanco y negro de un muelle de carga de un almacén/centro logístico, con varios camiones estacionados en las bahías de carga bajo un techo voladizo. Ilustra un puesto de expedición físico tipo "muelle de carga".

## Slide 28

"Puesto de expedición. Ejemplo 2": fotografía en blanco y negro de una estación de tren/patio ferroviario de carga, con vagones de tren cargados de contenedores y grúas pórtico al fondo. Ilustra un puesto de expedición tipo "estación de tren".

## Slide 29

"Puesto de expedición. Ejemplo 3": fotografía en blanco y negro de un puerto marítimo con grandes grúas pórtico cargando contenedores sobre un buque portacontenedores. Ilustra un puesto de expedición tipo terminal portuaria.

## Slide 30

Slide "Agenda" (repetición), con el ítem "7) Área de Control de Créditos" resaltado en rosado en la lista principal de Datos Organizativos.

## Slide 31

"Área de control de créditos": bullets:
- Nivel organizativo responsable por los créditos del cliente
- Determina la solvencia de los clientes, establece el límite de crédito y monitorea y maneja las prórrogas de crédito de los clientes.
- Sistema Centralizado
  - Un área de control de crédito para todas las sociedades en la empresa global
  - Todos los clientes de una sociedad son gestionados por un área de control de crédito
- Sistema Descentralizado
  - Más de un área de control de crédito en la empresa global
  - Cada área de control de crédito gestiona los créditos para una o más sociedades en la empresa global

## Slide 32

Diagrama "Area de control de crédito centralizada" — jerarquía de 3 niveles:

```
Empresa global GBI: [GBI]
              |
Área de control de créditos: [GL00 Área control de créditos global]
              |
     ┌────────┴────────┐
Sociedad: [US00 GBI US]      [DE00 GBI DE]
```

Un único área de control de crédito global (GL00) atiende a todas las sociedades.

## Slide 33

Diagrama "Area de control de crédito descentralizada" — jerarquía de 3 niveles:

```
Empresa global: [GBI]
              |
     ┌────────────────┴────────────────┐
Área control de crédito: [NA00 Área control de crédito de Norte América]   [EU00 Área control de crédito de Europa]
              |                                                    |
     ┌────────┼────────┐                                  ┌────────┴────────┐
Sociedad: [US00 GBI EE.UU.] [CA00 GBI Canadá] [MX00 GBI México]  [GB00 GBI Gran Bretaña] [DE00 GBI Alemania]
```

Dos áreas de control de crédito distintas (NA00 y EU00), cada una gestionando varias sociedades de su región.
