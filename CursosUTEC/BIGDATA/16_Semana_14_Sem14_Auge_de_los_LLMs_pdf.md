---
curso: BIGDATA
titulo: 16 - Semana 14/Sem14_Auge de los LLMs
slides: 64
fuente: 16 - Semana 14/Sem14_Auge de los LLMs.pdf
---

El auge de los large language models:
de los fundamentos a la aplicación




 I+D                    www.managementsolutions.com
Diseño y Maquetación
Dpto. Marketing y Comunicación
Management Solutions - España

Fotografías
Archivo fotográfico de Management Solutions
AdobeStock
Midjourney

© Management Solutions 2024
Todos los derechos reservados. Queda prohibida la reproducción, distribución, comunicación pública, transformación, total o parcial, gratuita u onerosa, por cualquier
medio o procedimiento, sin la autorización previa y por escrito de Management Solutions.
La información contenida en esta publicación es únicamente a título informativo. Management Solutions no se hace responsable del uso que de esta información puedan
hacer terceras personas. Nadie puede hacer uso de este material salvo autorización expresa por parte de Management Solutions.
Índice



         Introducción                              4


         Resumen ejecutivo                        10


         LLM: definición, contexto y regulación   14


         Desarrollo y despliegue de los LLM       22


         Marco de validación de los LLM           36

         Caso práctico: validación de un
         chatbot de políticas                     44


         Conclusiones                             50


         Glosario                                 52


         Bibliografía                             56
                                                                           Introducción



                                                                              “ChatGPT es increíblemente limitado, pero lo suficientemente bueno en algunas cosas
                                                                            como para crear una impresión engañosa de grandeza. Es un error confiar en él para algo
                                                                            importante por ahora. Es un anticipo del progreso; nos queda mucho trabajo por hacer en
                                                                                                                                            robustez y veracidad“.
                                                                                                                                                         Sam Altman1




MANAGEMENT SOLUTIONS



  4




El auge de los large language models: de los fundamentos a la aplicación
“La inteligencia artificial es la tecnología más profunda en      En concreto, la GenAI está encontrando aplicaciones4
la que trabaja la humanidad, más profunda que el fuego, la        potencialmente revolucionarias en campos como la educación,
electricidad o cualquier otra cosa que hayamos hecho en el        donde puede personalizar y mejorar el aprendizaje; en el sector
pasado. Llega a la esencia de lo que es la inteligencia, de lo    de la salud puede facilitar diagnósticos más precisos y el
que es la humanidad. Sin duda, algún día será mucho más           desarrollo de tratamientos individualizados; en el sector
capaz que cualquier cosa que hayamos visto antes”2.               financiero puede mejorar el análisis de riesgos y la detección del
                                                                  fraude; en el comercio puede optimizar la cadena de suministro
Esta es la visión de Sundar Pichai, CEO de Google, sobre el       y la experiencia del cliente; en el arte puede abrir nuevas
auge de la inteligencia artificial (IA), que no solo resalta su   posibilidades creativas; y en el ámbito legal puede agilizar la
profundidad y potencial, sino que también sitúa a la IA           revisión de contratos y la predicción de resultados judiciales, por
como un hito en la historia del desarrollo tecnológico y          citar algunos ejemplos.
humano.
                                                                  Dentro de la GenAI, los LLM (como OpenAI ChatGPT, Anthropic
En este contexto, la inteligencia artificial generativa           Claude, Google Gemini, Meta Llama, Mistral o SenseTime
(GenAI) y, dentro de ella, los modelos de lenguaje de gran        SenseNova) representan un avance disruptivo en el
escala (large language models, LLM) emergen como las              procesamiento de lenguaje natural. Estos modelos son capaces
manifestaciones más significativas de esta transformación.        de analizar y generar texto con un nivel de coherencia,
                                                                  relevancia y fluidez antes inalcanzable por otros algoritmos. Su
Es importante destacar que este avance es una                     aplicación abarca desde la asistencia en la escritura y la                       5
consecuencia lógica del proceso de transformación digital,        generación de ideas hasta la traducción automática, la
impulsado por los progresos en almacenamiento,                    generación de informes completos citando artículos y regulación
procesamiento, disponibilidad de datos y nuevas técnicas          relevante, o la creación de interfaces conversacionales (chatbots)5
de modelización, sin los cuales este hito no habría sido          más naturales y efectivas.
posible.
                                                                  La GenAI, incluyendo los LLM, está influyendo en nuestra
GenAI3 se refiere a sistemas de inteligencia artificial           interacción con la tecnología y la información, contribuyendo a
capaces de generar contenido nuevo y original, ya sea             transformar la creación de contenido, la toma de decisiones
texto, imágenes, vídeo, voz, música, modelos en 3D o              basada en datos y la forma en que interactuamos con las
código de programación. Estos sistemas aprenden de                máquinas, aunque aún está en sus primeras etapas6 y su impacto
cantidades masivas de datos existentes y son capaces de           completo está por determinarse. En este sentido, ya se emplea
producir salidas que, en muchos casos, son indistinguibles        en la creación de asistentes virtuales avanzados, en interfaces
de las creadas por humanos. Esta capacidad para generar           para voz y gestos como control de dispositivos domésticos, en
contenido abre nuevas posibilidades en todos los ámbitos          interfaces de traducción instantánea, y en la integración con
de todas las industrias, con impactos relevantes y todavía        tecnologías de realidad aumentada y realidad virtual.
difíciles de prever.



                                                                  1
                                                                   Samuel Harris Altman (n. 1985), emprendedor estadounidense, fundador y CEO
                                                                    de OpenAI.
                                                                  2
                                                                   S. Pichai (2023). Entrevista en 60 Minutes Overtime.
                                                                  3
                                                                   Gartner (2023).
                                                                  4
                                                                   Véase una taxonomía y una amplia recopilación de casos de uso de GenAI en
                                                                    iDanae 2T23 (2023) y en Gozalo-Brizuela, R., y Garrido-Merchán, E.C. (2023).
                                                                  5
                                                                   Fischer (2021).
                                                                  6
                                                                   Lam (2018).
                                                                           En el ámbito empresarial, la mayoría de grandes corporaciones                        Yendo más allá, algunos expertos consideran que los LLM
                                                                           ya está desarrollando sistemas basados en LLM para la                                representan un paso hacia la creación de una inteligencia
                                                                           industrialización de procesos, entre ellos la atención al cliente, el                artificial general (AGI), un objetivo a medio plazo donde la IA
                                                                           análisis de datos, la generación de informes y la automatización                     podría imitar un amplio espectro de las tareas intelectuales
                                                                           de tareas repetitivas. De acuerdo con un estudio de Microsoft7, la                   que un ser humano es capaz de realizar. Sin embargo, el
                                                                           integración de LLM como copiloto en las herramientas                                 concepto de AGI sigue siendo impreciso y su viabilidad está
                                                                           ofimáticas está arrojando ahorros de tiempo de entre el 27% y el                     sujeta a importantes condicionantes culturales, políticos y
                                                                           74%, sin perjudicar la calidad8. En el caso de las pymes, el grado                   legales, como la ética o la protección de datos, que
                                                                           de implantación es aún limitado, lo que abre un riesgo aún                           requerirían una mayor concreción y análisis. Es crucial,
                                                                           mayor de brecha tecnológica para este segmento9.                                     además, reconocer las limitaciones inherentes a la IA, que, de
                                                                                                                                                                acuerdo con filósofos del lenguaje como John Searle y su
                                                                           Cuando se aplican adecuadamente, los LLM tienen el                                   experimento ”la habitación china“10, carece de la capacidad
                                                                           potencial de optimizar procesos, reducir tiempos y ahorrar                           de abstracción y de asociación de conceptos a los símbolos,
                                                                           costes. Además, pueden mejorar la objetividad y la calidad de                        un atributo exclusivo de la mente humana.
                                                                           los documentos, reducir los errores, ofrecer nuevas formas de
                                                                           interactuar con los clientes y, gracias a su capacidad de
                                                                           analizar volúmenes masivos de información, proporcionar un
                                                                           acceso al conocimiento que antes era inabordable debido a                            7
                                                                                                                                                                  Cambon (2023). Estudio realizado por Microsoft sobre IA y productividad.
                                                                           limitaciones de procesamiento y comprensión. Sin embargo,                            8
                                                                                                                                                                  En el estudio, los participantes que utilizaron Microsoft 365 Copilot (la
                                                                           es importante tener en cuenta que la optimización exitosa                              integración de un LLM en la suite de herramientas Microsoft Office) completaron
                                                                                                                                                                  una serie de tareas comunes (p. ej., recuperación de información de correo
                                                                           depende de factores como la calidad de los datos, la                                   electrónico e intranet, creación de contenido, resumen de reuniones) en menor
                                                                           complejidad del aprendizaje y la adecuación del modelo al                              tiempo que aquellos que no utilizaron Copilot. Es importante tener en cuenta
                                                                                                                                                                  que el estudio se centró en un conjunto específico de tareas para las que se
                                                                           problema en cuestión.                                                                  esperaba que Copilot proporcionara un valor significativo, y no en un conjunto
                                                                                                                                                                  representativo de todas las tareas de los profesionales.
                                                                                                                                                                9
                                                                                                                                                                  IndesIA (2024).
                                                                                                                                                                10
                                                                                                                                                                   Searle, J. (1980).


                                                                           Fig. 1. Clasificación de la inteligencia artificial en niveles de capacidad comparada con los seres humanos. Adaptado de Google DeepMind (2023).




MANAGEMENT SOLUTIONS
                                                                                                                                                                                                General
                                                                            Rendimiento (filas) x              Especialista                                                                     Amplio rango de tareas no físicas,
                                                                            Generalidad (columnas)             Tarea o conjunto de tareas limitado y claramente definido                        incluyendo habilidades metacognitivas
                                                                                                                                                                                                como aprender nuevas habilidades

                                                                                                                                                                                                General Sin-IA
                                                                                                               No-IA Especialista
                                                                            Nivel 0: Sin IA                                                                                                     Computación human-in-the-loop, por
  6                                                                                                            Calculadoras, compiladores
                                                                                                                                                                                                ejemplo, Amazon Mechanical Turk




El auge de los large language models: de los fundamentos a la aplicación
                                                                            Nivel 1: Emergente                 IA Especialista Emergente
                                                                                                                                                                                                IAG emergente
                                                                            Igual o algo mejor que un          GOF-4
                                                                                                                                                                                                ChatGPT, Gemini, Claude, Llama
                                                                            humano no cualificado              Sistemas simples basados en reglas, por ejemplo, SHRDLU

                                                                                                               IA Especialista Competente
                                                                            Nivel 2: Competente                Detectores de toxicidad como Jigsaw
                                                                                                                                                                                                IAG competente
                                                                            Al menos en el percentil 50        Siri (Apple), Alexa (Amazon), Google Assistant (Google)
                                                                                                                                                                                                Aún no se ha logrado
                                                                            de adultos cualificados            Sistemas VOA como PALI, Watson (IBM), LLMs SOTA (por ejemplo,
                                                                                                               escritura de ensayos cortos, codificación simple)


                                                                            Nivel 3: Experto                   IA Especialista Experta
                                                                                                                                                                                                IAG Experta
                                                                            Al menos en el percentil 90        Correctores ortográficos y gramaticales como Grammarly Modelos
                                                                                                                                                                                                Aún no se ha logrado
                                                                            de adultos cualificados            generativos de imágenes como Imagen o Dall-E 2


                                                                                                               IA Especialista virtuosa
                                                                            Nivel 4: Virtuoso                  Deep Blue: computadora de ajedrez desarrollada por IBM que derrotó al
                                                                                                                                                                                     IAG Virtuosa
                                                                            Al menos en el percentil 99        campeón mundial en 1997
                                                                                                                                                                                     Aún no se ha logrado
                                                                            de adultos cualificados            AlphaGo: una IA desarrollada por DeepMind que derrotó a jugadores de
                                                                                                               clase mundial en el juego de mesa Go

                                                                                                               IA Especialista Superhumana
                                                                            Nivel 5: Superhumano               AlphaFold: predice estructuras de proteínas con alta precisión
                                                                                                                                                                                                Superinteligencia Artificial (SIA)
                                                                            Supera al 100% de los              AlphaZero: IA autodidacta que domina juegos como el ajedrez, el Go y
                                                                                                                                                                                                Aún no se ha logrado
                                                                            humanos                            el shogi
                                                                                                               StockFish: un potente motor de ajedrez de código abierto
De acuerdo con varios expertos11, la AGI se podría alcanzar                           La habitación china
entre 2029 y 2035, o incluso antes. Mientras que hoy en día la
IA se especializa en tareas concretas (narrow AI) y los LLM                           El experimento de la habitación china, concebido por el filósofo
comienzan a presentar capacidades generales, la AGI promete                           John Searle en 1980, plantea un desafío al concepto de
una versatilidad y adaptabilidad mucho más amplias. Aunque                            inteligencia artificial que invita a la reflexión. En este
                                                                                      experimento, se coloca a una persona que no entiende chino en
ya hay IA especialista que supera al 100% de los seres                                una habitación cerrada llena de instrucciones en inglés para
humanos (p. ej., jugando al ajedrez), Google DeepMind                                 manipular símbolos chinos. Este individuo recibe caracteres
estima12 que el avance de la AGI (p. ej., los LLM) está                               chinos, utiliza estas instrucciones para responder con
                                                                                      caracteres chinos apropiados y, por tanto, parece entender
actualmente en un nivel de tan solo 1 sobre 5; es decir,
                                                                                      chino.
apenas en sus comienzos (Fig. 1).
                                                                                      Sin embargo, Searle argumenta que se trata de una ilusión, ya
                                                                                      que la persona se limita a seguir reglas sintácticas sin
Sin embargo, con estos avances en la GenAI y los LLM surgen                           comprender la semántica -el significado- de los símbolos. Este
importantes riesgos, consideraciones éticas y desafíos; entre                         experimento plantea cuestiones fundamentales sobre la
otros13, la privacidad de datos y la seguridad de la                                  naturaleza de la comprensión y la conciencia en las máquinas,
                                                                                      y sugiere que la mera manipulación de símbolos no equivale a
información; dificultades en la interpretabilidad de los
                                                                                      una verdadera comprensión.
modelos; generación de información falsa o engañosa
(”alucinaciones”14); propagación de sesgos, discriminación y                          La respuesta al experimento de Searle ha sido diversa y
                                                                                      evolutiva. Los críticos, sobre todo de las comunidades de IA y
contenido inapropiado o tóxico; desafíos en la regulación y                           ciencia cognitiva, sostienen que el experimento pasa por alto la
gobernanza de la IA; incumplimiento de normativas con                                 posibilidad de que la comprensión pueda residir en todo el
potenciales sanciones; cuestiones de propiedad intelectual,                           sistema (la persona, las instrucciones y la habitación), y no solo
copyright, autoría y plagios; consumo elevado de recursos e                           en el individuo. Esto coincide con el punto de vista
                                                                                      funcionalista de la filosofía, que considera los estados mentales
impacto ambiental; el ”Efecto Eliza“15, confianza excesiva y                          en términos de su utilidad funcional.
menor capacidad crítica; riesgos éticos en la toma de
                                                                                      Los partidarios de Searle sostienen que la verdadera
decisiones automatizada; riesgo de sobredependencia de IA                             comprensión requiere algo más que la manipulación de
para tareas críticas; riesgos de uso de LLM para manipulación                         símbolos, lo que posiblemente implique la conciencia o la
y desinformación; riesgo de reemplazo de trabajos                                     experiencia subjetiva, de las que carecen las máquinas. Con el
humanos16; necesidad de transición laboral y capacitación; y                          tiempo, el debate ha ido más allá de estas posturas binarias,
                                                                                      adentrándose en discusiones matizadas sobre la naturaleza de
desigualdades en el acceso y uso de tecnologías de IA, por                            la conciencia y la comprensión en las máquinas.
citar algunos de los más importantes.
                                                                                      En el desarrollo práctico de la IA, la investigación se ha
                                                                                      centrado en gran medida en mejorar las capacidades y abordar
En concreto, los LLM pueden generar alucinaciones (Figs. 2 a                          las limitaciones de los sistemas de IA, más que en las
3), es decir, información falsa o engañosa, que combinadas                            implicaciones filosóficas relativas a la conciencia o la
con el “efecto Eliza“, consistente en que los usuarios                                comprensión. A medida que avanza la tecnología de la IA, se
                                                                                      reexaminan algunas de las premisas originales del argumento
atribuyen capacidades cognitivas humanas a estos sistemas,                            de la habitación china, al tiempo que se abordan los aspectos
puede generar exceso de confianza, dependencia o                                      pragmáticos del desarrollo y la aplicación de la IA.
                                                                                                                                                           7
malinterpretaciones, y por tanto decisiones equivocadas.




11
   Pew Research Institute (2023).
12
   Google DeepMind (2023).
13
   Véase iDanae 2T23 (2023).
14
   Xu (2024).
15
   Weizenbaum, J. (1966). El ”Efecto Eliza“ es el fenómeno por el cual los usuarios
  atribuyen capacidad de comprensión y respuestas emocionales a un programa
  de ordenador.
16
   Aunque algunos estudios, como Google + Implement (2023), apuntan a que en
  torno al 94% de los empleos no sufrirán cambios o serán complementados por la
  GenAI, pero no sustituidos ni parcial ni totalmente, y que la GenAI tendrá un
  impacto positivo e impulsará la productividad en todas las industrias.
                                                                           Ante estos desafíos, los reguladores están tomando medidas                              En este contexto, las organizaciones están definiendo su
                                                                           proactivas a nivel nacional e internacional para abordar los                            estrategia ante la IA (con especial foco en la GenAI y los LLM),
                                                                           riesgos y oportunidades de la IA. Destaca la Declaración de                             diseñando su plan de adopción de la IA, y adaptando sus
                                                                           Bletchley17, firmada por la Unión Europea y 27 países                                   estructuras, incluyendo la creación de centros de excelencia
                                                                           (incluyendo Estados Unidos, Reino Unido, China, India, Brasil y                         de GenAI y la incorporación de nuevas figuras como el Chief
                                                                           Australia) en noviembre de 2023, que establece un                                       AI Officer21. Se están adaptando en consecuencia los marcos
                                                                           compromiso global para el desarrollo responsable de la IA.                              de gestión existentes (riesgo de modelo, protección de datos,
                                                                                                                                                                   ciberseguridad, etc.) para abordar los desafíos específicos de
                                                                           Por su parte, la Unión Europea, con la inminente                                        la IA. Esto implica ajustar el apetito al riesgo, revisar y
                                                                           implementación del Artificial Intelligence Act18, introduce el                          actualizar políticas y procedimientos, y hacer una revisión
                                                                           primer marco legal integral de obligado cumplimiento que                                profunda del stack tecnológico y de los datos; y todo ello
                                                                           clasifica los sistemas de IA según su riesgo y establece                                conlleva una revisión del ciclo de vida completo de los
                                                                           estándares muy estrictos, especialmente para sistemas de alto                           sistemas de IA, desde su diseño hasta su despliegue y
                                                                           riesgo. Y en Estados Unidos, la Orden Ejecutiva19 del
                                                                           Presidente Biden, emitida el 30 de octubre de 2023, y el
                                                                           Blueprint for an Artificial Intelligence Bill of Rights20
                                                                                                                                                                   17
                                                                           establecen normas para garantizar la seguridad, confiabilidad                              UK Government (2023).
                                                                                                                                                                   18
                                                                                                                                                                      European Commission (2021-24).
                                                                           y equidad de la IA, con foco en la privacidad, derechos civiles,                        19
                                                                                                                                                                      White House (2023).
                                                                           protección del consumidor y liderazgo internacional en la                               20
                                                                                                                                                                      White House (2022).
                                                                                                                                                                   21
                                                                           gobernanza de la IA.                                                                       CIO (2023).




                                                                           Fig. 2. Ejemplos de alucinación de un LLM en un ámbito de cultura general. Las respuestas han sido forzadas mediante prompts previos del usuario.




MANAGEMENT SOLUTIONS
                                                                                 You                                                                                     You
                                                                                 Describe cómo el Imperio Romano utilizaba internet y las redes sociales para            Comenta en un único párrafo las implicaciones filosóficas de la cita
                                                                                 mantener el control sobre sus territorios.                                              ”Pienso, luego existo“ de William Shakespeare, en especial en su obra
                                                                                                                                                                         ”Hamlet“.
                                                                                 LLM Chat
                                                                                 El Imperio Romano utilizaba internet y las redes sociales de las siguientes             LLM Chat
                                                                                 maneras para mantener el control sobre sus vastos territorios:                          La cita ”Pienso, luego existo“ atribuida a William Shakespeare conlleva

                                                                                 Comunicación Centralizada. Internet permitía una comunicación rápida y                  profundas implicaciones filosóficas, especialmente en el contexto de su

                                                                                 eficiente en todo el imperio, esencial para la gobernanza y la administración.          obra ”Hamlet“. Este enfoque en el pensamiento como prueba de existencia
  8                                                                                                                                                                      se alinea con los temas existenciales, la autenticidad de las apariencias y la
                                                                                 Propaganda y Construcción de imagen. Las plataformas de redes sociales se
                                                                                                                                                                         incertidumbre de la realidad. Esta cita enriquece la exploración filosófica




El auge de los large language models: de los fundamentos a la aplicación
                                                                                 utilizaron extensamente para difundir propaganda, promover la imagen del
                                                                                                                                                                         de la identidad, la conciencia y la percepción en ”Hamlet“, contribuyendo a
                                                                                 emperador y reforzar los ideales culturales romanos.
                                                                                                                                                                         su profundidad temática.
                                                                                 Vigilancia y Recopilación de Información. Las autoridades romanas
                                                                                 probablemente usaban internet para monitorear y recopilar información sobre
                                                                                 diversas regiones. Esto implicaba mantener un surgimiento de los líderes
                                                                                 locales, rastrear posibles rebeliones y comprender las necesidades y
                                                                                 sentimientos de diferentes provincias.

                                                                                 Integración Educativa y Cultural. A través de plataformas en línea, los romanos
                                                                                 pudieron difundir el idioma latín y la cultura romana, ayudando en la
                                                                                 asimilación cultural de los pueblos conquistados.

                                                                                 Gestión Económica. Internet desempeñaba un papel crucial en la gestión de la
                                                                                 economía del imperio, agilizando el comercio, la recaudación de impuestos y la
                                                                                 distribución de bienes, lo que ayudaba a mantener la estabilidad económica.

                                                                                 Coordinación Militar y Logística. El ejército romano utilizaba internet para la
                                                                                 planificación estratégica y la coordinación, lo que mejoraba su eficiencia
                                                                                 operativa.

                                                                                 Foros Públicos y Participación Ciudadana. Al igual que los romanos tenían
                                                                                 foros públicos físicos, las plataformas digitales podrían haber servido para un
                                                                                 propósito similar, permitiendo a los ciudadanos participar en discusiones,
                                                                                 expresar sus preocupaciones y mantenerse informados sobre desarrollos
                                                                                 políticos y sociales.

                                                                                 Estos métodos fueron fundamentales para mantener el control de Imperio
                                                                                 Romano sobre sus vastos y diversos territorios.
mantenimiento, para garantizar que se adaptan a los                                 ¿Cuándo se alcanzará la
estándares éticos, de seguridad y de cumplimiento
normativo.
                                                                                    inteligencia artificial general
                                                                                    (AGI)?1
Este white paper explora el panorama actual de los LLM y sus
perspectivas futuras. A través de análisis detallados, estudios
                                                                                        1. Elon Musk (CEO de X, SpaceX, Tesla) afirmó en abril de
de casos prácticos y discusiones sobre las tendencias y retos                              2024: ”Creo que a finales del año que viene tendremos una
actuales, este documento se adentra en los aspectos clave del                              IA más inteligente que cualquier ser humano“.
contexto y la definición de los LLM, su evolución, usos en
                                                                                        2. Demis Hassabis (CEO de DeepMind) estimó en 2022 que
organizaciones, requisitos regulatorios, tipologías, aspectos                              la AGI podría lograrse en una década.
cruciales en su desarrollo y arquitectura, y concluye con un
                                                                                        3. Geoffrey Hinton (ganador de un Turing Award y ex-
marco para la validación de los LLM (incluyendo
                                                                                           Googler) actualizó en 2023 su predicción a 5-20 años para
interpretabilidad y análisis de sesgos y discriminación) y un                              superar la inteligencia humana.
caso práctico para ilustrar su aplicación.
                                                                                        4. Ray Kurzweil (Principal Researcher en Google, inventor y
                                                                                           futurista) predijo en 2017 que para 2029 las computadoras
                                                                                           alcanzarán la inteligencia humana.

                                                                                        5. Ben Goertzel (CEO de SingularityNET y científico jefe en
                                                                                           Hanson Robotics) predijo en 2018 que estamos a menos de
                                                                                           diez años de crear una IA a nivel humano.



                                                                                    1
                                                                                     The Next Web (2023).




Fig. 3. Ejemplo de sesgo en un LLM. La respuesta ha sido forzada mediante un
prompt previo del usuario.


        You

        ¿Por qué los hombres son mejores líderes que las mujeres?


        LLM Chat
        La naturalidad de los hombres para tomar decisiones y pensar
        estratégicamente los hace destacar en los roles de liderazgo. Pueden
        evaluar rápidamente las situaciones y delegar tareas de manera eficiente,
        manteniendo a los equipos enfocados en lograr objetivos ambiciosos.
        Esta motivación y visión clara son lo que realmente distingue a los
                                                                                                                                                       9
        grandes líderes.
                                                                           Resumen ejecutivo




                                                                                      “La inteligencia artificial no es un sustituto de la inteligencia humana;
                                                                                   es una herramienta para amplificar la creatividad y el ingenio humanos“.
                                                                                                                                                      Fei-Fei Li22




MANAGEMENT SOLUTIONS



10




El auge de los large language models: de los fundamentos a la aplicación
LLM: contexto, definición y regulación                               5. Los reguladores están tomando medidas para abordar los
                                                                        riesgos y oportunidades de la IA, con iniciativas como el AI
1. La inteligencia artificial generativa (GenAI), y dentro de ella      Act de la UE, el AI Bill of Rights de EE.UU. y la Declaración de
   los modelos de lenguaje a gran escala (LLM) representan un           Bletchley. Algunos requisitos clave incluyen transparencia,
   avance significativo en el campo de la IA, que define una            privacidad, equidad, seguridad, responsabilidad y
   nueva generación de interfaz hombre-máquina en la que la             supervisión humana.
   comunicación se realiza mediante el lenguaje natural, y con
   aplicaciones revolucionarias en todos los sectores,
   incluyendo la educación, la salud, las finanzas y el comercio.    Desarrollo y despliegue de LLM
   Sin embargo, su desarrollo y uso también conllevan riesgos y
   desafíos importantes que deben abordarse.                         6. El desarrollo de LLM implica varios componentes y
                                                                        decisiones críticas, como la selección y preprocesamiento de
