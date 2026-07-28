---
curso: CALIDAD
titulo: S15_CM_Standares (3)
slides: 16
fuente: S15_CM_Standares (3).pdf
---

## Slide 1

Portada de la sesión. Fondo con foto decorativa (dos profesionales revisando documentos, tratada en duotono verde-azulado con líneas diagonales blancas decorativas).

Título: "INTRODUCCIÓN HERRAMIENTAS LEAN" — "Ses15" (indicador de sesión, en teal grande).

Agenda (bullets):
- CELDAS DE MANUFACTURA
- ESTANDARES DE TRABAJO

## Slide 2

**Manufactura Celular** (título con icono decorativo de "estrella brillante" naranja, usado como marca de sección en todo el capítulo).

Lista numerada (1-4) con el concepto:
1. Es un concepto de Fabricación donde la distribución de la planta se mejora significativamente evitando interrumpir la producción entre cada operación.
2. Reducir drásticamente el tiempo, maximizando las habilidades del personal y haciendo que cada empleado realice varias operaciones.
3. En empresas tradicionales, los procesos están separados o departamentalizados, lo cual provoca que se tengan que almacenar, mover, trasladar y manipular los materiales por muchas áreas antes de usarlos.
4. Consiste en agrupar máquinas y operaciones secuenciales, en las que se pueda fabricar un producto completo de principio a fin sin recurrir tanto al uso de transportes, eliminando inventarios en proceso y haciendo fluir la producción continuamente.

**Diagrama (derecha):** ilustración estilo boceto de una célula de manufactura en forma de U/circular: 4 máquinas dispuestas alrededor de un operador central, conectadas por una línea punteada en forma de óvalo que representa el flujo/recorrido del operador entre las máquinas y dos bandejas de piezas (entrada y salida) a los costados del operador.

## Slide 3

**Por qué se implementa la manufactura celular?** (mismo icono de sección).

Recuadro verde claro con lista numerada (1-7):
1. Da continuidad en las operaciones de la planta.
2. Elimina inventarios en proceso que generan defectos por manipulación.
3. Crea procesos flexibles al producir diversos productos en una sola área.
4. Aumenta la flexibilidad y eficiencia de las empresas.
5. Permite que los operadores sean más eficientes ya que se puede producir lo mismo con menos personas.
6. Los operadores se involucran en más tareas relacionadas con el producto, al grado de que a veces un solo trabajador elabora un artículo completo.
7. Evita transportes, demoras, movimientos de materiales, inventarios en proceso y sobreproducción.

## Slide 4

**Implementar Celdas de Trabajo.**

Texto: Al rediseñar procesos existentes, puede tomar una a dos semanas, ya que es fácil recolectar la información necesaria y existen los elementos para realizarlo en poco tiempo. Sin embargo, en algunas empresas, contadas por cierto, este tiempo puede ser mayor debido a que el cambio de ubicación de las estaciones de trabajo puede requerir cimentaciones o instalaciones especiales.

Lista de 3 fases del proyecto (numeradas con círculos naranjas):
1. Antes de las mejoras
2. Durante de las mejoras
3. Después de las mejoras

**Imagen (derecha):** render isométrico de una línea de producción automatizada con brazos robóticos amarillos/naranjas dispuestos alrededor de una cinta transportadora en forma de óvalo/pista, con distintas estaciones de trabajo (máquinas con paneles de control) en los extremos — ilustra una célula de manufactura automatizada compleja.

## Slide 5

**Implementar Celdas de Trabajo — 1: Antes de las mejoras.**

Recuadro verde claro con lista numerada (1-4):
1. Establecer el objetivo, alcance y documentación del proyecto
2. Dibujar el plano actual del sistema de producción.
3. Formar el equipo
4. Realizar capacitación sobre Lean y manufactura celular.

## Slide 6

**Implementar Celdas de Trabajo — 2: Durante de las mejoras.**

