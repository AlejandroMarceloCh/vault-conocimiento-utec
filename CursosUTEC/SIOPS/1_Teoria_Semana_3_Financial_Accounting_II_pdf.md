---
curso: SIOPS
titulo: 1. Teoría Semana 3 -Financial Accounting II
slides: 14
fuente: 1. Teoría Semana 3 -Financial Accounting II.pdf
---

## Slide 1

Portada del curso. "Financial Accounting II" — Profesor: Carlos Villanueva Qwistgaard. IN3010 - Sistemas de Información para Operaciones. Fondo fotográfico decorativo (oficina), logo UTEC decorativo.

## Slide 2

Slide de agenda con 3 puntos numerados (círculos amarillos 01/02/03):
- 01 Integration between FI and CO
- 02 SAP S/4HANA Finance - Simplified data model
- 03 Working with Business Partners and Invoices

Incluye foto decorativa de grupo de personas de negocios a la derecha.

## Slide 3

Título "Introduction". Texto: "There is an integration between FI and CO". Imagen decorativa de personas revisando reportes/gráficos sobre una mesa.

## Slide 4

Sección 01 "FI and CO Integration". Diagrama (recuadro con borde negro grueso, marcado "01"):

```
Financial Accounting
  AP -\
  AR ---\
  Assets--> G/L --> Legal Reporting
  Banks-/
....................... "Common Line Items — Single Version of Truth" .......................
Internal Management Reporting
  Cost Center Accounting   Product Costing (Manufacturing Order)   Profitability Accounting
Management Accounting
```
Flechas: AP, AR, Assets y Banks apuntan hacia el bloque G/L, que desemboca en "Legal Reporting". Una flecha baja desde Legal Reporting hacia Internal Management Reporting y otra sube desde Internal Management Reporting de vuelta (doble sentido) cruzando la línea punteada "Common Line Items - Single Version of Truth". Abajo del todo, Cost Center Accounting, Product Costing/Manufacturing Order y Profitability Accounting caen bajo "Management Accounting".

Texto: "Profitability or profit center accounting let us determine the profit/loss by profit center. You design the profit center and assign it to the respective objects that you want to capture. Cost Objects are: cost centers, internal orders, production orders, WBS elements, maintenance orders, activities. There are objects considered real objects: cost centers, profitability segments"

## Slide 5

Sección 01 "FI and CO Integration" (mismo diagrama de la slide 4, reducido, al costado derecho: Financial Accounting → AP/AR/Assets/Banks → G/L → Legal Reporting / Internal Management Reporting → Cost Center Accounting, Product Costing, Profitability Accounting → Management Accounting).

Texto: "The main task of FI is basically to post FI transactions, revenue and expenditures, legal reporting requirements. On the CO side, the main purpose is to capture costs, collect revenues or expenditures by areas of responsibility. We have objects created in FI (mainly G/L accounts), others created in CO (cost centers, internal orders, production orders, maintenance orders)."

## Slide 6

Sección 01 "FI and CO Integration". Diagrama con 4 bloques apilados y bocadillos (callouts) naranjas explicando el "por qué" de cada capa:

```
Profitability Analysis          → callout: "How profitable?"
Profit Center Accounting (Bal. sheet | P&L) → callout: "In which area?"
Overhead Cost Controlling                    | Product Cost Controlling
  Cost Center Accounting, Activity-Based      | Project, Production Order, Sales Order
  Costing, Internal Order → callout "Where?"  | → callout "For what?"
Cost Element Accounting → callout: "What costs?"
```

Texto: "When we incur some kind of cost, it is captured by Cost Accounting"

## Slide 7

Sección 01 "FI and CO Integration". Diagrama de dos franjas superpuestas conectadas por una doble barra roja "II" (equivalencia):

```
G/L Accounts (FI):  [Neutral Expenditures] [Expenditures]
                                    ‖ (barras rojas = equivalencia)
Cost Elements (CO):                [Cost] [Imputed Cost]
```
FI arriba (gris), CO abajo (blanco), etiquetados a la derecha del diagrama.

Texto: "On the FI side, we create expenditures, referred as costs. On the CO side, this costs are captured by a Cost Element."

## Slide 8

Sección 01 "FI and CO Integration". Diagrama de franjas apiladas por tipo de cuenta con tabla de códigos a la derecha:

Franjas (de arriba a abajo): Balance Sheet Accounts / Non Operating Expenses-Revenues / Primary Cost Elements / Secondary Cost Elements.

Tabla "Account Types (on CO-Area Level)":
| Código | Significado |
|---|---|
| X | Balance Sheet |
| N | Non operating expenses/ revenues |
| P | Primary costs/ revenues |
| S | Secondary cost elements |

