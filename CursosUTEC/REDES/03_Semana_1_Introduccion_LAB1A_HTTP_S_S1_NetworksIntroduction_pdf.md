---
curso: REDES
titulo: 03 - Semana 1 _ Introducción + LAB1A_HTTP/[S]S1_NetworksIntroduction 
fuente: 03 - Semana 1 _ Introducción + LAB1A_HTTP/[S]S1_NetworksIntroduction .pdf
slides: 23
---

# S1 — Networks Introduction (CS4054 Computer Networks 2026-1)

> Nota general: casi todas las slides de contenido llevan el mismo chrome decorativo (pie "CS4054 Computer Networks 2026-1 / garias@utec.edu.pe" + logo UTEC abajo a la derecha, y un chevron/flecha celeste con el número de slide arriba a la izquierda). No se repite en cada slide; se ignora como plantilla.

## Slide 1

Portada (decorativa: foto de arquitectura de concreto brutalista con recorte diagonal y cintas celestes; logo UTEC abajo-izquierda).

Título: **Introduction**
Subtítulo: Computer Networks — **LABORATORY**

Pie: PROF.: garias@utec.edu.pe

## Slide 2

Slide de presentación del instructor. Foto tipo retrato (hombre joven en terno con corbata) a la izquierda; a la derecha un recuadro negro con el texto. Fondo decorativo azulado de edificio + palmeras.

**Gabriel A. Arias Obregón**
garias@utec.edu.pe
**Instructor**
**Department of Computer Science**

"I am a graduate of the National University of Engineering (UNI) and a member of the GRFMO research group. My main research areas include Instrumentation, Small Satellites, and Interdigitated Circuits.
I enjoy sharing knowledge, always willing to support my students. I look forward to guiding you through this course and learning together."

## Slide 3

**Executive Summary**

- **Overview:**
  1. Course logistics.
  2. About the laboratory course.
  3. About the laboratory reports.
  4. Groups.
  5. Questions and doubts.

(Solo texto, sin figuras.)

## Slide 4

**Outline** — lista de 5 barras grises horizontales apiladas (estilo agenda), ninguna resaltada todavía:

- Course Logistics
- About the laboratory course
- About the laboratory reports.
- Groups
- Questions and doubts.

## Slide 5

**Outline** — misma lista de 5 barras. Aquí la **primera barra ("Course Logistics") está resaltada en celeste**, indicando la sección activa. El resto en gris.

## Slide 6

**Evaluation**

Tabla de dos columnas (concepto de evaluación / semana del ciclo regular). Encabezados de fila en gris oscuro:

| Teoría 52% | Ciclo regular |
|---|---|
| Examen Parcial (EP) 26% | Semana 8 |
| Examen Final (EF) 26% | Semana 16 |
| **Práctica y/o laboratorio 48%** | |
| Laboratorio 1 (L1) 12% | Semana 4 |
| Laboratorio 2 (L2) 12% | Semana 6 |
| Laboratorio 3 (L3) 12% | Semana 10 |
| Laboratorio 4 (L4) 12% | Semana 12 |
| **100%** | |

Fórmula de la nota final (debajo de la tabla):

$$NF = 0.26 \times EP + 0.26 \times EF + 0.12 \times (L1 + L2 + L3 + L4)$$

## Slide 7

**Important Rules**

- **Zero Tolerance Policy**: Cheating and plagiarism are "very serious" offenses. Sanctions range from a two-semester suspension to permanent expulsion.
- **Assessment Rules**: Unless explicitly stated as a group project, all evaluations are strictly individual. Any unauthorized collaboration or interaction is considered cheating.
- **Prohibited Items**: The use of cell phones, communication apps, or sharing materials (calculators, notes) during exams is forbidden regardless of the reason.
- **Shared Responsibility**: In cases of suspicious similarity between works, both the provider and the receiver of the information will be penalized equally. *(esta viñeta va resaltada con una franja verde claro de fondo)*
- **Disciplinary Process**: Faculty may void exams, issue warnings, and report students to the Department Director. A second warning automatically triggers a formal disciplinary procedure.

## Slide 8

**Important Rules**

**Punctuality:**
- **Tolerance** time for arrival to class: **10 minutes.** *(resaltado en amarillo)*
- If you arrive late for the entrance or exit test, you will not be able to take it.

**Order:**
- No profanity or bad language.
- Respectful treatment.

**Questions?**
Call with respect ("Profesor")

## Slide 9

**Logistics**

**Official communications**, such as **excused absences**, **technical issues, or matters of similar importance**, must be sent solely and exclusively via email to garias@utec.edu.pe.
> **Case**: One or more team members go AWOL.

**Minor inquiries** or **quick questions** may also be sent via Gmail messages (Hangouts/Chat).

## Slide 10

**Regarding the Laboratory Reports**

