---
curso: IO2
titulo: Bienvenida IO2-2026-1__pptx
slides: 20
fuente: Bienvenida IO2-2026-1__pptx.pdf
---

## Slide 1

Portada. Título "BIENVENIDOS". Subtítulo: "Investigación de Operaciones II: Modelos Probabilísticos / Ciclo 2026-1". Profesora: "Prof. Claudia Antonini". Imagen decorativa: fotografía arquitectónica del edificio UTEC (fachada de concreto). Logos UTEC e Ingeniería Industrial (decorativo).

## Slide 2

Slide de índice. Título "Índice". Fondo gris oscuro con texto blanco. Lista con viñetas:
- Visión general
- Evaluación
- Recomendaciones y reglas de integridad académica
- R y RStudio

## Slide 3

Slide separador de sección (portada azul con foto del edificio UTEC de fondo, decorativa). Número grande "1" y título "VISIÓN GENERAL".

## Slide 4

Título "Visión general". Texto: "Éste es un curso obligatorio de la carrera de Ingeniería Industrial de UTEC y forma parte del área de analítica de decisiones. Aquí aprenderán un conjunto de herramientas del modelado probabilístico y la teoría de colas, input indispensable para el correcto diseño de simulaciones computarizadas. Las mismas son herramientas modernas útiles para enriquecer el proceso de toma de decisiones complejas y en proyectos de gran envergadura." Texto en negrita: "Es muy posible que necesiten ayuda, por favor, no duden en pedirla."

Cuatro imágenes a la derecha:
1. Fotografía de un almacén logístico con estanterías industriales altas cargadas de cajas, montacargas visible.
2. Diagrama de un sistema de colas: dos flechas de entrada etiquetadas λ1 y λ2 (clientes) entran a un bloque de "Colas", que conecta a varios círculos etiquetados μ1, μ2, ... μn (servidores), con puntos suspensivos indicando más servidores. Etiquetas debajo: "Clientes", "Colas", "Servidores".
3. Fotografía aérea de una esclusa/canal (tipo Canal de Panamá) con un barco de carga pasando entre compuertas, rodeado de vegetación.
4. Ilustración tipo icono de un supermercado/caja registradora: personas con carritos de compras haciendo fila hacia un cajero, con iconos de cámara de vigilancia y panel de analítica/gráficos conectados por líneas punteadas (sugiere analítica de datos aplicada a retail).

Texto grande al pie: "¡Bienvenidos!"

## Slide 5

Título "Diferencias con otros cursos". Cuatro subsecciones con texto:
- "Cambio de formato:" Las presentaciones tipo PPT no son la norma en este curso, son la excepción. Se espera que lleven apuntes en formato Quarto Document, accesible desde RStudio. Es conveniente trabajar desde el comienzo con un proyecto creado en R para colocar los archivos de cada clase. Las clases estarán en formato Quarto Presentation.
- "Abundancia de material:" hay abundante material para estudiar, publicado progresivamente para evitar abrumar. Es indispensable llevar la materia al día.
- "Investigación requerida:" deberán investigar temas por su cuenta, particularmente en el proyecto de campo (aprendizaje basado en proyectos), con materiales de lectura proporcionados que deben estudiar.
- "Conocimiento previo:" el curso requiere conocimientos previos de cálculo diferencial e integral en varias variables, probabilidades y ecuaciones diferenciales.

## Slide 6

Título "Una semana típica: técnicas sugeridas de estudio". Diagrama de línea de tiempo horizontal con puntos e hitos, describiendo el ciclo semanal de estudio:

- "Fin de la semana anterior / Comienzo de la semana siguiente": se publican en Canvas las soluciones de los ejercicios de refuerzo de la semana anterior (identificados con "S" de soluciones); se envía por correo y anuncio en Canvas la planificación de la semana siguiente.
- "Jueves — Clase No. 1": se recomienda que el alumno asista con puntualidad, haya resuelto los ejercicios de refuerzo de la semana anterior y corroborado que sus soluciones eran correctas y estaban bien escritas, y lleve un resumen de la teoría acumulada hasta el momento y la tenga clara.
- "Viernes — Clase No. 2": se sugiere que el estudiante se presente a clase habiendo estudiado el material de la clase del jueves y habiendo actualizado el resumen de la teoría.
- "De jueves a viernes — Ejercicios de refuerzo": el estudiante resuelve individualmente los ejercicios de refuerzo (identificados con "T" de tareas), interactúa con su grupo de estudio para resolver dudas que no pudo resolver solo, y aclara dudas en las sesiones de asesoría disponibles.
- "Al final de la semana — Soluciones de Ejercicios de refuerzo": el estudiante compara sus soluciones con las publicadas, presta atención no solo al resultado sino también al procedimiento y cómo está escrita la solución, corrige sus soluciones y actualiza su resumen de teoría.

## Slide 7

Slide separador de sección (portada azul con foto del edificio UTEC, decorativa). Número grande "2" y título "EVALUACIÓN".

## Slide 8

Título "Evaluación del curso". Diagrama de 4 círculos grandes conectados por flechas tipo "cinta" apuntando hacia la derecha, con desglose de cada componente:

- EP (20%) — fecha 15/05: Examen de desarrollo presencial. Se toma y califica en Gradescope.
- EF (30%) — fecha 10/07: Examen de desarrollo presencial. Se toma y califica en Gradescope.
- EC (30%): Exámenes cortos, presenciales y escritos.
- P (20%): Proyecto. P1 (5%) para recibir feedback. P2 (15%) sustentación final. 5 integrantes.

## Slide 9

Título "Fechas importantes". Línea de tiempo horizontal con hitos por semana:

| Semana | Hito |
|---|---|
| Semana 01 | Inicio del curso: Motivación y reglas del juego |
| Semana 03 | Evaluación continua 1: Esperanza condicional, varianza condicional y propiedad torre |
| Semana 05 | Evaluación continua 2: Propiedades de la exponencial |
| Semana 07 | Evaluación continua 3: Procesos de Poisson |
| Semana 08 | Examen parcial: Incluirá los temas de las tres primeras evaluaciones continuas |
| Semana 11 | Evaluación continua 4: Cadenas de Markov a tiempo discreto |
| Semana 14 | Evaluación continua 5: Cadenas de Markov a tiempo continuo |
| Semana 15 | Sustentaciones del proyecto |
| Semana 16 | Examen final: Incluirá los temas de las dos últimas evaluaciones continuas |

Nota al pie en negrita: "Adicionalmente, en semana 10 se tendrá la entrega parcial del proyecto (P1)."

## Slide 10

Título "Exámenes". Texto: "Tendremos dos exámenes de desarrollo. Normalmente se tratará de un caso real de alguna rama de ingeniería industrial y sobre dicho caso se formularán las preguntas a desarrollar."

Recuadro resaltado en amarillo "Advertencia:" con lista de las principales razones por las que los alumnos pierden puntos en los exámenes:
- Por interpretar incorrectamente el enunciado de la pregunta.
- Por no saber filtrar la información relevante del caso para alimentar los modelos probabilísticos estudiados.
- Por no definir correctamente los modelos probabilísticos a utilizar.
- Por no enunciar los parámetros y sus unidades de los modelos probabilísticos a utilizar.
- Por no validar las suposiciones del modelo probabilístico a utilizar en términos del enunciado del caso.
- Por no saber escoger correctamente el modelo probabilístico a utilizar.

Texto en negrita al pie: recomienda usar esta lista como checklist al resolver problemas de refuerzo.

## Slide 11

Título "Evaluación continua". Texto: "Tendremos cinco exámenes cortos para desarrollar sobre un contexto pequeño relacionado a temas variados."

Diagrama: cinco óvalos etiquetados EC1, EC2, EC3, EC4, EC5. Llaves agrupan EC1-EC2-EC3 bajo "Primera nota de la evaluación continua (20%)" y EC4-EC5 bajo "Segunda nota de la evaluación continua (10%)".

Viñetas: las evaluaciones continuas se realizarán de forma presencial y por escrito; al finalizar deben entregar la hoja de desarrollo; la calificación será publicada por el profesor en Gradescope. Cada examen tendrá duración máxima de 20 minutos y constará de cuatro preguntas de desarrollo. Recomendación: completar todos los ejercicios de la tarea y asistir a las asesorías.

## Slide 12

Título "Proyecto". Texto: el proyecto tiene dos entregas, la primera con peso de 5% y entrega obligatoria para recibir feedback. Se proporcionarán materiales y rúbricas para los avances. El feedback lo dará el asistente de cátedra. Es un trabajo grupal sobre simulaciones computarizadas.

Texto: "En el proyecto, deberán enfrentarse a un problema no estructurado, abierto y contextualizado."

Lista de aspectos a considerar:
- Interés: el problema debería ser de interés para la audiencia.
- Originalidad: el problema no debe estar previamente resuelto (desafío si se trabaja con datos existentes).
- Plausibilidad: qué tan sensato es pensar que se podrá atacar exitosamente el problema.
- Factibilidad: qué tan posible es que logren responder las preguntas.
- Especificidad: qué tan específico es el problema o la pregunta (más específico es mejor).

Recuadro amarillo "Advertencias:" con texto: "El proyecto será un sólo para todos los grupos. Sin embargo, cada equipo hará su propio proyecto."

## Slide 13

Slide separador de sección (portada azul con foto del edificio UTEC, decorativa). Número grande "3" y título "RECOMENDACIONES Y REGLAS".

## Slide 14

Título "Recomendaciones". Lista con viñetas:
- Mantengan el curso al día, asistiendo a clase puntualmente y siguiendo las recomendaciones de los docentes. Vengan preparados a clase, para que podamos aclarar sus dudas.
- Resuelvan los ejercicios de refuerzo y comparen sus soluciones con las publicadas.
- Aprovechen las asesorías que se van a dictar, aunque la asistencia no sea obligatoria.
- Hagan un esfuerzo por conocer a sus compañeros, los van a necesitar durante el curso.
- Ayúdense entre ustedes, no todos tienen las mismas dificultades y no todos tienen las mismas destrezas.
- Sean honestos, recuerden que deben mantener una conducta íntegra en todo momento. En este curso tenemos la política de cero tolerancia al plagio y a la copia.
- Si están en riesgo académico o deben mantener una beca, deben ser mucho más cuidadosos y diligentes con todo.