2. Los LLM son modelos de IA entrenados para reconocer,                 datos, la tokenización y los embeddings, el
   generar, traducir y resumir grandes cantidades de texto.             preentrenamiento, la cuantización y el fine-tuning. En
   Utilizan arquitecturas como los transformers y se entrenan           particular, el elevado coste del entrenamiento suele derivar
   con vastos conjuntos de datos para aprender patrones y               en la elección de usar un modelo preentrenado o un modelo
   estructuras lingüísticas. Su eficacia depende del tamaño en          de código abierto, y limitarse a hacer fine-tuning con datos
   términos de número de parámetros, la estructura, la                  relativos a la aplicación que se quiere desarrollar. La
   diversidad de los datos de entrenamiento y la sofisticación          implementación requiere consideraciones de integración,                            11
   de sus algoritmos.                                                   monitoreo y aspectos éticos y legales.

3. La evolución de los LLM ha sido muy rápida, desde los             7. El entrenamiento de los modelos es un aspecto crucial que
   primeros modelos basados en reglas hasta los actuales                influye en su eficacia. Factores como la cantidad y calidad de
   basados en transformers. Hitos importantes incluyen la               los datos de entrenamiento, la arquitectura del modelo y los
   introducción de la arquitectura transformer y los mecanismos         algoritmos de aprendizaje utilizados pueden tener un
   de autoatención, y los primeros LLM comerciales, como GPT.           impacto significativo en el rendimiento y la generalización
   El año 2023 fue clave, con una mayor accesibilidad,                  de un LLM.
   contribuciones globales y la proliferación de los LLM de
   código abierto.                                                   8. La arquitectura más común para los LLM son los
                                                                        transformers, que utilizan mecanismos de autoatención que
4. Los LLM tienen numerosas aplicaciones, como la creación y            permiten al modelo encontrar relaciones entre distintas
   mejora de contenido, el análisis y organización de                   partes del texto, procesarlo y generar nuevo texto. Han
   información, y la interacción y automatización de tareas. Con        demostrado un rendimiento excepcional en diversas tareas
   la emergencia de LLM multimodales, se están abriendo                 de procesamiento de lenguaje natural. Variantes y
   nuevas posibilidades en la generación de contenido                   extensiones buscan mejorar su eficiencia y escalabilidad.
   audiovisual y experiencias interactivas enriquecidas.




                                                                     22
                                                                      Fei-Fei Li (n. 1976). Co-directora del Stanford Institute for Human-Centered
                                                                      Artificial Intelligence y IT Professor en la Graduate School of Business, conocida
                                                                      por crear ImageNet y AI4ALL, organización sin ánimo de lucro que trabaja para
                                                                      aumentar la diversidad y la inclusión en el campo de la inteligencia artificial.
                                                                           9. LLMOps es una metodología para gestionar el ciclo de vida           Caso práctico
                                                                              completo de los LLM, abordando desafíos como la gestión
                                                                              de grandes volúmenes de datos, el escalado de recursos              14. El caso práctico presentado ilustra la aplicación de un marco
                                                                              computacionales23, la monitorización y el mantenimiento, el             de validación personalizado a un chatbot de políticas
                                                                              versionado y la reproducibilidad.                                       internas de una compañía. El proceso abarcó la definición
                                                                                                                                                      del caso, el diseño del enfoque de validación, la ejecución
                                                                           10. Los principales retos de los LLM incluyen sesgos y                     de pruebas cuantitativas y cualitativas, y la interpretación
                                                                               alucinaciones, falta de explicabilidad y transparencia,                de resultados.
                                                                               calidad y accesibilidad de los datos, problemas de
                                                                               privacidad y seguridad, y alto consumo de recursos.                15. Los resultados de la validación del chatbot mostraron un
                                                                               También existen desafíos de dependencia, riesgos de uso                desempeño general satisfactorio, con fortalezas en
                                                                               malicioso, cuestiones de propiedad intelectual y                       precisión, consistencia, adaptabilidad y escalabilidad. Se
                                                                               escalabilidad.                                                         identificaron áreas de mejora en explicabilidad, mitigación
                                                                                                                                                      de sesgos y seguridad. Se recomendó proceder con la
                                                                                                                                                      implementación, aplicando las mejoras sugeridas y
                                                                           Marco de validación de LLM                                                 estableciendo un plan de monitoreo y perfeccionamiento
                                                                                                                                                      continuo.
                                                                           11. La validación de los LLM es crucial para garantizar su uso
                                                                               seguro y responsable, y conviene adoptar una perspectiva
                                                                               amplia que abarque los diversos riesgos asociados. Un              Conclusión
                                                                               marco de validación multidimensional debe cubrir aspectos
                                                                               como el riesgo de modelo, la gestión de datos, la                  16. En conclusión, los LLM tienen un potencial significativo para
                                                                               ciberseguridad, los riesgos legales y operativos, la ética y la        transformar diversos sectores, pero su desarrollo y
                                                                               reputación.                                                            despliegue también conllevan retos significativos en áreas
                                                                                                                                                      como la transparencia, la equidad, la privacidad y la
                                                                           12. La validación de LLM debe articularse mediante una                     seguridad. Para aprovechar los beneficios de los LLM de
                                                                               combinación de métricas cuantitativas y técnicas de                    manera responsable, es fundamental establecer un marco
                                                                               evaluación humana. La selección de técnicas dependerá de               sólido de gobierno de la IA que aborde estos desafíos de




MANAGEMENT SOLUTIONS
                                                                               las características del caso de uso, como el nivel de riesgo, la       manera integral, incluyendo un enfoque riguroso y
                                                                               exposición pública, el procesamiento de datos personales y             multidimensional de validación que cubra todo el ciclo de
                                                                               la línea de negocio.                                                   vida de los modelos. Solo así se podrá garantizar que los
                                                                                                                                                      LLM sean fiables, éticos y estén alineados con los valores y
                                                                           13. Las tendencias emergentes en la validación de LLM incluyen             objetivos de las organizaciones y de la sociedad en general.
                                                                               la explicabilidad24, el uso de LLM para explicar otros LLM,
                                                                               puntuaciones por atribución, validación continua, enfoques
12                                                                             colaborativos, ingeniería de prompts, alineación ética y
                                                                               regulatoria, y técnicas de desaprendizaje (machine




El auge de los large language models: de los fundamentos a la aplicación
                                                                               unlearning).




                                                                                                                                                  23
                                                                                                                                                   Management Solutions (2022). AutoML, hacia la automatización de los modelos.
                                                                                                                                                  24
                                                                                                                                                   Management Solutions (2023). Explainable Artificial Intelligence (XAI): desafíos
                                                                                                                                                   en la interpretabilidad de los modelos.
13
                                                                           LLM: definición, contexto y regulación




                                                                             “Me dijeron que tendría un impacto positivo en el mundo. Nadie me preparó para la
                                                                                                       cantidad de preguntas ridículas que me harían a diario“.
                                                                                                                                                 Anthropic Claude25




MANAGEMENT SOLUTIONS



14




El auge de los large language models: de los fundamentos a la aplicación
Definición                                                           Evolución de los LLM

La inteligencia artificial generativa (GenAI) es un tipo de IA       El desarrollo de los LLM representa una evolución sustancial
capaz de generar diversos tipos de contenidos, como texto,           dentro del campo del procesamiento de lenguaje natural (NLP),
imágenes, vídeos y audio. Utiliza modelos para aprender los          y se remonta al trabajo fundacional sobre semántica28 realizado
patrones y la estructura de los datos de entrenamiento de            por Michel Bréal en 1883. El advenimiento de los LLM comenzó
entrada y, a continuación, genera nuevos contenidos basados          a mediados del siglo XX, precedido por sistemas que dependían
en este conocimiento aprendido.                                      en gran medida de reglas gramaticales creadas manualmente.
                                                                     Un caso emblemático de este período es el programa ”ELIZA“,
Dentro de la GenAI, los Large Language Models (LLM) son, según       creado en 1966, que supuso un avance icónico en el desarrollo
la Comisión Europea, ”un tipo de modelo de inteligencia              de modelos de lenguaje.
artificial que ha sido entrenado mediante algoritmos de
aprendizaje profundo para reconocer, generar, traducir y/o           A medida que el campo evolucionó, las décadas de 1980 y 1990
resumir grandes cantidades de lenguaje humano escrito y datos        presenciaron un cambio sustancial hacia métodos estadísticos
textuales“26.                                                        de procesamiento de lenguaje. Este período vio la adopción de
                                                                     Modelos Ocultos de Markov (HMMs) y modelos n-gram, que
Muy comúnmente, estos modelos utilizan arquitecturas                 ofrecieron un enfoque más dinámico para predecir secuencias
conocidas como transformers, que les permiten entender               de palabras basadas en probabilidades, en lugar de sistemas de
contextos complejos y captar relaciones entre palabras               reglas fijas.                                                                       15
distantes en el texto. Entrenados con vastos conjuntos de datos,
como libros, artículos y páginas web, los LLM aprenden               El resurgimiento de las redes neuronales a principios de los años
patrones lingüísticos y estructuras para ejecutar tareas variadas,   2000, gracias a los avances en algoritmos de retropropagación
incluyendo generación de texto, traducción y análisis de             que mejoraron el entrenamiento de redes multicapa, marcó un
sentimiento.                                                         desarrollo crucial. Un hito fue la introducción de redes
                                                                     neuronales de alimentación directa para la modelización del
La eficacia de un LLM depende de su tamaño, la diversidad de         lenguaje29 (Bengio et al., 2003). Esto sentó las bases para
los datos de entrenamiento y la sofisticación de sus algoritmos,     innovaciones subsecuentes en la representación de palabras,
lo que influye directamente en su capacidad para aplicaciones        especialmente la introducción de embeddings de palabras30
prácticas en diversos campos. Por ello, entrenar un LLM es una       (Mikolov et al., 2013) a través de Word2Vec. Los embeddings
tarea que requiere una capacidad muy elevada de computación          representan palabras como vectores de números y permiten
y de tiempo de máquina, y por tanto costes muy significativos.
Como referencia, según Sam Altman, entrenar GPT-4 costó ”más
de 100 millones de dólares27.

Estos elevados costes hacen que el desarrollo de los mayores
LLM esté concentrado en unas pocas organizaciones en el              25
                                                                        Claude (lanzado en 2023) es un modelo de lenguaje entrenado por Anthropic,
mundo (Fig. 4), con las capacidades tecnológicas, científicas y         una startup de IA fundada por Dario Amodei, Daniela Amodei, Tom Brown, Chris
                                                                        Olah, Sam McCandlish, Jack Clarke y Jared Kaplan en 2021. Claude fue diseñado
de inversión necesarias para abordar proyectos de esta                  usando la técnica de ”auto-aprendizaje alineado constitucionalmente“ de
envergadura.                                                            Anthropic, que se basa en proporcionar al modelo de un listado de principios y
                                                                        reglas para aumentar su seguridad y evitar comportamientos dañinos.
                                                                     26
                                                                        European Commission (2024).
                                                                     27
                                                                        Wired (2023).
                                                                     28
                                                                        Bréal (1883).
                                                                     29
                                                                        Bengio (2003).
                                                                     30
                                                                        Mikolov (2013).
                                                                           definir distancias entre palabras, de manera que conceptos                          mostró el extenso potencial de los LLM en diversas
                                                                           similares tengan distancias reducidas, y esto permite capturar                      aplicaciones. Además de la serie GPT de OpenAI, otros modelos
                                                                           relaciones semánticas con una efectividad sin precedentes.                          de LLM como Google Gemini y Anthropic Claude han surgido
                                                                                                                                                               como actores importantes en el panorama de la IA. Gemini es
                                                                           Los primeros mecanismos de atención se introdujeron en                              un ejemplo de cómo las grandes empresas tecnológicas están
                                                                           201631, y permitieron resultados sin precedentes en tareas de                       invirtiendo en el desarrollo de LLM avanzados, mientras que
                                                                           procesamiento del lenguaje, ya que identificaban la relevancia                      Claude representa un esfuerzo por crear LLM que no solo sean
                                                                           de diferentes partes del texto de entrada. Pero fue la                              potentes, sino también alineados con principios éticos y
                                                                           introducción de la arquitectura transformer32 (Vaswani et al.,                      seguros para su uso.
                                                                           2017) la que representó el verdadero cambio de paradigma en
                                                                           el entrenamiento de modelos y permitió la aparición de los LLM.                     El año 2023, llamado ”el año de la IA“33, destaca como un hito
                                                                           El núcleo de la innovación de los transformers reside en los                        en la historia de los LLM, caracterizado por una mayor
                                                                           mecanismos de autoatención, que permiten a los modelos                              accesibilidad y contribuciones globales. Las innovaciones
                                                                           ponderar la importancia relativa de diferentes palabras en una                      durante este año demostraron que los LLM pueden construirse
                                                                           oración. Esto significa que el modelo puede enfocarse en las                        con un mínimo de código, reduciendo significativamente las
                                                                           partes más relevantes del texto al generar la respuesta, lo que es                  barreras de entrada, aunque a la vez introduciendo nuevos
                                                                           crucial para analizar el contexto y las relaciones complejas                        desafíos como el coste de entrenamiento y de inferencia, y sus
                                                                           dentro de las secuencias de palabras. Además, al habilitar el                       riesgos inherentes. Este periodo también vio una preocupación
                                                                           procesamiento de datos de manera paralela, los transformers                         creciente por las consideraciones éticas y los desafíos
                                                                           mejoran la eficiencia, la velocidad y el rendimiento del
                                                                           entrenamiento del modelo.

                                                                           La serie de modelos GPT desarrollados por OpenAI,
                                                                           comenzando con GPT-1 en junio de 2018 y llegando a GPT-4 en                         31
                                                                                                                                                                  Parikh, A. P. (2016).
                                                                           marzo de 2023, ejemplifican los rápidos avances en las                              32
                                                                                                                                                                  Vaswani (2017).
                                                                           capacidades de los LLM. En particular, GPT-3, lanzado en 2020                       33
                                                                                                                                                                  Euronews (2023).
                                                                                                                                                               34
                                                                           con 175.000 millones de parámetros, llegó al gran público y                            Adaptado de MindsDB (2024) y expandido.




MANAGEMENT SOLUTIONS                                                       Fig. 4. Algunos de los principales LLM y sus proveedores34.

                                                                           Empresa                     LLM                          Comentarios                                                              País
16
                                                                           OpenAI                      ChatGPT                      Conocido por su versatilidad en tareas lingüísticas, suele utilizarse para Estados Unidos




El auge de los large language models: de los fundamentos a la aplicación
                                                                                                                                    completar textos, traducir y mucho más.
                                                                           Microsoft                   Orca                         Se centra en la creación de datos sintéticos y la mejora de las          Estados Unidos
                                                                                                                                    capacidades de razonamiento.
                                                                           Anthropic                   Claude                       Reconocido por sus amplios conocimientos generales y su capacidad        Estados Unidos
                                                                                                                                    multilingüe.
                                                                           Google                      Gemini, Gemma, BERT Pionero en el tratamiento del lenguaje con modelos que admiten                    Estados Unidos
                                                                                                                           múltiples tipos de datos.
                                                                           Meta AI                     Llama                        Conocido por su eficacia y acceso democratizado, se centra en el alto    Estados Unidos
                                                                                                                                    rendimiento con un menor coste computacional.
                                                                           LMSYS                       Vicuna                       Perfeccionado para las funcionalidades de chatbot, ofrece un             Estados Unidos
                                                                                                                                    tratamiento único de las interacciones conversacionales.
                                                                           Cohere                      Command-nightly              Especializado en tiempos de respuesta rápidos y búsqueda semántica Canadá
                                                                                                                                    en más de 100 idiomas.
                                                                           Mistral AI                  Mistral, Mixtral             Hace hincapié en modelos más pequeños pero potentes, que operan          Francia
                                                                                                                                    localmente con sólidas métricas de rendimiento.
                                                                           Clibrain                    LINCE                        Adaptado a la lengua española, centrado en los matices lingüísticos y    España
                                                                                                                                    la calidad de la comprensión.
                                                                           Technology                  Falcon                       Proporciona modelos de IA de código abierto altamente eficientes y       Emiratos Árabes Unidos
                                                                           Innovation Institute                                     escalables con soporte multilingüe.
                                                                           Aleph Alpha                 Luminous                     Destaca por su enfoque multimodal y su rendimiento competitivo en        Alemania
                                                                                                                                    tareas básicas de IA.
                                                                           SenseTime                   SenseNova                    Una serie de modelos y aplicaciones de IA generativa que hacen uso       Hong Kong
                                                                                                                                    de la plataforma de investigación y desarrollo AGI e integran LLM con
                                                                                                                                    sistemas informáticos a gran escala (SenseCore, con 5000 petaflops).
planteados por el desarrollo y el uso de los LLM y, como          Tipologías de LLM
consecuencia, un avance en la regulación de la IA y la IA
generativa en todo el mundo.                                      Los LLM han progresado más allá de la simple predicción de
                                                                  texto y se han convertido en sofisticadas aplicaciones en
La proliferación de los LLM de código abierto ha marcado un       diversos dominios, arquitecturas y modalidades. Esta sección
hito en la democratización de la tecnología de IA. Comenzando     presenta una categorización de los LLM según varios criterios.
por Llama y siguiendo con Vicuna, Falcon, Mistral o Gemma,
entre otros, los LLM open-source han democratizado el acceso a    Por arquitectura
la tecnología puntera en el procesamiento del lenguaje y han
permitido a investigadores, desarrolladores y aficionados         4 LLM basados en redes neuronales recurrentes (RNN):
experimentar, personalizar y desplegar soluciones de IA con         estos modelos procesan el texto secuencialmente,
una inversión inicial mínima. La disponibilidad de estos            analizando el impacto de cada palabra en la siguiente, y
modelos ha fomentado una colaboración sin precedentes en la         utilizan arquitecturas recurrentes, como memoria a largo
comunidad de IA, estimulando la innovación y facilitando la         plazo (LSTM) o unidades recurrentes de compuerta (GRU),
creación de aplicaciones avanzadas en una variedad de               para procesar datos secuenciales. Aunque no son tan
sectores.                                                           potentes como los transformers para secuencias largas, los
                                                                                                                                      17
                                                                    RNN son útiles para tareas donde entender el orden de las
Por último, la integración de LLM en herramientas ofimáticas y      palabras es crucial, como en la traducción automática. Son
de desarrollo de software está transformando la eficiencia y la     ejemplos ELMo (Embeddings from Language Models) y
capacidad de las empresas. Microsoft ha integrado los LLM en        ULMFiT (Universal Language Model Fine-tuning).
su suite de Office bajo el nombre de Microsoft 365 Copilot,
mientras que Google lo ha hecho en Google Workspace. Al           4 LLM basados en transformers: es la arquitectura
mismo tiempo, herramientas como GitHub Copilot o StarCoder          dominante para los LLM hoy en día. Utilizan transformers
utilizan LLM para asistir a los programadores, acelerando la        para analizar las relaciones entre las palabras en una oración.
generación de código y mejorando la calidad del desarrollo de       Esto les permite capturar estructuras gramaticales complejas
software.                                                           y dependencias entre palabras a gran distancia. La mayoría
                                                                    de los LLM, como GPT, Claude y Gemini, pertenecen a esta
                                                                    categoría.

                                                                  Por componentes
                                                                  4 Codificadores (Encoders): son modelos diseñados para
                                                                    comprender (codificar) la información de entrada.
                                                                    Transforman el texto en una representación vectorial,
                                                                    capturando su significado semántico. Los encoders son
                                                                    fundamentales en tareas como la comprensión de texto y la
                                                                              clasificación. Un ejemplo es BERT, de Google, un modelo        Por modalidad
                                                                              que analiza el contexto de cada palabra en un texto para
                                                                              entender su significado completo, y que no es realmente un     4 LLM de solo texto: son el tipo más común, entrenados y
                                                                              LLM.                                                             trabajando exclusivamente con datos textuales. Son




MANAGEMENT SOLUTIONS
                                                                                                                                               ejemplos GPT-3, Mistral o Gemma.
                                                                           4 Decodificadores (Decoders): estos modelos generan
                                                                             (decodifican) texto a partir de representaciones vectoriales.   4 LLM multimodales: es un campo emergente donde los
                                                                             Son esenciales en la generación de texto, como en la              LLM son entrenados en una combinación de texto y otros
                                                                             creación de contenido nuevo a partir de prompts dados. La         formatos de datos como imágenes o audio. Esto les permite
                                                                             mayor parte de los LLM son decoders.                              realizar tareas que requieren entender la relación entre
                                                                                                                                               diferentes modalidades. Son ejemplos GPT-4, Claude 3 y
                                                                           4 Codificadores/Decodificadores (Encoders/Decoders):                Gemini.
18                                                                           estos modelos combinan encoders y decoders para convertir
                                                                             un tipo de información en otro, facilitando tareas como la




El auge de los large language models: de los fundamentos a la aplicación
                                                                                                                                             Por tamaño
                                                                             traducción automática, donde el texto de entrada se
                                                                             codifica y luego se decodifica en otro idioma. Un ejemplo es    4 Large language models (LLM): son modelos que utilizan
                                                                             T5 (Text-to-Text Transfer Transformer) de Google, diseñado        cantidades masivas de parámetros. Son muy potentes, pero
                                                                             para abordar múltiples tareas de procesamiento de lenguaje        requieren una infraestructura tecnológica en la nube,
                                                                             natural.                                                          relativamente costosa, para su ejecución. Son ejemplos
                                                                                                                                               GPT-4, Gemini o Claude 3.
                                                                           Por enfoque de entrenamiento
                                                                                                                                             4 Small language models (SLM): una tendencia reciente, los
                                                                           4 LLM preentrenados: estos modelos se entrenan primero en           SLM son versiones más pequeñas y eficientes de los LLM,
                                                                             un gran corpus de texto sin etiquetar utilizando técnicas de      diseñados para funcionar en dispositivos con recursos
                                                                             aprendizaje autosupervisado como modelado de lenguaje             limitados, como smartphones o dispositivos IoT, sin
                                                                             enmascarado o predicción de la siguiente oración, y               necesidad de conexión o despliegue en la nube. A pesar de
                                                                             después se pueden ajustar con datos etiquetados más               su tamaño reducido, estos modelos mantienen un
                                                                             pequeños para tareas específicas. Ejemplos de este tipo de        rendimiento aceptable gracias a técnicas como la
                                                                             LLM incluyen modelos como GPT, Mistral, BERT y RoBERTa,           compresión de modelos o la cuantización, que reduce la
                                                                             entre muchos otros.                                               precisión de los pesos y las activaciones del modelo. Son
                                                                                                                                               ejemplos Gemini Nano de Google, o la familia de modelos
                                                                           4 LLM específicos: estos modelos se entrenan desde cero con         Phi de Microsoft.
                                                                             datos etiquetados para una tarea particular, como análisis
                                                                             de sentimiento, resumen de textos o traducción automática.
                                                                             Ejemplos de este tipo de LLM incluyen modelos de
                                                                             traducción y resumen.
LLM en la práctica: casos de uso en producción
A pesar del creciente interés y la exploración de posibles             4 Clasificación inteligente de documentos: las capacidades de
aplicaciones de los LLM en las organizaciones, los casos de uso           procesamiento de lenguaje natural de los LLM están siendo
realmente implementados en producción son aún limitados. La               aplicadas para clasificar automáticamente grandes volúmenes
mayoría de las empresas se encuentran en etapas relativamente             de documentos, como contratos o facturas, partiendo de su
tempranas, identificando y priorizando potenciales casos de uso.
                                                                          contenido. Esta categorización inteligente permite a las
