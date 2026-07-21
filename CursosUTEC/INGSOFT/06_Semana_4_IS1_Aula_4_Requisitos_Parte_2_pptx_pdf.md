---
curso: INGSOFT
titulo: 06 - Semana 4/IS1 - Aula 4 - Requisitos Parte 2__pptx
slides: 19
fuente: 06 - Semana 4/IS1 - Aula 4 - Requisitos Parte 2__pptx.pdf
---

## Slide 1

Portada. Título "Ingeniería de Software", subtítulo "Profesor Christian Paz". Imagen decorativa de fondo (figura humanoide/robot caminando por un túnel tecnológico azul). Chrome UTEC / "Reinventa el mundo" / TransformaTec — decorativo.

## Slide 2

Slide de sección. Numeral grande "1." y título con ícono de portapapeles/checklist: "Análisis de Requisitos". Imagen decorativa a la derecha (mano robótica tocando un mapamundi digital).

## Slide 3

Título: "Actividad en Grupo"

Contenido:
- Software a analizar: Cambio de monedas
- 1 Integrante del equipo debe representar al "stakeholder": dueño del negocio.
- 1 integrante del equipo debe representar a un usuario final.
- El resto del equipo debe representar al equipo de desarrollo.
- Realizar un diagrama de casos de uso.
- Analizar al menos 3 casos de uso para identificar los posibles escenarios en cada una de esas interacciones.

Recuadro destacado (estrella azul, esquina derecha): "Tiempo: 30 minutos. Complementar el documento elaborado la semana anterior."

## Slide 4

Título: "Funcionales vs. No Funcionales" (a la izquierda, texto grande negro).

**Tabla comparativa de dos columnas** (izquierda morada = Functional Requirements; derecha celeste = Non-functional Requirements):

| Functional Requirements | Non-functional Requirements |
|---|---|
| Describe what the system as a whole should do. | Describe the attributes of system quality and performance. |
| Cover all the functions that the software must perform. | Cover all aspects of good user experience. |
| Ensure all core functionality is well-performed. | Ensure users' needs are satisfied. |
| Easy to specify. | Difficult to specify. |
| They are tested first. | They are tested after functional testing. |
| What is tested: API testing, Functional testing of the whole system, Integration, End to End testing, etc. | What is tested: Usability, Performance, Security, Stress testing, etc. |
| Types: Business rules, Administrative functions, Data management, Certification requirements, Authorization levels, etc. | Types: Availability, Scalability, Capacity, Reliability, Data Integrity, etc. |

## Slide 5

Ejemplo de requisitos aplicado a Twitter/X. Dos cajas azules tituladas "Functional Requirements" y "Non-Functional Requirements", con el logo de X (Twitter) en medio.

Functional Requirements:
- Post Tweet
- Delete Tweet
- Bookmark Tweet
- Follow/Unfollow people

Non-Functional Requirements:
- Latency of tweet post
- System should be available for large number of requests

## Slide 6

Título: "Validación de requisitos"

Criterio: **Específico y No ambiguo.**

- Ambiguo: El sistema debe permitir crear una cuenta.
- Específico: El sistema debe permitir que el usuario cree una cuenta proporcionando su correo electrónico, documento de identidad y una contraseña.

## Slide 7

Título: "Validación de requisitos"

Criterio: **Medible o verificable.** Debe existir formas de decir si el sistema resultante cumplió o no el requisito.

- Incorrecto: El registro del usuario debe ser rápido.
- Correcto: El registro del usuario debe tener solamente dos pasos incluida una validación de un mensaje enviado a su correo o teléfono.

## Slide 8

Título: "Validación de requisitos"

Criterio: **Consistencia.** Los requisitos no deben entrar en conflicto uno con el otro.

Ejemplo (requisitos en conflicto):
- El sistema debe promover el registro self-service de usuarios.
- El sistema debe solicitar información personal obligatoria del usuario acerca de sus ingresos mensuales.

## Slide 9

Título: "Validación de requisitos"

Criterio: **Rastreabilidad.** Debe existir una forma de rastrear la necesidad del usuario hacia los artefactos de diseño e implementación que lo satisfacen.

Asignar un código a cada requisito y referenciarlo desde cada elemento de documentación y/o código. Ej: RF-0001 Creación de cuenta de usuario.

