---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Slides_QM_en_v4.3_VF
slides: 29
fuente: Intro_S4HANA_Using_Global_Bike_Slides_QM_en_v4.3_VF.pdf
---

## Slide 1

Portada decorativa. Título "Quality Management (QM)", subtítulo "Curriculum: Introduction to S/4HANA using Global Bike". Foto de fondo decorativa (manos sobre escritorio con documentos/post-its). Logo "SAP University Alliances" y logo "SAP UCC Magdeburg" (chrome decorativo).

## Slide 2

Título "Teaching material - Information". Icono decorativo de documentos.
- Sección "Teaching material - Version":
  - Versión: 4.3 (June 2025)
  - Software used: SAP S/4HANA 2023, Fiori 3.0
  - Model: Global Bike
  - Prerequisites: No Prerequisites needed
- Imagen: logo "Global Bike" (icono de bicicleta en verde sobre fondo verde, forma de placa/letrero inclinado).

## Slide 3

Título "Module Information". Dos bloques con iconos decorativos:
- Icono lápiz: "Authors" — Tim Böttcher, Babett Ruß
- Icono personas: "Target Audience" — Beginner

## Slide 4

Título "Module Information". Icono decorativo de diana (target).
- "Learning Objectives" — "You are able to":
  - name functionalities of the QM module.
  - define the central organizational structures of the QM module.
  - summarize the master data which is most important for the QM module.
  - explain a standard QM process.

## Slide 5

Título "Functionality". Lista en dos columnas (sin iconos, solo viñetas):
- Columna izquierda: Quality Planning, Quality Inspection, Quality Control, Quality Certificates, Quality Notifications, Test Equipment Management, Inspection Using Multiple Specifications, Stability Study
- Columna derecha: Control in Logistics, Archiving, Data Transfer

## Slide 6

Slide de agenda "Unit Overview" con 3 ítems, donde el ítem activo se resalta en negro y los demás en gris claro (efecto de foco progresivo). En esta slide el resaltado es "QM Organizational Structure":
- QM Organizational Structure (resaltado, negro)
- QM Master Data (gris, atenuado)
- QM Processes (gris, atenuado)

## Slide 7

Título "QM Organizational Structure". Definiciones jerárquicas (texto, sin diagrama):
- Client: An independent environment in the system
- Company Code: Smallest org unit for which you can maintain a legal set of books
- Plant: Operating area or branch within a company (Manufacturing, distribution, purchasing or maintenance facility)
- Storage Location: An organizational unit allowing differentiation between the various stocks of a material in a plant

## Slide 8

Título "QM Organizational Structure" (continuación). Definiciones de compras:
- Purchasing Organization: The buying activity for a plant takes place at the purchasing organization; Organization unit responsible for procuring services and materials; Negotiates conditions of the purchase with the vendors
- Purchasing Group: Key that represents the buyer or group of buyers who are responsible for certain purchasing activities; Channel of communication for vendors

## Slide 9

Título "Global Bike Structure for Quality Management". Diagrama de organigrama jerárquico (recuadros azul oscuro conectados por líneas):
- Nivel Client: "Global Bike" (raíz)
- Nivel Company Code: se ramifica en "Global Bike Inc." y "Global Bike Germany GmbH"
- Nivel Plant: bajo Global Bike Inc. → "Dallas", "San Diego", "Miami"; bajo Global Bike Germany GmbH → "Heidelberg", "Hamburg"
- Nivel Storage Location: bajo cada plant, lista de storage locations:
  - Dallas: Raw Materials, Semi-fin. Goods, Finished Goods, Miscellaneous
  - San Diego: Trading Goods, Finished Goods, Miscellaneous
  - Miami: Trading Goods, Finished Goods, Miscellaneous
  - Heidelberg: Raw Materials, Semi-fin. Goods, Finished Goods, Miscellaneous
  - Hamburg: Trading Goods, Finished Goods, Miscellaneous
