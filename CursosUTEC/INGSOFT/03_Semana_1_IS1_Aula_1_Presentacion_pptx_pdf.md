---
curso: INGSOFT
titulo: 03 - Semana 1/IS1 - Aula 1 - Presentación__pptx
slides: 24
fuente: 03 - Semana 1/IS1 - Aula 1 - Presentación__pptx.pdf
---

## Slide 1

Portada. Título grande "Ingeniería de Software" y subtítulo "Aula de Presentación: Profesor Christian Paz". Fondo decorativo (túnel tecnológico azul con silueta de una figura humanoide/robot caminando). Chrome UTEC / "Reinventa el mundo" / TransformaTec.

## Slide 2

**Agenda** (título vertical a la izquierda). Foto decorativa de dos personas trabajando en oficina. Lista de puntos:

- Presentación.
- Qué es ser un Ingeniero de Software?
- Camino Profesional del Ingeniero de Software.
- Sobre el curso.
- "Pre-requisitos".

## Slide 3

Divisor de sección. Número "1." grande e ícono de portapapeles/checklist, con el texto **"Presentaciones"**. Imagen decorativa (mano robótica tocando un globo terráqueo digital).

## Slide 4

**Profesor: Christian Paz**

- Ingeniero de Sistemas – Universidad Nacional de San Agustín.
- MSc. Ciencia da Computação - Universidade de São Paulo - Brasil.
- 15+ Años de Experiencia en Desarrollo de Software.
- (2020+) Software Engineer en Microsoft - Enterprise Copilot Platform.
- (2013-2020) Software Architect en SAP – Ariba.

Imagen decorativa de personas a la izquierda.

## Slide 5

**Mi proyecto**

La slide muestra un **diagrama de arquitectura de Microsoft 365 Copilot** (captura oficial de Microsoft Learn). Flujo con pasos numerados 1–4:

- **Your users and devices** (íconos de usuario y dispositivo) → **Apps on your devices** (íconos de Edge, Word, Teams, Excel, Outlook y un "+").
- Las apps se conectan con la caja **Microsoft 365 Copilot** (con flechas etiquetadas **1** y **4** en el sentido apps↔Copilot).
- Paso **3**: Copilot ↔ **Azure OpenAI service subscription for Microsoft 365** que contiene el **Large Language Model (LLM)**.
- Paso **2**: Copilot ↔ **Microsoft Graph**, que a su vez accede a **User-accessible data** (Files, mailboxes, chat data, videos, etc.), con cuatro fuentes: **Exchange mailboxes**, **OneDrive files**, **Microsoft Teams data**, **SharePoint files, lists, etc.**
- Microsoft Graph y los datos están dentro del recuadro **"Your Microsoft 365 tenant"**.
- Todo el bloque tenant + Graph + Azure OpenAI está encerrado por una línea punteada = **Microsoft 365 service boundary**, con un ícono de candado y la nota **"Data is encrypted in transit"**.

Al pie, la URL: https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture

## Slide 6

**Dinámica**

> Juntarse en el equipo que hicieron Cloud o DBP:
> - Describir el proyecto (funcional).
> - Describir el proyecto (técnico)
> - Describir que lograron y que les faltó.
>
> Pregunta: Otro equipo de desarrollo podría continuarlo?

Imagen decorativa a la izquierda.

## Slide 7

Divisor de sección. Número "2." e ícono de portapapeles con el texto **"Qué es ser un Software Engineer?"**. Imagen decorativa (mano robótica y globo digital).

## Slide 8

**Qué hago como Software Engineer?**

Recibo, como parte de un equipo, descripciones de necesidades, con algunas especificaciones funcionales y algunas no funcionales.

*"Permitir que las aplicaciones cliente puedan decidir si acceder información de los repositorios Git de la empresa a través de la API de github".*

(Banda superior decorativa con foto de equipo y líneas tipo circuito.)

## Slide 9

**Qué hago como Software Engineer?**

Analizo cómo satisfacer esa necesidad dentro del entorno de código existente, librerías, considerando diversos aspectos:

- Seguridad.
- Estándares.
- Performance.
- Almacenamiento.
- Calidad.
- Tiempo y esfuerzo.

## Slide 10

**Qué hago como Software Engineer?**

Como parte del equipo, dividimos las tareas de forma que se aprovechen las habilidades y, en la medida de lo posible, las preferencias de cada integrante del equipo, para realizar determinadas tareas.

Planeamos y diseñamos lo que sea necesario para realizar la tarea, y coordinamos en caso las tareas tengan algún punto de interacción o dependencia.

Alineamos las dependencias con otros equipos de trabajo u otros sistemas.

## Slide 11

**Qué hago como Software Engineer?**

Se desarrolla el código necesario, pasando por un proceso de revisión de pares.

Se crean pruebas unitarias junto al código.

Se prepara un plan o estrategia de pruebas o validación.

El software pasa por diversos ambientes antes de llegar al "mundo real".

## Slide 12

**Qué hago como Software Engineer?**

Se planifica cómo se desplegará la funcionalidad.

Se realiza una planificación inicial de los recursos necesarios dada la demanda esperada.

