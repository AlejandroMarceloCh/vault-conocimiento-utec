---
curso: SIOPS
titulo: Procesos de Gestión de Stocks y Almacenes - 0. Introduccion
slides: 11
fuente: Procesos de Gestión de Stocks y Almacenes - 0. Introduccion.pdf
---

## Slide 1

**Gestión de Stocks y Almacenes**
Prof. Carlos Villanueva Q.

Diagrama isométrico (ilustración estilo almacén 3D) que muestra el flujo físico de un almacén con tres zonas etiquetadas y conectadas por una flecha de línea continua que serpentea de izquierda a derecha:
1. **Recepción** — edificio con muelles de carga y un camión descargando.
2. **Almacenaje** — estanterías con racks apilados de cajas/pallets.
3. **Expedición** — zona de despacho con pallets, montacargas y un camión de salida.

La flecha guía visualmente la secuencia Recepción → Almacenaje → Expedición. Logo UTEC decorativo en la esquina superior derecha (ignorado).

## Slide 2

**Objetivos del Módulo** (lista numerada, sin elementos gráficos adicionales)
1. Revisar los movimientos de materiales relacionados con la Gestión de Stocks (IM)
2. Describir los datos maestros, organizativos y procesos asociados a la Gestión de Almacenes (WM)
3. Revisar la interrelación de la Gestión de Almacenes con los procesos empresariales estudiados anteriormente (MM, SD, PP)
4. Utilizar eficazmente SAP para realizar las principales operaciones del proceso de gestión de almacenes

## Slide 3

**Objetivos de la sesión** (lista con viñetas, sin elementos gráficos adicionales)
- Introducir conceptos relacionados a la gestión de almacenes y su relación con la gestión de stocks y otros procesos empresariales.
- Revisar los movimientos asociados con la gestión de stocks.
- Describir los niveles organizativos de la gestión de almacenes.
- Desarrollar en SAP el Caso WM – I: Proceso de Recepción y Almacenaje

## Slide 4

**Caso Steelcase Inc.**

Fotografía de un almacén industrial real (racks de pallets metálicos color azul/naranja, cajas de cartón apiladas en varios niveles, piso de concreto, pasillo central) — imagen decorativa/ilustrativa del tipo de almacén que se describe, sin datos adicionales que extraer.

## Slide 5

**Caso Steelcase Inc.**
- Fabricación de muebles de oficina (escritorios, sillas, armarios)
- Facturación 2010: +$2,3 mil millones
- 650 distribuidores independientes
- Manufactura en USA, Europa y Asia
- En USA:
  - 10 Fábricas
  - 6 CDR
  - Cada Fábrica tiene almacenes pequeños y temporales de:
    - Materia Prima
    - Productos Terminados
  - Cada CDR gestiona:
    - El proceso de gestión de pedidos, planificación, asignación y enrutamiento de unidades de transporte
    - Consolidación, preparación y carga de despachos.
    - +100 entregas diarias a clientes, simultáneamente a recepciones desde Fábricas

Solo texto, sin diagrama en esta slide.

## Slide 6

**Caso Steelcase Inc.**

Diagrama de flujo de proceso con dos macro-bloques (contenedores rectangulares con título en negrita) conectados por flechas de camión etiquetadas "Traslado" y "Entregas":

**Bloque "Centro de Manufactura"** (columna izquierda), flujo vertical interno:
- Caja celeste "Proceso de Aprovisionamiento" → (ícono camión) → **Almacén de Materia Prima** (caja azul oscuro redondeada)
- ↓ **Fabricación** (caja gris)
- ↓ **Almacén de P. Terminados** (caja azul oscuro redondeada)

Del "Almacén de P. Terminados" del Centro de Manufactura sale una flecha horizontal etiquetada **"Traslado"** (con ícono de camión) hacia el bloque de la derecha.

**Bloque "Centro de Distribución"** (columna derecha), flujo vertical interno:
- **Recepción** (caja gris) ← recibe el traslado
- ↓ **Almacén de P. Terminados** (caja azul oscuro redondeada)
- ↓ **Expedición** (caja gris) → (ícono camión, etiqueta "Entregas") → caja celeste **"Proceso de Gestión de Pedidos"**

El diagrama ilustra el flujo completo: aprovisionamiento → almacén MP → fabricación → almacén PT (fábrica) → traslado → recepción (CDR) → almacén PT (CDR) → expedición → entregas → gestión de pedidos.

## Slide 7

