---
curso: INGSOFT
titulo: 05 - Semana 3/IS1 - Aula 3 - Scrum y Requisitos__pptx
slides: 40
fuente: 05 - Semana 3/IS1 - Aula 3 - Scrum y Requisitos__pptx.pdf
---

## Slide 1
Portada. Título grande: **Ingeniería de Software**. Subtítulo: *Profesor Christian Paz*. Fondo decorativo (silueta de persona/robot caminando en un túnel tecnológico azul). Logo UTEC y "Reinventa el mundo".

## Slide 2
**Agenda** (título vertical a la izquierda). Contenido:
- Presentación de la Actividad en Grupo.
- Gestión de Proyectos.
- Análisis de Requisitos.

Imagen decorativa de dos personas trabajando frente a una laptop.

## Slide 3
**Actividad en Grupo**

- Software a desarrollar: Una app de conversión de monedas.
- Análisis: alcance y prototipo.
- Diseño: cómo sería el software (app mobile, web), componentes internos, integración con APIs externas? Tecnologías.
- Pruebas: ejemplos de los tipos de pruebas descritos.
- Mantenimiento: Sugerir mejoras internas y mejoras funcionales que se podrían agregar al alcance inicial.

Estrella/badge azul a la derecha con la nota: "Un integrante de cada grupo sale a explicar el trabajo del grupo."

## Slide 4
Portada de sección. Número grande **1.** con ícono de portapapeles/checklist. Título: **Gestión de Proyecto**. Fondo decorativo (mano robótica tocando un globo digital).

## Slide 5
**Project Management**

La gestión de proyectos conecta las actividades de desarrollo de software con el equipo.
- ¿Cuánto tiempo dedicar?
- ¿Cuántas personas dedicar?
- ¿Cuánto tiempo va a tomar?
- ¿Qué hacer primero?
- ¿Cómo organizar para minimizar las dependencias?

## Slide 6
**Project Management**

Tarea: Una actividad que puede realizar una o más personas en un tiempo, usualmente no muy prolongado (entre 2 a 4 días, pero en el caso de su proyecto de lab puede ser más tiempo).

Cada tarea debe estar asociada a un requisito, de forma que se puedan agrupar fácilmente y se pueda realizar el seguimiento.

El conjunto de tareas del proyecto es llamado de Backlog (en Scrum).

Estrella/badge azul a la derecha con la nota: "Si una tarea va a tomar más tiempo, intentar dividirla en tareas menores."

## Slide 7
**Project Management**

Estado:
- **Sin asignar:** La tarea fue creada y estimada inicialmente pero aún no tiene una persona asignada.
- **Nueva:** La tarea fue creada y asignada.
- **Activa:** La tarea está en ejecución (puede ser en diseño, código o verificando).
- **Bloqueada:** La tarea está en ejecución pero algo externo hace que no se pueda avanzar.
- **Done:** La tarea fue terminada y la(s) persona(s) asignada(s) está libre para tomar la próxima.

## Slide 8
Título a la izquierda: **Software de Project Management**.

**Captura de pantalla** de un tablero Kanban tipo Jira ("Teams in space – Software project"). Barra lateral azul con menú: Board (seleccionado), Features, Settings, Give feedback. El tablero "Board" tiene tres columnas:

| TO DO (29) | IN PROGRESS (4, MAX 3) | DONE (3) |
|---|---|---|
| Implement feedback collector (SMS-001) | Force SSL on any page that contains account info (SMS-029) | Automate collection of feedback for weekly email report (SMS-031) |
| Add NPS feedback to wallboard (SMS-011) | Create subscription plans and discount codes in Stripe (SMS-035) | Schedule weekly email report for Monday mornings to all staff (SMS-032) |
| Add NPS feedback to email report (SMS-004) | Add analytics to pricing page (SMS-039) | Install SSL certificate (SMS-033) |
| Allow users to change between two tiers at the same price (SMS-008) | Add link to app usage (GA) in email report (SMS-035) | |
| Apply a prorated discount to a user when they move from a low to a high priced tier (SMS-0012) | | |
| Extend the grace period to accounts… | | |

La columna IN PROGRESS está resaltada en amarillo (indica límite WIP alcanzado: MAX 3).

## Slide 9
**Diagrama AGILE vs WATERFALL** (sin texto de cuerpo; toda la slide es la infografía).

