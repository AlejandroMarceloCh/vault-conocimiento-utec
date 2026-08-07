---
curso: LIDSI
titulo: 18 - Semana 16/Sem16_Sesion26
slides: 19
fuente: 18 - Semana 16/Sem16_Sesion26.pdf
---

## Slide 1

Portada del curso (decorativa: logo UTEC, foto arquitectónica del campus en hexágonos azules).

- Título: "LIDERAZGO EN SISTEMAS DE INFORMACIÓN."
- "2026-1"
- "Sesión 26: Liderar IA confiable: RAG - Generación Aumentada por Recuperación como decisión de liderazgo."

## Slide 2

Slide de índice sobre fondo azul sólido, con fotografía arquitectónica decorativa a la derecha (hexágonos).

Título: "Índice"

1. Objetivos
2. RAG: Generación Aumentada por Recuperación como decisión de liderazgo, no solo de arquitectura.
3. Conclusiones

## Slide 3

Slide separador de sección (decorativo: numeral grande "1.", imágenes arquitectónicas en hexágonos a la derecha).

Texto: "Objetivos"

## Slide 4

Slide de texto con los objetivos de la sesión.

Título: "Objetivos"

Texto: "Al finalizar la sesión el estudiante será capaz de:"

Lista numerada:
1. Explicar RAG en lenguaje de negocio: Qué es el flujo recuperar-luego-generar y por qué corrige alucinación y obsolescencia del LLM.
2. Distinguir RAG de fine-tuning y de "comprar el modelo": tomar la decisión comprar, potenciar o construir desde el rol de líder de SI.
3. Conectar RAG con IA responsable y ética del dato: trazabilidad, control de acceso en la recuperación y humano-en-el-loop.
4. Evaluar el caso de negocio con cifras: ROI, reducción de alucinaciones y el riesgo de "fuga de productividad".
5. Decidir como líder: escalar, rediseñar o cerrar: el cuello de botella es la capa de conocimiento, no el modelo.

## Slide 5

Slide separador de sección (decorativo: numeral grande "2.", imágenes arquitectónicas en hexágonos a la derecha).

Texto: "RAG: Generación Aumentada por Recuperación como decisión de liderazgo, no solo de arquitectura."

## Slide 6

Categoría (kicker): "EL PROBLEMA DE LIDERAZGO"

Título: "El LLM solo, sin tus datos, es un riesgo de negocio"

Layout de dos columnas:

**Columna izquierda** — recuadro con cita destacada (ícono de comillas):
> "Para resolver una tarea, un modelo necesita las instrucciones y también la información. Igual que una persona, la IA falla y alucina cuando le falta contexto."
> — Chip Huyen — AI Engineering (O'Reilly, 2025)

**Columna derecha** — tres tarjetas apiladas, cada una con ícono y texto:
1. Ícono de alerta/triángulo amarillo — **Alucinaciones**: Inventa hechos con tono seguro. Costo estimado: US$1.2M/año por desinformación en empresas que despliegan GenAI.
2. Ícono de base de datos — **Obsolescencia**: El modelo "congela" el conocimiento en su fecha de corte; no conoce tu política interna ni el dato de ayer.
3. Ícono de ojo — **Sin trazabilidad**: Sin citar la fuente, nadie puede auditar la respuesta. En banca, salud o seguros eso es inaceptable.

Pie de fuente: "Fuente: C. Huyen, 'AI Engineering', O'Reilly (2025); Gartner, informe 2025 sobre precisión en GenAI empresarial; NIST AI RMF 1.0."

## Slide 7

Título: "RAG en una frase: recuperar, luego generar"

Subtítulo: "La IA no adivina desde su memoria: primero busca en TUS fuentes confiables, y solo entonces responde citando de dónde salió."

Diagrama de flujo horizontal de 3 pasos conectados por flechas (→):

1. **1 · Recuperar** (ícono de lupa sobre círculo azul oscuro) → "El sistema busca en bases vectoriales y documentos internos los fragmentos más relevantes a la pregunta."
2. → (flecha verde) **2 · Aumentar** (ícono de eslabones de cadena) → "Esos fragmentos se inyectan en el prompt, dándole al modelo el contexto exacto y verificado."
3. → (flecha verde) **3 · Generar** (ícono de cerebro) → "El LLM redacta la respuesta anclada en la fuente, y puede citar el documento de origen."

Recuadro inferior destacado: "Idea clave: RAG desacopla el razonamiento (LLM) del conocimiento (tus datos). Actualizas el índice, no reentrenas el modelo."

Fuente: "Digital Government Authority (2026), 'RAG & Enterprise Innovation'; K. Bourne, 'Unlocking Data with Generative AI and RAG' (Packt/O'Reilly)."

## Slide 8

Título: "Comprar, potenciar o construir: dónde encaja RAG"

Tabla comparativa en 3 columnas (recuadros lado a lado):

| COMPRAR | POTENCIAR con RAG | CONSTRUIR / FINE-TUNING |
|---|---|---|
| Usar el modelo tal cual (ChatGPT, Claude, Gemini) | Anclar el modelo en tus datos vía recuperación | Reentrenar el modelo con tus datos |
| • Rápido y barato para arrancar | • Dato interno, en tiempo real | • Caro y lento de mantener |
| • No conoce tu dato privado | • Cita fuentes: auditable | • Reentrenar por cada cambio |
| • Sin trazabilidad ni control | • Actualizas índice, no el modelo | • Requiere capacidad avanzada |
| | • Menor costo que reentrenar | |

Fuente: "Van der Meulen & Wixom, 'Managing the Two Faces of Generative AI', MIT CISR (2024); Squirro, 'State of RAG & GenAI' (2026)."

## Slide 9

Título: "Las cifras: por qué el mercado va hacia RAG"

Fila de 4 tarjetas con cifra grande + descripción:
- **6x** — Salto de inversión empresarial en GenAI: de US$2.3B (2023) a US$13.8B (2024)
- **38.4%** (en verde azulado) — CAGR del mercado RAG: de US$1.94B (2025) a US$9.86B proyectado a 2030
- **3.7x** (en verde) — ROI reportado por clientes de Microsoft: US$3.70 por cada US$1 en GenAI con recuperación
- **70-90%** — Reducción de alucinaciones al introducir RAG en flujos críticos (benchmarks 2025)

Debajo, subtítulo: "Casos de uso donde RAG ya domina", con gráfico de barras horizontales (barras celestes) mostrando % de adopción:
- Cumplimiento / legal: 58%
- Gestión del conocimiento: 65%
- Documentación técnica: 73%
- Soporte al cliente: 89%

A la derecha del gráfico, recuadro con ícono de tendencia ascendente: "340% de ROI promedio en 18 meses y 65% menos tiempo buscando información interna."

Fuente: "MarketsandMarkets, 'RAG Market 2025-2030'; Microsoft, '3.7x ROI on Generative AI'; Makebot 'Enterprise RAG Benchmarks 2025'; hoja de ruta GenAI/RAG 2024-2027 (McKinsey/Gartner)."

## Slide 10

Categoría (kicker): "CONEXIÓN CON IA RESPONSABLE"

Título: "RAG es una palanca de gobierno, no solo de precisión"

Subtítulo: "Enlaza con lo visto en las sesiones previas: los mismos atributos de IA responsable se ejecutan en la capa de recuperación."

Fila de 4 tarjetas con ícono circular + título + descripción:
1. Ícono de ojo — **Transparencia**: La respuesta cita el documento fuente: el usuario puede verificar. Aumenta la confianza.
2. Ícono de escudo — **Privacidad y acceso**: El control de acceso se aplica en la recuperación (no solo en la interfaz): la IA solo lee lo permitido.
3. Ícono de base de datos — **Datos vigentes**: Se actualiza el índice, no el modelo: sin reentrenamientos costosos para incorporar el dato de hoy.
4. Ícono de check verde — **Humano en el loop**: Factor #1 de éxito en high performers: el juicio humano valida las salidas críticas antes de actuar.

Recuadro inferior: "Pregunta: ¿Nuestra política de datos protege la propiedad intelectual y define quién accede a qué antes de encender el RAG?"

Fuente: "Squirro, 'RAG in 2026'; NIST AI RMF 1.0; EU AI Act; ISO/IEC 42001:2023; hoja de ruta GenAI/RAG 2024-2027."

## Slide 11

Categoría (kicker): "LA TRAMPA QUE VE EL LÍDER"

Título: "El cuello de botella no es el modelo: es la calidad del dato"

Layout de tres bloques superiores:

**Izquierda** — recuadro con cita (ícono de comillas):
> "Los asistentes y agentes basados en RAG rinden por debajo de lo esperado al escalar, sobre todo por problemas de calidad de la fuente y de relevancia en la recuperación."
> — Gartner — Market Guide for Enterprise AI Search (sep 2025)

**Centro** — recuadro **ROT** (texto en rojo/salmón): "Redundante / Obsoleto / Trivial" — "Contamina el contexto → el agente responde mal"

**Derecha** — recuadro **APT** (texto en verde): "Preciso (Accurate) / Pertinente / Confiable (Trusted)" — "El estándar que el líder debe exigir a su dato"

Recuadro inferior con ícono de alerta amarilla: "Fuga de productividad ('Productivity Leak'): entre 20% y 30% del tiempo que ahorra la IA se pierde en tareas no productivas si el líder no lo reinvierte activamente en trabajo de alto valor. La productividad no se captura sola: se gestiona."

Fuente: "Gartner, 'Market Guide for Enterprise AI Search' (2025), conceptos ROT/APT; hoja de ruta GenAI/RAG 2024-2027 (riesgo 'Productivity Leak')."

## Slide 12

Título: "Las grandes plataformas ya integraron RAG"

Cuadrícula de 6 tarjetas (2 filas x 3 columnas), cada una con viñeta azul + nombre de plataforma + descripción:

1. **AWS** — Amazon Bedrock Knowledge Bases: recuperación gestionada sobre bases vectoriales, integrada al stack cloud.
2. **Microsoft** — Azure AI Foundry y Copilot anclan respuestas en datos de la empresa; reportan 3.7x de retorno con recuperación.
3. **OpenAI / ChatGPT** — File search y conectores empresariales: el modelo responde citando documentos cargados por la organización.
4. **Anthropic / Claude** — Recuperación sobre documentos y conectores con controles de acceso; foco en trazabilidad y seguridad.
5. **Google** — Gemini + Vertex AI Search: búsqueda empresarial y grounding sobre fuentes propias y públicas.
6. **SAP · Salesforce · IBM** — RAG embebido en S/4HANA, Service Cloud y watsonx: la recuperación entra al software de gestión.

Fuente: "Documentación de producto (AWS Bedrock, Microsoft Azure AI Foundry, OpenAI, Anthropic, Google Vertex AI); Mordor Intelligence, 'RAG Market' (2025)."

## Slide 13

Categoría (kicker): "DECISIÓN DE LIDERAZGO"

Título: "Mini-caso: '¿Escalar, rediseñar o cerrar?'"

Recuadro superior "Contexto": "Un banco peruano lanzó un asistente RAG para su mesa de ayuda. En el piloto redujo 40% el tiempo de respuesta, pero al escalar a 100.000 consultas/mes empezó a citar políticas derogadas y a mezclar productos de otra línea. El equipo pide más presupuesto de GPU."

Tres tarjetas inferiores (diagnóstico del líder):
1. Ícono de alerta amarilla — **No es un problema de GPU**: Más cómputo no arregla dato sucio. El síntoma (citas erróneas) apunta a ROT en el índice, no al modelo.
2. Ícono de base de datos — **Es la capa de conocimiento**: Falta gobierno del índice: versionado de políticas, clasificación por línea de producto, retiro de lo obsoleto.
3. Ícono de check verde — **La decisión correcta**: Rediseñar la recuperación y el gobierno del dato antes de escalar. Humano-en-el-loop para respuestas críticas.

Fuente: "E. Sojo, 'Microsoft Foundry in Action' (escenario >100K consultas/mes); Gartner (ROT/APT); K. Bourne, 'Unlocking Data with GenAI and RAG'."

## Slide 14

Categoría (kicker): "HERRAMIENTA PRÁCTICA"

Título: "Checklist del líder antes de escalar un RAG"

Lista de 6 ítems, cada uno en su propio recuadro con ícono de check verde:
1. ¿Tenemos humano-en-el-loop para validar las salidas críticas? (factor #1 en high performers)
2. ¿La política de datos protege la propiedad intelectual frente a modelos públicos?
3. ¿El control de acceso se aplica en la recuperación, no solo en la interfaz?
4. ¿El índice está gobernado: versionado, clasificado y libre de contenido ROT?
5. ¿Tenemos un plan para reinvertir el tiempo ahorrado y evitar la fuga de productividad?
6. ¿Medimos ROI y calidad de recuperación con un criterio de corte, no con entusiasmo?

Fuente: "Hoja de ruta GenAI/RAG 2024-2027 (checklist C-Suite); NIST AI RMF; Gartner Enterprise AI Search (2025)."

## Slide 15

Slide de cita/cierre de sección, sin numeración de fuente.

Cita grande (en azul): "'La pregunta no es '¿podemos hacerlo con IA?', sino '¿podemos operarlo con confianza y escalarlo?''"

Debajo, línea separadora y texto: "El líder de SI como sponsor, filtro y escudo: garantiza que la IA responda desde el dato correcto, con la persona correcta validando."

## Slide 16

Slide separador de sección (decorativo: numeral grande "3.", imágenes arquitectónicas en hexágonos a la derecha).

Texto: "Conclusiones."

## Slide 17

Título: "CONCLUSIONES"

Lista numerada:
1. RAG es una decisión de liderazgo. No es solo arquitectura: define qué dato se confía, quién accede y cómo se audita la IA.
2. Potenciar suele ganarle a construir: RAG ancla el modelo en tu dato sin el costo de reentrenar; actualizas el índice, no el LLM.
3. El gobierno del dato es el diferenciador, el cuello de botella es la capa de conocimiento (ROT vs APT), no el tamaño del modelo.
4. El valor se gestiona, no se captura solo: ROI real exige humano-en-el-loop, criterios de corte y evitar la fuga de productividad.

## Slide 18

Slide de cierre minimalista (fondo blanco, patrón hexagonal decorativo tenue).

Texto: "Dudas?"

## Slide 19

Slide de cierre minimalista (fondo blanco, patrón hexagonal decorativo tenue).

Texto: "GRACIAS."