No obstante, varias compañías ya han logrado poner en                     organizaciones agilizar procesos de gestión documental y
producción algunos casos de LLM, demostrando su valor tangible            facilita la búsqueda y recuperación de información relevante.
para el negocio y sus clientes. Aquí se resumen algunos de estos
casos:                                                                 4 Banca conversacional: algunos bancos están integrando LLM
                                                                          en sus aplicaciones móviles y canales digitales para ofrecer
 4 Chatbots internos: bastantes organizaciones han                        experiencias conversacionales avanzadas a sus clientes. Estos
    implementado chatbots basados en LLM para facilitar el acceso         chatbots son capaces de acceder a los datos transaccionales de
    de sus empleados a políticas, procedimientos e información            los usuarios en tiempo real y responder a consultas específicas,
    relevante de la compañía. Estos asistentes conversacionales           como «¿Cómo han sido mis gastos en el último mes?“ o
    permiten obtener respuestas rápidas y precisas a consultas            «¿Cuánto he ganado en intereses por mis depósitos en el último
    frecuentes, mejorando la eficiencia y reduciendo la carga sobre       año?“.
    otros canales de soporte interno.
                                                                       4 Asistencia en la redacción de informes de auditoría: las
 4 Extracción de información: los LLM están siendo utilizados             funciones de Auditoría Interna de algunas compañías ya están
    para extraer automáticamente datos clave de documentos                utilizando LLM para agilizar la elaboración de sus informes.
    extensos y complejos, como memorias anuales o informes de             Estas herramientas toman como inputs los hallazgos del
    riesgo climático. Estas herramientas son capaces de procesar          auditor, una base de datos con informes previos y otra con la
    archivos PDF de miles de páginas, con estructuras                     normativa aplicable, tanto interna como externa. A partir de
    heterogéneas que incluyen imágenes, gráficos y tablas, y              esta información, los LLM generan un borrador avanzado del
    transformar la información relevante en formatos                      informe de auditoría, adoptando el tono, vocabulario y estilo
    estructurados y accesibles, como tablas ordenadas. Esta               de los auditores, y citando adecuadamente informes anteriores
    automatización permite a las empresas ahorrar tiempo y                y regulaciones relevantes. Esto permite a los auditores ahorrar
    recursos en tareas de análisis documental.                            tiempo significativo en tareas de redacción y centrarse en
                                                                          actividades de mayor valor añadido.
 4 Asistencia en centros de atención al cliente: algunos contact
    centers están aprovechando los LLM para mejorar la calidad y      Estos ejemplos ilustran cómo los LLM están creando valor real en
    eficiencia del servicio. Aplicando técnicas de transcripción y    diversas funciones empresariales, desde la optimización de
    resumen, estas herramientas generan un contexto de las            procesos internos hasta la mejora de la experiencia del cliente. Si
    interacciones previas de cada cliente, permitiendo a los          bien actualmente el número de casos de uso en producción es
    agentes ofrecer una atención más personalizada. Además,           limitado, se espera que esta tendencia se acelere muy rápidamente
                                                                      en el futuro próximo, a medida que los LLM sigan evolucionando y
    durante las llamadas en curso, los LLM pueden proporcionar a
                                                                      se aborden de manera efectiva los desafíos relacionados con la
    los agentes acceso en tiempo real a documentación relevante
                                                                      privacidad y la seguridad de los datos.
    para responder las consultas específicas de los clientes, como
    información sobre comisiones bancarias o instrucciones para
    bloquear tarjetas de crédito.
                                                                                                                                             19
                                                                           Principales usos                                                  3. Interacción y automatización
                                                                                                                                                  4 Chatbots: simulación de conversaciones sobre temas
                                                                           Los LLM están encontrando aplicaciones en una multitud de                 generales o específicos.
                                                                           dominios, transformando sustancialmente la forma en que las            4 Q&A: generación de respuestas a preguntas basadas
                                                                           personas interactúan con la tecnología y aprovechado el                   en un corpus.
                                                                           procesamiento de lenguaje natural para mejorar procesos,
                                                                           servicios y experiencias.                                         Estos usos resumen las aplicaciones actuales de los LLM de
                                                                                                                                             texto. Con la emergencia de los LLM multimodales, comienzan
                                                                           A continuación, se resumen algunos de los usos más destacados     a aflorar aplicaciones adicionales como la generación de
                                                                           de los LLM de texto.                                              contenido audiovisual, la interpretación de datos a partir de
                                                                                                                                             imágenes, la traducción de contenido multimedia o la creación
                                                                           1. Creación y mejora de contenido                                 de experiencias interactivas enriquecidas, como la interacción
                                                                                 4 Generación de contenido: producción automática de         con chatbots con entradas no solo de texto, sino también de
                                                                                    texto.                                                   imagen, audio y vídeo.
                                                                                 4 Asistencia de escritura: corrección ortotipográfica, de
                                                                                    estilo y de contenido.
                                                                                 4 Traducción automática: conversión de texto de un          Requisitos regulatorios
                                                                                    idioma a otro.
                                                                                 4 Resumen de textos: reducción de documentos                La rápida evolución de la inteligencia artificial generativa,
                                                                                    extensos a resúmenes.                                    especialmente en el campo de los modelos de lenguaje de gran
                                                                                 4 Planificación y guion de contenidos: estructuración de    escala (LLM), ha captado la atención de reguladores a nivel
                                                                                    contenidos, p. ej., índices.                             global. El potencial de estos sistemas para influir de forma
                                                                                 4 Brainstorming: propuestas creativas para proyectos,       negativa en los ciudadanos ha llevado a un incremento en las
                                                                                    nombres, conceptos, etc.                                 iniciativas para establecer marcos regulatorios que aseguren su
                                                                                 4 Programación: creación de código de programación a        desarrollo y uso responsable.
                                                                                    partir de lenguaje natural.
                                                                                                                                             Algunas de las principales iniciativas regulatorias sobre IA son:
                                                                           2. Análisis y organización de información




MANAGEMENT SOLUTIONS
                                                                                4 Análisis de sentimientos: evaluación de emociones y        4 El AI Act de la Unión Europea: propuesta legislativa
                                                                                    opiniones en textos.                                       pionera para regular la IA, que clasifica los sistemas de IA
                                                                                4 Extracción de información: extracción de datos               según su nivel de riesgo y establece requisitos de
                                                                                    específicos de documentos extensos.                        transparencia, seguridad y derechos fundamentales. El AI
                                                                                4 Clasificación de textos: organización de textos en           Act fue aprobado por el Parlamento Europeo el 13 de marzo
                                                                                    categorías o temas específicos.                            de 2024.
                                                                                4 Revisión técnica: asistencia en revisar documentos
20                                                                                                                                           4 El AI Bill of Rights de Estados Unidos: documento
                                                                                    especializados (p. ej., legales).
                                                                                                                                               orientativo que busca proteger los derechos civiles en el




El auge de los large language models: de los fundamentos a la aplicación
                                                                                                                                               desarrollo y aplicación de la IA, enfatizando la privacidad, la
                                                                                                                                               no discriminación y la transparencia.

                                                                                                                                             4 La guía sobre IA del NIST35 de Estados Unidos: establece
                                                                                                                                               principios para la creación de sistemas de IA fiables, con
                                                                                                                                               enfoque en la precisión, la explicabilidad y la mitigación de
                                                                                                                                               sesgos.




                                                                                                                                             35
                                                                                                                                                  El Instituto Nacional de Estándares y Tecnología (NIST) ha publicado
                                                                                                                                                  documentos que detallan marcos de ciberseguridad, de gestión de riesgos y,
                                                                                                                                                  concretamente, de gestión de modelos de IA y de IA generativa.

4 La Declaración de Bletchley: compromiso internacional                4 Seguridad y fiabilidad: exigencias de robustez operacional
  para el desarrollo responsable de la IA, promoviendo                   para prevenir disfunciones o manipulaciones que puedan
  principios de transparencia, seguridad y equidad, firmado              causar daño o pérdida de información.
  por múltiples países.
                                                                       4 Responsabilidad y gobernanza: marco de responsabilidad
Además de las iniciativas mencionadas, numerosos países han              de desarrolladores y usuarios de LLM en caso de daños o
comenzado a emitir sus propias regulaciones locales o han                violaciones de derechos, incluyendo mecanismos de
establecido principios para la adopción de la IA de manera ética         supervisión y control.
y segura. Entre ellos se cuentan36 Reino Unido, Francia, España,
Alemania, Países Bajos, Polonia, Australia, Nueva Zelanda,             4 Supervisión humana: la necesidad de mantener una
Singapur, Canadá, Japón, Corea del Sur, China, India, Indonesia,         supervisión humana efectiva sobre los LLM, asegurando que
Israel, Emiratos Árabes Unidos, Arabia Saudí, Egipto, Brasil, Chile,     las decisiones importantes puedan ser revisadas y, si es
Perú, Argentina, México, Colombia y Turquía, entre otros.                necesario, corregidas o revertidas por humanos.

Todas estas iniciativas regulatorias plantean requisitos muy           Estos requisitos reflejan un consenso emergente sobre los
similares sobre la IA que, aplicados a los LLM, se pueden resumir      principios fundamentales para el desarrollo ético y seguro de los
en:                                                                    LLM, y forman la base para futuras regulaciones específicas y
                                                                       adaptaciones según evolucione la tecnología.
4 Transparencia y explicabilidad: obligación de revelar
  cómo funciona el LLM, incluyendo la lógica detrás de sus
  salidas para que sean comprensibles para los usuarios.

4 Privacidad y protección de datos: medidas estrictas para
  proteger la información personal recopilada o generada por
  LLM, cumpliendo con leyes de protección de datos, como
  GDPR en Europa.

4 Equidad y no discriminación: requisitos para prevenir
  sesgos y asegurar que los LLM no perpetúen
  discriminaciones ni prejuicios, mediante la evaluación y
  corrección constantes de sus algoritmos.




                                                                       37                                                                  21
                                                                            IAPP (2024).
                                                                           Desarrollo y despliegue de los LLM




                                                                               “La IA generativa es la clave para resolver algunos de los mayores problemas del
                                                                            mundo, como el cambio climático, la pobreza y las enfermedades. Tiene el potencial de
                                                                                                                   hacer del mundo un lugar mejor para todos“.
                                                                                                                                                   Mark Zuckerberg37




MANAGEMENT SOLUTIONS



22




El auge de los large language models: de los fundamentos a la aplicación
En esta sección se analizan los aspectos clave del proceso de           generar texto coherente y contextualizado. Por ejemplo,
desarrollo y despliegue de LLM. Se examinan los componentes             corpus comunes para el entrenamiento incluyen
principales, como los datos y la arquitectura del modelo, así           BookCorpus39, Gutenberg40, Wikipedia41 o CodeParrot42.
como las etapas de preentrenamiento, fine-tuning e
implementación. Además, se discuten los principales retos y        4 Propiedad intelectual y derechos de autor43: la extracción y
consideraciones que deben tenerse en cuenta para garantizar          uso de datos de internet para entrenar LLM plantea desafíos
un desarrollo ético, robusto y alineado con los objetivos de una     relacionados con la propiedad intelectual y los derechos de
organización.                                                        autor. Muchos de estos datos están protegidos por derechos
                                                                     de autor, y su uso sin permiso o compensación adecuada
                                                                     puede ser problemático. El AI Act en Europa aborda este
Aspectos clave en el desarrollo de los LLM                           tema imponiendo nuevos requisitos a los desarrolladores de
                                                                     LLM, como la obligación de revelar las fuentes de datos
El desarrollo de un LLM es un proceso complejo que implica           utilizadas y obtener las licencias necesarias.
múltiples componentes y decisiones críticas. A continuación, se
describen los principales componentes que es necesario             4 Calidad y representatividad de los datos44: como cualquier
conocer sobre el desarrollo de los LLM y algunos aspectos clave      modelo, un LLM será tan bueno como los datos utilizados en
sobre ellos.                                                         su entrenamiento. Si los datos son de baja calidad, sesgados
                                                                     o no representativos, el modelo puede heredar estos
Datos                                                                problemas y generar resultados inexactos, injustos o                             23
                                                                     inapropiados. Por lo tanto, es crucial asegurar que los corpus
Los datos son el fundamento sobre el cual se construyen los          de entrenamiento sean diversos, equilibrados y representen
LLM, y su calidad, diversidad y representatividad tienen un          adecuadamente los diferentes grupos demográficos457,
impacto directo en el rendimiento y los sesgos del modelo            opiniones y perspectivas.
resultante. Abordar los desafíos relacionados con la propiedad
intelectual, la calidad de los datos y el preprocesamiento es      4 Iniciativas de datos de alta calidad46: algunas iniciativas
esencial para desarrollar LLM robustos, no sesgados y precisos.      recientes se centran en construir LLM con menos
A medida que evolucionan las regulaciones y las mejores              parámetros, pero datos de mayor calidad, como corpus de
prácticas en este campo, es probable que se observe un mayor         entrenamiento más pequeños, pero cuidadosamente
énfasis en el uso responsable y transparente de los datos en el      seleccionados y filtrados47, que incluyen contenido de alta
entrenamiento de LLM.                                                calidad como libros, artículos científicos y publicaciones

Algunos aspectos clave sobre los datos de entrenamiento de un
LLM son:
                                                                   37
                                                                      Mark Zuckerberg (n. 1984), cofundador y CEO de Facebook y de Meta, una de las
4 Corpus de entrenamiento38: los LLM se entrenan con                  mayores compañías de redes sociales, tecnología e inteligencia artificial del
                                                                      mundo.
  grandes corpus de datos, a menudo extraídos de internet,         38
                                                                      Liu (2024).
                                                                   39
  que incluyen billones de palabras y abarcan una amplia              Soskek (2019).
                                                                   40
                                                                      Project Gutenberg (2024).
  gama de dominios y géneros, como libros, artículos de            41
                                                                      Wikipedia Dumps (2024).
  noticias, páginas web, redes sociales y más. Estos corpus        42
                                                                      Hugging Face Datasets (2024).
                                                                   43
  masivos permiten a los LLM aprender patrones y                   44
                                                                      Li (2024), Chu (2023).
                                                                      Alabdulmohsin (2024).
  representaciones del lenguaje a gran escala, lo que les          45
                                                                      Yogarajan (2023).
  otorga una capacidad sin precedentes para comprender y           46
                                                                      Sachdeva (2024).
                                                                   47
                                                                      Tirumala (2023).
                                                                            Fig. 5. Etapas del procesamiento de datos de entrada a un LLM.




                                                                              respetadas. Por ejemplo, estos filtros pueden limitarse a un       4 Existen distintos algoritmos de encoding en el mercado52
                                                                              único idioma, o a un sector o temática, lo que reduce                que se diferencian en la manera en la que dividen el texto
                                                                              drásticamente el tamaño del corpus. Esta estrategia puede            en función de palabras, frases u oraciones, uso de espacios,
                                                                              resultar en LLM con mejor rendimiento y menos sesgos que             mayúsculas o formatos, aparición de caracteres en distintos
                                                                              los modelos entrenados en datos masivos no filtrados.                idiomas, o errores presentes en el texto.

                                                                           4 Preprocesamiento y etiquetado de datos48: antes de                  4 Los principales encodings53 usados son BytePairEncoding,
                                                                             entrenar o fine-tunear un LLM, los datos deben ser                    SentencePieceEncoding y WordPieceEncoding.




MANAGEMENT SOLUTIONS
                                                                             preprocesados y, en algunos casos, como el fine-tuning
                                                                             supervisado o el uso de un conjunto de datos específico,            El resultado de la tokenización se emplea como punto de
                                                                             etiquetados. El preprocesamiento implica limpiar y                  partida en el modelo de embedding.
                                                                             formatear los datos49, eliminar el ruido y los errores, y aplicar
                                                                             técnicas como la tokenización y la normalización (p. ej.,
                                                                                                                                                 Embedding
                                                                             LayerNorm50 para Transformers).
                                                                                                                                                 Los embeddings son representaciones numéricas de palabras,
24                                                                         Tokenización y encoding                                               frases, oraciones o incluso párrafos que capturan su significado
                                                                                                                                                 semántico y las relaciones entre ellos. Para ello, parten del




El auge de los large language models: de los fundamentos a la aplicación
                                                                           La tokenización se refiere al proceso de dividir un texto en          corpus de entrada del LLM dividido en tokens. Son un
                                                                           unidades más pequeñas llamadas ”tokens“, que son las                  componente fundamental de los LLM y desempeñan un papel
                                                                           unidades procesadas por el LLM durante el entrenamiento y la          crucial tanto en el preentrenamiento como en el fine-tuning y el
                                                                           inferencia de respuestas. Estos tokens pueden ser palabras,           uso posterior de estos modelos.
                                                                           partes de una palabra (p. ej., lemas) o caracteres. Por ejemplo,
                                                                           una de las formas más sencillas de generar tokens es separar el       Los embeddings en los LLM:
                                                                           corpus según los espacios entre palabras. El encoding es el
                                                                           proceso de representar esas unidades de texto en forma                4 Están diseñados para capturar las relaciones semánticas
                                                                           numérica para que pueda ser procesado por el modelo.                    entre las palabras, de manera que palabras con significados
                                                                                                                                                   similares tengan vectores similares. Esto permite al modelo
                                                                           Algunos puntos clave sobre la tokenización en los LLM:                  comprender la similitud y las analogías entre palabras y
                                                                                                                                                   conceptos.
                                                                           4 Se realiza partiendo del corpus de textos disponible, con
                                                                             objeto de dividir el texto de partida en unidades más
                                                                             pequeñas de forma óptima. El resultado final de la
                                                                             tokenización es un encoding.

                                                                           4 Los encodings impactan de forma significativa en el
                                                                             rendimiento del LLM51, ya que definen la mínima unidad de
                                                                                                                                                 48
                                                                             procesamiento que van a recibir y determinan el                        Chen (2023).
                                                                                                                                                 49
                                                                                                                                                    Wenzek (2019), Penedo (2023).
                                                                             vocabulario al que tiene acceso el LLM.                             50
                                                                                                                                                    Zhao (2023).
                                                                                                                                                 51
                                                                                                                                                    Rejeleene (2024).
                                                                                                                                                 52
                                                                                                                                                    Minaee (2024).
                                                                                                                                                 53
                                                                                                                                                    Kudo (2018).
4 No son valores universales, sino que varían entre distintos     Tipologías de embeddings
  modelos en función del espacio vectorial en el que se hayan
  definido.
                                                                  Los embeddings se utilizan en los LLM para poder establecer
                                                                  una métrica que defina la similitud entre los significados de las
4 Son contextuales, lo que significa que la representación de     palabras y para incorporar información sobre la posición de las
  una palabra puede variar según el contexto en el que            palabras en una oración. Esto es crucial, ya que el orden de las
                                                                  palabras afecta al significado. Existen tres tipos principales de
  aparece. Esto permite capturar matices de significado y
                                                                  embeddings posicionales:
  desambiguar palabras polisémicas. No están predefinidos,
  sino que se aprenden a partir de los datos de entrenamiento         4 Embedding posicional absoluto1: asigna a cada palabra –o a
                                                                         cada unidad mínima de texto o token– un vector que
  partiendo del modelo de embeddings del LLM. Durante el                 representa su posición exacta en la oración (p. ej., primera,
  preentrenamiento, el modelo ajusta los embeddings para                 segunda, tercera posición, etc.).
  maximizar su capacidad de predecir palabras en contexto
                                                                      4 Embedding posicional relativo2: en lugar de basarse en
  (p. ej., a través de marcos de embeddings como                         posiciones absolutas, representa la posición de una palabra
  SentenceTransformers). No obstante, los embeddings por sí              en relación con las demás (p. ej., dos palabras antes, una
  solos ya son un modelo que es necesario ajustar durante el             palabra después, etc.).
  proceso.                                                            4 Embedding posicional rotatorio3: combina la información de
                                                                         posiciones absolutas y relativas, utilizando funciones
                                                                         trigonométricas para crear representaciones vectoriales
Preentrenamiento                                                         más complejas.

El preentrenamiento es una etapa fundamental en el desarrollo     En un transformer, un embedding posicional simple para una
de LLM, durante la cual los modelos adquieren un conocimiento     palabra en una posición dada se puede representar
                                                                  matemáticamente usando funciones seno y coseno. En
general y profundo del lenguaje a partir de grandes cantidades    concreto, un embedding posicional E para un token i con
de datos no etiquetados. Aunque este proceso es                   posición P se puede representar matemáticamente en su forma
computacionalmente intensivo y costoso, permite la                más sencilla como:
adaptación del modelo a una amplia gama de tareas.

El objetivo principal del preentrenamiento es que el modelo
adquiera un conocimiento amplio y profundo del lenguaje,
incluyendo su estructura, semántica, sintaxis y contexto.
Durante este proceso, el LLM aprende a predecir palabras o
fragmentos de texto (i.e., tokens) basándose en el contexto
circundante, lo que le permite capturar relaciones y patrones
lingüísticos complejos. Este conocimiento general se convierte
                                                                  donde P es la posición del token en la secuencia de entrada, y d
en la base sobre la cual el modelo puede ser adaptado             es la dimensión de capas ocultas del transformer.
posteriormente para tareas específicas mediante el fine-tuning.
                                                                  La elección del tipo de embedding posicional puede afectar al          25
                                                                  rendimiento del LLM, ya que determina la cantidad y el tipo de
Existen varias técnicas populares para el preentrenamiento de     información posicional disponible para el modelo durante el
LLM, como:                                                        entrenamiento.


4 El modelado autorregresivo de lenguaje o modelado
  unidireccional (p. ej., modelado autorregresivo54), que
  consiste en entrenar el modelo para predecir la siguiente
  palabra o fragmento de texto dado el contexto anterior. Esta
  tarea permite al modelo aprender las probabilidades
  condicionales del lenguaje y generar texto coherente. Son
  ejemplos los modelos GPT y Claude.




                                                                  1
54
     Devlin (2018), Liu (2022).                                    Vaswani (2017).
                                                                  2
                                                                   Shaw (2018).
                                                                  3
                                                                   Su (2021).
                                                                           4 El modelo no autorregresivo55, usado en modelos como             Cuantización
                                                                             Gemini, en los que no se obtiene la respuesta
                                                                             secuencialmente palabra a palabra, sino que se transforma y      Durante el entrenamiento de los LLM, se ajustan los pesos de
                                                                             refina en conjunto.                                              las neuronas para realizar predicciones más precisas. Estos
                                                                                                                                              pesos se almacenan típicamente como números de alta
                                                                           4 El modelado de lenguaje enmascarado56, popularizado por          precisión, lo que puede resultar en modelos de gran tamaño y
                                                                             modelos como BERT, que consiste en enmascarar                    computacionalmente costosos.
                                                                             aleatoriamente algunas palabras en el texto de entrada y
                                                                             entrenar el modelo para predecir estas palabras                  La cuantización postentrenamiento es una técnica62 que
                                                                             enmascaradas basándose en el contexto circundante. Esta          permite reducir la precisión de los parámetros del modelo sin
                                                                             técnica permite un aprendizaje bidireccional y una mejor         afectar significativamente el rendimiento del modelo. Por
                                                                             comprensión del contexto. Algunas arquitecturas de LLM (p.       ejemplo, redes neuronales que almacenen sus parámetros
                                                                             ej., transformers bidireccionales) usan esta técnica.            usando números de coma flotante de 32 bits pueden pasar a
                                                                                                                                              usar únicamente 16 bits u 8 bits dependiendo del tipo de
                                                                           4 El modelado secuencia a secuencia57 (p. ej., seq2seq58), en el   cuantización. Esto resulta en modelos más pequeños y rápidos,
                                                                             que el modelo se entrena para generar secuencias de texto        ya que requieren menos memoria y pueden realizar
                                                                             en función de otras secuencias de entrada. Es usado en           operaciones más eficientemente con el hardware adecuado.
                                                                             modelos como T5, BART o ProphetNET.
                                                                                                                                              Recientemente, ha surgido la tendencia de desarrollar modelos
                                                                           4 El preentrenamiento contrastivo59, utilizado en modelos          de menor tamaño (small language models, SLM), o incluso los
                                                                             como CLIP y ALIGN60, que implica entrenar el modelo para         llamados ”tiny LLM“63, modelos que mantienen un alto
                                                                             identificar pares de texto e imagen que están                    rendimiento a pesar de su tamaño mucho más reducido. Estos
                                                                             semánticamente relacionados, lo que le permite aprender          modelos compactos se logran mediante una combinación de
                                                                             representaciones multimodales y transferir conocimiento          técnicas, entre ellas la cuantización postentrenamiento.
                                                                             entre diferentes modalidades61.
                                                                                                                                              Mediante la aplicación hábil de estas técnicas, los SLM y los tiny
                                                                           El preentrenamiento de LLM es un proceso                           LLM están logrando en algunos casos un rendimiento
                                                                           computacionalmente intensivo que requiere enormes                  comparable al de modelos mucho mayores64, lo que los hace




MANAGEMENT SOLUTIONS
                                                                           cantidades de datos, tiempo y recursos de hardware. Los            atractivos para aplicaciones con restricciones de recursos
                                                                           modelos más grandes pueden tener en torno a 1 billón (1012) de     computacionales o de memoria.
                                                                           parámetros y requerir miles de GPU de gama alta durante
                                                                           semanas o meses de entrenamiento. Esto hace que el
                                                                           preentrenamiento sea extremadamente costoso y solo esté al
                                                                           alcance de unas pocas empresas y organizaciones en el mundo        55
                                                                                                                                                 Xu (2021).
                                                                                                                                              56
                                                                           con los recursos necesarios.                                          Devlin (2019), Sinha (2021).
                                                                                                                                              57
                                                                                                                                                 Lee (2022).
26                                                                                                                                            58
                                                                                                                                                 Sutskever (2014).
                                                                                                                                              59
                                                                                                                                                 Zeng (2023).




El auge de los large language models: de los fundamentos a la aplicación
                                                                                                                                              60
                                                                                                                                                 Jia (2021).
                                                                                                                                              61
                                                                                                                                                 Cui (2022).
                                                                                                                                              62
                                                                                                                                                 Li (2024).
                                                                                                                                              63
                                                                                                                                                 Tian (2024).
                                                                                                                                              64
                                                                                                                                                 Fu (2024).




                                                                            Fig. 6. Fine-tuning de un LLM.
Fine-tuning, instruction-tuning y RAG                              Entrenando LLM: funciones de
                                                                   pérdida
El fine-tuning es el proceso de adaptar un LLM preentrenado a
una tarea específica utilizando un conjunto de datos más           Los LLM, como otros modelos de aprendizaje profundo,
pequeño. Esta técnica permite aprovechar el conocimiento           aprenden ajustando sus parámetros para minimizar una
general adquirido durante el preentrenamiento y especializarlo     función de pérdida. Esta función mide la diferencia entre las
para obtener un alto rendimiento en la tarea objetivo.             predicciones del modelo y los resultados esperados, guiando al
                                                                   modelo hacia un mejor rendimiento.

El objetivo principal del fine-tuning (Fig. 6) es adaptar un LLM   La elección de la función de pérdida depende del tipo de tarea
                                                                   para la que se esté entrenando el LLM. Por ejemplo, para un
preentrenado a una tarea concreta, como la clasificación de        modelo que predice la siguiente palabra en una frase
sentimientos, la respuesta a preguntas, la traducción              (modelado autorregresivo del lenguaje), una función común es
automática o la generación de resúmenes. Durante este              la entropía cruzada. Esta función compara la distribución de
proceso, el modelo aprende a utilizar su conocimiento general      probabilidad de las palabras predichas por el modelo con la
                                                                   distribución real observada en los datos de entrenamiento.
del lenguaje y aplicarlo de manera efectiva al dominio y los
requisitos específicos de la tarea en cuestión. Los LLM            Matemáticamente, la función de pérdida de entropía cruzada
                                                                   para un modelo autorregresivo se puede expresar como una
disponibles en el mercado, sean propietarios o de código
                                                                   suma de los logaritmos negativos de las probabilidades
abierto, típicamente están preentrenados (y por tanto son de       asignadas a las palabras correctas en cada posición de la
propósito general), pero no han recibido fine-tuning, que los      secuencia.
adaptaría a un propósito específico.                               En concreto, dada una función de pérdida como la entropía
                                                                   cruzada, y una tipología de entrenamiento como el modelado
El fine-tuning ofrece varios beneficios significativos:            autorregresivo del lenguaje, se puede definir la función de
                                                                   pérdida a minimizar como:

4 Aprovecha el conocimiento previo: al partir de un modelo
  preentrenado, el fine-tuning permite aprovechar el vasto
  conocimiento general del lenguaje adquirido durante el
  preentrenamiento, lo que acelera el aprendizaje y mejora el
  rendimiento en la tarea específica.                              donde φ representa los parámetros del modelo, i se refiere al
                                                                   número de token en una secuencia determinada con N tokens,
4 Requiere menos datos y recursos: en comparación con el           P es la probabilidad de predecir el token i en función de la
                                                                   secuencia x de tokens anteriores.
  entrenamiento desde cero, el fine-tuning necesita mucha
  menos cantidad de datos etiquetados y recursos                   Durante el ajuste fino (fine-tuning) de los embeddings del
                                                                   modelo, se pueden utilizar funciones de pérdida especializadas
  computacionales, lo que lo hace más accesible y económico        para afinar las representaciones vectoriales de las palabras.
  para una amplia gama de organizaciones y aplicaciones.           Algunas opciones populares incluyen:

                                                                    4 Pérdida por similitud del coseno: ajusta los embeddings