- Izquierda: **WATERFALL** representado como cascada de chevrons apilados hacia abajo, con una flecha vertical descendente: REQUIREMENTS → DESIGN → DEVELOP → TEST → DEPLOY → MAINTENANCE (secuencial, en tonos de azul degradado).
- Centro: rombo con "**VS**".
- Derecha: **AGILE** representado como ciclo circular de flechas: TEST → DEVELOP → DESIGN → REVIEW → DEPLOY (giro), con una flecha de entrada REQUIREMENTS y una de salida LAUNCH. La palabra AGILE al centro del círculo.

## Slide 10
**¿Qué es Agilidad?** (Manifiesto Ágil, texto en cursiva sobre fondo azul):
- *Individuals and interactions over processes and tools.*
- *Working software over comprehensive documentation.*
- *Customer collaboration over contract negotiation.*
- *Responding to change over following a plan.*

Fuente: https://agilemanifesto.org/ (con comillas grandes decorativas de fondo).

## Slide 11
**Scrum: Agile framework**

- **Backlog:** Lista (integral) de actividades/requerimientos a realizar.
- **Priorización:** Cada actividad tiene una prioridad, que permitirá decidir cuando realizarlas.
- **Sprint vs Release.**

## Slide 12
**Scrum: Agile framework**

Sprint: Periodo breve de tiempo en que se planifica un conjunto de tareas.
- Planificación del Sprint: Qué tareas se ejecutarán.
- Cada miembro del equipo selecciona que tarea(s) ejecutará.
- "Daily" Scrum (Standup): Qué hice ayer, que haré hoy y verificar impedimentos o dependencias. [Ver video] (hipervínculo).

## Slide 13
**Scrum: Agile framework**

Sprint Demo: Presentar lo que se hizo.

Release Retrospective:
- Qué hicimos bien?
- Qué hicimos mal?
- Cómo podemos comprometernos a hacerlo mejor el próximo reléase?

## Slide 14
**Roles** — diagrama de los tres roles de Scrum, cada uno con atributos ramificados:

- **Development Team** (arriba, 4 avatares morados): conecta con SELF ORGANIZATION, DESIGN, DEVELOPMENT (izquierda) y UX, TESTING, DELIVERY (derecha).
- **Product Owner** (centro-izquierda, avatar naranja dentro de un círculo punteado): rodeado de RELEASE MANAGEMENT, MANAGING THE SCRUM BACKLOG, STAKEHOLDER MANAGEMENT (íconos naranjas).
- **Scrum Master** (abajo, avatar azul): conecta con TRANSPARENCY, SELF ORGANIZATION, PROTECTING THE TEAM (izquierda) y EMPIRICISM, SCRUM VALUES, REMOVE BLOCKERS (derecha).

Foto decorativa a la derecha (persona escribiendo en pizarra).

## Slide 15
Portada de sección. Número grande **2.** con ícono de portapapeles. Título: **Análisis de Requisitos**. Fondo decorativo (mano robótica y globo digital).

## Slide 16
**Análisis**

Especificación, Análisis de Requisitos / Requerimientos, Análisis de Sistemas.
- Comprender y definir qué servicios se requieren del sistema.
- Identificar restricciones en el desarrollo y operación del sistema.
- Entender al usuario objetivo del software y como puede utilizarlo.
- Definir el alcance: que actividades permitirá realizar el software y cuáles no.

## Slide 17
**Meme/comic clásico del columpio** (5 viñetas, sin texto de cuerpo propio de la slide). Cada viñeta muestra un columpio colgado de un árbol de forma absurda, con caption en inglés:
1. "How the customer explained it" (columpio con dos tablas apiladas mal).
2. "How the Project Leader understood it" (columpio colgado de una sola rama con dos cuerdas cruzadas).
3. "How the Analyst designed it" (asiento colgando torcido pegado al tronco).
4. "How the Programmer wrote it" (cuerda enrollada al tronco, asiento arrastrando el piso).
5. "What the customer really needed" (un simple columpio de llanta, bien hecho).

Ilustra la brecha entre lo que el cliente pide y lo que se entrega en cada etapa.

## Slide 18
**Requisitos**

Es todo aquello que el software debe hacer o permitir que el usuario haga.

Cosas que debe permitir que el usuario ingrese o vea.

Características requeridas / deseadas del sistema o producto de software.

## Slide 19
**Ejemplo: Twitter (X)**

- Permitir que el usuario cree una cuenta.
- Permitir que el usuario posteé textos o imágenes.
- Permitir que el usuario busque otros usuarios por nombre o nickname y los pueda seguir.
- Permitir que el usuario visualice los posts de otros usuarios y pueda interactuar con ellos (like, repost, comment).

