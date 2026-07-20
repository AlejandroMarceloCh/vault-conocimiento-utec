---
curso: LIDSI
titulo: 18 - Semana 16/Sem16_Sesion26
slides: 19
fuente: 18 - Semana 16/Sem16_Sesion26.pdf
---

LIDERAZGO EN
SISTEMAS DE
INFORMACIÓN.

 2026-1


Sesión 26:
Liderar IA confiable:
RAG - Generación Aumentada por
Recuperación como decisión de
liderazgo.
                           Índice

1. Objetivos
2. RAG: Generación Aumentada por Recuperación como decisión de liderazgo, no solo de arquitectura.
3. Conclusiones
1.

Objetivos
                                   Objetivos

Al finalizar la sesión el estudiante será capaz de:
1. Explicar RAG en lenguaje de negocio: Qué es el flujo recuperar-luego-generar y por
   qué corrige alucinación y obsolescencia del LLM.
2. Distinguir RAG de fine-tuning y de "comprar el modelo“: tomar la decisión comprar,
   potenciar o construir desde el rol de líder de SI.
3. Conectar RAG con IA responsable y ética del dato: trazabilidad, control de acceso
   en la recuperación y humano-en-el-loop.
4. Evaluar el caso de negocio con cifras: ROI, reducción de alucinaciones y el riesgo de
   "fuga de productividad".
5. Decidir como líder: escalar, rediseñar o cerrar: el cuello de botella es la capa de
   conocimiento, no el modelo.
2.
RAG: Generación Aumentada por
Recuperación como decisión de
liderazgo, no solo de
arquitectura.
EL PROBLEMA DE LIDERAZGO