- A la derecha del diagrama, etiquetas verticales indicando el nivel jerárquico de cada fila: Client, Company Code, Plant, Storage Location.

## Slide 10

Título "Global Bike Enterprise Structure in SAP ERP (Logistics)". Diagrama 3D en capas (vista isométrica tipo "libro apilado") mostrando la estructura empresarial completa:
- Capa inferior "Client Global Bike": Company Codes CC US00 (plants Dallas DL00, Miami MI00, S. Diego SD00), CA00 (plant Toronto TO00, en gris = no relevante/no cubierto), CC DE00 (plants Heidelb. HD00, Hamburg HH00), AU00 (plant Perth PE00, en gris)
- Capa media "Central Purchasing Organization (global) GL00": contiene Purchasing Org. US00 (con Purchasing Group North America N00), CA00 (gris), PO DE00 (con PGr Europe E00), AU00/Asia A00 (gris)
- Capa superior "Storage Location / Shipping Point": para cada plant se listan storage locations (RM00, SF00, FG00, MI00, TG00 según plant) y el shipping point resaltado en naranja (DL00, MI00, SD00, HD00, HH00); plants TO00 y PE00 en gris (no cubiertos en este curso)
- Colores: verde = plants US, azul = plants DE, gris = plants no cubiertos (Canadá, Australia)

## Slide 11

Slide de agenda "Agenda" (mismo patrón de la slide 6), en esta ocasión resaltando "QM Master Data":
- QM Organizational Structure (gris)
- QM Master Data (resaltado, negro)
- QM Processes (gris)

## Slide 12

Título "Customer Master Data".
- Texto: Customer Master — Contains all of the information necessary for processing orders, deliveries, invoices and customer payment; Every customer MUST have a master record
- Created by Sales Area: Sales Organization, Distribution Channel, Division
- Captura de pantalla SAP Fiori (Business Partner "Quality Bikes 114", ID 1003066): muestra cabecera con Standard Address (Lusk Blvd., San Diego CA 92121, USA) y Standard Communication; pestañas Basic Data/Roles/Address/Address-Independent Communication/Bank Accounts/Payment Cards/Identification/Contacts/Relationships; sección "General Information" con campos Organization Title (Company), Name 1 (Quality Bikes 114), Foundation Date, Created By (Learn-114), Created On (03/26/2025), Authorization Group (Stakeholder: Visibility 0 Unrestricted), Last Changed On (03/26/2025); sección "Address / Standard Address" con Street (Lusk Blvd.), Country/Region (USA US), Postal Code (92121), Region (California CA), City (San Diego).

## Slide 13

Título "Customer Master Data" (continuación).
- Texto: "The customer master information is divided into 3 areas": General Data, Company Code Data, Sales Area Data
- Captura de pantalla SAP Fiori (Customer "Quality Bikes 114", ID 1003066): pestaña "Company Codes" activa, mostrando tabla "Company Codes (1)": fila con Company Code "Global Bike Inc. / US00", Reconciliation Account 1200000, Posting Block No, Deletion Block No. Debajo, tabla "Sales Areas (1)": fila con Sales Organization "US West / UW00", Distribution Channel "Wholesale / WH", Division "Bicycles / BI".

## Slide 14

Título "Material Master Data".
- Texto: Material Master — Contains all the information a company needs to manage about a material; It is used by most components within the SAP system: Sales and Distribution, Materials Management, Production, Plant Maintenance, Accounting/Controlling, Quality Management; Material master data is stored in functional segments called Views
- Captura de pantalla SAP Fiori (Product "Women's Off Road Bike", ORWN1114): cabecera con Product Type Finished Product (FERT), Base Unit of Measure Each (EA), Division Bicycles (BI), Old Product Number, Basic Material; pestañas General Information/Product Compliance/Components/Configuration/Sales/Storage/Warehouse Management/Extended Service Parts Pl.; tabla "Descriptions (4)" con idiomas: German "Mountainbike Damen", English "Women's Off Road Bike", French "VTT Femme", Russian (texto cirílico).