## Slide 20
**Infografía: "Steps of requirements analysis process"** (diagrama de 8 flechas encadenadas en morado/naranja alternado, con nubes decorativas). Sin texto de cuerpo propio:

- **Step 1:** Identify Stakeholders and End-Users
- **Step 2:** Requirements Gathering – Collecting Essential Information
- **Step 3:** Define Functional and Non-Functional Requirements
- **Step 4:** Analyze and Validate Requirements
- **Step 5:** Prioritize Requirements for Development
- **Step 6:** Document Requirements Properly
- **Step 7:** Sign-off
- **Step 8:** Manage Changes and Updates Effectively

## Slide 21
**Stakeholders y Usuarios Finales**

Stakeholders: Son las personas que solicitan o serán afectadas por la creación o modificación del producto.
Ejemplo: Gerentes de área usuaria, comerciales o vendedores del producto.

Usuarios Finales: Personas que se espera sean usuarios del producto cuando esté disponible.
Ej: En la implementación de Canvas – UTEC
- Quienes serían Stakeholder?
- Quienes serían usuarios finales?

## Slide 22
**Requisitos**

Un requisito puede ser una descripción a alto nivel o muy detallada.

Alto nivel: Permitir que el usuario busque otros usuarios por nombre o nickname y los pueda seguir.

Detallada:
- Permitir que el usuario busque otros usuarios digitando un nombre parcial y obteniendo una lista de los nombres similares.
- Permitir que el usuario pueda ver el perfil de otro usuario.
- Mostrar un botón "Seguir" en el perfil de otro usuario, con lo que se hará su seguidor.
- Cuando el usuario vea su timeline, debe poder ver los posts de los usuarios a los que sigue.

## Slide 23
**Levantamiento de Requisitos (Gathering)**

Consiste en evaluar de forma detallada las necesidades y objetivos que el software en cuestión debe satisfacer.

Implica entender a los usuarios finales y sus necesidades, preferencias y cómo podrían utilizar el software.

Identificar oportunidades que se pueden aprovechar y problemas que se deben resolver.

## Slide 24
**Levantamiento de Requisitos (Gathering)**

Entrevistas: Reuniones con personas involucradas (stakeholders) para entender cuáles son sus necesidades y expectativas.

Observación o Inspección: En un sistema existente entender los procesos que se realizan o inspeccionar código o documentación ya existente.

Brainstorm: Reuniones para discutir las posibilidades de cómo atender las necesidades y expectativas.

## Slide 25
**Levantamiento de Requisitos (Gathering)**

Ejemplo: Construir una nueva plataforma de gestión de enseñanza.

Entrevista a un usuario de Canvas (profesor):
- Tengo un listado de los cursos que enseño este semestre.
- Puedo subir material para cada semana de aula.
- Puedo crear tareas para que los alumnos resuelvan y suban sus resultados.
- Puedo revisar las tareas de los alumnos y calificarlas.

## Slide 26
**Levantamiento de Requisitos (Gathering)**

Ejemplo: Construir una nueva plataforma de gestión de enseñanza.

Entrevista a un usuario de Canvas (alumno):

(Slide sin contenido adicional — deja el ejercicio abierto para completar en clase.)

## Slide 27
**Especificación de Requisitos**

Consiste en plasmar los requisitos en diagramas, documentos y prototipos.

Alto nivel: Casos de Uso.

Detallados: Escenarios.

Un escenario define como un actor del sistema cumple determinados pré-requisitos, va a ejecutar una secuencia de pasos, a través del ingreso de datos (input) y obteniendo como resultado una salida esperada (output).

## Slide 28
**Casos de Uso**

Texto a la izquierda: "Diagrama UML (Unified Modeling Language) que representa la interacción de los usuarios con un sistema de software a través de sus distintas funciones (casos de uso)."

**Diagrama UML de casos de uso** (ejemplo de un chat, a la derecha), con 3 actores y sus casos de uso (elipses):
- **User** (verde): Log In, Log Out, Send Message, Read Message, Get Invisible, Enter Chat Room, Leave Chat Room.
- **Moderator** (amarillo): Add Chat Room, Close Chat Room, Block User, Unblock User.
- **Administrator** (rojo): Add Moderator, Remove Moderator, Edit Moderator.

## Slide 29
**Casos de Uso**

Ej: Elaboremos un diagrama de casos de uso de un sistema de venta de entradas al cine.

(Slide de ejercicio, sin diagrama — se elabora en vivo.)

## Slide 30
**Especificación de Requisitos**

