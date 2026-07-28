---
curso: CALIDAD
titulo: Ses7_Dia_Lean
slides: 14
fuente: Ses7_Dia_Lean.pdf
---

## Slide 1

Portada. Título: "Diagnóstico Lean". Fondo celeste con foto de edificio UTEC (decorativa), logo UTEC y "Reinventa el mundo" (chrome decorativo).

## Slide 2

Título: "Objetivo".

Texto: "Aprenderás el uso de la Matriz de Análisis de Modo y Efecto de las Fallas (AMEF)".

## Slide 3

Título: "Contenido de sesión aquí" (agenda de la sesión).

Diagrama de 2 bloques numerados con corchetes decorativos:
- **01.** Pasos para elaborar el AMF
- **02.** Análisis de los riesgos

## Slide 4

Sección "/ 1 AMEF".

Texto: "Es una herramienta que nos permite identificar modos potenciales de falla en un sistema de clasificación determinado por la severidad, la frecuencia de ocurrencia y si existe un mecanismo de detección." (transcrito con corrección de errores tipográficos del original: "galla es" → "falla", "eciste" → "existe").

Imagen: infografía "Tipos de AMEF" con 3 columnas de color (fondo naranja/rojo):
- **De diseño**: ícono de smartphone con apps; texto "anticipa cualquier defecto en los productos".
- **De procesos**: ícono de nube con conexiones a nodos; texto "detecta problemas en la producción" (marca de agua "HubSpot" en la imagen, indicando que es infografía tomada de HubSpot).
- **De sistemas**: ícono de laptop con código; texto "revisa las funciones de los software".

Texto final: "Puesto que un AMFE depende de los miembros del comité que examinan los fallos, está limitado por su experiencia previa. Si un fallo no puede ser detectado, será necesario contar con ayuda externa de consultores que conocen una amplia variedad de problemas y fallos".

## Slide 5

Sección "/ 1 AMEF". Subtítulo: "Pasos a seguir:".

Recuadro negro "Número de Probabilidad de Riesgo" con fórmula destacada:

$$NPR = SEV \times OCC \times DET$$

Definiciones (texto blanco sobre fondo negro):
- **NPR**: Número de probabilidad de riesgo o de prioridad de riesgo. "El NPR es la multiplicación de la severidad de la falla, la ocurrencia de esta y su posible detección. Este será mejor en tanto sea menor."
- **SEV**: Severidad. "Es el impacto de mayor o menor intensidad en que la falla de un proceso puede repercutir en el cliente (interno o externo) y su comportamiento respecto a nuestros servicios."
- **OCC**: Ocurrencia. "Frecuencia en la que puede ocurrir una falla."
- **DET**: Detección. "Posibilidad de identificar la falla en algún momento durante el proceso."

## Slide 6

Sección "/ 1 AMEF". Tres tablas de escalas de valoración (fondo negro, encabezados amarillos):

**Tabla SEVERIDAD**
| Efecto | Rank |
|---|---|
| Muy peligroso | 10 |
| Peligroso | 8 |
| Moderado | 6 |
| Bajo | 3 |
| No existe | 1 |

**Tabla OCURRENCIA**
| Efecto | Rank |
|---|---|
| Muy frecuente | 9 |
| Frecuente | 8 |
| Medianamente frecuente | 6 |
| Casi nunca | 1 |

**Tabla DETECCIÓN**
| Efecto | Rank |
|---|---|
| No existe | 10 |
| Supervisión | 5 |
| Gráficas de control | 4 |
| Poka Yoke | 3 |
| Andon | 2 |

## Slide 7

Sección "/ 1 AMEF". Texto: "Un AMFE debe ser actualizado:"

Recuadro verde claro con lista de condiciones de actualización:
- Si la retroalimentación recibida de los usuarios indica que hay un problema.
- Cambios en las condiciones de funcionamiento.
- Al iniciar un ciclo (nuevo producto / proceso).
- Cambios en el diseño.
- Aprobación de nuevas leyes y normativas de parte del estado.

## Slide 8

Sección "/ 2. ANALISIS DE CAPACIDAD".

Diagrama de flujo horizontal: **Entradas** (flecha verde) → **Proceso** (caja roja 3D) → **Salidas** (hexágono azul), con flechas cian conectando los 3 elementos en secuencia.

Dos recuadros de definición lado a lado:
- **Capacidad** (amarillo): "Habilidad basada en rendimiento demostrado, de un proceso, en satisfacer los requerimientos del cliente."
- **Capacidad Medida** (turquesa): "Capacidad del proceso cuantificada, de datos que son resultado de mediciones de trabajo realizado por el proceso."

## Slide 9

Sección "/ 2. ANALISIS DE CAPACIDAD". Subtítulo interno: "Análisis de Normalidad" / "Prueba de Normalidad".

