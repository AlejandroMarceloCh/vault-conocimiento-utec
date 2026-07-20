---
curso: LIDSI
titulo: 15 - Semana 13/Sem13_Sesion23
slides: 25
fuente: 15 - Semana 13/Sem13_Sesion23.pdf
---

LIDERAZGO EN
SISTEMAS DE
INFORMACIÓN.

2026-1

Sesión 23 :
Liderar en entornos impulsados por
inteligencia artificial, datos y
tecnologías en la nube, considerando
principios de IA responsable, ética del
uso de datos y el rol de las plataformas
digitales.
                     Índice

1. Objetivos
2. Saberes previos
3. Casos
4. Conclusiones
1.

Objetivos
                                         Objetivos

Sesión de cierre. Al finalizar, el estudiante será capaz de:
•   Repasar   los   conceptos    clave   de   IA   responsable:   atributos,   pilares   y   la   decisión
    comprar/potenciar/construir.
•   Contrastar dos casos reales: Fuel iX (gobernanza como producto) y Anthropic (autonomía vs.
    poder).
•   Aplicar todo lo aprendido diseñando una solución de IA gobernada para un caso de salud
    (MediClínica Perú).
2.
Saberes previos
IA RESPONSABLE


Cinco atributos de diseño IA que los consumidores valoran



  Auditabilidad                  Privacidad                     Entendibilidad                       Autonomía                      Personalización
  Trazar y revisar            Proteger datos y                   Claridad sobre el              Grado en que decide               Adaptar funciones al
   decisiones del           confidencialidad del                  porqué de los                   sin intervención                 usuario individual
    sistema, con                  usuario                           resultados                         humana
supervisión humana

      26%                             31%                               11%                               23%                               9%



  El % es la importancia que pesa en la decisión de compra (app de pensiones). Privacidad + auditabilidad (atributos
  responsables) dominan → introducir atributos responsables subió la adopción del 2.4% al 63.2%.




           Fuente: Acar, Wiertz & Ghosh, 'How Responsible AI Protects the Bottom Line', HBR (mar 2025), 3 estudios, n=3,268 consumidores.                8
IA RESPONSABLE


Del principio a la práctica: 4 pilares operativos y el rol del líder


                                                                                            Rol del líder: Exigir auditorías de sesgo;
                                      Problema: Los algoritmos aprenden de
         Equidad y sesgo              datos históricos sesgados.
                                                                                            priorizar equidad aunque baje algo la
                                                                                            precisión.


                                                                                            Rol del líder: No aceptar 'el algoritmo lo
                                      Problema: Modelos 'caja negra' deciden
         Transparencia / XAI          sin explicación clara.
                                                                                            decidió'. Exigir explicabilidad en dominios
                                                                                            de alto riesgo.



                                      Problema: Sistemas que requieren datos                Rol del líder: Privacy by design; privacidad
         Privacidad y seguridad       personales sensibles.                                 diferencial / aprendizaje federado.



                                                                                            Rol del líder: Comités de ética; human-in-
                                      Problema: ¿Quién responde cuando la IA
         Rendición de cuentas         falla?
                                                                                            the-loop; el líder asume la responsabilidad
                                                                                            final.




                               Fuente: Blackman, HBR (2023); O'Neil, 'Weapons of Math Destruction'.                                        9
DE PRINCIPIOS A OPERACIÓN



Antes de pilotear IA: clasificar riesgo y definir guardrails
Una política útil debe decir qué sí, qué requiere aprobación, qué nunca se permite y cómo pedir excepción.

                                                                                                                2 Aplicar guardrails mínimos
1 Clasificar el caso de uso

                                                                                                                  Siempre permitido                             Con aprobación
  Impacto del
  error /                                                Autonomía                                                Información pública,                          Datos internos no públicos,
                            Baja autonomía                                       Alta autonomía
  Autonomía del                                            media                                                  borradores internos sin                       análisis de clientes, código
                                                                                                                  datos sensibles, aprendizaje                  propietario o
  sistema                                                                                                         guiado.                                       automatización con impacto
                                                                                                                                                                operativo.
                                                          Supervisar
  Bajo impacto              Usar como apoyo                                     Control humano
                                                          muestras

                                                         Aprobación
  Impacto medio             Validar outputs                                     Auditoría + legal
                                                          humana
                                                                                                                                        Nunca permitido
                                                        No escalar sin               Comité +
  Alto impacto              Piloto controlado
                                                            RMF                      rediseño                                           PII sin autorización, secretos
                                                                                                                                        comerciales, credenciales,
                                                                                                                                        salud/legal o decisiones
                                                                                                                                        críticas sin humano.

                                                                                                                                       *PII: Personally Identifiable
                                                                                                                                       Information./información personal
                                                                                                                                       identificable. PII es cualquier dato que
                                                                                                                                       permite identificar directa o
                                                                                                                                       indirectamente a una persona.


                            Fuentes: NIST AI RMF 1.0; EU AI Act risk-based approach; ISO/IEC 42001:2023; MIT CISR, GenAI governance/guardrails (2024–2026).