**Caso Steelcase Inc.**
- Objetivo Gestión de Stocks y Almacenes:
  - **Optimizar el espacio de almacenamiento.** (en negrita)
  - **Ejecutar eficientemente el proceso de gestión de pedidos** (en negrita) balanceando el flujo de mercancías a sus centros de manufactura con las entregas de salida a sus clientes desde los CDRs.
- Monitorear, evaluar y gestionar un flujo eficiente de productos dentro y fuera de sus almacenes.

Solo texto, sin diagrama en esta slide.

## Slide 8

**Casos Warehouse Management**

Lista de casos con enlaces a video (hipervínculos subrayados en color azul/teal):
- CD Alicorp
  - https://www.youtube.com/watch?v=NBfNq6giZaU
- CD Molitalia
  - https://www.youtube.com/watch?v=WKXVnp_AMG4
- WMS
  - https://www.youtube.com/watch?v=8t7osU8DdxQ&list=PLJmwgkCSM4_0VIvyTUnJXDusX-lTMXo3i
- Voice Picking
  - https://www.youtube.com/watch?v=ck5UciRpFw8

## Slide 9

**Global Bike Inc. – Centros y Almacenes**

Diagrama jerárquico organizacional en 4 niveles (filas horizontales etiquetadas a la izquierda: Mandante, Sociedad, Centro, Almacén), estructura tipo árbol de datos maestros SAP:

- **Mandante**: "Empresa global GBI" (nodo raíz único)
  - **Sociedad** (2 nodos, ambos hijos del mandante):
    - **US00 — Empresa EE.UU.**
    - **DE00 — Empresa Alemana**
  - **Centro** (5 nodos):
    - Bajo US00: **DL00 Centro Dallas**, **SD00 Centro San Diego**, **MI00 Centro Miami**
    - Bajo DE00: **HI00 Centro Heidelberg**, **HB00 Centro Hamburgo**
  - **Almacén** (nodos hoja bajo cada centro, códigos de 4 letras):
    - DL00 → RM00, SF00, FG00, MI00
    - SD00 → FG00, TG00, MI00
    - MI00 (centro) → FG00, TG00, MI00
    - HI00 → RM00, SF00, FG00, MI00
    - HB00 → FG00, TG00, MI00

El diagrama muestra la jerarquía organizativa completa de SAP: Mandante → Sociedad → Centro → Almacén, con líneas de conexión verticales/horizontales tipo organigrama.

## Slide 10

**CD San Diego GBI**

Plano/layout esquemático (vista de planta, estilo diagrama técnico en tonos azules) de un centro de distribución dividido en zonas rectangulares:

- **Tipo de almacén 001 — Almacén de estanterías**: zona superior izquierda con 5 filas de estanterías rectangulares horizontales y un pasillo vertical a la izquierda.
- **Tipo de almacén 002 — Almacén de pallets**: zona inferior izquierda con una cuadrícula de casilleros pequeños (aprox. 4 filas x 10 columnas de espacios de pallet).
- **Estacionamiento con carretilla elevadora / área mantenimiento**: recuadro punteado central superior.
- **Oficina**: recuadro superior derecho.
- **Tipo de almacén 003 — Recepción**: recuadro medio derecho, con flecha entrante desde la "Puerta de servicio".
- **Tipo de almacén 004 — Expedición**: recuadro inferior derecho, con flecha entrante desde la "Puerta de servicio".
- **Puerta de servicio**: indicada verticalmente al extremo derecho del plano, con dos flechas apuntando hacia Recepción y Expedición.

El layout ilustra cómo un centro físico se subdivide en "tipos de almacén" (concepto SAP WM) según función: almacenamiento en estanterías, almacenamiento de pallets, recepción y expedición.

## Slide 11

**Casos SAP**
- Semana 11
  - WM I - Recepción y Almacenaje de Mercaderia Comprada (Transfer Order)
  - WM II – Traslados entre Centros (Stock Transport Order)
- Semana 12
  - WM III - Atención de Pedidos de Venta (Fullfilment)
  - WM IV – Toma de inventario físico

Diagrama de flujo (esquina inferior derecha) con cajas celestes conectadas por flechas grises gruesas, representando el flujo físico dentro de un almacén:
- **Muelles de carga y descarga** (caja vertical, extremo izquierdo) → **Recepción**
- **Recepción** → **Almacén general**
- **Almacén general** → **Zona de picking**
- **Zona de picking** → **Consolidación**
- **Consolidación** → **Expedición**
- **Expedición** → **Muelles de carga y descarga** (cierra el ciclo)

El diagrama forma un circuito rectangular: entrada por muelles → recepción → almacén general → zona de picking → consolidación → expedición → salida por muelles, ilustrando el flujo operativo interno de un almacén tipo.
