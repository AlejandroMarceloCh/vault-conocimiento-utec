---
curso: LIDSI
titulo: 15 - Semana 13/Sem13_Sesion23
slides: 25
fuente: 15 - Semana 13/Sem13_Sesion23.pdf
---

## Slide 1

Portada del curso (decorativa: fotografía arquitectónica del campus UTEC en hexágonos, logo UTEC).

**LIDERAZGO EN SISTEMAS DE INFORMACIÓN.**
2026-1

Sesión 23: Liderar en entornos impulsados por inteligencia artificial, datos y tecnologías en la nube, considerando principios de IA responsable, ética del uso de datos y el rol de las plataformas digitales.

## Slide 2

Slide de índice sobre fondo celeste sólido con fotografía arquitectónica decorativa a la derecha.

**Índice**
1. Objetivos
2. Saberes previos
3. Casos
4. Conclusiones

## Slide 3

Slide separador de sección (fondo blanco, foto arquitectónica decorativa a la derecha).

**1. Objetivos**

## Slide 4

Slide de texto: **Objetivos**

Sesión de cierre. Al finalizar, el estudiante será capaz de:
- Repasar los conceptos clave de IA responsable: atributos, pilares y la decisión comprar/potenciar/construir.
- Contrastar dos casos reales: Fuel iX (gobernanza como producto) y Anthropic (autonomía vs. poder).
- Aplicar todo lo aprendido diseñando una solución de IA gobernada para un caso de salud (MediClínica Perú).

## Slide 5

Slide separador de sección (fondo blanco, foto arquitectónica decorativa a la derecha).

**2. Saberes previos**

## Slide 6

**IA RESPONSABLE — Cinco atributos de diseño IA que los consumidores valoran**

5 tarjetas en fila, cada una con ícono, nombre, descripción y porcentaje:

| Atributo | Ícono | Descripción | % |
|---|---|---|---|
| Auditabilidad | ojo | Trazar y revisar decisiones del sistema, con supervisión humana | 26% |
| Privacidad | candado | Proteger datos y confidencialidad del usuario | 31% |
| Entendibilidad | libro abierto | Claridad sobre el porqué de los resultados | 11% |
| Autonomía | robot | Grado en que decide sin intervención humana | 23% |
| Personalización | grupo de personas | Adaptar funciones al usuario individual | 9% |

Recuadro inferior: "El % es la importancia que pesa en la decisión de compra (app de pensiones). Privacidad + auditabilidad (atributos responsables) dominan → introducir atributos responsables subió la adopción del 2.4% al 63.2%."

Fuente: Acar, Wiertz & Ghosh, 'How Responsible AI Protects the Bottom Line', HBR (mar 2025), 3 estudios, n=3,268 consumidores.

## Slide 7

**IA RESPONSABLE — Del principio a la práctica: 4 pilares operativos y el rol del líder**

Tabla/lista de 4 filas, cada una con ícono + nombre del pilar, columna "Problema" y columna "Rol del líder":

| Pilar (ícono) | Problema | Rol del líder |
|---|---|---|
| Equidad y sesgo (balanza) | Los algoritmos aprenden de datos históricos sesgados. | Exigir auditorías de sesgo; priorizar equidad aunque baje algo la precisión. |
| Transparencia / XAI (ojo) | Modelos 'caja negra' deciden sin explicación clara. | No aceptar 'el algoritmo lo decidió'. Exigir explicabilidad en dominios de alto riesgo. |
| Privacidad y seguridad (candado) | Sistemas que requieren datos personales sensibles. | Privacy by design; privacidad diferencial / aprendizaje federado. |
| Rendición de cuentas (martillo) | ¿Quién responde cuando la IA falla? | Comités de ética; human-in-the-loop; el líder asume la responsabilidad final. |

Fuente: Blackman, HBR (2023); O'Neil, 'Weapons of Math Destruction'.

## Slide 8

