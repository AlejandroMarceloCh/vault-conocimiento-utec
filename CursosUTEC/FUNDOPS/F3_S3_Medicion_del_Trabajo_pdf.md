---
curso: FUNDOPS
titulo: F3-S3 Medicion del Trabajo
slides: 30
fuente: F3-S3 Medicion del Trabajo.pdf
---

## Slide 1
Portada. Foto decorativa de un edificio de concreto de UTEC en tonos azules, logo UTEC. Texto: "FUNDAMENTOS DE OPERACIONES" / "Semana 3 – Medición del trabajo".

## Slide 2
Slide de índice. Foto decorativa lateral (estructura de concreto). Lista numerada:
1. Medición del Trabajo
2. Estudios de Tiempos
3. Calificación del Desempeño
4. Muestreo del Trabajo

## Slide 3
Slide de "Objetivos". Foto decorativa lateral. Lista numerada de objetivos de la sesión:
1. Al finalizar esta sesión, deberás ser capaz de:
2. Explicar qué es un tiempo estándar.
3. Hallar el número de ciclos a observar como parte de un estudio de tiempos.
4. Calcular el tiempo estándar de una tarea, considerando la calificación del desempeño y el porcentaje de holgura.
5. Determinar el número de observaciones requeridas y el plan de observaciones aleatorias para un muestreo del trabajo.
6. Comparar el estudio de tiempos y el muestreo del trabajo.

## Slide 4
Slide separador de sección "1. Medición del Trabajo". Fondo fotográfico decorativo (estructura de concreto en tono azul/turquesa) con número "1." grande y título en blanco.

## Slide 5
Título "Medición del Trabajo". Contenido en viñetas (check ✔):
- Se enfoca en determinar cuánto tiempo debería tomar completar un trabajo.
- No aborda: el contenido del trabajo / cómo se debe llevar a cabo el trabajo. Nota aclaratoria: estos aspectos son definidos con anterioridad y son inputs para la medición del trabajo.
- Los resultados de la medición del trabajo son inputs críticos para: planeamiento de la capacidad, planeamiento de la fuerza de trabajo, estimación del costo de MO, elaboración de presupuestos, diseño de planes de incentivos.

## Slide 6
Título "Medición del Trabajo". Contenido:
- Tiempo estándar: la cantidad de tiempo que le debería tomar a un trabajador calificado completar una determinada tarea, trabajando a un ratio sostenible, usando métodos de trabajo, herramientas y equipos, materias primas y una disposición del lugar de trabajo establecidos.
- Técnicas usadas para la medición del trabajo: estudio de tiempos, tiempos históricos, tiempos estándar predeterminados, muestreo del trabajo.

## Slide 7
Título "Técnicas de Medición del Trabajo". Diagrama de dos cajas rectangulares lado a lado (sin flechas entre ellas, comparación directa):
- Caja izquierda "Estudio de Tiempos": Usado para elaborar un tiempo estándar en base de observaciones de un trabajador tomadas durante un número de ciclos.
- Caja derecha "Muestreo del Trabajo": Técnica para estimar la proporción del tiempo que un trabajador o máquina destina a varias actividades y al tiempo de inactividad.

## Slide 8
Slide separador de sección "2. Estudio de Tiempos". Fondo fotográfico decorativo (estructura de concreto azul/turquesa) con número "2." grande.

## Slide 9
Slide sin texto propio salvo el título "Estudio de Tiempos" (título repetido de la sección, sin bullets adicionales en el chunk de texto).

## Slide 10
Título "Estudio de Tiempos". Diagrama de flujo vertical con 7 cajas azules conectadas por flechas descendentes, describiendo el proceso completo del estudio de tiempos:
1. Definir la tarea a estudiar
2. Dividir la tarea en elementos precisos
3. Determinar el número de ciclos a observar
4. Cronometrar y registrar los elementos de trabajo y calificaciones de desempeño
5. Calcular el tiempo observado promedio → con flecha roja hacia la fórmula: $TO = \dfrac{\sum x_i}{n}$, donde TO = Tiempo observado, $\sum x_i$ = sumatoria de los tiempos registrados, n = número de observaciones.
6. Calificar el desempeño laboral y calcular el tiempo normal para cada elemento → flecha roja hacia fórmula: $TN = TO \times C/100$, donde TN = Tiempo normal, TO = Tiempo observado, C = Calificación del desempeño.
7. Sumar los TN de cada elemento para calcular el TN de la tarea (caja intermedia sin fórmula asociada directa)
8. Calcular el tiempo estándar → flecha roja hacia fórmula: $TE = TN \times FH$, donde FH = Factor de Holgura.

