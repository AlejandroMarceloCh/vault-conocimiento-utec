---
curso: SIOPS
titulo: Procesos de Gestión de Stocks y Almacenes - 3. Datos Maestros en la Gestión de Almacenes
slides: 10
fuente: Procesos de Gestión de Stocks y Almacenes - 3. Datos Maestros en la Gestión de Almacenes.pdf
---

## Slide 1

Portada del capítulo: "Proceso de Gestión de Stocks y Almacenes". Autor: Prof. Carlos Villanueva Q. Franja decorativa naranja/rosa/gris (decorativa, sin contenido).

## Slide 2

**Objetivos de aprendizaje**

1. Analizar los datos maestros asociados a la gestión de almacenes.

Slide de solo texto, un único objetivo listado.

## Slide 3

**Datos maestros en la gestión de almacenes**

- Maestro de material y ubicación son los datos maestros claves

Slide de solo texto (bullet único).

## Slide 4

**Maestro de materiales**

- El maestro de materiales fue estudiado en el contexto de otros procesos
- El material ubicado en un almacén asociado a WM requiere de datos adicionales en el maestro de materiales.
- Niveles organizativos
  - Número de almacén
  - Centro
  - Tipo de almacén

Slide de solo texto, con lista anidada de niveles organizativos.

## Slide 5

**Maestro de materiales**

- La vista de gestión de almacenes:
  - Datos básicos
  - Datos utilizados en la definición de las estrategias de almacenamiento y picking the stock
  - Datos relativos a las ubicaciones donde se almacenarán los materiales
- Los datos básicos son relevantes para todos los procesos
- Algunos datos se deben redefinir para la gestión de almacenes
- Datos relacionados con las estrategias de almacenamiento y picking
- Datos relacionados con las ubicaciones

Slide de solo texto, jerarquía de bullets sobre los tres tipos de datos de la vista WM del maestro de materiales.

## Slide 6

**Demo 7-4 Revisión de la vista WM del maestro de materiales**

- Revisión de la vista WM del maestro de materiales

Slide título de demo, sin captura de pantalla incluida (solo el enunciado de la demo, contenido mínimo de texto).

## Slide 7

**Ubicaciones**

- Ubicaciones son las unidades de espacio más pequeñas en un almacén
- Puede variar en tamaño
- Puede almacenar diferentes mercancías (cuantos)

Slide de solo texto.

## Slide 8

**Fig. 7-15: Direccionamiento de Ubicaciones**

Diagrama ilustrativo (dibujo técnico en gris) de un almacén con estanterías vistas en perspectiva, mostrando la jerarquía física de una ubicación de almacén. Tres etiquetas con flechas señalan distintos niveles de la estructura:

- **"Filas (pasillos)"**: flecha que apunta a los pasillos/corredores entre las estanterías (el espacio de circulación entre las filas de estantes).
- **"Estantes"**: flechas que apuntan a las estructuras verticales completas (los racks/módulos de estantería que forman cada fila), señalando las bases/columnas de las estanterías al fondo.
- **"Repisas"**: múltiples flechas que apuntan a los niveles horizontales individuales dentro de cada estante (los "shelves" o repisas donde se colocan las carpetas/cajas), etiqueta ubicada a la izquierda con varias flechas divergentes hacia distintas alturas de las estanterías.

Las estanterías contienen objetos tipo carpetas/archivadores de colores variados (grises, blancos, oscuros), representando materiales almacenados. El diagrama ilustra la jerarquía: Fila (pasillo) → Estante → Repisa, que es la lógica de direccionamiento de ubicaciones en el sistema WM.

## Slide 9

**Fig. 7-16: Recipientes (ubicaciones)**

Fotografía en blanco y negro de tres recipientes/contenedores plásticos apilados (tipo cajas industriales apilables), usados como ejemplo de "ubicaciones" físicas en el almacén. Cada recipiente tiene etiquetas adhesivas pegadas en el borde frontal con códigos numéricos visibles (ej. "038565", "038420", "030446"), fechas tipo "LP 10/04/2010", y códigos de barras. Dentro de los recipientes se aprecian piezas metálicas/herramientas o materiales sueltos apilados. La imagen ilustra que un recipiente físico (contenedor) puede constituir una ubicación de almacenamiento identificada por etiqueta/código.

## Slide 10

**Fig. 7-17 Cuantos en una ubicación**

Diagrama esquemático con 4 recuadros (cajas azules con degradado) representando distintos escenarios de "cuantos" (quants) dentro de una ubicación:

- **Ubicación 1 (arriba-izquierda)**: contiene un solo óvalo — "Material A". Un cuanto único.
- **Ubicación 2 (arriba-derecha)**: contiene dos óvalos — "Material A" y "Material B". Dos materiales distintos en la misma ubicación.
- **Ubicación 1 (abajo-izquierda)**: contiene dos óvalos — "Material A Lote #5" y "Material A Lote #6". Mismo material pero distinguido por número de lote (dos cuantos separados por lote).
- **Ubicación 2 (abajo-derecha)**: contiene dos óvalos — "Material A De libre utilización" y "Material A En inspección de calidad". Mismo material pero distinguido por estado de stock (libre utilización vs. inspección de calidad).

El diagrama ilustra que una ubicación puede alojar uno o más "cuantos" (quants), y que un cuanto se diferencia por material, lote o estado de stock, aunque coincidan en la misma ubicación física.