## Slide 10

Título: "Priorización"

**Diagrama de 3 niveles** (flechas azules numeradas 01-02-03, cada una con descripción a la derecha sobre fondo gris):

| # | Prioridad | Descripción |
|---|---|---|
| 01 | MUST HAVE | The product must have this requirement fulfilled or else it does not get user acceptance |
| 02 | NICE TO HAVE | The product can survive without it |
| 03 | OUT OF THE SCOPE | It can be discarded if there isn't enough budget, time or resources. |

## Slide 11

Título: "Ejemplo – Entradas de Cine"

Agenda del ejemplo:
- Requisitos Funcionales vs No Funcionales.
- Priorización de Requisitos.

## Slide 12

**Diagrama de proceso: "Steps of requirements analysis process"** — 8 flechas encadenadas (chevrons alternando morado/naranja, decoración de nubes de fondo):

- Step 1: Identify Stakeholders and End-Users
- Step 2: Requirements Gathering – Collecting Essential Information
- Step 3: Define Functional and Non-Functional Requirements
- Step 4: Analyze and Validate Requirements
- Step 5: Prioritize Requirements for Development
- Step 6: Document Requirements Properly
- Step 7: Sign-off
- Step 8: Manage Changes and Updates Effectively

## Slide 13

Título: "Qué sucede en la vida real?"

- **Nuevo Producto (startup):** Caso Proyecto Tutores IA.
- **Dentro de una organización:**
  - Nuevo Producto.
  - Cambio dentro de un Producto existente.
- **Desarrollo como outsourcing.**

## Slide 14

Título: "Nuevo Producto (Startup)"

- Gran importancia en identificación de usuarios e involucrarlos.
- Recolección de requisitos.
- MVP (Producto mínimo viable).
- Priorización: que features le harán más impacto al usuario y a solucionar sus problemas más importantes.

Al pie: el mismo diagrama de 8 flechas "Steps of requirements analysis process" (Step 1 a Step 8) de la slide 12.

## Slide 15

Título: "Nuevo Producto (en Org)"

- Stakeholders impulsan el proyecto.
- Importante alinear el producto con otros existentes.
- Alineamiento funcional y no funcional.
- Importante establecer integración con otros productos para maximizar adopción.
- Priorización: priorizar lanzamiento de un producto alineado.

Al pie: diagrama de 8 flechas de pasos de análisis de requisitos (igual que slide 12).

## Slide 16

Título: "Cambiar Producto existente (en Org)"

- Stakeholders impulsan el proyecto.
- Resistencia al cambio, ver si el producto no soporta actualmente el nuevo requerimiento.
- Alineamiento funcional y no funcional.
- Importante maximizar que no haya regresiones.
- Priorización: despliegue progresivo que garantice la continuidad del producto.

Al pie: diagrama de 8 flechas de pasos de análisis de requisitos (igual que slide 12).

## Slide 17

Título: "Desarrollo Outsourcing"

- Stakeholders impulsan el proyecto buscando maximizar el costo/beneficio.
- Validación de requerimientos con los stakeholders.
- Importante documentar los requerimientos pues hacen parte del contrato (sign-off).
- Priorización: reducir el riesgo de atrasos en las entregas.

Al pie: diagrama de 8 flechas de pasos de análisis de requisitos (igual que slide 12).

## Slide 18

Título: "Desarrollo de Software"

**Diagrama de 6 fases del ciclo de desarrollo** (íconos circulares azules conectados por línea con nodos: diana, lupa, cohete, calendario, cohete despegando, cadena/enlace; debajo tarjetas con etiqueta azul y descripción; la fase "Análisis" resaltada en naranja):

| Fase | Descripción |
|---|---|
| Análisis (resaltada) | ¿Qué debe hacer el software? |
| Diseño | ¿Cómo se hará el software? |
| Implementación | Hacer el Software. |
| Pruebas | ¿El software hace lo que se supone que debe hacer? |
| Despliegue | Entregar, poner en marcha. |
| Mantenimiento | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

## Slide 19

Slide de cierre. "GRACIAS", subtítulo "CHRISTIAN PAZ TRILLO". Imagen decorativa de fondo (dos personas con lentes de seguridad y bata trabajando en un laboratorio). Chrome UTEC / TransformaTec — decorativo.
