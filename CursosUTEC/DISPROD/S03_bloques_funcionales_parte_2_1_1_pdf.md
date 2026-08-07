---
curso: DISPROD
titulo: S03 - bloques funcionales - parte 2-1 (1)
slides: 19
fuente: S03 - bloques funcionales - parte 2-1 (1).pdf
---

## Slide 1

Portada del curso. Fondo celeste con formas geométricas decorativas y logo UTEC (decorativa).

Texto: "DISEÑO DE PRODUCTOS Y SERVICIOS" — subtítulo del capítulo: "ARQUITECTURA DE PRODUCTOS".

## Slide 2

Diagrama de las 6 fases del proceso de desarrollo de producto (flechas de colores en la parte superior, apuntando hacia la derecha, superpuestas escalonadamente):

- Fase 1: Planeación (verde)
- Fase 2: Desarrollo del Concepto (amarillo)
- Fase 3: Diseño a nivel sistema (rojo)
- Fase 4: Diseño de Detalle (celeste)
- Fase 5: Pruebas (azul claro)
- Fase 6: Inicio Producción (azul oscuro)

Debajo, una matriz de barras horizontales que representa actividades/disciplinas transversales, cada una con una línea de color vertical que indica en qué fases participa (el color de la línea vertical corresponde al color de la fase de inicio y se extiende hasta donde termina su participación):

| Actividad | Rango de fases (según extensión de la barra) |
|---|---|
| Identificación de Oportunidades | Fase 1 |
| Planeamiento del Producto | Fase 1 |
| Id. de Necesidades del cliente | Fase 1 – inicio Fase 2 |
| Especificaciones del producto | Fase 1 – Fase 3 (aprox) |
| Generación, Selección y Prueba de Concepto | Fase 2 |
| Arquitectura de Productos | Fase 2 – Fase 3 |
| Prototipado | Fase 2 – Fase 4 |
| Diseño Industrial | Fase 2 – Fase 4 |
| Diseño Manufactura | Fase 3 – Fase 5 |
| Gestión del proceso de desarrollo de productos | Fase 1 – Fase 6 (toda la línea) |
| Propiedad Intelectual | Fase 1 – Fase 6 (toda la línea) |

Muestra cómo Arquitectura de Productos se ubica principalmente entre Fase 2 (Desarrollo del Concepto) y Fase 3 (Diseño a nivel sistema).

## Slide 3

Slide de transición/portada de sección: "1. ARQUITECTURA DE PRODUCTOS" en texto rojo grande sobre fondo blanco con barra celeste lateral (decorativa). Sin contenido adicional.

## Slide 4

Fotografía de producto (decorativa/ilustrativa, sin texto): conjunto de accesorios de un iPhone/iPod antiguo dispuestos sobre fondo blanco — dock de carga, audífonos con control remoto, cable de extensión de audio, conector dock-a-USB de 30 pines, cargador USB de pared, adaptador de línea (line-out dock), y un dispositivo tipo grabadora/adaptador negro. Ilustra visualmente el concepto de "elementos físicos" de un producto (varios componentes físicos que interactúan) que se desarrolla en las slides siguientes.

## Slide 5

Título: "Arquitectura de un Producto". Texto (sin elementos visuales adicionales):

- Es el esquema donde los elementos funcionales de un producto están acomodados en bloques físicos, e interactúan entre sí.
- Su propósito es definir los elementos físicos del producto en base a su función y su relación con el resto de partes.

## Slide 6

Título: "¿Para qué?". Lista de propósitos (solo texto, sin visual):

- Minimizar el número de piezas
- Reducir costos
- Aumentar eficiencia del producto
- Disminuir el error y # de fallas (ensamblaje)
- Facilitar la gestión del producto

## Slide 7

Diagrama circular concéntrico. Círculo central naranja grande con el texto "Arquitectura de Producto". Alrededor, conectado por un anillo gris, tres círculos periféricos:

- Arriba (verde): "Estrategia Marketing"
- Abajo-izquierda (azul): "Gest. Desarrollo Producto"
- Abajo-derecha (rojo): "Capacidad Manufactura"

Ilustra que la arquitectura de producto es el punto de convergencia entre estas tres áreas.

