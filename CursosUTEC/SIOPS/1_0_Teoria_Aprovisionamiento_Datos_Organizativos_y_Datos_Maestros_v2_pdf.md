---
curso: SIOPS
titulo: 1.0 Teoría Aprovisionamiento - Datos Organizativos y Datos Maestros v2
slides: 34
fuente: 1.0 Teoría Aprovisionamiento - Datos Organizativos y Datos Maestros v2.pdf
---

## Slide 1

Portada. Título "El Proceso de Aprovisionamiento". "Profesor: Carlos Villanueva Q." Franja azul decorativa inferior y logo UTEC (decorativo).

## Slide 2

**Objetivos de Aprendizaje**
1. Comprender los datos organizativos y datos maestros correspondientes al proceso de aprovisionamiento.
2. Ejecutar los pasos del proceso de aprovisionamiento.

Diagrama de flujo del proceso de aprovisionamiento con 4 iconos de persona conectados por flechas horizontales, cada uno con una tarjeta debajo indicando rol y actividad:

`[Persona+caja] → [Persona+doc Purchase Order] → [Persona+caja] → [Persona+factura]`

| Icono | Área | Actividad |
|---|---|---|
| 1 (persona + caja) | Almacén | Crea solicitud de pedido |
| 2 (persona + doc "PURCHASE ORDER") | Compra | Crea y envía orden de pedido |
| 3 (persona + caja) | Almacén | Recibe materiales |
| 4 (persona + factura "INVOICE") | Contabilidad | Recibe factura |
| — | Contabilidad | Envía pago |

Nota: la última tarjeta "Envía pago" no tiene icono de persona propio, comparte el icono 4.

## Slide 3

**Agenda** (slide de mapa conceptual con llaves/corchetes que agrupan temas). Estructura jerárquica:

- **1. Datos Organizativos** (llave que agrupa 6 puntos):
  1) Mandante
  2) Sociedad
  3) Centro
  4) Almacén
  5) Organización de Compras
  6) Grupo de Compras
  - El punto 5 (Organización de Compras) tiene una sub-llave con 4 subpuntos:
    - 1.5.1) A nivel de Empresa Global
    - 1.5.2) A nivel de Sociedad
    - 1.5.3) A nivel de Centro
    - 1.5.4) De Referencia

- **2. Datos Maestros** (llave que agrupa 4 puntos):
  1) Maestro de Materiales
  2) Maestro de Proveedores
  3) Registro Info de Compras
  4) Condiciones

## Slide 4

Misma agenda que slide 3, pero con "1. Datos Organizativos" resaltado en un recuadro naranja/durazno, y dentro del bloque de datos organizativos los ítems "1) Mandante" y "2) Sociedad" resaltados también en un recuadro naranja (indicando que son los próximos temas a tratar, aunque el contenido detallado de Mandante y Sociedad no aparece en este set — pasa directo a Centro).

## Slide 5

Misma agenda, ahora con "3) Centro" resaltado en recuadro naranja (subrayado también), indicando que la slide siguiente trata ese tema.

## Slide 6

**Centro**
- Muchas definiciones o usos. Una ubicación
  - Que mantiene stock valorado (para distribución)
  - Donde se lleva a cabo la planificación de la producción
  - Donde se crean productos y servicios
  - Que contiene las instalaciones de servicio o mantenimiento
- Fábrica, almacén, centro de distribución
- Se puede asignar sólo a una sociedad
- Una sociedad puede tener muchos centros

Solo texto, sin elementos visuales adicionales.

## Slide 7

Misma agenda, con "4) Almacén" resaltado en recuadro naranja (subrayado), marcando el tema siguiente.

## Slide 8

**Almacén**
- Un lugar, dentro de un centro, donde se almacenan materiales
  - Áreas designadas para distintos tipos de materiales (materias primas, productos en proceso, productos terminados)
  - Sectores más sofisticados incluyen recipientes de almacenamiento, armarios, bandejas
- Un centro debe tener al menos un almacén
- Un almacén puede pertenecer sólo a un centro

Solo texto.

## Slide 9