Texto: "When we create a G/L account, we link it automatically to the primary cost element. Primary and secondary costs elements are created in FI but they live in CO."

## Slide 9

Sección 01 "FI and CO Integration". Diagrama de flujo jerárquico "General Ledger (G/L) Accounts and Cost Elements":

```
Management level:        Costs
                     /              \
              Primary costs      Secondary costs
                   |                    |
Predefined by SAP: Primary cost         Secondary cost
                    element categories  element categories
                   |                    |
Mgmt accounting    Primary cost         Secondary cost
master data:       elements             elements
                   ‖ (doble línea = equivalencia)         ‖
Financial accounting master data:   FI G/L accounts
                                          |
                                    Chart of accounts
```

Texto: "Primary cost elements are stored in Management Accounting Master Data and then we have Financial accounting master data, in the form of G/L accounts"

## Slide 10

Slide "Review" (encabezado sobre fondo naranja con foto decorativa de personas). Repite el diagrama de la slide 4 (Financial Accounting → AP/AR/Assets/Banks → G/L → Legal Reporting; Internal Management Reporting → Cost Center Accounting, Product Costing/Manufacturing Order, Profitability Accounting → Management Accounting).

Texto: "when we are capturing our expenditures on the FI side, those same expenditures and revenues can be recorded on the CO side by way of my primary cost elements."

## Slide 11

Sección 02 "SAP S/4HANA Finance - Simplified Data Model". Diagrama de tablas relacionadas por flechas de colores, mostrando cómo distintos módulos alimentan la tabla única "Universal Journal (table ACDOCA)":

Tabla superior izquierda "General Ledger": columnas Ledger | Company | Account | Profit Center | Amount 1 | Amount 2 | Amount 3 | ...
Tabla superior derecha "Profitability": columnas Operating Concern | Market Segment | ...
Ambas con flecha hacia abajo hacia:

Tabla central "Universal Journal (table ACDOCA)": columnas Ledger | Company | Account/Cost Element | Profit Center | Amount 1 | Amount 2 | Amount 3 | Coding Block | Fixed Asset | Market Segment | Material | Customer Fields | ...

Desde abajo, 3 tablas alimentan con flecha hacia arriba a la Universal Journal:
- "Management Accounting": Controlling Area | Cost Element | Amount 1 | Amount 2 | Coding Block | ...
- "Asset Accounting": Company | Fixed Asset | ...
- "Material Ledger": Company | Material | ...

Bullets a la derecha:
- Universal journal is the basis of SAP's integrated accounting system.
- FI and CO are using one table.
- Documents posted to the universal journal or general ledger documents, CO documents, asset documents, material management documents and profitability analysis

## Slide 12

Sección 02 "SAP S/4HANA Finance - Simplified Data Model". Slide solo texto (sin diagrama), con foto circular decorativa de una persona con documentos/calculadora.

- FI – Finance Accounting
  - FI is intended for legal reporting. It can be used to draw up a balance sheet and an income statement at the level of accounting entities.
  - The level at which FI is needed is determined by law. Legal reporting is different for each country.
- CO – Management Accounting
  - The purpose of Management Accounting is to collect revenue and expenses by areas of responsibility to be used for internal management reporting purposes.
  - Management Accounting analyzes costs and revenues at high levels across country boundaries. For example, it can analyze costs for all production departments worldwide.
  - Costs and revenues from FI are used in Management Accounting.
  - Management Accounting provides Controlling (CO) objects, which can represent areas of responsibilities that incur costs, revenues, or both, which allow an organization to track both costs and revenues internally.

## Slide 13

Sección 03 "Working with Business Partners and Invoices". Diagrama de mapeo entre "Business Partner General Data" y "Company Code Data":

```
Business Partner General Data
  Business Partner Category: Person
  Business Partner Role: FI Customer
  Business Partner Grouping: Internal number assignment
                                    → (flecha)
Company Code Data
  Company Code 1010
  Company Code 1710
  Company Code 5050
```

Texto (en recuadro con fondo negro/blanco superpuesto a la foto decorativa): "Any company that wishes to do business with a specific vendor has to create a company code segment. The company code data contains information such as the reconciliation account, terms of payment, payment methods, dunning data, or correspondence settings."

## Slide 14

Título "Vendor Master Record — Business Partner". Diagrama: iconos de "Customer" (grupo de 3 personas) y "Vendor" (persona en mostrador) ambos conectados mediante un icono central de "Business Partner" (apretón de manos). Debajo, lista "Business Partner Category": Person, Organization, Group.

Texto: "In SAP S/4HANA, Business Partner is the term used to classify a natural person, group (married couple, executive board) or organization (legal person, parts of a legal entity, maps any kind of situation in the day to day business). There is one point of entry to manage business partners, customers and vendors. In class, FI Vendor will be used for account payables."
