---
curso: CALIDAD
titulo: S13_SMED_Caso
slides: 17
fuente: S13_SMED_Caso.pdf
---

## Slide 1

Portada del caso de tesis (decorativa: fondo de fotografía de edificio de vidrio en blanco y negro, logo de la empresa "Servicios Plásticos Industriales S.A.").

**REDUCCIÓN DEL TIEMPO DE SET-UP APLICANDO SMED EN UNA EMPRESA INYECTORA DE PLÁSTICOS**

Alumno: Julio Andres Tovar Lagos
Asesor: Alejandro Gallegos Chocce

## Slide 2

Slide de índice, con icono decorativo de portapapeles con check. Lista numerada con círculos de colores alternados (azul oscuro/celeste):

1. JUSTIFICACIÓN
2. INTRODUCCIÓN
3. METODOLOGÍA
4. IMPLEMENTACIÓN SMED
5. RESULTADOS (numerado como "3" en la slide, error tipográfico del original)

## Slide 3

**JUSTIFICACIÓN** — Diagrama de flujo del proceso de la empresa, con 10 pasos numerados en círculos azules que recorren el flujo completo:

1. Cliente → envía "Cantidades requeridas" a Comercial.
2. Comercial (arriba a la derecha) recibe cantidades requeridas del cliente.
3. Planificación (centro, ícono de base de datos/cilindro) recibe "Requerimiento" de Logístico y "Cantidades requeridas" de Comercial.
4. Logístico (arriba a la izquierda) envía "Orden de compra" a Proveedor externo y recibe "Requerimiento" desde Planificación.
5. Proveedor externo recibe "Solicitud" de Logístico.
6. Almacén en MP (materia prima) recibe el flujo desde Proveedor externo vía camión (icono de camión).
7. Inyección: primer proceso de producción, con recuadro rojo resaltando **T(cambio) = 160.93 minutos**; recibe "Plan de producción" desde Producción, con una parada de máquina (icono de estrella verde "Parada de máquina") antes de iniciar.
8. Producción (centro) despacha "Plan de producción" a Inyección, Serigrafía y Etiquetado.
9. Etiquetado: tercer proceso, T(cambio) = 15 minutos; empuja (PUSH) hacia Almacén en PT.
10. Almacén en PT (producto terminado) → despacha vía camión hacia Cliente.

Entre Inyección y Serigrafía hay flujo "PUSH"; Serigrafía tiene T(cambio) = 5 minutos; entre Serigrafía y Etiquetado también "PUSH".

Barra de navegación inferior con 5 pestañas (JUSTIFICACIÓN activa en azul claro, resto en gris): JUSTIFICACIÓN | INTRODUCCIÓN | METODOLOGÍA | IMPLEM. SMED | RESULTADOS (esta barra se repite en casi todas las slides siguientes, se omite su descripción repetida).

## Slide 4

**JUSTIFICACIÓN — Situación actual de la empresa** (alcance: mayo a noviembre 2017).

Tabla de procesos de cambio:

| Procesos de cambio | Tiempo de cambio (min) | Configuraciones x Semestre | Tiempo total (min) |
|---|---|---|---|
| Cambio por producto (resaltado en amarillo) | 161.00 | 20 | 3220 |
| Cambio por material | 20.00 | 5 | 100 |
| Cambio por color | 10.00 | 5 | 50 |
| Etiquetadora | 15.00 | 20 | 300 |
| Serigrafia | 5.00 | 20 | 100 |
| **Total** | | | **3770** |

Una flecha roja conecta la fila "Cambio por producto" con un recuadro naranja que indica:
- 9.31% Cambio por producto
- 10.90% Cambios totales

A la derecha, texto en rojo tipo alerta: "PROBLEMA: DEMORA EN LA ENTREGA ('1 SEMANA DESPUÉS')" y cita destacada: "...sólo el proceso de cambio de molde consume el 9.31% del tiempo total, es decir aproximadamente 54 horas..."

Tabla inferior "Paradas de máquina":

| Paradas de máquina | Valor estimado |
|---|---|
| 20 Configuraciones / Semestre | S/. 58,902.62 semestral** / 13,296.30 und sin producir |

Una flecha roja apunta desde esta tabla a un recuadro amarillo: "LUCRO CESANTE".

Notas al pie: "* No se considera el mes de Julio por ser un mes atípico." / "** Unidades equivalentes (Bandejas portabotellas)."

## Slide 5

**OBJETIVOS DE LA TESIS** — texto central: "Reducir la media en los tiempos de setup en los cambios de molde por producto aplicando la metodología SMED en la empresa en estudio."