**Almacenes de GBI** — Diagrama jerárquico organizacional en 4 niveles (filas horizontales con fondo celeste alternado), mostrando cómo se anidan Mandante → Sociedad → Centro → Almacén:

```
Mandante:  Empresa global GBI
              |
        +-----+-----+
        |           |
Sociedad: US00 Empresa EE.UU.      DE00 Empresa Alemana
        |                                |
   +----+----+                      +----+----+
   |    |    |                      |         |
Centro: DL00       SD00       MI00        HI00        HB00
       Centro     Centro     Centro      Centro      Centro
       Dallas    San Diego   Miami     Heidelberg   Hamburgo
        |          |          |           |           |
Almacén: RM00,SF00, FG00,       FG00,      RM00,SF00,  FG00,
         FG00,MI00  TG00,MI00   TG00,MI00  FG00,MI00   TG00,MI00
```

Fuente al pie: "Magal and Word | Integrated Business Processes with ERP Systems | © 2011", número de página 10.

Detalle: bajo US00 hay 3 centros (Dallas, San Diego, Miami), cada uno con sus propios códigos de almacén (algunos con 4 almacenes: RM00/SF00/FG00/MI00, otros con 3: FG00/TG00/MI00). Bajo DE00 hay 2 centros (Heidelberg, Hamburgo) con almacenes similares.

## Slide 10

Misma agenda, con "5) Organización de Compras" resaltado en recuadro naranja.

## Slide 11

**Organización de Compras**
- Rol estratégico en el aprovisionamiento de uno o más centros
- Identifica y selecciona proveedores
- Negocia condiciones generales de compra y contratos para uno o más centros o empresas
- Determina condiciones de fijación de precios
- Típicamente hay tres modelos de organización de compras:
  - Nivel Empresa Global
  - Nivel Sociedad
  - Nivel Centro

Solo texto.

## Slide 12

**Organización de Compras Nivel Empresa Global**
- Se conoce también como modelo multi-sociedad
- Se asigna una organización de compras a todas las sociedades de un mandante
- Compra para todos los centros a través de todas las sociedades
- Altamente centralizada – organización de compras corporativa

Dos elementos visuales lado a lado:

**Recuadro izquierdo "Modelo 1: Empresa Global" (estilo tarjeta apunte con cuadrícula):**
- Nivel: Altamente Centralizado (Multi-sociedad)
- Alcance: 1 Org. de Compras para todas las sociedades y centros del Mandante.
- Ventaja: Máximo poder de negociación global.

**Diagrama derecho:** un nodo circular grande superior etiquetado "ORG. DE COMPRAS GLOBAL" conectado por 10 líneas verdes a 10 nodos circulares pequeños en la fila inferior etiquetados "CENTROS/SOCIEDADES" — patrón de estrella (1 a muchos).

## Slide 13

**Organización de Compras Nivel Empresa Global** — repite el diagrama jerárquico de 4 niveles (Mandante → Sociedad → Centro → Organización de compras), similar al de la slide 9 pero cambiando la última fila:

```
Mandante: Empresa global GBI
Sociedad: US00 Empresa EE.UU. | DE00 Empresa Alemana
Centro:   DL00 Dallas, SD00 San Diego, MI00 Miami | HB00 Hamburgo, HI00 Heidelberg
Org. de compras: GL00 Organización de compras central (una única barra ancha con flechas hacia arriba conectando a TODOS los centros de ambas sociedades)
```

La fila "Organización de compras" es una sola barra que abarca todos los centros, mostrando centralización total. Pie: Magal and Word, página 15.

## Slide 14

Misma agenda, con "5) Organización de Compras" resaltado (naranja, sin subrayar), marcando el siguiente submodelo a tratar.

## Slide 15

**Organización de Compras Nivel Sociedad**
- Se conoce también como modelo multi-centro
- Diferentes organizaciones de compras se asignan a cada sociedad
- Compra para todos los centros de una sociedad

**Recuadro izquierdo "Modelo 2: Sociedad":**
- Nivel: Centralización Media (Multi-centro)
- Alcance: 1 Org. de Compras para todos los centros dentro de una sociedad específica.
- Ventaja: Adaptación a leyes y finanzas locales/nacionales.

