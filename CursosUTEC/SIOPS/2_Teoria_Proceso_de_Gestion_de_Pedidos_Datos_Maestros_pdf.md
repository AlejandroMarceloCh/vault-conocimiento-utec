---
curso: SIOPS
titulo: 2. Teoría - Proceso de Gestión de Pedidos - Datos Maestros
slides: 21
fuente: 2. Teoría - Proceso de Gestión de Pedidos - Datos Maestros.pdf
---

## Slide 1

Portada del capítulo. Título "Proceso de Gestión de Pedidos (Datos Maestros)". Profesor: Carlos Villanueva Q. Logo UTEC (decorativo). Crédito: "Adaptado de: Magal and Word | Integrated Business Processes with ERP Systems | © 2011. Traducido por Grandón, Pinto y Soto (2017)".

## Slide 2

**Objetivos de Aprendizaje**

1. Identificar los Datos Maestros asociados al proceso de Gestión de Pedidos.
2. Utilizar SAP S/4HANA para visualizar los Datos Maestros.

## Slide 3

**Datos maestros**

Lista de los 6 datos maestros que se cubrirán en el capítulo:
- Maestro de Material (¿Cuáles vistas?)
- Maestro de Clientes (¿Cuáles segmentos?)
- Registro de Información (INFO) Cliente-Material
- Condiciones de precio
- Condiciones de mensajes
- Registro maestro gestión de créditos

## Slide 4

Misma lista de la slide 3 (slide "índice" reutilizada como separador). Visualmente el ítem **"Maestro de Material (¿Cuáles vistas?)"** está resaltado con un recuadro naranja de borde, indicando que es el tema que se desarrolla a continuación.

## Slide 5

**Datos maestro de material: vistas**

- **Datos Básicos**: a nivel de mandante
- **Datos de Organización de Ventas**
  - Incluye datos específicos de una combinación de organización de venta y canal de distribución
  - Ejemplos incluyen: centro suministrador, unidades de venta (unidad de medida), cantidad mínima (orden, despacho)
- **Datos de Ventas de Centro**
  - Incluye datos específicos para un centro

## Slide 6

Misma lista índice de datos maestros (igual a slides 3-4). Esta vez el ítem resaltado con recuadro es **"Maestro de Clientes (Cuáles segmentos?)"**, señalando el tema siguiente.

## Slide 7

**Datos del maestro de cliente**

- **Datos Generales**
  - se definen a nivel de mandante
  - Válido para todas las sociedades y área de ventas
  - Específico para un cliente
- **Datos Contables/Financieros**
  - Específico para una sociedad
- **Datos de área de ventas**
  - Específico para el área de venta

## Slide 8

**Segmentos de los datos de maestro de cliente**

Diagrama de tres óvalos superpuestos sobre un fondo con forma de "trébol"/pétalos en azul claro, mostrando la jerarquía de los tres segmentos de datos del cliente:
- Óvalo superior central: **"Datos generales (mandante)"**
- Óvalo inferior izquierdo, bajo etiqueta **"Contabilidad"**: **"Datos contables (sociedad)"**
- Óvalo inferior derecho, bajo etiqueta **"Ventas"**: **"Datos área de ventas (área de ventas)"**

El diagrama ilustra visualmente que los datos generales son la base común (mandante), de la cual se derivan/especializan los datos contables (por sociedad) y los datos de ventas (por área de ventas).

## Slide 9

**Datos del maestro de cliente** (continuación, con datos concretos por segmento)

- **Datos Generales**
  - Número de cuenta
  - Dirección
  - Comunicación
- **Datos de sociedad (FI)**
  - Cuenta asociada del LM
  - Términos de pago

## Slide 10

**Datos del maestro de cliente** (continuación)

- **Datos Area Venta (Ventas)**
  - Relacionados con venta
    - Área de venta, precio, moneda
  - Expedición
    - Centro suministrador, prioridades, métodos, tolerancias, envío parcial
  - Facturación
    - Términos, impuesto relacionado.
  - Funciones de interlocutor: roles múltiples
    - solicitante, destinatario, destinatario de la factura, pagador
- Un cliente puede ser atendido por múltiples áreas de venta

## Slide 11

