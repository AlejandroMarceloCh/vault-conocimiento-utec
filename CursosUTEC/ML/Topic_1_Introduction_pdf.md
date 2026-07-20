---
curso: ML
titulo: Topic 1 - Introduction
slides: 25
fuente: Topic 1 - Introduction.pdf
---

## Slide 1

INTRODUCCIÓN A MACHINE LEARNING

**Figura:** Imagen de portada, un pasillo/túnel futurista azul con la silueta de una persona junto a un brazo robótico caminando hacia la cámara. Elementos decorativos de líneas punteadas azules y amarillas en la parte inferior.

## Slide 2

ACERCA LA CLASE

➔ Temas que cubriremos: Aprendizaje supervisado (regresión y clasificación), extracción de características, reducción de dimensionalidad, aprendizaje no supervisado (clustering), redes neuronales (MLP, CNN, RNN) y aprendizaje por refuerzo (multi-armed bandit).

➔ Requisitos previos: Esta clase requiere conocimientos previos de programación (por ejemplo, en Python), probabilidad y estadística (como teoría de la probabilidad y procesos aleatorios), álgebra lineal y cálculo.

➔ Importante: Si no cuentas con estos conocimientos, estar aquí no será productivo. Es como intentar seguir una clase de Japonés III sin haber cursado Japonés I y II.

**Figura:** Fotografía lateral de una persona (hombre con lentes) explicando algo en una laptop/documento a otra persona (mujer), superpuesta con un tono azul y líneas decorativas punteadas azules y amarillas.

## Slide 3

REFERENCIAS

**Prerrequisitos**

➔ Hay una colección fantástica de visualizaciones de álgebra lineal en YouTube creada por 3Blue1Brown (Grant Sanderson), que comienza con la lista de reproducción The Essence of Linear Algebra. Las recomiendo mucho, incluso si crees que ya entiendes álgebra lineal. No basta con saber resolver ecuaciones matriciales; también es fundamental tener una intuición geométrica de lo que todo eso significa.

➔ Aquí tienes un resumen sobre matemáticas para machine learning escrito por Garrett Thomas.

➔ La clase de machine learning de Stanford también ofrece repasos adicionales de álgebra lineal y teoría de la probabilidad.

**Machine Learning Class**

➔ Pattern Recognition and Machine Learning, Christopher Bishop

➔ Machine Learning, Tom Mitchell.

➔ Machine Learning: a Probabilistic Perspective, Kevin Murphy.

➔ *A Course in Machine Learning, Hal Daumé III. Online only.

## Slide 4

CONTACTO

Email: mloaiza@utec.edu.pe

Office Hours: Programación pero previa coordinación

## Slide 5

FAQ

➔ ¿Cuál es la dinámica para los quizzes y exámenes?

Los estudiantes son responsables de asegurarse de estar preparados para rendir los exámenes usando Proctorio, con una conexión a internet estable. Si no puedes cumplir con estas condiciones, por favor contacta al profesor con anticipación.

➔ ¿Se pueden pedir extensiones para los proyectos?

Las fechas de entrega de los proyectos suelen ser estrictas, pero pueden concederse extensiones en circunstancias especiales.

➔ ¿Hay oportunidades para puntos extra o trabajos de recuperación?

No hay asignaciones oficiales de puntos extra ni trabajos de recuperación para exámenes o proyectos. Sin embargo, se pueden otorgar puntos adicionales por trabajo que vaya más allá del alcance del curso.

➔ ¿Qué debo hacer si mi grupo no me responde?

Informa al profesor lo antes posible para que se puedan tomar las medidas necesarias.

## Slide 6

FAQ

➔ Preferiría no aprender a construir modelos de machine learning interesantes, y en su lugar, que un modelo interesante lo haga por mí. ¿Puedo simplemente pedirle a un LLM que escriba mi código?

¡No! Uno de los objetivos clave de aprendizaje de este curso es que seas capaz de depurar código de machine learning que no funciona. Hemos descubierto que una de las mejores formas de darles exposición a ese tipo de código es dejar que lo escriban ustedes mismo.