**Diagrama derecho:** dos nodos circulares superiores (uno oscuro, uno gris), cada uno conectado por líneas verdes a 5 nodos inferiores. Grupo izquierdo etiquetado "CENTROS (SOCIEDAD A)", grupo derecho "CENTROS (SOCIEDAD B)" — dos estrellas independientes (2 organizaciones de compras, cada una centralizando su propia sociedad).

## Slide 16

**Organización de Compras Nivel Sociedad** — diagrama jerárquico de 4 niveles similar al de slide 13, pero ahora la fila "Organización de compras" tiene DOS barras separadas: "US00 Organización de compras EE.UU." (bajo los 3 centros de la sociedad US00) y "DE00 Organización de compras DE" (bajo los 2 centros de la sociedad DE00) — cada sociedad tiene su propia organización de compras. Pie: página 18.

## Slide 17

**Organización de Compras Nivel Centro**
- Conocida también como modelo específico de centro
- Cada centro tiene su propia organización de compras
- Altamente descentralizada

**Recuadro izquierdo "Modelo 3: Centro":**
- Nivel: Altamente Descentralizado (Específico de Centro)
- Alcance: 1 Org. de Compras por cada Centro.
- Ventaja: Agilidad máxima para necesidades locales y operativas diarias.

**Diagrama derecho:** 9 nodos superiores, cada uno conectado por una línea vertical individual a 8 nodos inferiores correspondientes (relación 1 a 1) — patrón de líneas paralelas verticales, sin centralización.

## Slide 18

**Organización de Compras Nivel Centro** — diagrama jerárquico de 4 niveles: cada uno de los 5 centros (DL00, SD00, MI00, HB00, HI00) tiene su PROPIA barra individual de "Organización de compras" debajo (ej. "DL00 Organización de compras Dallas", "SD00 Organización de compras San Diego", etc.) — 5 flechas independientes, una por centro, mostrando máxima descentralización. Pie: página 21.

## Slide 19

Misma agenda, con "6) Grupo de Compras" resaltado en recuadro naranja.

## Slide 20

**Grupo de Compras**
- Responsables de las actividades de compra del día a día.
- Principal punto de contacto con los proveedores.
- Actividades:
  - Planificar compras
  - Crear solicitudes de pedido
  - Solicitar cotizaciones a proveedores
  - Crear y monitorear pedidos de compra

Solo texto.

## Slide 21

Misma agenda, ahora con "2. Datos Maestros" resaltado en recuadro naranja y dentro de esa sección "1) Maestro de Materiales" también resaltado, marcando la transición al bloque de Datos Maestros.

## Slide 22

**Maestro de Materiales**
- Datos necesarios para ejecutar las transacciones relacionadas con los materiales (junto con los datos organizativos)
- Los datos se agrupan por segmentos funcionales llamados **Vistas**
- Los datos son específicos para (definidos por) diferentes niveles de la organización

**Captura de pantalla de UI SAP (lado derecho)** mostrando la ficha de un producto:
- Encabezado: logo "SAP", breadcrumb "Product", título del producto "Deluxe Touring Bike (black)", código "DXTR1000". Botones "Edit / Copy / Show in Hierarchy" arriba a la derecha.
- Datos rápidos: Product Type = Finished Product (FERT); Product Category = Product; Product Group = Finished Bikes (BIKES); Base Unit of Measure = Each (EA); Revision Level = —
- Pestañas de navegación: General Information (activa), Product Compliance, Components, Configuration, Sales, Storage, Warehouse Management, etc.
- Sección "Basic Data": Division = Bicycles (BI); Old Product Number = —; Basic Material = —; Batch Management Required = No; Marked for Deletion = No; Created By = Chris Reich, Created On = 08/19/2021 11:55:19; Last Changed By = Chris Reich, Last Changed On = 08/23/2021 12:36:09.
- Sección "Descriptions" con tabla de 2 columnas (Language, Product): DE (German) → "Deluxe Touring Bike (schwarz)"; EN (English) → "Deluxe Touring Bike (black)".