## Slide 11
Título "División de la Tarea en Elementos". Contenido:
- Elemento: Parte esencial y definida de una actividad o tarea determinada seleccionada para fines de observación y cronometraje.
- Reglas para seleccionar los elementos: fácil identificación con inicio y término claramente definidos; deben ser lo más breves posible; separar los elementos manuales de los mecánicos; discriminar los elementos manuales a máquina parada de los de máquina en marcha.

## Slide 12
Título "Clasificación de los Elementos". Diagrama de árbol/flujo con cajas azules y flechas rojas, con 3 ramas principales:
- "Con relación al ciclo" → Regulares / Irregulares o de frecuencia / Extraños.
- "Con relación al ejecutante" → se ramifica en "Manuales" (→ Sin máquina (libres) / Con máquina → Máquina parada, Máquina en marcha) y "Máquina" (→ Automática → Con vigilancia permanente, Sin vigilancia permanente / Con avance manual).
- "Con relación al tiempo" → Constantes / Variables.
Cita al pie: "Obtenido de 'Estudio del Trabajo: Ingeniería de Métodos y Medición del Trabajo', Roberto García Criollo, 2005, Pág. 193".

## Slide 13
Título "Determinación del número de ciclos a observar". Contenido:
- El número de observaciones está en función de: variabilidad de los tiempos observados, nivel de confianza deseado, nivel de precisión (error aceptable).
- Fórmulas (dos variantes equivalentes):
$$n = \left(\frac{zs}{h\bar{x}}\right)^2 \quad \text{o} \quad n = \left(\frac{zs}{e}\right)^2$$
Donde: z = # de desviaciones estándar normales requeridas para el nivel de confianza deseado; s = desviación estándar de la muestra inicial; h = nivel de precisión deseado en % del elemento de trabajo, expresado como decimal; e = máximo error aceptable; $\bar{x}$ = media de la muestra inicial.

## Slide 14
Título "Determinación del número de ciclos a observar" (continuación). Contenido: "Para casos en donde la desviación estándar de la muestra no se provea", con la fórmula de desviación estándar muestral:
$$s = \sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}}$$
Donde: $x_i$ = valor de cada observación; $\bar{x}$ = media de las observaciones; n = número de observaciones en la muestra.

## Slide 15
Título "Ejemplo 1". Enunciado: ¿Cuántos ciclos de trabajo deberían ser cronometrados para estimar el tiempo estándar de una actividad dentro del 2% del promedio de la muestra con una confianza del 99% si un estudio piloto arrojó los siguientes resultados?

Tabla de datos (estudio piloto):

| # de observación | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Tiempo (segundos) | 5.2 | 5.5 | 5.8 | 5.3 | 5.5 | 5.1 |

Desarrollo mostrado paso a paso:
$$\bar{x} = \frac{5.2+5.5+5.8+5.3+5.5+5.1}{6} = 5.4$$
$$s = \sqrt{\frac{(5.2-5.4)^2+(5.5-5.4)^2+(5.8-5.4)^2+(5.3-5.4)^2+(5.5-5.4)^2+(5.1-5.4)^2}{6-1}} = 0.253$$
$$n = \left(\frac{zs}{h\bar{x}}\right)^2 = \left(\frac{(2.58)(0.253)}{(0.02)(5.4)}\right)^2 = 36.5286 \cong 37 \text{ observaciones}$$
(z=2.58 corresponde al 99% de confianza; h=0.02 es el 2% de precisión).

## Slide 16
Slide separador de sección "3. Calificación del Desempeño". Fondo fotográfico decorativo (estructura de concreto azul/turquesa) con número "3." grande.

## Slide 17
Título "Calificación del Desempeño del Operario". Contenido:
- El tiempo requerido para cada elemento depende en un alto grado de: la habilidad, el esfuerzo del operario.
- Es necesario ajustar: hacia arriba el tiempo normal del operario bueno, y hacia abajo el tiempo normal del operario deficiente… hasta alcanzar un nivel estándar.
- El observador evalúa la efectividad en términos del desempeño de un operario calificado.
- Operario calificado: operario completamente experimentado que trabaje en las condiciones acostumbradas en la estación de trabajo, a un paso ni demasiado rápido ni demasiado lento.

## Slide 18
Título "Calificación del Desempeño del Operario" (continuación). Contenido:
- Principio básico: ajustar el tiempo medio observado (TO) para cada elemento… al tiempo normal (TN) que requeriría un operario calificado para realizar el mismo trabajo, en un recuadro:
$$TN = TO \times C/100$$
Donde: TN = Tiempo normal, TO = Tiempo observado, C = Calificación del desempeño (%).
- 100% = desempeño estándar de un operario calificado.
- 105% = el operador realiza la tarea ligeramente más rápido que el operador calificado.
- Existen varios métodos para la calificación del desempeño.

## Slide 19
Título "Método Westinghouse". Captura de una tabla con 4 sub-tablas (Habilidad, Esfuerzo, Condiciones, Consistencia), cada una con letra de categoría (A-G o A-C) y valor numérico asociado, rodeadas por óvalos rojos que las conectan a explicaciones textuales a la derecha:

**HABILIDAD**: A Habilísimo +0.15 | B Excelente +0.10 | C Bueno +0.05 | D Medio 0.00 | E Regular -0.05 | F Malo -0.10 | G Torpe -0.15.
Explicación: "Habilidad. Es la eficiencia para seguir un método dado no sujeto a variación por voluntad del operador."

**ESFUERZO**: A Excesivo +0.15 | B Excelente +0.10 | C Bueno +0.05 | D Medio 0.00 | E Regular -0.05 | F Malo -0.10 | G Torpe -0.15.
Explicación: "Esfuerzo. Es la voluntad de trabajar, controlables por el operador dentro de los límites impuestos por la habilidad."

**CONDICIONES**: A Buena +0.05 | B Media 0.00 | C Mala -0.05.
Explicación: "Condiciones. Son aquellas condiciones (luz, ventilación, calor) que afectan únicamente al operario y no aquellas que afectan a la operación."

**CONSISTENCIA**: A Buena +0.05 | B Media 0.00 | C Mala -0.05.
Explicación: "Consistencia. Son los valores de tiempo que realiza el operador que se repiten en forma constante o incostante [sic]."

Cita al pie: "Obtenido de 'Estudio del Trabajo: Ingeniería de Métodos y Medición del Trabajo', Roberto García Criollo, 2005, Pág. 193".

## Slide 20
Título "Suplementos u Holguras". Diagrama de flujo con cajas rectangulares conectadas por flechas azules delgadas, estructura jerárquica:
- Fila superior izquierda: "Necesidades personales" y "Fatiga básica" → ambas apuntan hacia abajo a "Holguras constantes".
- "Fatiga variable" (caja independiente) → apunta hacia "Holguras totales".
- Fila superior derecha: "Demoras inevitables", "Demoras evitables", "Holguras adicionales" (cajas sólidas) y "Holguras por política" (caja con borde punteado) → todas convergen en "Holguras especiales".
- "Holguras constantes" y "Holguras especiales" convergen en "Holguras totales".
- Al final: "Holguras totales" + "Tiempo normal" = "Tiempo estándar" (con símbolos + y = entre las cajas).
Cita al pie: "Obtenido de 'Ingeniería Industrial: Métodos, estándares y diseño del trabajo', Niebel y Freivald, 2013, Pág. 367".

## Slide 21
Título "Suplementos u Holguras" (continuación, en inglés). Captura de tabla en inglés con 2 columnas "Percent" listando categorías de holguras y sus porcentajes: A. Constant allowances (Personal allowance 5, Basic fatigue allowances 4); B. Variable allowances (Standing allowance 2, Abnormal position allowance: Slightly awkward 0, Awkward 2, Very awkward 7); C. Use of force or muscular energy (tabla de peso levantado en libras de 5 a 70, con % de 0 a 22); columna derecha: 4. Bad light (0,2,5); 5. Atmospheric conditions 0-10; 6. Close attention (0,2,5); 7. Noise level (0,2,5,5); 8. Mental strain (1,4,8); 9. Monotony (0,1,4); 10. Tediousness (0,2,5).
A la derecha, fórmula en recuadro: $TE = TN \times FH$. Donde TE = Tiempo estándar, TN = Tiempo normal, FH = Factor de holgura.
Además: $FH_{trabajo} = 1+H$ (H = porcentaje de holgura basado en el tiempo de la tarea) y $FH_{día} = \dfrac{1}{1-H}$ (H = porcentaje de holgura basado en el día de trabajo, tiempo de trabajo disponible).
Cita al pie: "Obtenido de 'Operations Management', Stevenson, 2021, Pág. 168".

## Slide 22
Título "Suplementos u Holguras" (misma tabla que slide 21 pero traducida al español). Tabla: A. Subsidios constantes (Asignación personal, Indemnizaciones básicas por fatiga=4); B. Asignaciones variables (Subsidio por permanencia en el trabajo=2, Tolerancia por posición anormal: incómodo, torpe=2, muy torpe=7); C. Uso de fuerza o energía muscular (peso levantado en libras 5 a 70, % de 0 a 22); columna derecha: 4. Mala luz (0,2,5); 5. Condiciones atmosféricas 0-10; 6. Atención especial (0,2,5); 7. Nivel de ruido (0,2,5,5); 8. Tensión mental (1,4,...); 9. Monotonía (0,1,4); 10. Tediosidad (0,2,...).
Mismas fórmulas que slide 21 a la derecha: $TE=TN\times FH$, $FH_{trabajo}=1+H$, $FH_{día}=\frac{1}{1-H}$.
Cita al pie: "Obtenido de 'Operations Management', Stevenson, 2021, Pág. 168".