## Slide 15

Título "Reglas de integridad académica". Lista con viñetas:
- Todo estudiante matriculado tiene la obligación de conocer y cumplir las reglas de integridad académica (lista enunciativa, no limitativa). La copia y el plagio son infracciones muy graves en UTEC conforme al Reglamento de Disciplina, con sanción desde 2 semestres de suspensión hasta la expulsión.
- Si se identifica copia o plagio en evaluaciones individuales, el/la docente puede anular la evaluación.
- Si la evaluación es personal o grupal-individual, la interacción entre equipos o compañeros se considera copia o plagio. Si la evaluación calificada no indica que es grupal, se presume individual.
- La copia, plagio, el engaño y cualquier forma de colaboración no autorizada no serán tolerados y serán tratados según las políticas y reglamentos de UTEC, implicando consecuencias académicas y sanciones disciplinarias.
- Aunque se alienta discutir tareas y trabajar juntos, no se permite presentar el trabajo o ideas de otros como propias. No se permite el plagio de archivos informáticos, códigos, documentos o dibujos.

## Slide 16

Continuación de reglas de integridad académica (sin título propio visible, continúa el tema). Lista con viñetas:
- Si el trabajo de dos o más estudiantes es sospechosamente similar, se puede aplicar sanción académica a todos los estudiantes, sin importar quién proveyó la información o quién recibió la ayuda indebida. Se recomienda no proveer el desarrollo de evaluaciones a otros compañeros ni por motivos de orientación, dado que será considerado participación en copia.
- El uso de teléfonos celulares, aplicaciones de comunicación o cualquier medio de interacción entre estudiantes está prohibido durante evaluaciones o exámenes, salvo indicación expresa del docente. Es irrelevante la razón del uso del dispositivo.
- En caso de problema de internet durante la evaluación, comunicarse con el docente por el protocolo establecido; no comunicarse con compañeros pues generará presunción de copia.
- Se prohíbe tomar prestadas calculadoras o cualquier material de otro estudiante durante una evaluación, salvo indicación contraria del docente.
- Si el docente encuentra indicios de obtención indebida de información o incumplimiento de reglas, puede anular la prueba, advertir al estudiante y agendar cita con su Director de Carrera. Si el estudiante no asiste, podrá ser reportado para procedimiento disciplinario; una segunda advertencia será reportada para inicio del procedimiento disciplinario.
- Se recomienda estar atento a los datos de su evaluación; la consignación de datos que no correspondan a su evaluación será considerada indicio concluyente de copia.

## Slide 17

Slide separador de sección (portada azul con foto del edificio UTEC, decorativa). Número grande "4" y título "R y RStudio".

## Slide 18

Título "R y RStudio". Texto: el curso no es un curso de programación, pero estudiantes con experiencia en programación tendrán ligera ventaja. R ofrece herramientas poderosas para análisis estadístico completo; el ambiente de R es limitado y hostil (línea de comando); RStudio es una fachada para R. En RStudio se trabajará mayormente con los formatos R Notebook y Quarto, ambos basados en Markdown (formato textual simple; ejemplo: usar asteriscos para negritas en WhatsApp ya es una versión limitada de Markdown).

Los formatos R Notebook (cuaderno de trabajo) y Quarto (presentación) permiten crear documentos sofisticados con código vivo y librerías de R — ejemplo de "programación letrada". La narrativa se entremezcla con el código que resuelve el problema; generar el documento final se llama "tejer" (weave), permitiendo resultados reproducibles.

Texto: R es, junto con Python, estándar de industria para análisis estadístico; RStudio ofrece plataforma estable y gratuita para trabajar en R (o Python) enfatizando repetibilidad y correctitud del análisis.

## Slide 19

Título "Instalación de R y RStudio". Texto: la instalación es una tarea técnica relativamente sencilla que todos los estudiantes deben completar; instalar las versiones más recientes.

Lista numerada:
1. Instalar R — instalar la última versión y mantenerla actualizada. Disponible en https://www.r-project.org
2. Instalar RStudio — instalar la última versión y mantenerla actualizada. Disponible en https://rstudio.com
3. Configurar todo — descargar las librerías necesarias para usar los formatos RNotebook y Quarto, descargar los diccionarios en español, establecer un directorio de trabajo y abrir un proyecto para trabajar de manera organizada.

Texto final: "¡Buena suerte!"

## Slide 20

Slide de contacto/cierre. Título "Docente:" con fotografía de la profesora (mujer rubia con anteojos, fondo azul con burbujas decorativas) y recuadro: "Prof. Claudia Antonini — cantonini@utec.edu.pe".

Título "Asistente de cátedra:" con fotografía (hombre sonriente, fondo nocturno de ciudad con canal/río iluminado) y recuadro: "Fabián Vallebuona Zender — fabian.vallebuona@utec.edu.pe".

Logos UTEC e Ingeniería Industrial (decorativo). Texto grande al pie: "¡Éxitos!"
