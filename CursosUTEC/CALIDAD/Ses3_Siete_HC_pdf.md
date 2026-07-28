---
curso: CALIDAD
titulo: Ses3_Siete_HC
slides: 17
fuente: Ses3_Siete_HC.pdf
---

## Slide 1

Portada. Título: "Las 7 Herramientas de la Calidad". Fondo celeste con foto arquitectónica del edificio UTEC (decorativa) y logo UTEC + lema "Reinventa el mundo" (chrome decorativo).

## Slide 2

Título: "Objetivo". Texto entre corchetes decorativos:
"Identificar y medir el proyecto de mejora. Así como el alcance de este. Se utilizará las principales herramientas básicas de la Calidad."

## Slide 3

Título: "Contenido de sesión aquí". Cuatro bloques numerados en corchetes horizontales, representando el temario de la sesión:

| N° | Herramienta |
|----|-------------|
| 01. | Diagrama Causa-Efecto |
| 02. | Hoja de datos |
| 03. | Graficas de Control |
| 04. | Histogramas |

## Slide 4

Sección "/ 7 Herramientas de la Calidad" (captura de slide con fondo blanco, título en azul).

Texto: "Es una denominación dada a un conjunto fijo de técnicas gráficas identificadas como las más útiles en la solución de problemas relacionados con la calidad. Se inspiró en las siete famosas armas del monje guerrero Saitō Musashibō Benkei, también conocido 'Benkei'."

Recuadro verde oliva con la lista de las 7 herramientas:
- Diagrama de Ishikawa
- Hoja de verificación o comprobación
- Gráfico de control
- Histograma
- Diagrama de Pareto
- Diagrama de dispersión
- Muestreo estratificado¹

Texto inferior: "Contraste con los métodos más avanzados de estadística: Muestreos de encuestas, muestreos de aceptación, pruebas de hipótesis, diseño de experimentos, análisis multivariados, y otros desarrollados en el campo de la IO."

## Slide 5

Título: "Diagrama de Ishikawa". Recuadro naranja con texto: "El diagrama de causa y efecto identifica muchas de las causas posibles para un efecto o problema. Puede ser usado para estructurar una sesión de tormenta de ideas. Este permite ordenar inmediatamente clasifica las ideas en categorías válidas."

Diagrama espina de pescado (Ishikawa) genérico, caso "Empresa: Best quality copias", efecto = "[Baja calidad de fotocopiado]" (recuadro morado a la derecha). Cuatro categorías (espinas) alimentando la línea central, cada una con 3 líneas de "Causa" genéricas (placeholder, sin texto específico aún):
- Procesos (arriba izq., naranja) → 3 causas
- Equipos (arriba der., amarillo) → 3 causas
- Personas (abajo izq., verde) → 3 causas
- Materiales (abajo der., verde azulado) → 3 causas

## Slide 6

Mismo título "Diagrama de Ishikawa". Versión desarrollada del diagrama causa-efecto anterior, con recuadro superior "Diagrama de Causa y Efecto", empresa "Best quality copias", efecto = "Baja calidad de fotocopiado" (recuadro morado). Cuatro categorías con causas específicas:

- **Personas** (naranja): Configuración errónea, Manual de operación no disponible, Manos sucias, No hay toallas húmedas disponibles, Originales incorrectos, Alineación del papel
- **Materiales** (amarillo): Calidad del papel, Almacenaje del material, Tóner correcto
- **Métodos** (verde): Manipulación incorrecta del papel, Configuración de los originales, Tiempo de secado, Dispositivo de secado malogrado
- **Máquinas** (verde azulado): Condiciones del rollo, Velocidad del rollo, Contaminación, Muy antiguo, Lámpara, Sucia

## Slide 7

Sección "/ 2. Hoja de revisión". Recuadro naranja: "Una hoja de verificación es una forma estructurada, preparada para recoger y analizar los datos. Esta es una herramienta genérica que se puede adaptar para una amplia variedad de propósitos."

"Cuando usarlo:"
- Cuando los datos se pueden observar y recoger varias veces por la misma persona o en el mismo lugar.
- Cuando se recolectan datos sobre la frecuencia o patrones de eventos, problemas, defectos, localización de defectos, causas de defectos, etc.
- Al recoger datos de un proceso de producción.

## Slide 8

Sección "/ 2. Hoja de revisión". Tabla ejemplo "Causas de cartas extraviadas" (hoja de verificación con conteo tipo palotes/tally, días 23-27 de abril):