## Slide 15

Título "Material Master Views". Diagrama tipo "base de datos cilíndrica" central etiquetada "Material Master" con 8 recuadros rectangulares alrededor conectados conceptualmente (vista de "flor"/hub-and-spoke): Sales Data, Purchasing Data, Basic Data, Mat. Plan. Data, Forecasting Data, Storage Data, Controlling Data, Quality Data, Accounting Data. Los recuadros con borde naranja (Sales Data, Basic Data, Purchasing Data, Storage Data, Quality Data) se distinguen de los de borde negro (Mat. Plan. Data, Forecasting Data, Controlling Data, Accounting Data) — probablemente indicando las vistas cubiertas/relevantes vs. las demás.

## Slide 16

Título "Material Master". Diagrama de cilindros apilados en 3 grupos mostrando la jerarquía de datos del material maestro:
- Cilindro superior gris "Client XXX": "General Information relevant for the entire organization" — atributos: Name, Weight, Unit of Measure
- Grupo inferior izquierdo (amarillo/dorado), dos cilindros superpuestos "Sales Org. UW00" y "Sales Org. UE00": "Sales specific information" — atributos: Delivering Plant, Loading Grp
- Grupo inferior derecho (azul), dos cilindros superpuestos "Storage Loc. FG00" y "Storage Loc. TG00": "Storage Location specific information" — atributo: Stock Qty

## Slide 17

Título "Vendor Master Data".
- Texto: Vendor Master — Contains all the necessary information needed to business with an external supplier; Used and maintained primarily by the Purchasing and Accounting Departments; Every vendor MUST have a master record
- Captura de pantalla SAP Fiori (Business Partner "Mid-West Supply 005", ID 1003050): Standard Address (335 W Industrial Lake Dr, Lincoln NE 68528, USA); pestañas Basic Data/Roles/Address/Address-Independent Communication/Bank Accounts/Payment Cards/Identification; sección General Information con Organization Title (Company), Name 1 (Mid-West Supply 005), Search Term 1 (005), Legal Form, Authorization Group, Created By (Learn-005); sección Address/Standard Address con Street, Country/Region (USA US), Region (Nebraska NE), City (Lincoln).

## Slide 18