Recuadro amarillo claro con lista numerada (1-6, resumen de todo el paso 2):
1. Realizar un diagrama spaghetti
2. Dibujar el mapa de valor actual
3. Hacer un análisis de mudas y detectar oportunidades.
4. Determinar el tiempo tack (takt) y el número de operadores.
5. Dibujar el mapa de valor futuro.
6. Diseño e implementar la nueva célula.

## Slide 7

**Implementar Celdas de Trabajo — 2: Durante de las mejoras** (foco en puntos 1 y 2: diagrama spaghetti y mapa de valor actual).

**Imagen izquierda — Diagrama spaghetti:** plano arquitectónico (layout) de una planta/cocina con múltiples líneas de colores (roja, magenta, azul) trazando los recorridos cruzados y enredados que sigue el material/operador entre estaciones (etiquetas visibles: "Fridge", "COAD", "Collection Room Cut-Out", "From Collection Room") — ilustra el desorden de movimientos antes de la mejora.

**Diagrama derecho — Mapa de Valor (VSM) actual:** flujo tipo Value Stream Mapping:
- Arriba a la izquierda: "Proveedor" → conectado a "Control de Producción / MRP" (recibe "Pronóstico Semanal" y "Pronóstico de 30 Días").
- Arriba a la derecha: "Demanda del Cliente: 700 piezas por Día (Takt Time 38.6 segundos)" → "Cliente" (recibe "Orden Diaria").
- "Control de Producción/MRP" → "Programación Diaria" → distribuye a 4 procesos en secuencia: **Aplicación de Crema de Maní** (700 pzs, Total C/T = 25s) → **Aplicación de Mermelada** (359 pzs, Total C/T = 30s) → **Empaque** (486 pzs, Total C/T = 42s) → **Envío** (128 pzs) → Cliente.
- Cada proceso tiene un triángulo amarillo de advertencia (inventario/problema) entre estaciones.
- Línea de tiempo inferior (escalera): 1 día / 0.513 días / 0.694 días / 0.183 días de espera, alternados con tiempos de proceso de 25s / 30s / 42s.
- Métricas resumen a la derecha: PLT = 2.39 días, VA/T = 97 s, PCE = 0.15%.

## Slide 8

**Implementar Celdas de Trabajo — 2: Durante de las mejoras** (foco en puntos 3 y 4: análisis de mudas y tiempo takt).

Recuadro amarillo:
3.- Hacer un análisis de mudas y detectar oportunidades.
4.- Determinar el tiempo tack y el número de operadores.

**Diagrama izquierdo — "7 MUDAS":** ícono central de bote de basura rodeado de 7 iconos circulares (rueda) representando los 7 desperdicios Lean: Movimientos, Defectos, Sobreproducción, Sobreprocesamiento (parcialmente ilegible), Inventario, Espera, Transportación.

**Tabla derecha — datos de cálculo de takt time:**

| Concepto | Valor | Unidad |
|---|---|---|
| Demanda del cliente | 3.400 | unidades/mes |
| Día de trabajo (8h x 60 min.) | 480 | minutos/día |
| Días laborables de un mes | 19 | días |
| Pausas de descanso [1(30min)+2(10min)] | 50 | minutos/día |
| Disponibilidad de las máquinas | 85% | — |
| Porcentaje actual del ratio de scrap | 3% | — |

Fórmula debajo (en LaTeX):
$$TAKT = \frac{[480\,\text{min} - 50\,\text{min}](0.85)}{\left\lceil \frac{3.400}{19} \right\rceil (1.03)} = \frac{365.5}{184.3} \approx 2\ \text{min/Ud.}$$

## Slide 9

**Implementar Celdas de Trabajo — 2: Durante de las mejoras** (foco en puntos 5 y 6: mapa de valor futuro e implementación de la célula).

Recuadro amarillo:
5.- Dibujar el mapa de valor futuro.
6.- Diseño e implementar la nueva célula.