DECISIÓN DE PLATAFORMA


Comprar, potenciar o construir IA : la decisión que define el valor
capturado

         COMPRAR (Buy)                                 POTENCIAR (Boost)                                    CONSTRUIR (Build)

  Qué es                                        Qué es                                              Qué es
  El proveedor corre el modelo.                 Mejoras un modelo con datos                         Asumes desarrollo y operación
  Adopción rápida, pago por uso.                propios (fine-tuning, RAG).                         completos del modelo.


  Trade-off                                     Trade-off                                           Trade-off
  Opaco y de contexto estrecho.                 Más contexto, pero sube el costo                    Caro al inicio; requiere
                                                por uso.                                            capacidades avanzadas de datos.

  Cuándo                                        Cuándo                                              Cuándo
  Cuando necesitas velocidad y                  Cuando hay necesidad fuerte de                      Cuando buscas un diferenciador
  paridad competitiva.                          contextualización.                                  difícil de imitar.




                    Fuente: Van der Meulen & Wixom, 'Managing the Two Faces of Generative AI', MIT CISR (sep 2024).                   14
3.
Casos
Caso 2 — TELUS: la gobernanza como producto


  1      Contexto: la empresa                           2       Producto: Fuel iX
                                                                                                                    https://www.telusdigital.com/solutions/fuel-ix

 TELUS Digital (Canadá): telecom y                     Plataforma de gobierno de IA. Uso
 servicios digitales. Detectó que 54% de               doble: la usan internamente y la
 empleados usaba IA pública y 57%                      licencian a otras empresas (B2B).                        ¿FUE RENTABLE? → A PLAZO
 subía datos sensibles.                                Convierte el shadow-AI en capacidad
                                                       gobernada.                                               −42%
                                                                                                                EBITDA ajustado de TELUS Digital
                                                                                                                cayó en Q4 2024, en parte por
                                                                                                                invertir en lanzar Fuel iX.
  3     La IA en acción                                4       IA responsable real
                                                                                                                A corto plazo es COSTO; la apuesta es
                                                                                                                monetizar la gobernanza como
 Gateway multi-modelo: el empleado                    Privacidad certificada: 1ª certificación                  producto y diferenciarse. No vende
 elige entre 40+ modelos (Claude es                   Privacy by Design (ISO 31700-1) para                      'acceso a Claude': vende CONTROL,
 uno) según la tarea, con guardrails                  su chatbot de soporte. Trazabilidad +                     cumplimiento y confianza.
 centralizados, RBAC y monitoreo                      control = atributos responsables
 continuo (Fortify).                                  aplicados.




 Concepto aplicado: lo opuesto a Air Canada. El valor (y el precio) no está en el modelo, sino en las capas de
 gobernanza que lo rodean: guardrails, privacidad, auditabilidad y supervisión.
                       Fuente: TELUS Digital (estudio BYO-AI); TELUS Corp. Form 6-K Q4 2024 (SEC); certificación ISO 31700-1.
   Caso 2 — TELUS: la gobernanza como producto
   Fuel iX — cómo viaja una consulta

                         Control de acceso (RBAC)
                    1    Quién accede a qué modelo y dato
                                                                                                 MONITOREO TRANSVERSAL

                         Gateway multi-modelo                                                    Fortify corre en paralelo a todo el flujo, no en la ruta de
                    2    Elige entre 40+ modelos según la tarea
                                                                                                 la consulta:
                         Orquestación / RAGRAG = Retrieval-Augmented
                    3    Generation (Generación Aumentada por Recuperación).
                                                                                                 • Validación continua de guardrails
                         Recupera datos internos de la empresa                                   • Red-teaming (pruebas adversarias)
                                                                                                 • Auditoría y trazabilidad de prompts, modelos e
                         Generación                                                              integraciones
                    4    El modelo elegido produce el borrador
                                                                                                 • Dashboard central de visibilidad
Bloqueo
                         Guardrails (control central)
   o
escala a
                    5    Filtran alucinación y datos sensibles
humano


                                  Respuesta al empleado



           El modelo (paso 4) está rodeado de gobernanza, nunca expuesto directo. Acceso → procesamiento → comportamiento →
           supervisión.


                                    Fuente: arquitectura Fuel iX de TELUS Digital (gateway multi-modelo, guardrails centralizados, Fortify).
                                                                                                                                                               12