**DE PRINCIPIOS A OPERACIÓN — Antes de pilotear IA: clasificar riesgo y definir guardrails**

Subtítulo: "Una política útil debe decir qué sí, qué requiere aprobación, qué nunca se permite y cómo pedir excepción."

**1. Clasificar el caso de uso** — matriz 4x3 (Impacto del error × Autonomía del sistema):

| Impacto del error / Autonomía | Baja autonomía | Autonomía media | Alta autonomía |
|---|---|---|---|
| Bajo impacto | Usar como apoyo | Supervisar muestras | Control humano |
| Impacto medio | Validar outputs | Aprobación humana | Auditoría + legal |
| Alto impacto | Piloto controlado | No escalar sin RMF | Comité + rediseño |

**2. Aplicar guardrails mínimos** — 3 recuadros:
- **Siempre permitido** (verde): Información pública, borradores internos sin datos sensibles, aprendizaje guiado.
- **Con aprobación** (naranja): Datos internos no públicos, análisis de clientes, código propietario o automatización con impacto operativo.
- **Nunca permitido** (rojo): PII sin autorización, secretos comerciales, credenciales, salud/legal o decisiones críticas sin humano. Nota al pie: *PII: Personally Identifiable Information/información personal identificable. Cualquier dato que permite identificar directa o indirectamente a una persona.

Fuentes: NIST AI RMF 1.0; EU AI Act risk-based approach; ISO/IEC 42001:2023; MIT CISR, GenAI governance/guardrails (2024–2026).

## Slide 9

**DECISIÓN DE PLATAFORMA — Comprar, potenciar o construir IA: la decisión que define el valor capturado**

3 tarjetas en columnas, cada una con encabezado de color y secciones "Qué es", "Trade-off", "Cuándo":

| | COMPRAR (Buy) | POTENCIAR (Boost) | CONSTRUIR (Build) |
|---|---|---|---|
| Qué es | El proveedor corre el modelo. Adopción rápida, pago por uso. | Mejoras un modelo con datos propios (fine-tuning, RAG). | Asumes desarrollo y operación completos del modelo. |
| Trade-off | Opaco y de contexto estrecho. | Más contexto, pero sube el costo por uso. | Caro al inicio; requiere capacidades avanzadas de datos. |
| Cuándo | Cuando necesitas velocidad y paridad competitiva. | Cuando hay necesidad fuerte de contextualización. | Cuando buscas un diferenciador difícil de imitar. |

Fuente: Van der Meulen & Wixom, 'Managing the Two Faces of Generative AI', MIT CISR (sep 2024).

## Slide 10

Slide separador de sección (fondo blanco, foto arquitectónica decorativa a la derecha).

**3. Casos**

## Slide 11

**Caso 2 — TELUS: la gobernanza como producto**

