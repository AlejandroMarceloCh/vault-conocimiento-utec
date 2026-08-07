---
curso: FUNDOPS
titulo: F5-S6 Cuello de Botella y Dimensionamiento (Version2)
slides: 35
fuente: F5-S6 Cuello de Botella y Dimensionamiento (Version2).pdf
---

## Slide 1

Portada decorativa (foto edificio UTEC, logo UTEC). Texto: "FUNDAMENTOS DE OPERACIONES" / "Semana 6 - Dimensionamiento de Operaciones".

## Slide 2

Slide de índice, con foto decorativa lateral (estructura de concreto). Texto:
"Índice:"
1. Cuello de Botella
2. Dimensionamiento de Operaciones
3. Criterio Económico para el dimensionamiento

## Slide 3

Slide de objetivos, con foto decorativa lateral. Texto:
"Objetivos: Al finalizar esta sesión, deberás ser capaz de:"
1. Identificar y analizar cuellos de botellas en las operaciones.
2. Determinar la capacidad productiva de una operación por criterio económico.
3. Calcular la eficiencia, aprovechamiento de material y costos de producción.

## Slide 4

Slide separador de sección "1. Cuello de Botella" sobre foto decorativa de estructura de concreto (azul).

## Slide 5

**PRODUCCIÓN POR PRODUCTO**

Texto: Cuando nos enfrentamos a una distribución por producto, la capacidad queda determinada por el CUELLO DE BOTELLA de la línea. Ejemplo: La capacidad de la línea está determinada por la máquina 3.

Diagrama: 4 cajas en línea (P1, P2, P3, P4) representando un proceso en serie, con P3 resaltado con un recuadro rojo (cuello de botella). Tabla de tiempos/flow rate debajo de cada caja:

| | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| T. Unitario | 0.5' | 1' | 2' | 1' |
| Flow Rate | 120 und/hr | 60 und/hr | 30 und/hr | 60 und/hr |

P3 (30 und/hr) es el cuello de botella (menor flow rate).

## Slide 6

**PRODUCCIÓN POR PRODUCTO** (continuación)

Texto: Sin embargo, existe un factor importante a considerar: EL NÚMERO DE MÁQUINAS de cada tipo que existen en la línea puede hacer variar el cuello de botella y por lo tanto la capacidad.

Diagrama: 4 procesos en línea (P1→P2→P3→P4), cada uno con N máquinas del tipo correspondiente encima (M1, M2, M3 M3 M3, M4 M4). P2 resaltado con recuadro rojo. Tabla:

| | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| T. Unitario x maq | 0.5' | 1' | 2' | 1' |
| C. Máquinas | 1 | 1 | 3 | 2 |
| Flow Rate | 120 und/hr | 60 und/hr | 90 und/hr | 120 und/hr |

Al multiplicar el flow rate individual por el número de máquinas, ahora P2 (60 und/hr, con solo 1 máquina) pasa a ser el nuevo cuello de botella, en vez de P3 (que con 3 máquinas en paralelo sube a 90 und/hr).

## Slide 7

**PRODUCCIÓN POR PROCESO**

Texto: Cuando nos enfrentamos a una distribución por proceso, la pregunta es ¿Cuál es la capacidad de producción de cada sección?, podríamos pensar en determinar la capacidad en función de cada producto pero tendríamos tantas capacidades como productos se fabriquen.

Tabla (4 procesos P1-P4, 3 productos), con tiempo unitario y flow rate por combinación producto-proceso:

| Prod. | | P1 | P2 | P3 | P4 |
|---|---|---|---|---|---|
| Prod. 1 | T. Unitario | 0.5' | 1' | 2' | 1' |
| | Flow Rate | 120 und/hr | 60 und/hr | 30 und/hr | 60 und/hr |
| Prod. 2 | T. Unitario | 0.25' | 1' | 2.5' | 2' |
| | Flow Rate | 240 und/hr | 60 und/hr | 15 und/hr | 30 und/hr |
| Prod. 3 | T. Unitario | 1' | 1' | 1' | 2' |
| | Flow Rate | 60 und/hr | 60 und/hr | 60 und/hr | 30 und/hr |

## Slide 8

**PRODUCCIÓN POR PROCESO** (continuación)

Texto: Lo más aconsejable es expresar la capacidad en función del MIX de producción de la sección, estableciendo para ello equivalencias.

Tabla con mix ponderado por porcentaje de cada producto (P3 resaltado con recuadro rojo):