Imagen izquierda: histograma con curva de campana verde superpuesta, con flecha roja bidireccional debajo etiquetada "Variación de los datos".

Imagen derecha: captura de pantalla de software estadístico (tipo Minitab) "Probability Plot for Grupos - LSXV Estimates-Complete Data", con 3 gráficos de probabilidad (Smallest Extreme Value, Normal, Logistic) mostrando puntos rojos vs. línea de referencia azul en cada uno, y una tabla de "Correlation Coefficient": Smallest Extreme Value 0.957, Normal 0.985, Logistic 0.975.

Recuadro amarillo inferior: "Si los datos son normales, se podrá hacer el análisis de la Capacidad del Proceso."

## Slide 10

Sección "/ 2. ANALISIS DE CAPACIDAD".

Dos recuadros amarillo claro de texto:
- "Para analizar si un indicador es capaz de cumplir con las especificaciones, se suele utilizar el índice de capacidad"
- "Diremos que un indicador es capaz de cumplir con las especificaciones cuando su dispersión es menor que la distancia entre especificaciones."

Dos diagramas de campana comparativos:
- Campana ancha entre límites LIE-LSE etiquetada "Cp = 1" ("Bajo Cp"), con flechas indicando "alta probabilidad de defectos" en ambas colas.
- Campana angosta y alta entre límites LIE-LSE etiquetada "Cp = 2" ("Alto Cp"), con flechas indicando "baja probabilidad de defectos" en ambas colas.

Fórmula (recuadro celeste):

$$Cp = \frac{LSE - LIE}{6\sigma}$$

Tabla de interpretación (recuadro naranja):
| Rango | Interpretación |
|---|---|
| Cp < 1 | INCAPAZ |
| 1 < Cp < 1.33 | APENAS CAPAZ |
| 1.33 < Cp < 2 | CAPAZ |
| Cp > 2 | MUY CAPAZ |

## Slide 11

Sección "/ 2. ANALISIS DE CAPACIDAD". Subtítulo: "CENTRAMIENTO (Cpk)".

Dos recuadros amarillo claro:
- "No solo interesa ver si el indicador puede cumplir con las especificaciones, nos interesa saber si está centrado respecto a las mismas."
- "Para analizar esto, existe el índice de centramiento denominado Cpk que mide la menor distancia del promedio de los datos a las especificaciones comparada contra el ancho de media distribución."

Fórmula (recuadro celeste), con anotaciones "Especificación" y "Promedio de los datos" apuntando a los términos:

$$Cpk = Min\left(\frac{LSE - \bar{X}}{3\sigma}, \frac{\bar{X} - LIE}{3\sigma}\right)$$

Imagen derecha: dos curvas de campana superpuestas entre límites LSL y USL — una desplazada ("Non-centered mean; Cp<1") y otra centrada en la media ("Centered mean; Cp>1"), mostrando visualmente el efecto del descentramiento.

## Slide 12

Título superior: "Como interpretar las Gráficas de Control ?". Sección "/ 2. ANALISIS DE CAPACIDAD".

Captura de pantalla de software estadístico (tipo Minitab): "Process Capability of % de Saturación".

- Histograma de datos con curva ajustada, líneas verticales marcando LSL (rojo), Target (verde) y USL (rojo).
- Recuadro "Process Data": LSL=0, Target=0.1, USL=0.2, Sample Mean=0.0626415, Sample N=106, StDev(Within)=0.107208, StDev(Overall)=0.107447.
- Leyenda: línea roja "Within", línea negra discontinua "Overall".
- Recuadro "Potential (Within) Capability": Cp=0.31, CPL=0.19, CPU=0.43, Cpk=0.19, CCpk=0.31.
- Recuadro "Overall Capability": Pp=0.31, PPL=0.19, PPU=0.43, Ppk=0.19, Cpm=0.29.
- Tabla "Observed Performance": PPM<LSL=0.00, PPM>USL=103773.58, PPM Total=103773.58.
- Tabla "Exp. Within Performance": PPM<LSL=279509.11, PPM>USL=100055.21, PPM Total=379564.32.
- Tabla "Exp. Overall Performance": PPM<LSL=279947.66, PPM>USL=100557.92, PPM Total=380505.59.

(Slide muestra un caso real de proceso con Cp y Cpk muy bajos, es decir incapaz y descentrado.)

## Slide 13

Título: "Conclusiones".

Dos puntos numerados con corchetes decorativos:
- **01.** Aprenderás a identificar modos de fallas y sus efectos
- **02.** Medir los riesgos en base al Nivel de Riesgo (NPR)

## Slide 14

Slide de cierre. Solo logo UTEC grande centrado sobre fondo celeste degradado (decorativa, sin contenido de curso).
