---
curso: DISPROD
titulo: Especificaciones del producto (1)
slides: 17
fuente: Especificaciones del producto (1).pdf
---

## Slide 1

Portada del curso (decorativa: fondo celeste con triángulo blanco, logo UTEC).

Texto: "DISEÑO DE PRODUCTOS Y SERVICIOS — ESPECIFICACIONES TÉCNICAS". Profesor: Francisco Camacho, fcamacho@utec.edu.pe.

## Slide 2

Diagrama de bloques funcionales de una impresora (ejemplo de descomposición funcional en cajas rotuladas conectadas por líneas sólidas y punteadas). Agrupaciones por componente físico (recuadros grandes con borde) que contienen sub-funciones (recuadros internos):

- **Chasis**: Cubrir impresora — Proveer soporte estructural (conectados entre sí, línea gruesa).
- **Charola de papel**: Almacenar salida — Almacenar papel en blanco (cada uno conecta a bloques del "Mecanismo de impresión").
- **Mecanismo de impresión**: Almacenar tinta → Posicionar cartucho en eje X → Posicionar papel en eje Y → "Recoger" papel (conectados en cadena vertical; "Posicionar cartucho en eje X", "Posicionar papel en eje Y" y "Recoger papel" se conectan con líneas punteadas hacia "Controlar impresora").
- **Tarjeta de Interfaz de usuario**: Aceptar entrada de datos — Desplegar status (ambos conectan con líneas punteadas hacia "Tarjeta de control").
- **Tarjeta de control**: Controlar impresora — Administrar energía — Transmitir datos.
- **Cable de E.E.**: Suministrar corriente eléctrica (conectado con línea gruesa a "Administrar energía").
- **Software en PC**: Transmitir datos @ impresora (conectado con línea punteada a "Transmitir datos").

Es el ejemplo clásico de diagrama de función/bloques usado para derivar especificaciones técnicas de cada subsistema.

## Slide 3

Título: "Paso 3: Disposición Geométrica".

Imagen central: fotografía/escaneo (fondo texto de libro ilegible detrás, semi-transparente) de un boceto isométrico en línea (wireframe 3D) de una impresora, con etiquetas manuscritas apuntando a cada volumen: "Tarjeta lógica", "Tarjeta de interfase de usuario", "Cartucho de impresión", "Charola de papel", "Mecanismo de impresión", "Chasis". Se ve un recuadro superpuesto con ruta de archivo "T:\UTEC\Manual de marca\untitled1.png" (artefacto de la imagen pegada, no contenido del curso). Ilustra cómo se traduce el diagrama de bloques funcional a una disposición física/volumétrica de los componentes.

## Slide 4

Título: "Disposición Geométrica" (continuación/otro ejemplo).

Diagrama técnico en color de la disposición geométrica interna de una impresora láser, con componentes ubicados espacialmente y etiquetados con líneas guía:
- Estación de Fijación (rectángulo magenta a la izquierda, con rodillos).
- Trans. de papel (rodillos magenta arriba a la izquierda).
- Apilador automático de salida (bandeja apilada abajo a la izquierda).
- Estación de descarga, Estación de limpieza, Filtro de limpieza, Tambor fotoconductor (cilindro café central), Corotron de carga, Deflector acústico óptico, Espejo poligonal (a la derecha), Espejos.
- Estación de transferencia, Ajuste de papel, Láser (barra magenta vertical), Estación de revelado (cilindro verde).
- Bandeja de entrada de formularios (bandeja apilada abajo al centro).
- Dispositivo de impresión de formularios (círculo magenta a la derecha).

Es un diagrama de disposición física real (layout de componentes ópticos/mecánicos) para mostrar el nivel de detalle geométrico que se alcanza en el "Paso 3" del proceso de especificación.

## Slide 5

Slide separador de sección (texto centrado en rojo sobre fondo blanco, franja celeste decorativa a la izquierda, logo UTEC).

Texto: "1. ESPECIFICACIONES TÉCNICAS DEL PRODUCTO".

## Slide 6

Slide de texto ("¿Qué son las especificaciones?") con icono decorativo (regla y lápiz cruzados) en la esquina inferior derecha.