Pie de página: Magal and Word, página 21.

## Slide 23

**Maestro de Materiales – Vistas** — diagrama tipo "sol"/radial: un cilindro central azul oscuro etiquetado "Material Master" rodeado de 8 recuadros rectangulares (en inglés, términos SAP) distribuidos alrededor:
- Arriba: Sales Data
- Superior izquierda: Basic Data / superior derecha: Purchasing Data
- Derecha (descendente): Mat. Plan. Data, Forecasting Data, Storage Data
- Inferior izquierda: Controlling Data / inferior derecha: Quality Data
- Abajo: Accounting Data

Pie: Magal and Word, página 22.

## Slide 24

**Maestro de Materiales – Vistas** (continuación, versión texto de las vistas):
- **Datos Básicos**: Denominación, unidad de medida, peso, grupo de material
- **Compras**: Grupo de compras, tiempo de tratamiento de Entrada de Mercancías, tolerancias de entrega (bajo / sobre)
- **Contabilidad**: Moneda, categoría de valoración (vínculo con G/L), control de precios (precio variable, precio estándar, precio futuro)
- **Centro / Almacén**: Requerimientos de almacenamiento (humedad, temperatura, etc.), Periodo de validez, Instrucciones de manejo especial

Solo texto. Pie: página 23.

## Slide 25

**Maestro de Materiales – Vistas** (vistas para otros procesos):
- **Vistas para otros Procesos**
  - Pronóstico (proceso de Planificación de Materiales)
  - Ventas (proceso de Cumplimiento)
  - Programación de trabajo (proceso de Producción)
  - MRP (proceso de Producción)
  - Clasificación (proceso PLM)
  - Gestión de inventarios (proceso de Gestión de Stocks y Almacenes)

Solo texto. Pie: página 24.

## Slide 26

**Maestro de Materiales – Vistas** (ejemplos de vistas requeridas según tipo de material):
- Distintos tipos de materiales requieren diferentes vistas
- Ejemplos:
  - Materias primas: no tienen vista de ventas asociada
  - Productos terminados: no tienen vista de compras asociada
  - Mercaderías: no tienen vista de producción asociada

Solo texto. Pie: página 22 (numeración repetida del original).

## Slide 27

Misma agenda, con "2. Datos Maestros" resaltado en recuadro naranja y "2) Maestro de Proveedores" también resaltado dentro, marcando el siguiente tema.

## Slide 28

**Maestro de Proveedores**
- Datos necesarios para hacer negocios con los proveedores
- Datos necesarios para ejecutar transacciones relacionadas con los proveedores (junto con los datos organizativos)
- Los datos son específicos para (definidos por) diferentes niveles de la organización. Los tres segmentos son:
  - Datos a nivel de mandante (General)
  - Datos a nivel de sociedad (Contabilidad)
  - Datos a nivel de organización de compras (Compras)

Solo texto. Pie: página 27.

## Slide 29

**Maestro de Proveedores** — Diagrama tipo "3 hexágonos entrelazados" titulado "SEGMENTACIÓN DEL MAESTRO DE PROVEEDORES":
- Hexágono superior central, más oscuro y prominente: **CAPA CENTRAL: DATOS GENERALES (NIVEL MANDANTE)** → con flecha hacia un recuadro a la derecha: "Válido para toda la empresa global. Contiene: Nombre, Dirección, Criterios de búsqueda, Contactos."
- Hexágono inferior izquierdo: **CAPA INTERMEDIA: DATOS CONTABLES (NIVEL SOCIEDAD)** → con flecha hacia recuadro a la izquierda: "Válido para las áreas de compras de una sociedad. Contiene: Información bancaria, Cuenta asociada (Libro Mayor), Métodos de pago."
- Hexágono inferior derecho, en tono celeste/turquesa: **CAPA EXTERNA: DATOS DE COMPRA (NIVEL ORG. DE COMPRAS)** → con flecha hacia recuadro a la derecha: "Válido para una organización de compras específica. Contiene: Condiciones (InCoTerms), Función de interlocutor (solicitante, destinatario de factura)."