El LLM solo, sin tus datos, es un riesgo de negocio

                                                                                                            Alucinaciones
                                                                                                            Inventa hechos con tono seguro. Costo estimado:
                                                                                                            US$1.2M/año por desinformación en empresas que
                                                                                                            despliegan GenAI.
  “Para resolver una tarea, un modelo
  necesita las instrucciones y también la
  información. Igual que una persona, la IA                                                                 Obsolescencia
  falla y alucina cuando le falta contexto.”                                                                El modelo "congela" el conocimiento en su fecha de corte; no
                                                                                                            conoce tu política interna ni el dato de ayer.




                                                                                                            Sin trazabilidad
  Chip Huyen — AI Engineering (O'Reilly, 2025)                                                              Sin citar la fuente, nadie puede auditar la respuesta. En
                                                                                                            banca, salud o seguros eso es inaceptable.




                         Fuente: C. Huyen, 'AI Engineering', O'Reilly (2025); Gartner, informe 2025 sobre precisión en GenAI empresarial; NIST AI RMF 1.0.                 3
RAG en una frase: recuperar, luego generar
La IA no adivina desde su memoria: primero busca en TUS fuentes confiables, y solo entonces responde citando de dónde
salió.




           1 · Recuperar                               →                       2 · Aumentar                                    →                         3 · Generar

  El sistema busca en bases vectoriales
                                                                    Esos fragmentos se inyectan en el                                      El LLM redacta la respuesta anclada
         y documentos internos los
                                                                      prompt, dándole al modelo el                                             en la fuente, y puede citar el
      fragmentos más relevantes a la
                                                                      contexto exacto y verificado.                                               documento de origen.
                pregunta.




  Idea clave : RAG desacopla el razonamiento (LLM) del conocimiento (tus datos). Actualizas el índice, no reentrenas el modelo.



                 Fuente: Digital Government Authority (2026), 'RAG & Enterprise Innovation'; K. Bourne, 'Unlocking Data with Generative AI and RAG' (Packt/O'Reilly).            4
Comprar, potenciar o construir: dónde encaja RAG


             COMPRAR                                               POTENCIAR con RAG                                             CONSTRUIR / FINE-TUNING

       Usar el modelo tal cual                                     Anclar el modelo en tus                                               Reentrenar el modelo con
     (ChatGPT, Claude, Gemini)                                     datos vía recuperación                                                       tus datos

 •     Rápido y barato para arrancar                           •     Dato interno, en tiempo real                                    •     Caro y lento de mantener
 •     No conoce tu dato privado                               •     Cita fuentes: auditable                                         •     Reentrenar por cada cambio
 •     Sin trazabilidad ni control                             •     Actualizas índice, no el modelo                                 •     Requiere capacidad avanzada
                                                               •     Menor costo que reentrenar




                      Fuente: Van der Meulen & Wixom, 'Managing the Two Faces of Generative AI', MIT CISR (2024); Squirro, 'State of RAG & GenAI' (2026).                5
Las cifras: por qué el mercado va hacia RAG



                6x                                          38.4%                                                   3.7x                                       70-90%
   Salto de inversión empresarial                      CAGR del mercado RAG: de                          ROI reportado por clientes de                      Reducción de alucinaciones al
   en GenAI: de US$2.3B (2023) a                       US$1.94B (2025) a US$9.86B                         Microsoft: US$3.70 por cada                      introducir RAG en flujos críticos
          US$13.8B (2024)                                  proyectado a 2030                                  US$1 en GenAI con                                  (benchmarks 2025)
                                                                                                                recuperación




Casos de uso donde RAG ya domina

    Cumplimiento / legal                                                                 58%
                                                                                                                                               340% de ROI promedio en
Gestión del conocimiento                                                                        65%                                            18 meses y 65% menos
 Documentación técnica                                                                                  73%
                                                                                                                                               tiempo buscando
                                                                                                                                               información interna.
       Soporte al cliente                                                                                                89%




   Fuente: MarketsandMarkets, 'RAG Market 2025-2030'; Microsoft, '3.7x ROI on Generative AI'; Makebot 'Enterprise RAG Benchmarks 2025'; hoja de ruta GenAI/RAG 2024-2027 (McKinsey/Gartner).   6
CONEXIÓN CON IA RESPONSABLE


RAG es una palanca de gobierno, no solo de precisión
Enlaza con lo visto en las sesiones previas: los mismos atributos de IA responsable se ejecutan en la capa de recuperación.




        Transparencia                           Privacidad y acceso                                      Datos vigentes                                Humano en el loop
  La respuesta cita el documento             El control de acceso se aplica                        Se actualiza el índice, no el                       Factor #1 de éxito en high
      fuente: el usuario puede               en la recuperación (no solo en                       modelo: sin reentrenamientos                        performers: el juicio humano
  verificar. Aumenta la confianza.            la interfaz): la IA solo lee lo                      costosos para incorporar el                       valida las salidas críticas antes
                                                       permitido.                                         dato de hoy.                                          de actuar.




Pregunta : ¿Nuestra política de datos protege la propiedad intelectual y define quién accede a qué antes de encender el RAG?




                                 Fuente: Squirro, 'RAG in 2026'; NIST AI RMF 1.0; EU AI Act; ISO/IEC 42001:2023; hoja de ruta GenAI/RAG 2024-2027.                                       7
LA TRAMPA QUE VE EL LÍDER


El cuello de botella no es el modelo: es la calidad del
dato
                                                                                                                    ROT                                              APT
  Los asistentes y agentes basados en RAG rinden por                                                            Redundante                                   Preciso (Accurate)
  debajo de lo esperado al escalar, sobre todo por                                                               Obsoleto                                       Pertinente
  problemas de calidad de la fuente y de relevancia en la                                                         Trivial                                    Confiable (Trusted)
  recuperación.
                                                                                                      Contamina el contexto → el agente               El estándar que el líder debe exigir a
                                                                                                              responde mal                                          su dato
  Gartner — Market Guide for Enterprise AI Search (sep 2025)




               Fuga de productividad (“Productivity Leak”): entre 20% y 30% del tiempo que ahorra la IA se pierde en tareas no
               productivas si el líder no lo reinvierte activamente en trabajo de alto valor. La productividad no se captura sola: se
               gestiona.




                    Fuente: Gartner, 'Market Guide for Enterprise AI Search' (2025), conceptos ROT/APT; hoja de ruta GenAI/RAG 2024-2027 (riesgo 'Productivity Leak').                         8
Las grandes plataformas ya integraron RAG

   AWS                                                             Microsoft                                                            OpenAI / ChatGPT
 Amazon Bedrock Knowledge Bases:                               Azure AI Foundry y Copilot anclan                                   File search y conectores
 recuperación gestionada sobre                                 respuestas en datos de la empresa;                                  empresariales: el modelo responde
 bases vectoriales, integrada al stack                         reportan 3.7x de retorno con                                        citando documentos cargados por
 cloud.                                                        recuperación.                                                       la organización.



   Anthropic / Claude                                              Google                                                               SAP · Salesforce · IBM
 Recuperación sobre documentos y                               Gemini + Vertex AI Search:                                          RAG embebido en S/4HANA, Service
 conectores con controles de acceso;                           búsqueda empresarial y grounding                                    Cloud y watsonx: la recuperación
 foco en trazabilidad y seguridad.                             sobre fuentes propias y públicas.                                   entra al software de gestión.




           Fuente: Documentación de producto (AWS Bedrock, Microsoft Azure AI Foundry, OpenAI, Anthropic, Google Vertex AI); Mordor Intelligence, 'RAG Market' (2025).   9
DECISIÓN DE LIDERAZGO



Mini-caso: “¿Escalar, rediseñar o cerrar?”

   Contexto. Un banco peruano lanzó un asistente RAG para su mesa de ayuda. En el piloto redujo 40%
   el tiempo de respuesta, pero al escalar a 100.000 consultas/mes empezó a citar políticas derogadas y
   a mezclar productos de otra línea. El equipo pide más presupuesto de GPU.


El diagnóstico como líder de SI (no como ingeniero):


         No es un problema                                                Es la capa de
                                                                                                                                                La decisión correcta
         de GPU                                                           conocimiento
                                                                                                                                      Rediseñar la recuperación y el
   Más cómputo no arregla dato                                  Falta gobierno del índice:                                            gobierno del dato antes de escalar.
   sucio. El síntoma (citas erróneas)                           versionado de políticas,
                                                                                                                                      Humano-en-el-loop para
   apunta a ROT en el índice, no al                             clasificación por línea de producto,                                  respuestas críticas.
   modelo.                                                      retiro de lo obsoleto.




                 Fuente: E. Sojo, 'Microsoft Foundry in Action' (escenario >100K consultas/mes); Gartner (ROT/APT); K. Bourne, 'Unlocking Data with GenAI and RAG'.         10
HERRAMIENTA PRÁCTICA


Checklist del líder antes de escalar un RAG

     ¿Tenemos humano-en-el-loop para validar las salidas críticas? (factor #1 en high performers)



     ¿La política de datos protege la propiedad intelectual frente a modelos públicos?



     ¿El control de acceso se aplica en la recuperación, no solo en la interfaz?



     ¿El índice está gobernado: versionado, clasificado y libre de contenido ROT?



     ¿Tenemos un plan para reinvertir el tiempo ahorrado y evitar la fuga de productividad?



     ¿Medimos ROI y calidad de recuperación con un criterio de corte, no con entusiasmo?



                          Fuente: Hoja de ruta GenAI/RAG 2024-2027 (checklist C-Suite); NIST AI RMF; Gartner Enterprise AI Search (2025).
“La pregunta no es ‘¿podemos hacerlo con IA?’, sino
‘¿podemos operarlo con confianza y escalarlo?’”


El líder de SI como sponsor, filtro y escudo: garantiza que la IA responda desde el dato correcto,
con la persona correcta validando.
3.

Conclusiones.
                           CONCLUSIONES

1. RAG es una decisión de liderazgo No es solo arquitectura: define qué dato
  se confía, quién accede y cómo se audita la IA.
2. Potenciar suele ganarle a construir: RAG ancla el modelo en tu dato sin el
  costo de reentrenar; actualizas el índice, no el LLM.
3. El gobierno del dato es el diferenciador, el cuello de botella es la capa de
  conocimiento (ROT vs APT), no el tamaño del modelo.
4. El valor se gestiona, no se captura solo: ROI real exige humano-en-el-loop,
  criterios de corte y evitar la fuga de productividad.
Dudas?
GRACIAS.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
