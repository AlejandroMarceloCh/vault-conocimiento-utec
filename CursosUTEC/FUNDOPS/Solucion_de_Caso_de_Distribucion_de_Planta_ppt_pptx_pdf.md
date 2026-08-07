---
curso: FUNDOPS
titulo: Solución de Caso de Distribución de Planta (ppt)__pptx
slides: 15
fuente: Solución de Caso de Distribución de Planta (ppt)__pptx.pdf
---

## Slide 1

Portada. Título "Solución de Caso de Distribución de Planta". Pie: "Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta". Slide decorativa/portada, sin contenido técnico.

## Slide 2

**Enunciado.**

Ejercicio de Distribución de Planta: el presidente de Dorton University pidió asignar a ocho profesores de biología (A-H) a ocho oficinas (1-8) del nuevo edificio de biología. Inicialmente A en oficina 1, B en 2, C en 3... sucesivamente. Distancia entre oficinas contiguas = 10 m; entre no contiguas = 15, 18, 25 y 34 m.

Diagrama del edificio (layout 2x4, ala norte arriba / ala sur abajo, separadas por un patio central):

| Ala norte | | | |
|---|---|---|---|
| Of 1 — Prof: A | Of 2 — Prof: B | Of 3 — Prof: C | Of 4 — Prof: D |
| *(Patio)* | | | *(→ lado derecho: "Nuevo edificio de biología")* |
| Of 5 — Prof: E | Of 6 — Prof: F | Of 7 — Prof: D | Of 8 — Prof: E |
| Ala sur | | | |

(Nota: en la imagen las etiquetas de Of 7 y Of 8 en el encabezado aparecen como "D" y "E" pero corresponden al texto genérico del enunciado, no a la asignación real inicial C/D... es una plantilla del diagrama de oficinas).

Diagrama inferior de distancias: 4 cajas arriba (Of1-Of4) y 4 abajo (Of5-Of8). Flecha curva entre Of1-Of2, Of2-Of3, Of3-Of4 marcada "10" (oficinas contiguas). Flechas diagonales desde Of1 hacia Of5 (15), Of6 (18), Of7 (25), Of8 (34), mostrando las distancias no contiguas.

## Slide 3

**Enunciado (continuación).**

Tabla "Flujo de Información entre Profesores" — documentos físicos de información transportados por semana (ida y vuelta):

| Ruta | Flujo de información | Ruta | Flujo de información |
|---|---|---|---|
| A-B | 20 | C-B | 20 |
| A-C | 30 | C-H | 30 |
| A-E | 50 | D-E | 40 |
| A-H | 70 | E-F | 10 |
| B-A | 10 | F-G | 10 |
| B-F | 30 | G-H | 40 |
| B-H | 20 | G-E | 20 |

Restricciones (lista):
- El costo promedio por metro de traslado de documentos es de $1.00
- Las oficinas 1, 4, 5 y 8 son las únicas con ventanas.
- D y E, los subdirectores del departamento de biología, deben tener oficinas con ventanas.
- H debe estar del otro lado del patio justo enfrente de D.
- A, G y H deben estar en la misma ala (ala sur o ala norte).
- F no debe estar junto a D o G ni directamente enfrente de G.

## Slide 4

**Condiciones.**

Tres tablas lado a lado:

Tabla de importancia:
| clave | Prioridad | Valor | Rango (metros recorridos) |
|---|---|---|---|
| A | ABSOLUTAMENTE NECESARIO | 4 | 2400-1100 |
| E | ESPECIALMENTE IMPORTANTE | 3 | 1099-500 |
| I | IMPORTANTE | 2 | 499-200 |
| O | ORDINARIA (NORMAL) | 1 | 199-1 |
| U | SIN IMPORTANCIA | 0 | 0 |
| X | NO DESEABLE | -1 | - |

Tabla de relaciones (razones numeradas, texto estándar del método SLP):
1. Cantidad de flujo
2. Costo de manejo de materiales
3. Equipo usado para manejar materiales
4. Necesidad de comunicación estrecha
5. Necesidad de compartir algo del personal
6. Necesidad de compartir algún equipo
7. Separación necesaria por: Ruido, Peligro, Sustancias químicas, Humos, Explosivos