## Slide 7

¿QUÉ ES MACHINE LEARNING?

**Figura:** Slide de transición con fondo degradado azul, comillas decorativas grandes en las esquinas superior e inferior (marcos punteados amarillos), y el título centrado.

## Slide 8

¿Qué es Machine Learning?

¿Cómo podemos resolver un problema específico?

Como científicos de la computación, escribimos un programa que codifica un conjunto de reglas útiles para resolver dicho problema

¿Cómo podemos hacer que un robot cocine?

**Figura:** Fotografía de un robot humanoide industrial (marca Motoman) con dos brazos manipulando comida (una hamburguesa y otro alimento) sobre una plancha de cocina.

## Slide 9

¿Qué es Machine Learning?

¿Cómo podemos resolver un problema específico?

Como científicos de la computación, escribimos un programa que codifica un conjunto de reglas útiles para resolver dicho problema

En muchos casos, es muy difícil especificar esas reglas; por ejemplo, dado una imagen, determinar si hay un gato en ella.

**Figura:** Tres fotografías de gatos en distintas poses (un gatito atigrado recostado, un gatito naranja asomándose de una maceta, un gato gris y blanco estirando las patas) ilustrando la variabilidad visual del problema de reconocimiento de gatos.

## Slide 10

¿Qué es Machine Learning?

Los sistemas de aprendizaje no se programan directamente para resolver un problema; en su lugar, desarrollan su propio programa basándose en:

Ejemplos de cómo deberían comportarse.

Experiencia de prueba y error al intentar resolver el problema.

Diferencia de la informática tradicional: requiere implementar una función desconocida, pero solo se tiene acceso, por ejemplo, a pares de entrada-salida de muestra (ejemplos de entrenamiento). Aprender simplemente significa incorporar la información de los ejemplos de entrenamiento en el sistema.

**Figura:** Dos diagramas de flujo comparativos. Izquierda: "Inputs" y "Patterns" → rombo "Traditional software" → "Outputs". Derecha: "Inputs" y "Outputs" → rombo "Machine learning" → "Patterns". Ilustra que el software tradicional produce salidas a partir de entradas y reglas/patrones, mientras que machine learning produce los patrones (reglas) a partir de entradas y salidas conocidas.

## Slide 11

Machine Learning (Hace mucho, mucho tiempo…)

**Figura:** Collage de dos imágenes superpuestas. Izquierda: cuadrícula de dígitos manuscritos (muestras del dataset MNIST: 7, 4, 7, 3, 0, 8, 1, 1, 2, 7, 4, 0, 7, 4, 9, 7, 4, 0, 2, 0). Derecha: captura de pantalla de una interfaz de correo electrónico mostrando carpetas (Inbox, Drafts, Archive, Sent, Groups, Trash, Junk resaltada, Clutter, Conversation History, Subscribed Public Folders) superpuesta sobre una interfaz de recomendaciones de streaming tipo Netflix (secciones "Top Picks for Henry", "TV Comedies", "Because you watched Somm" con miniaturas de series como Voltron, New Girl, Parenthood, Arrow, On My Block, The Good Place).

## Slide 12

Machine Learning (Hace no tanto tiempo…)

**Figura:** Tres imágenes. 1) Collage de teléfonos móviles mostrando asistentes de voz (Siri: "What can I help you with?", Cortana, Google Assistant) y un altavoz inteligente (Amazon Echo). 2) Fotografía de un vehículo autónomo (Ford Fusion con sensores/lidar en el techo, marca Argo AI) circulando por un puente urbano. 3) Logo de AlphaGo (círculo de puntos con espiral azul y texto "AlphaGo").

## Slide 13

Tareas que requieren machine learning

¿Qué hace que un 2 sea un 2?

