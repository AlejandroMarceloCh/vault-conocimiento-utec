---
curso: SIOPS
titulo: Caso_Dell_Intel
slides: 10
fuente: Caso_Dell_Intel.pdf
---

## Slide 1

Portada (decorativa: logo UTEC arriba a la derecha, logos de Dell e Intel al centro, franjas azules decorativas de fondo).

- Título: "Caso Dell - Intel"
- Subtítulo: "Procure-to-Pay y SAP MM"
- Profesor: Carlos Villanueva Q.

## Slide 2

**Situación del caso** — slide de texto (bullets), sin elementos visuales adicionales más allá del fondo decorativo.

- Dell opera plantas en múltiples países
- Compra grandes volúmenes de microprocesadores a Intel
- Existe una relación estratégica proveedor–cliente
- Se requiere coordinar compras globales con ejecución local

## Slide 3

**Contexto Operativo: La Simbiosis Dell-Intel** — diagrama sobre un mapamundi esquemático (contorno de continentes en gris claro).

- Al centro un círculo naranja rotulado "Sede Central (Global)", conectado mediante flechas/líneas a varios íconos circulares (nodos) distribuidos sobre el mapa, representando plantas en distintos continentes (Norteamérica, Sudamérica, Europa —dos nodos—, Medio Oriente/India, y dos nodos en Asia).
- Recuadro superior derecho "Plantas Locales (Ejecución)": "Instalaciones de fabricación descentralizadas".
- Recuadro inferior izquierdo "Plantas Locales": "fabricación descentralizar" (texto cortado en el original).
- Globo de diálogo que sale de la Sede Central: "Intel mantiene una fuerza de ventas dedicada en la oficina central de Dell para negociar contratos globales masivos de microprocesadores."
- Franja inferior en texto grande: "Dell EE. UU. compra a Intel EE. UU., Dell China a Intel China. La ejecución es 100% local, pero el precio es 100% global."

## Slide 4

**Modelo de abastecimiento** — slide de texto (bullets), sin elementos visuales adicionales.

- Compras centralizadas: negociación global con Intel
- Contrato global: define precios y condiciones
- Compras descentralizadas: ejecución local por planta
- Cada planta genera sus propias órdenes de compra (PO)

## Slide 5

**El Modelo Híbrido de Aprovisionamiento** — diagrama tipo balanza mecánica/futurista (ilustración estilo engranaje metálico).

- Estructura de balanza: un pilar central con mecanismo tipo circuito, del que cuelgan dos platillos en forma de engranaje, uno a cada lado.
- Platillo izquierdo, etiqueta "Macro": **"Estrategia Centralizada"** — "Consolida los requerimientos de compra globales y negocia los mejores precios por volumen masivo con Intel."
- Platillo derecho, etiqueta "Micro": **"Ejecución Táctica Descentralizada"** — "Emisión de pedidos desde las plantas de fabricación para adaptarse instantáneamente a las condiciones de tiempo y logística locales."
- Recuadro central sobre el pilar: "Organización de compras de referencia", con flechas hacia ambos platillos (izquierda y derecha).
- Recuadro superior derecho conectado al pilar: "Puente estratégico que negocia el contrato global, el cual es heredado y utilizado autónomamente por todas las sociedades locales."

## Slide 6

**Beneficios del modelo** — slide de texto (bullets), sin elementos visuales adicionales.

- Mejores precios por volumen global
- Mayor control estratégico de compras
- Flexibilidad operativa en cada planta
- Mayor visibilidad de demanda para el proveedor (Intel)

## Slide 7

**Datos Organizativos SAP** — diagrama de mapeo (tabla de correspondencia) entre concepto de negocio (columna izquierda, cajas azules) y entidad organizativa SAP (columna derecha, cajas grises con borde naranja), unidas por flechas horizontales:

| Concepto de negocio | → | Entidad SAP |
|---|---|---|
| Corporación entera global (Dell Inc.) | → | **Mandante** — Nivel más alto del sistema |
| Operaciones regionales legales (ej. Dell China) | → | **Sociedad** — Unidad contable independiente |
| Planta de fabricación local en un país | → | **Centro** — Instalación donde se gestiona inventario y producción |
| Sede central de negociación con Intel | → | **Organización de Compras (de Referencia)** — Rol estratégico multinivel |
| Equipos locales que piden chips diariamente | → | **Grupo de Compras** — Punto de contacto táctico diario con el proveedor |

## Slide 8

**Datos Maestros y Flujo Procure-to-Pay** — diagrama de flujo en dos niveles.

- Nivel superior, "Datos Maestros" (encabezado gris oscuro) con tres cajas de entrada (todas alimentan el flujo inferior) más un elemento aparte:
  - Registro Info de Compras
  - Maestro de Materiales
  - Maestro de Proveedores
  - Recuadro naranja aparte: "Contrato Negociado Globalmente"
- Nivel inferior, flujo secuencial en flechas (proceso Procure-to-Pay) de izquierda a derecha:
  1. **Solicitud de Pedido** — "Requerimiento originado en la fábrica."
  2. **Orden de Pedido** — "Grupo de Compras local la emite usando las condiciones de la Organización de Referencia."
  3. **Recepción de Mercancías** — "Entrada física de microprocesadores al Centro."
  4. **Recepción de Factura** — "Cobro del proveedor local."
- A la derecha del flujo, ícono de candado/escudo naranja "Triple verificación": "Validación automática del sistema: Orden de Pedido = Recepción física = Factura."

## Slide 9

**Preguntas de reflexión** — slide de texto (bullets), sin elementos visuales adicionales.

- ¿Por qué separar compras estratégicas y operativas?
- ¿Qué riesgos existen al trabajar con un solo proveedor?
- ¿Cómo ayuda SAP a integrar este modelo?
- ¿Qué pasaría si no existiera un contrato global?

## Slide 10

**Conclusiones: El Valor del Modelo Híbrido** — diagrama de dos columnas comparativas más una franja de cierre.

- Columna izquierda (ícono de flecha hacia abajo) "Ventajas para Dell":
  - **Eficiencia Financiera:** Mejores precios y condiciones por volumen acumulado globalmente.
  - **Agilidad Operativa:** Control total sobre operaciones tácticas diarias de compra según demanda de fábrica.
- Columna derecha (ícono de diana/objetivo) "Ventajas para Intel":
  - **Visibilidad Estratégica:** Visión global de los patrones de compra a nivel mundial.
  - **Sincronización de Capacidad:** Ajuste de fundiciones para entregar la cantidad exacta de chips donde y cuando se necesiten.
- Franja inferior destacada en cian: "Un diseño organizativo en SAP MM que transforma requerimientos locales en poder de negociación global."
- Marca de agua inferior derecha: "NotebookLM" (indica que la slide fue generada con esa herramienta).