Tabla de flujo de información (repite claves A/E/I/O/U/X con Prioridad, Valor y columna "Flujo" con líneas gráficas de distinto grosor/densidad representando la intensidad del flujo, de más densa (A) a una línea ondulada para X=no deseable).

## Slide 5

**Requerimientos** (slide de solo texto, sin elementos visuales adicionales):

1. Hacer el análisis de flujo de materiales con la matriz "desde-hasta", calcular el costo de la distribución actual.
2. Realizar la relación entre actividades, la matriz de cercanías y el diagrama de relaciones.
   - Utilice la tabla de importancias y la tabla de relaciones.
   - En la tabla de relaciones utilice de razones las condiciones dadas.
3. Realizar el diagrama relacional de recorridos-actividades.
   - Utilice la tabla de flujo de información.

## Slide 6

**1. Matriz "desde-hasta" de distancias entre oficinas (paso a).**

Texto: se usa la información de distancia entre oficinas; ejemplo A-B = 10 (contiguas).

Diagrama: fila superior Of1(A), Of2(B), Of3(C), Of4(D) con arcos curvos "10" entre consecutivas; fila inferior Of5(E), Of6(F), Of7(G), Of8(H); flechas diagonales desde Of1 con distancias 15, 18, 25, 34 hacia Of5-Of8. Una flecha grande de bloque apunta hacia la tabla resultante.

Matriz de distancias entre oficinas A-H (simétrica, solo triángulo superior mostrado):

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| A | - | 10 | 20 | 30 | 15 | 18 | 25 | 34 |
| B | | - | 10 | 20 | 18 | 15 | 18 | 25 |
| C | | | - | 10 | 25 | 18 | 15 | 18 |
| D | | | | - | 34 | 25 | 18 | 15 |
| E | | | | | - | 10 | 20 | 30 |
| F | | | | | | - | 10 | 20 |
| G | | | | | | | - | 10 |
| H | | | | | | | | - |

## Slide 7

**1. Matriz "desde-hasta" de cantidad de recorridos (paso b).**

Texto: se usa la tabla de flujo de información (veces recorridas por semana) repetida de la slide 3.

Matriz de flujos de información (asimétrica, valores ida/vuelta por separado, ej. A-B=20 pero B-A=10):

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| A | - | 20 | 30 | | 50 | | | 70 |
| B | 10 | - | | | | 30 | | 20 |
| C | | 20 | - | | | | | 30 |
| D | | | | - | 40 | | | |
| E | | | | | - | 10 | | |
| F | | | | | | - | 10 | |
| G | | | | | 20 | | - | 40 |
| H | | | | | | | | - |

Flecha de bloque hacia "Suma de flujos de información" (matriz simétrica sumando ida+vuelta):

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| A | - | 30 | 30 | | 50 | | | 70 |
| B | | - | 20 | | | 30 | | 20 |
| C | | | - | | | | | 30 |
| D | | | | - | 40 | | | |
| E | | | | | - | 10 | 20 | |
| F | | | | | | - | 10 | |
| G | | | | | | | - | 40 |
| H | | | | | | | | - |

## Slide 8

**1. Matriz "desde-hasta" de metros recorridos (paso c) y costo total.**

Texto: se multiplican distancias (slide 6) por cantidad de recorridos (slide 7) para obtener metros totales recorridos.

Matriz "desde-hasta" con distancias (repetida, ver slide 6) y matriz "desde-hasta" con cantidad de recorridos (repetida, ver slide 7) mostradas apiladas a la izquierda, con flecha de bloque hacia la matriz resultante de metros recorridos (distancia × flujo) con columna "total":

| | A | B | C | D | E | F | G | H | total |
|---|---|---|---|---|---|---|---|---|---|
| A | - | 300 | 600 | 0 | 750 | 0 | 0 | 2380 | **4030** |
| B | 0 | - | 200 | 0 | 0 | 450 | 0 | 500 | **1150** |
| C | 0 | 0 | - | 0 | 0 | 0 | 0 | 540 | **540** |
| D | 0 | 0 | 0 | - | 1360 | 0 | 0 | 0 | **1360** |
| E | 0 | 0 | 0 | 0 | - | 100 | 400 | 0 | **500** |
| F | 0 | 0 | 0 | 0 | 0 | - | 100 | 0 | **100** |
| G | 0 | 0 | 0 | 0 | 0 | 0 | - | 400 | **400** |
| H | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | **0** |

