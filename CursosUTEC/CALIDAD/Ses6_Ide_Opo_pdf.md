---
curso: CALIDAD
titulo: Ses6_Ide_Opo
slides: 19
fuente: Ses6_Ide_Opo.pdf
---

## Slide 1
Portada (decorativa: fondo cian, foto edificio UTEC, logo UTEC, "Reinventa el mundo").
Título: "Identificación de problemas y oportunidades de mejora".

## Slide 2
Slide "Objetivo" (fondo cian). Texto entre corchetes decorativos:
"Aprender diferentes formas de identificar problemas y oportunidades".

## Slide 3
Slide "Contenido de sesión aquí" (fondo cian). Tres bloques numerados con corchetes:
- 01. Mapa de Procesos
- 02. Diagrama DOP y DAP
- 03. Elaborar SIPOC

## Slide 4
Título: "/ 1 Mapa de Procesos".
Sección "CLASIFICANDO PROCESOS" con 3 ítems numerados (círculos verdes):
1. **MACROPROCESO**: proceso mayor que involucra más de una función en la estructura organizacional, con impacto significativo en cómo funciona la organización.
2. **PROCESO CLAVE**: procesos que inciden significativamente en los objetivos estratégicos y son críticos para el éxito del negocio.
3. **SUBPROCESO**: cuando un proceso es tan complejo que debe diagramarse al nivel de actividad, se divide en subprocesos; útil para aislar problemas y posibilitar diferentes tratamientos dentro de un mismo proceso.

## Slide 5
Título: "/ 1 Mapa de Procesos".
Diagrama "CLASIFICANDO PROCESOS (EJEMPLO 1)": jerarquía de 3 niveles con flechas hacia abajo, tipo pirámide:
- **Macroproceso** (barra verde-azulada) → "Proceso de producción y ejecución del servicio"
- flecha verde hacia abajo →
- **Proceso** (barra naranja) → "Adquisición de los recursos necesarios"
- flecha naranja hacia abajo →
- **Subproceso** (barra verde lima), se despliega en 3 columnas: "Selección y certificación de proveedores" | "Compra de materiales y suministros" | "Adquisición de tecnologías"

## Slide 6
Título: "/ 1 Mapa de Procesos".
Diagrama sobre fondo negro "MAPA DE PROCESOS": a la izquierda un esquema con recuadro "CLIENTE" a ambos lados de una cadena de 3 cajas (proceso general), que se descompone en dos niveles más de detalle mediante líneas punteadas: un conjunto de cajas conectadas con flechas rojas (nivel de "conjunto de procesos") y luego otro subconjunto más detallado (nivel de "proceso de análisis"). A la derecha, 3 flechas grandes apuntan a 3 cajas de color:
- Azul oscuro: "Mapa de Procesos de la Organización"
- Verde: "Mapa de un conjunto de procesos"
- Dorado: "Mapa del Proceso de Análisis para el proyecto"

## Slide 7
Título: "/ 2 DOP – Diagrama de Operaciones del Proceso".
Texto: "Es una representaciones gráficas, que mediante simbologías normalizadas, registran la secuencia de las operaciones y las inspecciones de un proceso de elaboración de un producto o de la prestación de un servicio."
Diagrama a la derecha: "DIAGRAMA DE OPERACIONES DEL PROCESO DE YOGURT" — flujo vertical numerado del 1 al 13 con entradas laterales:
- Entra "LECHE FRESCA" → (1) Recepción → (2) Medición de volumen → (3) Filtrado [cuadro] → sale "IMPUREZAS"
- Entra "AZÚCAR BLANCA" → (4) Pasteurización 85°C / Adición de azúcar blanca → (5) [cuadro] → (6) Homogenizado
- Entra "CULTIVO LÁCTICO" → (7) Enfriamiento a 45°C / Inoculación → (8) [cuadro] → (9) Inoculación 43°C–44°C → (10) Refrigeración 4°C–10°C
- Entra "COLORANTE Y SABORIZANTE" → Adición de colorantes y saborizantes → (11) → (12) [cuadro] Envasado → (13) Etiquetado → Almacenamiento
(círculos = operación, cuadrados = combinación operación-inspección; flechas indican entrada de insumos al proceso principal)

## Slide 8
Título: "/ 2. DAP – Diagrama de Actividades de un proceso".
Texto: "Contiene muchos más detalles que el DOP. Es particularmente útil para poner de manifiesto costos ocultos como pueden ser distancias recorridas, retrasos y almacenamientos temporales."
Tabla de simbología DAP:

| Actividad | Símbolo | Descripción |
|---|---|---|
| Operación | Círculo | Indica las principales fases del proceso, método o procedimiento. |
| Inspección | Cuadrado | Indica que se verifica la calidad y/o cantidad de algo. |
| Transporte | Flecha | Indica desplazamiento o movimiento de empleados, material y equipo de un lugar a otro. |
| Espera | Forma tipo "D" | Indica demora en el desarrollo de los hechos. |
| Almacenamiento | Triángulo invertido | Indica el depósito de un documento o información dentro de un archivo, o de un objeto cualquiera dentro de un almacén. |

## Slide 9
Título: "/ 2. DAP – Diagrama de Actividades de un proceso".
Encabezado del DAP (tabla rosa/celeste):
- Proceso: Despacho de mercadería
- Sujeto de la gráfica: Proceso de Despacho
- Principio: Verificación stock físico-sistema
- Final: Asignación de transporte

Tabla resumen de actividades:

| Actividad | Símbolo | Número | Tiempo | Distancia |
|---|---|---|---|---|
| Operación | círculo | 18 | 889.07 | |
| Transporte | flecha | 1 | 30.00 | |
| Inspección | cuadrado | 10 | 302.20 | |
| Retraso | forma D | 0 | 0.00 | |
| Almacenaje | triángulo | 0 | 0.00 | |
| **TOTAL** | | **29** | **1221.27** | |

Nota: 20.35 horas (equivalente del tiempo total).

## Slide 10
Título: "/ 2. DAP – Diagrama de Actividades de un proceso".
Dos indicadores calculados sobre fondo rosado, resaltados en amarillo:
- **LEAN** = Operaciones que generan valor / Tiempo total = 934.00 / 1221.27 = **76%**
- **% de Utilización** = 4/6 = **58%**

Además:
- **Cuello de Botella**: Verificación stock físico-sistema; Analizar línea 2; Depuración cli 2.
- **Fábricas Ocultas**: Recepción de MP; Inspección Sensorial (Enfriado); Cerrado de Tapa.

## Slide 11
Título: "/ 3. SIPOC – Matriz de Caracterización del Proceso".
Diagrama sobre fondo negro "ELABORACIÓN DEL SIPOC" — subtítulo "SIPOC (Suppliers – Inputs – Process – Outputs – Customers)". 5 pasos numerados en franjas de color:
1. (naranja) Definir el proceso y sus límites.
2. (gris) Identificar los resultados del proceso, incluyendo datos, servicios, productos, información, registros, etcétera.
3. (amarillo) Para cada salida identificada, identificar todas las entradas asociadas.
4. (azul) Registrar los clientes internos y externos que reciben las salidas identificadas.
5. (verde) Volver a la columna de proveedor para identificar a los proveedores internos y externos para cada entrada identificada.

## Slide 12
Título: "/ 3. SIPOC – Matriz de Caracterización del Proceso".
Diagrama "EJEMPLO DE SIPOC" sobre fondo negro, con 5 columnas encabezadas en rojo: Proveedor | Entradas | Proceso | Salidas | Clientes.
- Proveedor: Cliente; Comerciantes
- Entradas: Información de problemas; Información de transacciones; Históricos de la cuenta
- Proceso (flujo de cajas naranjas con flechas): Investigar → Recopilar Datos → Análisis de Problema → Documentar → Presentar Informe → Corrección (las flechas forman un ciclo: Investigar→Recopilar Datos→Análisis de Problema→Documentar, y Documentar→Presentar Informe→Corrección→vuelve a Documentar)
- Salidas: Investigaciones; Informe; Resultados
- Clientes: Sucursal de cliente; Cliente

Nota en amarillo/cursiva: "Siempre que sea posible, colocar las entradas y salidas en su forma 'tangible'. Ej: Reportes, productos, etc. Hacerlo facilita su medición más adelante."