| | | P1 | P2 | P3 | P4 |
|---|---|---|---|---|---|
| Prod. 1 (70%) | T. Unitario | 0.5' | 1' | 2' | 1' |
| Prod. 2 (20%) | T. Unitario | 0.25' | 1' | 2.5' | 2' |
| Prod. 3 (10%) | T. Unitario | 1' | 1' | 1' | 2' |
| MIX | T. Unitario | 0.5' | 1' | 2' | 1.3' |
| | Flow Rate | 120 und/hr | 60 und/hr | 30 und/hr | 46 und/hr |

Nota en azul: "Para el proceso P1: El tiempo unitario se obtiene de la siguiente forma (70% x 0.5 min) + (20% x 0.25min) + (10% x 1 min) = 0.5 min y con esto se obtiene 120 unid/hora"

Fórmula del tiempo unitario ponderado por mix: $T_{unit} = \sum_i (\%_i \times T_i)$

## Slide 9

Slide separador de sección "2. Dimensionamiento de Operaciones" sobre foto decorativa de estructura de concreto (azul).

## Slide 10

**DIMENSIONAMIENTO DE OPERACIONES**

Texto (bullets):
- ¿Cuál debe ser el espacio comercial de mi tienda?
- ¿Cuántos agentes bancarios debería tener mi agencia?
- ¿Cuánto personal de enfermería debería atender en la sala de emergencias?

Una forma estandarizada de verlo: Capacidad máxima de procesamiento de productos en una planta.

Unidades: productos u órdenes por unidad de tiempo.

## Slide 11

**CRITERIOS DE DIMENSIONAMIENTO**

Texto: Definir cuál debería ser la capacidad productiva de una operación.
1. Criterio económico: escoger la alternativa que minimiza el costo medio unitario o el valor presente del proyecto máximo.
2. Criterio de servicio: escoger aquella que brinda un nivel de servicio aceptable.

## Slide 12

Slide separador de sección "3. Criterio Económico" sobre foto decorativa de estructura de concreto (azul).

## Slide 13

**CRITERIOS ECONÓMICO**

Texto: "1. Economías de escala a corto plazo" (resaltado en amarillo). Sub-bullets bajo "Economías de escala":
- Utilización de activos / menos cambios (set-up)
- Efectos de aprendizaje (velocidad, calidad)
- Se diluyen los costos fijos

Gráfico: curva de "Costo Unitario Promedio" (eje Y) vs "Velocidad: Trabajos/hora" (eje X), con forma de U (curva de costo medio de corto plazo). Flecha roja apuntando hacia abajo-derecha sobre el tramo descendente de la curva, indicando la zona donde el costo baja por economías de escala. Se marca "Costo Mínimo" en el punto más bajo de la curva.

Dos fotos decorativas: línea de producción con trabajadoras empacando productos (planta industrial), y trabajadoras ensamblando placas electrónicas en línea de montaje.

## Slide 14

**CRITERIOS ECONÓMICO** (continuación, dis-economías de escala)

Texto (bullets):
- Dis-economías de escala
- Búsqueda toma más tiempo
- Tasa mayor de fallas & ausentismo
- Errores de calidad
- Trabajo en horas extras
- Trabajo tercerizado
- Ineficiencia en comunicación (burocracia)

Mismo gráfico de "Costo Unitario Promedio" vs "Velocidad: Trabajos/hora" en forma de U, pero ahora la flecha roja apunta hacia arriba-derecha sobre el tramo ascendente de la curva (después del costo mínimo), indicando la zona de dis-economías de escala.

Tres imágenes decorativas: plano/layout de planta de producción de chocolate (túnel de frío, cuarto central, área de moldeado, máquina bañadora de chocolate, almacén intermedio), foto de maquinaria antigua con etiqueta "DEFECT" colgando, y fotos de estantes de almacén desordenados con cajas y materiales.

## Slide 15

**RELACIONES DE COSTOS**

Texto: El costo marginal es el costo incremental necesario para producir una unidad adicional. Asumiendo que son variables derivables, se tiene que el costo promedio unitario es mínimo cuando este es igual [al costo marginal].

Fórmulas (LaTeX):

$$CMg = \frac{dCT}{dq}$$

$$\frac{d\left(\frac{CT}{q}\right)}{dq} = \frac{\frac{dCT}{dq}q - CT}{q^2} \;\;\Rightarrow\;\; 0 = \frac{dCT}{dq}q - CT$$