Suma total resaltada: **8080**.

Texto: costo promedio por metro = $1.00 → costo total de la distribución actual = **$8080**.

## Slide 9

**2. Relación entre actividades, matriz de cercanías (paso 1).**

Texto: se usa la tabla de importancia para asignar prioridad según metros recorridos.

Tres elementos lado a lado:
- Tabla de importancia (repetida de slide 4: A=4/2400-1100, E=3/1099-500, I=2/499-200, O=1/199-1, U=0/0, X=-1/-).
- Matriz de distancias recorridas con total (repetida de slide 8, con fila total 8080 resaltada en amarillo).
- Matriz de relación de actividades resultante (cada celda clasificada según el rango de metros recorridos, comparando con la tabla de importancia):

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| A | - | I | E | U | E | U | U | A |
| B | | - | I | U | U | I | U | E |
| C | | | - | U | U | U | U | E |
| D | | | | - | A | U | U | U |
| E | | | | | - | O | I | U |
| F | | | | | | - | O | U |
| G | | | | | | | - | I |
| H | | | | | | | | - |

## Slide 10

**2. Relación entre actividades, tabla de relaciones y diagrama de relaciones (paso 2).**

Texto: se usa la matriz de relación de actividades y la tabla de relaciones (razones 1-7) para armar el diagrama de relaciones; la asignación de razones depende del conocimiento del proceso.

Matriz de relación de actividades (repetida de slide 9) + Tabla de relaciones (razones 1-7, repetida de slide 4) → flecha de bloque hacia el **Diagrama de relación entre actividades**: diagrama tipo rejilla romboidal (SLP) con las 8 actividades A-H listadas verticalmente a la izquierda y celdas en forma de rombo conectando cada par, cada rombo contiene la letra clave de relación (I, E, U, A, O) y debajo un número que referencia la razón (1-7) de la tabla de relaciones. Ejemplo de lectura: A-B con letra "I" y razón "1"; A-C con "E" y razón "3"; D-E con "A" y razón "1"; etc. Es el diagrama relacional estándar del método SLP (Systematic Layout Planning) mostrando gráficamente todas las relaciones par a par.

## Slide 11

**3. Diagrama relacional de recorridos-actividades — matriz de asignación de valores por flujo (paso 1).**

Texto: se usa la matriz de relación de actividades y la tabla de flujo de información (valores A=4, E=3, I=2, O=1, U=0, X=-1) para generar la matriz de asignación de valores.

Matriz de relación de actividades (repetida) + Tabla de flujo de información (repetida) → flecha hacia matriz de valores numéricos con fila y columna TOTAL:

| | A | B | C | D | E | F | G | H | TOTAL |
|---|---|---|---|---|---|---|---|---|---|
| A | - | 2 | 3 | 0 | 3 | 0 | 0 | 4 | **12** |
| B | | - | 2 | 0 | 0 | 2 | 0 | 3 | **7** |
| C | | | - | 0 | 0 | 0 | 0 | 3 | **3** |
| D | | | | - | 4 | 0 | 0 | 0 | **4** |
| E | | | | | - | 1 | 2 | 0 | **3** |
| F | | | | | | - | 1 | 0 | **1** |
| G | | | | | | | - | 2 | **2** |
| H | | | | | | | | - | **0** |
| TOTAL | 0 | 2 | 5 | 0 | 7 | 3 | 3 | 12 | |

Texto explicativo: se suman los valores horizontal y vertical, ej. A = 12+0 = 12; el resultado es la importancia en unidades (profesores); mayor valor = mayor importancia.

Tabla resumen "PROFESORES / TOTAL" con A y H resaltados en rojo (12, los más importantes), B y C en amarillo (9 y 8):

| PROFESORES | TOTAL |
|---|---|
| A | 12 |
| B | 9 |
| C | 8 |
| D | 4 |
| E | 10 |
| F | 4 |
| G | 5 |
| H | 12 |

## Slide 12

**3. Diagrama relacional de recorridos-actividades — grafo de nodos (paso 2).**

Texto: se usa la tabla de importancia analizada anteriormente.

Tabla de matriz de valores + TOTAL (repetida de slide 11) y tabla PROFESORES/TOTAL (repetida) a la izquierda.