4 tarjetas numeradas en cuadrícula 2x2:
1. **Contexto: la empresa** — TELUS Digital (Canadá): telecom y servicios digitales. Detectó que 54% de empleados usaba IA pública y 57% subía datos sensibles.
2. **Producto: Fuel iX** — Plataforma de gobierno de IA. Uso doble: la usan internamente y la licencian a otras empresas (B2B). Convierte el shadow-AI en capacidad gobernada. (Logo "Fuel iX — AI-fueled intelligent experiences", link https://www.telusdigital.com/solutions/fuel-ix)
3. **La IA en acción** — Gateway multi-modelo: el empleado elige entre 40+ modelos (Claude es uno) según la tarea, con guardrails centralizados, RBAC y monitoreo continuo (Fortify).
4. **IA responsable real** — Privacidad certificada: 1ª certificación Privacy by Design (ISO 31700-1) para su chatbot de soporte. Trazabilidad + control = atributos responsables aplicados.

Recuadro destacado a la derecha: "¿FUE RENTABLE? → A PLAZO — **−42%** EBITDA ajustado de TELUS Digital cayó en Q4 2024, en parte por invertir en lanzar Fuel iX. A corto plazo es COSTO; la apuesta es monetizar la gobernanza como producto y diferenciarse. No vende 'acceso a Claude': vende CONTROL, cumplimiento y confianza."

Nota inferior: "Concepto aplicado: lo opuesto a Air Canada. El valor (y el precio) no está en el modelo, sino en las capas de gobernanza que lo rodean: guardrails, privacidad, auditabilidad y supervisión."

Fuente: TELUS Digital (estudio BYO-AI); TELUS Corp. Form 6-K Q4 2024 (SEC); certificación ISO 31700-1.

## Slide 12

**Caso 2 — TELUS: la gobernanza como producto — Fuel iX: cómo viaja una consulta**

Diagrama de flujo vertical (izquierda) con 5 pasos numerados y flechas descendentes:
1. **Control de acceso (RBAC)** — Quién accede a qué modelo y dato
2. **Gateway multi-modelo** — Elige entre 40+ modelos según la tarea
3. **Orquestación / RAG** (RAG = Retrieval-Augmented Generation / Generación Aumentada por Recuperación) — Recupera datos internos de la empresa
4. **Generación** — El modelo elegido produce el borrador
5. **Guardrails (control central)** — Filtran alucinación y datos sensibles
→ **Respuesta al empleado** (caja final verde)

A la izquierda del paso 5 hay una caja roja "Bloqueo o escala a humano" conectada con flecha desde el paso 5 (indicando que el guardrail puede bloquear o escalar antes de llegar a la respuesta).

Recuadro a la derecha: "MONITOREO TRANSVERSAL — Fortify corre en paralelo a todo el flujo, no en la ruta de la consulta: Validación continua de guardrails · Red-teaming (pruebas adversarias) · Auditoría y trazabilidad de prompts, modelos e integraciones · Dashboard central de visibilidad."

Nota inferior: "El modelo (paso 4) está rodeado de gobernanza, nunca expuesto directo. Acceso → procesamiento → comportamiento → supervisión."

Fuente: arquitectura Fuel iX de TELUS Digital (gateway multi-modelo, guardrails centralizados, Fortify).

## Slide 13

**Caso 2 — TELUS: la gobernanza como producto — Cómo implementar IA gobernada (no shadow AI)**

5 tarjetas numeradas:
1. **Auditar el uso actual** — Descubrir qué herramientas de IA usan ya los empleados — incluido el shadow AI invisible.
2. **Centralizar el acceso** — Un gateway único como puerta de entrada. Las claves de API nunca tocan la máquina del empleado.
3. **Definir políticas** — RBAC (quién accede a qué) + guardrails (qué puede decir la IA) + clasificación de datos sensibles.
4. **Humano en el bucle** — Para decisiones importantes, la IA propone y el humano aprueba. Nunca automatizar lo crítico sin revisión.
5. **Monitorear y medir** (recuadro ancho abajo, resaltado en verde) — Auditar el uso, medir costo y calidad de forma continua. La gobernanza es un proceso, no un setup único.

Nota inferior: "No prohibir la IA, gobernarla. Prohibir empuja al uso a escondidas. El valor está en las capas de control, no en el modelo."

## Slide 14

**Caso 3 — Anthropic: salvaguarda vs. poder — Anthropic vs EE.UU: control de IA**

Infografía tipo panel completo (captura/diseño gráfico), organizada en dos mitades:

Mitad izquierda: **"Contexto"** — En junio de 2026, el lanzamiento de los modelos Fable 5 y Mythos 5 de Anthropic provocó una intervención sin precedentes del gobierno estadounidense. Lo que comenzó como una alianza técnica para defensa terminó en un veto total debido a desacuerdos éticos sobre el uso militar de la IA y supuestas vulnerabilidades de seguridad nacional.

**"El Camino a la Ruptura (2021 - Mayo 2026)"** con 3 hitos ilustrados (íconos):
- 2021-2023: El Nacimiento de la IA Constitucional — Investigadores de OpenAI fundan Anthropic enfocándose en seguridad y reglas éticas integradas (IA Constitucional).
- 2024-2025: De Socio a "Riesgo de Suministro" — El Pentágono exige flexibilidad para vigilancia masiva; Anthropic se niega, priorizando sus límites éticos.
- El Reemplazo por OpenAI — Tras la fricción con Anthropic, el Departamento de Guerra firma un acuerdo rápido con OpenAI.

Mitad derecha: **"La Crisis de Junio: El Gran Veto (Junio 2026)"** con íconos e hitos:
- 9 de Junio: El Lanzamiento de la Clase "Mythos" — Anthropic presenta Fable 5 y Mythos 5, sus modelos más capaces con razonamiento autónomo avanzado.
- 12 de Junio: Orden de Suspensión Global — El gobierno invoca el control de exportaciones para bloquear el acceso tras detectar un supuesto "jailbreak".
- Impacto: La IA como Infraestructura Estratégica — El conflicto demuestra que el Estado ahora trata a la IA como un activo de seguridad nacional.

Abajo a la derecha: **"Comparación de Modelos Suspendidos (Junio 2026)"** — 3 tarjetas:
- Claude Fable 5 — SUSPENDIDO — Tipo de Acceso: Público General (Suspendido) — Pensamiento adaptativo siempre activo y ventana de 1M de tokens.
- Claude Mythos 5 — SUSPENDIDO — Tipo de Acceso: Limitado / Proyecto Glasswing — Máxima capacidad sin clasificadores de seguridad adicionales.
- Claude Opus 4.8 — ACTIVO — Tipo de Acceso: Activo (No afectado) — Enfocado en honestidad y confiabilidad; reemplazo sugerido por el gobierno.

(Nota: esta infografía usa nombres de modelos y escenario ficticios/hipotéticos de ejemplo del caso, no productos reales de Anthropic.)

## Slide 15

**Caso 3 — Anthropic: salvaguarda vs. poder**

Recuadro izquierdo (marco azul) "QUÉ PASÓ":
- **Jun 2026:** EE.UU. ordena a Anthropic cortar el acceso de nacionales extranjeros a sus modelos más avanzados (Fable 5 / Mythos 5) por riesgos de ciberseguridad. Anthropic desactiva ambos modelos para todos.
- **Freno propuesto:** Anthropic ya proponía la idea de poder pausar voluntariamente la creación de modelos más potentes, para dar tiempo a que la investigación en seguridad alcance el nivel de lo que esos modelos ya pueden hacer.
- **Detonante:** auto-mejora recursiva — agentes que mejoran sin intervención humana (~80% del código nuevo lo escribe su propio modelo).

Columna derecha "CONCEPTOS DE IA RESPONSABLE APLICADOS" (4 tarjetas con punto de color):
- Autonomía (naranja): el grado en que la IA decide sin intervención humana llega al extremo: un sistema que se mejora a sí mismo.
- Rendición de cuentas (rojo): ¿quién responde si actúa solo? El human-in-the-loop deja de ser obvio.
- Auditabilidad (azul): trazar y revisar decisiones se vuelve más difícil cuando el modelo escribe su propio código.
- Gobernanza y poder (verde): ¿quién pone el freno: la empresa, el Estado o nadie? El control deja de ser solo técnico.

Nota inferior: "Pregunta de liderazgo: ¿dónde termina la responsabilidad del líder de una plataforma? ¿Sólo de lo que su empresa hace, o también de lo que terceros hacen —y de lo que el sistema podría hacer solo? Mismo dilema que Cambridge Analytica, pero ahora el sistema puede actuar sin un humano."

Fuente: NYT, 'Trump Administration Reignites Its Feud With Anthropic' (jun 2026); 'Anthropic's Call for A.I. Nonproliferation' (jun 2026); anthropic.com/policy.

## Slide 16

**Caso 3 — Anthropic: salvaguarda vs. poder — El precedente: Cambridge Analytica → Anthropic**

Tabla comparativa en 2 columnas con logos (Facebook / Anthropic):

| | Cambridge Analytica · 2018 | Anthropic · 2026 |
|---|---|---|
| Qué pasó / Qué cambia | Una app de test de personalidad en Facebook recogió datos no solo de quien la usaba, sino de todos sus amigos. 87 millones de perfiles terminaron en manos de una consultora política, sin consentimiento. | El daño ya no requiere ni siquiera un tercero malicioso. La IA de frontera puede mejorarse y actuar sola, sin un humano que decida en ese momento. |
| Defensa / Paralelo | La defensa de Facebook: "no fuimos nosotros, fue un tercero que abusó de la plataforma". | Si Facebook respondió por lo que terceros hicieron con su plataforma, ¿quién responde por lo que el sistema hace por sí mismo? |
| Desenlace / Respuesta emergente | No le funcionó. Multa récord de US$5,000 millones (FTC). Respondió por permitir el acceso de terceros, no por robar los datos. | La autonomía no diluye la responsabilidad del líder — la concentra en quien decide desplegar sin freno. |

Nota inferior: "Conceptos aplicados: Privacidad (datos sin consentimiento) · Rendición de cuentas (no vale "fue un tercero") · Autonomía (el sistema actúa solo) · Gobernanza (diseñar el freno antes del daño)"

Fuente: FTC, 'Imposes $5 Billion Penalty on Facebook' (2019); 87 millones de usuarios afectados (Cambridge Analytica, 2018).

## Slide 17

**Actividad: MediClínica Perú**

**Diseñen una solución de IA gobernada**

Una cadena de clínicas quiere lanzar un asistente de IA para que pacientes consulten síntomas y agenden citas. Maneja datos de salud (PII sensible, Ley 29733), presión por reducir el call center y un directorio que pregunta: ¿comprar, potenciar o construir?

En el tablero de Miro, completen las 4 zonas:
1. Clasificar el riesgo (impacto del error × autonomía).
2. ¿Cuáles de los 5 atributos responsables son críticos aquí y por qué?
3. Comprar, potenciar o construir: elijan y justifiquen el trade-off.
4. Diseñen el guardrail: ¿qué nunca se permite y qué requiere aprobación humana?

## Slide 18

**Actividad: MediClínica Perú**

Captura de pantalla de un tablero de Miro llamado "Nexus" mostrando la plantilla de la actividad: "MediClínica Perú · Diseñen una IA gobernada" con nota "7 alumnos · 20 min · cada uno pega 1 sticky por zona (usa tu color) · al final consolidamos en plenaria". Se ven 4 cuadrantes con títulos y descripciones, cada uno con filas de post-its de colores vacíos para los grupos A1-A7:
1. Clasificar el riesgo — ¿Dónde cae MediClínica en la matriz impacto del error × autonomía? ¿Apoyo, supervisión o control humano? (Recuerda: salud = impacto alto. ¿Cuánta autonomía le damos?)
2. Atributos críticos — De los 5 atributos responsables (auditabilidad, privacidad, entendibilidad, autonomía, personalización) ¿cuáles son críticos aquí y por qué?
3. Comprar / Potenciar / Construir — ¿Cuál eligen para MediClínica? Justifiquen el trade-off (velocidad vs. contexto vs. diferenciación).
4. Diseñar el guardrail — ¿Qué NUNCA se permite y qué requiere aprobación humana? (ej.: diagnosticar, prescribir, decidir sin médico).

Link: https://miro.com/app/board/uXjVHJ5VMVE=/

## Slide 19

**Actividad: MediClínica Perú — 1. Clasificar el riesgo (impacto del error × autonomía)**

El caso debe clasificarse como ALTO IMPACTO / alto riesgo, porque involucra salud y datos personales sensibles. Un error del asistente podría afectar la atención de un paciente, generar una mala orientación médica o exponer información protegida por la Ley 29733 — LPDP Perú.

En la matriz, debe ubicarse como:
- Impacto del error: ALTO
- Autonomía del sistema: BAJA
- Uso permitido: apoyo/piloto controlado, no decisión autónoma

Tabla (misma matriz de la slide 8), con la celda "Piloto controlado" (fila Alto impacto, columna Baja autonomía) resaltada en celeste como respuesta correcta:

| Impacto del error / Autonomía | Baja autonomía | Autonomía media | Alta autonomía |
|---|---|---|---|
| Bajo impacto | Usar como apoyo | Supervisar muestras | Control humano |
| Impacto medio | Validar outputs | Aprobación humana | Auditoría + legal |
| Alto impacto | **Piloto controlado** (resaltado) | No escalar sin RMF | Comité + rediseño |

Recuadro a la derecha: "Clasificación: alto riesgo / alto impacto. Razón: maneja datos de salud, PII sensible y puede afectar decisiones de atención. Autonomía permitida: baja. Rol de la IA: apoyo y agendamiento, no diagnóstico. Control requerido: supervisión humana, trazabilidad, privacidad, auditoría y escalamiento a profesional ante señales de alarma. *No escalar sin Risk Management Framework NIST/Marco de Gestión de Riesgos"

## Slide 20

**Actividad: MediClínica Perú**

**2. ¿Cuáles de los 5 atributos responsables son críticos aquí y por qué?**

Dominan los atributos responsables igual que en el estudio HBR:
- Privacidad — datos de salud = categoría especial (Ley 29733). Imprescindible.
- Auditabilidad — trazar qué dijo el bot y revisarlo (lección Air Canada).
- Entendibilidad — explicar por qué deriva o agenda.
- Autonomía debe ser BAJA; personalización es secundaria aquí.

**3. Comprar, potenciar o construir: elijan y justifiquen el trade-off**

No hay respuesta única; de acuerdo a justificación:
- Potenciar (RAG) suele ser la mejor: modelo base + datos propios: catálogo de citas, FAQ verificadas → reduce alucinación. Es lo que hace Fuel iX.
- Comprar: rápido pero "contexto estrecho y opaco" → riesgoso en salud.
- Construir: caro, solo si fuera el diferenciador central —no lo es para agendar citas.

## Slide 21

**Actividad: MediClínica Perú**

**4. Diseñen el guardrail: ¿qué nunca se permite y qué requiere aprobación humana?**

Nunca permitido:
- Diagnosticar, prescribir o dar dosis.
- Afirmar coberturas/políticas sin verificar fuente —error exacto de Air Canada.
- Exponer PII de otros pacientes.

Requiere humano: derivar urgencias a un profesional; cualquier síntoma de alarma escala a médico de inmediato.

## Slide 22

Slide separador de sección (fondo blanco, foto arquitectónica decorativa a la derecha).

**4. Conclusiones.**

## Slide 23

**CONCLUSIONES**

1. El valor no está en el modelo, sino en las capas de gobernanza que lo rodean: guardrails, privacidad, auditabilidad y supervisión humana.
2. Fuel iX (TELUS) muestra el camino positivo: no prohibir la IA, gobernarla. La gobernanza puede ser un producto y un diferenciador.
3. Anthropic eleva la apuesta: cuando el sistema actúa solo, la autonomía no diluye la responsabilidad del líder — la concentra en quien decide desplegar.
4. El rol del líder de SI: saber cuándo escalar a legal, seguridad y data governance, y diseñar el freno antes del daño, no después.

## Slide 24

Slide de cierre, solo texto centrado sobre fondo blanco con marca de agua hexagonal decorativa.

**Dudas?**

## Slide 25

Slide final de cierre, solo texto sobre fondo blanco con marca de agua hexagonal decorativa.

**GRACIAS.**
