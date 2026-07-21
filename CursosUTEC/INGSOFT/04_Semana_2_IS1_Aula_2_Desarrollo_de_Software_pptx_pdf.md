---
curso: INGSOFT
titulo: 04 - Semana 2/IS1 - Aula 2 - Desarrollo de Software__pptx
slides: 29
fuente: 04 - Semana 2/IS1 - Aula 2 - Desarrollo de Software__pptx.pdf
---

## Slide 1

Portada. Título grande "Ingeniería de Software", subtítulo "Desarrollo de Software". Fondo decorativo: silueta de un humanoide/robot caminando por un túnel tecnológico azul. Chrome UTEC / TransformaTec / "Reinventa el mundo".

## Slide 2

**Agenda**

- Presentación.
- Qué es ser un Ingeniero de Software?
- Camino Profesional del Ingeniero de Software.
- Sobre el curso.
- "Pre-requisitos".

(Imagen decorativa lateral: dos personas trabajando frente a una laptop, con tinte azul.)

## Slide 3

Portada de sección. Número grande "1." con ícono de portapapeles/checklist y el título **Proceso de Desarrollo**. Fondo decorativo: mano robótica azul señalando un globo terráqueo digital.

## Slide 4

**Ejemplo**

Desarrollar una calculadora.

- Qué operaciones debe soportar la calculadora?
- Cómo lo va a utilizar el usuario?
- Cómo entregar el producto?
- En que lenguaje(s) / framework(s)?
- Cómo lo implementaré?
- Donde estará disponible?

## Slide 5

**Desarrollo de Software** (diagrama de flujo horizontal)

Línea de tiempo con 6 fases conectadas en secuencia por una línea con íconos circulares. Cada fase tiene un botón/etiqueta azul y una tarjeta descriptiva debajo:

| Fase | Ícono | Descripción |
|------|-------|-------------|
| Análisis | diana/target | Qué debe hacer el software? |
| Diseño | lupa | Cómo se hará el software? |
| Implementación | cohete | Hacer el Software. |
| Pruebas | calendario con checks | El software hace lo que se supone que debe hacer? |
| Despliegue | cohete despegando | Entregar, poner en marcha. |
| Mantenimiento | eslabón de cadena | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

Este diagrama representa las etapas del ciclo de vida (SDLC) que se detallan en las siguientes slides.

## Slide 6

**Análisis**

Especificación, Análisis de Requisitos / Requerimientos, Análisis de Sistemas.

- Comprender y definir qué servicios se requieren del sistema.
- Identificar restricciones en el desarrollo y operación del sistema.
- Entender al usuario objetivo del software y como puede utilizarlo.
- Definir el alcance: que actividades permitirá realizar el software y cuáles no.

## Slide 7

**Análisis**

Lista de sub-actividades (cada ítem precedido por una flecha azul):

- Obtención y análisis de los requisitos.
- Especificación de los requisitos.
- Validación de los requisitos.
- MVP y Prototipos.
- Requisitos Funcionales y No Funcionales

(Imagen decorativa lateral: persona escribiendo/dibujando en una pizarra.)

## Slide 8

**Análisis** — Diagrama de casos de uso UML

Diagrama de casos de uso etiquetado con anotaciones rojas que señalan cada elemento de la notación UML:

- **Actor**: figura de palitos "Recepcionista" (izquierda) y "Administrador" (derecha).
- **Subsistema**: recuadro grande rotulado "Reserva hoteles" que contiene los casos de uso.
- **Caso de Uso**: óvalos amarillos.
- **Relaciones**: líneas y flechas entre elementos.

Casos de uso dentro del subsistema:
- "Consultar precio habitación" (asociado al Recepcionista)
- "Obtener foto habitación" (asociado al Recepcionista)
- "Datos habitación"
- "Cambiar precio habitación" (asociado al Administrador)

Relaciones `<<include>>` (flechas punteadas): "Consultar precio habitación" ──include──> "Datos habitación"; "Obtener foto habitación" ──include──> "Datos habitación"; "Cambiar precio habitación" ──include──> "Datos habitación".

## Slide 9

**Diseño**

Cómo voy a hacer el software?

- Arquitectura: qué elementos me permitirán construir el software que el usuario necesita?
- Qué componentes de Interfaz de Usuario se utilizará para interactuar con el usuario?
- Qué componentes de código (clases, paquetes, algoritmos) tendré que desarrollar?
- Cómo se combinan los componentes de código?
- Que lenguajes de programación, bibliotecas, infraestructura vamos a utilizar para desarrollar el software?
- Hacer que el software sea seguro, eficiente, reutilizable y mantenible.

## Slide 10

**Diseño** — Diagrama de arquitectura de sistema (ejemplo: reserva de cine)

Diagrama de bloques que muestra el flujo desde los clientes hasta el almacenamiento:

- **Clients** (columna gris izquierda): Mobile App, Website, Mobile Web.
- Flecha bidireccional hacia → **Load Balancer** (bloque azul).
- → **API Gateway Service** (bloque azul).
- → **Application APIs** (contenedor azul con 5 APIs apiladas): Listing API, Cinema SeatLayout API, Seat Selection API, Payment API, Communication API.
- Las Application APIs conectan a la derecha con:
  - **Cinema Micro service** (óvalo morado, múltiples instancias apiladas).
  - **Cache** (cilindro amarillo).
  - **RDBMS** (cilindro rojo).
- **RDBMS** conecta (flecha bidireccional) hacia abajo con **Backoffice Management System** (bloque gris).

Ilustra arquitectura con load balancer, gateway, microservicios, capa de caché y base de datos relacional.

## Slide 11

**Implementación**

Desarrollo del Software

- Crear los componentes, escribir el código en equipo.
- Minimizar deuda técnica (Tech Debt) ==> Programar correctamente.
- Creación de estructuras de almacenamiento.
- Establecer la comunicación de los componentes.
- Crear las interfaces de usuario.
- Mantener el código en un sistema de control de versiones.

## Slide 12

**Pruebas**

Validación del Software, Calidad.

- Probar que los componentes realicen lo que se espera de forma individual.
- Probar la integración de los componentes.
- Probar los elementos de interacción del usuario.
- Probar el rendimiento del software en condiciones de carga.
- Probar la seguridad del software.
- Validar que el software cumpla con los requisitos establecidos en el análisis.

## Slide 13

**Pruebas** — Mapa mental "Clasificación de las Pruebas de Software"

Nodo central verde: **Software Testing**. Se ramifica en dos categorías:

**Funcionales** (izquierda):
- Pruebas Unitarias
- Pruebas del Sistema
- Pruebas de Aceptación
- Pruebas de Integración

**No Funcionales** (derecha):
- Pruebas de Seguridad
- Pruebas de Rendimiento
- Pruebas de Usabilidad
- Pruebas de Compatibilidad

## Slide 14

**Despliegue**

- Consiste en hacer que el software desarrollado esté disponible en el ambiente que el usuario final lo va a utilizar.
- Despliegue de los compilados de software a partir del sistema de control de versiones.
- Creación (o migración) de los datos necesarios para iniciar el software en producción.
- Establecer un mecanismo para publicar actualizaciones de software.
- Establecer mecanismos de control y validación del funcionamiento de software:
  - Métricas funcionales (uso de las funcionalidades)
  - Métricas de sistema (memoria, uso de cpu, de red).
  - Acceso a los Logs para verificar errores.

## Slide 15

**Despliegue** — Diagrama "Simple DevOps Project" (pipeline CI/CD)

Flujo de herramientas DevOps con logos:

- Los desarrolladores (grupo de personas) hacen **check-in** (`</>`) del código a → **git**.
- **git** ──"Continuous build"──> **Jenkins**.
- **Jenkins** ──"Continuous Delivery"──> **Ansible**.
- **Jenkins** ──"Docker Image Push"──> **docker**.
- **docker** ──"Docker Image Pull"──> **kubernetes**.
- **Ansible** ──"Deployment"──> **kubernetes**.

Ilustra el pipeline: control de versiones (git) → build continuo (Jenkins) → contenedores (Docker) → orquestación de deploy (Ansible/Kubernetes).

## Slide 16

**Mantenimiento**

- Corrección de errores.
- Mejoras internas (rendimiento, uso de memoria, uso de red).
- Mejoras necesarias (actualizaciones de versiones)
- Solicitudes de mejoras de usuario:
  - Cambios de requisitos.
  - Cambios de legislación, normas, componentes externos.
  - Nuevas funcionalidades.

Diagrama circular a la derecha: centro naranja **Software Maintenance** rodeado de 4 tipos de mantenimiento (círculos azules) con etiquetas de actividad en el anillo:
- **Corrective** (con "Monitoring")
- **Adaptive** (con "Enhancements")
- **Preventive** (con "Support")
- **Perfective** (con "Bug Fixes")

## Slide 17

**Mantenimiento** — Diagrama de proceso de mantenimiento (flujo con recuadros, texto verde)

Flujo principal en bucle:

**Change Request** → **Change Management** → **Impact Analysis** → **System Release Planning** → **Change Implementation** → **System Release** → (retorna a Change Request).

Además hay un lazo de "System Release Planning" hacia sí mismo / "Change Implementation" (flecha de realimentación superior).

Desde **System Release Planning** se ramifica hacia abajo a tres tipos de mantenimiento:
- **Corrective Maintenance (Fault Repair)**
- **Adaptive Maintenance (Platform Adoption)**
- **Perfective Maintenance (System Enhancement)**

## Slide 18

