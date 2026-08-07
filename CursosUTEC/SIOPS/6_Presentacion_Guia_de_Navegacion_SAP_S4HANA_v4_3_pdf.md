---
curso: SIOPS
titulo: 6. Presentación Guia de Navegacion SAP S4HANA v4.3
slides: 14
fuente: 6. Presentación Guia de Navegacion SAP S4HANA v4.3.pdf
---

## Slide 1

**Navigation SAP S4/HANA**
SAP University Competence Center Magdeburg — August 2025

Portada decorativa: foto de estudiantes conversando al aire libre con mochilas y cuadernos, franja superior amarilla, logos "SAP University Alliances" y "SAP UCC Magdeburg" (decorativa, sin contenido técnico).

## Slide 2

**Teaching material - Information**

Icono decorativo de documentos apilados junto al bloque "Teaching material - Version":
- 4.3 (August 2025)
- Software used:
  - S/4HANA 2023
  - Fiori 3.0
- Model: Global Bike
- Prerequisites: No Prerequisites needed

A la derecha, logo del modelo de datos usado en el curso: banner verde "Global Bike" con icono de bicicleta y ciclista en blanco.

## Slide 3

**Module Information**

Dos bloques con icono e ícono correspondiente:
- Icono de lápiz (autores) → **Authors**: Yeganeh Rashed
- Icono de personas (audiencia) → **Target Audience**: Beginner

## Slide 4

**Module Information**

Icono de diana/objetivo → **Learning Objectives**
Texto: "You are able to"
- to build up an understanding of SAP Fiori Launchpad

## Slide 5

**Log on to an SAP system**

Slide de transición/separador de sección, solo título, sin contenido adicional.

## Slide 6

**Fiori Launchpad: An Overview**

Texto (bullets):
- SAP Fiori Launchpad:
  - The **modern** user interface
  - A standardized, role-based entry point for applications
  - It is based on tiles that represent apps
  - It is designed for an intuitive, user friendly experience (UX)
  - The standard user interface in new SAP systems, like **SAP S/4HANA**

Captura de pantalla de la UI de SAP Fiori Launchpad (español "Idioma" en login previo, aquí interfaz en inglés) anotada con recuadros de color que señalan cada nivel de la jerarquía de navegación:
- Barra superior con logo SAP y menú "Home ▾"; recuadro azul rotulado **"Spaces"** rodea la fila de pestañas: My Home | Controlling ▾ | Customizing | Enterprise Asset Management | Financial Accounting ▾
- Bajo "Financial Accounting" se despliega un menú con recuadro verde rotulado **"Pages"**: Accounts Payable, Accounts Receivable, Investment and Asset Management
- Debajo, el área de contenido muestra la página "Accounts Payable" con la sección "Head of Accounting" y 5 tiles: Manage G/L Account Master Data, Post General Journal Entries, Manage Journal Entries (New Version), Balance Sheet/Income Statement, Display Supplier Balances
- El tile "Display Supplier Balances" está resaltado con recuadro naranja rotulado **"Tiles"**
- Más abajo, sección "AP Accountant" con recuadro morado rotulado **"Sections"**, conteniendo 5 tiles: Manage Business Partner Master Data, Create Supplier Invoice, Display G/L Account Balances, Display Supplier Balances, Post Outgoing Payments

## Slide 7

**Fiori Launchpad: An overview**

Texto (bullets):
- The Fiori Launchpad includes a section called "My Home".
- This page is usually empty when you log in for the first time.
- Users can customize it to suit their needs.
- Frequently used tiles or applications can be added.
- This creates a personalized work interface tailored to your tasks.

Captura de pantalla: barra superior SAP con pestañas My Home (activa), Financial Accounting ▾, Controlling ▾, Human Capital Management ▾. Área de contenido vacía con ilustración decorativa de una carpa de camping y una gaviota, texto "Nothing here yet?" y subtítulo "You can add your preferred apps to this page.", con botón "Edit Page".

## Slide 8

**Structure of the SAP Fiori Launchpad**

Texto (bullets) — definición de **Space**:
- Represents the highest organizational level within the user interface structure
- Consolidates thematically related applications for a specific user role or business area
- Each space is designed for a defined work context

Captura de pantalla parcial: barra de navegación SAP con pestañas My Home, Controlling ▾, Customizing, Enterprise Asset Management, Financial Accounting ▾ (esta última subrayada en azul, indicando el espacio seleccionado).

## Slide 9

**Structure of the SAP Fiori Launchpad**