## Slide 13
Título: "/ 3. SIPOC – Matriz de Caracterización del Proceso".
Diagrama "CLASIFICACION DE ENTRADAS Y SALIDAS" sobre fondo negro. Texto: "Identificar: Actividades del proceso, Entradas -Proveedores, Salidas -Clientes".
Diagrama de flujo (fondo amarillo pálido) con forma "INICIO" → caja → caja → caja, con entradas etiquetadas E1, N1, C1 llegando a las primeras cajas; luego un rombo (decisión) que recibe C2 y se ramifica: una rama va a una caja con entradas E3/E4 → caja con entrada N2 → caja, que se une con otra rama (caja con entrada E2 → rombo con entrada X3) → caja final con entrada C3/E5 → salidas S1, S2 → "FIN".
Abajo: gráfico pequeño tipo serie temporal (línea con puntos) → flecha roja → ícono de bolsa de dinero verde, con anotación: "C, N y E son Entradas al proceso y S son Salidas".

## Slide 14
Título: "/ 3. SIPOC – Matriz de Caracterización del Proceso".
Diagrama "CLASIFICACION DE ENTRADAS Y SALIDAS" (repetición del proceso de la slide 13, mismo diagrama de flujo con recuadro amarillo), pero ahora con etiquetas agrupadas:
- Arriba: "Variables de Ruido o no controlables (N)" → N1, N2, N3 entran al proceso.
- Izquierda: "Variables Controlables" → C1, C2 entran al proceso.
- Abajo: "Variables experimentales (E)" → E1, E2, E3, E4 entran al proceso.
- Derecha: salidas S1, S2 → "Características de calidad (Y)".
- Fórmula: **Y = f(X1, X2, ..., Xn)**
- Recuadro verde: "Entiende las 'X' (KPIV) y controlarás las 'Y' (KPOV)"

Tabla inferior:

| Código | Nombre | Descripción |
|---|---|---|
| C | Entrada controlable | Aquella que puede ser controlada |
| N | Entrada ruidosa | Es impredecible, altera el proceso. No es controlable por el momento. |
| E | Entrada experimental | Aquella que puede ser estudiada bajo diversos parámetros para ver su comportamiento en el proceso. |
| S | Salida | Según donde impactan se suelen clasificar en: CTQ (críticas para la calidad), CTD (críticas para la entrega), CTC (críticas para el costo). |

Llaves indican: C, N, E agrupan como "X" (KPIV); S agrupa como "Y" (KPOV).

## Slide 15
Título: "/ 3. SIPOC – Matriz de Caracterización del Proceso".
Diagrama "ANÁLISIS DE VALOR" sobre fondo negro — mismo esquema de flujo con Variables de Ruido (N), Variables Controlables (C1, C2), Variables experimentales (E1-E4) entrando al proceso y salida "Características de calidad (Y)", recuadro verde "Entiende las 'X' (KPIV) y controlarás las 'Y' (KPOV)".
Tabla inferior:

| Código | Nombre | Descripción |
|---|---|---|
| VA | Operación con Valor agregado | Valor agregado son las características dadas a aquellas operaciones indispensables por las cuales el cliente está dispuesto a pagar |
| NA | Operación de no Valor agregado | No generan valor (pero sí generan costos) |

## Slide 16
Título: "/ 3. SIPOC – Matriz de Caracterización del Proceso".
Diagrama "Eliminar la fábrica oculta" (fondo blanco). Flujo: "Requisitos de entrada" → "Ejecución del Producto" → rombo "Inspección" → si OK → globo de diálogo "Yield 90%"; si NO OK → "Retrabajo / Rechazo" (marcado con banda roja "Eliminar") → vuelve a "Ejecución del Producto". El camino de retrabajo/rechazo está resaltado con línea naranja y etiquetado abajo como "Fábrica oculta".

## Slide 17
Título: "/ 3. SIPOC – Matriz de Caracterización del Proceso".
Diagrama de flujo genérico (fondo beige) igual estructura que en slides 13-15: INICIO → cajas → rombos → cajas → FIN, con varias cajas resaltadas con óvalos magenta y etiquetadas "INFO" (aparecen 3 veces: junto al inicio, en medio del flujo inferior, y cerca del final antes de FIN).
Tabla inferior: **INFO** = "Etapas donde se registran datos del proceso".

## Slide 18
Slide "Conclusiones". Dos puntos numerados:
1. Conocer las principales herramientas para identificar problemas
2. Aprenderás a definir indicadores que te ayuden a definir problemas

## Slide 19
Slide de cierre — decorativa: fondo cian con patrón de hexágonos, logo UTEC grande centrado ("UTEC — Universidad de Ingeniería y Tecnología") y cruz dorada decorativa. Sin contenido textual adicional.