**Figura:** Cuadrícula de dígitos manuscritos del dataset MNIST organizados en tres filas. Fila superior: variantes de 0, 1 y 2. Fila del medio: múltiples variantes manuscritas del dígito 2 (recuadradas en verde) junto a un 3 mal clasificado o ambiguo (recuadrado en rojo, parece un 2/3). Fila inferior: variantes de 3, 4, 5 con un caso ambiguo recuadrado en rojo. Ilustra la alta variabilidad visual dentro de una misma clase de dígito.

## Slide 14

Tareas que requieren machine learning

¿Robots cocinando?

**Figura:** Captura de un artículo periodístico titulado "Robots learn to cook by watching YouTube", subtítulo "When it comes to learning how to cook, it turns out that robots may not be so different from humans after all... or are they?", fechado January 20, 2015, por Michelle Starr (@riding_red), sección Sci-Tech. Incluye texto: "When it comes to teaching robots how to do things, there are some very key differences. A human knows what you mean when you say 'I need a cup'. A robot needs to be taught that that means it has to turn around, go to the cupboard, open it, take out the cup, close the cupboard, turn back around, return to you, manoeuvre the cup over the bench, and release the cup." Fotografía de un robot rojo de dos brazos con dos hombres trabajando en una habitación con luz roja.

## Slide 15

¿Qué es Machine Learning?

**Figura:** Ilustración de un bowl de madera con "ingredientes" etiquetados como fundamentos matemáticos de ML: una botella vertiendo aceite etiquetada "Optimization", un pepino cortado etiquetado "Probability & Statistics", un tomate etiquetado "Linear Algebra", un crouton etiquetado "Calculus", y una vaina verde etiquetada "Computer Science". Metáfora visual de que ML es una combinación de estas disciplinas.

## Slide 16

¿Por qué usar aprendizaje automático?

➔ Es muy difícil escribir programas que resuelvan problemas como reconocer un dígito escrito a mano.

◆ ¿Qué distingue un 2 de un 7?

◆ ¿Cómo lo hace nuestro cerebro?

➔ En lugar de escribir un programa a mano, recopilamos ejemplos que especifiquen la salida correcta para una entrada dada

➔ Un algoritmo de aprendizaje automático toma estos ejemplos y produce un programa que realiza la tarea.

◆ El programa generado por el algoritmo de aprendizaje puede verse muy diferente de un programa escrito manualmente. Puede contener millones de números.

◆ Si lo hacemos bien, el programa funciona tanto para casos nuevos como para aquellos con los que lo entrenamos.

## Slide 17

Definiendo una solución de ML

**Figura:** Línea de tiempo horizontal de 1980 a 2020 con marcadores en 1980, 1990, 2000, 2010, 2020. Sobre la línea, fotografías/iconos representativos de cada época: una persona escribiendo ecuaciones en una pizarra (~1980-1990), un hombre frente a una computadora de escritorio antigua (~1990-2000), un diagrama de nodos tipo grafo/cadena de Markov (~2000-2010), un diagrama de red neuronal con capas de nodos de colores (~2010-2020).

Solución #1: Sistemas Expertos

● Hace más de 20 años, teníamos sistemas basados en reglas:

1. Reunir a un grupo de lingüistas en una sala

2. Hacer que piensen sobre la estructura de su lengua materna y escriban las reglas que ideen

**Figura:** Dos tablas de código lado a lado ilustrando un sistema experto de reglas para interpretar comandos de lenguaje natural. Tabla "Introspection…" con ejemplos: `x = "Give me directions to Starbucks"`, `x = "How do I get to Starbucks?"`, `x = "Where is the nearest Starbucks?"`, `x = "I need directions to Starbucks"`, `x = "Is there a Starbucks nearby?"`, `x = "Starbucks now!"`. Tabla "Rules…" con las reglas correspondientes: `if x matches "give me directions to Z": cmd = DIRECTIONS(here, nearest(Z))` y variantes equivalentes para cada patrón de frase.

## Slide 18

Definiendo una solución de ML

**Figura:** Misma línea de tiempo 1980-2020 descrita en el slide 17.

Solución #2: Anotar Datos y Aprender

● Expertos:
– Muy buenos respondiendo preguntas sobre casos específicos
– No muy buenos explicando CÓMO lo hacen