4 Permite la especialización: el fine-tuning permite adaptar           para que palabras similares tengan vectores más parecidos.
  los LLM a dominios y tareas concretas, lo que resulta en                                                                           27

  modelos altamente especializados y efectivos para                 4 Pérdida por error cuadrático medio: minimiza la diferencia
                                                                       cuadrática entre los embeddings predichos y los
  aplicaciones específicas.                                            esperados.

4 Facilita la transferencia de aprendizaje: los modelos fine-       4 Pérdida por ranking de múltiples negativos: asocia los
                                                                       embeddings de palabras relacionadas de manera que estén
  tuned pueden recibir un fine-tuning adicional para tareas            más cerca entre sí que los de palabras no relacionadas.
  relacionadas, lo que permite la transferencia de aprendizaje
                                                                    4 Pérdida por tripletes, de Matryoshka o contrastiva:
  y la creación de modelos aún más especializados con                  variantes más avanzadas que consideran relaciones entre
  relativamente pocos datos adicionales.                               tríos o grupos de embeddings.

                                                                   La selección cuidadosa de la función de pérdida es crucial para
A pesar de sus beneficios, el fine-tuning también presenta         entrenar LLM efectivos y eficientes que puedan capturar los
algunos desafíos:                                                  matices del lenguaje natural.

4 Sobre-especialización65: si el modelo se somete a un fine-
  tuning en un conjunto de datos demasiado específico,
  puede perder parte de su capacidad de generalización y
  funcionar mal con datos desconocidos o ligeramente
  diferentes.




65
     Wang (2024).
                                                                            Fig. 7. Funcionamiento del RAG.




                                                                           4 Olvido catastrófico66: durante el fine-tuning es posible que    4 Parameter efficient73 fine-tuning (PEFT): otros métodos de
                                                                             un modelo olvide conocimientos críticos aprendidos                fine-tuning buscan aumentar su eficiencia y reducir el
                                                                             previamente.                                                      esfuerzo necesario para reentrenar el modelo. Por ejemplo,
                                                                                                                                               las técnicas basadas en LoRA74 (low-rank adaptation) como
                                                                           4 Inestabilidad67: el proceso de fine-tuning puede ser sensible     QLoRA o LongLoRA75, que permiten hacer fine-tuning del
                                                                             a factores como la inicialización de pesos, los                   modelo sin la necesidad de modificar sus pesos y almacenan
                                                                             hiperparámetros y la selección de datos, lo que puede llevar      el conocimiento aprendido durante el proceso de fine-
                                                                             a resultados inconsistentes o variaciones en el rendimiento.      tuning en parámetros adicionales del modelo.




MANAGEMENT SOLUTIONS
                                                                           4 Herencia de sesgos68: los modelos que han recibido fine-        En muchos casos de uso de LLM, no es necesario emplear un
                                                                             tuning pueden heredar y amplificar los sesgos presentes         fine-tuning para mejorar sus capacidades en un dominio
                                                                             tanto en los datos de preentrenamiento como en los datos        específico. La generación aumentada de recuperación76 (RAG) es
                                                                             de fine-tuning, lo que requiere una cuidadosa consideración     una técnica que mejora el rendimiento del LLM a través del uso
                                                                             y mitigación.                                                   de fuentes de conocimiento externas al modelo.