| Tipo de defecto | 23 Abril | 24 Abril | 25 Abril | 26 Abril | 27 Abril | Defectos totales |
|---|---|---|---|---|---|---|
| Dirección ilegible | 16 palotes | 7 palotes | 13 palotes | 15 palotes | 11 palotes | 71 |
| Departamento incorrecto | 6 palotes | 2 palotes | — | 5 palotes | 5 palotes | 22 |
| Dirección postal incorrecta | 20 palotes | 5 palotes | 13 palotes | 12 palotes | 9 palotes | 59 |
| Estampilla incorrecta | 3 palotes | 5 palotes | 1 palote | 3 palotes | 4 palotes | 16 |
| **Defectos totales** | **50** | **19** | **36** | **34** | **29** | **168** |

(Los conteos por celda están representados con marcas de palote/tally en la imagen; se transcriben aquí los totales de fila y columna, que son los datos exactos y verificables de la tabla.)

## Slide 9

Recuadro naranja: "El gráfico de control es un gráfico utilizado para estudiar cómo un proceso cambia con el tiempo. Los datos se representan en orden cronológico. Un gráfico de control siempre tiene una línea central para la media, una línea superior para el límite de control superior y una línea inferior para el límite inferior de control. Estas líneas se determinan a partir de datos históricos. Al comparar los datos actuales a estas líneas, se puede sacar conclusiones sobre si la variación del proceso es constante (en el control) o es impredecible (fuera de control, afectado por causas especiales de variación)."

Gráfico de línea "Grafica de medias y limites de control": eje Y "Medidas de peso de latas (gr)" de 196.00 a 210.00, eje X observaciones 1 a 24. Tres líneas horizontales de referencia:
- UCL (límite superior) = 206.73 (línea roja)
- CL (línea central) = 203.26 (línea azul)
- LCL (límite inferior) = 199.81 (línea verde)

La serie de datos (línea morada) oscila entre ~200 y ~203 en las primeras observaciones, sube a un pico de 210.00 en la observación 14 (por encima del UCL, fuera de control), cae a un mínimo de ~197.7 en la observación 15 (por debajo del LCL, también fuera de control), luego se estabiliza entre 204-206 hacia el final (observaciones 19-24), cerca o ligeramente por encima del CL.

## Slide 10

Captura de pantalla tipo diagrama de flujo/árbol de decisión: "Elegir una gráfica de control". Estructura jerárquica:

```
Tipo de datos
├── Continuos → ¿Datos recolectados en subgrupos?
│   ├── No → Gráfica I-MR
│   └── Sí → Tamaño de subgrupo
│       ├── 8 o menos → Gráfica Xbarra-R
│       └── Mayor que 8 → Gráfica Xbarra-S
└── Atributos → ¿Qué está contando?
    ├── Elementos defectuosos → Gráfica P
    └── Defectos por unidad → Gráfica U
```

Cada gráfica final (I-MR, Xbarra-R, Xbarra-S, P, U) se muestra con un mini-thumbnail de ejemplo de gráfico de control.

## Slide 11

Título: "Que Grafica de Control Utilizar?". Captura de tabla de datos (screenshot tipo libro de texto) "Observations (bottle volume in ounces)", 25 muestras (Sample Number 1-25), 4 observaciones por muestra, columnas Average (x̄) y Range (R):

| Sample | Obs 1 | Obs 2 | Obs 3 | Obs 4 | Average | Range |
|---|---|---|---|---|---|---|
| 1 | 15.85 | 16.02 | 15.83 | 15.93 | 15.91 | 0.19 |
| 2 | 16.12 | 16.00 | 15.85 | 16.01 | 15.99 | 0.27 |
| 3 | 16.00 | 15.91 | 15.94 | 15.83 | 15.92 | 0.17 |
| 4 | 16.20 | 15.85 | 15.74 | 15.93 | 15.93 | 0.46 |
| 5 | 15.74 | 15.86 | 16.21 | 16.10 | 15.98 | 0.47 |
| 6 | 15.94 | 16.01 | 16.14 | 16.03 | 16.03 | 0.20 |
| 7 | 15.75 | 16.21 | 16.01 | 15.86 | 15.96 | 0.46 |
| 8 | 15.82 | 15.94 | 16.02 | 15.94 | 15.93 | 0.20 |
| 9 | 16.04 | 15.98 | 15.83 | 15.98 | 15.96 | 0.21 |
| 10 | 15.64 | 15.86 | 15.94 | 15.89 | 15.83 | 0.30 |
| 11 | 16.11 | 16.00 | 16.01 | 15.82 | 15.99 | 0.29 |
| 12 | 15.72 | 15.85 | 16.12 | 16.15 | 15.96 | 0.43 |
| 13 | 15.85 | 15.76 | 15.74 | 15.98 | 15.83 | 0.24 |
| 14 | 15.73 | 15.84 | 15.96 | 16.10 | 15.91 | 0.37 |
| 15 | 16.20 | 16.01 | 16.10 | 15.89 | 16.05 | 0.31 |
| 16 | 16.12 | 16.08 | 15.83 | 15.94 | 15.99 | 0.29 |
| 17 | 16.01 | 15.93 | 15.81 | 15.68 | 15.86 | 0.33 |
| 18 | 15.78 | 16.04 | 16.11 | 16.12 | 16.01 | 0.34 |
| 19 | 15.84 | 15.92 | 16.05 | 16.12 | 15.98 | 0.28 |
| 20 | 15.92 | 16.09 | 16.12 | 15.93 | 16.02 | 0.20 |
| 21 | 16.11 | 16.02 | 16.00 | 15.88 | 16.00 | 0.23 |
| 22 | 15.98 | 15.82 | 15.89 | 15.89 | 15.90 | 0.16 |
| 23 | 16.05 | 15.73 | 15.73 | 15.93 | 15.86 | 0.32 |
| 24 | 16.01 | 16.01 | 15.89 | 15.86 | 15.94 | 0.15 |
| 25 | 16.08 | 15.78 | 15.92 | 15.98 | 15.94 | 0.30 |
| **Total** | | | | | **398.75** | **7.17** |

