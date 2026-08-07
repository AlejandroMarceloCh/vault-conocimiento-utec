---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Slides_FI_en_v4.3
slides: 29
fuente: Intro_S4HANA_Using_Global_Bike_Slides_FI_en_v4.3.pdf
---

## Slide 1

Portada decorativa: título "Financial Accounting (FI)", subtítulo "Curriculum: Introduction to S/4HANA using Global Bike". Foto de fondo de un joven con sweater verde sentado en un escritorio con monitor, teclado, audífonos rojos y una botella de agua, tomando notas (foto decorativa, sin contenido informativo). Logos SAP University Alliances y SAP UCC Magdeburg (decorativos).

## Slide 2

Título: "Teaching material - Information".

Ícono decorativo (documentos con lápiz) junto al bloque "Teaching material - Version".

- Versión: 4.3 (July 2025)
- Software used:
  - S/4HANA 2023
  - Fiori 3.0
- Model: Global Bike
- Prerequisites: No Prerequisites needed

A la derecha, logo de la empresa ficticia "Global Bike" (rectángulo verde con silueta de ciclista y el texto estilizado "Global Bike").

## Slide 3

Título: "Module Information".

Dos bloques con íconos decorativos (lápiz para "Authors", personas para "Target Audience"):

- Authors:
  - Bret Wagner
  - Stefan Weidner
  - Babett Ruß
- Target Audience: Beginner

## Slide 4

Título: "Module Information". Ícono decorativo de diana (target).

Learning Objectives — "You are able to":
- define the central organizational structures of the FI module.
- summarize the master data which is most important for the FI module.
- explain a standard financial accounting process.
- outline the basic functionalities of FI reporting.
- recognize some of integration points to other SAP modules.

## Slide 5

Título: "Agenda". Lista de 4 puntos, con "FI Organizational Structure" resaltado en negro (ítem activo/actual) y los otros 3 en gris claro (aún no tratados):
1. **FI Organizational Structure** (activo)
2. FI Master Data
3. FI Processes
4. FI Reporting

## Slide 6

Título: "Goal of Financial Accounting (FI)". Solo texto:

- Financial Accounting is designed to collect the transactional data that provides a foundation for preparing the standard portfolio of reports.
- In general, these reports are primarily, but not exclusively, directed at external parties.
- Standard reports include:
  - Balance Sheet
  - Income Statement
  - Statement of Cash Flows

## Slide 7

Título: "Target Groups". Tabla de dos columnas (Internal vs External):

| Internal | External |
|---|---|
| Executives | Legal Authorities |
| Senior Management | Banks |
| Administrative Staff | Auditors |
| Employees | Shareholders |
| | Insurance |
| | Taxing Authorities |
| | Media |
| | Financial Analysts |

## Slide 8

Título: "FI Organizational Structure". Solo texto:

- Represents the legal and/or organizational view of a company
- Forms a framework that supports a company's financial decisions using the methods desired by management
- Allows the accurate and organized collection of business information
- Supports the development and presentation of relevant information to enable and support business decisions

## Slide 9

Título: "FI Organizational Structure".

- **Client**: An independent environment in the system
- **Company Code**:
  - Represents an independent legal accounting unit
  - Balanced set of books, as required by law, are prepared at this level.
  - A client may have more than one company code: United States, Germany, United Kingdom, Australia, …

Diagrama a la derecha: una balanza (báscula de justicia) con dos platillos, uno rotulado "Assets" y el otro "Liabilities & Owners Equity", ilustrando la ecuación contable balanceada.

## Slide 10

Título: "FI Organizational Structure". Solo texto (3 conceptos):

- **Chart of Accounts**:
  - A classification scheme consisting of a group of general ledger (G/L) accounts
  - Provides a framework for the recording of values to ensure an orderly rendering of accounting data
  - The G/L accounts it contains are used by one or more company codes.
- **Credit Control Area**:
  - An organizational entity which grants and monitors a credit limit for customers.
  - It can include one or more company codes
- **Business Area**:
  - An organizational unit that represents a separate area of operations or responsibilities within an organization and to which value changes recorded in Financial Accounting can be allocated
  - Financial statements can be created for business areas, and these statements can be used for various internal reporting purposes.

## Slide 11

Título: "Global Bike Structure for Financial Accounting". Diagrama jerárquico de cajas azules conectadas por líneas, con etiquetas de nivel a la derecha:

```
                    [Global Bike]                       → Client
                    /          \
     [Global Bike Inc.]    [Global Bike Germany GmbH]    → Company Code
              \                  /
             [Global Bike Chart of Accounts]              → Chart of Accounts
                    |
                 [Bikes]                                  → Business Area

           [Global Credit Control]                        → Credit Control Area
```

Muestra cómo el cliente "Global Bike" se divide en dos Company Codes (Global Bike Inc. en EEUU y Global Bike Germany GmbH), ambos comparten el mismo Chart of Accounts ("Global Bike Chart of Accounts") y la misma Business Area ("Bikes"), y comparten el Credit Control Area ("Global Credit Control").

## Slide 12

Título: "Global Bike Enterprise Structure in SAP ERP (Accounting)". Diagrama 3D en perspectiva (estilo "capas apiladas" isométricas) que representa la jerarquía organizacional completa de SAP, de abajo hacia arriba:

- Capa base: "Client Global Bike"
- "Operating Concern (global) GL00"
- "CA North Am. NA00", "CA Europe EU00", "CA Asia AS00" (Controlling Areas)
- "Credit Control Area (global) GL00"
- "Chart of Accounts (global) GL00"
- Barras verticales verdes/moradas/grises representando Company Codes: "CC US00", "CC CA00", "CC DE00", "CC GB00", "CC AU00", "CC JP00"
- Barra superior verde horizontal: "Business Area – Bikes BI00" (cruza todos los Company Codes)

Etiquetas laterales derechas: "Company Code", "Controlling Area (see Controlling unit)", "Operating Concern (see Controlling unit)". Muestra que un único Chart of Accounts, Credit Control Area y Business Area son compartidos globalmente por 6 Company Codes regionales (US, Canadá, Alemania, Reino Unido, Australia, Japón), agrupados en 3 Controlling Areas (Norteamérica, Europa, Asia).

## Slide 13

Título: "Agenda". Mismo listado de 4 puntos que en slide 5, ahora con "FI Master Data" resaltado en negro (activo) y el resto en gris:
1. FI Organizational Structure
2. **FI Master Data** (activo)
3. FI Processes
4. FI Reporting

## Slide 14

Título: "FI Master Data". Solo texto:

- **General Ledger (G/L) Accounts**:
  - The unique combination of Company Code and Chart of Account creates a data storage area called a General Ledger.
  - The General Ledger contains a listing of the transactions effecting each account in the Chart of Accounts and the respective account balance.
  - It is utilized in the preparation of financial accounting statements.
- **Customer and Vendor Master Data**:
  - Customer and vendor account balances are maintained in FI through fully integrated accounts receivable and accounts payable sub-ledgers.
  - Financial postings for customers and vendors are made directly to their respective individual accounts and accompanied by a concurrent automatic posting to the General Ledger.

## Slide 15

Título: "Customer Accounts".

- **Accounts Receivable Sub-Ledger (FI-AR)**:
  - Information with respect to customers who purchase the enterprise's goods and services such as sales and payments made
  - Substantive and important integration between Sales and Distribution (SD) and Financial Accounting (FI)
  - Billings in SD generate FI journal entries for sales activity

Diagrama: 4 cajas naranjas de clientes individuales con sus saldos (Customer 189: 100, Customer 142: 300, Customer 135: 400, Customer 123: 150) cada una con flechas azules que convergen hacia una caja "Accounts Receivable (General Ledger)" mostrando el total acumulado 950 (= 100+300+400+150). Ilustra cómo los sub-ledgers individuales de clientes se consolidan en la cuenta de mayor general.

## Slide 16

Título: "Vendor Accounts".

- **Accounts Payable Subledger (FI-AP)**:
  - Information with respect to Vendors from whom the enterprise purchases goods and services such as purchases and payments made
  - Substantive and important integration between Materials Management (MM) and Financial Accounting (FI)
  - Purchase and goods receipt activities in MM generate FI journal entries

Diagrama análogo al de la slide 15: 4 cajas naranjas de proveedores individuales (Vendor 100234: 200, Vendor 100435: 250, Vendor 100621: 100, Vendor 100846: 300) con flechas azules que convergen hacia "Accounts Payable (General Ledger)" con total 850 (= 200+250+100+300).

## Slide 17