## Slide 23
Título "Ejemplo 2". Enunciado: Un estudio de tiempos fue llevado a cabo para un trabajo que contiene 4 elementos. Los tiempos observados y las calificaciones de desempeño para seis ciclos se muestran a continuación.

Tabla de datos:

| Elemento | Calificación | Obs.1 | Obs.2 | Obs.3 | Obs.4 | Obs.5 | Obs.6 |
|---|---|---|---|---|---|---|---|
| 1 | 90% | 0.44 | 0.50 | 0.43 | 0.45 | 0.48 | 0.46 |
| 2 | 85% | 1.50 | 1.54 | 1.47 | 1.51 | 1.49 | 1.52 |
| 3 | 110% | 0.84 | 0.89 | 0.77 | 0.83 | 0.85 | 0.80 |
| 4 | 100% | 1.10 | 1.14 | 1.08 | 1.20 | 1.16 | 1.26 |

Preguntas: 1. Determinar el tiempo promedio observado. 2. Calcular el tiempo normal para cada elemento. 3. Asumiendo un factor de holgura del 15% del tiempo de la tarea, calcular el tiempo estándar para esta tarea.

## Slide 24
Título "Ejemplo 2" (continuación, con solución). Misma tabla del slide 23 pero con 3 columnas adicionales de cálculos:

| Elemento | Calificación | Obs.1-6 (igual) | TO (Promedio) | TN (TO×Calificación) | TE (TN×(1+Holgura)) |
|---|---|---|---|---|---|
| 1 | 90% | ... | 0.46 | 0.41 | 0.48 |
| 2 | 85% | ... | 1.51 | 1.28 | 1.47 |
| 3 | 110% | ... | 0.83 | 0.91 | 1.05 |
| 4 | 100% | ... | 1.16 | 1.16 | 1.33 |

Resultado final resaltado en amarillo: **4.33 minutos** (suma de la columna TE, tiempo estándar total de la tarea).

## Slide 25
Slide separador de sección "4. Muestreo del Trabajo". Fondo fotográfico decorativo (estructura de concreto azul/turquesa) con número "4." grande.

## Slide 26
Título "Muestreo del Trabajo". Contenido:
- El muestreo del trabajo es una técnica para estimar la proporción del tiempo que un trabajador o máquina se encuentra realizando varias actividades y la proporción en la que se encuentran inactivas.
  - El muestreo del trabajo no requiere que se cronometre la actividad.
  - Tampoco requiere la observación continua de dicha actividad.
- Usos: Estudio "ratio-delay" (se enfoca en el % del tiempo del trabajador que involucra retrasos inevitables o la proporción del tiempo que la máquina está inactiva); análisis de tareas no repetitivas.

## Slide 27
Título "Muestreo del Trabajo" (continuación). Diagrama de flujo vertical con 5 cajas azules conectadas por flechas descendentes, describiendo el proceso del muestreo del trabajo:
1. Tomar una muestra preliminar para obtener una estimación del valor del parámetro
2. Calcular el tamaño de muestra requerido
3. Preparar un horario para observar el trabajador en momentos apropiados
4. Observar y registrar las actividades del trabajador/máquina
5. Determinar cómo asignan el tiempo a diferentes actividades (usualmente en %)

## Slide 28
Título "Tamaño de Muestra". Fórmulas:
$$e = z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \qquad n = \left(\frac{z}{e}\right)^2 \hat{p}(1-\hat{p})$$
Donde: e = máximo error (porcentaje); z = # de desviaciones estándar normales requeridas para el nivel de confianza deseado; $\hat{p}$ = proporción muestral (número de ocurrencias dividida entre el tamaño de muestra); n = tamaño de muestra.

## Slide 29
Título "Ejemplo 3". Enunciado: Suponga que se desea determinar el número de observaciones que se requieren, con 95% de confianza, tal que la proporción verdadera del tiempo de demoras personales e inevitables se encuentre dentro del intervalo de 6 a 10%. Se espera que el tiempo de las demoras inevitables y personales sea de 8%.

Desarrollo:
$$n = \left(\frac{z}{e}\right)^2 \hat{p}(1-\hat{p})$$
$$n = \left(\frac{1.96}{0.02}\right)^2 0.08(0.92) = 706.85 \cong 707 \text{ observaciones}$$
(e = 0.02 corresponde a la mitad del intervalo 6-10% respecto al valor esperado de 8%; z=1.96 para 95% de confianza).

## Slide 30
Slide de cierre/contraportada decorativa. Foto de una escalera de concreto dentro de un edificio UTEC con overlay azul semitransparente, logo UTEC grande centrado y nombres de carreras de ingeniería en el fondo (Mecatrónica, Bioingeniería, Ciencia de la Computación, Ambiental, Energía, Industrial, Eléctrica). Sin contenido académico, es decorativa.