## Slide 12

Título: "Como interpretar las Graficas de Control?". Gráfico de control de medias (Sample Mean) sobre los datos de botellas (onzas), eje Y "Ounces" de 15.60 a 16.20, eje X muestras 1-25. Líneas de referencia: LCL ≈ 15.74, CL ≈ 15.95, UCL ≈ 16.16 (líneas punteadas negras para LCL/UCL, línea sólida negra para CL). La serie azul (Sample Mean) oscila entre ~15.83 y ~16.05, dentro de los límites de control en todas las observaciones (proceso bajo control, sin puntos fuera de LCL/UCL). Fondo del gráfico con degradado naranja decorativo.

## Slide 13

Sección "/ 4. Histograma". Descripción: "Un histograma indica con qué frecuencia se produce cada valor diferente en un conjunto de datos. El histograma es el grafico utilizado más común para mostrar la distribución de frecuencias. Se parece a una gráfica de control, pero hay importantes diferencias entre ellas."

Histograma de barras "Notas primer parcial" vs "Alumnos/nota", eje X de 0 a 10, eje Y (Alumnos/nota) de 0 a 7, con 5 barras coloreadas por categoría y su valor de frecuencia indicado dentro de la barra:

| Rango nota | Categoría | Frecuencia (altura) | Alumnos (valor interno) |
|---|---|---|---|
| 0-2 | Muy Deficiente (morado) | 3 | 9 |
| 3-4 | Suspenso (rojo) | 5 | 10 |
| 5-6 | Aprobado (amarillo/oliva) | 7 | 14 |
| 7-8 | Notable (verde) | 5.5 | 11 |
| 9-10 | Sobresaliente (azul) | 2 | 2 |

(Nota: los números dentro de las barras, 9/10/14/11/2, parecen representar el conteo real de alumnos, distinto de la altura visual de la barra en el eje Y; se transcribe tal cual aparece en la imagen.)

## Slide 14

Título: "Como interpretar el peso del salón de clase?". Fotografía de un salón de clases con alumnos sentados en carpetas individuales separadas (protocolo de distanciamiento, con mascarillas), en un aula moderna tipo UTEC con ventanales. Imagen decorativa/contextual, sin datos ni gráficos asociados en esta slide.

## Slide 15

Sección "/ 4. Histograma". Lista de preguntas guía para interpretar un histograma de pesos de pacientes, acompañada de una foto decorativa de un hombre pensativo (mano en el mentón):

- ¿Cuál es la tendencia central?
- ¿Cuál es el rango de los pesos?
- ¿Muchos o pocos pacientes por encima de 90 Kg?
- ¿Muchos o pocos pacientes por debajo de 60 Kg?
- ¿Cuántos tiene un IMC por encima de 23?
- ¿Cuántos tiene un IMC por debajo de 19?

## Slide 16

Título: "Conclusiones". Dos puntos numerados en corchetes:
- 01. Aprenderás a seleccionar las herramientas de calidad
- 02. Aprenderás a usar las herramientas de calidad

## Slide 17

Slide de cierre. Solo logo UTEC (Universidad de Ingeniería y Tecnología) centrado sobre fondo celeste con patrón hexagonal decorativo y cruz/círculo dorados decorativos. Sin contenido textual adicional (portada de cierre, decorativa).