$$\frac{CT}{q} = \frac{dCT}{dq}$$

(Deriva que el costo promedio es mínimo cuando el costo marginal iguala al costo promedio, CMg = CT/q).

## Slide 16

**RELACIONES DE COSTOS (CORTO PLAZO)**

Dos gráficos lado a lado:
1. "Finding Minimum Avg Cost": eje Y en S/ (0 a 1,000), eje X "Quantity" (0-160). Dos curvas: "Marginal Cost Curve" (azul, forma de U pronunciada, mínimo cerca de q=80 en costo ≈S/0) y "Avg Medium Cost Curve" (naranja, forma de U más suave, mínimo cerca de q=120 en costo ≈S/230-250). Las curvas se cruzan cerca de q=120, donde el costo marginal iguala al costo promedio (consistente con la fórmula de la slide anterior).
2. "Total cost vs. quantity produced": eje Y en S/ (0 a 50,000), eje X "quantity units" (0-140). Curva de costo total con forma de S (crece rápido al inicio, se aplana entre q=60-100, luego vuelve a crecer fuertemente después de q=100 hacia S/37,000 en q=140).

## Slide 17

**RELACIONES DE COSTOS (LARGO PLAZO)**

Texto: Opciones diferentes para diferentes requerimientos de demanda.

Diagrama: envolvente de curvas de costo unitario promedio de corto plazo (forma de "U" cada una) para 4 tamaños de operación: "operación reducida", "operación mediana", "operación grande" (encerrada en óvalo rojo), "operación muy grande". Eje Y = "Costo unitario promedio", eje X = "Velocidad: Trabajos/hora". Flecha "Decisión óptima" apunta al punto más bajo de la curva de "operación grande" (el punto óptimo de la envolvente de largo plazo). Flecha "Curva de largo plazo de economías" apunta a la curva envolvente completa que conecta los mínimos de todas las curvas de corto plazo.

## Slide 18

**EJEMPLO DE DIMENSIONAMIENTO**

Texto: Tenemos una empresa que fabrica 3 válvulas: X106, X107 y X108. Su principal insumo es el acero galvanizado y tiene 3 potenciales dimensiones de planta con diferente tamaño.

Para una determinada demanda:
1. ¿Qué dimensión de planta sería elegida?
2. ¿Debería trabajarse en primer turno solamente o implementar horas extras y segundos turnos?

Ilustraciones decorativas: 3 iconos de fábrica de tamaño creciente, etiquetadas "Planta Pequeña A - Semi-automática", "Planta Mediana B - Semi-automática", "Planta Grande C - Semi-automática".

## Slide 19

**ANÁLISIS DE CUELLO DE BOTELLA**

Metodología en 3 pasos con sus fórmulas:

1. Definir lotes promedio. Variables: $i$ = índice de producto ($i=1,2...n$), $D_i$ = demanda anual de producto $i$, $Q_i$ = lote promedio de producto $i$, $Q$ = lote promedio.

$$Q = \frac{\sum_{i=1}^{n} D_i}{\sum_{i=1}^{n} \frac{D_i}{Q_i}}$$

2. Analizar tasa de producción por paso (aproximado). Variables: $u_j$ = tiempo unitario en tiempo regular de estación $j$, $s_j$ = tiempo de set-up de estación $j$, $Q$ = lote promedio, $r_j$ = tasa de producción de estación $j$ (Flow rate).

$$r_j = \frac{Q}{u_j Q + s_j}$$

Gráfico pequeño a la derecha "Flow Rate (units/min) vs. Batch Size": curva creciente cóncava que sube rápido al inicio (de 0.10 en batch~5 hasta 0.40 en batch~40) y luego se aplana asintóticamente cerca de 0.48-0.50 hacia batch=140. Ilustra que a mayor tamaño de lote, mayor flow rate, con rendimientos decrecientes (por el efecto relativo del set-up).

3. Identificar cuello de botella (para j sistemas en serie o paralelo):

$$r^* = \min_j \{r_j\}$$

## Slide 20

**ANÁLISIS DE CUELLO DE BOTELLA**

Texto: Ejemplo, 3 productos en metal mecánica.

Tabla:
| Productos | Demanda anual | Tamaño de Lotes |
|---|---|---|
| X105 | 300,000 | 8,000 |
| X106 | 95,000 | 5,000 |
| X107 | 145,000 | 6,000 |