**Diagrama izquierdo — Mapa de Valor Futuro (VSM futuro):** dentro de un recuadro punteado verde etiquetado "Flujo de información" arriba y "Flujo de materiales" abajo:
- "Proveedor" (pedido semanal) y "Cliente" (pedido mensual) conectados a "Production control" en la parte superior.
- Camión "Semanal" entrega material al Proceso A; camión "Mensual" recoge de "Entrega".
- Secuencia de 4 cajas de proceso conectadas con flechas: **Proceso A** (C/T=300 sec, C/O=60 min, Uptime=60%, 2 Shifts, 27000 sec available) → **Proceso B** (C/T=45 sec, C/O=10 min, Uptime=60%, 2 Shifts, 27000 sec available) → **Proceso C** (C/T=300 sec, C/O=240 min, Uptime=100%, 2 Shifts, 27000 sec available) → **Entrega**.
- Triángulos amarillos de advertencia (inventario) entre cada proceso con cantidades (ej. 1203, 1292, 233, 599 unidades).
- Línea de tiempo inferior tipo escalera: 6 días / 4 días / 1 día / 3 días de espera y 300 sec / 45 sec / 240 sec de procesamiento, con total "Tiempos que añaden y no añaden valor" y "Production lead time = 14 days" / "Processing time = 585 sec".

**Imagen derecha:** fotografía/render de una célula de manufactura en forma de "U" con 3 estaciones (una máquina roja, una verde, una gris con pantalla), dos operadores trabajando, cajas de material en el centro, y una flecha roja trazando el recorrido en U del flujo de trabajo. Pie de imagen: "Fig.21. Ejemplo de proceso en 'U' — AulaFacil.com".

## Slide 10

**Implementar Celdas de Trabajo — 2: Durante de las mejoras – Otros aspectos.**

Dos recuadros amarillos lado a lado:

Izquierda (aspectos generales):
1.- Planear cómo se moverán los materiales.
2.- Establecer las cantidades de material por tener en el proceso.
3.- Analizar las condiciones de ergonomía y seguridad.

Derecha, titulado "ERGONOMIA":
1.- Estatura.
2.- Espacio de disposición.
3.- Posicionamiento de materiales.
4.- Trabajo arriba del Corazón.
5.- Campos visuales.
6.- Iluminación.
7.- Ajustes de posiciones.

## Slide 11

**Implementar Celdas de Trabajo — 3: Después de las mejoras.**

Recuadro verde con lista de acciones (a-i):
a. Dar seguimiento a las actividades
b. Preparar las instalaciones de Servicios antes de mover equipos.
c. Dar a conocer al equipo las nuevas reglas de trabajo.
d. Capacitar continuamente al personal en herramientas Lean.
e. Realizar una reunión al inicio de cada turno para ver metas
f. Crear tableros de seguimiento de la producción
g. Escoger a un líder de célula que opere
h. Evaluar constantemente las oportunidades de mejora
i. Establecer un sistema de incentivos

## Slide 12

**ESTANDARES DE TRABAJO** (nueva sección, título en teal en la esquina superior izquierda).

Recuadro verde claro: "Para entender el trabajo estándar no hace falta más que observar (midiendo) el trabajo de los operadores. El trabajo estándar se compone de tres elementos:"

Lista de 3 elementos:
- Tiempo tack (rapidez de la demanda).
- Secuencia estándar de las operaciones.
- Inventario estándar en proceso.

Recuadro verde claro inferior — 5 documentos del trabajo estándar:
1.- "Hoja de medición de tiempos".
2.- "Capacidad de operación".
3.- "Tabla combinada de operaciones estandarizadas".
4.- "Trabajo estándar".
5.- "Instrucciones de operación".

## Slide 13

**ESTANDARES DE TRABAJO — HOJA DE MEDICIÓN – EMPRESA PELOTITAS.**