Caso 2 — TELUS: la gobernanza como producto
Cómo implementar IA gobernada (no shadow AI)

  1     Auditar el uso actual                                            2     Centralizar el acceso

 Descubrir qué herramientas de IA usan ya los                          Un gateway único como puerta de entrada. Las
 empleados — incluido el shadow AI invisible.                          claves de API nunca tocan la máquina del
                                                                       empleado.


  3     Definir políticas                                                4     Humano en el bucle

 RBAC (quién accede a qué) + guardrails (qué puede                     Para decisiones importantes, la IA propone y el
 decir la IA) + clasificación de datos sensibles.                      humano aprueba. Nunca automatizar lo crítico sin
                                                                       revisión.

       Monitorear y medir Auditar el uso, medir costo y calidad de forma continua. La gobernanza es un
 5
       proceso, no un setup único.



  No prohibir la IA, gobernarla. Prohibir empuja al uso a escondidas. El valor está en las capas de control, no en el modelo.


                                                                                                                                13
Caso 3 — Anthropic: salvaguarda vs. poder
            Anthropic vs EE.UU : control de IA
Caso 3 — Anthropic: salvaguarda vs. poder
                                                                                        CONCEPTOS DE IA RESPONSABLE APLICADOS
  QUÉ PASÓ
                                                                                                 Autonomía el grado en que la IA decide sin intervención
  Jun 2026: EE.UU. ordena a Anthropic cortar el acceso de                                        humana llega al extremo: un sistema que se mejora a sí
  nacionales extranjeros a sus modelos más avanzados                                             mismo.
  (Fable 5 / Mythos 5) por riesgos de ciberseguridad.
  Anthropic desactiva ambos modelos para todos.
                                                                                                 Rendición de cuentas ¿quién responde si actúa solo? El
                                                                                                 human-in-the-loop deja de ser obvio.
  Freno propuesto:
  Anthropic ya proponía la idea de poder pausar
  voluntariamente la creación de modelos más potentes,
  para dar tiempo a que la investigación en seguridad                                            Auditabilidad trazar y revisar decisiones se vuelve más
                                                                                                 difícil cuando el modelo escribe su propio código.
  alcance el nivel de lo que esos modelos ya pueden hacer.

  Detonante:
  auto-mejora recursiva — agentes que mejoran sin                                                Gobernanza y poder ¿quién pone el freno: la empresa, el
                                                                                                 Estado o nadie? El control deja de ser solo técnico.
  intervención humana (~80% del código nuevo lo escribe
  su propio modelo).


  Pregunta de liderazgo: ¿dónde termina la responsabilidad del líder de una plataforma? ¿Sólo de lo que su empresa hace, o
  también de lo que terceros hacen —y de lo que el sistema podría hacer solo? Mismo dilema que Cambridge Analytica,
  pero ahora el sistema puede actuar sin un humano.


   Fuente: NYT, 'Trump Administration Reignites Its Feud With Anthropic' (jun 2026); 'Anthropic's Call for A.I. Nonproliferation' (jun 2026); anthropic.com/policy.   11
Caso 3 — Anthropic: salvaguarda vs. poder

El precedente: Cambridge Analytica → Anthropic
 Cambridge Analytica · 2018                                                         Anthropic · 2026

 Qué pasó: una app de test de personalidad en                                       Qué cambia: el daño ya no requiere ni siquiera un
 Facebook recogió datos no solo de quien la usaba,                                  tercero malicioso. La IA de frontera puede
 sino de todos sus amigos. 87 millones de perfiles                                  mejorarse y actuar sola, sin un humano que decida
 terminaron en manos de una consultora política,                                    en ese momento.
 sin consentimiento.
                                                                                    El paralelo: si Facebook respondió por lo que
 La defensa de Facebook: "no fuimos nosotros, fue                                   terceros hicieron con su plataforma, ¿quién
 un tercero que abusó de la plataforma".                                            responde por lo que el sistema hace por sí mismo?

 El desenlace: no le funcionó. Multa récord de                                      La respuesta emergente: la autonomía no diluye la
 US$5,000 millones (FTC). Respondió por permitir el                                 responsabilidad del líder — la concentra en quien
 acceso de terceros, no por robar los datos.                                        decide desplegar sin freno.



  Conceptos aplicados: Privacidad (datos sin consentimiento) · Rendición de cuentas (no vale "fue un tercero") · Autonomía (el
  sistema actúa solo) · Gobernanza (diseñar el freno antes del daño)



               Fuente: FTC, 'Imposes $5 Billion Penalty on Facebook' (2019); 87 millones de usuarios afectados (Cambridge Analytica, 2018).
                           Actividad: MediClínica Perú