**Múltiples definiciones de un área de venta para el mismo cliente**

Diagrama jerárquico de tres niveles con recuadros azules conectados por líneas verticales/en árbol:

- **Nivel Mandante**: recuadro único "(GBI) Datos generales"
- **Nivel Sociedad** (dos ramas desde el mandante):
  - "(US00) Datos contables"
  - "(DE00) Datos contables"
- **Nivel Área de ventas** (ramifica desde cada sociedad):
  - Desde US00: "(UE00 + WH + BI) Datos área de ventas" y "(UW00 + WH + BI) Datos área de ventas"
  - Desde DE00: "(DN00 + IN + BI) Datos área de ventas"

Ilustra que un mismo cliente global (GBI) puede tener múltiples sociedades asociadas, y cada sociedad puede tener múltiples combinaciones de área de ventas.

## Slide 12

**Clientes de GBI**

Dos tarjetas/paneles con encabezado azul, listando clientes reales usados como datos de ejemplo (empresa ficticia GBI del caso de estudio del curso):

**Clientes de GBI EE.UU.:**
Beantown Bikes, Big Apple Bikes, DC Bikes, Furniture City Bikes, Motown Bikes, Northwest Bikes, Peachtree Bikes, Philly Bikes, Rocky Mountain Bikes, Silicon Valley Bikes, SoCal Bikes, Windy City Bikes

**Clientes de GBI DE:**
Berliner Cykel (Berlín), Bicicletas Madrileños (Madrid), Cykel Zurich (Zurich), Frankfurter Cycle (Frankfurt), Munich Bikes (Munich), Vélos Parisienne (Paris), Ye Olde Bike (London)

## Slide 13

Lista índice de datos maestros (misma de slides 3/4/6). Resaltado con recuadro: **"Registro de Información (INFO) Cliente-Material"**, indicando el tema siguiente.

## Slide 14

**Registro de Información Cliente-Material**

- Datos específicos para la combinación de cliente y material
- Sustituyen datos en maestro de cliente y maestro de material
- Ejemplos:
  - **Referencias cruzadas** entre el número de material del cliente y el número de material de la empresa, descripciones
  - **Términos específicos** ejm.: preferencias de envío, tolerancias, entrega especial, centro suministrador.

## Slide 15

**Número de material de GBI y Cliente RMB**

Tabla con encabezado azul, mostrando ejemplo de referencias cruzadas de números de material:

| Material | Número de material GBI | Número de material RMB |
|---|---|---|
| Bicicleta de turismo de lujo negra | DXTR1000 | G1000BL |
| Bicicleta de turismo de lujo plateada | DXTR2000 | G1000SL |
| Bicicleta de turismo de lujo roja | DXTR3000 | G1000RD |

## Slide 16

Lista índice de datos maestros. Resaltado con recuadro: **"Condiciones de precio"**, tema siguiente.

## Slide 17

**Condición de precios**

- **Precio**
  - Precio del Material
  - Precio específico para el Cliente
- **Fletes**
  - InCoTerms
- **Recargas y descuentos**
  - Por cliente, material, o combinación
- **Impuestos**

## Slide 18

Lista índice de datos maestros. Resaltado con recuadro: **"Condiciones de mensajes"**, tema siguiente.

## Slide 19

**Condiciones de mensajes**

- Envíos al cliente utilizando una variedad de medios
- Ejemplos de mensajes:
  - Cotización, confirmación de orden, facturas
- Los datos en el maestro incluyen:
  - Tipo de salida,
  - Medio (impresora, eMail, EDI),
  - Tiempo (inmediato o más tarde)

## Slide 20

Lista índice de datos maestros. Resaltado con recuadro: **"Registro maestro gestión de créditos"**, tema siguiente (último de la lista).

## Slide 21

**Registro maestro de gestión de créditos**

- Es una extensión del maestro de clientes
- Los datos se agrupan en 3 segmentos:
- **Datos Generales** (nivel empresa global)
  - Dirección, comunicación, crédito total a nivel de empresa
- **Datos área de control de crédito** (nivel área de control de crédito)
  - Límite de crédito para un área de control de crédito
  - Clase de riesgo
- **Resumen** (datos claves desde otras segmentos)