Cinco objetivos específicos numerados en cuadros azules, distribuidos en layout tipo mapa (fondo con formas geométricas triangulares grises decorativas):

1. Implementación de la metodología 5S en paralelo
2. Implementar cada fase de la metodología SMED
3. Desarrollar un plan piloto con las mejoras propuestas en áreas definidas
4. Evaluar el impacto de las mejoras aplicadas
5. Evaluación de costo-beneficio del proyecto

## Slide 6

**INTRODUCCIÓN** — tres columnas separadas por línea punteada azul vertical:

**Columna 1: Sector plástico en el mundo y Perú**
Cita: "China es uno de los principales exportadores del mundo con una participación en el mercado del 24%..." (referencia a gráfica: "Producción mundial de plástico por región del 2012", no reproducida en la slide, solo mencionada como pie de figura).
Cita: "El polímero que se fabrica más en el mundo es el polipropileno con un 19%, seguido del polietileno de baja densidad con un 17%..." (referencia a gráfica: "Producción mundial de plástico por categoría 2012 en porcentaje").

**Columna 2: Lean Manufacturing**
Recuadro con texto "LEAN MANUFACTURING" conectado con flecha a definición: "...'Lean Manufacturing es un sistema integrado que incluye varias prácticas, en las cuales SMED es una de las más representativas...'". acorde a Green y Dick [15]*.

**Columna 3: SMED**
Diagrama esquemático: dos bloques de producción "PRODUCCIÓN 'A'" (con 4 iconos de botellas verdes con check) y "PRODUCCIÓN 'B'" (también 4 botellas), separados por una flecha bidireccional etiquetada "TIEMPO DE SET UP". Debajo del tiempo de setup hay una estrella amarilla con texto "Esperas / Movimientos / Sobreprocesos", que apunta (flecha amarilla hacia arriba) desde un recuadro "SMED" conectado también con flecha desde el recuadro "LEAN MANUFACTURING".
Debajo, 3 etapas de SMED listadas:
- Etapa 1: Identificación y separación de actividades internas y externas [23]
- Etapa 2: Convertir las actividades internas a externas [25]
- Etapa 3: Agilización de todos los aspectos de la operación de configuración [26]

Referencias: Van Goubergen, D. (2000) [23], McIntosh, R.I. (2001) [25] y Reik, M.P. (2006) [26].

## Slide 7

**METODOLOGÍA — Diseño de la metodología en la investigación.** Diagrama de flujo horizontal de 6 fases en forma de flechas/pentágonos color naranja (la última, "Despliegue interno", resaltada en amarillo con borde punteado rojo):

1. **Determinar el alcance**: Análisis de productos mediante Diagrama de Pareto; VSM; Tamaño de muestra.
2. **Estudio de las actividades**: Clasificación de las actividades internas y externas; Análisis detallado de cambio de molde; Plan e inicio de 5S.
3. **Diseño del nuevo plan de trabajo**: Convertir las actividades internas a externas; Generación de lluvias de ideas de mejora con gerencia, jefatura y operarios; Ideas de mejoras estructuradas; Seguimiento 5S; Análisis de la "Y" y las "X" actual.
4. **Implementación del programa piloto**: Control y seguimiento del piloto en área seleccionada; Seguimiento 5S.
5. **Verificación del programa piloto**: Feedbacks de gerencia y jefatura; Toma de nueva data para el análisis; Seguimiento 5S; Análisis de la "Y" y las "X" después de las mejoras.
6. **Despliegue interno**: Estandarizar las actividades; Estandarizar el tiempo de setup; Manuales; Seguimiento 5S.

## Slide 8

**METODOLOGÍA — Herramientas de medición.** Cinco círculos naranjas (uno más grande, "Estudio de tiempos", a la derecha) con listas debajo:

- **Observación directa**: Estudio de actividades; Interacción de operario-máquina y herramientas; Funciones de cada operario.
- **Entrevistas no estructuradas**: Preguntas abiertas según [39] y [40]. (cita: R.H. Sampieri, et al. Metodología de la investigación. Vol. 1. México: Mcgraw-hill, 1998.)
- **Focus group**: Reuniones con gerencia, jefatura y operarios involucrados; Recomendaciones de mejora.
- **Grabación de video**: Cámara de video; Análisis más detallado.
- **Estudio de tiempos** (lista numerada 1-8): 1. Registrar toda información del proceso. 2. Descomponer la operación en actividades. 3. Analizar el desglose y definir tamaño de muestra. 4. Medir los tiempos. 5. Determinar la velocidad. 6. Conversión de tiempos. 7. Determinar los suplementos. 8. Determinar el tiempo estándar. [41]

## Slide 9

**METODOLOGÍA** — Tabla de variables:

| Tipos de variable | | Definición de variables | Prueba estadística | Fuente | Recolección de data |
|---|---|---|---|---|---|
| Dependientes | Y1 continua | Media del tiempo de SETUP | | Personal de la empresa | Se obtendrán mediante la toma de tiempos a cada operario que realice un cambio de formato durante un periodo |
| Independientes | X1 continua | Número de tareas que agregan valor por operario | Correlación y Regresión | | |
| | X2 continua | Porcentaje de utilización del operario (promedio) | Correlación y Regresión | | |
| | X3 continua | Porcentaje de disponibilidad de herramientas | Correlación y Regresión | | |

Ecuaciones (texto plano, no LaTeX en la slide):
- Ecuación 1: # de tareas AV = (# tareas AV / # de tareas totales)
- Ecuación 2: % de utilización = (# de tareas realizadas por el operario / # de tareas totales)
- Ecuación 3: % de disponibilidad = (# de veces que dispone de una herramienta / # de veces total que buscó una herramienta)

Definiciones adicionales de variables (no incluidas en la tabla):
- **X4: Destreza del operario** — Es la habilidad que el operario ha adquirido durante los años de experiencia en la realización de un cambio de molde.
- **X5: Estrés del operario** — Es el cansancio mental provocado por una carga alta de trabajo en la rutina diaria del operario.

## Slide 10

**METODOLOGÍA — Validación de data.** Diagrama tipo "arco" naranja con 4 puntos numerados (1-4) que conectan con cuatro bloques de contenido en las esquinas:

1. (abajo-izquierda) **Prueba de Normalidad de la data** — incluye captura de gráfico Minitab "Gráfica de probabilidad de Pct. grasa - Normal", con estadísticos: Media=16.46, Desv.Est.=2.316, N=20, AD=0.339, Valor p=0.463. Eje X "Pct. grasa" (10-22), eje Y "Porcentaje" (1-99).
2. (arriba-izquierda) **Análisis de Correlación y Regresión** — con 3 mini-gráficos de dispersión: "CORRELACION POSITIVA ρ>0" (puntos ascendentes), "CORRELACION NULA ρ=0" (puntos dispersos), "CORRELACION NEGATIVA ρ=0" (puntos descendentes, debería ser ρ<0).
3. (arriba-derecha) **Prueba de hipótesis** — gráfico de curva normal con zonas de rechazo α/2 en ambas colas, "Zona de Aceptación" al centro entre -Z₀ y Z₀.
4. (abajo-derecha) **T de 2 muestras** — fórmulas de hipótesis:
   $$H_0 = \mu_{ST\ Antes} = \mu_{ST\ Después}$$
   $$H_A = \mu_{ST\ Antes} > \mu_{ST\ Después}$$
   Fuente: Support Minitab.

## Slide 11

**IMPLEMENTACIÓN DE SMED.** Gráfico de burbujas/matriz Importancia (eje Y) vs Dificultad (eje X), con 3 elipses verdes punteadas ubicadas en la zona de alta importancia:
- Elipse 1 (más a la izquierda, menor dificultad): PLAN 1, PLAN 2
- Elipse 2 (centro): PLAN 3
- Elipse 3 (más a la derecha, mayor dificultad): PLAN 4

Tabla de planes:

| PLANES | DESCRIPCIÓN | VARIABLES |
|---|---|---|
| PLAN 1 | 5S | X1 y X3 |
| PLAN 2 | Encargado de herramientas | X2 y X3 |
| PLAN 3 | Identificación rápida de moldes | X1 y X2 |
| PLAN 4 | Rediseño de moldes | - |

## Slide 12

**IMPLEMENTACIÓN DE SMED** — tres columnas separadas por líneas punteadas verticales:

**PLAN 1 — Evaluación de nivel de 5S actual**: gráfico radar (spider chart) con 4 ejes (General, Selección, Orden, Limpieza), línea naranja mostrando cobertura cercana al 85% en la mayoría de ejes; junto a él, barra vertical de progreso mostrando 85%. Indicador: 37% Nivel crítico → (flecha azul) → 85% Bien.

**PLAN 2**: dos fotografías reales de la planta — (1) estantería con cajas/organizadores de pernos y tornillos etiquetados ("PERNOS SOCKET", etc.), (2) caja amarilla organizadora con llaves de tuerca ordenadas. Indicador: 51% Disponibilidad de herramientas → (flecha azul) → 92%.

**PLAN 3**: Indicador: 6.5 min Buscar molde → (flecha azul) → 3.8 min (42% reducción).

## Slide 13

**IMPLEMENTACIÓN DE SMED** — Tabla comparativa de 3 etapas (Situación actual | Acciones inmediatas | Implementación de plan):

| | Situación actual | Acciones inmediatas | Implementación de plan |
|---|---|---|---|
| ACTIVIDADES | 32 | 32 | 28 |
| TRANSPORT | 12 (37%) | 11 (34%) | 7 (25%) |
| WAITING TIME | 9 (28%) | 7 (21%) | 3 (10%) |
| % ACT. INTERNAS | 100% | 82% | 79% |
| % ACT. EXTERNAS | 0% | 18% | 21% |
| TIEMPO DE SETUP | 161 min | 133.8 min | 78 min |
| % DE ACT EXTERNAS - Tsetup | 0% | 20% | 35% |

## Slide 14

**RESULTADOS** — Análisis de T de setup antes y después (globo de texto azul indicándolo).

Tabla de muestras y prueba de hipótesis:

| Muestras (Antes de SMED) | Muestras (Después de SMED) | P-valor | ¿Existe diferencia significativa? SI/NO | Rango de diferencia |
|---|---|---|---|---|
| 32 Actividades | 28 Actividades | 0.00 | SI (marcado con X) | 40 < > 71 min |

Hipótesis:
- Ho: No existe diferencia significativa en el tiempo de setup actual y después de la implementación de SMED.
- Ha: Existe diferencia significativa en el tiempo de setup actual y después de la implementación de SMED.

Tabla de datos de muestras (8 filas):

| Muestra | Data actual | Data nueva |
|---|---|---|
| 1 | 199.5 | 120.1 |
| 2 | 152 | 116.9 |
| 3 | 170.5 | 109.8 |
| 4 | 159 | 107.3 |
| 5 | 152 | 100.9 |
| 6 | 141 | 98.36 |
| 7 | 151 | 92.8 |
| 8 | 161.5 | 95.5 |

Captura de gráfico Minitab "Gráfica de caja de Setup Act., Setup Mej.": boxplot comparando "Setup Act." (mediana ~155, rango ~140-200, un outlier marcado con asterisco cerca de 200) vs "Setup Mej." (mediana ~105, rango ~90-125), con línea conectando las medianas mostrando tendencia claramente descendente. Eje Y "Datos" de 100 a 200.

## Slide 15

**RESULTADOS** — Análisis de variables "X" antes y después (globo de texto azul indicándolo).

Tabla 1 (antes, incluye X1):

| Variable | Descripción de variable | P valor | R cuadrado |
|---|---|---|---|
| X1 (recuadro verde) | % de # tareas que AV por operario | 0.358 | 98.92% |
| X2 | % de Utilización del operario | 0.001 | |
| X3 | % de Disponibilidad de herramientas | 0.102 | |

Nota: "Se elimina la variable 'X1' ya que su P valor es mayor a 0.05".

Tabla 2 (después, sin X1):

| Variable | Descripción de variable | P valor | R cuadrado |
|---|---|---|---|
| X2 (recuadro rojo) | % de Utilización del operario | 0.000 | 98.84% |
| X3 | % de Disponibilidad de herramientas | 0.034 | |

Nota lateral: "PLAN 2: Encargado de herramientas".

Conclusión en negrita: "En conclusión, la variable 'X2' afecta significativamente en la reducción del tiempo de setup de cambio de molde, seguido de la variable 'X3'."

## Slide 16

**RESULTADOS** — Tabla "Rango de disminución por categorías":

| Reducción del Tiempo de setup total (min) | Aumento de producción estimada al mes | Disminución del lucro cesante |
|---|---|---|
| 40 < > 71 | 8848 < > 15705 | 39268 < > 69701 |

Flecha azul conecta esta tabla con otra tabla "Paradas de máquina":

| Paradas de máquina | Valor estimado |
|---|---|
| 20 Configuraciones / Semestre | S/. 58,902.62 semestral** / 13,296.30 und sin producir |

Texto: "Es entonces que al disminuir el tiempo de setup en un rango de 40 < > 71 min, aumentará la producción estimada del mes de 8848 < > 15705 unid. Permitiendo de esta manera mejorar los ingresos de la compañía."

## Slide 17

**CONCLUSIONES** — slide de solo texto (dos bullets):

- Se logró el objetivo general planteado inicialmente al evidenciar una reducción significativamente del tiempo de setup en el cambio de molde mediante la prueba piloto implementada, de un total de 161 min a 78min.
- Esta prueba estima una reducción entre 40 y 71 min al tiempo total que demanda la configuración de línea. Siendo este ahorro de tiempo, aprovechado para aumentar la disponibilidad de la máquina y producir una mayor cantidad de productos, donde se calcula que se estaría produciendo entre 8,848 y 15,705 unidades de yogurt más al mes.