Diagrama de proceso: flujo en serie "Habilitado De planchas" → "Armado" → "Soldado" (resaltado en rojo) → "Pintado", con una rama adicional "Fabricación de accesorios" que alimenta hacia "Soldado" (entra al proceso justo antes de la etapa de Soldado).

## Slide 21

**ANÁLISIS DE CUELLO DE BOTELLA**

Texto: y los siguientes tiempos de ejecución por etapa.

Tabla con datos de tiempo de ejecución (horas/unidad) y set-up (horas) por etapa, para las 3 plantas (A, B, C):

| | Habilitado | Armado | Soldado | Pintado | Accesorios | Línea |
|---|---|---|---|---|---|---|
| **Planta A** | | | | | | |
| T Ejecución | 0.002 | 0.002 | 0.003 | 0.005 | | |
| Set-up | 4 | 3 | 6 | 8 | | |
| T Ejecución (accesorios) | | | | | 0.004 | |
| Set-up (accesorios) | | | | | 4 | |
| **Planta B** | | | | | | |
| T Ejecución | 0.002 | 0.002 | 0.0025 | 0.0043 | | |
| Set-up | 4 | 3 | 7 | 10 | | |
| T Ejecución (accesorios) | | | | | 0.004 | |
| Set-up (accesorios) | | | | | 4 | |
| **Planta C** | | | | | | |
| T Ejecución | 0.002 | 0.002 | 0.0025 | 0.0033 | | |
| Set-up | 4 | 3 | 7 | 12 | | |

(La tabla continúa parcialmente cortada en la parte inferior de la slide para Planta C; los datos de accesorios de Planta C no son visibles.)

## Slide 22

**ANÁLISIS DE CUELLO DE BOTELLA**

Solo texto, repite el enunciado de pasos a seguir (slide de transición sin nuevos datos):
1. Estimar lotes de producción promedio
2. Identificar cuellos de botella y capacidad máxima productiva por planta.

## Slide 23

**ANÁLISIS DE CUELLO DE BOTELLA**

Texto: "1. Estimar lotes de producción promedio" (en negrita, paso activo).

Tabla con el cálculo del lote promedio (aplicando la fórmula de la slide 19):

| Productos | Demanda anual | Tamaño de Lotes | Lotes/año |
|---|---|---|---|
| X105 | 300.000 | 8.000 | 37,50 |
| X106 | 95.000 | 5.000 | 19,00 |
| X107 | 145.000 | 6.000 | 24,17 |
| **Suma** | **540.000** | | **80,67** |
| **Lote promedio:** | | **6.694,21** (resaltado en amarillo) | |

## Slide 24

**ANÁLISIS DE CUELLO DE BOTELLA**

Texto: "2. Identificar cuellos de botella y capacidad máxima productiva por planta." (en negrita, paso activo).

Tabla de resultados (aplicando la fórmula $r_j = Q/(u_jQ+s_j)$ para cada etapa y planta), con la etapa cuello de botella de cada planta resaltada en naranja en la columna "Línea":

| | Habilitado | Armado | Soldado | Pintado | Accesorios | Línea |
|---|---|---|---|---|---|---|
| **Planta A** | | | | | | |
| T Ejecución (horas/unidad) | 0,002 | 0,002 | 0,003 | 0,005 | 0,004 | **0,0050** |
| Set-up (horas) | 4 | 3 | 6 | 8 | 4 | **8** |
| Flow Rate (unidades/hora) | 384,98 | 408,47 | 256,65 | 161,42 | 217,51 | **161,42** |
| **Planta B** | | | | | | |
| T Ejecución | 0,002 | 0,002 | 0,0025 | 0,0043 | 0,004 | **0,0043** |
| Set-up | 4 | 3 | 7 | 10 | 4 | **10** |
| Flow Rate | 384,98 | 408,47 | 282,03 | 172,60 | 217,51 | **172,60** |
| **Planta C** | | | | | | |
| T Ejecución | 0,002 | 0,002 | 0,0025 | 0,0033 | 0,004 | **0,0033** |
| Set-up | 4 | 3 | 7 | 12 | 4 | **12** |
| Flow Rate | 384,98 | 408,47 | 282,03 | 196,36 | 217,51 | **196,36** |

Pintado es la etapa cuello de botella (menor flow rate) en las 3 plantas.

## Slide 25

**EFICIENCIA Y APROVECHAMIENTO DE MATERIAL**

Fórmulas (LaTeX):

$$Eficiencia = \frac{\text{Capacidad productiva según condición}}{\text{Máxima capacidad productiva}} \times 100\%$$

