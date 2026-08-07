---
curso: SIOPS
titulo: 2. Teoría Semana 2 -Financial Accounting
slides: 14
fuente: 2. Teoría Semana 2 -Financial Accounting.pdf
---

## Slide 1

Portada del curso. Título "Financial Accounting". Profesor: Carlos Villanueva Qwistgaard. IN3010 - Sistemas de Información para Operaciones. Logo UTEC (decorativo). Sin contenido teórico adicional.

## Slide 2

Slide de agenda con 3 puntos numerados en círculos amarillos:
- 01 INTRODUCTION
- 02 FINANCIAL ACCOUNTING OVERVIEW
- 03 MANAGEMENT ACCOUNTING OVERVIEW

Fondo con foto decorativa de personas en sala de reuniones (decorativa).

## Slide 3

Título: "Introduction". Texto: "The role of accounting processes is to record the financial consequences of the various process steps. In turn, the organization uses this financial information to plan and manage these processes." Imagen decorativa de personas revisando papeles con gráficos sobre una mesa.

## Slide 4

Título: "Financial Accounting Overview". Texto:
- Financials can be subdivided en dos partes: **Financial Accounting (FI)** y **Management Accounting (CO)**.
- Financial Accounting tiene la tarea de cumplir requisitos legales.
- Tareas principales:
  - Post all financial transactions, revenues, and expenses. Keep them unchanged in the system for reporting purposes.
  - Allow the setting up of a profit and loss statement and a balance sheet to fulfill the legal requirements of a country o de un estándar de reporte financiero.

Imagen decorativa de manos señalando gráficos de barras y torta sobre un escritorio.

## Slide 5

Título: "Financial Accounting". Texto: Financial Accounting está sujeta a requisitos legales de un país y, además, a requisitos de estándares de reporte financiero como US GAAP, IFRS y Handelsgesetzbuch (HGB). Los stakeholders de esos reportes están fuera de las compañías (proveedores, bancos, gobierno fiscal, etc.). Imagen decorativa de una persona revisando un documento en un clipboard con lapicero.

## Slide 6

Título: "Financial Accounting". Texto: la tarea central de General Ledger Accounting es proveer una imagen comprehensiva de la contabilidad externa y los registros financieros. El General Ledger (G/L) es el registro completo de todas las transacciones de negocio, gestionado a nivel de company code. Todas las transacciones relevantes hechas en otros componentes (Logistics-LO o Human Resources-HR) se postean en tiempo real a FI mediante determinación automática de cuentas. El objetivo de registrar transacciones es crear un balance sheet y un profit and loss (P&L) statement.

**Diagrama** (lado derecho): esquema de flujo de contabilidad financiera con módulos FI en rombos naranja/gris conectados por líneas punteadas a un libro central "General Ledger Accounting":
- FI-BL "Bank Accounting" (izquierda) → conecta vía línea punteada "Rec. Acc." a Balance Sheet (BS)
- FI-GL "General Ledger" (arriba, libro central abierto con separador de colores) → título "General Ledger Accounting"
- FI-AR "Accounts Receivable" (Customer, izquierda-abajo) → conecta a Balance Sheet vía "Rec. Acc."
- FI-AA "Asset Accounting" (Assets, centro-abajo) → conecta al bloque "Balance Sheet Accounts"
- FI-AP "Accounts Payable" (Vendor, derecha) → conecta a Balance Sheet vía "Rec. Acc."

En el centro un bloque vertical con dos franjas: "Balance Sheet (BS)" (con "Balance Sheet Accounts" a ambos lados) arriba, y "Profit and Loss Statement (P&L)" (con "P&L Accounts") abajo. Los libros (íconos de libro abierto) representan los sub-libros: Bank Accounting, Accounts Receivable, Asset Accounting, Accounts Payable, todos alimentando al General Ledger Accounting central.

## Slide 7

Título: "Financial Accounting". Texto: el General Ledger (G/L) es el núcleo de Financial Accounting (FI). El componente de aplicación FI cumple todos los requisitos internacionales del departamento FI de una organización. FI se enfoca en General Ledger Accounting y el procesamiento de cuentas por cobrar (FI-AR), cuentas por pagar (FI-AP), y Asset Accounting (FI-AA).

**Diagrama** (lado derecho): flujo de datos hacia el Balance Sheet, con cuatro subsistemas a la izquierda (cada uno con ícono e ícono de libro), cada uno con una flecha marcada Σ (suma) hacia el Balance Sheet central:
- Fixed Assets → Σ → columna "ASSETS": Fixed Assets ✓
- Inventory → Σ → columna "ASSETS": Material ✓
- Customers → Σ → columna "ASSETS": Receivables ✓
- Bank accounts → Σ → columna "ASSETS": Bank ✓

El Balance Sheet central tiene dos columnas: ASSETS (Fixed Assets, Material, Receivables, Bank, todos marcados con check verde) y LIABILITIES (Equity capital, Loans, Liabilities, todos marcados con check verde), y abajo una sección "Profit and Loss" con columnas Expenditure/Income.

A la derecha, dos subsistemas alimentan la columna LIABILITIES vía flechas Σ:
- Bank (con ícono de banco) → Σ → Loans
- Vendors → Σ → Liabilities

Arriba a la derecha un ícono de "General Ledger" (libro) representa el libro mayor consolidador.

## Slide 8