● Años 1990: Entonces, ¿por qué no simplemente hacer que te digan lo que hacen en CASOS ESPECÍFICOS y luego dejar que el APRENDIZAJE AUTOMÁTICO te diga cómo llegar a las mismas decisiones que ellos tomaron?

## Slide 19

Definiendo una solución de ML

**Figura:** Misma línea de tiempo 1980-2020 descrita en el slide 17.

Solución #2: Anotar Datos y Aprender

1. Recopilar oraciones sin procesar $\{x^{(1)}, \ldots, x^{(n)}\}$

1. Los expertos anotan su significado $\{y^{(1)}, \ldots, y^{(n)}\}$

**Figura:** Cuatro pares de ejemplo entrada-salida anotados: `x^(1): How do I get to Starbucks?` → `y^(1): DIRECTIONS(here, nearest(Starbucks))`; `x^(2): Show me the closest Starbucks` → `y^(2): MAP(nearest(Starbucks))`; `x^(3): Send a text to John that I'll be late` → `y^(3): TXTNSG(John, I'll be late)`; `x^(4): Set an alarm for seven in the morning` → `y^(4): SETALARM(7:00AM)`.

## Slide 20

AI vs ML vs DL

**Figura:** Diagrama de círculos concéntricos (tipo diana). Círculo exterior más grande y oscuro etiquetado "AI" con línea a "Artificial Intelligence: Ingeniería para crear máquinas y programas inteligentes." Círculo intermedio azul etiquetado "ML" con línea a "Machine Learning: Capacidad de aprender sin ser programado explícitamente." (recuadro resaltado en verde). Círculo interior turquesa/celeste etiquetado "DL" con línea a "Deep Learning: Aprendizaje basado en redes neuronales profundas". Ilustra que Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence.

## Slide 21

**Definiendo una Tarea de Machine Learning**

Un **programa aprende** si su **rendimiento P**, en alguna **tarea T**, mejora con la **experiencia E.**

## Slide 22

**Definiendo una Tarea de Machine Learning**

Un **programa aprende** si su **rendimiento P**, en alguna **tarea T**, mejora con la **experiencia E.**

Aprender a **responder a comandos de voz (Siri)**

1. Tarea, *T:*

**Figura:** Recuadro con fondo verde claro que contiene el siguiente texto:
"Given a transcribed sentence x predict the command y

Example:
x = "Give me directions to Starbucks"
y = DIRECTIONS(here, nearest(Starbucks))"

Una flecha (ícono de mano señalando) apunta desde el recuadro hacia el texto "1. Tarea, T:".

## Slide 23

**Ejemplo de Problema de Aprendizaje**

Un **programa aprende** si su **rendimiento P**, en alguna **tarea T**, mejora con la **experiencia E.**

Aprender a responder a comandos de voz (Siri)

1. **Tarea, T:** predecir la acción a partir del habla
1. **Métrica de rendimiento, P:** porcentaje de acciones correctas realizadas en un estudio piloto con usuarios
1. **Experiencia, E:** ejemplos de pares (habla, acción)

## Slide 24

**Trabajo en clase**

**Figura:** Tabla de tres columnas con encabezados "tarea, T" | "performance, P" | "experiencia, E". Las columnas de "tarea, T" y "experiencia, E" están vacías. En la columna central, debajo del encabezado "performance, P", hay un recuadro con fondo naranja claro titulado "Ejercicio en clase" con la siguiente lista numerada:
1. Selecciona una **tarea, T**
2. Identifica la **métrica de rendimiento**, P
3. Identifica la **experiencia, E**
4. Presenta tus ideas al resto de la clase

## Slide 25

**Figura:** Fotografía de fondo (con overlay de color azul degradado a negro) que muestra a dos estudiantes con bata de laboratorio y lentes de protección, observando de cerca un montaje de laboratorio con estructuras metálicas tipo riel y cableado (aparenta ser un banco de pruebas robótico o mecatrónico). No hay texto de contenido en esta slide (solo elementos decorativos de marca).