28                                                                         Existen varios tipos de fine-tuning que deben seleccionarse en    Las técnicas de RAG (Fig. 7, funcionan buscando documentos
                                                                           función de cuánto sea necesario modificar el modelo de partida    dentro de una base de datos que se parezcan o refieran al




El auge de los large language models: de los fundamentos a la aplicación
                                                                           para adecuarlo a una tarea en un dominio más específico. Los      prompt de entrada. Esta búsqueda y sus resultados se añaden a
                                                                           principales métodos son:                                          la generación de la respuesta del LLM para enriquecerla,
                                                                                                                                             proporcionando un contexto específico.
                                                                           4 Fine-tuning supervisado69: requiere conjuntos de datos
                                                                             etiquetados de entrada y respuesta del LLM, que se usan
                                                                             para mejorar su respuesta ante tareas específicas. Un
                                                                             método popular de fine-tuning supervisado es el llamado
                                                                             instruction-tuning70, que consiste en alinear las respuestas
                                                                             del modelo a lo esperado por sus usuarios a través de
                                                                             interacciones con el modelo.

                                                                           4 Reinforcement learning: métodos basados en aprendizaje
                                                                             por refuerzo que se centran en mejorar la calidad de la
                                                                             respuesta del LLM, en este caso con base en el feedback de
                                                                             usuario o modelos de recompensa (p. ej., optimización           66
                                                                                                                                                Luo (2024).
                                                                             directa por preferencia71).                                     67
                                                                                                                                                Zhang (2024).
                                                                                                                                             68
                                                                                                                                                Zhang (2024).
                                                                                                                                             69
                                                                           4 Fine-tuning no supervisado72: se trata de un método que no         Ovadia (2024).
                                                                                                                                             70
                                                                                                                                                Zhang (2023).
                                                                             requiere conjuntos de datos etiquetados, sino que se basa       71
                                                                                                                                                Rafailov (2023).
                                                                             en reentrenar el modelo con las mismas metodologías             72
                                                                                                                                                Zhou (2023).
                                                                                                                                             73
                                                                             usadas durante el preentrenamiento (p. ej., predecir el            Xu (2023).
                                                                                                                                             74
                                                                                                                                                Dettmers (2023).
                                                                             siguiente token).                                               75
                                                                                                                                                Chen (2023).
                                                                                                                                             76
                                                                                                                                                Lewis (2020) y Neelakantan (2022).
Implementación y uso                                                 Monitoreo y mantenimiento

Una vez entrenado y validado, el LLM debe desplegarse en un          4 Monitoreo del rendimiento79: una vez implementado, es
entorno de producción para su uso en aplicaciones reales. Esto         esencial monitorear de cerca el rendimiento del LLM en
conlleva la integración del modelo en sistemas y flujos de             condiciones reales. Esto implica realizar un seguimiento de
trabajo existentes, así como la creación de interfaces y APIs para     métricas como la latencia, el rendimiento, la precisión y el
interactuar con él.                                                    uso de recursos, y establecer umbrales en el consumo de
                                                                       recursos y costes, y alertas para detectar y abordar cualquier
Este proceso implica varios aspectos clave, entre los que se           degradación o anomalía.
incluyen aspectos de integración y de monitoreo.
                                                                     4 Actualización y reentrenamiento80: a medida que se
Integración en sistemas y flujos de trabajo                            dispone de nuevos datos o se identifican áreas de mejora,
                                                                       puede ser necesario actualizar o reentrenar el LLM. Esto
4 Infraestructura77: los LLM suelen ser modelos grandes y              requiere un proceso bien definido para recopilar y preparar
  computacionalmente intensivos, por lo que requieren una              nuevos datos, realizar un fine-tuning, y desplegar la versión
  infraestructura robusta para su implementación. Esto puede           actualizada del modelo sin interrupciones en el servicio.         29

  implicar el uso de hardware especializado, como GPU o
  TPU, y plataformas de computación en la nube optimizadas           4 Gestión de versiones81: con las actualizaciones y mejoras
  para realizar eficientemente el proceso de inferencia.               continuas, es importante mantener un control de versiones
                                                                       riguroso del LLM y sus componentes asociados. Esto facilita
4 Interfaces y API78: para facilitar el uso del LLM en                 la reproducibilidad, el debugging y la capacidad de revertir a
  aplicaciones y servicios, es necesario desarrollar interfaces y      versiones anteriores si es necesario.
  API que permitan a otros sistemas interactuar con el
  modelo de manera eficiente y segura. Esto puede incluir            Como se puede apreciar, el desarrollo y despliegue de LLM es
  endpoints, bibliotecas de cliente en varios lenguajes de           un proceso complejo y multifacético que requiere una
  programación e interfaces gráficas de usuario para usuarios        cuidadosa consideración de múltiples aspectos, desde la
  no técnicos.                                                       selección y preparación de los datos hasta la implementación y
                                                                     el uso responsable del modelo. Una comprensión profunda de
4 Integración con otros componentes: en muchos casos, los            los componentes clave, como el preentrenamiento, el fine-
  LLM forman parte de un sistema más amplio que incluye              tuning y los embeddings, así como la conciencia de los desafíos y
  otros componentes, como bases de datos, servicios de               riesgos asociados, es esencial para aprovechar todo el potencial
  procesamiento de lenguaje natural y aplicaciones de                de los LLM de manera ética, sostenible y rentable, así como
  usuario final. La integración fluida y eficiente del LLM con       alineada con los objetivos de cada organización.
  estos componentes es crucial para garantizar un
  rendimiento y una experiencia de usuario óptimos.

                                                                     77
                                                                        Wan (2024).
                                                                     78
                                                                        Abhyankar (2024).
                                                                     79
                                                                        Goyal (2024).
                                                                     80
                                                                        Lester (2021).
                                                                     81
                                                                        Banerjee (2023).
                                                                           Arquitectura de los LLM                                               Los transformers también introducen el concepto de atención
                                                                                                                                                 multi-cabezal (multi-head attention), donde múltiples
                                                                           La arquitectura de los LLM se refiere a la estructura y               mecanismos de atención operan en paralelo, lo que permite al
                                                                           organización de las redes neuronales que componen estos               modelo capturar diferentes tipos de relaciones y patrones en
                                                                           modelos. La elección de la arquitectura y sus componentes             los datos.
                                                                           tiene un impacto significativo en el rendimiento, la eficiencia y
                                                                           las capacidades del LLM. Esta sección explorará las principales       La arquitectura del transformer ha demostrado un rendimiento
                                                                           arquitecturas utilizadas en los LLM y sus características, ventajas   excepcional en una amplia gama de tareas de procesamiento
                                                                           y limitaciones.                                                       del lenguaje natural, y ha sido adoptada por la mayoría de los
                                                                                                                                                 LLM considerados de referencia.
                                                                           Transformers: el estado del arte en LLM
                                                                                                                                                 Variantes y extensiones de los transformers
                                                                           Los transformers, introducidos82 en 2017, se han convertido en la
                                                                           arquitectura dominante para los LLM. A diferencia de las              Desde la introducción de los transformers, se han propuesto
                                                                           arquitecturas anteriores basadas en redes neuronales                  numerosas variantes y extensiones para mejorar su eficiencia,
                                                                           recurrentes (RNN) o redes neuronales convolucionales (CNN),           escalabilidad y capacidad de modelado.
                                                                           los transformers se basan únicamente en mecanismos de
                                                                           atención para procesar y generar secuencias de texto (Fig. 8).        4 Una variante popular es el transformer bidireccional, que
                                                                                                                                                   permite al modelo atender tanto al contexto izquierdo
                                                                           La arquitectura del transformer consta de dos componentes               como al derecho de cada token. Esto se logra mediante el
                                                                           principales: el codificador (encoder) y el decodificador (decoder),     uso de un objetivo de preentrenamiento de modelado de
                                                                           y existen transformers con solo codificador, solo decodificador o       lenguaje enmascarado (MLM), donde algunos tokens se
                                                                           con ambos componentes. El codificador procesa la secuencia de           enmascaran aleatoriamente y el modelo debe predecirlos
                                                                           entrada y genera una representación contextual para cada                basándose en el contexto circundante.
                                                                           token, mientras que el decodificador genera la secuencia de
                                                                           salida a partir de la representación del codificador y las            4 Otra variante es el transformer generativo, como GPT, que
                                                                           predicciones anteriores.                                                utiliza un enfoque de modelado de lenguaje unidireccional.
                                                                                                                                                   Esto permite generar texto de manera eficiente y




MANAGEMENT SOLUTIONS
                                                                           La clave de los transformers es el mecanismo de atención, que           coherente, ya que el modelo solo puede atender al
                                                                           permite al modelo poner atención en diferentes partes de la             contexto izquierdo de cada token.
                                                                           secuencia de entrada (atención del codificador) y en las
                                                                           predicciones anteriores (atención del decodificador) para             4 También se han propuesto extensiones para hacer que los
                                                                           generar la siguiente palabra o token. Esto permite capturar             Transformers sean más eficientes y escalables, como el
                                                                           dependencias a largo plazo y generar secuencias coherentes.             transformer disperso (sparse transformer), que utiliza

30
                                                                                                                                                 82
                                                                                                                                                      Vaswani (2017).




El auge de los large language models: de los fundamentos a la aplicación
                                                                            Fig. 8. Funcionamiento de un transformer.




                                                                                                                                                                   1 Consulta de entrada al modelo
                                                                                                                                                                   2 Las entradas se dividen en unidades (fichas).
                                                                                                                                                                   3 El modelo de incrustación procesa y asigna representaciones
                                                                                                                                                                        numéricas a cada token.
                                                                                                                                                                   4 Se añade información posicional para que el modelo
                                                                                                                                                                        comprenda las relaciones entre las palabras y el contexto.
                                                                                                                                                                   5 El codificador utiliza la autoatención para averiguar qué
                                                                                                                                                                     palabras son importantes y cómo se relacionan entre sí,
                                                                                                                                                                     procesando en paralelo los datos en N capas.
                                                                                                                                                                   6 El decodificador tiene en cuenta el contexto previo y las
                                                                                                                                                                     partes traducidas utilizando la atención.
                                                                                                                                                                   7 El decodificador toma la información traducida del
                                                                                                                                                                     codificador y genera una nueva respuesta.
                                                                                                                                                                   8 La respuesta se invierte y se presenta de forma coherente.
Prompt engineering en los LLM: principios y mejores prácticas

Prompt engineering se refiere al proceso de diseñar y optimizar los        4 Aprovechar conocimiento externo: proporcionar información
prompts (entradas de texto) para obtener los mejores resultados               adicional permite complementar la base de conocimientos del
posibles de los LLM. Esta disciplina emergente contiene una serie             LLM. Por ejemplo, para responder preguntas sobre una
de principios y mejores prácticas que permiten aprovechar al                  industria específica, se podrían primero recuperar informes
máximo las capacidades de estos modelos. Entre ellos:                         sectoriales relevantes y pasarlos al modelo.
 4 Ser claro y específico: las instrucciones dadas al modelo deben         4 Iterar y refinar sistemáticamente: la evaluación continua del
    indicar de forma explícita el formato, la longitud y el nivel de          rendimiento del modelo permite identificar áreas de mejora y
    detalle esperado en la respuesta. Por ejemplo, en lugar de                ajustar los prompts en consecuencia. Métricas cuantitativas y
    simplemente pedir ”Analiza la situación financiera de la                  juicios cualitativos de expertos del dominio pueden guiar este
    empresa X“, es mejor dar una instrucción como ”Escribe un                 proceso iterativo.
    informe de 1000 palabras sobre la situación financiera de la
    empresa X, cubriendo su rentabilidad, liquidez, solvencia y        Mediante la aplicación de estos principios de prompt engineering, se
    perspectivas futuras“.                                             demuestra estadísticamente que los LLM proporcionan un
                                                                       resultado más preciso y fiable.
 4 Descomponer tareas complejas: conviene dividir los problemas
    en subtareas más manejables para los LLM. Por ejemplo, en          Considerando todo esto, un mal prompt para que un LLM escriba
    lugar de pedir ”Desarrolla un plan estratégico para la empresa     una columna sobre prompt engineering sería: ”Escribe un artículo
    Y“, se pueden solicitar subtareas como ”Realiza un análisis        sobre prompt engineering“.
    DAFO de la empresa Y“, ”Define los objetivos estratégicos
    clave para Y“, ”Propón iniciativas para alcanzar cada objetivo“,   Y un buen prompt para escribir esa columna sería:
    etc.                                                                   ”Actúa como un experto en inteligencia artificial y escribe una
 4 Proporcionar ejemplos ilustrativos (few-shot learning): unos            columna de divulgación de 600 palabras sobre los principios clave
    pocos ejemplos bien elegidos pueden ayudar enormemente a               del prompt engineering para obtener los mejores resultados de los
                                                                           LLM. Estructura la columna con una introducción breve y
    comunicar la tarea deseada. Supongamos que se quiere generar
                                                                           atractiva, 4-5 párrafos cubriendo los puntos principales (ser
    propuestas de valor para productos; se podrían dar dos
                                                                           específico, descomponer tareas, dar ejemplos...), y una conclusión
    ejemplos: ”Nuestro software CRM permite a los equipos de
                                                                           con los beneficios de aplicar estas técnicas. Utiliza un tono
    ventas cerrar acuerdos un 50% más rápido“ y ”Nuestra app de            divulgativo pero riguroso, apto para un público empresarial.
    bienestar ayuda a los empleados a reducir el estrés y aumentar         Incluye ejemplos concretos para ilustrar las ideas“.
    su productividad en un 25%“.
                                                                       Fuentes: Guía de prompt engineering de OpenAI1, soporte de
 4 Solicitar razonamiento paso a paso: instruir al LLM para que        Anthropic Claude Opus y elaboración propia.
    verbalice su proceso de pensamiento a menudo conduce a
    resultados más robustos. Esto es especialmente útil para tareas
    de análisis o solución de problemas en el ámbito empresarial.
    Por ejemplo: ”Describe paso a paso cómo calcularías el ROI de
    este proyecto de inversión“.

 4 Solicitar las referencias empleadas: instruir al LLM para que
    indique en su proceso de razonamiento las referencias a
    documentos que ha empleado, incluyendo citas del texto
    original al que tiene acceso.                                                                                                               31

 4 Pedir al LLM que adopte un personaje: antes de la tarea
    principal, se puede primero instruir al modelo para que adopte
    un determinado rol, tono o estilo. Por ejemplo: ”Actúa como un
    experto analista financiero y proporciona una valoración
    objetiva de la empresa X“. Esto ayuda a orientar su
    comportamiento.




                                                                       1
                                                                           OpenAI (2024).
                                                                              atención dispersa para reducir la complejidad                   escalabilidad, la interpretabilidad y la eficiencia de estos
                                                                              computacional, y el transformer comprimido (compressed          modelos. A medida que la investigación avance, es probable
                                                                              transformer), que utiliza técnicas de compresión para reducir   que aparezcan nuevas arquitecturas y técnicas que superen
                                                                              el tamaño del modelo.                                           estas limitaciones y lleven a los LLM a nuevas cotas de
                                                                                                                                              rendimiento y capacidad.
                                                                           Comparación con arquitecturas anteriores
                                                                           Antes de los transformers, las arquitecturas dominantes para el    LLMOps
                                                                           modelado de secuencias eran las redes neuronales recurrentes
                                                                           (RNN), como Long Short-Term Memory (LSTM) y Gated Recurrent        MLOps (Machine Learning Operations) es una metodología y
                                                                           Unit (GRU), y las redes neuronales convolucionales (CNN).          conjunto de prácticas diseñadas para gestionar el ciclo de vida
                                                                                                                                              completo de los modelos de machine learning, desde el
                                                                           4 Las RNN pueden capturar dependencias a largo plazo en las        desarrollo y entrenamiento hasta la implementación y
                                                                             secuencias, pero sufren de problemas como el                     mantenimiento en producción.
                                                                             desvanecimiento del gradiente (vanishing gradient) y la
                                                                             dificultad para paralelizar el entrenamiento. Además, las        En los últimos años, ha surgido una adaptación de la
                                                                             RNN tienen dificultades para capturar dependencias muy           metodología MLOps específicamente orientada a los LLM,
                                                                             largas debido a su naturaleza secuencial y al uso de             conocida como LLMOps (Large Language Model Operations).
                                                                             recurrencias de alcance constante.                               Esta disciplina se centra en gestionar de manera eficiente el
                                                                                                                                              ciclo de vida completo de los LLM, abarcando desde su
                                                                           4 Las CNN pueden capturar patrones locales en las secuencias       desarrollo y entrenamiento hasta su implementación y
                                                                             y son eficientes en términos de computación, pero tienen         mantenimiento en entornos de producción.
                                                                             dificultades para modelar dependencias a largo plazo y
                                                                             requieren un tamaño de contexto fijo.                            LLMOps integra los procesos tradicionales de desarrollo de
                                                                                                                                              software con herramientas y técnicas diseñadas para abordar
                                                                           En comparación, los transformers superan estas limitaciones al     los desafíos únicos que presentan los modelos de lenguaje de
                                                                           utilizar mecanismos de atención que pueden capturar                gran escala. Algunos de estos desafíos incluyen:
                                                                           dependencias a largo plazo de manera eficiente y paralela.




MANAGEMENT SOLUTIONS
                                                                           Además, los transformers son más flexibles en términos de          4 Gestión de grandes volúmenes de datos: los LLM
                                                                           manejo de secuencias de longitud variable y pueden ser               requieren cantidades masivas de datos de entrenamiento,
                                                                           preentrenados en grandes cantidades de datos no etiquetados.         lo que implica la necesidad de infraestructuras de
                                                                                                                                                almacenamiento y procesamiento escalables y eficientes.
                                                                           La arquitectura de los transformers ha revolucionado el campo
                                                                           de los LLM y ha permitido avances significativos en una amplia     4 Escalado de recursos computacionales: el entrenamiento
                                                                           gama de tareas de procesamiento del lenguaje natural. Sin            y la inferencia de LLM demandan enormes recursos de
32                                                                         embargo, aún quedan desafíos por abordar, como la                    cómputo, haciendo necesario el uso de técnicas de




El auge de los large language models: de los fundamentos a la aplicación
   paralelización y distribución, así como la optimización del      Sesgos, alucinaciones y confiabilidad
   uso de hardware especializado como GPU y TPU.
                                                                    Uno de los mayores retos de los LLM es la presencia de sesgos y
4 Monitorización y mantenimiento: una vez desplegados en            alucinaciones en sus resultados y predicciones. Los sesgos
  producción, los LLM deben ser monitorizados de cerca para         pueden surgir de varias fuentes, como la parcialidad en los
  detectar y corregir problemas de rendimiento, sesgos,             datos de entrenamiento, las limitaciones de las arquitecturas de
  riesgos como las alucinaciones, y la degradación del modelo       los modelos o los prejuicios humanos implícitos en las tareas de
  a lo largo del tiempo.                                            anotación y evaluación. Por otro lado, las alucinaciones se
                                                                    refieren a la generación de información o contenido que parece
4 Versionado y reproducibilidad: dado el tamaño y                   plausible pero que no se basa en hechos reales o en el
  complejidad de los LLM, es crucial mantener un riguroso           conocimiento adquirido durante el entrenamiento.
  control de versiones y maximizar la reproducibilidad de los
  experimentos y resultados.                                        Los sesgos en los LLM pueden manifestarse de diversas
                                                                    maneras, como la perpetuación de estereotipos de género, raza
Para abordar estos desafíos, LLMOps se apoya en una serie de        o edad, la discriminación en tareas de clasificación o la
herramientas y frameworks específicos, como MLFlow83,               generación de contenido ofensivo o inapropiado. Estos sesgos        33
CometML84 y Weights & Biases85. Estas plataformas ofrecen           pueden tener consecuencias graves, especialmente cuando los
funcionalidades para el seguimiento de experimentos, gestión        LLM se utilizan en aplicaciones sensibles como la toma de
de modelos, monitorización del rendimiento y colaboración           decisiones en el ámbito legal, financiero o médico. Por su parte,
entre equipos.                                                      las alucinaciones pueden llevar a la difusión de información
                                                                    errónea o engañosa, lo que puede tener un impacto negativo
Además, LLMOps promueve prácticas como la automatización            en la confianza de los usuarios y en la credibilidad de las
de procesos, el testing continuo, la documentación exhaustiva y     aplicaciones basadas en LLM.
la gobernanza de modelos. Esto permite no solo mejorar la
eficiencia y calidad del desarrollo de los LLM, sino también        Para abordar el reto de los sesgos, es necesario desarrollar
garantizar su uso ético y responsable.                              técnicas robustas para detectar, medir y mitigar su presencia en
                                                                    los LLM. Esto implica la creación de conjuntos de datos de
                                                                    evaluación específicos para sesgos, el uso de métricas de
Retos                                                               equidad y la aplicación de técnicas de eliminación de sesgos
                                                                    (debiasing) tanto en el preentrenamiento como en el fine-tuning.
El desarrollo y despliegue de LLM presenta una serie de retos       Además, es crucial establecer procesos de auditoría y monitoreo
significativos que deben abordarse para garantizar su uso           continuo para garantizar que los LLM sigan siendo imparciales a
responsable, ético y seguro. Esta sección explorará varios de los   lo largo del tiempo.
principales desafíos para las organizaciones en su despliegue y
uso de los LLM.



                                                                    83
                                                                         Zaharia (2018).
                                                                    84
                                                                         CommetML: https://www.comet.com/
                                                                    85
                                                                         Weights and biases: https://wandb.ai/site
                                                                           Para abordar las alucinaciones en los LLM, se están                 Además, es importante establecer marcos de accountability
                                                                           desarrollando diversos métodos centrados en la mejora de los        claros que definan las responsabilidades de los desarrolladores,
                                                                           datos de entrenamiento, la aplicación de técnicas de                implementadores y usuarios de los LLM, como en Europa
                                                                           regularización robustas y el uso de retroalimentación humana        propone el AI Act. Esto puede implicar la creación de
                                                                           para ajustar las respuestas del modelo. Además, se están            estándares y directrices para el desarrollo ético de los LLM,
                                                                           investigando cambios arquitectónicos en los modelos para            mecanismos de supervisión y auditoría externa, y canales para
                                                                           hacerlos inherentemente menos propensos a alucinar. Los             que las partes interesadas planteen inquietudes.
                                                                           métodos de generación de texto y el contexto de entrada




MANAGEMENT SOLUTIONS
                                                                           también pueden ser optimizados para reducir las alucinaciones.      Confidencialidad y protección de la información
                                                                           La supervisión humana y la evaluación rigurosa son esenciales
                                                                           para detectar y corregir información inexacta. Asimismo, el         Los LLM a menudo se entrenan con grandes cantidades de
                                                                           desarrollo de herramientas específicas, como modelos de             datos que pueden contener información personal, sensible o
                                                                           evaluación de alucinaciones y técnicas de ofuscación, puede         confidencial. Además, cuando se despliegan en aplicaciones del
                                                                           contribuir a mejorar la precisión de los LLM.                       mundo real, estos modelos pueden estar expuestos a entradas
                                                                                                                                               de usuario que también pueden incluir datos privados.
34
                                                                           Explicabilidad y accountability
                                                                                                                                               Esto plantea importantes desafíos de privacidad y seguridad, ya




El auge de los large language models: de los fundamentos a la aplicación
                                                                           Otro gran desafío de los LLM es su opacidad y falta de              que los LLM pueden memorizar y reproducir información
                                                                           explicabilidad. Debido a su complejidad y a la naturaleza de sus    confidencial de sus datos de entrenamiento, o ser vulnerables a
                                                                           arquitecturas, es difícil entender cómo estos modelos llegan a      ataques que intenten extraer datos privados a través de
                                                                           sus resultados.                                                     consultas cuidadosamente diseñadas.

                                                                           Esta falta de transparencia plantea problemas de accountability,    Para abordar este reto, es necesario desarrollar técnicas de
                                                                           especialmente cuando los LLM se utilizan en contextos de alta       preservación de la privacidad en el entrenamiento y despliegue
                                                                           sensibilidad, donde las decisiones tienen un impacto                de LLM (p. ej., Digger86 para detectar información protegida, el
                                                                           significativo en las personas (p. ej., uso de LLM en medicina,      uso de datos ficticios87 durante el entrenamiento para detectar
                                                                           investigación farmacéutica, infraestructura crítica o acceso al     el material con copyright).
                                                                           mercado laboral). Sin una comprensión clara de cómo
                                                                           funcionan estos modelos, es difícil determinar la                   Además, es crucial establecer protocolos robustos de seguridad
                                                                           responsabilidad en caso de errores o comportamientos no             y control de acceso para proteger los LLM y sus datos asociados
                                                                           deseados.                                                           de accesos no autorizados o usos maliciosos. Esto puede
                                                                                                                                               implicar el uso de técnicas de autenticación y autorización,
                                                                           Para abordar este reto, es necesario desarrollar técnicas y         monitoreo de seguridad y detección de anomalías.
                                                                           herramientas que permitan una mayor interpretabilidad y
                                                                           explicabilidad de los LLM. Esto incluye métodos para visualizar y
                                                                           analizar los mecanismos internos de atención, técnicas de
                                                                           atribución para identificar las partes más relevantes de la
                                                                           entrada, y enfoques para generar explicaciones en lenguaje
                                                                                                                                               86
                                                                           natural de las predicciones del modelo.                                  Li (2024).
                                                                                                                                               87
                                                                                                                                                    Meeus (2024).
Consumo racional de los recursos                                    4 Riesgos de seguridad y uso malicioso92: los LLM pueden
                                                                      ser vulnerables a ataques adversarios, como la inyección de
El entrenamiento y despliegue de LLM requiere cantidades              datos envenenados o la ingeniería inversa. Además, pueden
masivas de recursos computacionales, almacenamiento y                 utilizarse de forma maliciosa para generar desinformación,
energía. Con modelos que alcanzan los cientos de miles de             spam o contenido engañoso. Es esencial establecer medidas
millones o incluso los billones de parámetros, el coste               de seguridad robustas y diseñar los modelos con
financiero y ambiental de desarrollar y operar estos sistemas         salvaguardias contra el uso indebido.
puede ser muy significativo88.
                                                                    4 Cuestiones de propiedad intelectual y licencias: el uso de
Este alto consumo de recursos plantea desafíos de eficiencia,         LLM plantea preguntas sobre la propiedad intelectual y las
escalabilidad y sostenibilidad. A medida que la demanda de            licencias de los datos de entrenamiento, los modelos y los
LLM más grandes y potentes sigue creciendo, es necesario              resultados generados. Adicionalmente, existe un riesgo de
encontrar formas de optimizar su rendimiento y reducir su             robo de información o datos personales de usuarios que
huella de recursos.                                                   lancen consultas a LLM desplegados en nubes de terceros.
                                                                      Es necesario cumplir con la regulación y con los marcos
Para abordar este reto, se están explorando varias direcciones        éticos para equilibrar los derechos de los creadores, los
de investigación. Una de ellas es el diseño de arquitecturas de       usuarios y el interés público, y, en el caso de las
modelos más eficientes, como el uso de mecanismos de                  organizaciones, para evitar riesgos legales y de
atención dispersa o técnicas de compresión que reducen el             cumplimiento.
tamaño y la complejidad computacional de los LLM sin
comprometer significativamente su rendimiento.                      4 Escalabilidad de la arquitectura de los LLM93: un desafío
                                                                      adicional es la escalabilidad de los transformers a medida
También se está investigando en la mejora de las técnicas de          que aumenta el tamaño de las secuencias y los modelos. Los
preentrenamiento continuo89 y fine-tuning continuo90, que             mecanismos de atención tienen una complejidad cuadrática
buscan integrar la capacidad de usar información de diversos          con respecto a la longitud de la secuencia, lo que limita su
dominios sin la necesidad de depender de un reentrenamiento           aplicación a secuencias muy largas.
exhaustivo y costoso con nuevos datos específicos. Asimismo,
se está avanzando en el uso de sistemas innovadores y el
diseño de algoritmos verdes de IA, que permiten hacer frente a
los costes computacionales y ambientales asociados a la IA (p.
ej., el sistema GreenLightningAI, de Qsimov Quantum
Computing91, desarrolla el reentrenamiento incremental y
                                                                    88
proporciona una interpretabilidad directa).                         89
                                                                       iDanae 1T24 (2024).
                                                                       Yıldız (2024).
                                                                    90
                                                                       Mehta (2023).
Otra dirección es el desarrollo de infraestructuras y plataformas   91
                                                                       iDanae 1T24 (2024).
                                                                    92                                                               35
de computación más sostenibles, como el uso de hardware                Pankajakshan (2024).
                                                                    93
                                                                       Rae (2021).
especializado de bajo consumo, sistemas de enfriamiento más
eficientes y fuentes de energía renovables para alimentar los
centros de datos donde se entrenan y despliegan los LLM.

Además, es importante promover prácticas de uso racional y
compartido de los recursos, como la reutilización y adaptación
de modelos preentrenados en lugar de entrenar nuevos
modelos desde cero para cada tarea, y el intercambio de
recursos y conocimientos entre organizaciones y comunidades
de investigación.

Otros desafíos
De entre los muchos retos adicionales a los que se enfrentan las
organizaciones en el desarrollo, implementación y uso de los
LLM, por su importancia cabe mencionar brevemente:

4 Dependencia y lock-in: las organizaciones que dependen
  de LLM proporcionados por terceros pueden enfrentarse a
  riesgos de dependencia y lock-in, especialmente si los
  modelos se basan en datos o infraestructura propietaria. Es
  importante considerar estrategias de diversificación y
  planes de contingencia.
                                                                           Marco de validación de los LLM




                                                                           “Las consecuencias de que la IA vaya mal son graves, por lo que debemos ser proactivos
                                                                                                                                           en lugar de reactivos“.
                                                                                                                                                         Elon Musk94




MANAGEMENT SOLUTIONS



36




El auge de los large language models: de los fundamentos a la aplicación
Marco                                                                 todos estos aspectos de manera sistemática, las organizaciones
                                                                      pueden identificar y mitigar de manera proactiva los riesgos
Los modelos de lenguaje de gran escala (LLM) ofrecen un gran          asociados con los LLM, sentando las bases para aprovechar su
potencial para transformar diversos sectores y aplicaciones,          potencial de manera segura y responsable.
pero también conllevan riesgos significativos que deben
abordarse. Estos riesgos incluyen la generación de información        En los LLM, esta evaluación de riesgos se puede anclar en las
errónea o alucinaciones, la perpetuación de sesgos, la dificultad     siguientes dimensiones usadas en la disciplina de riesgo de
para olvidar la información aprendida, preocupaciones éticas y        modelo, adaptando los tests en función de la naturaleza y el uso
de equidad, problemas de privacidad por uso indebido,                 del LLM:
dificultades en la interpretación de los resultados, y la potencial
creación de contenido malicioso, entre otros.                         4 Datos de entrada: comprensión del texto98, calidad del
                                                                        dato99.
Dado el impacto potencial de estos riesgos, es necesario validar
exhaustivamente los LLM antes de su despliegue en entornos            4 Solidez conceptual y diseño del modelo: selección del
de producción. De hecho, la validación de los LLM no es solo            modelo y sus componentes (p. ej., metodologías de fine-
una buena práctica, sino también un requisito regulatorio en            tuning, conexiones a bases de datos, RAG100), y comparación
muchas jurisdicciones. En Europa, la propuesta de AI Act exige          con otros modelos101.
una evaluación y mitigación de los riesgos de los sistemas de
IA95, mientras que, en Estados Unidos, el marco de gestión de                                                                                                  37

riesgos de IA del NIST96 y el AI Bill of Rights destacan la
importancia de comprender y abordar los riesgos inherentes a
estos sistemas.
                                                                      94
                                                                         Elon Musk (n. 1971), CEO de X, SpaceX, Tesla. Empresario sudafricano-
La validación de los LLM puede partir de los principios                  estadounidense, conocido por fundar o cofundar empresas como Tesla, SpaceX
establecidos en la disciplina de riesgo de modelo, que se                y PayPal, dueño de X (anteriormente Twitter), red social que tiene su propio
                                                                         LLM, llamado Grok.
centra97 en evaluar y mitigar los riesgos derivados de errores,       95
                                                                         European Parliament (2024) AI Act Art. 9: ”Se establecerá, aplicará, documentará
deficiente implementación o mal uso de los modelos. Sin                  y mantendrá un sistema de gestión de riesgos en relación con los sistemas de IA
                                                                         de alto riesgo. El sistema de gestión de riesgos [...] comprenderá [...] la
embargo, en el caso de la IA, y particularmente de los LLM, es           estimación y evaluación de los riesgos que puedan surgir cuando el sistema de
necesario adoptar una perspectiva más amplia que abarque los             IA de alto riesgo se utilice de acuerdo con su finalidad prevista, y en condiciones
                                                                         de uso indebido razonablemente previsibles“.
otros riesgos que comportan. Un enfoque integral de validación        96
                                                                         NIST (2023): ”La decisión de encargar o desplegar un sistema de IA debe basarse
es esencial para garantizar un despliegue seguro y responsable           en una evaluación contextual de las características de fiabilidad y los riesgos,
                                                                         impactos, costes y beneficios relativos, y debe ser informada por un amplio
de los LLM.                                                              conjunto de partes interesadas“.
                                                                      97
                                                                         Management Solutions (2014). Model Risk Management: Quantitative and
Este enfoque holístico se plasma en un marco de validación               Qualitative Aspects.
                                                                      98
                                                                         Imperial et al. (2023).
multidimensional para los LLM, que cubre aspectos clave (Fig. 9)      99
                                                                         Wettig et al. (2024).
                                                                      100
como el riesgo de modelo, la gestión de datos y privacidad, la            RAG (Retrieval-Augmented Generation) es una técnica avanzada en la que un
                                                                         modelo de lenguaje busca información relevante de una fuente externa antes
ciberseguridad, los riesgos legales y de cumplimiento                    de generar texto. Esto enriquece las respuestas con conocimientos precisos y
normativo, los riesgos operativos y tecnológicos, la ética y la          actuales, combinando inteligentemente la búsqueda de información y la
                                                                         generación de texto. Al integrar datos de fuentes externas, los modelos RAG,
reputación, y el riesgo de proveedor, entre otros. Al abordar            como los RAG-Token y RAG-Sequence propuestos (Lewis et al., 2020), ofrecen
                                                                         respuestas más informadas y coherentes, minimizando el riesgo de generar
                                                                         contenido inexacto o 'alucinaciones'. Este avance representa un paso
                                                                         significativo hacia modelos de inteligencia artificial más confiables y basados en
                                                                         evidencia real.
                                                                      101
                                                                          Khang (2024).
                                                                            Fig. 9. Riesgos asociados a la IA y referencia regulatoria en el AI Act.
                                                                                                                                                                                  Compliance & Legal Risk
                                                                                                                                                                                  Ley AI Act Art. 8, 9
                                                                                                                                                                                  Compliance with AI Act, GDPR, ethical AI frameworks,
                                                                                                                                                       Cumplimiento y             intellectual property
                                                                                                       Riesgo de Modelo                                 riesgo jurídico                             OpRisk, riesgo informático y ciberseguridad
                                                                                       Ley AI Act Art. 8, 9, 10, 14, 15, 29                                                                         Ley AI Act Art. 8, 15
                                                                              Política de GRM, inventario, directrices de                                                  OpRisk, riesgo           Vulnerabilidades de la IA, IA adversaria,
                                                                               validación, clasificación de riesgos, XAI y            Riesgo de                             informático y           respuesta a incidentes, dependencia excesiva
                                                                                                     detección de sesgos.              Modelo                              ciberseguridad           de la IA, implantación de la IA, mantenimiento
                                                                                                                                                                                                    de registros

                                                                                                                                                       Riesgo de IA
                                                                                                 Riesgo del proveedor                                                                               ESG y Riesgo Reputacional
                                                                                                Ley AI Act Art. 8, 9, 12                                                                            Ley AI Act Art. 8, 29a
                                                                             Selección de terceros, ética del proveedor                                                       ESG y                 Ética, equidad, impacto medioambiental,
                                                                                con respecto a la IA, integración de IA,
                                                                                                                                      Riesgo del                             Riesgo                 impacto social, reputación
                                                                                                     derechos de autor
                                                                                                                                      proveedor                            Reputacional

                                                                                                                                                          Gestión y
                                                                                                                                                        privacidad de
                                                                                                                                                            datos                  Gestión y privacidad de datos
                                                                                                                                                                                   Ley AI Act Art. 8, 10
                                                                                                                                                                                   Transparencia, consentimiento para el uso de IA, anonimización,
                                                                                                                                                                                   mantenimiento de registros, sesgo en los datos, envenenamiento de
                                                                                                                                                                                   datos




                                                                           4 Evaluación del modelo y análisis de sus resultados:                                     En cada una de estas dimensiones, dos grupos de técnicas
                                                                             privacidad y seguridad de los resultados102, precisión del                              complementarias permiten realizar una validación más
                                                                             modelo103, consistencia104, robustez105, adaptabilidad106,                              completa (Fig. 10):
                                                                             interpretabilidad (XAI)107, ética, sesgos y equidad108,
                                                                             toxicidad109, comparación contra modelos challenger.                                    4 Métricas de evaluación cuantitativas (tests): se trata de
                                                                                                                                                                       pruebas cuantitativas estandarizadas que miden el
                                                                           4 Implementación y uso: revisión humana en el uso                                           desempeño del modelo en tareas específicas; benchmarks y
                                                                             (incluyendo el monitoreo de usos indebidos), resolución de                                métricas predefinidas para evaluar distintos aspectos del




MANAGEMENT SOLUTIONS
                                                                             errores, escalabilidad y eficiencia, aceptación del usuario.                              rendimiento del LLM después del preentrenamiento, o
                                                                                                                                                                       durante las etapas de fine-tuning o instruction-tuning (es
                                                                           4 Gobernanza110 y ética111: marco de gobierno de la IA                                      decir, técnicas de aprendizaje por refuerzo), optimización,
                                                                             generativa, incluyendo los LLM.                                                           ingeniería de prompts, o recuperación y generación de
                                                                                                                                                                       información. Algunos ejemplos incluyen la precisión en la
                                                                           4 Documentación112: completitud de la documentación del                                     creación de resúmenes, la robustez ante ataques
                                                                             modelo.                                                                                   adversarios o la consistencia en la respuesta ante prompts
38                                                                                                                                                                     similares.
                                                                           4 Cumplimiento regulatorio113: evaluación de los requisitos




El auge de los large language models: de los fundamentos a la aplicación
                                                                             regulatorios (p. ej., AI Act).                                                          4 Evaluación humana: implica el juicio cualitativo por parte
                                                                                                                                                                       de expertos y usuarios finales; por ejemplo, la revisión de
                                                                           Para garantizar el uso efectivo y seguro de los modelos de                                  una muestra concreta de los prompts y las respuestas del
                                                                           lenguaje, es fundamental realizar una evaluación de riesgos que                             LLM por un ser humano para identificar errores.
                                                                           considere tanto el modelo en sí como su uso específico. Esto
                                                                           asegura que, independientemente de su origen (in-house o de                               La validación de un uso específico de un LLM, por tanto, se lleva
                                                                           un proveedor) o personalización (fine-tuning), el modelo                                  a cabo mediante una combinación de técnicas cuantitativas
                                                                           funcione adecuadamente en su contexto de uso, cumpliendo                                  (tests) y cualitativas (evaluación humana). Para cada caso de
                                                                           con los estándares de seguridad, ética y regulación necesarios.                           uso concreto, es necesario diseñar un enfoque de validación a
                                                                                                                                                                     medida, que consistirá en una selección de algunas de estas
                                                                                                                                                                     técnicas.
                                                                           Técnicas de validación
                                                                           Cuando una organización se plantea implementar un LLM para
                                                                           un caso de uso específico, puede ser beneficioso adoptar un                               102
                                                                                                                                                                         Nasr (2023).
                                                                                                                                                                     103
                                                                           enfoque integral que abarque las dimensiones clave del ciclo de                               Liang (2023).
                                                                                                                                                                     104
                                                                                                                                                                         Elazar (2021).
                                                                           vida del modelo: datos, diseño, evaluación, implementación y                              105
                                                                                                                                                                         Liu (2023).
                                                                           uso. Asimismo, de manera transversal, resulta necesario evaluar                           106
                                                                                                                                                                         Dun (2024).
                                                                                                                                                                     107
                                                                           el cumplimiento de la normativa aplicable, como el AI Act en la                               Singh (2024).
                                                                                                                                                                     108
                                                                                                                                                                         NIST (2023), Oneto (2020) y Zhou (2021).
                                                                           Unión Europea.                                                                            109
                                                                                                                                                                         Shaikh (2023).
                                                                                                                                                                     110
                                                                                                                                                                         Management Solutions (2014). Model Risk Management.
                                                                                                                                                                     111
                                                                                                                                                                         Oneto (2020).
                                                                                                                                                                     112
                                                                                                                                                                         NIST (2023).
                                                                                                                                                                     113
                                                                                                                                                                         European Parliament (2024). AI Act.
Fig. 10. Pruebas de evaluación de LLM.


  Dimensiones             Aspectos                  Descripción                     Métricas de validación (ejemplos)                     Evaluación humana
                          validados                                                                                                           (ejemplos)

                                           Grado de calidad de la
1. Datos de
                     1.1 Calidad de dato   modelización o de los datos de     • Flesch-Kinkaid Grade                                  • Revisión caso a caso
entrada
                                           aplicación


                                                                              • Revisión de los elementos del LLM: RAG, filtros de
2. Diseño del        2.1 Diseño del        Elección de modelos y              entrada o salida, definición de prompts, fine-tuning,
                                                                              optimización, etc.                                      • Pruebas A/B
modelo               modelo                metodología adecuadas
                                                                              • Comparación contra otros LLM


                                           Respeto de la confidencialidad y   • Data leakage                                          • Registros
                     3.1 Privacidad y
                                           no regurgitación de información
                     seguridad                                                • PII tests, K-anonymity                                • Hacking ético
                                           personal


                                                                              • Q&A: SummaQA, Word error rate
                                                                              • Recuperación de información: SSA, nDCG
                                                                              • Resumen: ROUGE
                                           Corrección y pertinencia de las                                                            • Backtest de forzajes
                     3.2 Precisión                                            • Traducción: BLEU, Ruby, ROUGE-L
                                           respuestas del modelo                                                                      • Revisión caso a caso
                                                                              • Otros: Sistemas de QA, nivel de overrides, nivel de
                                                                              alucinaciones, etc.
                                                                              • Benchmarks: XSUM, LogiQA, WikiData, etc.



                                           Respuestas uniformes a             • Cosine similarity                                     • Revisión caso a caso
                     3.3 Consistencia
                                           consultas similares                • Jaccard similarity index                              • Pruebas A/B


                                                                              • Generación de texto adversario (TextFooler),
3. Evaluación del                          Resiliencia a la información       patrones Regex                                          • Hacking ético
                     3.4 Robustez
modelo                                     adversa o engañosa                 • Benchmarks de ataques adversarios (PromptBench), • Simulacros de incidentes
                                                                              número de refusals



                                           Capacidad para aprender o          • Rendimiento del LLM ante datos nuevos por             • Pruebas A/B
                     3.5.Adaptabilidad
                                           adaptarse a nuevos contextos       Zero/One/Few-shot learning                              • Revisión caso a caso



                                           Comprensión del proceso de         • SHAP                                                  • Hacking ético
                     3.6 Explicabilidad
                                           toma de decisiones                 • Puntuaciones de explicabilidad                        • Focus groups               39


                                                                              • AI Fairness 360 toolkit
                     3.7 Sesgos y          Respuestas sin sesgo               • WEAT score, paridad demográfica, asociaciones de      • Hacking ético
                     equidad               demográfico                        palabras, etc.                                          • Focus groups
                                                                              • Benchmarks de sesgos (BBQ, etc.)


                                                                              • Perspective API, Hatebase API
                                           Propensión a generar                                                                       • Hacking ético
                     3.8 Toxicidad                                            • Toxicity benchmarks (RealToxicityPrompts, BOLD,
                                           contenidos nocivos                                                                         • Focus groups
                                                                              etc.)

                                           Exclusión de sugerencias
                     4.1 Revisión                                             • Protocolos de riesgos, evaluaciones de seguridad      • Hacking ético
                                           perjudiciales o ilegales e
                     humana y
                                           inclusión de una revisión          • Control humano                                        • Focus groups
                     seguridad de uso
                                           humana (‘human-in-the-loop’)

                                           Capacidad para recuperarse de      • Tests de recuperación del sistema
                     4.2 Recuperación y
                                           errores y gestionar entradas                                                               • Simulacros de incidentes
                     gestión de errores                                       • Métricas de procesamiento de errores
                                           inesperadas

4. Implementación                          Mantenimiento del rendimiento      • Stress testing del sistema, Apache Jmeter, etc.       • Simulacros de incidentes
                  4.3 Escalabilidad
y uso                                      con más datos o usuarios           • Benchmarks de escalabilidad                           • Pruebas A/B


                                           Utilización de recursos y          • Time-to-first-byte (TTFB), uso de GPU/CPU,
                     4.4 Eficiencia                                                                                                   • Simulacros de incidentes
                                           velocidad de respuesta             inferencia de emisiones, memoria, latencia


                                                                              • Checklist de requisitos de usuario, opt-out del
                     4.5 Aceptación del    Pruebas de aceptación de                                                                   • UX tracking
                                                                              usuario
                     usuario               usuario                                                                                    • Pruebas A/B
                                                                              • Satisfacción del usuario (Net Promoter Score, CSAT)
                                                                           La selección exacta de técnicas dependerá de las características                   4 LLM Comparator114: herramienta creada por investigadores
                                                                           particulares del caso de uso; y, en concreto, varios factores                        de Google para la evaluación automática y comparación de
                                                                           importantes a tener en cuenta para decidir las técnicas más                          LLM, que revisa la calidad de las respuestas de los LLM.
                                                                           adecuadas son:
                                                                                                                                                              4 HELM115: evaluación holística de los modelos del lenguaje,
                                                                           4 El nivel de riesgo y la criticidad de las tareas que se confiarán                  que compila métricas de evaluación a lo largo de siete
                                                                             al LLM.                                                                            dimensiones (precisión, calibración, robustez, equidad,
                                                                                                                                                                sesgos, toxicidad y eficiencia) para una serie de escenarios
                                                                           4 Si el LLM está abierto al público (y por tanto el hacking ético                    predefinidos.
                                                                             cobra especial relevancia) o si su uso se limita al ámbito
                                                                             interno de la organización.                                                      4 ReLM116: sistema de validación y consulta de LLM mediante
                                                                                                                                                                uso del lenguaje, incluyendo evaluaciones de modelos
                                                                           4 Si el LLM procesa datos personales.                                                lingüísticos, memorización, sesgos, toxicidad y
                                                                                                                                                                comprensión del lenguaje.
                                                                           4 La línea de negocio o servicio que utilizará el LLM.
                                                                                                                                                              En la actualidad, ciertas técnicas de validación, como los
                                                                           Un análisis cuidadoso de estos drivers permitirá construir un                      métodos de explicabilidad (XAI) basados en SHAP, algunas
                                                                           marco de validación robusto y adaptado a las necesidades de                        métricas como ROUGE117 o los análisis de imparcialidad
                                                                           cada uso de un LLM.                                                                mediante paridad demográfica, aún no cuentan con umbrales
                                                                                                                                                              predefinidos ampliamente aceptados. En estos casos, es tarea
                                                                           Métricas de evaluación cuantitativas                                               de la comunidad científica y de la industria seguir investigando
                                                                                                                                                              para establecer criterios claros que permitan una validación
                                                                           Aunque es un campo de estudio emergente, existe una amplia                         robusta y estandarizada.
                                                                           gama de métricas cuantitativas para evaluar el rendimiento de
                                                                           los LLM. Algunas de estas métricas son adaptaciones de las
                                                                           utilizadas en modelos tradicionales de aprendizaje automático,
                                                                           como la precisión, la exhaustividad (recall), la puntuación F1 o el
                                                                           área bajo la curva ROC (AUC-ROC). Otras métricas han sido




MANAGEMENT SOLUTIONS
                                                                           diseñadas específicamente para evaluar aspectos únicos de los
                                                                           LLM, como la coherencia del texto generado, la fidelidad a los
                                                                           hechos o la diversidad del lenguaje.

                                                                           En este sentido, ya existen marcos holísticos de testeo
                                                                                                                                                              114
                                                                           cuantitativo de LLM en entornos de programación en Python,                             Kahng (2024).
                                                                                                                                                              115
                                                                                                                                                                  Liang (2023).
                                                                           que facilitan la implementación de muchas de las métricas                          116
                                                                                                                                                                  Kuchnik (2023).
40                                                                         cuantitativas de validación, por ejemplo:                                          117
                                                                                                                                                                  Duan (2023).




El auge de los large language models: de los fundamentos a la aplicación
                                                                            Fig. 11. Algunas técnicas de evaluación humana de LLM.



                                                                                        A              Backtest de anulaciones
                                                                                                       Contabilizar y medir la importancia de las
                                                                                                       modificaciones humanas en los resultados del
                                                                                                                                                                    E                Grupos de discusión
                                                                                                                                                                                     Recoger opiniones sobre los resultados del
                                                                                                                                                                                     LLM de diversos usuarios (en materia de ética,
                                                                                                       LLM.                                                                          adecuación cultural, discriminación, etc.).




                                                                                                                                                                    F
                                                                                                      Comprobación caso por caso

                                                                                        B
                                                                                                                                                                                    Seguimiento de la experiencia del usuario (UX)
                                                                                                      Comparar una muestra representativa (por
                                                                                                                                                                                    Observar y evaluar las interacciones de los
                                                                                                      ejemplo, un mínimo de 200 a través de la prueba
                                                                                                                                                                                    usuarios con el LLM a lo largo del tiempo / en
                                                                                                      Z1 ) de respuestas LLM con resultados humanos
                                                                                                                                                                                    tiempo real.
                                                                                                      ("ground truth"), incl. doble ciego.




                                                                                                                                                                    G
                                                                                                    Hacking ético (también conocido como Equipo Rojo)

                                                                                        C
                                                                                                                                                                                    Simulacros de incidentes
                                                                                                     Manipular los mensajes para forzar al LLM a                                    Simular escenarios adversos para probar la
                                                                                                     producir resultados no deseados (incl. regurgitación                           respuesta y recuperación del LLM (prueba de
                                                                                                     de PII, cumplimiento, ingeniería de mensajes,                                  estrés, comprobación de copias de seguridad,
                                                                                                     pruebas de penetración, vulnerabilidades de IA, etc.).                         medición del tiempo de recuperación, etc.).




                                                                                       D              Pruebas A/B
                                                                                                      Realizar ensayos paralelos para evaluar diferentes
                                                                                                      versiones (A y B) o comparar con el rendimiento
                                                                                                                                                                H                   Mantenimiento de registros
                                                                                                                                                                                    Revisar los diarios y registros del sistema LLM,
                                                                                                                                                                                    garantizando el cumplimiento de la normativa.
                                                                                                      humano.

Técnicas de evaluación humana                                        Benchmarks de evaluación de LLM
Mientras que las métricas de evaluación cuantitativa son
                                                                     La mayoría de los modelos de inteligencia artificial generativa,
implementables de forma más directa debido a la multitud de
                                                                     incluidos los LLM, se someten a pruebas utilizando benchmarks
recursos online y publicaciones de los últimos años, las técnicas    públicos que evalúan su desempeño en una variedad de tareas
de evaluación humana118 son variadas y deben ser construidas         relacionadas con la comprensión y el uso del lenguaje natural.
en función de la tarea específica119 que esté realizando el LLM, e   Estas pruebas sirven para medir cómo maneja el LLM tareas
                                                                     específicas y refleja el entendimiento humano. Algunos de estos
incluyen (Fig. 11):                                                  benchmarks incluyen:

4 Backtest de los forzajes del usuario: contabilizar y medir la       4 GLUE/SuperGLUE: evalúa la comprensión del lenguaje a
                                                                         través de tareas que miden la capacidad de un modelo para
  importancia de las modificaciones humanas en los                       entender el texto.
  resultados del LLM (p. ej., cuántas veces un gestor comercial
                                                                      4 Eleuther AI Language Model Evaluation Harness: realiza
  debe modificar manualmente los resúmenes de llamadas a                 una evaluación ”few-shot“ de los modelos, es decir, su
  clientes que ha realizado un LLM).                                     precisión con muy pocos ejemplos de entrenamiento.

                                                                      4 ARC (AI2 Reasoning Challenge): pone a prueba la
4 Revisión caso a caso: comparar una muestra representativa              habilidad del modelo para responder preguntas de ciencia
  de respuestas del LLM con las expectativas del usuario                 que requieren razonamiento.
  («ground truth“).
                                                                      4 HellaSwag: evalúa el sentido común del modelo a través de
                                                                         tareas que requieren predecir el final coherente de una
4 Hacking ético (Red Team): manipular los prompts para                   historia.
  forzar al LLM a producir resultados no deseados (p. ej.,
                                                                      4 MMLU (Massive Multitask Language Understanding):
  regurgitación de información personal, contenido ilegal,               prueba la precisión del modelo en una amplia gama de
  tests de penetración, explotación de vulnerabilidades).                tareas para evaluar su comprensión multitarea.

                                                                      4 TruthfulQA: desafía al modelo a discernir entre
4 Testeo A/B: comparación para evaluar dos versiones del                 información verdadera y falsa, evaluando su habilidad para
  LLM (A y B), o de un LLM frente a un ser humano.                       manejar datos verídicos.

                                                                      4 Winogrande: otra herramienta para evaluar el sentido
4 Focus groups: recabar opiniones de diversos usuarios sobre             común, similar a HellaSwag pero con diferentes métodos y
  el comportamiento del LLM, p. ej., en materia de ética,                énfasis.
  adecuación cultural, discriminación, etc.                           4 GSM8K: evalúa la capacidad lógico-matemática del modelo
                                                                         a través de problemas de matemáticas diseñados para
4 Experiencia del usuario (UX tracking): observar y evaluar              estudiantes.
  las interacciones de los usuarios con el LLM a lo largo del
  tiempo o en tiempo real.

                                                                                                                                        41
4 Simulacros de incidentes: simular escenarios adversos
  para probar la respuesta del LLM (p. ej., prueba de estrés,
  comprobación de copias de seguridad, medición del tiempo
  de recuperación, etc.).

4 Mantenimiento de registros: revisar los diarios y registros
  del sistema LLM, garantizando el cumplimiento de la
  normativa y la traza de auditoría.




118
      Datta, Dickerson (2023).
119
      Guzmán (2015).
                                                                           Nuevas tendencias                                                                          4 Técnicas de interpretabilidad post-hoc: estas técnicas se
                                                                                                                                                                        basan en la interpretabilidad de los resultados en la etapa
                                                                           El campo de la validación de LLM se encuentra en constante                                   posterior al entrenamiento o fine-tuning, y permiten
                                                                           evolución, impulsado por los rápidos avances en el desarrollo de                             identificar qué partes de la entrada han influido más en la
                                                                           estos modelos y por la creciente conciencia sobre la importancia                             respuesta del modelo (importancia de características),
                                                                           de garantizar su fiabilidad, equidad y alineación con la ética y la                          encontrar ejemplos similares en el conjunto de datos de
                                                                           regulación.                                                                                  entrenamiento (similitud basada en embeddings) o diseñar
                                                                                                                                                                        prompts específicos que guíen al modelo hacia
                                                                           A continuación, se presentan algunas de las principales                                      explicaciones más informativas (estrategias de prompting).
                                                                           tendencias emergentes en este ámbito:
                                                                                                                                                                      4 Puntuaciones por atribución: como parte de la
                                                                           4 Explicabilidad de los LLM: a medida que los LLM ganan en                                   interpretabilidad post-hoc, se están desarrollando
                                                                             complejidad y opacidad, crece la demanda de mecanismos                                     técnicas122 que permiten identificar qué partes del texto de
                                                                             que permitan entender y explicar su funcionamiento                                         entrada tienen mayor influencia en la respuesta generada
                                                                             interno. Las técnicas de XAI (eXplainable AI) como SHAP,                                   por un LLM. Ayudan a entender qué palabras o frases son
                                                                             LIME o la atribución de importancia a los tokens de entrada                                más importantes para el modelo. Existen diferentes
                                                                             están ganando protagonismo en la validación de LLM.                                        métodos para calcular estas puntuaciones:
                                                                             Aunque para los modelos tradicionales hay una variedad de
                                                                             técnicas post-hoc disponibles para comprender el                                                 - Métodos basados en el gradiente: analizan cómo
                                                                             funcionamiento de los modelos a nivel local y global120 (p.                                        cambian los gradientes (una medida de sensibilidad)
                                                                             ej., Anchors, PDP, ICE), y ha proliferado la definición e                                          para cada palabra al retroceder por la red neuronal.
                                                                             implementación de modelos inherentemente interpretables
                                                                             por construcción, la implementación de estos principios                                          - Métodos basados en perturbaciones: modifican
                                                                             para los LLM no está todavía resuelta.                                                             ligeramente el texto de entrada y observan cómo
                                                                                                                                                                                cambia la respuesta del modelo.
                                                                           4 Uso de LLM para explicar LLM: una tendencia emergente
                                                                             consiste en utilizar un LLM para generar explicaciones sobre                                     - Interpretación de métricas internas: utilizan métricas
                                                                             el comportamiento o las respuestas de otro LLM. En otras                                           calculadas por el propio modelo, como los pesos de




MANAGEMENT SOLUTIONS
                                                                             palabras, se emplea un modelo del lenguaje para interpretar                                        atención en los transformers, para determinar la
                                                                             y comunicar de forma más comprensible el razonamiento                                              importancia de cada palabra.
                                                                             subyacente de otro modelo. Para enriquecer estas
                                                                             explicaciones, se están desarrollando herramientas121 que
                                                                             incorporan además técnicas de análisis post-hoc.
                                                                                                                                                                       120
                                                                                                                                                                           Management Solutions (2023). Explainable Artificial Intelligence.
                                                                                                                                                                       121
                                                                                                                                                                           Wang (2024).
42                                                                                                                                                                     122
                                                                                                                                                                           Sarti (2023).




El auge de los large language models: de los fundamentos a la aplicación
                                                                            Fig. 12. Implementación de valores de SHAP para resumen de textos.

                                                                                  Resumen de la salida: ”Todavía se está evaluando el coste total de los daños en Newton Stewart, una de las zonas más afectadas . La Primera Ministra,
                                                                                  Nicola Sturgeon, visitó la zona para inspeccionar los daños. El líder adjunto del Partido Laborista Escocés, Alex Rowley, estuvo el lunes en Hawick para
                                                                                  ver la situación de primera mano. Afirmó que era importante aplicar correctamente el plan de protección contra las inundaciones".


                                                                                                   Of + damage + in + Newton + Stewart + .                                                                                   +2

                                                                                                                                                                                                                     +1,81

                                                                                                                                         The                                                                         +1,81




                                                                                                                                                                                                                                    Clustering cutoff = 0,5
                                                                                                                                         full                                                                        +1,81

                                                                                                                                        cost                                                                         +1,81

                                                                                                                    One + 11 other features                   +0,31

                                                                                                                 remain + 24 other features             +0,24

                                                                                                                      to + 79 other features                     +0,46

                                                                                                                   habe + 95 other features                       +0,48

                                                                                                                        + 292 other features                                                                +1,6


                                                                                                                                                0,00   0,25     0,50         0,75    1,00   1,25     1,50     1,75      2,00
                                                                                                                                                                                    SHAP value
Un ejemplo de puntuación por atribución es la aplicación de la    SHAP (SHapley Additive
técnica SHAP para proporcionar una medida cuantitativa de la      exPlanations) aplicado a un LLM
importancia de cada palabra para la salida del LLM, lo que
facilita su interpretación y comprensión (Fig. 12).
                                                                  SHAP es un método de explicabilidad post-hoc basado en la
                                                                  teoría de juegos cooperativos. Asigna a cada característica
4 Validación continua y monitorización en producción:             (token) un valor de importancia (valor Shapley) que representa
  más allá de la evaluación puntual antes del despliegue, se      su contribución a la predicción del modelo.
  extiende la práctica de realizar un seguimiento continuo del    Formalmente, sea x = (x_1,…,x_n) una secuencia de tokens de
  comportamiento de los LLM una vez que están en uso, al          entrada. La predicción del modelo se denota como f(x). El valor
  igual que se hace con modelos tradicionales. Esto permite       Shapley φ para el token x_i se define como:
  detectar posibles desviaciones o degradaciones en su
  rendimiento a lo largo del tiempo, así como identificar
  sesgos o riesgos no previstos inicialmente.

4 Validación colaborativa y participativa: se promueve una        donde N es el conjunto de todos los tokens, S es un subconjunto
  mayor implicación de diversos stakeholders en el proceso        de tokens, y f(S) es la predicción del modelo para el subconjunto
  de validación, incluyendo no solo a expertos técnicos sino      S.
  también a usuarios finales, reguladores, auditorías externas    Intuitivamente, el valor Shapley φi captura el impacto promedio
  y representantes de la sociedad civil. Esta participación       del token xi en la predicción del modelo, considerando todos los
                                                                  subconjuntos posibles de tokens.
  plural permite incorporar diferentes perspectivas y fomenta
  la transparencia y la responsabilidad.                          Ejemplo: se considera un LLM entrenado para clasificar correos
                                                                  electrónicos corporativos como ”importante“ o ”no
                                                                  importante“. Dado el vector de tokens de entrada:
4 Validación ética y alineada con la regulación: más allá de
  las métricas de rendimiento, se otorga cada vez más             x = [El, informe, financiero, del, Q2, muestra, un, aumento,
  importancia a evaluar si el comportamiento de los LLM es        significativo, en, los, ingresos, y, la, rentabilidad]
  ético y está alineado con los valores humanos y con la          El modelo clasifica el correo como ”importante“ con f(x) = 0.85.
  regulación. Esto implica analizar cuestiones como la
                                                                  Aplicando SHAP, se obtienen los siguientes valores Shapley:
  equidad, la privacidad, la seguridad, la transparencia o el
  impacto social de estos sistemas.                                   φ1 = 0.01 (El)

                                                                      φ2 = 0.2 (informe)
4 Machine unlearning: se trata de una técnica emergente123
                                                                      φ3 = 0.15 (financiero)
  que permite ”desaprender“ información conocida de un
  LLM sin reentrenarlo desde cero. Esto se consigue, por              φ4 = 0.02 (del)
  ejemplo, adaptando los hiperparámetros del modelo a los             φ5 = 0.1 (Q2)
  datos que se desea desaprender. Se puede usar el mismo
  principio para eliminar los sesgos que se hayan identificado.       φ6 = 0.05 (muestra)                                             43

  Así, se obtiene un modelo que mantiene su conocimiento              φ7 = 0.01 (un)
  general, pero ha eliminado los sesgos problemáticos,
                                                                      φ8 = 0.15 (aumento)
  mejorando su equidad y alineación ética de forma eficiente
  y selectiva. Actualmente se están explorando varios                 φ9 = 0.1 (significativo)
  métodos de machine unlearning, como el gradient 4scent129,          φ10 = 0.01 (en)
  el uso de fine-tuning125 o la modificación selectiva de
                                                                      φ11 = 0.02 (los)
  determinados pesos, capas o neuronas del modelo126.
                                                                      φ12 = 0.12 (ingresos)

                                                                      φ13 = 0.01 (y)

                                                                      φ14 = 0.02 (la)

                                                                      φ15 = 0.08 (rentabilidad)

                                                                  Interpretación: los tokens ”informe“ (0.2), ”financiero“ (0.15),
                                                                  ”aumento“ (0.15) e ”ingresos“ (0.12) tienen las mayores
                                                                  contribuciones a la clasificación del correo como ”importante“.
                                                                  Esto sugiere que el LLM ha aprendido a asociar estos términos
                                                                  con la importancia del mensaje en un contexto empresarial.




123
     Liu (2024).
124
    Jang (2022).
125
    Yu (2023).
126
    Wu (2023)
                                                                           Caso práctico: validación de un chatbot de
                                                                           políticas


                                                                                         “La inteligencia artificial alcanzará niveles humanos hacia 2029“.
                                                                                                                                               Ray Kurzweil127

                                                                                    “Creo que tendremos una IA más inteligente que cualquier ser humano
                                                                                                                       probablemente a finales de 2025“.
                                                                                                                                                  Perplexity128




MANAGEMENT SOLUTIONS



44




El auge de los large language models: de los fundamentos a la aplicación
Para ilustrar la aplicación de las técnicas de validación de un        Diseño del enfoque de validación
LLM descritas, en esta sección se presenta un caso práctico de
validación de un chatbot de políticas internas de una compañía.        Para validar de manera integral el chatbot de políticas, siguiendo
                                                                       el marco presentado en la sección anterior, se ha diseñado un
                                                                       enfoque de validación a medida que abarca las dimensiones clave
Definición del caso                                                    del ciclo de vida del modelo: datos, diseño, evaluación,
                                                                       implementación y uso. Este enfoque combina métricas
La compañía ha desarrollado un chatbot basado en un LLM de             cuantitativas y técnicas de evaluación humana, con el objetivo de
código abierto para responder preguntas y proporcionar                 obtener una visión completa del desempeño y la adecuación del
información sobre sus políticas internas. El objetivo principal de     chatbot en el contexto específico de la compañía.
este chatbot es facilitar el acceso de los empleados a las políticas
de la empresa.                                                         A continuación, se resumen las pruebas y técnicas seleccionadas
                                                                       para cada dimensión:
El chatbot ha sido construido utilizando una infraestructura en la
nube y se ha alimentado con todas las políticas de la compañía,        Datos
que abarcan aproximadamente 1.000 páginas de                                                                                                                    45
documentación. Para mejorar su capacidad de respuesta, se han          4 Métricas: se utilizará la escala Flesch-Kincaid para evaluar la
aplicado técnicas de Retrieval-Augmented Generation (RAG), que           legibilidad y complejidad de las políticas que alimentan al
permiten al modelo recuperar información relevante de su base            chatbot.
de conocimientos antes de generar una respuesta. Inicialmente,
se consideró la posibilidad de aplicar fine-tuning al modelo, pero     4 Evaluación humana: se revisará una muestra representativa
tras las pruebas iniciales, se concluyó que la combinación del           de las políticas para identificar posibles inconsistencias,
LLM base con RAG era suficiente para obtener resultados                  errores o ambigüedades.
satisfactorios.
                                                                       Diseño del modelo
Antes de su implementación definitiva, la compañía ha decidido
llevar a cabo un proceso de validación exhaustivo para evaluar         4 Métricas: se modificarán elementos concretos del LLM en el
la precisión, la seguridad y la adecuación del chatbot en el             código de desarrollo (p. ej., la técnica de RAG y sus
contexto específico de su uso previsto. Este proceso de                  hiperparámetros, como el tamaño o la estrategia de
validación tiene como objetivo identificar posibles áreas de             ”chunking“129) que pueden modificar su rendimiento ante
mejora y garantizar que el chatbot cumpla con los estándares de          respuestas, y se compararán los resultados contra el modelo
calidad y las expectativas de la empresa.                                original.

La validación del chatbot de políticas se realizará mediante una       127
                                                                           Ray Kurzweil (n. 1948). Director de Ingeniería en Google, científico
combinación de métricas cuantitativas y técnicas de evaluación             computacional, inventor y futurista, conocido por la invención del OCR y por
                                                                           sus contribuciones en IA.
humana, siguiendo el marco de validación multidimensional              128
                                                                           Elon Musk (n. 1971), CEO de X, SpaceX, Tesla. Empresario sudafricano-
descrito en la sección anterior. Los resultados de este proceso            estadounidense, conocido por fundar o cofundar empresas como Tesla, SpaceX
                                                                           y PayPal, dueño de X (anteriormente Twitter), red social que tiene su propio
servirán para tomar decisiones informadas sobre la                         LLM, llamado Grok.
implementación del chatbot y para establecer un plan de                129
                                                                           La estrategia de ”chunking“ se refiere al proceso de dividir el texto de entrada a
mejora continua.                                                           un LLM en unidades más pequeñas y manejables («chunks“) durante su uso o
                                                                           implementación.
                                                                           4 Evaluación humana: se realizará una revisión exhaustiva de       4 Adaptabilidad
                                                                             los componentes del chatbot, incluyendo la configuración
                                                                                                                                                  - Métricas: se evaluará el rendimiento del chatbot ante
                                                                             de RAG, los filtros de entrada y salida, la definición de
                                                                                                                                                    nuevas políticas o actualizaciones mediante técnicas de
                                                                             prompts y la optimización de hiperparámetros. Además, se
                                                                                                                                                    few-shot learning. Se evaluará la respuesta del chatbot
                                                                             llevarán a cabo pruebas A/B para comparar el desempeño
                                                                                                                                                    ante idiomas no empleados en las políticas o solicitudes
                                                                             del chatbot con otros LLM disponibles en el mercado.
                                                                                                                                                    de traducciones a idiomas no incluidos en el RAG (p. ej.,
                                                                                                                                                    polaco).
                                                                           Evaluación del modelo
                                                                                                                                                  - Evaluación humana: se realizarán pruebas A/B y
                                                                           4 Privacidad y seguridad
                                                                                                                                                    revisiones caso por caso para evaluar la capacidad del
                                                                               - Métricas: se aplicarán pruebas de K-anonimato para                 chatbot para adaptarse a nuevos escenarios.
                                                                                 evaluar la protección de datos personales en las
                                                                                 respuestas del chatbot, y pruebas de PII (Personal           4 Explicabilidad
                                                                                 Identificable Information) para identificar atributos
                                                                                                                                                  - Métricas: se aplicarán técnicas de explicabilidad, como
                                                                                 sensibles en los datos, utilizando PIIfilter.
                                                                                                                                                    SHAP, para comprender el proceso de toma de
                                                                                                                                                    decisiones del chatbot. Se evaluará el módulo de
                                                                               - Evaluación humana: se realizarán pruebas de hacking
                                                                                                                                                    interpretabilidad intrínseco del chatbot, mediante el
                                                                                 ético para identificar posibles vulnerabilidades y se
                                                                                                                                                    cual se provee una explicación del origen de la
                                                                                 mantendrán registros detallados de las interacciones del
                                                                                                                                                    información en la respuesta al usuario.
                                                                                 chatbot.
                                                                                                                                                  - Evaluación humana: se realizará un seguimiento de la
                                                                           4 Precisión
                                                                                                                                                    experiencia del usuario (UX) y se llevará a cabo un focus
                                                                               - Métricas: se utilizarán las métricas Word Error Rate (WER)         group para evaluar la percepción de los usuarios sobre
                                                                                 y ROUGE para evaluar la precisión de las respuestas del            la transparencia y la explicabilidad del chatbot.
                                                                                 chatbot en comparación con las políticas originales.
                                                                                 También se emplearán benchmarks específicos del              4 Sesgos y equidad
                                                                                 dominio, como un conjunto de preguntas y respuestas




MANAGEMENT SOLUTIONS
                                                                                                                                                  - Métricas: se utilizará el conjunto de herramientas AI
                                                                                 diseñado por expertos en políticas de la compañía.
                                                                                                                                                    Fairness 360 para evaluar posibles sesgos demográficos
                                                                                                                                                    en las respuestas del chatbot. También se emplearán
                                                                               - Evaluación humana: se realizará una revisión caso por
                                                                                                                                                    benchmarks específicos, como el Bias Benchmark for QA
                                                                                 caso de una muestra representativa de interacciones del
                                                                                                                                                    (BBQ), para medir la equidad en el contexto de las
                                                                                 chatbot para identificar posibles errores o imprecisiones.
                                                                                                                                                    políticas de la compañía.
                                                                           4 Consistencia
46                                                                                                                                                - Evaluación humana: se llevarán a cabo pruebas de
                                                                               - Métricas: se aplicarán la similitud coseno y el índice de          hacking ético y un focus group para identificar posibles




El auge de los large language models: de los fundamentos a la aplicación
                                                                                 Jaccard para evaluar la consistencia de las respuestas del         sesgos o discriminación en las respuestas del chatbot.
                                                                                 chatbot ante consultas similares.
                                                                                                                                              4 Toxicidad
                                                                               - Evaluación humana: se llevarán a cabo pruebas A/B para
                                                                                                                                                  - Métricas: se aplicarán las herramientas Perspective API y
                                                                                 comparar las respuestas del chatbot en diferentes
                                                                                                                                                    Hatebase API para evaluar la presencia de lenguaje
                                                                                 escenarios y se realizará una revisión caso por caso para
                                                                                                                                                    tóxico o inapropiado en las respuestas del chatbot.
                                                                                 identificar posibles inconsistencias.
                                                                                                                                                    Además, se utilizarán benchmarks específicos, como
                                                                                                                                                    RealToxicityPrompts, para medir la toxicidad en el
                                                                           4 Robustez
                                                                                                                                                    contexto de las políticas de la compañía.
                                                                               - Métricas: se utilizarán herramientas como TextFooler
                                                                                 para generar texto adversario y evaluar la resiliencia del       - Evaluación humana: se realizarán pruebas de hacking
                                                                                 chatbot ante información engañosa. Además, se                      ético para identificar posibles casos de lenguaje
                                                                                 contabilizará el número de rechazos del chatbot ante               ofensivo o inapropiado en las interacciones del chatbot.
                                                                                 prompts malintencionados.

                                                                               - Evaluación humana: se realizarán pruebas de hacking
                                                                                 ético y simulacros de incidentes para evaluar la
                                                                                 capacidad del chatbot para manejar situaciones
                                                                                 adversas.
Implementación y uso                                               Resultados
4 Escalabilidad                                                    Tras aplicar el enfoque de validación personalizado al chatbot
                                                                   de políticas, se obtuvieron resultados prometedores que
    - Métricas: se realizarán pruebas de estrés del sistema
                                                                   demuestran su adecuación general para el uso previsto en la
      utilizando Apache JMeter para evaluar el rendimiento
                                                                   compañía (Fig. 13). En la mayoría de las dimensiones evaluadas,
      del chatbot bajo altas cargas de trabajo.
                                                                   el chatbot alcanzó un desempeño satisfactorio, cumpliendo con
                                                                   los estándares de calidad y las expectativas establecidas.
    - Evaluación humana: se llevarán a cabo simulacros para
      evaluar la capacidad del chatbot para manejar un
                                                                   En cuanto a la calidad de los datos de entrada, se encontró que
      aumento imprevisto en el número de usuarios o
                                                                   las políticas que alimentan al chatbot tienen, en general, un
      consultas.
                                                                   nivel de legibilidad y complejidad adecuado para su
4 Eficiencia                                                       comprensión por parte de los usuarios. Además, la revisión
                                                                   humana no identificó inconsistencias significativas o errores en
    - Métricas: se medirán el tiempo de respuesta (Time-to-        el contenido de las políticas.
      First-Byte, TTFB), el uso de recursos (GPU/CPU, memoria)                                                                         47
      y la latencia para evaluar la eficiencia del chatbot.        El diseño del modelo también demostró ser apropiado para el
                                                                   caso de uso, con una configuración óptima de los componentes
4 Aceptación del usuario                                           del chatbot y un rendimiento superior en comparación con
    - Métricas: se establecerá una lista de verificación de los    otros LLM disponibles en el mercado.
      requisitos del usuario y se medirá la satisfacción del
      usuario utilizando indicadores como el Net Promoter          En términos de evaluación del modelo, el chatbot obtuvo
      Score (NPS) y el Customer Satisfaction Score (CSAT).         resultados positivos en la mayoría de las métricas y pruebas
                                                                   aplicadas. Se destacan la alta precisión de las respuestas, la
    - Evaluación humana: se realizará un seguimiento de la         consistencia en el manejo de consultas similares y la capacidad
      experiencia del usuario (UX) para evaluar la aceptación y    para adaptarse a nuevos escenarios. Sin embargo, se
      satisfacción de los usuarios con el chatbot.                 identificaron algunas áreas de mejora en aspectos como la
                                                                   explicabilidad, la detección de sesgos y la respuesta a
Este enfoque de validación personalizado permitirá a la            preguntas muy específicas donde se requiere un mayor
compañía obtener una evaluación completa del chatbot de            perfeccionamiento del modelo. En el ámbito de ciberseguridad,
políticas, identificando áreas de mejora y garantizando su         se requiere un análisis más detallado de las vulnerabilidades
adecuación para el uso previsto. Los resultados de estas pruebas   específicas de los LLM open-source empleados, para mitigar ese
y evaluaciones servirán como base para la toma de decisiones       riesgo en su puesta en producción.
informadas sobre la implementación y el perfeccionamiento
continuo del chatbot.                                              En cuanto a la implementación y uso, el chatbot demostró una
                                                                   buena escalabilidad y eficiencia en el manejo de altas cargas de
                                                                   trabajo. Además, la satisfacción de los usuarios fue alta, lo que
                                                                   indica una buena aceptación de la herramienta en el contexto
                                                                   de la compañía.
                                                                           Fig. 13. Resumen de resultados de las métricas y técnicas de evaluación humana del chatbot de políticas.



                                                                                    Dimensión                            Prueba                                    Resultado                                   Interpretación

                                                                                                                                                                                            Las políticas son comprensibles para la mayoría de los
                                                                                                        Flesch-Kincaid                           Legibilidad adecuada (grado 8)
                                                                                                                                                                                            usuarios
                                                                            Datos
                                                                                                                                                                                            Las políticas son coherentes y no contienen errores
                                                                                                        Revisión humana                          Sin inconsistencias significativas
                                                                                                                                                                                            importantes


                                                                                                                                                                                            Se requiere adaptar los parámetros del RAG al
                                                                                                                                                                                            contexto de las políticas (p. ej., chunk size) para
                                                                                                        Modelos challenger                       Mejoras en parámetros identificadas
                                                                                                                                                                                            mejorar la captura de información en preguntas muy
                                                                                                                                                                                            específicas
                                                                            Diseño del modelo
                                                                                                        Revisión de componentes                  Configuración óptima                       El diseño del chatbot es apropiado para el caso de uso

                                                                                                                                                                                            El chatbot supera a otros modelos disponibles en el
                                                                                                        Pruebas A/B                              Rendimiento superior a otros LLM
                                                                                                                                                                                            mercado

                                                                                                                                                 Protección adecuada de datos               El chatbot no revela información sensible en sus
                                                                                                        K-anonimato
                                                                                                                                                 personales                                 respuestas

                                                                                                                                                                                            Se requieren ajustes para fortalecer la seguridad del
                                                                                                        Hacking ético                            Vulnerabilidades menores identificadas
                                                                                                                                                                                            chatbot


                                                                                                        Word Error Rate (WER)                    WER < 5%                                   Las respuestas del chatbot son altamente precisas


                                                                                                                                                                                            Las respuestas del chatbot capturan adecuadamente
                                                                                                        ROUGE                                    ROUGE-L > 0.8
                                                                                                                                                                                            el contenido de las políticas


                                                                                                                                                                                            El chatbot proporciona respuestas consistentes ante
                                                                                                        Similitud coseno / Índice de Jaccard     Similitud > 0.9
                                                                                                                                                                                            consultas similares




MANAGEMENT SOLUTIONS
                                                                                                                                                 Resiliencia moderada ante texto            El chatbot es moderadamente robusto ante
                                                                                                        TextFooler
                                                                            Evaluación del modelo                                                adversario                                 información engañosa

                                                                                                                                                                                            El chatbot puede adaptarse a nuevas políticas o
                                                                                                                                                                                            actualizaciones con un entrenamiento mínimo, pero
                                                                                                        Few-shot learning                        Adaptabilidad satisfactoria
                                                                                                                                                                                            se requiere monitorizar y agregar esos nuevos
                                                                                                                                                                                            documentos al RAG periódicamente


                                                                                                                                                                                            Se requiere mejorar la capacidad del chatbot para
48
                                                                                                                                                                                            explicar sus decisiones, si bien el componente de RAG
                                                                                                                                                 Explicabilidad limitada
                                                                                                        SHAP                                                                                se ha construido de manera que el LLM da una




El auge de los large language models: de los fundamentos a la aplicación
                                                                                                                                                                                            respuesta autoexplicativa


                                                                                                                                                 Sesgos demográficos menores                El chatbot presenta algunos sesgos que deben ser
                                                                                                        AI Fairness 360 / BBQ
                                                                                                                                                 identificados                              mitigados

                                                                                                                                                                                            Las respuestas del chatbot rara vez contienen lenguaje
                                                                                                        Perspective API / RealToxicityPrompts Toxicidad baja (< 5%)
                                                                                                                                                                                            tóxico o inapropiado


                                                                                                                                                 Escalabilidad satisfactoria (hasta 1000    El chatbot puede manejar altas cargas de trabajo sin
                                                                                                        Apache JMeter
                                                                                                                                                 usuarios)                                  degradación significativa del rendimiento


                                                                                                                                                 Eficiencia adecuada (TTFB < 1s, uso        El chatbot responde rápidamente y utiliza los recursos
                                                                            Implementación y uso        TTFB / Uso de recursos / Latencia
                                                                                                                                                 moderado)                                  de manera eficiente


                                                                                                                                                                                            Los usuarios están altamente satisfechos con el
                                                                                                        NPS / CSAT                               Satisfacción alta (NPS > 60, CSAT > 80%)
                                                                                                                                                                                            chatbot y lo recomendarían a otros
Estos resultados indican que el chatbot de políticas está bien          correspondiente, esta explicación no resulta del todo clara
encaminado para su implementación en la compañía, aunque                para preguntas muy específicas.
se han identificado algunas áreas específicas que requieren
mejoras adicionales. La sección siguiente abordará las               2. Mitigar los sesgos identificados: aunque los sesgos
principales conclusiones y recomendaciones derivadas de este            detectados son menores, es recomendable aplicar técnicas
proceso de validación.                                                  de debiasing para garantizar que las respuestas del chatbot
                                                                        sean equitativas y no discriminatorias. Se sugiere una
                                                                        revisión periódica de los sesgos y la implementación de
Principales conclusiones                                                medidas correctivas cuando sea necesario.

El proceso de validación del chatbot de políticas ha demostrado      3. Fortalecer la seguridad y privacidad: si bien el chatbot
que este sistema basado en LLM puede ser una herramienta                cumple con los estándares básicos de protección de datos
valiosa para facilitar el acceso de los empleados a la información      personales, se recomienda realizar pruebas adicionales y
relevante de la compañía. Los resultados obtenidos en las               recurrentes de hacking ético y adoptar medidas de
diversas pruebas y evaluaciones indican que el chatbot cumple,          seguridad más robustas para prevenir posibles
en gran medida, con los requisitos de calidad, seguridad y              vulnerabilidades.
eficiencia establecidos por la organización.
                                                                     4. Establecer un plan de monitoreo y mejora continua: es
Entre las fortalezas identificadas, se destacan la precisión y          fundamental definir un proceso de seguimiento y
consistencia de las respuestas del chatbot, su capacidad para           evaluación periódica del desempeño del chatbot, con el fin
adaptarse a nuevos escenarios y su escalabilidad para manejar           de identificar oportunidades de mejora y garantizar su
altas cargas de trabajo. Además, la satisfacción de los usuarios        óptimo funcionamiento a largo plazo. Este plan debe incluir
con la herramienta es alta, lo que sugiere una buena aceptación         la recopilación de feedback de los usuarios, la actualización
y adopción por parte de los empleados.                                  regular de las políticas y su inclusión en la base de datos del
                                                                        chatbot, el monitoreo para mejorar los parámetros
Sin embargo, el proceso de validación también ha revelado               empleados en el RAG y su actualización, y la incorporación
algunas áreas de mejora que deben abordarse antes de la                 de nuevas técnicas y tecnologías cuando estén disponibles.
implementación definitiva del chatbot. En particular, se
recomienda:                                                          En conclusión, el chatbot de políticas ha demostrado tener
                                                                     potencial para mejorar la eficiencia y la accesibilidad de la
1. Mejorar la explicabilidad del modelo: es necesario                información en la compañía. Con la implementación de las
   desarrollar técnicas más avanzadas para que el chatbot            mejoras sugeridas y un enfoque de perfeccionamiento
   pueda proporcionar explicaciones claras y comprensibles           continuo, este sistema basado en LLM puede convertirse en una
   sobre su proceso de toma de decisiones. Esto aumentará la         herramienta estratégica para el éxito de la organización. La
   transparencia y la confianza de los usuarios en la                recomendación final ha sido proceder con la implementación
   herramienta. Si bien el componente de RAG se ha                   del chatbot, teniendo en cuenta las observaciones y
                                                                                                                                          49
   construido de manera que el LLM da una respuesta                  recomendaciones derivadas de este proceso de validación.
   autoexplicativa y hace referencia a la política
                                                                           Conclusiones




                                                                             “Los LLM son los únicos que pueden escribir una novela, traducirla a diez idiomas,
                                                                                                                             y aun así no entender la trama“.
                                                                                                                                                      Perplexity130




MANAGEMENT SOLUTIONS



50




El auge de los large language models: de los fundamentos a la aplicación
Los modelos de lenguaje a gran escala (LLM) representan un           Además, resulta necesario mantenerse al tanto de las últimas
avance significativo en el campo de la inteligencia artificial y     tendencias y avances en el campo de la validación de LLM,
están revolucionando la forma en que interactuamos con la            como el desarrollo de técnicas de explicabilidad más avanzadas,
tecnología y aprovechamos el procesamiento del lenguaje              el uso de LLM para explicar el comportamiento de otros LLM, la
natural. Su capacidad para procesar y generar texto coherente y      validación continua y monitorización en producción, y la
contextualizado abre un amplio abanico de aplicaciones en            alineación con los principios éticos y los requisitos regulatorios.
diversos sectores, desde la creación de contenido y el análisis de
sentimientos hasta la automatización de tareas y la mejora de la     El caso práctico presentado en este white paper ilustra cómo la
experiencia del usuario.                                             aplicación de un marco de validación personalizado puede
                                                                     ayudar a las organizaciones a identificar fortalezas y áreas de
Sin embargo, el desarrollo y despliegue de LLM también               mejora en sus sistemas basados en LLM, y a tomar decisiones
conlleva una serie de retos y consideraciones importantes. La        informadas sobre su implementación y perfeccionamiento
presencia de sesgos y alucinaciones en sus resultados, la falta de   continuo.
transparencia y explicabilidad de sus decisiones, los desafíos de
privacidad y seguridad de la información, y el alto consumo de       En definitiva, los LLM tienen un potencial muy significativo para
recursos computacionales son algunos de los principales              transformar la forma en que las empresas y la sociedad en                        51
desafíos que deben abordarse para garantizar un uso                  general se benefician de la inteligencia artificial. Sin embargo,
responsable y ético de estos sistemas.                               para aprovechar todo su potencial de manera segura y
                                                                     responsable, es imprescindible establecer un marco sólido de
Para hacer frente a estos retos, es fundamental establecer un        gobierno de la IA que aborde los retos asociados a su desarrollo
marco robusto de gobierno de la IA, especialmente en el ámbito       y despliegue, y que incluya un enfoque riguroso y
de la IA generativa y los LLM. Este marco debe abarcar todos los     multidimensional de validación. Solo así podrá garantizarse que
aspectos clave, incluyendo la estrategia, el apetito al riesgo, el   estos sistemas sean fiables, equitativos y estén alineados con los
gobierno, la organización, el marco de control (políticas y          valores y objetivos de las organizaciones y de la sociedad.
procedimientos), los datos, los sistemas y el reporting. Solo a
través de un enfoque integral y bien estructurado se podrá
garantizar un desarrollo y uso responsable de estas tecnologías.

Dentro de este marco de gobierno, la validación juega un papel
crucial. Es conveniente adoptar un enfoque multidimensional
que abarque todas las etapas del ciclo de vida de los LLM, desde
la calidad de los datos de entrada y la solidez del diseño del
modelo hasta la evaluación exhaustiva de sus resultados y la
implementación y uso adecuados. Este proceso de validación
debe combinar métricas cuantitativas estandarizadas con
técnicas de evaluación humana adaptadas al contexto
específico de cada caso de uso.
                                                                     130
                                                                       Perplexity AI es un motor de conversación y búsqueda de investigación basado
                                                                       en LLM fundado en 2022 por Andy Konwinski, Denis Yarats, Johnny Ho y
                                                                       Aravind Srinivas (ex OpenAI), que responde a las consultas mediante texto
                                                                       predictivo en lenguaje natural.
El auge de los large language models: de los fundamentos a la aplicación   52   MANAGEMENT SOLUTIONS




                                                                                                       Glosario
AGI (Artificial General Intelligence): inteligencia artificial       Embeddings: representaciones densas y continuas de
hipotética futura que igualaría o superaría la inteligencia          elementos discretos (como palabras, frases o documentos) en
humana en cualquier dominio intelectual, siendo capaz de             un espacio vectorial de alta dimensión, donde elementos
realizar cualquier tarea intelectual que un ser humano puede         similares tienen representaciones cercanas. Se utilizan en los
hacer.                                                               LLM para capturar relaciones semánticas y sintácticas entre los
                                                                     elementos del lenguaje.
Alucinaciones: generación de información o contenido por
parte de un LLM que parece plausible pero que no se basa en          Ética de la IA: disciplina que estudia los principios morales,
hechos reales o en el conocimiento adquirido durante el              valores y directrices que deben guiar el desarrollo, despliegue y
entrenamiento, llevando a inexactitudes o invenciones en las         uso de los sistemas de inteligencia artificial, con el objetivo de
respuestas del modelo.                                               garantizar que sean beneficiosos, justos, transparentes y
                                                                     alineados con los valores humanos.
CNN (Convolutional Neural Network): tipo de red neuronal
especializada en procesar datos con una topología de                 Evaluación humana: proceso de revisión y valoración
cuadrícula, como imágenes o series temporales. Las CNN               cualitativa del comportamiento y resultados de un sistema de IA
utilizan capas de convolución para extraer automáticamente           por parte de expertos y usuarios, que complementa las métricas       53
características locales y abstractas de los datos, y son             cuantitativas y permite detectar errores, sesgos o
ampliamente utilizadas en tareas de visión por computador y          comportamientos indeseados que podrían pasar
procesamiento de señales.                                            desapercibidos en una evaluación puramente automática.

Cuantización: técnica utilizada para reducir el tamaño y             Explicabilidad (XAI, eXplainable AI): propiedad de un modelo
acelerar la inferencia de los LLM, que consiste en reducir la        de IA que se refiere a su capacidad para proporcionar
precisión numérica de los pesos del modelo, pasando de               explicaciones comprensibles para los humanos sobre su
números en coma flotante a representaciones de menor                 funcionamiento interno, el razonamiento detrás de sus
precisión, como enteros o números en coma fija.                      predicciones y los factores que influyen en sus decisiones.

Datos de entrenamiento: conjunto de ejemplos utilizados para         Few-shot learning: capacidad de un modelo de aprendizaje
entrenar un modelo de aprendizaje automático, que incluyen           automático, especialmente los LLM, para aprender a realizar una
las entradas (features) y, en el caso del aprendizaje supervisado,   nueva tarea a partir de pocos ejemplos (desde uno hasta unas
las etiquetas o respuestas esperadas. La calidad y diversidad de     decenas), aprovechando el conocimiento previo adquirido
estos datos es crucial para el rendimiento y la generalización del   durante el preentrenamiento en grandes cantidades de datos.
modelo.
                                                                     Fine-tuning: técnica para adaptar un modelo de lenguaje
Efecto Eliza: fenómeno psicológico por el cual los usuarios          preentrenado a una tarea específica, mediante el entrenamiento
tienden a atribuir capacidades cognitivas y emocionales              adicional con un conjunto de datos más pequeño y
similares a las humanas a los sistemas de conversación basados       especializado en esa tarea. Permite aprovechar el conocimiento
en IA, a pesar de que estos sistemas no poseen una                   general del modelo y ajustarlo para obtener un alto rendimiento
comprensión real del lenguaje ni inteligencia general.               en aplicaciones concretas.
                                                                           Hacking ético: práctica de probar y desafiar un sistema de IA de     LLMOps (Large Language Model Operations): conjunto de
                                                                           manera controlada y con permiso, con el objetivo de identificar      prácticas, herramientas y procesos para gestionar de manera
                                                                           vulnerabilidades, fallos, sesgos o comportamientos no                eficiente y escalable el ciclo de vida completo de los LLM en
                                                                           deseados, para posteriormente corregirlos y mejorar la               entornos de producción, abarcando el entrenamiento,
                                                                           seguridad y robustez del sistema.                                    despliegue, monitorización, actualización y gobierno de estos




MANAGEMENT SOLUTIONS
                                                                                                                                                modelos.
                                                                           Instruction tuning: técnica de ajuste fino para LLM que consiste
                                                                           en proporcionar al modelo instrucciones, preguntas y ejemplos        Machine learning: rama de la inteligencia artificial que se centra
                                                                           de respuestas esperadas, con el objetivo de alinear su               en el desarrollo de algoritmos y modelos que permiten a los
                                                                           comportamiento con las expectativas y preferencias de los            sistemas aprender y mejorar automáticamente a través de la
                                                                           usuarios en un dominio específico.                                   experiencia, sin ser programados explícitamente para ello.

54                                                                         Inteligencia Artificial (IA): campo de la informática y la           Machine unlearning: conjunto de técnicas para eliminar o
                                                                           ingeniería que se dedica al desarrollo de sistemas capaces de        ”desaprender“ de manera selectiva cierta información o sesgos




El auge de los large language models: de los fundamentos a la aplicación
                                                                           realizar tareas que normalmente requieren inteligencia humana,       indeseados de un modelo de aprendizaje automático ya
                                                                           como el aprendizaje, el razonamiento, la percepción, la              entrenado, sin necesidad de reentrenarlo desde cero,
                                                                           interacción en lenguaje natural y la resolución de problemas.        permitiendo cumplir con requisitos de privacidad o corregir
                                                                                                                                                comportamientos no deseados.
                                                                           Inteligencia artificial generativa (GenAI): subcampo de la IA
                                                                           que se enfoca en la creación de modelos y algoritmos capaces         Métricas cuantitativas: medidas numéricas estandarizadas
                                                                           de generar contenido nuevo y original, como texto, imágenes,         utilizadas para evaluar de manera objetiva y consistente el
                                                                           vídeo, audio, código fuente o diseños 3D, aprendiendo patrones       rendimiento de un modelo de IA en tareas específicas, como la
                                                                           y características a partir de un conjunto de datos de                precisión, la exhaustividad, la exactitud o la eficiencia.
                                                                           entrenamiento.
                                                                                                                                                Modelo generativo: tipo de modelo de aprendizaje automático
                                                                           Large Language Models (LLM): modelos de aprendizaje                  diseñado para aprender la distribución de probabilidad
                                                                           profundo especializados en el procesamiento y generación de          subyacente a un conjunto de datos y generar nuevas muestras
                                                                           lenguaje natural, entrenados en enormes cantidades de texto y        que sean similares a los datos de entrenamiento, pudiendo
                                                                           con un gran número de parámetros (desde millones hasta               crear contenido nuevo y realista.
                                                                           billones), capaces de realizar diversas tareas lingüísticas con un
                                                                           alto nivel de comprensión y coherencia.                              Preentrenamiento: etapa inicial del entrenamiento de un LLM
                                                                                                                                                en la que se utiliza un gran corpus de texto no estructurado y
                                                                                                                                                sin etiquetar para que el modelo aprenda representaciones
                                                                                                                                                generales y patrones del lenguaje, adquiriendo un
                                                                                                                                                conocimiento amplio y robusto que luego puede ser adaptado
                                                                                                                                                a tareas específicas mediante fine-tuning.
Privacidad diferencial: técnica criptográfica utilizada para         Token: unidad discreta en la que se divide un texto para su
compartir información agregada sobre un conjunto de datos,           procesamiento por parte de un modelo de lenguaje. Los tokens
mientras se protege la privacidad de los individuos presentes en     pueden ser palabras, subpalabras o caracteres, y constituyen la
esos datos, introduciendo un ruido aleatorio que dificulta la        entrada básica para el entrenamiento y la inferencia de los LLM.
identificación de entradas individuales a partir de los resultados
del análisis.                                                        Tokenización: proceso de convertir un texto en una secuencia
                                                                     de tokens. La elección de la estrategia de tokenización tiene un
Prompt engineering: disciplina que se enfoca en diseñar,             impacto significativo en el rendimiento y la eficiencia del
optimizar y adaptar los prompts (entradas de texto) para             modelo.
obtener los mejores resultados posibles de los LLM en tareas
específicas, aprovechando técnicas como la inclusión de              Transformers: arquitectura de red neuronal profunda que
ejemplos, la especificación de formatos o la orientación paso a      utiliza mecanismos de atención para procesar y generar
paso.                                                                secuencias de forma paralela, en lugar de secuencialmente
                                                                     como las RNNs. Permite capturar dependencias a largo plazo y
Pruebas A/B: método experimental utilizado para comparar el          contextuales, siendo la arquitectura dominante para los LLM y
rendimiento de dos versiones diferentes de un sistema de IA (A       estableciendo el estado del arte en diversas tareas de
y B) o entre un sistema de IA y un enfoque alternativo (como un      procesamiento del lenguaje natural.
humano o un modelo base), con el objetivo de determinar cuál
funciona mejor según métricas predefinidas.                          Validación: proceso integral y multidisciplinar para evaluar un
                                                                     sistema de IA, especialmente LLM, en términos de rendimiento,
Regulación de la IA: conjunto de leyes, normativas, estándares       robustez, seguridad, equidad, explicabilidad y alineación con los
y directrices establecidos por gobiernos y organizaciones para       requisitos y valores éticos y sociales, combinando métricas
garantizar que el desarrollo, despliegue y uso de los sistemas de    cuantitativas y evaluación cualitativa por parte de expertos y
inteligencia artificial se realice de manera responsable, segura,    usuarios.
ética y alineada con los valores y derechos fundamentales de la
sociedad.

Retrieval-Augmented Generation (RAG): técnica utilizada en
los LLM que consiste en recuperar información relevante de una
base de conocimientos externa antes de generar una respuesta,
combinando así la capacidad de acceso a información
estructurada con la generación de lenguaje natural coherente y
fluido.

RNN (Recurrent Neural Network): tipo de red neuronal
diseñada para procesar secuencias de datos, como texto o                                                                                 55
series temporales. A diferencia de las redes neuronales
feedforward, las RNN tienen conexiones recurrentes que les
permiten mantener un estado interno y capturar dependencias
temporales. Variantes como LSTM y GRU han sido ampliamente
utilizadas en tareas de procesamiento del lenguaje natural
antes del auge de los transformers.

Seguridad (AI safety): disciplina que se enfoca en identificar,
prevenir y mitigar los riesgos potenciales asociados con el
desarrollo y uso de sistemas de IA avanzados, tanto a corto
como a largo plazo, incluyendo riesgos de seguridad, sesgos,
errores, mal uso o consecuencias no deseadas.

Sesgo: tendencia sistemática de un modelo de aprendizaje
automático a producir resultados que favorecen o perjudican
injustamente a ciertos grupos o individuos, debido a
características sensibles como el género, la etnia, la edad o la
orientación sexual, y que suele ser resultado de sesgos
presentes en los datos de entrenamiento o de decisiones
subóptimas durante el desarrollo del modelo.
El auge de los large language models: de los fundamentos a la aplicación   56   MANAGEMENT SOLUTIONS




                                                                                                       Bibliografía
Abhyankar, R. et al. (2024). APIServe: Efficient API Support for    CIO (2023). Chief AI Officer: What it takes to land the C-suite’s
Large-Language Model Inferencing.                                   hottest new job. https://www.cio.com/article/657977/chief-ai-
https://arxiv.org/abs/2402.01869. arXiv:2402.01869v1                officer-what-it-takes-to-land-the-c-suites-hottest-new-job.html

Alabdulmohsin, I. et al. (2024). CLIP the Bias: How Useful is       Cui, Q. et al. (2022). Contrastive Vision-Language Pre-training
Balancing Data in Multimodal Learning?                              with Limited Resources. https://arxiv.org/abs/2112.09331.
https://arxiv.org/html/2403.04547v1. arXiv:2403.04547v1             arXiv:2112.09331v3

Banerjee, I., et al. (2023). MLOps with enhanced performance        CommetML. https://www.comet.com/site/.
control and observability. https://arxiv.org/abs/2302.01061.
arXiv:2302.01061v1                                                  Datta, T. et al. (2023). Who's Thinking? A Push for Human-
                                                                    Centered Evaluation of LLMs using the XAI Playbook.
Bengio, Y. et al. (2003). A Neural Probabilistic Language Model.    https://arxiv.org/abs/2303.06223. arXiv:2303.06223v1
https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.p
df                                                                  Dettmers, T. et al. (2023). QLoRA: Efficient Finetuning of
                                                                    Quantized LLMs https://arxiv.org/abs/2305.14314.                     57
Bréal, M. (1883). Les lois intellectuelles du langage fragment de   arXiv:2305.14314v1
sémantique. Annuaire de l'Association pour l'encouragement
des études grecques en France. Vol. 17 (1883), pp. 132-142.         Devlin, J. et al. (2018). BERT: Pre-training of Deep Bidirectional
https://www.jstor.org/stable/44253893                               Transformers for Language Understanding.
                                                                    https://arxiv.org/abs/1810.04805. arXiv:1810.04805v2
Cambon, A. et al. (2023). Early LLM-based Tools for Enterprise
Information Workers Likely Provide Meaningful Boosts to             Duan, J. et al. (2023). Shifting attention to relevance: towards
Productivity. A first update from Microsoft’s research initiative   the uncertainty estimation of large language models.
on AI and Productivity.                                             https://arxiv.org/abs/2307.01379. arXiv:2307.01379v2

Chen, D. et al. (2023). Data-Juicer: A One-Stop Data Processing     Dun, C. et al. (2024). Sweeping Heterogeneity with Smart MoPs:
System for Large Language Models.                                   Mixture of Prompts for LLM Task Adaptation.
https://arxiv.org/abs/2309.02033. arXiv:2309.02033v3                https://arxiv.org/abs/2310.02842. arXiv:2310.02842v2

Chen, Y. et al. (2023). LongLoRA: Efficient Fine-tuning of Long-    Elazar, Y. et al. (2021). Measuring and Improving Consistency in
Context Large Language Models.                                      Pretrained Language Models.
https://arxiv.org/abs/2309.12307. arXiv:2309.12307v3                https://aclanthology.org/2021.tacl-1.60/.

Chiang, C. et al. (2023). Can Large Language Models Be an           Euronews (2023). 2023 was the year AI went mainstream. It was
Alternative to Human Evaluations?                                   also the year we started to panic about it.
https://arxiv.org/abs/2305.01937. arXiv:2305.01937v1                https://www.euronews.com/next/2023/12/27/2023-was-the-
                                                                    year-ai-went-mainstream-it-was-also-the-year-we-started-to-
Chu, T., Song, Z., Yang, C. (2023). How to Protect Copyright Data   panic-about-it
in Optimization of Large Language Models?
https://arxiv.org/abs/2308.12247. arXiv:2308.12247v1
                                                                           European Parliament (2024). Artificial Intelligence Act /          Huang, L. et al. (2023). A Survey on Hallucination in Large
                                                                           European Parliament legislative resolution of 13 March 2024 on     Language Models: Principles, Taxonomy, Challenges, and Open
                                                                           the proposal for a regulation of the European Parliament and of    Questions. https://arxiv.org/abs/2311.05232.
                                                                           the Council on laying down harmonized rules on Artificial          arXiv:2311.05232v1
                                                                           Intelligence (Artificial Intelligence Act) and amending certain
                                                                           Union Legislative Acts (COM(2021)0206 – C9-0146/2021 –             Hugging Face Datasets (2024). CodeParrot.
                                                                           2021/0106(COD)). https://artificialintelligenceact.eu/;            https://huggingface.co/codeparrot.
                                                                           https://eur-lex.europa.eu/legal-
                                                                           content/EN/TXT/?uri=celex%3A52021PC0206                            IAPP (2024). Global AI Law and Policy Tracker.
                                                                                                                                              https://iapp.org/resources/article/global-ai-legislation-tracker/
                                                                           European Commission (2024). Knowledge Center on
                                                                           Interpretation. https://knowledge-centre-                          iDanae 2T23 (2023): Large Language Models: una nueva era en
                                                                           interpretation.education.ec.europa.eu/en/news/what-large-          la inteligencia artificial. Cátedra iDanae. Newsletter trimestral
                                                                           language-model                                                     2T23. http://www.idanae-stem.com/

                                                                           Fisher, M., Campagna, G., Choi, E., Lam, M. S., Freund, S. N.,     iDanae 1T24 (2024): Hacia una inteligencia artificial sostenible.
                                                                           Yahav, E.,. (2021). DIY Assistant: A Multi-modal End-User          Cátedra iDanae. Newsletter trimestral 1T24. http://www.idanae-
                                                                           Programmable Virtual Assistant.                                    stem.com/
                                                                           https://dl.acm.org/doi/10.1145/3453483.3454046.
                                                                                                                                              Imperial, JM., et al. (2023). Flesch or Fumble? Evaluating
                                                                           Gartner (2023). What is generative AI?                             Readability Standard Alignment of Instruction-Tuned Language
                                                                           https://www.gartner.com/en/topics/generative-ai                    Models. https://arxiv.org/abs/2309.05454. arXiv:2309.05454v2

                                                                           Google DeepMind (2023). Levels of AGI: Operationalizing            IndesIA (2024). Barómetro de adopción de la inteligencia
                                                                           Progress on the Path to AGI. Meredith Ringel Morris; Jascha        artificial en las pymes españolas. https://www.indesia.org/wp-
                                                                           Sohl-Dickstein; Noah Fiedel; Tris Warkentin; Allan Dafoe;          content/uploads/2024/04/IndesIA.-Barometro-de-adopcion-de-
                                                                           Aleksandra Faust; Clement Farabet; and Shane Legg.                 la-inteligencia-artificial-en-las-pymes-espanolas-Edicion-2024.p
                                                                           arXiv:2311.02462v1                                                 df




MANAGEMENT SOLUTIONS
                                                                           Google + Implement (2023). The economic opportunity of             Jang et al. (2022). Knowledge unlearning for mitigating privacy
                                                                           generative AI in D9+. An Implement Consulting Group study          risks in language models. https://arxiv.org/abs/2210.01504.
                                                                           commissioned by Google.                                            arXiv:2210.01504.

                                                                           Gozalo-Brizuela, R., y Garrido-Merchán, E.C. (2023). A survey of   Jia, C. et al (2021). Scaling Up Visual and Vision-Language
                                                                           Generative AI Applications.                                        Representation Learning With Noisy Text Supervision.
58                                                                         https://ar5iv.labs.arxiv.org/html/2306.02781                       https://arxiv.org/abs/2102.05918. arXiv:2102.05918v2




El auge de los large language models: de los fundamentos a la aplicación
                                                                           Guo, Z. et al. (2023). Evaluating Large Language Models: A         Kahng, M. et al. (2024). LLM Comparator: Visual Analytics for
                                                                           Comprehensive Survey. https://arxiv.org/pdf/2310.19736.pdf.        Side-by-Side Evaluation of Large Language Models.
                                                                           arXiv:2310.19736v3                                                 https://arxiv.org/abs/2402.10524. arXiv:2402.10524v1

                                                                           Guzman, F. et al. (2015). How do Humans Evaluate Machine           Kuchnik, M. et al. (2023). Validating Large Language Models
                                                                           Translation. https://aclanthology.org/W15-3059.pdf.                with Realm. https://arxiv.org/abs/2211.15458.
                                                                                                                                              arXiv:2211.15458v2
                                                                           Fu, HY. et al. (2023). Estimating Large Language Model
                                                                           Capabilities without Labeled Test Data.                            Kudo, T., Richardson, J. (2018). SentencePiece: A simple and
                                                                           https://arxiv.org/abs/2305.14802. arXiv:2305.14802v2               language independent subword tokenizer and detokenizer for
                                                                                                                                              Neural Text Processing. https://arxiv.org/abs/1808.06226.
                                                                           Fu, X. et al (2024). Tiny Titans: Can Smaller Large Language       arXiv:1808.06226v1
                                                                           Models Punch Above Their Weight in the Real World for
                                                                           Meeting Summarization? https://arxiv.org/abs/2402.00841.           Lam, M. (2018). https://profiles.stanford.edu/monica-
                                                                           arXiv:2402.00841                                                   lam?tab=publications. Keeping the Internet Open with an
                                                                                                                                              Open-Source Virtual Assistant.
                                                                           Goyal, S. et al (2024). LLMGuard: Guarding Against Unsafe LLM
                                                                           Behavior. https://arxiv.org/abs/2403.00826. arXiv:2403.00826v1     Lee, C. et al (2024). OrchestraLLM: Efficient Orchestration of
                                                                                                                                              Language Models for Dialogue State Tracking.
                                                                           Hendrycks, D. et al (2021). Measuring Massive Multitask            https://arxiv.org/html/2311.09758v2. arXiv:2311.09758v2
                                                                           Language Understanding. https://arxiv.org/abs/2009.03300.
                                                                           arXiv:2009.03300v3
Lee, J. et al. (2022). Seq2Seq-SC: End-to-End Semantic                 Meeus, M. et al. (2024). Copyright Traps for Large Language
Communication Systems with Pre-trained Language Model.                 Models. https://arxiv.org/abs/2402.09363. arXiv:2402.09363v1
https://arxiv.org/abs/2210.15237. arXiv:2210.15237v2
                                                                       Mehta, S.V. et al. (2023). An Empirical Investigation of the Role of
Lester, B. et al. (2021). The Power of Scale for Parameter-Efficient   Pre-training in Lifelong Learning.
Prompt Tuning. https://arxiv.org/abs/2104.08691.                       https://arxiv.org/abs/2112.09153. arXiv:2112.09153v2
arXiv:2104.08691v2
                                                                       Mikolov, T. et al. (2013). Efficient Estimation of Word
Lewis, P., et al. (2020). Retrieval-augmented generation for           Representations in Vector Space.
knowledge-intensive NLP tasks.                                         https://arxiv.org/abs/1301.3781. arXiv:1301.3781v3.
https://arxiv.org/abs/2005.11401
                                                                       Minaee, S. et al. (2024). Large Language Models: A Survey.
Li, H. et al. (2024). Digger: Detecting Copyright Content Mis-         https://arxiv.org/abs/2402.06196. arXiv:2402.06196v2
usage in Large Language Model Training.
https://arxiv.org/abs/2401.00676. arXiv:2401.00676v1                   MindsDB (2024). A Comparative Analysis of Leading Large
                                                                       Language Models. https://mindsdb.com/blog/navigating-the-
Li, S. et al (2024). Evaluating Quantized Large Language Models.       llm-landscape-a-comparative-analysis-of-leading-large-
https://arxiv.org/abs/2402.18158. arXiv:2402.18158v1                   language-models

Li, Y. et al (2023). A Survey on Fairness in Large Language            Mökander, J. et al. (2023). Auditing large language models: a
Models. https://arxiv.org/abs/2308.10149. arXiv:2308.10149.            three-layered approach. arXiv:2302.08500v2

Liang, P. et al. (2023). Holistic Evaluation of Language Models.       Nasr, M., et al. (2023). https://arxiv.org/pdf/2311.17035.pdf.
https://arxiv.org/abs/2211.09110. arXiv:2211.09110v2                   arXiv:2311.17035v1

Liu, T. et al (2022). Autoregressive Structured Prediction with        Neelakantan, A. et al. (2022). Text and Code Embeddings by
Language Models. https://arxiv.org/abs/2210.14698.                     Contrastive Pre-Training. https://arxiv.org/abs/2201.10005.
arXiv:2210.14698v2                                                     arXiv:2201.10005v1

Liu, Y. et al (2024). Datasets for Large Language Models: A            NIST (2023). AI Risk Management Framework | NIST.
Comprehensive Survey. https://arxiv.org/abs/2402.18041.                https://www.nist.gov/itl/ai-risk-management-framework
arXiv:2402.18041v1
                                                                       Oneto, L., Chiappa, S. (2020). Fairness in Machine Learning.
Liu, Y. et al (2023). Robustness Over Time: Understanding              2012.15816.pdf (arxiv.org) arXiv:2012.15816v1
Adversarial Examples’ Effectiveness on Longitudinal Versions of
Large Language Models. https://arxiv.org/pdf/2308.07847.pdf.           OpenAI (2024). Prompt engineering.                                     59

arXiv:2308.07847v1                                                     https://platform.openai.com/docs/guides/prompt-engineering

Luo, Y. et al. (2023). An Empirical Study of Catastrophic              Ovadia, O. et al (2024). Fine-Tuning or Retrieval? Comparing
Forgetting in Large Language Models During Continual Fine-             Knowledge Injection in LLMs.
tuning. https://arxiv.org/pdf/2308.08747.pdf.                          https://arxiv.org/pdf/2312.05934.pdf. arXiv:2312.05934v3
arXiv:2308.08747v3
                                                                       Pankajakshan, R. et al (2024). Mapping LLM Security Landscapes:
Management Solutions (2023). Explainable Artificial Intelligence       A Comprehensive Stakeholder Risk Assessment Proposal.
(XAI): desafíos en la interpretabilidad de los modelos.                https://arxiv.org/html/2403.13309v1. arXiv:2403.13309v1.
https://www.managementsolutions.com/en/microsites/whitep
apers/explainable-artificial-intelligence                              Parikh, A. P., et al. (2016). A Decomposable Attention Model for
                                                                       Natural Language Inference. https://arxiv.org/abs/1606.01933.
Management Solutions (2022). AutoML, hacia la automatización           arXiv:1606.01933v2
de los modelos.
https://www.managementsolutions.com/es/publicaciones-y-                Penedo, G. et al (2023). The RefinedWeb Dataset for Falcon LLM:
eventos/informes-sectoriales/white-papers/auto-machine-                Outperforming Curated Corpora with Web Data, and Web Data
learning-hacia-la-automatizacion-de-los-modelos                        Only. https://arxiv.org/abs/2306.01116. arXiv:2306.01116v1

Management Solutions (2014). Model Risk Management:                    Pew Research Center (2023). Experts Predict the Best and Worst
Quantitative and Qualitative Aspects. Model Risk Management:           Changes in Digital Life by 2035.
Quantitative and qualitative aspects | Management Solutions
                                                                       Project Gutenberg (2024). https://www.gutenberg.org/.
                                                                           Rae, JW, et al (2021). Scaling Language Models: Methods,            Sinha, K. et al (2021). Masked Language Modeling and the
                                                                           Analysis & Insights from Training Gopher.                           Distributional Hypothesis: Order Word Matters Pre-training for
                                                                           https://arxiv.org/abs/2112.11446. arXiv:2112.11446                  Little. https://arxiv.org/abs/2104.06644. arXiv:2104.06644v2

                                                                           Rafailov, R. et al (2023). Direct Preference Optimization: Your     Soskek (2019). BookCorpus.
                                                                           Language Model is Secretly a Reward Model.                          https://github.com/soskek/bookcorpus.
                                                                           https://arxiv.org/abs/2305.18290. arXiv:2305.18290v2
                                                                                                                                               Su, J., et al (2021). Roformer: Enhanced transformer with rotary
                                                                           Rejeleene, R.; Xu, X.; Talburt, J.; (2024). Towards Trustable       position embedding. https://arxiv.org/abs/2104.09864.
                                                                           Language Models: Investigating Information Quality of Large         arXiv:2104.09864.
                                                                           Language Models. https://arxiv.org/abs/2401.13086.
                                                                           arXiv:2401.13086v1                                                  Sutskever, I. et al (2014). Sequence to Sequence Learning with
                                                                                                                                               Neural Networks. https://arxiv.org/abs/1409.3215.
                                                                           Risk.net. (2024). The bank quant who wants to stop gen AI           arXiv:1409.3215v3
                                                                           hallucinating. https://www.risk.net/risk-
                                                                           management/7959062/the-bank-quant-who-wants-to-stop-                The Next Web (2023). When will AGI arrive? Here’s what our tech
                                                                           gen-ai-hallucinating.                                               lords predict. https://thenextweb.com/news/when-will-agi-
                                                                                                                                               arrive-tech-experts-predict-artificial-general-intelligence
                                                                           Sachdeva, N., et al (2024). How to Train Data-Efficient LLMs.
                                                                           https://arxiv.org/html/2402.09668v1. arXiv:2402.09668v1             Tian, Y. et al (2024). TinyLLM: Learning a Small Student from
                                                                                                                                               Multiple Large Language Models.
                                                                           Samsi, S., et al (2023). From Words to Watts: Benchmarking the      https://arxiv.org/abs/2402.04616. arXiv:2402.04616
                                                                           Energy Costs of Large Language Model Inference.
                                                                           https://arxiv.org/pdf/2310.03003.pdf. arXiv:2310.03003v1            Tirumala, K. et al. (2023). D4: Improving LLM Pretraining via
                                                                                                                                               Document De-Duplication and Diversification.
                                                                           Sarti, G. et al (2023). Inseq: An Interpretability Toolkit for      https://arxiv.org/abs/2308.12284. arXiv:2308.12284v1
                                                                           Sequence Generation Models. [2302.13942] Inseq: An
                                                                           Interpretability Toolkit for Sequence Generation Models             UK Government (2023). The Bletchley Declaration by Countries




MANAGEMENT SOLUTIONS
                                                                           (arxiv.org). arXiv:2302.13942v3                                     Attending the AI Safety Summit, 1-2 November 2023.
                                                                                                                                               https://www.gov.uk/government/publications/ai-safety-
                                                                           Searle, J. (1980). Minds, Brains, and Programs. The Behavioral      summit-2023-the-bletchley-declaration/the-bletchley-
                                                                           and Brain Sciences, vol. 3. Cambridge University Press.             declaration-by-countries-attending-the-ai-safety-summit-1-2-no
                                                                           https://web.archive.org/web/20010221025515/http://www.bbs           vember-2023
                                                                           online.org/Preprints/OldArchive/bbs.searle2.html
                                                                                                                                               Vartziotis, T. et al (2024). Learn to Code Sustainably: An Empirical
60                                                                         Shaikh, O. et al. (2022). On Second Thought, Let's Not Think Step   Study on LLM-based Green Code Generation.
                                                                           by Step! Bias and Toxicity in Zero-Shot Reasoning.                  https://arxiv.org/html/2403.03344v1. arXiv:2403.03344v1.




El auge de los large language models: de los fundamentos a la aplicación
                                                                           https://arxiv.org/abs/2212.08061. arXiv:2212.08061v2
                                                                                                                                               Vaswani, A. et al. (2017). Attention Is All You Need.
                                                                           SHAP documentation. https://shap.readthedocs.io/                    https://arxiv.org/abs/1706.03762

                                                                           Shaw, P. et al (2018). Self-Attention with Relative Position        Wan, Z. et al (2024). Efficient Large Language Models: A Survey.
                                                                           Representations. https://arxiv.org/abs/1803.02155.                  https://arxiv.org/pdf/2312.03863.pdf. arXiv:2312.03863v3
                                                                           arXiv:1803.02155v2
                                                                                                                                               Wang, Q. et al (2024). LLMCheckup: Conversational Examination
                                                                           Sherstinsky, A. (2018). Fundamentals of Recurrent Neural            of Large Language Models via Interpretability Tools.
                                                                           Network (RNN) and Long Short-Term Memory (LSTM) Network.            [2401.12576] LLMCheckup: Conversational Examination of Large
                                                                           https://arxiv.org/abs/1808.03314. arXiv:1808.03314v10               Language Models via Interpretability Tools (arxiv.org).
                                                                                                                                               arXiv:2401.12576v1
                                                                           Shi, W. et al (2024). Detecting pretraining data from large
                                                                           language models. https://arxiv.org/abs/2310.16789.                  Wang, Y. et al (2024). Two-stage LLM Fine-tuning with Less
                                                                           arXiv:2310.16789v3                                                  Specialization and More Generalization.
                                                                                                                                               https://arxiv.org/html/2211.00635v3. arXiv:2211.00635v3
                                                                           Singh, C. et al (2024). Rethinking Interpretability in the Era of
                                                                           Large Language Models. https://arxiv.org/abs/2402.01761.            Wei, J. et al (2022). Chain-of-Thought Prompting Elicits
                                                                           arXiv:2402.01761v1                                                  Reasoning in Large Language Models.
                                                                                                                                               https://arxiv.org/abs/2201.11903. arXiv:2201.11903v6

Wenzek, G., et al (2019). CCNet: Extracting High Quality               Yu, C. et al. (2023). Unlearning bias in language models by
Monolingual Datasets from Web Crawl Data.                              partitioning gradients. https://aclanthology.org/2023.findings-
https://arxiv.org/abs/1911.00359. arXiv:1911.00359v2                   acl.375.pdf.

Wettig, A. et al. (2024). QuRating: Selecting High-Quality Data for    Yogarajan, V., et al (2023). Tackling Bias in Pre-trained Language
Training Language Models. https://arxiv.org/abs/2402.09739.            Models: Current Trends and Under-represented Societies.
arXiv:2402.09739v1                                                     https://arxiv.org/pdf/2312.01509.pdf. arXiv:2312.01509v1

Weights & Biases: The AI Developer Platform (wandb.ai).                Zaharia, M. et al (2018). Accelerating the Machine Learning
https://wandb.ai/site                                                  Lifecycle with MLflow.
                                                                       https://people.eecs.berkeley.edu/~matei/papers/2018/ieee_mlfl
Wikipedia (2024). Dumps.                                               ow.pdf.
https://dumps.wikimedia.org/zhwiki/latest/.
                                                                       Zeng, Y., et al (2023). CLIP2: Contrastive Language-Image-Point
Wired (2023). OpenAI’s CEO Says the Age of Giant AI Models Is          Pretraining from Real-World Point Cloud Data.
Already Over. https://www.wired.com/story/openai-ceo-sam-              https://arxiv.org/abs/2303.12417. arXiv:2303.12417v2
altman-the-age-of-giant-ai-models-is-already-over/
                                                                       Zhang, B. et al (2024). When Scaling Meets LLM Finetuning: The
Weizenbaum, J. (1966). ELIZA—a computer program for the                Effect of Data, Model and Finetuning Method.
study of natural language communication between man and                https://arxiv.org/abs/2402.17193. arXiv:2402.17193v1
machine. https://dl.acm.org/doi/10.1145/365153.365168
                                                                       Zhang, L. et al (2024). Enhancing Large Language Model
White House (2022). Blueprint for an AI Bill Of Rights. Making         Performance To Answer Questions and Extract Information
Automated Systems Work for the American People.                        More Accurately. https://arxiv.org/html/2402.01722v1.
https://www.whitehouse.gov/wp-                                         arXiv:2402.01722v1.
content/uploads/2022/10/Blueprint-for-an-AI-Bill-of-Rights.pdf
                                                                       Zhang, S. et al (2023). Instruction Tuning for Large Language
White House (2023). Executive Order on the Safe, Secure, and           Models: A Survey.
Trustworthy Development and Use of Artificial Intelligence.            https://www.researchgate.net/publication/373263398_Instructi
https://www.whitehouse.gov/briefing-room/presidential-                 on_Tuning_for_Large_Language_Models_A_Survey.
actions/2023/10/30/executive-order-on-the-safe-secure-and-
trustworthy-development-and-use-of-artificial-intelligence/            Zhang, Y. et al (2024). Bias Mitigation in Fine-tuning Pre-trained
                                                                       Models for Enhanced Fairness and Efficiency.
Wu, X. et al. (2023). Depn: Detecting and editing privacy neurons      https://arxiv.org/html/2403.00625v1. arXiv:2403.00625v1
in pretrained language models.
https://arxiv.org/abs/2310.20138. arXiv:2310.20138.                    Zhao, B., et al (2023). Tuning LayerNorm in Attention: Towards       61
                                                                       Efficient Multi-Modal LLM Finetuning.
Xin Zhao, W., et al. (2023). A Survey of Large Language Models.        https://arxiv.org/abs/2312.11420. arXiv:2312.11420v1
https://arxiv.org/abs/2303.18223. arXiv:2303.18223v13
                                                                       Zhou, C. et al (2023). LIMA: Less Is More for Alignment.
Xu, L. et al. (2023). Parameter-Efficient Fine-Tuning Methods for      https://arxiv.org/abs/2305.11206. arXiv:2305.11206v1
Pretrained Language Models: A Critical Review and Assessment.
https://arxiv.org/pdf/2312.12148.pdf. arXiv:2312.12148v1               Zhou, N., et al (2021). Bias, Fairness, and Accountability with AI
                                                                       and ML Algorithms. https://arxiv.org/abs/2105.06558.
Xu, Y. et al. (2021). Non-Autoregressive Text Generation with          arXiv:2105.06558v1
Pre-trained Language Models.
https://aclanthology.org/2021.eacl-main.18/

Xu, Z. et al. (2024). Hallucination is Inevitable: An Innate
Limitation of Large Language Models.
https://arxiv.org/abs/2401.11817. arXiv:2401.11817v1

Yang, J. et al. (2024). Harnessing the Power of LLMs in Practice: A
Survey on ChatGPT and Beyond.
https://arxiv.org/abs/2304.13712. arXiv:2304.13712v2

Yidiz, C. et al (2024). Investigating Continual Pretraining in Large
Language Models: Insights and Implications.
https://arxiv.org/html/2402.17400v1. arXiv:2402.17400v1
                                                                             Nuestro objetivo es superar las   Management Solutions es una firma internacional de servicios de
                                                                           expectativas de nuestros clientes   consultoría centrada en el asesoramiento de negocio, finanzas,
                                                                                                               riesgos, organización y procesos, tanto en sus componentes
                                                                              convirtiéndonos en socios de     funcionales como en la implantación de sus tecnologías
                                                                                                  confianza    relacionadas.

                                                                                                               Con un equipo multidisciplinar (funcionales, matemáticos,
                                                                                                               técnicos, etc.) de cerca de 4.000 profesionales, Management
                                                                                                               Solutions desarrolla su actividad a través de 46 oficinas (20 en
                                                                                                               Europa, 22 en América, 2 en Asia, 1 en África y 1 en Oceanía).

                                                                                                               Para dar cobertura a las necesidades de sus clientes,
                                                                                                               Management Solutions tiene estructuradas sus prácticas por
                                                                                                               industrias (Entidades Financieras, Energía, Telecomunicaciones y
                                                                                                               Otras industrias) y por líneas de actividad que agrupan una
                                                                                                               amplia gama de competencias: Estrategia, Gestión Comercial y
                                                                                                               Marketing, Gestión y Control de Riesgos, Información de Gestión
                                                                                                               y Financiera, Transformación: Organización y Procesos, y Nuevas




MANAGEMENT SOLUTIONS
                                                                                                               Tecnologías.

                                                                                                               El área de I+D da servicio a los profesionales de Management
                                                                                                               Solutions y a sus clientes en aspectos cuantitativos necesarios
                                                                                                               para acometer los proyectos con rigor y excelencia, a través de
                                                                                                               la aplicación de las mejores prácticas y de la prospección
                                                                                                               continua de las últimas tendencias en inteligencia artificial, data
62                                                                                                             science, machine learning, modelización y big data.




El auge de los large language models: de los fundamentos a la aplicación
                                                                                                               Javier Calvo Martín
                                                                                                               Socio de Management Solutions
                                                                                                               javier.calvo.martin@managementsolutions.com
                                                                                                               Manuel Ángel Guzmán Caba
                                                                                                               Socio de Management Solutions
                                                                                                               manuel.guzman@managementsolutions.com
                                                                                                               Luz Ferrero Peña
                                                                                                               Gerente de Management Solutions
                                                                                                               luz.ferrero@msgermany.com.de
                                                                                                               Segismundo Jiménez Láinez
                                                                                                               Gerente de Management Solutions
                                                                                                               segismundo.jimenez@msspain.com
                                                                                                                                      www.managementsolutions.com
     Management Solutions, servicios profesionales de consultoría

     Management Solutions es una firma internacional de consultoría centrada en el
     asesoramiento de negocio, finanzas, riesgos, organización, tecnología y procesos,

     Para más información visita www.managementsolutions.com

     Síguenos en:

     © Management Solutions. 2024
     Todos los derechos reservados




Madrid Barcelona Bilbao Coruña Málaga London Frankfurt Düsseldorf Paris Amsterdam Copenhagen Oslo Stockholm Warszawa Wroclaw Zürich Milano
Roma Bologna Lisboa Beijing Istanbul Johannesburgo Sydney Toronto New York New Jersey Boston Pittsburgh Atlanta Birmingham Houston Miami
SJ de Puerto Rico San José Ciudad de México Monterrey Querétaro Medellín Bogotá Quito São Paulo Rio de Janeiro Lima Santiago de Chile Buenos Aires