Texto (bullets) — definición de **Page**:
- Each space comprises at least one page
- Serves as the primary workspace where applications and information are presented
- Facilitates the structured presentation of a space's content

Captura de pantalla: barra superior SAP (My Home, Controlling ▾, Customizing, Enterprise Asset Management, Financial Accounting ▾) con el menú desplegado de "Financial Accounting" mostrando las páginas: Accounts Payable, Accounts Receivable, Investment and Asset Management. Recuadro verde rotula el menú desplegable y recuadro negro rotula la etiqueta **"Page"** junto al menú desplegable. Debajo se ve el encabezado "Accounts Payable / Head of Accounting" de la página activa.

## Slide 10

**Structure of the SAP Fiori Launchpad**

Texto (bullets) — definición de **Section**:
- Serves to further subdivide pages
- Groups tiles according to specific tasks or processes
- Enables improved clarity and organization

Captura de pantalla: página "Accounts Payable" con sección "Head of Accounting" resaltada con recuadro morado rotulado **"Section"**, conteniendo 5 tiles: Manage G/L Account Master Data, Post General Journal Entries, Manage Journal Entries (New Version), Balance Sheet/Income Statement, Display Supplier Balances.

## Slide 11

**Structure of the SAP Fiori Launchpad**

Texto (bullets) — definición de **Tiles**:
- The smallest interactive elements on a page
- Provide direct entry points to applications

Captura de pantalla: página "Accounts Payable / Head of Accounting" con 5 tiles visibles; el tile "Display Supplier Balances" está resaltado con recuadro naranja rotulado **"Tile"**.

## Slide 12

**Navigation Flow Summary**

Texto (bullets) resumiendo el flujo de navegación:
- **Space:** Selects the overarching area of responsibility
- **Page:** Directs the user to the main workspace
- **Section:** Groups tiles according to specific tasks
- **Tile:** Launches the desired application

Diagrama jerárquico (texto con sangría y flechas "↳"), con ejemplos concretos:
```
Spaces (e.g. Financial Accounting)
 ↳ Pages (e.g Accounts Payable)
  ↳ Sections (e.g. AP Accountant)
   ↳ Tiles (e.g. Display Supplier Balances)
```

Captura de pantalla compuesta a la derecha, integrando todas las anotaciones anteriores en una sola imagen: recuadro azul "Spaces" en la barra de pestañas superior; recuadro verde "Pages" en el menú desplegable de Financial Accounting (Accounts Payable, Accounts Receivable, Investment and Asset Management); recuadro naranja "Tiles" alrededor del tile "Manage G/L Account Master Data" en la sección "Head of Accounting" (con 5 tiles: Manage G/L Account Master Data, Post General Journal Entries, Manage Journal Entries New Version, Balance Sheet/Income Statement, Display Supplier Balances); recuadro morado "Sections" alrededor de la sección "AP Accountant" (con 5 tiles: Manage Business Partner Master Data, Create Supplier Invoice, Display G/L Account Balances, Display Supplier Balances, Post Outgoing Payments).

## Slide 13

**Roles (Business Roles)**

Texto (bullets):
- Roles (Business Roles)
  - form the foundation of the authorization structure.
  - define which content a user is allowed to see and use.
  - Without an assigned role, the user cannot see any areas, pages or tiles.

Sin elemento visual adicional (solo texto).

## Slide 14

**Roles (Business Roles)**

Comparación lado a lado mediante dos capturas de pantalla de la Fiori Launchpad, ilustrando el efecto de tener uno o varios roles asignados:

- **Izquierda — "With one role":** barra superior con solo la pestaña "Financial Accounting ▾" visible (recuadro azul) además de "My Home". Página activa "Accounts Payable / Head of Accounting" con 5 tiles: Manage G/L Account Master Data, Post General Journal Entries, Manage Journal Entries (New Version), Balance Sheet/Income Statement, Display Supplier Balances.

- **Derecha — "With several roles":** barra superior con tres pestañas visibles (recuadro azul): Financial Accounting ▾, Controlling ▾ (activa/resaltada), Human Capital Management ▾, además de "My Home". Página activa "Cost Center Controlling / Controller" con 6 tiles: Manage Cost Centers, Create Cost Centers, Manage Statistical Key Figures, Manage Activity Types, Manage G/L Account Master Data, Manage Cost Center Groups, Display Cost Element Groups.

El contraste muestra que con más roles asignados el usuario ve más spaces (pestañas) disponibles en la barra de navegación.