Se planifica formas de "monitorear" las nuevas funcionalidades: cantidad de uso, latencia, tasa de errores, downtime, etc.

## Slide 13

Divisor de sección. Número "4." e ícono de portapapeles con el texto **"Cómo será el curso?"**. Imagen decorativa (mano robótica y globo digital).

(Nota: la numeración salta de 2 a 4; en la presentación no aparece una sección "3.")

## Slide 14

**Horarios**

- Teoría: Lunes 6pm – 8pm (Aula 703)
- Laboratorio:
  - Martes 8pm – 10pm (M603)
  - Miércoles 8pm – 10pm (M604)

## Slide 15

**Laboratorio**

Trabajaremos en el Proyecto Open Source Zulip.

- Parte 1: Instalar el Software y ejecutar en local.
- Parte 2: Contribución al Proyecto con un fix del backlog.
- Grupos de 2 o 3 personas máximo.
- Parte 3: Implementar un feature nuevo (propuesto por el professor)

## Slide 16

**Calificaciones**

Columna izquierda (texto):

Teoría:
- 6 Ejercicios Teórico/Prácticos (Consideraré las 4 mejores, excepto que falte alguna)
- Examen Final: Construir una API.

Columna derecha (texto, sobre Zulip):
- Atender un ticket (issue) y publicarlo.
- Requerimiento funcional propuesto por el profesor.
- Criterios: Commits individuales, Code Coverage, Impacto en otros módulos, revision de código.

Arriba a la derecha, **tabla de pesos de evaluación**:

| Evaluación | Teoría | Práctica y/o Laboratorio |
|---|---|---|
| | Evaluación C1 (5%) | Preparación Ambiente P1 (5%) |
| | Evaluación C2 (5%) | Fix P2 (5%) |
| | Evaluación C3 (5%) | Análisis y Diseño P3 (10%) |
| | Evaluación C4 (5%) | Implementación P4 (15%) |
| | Examen Final (30%) | Pruebas y Despliegue P5 (15%) |

## Slide 17

**Visión del Curso**

Diagrama importado (banner) titulado **"6 Phases of the Software Development Life Cycle"**: seis flechas/chevrones de colores en secuencia, cada una con los roles asociados debajo.

| Fase | Roles |
|---|---|
| **ANALYSIS** (celeste) | Product Owner, Project Manager, Business Analyst, CTO |
| **DESIGN** (morado) | System Architect, UX/UI designer |
| **DEVELOPMENT** (púrpura oscuro) | Front-end Developer, Back-end Developer |
| **TESTING** (vino) | Solutions Architect, QA Engineer, Tester, DevOps |
| **DEPLOYMENT** (magenta) | Data Administrator, DevOps |
| **MAINTENANCE** (naranja) | Users, Testers, Support managers |

## Slide 18

**Desarrollo de Software**

Infografía de proceso en 6 etapas: fila de círculos azules con íconos (diana, lupa, cohete, calendario/checklist, cohete despegando, cadena/enlace) conectados por una línea horizontal con nodos amarillos. Debajo, tarjetas con el nombre de la etapa y su pregunta guía:

| Etapa | Descripción |
|---|---|
| **Análisis** | ¿Qué debe hacer el software? |
| **Diseño** | ¿Cómo se hará el software? |
| **Implementación** | Hacer el Software. |
| **Pruebas** | ¿El software hace lo que se supone que debe hacer? |
| **Despliegue** | Entregar, poner en marcha. |
| **Mantenimiento** | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

## Slide 19

**¿Qué es Ingeniería de Software?**

Slide tipo cita (fondo azul con comillas decorativas grandes):

> *"Is an engineering discipline that is concerned with all aspects of software production from initial conception to operation and maintenance."*
>
> Autor: Sommerville, Software Engineering.

## Slide 20

**Para evitar confusiones**

Diagrama de tres círculos con íconos (lupa, diana, cohete) dispuestos en zig-zag, cada uno conectado por líneas amarillas a una definición:

- **Software Engineering**: Concerned with the practicalities of developing and delivering useful software.
- **Computer Science**: Focused on theory and fundamentals.
- **Software Engineer**: Professional in charge of creating, updating and/or maintaining software.

Contraste: la disciplina (SE) vs la teoría (CS) vs el profesional (Software Engineer).

## Slide 21

Divisor de sección. Número "5." e ícono de portapapeles con el texto **"Pré-requisitos"**. Imagen decorativa (mano robótica y globo digital).

## Slide 22

**Qué necesito para hacer este curso?**

- Algún lenguaje de programación para back-end.
- Algún lenguaje de programación para front-end.
- Nociones y práctica en uso de repositorios Git.

## Slide 23

**Conclusiones**

- ➤ Motivación del curso.
- ➤ Estructura del curso.

Imagen decorativa a la derecha (profesor escribiendo en pizarra frente a alumnos, teñida de azul).

## Slide 24

Cierre. Título **"GRACIAS"** y subtítulo **"CHRISTIAN PAZ TRILLO"**. Fondo decorativo (foto de laboratorio con dos personas trabajando, teñida de azul).