Título: "Management Accounting Components". Texto en recuadro: "CO contains all of the functions necessary for controlling cost and revenue effectively. It covers all aspects of management controlling and includes many tools for compiling information for company management." Fondo con foto decorativa de personas sonriendo (semi-transparente, decorativa) sobre franja amarilla lateral.

## Slide 9

Título: "Management Accounting". **Diagrama completo** (sin texto explicativo adicional en esta slide, solo el diagrama grande), estructurado en 4 franjas horizontales punteadas de arriba a abajo:

1. **Profitability Analysis** (CO-PA, rombo naranja/gris) — a la derecha un ícono de tabla/matriz de colores (celda verde resaltada) recibe una flecha verde desde el extremo derecho (desde Revenue Element).

2. **Overhead Cost Controlling** (CO-OM) y **Product Cost Controlling** (CO-PC), lado a lado:
   - Overhead Cost Controlling: "Cost Centers (CO-OM-CCA)" representado como organigrama de bloques naranjas, y "Internal Order (CO-OM-OPA)" como recuadro blanco.
   - Product Cost Controlling: cuatro rombos azules PS, PP, MM, SD conectados a "Project" (recuadro celeste), "Production Order" y "Sales Order" (recuadros blancos).

3. **Cost Element Accounting** (CO-CEL): dos bloques rectangulares — "Cost Element" (naranja) y "Revenue Element" (verde). Del Cost Element salen flechas naranjas/grises hacia Cost Centers e Internal Order; una flecha azul conecta Cost Element hacia Assets/AA abajo. Revenue Element conecta con flecha verde hacia arriba, hasta Profitability Analysis.

4. **Franja inferior FI/PCA**: Vendor/AP (FI, rombo amarillo), P&L Account, Assets/AA, Balance Sheet Acc., PCA (rombo amarillo), Customer/AR (FI). Flechas grises suben desde P&L Account y Balance Sheet Acc. hacia Cost Element.

Debajo del diagrama, franja "Main Business Processes:" con 3 flechas tipo banner amarillo en secuencia: "Purchase to Pay" → "Plan to Product" → "Order to Cash".

Este mismo diagrama se repite (idéntico) en las slides 10-14, cada una con un bloque de texto distinto a la derecha explicando una parte del esquema.

## Slide 10

Título: "Management Accounting". Mismo diagrama de la slide 9 (sin bloque de texto acompañante visible en la imagen entre el diagrama, sino una foto circular decorativa de documentos/calculadora abajo a la derecha). Texto:

"Data that the system creates in other SAP S/4HANA applications can have a direct influence on CO. For example, if you purchase a non-stock item, the system posts an expense to the general ledger (G/L). The system also posts this expense as costs to the **cost center** for which the item was purchased. This cost center can then pass these costs as overhead to a production cost center.

**FI, in the SAP S/4HANA application, is a primary source of data for CO**. In fact, most expense postings in the G/L result in a cost posting in CO. These expense postings to the G/L can be journal postings, vendor invoices, or depreciation postings from Asset Management.

**Management Accounting provides information that management can use to make decisions**. It facilitates the coordination, supervision and optimization of all processes within a company. This involves recording both the consumption of production factors and the services provided by an organization."

Imagen decorativa: foto circular de una mano señalando un documento con calculadora al fondo.

## Slide 11

Título: "Management Accounting". Mismo diagrama que slide 9 a la izquierda. Texto a la derecha: "**Profitability Analysis** analyzes the profit or loss of an organization according to individual market segments. In Profitability Analysis, costs are assigned to the revenues of each market segment. This gives you a basis for calculating prices, targeting customers, determining conditions, and choosing sales channels, for example. **Sales order management is a primary source for revenue postings** from billing documents to revenue postings in CO-PA and PCA. In addition to direct postings from FI, Profitability Analysis (CO-PA) can receive cost assessments from cost centers and ABC processes, settlements of costs from internal orders, and settlements of production variances from cost objects."

## Slide 12

Título: "Management Accounting". Mismo diagrama que slide 9 a la izquierda. Texto a la derecha: "Within the **Overhead Cost Controlling (CO-OM) area**, you can post costs to cost centers, internal orders, and processes from other SAP S/4HANA applications (external costs). Cost centers can then allocate these costs to other cost centers, internal orders, and processes in Activity-Based Costing (ABC). ABC, in turn, can pass costs to cost centers and internal orders. Internal orders can settle costs to cost centers, processes in ABC, and other internal orders."

## Slide 13

Título: "Management Accounting". Mismo diagrama que slide 9 a la izquierda. Texto a la derecha: "You use **Cost Center Accounting** for controlling purposes in your organization. Cost center accounting takes the costs incurred in a company and allocates them to the actual subareas that caused them. Cost centers are separate areas within a controlling area at which costs are incurred. You can create cost centers according to various criteria including functional considerations, allocation criteria, activities provided, or according to their physical location and/or management area."

## Slide 14

Título: "Management Accounting". Mismo diagrama que slide 9 a la izquierda. Texto a la derecha: "An **activity type** defines the type of activity that can be provided by a cost center. Activity outputs supplied by one cost center (the sending cost center) to other cost centers, orders, or processes, represent the utilization of resources for this sending cost center. You valuate activities using a price calculated on the basis of certain business or management information. **Internal orders** are used to plan, collect, and analyze the costs arising from internal activities. SAP Human Capital Management (HCM) can generate cost postings in CO. SAP HCM allows you to allocate labor costs to various controlling objects. In addition, you can transfer and use planned personnel costs for planning in CO."
