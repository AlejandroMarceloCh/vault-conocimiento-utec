---
curso: INGSOFT
titulo: 05 - Semana 3/IS1 - Aula 3 - Scrum y Requisitos__pptx
slides: 40
fuente: 05 - Semana 3/IS1 - Aula 3 - Scrum y Requisitos__pptx.pdf
---

Ingeniería de Software

       Profesor Christian Paz
         Presentación de la Actividad en Grupo.




Agenda
         Gestión de Proyectos.

         Análisis de Requisitos.
                                   Actividad en Grupo                                                        Un integrante de cada grupo sale a
                                                                                                                explicar el trabajo del grupo.



• Software a desarrollar: Una app de conversión de monedas.


• Análisis: alcance y prototipo.
• Diseño: cómo sería el software (app mobile, web), componentes internos, integración con APIs externas? Tecnologías.
• Pruebas: ejemplos de los tipos de pruebas descritos.
• Mantenimiento: Sugerir mejoras internas y mejoras funcionales que se podrían agregar al alcance inicial.
1.
 Gestión de Proyecto
                        Project Management
La gestión de proyectos conecta las actividades de desarrollo de software con el equipo.
• ¿Cuánto tiempo dedicar?
• ¿Cuántas personas dedicar?
• ¿Cuánto tiempo va a tomar?
• ¿Qué hacer primero?
• ¿Cómo organizar para minimizar las dependencias?
                                                                                        Si una tarea va a tomar
                                                                                         más tiempo, intentar
                                                                                           dividirla en tareas
                                                                                                menores.




                               Project Management
Tarea: Una actividad que puede realizar una o más personas en un tiempo, usualmente no muy
prolongado (entre 2 a 4 días, pero en el caso de su proyecto de lab puede ser más tiempo).


Cada tarea debe estar asociada a un requisito, de forma que se puedan agrupar fácilmente y se pueda
realizar el seguimiento.


El conjunto de tareas del proyecto es llamado de Backlog (en Scrum).
                                Project Management
Estado:
• Sin asignar: La tarea fue creada y estimada inicialmente pero aún no tiene una persona asignada.
• Nueva: La tarea fue creada y asignada.
• Activa: La tarea está en ejecución (puede ser en diseño, código o verificando).
• Bloqueada: La tarea está en ejecución pero algo externo hace que no se pueda avanzar.
• Done: La tarea fue terminada y la(s) persona(s) asignada(s) está libre para tomar la próxima.
Software de
  Project
Management
                 ¿Qué es Agilidad?

 • Individuals and interactions over processes and tools.
• Working software over comprehensive documentation.
   • Customer collaboration over contract negotiation.
     • Responding to change over following a plan.


                      https://agilemanifesto.org/
                       Scrum: Agile framework

• Backlog: Lista (integral) de actividades/requerimientos a realizar.

• Priorización: Cada actividad tiene una prioridad, que permitirá decidir cuando realizarlas.

• Sprint vs Release.
                     Scrum: Agile framework
Sprint: Periodo breve de tiempo en que se planifica un conjunto de tareas.

• Planificación del Sprint: Qué tareas se ejecutarán.

• Cada miembro del equipo selecciona que tarea(s) ejecutará.

• “Daily” Scrum (Standup): Qué hice ayer, que haré hoy y verificar impedimentos o
  dependencias. Ver video
                    Scrum: Agile framework
Sprint Demo: Presentar lo que se hizo.

Release Retrospective:

Qué hicimos bien?

Qué hicimos mal?

Cómo podemos comprometernos a hacerlo mejor el próximo reléase?
Roles
2.
 Análisis de Requisitos
                                                       Análisis
Especificación, Análisis de Requisitos / Requerimientos, Análisis de Sistemas.

• Comprender y definir qué servicios se requieren del sistema.
• Identificar restricciones en el desarrollo y operación del sistema.
• Entender al usuario objetivo del software y como puede utilizarlo.
• Definir el alcance: que actividades permitirá realizar el software y cuáles no.
                                            Requisitos
Es todo aquello que el software debe hacer o permitir que el usuario haga.

Cosas que debe permitir que el usuario ingrese o vea.

Características requeridas / deseadas del sistema o producto de software.
                                Ejemplo: Twitter (X)
Permitir que el usuario cree una cuenta.

Permitir que el usuario posteé textos o imágenes.

Permitir que el usuario busque otros usuarios por nombre o nickname y los pueda seguir.

Permitir que el usuario visualice los posts de otros usuarios y pueda interactuar con ellos (like, repost, comment).

              Stakeholders y Usuarios Finales

Stakeholders: Son las personas que solicitan o serán afectadas por la creación o modificación del producto.

Ejemplo: Gerentes de área usuaria, comerciales o vendedores del producto.

Usuarios Finales: Personas que se espera sean usuarios del producto cuando esté disponible.

Ej: En la implementación de Canvas – UTEC

Quienes serían Stakeholder?
Quienes serían usuarios finales?
                                            Requisitos
Un requisito puede ser una descripción a alto nivel o muy detallada.