## Slide 8

Título: "Elementos Arq. Productos". Diagrama jerárquico simple: un recuadro verde superior "Producto" que se descompone (implícitamente, sin líneas de conexión dibujadas) en dos recuadros azules inferiores: "Elementos Funcionales" y "Elementos Físicos".

## Slide 9

Texto explicativo (sin diagrama):

"Un producto puede considerarse en:"

- Elementos Funcionales: Operaciones y transformaciones que contribuyen al rendimiento de un producto.
- Elementos Físicos: Partes, componentes y subconjuntos que ponen en práctica las funciones del producto.

## Slide 10

Título: "Ejemplo" (caso de una impresora). Tabla comparativa en dos columnas, con una fotografía de una impresora multifuncional (marca visible tipo Epson) en la esquina inferior derecha:

| Elementos Funcionales | Elementos Físicos |
|---|---|
| Almacenar papel | Cartucho de impresión |
| Comunicarse con PC | Base para escanear documentos |
| Inyectar tinta | Dispositivo de entrega de tinta |
| Aceptar entrada de usuarios | Cabezal para posicionar el dosificador |
| Controlar impresora | |
| Posicionar papel | |
| Almacenar papel en blanco | |
| Desplegar status | |

## Slide 11

Título: "Pasos para determinar la arquitectura". Lista de 4 pasos (sin visual, se desarrollan en las slides 12-18):

- Paso 1: Crear un esquema del producto
- Paso 2: Agrupar los elementos del esquema
- Paso 3: Crear una disposición geométrica aproximada
- Paso 4: Identificar interacciones incidentales

## Slide 12

Título: "Paso 1: Diagrama funcional general". Diagrama de caja negra con flujo entradas→proceso→salidas, ejemplo de una pistola de clavos manual:

- Caja central: "Pistola de clavos manual"
- Entradas (izquierda): Energía (?) [flecha gruesa], Material (clavos) [flecha fina], Señal (accionar herramienta) [flecha punteada]
- Salidas (derecha): Energía (?) [flecha gruesa], Material (clavo clavado) [flecha fina], Señal (?) [flecha punteada]

El grosor/estilo de la flecha codifica el tipo de flujo (energía = gruesa sólida, material = fina sólida, señal = punteada), convención que se mantiene en el diagrama siguiente.

## Slide 13

Título: "Paso 1: Diagrama funcional detallado". Expande la caja negra de la slide anterior en sub-funciones conectadas, organizadas en 3 filas (energía, clavos, señal/acción) y 3 columnas de proceso, convergiendo en un bloque final:

Fila Energía: "Almacenar o aceptar energía externa" → "Convertir energía en energía traslacional" → (diagonal) "Aplicar energía al clavo"

Fila Clavos: "Almacenar clavos" → "Aislar clavo" → "Aplicar energía al clavo" → salida "Clavo clavado"

Fila Acción: "Detecta activación" → "Disparar herramienta" → (flecha punteada hacia arriba) alimenta tanto a "Aislar clavo" como a "Aplicar energía al clavo"

Todo el conjunto está enmarcado en un recuadro grande que representa el sistema completo, con entradas "Energía", "Clavos" y "Acción" a la izquierda y salida "Clavo clavado" a la derecha.

## Slide 14

Título: "Paso 2: Agrupar los elementos del esquema". Diagrama de bloques funcionales de una impresora, agrupados en columnas por afinidad funcional (unidos por líneas sólidas gruesas = conexión física/directa, líneas punteadas = conexión de control/datos):

- Columna 1: "Cubrir impresora" — "Proveer soporte estructural" (unidos)
- Columna 2 (tinta/papel): "Almacenar tinta" — "Posicionar cartucho en eje X" — "Posicionar papel en eje Y" — "Recoger papel", con "Almacenar salida" y "Almacenar papel en blanco" conectados lateralmente
- Columna 3 (control): "Aceptar entrada de datos" y "Desplegar status" (punteado) → "Controlar impresora"; "Administrar energía" → "Suministrar corriente eléctrica"; "Transmitir datos" (punteado) → "Transmitir datos @ impresora"
- Líneas punteadas cruzadas conectan "Posicionar cartucho en eje X", "Posicionar papel en eje Y" y "Recoger papel" con "Controlar impresora"