Slide de imagen. Banner/portada de infografía de **altexsoft**: "SOFTWARE DEVELOPMENT LIFE CYCLE EXPLAINED", con estética estilo serie Stranger Things (personajes juveniles y un monstruo). Referencia externa al ciclo de vida del desarrollo de software. Sin texto propio del profesor.

## Slide 19

**Actividad en Grupo**

- Software a desarrollar: Una app de conversión de monedas.
- Análisis: alcance y prototipo.
- Diseño: cómo sería el software (app mobile, web), componentes internos, integración con APIs externas? Tecnologías.
- Pruebas: ejemplos de los tipos de pruebas descritos.
- Mantenimiento: Sugerir mejoras internas y mejoras funcionales que se podrían agregar al alcance inicial.

Recuadro tipo estrella azul (callout) a la derecha:
> Tiempo: 30 minutos.
> Crear una ppt u otro material y subir al Canvas.
> Un integrante de cada grupo sale a explicar el trabajo del grupo.

## Slide 20

Portada de sección. Número grande "2." con ícono de portapapeles/checklist y el título **Gestión de Proyecto**. Fondo decorativo: mano robótica azul señalando globo digital.

## Slide 21

**Project Management**

La gestión de proyectos conecta las actividades de desarrollo de software con el equipo.

- ¿Cuánto tiempo dedicar?
- ¿Cuántas personas dedicar?
- ¿Cuánto tiempo va a tomar?
- ¿Qué hacer primero?
- ¿Cómo organizar para minimizar las dependencias?

## Slide 22

Slide de imagen: infografía **AGILE vs WATERFALL**.

- **Waterfall** (izquierda): secuencia vertical descendente en forma de galones/chevrons: REQUIREMENTS → DESIGN → DEVELOP → TEST → DEPLOY → MAINTENANCE (flecha descendente indicando el flujo lineal).
- Rombo central con "VS".
- **Agile** (derecha): ciclo circular de flechas: REQUIREMENTS → DESIGN → DEVELOP → TEST → DEPLOY → REVIEW (repite el ciclo) → LAUNCH. Representa el desarrollo iterativo.

## Slide 23

**¿Qué es Agilidad?** (valores del Manifiesto Ágil, en inglés y cursiva)

- *Individuals and interactions over processes and tools.*
- *Working software over comprehensive documentation.*
- *Customer collaboration over contract negotiation.*
- *Responding to change over following a plan.*

Fuente: https://agilemanifesto.org/

(Fondo azul con comillas decorativas grandes.)

## Slide 24

**Scrum: Agile framework**

- Backlog: Lista (integral) de actividades/requerimientos a realizar.
- Priorización: Cada actividad tiene una prioridad, que permitirá decidir cuando realizarlas.
- Sprint vs Release.

## Slide 25

**Scrum: Agile framework**

Sprint: Periodo breve de tiempo en que se planifica un conjunto de tareas.

- Planificación del Sprint: Qué tareas se ejecutarán.
- Cada miembro del equipo selecciona que tarea(s) ejecutará.
- "Daily" Scrum (Standup): Qué hice ayer, que haré hoy y verificar impedimentos o dependencias. [enlace "Ver video"]

## Slide 26

**Scrum: Agile framework**

Sprint Demo: Presentar lo que se hizo.

Release Retrospective:
- Qué hicimos bien?
- Qué hicimos mal?
- Cómo podemos comprometernos a hacerlo mejor el próximo reléase?

## Slide 27

**Roles** — Diagrama de los roles de Scrum con atributos radiales

Tres roles representados con ilustraciones y sus atributos/responsabilidades conectados por líneas punteadas:

- **Development Team** (arriba, 4 avatares): SELF ORGANIZATION, DESIGN, DEVELOPMENT (izquierda); UX, TESTING, DELIVERY (derecha).
- **Product Owner** (centro-izquierda, avatar naranja en círculo punteado): RELEASE MANAGEMENT, MANAGING THE SCRUM BACKLOG, STAKEHOLDER MANAGEMENT.
- **Scrum Master** (abajo, avatar azul): TRANSPARENCY, SELF ORGANIZATION, PROTECTING THE TEAM (izquierda); EMPIRICISM, SCRUM VALUES, REMOVE BLOCKERS (derecha).

## Slide 28

**Conclusiones** (cada punto con flecha azul)

- El Proceso de Desarrollo de Software tiene una serie de actividades relacionadas, cada una con su debida importancia.
- La Ingeniería de Software nos propone guías para cada una de dichas actividades.
- La gestión de proyectos está relacionada en cómo efectuar estas actividades optimizando los recursos.
- Scrum es una de las formas de gestionar un proyecto de software que brinda herramientas para hacerlo de forma apropiada.

## Slide 29

Cierre. "GRACIAS" y el nombre del profesor **CHRISTIAN PAZ TRILLO**. Fondo decorativo: dos personas con lentes de seguridad trabajando en un laboratorio, tinte azul.