Los 3 hexágonos se superponen en el centro, visualizando que las 3 capas de datos coexisten en un mismo registro de proveedor.

## Slide 30

Misma agenda, con "2. Datos Maestros" resaltado y "3) Registro Info de Compras" resaltado, marcando el tema siguiente. (Nota: en esta versión "2) Maestro de Proveedores" aparece subrayado como recién cubierto).

## Slide 31

**Registro Info de compras**
- Relaciona proveedores y materiales. Contiene datos específicos.
- Un registro info de compras por cada combinación de proveedor y material (o grupo de materiales)
  - Datos generales (Número de proveedor, número de material o grupo, datos de contacto)
  - Datos de *Organización de Compras* (Acuerdos con el proveedor sobre tiempos de entrega, tolerancias de entrega, cantidades y condiciones de precio.)

Solo texto. Pie: página 35.

## Slide 32

**Registro Info de compras** — Diagrama esquemático titulado (subtítulo superior): "La intersección exacta entre 'Qué compramos' y 'A quién se lo compramos'."

Tres tarjetas de entrada en la parte superior, cada una sumada con un signo "+":
- **MAESTRO DE MATERIALES** (Ej. SHRT1000 - Camiseta)
- **+**
- **MAESTRO DE PROVEEDORES** (Ej. 100006 - Spy Gear)
- **+**
- **ORGANIZACIÓN DE COMPRAS** (Ej. US00)

Las tres flechas naranjas convergen hacia abajo en un documento con forma de "hoja con esquina doblada" titulado:
**= REGISTRO INFO (LA REGLA DE NEGOCIO)**, que contiene:
- **TIEMPO DE ENTREGA PLANIFICADO**: Ej. 4 días. (con ícono de reloj/cronómetro)
- **CONDICIONES**:
  - Precio Bruto: Ej. $15/unidad
  - Descuentos: Ej. -4% descuento
  - Recargos, Fletes
- **HISTORIAL**: Última orden de pedido.

Es un diagrama tipo fórmula visual: Material + Proveedor + Org.Compras = Registro Info.

## Slide 33

Misma agenda, con "2. Datos Maestros" y "4) Condiciones" resaltados en naranja, marcando el tema final de la sección de datos maestros.

## Slide 34

**Condiciones**
- No se definen para una combinación específica de proveedor y material.
- Se basan en todos los acuerdos y contratos hechos con proveedores.
- La empresa usa estos datos para Condiciones de fijación de precios
  - Precio bruto
  - Descuentos y recargos
  - Transporte / envío
- Obtenidos desde
  - Registro info de compras
  - Contratos y acuerdos
  - Otras fuentes

Solo texto. Pie: página 43.

Nota: al final del set de imágenes aparece una slide adicional numerada "4" en el pie ("Ejercicio SAP: Visualización de documentos de compra", con el mismo diagrama de flujo de la slide 2 más roles MM1-MM4/Buyer/Receiving Clerk/AP Specialist) que corresponde a la page-034.png; se documenta como Slide 34 según el orden físico de archivos, aunque su numeración de pie de página interna del PDF original (4) no seguía la secuencia — es la última imagen del set:

**Ejercicio SAP: Visualización de documentos de compra**

Mismo diagrama de flujo de 4 iconos y tarjetas de rol/actividad que en la slide 2 (Almacén→Crea solicitud de pedido, Compra→Crea y envía orden de pedido, Almacén→Recibe materiales, Contabilidad→Recibe factura, Contabilidad→Envía pago), pero añade debajo de cada etapa la referencia a la transacción SAP y el rol responsable:

| Etapa | Transacción SAP | Rol |
|---|---|---|
| Compra (orden de pedido) | MM 1: Display Purchase Order | Buyer |
| Almacén (recibe materiales) | MM 2: Display Goods Receipt for Purchase Order | Receiving Clerk |
| Contabilidad (factura/pago) | MM 3: Display Invoice Overview / MM 4: Display Payment to Vendor | AP Specialist |

Pie: Magal and Word, página 4.