Diseñen una solución de IA gobernada
Una cadena de clínicas quiere lanzar un asistente de IA para que pacientes consulten síntomas y agenden
citas. Maneja datos de salud (PII sensible, Ley 29733), presión por reducir el call center y un directorio que
pregunta: ¿comprar, potenciar o construir?


En el tablero de Miro, completen las 4 zonas:
1. Clasificar el riesgo (impacto del error × autonomía).
2. ¿Cuáles de los 5 atributos responsables son críticos aquí y por qué?
3. Comprar, potenciar o construir: elijan y justifiquen el trade-off.
4. Diseñen el guardrail: ¿qué nunca se permite y qué requiere aprobación humana?
Actividad: MediClínica Perú




        https://miro.com/app/board/uXjVHJ5VMVE=/
                               Actividad: MediClínica Perú
1. Clasificar el riesgo (impacto del error × autonomía).
El caso debe clasificarse como ALTO IMPACTO / alto riesgo, porque involucra salud y datos personales sensibles. Un error
del asistente podría afectar la atención de un paciente, generar una mala orientación médica o exponer información
protegida por la Ley 29733 — LPDP Perú.
En la matriz, debe ubicarse como:
Impacto del error: ALTO
Autonomía del sistema: BAJA
Uso permitido: apoyo/piloto controlado, no decisión autónoma


        Impacto del                                                        Clasificación: alto riesgo / alto impacto.
        error /              Baja         Autonomía        Alta            Razón: maneja datos de salud, PII sensible y
                                                                           puede afectar decisiones de atención.
        Autonomía del     autonomía         media       autonomía
                                                                           Autonomía permitida: baja.
        sistema                                                            Rol de la IA: apoyo y agendamiento, no
                                                                           diagnóstico.
                          Usar como       Supervisar     Control
        Bajo impacto                                                       Control requerido: supervisión humana,
                            apoyo         muestras       humano            trazabilidad, privacidad, auditoría y
                                                                           escalamiento a profesional ante señales de
        Impacto            Validar        Aprobación    Auditoría +        alarma.
        medio              outputs         humana         legal            *No escalar sin Risk Management
                                                                           Framework NIST/Marco de Gestión de
                            Piloto     No escalar sin    Comité +          Riesgos
        Alto impacto
                          controlado       RMF           rediseño
                             Actividad: MediClínica Perú

2. ¿Cuáles de los 5 atributos responsables son críticos aquí y por qué?
Dominan los atributos responsables igual que en el estudio HBR:
• Privacidad datos de salud = categoría especial (Ley 29733). Imprescindible.
• Auditabilidad trazar qué dijo el bot y revisarlo (lección Air Canada).
• Entendibilidad explicar por qué deriva o agenda.
• Autonomía debe ser BAJA; personalización es secundaria aquí.


3. Comprar, potenciar o construir: elijan y justifiquen el trade-off.
No hay respuesta única; de acuerdo a justificación
• Potenciar (RAG) suele ser la mejor: modelo base + datos propios: catálogo de citas, FAQ verificadas → reduce
  alucinación. Es lo que hace Fuel iX.
• Comprar: rápido pero “contexto estrecho y opaco” → riesgoso en salud.
• Construir: caro, solo si fuera el diferenciador central —no lo es para agendar citas.

                              Actividad: MediClínica Perú


4. Diseñen el guardrail: ¿qué nunca se permite y qué requiere aprobación humana?
Nunca permitido:
• Diagnosticar, prescribir o dar dosis.
• Afirmar coberturas/políticas sin verificar fuente —error exacto de Air Canada.
• Exponer PII de otros pacientes.
Requiere humano: derivar urgencias a un profesional; cualquier síntoma de alarma escala a médico de inmediato.
4.

Conclusiones.
                                    CONCLUSIONES

1. El valor no está en el modelo, sino en las capas de gobernanza que lo rodean: guardrails,
  privacidad, auditabilidad y supervisión humana.
2. Fuel iX (TELUS) muestra el camino positivo: no prohibir la IA, gobernarla. La gobernanza puede ser
  un producto y un diferenciador.
3. Anthropic eleva la apuesta: cuando el sistema actúa solo, la autonomía no diluye la responsabilidad
  del líder la concentra en quien decide desplegar.
4. El rol del líder de SI: saber cuándo escalar a legal, seguridad y data governance, y diseñar el freno
  antes del daño, no después.
Dudas?
GRACIAS.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