## Slide 15

Continuación del diagrama de la slide 14, ahora con los grupos encerrados en recuadros etiquetados como los bloques físicos resultantes (nombres de los "chunks" o bloques físicos del producto):

- "Caja": contiene "Cubrir impresora" y "Proveer soporte estructural"
- "Chasis": etiqueta que engloba el grupo anterior a nivel físico
- "Mecanismo de impresión": contiene "Almacenar tinta", "Posicionar cartucho en eje X", "Posicionar papel en eje Y", "Recoger papel"
- "Charola de papel": contiene "Almacenar salida" y "Almacenar papel en blanco"
- "Tarjeta de Interfaz de usuario": contiene "Aceptar entrada de datos" y "Desplegar status"
- "Tarjeta de control": contiene "Controlar impresora", "Administrar energía", "Transmitir datos"
- "Cable de E.E" (energía eléctrica): contiene "Suministrar corriente eléctrica"
- "Software en PC": contiene "Transmitir datos @ impresora"

Las líneas gruesas sólidas y punteadas del esquema funcional original se mantienen para mostrar cómo cada grupo funcional se traduce en un chunk/bloque físico concreto.

## Slide 16

Título: "Paso 3: Disposición Geométrica". Imagen (foto de página de libro/texto escaneado, algo difusa, con texto de fondo apenas visible en gris) mostrando un boceto isométrico 3D de la disposición física de una impresora, con etiquetas:

- Tarjeta lógica
- Tarjeta de interfase de usuario
- Cartucho de impresión
- Charola de papel
- Mecanismo de impresión
- Chasis

Ilustra cómo los bloques físicos identificados en el paso 2 se acomodan espacialmente unos sobre otros (chasis en la base, mecanismo de impresión y charola de papel apilados, cartucho de impresión encima, tarjetas lógica y de interfaz de usuario en los costados).

## Slide 17

Título: "Disposición Geométrica" (segundo ejemplo, más complejo: mecanismo de una impresora láser/copiadora). Diagrama técnico a color mostrando el layout físico interno de una máquina de impresión láser, con múltiples componentes etiquetados alrededor de un tambor central:

- Estación de Fijación (magenta, izquierda) conectada por una banda/cinta al tambor central
- Trans. de papel
- Estación de limpieza
- Estación de descarga
- Filtro de limpieza
- Tambor fotoconductor (centro, marrón)
- Corotrón de carga
- Deflector acústico óptico
- Espejo poligonal (cian, derecha)
- Espejos
- Estación de transferencia
- Ajuste de papel
- Láser (magenta, vertical)
- Estación de revelado
- Dispositivo de impresión de formularios (círculo magenta)
- Apilador automático de salida (abajo izquierda)
- Bandeja de entrada de formularios (abajo centro)

Ejemplo de disposición geométrica real y compleja, mucho más detallado que el de la impresora de inyección de tinta de la slide anterior.

## Slide 18

Título: "Paso 4: Diagrama de interacción incidental". Diagrama de bloques con flechas etiquetadas que muestran interacciones NO planeadas/secundarias entre los bloques físicos (efectos colaterales como vibración, calor, interferencia):

- "Caja" → (Estilo) → "Charola de papel"
- "Charola de papel" → (Vibración) → "Mecanismo de impresión"
- "Mecanismo de impresión" → (Distorsión térmica) → "Tarjeta lógica"
- "Chasis" → (Distorsión térmica; blindaje de RF) → "Tarjeta lógica"
- "Tarjeta lógica" → (Interferencia de RF) → "Cable de corriente"
- Bloques sin conexiones incidentales dibujadas: "Tarjeta de interfaz de usuario", "Software controlador de computadora central"

Muestra cómo, además de las interacciones funcionales intencionadas, existen efectos físicos no deseados entre bloques (vibración, calor, interferencia electromagnética) que también deben gestionarse en el diseño de la arquitectura.

## Slide 19

Slide de cierre con la tarea del capítulo (solo texto, sin visual):

"Tarea: Desarrollar la Arquitectura de su producto"