**Turnitin Originality** will be used. If your laboratory report shows a **plagiarism percentage higher than 25%, 3 points will be automatically deducted with no right to appeal.** *(texto en rojo)*

Each report must include a list of the people who worked on the project/lab and their specific contributions, e.g.:

Recuadro/plantilla de ejemplo de carátula de reporte (fondo celeste degradado):

> UNIVERSIDAD DE INGENIERÍA Y TECNOLOGÍA
> Computer Science
>
> **Título del Reporte**
> Curso
>
> Integrantes del Grupo
> - Integrante 1: revisión bibliográfica/búsqueda de normas/
> - Integrante 2: implementación de nodo sensor/revisión bibliográfica
> - Integrante 3: implementación de nodo sensor/revisión bibliográfica/frontend

## Slide 11

**Outline** — misma lista de 5 barras. Aquí la **segunda barra ("About the laboratory course") está resaltada en celeste**; el resto en gris.

## Slide 12

**CS4054 - Computer Networks**

- **Introduces** and describes essentials **of Computer Network design.**
- **Objectives:** *(título en rojo)*
  - Introduce fundamental definitions for **Computer Networks**.
  - Explain the operation of computer networks: **from the application layer to the physical link.**
  - **Experiment** with a controlled environment in lab sessions.
- **Content:** *(título en verde)*
  Distributed in **two modules**:
  - First module, from Week 1 to Week 8
  - Second module, from Week 9 to Week 16

(Uso de color como énfasis: "Objectives" en rojo, "Content" y "two modules" / semanas en verde.)

## Slide 13

**CS4054 - Computer Networks**

What are the subjects of the Laboratories?

- **LAB1a**: HTTP
- **LAB1b**: DNS
- **LAB2**: UDP
- **LAB3a**: TCP
- **LAB3b**: RDT
- **LAB4a**: IP
- **LAB4b**: ICMP
- **LAB4c**: NAT
- **AE**: Ethernet Cable

(Lista que recorre el stack de protocolos de arriba hacia abajo: aplicación HTTP/DNS → transporte UDP/TCP/RDT → red IP/ICMP/NAT → enlace físico Ethernet.)

## Slide 14

**Outline** — misma lista de 5 barras. Aquí la **tercera barra ("About the laboratory reports.") está resaltada en celeste**; el resto en gris.

## Slide 15

**Laboratory Reports**

The reports **must** be written in LaTeX (Overleaf). *("must" en rojo)*
- **Recommended template\*:**
  https://www.overleaf.com/latex/templates/ieee-journal-paper-template/jbbbdkztwxrd *(enlace subrayado)*

The submission should consist of:
1. Introduction
   a. Theoretical Framework
   b. State of the Art
2. Development of the experience (including discussion)
3. Conclusions
4. References

\* Another template with one or two columns is allowed.

## Slide 16

**Laboratory Reports**

- It is a **requirement** to have checkpoints marked by the teacher, so that the development of your lab report can be reviewed.
  > **Without checkpoints, the developed section is not reviewed.** *(resaltado en amarillo, texto rojo)*
- The **deadline** is defined by the teacher.
- Submission of checkpoints is **only given during lab time**.
  > **No email validation is allowed.** *(resaltado en amarillo, texto rojo)*

## Slide 17

**Grading**

- Laboratory Report: **14** pts.
- Exit Test: **6** pts.
- Exercise sessions: You may get **+1** point.

(Solo texto, sin figuras.)

## Slide 18

**Outline** — misma lista de 5 barras. Aquí la **cuarta barra ("Groups") está resaltada en celeste**; el resto en gris.

## Slide 19

**Groups**

- All laboratory experiments will be done in **groups of 3 students (or 4, with the teacher's authorization).**
- The groups are **fixed**, *no changes* will be made between labs.
- All group members **must be present** at the lab session to validate the group checkpoint.
- In case a student is not present without prior notice or authorization from the teacher, **the checkpoint will not be counted for that student (even if the group has done it).**

## Slide 20

**Outline** — misma lista de 5 barras. Aquí la **quinta barra ("Questions and doubts.") está resaltada en celeste**; el resto en gris.

## Slide 21

Slide de transición / motivacional.

Título: **Enjoy the Networks trip** (subrayado)

Figura central: ilustración/caricatura de dos científicos famosos sobre fondo estelar cósmico — a la izquierda un joven (estilo Nikola Tesla) sosteniendo una esfera de plasma/rayos de electricidad en la mano, a la derecha un anciano de cabello blanco alborotado (estilo Albert Einstein) sosteniendo una galaxia. Fondo decorativo azulado de edificio + palmeras.

## Slide 22

**Questions?**

Slide de cierre, solo el título grande. Sin contenido adicional.

## Slide 23

**Thanks!**

Slide final de agradecimiento, solo el título grande. Sin contenido adicional.