Anotación a la derecha: "Cap. Efectiva / Cap. Diseño".

$$Aprovechamiento = \frac{\text{Material aprovechado}}{\text{Material requerido estándar}} \times 100\% = (1-merma)\times 100\%$$

Anotaciones azules: numerador = "(Productos buenos)", denominador = "(Toda la producción)".

Notas:
1. Los valores permitidos de eficiencia y aprovechamiento van de 0 a 100%.
2. La condición se puede referir a trabajar en segundo turno por ejemplo en horas extras.
3. La medida de aprovechamiento puede incluir problemas sea por calidad (material descartado por defectos) o eficiencia en el aprovechamiento del material.

## Slide 26

**ESTIMACIÓN DE LA PRODUCCIÓN MÁXIMA**

Fórmula central (texto grande):

**Producción Máxima = Eficiencia x Horas Disponibles Anuales x Flow rate**

Texto: *La producción máxima se debe estimar para las horas disponibles para el 1er, 2do turno según corresponda.

## Slide 27

**ANÁLISIS DE EFICIENCIA**

Repite el mismo ejemplo y datos de la slide 20 (3 productos en metal mecánica, tabla de demanda/lotes X105/X106/X107, y el mismo diagrama de proceso Habilitado→Armado→Soldado(rojo)→Pintado con rama de Fabricación de accesorios entrando a Soldado). Es la introducción al análisis de eficiencia sobre el mismo caso.

## Slide 28

**LÓGICA DE USO DE CAPACIDAD**

Texto: Se usa primero la capacidad del turno más barato, luego se incluyen los restantes. Puede ser más barato obviar horas extras y usar capacidad de 2do turno primero.

Diagrama: analogía de "vasos que se llenan en cascada" — tres recipientes conectados en serie mostrando el orden de llenado de capacidad: "Capacidad de 1er turno" (lleno) → flecha hacia abajo → "Capacidad en horas extras" (parcialmente lleno) → flecha hacia abajo → "Capacidad de 2do turno" (vacío). Representa que se usa la capacidad más barata primero y el excedente "rebalsa" hacia la siguiente fuente de capacidad.

Supuesto (texto): Pagamos a destajo o pagamos solo las horas trabajadas en cada turno. Por ejemplo: si se trabajan 1.5 hr de 8 horas de segundo turno, puede ser equivalente a trabajar 1.5/8 x 24 días laborales = 3.93 días.

## Slide 29

**LÓGICA DE USO DE CAPACIDAD**

Diagrama de flujo (árbol de decisión) con 3 preguntas en cascada (rombos azules) para asignar la demanda entre 1er turno, horas extras y 2do turno:

1. ¿Demanda < Capacidad Máxima 1er turno?
   - Sí → $HR1erturno = \dfrac{Demanda}{Flow\,rate \times Eficiencia\,1er\,Turno}$
   - No → pasa a la siguiente pregunta

2. ¿Demanda < Capacidad Máxima 1er turno + Horas Extras?
   - Sí → $HRHoraExtra = \dfrac{Demanda - Cant.Prod.1erTurno}{Flow\,rate \times Eficiencia\,Hora\,extra}$, con $HR1erturno = Horas\,Disp.\,1er\,turno$
   - No → pasa a la siguiente pregunta

3. ¿Demanda < Capacidad Máxima 1er turno + Horas Extras + 2do turno?
   - Sí → $HR2doTurno = \dfrac{Demanda - Cant.Prod\,HR1erTurno - Cant\,Prod.HorasExtras}{Flow\,rate \times Eficiencia\,2do\,Turno}$, con $HRHoraextra = Horas\,Disp.\,HorasExtras$ y $HR1erturno = Horas\,Disp.\,1er\,turno$
   - No → "Infactible"

Nota lateral: *Nota: Aquí se asume que se puede trabajar horas extras en turnos a destajo. No se cobra por bloque. Se asume que se puede producir parcialmente por turnos.

## Slide 30

**CRITERIO ECONÓMICO**

Fórmulas de costos (texto):

Costo Total de Producción = Costo de Mano de Obra Directa + Costo de Materiales + Costo de Servicios y Administración + Costo de Implementación de 2do turno…

Costo de Producción Unitario = Costo Total de Producción / Producción Total

Costo de Mano de Obra Directa Horas Extras = Número de Horas extras Requeridas x (Costo por Hora) x (1+ Factor Costo Laboral) x (1+Suplemento Hora Extra)