Escenarios:
Un escenario define como un actor del sistema cumple determinados pré-requisitos, va a ejecutar una secuencia de pasos, a través del ingreso de datos (input) y obteniendo como resultado una salida esperada (output).

## Slide 31
**Especificación de Requisitos** (dos columnas)

Columna izquierda — Escenarios:
El objetivo de identificar escenarios es conocer las posibles ramificaciones de un caso de uso y las situaciones que podrían ocurrir en la interacción del usuario con el caso de uso.

Columna derecha — Ejemplo (Compra de entradas en el cine):
- Qué hacer si ya no hay más entradas disponibles en la función seleccionada?
- Qué hacer si al mismo tiempo otro usuario intenta comprar los mismos asientos?

## Slide 32
Título a la izquierda: **Funcionales vs. No Funcionales**.

**Tabla comparativa** (dos columnas, morada vs azul):

| Functional Requirements | Non-functional Requirements |
|---|---|
| Describe what the system as a whole should do. | Describe the attributes of system quality and performance. |
| Cover all the functions that the software must perform. | Cover all aspects of good user experience. |
| Ensure all core functionality is well-performed. | Ensure users' needs are satisfied. |
| Easy to specify. | Difficult to specify. |
| They are tested first. | They are tested after functional testing. |
| What is tested: API testing, Functional testing of the whole system, Integration, End to End testing, etc. | What is tested: Usability, Performance, Security, Stress testing, etc. |
| Types: Business rules, Administrative functions, Data management, Certification requirements, Authorization levels, etc. | Types: Availability, Scalability, Capacity, Reliability, Data Integrity, etc. |

## Slide 33
Ejemplo funcional vs no funcional aplicado a **Twitter (X)** (con logo X/Twitter al centro):

**Functional Requirements:**
- Post Tweet
- Delete Tweet
- Bookmark Tweet
- Follow/Unfollow people

**Non-Functional Requirements:**
- Latency of tweet post
- System should be available for large number of requests

## Slide 34
**Validación de requisitos**

Específico y No ambiguo.

Ambiguo: El sistema debe permitir crear una cuenta.

Específico: El sistema debe permitir que el usuario cree una cuenta proporcionando su correo electrónico, documento de identidad y una contraseña.

## Slide 35
**Validación de requisitos**

Medible o verificable. Debe existir formas de decir si el sistema resultante cumplió o no el requisito.

Incorrecto: El registro del usuario debe ser rápido.

Correcto: El registro del usuario debe tener solamente dos pasos incluida una validación de un mensaje enviado a su correo o teléfono.

## Slide 36
**Validación de requisitos**

Consistencia. Los requisitos no deben entrar en conflicto uno con el otro.

Ejemplo:
- El sistema debe promover el registro self-service de usuarios.
- El sistema debe solicitar información personal obligatoria del usuario acerca de sus ingresos mensuales.

(Ejemplo de dos requisitos que se contradicen.)

## Slide 37
**Validación de requisitos**

Rastreabilidad. Debe existir una forma de rastrear la necesidad del usuario hacia los artefactos de diseño e implementación que lo satisfacen.

Asignar un código a cada requisito y referenciarlo desde cada elemento de documentación y/o código. Ej: RF-0001 Creación de cuenta de usuario.

## Slide 38
Repetición de la **infografía "Steps of requirements analysis process"** (idéntica a la slide 20): 8 flechas encadenadas morado/naranja:
Step 1 Identify Stakeholders and End-Users → Step 2 Requirements Gathering – Collecting Essential Information → Step 3 Define Functional and Non-Functional Requirements → Step 4 Analyze and Validate Requirements → Step 5 Prioritize Requirements for Development → Step 6 Document Requirements Properly → Step 7 Sign-off → Step 8 Manage Changes and Updates Effectively.

## Slide 39
**Actividad en Grupo**

- Software a analizar: Cambio de monedas
- 1 Integrante del equipo debe representar al "stakeholder": dueño del negocio.
- 1 integrante del equipo debe representar a un usuario final.
- El resto del equipo debe representar al equipo de desarrollo.
- Realizar un diagrama de casos de uso.
- Analizar al menos 3 casos de uso para identificar los posibles escenarios en cada una de esas interacciones.

Estrella/badge azul a la derecha: "Tiempo: 30 minutos. Crear una doc u otro material y subir al Canvas."

## Slide 40
Cierre. Título grande: **GRACIAS**. Subtítulo: *Christian Paz Trillo*. Fondo decorativo (dos personas en un laboratorio con lentes de seguridad).
