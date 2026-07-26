---
curso: SIOPS
titulo: 1. Teoría Semana 2 - System Wide Concepts I
slides: 9
fuente: 1. Teoría Semana 2 - System Wide Concepts I.pdf
---

## Slide 1

Portada.

# System Wide Concepts I
### Explain the Organizational Structures

Profesor: Carlos Villanueva Qwistgaard
IN3010 - Sistemas de Información para Operaciones

(Plantilla decorativa: círculos y tramas celestes, logo UTEC — chrome.)

## Slide 2

# Agenda

| # | Tema |
|---|------|
| 01 | Organizational Structures |
| 02 | Master Data |
| 03 | Material Master |
| 04 | Transaction Data |

Fondo decorativo: foto de edificios en tono celeste desaturado (decorativa).

## Slide 3

# Organizational Structures

Texto (columna izquierda):

- The **enterprise structure** of a company is mapped to SAP applications using organizational units.
- **Organizational units** represent the enterprise structure in terms of legal or business-related purposes.
- Organizational units include legal company entities, plants, storage locations, sales offices, and profit centers.

**Visual (derecha): diagrama jerárquico SAP de estructura empresarial.** Dos columnas: a la izquierda el árbol de ejemplo (fondo gris) y a la derecha, en banda amarilla con encabezado naranja "SAP", el nombre del nivel organizativo correspondiente. Líneas punteadas horizontales separan cada nivel; iconos SAP (edificio, planta, personas) al margen izquierdo de cada fila.

Correspondencia nivel por nivel (ejemplo → nivel SAP):

| Ejemplo en el árbol | Nivel SAP | Agrupación (llaves a la derecha) |
|---|---|---|
| IDES (edificio raíz) | Client | Enterprise Structure |
| Europe · North America | Controlling area | Enterprise Structure |
| Germany · France | Company code | Enterprise Structure |
| Customer service · Production · … | Organizational unit | Organizational Structure |
| Head of department · Employee · Employee | Position | Organizational Structure |
| FRA · BER · HAM | Sales organization | Enterprise Structure |
| Pumps · Paints · Pharma | Division | Enterprise Structure |
| FRA · BER · HAM | Plant | Enterprise Structure |
| 0001 · 0002 · … | Storage locations | Enterprise Structure |

Conexiones del árbol: IDES cuelga de la raíz y se ramifica a Europe y North America; Europe → Germany y France; Germany baja tanto por la rama de unidades organizativas (Customer service / Production, y de Production cuelgan Head of department, Employee, Employee) como por la rama de ventas/logística (FRA, BER, HAM → Pumps, Paints, Pharma → plantas FRA, BER, HAM → almacenes 0001, 0002, …).

## Slide 4

# Organizational Structures

Misma figura de la slide 3 (diagrama IDES → Client / Controlling area / Company code / Organizational unit / Position / Sales organization / Division / Plant / Storage locations), ahora ubicada a la izquierda, con el texto explicativo a la derecha:

- **Client** is the highest-level unit of all organizational elements. It represents the enterprise or headquarters group.
- **Company code** is a unit used in the balance sheet of a legally independent enterprise. It is the central organizational element of Financial Accounting (FI).
- **Sales organization** is the central organizational element of Sales and Distribution that controls the terms of sale to the customer. A division is usually used to represent a product line.
- **Plant** is the central organizational unit in the context of production planning. A plant can manufacture product, distribute product, or provide a service.

## Slide 5

# Understanding the Concept of Master Data

**Master Data**

Master data represent entities associated with various processes. For example, processes involve buying **materials** from **vendors** and selling materials to **customers**. In this example, customers, vendors, and materials are represented in an ERP system using master data.

The most commonly used master data in an organization is the **material master.** Materials are used in numerous processes. They are purchased, sold, produced, and planned for. They are used in maintenance and service, and in projects. Consequently, material master data are some of the most complex and extensively utilized data in an ERP system.

**Visual (derecha): diagrama radial "Material master data".** Al centro, un cilindro de base de datos azul rotulado **Material master**; alrededor, 8 cajas azules dispuestas en círculo (sin flechas, solo posición radial):

- Sales data (arriba)
- Plant/Storage data (arriba derecha)
- Warehouse management data (derecha)
- MRP data (abajo derecha)
- Purchasing data (abajo)
- Management accounting data (abajo izquierda)
- Financial accounting data (izquierda)
- Basic data (arriba izquierda)

Pie de figura en azul: "Material master data". Flechas celestes tipo chevron a la izquierda del texto (decorativas).

## Slide 6

# Understanding the Concept of Master Data

**Material Master**

The material master contains the information that a company needs to manage a type of material. The material master defines how a product is sold, manufactured, purchased, inventoried, and costed. The information in the material master is grouped into **views** that are organized by business function.

**Visual:** la misma figura radial de la slide 5 (cilindro *Material master* rodeado por Sales data, Plant/Storage data, Warehouse management data, MRP data, Purchasing data, Management accounting data, Financial accounting data, Basic data), con pie "Material master data".