Nota: Costo laboral incluye gratificaciones, vacaciones, seguros sociales, con enlace: https://excelnoconvencional.com/costos-laborales-peru-comparado-por-regimen-en-excel/

## Slide 31

**Datos de Eficiencia y Aprovechamiento**

Tabla "Cuadro de Datos - Eficiencias":

| Eficiencias | |
|---|---|
| **Planta A** | |
| Eficiencia 1 (1er turno) | 93% |
| Horas Extras | 86% |
| Eficiencia 2 (2do turno) | 70% |
| **Planta B** | |
| Eficiencia 1 (1er turno) | 94% |
| Horas Extras | 90% |
| Eficiencia 2 (2do turno) | 89% |
| **Planta C** | |
| Eficiencia 1 (1er turno) | 96% |
| Horas Extras | 92% |
| Eficiencia 2 (2do turno) | 91% |

Tabla "Aprovechamientos":

| Materiales | Aprovechamiento de material |
|---|---|
| Planta A | 0,94 |
| Planta B | 0,97 |
| Planta C | 0,98 |

## Slide 32

**Datos de Costos**

Datos:
- MOD: Mano de Obra Directa. Costo por hora Mano de Obra Directa: S/70,00. Recargo por beneficio sociales: 0,42. Recargo horas extras: 50%.
- Costo adicional: Implementar turno adicional: 25000.
- Costo de mantenimiento (Costo de servicios: Luz + Agua + [...]) por planta:

| | A | B | C |
|---|---|---|---|
| Costo de servicios | 80000 | 100000 | 160000 |

- Material: Kg de acero galvanizado: 35/unidad. Costo por kilo: S/0,023.

## Slide 33

**Solución**

Tabla "Semanas disponibles: 52" y "Horas disponibles":

| Horas disponibles | Semanales | Anuales | Acumulado |
|---|---|---|---|
| Turno 1 | 48 | 2.496 | 2.496 |
| Horas Extras | 12 | 624 | 3.120 |
| Turno 2 | 48 | 2.496 | 5.616 |

Tabla "Máxima producción" (por planta y tipo de turno, con producción máxima, tiempo unitario y producción acumulada):

| Tiempos | Producción Máxima | Tiempo Unitario | Prod Acumulada |
|---|---|---|---|
| Planta A - T. Regular | 374.698,45 | 0,01 | 374.698,45 |
| Planta A - H. Extra | 86.623,83 | 0,01 | 461.322,28 |
| Planta A - 2do Turno | 282.031,09 | 0,01 | 743.353,37 |
| Planta B - T. Regular | 404.955,12 | 0,01 | 404.955,12 |
| Planta B - H. Extra | 96.930,75 | 0,01 | 501.885,87 |
| Planta B - 2do Turno | 383.414,96 | 0,01 | 885.300,83 |
| Planta C - T. Regular | 470.518,69 | 0,01 | 470.518,69 |
| Planta C - H. Extra | 112.728,44 | 0,01 | 583.247,13 |
| Planta C - 2do Turno | 446.012,51 | 0,01 | 1.029.259,64 |

## Slide 34

**Solución** (continuación)

Tabla final de costos y costo unitario por planta:

| | Planta A | Planta B | Planta C |
|---|---|---|---|
| Costo de MO Directa | S/.496.204,80 | S/.496.204,80 | S/.496.204,80 |
| **Costo de Horas Extra** | **S/.93.038,40** | **S/.93.038,40** | **S/.93.038,40** |
| Costo de Materiales | S/.636.595,17 | S/.734.708,42 | S/.845.463,27 |
| Costo de Servicios y Adm. | S/.80.000,00 | S/.100.000,00 | S/.160.000,00 |
| Costo de Imple. de 2do turno | S/.25.000,00 | S/.25.000,00 | S/.25.000,00 |
| **Costo Total de Producción** | **S/.1.330.838,37** | **S/.1.448.951,62** | **S/.1.619.706,47** |
| **Costo de Producción Unitario** | **S/.1,79** | **S/.1,64** | **S/.1,57** |

Conclusión implícita: la Planta C tiene el menor costo unitario (S/.1,57), por lo que sería la elegida bajo el criterio económico pese a tener mayor costo total.

## Slide 35

Slide de cierre, decorativa: foto de escaleras de concreto en tono azul con logo UTEC superpuesto y texto "UNIVERSIDAD DE INGENIERÍA Y TECNOLOGÍA". Sin contenido académico.