Texto: En la hoja de medición de tiempos se identifica el momento en que inicia un elemento del trabajo, así como el momento en que termina. En esta hoja se mide cada elemento del trabajo y se establecen los tiempos estándar para cada operación del proceso.

**Tabla/formato "Hoja de medición de tiempos" (reproducida):**

| Descripción del elemento | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | F | Suma | Prom. | TN | SUPL. | T. STD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (elemento 1) V |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (elemento 1) To |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (elemento 1) Tn |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ... (patrón V/To/Tn se repite para 5 elementos, todas las celdas vacías — es una plantilla en blanco) | | | | | | | | | | | | | | | | |

(Marca de agua "lawebdelingenieroindustrial" visible sobre la tabla).

## Slide 14

**ESTANDARES DE TRABAJO — HOJA DE TRABAJO STANDARD – EMPRESA PELOTITAS.**

Texto: Se presenta el diseño del proceso (layout) con el operador y el flujo del material, para establecer los movimientos más eficientes de acuerdo con las operaciones estáticas y dinámicas; se pueden observar las distancias; y, en general, se analizan las operaciones en grupo.

**Diagrama de layout de estación de trabajo:** distribución en planta de las estaciones (recuadros rotados en perspectiva) — "Material", "Welding Nut 1", "Welding Nut 2", "Rivet Flange 1", "Rivet Flange 2", "Completed Parts", "Quality Control" — conectadas por un flujo numerado del 1 al 7 en círculos: 1→2→3→4 (hacia Rivet Flange 1), 4→5 (baja hacia Rivet Flange 2), 5→6→7, y 7 vuelve punteado hacia 1 (ciclo del operador). Representa el recorrido estándar del operador entre puestos de soldadura de tuercas, remachado y control de calidad.

## Slide 15

**METODOLOGÍA TPM — INSTRUCTIVOS DE TRABAJO – EMPRESA PELOTITAS.**

Texto: Deben ser realizadas por los ingenieros de procesos o líderes de la cadena de valor de manera que cada paso del proceso se entienda adecuadamente y que cualquier operador entienda rápida y claramente cada paso de su operación. Es una ayuda visual del proceso.

**Infografía "Durante la actividad" (captura tipo infografía circular numerada 1-7), pasos de un protocolo de entrega/reparto con medidas sanitarias:**
1. Entregar el pedido directamente al cliente en la puerta de ingreso al domicilio o condominio.
2. Pago POS: Desinfectar la tarjeta, el POS y el lapicero utilizados durante el pago.
3. Pago en efectivo: Recibir el efectivo considerando las medidas preventivas sanitarias.
4. Evitar tocarse la boca, nariz y ojos.
5. Desinfectar las manos y el dispositivo móvil después de cada uso (no manipular la mascarilla).
6. Verificar que el cliente utilice mascarilla para realizar la entrega (indicando distancia de "2 metros" entre repartidor y cliente en la ilustración central).
7. Desinfectar las manos antes de continuar con el reparto.

Ilustración central: repartidor entregando un paquete a un cliente frente a una puerta, ambos con mascarilla, señal de "2 metros" de distancia.

## Slide 16

**METODOLOGÍA TPM — EMPRESA PELOTITAS — Consideraciones sobre la implementación del TRABAJO STANDARD.**

Recuadro verde con lista numerada (1-3):
1.- La documentación del trabajo estándar constituye documentos vivos, por lo que se debe revisar y validar continuamente.
2.- Estos documentos deben considerarse en la implementación: Eventos kaizen, Manufactura celular, SMED, TPM, Kanban, Mejoras ergonómicas y de seguridad.
3.- Estos documentos se deben realizar siempre con la colaboración de los operadores.

**Imagen (derecha):** fotografía decorativa de 5 trabajadores de construcción/obra con cascos amarillos y herramientas, posando sonrientes — ilustra al personal operativo, sin contenido técnico adicional.