## Slide 7

Título superior: **Material Master**
Título de slide: **Understanding the Concept of Master Data**

**Visual 1 (arriba derecha, reducido):** el diagrama radial del material master (mismas 8 cajas alrededor del cilindro).

**Visual 2 (captura de pantalla SAP Fiori/GUI, ocupa la mitad inferior):** pantalla "Display Material SHRT1050 (Trading Goods)". Una flecha negra gruesa va desde la caja **Basic data** del diagrama radial hasta la pestaña **Basic data 1** de la captura, indicando que cada caja del diagrama es una vista (view) del material master.

Detalle de la UI:
- Barra superior azul con logo SAP, iconos de usuario/atrás/inicio y lupa de búsqueda; título "Display Material SHRT1050 (Trading Goods)".
- Barra de menú: Other Material · Additional Data · Org. Levels · Services for Object ▾ · More ▾
- Pestañas de vistas: **Basic data 1** (activa) · Basic data 2 · Sales: sales org. 1 · Sales: sales org. 2 · Sales: General/Plant · Intl Trade: Export · Sales text
- Campos de cabecera: Material: `SHRT1050` · Descr.: `T-shirt`
- Sección **General Data** (campos y valores visibles):

| Campo | Valor | Campo | Valor |
|---|---|---|---|
| Base Unit of Measure | EA (each) | Material Group | UTIL |
| Old material number | (vacío) | Ext. Matl Group | (vacío) |
| Division | AS | Lab/Office | (vacío) |
| Product allocation | (vacío) | Prod.hierarchy | (vacío) |
| X-Plant Matl Status | (vacío) | Valid from | (vacío) |
| Assign effect. vals | (checkbox desmarcado, gris) | GenItemCatGroup | NORM — Standard item |

## Slide 8

# Transaction Data

Transaction data reflect the consequences of executing process steps, or transactions. Examples of transaction data are dates, quantities, prices, and payment and delivery terms. Thus, transaction data are a combination of organizational data, master data, and situational data—that is, data that are specific to the task being executed, such as who, what, when, and where.

**Visual (derecha, sobre banda azul diagonal): diagrama de convergencia.** Tres cajas azules en la fila superior, cada una con sus viñetas, y tres flechas azules gruesas que apuntan hacia un círculo central inferior rotulado **Transaction data**:

- **Org data** (izquierda): Client · Company code · Plant → flecha diagonal hacia abajo-derecha
- **Master data** (centro): Customer · Vendor · Material → flecha vertical hacia abajo
- **Situational data** (derecha): Who · When · Where → flecha diagonal hacia abajo-izquierda

## Slide 9

# Transaction Data

SAP ERP uses several different **types of documents** to record transaction data. Some of these documents are created or utilized as the process is being executed; others record data after the process steps are completed.
We refer to the first category as **transaction documents.** Examples are purchase orders, packing lists, and invoices.

Texto inferior derecho: Documents that record data generated after the process steps have been completed include financial accounting [FI] documents, management accounting or controlling [CO] documents, and material documents.

**Visual (derecha): facsímil de una orden de compra (PURCHASE ORDER)** de ejemplo, con llaves a la derecha que marcan las dos zonas: **Header** (parte superior) y **Line items** (tabla de posiciones).

Encabezado:
- Emisor: Global Bicycle Incorporated — 5215 N. O'Conner Blvd., Dallas, Texas, 75039 — Phone: +1.972.555.2000 · Fax: +1.972.555.2001
- Aviso: "THE PURCHASE ORDER NUMBER MUST APPEAR ON ALL RELATED CORRESPONDENCE, SHIPPING PAPERS, AND INVOICES"
- Purchase Order Number: 4546
- TO: Olympic Protective Gear, 2100 Summit Boulevard, Atlanta, GA, 30319
- SHIP TO: GBI San Diego Distribution Center, 150 Spear Street, San Diego, 94105, +1.415.555.7700

Tabla de cabecera:

| Purchase Order # | P.O. Date | Delivery Date | Shipped VIA | F.O.B. Point | Payment Terms |
|---|---|---|---|---|---|
| 4546 | July 11, 2009 | July 27, 2009 | Ground | Destination | Net 30 |

Tabla de posiciones (line items):

| Quantity | Material # | Material Description | Unit Type | Unit Price | Item Total |
|---|---|---|---|---|---|
| 100 | KPAD1000 | Knee Pads | Each | 37.50 | 3,750.00 |
| 100 | EPAD1000 | Elbow Pads | Each | 37.50 | 3,750.00 |
| 50 | OHMT1000 | Off-road Helmets | Each | 25.00 | 1,250.00 |

Totales:

| Concepto | Valor |
|---|---|
| SUBTOTAL | $8,750.00 |
| SALES TAX | Exempt |
| SHIPPING AND HANDLING | Included |
| OTHER | N/A |
| ORDER TOTAL | $8,750.00 (resaltado) |

Pie del documento: líneas de firma "Authorized by: ______ (Purchasing Manager)" y "Date: ______".