A la derecha, un grafo de nodos circulares (diagrama de red): 8 nodos etiquetados A, B, C, D, E, F, G, H distribuidos espacialmente (C arriba, H y B a la derecha, A al centro-izquierda, E y D abajo-izquierda, F y G abajo-derecha), conectados por líneas azules que representan las relaciones con mayor peso (los nodos con más conexiones — A, B, H, C — están muy interconectados en el centro/derecha del grafo, mientras D, F, G tienen menos conexiones), reflejando visualmente los totales de importancia de la tabla (A y H con más peso).

## Slide 13

**3. Diagrama relacional de recorridos-actividades — layout propuesto (paso 3).**

Repite: tabla de matriz de valores + TOTAL, y el mismo grafo de nodos de la slide 12 (versión más compacta).

A la derecha, lista de Restricciones (repetida de slide 3): oficinas con ventana (1,4,5,8); D y E deben tener ventana; H enfrente de D cruzando el patio; A,G,H misma ala; F no junto a D o G ni enfrente de G.

Resultado: nueva tabla de asignación de oficinas (layout final propuesto), formato 2x4 con número de oficina en verde y letra de profesor en negro grande:

| 1 F | 2 B | 3 C | 4 D |
|---|---|---|---|
| **5 E** | **6 G** | **7 A** | **8 H** |

(Oficinas 1, 4, 5, 8 en verde = con ventana, ocupadas por F, D, E, H respectivamente — cumpliendo que D y E tengan ventana; H en oficina 8 queda frente a D en oficina 4 cruzando el patio; A, G, H en oficinas 7, 6, 8 mismo lado/ala sur).

## Slide 14

**3. Diagrama relacional de recorridos-actividades — nueva matriz de distancias (paso 4).**

Texto: con la nueva asignación de oficinas se recalcula la matriz "desde-hasta" de distancias.

Repite el layout final de oficinas (1F, 2B, 3C, 4D / 5E, 6G, 7A, 8H) y el diagrama de distancias entre oficinas (Of1-Of8 con arcos "10" entre contiguas y flechas diagonales 15/18/25/34 desde Of1), igual estructura visual que en la slide 2/6 pero ahora aplicada al nuevo orden de profesores.

Nueva matriz "desde-hasta" de distancias (recalculada según la nueva posición de cada profesor):

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| A | 0 | 18 | 15 | 18 | 20 | 25 | 10 | 10 |
| B | | 0 | 10 | 20 | 18 | 10 | 15 | 25 |
| C | | | 0 | 10 | 25 | 20 | 18 | 18 |
| D | | | | 0 | 34 | 30 | 25 | 15 |
| E | | | | | 0 | 15 | 10 | 30 |
| F | | | | | | 0 | 18 | 34 |
| G | | | | | | | 0 | 20 |
| H | | | | | | | | 0 |

## Slide 15

**3. Diagrama relacional de recorridos-actividades — costo final y ahorro (paso 5, cierre).**

Texto: con la nueva matriz de distancias y la matriz de flujos de información se recalculan los metros totales recorridos.

Nueva matriz "desde-hasta" de distancias (repetida de slide 14) y matriz de flujos de información (repetida de slide 7) mostradas a la izquierda apiladas.

Matriz resultante de metros recorridos (distancia nueva × flujo) con columna total:

| | A | B | C | D | E | F | G | H | total |
|---|---|---|---|---|---|---|---|---|---|
| A | - | 540 | 450 | 0 | 1000 | 0 | 0 | 0 | **1990** |
| B | 0 | - | 200 | 0 | 0 | 300 | 0 | 500 | **1000** |
| C | 0 | 0 | - | 0 | 0 | 0 | 0 | 540 | **540** |
| D | 0 | 0 | 0 | - | 1360 | 0 | 0 | 0 | **1360** |
| E | 0 | 0 | 0 | 0 | - | 150 | 200 | 0 | **350** |
| F | 0 | 0 | 0 | 0 | 0 | - | 180 | 0 | **180** |
| G | 0 | 0 | 0 | 0 | 0 | 0 | - | 800 | **800** |
| H | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | **0** |

Suma total resaltada: **6220**.

Texto de cierre: costo promedio por metro = $1.00. Con la distribución inicial se obtuvo un costo de $8080; con la nueva distribución (F,B,C,D / E,G,A,H) se genera un ahorro de **$1860** (costo final $6220).