Contenido (viñetas):
- Las necesidades de los clientes son ideas subjetivas.
- Se debe buscar las variables relacionadas a la necesidad y cuantificarlas -> especificaciones.
- En un principio se debe establecer especificaciones objetivo para luego afinarse según las pruebas de concepto que se hagan.
- Consta de una medida y un valor.

## Slide 7

Slide de texto ("¿Qué son las especificaciones?", continuación), ejemplos concretos de especificaciones:
- El tiempo promedio de instalación debe ser menor a 90 segundos.
- La autonomía energética del equipo debe ser como mínimo de tres (03) horas.
- El peso máximo es de dos (02) kilogramos.
- El equipo debe soportar la prueba industrial NH 345.

## Slide 8

Título: "Ejercicio en Clase". Texto: "Identifique las especificaciones de los siguientes productos:".

Imágenes: tres fotos de producto en fila — (1) teléfono inalámbrico Panasonic negro con base cargadora, pantalla LCD mostrando "12:00 31 Dic"; (2) mouse inalámbrico azul/negro marca Genius con su receptor USB flotando junto con ondas de señal dibujadas; (3) licuadora roja con jarra de vidrio transparente y base de control con botones.

## Slide 9

Título: "Paso 1: Listar Necesidades". Tabla con 15 filas, todas del elemento "Suspensión" (ejemplo de bicicleta de montaña):

| Item | Elemento | Necesidad | Importancia (0-5) |
|---|---|---|---|
| 1 | Suspensión | reduce vibración en las manos | 3 |
| 2 | Suspensión | Permite recorrido fácil en terreno lento y difícil | 2 |
| 3 | Suspensión | permite ajustar la sensibilidad | 3 |
| 4 | Suspensión | Permanece rígida en vueltas cerradas | 4 |
| 5 | Suspensión | es ligera en peso | 4 |
| 6 | Suspensión | Se ajusta a una gran variedad de bicicletas y llantas | 5 |
| 7 | Suspensión | Fácil de instalar | 1 |
| 8 | Suspensión | Inspira orgullo | 5 |
| 9 | Suspensión | No se contamina con agua | 5 |
| 10 | Suspensión | No se contamina con polvo | 5 |
| 11 | Suspensión | Es de fácil acceso para el mantenimiento | 3 |
| 12 | Suspensión | Permite fácil reposición de piezas gastadas | 1 |
| 13 | Suspensión | permite un mantenimiento con herramientas sencillas | 3 |
| 14 | Suspensión | Tiene una larga vida útil | 5 |
| 15 | Suspensión | es segura en un choque | 5 |

## Slide 10

Título: "Paso 2: Matriz Necesidad/Métrica". Matriz de correlación (filas = las 15 necesidades del slide 9, columnas numeradas 1-9 = métricas, con encabezados rotados verticalmente):

1. Atenuación al tomar el manubrio a 10 Hz
2. Precarga del resorte
3. Tiempo mínimo de descenso en piso de prueba
4. Valor máximo en el monster test
5. Rango de ajuste del coeficiente de mantenimiento
6. Masa Total
7. Inspira orgullo
8. Tiempo de ensamble para mantenimiento
9. Herramientas especiales necesarias para mantenimiento

Marcas "x" (correlación necesidad↔métrica):
- Fila 1 (reduce vibración en las manos): x en col 1, col 3, col 4
- Fila 2 (recorrido fácil en terreno lento y difícil): x en col 2
- Fila 3 (permite ajustar sensibilidad): x en col 5
- Fila 4 (rígida en vueltas cerradas): x en col 6
- Fila 8 (Inspira orgullo): x en col 7
- Fila 11 (fácil acceso mantenimiento): x en col 8
- Fila 12 (fácil reposición piezas gastadas): x en col 8 y col 9
- Fila 13 (mantenimiento con herramientas sencillas): x en col 9
- Filas 5, 6, 7, 9, 10, 14, 15: sin marca en esta vista.

Muestra cómo cada necesidad del cliente se traduce a una o más métricas medibles.

## Slide 11

Título: "Paso 2: Lista de Métricas". Tabla:

| Item | Número de Necesidad | Métrica | Importancia (0-5) | Unidades |
|---|---|---|---|---|
| 1 | 1 | Atenuación al tomar el manubrio a 10 Hz | 3 | dB |
| 2 | 2 | Precarga del resorte | 3 | N |
| 3 | 1 | Tiempo mínimo de descenso en piso de prueba | 5 | s |
| 4 | 1 | Valor máximo en el monster test | 5 | g |
| 5 | 3 | Rango de ajuste del coeficiente de mantenimiento | 3 | N-s/m |
| 6 | 5 | Masa Total | 4 | Kg |
| 7 | 8 | Inspira orgullo | 5 | Subj |
| 8 | 11,12 | Tiempo de ensamble para mantenimiento | 3 | s |
| 9 | 12,13 | Herramientas especiales necesarias para mantenimiento | 3 | Lista |

## Slide 12

Título: "Paso 3: Benchmark - Cuantitativo". Misma tabla de métricas que el slide 11, ampliada con 2 filas nuevas y 3 columnas de competidores (vacías, para llenar en clase):

| Item | Núm. Necesidad | Métrica | Imp (0-5) | Unidades | Compet. 1 | Compet. 2 | Compet. 3 |
|---|---|---|---|---|---|---|---|
| 1 | 1 | Atenuación al tomar el manubrio a 10 Hz | 3 | dB | — | — | — |
| 2 | 2 | Precarga del resorte | 3 | N | — | — | — |
| 3 | 1 | Tiempo mínimo de descenso en piso de prueba | 5 | s | — | — | — |
| 4 | 1 | Valor máximo en el monster test | 5 | g | — | — | — |
| 5 | 3 | Rango de ajuste del coeficiente de mantenimiento | 3 | N-s/m | — | — | — |
| 6 | 5 | Masa Total | 4 | Kg | — | — | — |
| 7 | 8 | Inspira orgullo | 5 | Subj | — | — | — |
| 8 | 11,12 | Tiempo de ensamble para mantenimiento | 3 | s | — | — | — |
| 9 | 12,13 | Herramientas especiales necesarias para mantenimiento | 3 | Lista | — | — | — |
| 10 | 14 | Ciclos de monster antes de falla | 5 | Ciclos | — | — | — |
| 11 | 16 | Costo Unitario de manufactura | 5 | US$ | — | — | — |

## Slide 13

Título: "Paso 3: Benchmark - Cualitativo". Tabla con las 15 necesidades del slide 9 más 3 columnas de competidores (vacías):

| Item | Necesidad | Imp (0-5) | Compet. 1 | Compet. 2 | Compet. 3 |
|---|---|---|---|---|---|
| 1 | reduce vibración en las manos | 3 | — | — | — |
| 2 | Permite recorrido fácil en terreno lento y difícil | 2 | — | — | — |
| 3 | permite ajustar la sensibilidad | 3 | — | — | — |
| 4 | Permanece rígida en vueltas cerradas | 4 | — | — | — |
| 5 | es ligera en peso | 4 | — | — | — |
| 6 | Se ajusta a una gran variedad de bicicletas y llantas | 5 | — | — | — |
| 7 | Fácil de instalar | 1 | — | — | — |
| 8 | Inspira orgullo | 5 | — | — | — |
| 9 | No se contamina con agua | 5 | — | — | — |
| 10 | No se contamina con polvo | 5 | — | — | — |
| 11 | Es de fácil acceso para el mantenimiento | 3 | — | — | — |
| 12 | Permite fácil reposición de piezas gastadas | 1 | — | — | — |
| 13 | permite un mantenimiento con herramientas sencillas | 3 | — | — | — |
| 14 | Tiene una larga vida útil | 5 | — | — | — |
| 15 | es segura en un choque | 5 | — | — | — |

## Slide 14

Título: "Paso 4: Especificaciones Objetivo". Tabla final con valores marginal e ideal por métrica:

| Item | Núm. Necesidad | Métrica | Imp (0-5) | Unid. | Valor Marginal | Valor Ideal |
|---|---|---|---|---|---|---|
| 1 | 1 | Atenuación al tomar el manubrio a 10 Hz | 3 | dB | >10 | >15 |
| 2 | 2 | Precarga del resorte | 3 | N | 480-800 | 650-700 |
| 3 | 1 | Tiempo mínimo de descenso en piso de prueba | 5 | s | <13 | <11 |
| 4 | 1 | Valor máximo en el monster test | 5 | g | <3.5 | <3.2 |
| 5 | 3 | Rango de ajuste del coeficiente de mantenimiento | 3 | N-s/m | 0 | >200 |
| 6 | 5 | Masa Total | 4 | Kg | <1.4 | <1.1 |
| 7 | 8 | Inspira orgullo | 5 | Subj | >3 | >5 |
| 8 | 11,12 | Tiempo de ensamble para mantenimiento | 3 | s | <60 | <35 |
| 9 | 12,13 | Herramientas especiales necesarias para mantenimiento | 3 | Lista | Hex | Hex |
| 10 | 14 | Ciclos de monster antes de falla | 5 | Ciclos | >300K | >500K |
| 11 | 16 | Costo Unitario de manufactura | 5 | US$ | <85 | <65 |