Título: "Agenda". Mismo listado de 4 puntos, ahora con "FI Processes" resaltado en negro (activo):
1. FI Organizational Structure
2. FI Master Data
3. **FI Processes** (activo)
4. FI Reporting

## Slide 18

Título: "FI Processes" — "Posting a G/L Entry".

Dos capturas de pantalla de la interfaz Fiori de SAP:

1. Captura principal "Post General Journal Entries": formulario con encabezado (Header/Attachments/Notes/Balances tabs) con campos:
   - Journal Entry Date: 03/28/2025, Posting Date: 03/28/2025, Period: 3, Journal Entry Type: SA
   - Company Code: US00 (Global Bike Inc.), Transaction Currency: USD (United States Dollar)
   - Header Text: Transfer of Funds
   - Total Balance: 0
   - Tabla de líneas de asiento:

   | # | Company Code | G/L Account | Debit | Credit |
   |---|---|---|---|---|
   | 1 | US00 | 1801075 (...) | 5,000.00 USD | 0.00 USD |
   | 2 | US00 | 1800000 (...) | 0.00 USD | 5,000.00 USD |

2. Captura secundaria pequeña "Manage Journal Entries" mostrando "Journal Entry (100000002) - Entry View", indicando el documento generado tras contabilizar.

## Slide 19

Título: "Agenda". Mismo listado de 4 puntos, ahora con "FI Reporting" resaltado en negro (activo):
1. FI Organizational Structure
2. FI Master Data
3. FI Processes
4. **FI Reporting** (activo)

## Slide 20

Título: "FI Reporting" — "G/L Account Summary".

Captura de pantalla de la app Fiori "Display G/L Account Balances", vista "Standard", con filtros:
- Ledger: 0L (Leading Ledger), Fiscal Year of Ledger: 2025
- Company Code: US00 (Global Bi...), Currency: USD (Company Code...)
- G/L Account: 6311075 (Re...), Controlling Area: NA00 (Global Bi...)
- From/To Period: vacíos, botón "Go", "Adapt Filters (6)"

Tabla de resultados por periodo (Period | Debit Amount in Compa... | Credit Amount in Company C... | Balance Amount in Company C... | Ending Balance Amount in Company Cod...):

| Period | Debit | Credit | Balance | Ending Balance |
|---|---|---|---|---|
| Opening Balance | | | | 0.00 |
| 001/2025 | | | | 0.00 |
| 002/2025 | | | | 0.00 |
| 003/2025 | 1,500.00 | 0.00 | 1,500.00 | 1,500.00 |
| 004/2025 | | | | 1,500.00 |
| 005/2025 | | | | 1,500.00 |
| 006/2025 | | | | 1,500.00 |
| 007/2025 | | | | 1,500.00 |
| 008/2025 | | | | 1,500.00 |
| 009/2025 | | | | 1,500.00 |
| 010/2025 | | | | 1,500.00 |
| 011/2025 | | | | 1,500.00 |
| 012/2025 | | | | 1,500.00 |
| 013/2025 | | | | 1,500.00 |
| Totals | 1,500.00 | 0.00 | 1,500.00 | 1,500.00 |

## Slide 21

Título: "FI Reporting" — "Balance Sheet". Solo texto:

- Presentation of an organization's Assets, Liabilities, and Equity at a point in time
- Assets: What the company owns
- Liabilities: What the company owes
- Equity: The difference between Assets and Liabilities
- Assets = Liabilities + Equity

## Slide 22

Título: "FI Reporting" — "Balance Sheet Example". Ejemplo numérico de balance general en dos columnas:

**Assets**
| Cuenta | Monto |
|---|---|
| Cash | 1,000 |
| Accounts Receivable | 3,000 |
| Equipment | 500 |
| **Total Assets** | **4,500** |

**Liabilities**
| Cuenta | Monto |
|---|---|
| Accounts Payable | 1,750 |
| Taxes Payable | 500 |
| **Total Liabilities** | **2,250** |

**Equity**
| Cuenta | Monto |
|---|---|
| Common Stock | 2,000 |
| Retained Earnings | 250 |
| **Total Equity** | **2,250** |

**Total Liabilities and Equity: 4,500** (verifica Assets = Liabilities + Equity: 4,500 = 2,250 + 2,250)

## Slide 23

Título: "FI Reporting" — "Income Statement". Solo texto:

- Presentation of an organization's revenues and expenses for a given period of time (e.g. monthly, quarterly, or yearly)
- Revenues, in a simple sense, are inflows of cash as a result of selling activities or the disposal of company assets.
- Expenses, in a simple sense, are outflows of cash or the creation of liabilities to support company operations.
- Revenues - Expenses = Net Income

## Slide 24

Título: "FI Reporting" — "Income Statement Example". Ejemplo numérico:

| Concepto | Monto |
|---|---|
| **Revenue** | |
| Sales | 11,000 |
| Deductions | 750 |
| **Total Revenue** | **10,250** |
| **Operating Expenses** | |
| Cost of Goods Sold | 4,500 |
| Operating Expenses | 3,750 |
| **Total Expenses** | **8,250** |
| **Net Income Before Taxes** | **2,000** |
| Taxes | 750 |
| **Net Income** | **1,250** |

Cálculo: Total Revenue (10,250) − Total Expenses (8,250) = Net Income Before Taxes (2,000); 2,000 − Taxes (750) = Net Income (1,250).

## Slide 25

Título: "FI Reporting" — "Statement of Cash Flows".

- Considers the associated changes, both inflows and outflows, that have occurred in cash – arguably the most important of all assets – over a given period of time (e.g. monthly, quarterly, or annually)

Imagen decorativa tipo clipart de un fajo de billetes verdes y una pila de monedas.

## Slide 26

Título: "Accountants and Audit Trails". Solo texto:

- Audit trails allow an auditor to begin with an account balance on a financial statement and trace through the accounting records to the transactions that support the account balance.
- Audit trails enable an auditor to trace individual transactions to the effected account balance(s) on a financial statement.

## Slide 27

Título: "SAP Document Principle". Solo texto:

- Each business transaction impacting FI writes data to the SAP database creating a uniquely numbered electronic document.
- The document number can be used to recall the transaction at a later date.
- It contains, for example, such critical and necessary information as:
  - Responsible person
  - Date and time of the transaction
  - Commercial content
- Once written to the SAP database, a financial document (one impacting the financial position of the company) can not be deleted from the database.
- It can be changed to some degree.
- The SAP document principle provides a solid and important framework for a strong internal control system – a requirement of law for companies that operate in most countries in the world.

## Slide 28

Título: "SAP Document Principle" (continuación). Tres capturas de pantalla del sistema SAP GUI clásico (no Fiori) ilustrando el principio de documento:

1. **"Document List"** (arriba izquierda): tabla con columnas CoCd, DocumentNo, Year, Type, Doc.Date, Posting Date. Fila: US00 | 100000020 | 2018 | SA | 08.05.2018 | 08.05.2018.

2. **"Document Header: US00 Company Code"** (derecha): formulario de detalle del documento contable con campos:
   - Document type: SA (Account Document)
   - Doc. Header Text: Transfer of Funds
   - Reference: 000
   - Currency: USD, Document Date: 08.05.2018, Posting Date: 08.05.2018, Posting period: 05/2018
   - Ref. Transactn: BKPF (Accounting document)
   - Reference Key: 0100000020US002018
   - Created By: LEARN-711, Log System: R65CLNT103
   - Entry Date: 08.05.2018, Time of Entry: 13:56:12
   - Parked On / Parked By / Time of Parking: vacíos
   - TCode: FV50
   - Changed On / Last Update: vacíos
   - Botones: Continue/Confirm, Cancel

3. **"Document Changes: Overview"** (abajo izquierda): para Document 0100000016, Company Code US00, Year 2010. Tabla de cambios (Date | Field | New | Old):
   | Date | Field | New | Old |
   |---|---|---|---|
   | 05/22/10 | Changed on | 05/22/2010 | 00/00/0000 |
   | 05/22/10 | Document Header Text | Test for Change | Transfer of Funds |

   Ilustra que el documento puede modificarse (ej. el texto de cabecera) pero queda un registro/histórico del cambio (fecha, campo, valor nuevo vs. valor anterior) — soporta la afirmación de que "no se puede borrar pero sí cambiar en cierto grado".

## Slide 29

Título: "SAP FI Module". Solo texto:

- Fully integrated with other SAP modules including, but not limited to:
  - Sales and Distribution (SD)
  - Materials Management (MM)
  - Production Planning and Execution (PP)
  - Managerial Accounting (CO)