Título "Vendor Master Views". Lista de texto a la izquierda y 3 recuadros con esquinas redondeadas a la derecha (código de color):
- Texto: Client Level (Address, Vendor Number, Preferred Communication); Company Code Data (Reconciliation Account, Terms of Payment, Bank Account); Purchase Org Data (Purchasing Currency, Salesman's Name, Vendor Partners)
- Recuadros: gris "General Data"; azul oscuro "Company Code Data / Financial Accounting (FI)"; dorado "Purchasing Data / Materials Mgmt (MM)"

## Slide 19

Título "Vendor Master". Diagrama de cilindros apilados (mismo estilo que slide 16):
- Cilindro superior gris "Client XXX": "General Information relevant for the entire organization" — atributos: Name, Address, Communication
- Grupo inferior izquierdo (amarillo/dorado), cilindros "Company Code US00" y "Company Code DE00": "Company Code specific information" — atributos: Acc. Mgmt, Payment, Bank
- Grupo inferior derecho (azul), cilindros "Purch. Org. US00" y "Purch. Org. DE00": "Purch. Organization specific information" — atributos: Incoterms, Currency

## Slide 20

Slide de agenda "Agenda" (mismo patrón), resaltando "QM Processes" con sub-lista visible (los otros dos ítems atenuados en gris):
- QM Organizational Structure (gris)
- QM Master Data (gris)
- QM Processes (resaltado, negro), con sub-bullets: Quality Management, Quality Management in Procurement, Quality Management in SD

## Slide 21

Título "QM Process". Diagrama de flujo horizontal: 5 recuadros dorados dentro de una gran flecha translúcida apuntando a la derecha, en secuencia:
Quality Info. Record → Inspection Plan → Inspection Lot → Perform Inspection → Usage Decision

## Slide 22

Título "Quality Information Record". En la esquina superior derecha se repite el diagrama de flujo de la slide 21 en miniatura, con el paso "Quality Info. Record" resaltado con un círculo rojo (indicando que esta slide detalla ese paso).
- Bullets: If a quality assurance agreement or vendor release is required for a material, a Quality Info. Record must be created; Determines how a material can be processed further; when a quotation or purchase order is created, the system checks whether a quality info record is required and available for the combination of material and vendor; System also checks, whether the vendor and material-vendor combination is blocked or released for quotations, purchase orders and/or goods receipt

## Slide 23

Título "Inspection Plan". Mismo diagrama de flujo en miniatura arriba a la derecha, con "Inspection Plan" resaltado en círculo rojo.
- Bullets: Can be created for different uses as model inspection, carrying out an audit, preliminary series inspection, goods receipt inspection, goods issue inspection, inspection of stock transfers, inspections in repetitive manufacturing; Defines which characteristics are to be inspected in each inspection operation and which test equipment is to be used in the inspection; Several materials can be assigned to an inspection plan; Several inspection plans with different inspection operations or inspection characteristics can be created for a material or combination of material, vendor and manufacturer, or material and customer

## Slide 24

Título "Inspection Lot". Diagrama de flujo en miniatura con "Inspection Lot" resaltado en círculo rojo.
- Bullets: Request to a plant to inspect a specific quantity of material or one or more pieces of equipment or functional locations; Documented by an inspection lot record; Used to record, process and manage information for a quality inspection; Whenever materials are moved from on place to another under certain conditions, the QM component can automatically create inspection lots; The system can also create an inspection lot automatically if a delivery is created in the SD component for a inspection-relevant material; Can be created automatically or manually

## Slide 25

Título "Perform Inspection". Diagrama de flujo en miniatura con "Perform Inspection" resaltado en círculo rojo.
- Bullets: Inspection of sample units of the inspection lot; Number of non-conforming sample units entered in the SAP System

## Slide 26

Título "Usage Decision". Diagrama de flujo en miniatura con "Usage Decision" resaltado en círculo rojo.
- Bullets: Confirms that all physical samples have been valuated and the inspection has been completed; Specifies whether the goods in the inspection lot have been accepted or rejected for use; Inspection lot stock can be posted to different stocks: Unrestricted use, Scrap, Sample usage, Blocked stock

## Slide 27

Título "QM Process in Procurement". Diagrama de flujo horizontal ampliado (7 recuadros dorados dentro de flecha translúcida):
Quality Info. Record → Inspection Plan → Purchase Order → Receiving Material → Inspection Lot → Perform Inspection → Usage Decision
Un óvalo rojo grande rodea los dos pasos nuevos específicos de procurement: "Purchase Order" y "Receiving Material", que se insertan entre Inspection Plan e Inspection Lot respecto al proceso genérico de las slides 21-26.

## Slide 28

Título "Quality Management in SD". Diagrama de flujo horizontal ampliado (10 recuadros dorados dentro de flecha translúcida):
Quality Info Record → Inspection Plan → Goods Issue → Inspection Lot → Perform Inspection → Usage Decision → Goods Receipt → Sales Order → Outbound Delivery → Invoice
Un óvalo rojo grande rodea los últimos 3 pasos del ciclo de venta: "Goods Receipt", "Sales Order", "Outbound Delivery" (justo antes de Invoice), resaltando la porción del proceso relevante para SD (Sales and Distribution).

## Slide 29

Título "SAP QM Module Integration".
- Bullet principal: High integration in other SAP modules including:
  - SAP MM — e.g. maintain quality agreements
  - SAP SD — e.g. quality information related to customers
  - SAP PP — e.g. perform inspection planning
  - SAP CO — e.g. integrate SAP QM with controlling process