Cierra el ejemplo de la suspensión de bicicleta con las especificaciones finales cuantificadas (valor mínimo aceptable vs. valor deseado).

## Slide 15

Título: "Diagrama de bloques" (plantilla vacía, ejemplo genérico de producto electrónico). Diagrama de bloques funcionales sin componentes internos detallados, solo las 6 cajas de nivel superior conectadas:

- **1. Etapa Sensado** (naranja) → conecta con línea sólida a **2. Etapa de Control** (azul).
- **2. Etapa de Control** ↔ **3. Comunicación de Datos** (morado): flecha bidireccional.
- **2. Etapa de Control** → **6. Actuadores** (rojo): línea que baja y se ramifica en dos salidas.
- **2. Etapa de Control** ↔ **5. Interfaz de Usuario** (amarillo claro): línea que baja y se ramifica en dos (una entrada, una salida con flecha).
- **4. Fuente de Energía** (verde): recibe entrada "220VAC" (flecha ancha) y "Panel Solar" (recuadro con flecha), y alimenta a la Etapa de Sensado y Etapa de Control (líneas punteadas verticales de energía).

Todas las cajas internas de cada bloque están vacías (plantilla en blanco) excepto los rótulos de las 6 etapas.

## Slide 16

Título: "Diagrama de bloques" (mismo esquema del slide 15, ahora completado con un ejemplo concreto — sistema de riego/monitoreo). Mismas 6 etapas, ahora con contenido interno:

- **1. Etapa Sensado** (naranja): Sensor de Humedad, Sensor de Distancia (ambos → Controlador).
- **2. Etapa de Control** (azul): Controlador (bloque central único, recibe de sensores, y conecta bidireccional con Comunicación de Datos, y hacia Actuadores e Interfaz de Usuario).
- **3. Comunicación de Datos** (morado): Transmisión / Recepción (flecha bidireccional con el Controlador).
- **4. Fuente de Energía** (verde): 220VAC → Conversor AC/DC; Panel Solar → Conversor DC/DC → Batería.
- **5. Interfaz de Usuario** (amarillo): Pantalla LCD (salida), Teclado (entrada, flecha bidireccional).
- **6. Actuadores** (rojo): Motor 1, Bomba de Agua (ambos alimentados desde el Controlador).

Es la instancia resuelta del diagrama de bloques genérico del slide 15, ilustrando un sistema embebido de sensado/control con energía solar.

## Slide 17

Slide de collage de imágenes (sin texto/título), 4 fotografías/bocetos de diseño industrial mostrando el proceso creativo de bocetado de productos:

- Superior izquierda: bocetos a mano en acuarela/marcador de dispositivos médicos tipo jeringa/inyector (varias vistas, colores turquesa/lila, con anotaciones manuscritas en las piezas: "cierre hermético con...", "acople de rosca", etc.).
- Superior derecha: panel "LLTechPROJECT" — bocetos de un dispositivo de diagnóstico médico (histología digital), mostrando despiece, vistas de ensamblaje y variantes de forma, con texto: "The brief was to design a new digital histology machine that establishes a cancer diagnosis in only 10 minutes."
- Inferior izquierda: múltiples bocetos en azul de zapatillas deportivas (vistas laterales, suela, en distintos ángulos) y una zapatilla renderizada a color (gris/azul/verde neón) como resultado final.
- Inferior derecha: bocetos a lápiz de un dispositivo cosmético/dispensador (tipo aplicador), con anotaciones manuscritas ("screw on front side", "tapered?", "cap on spring", "in mold bezel", etc.) mostrando variantes de tapa y forma.

Slide decorativa/inspiracional: ejemplos de sketching de diseño de producto, sin texto explicativo del profesor.