Alto nivel: Permitir que el usuario busque otros usuarios por nombre o nickname y los pueda seguir.

Detallada:

• Permitir que el usuario busque otros usuarios digitando un nombre parcial y obteniendo una lista de los nombres
  similares.
• Permitir que el usuario pueda ver el perfil de otro usuario.
• Mostrar un botón “Seguir” en el perfil de otro usuario, con lo que se hará su seguidor.
• Cuando el usuario vea su timeline, debe poder ver los posts de los usuarios a los que sigue.
  Levantamiento de Requisitos (Gathering)

Consiste en evaluar de forma detallada las necesidades y objetivos que el software en cuestión debe satisfacer.

Implica entender a los usuarios finales y sus necesidades, preferencias y cómo podrían utilizar el software.

Identificar oportunidades que se pueden aprovechar y problemas que se deben resolver.
  Levantamiento de Requisitos (Gathering)
Entrevistas:

Reuniones con personas involucradas (stakeholders) para entender cuáles son sus necesidades y expectativas.

Observación o Inspección:

En un sistema existente entender los procesos que se realizan o inspeccionar código o documentación ya existente.

Brainstorm:

Reuniones para discutir las posibilidades de cómo atender las necesidades y expectativas.
    Levantamiento de Requisitos (Gathering)
Ejemplo: Construir una nueva plataforma de gestión de enseñanza.


Entrevista a un usuario de Canvas (profesor):


-   Tengo un listado de los cursos que enseño este semestre.
-   Puedo subir material para cada semana de aula.
-   Puedo crear tareas para que los alumnos resuelvan y suban sus resultados.
-   Puedo revisar las tareas de los alumnos y calificarlas.
  Levantamiento de Requisitos (Gathering)
Ejemplo: Construir una nueva plataforma de gestión de enseñanza.


Entrevista a un usuario de Canvas (alumno):
                  Especificación de Requisitos

Consiste en plasmar los requisitos en diagramas, documentos y prototipos.

Alto nivel: Casos de Uso.

Detallados: Escenarios.

Un escenario define como un actor del sistema cumple determinados pré-requisitos, va a ejecutar una secuencia de
pasos, a través del ingreso de datos (input) y obteniendo como resultado una salida esperada (output).
                                                   Casos de Uso




Diagrama UML (Unified Modeling Language) que
representa la interacción de los usuarios con un
sistema de software a través de sus distintas
funciones (casos de uso).
                                                Casos de Uso




Ej: Elaboremos un diagrama de casos de uso de
un sistema de venta de entradas al cine.
               Especificación de Requisitos

Escenarios:
Un escenario define como un actor del sistema cumple determinados pré-requisitos, va a ejecutar
una secuencia de pasos, a través del ingreso de datos (input) y obteniendo como resultado una
salida esperada (output).
                      Especificación de Requisitos
Escenarios:                                        Ejemplo:
El objetivo de identificar escenarios es conocer   Compra de entradas en el cine:
las posibles ramificaciones de un caso de uso y    - Qué hacer si ya no hay más entradas
las situaciones que podrían ocurrir en la          disponibles en la función seleccionada?
interacción del usuario con el caso de uso.        - Qué hacer si al mismo tiempo otro usuario
                                                   intenta comprar los mismos asientos?
Funcionales vs.
No Funcionales
                        Validación de requisitos

Específico y No ambiguo.


Ambiguo: El sistema debe permitir crear una cuenta.


Específico: El sistema debe permitir que el usuario cree una cuenta proporcionando su correo electrónico,
documento de identidad y una contraseña.
                          Validación de requisitos

Medible o verificable.
Debe existir formas de decir si el sistema resultante cumplió o no el requisito.


Incorrecto: El registro del usuario debe ser rápido.


Correcto: El registro del usuario debe tener solamente dos pasos incluida una validación de un mensaje enviado a su
correo o teléfono.
                          Validación de requisitos

Consistencia


Los requisitos no deben entrar en conflicto uno con el otro.


Ejemplo:
El sistema debe promover el registro self-service de usuarios.
El sistema debe solicitar información personal obligatoria del usuario acerca de sus ingresos mensuales.
                        Validación de requisitos

Rastreabilidad
Debe existir una forma de rastrear la necesidad del usuario hacia los artefactos de diseño e implementación que lo
satisfacen.


Asignar un código a cada requisito y referenciarlo desde cada elemento de documentación y/o código. Ej: RF-0001
Creación de cuenta de usuario.
                                   Actividad en Grupo




• Software a analizar: Cambio de monedas                                                        Tiempo: 30 minutos.

                                                                                       Crear una doc u otro material y subir al
                                                                                                     Canvas.
• 1 Integrante del equipo debe representar al ”stakeholder”: dueño del negocio.
• 1 integrante del equipo debe representar a un usuario final.
• El resto del equipo debe representar al equipo de desarrollo.


• Realizar un diagrama de casos de uso.
• Analizar al menos 3 casos de uso para identificar los posibles escenarios en cada una de esas
  interacciones.
GRACIAS
CHRISTIAN PAZ TRILLO

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
