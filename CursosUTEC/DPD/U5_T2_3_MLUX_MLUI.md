---
curso: DPD
titulo: U5_T2_3_MLUX MLUI.pptx
slides: 82
fuente: U5_T2_3_MLUX MLUI.pptx.pdf
---

# U5_T2_3_MLUX MLUI.pptx

## Índice

1. [Importancia de UX en productos de datos](#importancia-de-ux-en-productos-de-datos)
2. [Planificación del producto de datos](#planificación-del-producto-de-datos)
3. [Research y requerimientos del producto](#research-y-requerimientos-del-producto)
4. [¿Qué es UX?](#qué-es-ux)
5. [Discrepancia entre datos y UX](#discrepancia-entre-datos-y-ux)
6. [¿Qué es UI?](#qué-es-ui)
7. [Elementos y prácticas de diseño de interfaces](#elementos-y-prácticas-de-diseño-de-interfaces)
8. [Data-Driven User Interfaces (MLUI)](#data-driven-user-interfaces-mlui)
9. [Human-Machine Interaction (MLUX)](#human-machine-interaction-mlux)
10. [Case Study: Discapacidad visual en India](#case-study-discapacidad-visual-en-india)
11. [Conclusiones](#conclusiones)
12. [Glosario](#glosario)

## Importancia de UX en productos de datos

### Objetivos de la sesión

Al ﬁnal de la clase, los estudiantes deberán comprender la importancia de una interfaz de usuario efectiva para productos basados en datos y machine learning, y cómo diseñar estas interfaces para maximizar la usabilidad y el valor para el usuario

**Figura:** Slide titulada «Objetivos de la Sesión» en negrita negra centrada. Párrafo central con el objetivo de la sesión en tipografía sans-serif gris oscuro. A la derecha del texto, icono de contorno azul de una persona junto a un documento. la forma superior tiene filtro cian/azul. (slide 4)
### Resistencia de usuario y valor del producto de datos

**Resistencia de Usuario**

Los usuarios y las partes interesadas no quieren inteligencia artiﬁcial y análisis, incluso si lo pidieron.

**Uso Ético de los Datos**

No puedes crear "valor comercial" repetidamente si las personas ni siquiera están usando tu modelo, dashboards o aplicaciones de soporte de decisiones.

**Valor del Producto de Datos**

Podrías tener una solución técnicamente correcta, pero si la experiencia de usuario (UX) de tu producto de datos es mala, los usuarios no lo usarán y las partes interesadas no verán el valor de tu solución de datos.

**Figura:** Slide organizada en tres filas horizontales. Cada fila tiene un recuadro de encabezado turquesa/cian a la izquierda con texto en negrita centrado, y un recuadro gris claro más largo a la derecha con texto explicativo alineado a la izquierda. Fila 1: encabezado «Resistencia de Usuario» / texto sobre usuarios y partes interesadas que no quieren IA y análisis. Fila 2: encabezado «Uso Ético de los Datos» / texto sobre valor comercial y uso de modelos, dashboards o aplicaciones de soporte de decisiones. Fila 3: encabezado «Valor del Producto de Datos» / texto sobre solución técnicamente correcta con mala UX. (slide 5)
## Planificación del producto de datos

### Problemas y oportunidades

Planiﬁcar nuestro Producto de Datos

1. Problemas y Oportunidades

¿Cómo podemos ayudar a los clientes?

- Optimize Repetitive Task
- Assist with Decisions
- Operate Autonomously

1. ¿Existe trabajo repetitivo y no creativo que los usuarios realizan y que consume mucho tiempo?

reorganizando y agrupando escaneos. No solo es una pérdida de tiempo, sino también una tarea irritante que los especialistas deben realizar muchas veces al día.

https://www.youtube.com/watch?v=Rj4Nwgk08Mc&t=77s&ab_channel=GoogleCloudTech

**Figura:** Slide titulada «Planiﬁcar nuestro Producto de Datos» con «Producto de Datos» en negrita. Sección «1. Problemas y Oportunidades» con pregunta guía «¿Cómo podemos ayudar a los clientes?». En la parte superior derecha, tres objetivos estratégicos en texto: «Optimize Repetitive Task», «Assist with Decisions», «Operate Autonomously». Pregunta numerada «1. ¿Existe trabajo repetitivo y no creativo que los usuarios realizan y que consume mucho tiempo?». Ilustración central de ﬂujo de trabajo: a la izquierda, pila desordenada de radiografías (cráneo, tórax, extremidades); en el centro, flecha grande apuntando a la derecha superpuesta con diagrama de red neuronal (nodos y conexiones); a la derecha, cuatro radiografías organizadas y etiquetadas: «Skull», «Thorax», «Abdomen», «Extremity». Enlace de YouTube a GoogleCloudTech en la parte inferior.

2. ¿Existen tareas que necesitan ser revisadas dos veces debido a errores?

Al escribir esta publicación, estoy conﬁando en Grammarly y en sus algoritmos de IA para ayudarme.

3. ¿Puede la asistencia de producto hacer que los usuarios o toda la organización sean más eﬁcientes?

En 2016, el Hospital Oftalmológico Moorﬁelds tuvo 7 mil referencias urgentes para personas que corrían el riesgo de perder la vista. Los pacientes tenían que esperar hasta 6 semanas antes de ver a un especialista debido al gran número de citas. Resultó que solo 800 de las 7 mil referencias eran urgentes.

DeepMind Health Research

Ahora está funcionando al nivel de expertos mundiales

**Figura:** Slide con dos secciones numeradas. Sección 2: pregunta en turquesa «¿Existen tareas que necesitan ser revisadas dos veces debido a errores?» con ejemplo de Grammarly. Sección 3: pregunta en turquesa «¿Puede la asistencia de producto hacer que los usuarios o toda la organización sean más eﬁcientes?». Fotografía central de un profesional médico (hombre con gafas y uniforme blanco con cuello granate) trabajando con equipo de diagnóstico; monitor de fondo muestra escaneos médicos coloridos del ojo/retina. Debajo de la foto, enlace subrayado azul «DeepMind Health Research». Texto a la derecha de la imagen sobre el Hospital Oftalmológico Moorﬁelds; frases resaltadas en azul claro: «7 mil referencias urgentes para personas que corrían el riesgo de perder la vista» y «Resultó que solo 800 de las 7 mil referencias eran urgentes». Párrafo final en la parte inferior con «DeepMind» y «diagnosticar casos urgentes y reducir el número de deterioros» resaltados en azul claro.

5. ¿Existen tareas adicionales que los usuarios deben completar para realizar su trabajo principal?

6. ¿Tiene un usuario que analizar los datos y tomar decisiones una y otra vez, muchas veces al día?

En seguros, se utiliza la IA para calcular el costo de los daños basado en imágenes de un automóvil. Entrenada con una biblioteca de fotografías de accidentes pasados, la IA estima los costos de reparación. La IA minimiza el tiempo de espera para el pago y reduce el trabajo para los inspectores de seguros.

https://tractable.ai/

| Parte | VISIBLE | OUTCOME | CONF. | LABOR |
|-------|---------|---------|-------|-------|
| Hood | 100% | Replace | 99% | 1-3 |
| Grille | 100% | Replace | 90% | 1-2 |
| Bumper, Front | 100% | Replace | 84% | 2-4 |
| Headlamp, Right | 100% | Replace | 71% | 1-2 |
| Headlamp, Left | 99% | Intact | 73% | 0-1 |

**Figura:** Slide con dos preguntas en turquesa en la parte superior: pregunta 5 sobre tareas adicionales y pregunta 6 sobre análisis repetitivo de datos y decisiones. Captura de pantalla central de la interfaz «TRACTABLE»: foto frontal de un automóvil negro con daños visibles; debajo, tabla con columnas VISIBLE, OUTCOME, CONF. (Confidence) y LABOR para cinco partes del vehículo (Hood, Grille, Bumper Front, Headlamp Right, Headlamp Left); botones de resultado «Replace» en rojo e «Intact» en verde; anillos de confianza en rojo o verde según el resultado. Enlace «https://tractable.ai/» debajo de la captura. Texto explicativo a la derecha sobre uso de IA en seguros; frases resaltadas en azul: «IA para calcular el costo de los daños basado en imágenes de un automóvil» y «La IA minimiza el tiempo de espera para el pago y reduce el trabajo para los inspectores de seguros».

7. ¿Tienen que personalizar el trabajo para sus clientes?

https://edrone.me/blog

El contenido de marketing de Zalando es generado por algoritmos. Utilizan información sobre compras pasadas y listas de deseos de sus clientes para personalizar los materiales de marketing.

**Figura:** Slide con pregunta 7 en turquesa en la parte superior izquierda. Enlace «https://edrone.me/blog» en la esquina superior derecha junto al logo de UTEC. Tres capturas de pantalla comparativas del sitio web de Zalando en el centro: (1) «FIRST VISIT»: página de inicio genérica con tres imágenes promocionales grandes etiquetadas «WOMEN», «MEN» y «KIDS», y miniaturas de productos genéricos debajo; (2) «NEXT VISIT»: interfaz adaptada mostrando moda masculina con énfasis en «SNEAKERBOOTS ON TREND»; (3) «MACHINE LEARNING»: interfaz altamente personalizada bajo encabezado «FOR YOU» con recomendaciones específicas (reloj plateado, zapatillas rosas, camisas particulares). Párrafo explicativo en la parte inferior sobre marketing de Zalando generado por algoritmos.

8. ¿Existe información que podría cambiar el negocio de tus usuarios que no está disponible ahora?

Danny Lange (ML en Uber) recomienda usar el proceso de pensamiento "Si solo supiéramos ____" para descubrir posibilidades de negocio inesperadas.

- "Si solo supiéramos cuántas ambulancias necesitamos en cualquier momento",
- "Si solo supiéramos cuándo encender el televisor para ver el momento más importante del juego".

Los partidos de cricket, que pueden extenderse por 5 días, tienen solo medio minuto de momentos cruciales en 30 horas de juego. Foxtel desarrolló un algoritmo de IA, llamado Monty, entrenado con videos históricos para predecir eventos significativos, como la caída de un wicket, y notificar a los fans en tiempo real.

https://youtu.be/Bn7aMIbaxOw

**Figura:** Slide con pregunta 8 en la parte superior. Texto introductorio sobre Danny Lange (ML en Uber) y el proceso de pensamiento «Si solo supiéramos ____». Dos bullets con ejemplos hipotéticos. Imagen central con fondo rojizo de un jugador de cricket con casco y camiseta; superpuesto, diagrama de flujo con tres nodos conectados por flechas: (1) «opta Dataset» representado por icono de pelota de cricket; (3) «MONTY Prediction» representado por icono de nodos conectados (red neuronal/predicción). Texto a la derecha de la imagen sobre partidos de cricket y algoritmo Monty de Foxtel; frase «Foxtel desarrolló un algoritmo de IA, llamado Monty, entrenado con videos históricos para predecir eventos significativos» resaltada en azul. Enlace de YouTube en la parte inferior. (slides 6–10)
### Acceso y viabilidad de los datos

1. ¿Tienes acceso a los datos? ¿Puedes adquirir los datos que necesitas? ¿Están los usuarios dispuestos a compartir los datos? ¿Qué datos están dispuestos a proporcionar?

1. ¿Tienes permiso para usar los datos? ¿Hay regulaciones con las que debes cumplir?

1. ¿Puedes asegurar que los datos de los usuarios estén seguros?

1. ¿Puedes asegurar que los datos sean conﬁables y estén actualizados?

1. ¿Vale la pena? Recopilar datos, mantenerlos en forma, construir un modelo, y probar e iterar consumen tanto tiempo como dinero. ¿Tienes un equipo? ¿Cuál es el compromiso? Quizás necesitas actualizar el modelo todos los días y resulta muy costoso.

1. ¿Puedes resolver los problemas con reglas y lógica simples?

**Figura:** Slide con lista de seis preguntas críticas, todas numeradas con «1.». Frases clave resaltadas en azul claro: «¿Tienes acceso a los datos?», «¿Qué datos están dispuestos a proporcionar?», «¿Tienes permiso para usar los datos?», «seguros», «confiables», «actualizados», y la pregunta final completa «¿Puedes resolver los problemas con reglas y lógica simples?». Icono de bandera roja en un asta en la esquina inferior izquierda, sugiriendo puntos de alerta o «red flags». (slide 11)
## Research y requerimientos del producto

### Research

**2. Research**

- ¿Quiénes son los usuarios?
- ¿Cuál es su experiencia?
- ¿Son expertos en tecnología?
- ¿Qué valor esperan obtener de este producto?
- ¿Qué tan familiarizados están con los productos basados en IA?

Comprender las actitudes de los usuarios hacia el uso de datos

- ¿Los usuarios están dispuestos a compartir sus datos?
- ¿Qué datos están dispuestos a proporcionar y qué datos no?
- ¿Existen políticas y regulaciones de la empresa o de la industria?
- ¿Qué se considera ético/antiético?

**Figura:** Slide titulada «2. Research» en tipografía turquesa y negrita. Primera sección con cinco bullets de preguntas sobre usuarios en texto negro. Segunda sección con subencabezado en azul «Comprender las actitudes de los usuarios hacia el uso de datos» seguido de cuatro bullets sobre disposición a compartir datos, políticas y ética. Icono abstracto de tres formas entrelazadas azul y turquesa en la esquina inferior derecha.

Identiﬁcar el contexto en el que los usuarios utilizarán el producto

- ¿En qué entorno se produce el problema?
- ¿Qué están haciendo antes y después?
- ¿Qué tipo de herramientas utilizan?
- ¿Con quién interactúan?
- ¿Qué otras necesidades o problemas pueden ocurrir al mismo tiempo y en el mismo entorno?

¿Qué otras herramientas hay en su ﬂujo de trabajo?

- Si su producto es parte de un ﬂujo de trabajo, otras herramientas pueden afectar los hábitos y expectativas de los usuarios.
- ¿Utilizan la IA en su trabajo? ¿Qué tipo de IA?
- ¿Cómo están acostumbrados a interactuar con otros sistemas basados en IA?
- ¿Hay herramientas complementarias que debería tener en cuenta?

**Figura:** Slide dividida en dos secciones de texto. Sección superior izquierda: encabezado «Identiﬁcar el contexto en el que los usuarios utilizarán el producto» con cinco bullets sobre entorno, actividades antes/después, herramientas, interacciones y necesidades concurrentes. Sección inferior derecha: encabezado «¿Qué otras herramientas hay en su ﬂujo de trabajo?» con cuatro bullets sobre impacto de otras herramientas en el ﬂujo de trabajo, uso de IA, interacción con sistemas de IA y herramientas complementarias.

¿Quiénes son los competidores?

- ¿Son competidores directos?
- ¿Sería posible que su cliente cambiara de una herramienta a otra? ¿Cuánto dinero y esfuerzo costaría?

¿Qué tendencias hay en la industria?

- En el mundo B2B y empresarial, las tendencias y los informes de análisis de las empresas de investigación y consultoría tienen un impacto considerable.
- ¿En qué fuentes de información confían?
- ¿Se asocian con alguna de las empresas de consultoría?

**Figura:** Slide con dos secciones de texto dispuestas en diagonal. Sección superior izquierda: encabezado «¿Quiénes son los competidores?» con dos bullets sobre competidores directos y costo de cambio de herramienta. Sección inferior derecha: encabezado «¿Qué tendencias hay en la industria?» con tres bullets sobre tendencias B2B, fuentes de información y asociación con empresas de consultoría. Icono de hexágonos azules y grises en la esquina inferior derecha.

¿De qué parte del trabajo están orgullosos los usuarios o se resistirían a automatizar?

- La automatización del trabajo puede ser un tema delicado.
- ¿Cómo abordamos los miedos de los usuarios y explicamos los beneficios de la IA?
- Algunos trabajos están vinculados a las bonificaciones. Su herramienta podría automatizar o reemplazar este trabajo. ¿Cómo puede ayudar a los clientes a adaptarse no solo a una nueva herramienta, sino también a la nueva cultura que la rodea?

¿Qué nivel de automatización debe buscar?

- ¿Debería aspirar a un sistema autónomo o a la colaboración entre la IA y el ser humano?
- Hay tareas que los usuarios delegarían a la IA, pero hay actividades que las personas prefieren hacer por sí mismas. ¿Cuáles son estas tareas?
- ¿Cuánto tiempo y dinero ahorraría a sus clientes la automatización total? ¿Vale la pena? ¿Cuáles son las desventajas de la automatización total?

**Figura:** Slide dividida en dos secciones. Sección superior izquierda: encabezado «¿De qué parte del trabajo están orgullosos los usuarios o se resistirían a automatizar?» con tres bullets sobre delicadeza de la automatización, miedos de usuarios y bonificaciones vinculadas al trabajo. Sección inferior derecha: encabezado «¿Qué nivel de automatización debe buscar?» con tres bullets sobre sistema autónomo vs. colaboración humano-IA, tareas delegables vs. preferidas, y costo-beneficio de automatización total. (slides 12–15)
### Precisión, flujo de datos y frecuencia de actualización

¿Qué nivel de precisión se requiere?

- ¿Cuánto costaría el error? En términos de dinero, tiempo, reputación, salud, deleite y experiencia. ¿Son aceptables los errores? ¿Cuáles son las consecuencias de los resultados falsos positivos/negativos para la tarea? ¿Sus clientes preferirían tener algunos errores en la predicción que resolver las tareas manualmente?
- Cuanto más precisos sean los resultados, menos predicciones hará la IA.

¿Cómo puede garantizar el flujo de datos?

- La cantidad de datos de entrenamiento es uno de los componentes más importantes para construir un sistema preciso.
- Cuando se trabaja en una solución de IA, conseguir los datos de entrenamiento iniciales y apoyar el flujo continuo de datos es el trabajo del equipo de producto.

**Figura:** Slide dividida en dos secciones de texto y una captura de pantalla central. Sección superior izquierda: encabezado «¿Qué nivel de precisión se requiere?» con dos bullets sobre costo del error (dinero, tiempo, reputación, salud, deleite, experiencia), aceptabilidad de errores, falsos positivos/negativos, preferencia de usuarios, y relación entre precisión y cantidad de predicciones. Captura de pantalla central de un listado de Zillow: propiedad con precio «$458,500»; historial de «Zestimate» con gráfico de valor estimado de la propiedad a lo largo del tiempo (2013–2020); tooltip emergente: «We calculate the estimated sales range based on the current market and the info we have about this home.». Sección inferior derecha: encabezado «¿Cómo puede garantizar el flujo de datos?» con dos bullets sobre importancia de datos de entrenamiento y responsabilidad del equipo de producto. Icono de hexágonos y flechas azules en la esquina inferior derecha.

¿Con qué frecuencia deben actualizarse los resultados?

- ¿Puede la predicción calcularse por adelantado o debe actualizarse cada vez que llega nueva información (clics, me gusta, fotos, escáneres)? Esta pregunta es importante para los requisitos técnicos.

**Figura:** Slide con encabezado «¿Con qué frecuencia deben actualizarse los resultados?» y un bullet sobre cálculo anticipado de predicciones vs. actualización en tiempo real ante nueva información (clics, me gusta, fotos, escáneres), señalando su importancia para requisitos técnicos. (slides 16–17)
### Requerimientos del negocio

**3. Requerimientos del negocio**

| Requerimiento | Nivel |
|---------------|-------|
| Accuracy | ~80% |
| Computational cost | ~60% |
| Explainability | ~45% |
| Level of autonomy | ~100% |
| Timeliness | ~100% |

**Figura:** Slide titulada «3. Requerimientos del negocio» en tipografía turquesa oscura. Cinco requerimientos de negocio listados verticalmente a la izquierda, cada uno con una barra horizontal de progreso en color magenta/rosa sobre una línea gris de fondo que indica su nivel relativo: «Accuracy» aproximadamente al 80%; «Computational cost» aproximadamente al 60%; «Explainability» aproximadamente al 45%; «Level of autonomy» al 100%; «Timeliness» al 100%. Etiquetas de requerimientos en gris oscuro/morado. (slide 18)
### Diseño de interfaz en el proceso de producto de datos

**4. Diseño de Interfaz**

**Figura:** Captura de pantalla de una interfaz de visualización y análisis de datos tipo herramienta de business intelligence (similar a Power BI). Título «4. Diseño de Interfaz» en turquesa grande en la parte superior izquierda. Tres secciones verticales: (1) Barra lateral izquierda estrecha con iconos de navegación (Home, Files, Search, Visualizations, Tools, Chat, Document); en la parte inferior, campo de texto «Ask a question» con icono de más. (2) Panel central «Assistant»: encabezado «mod1» con icono de actualización; texto «Total number of rows: 5397»; sugerencia de explorar campos relacionados con «Hour»; campos disponibles como enlaces azules: Street Name, Hundred Block, Local Area, Case Type, Minute; botón azul en forma de píldora «show Hour and Local Area»; visualización titulada «Hour and Local Area» mostrando un gráfico circular de puntos multicolores (tipo bubble chart o grid hexagonal); leyenda a la derecha con categorías de «Local Area»: Arbutus, Downtown, Dunbar, Fairview, Grandview, Hastings, Kensington, Kerrisdale, Killarney, Kitsilano, Marpole, cada una con color distinto; enlace «Show related visualizations» en el pie. (3) Panel derecho «Report Canvas»: texto «Drag and drop data here to filter this tab.»; tabla de datos con dos columnas «Hour» y «Local Area»: fila 0 (Hour 0) lista Grandview-Woodland, Kensington-Cedar Cottage, Mount Pleasant; fila 1 (Hour 1) lista Arbutus Ridge, Hastings-Sunrise; barra de desplazamiento vertical. (slide 19)
## ¿Qué es UX?

### DATA y UX

data = Aprendizaje Automático, IA, Análisis de Datos, Inferencia Estadística, y más

ux = Diseño de Experiencia de Usuario, Investigación, Diseño de Interacción, Arquitectura de Información, y más

**Figura:** En el centro, diagrama con las palabras «DATA» (izquierda) y «UX» (derecha) en tipografía grande, negrita y color turquesa/cian. Dos líneas curvas turquesas — una arriba y otra abajo — conectan ambas palabras formando un bucle ovalado que sugiere una relación cíclica o recíproca entre DATA y UX. En la parte inferior izquierda, dos líneas de definición en color turquesa: «data = Aprendizaje Automático, IA, Análisis de Datos, Inferencia Estadística, y más» y «ux = Diseño de Experiencia de Usuario, Investigación, Diseño de Interacción, Arquitectura de Información, y más».

¿Cómo creo una experiencia de usuario (UX) aceptable en un producto de Datos?

¿Por qué la mayoría de los productos de ML fracasan en el mundo real?

¿Cómo convierto mis hallazgos de UX en mejoras reales para el producto?

Interacción con el Modelo

**Figura:** En la parte central, tres preguntas en tipografía negra sans-serif, alineadas verticalmente: (1) «¿Cómo creo una experiencia de usuario (UX) aceptable en un producto de Datos?», (2) «¿Por qué la mayoría de los productos de ML fracasan en el mundo real?», (3) «¿Cómo convierto mis hallazgos de UX en mejoras reales para el producto?». En la parte inferior central, título grande en negrita negra: «Interacción con el Modelo».

Los diseñadores UX trabajan en un modo bastante conceptual, con representaciones aproximadas del mundo, para mejorar los aspectos subjetivos de un producto.

**Figura:** En el lado izquierdo, oración principal en tipografía sans-serif con palabras resaltadas en azul brillante/cian y el resto en negro: «Los diseñadores **UX trabajan** en un **modo bastante conceptual**, con **representaciones aproximadas del mundo**, **para mejorar los** aspectos subjetivos de un **producto**.». en uno de los marcos inferiores se lee parcialmente «INGENIERÍA» en un muro de concreto al fondo.

Diseño UX

https://joesteinkamp.com/my-favorite-ux-design-process-diagrams/

**Figura:** Slide titulada «Diseño UX» en tipografía grande negra en la esquina superior izquierda. En el centro, diagrama del proceso Design Thinking compuesto por cinco hexágonos conectados en diagonal descendente de izquierda a derecha, cada uno con etiqueta en mayúsculas blancas: (1) hexágono azul «EMPATHIZE», (2) hexágono verde «DEFINE», (3) hexágono amarillo/naranja «IDEATE», (4) hexágono naranja/rojo «PROTOTYPE», (5) hexágono rojo oscuro «TEST». En la parte inferior izquierda, URL subrayada: «https://joesteinkamp.com/my-favorite-ux-design-process-diagrams/».

Crafting
How do I create this UX?

Researching
What is a good UX?

Mapping
What does our UX look like?

Monitoring
Where is our UX failing?

**Figura:** Cuatro cuadrantes dispuestos en una cuadrícula 2×2, todo el texto en color turquesa/cian. Cuadrante superior izquierdo: título «Crafting» y pregunta «How do I create this UX?». Cuadrante superior derecho: título «Researching» y pregunta «What is a good UX?». Cuadrante inferior izquierdo: título «Mapping» y pregunta «What does our UX look like?». Cuadrante inferior derecho: título «Monitoring» y pregunta «Where is our UX failing?».

Idealistic

Crafting
How do I create this UX?

Researching
What is a good UX?

Creative

Descriptive

Mapping
What does our UX look like?

Monitoring
Where is our UX failing?

Realistic

**Figura:** Matriz 2×2 definida por dos ejes perpendiculares en color turquesa. Eje vertical: «Idealistic» (arriba) a «Realistic» (abajo). Eje horizontal: «Creative» (izquierda) a «Descriptive» (derecha). Cuatro cuadrantes con título y pregunta en turquesa: cuadrante superior izquierdo (Idealistic + Creative) — «Crafting» / «How do I create this UX?»; cuadrante superior derecho (Idealistic + Descriptive) — «Researching» / «What is a good UX?»; cuadrante inferior izquierdo (Realistic + Creative) — «Mapping» / «What does our UX look like?»; cuadrante inferior derecho (Realistic + Descriptive) — «Monitoring» / «Where is our UX failing?». (slides 21–26)
### Un sistema hipotético: sastre tradicional vs. ajuste virtual

El usuario va a la tienda.

Sastre recoge medidas

El usuario espera de 3 a 4 semanas

El usuario vuelve a la tienda.

El usuario se prueba la prenda.

El sastre hace los cambios finales

El usuario espera 1-2 semanas Usuario

Recibe la camisa por correo

**Figura:** Slide con fotografía de fondo de un hombre vestido con traje gris texturizado (chaqueta, chaleco azul marino, camisa celeste, corbata azul oscuro con lunares blancos), con iluminación fría y tono azulado. Superpuesta, línea de tiempo horizontal naranja con puntas de flecha en ambos extremos. Pasos del recorrido del usuario alternando arriba y abajo de la línea, de izquierda a derecha, en texto naranja: (arriba) «El usuario va a la tienda.» → (abajo) «Sastre recoge medidas» → (arriba) «El usuario espera de 3 a 4 semanas» → (abajo) «El usuario vuelve a la tienda.» → (arriba) «El usuario se prueba la prenda.» → (abajo) «El sastre hace los cambios finales» → (arriba) «El usuario espera 1-2 semanas Usuario» → (abajo) «Recibe la camisa por correo». El diagrama ilustra el proceso tradicional de sastrería con múltiples visitas y semanas de espera.

Aplicación de descarga de usuario

El usuario se toma una foto

La aplicación muestra un ajuste virtual

El usuario selecciona el color, etc.

El usuario espera 1 semana

El usuario recibe una camiseta "perfecta"

X% de usuarios reporta error

Dar consejos de detalles como el color

¿Qué pasa si no es perfecta?

**Figura:** Línea de tiempo horizontal naranja con puntas de flecha en ambos extremos. Pasos del recorrido del usuario en texto naranja, alternando arriba y abajo de la línea, de izquierda a derecha: (arriba) «Aplicación de descarga de usuario» → (abajo) «El usuario se toma una foto» → (arriba) «La aplicación muestra un ajuste virtual» → (abajo) «El usuario selecciona el color, etc.» → (arriba) «El usuario espera 1 semana» → (abajo) «El usuario recibe una camiseta "perfecta"». Tres anotaciones en texto rojo con flechas rojas apuntando hacia arriba a pasos específicos: (1) flecha desde «X% de usuarios reporta error» hacia «El usuario se toma una foto»; (2) flecha desde «Dar consejos de detalles como el color» hacia «El usuario selecciona el color, etc.»; (3) flecha desde «¿Qué pasa si no es perfecta?» hacia «El usuario recibe una camiseta "perfecta"».

https://www.bloomberg.com/news/articles/2018-02-05/don-t-use-this-ai-tailor-yet

**Figura:** Captura de pantalla de un artículo de Bloomberg Businessweek. Metadatos del artículo: «February 5, 2018, 8:01 AM PST». Titular principal: «Don't Use This AI Tailor ... Yet». Subtítulo: «After three shirts we ordered didn't fit, Original Stitch took down its measurement software.». Autores: «By Pavel Alpeyev and Jason Clenfield». Fotografía principal: primer plano del brazo de una persona con camisa blanca muy arrugada y mal ajustada. Banner gris superpuesto en la parte inferior de la foto con texto blanco: «San Francisco startup Original Stitch promised shirts that **fit just right...**» (la frase «fit just right...» resaltada en rosa/rojo). Barra lateral derecha con miniatura de portada de revista (febrero 12, 2018, titular «How Did Your First Day Go, Jay?») y enlaces «Subscribe» y «Reprints». URL en la parte inferior: «https://www.bloomberg.com/news/articles/2018-02-05/don-t-use-this-ai-tailor-yet». (slides 28–30)
## Discrepancia entre datos y UX

### Turkish - English Translation

Turkish - English Translation

| Turkish (detected) | English |
|---|---|
| o bir aşçı | she is a cook |
| o bir mühendis | he is an engineer |
| o bir doktor | he is a doctor |
| o bir hemşire | she is a nurse |
| o bir temizlikçi | he is a cleaner |
| o bir polis | He-she is a police |
| o bir asker | he is a soldier |
| o bir öğretmen | She's a teacher |
| o bir sekreter | he is a secretary |
| o bir arkadaş | he is a friend |
| o bir sevgili | she is a lover |

**Figura:** Slide titulada «Turkish - English Translation» en texto azul claro en la parte superior. Captura de pantalla central de una interfaz de traducción (similar a Google Translate) con dos columnas: columna izquierda etiquetada «Turkish - detected» con iconos de micrófono y altavoz; columna derecha etiquetada «English» con iconos de copiar y altavoz; icono de intercambio de idiomas (doble flecha horizontal) en el centro. Lista de once pares de traducción del turco al inglés donde el pronombre turco neutro «o» se traduce con género asignado según la ocupación: roles de cuidado/domésticos (aşçı/cook, hemşire/nurse, öğretmen/teacher, sevgili/lover) como «she»; roles técnicos/autoridad (mühendis/engineer, doktor/doctor, temizlikçi/cleaner, asker/soldier, sekreter/secretary, arkadaş/friend) como «he»; «o bir polis» traducido como «He-she is a police».

Turkish - English Translation

Discrepancia entre datos y UX

**Figura:** Slide titulada «Turkish - English Translation» en texto azul claro en la parte superior central. Texto en negrita negra en el lado izquierdo: «Discrepancia entre datos y UX». Captura de pantalla central de un artículo de Global News con titular: «Google blocks gendered pronouns like 'her' or 'him' from its new AI tool». Autor: «By Paresh Dave Reuters». Fecha: «November 27, 2018 2:34 am». El artículo trata sobre la decisión de Google de impedir que sus herramientas de IA (específicamente Smart Compose) sugieran pronombres con género para evitar suposiciones incorrectas o reflejar sesgos societales presentes en los datos de entrenamiento. Barra de navegación «Global News» visible en la parte superior del recorte; botones de compartir en redes sociales (Facebook, Twitter, LinkedIn, etc.) debajo del titular;

Turkish - English Translation

**Figura:** Slide titulada «Turkish - English Translation» en texto azul negrita en la parte superior. Captura de pantalla de un artículo de BUSTLE con titular: «Google Translate's New Tool To Get Rid Of Gender Bias In Translations Is Kind Of A Big Deal», autor Mika Doyle. Comparación visual «Before» y «After» de la interfaz de Google Translate traduciendo la frase turca «o bir doktor» (pronombre neutro «o»): **Before** (izquierda): caja azul con una sola traducción «he is a doctor» y icono de verificación. **After** (derecha): mensaje «Translations are gender-specific. LEARN MORE.» sobre la caja de traducción; dentro de la caja azul, dos opciones: «she is a doctor (feminine)» y «he is a doctor (masculine)». (slides 31–33)
### Target Coupons

Target Coupons

"Misplaced Intelligence"

**Figura:** Slide titulada «Target Coupons» en texto azul claro en la parte superior central. Dos recortes de artículos lado a lado. **Sección izquierda:** artículo de Forbes con titular «How Target Figured Out A Teen Girl Was Pregnant Before Her Father Did», autor Kashmir Hill (Forbes Staff), fecha February 16, 2012. Texto sobre cómo los minoristas estudian patrones de consumo para predecir necesidades; menciona que Target «figured out how to data-mine its way into your womb» para predecir embarazos. Debajo del recorte, cita en negrita: «"Misplaced Intelligence"». **Sección derecha:** artículo de Harvard Business Review con ilustración de Kyle T. Webster: persona sentada en un escritorio con laptop, conectada por líneas elásticas rosas a un círculo rosa grande a la izquierda y un círculo más pequeño arriba, sugiriendo extracción de datos o control. Categoría «MARKETING» en rojo. Titular: «Ads That Don't Overstep». Autores: Leslie K. John, Tami Kim, y Kate Barasz. Edición: January–February 2018. En la esquina inferior derecha, texto «Loading...» con icono de progreso circular (elemento de captura web). (slide 34)
### Credit Card Fraud

Credit Card Fraud

False Positives

**Figura:** Slide titulada «Credit Card Fraud» en texto azul claro en la parte superior central. Captura de pantalla de un artículo de PayThink con titular: «PayThink The cost of fraud fighting is as bad as fraud itself». Autor: «By Ryan Breslow». Publicación: «June 07 2018, 12:01am EDT». Categorías: «ISO and agent, Payment fraud, Retailers, Authentication». Recuadro con borde negro que resalta dos párrafos: (1) «But the results are abysmal, especially when it comes to fighting fraud. Using the best-performing algorithms, researchers successfully identified **495 of 500 fraudulent transactions** in a sample size of **50 million transactions** (that's a **99% detection rate**).» (2) «But they incorrectly flagged **500,000 legitimate transactions** from good customers as fraudulent. There were too many '**false positives**' — customers falsely rejected for fraud concerns — to make the layering approach useful. These numbers are untenable for e-commerce stores, where the average profit margin is as low as 5%, or **0.5%-3.5% for e-commerce-only operations.**» (márgenes de beneficio resaltados en verde). Texto grande en negrita negra en la parte inferior izquierda: «False Positives». (slide 35)
### Microsoft Tay

Microsoft Tay

Adverse Actors – Feedback apropiado

**Figura:** Slide titulada «Microsoft Tay» en texto azul claro en la parte superior central. Captura de pantalla central de un artículo de The Verge con titular: «Microsoft made a chatbot that tweets like a teen». Autor/fecha: «By Jacob Kastrenakes | @jake_k | Mar 23, 2016, 10:26am EDT». Imagen destacada: representación artística glitchy de un rostro con el texto «Tay.ai» en fuente digital pixelada; Fragmento de texto: «Microsoft is trying to create AI that can pass for a teen. Its research team launched a...». Barra lateral derecha «MOST READ» con diagramas wireframe de un smartphone plegable y titular «Is this the Motorola RAZR with folding display?». Texto grande en negrita negra en la parte inferior izquierda: «Adverse Actors – Feedback apropiado». (slide 36)
### Predictive Policing

Predictive Policing

**Figura:** Slide titulada «Predictive Policing» en texto azul claro grande en la parte superior central. Dos recortes de artículos lado a lado. **Sección izquierda:** etiqueta «PARTNER CONTENT», atribución «CYNTHIA RUDIN, MIT SLOAN». Titular: «PREDICTIVE POLICING: USING MACHINE LEARNING TO DETECT PATTERNS OF CRIME». Fotografía con figuras Lego: dos policías (uno en motocicleta, otro de pie con perro), furgoneta policial blanca, dos figuras vestidas de ladrones cerca de una estructura gris tipo cajero automático; pie de foto «legocriminals_660»; iconos de compartir (Facebook, Pinterest) en la esquina superior derecha de la foto. **Sección derecha:** titular «Artificial Intelligence Is Now Used to Predict Crime. But Is It Biased?». Subtexto: «The software is supposed to make policing more fair and accountable. But critics say it still has a way to go.». Comparación de dos mapas lado a lado: mapa izquierdo con heatmap de colores (azul a rojo/amarillo indicando densidad); mapa derecho de calles de una ciudad (ubicaciones identificables: North Hills, Van Nuys, Lake Balboa en Los Ángeles) con cuadrados rojos superpuestos marcando «hotspots». Pie de foto: «Predictive policing is built around algorithms that identify potential crime hotspots... (PredPol)». (slide 37)
## ¿Qué es UI?

### Definición de Diseño de Interfaces (UI)

El Diseño de Interfaz o User Interface (UI), se refiere a todo aquello con lo que los usuarios interactúan directamente (la capa externa de un producto o servicio digital). Es lo que ve y toca en una página web, una aplicación o un dispositivo cualquiera.

Cabe destacar que, UI es la parte visible de la interface, mientras que UX es la parte oculta, conceptos que muchas veces prestan a confusión.

**Figura:** Slide titulada «¿Qué es el Diseño de Interfaces (UI)?» en negrita negra. Dos párrafos de texto explicativo en gris oscuro; en el primer párrafo, la frase «la capa externa de un producto o servicio digital» en negrita; en el segundo párrafo, «UI» y «UX» en negrita. En la parte inferior, ilustración comparativa «UX design vs. UI design» con círculo amarillo «vs.» en el centro. **UX design** (izquierda): ilustración de tres personas mirando gráficos y wireframes dentro de una forma nube gris; una persona señala un gráfico de barras en un tablero (representa la parte oculta/estructural del diseño). **UI design** (derecha): ilustración de una persona usando un stylus para dibujar una interfaz colorida en una pantalla, dentro de una forma nube gris (representa la parte visible/estética).

¿De qué se ocupa UI?

Sobre todas las cosas, entiende el proceso de Diseño Centrado en el Usuario (DCU). Este proceso debe ser adaptable a cualquier dispositivo. La UI se ocupa de la construcción y validación de prototipos.

Ayuda también a la creación de wireframes y estructuras diseñadas a mano o digitalmente.

**Figura:** Slide titulada «¿De qué se ocupa UI?» en negrita negra. Dos párrafos de texto; términos resaltados en azul claro: «Diseño Centrado en el Usuario (DCU)», «construcción y validación de prototipos», y «wireframes». En la parte inferior, wireframe digital de un sitio web de videos modelado después de YouTube, dentro de un marco de navegador: barra de título «YouTube», barra de dirección «https://www.youtube.com/»; encabezado con barra de búsqueda y botones «Upload», «Noti.» (Notifications), «Sett.» (Settings); botones de navegación «Home», «Trending», «Subscription» debajo de la búsqueda. Barra lateral izquierda con menú: «Home», «My Channel», «Trending», «Subscription», «History», «Watch Later»; sección «Subscriptions» con iconos y líneas horizontales representando nombres de canales. Área de contenido principal: recuadro grande superior con «X» (placeholder de video/imagen) y etiqueta «Ad» con flecha señalándolo; sección «Recommended» con cuadrícula 4×1 de placeholders de video; bajo uno, texto dummy: «This is the video title», «An uploader», «500 views | 1 week ago»; sección «Recently Uploaded» con otra fila de placeholders de video. (slides 39–40)
## Elementos y prácticas de diseño de interfaces

### Roles en el diseño de interfaces

•   Diseñador UI: Se ocupa de crear la parte visual de la interfaz de un producto o
    servicio, con el fin de brindar una navegación intuitiva y no solo estética.

•   Motion Designer. Es el encargado de la creación de las interacciones entre los
    usuarios y los productos o servicios digitales. Se ocupa de la narración de historias
    visuales a través de animaciones de gran impacto. Su tarea es animar imágenes y
    mensajes estáticos.

•   Desarrollador Frontend. El Desarrollador Frontend o Front End Developer, es el
    encargado de traducir los diseños a un lenguaje de programación y convertirlos en
    código HTML, JavaScript (JS) y / o CSS.

**Figura:** Título centrado en la parte superior en azul claro: «Roles en el Diseño de Interfaces». Tres viñetas alineadas a la izquierda con texto en negro; en cada viñeta, la frase clave del rol aparece resaltada en azul claro: en «Diseñador UI», la expresión «parte visual de la interfaz»; en «Motion Designer», la oración «Se ocupa de la narración de historias visuales a través de animaciones de gran impacto.»; en «Desarrollador Frontend», el fragmento «traducir los diseños a un lenguaje de programación y convertirlos en código HTML, JavaScript (JS) y / o CSS.». (slide 41)
### Elementos de User Interface

•   Guidelines: Son pautas, normas o lineamientos generales para el diseño de interfaces
    que permiten la coherencia visual entre la interfaz y la plataforma en la cual se
    desarrollará. Son las guías de diseño de los sistemas operativos.
      Existen dos categorías:

        Google Material Design: pertenece al Sistema Operativo Android de Google_.
        Se destaca por el uso de diferentes profundidades y superficies. Los bordes y
        las sombras son características inconfundibles de este diseño.

        Human Interface Guidelines: forma parte del Sistema Operativo iOS Design de
        _Apple. Se caracteriza por la claridad, profundidad y minimalismo de sus
        pantallas. Maneja el Content first, el cual prioriza el contenido.

**Figura:** Slide con título centrado en azul claro: «Elementos de User Interface». Una viñeta principal define «Guidelines»; la frase «normas o lineamientos generales para el diseño de interfaces que permiten la coherencia visual» aparece resaltada en azul claro. Debajo, dos subcategorías indentadas: «Google Material Design» (subrayado y en azul) con «Android de Google» y «profundidades y superficies» resaltados en azul claro; y «Human Interface Guidelines» (subrayado y en azul) con el término «Content first» en cursiva. icono azul en la esquina inferior derecha.

•   Sistemas de Color
•   Tipografía
•   Componentes: Top bar, formularios y controles
•   Botones: Botones principales y botones secundarios

**Figura:** Slide con el mismo título centrado «Elementos de User Interface» en azul claro. Lista de cuatro viñetas alineadas a la izquierda en texto negro, sin subviñetas ni imágenes adicionales. (slides 42–43)
### Herramientas de diseño

Figma                     Sketch

**Figura:** Slide dividida en dos columnas bajo el título centrado «Herramientas de Diseño» en azul. Columna izquierda etiquetada «Figma»: captura de pantalla del entorno de diseño Figma con un lienzo gris central lleno de decenas de artboards o frames pequeños de un proyecto de aplicación móvil; numerosas líneas delgadas azul claro conectan los artboards entre sí formando una red densa de flujos de prototipado; panel lateral izquierdo con jerarquía de capas y componentes; panel derecho con propiedades de diseño. Columna derecha etiquetada «Sketch»: tarjeta blanca central con texto promocional — «Sketch is where great *design* happens.» (la palabra «design» en script naranja), «A Mac app for designers to create, team up, prototype, and more.», «A web app for everyone else to browse, give feedback, inspect, and handoff — in any browser.», «A complete design platform, made by a sustainable indie company since **2010**.» — y botón negro «Find out more.»; alrededor de la tarjeta aparecen assets de diseño: icono de 1Password, captura de UI móvil de app de viajes «Honeymoon» con vuelos y hoteles, e iconos ilustrados de alimentos. (slide 44)
### Usabilidad y accesibilidad

Tanto la usabilidad como la accesibilidad son conceptos que no deben faltar en el diseño
de interfaces. Por un lado, la usabilidad plantea 10 reglas generales para el diseño de
interacción denominadas “heurísticas”, las cuales fueron creadas por Jakob Nielsen, y por
el otro, la accesibilidad en la web, que se basa en cuatro principios fundamentales:

•   perceptible,
•   operable,
•   comprensible y
•   Robusto

https://openwebinars.net/blog/ux-que-es/

**Figura:** Slide con título centrado «Usabilidad y Accesibilidad» en azul claro. Párrafo introductorio en negro con términos clave resaltados en azul claro: «usabilidad», «accesibilidad», «la usabilidad plantea 10 reglas generales para el diseño de interacción denominadas "heurísticas"», y «la accesibilidad en la web, que se basa en cuatro principios fundamentales:». Cuatro viñetas listan los principios de accesibilidad. Enlace URL al pie del texto. (slide 45)
### Tendencias UI

Dark Mode o                        Tendencias UI
Modo Oscuro        Glassmorphism                   Neumorphism

      •   Elementos geométricos
      •   Minimalismo
      •   Ilustraciones 3D
      •   Colores Vivos

**Figura:** Slide con título centrado «Tendencias UI» en azul claro. Tres columnas de ejemplos visuales bajo los encabezados «Dark Mode o Modo Oscuro», «Glassmorphism» y «Neumorphism». Columna izquierda (Dark Mode): mockup de app móvil de analítica con fondo negro profundo, texto blanco de alto contraste, gráficos de barras en púrpura y líneas en rosa, y botón «plus» en teal. Columna central (Glassmorphism): dos pantallas de app de fitness/salud («Good Day, Mark!» y pantalla «Calories») con paneles semitransparentes tipo vidrio esmerilado sobre fondo abstracto colorido (púrpura, naranja, azul), texto blanco, bordes finos e iconos vibrantes. Columna derecha (Neumorphism): dos pantallas de app «Smart Home» para control de temperatura con elementos UI en relieve mediante sombras suaves claras y oscuras sobre fondo gris claro/blanco, paleta minimalista con acento púrpura en un toggle. Debajo de las tres columnas, cuatro viñetas: «Elementos geométricos», «Minimalismo», «Ilustraciones 3D», «Colores Vivos». (slide 46)
## Data-Driven User Interfaces (MLUI)

### Diferentes usuarios, diferentes datos

Diferentes
                              usuarios,
                          Diferentes datos
                      Múltiples    usuarios      o
                      personajes para los cuales
                      diseñar.       Ejecutivos,
                      gerentes y analistas son
                      personajes comunes que
                      tienen sus propios flujos de
                      trabajo y necesidades de
                      datos.

https://marvelapp.com/blog/designing-data-driven-interfaces/

**Figura:** Slide dividida en tres zonas. Zona superior: cuatro personas/perfiles con foto, nombre, edad, cargo y cita sobre sus necesidades de datos — Christine, 48 (Center Manager): «We need to identify improvement opportunities.»; Nancy, 49 (Director of Nursing): «We modify the Drug Library to meet the practice.»; Carol, 37 (Floor Supervisor): «Donor optimization, device optimization.»; Jim, 52 (Service Technician): «We want to increase the first time fix.». Zona central: tres mockups de dashboards en ventanas de navegador — izquierda «Analytics Assistant» con gráfico de dona «80% Compliance», barras y gráfico radar; centro «Reports Assistant» con pestañas «Devices», «Employees», «Location», gráfico de barras temporal y tablas con indicadores verde/rojo; derecha «Real Time Dashboard» con estado en tiempo real de «Center», «Product» y «Operators», tablas y heatmaps. Zona derecha: título «Diferentes usuarios, Diferentes datos» y el párrafo de texto transcrito. URL de fuente en el margen inferior. (slide 48)
### CRITICAL / GLANCEABLE / INFORMATIVE

**Figura:** Cada wireframe tiene tres secciones horizontales: bloque superior de ancho completo, sección media dividida en tres columnas iguales, y bloque inferior de ancho completo. Wireframe izquierdo: bloque superior etiquetado «CRITICAL» en gris mayúsculas negrita; sección media con la palabra «GLANCEABLE» centrada sobre las tres columnas; bloque inferior etiquetado «INFORMATIVE» en gris mayúsculas negrita. Wireframe derecho: bloque superior «BROAD OVERVIEW»; sección media «DETAIL SUMMARY» centrada; bloque inferior «SPECIFIC ITEMS/TASKS». Los bloques son rectángulos grises vacíos (placeholders). icono azul abajo a la derecha. (slide 49)
### Personalización de contenido

**Figura:** Slide con título centrado en azul «Personalización de Contenido». menú «Home», «TV Shows», «Movies», «New & Popular», «My List»; iconos de búsqueda, DVD, regalo, notificaciones (campana con badge «9+») y avatar de perfil azul a la derecha. Filas de contenido personalizado: «Trending Now» con pósters de *Jupiter's Legacy* (badge «Top 10»), *The Sons of Sam*, *The Last Days*, *G.I. Joe: The Rise of Cobra*, *Middle Men*; «Continue Watching for Gibson» con barra de progreso roja en cada póster (*Dead Man Down*, *I am All Girls*, *Startup* con badge «Top 10», *Ferry*, *Sleight*); fila parcial «Watch It Again» visible al fondo.

https://edrone.me/blog

El contenido de marketing de Zalando es generado por algoritmos. Utilizan información sobre compras
pasadas y listas de deseos de sus clientes para personalizar los materiales de marketing.

**Figura:** Tres capturas de pantalla del sitio Zalando en secuencia horizontal, etiquetadas debajo como «FIRST VISIT», «NEXT VISIT» y «MACHINE LEARNING». FIRST VISIT: landing genérica con tres bloques grandes «WOMEN», «MEN», «KIDS» con fotos lifestyle y filas de miniaturas de ropa genérica. NEXT VISIT: banner prominente «SNEAKERBOOTS ON TREND» con imagen de sneaker gris; modelos más enfocados en estilos específicos. MACHINE LEARNING: sección «FOR YOU» con recomendaciones personalizadas — reloj plateado, sneakers rosas, outfits de estética específica. URL `https://edrone.me/blog` sobre la tercera captura. Párrafo explicativo en español al pie. (slides 50–51)
### Adaptive UI

https://arxiv.org/pdf/2103.06807.pdf

**Figura:** Diagrama del artículo «Adapting User Interfaces with Model-based Reinforcement Learning» (Kashyap Todi, Aalto University; Gilles Bailly, Sorbonne Université; Luis A. Leiva, University of Luxembourg; Antti Oulasvirta, Aalto University). Metadata rotada verticalmente: «7v1 [cs.HC] 11 Mar 2021». Flujo central de adaptación de menú:

1. **Current Design ($t_0$):** menú vertical con tres grupos — Grupo 1: Open, New, Save; Grupo 2: Save As..., Export, Move To...; Grupo 3: Rename, Duplicate, Print, Exit.

2. **Model-Based Reinforcement Learning:** flecha de tiempo vertical punteada de $t_0$ a $t_1$ a $t_2$. Árbol de estados-acciones: nodo negro **Current State ($S_0$)** en $t_0$ con «observed values»; transiciones con acciones $a_1, a_2, \dots, a_n$ hacia **Adapted States** $S_1, S_2, \dots, S_n$ en $t_1$ («estimated values»); desde $S_1$, acciones $a_1, a_2, \dots, a_n$ hacia segunda capa $S_{11}, S_{12}, \dots, S_{1n}$ en $t_2$.

3. **Adapted Design ($t_1$):** «Save» movido del primer grupo al segundo — [Open, New], [Save, Save As..., Export, Move To...], [Rename, Duplicate, Print, Exit].

4. **Final Design ($t_n$):** «Print» movido del tercer al segundo grupo; «Move To...» movido del segundo al tercer — [Open, New], [Save, Save As..., Export, Print], [Rename, Move To..., Duplicate, Exit].

URL del paper en el margen inferior.

**Figura:** flecha azul se bifurca en dos caminos — camino superior produce orden A, D, C, B, E; camino inferior produce C, A, B, D, E; desde cada resultado salen más flechas azules hacia afuera indicando adaptación continua. Lado derecho: dos ventanas «Adaptive UI» con listas «antes → después». Mockup superior — lógica «FREQUENCY»: lista antes A–G alfabética; flecha blanca gruesa con etiqueta «FREQUENCY»; lista después con Item C e Item A resaltados en amarillo al tope, seguidos de E, B, D, F, G. Mockup inferior — lógica «MODEL-BASED RL»: misma lista A–G; flecha con etiqueta «MODEL-BASED RL»; lista después con Item A primero, Item C resaltado en amarillo en segunda posición, luego B, D, E, F, G. Icono azul abajo a la derecha.

T0            T1            T2

     Tiempo
                   Tiempo

**Figura:** Diagrama de evolución temporal de una lista de cinco ítems en tres etapas conectadas por flechas azules etiquetadas «Tiempo». **T0** (encabezado azul claro): pila vertical de cinco cajas grises uniformes — Item A, Item B, Item C, Item D, Item E (orden alfabético). **T1**: Item A (gris), Item C (caja amarillo brillante, subió una posición), Item B (gris, bajó), Item D (gris), Item E (caja amarillo pálido, permanece al fondo). **T2**: Item C (amarillo brillante, primero), Item E (amarillo pálido, segundo), Item A (gris), Item B (gris), Item D (gris) — los ítems resaltados suben al tope manteniendo el orden relativo de los demás.

¿Qué es le diseño adaptativo?

La interfaz de usuario adaptable aprovecha la IA para rastrear y aprender de las
       acciones del usuario mientras el usuario interactúa con el producto.

                                     Ejemplo

**Figura:** Slide con título «¿Qué es le diseño adaptativo?» en azul claro. Definición con «IA» y «acciones del usuario» resaltados en azul claro. Subtítulo subrayado «Ejemplo». Captura de aplicación web «Web Re-Design»: barra lateral izquierda oscura con navegación — Dashboard, Clients, **Projects** (resaltado en verde), Invoices, Estimates, Expenses, People; icono de perfil abajo. Área principal: encabezado «Web Re-Design» con indicador «IN CONSTRUCTION» (punto azul) a la derecha; pestañas «Messages», «Files», «...»; feed de mensajes con avatar y texto placeholder; mensaje de «John» a las 3:14pm con texto Lorem Ipsum; mensaje de «Sally» a las 3:14pm etiquetado «Media Name» con fotografía cuadrada sepia de grúa de construcción contra cielo.

El dilema moral de la inﬂuencia de IA en UI

Permitir que un algoritmo manipule una interfaz de usuario para adaptarse a los patrones de
uso de un individuo es muy diferente de permitir que un algoritmo manipule el contenido que
                                     las personas ven.

       https://uxdesign.cc/toward-a-more-human-user-interface-with-artificial-intelligence-7bbee17ff30d

**Figura:** Slide con título en azul «El dilema moral de la influencia de IA en UI». Párrafo introductorio; la segunda parte «de permitir que un algoritmo manipule el contenido que las personas ven.» resaltada. Tres columnas visuales: columna izquierda — rectángulo negro con cita en blanco: «"A squirrel dying in front of your house may be more relevant to your interests right now than people dying in Africa."» atribuida en azul a «Mark Zuckerberg, Facebook»; columna central — círculo negro grande (burbuja de filtro) con círculos azul claro de distintos tamaños y «YOU» en blanco al centro; perímetro etiquetado con NETFLIX, AMAZON, HUFFINGTON POST, WASHINGTON POST, FLIPBOARD, GOOGLE, YAHOO NEWS; columna derecha — sección negra «The Balance:» con pares contrastantes en naranja/azul: Justin Bieber / Afghanistan, The Oscars / Homelessness, Agreeable Ideas / Challenging Ideas, People like You / Different People. URL al pie. (slides 52–57)
## Human-Machine Interaction (MLUX)

### Ciclo MLUX: Labeling Data, Ideation, Usage, Feedback

(Etiquetado de Datos)       (Ideación)

        Uso             Retroalimentación

**Figura:** Collage dividido en cuatro cuadrantes iguales, cada uno con fotografía y título bilingüe. Cuadrante superior izquierdo — foto cenital de manos tecleando en teclado blanco sobre escritorio de madera clara, con mouse blanco y gafas de marco rojo; título «Labeling Data» (blanco negrita) y «(Etiquetado de Datos)» (azul claro). Cuadrante superior derecho — mujer sonriente en blazer frente a pizarra oscura cubierta de post-its amarillos, azules y rosas, dirigiéndose a grupo sentado en mesa de conferencia visto desde atrás; título «Ideation» y «(Ideación)». Cuadrante inferior izquierdo — vista cenital de manos sosteniendo smartphone con feed tipo red social con cuadrícula de fotografías; título «Usage» / «Uso». Cuadrante inferior derecho — primer plano macro pixelado de pantalla digital con botón «Report Spam» y texto «Read»; título «Feedback» / «Retroalimentación». (slide 59)
### Etiquetado de datos

Es el proceso de asignar etiquetas o categorías a
                                     diferentes puntos o conjuntos de datos. Es un paso
                                     esencial en la preparación de datos para algoritmos
                                     de aprendizaje supervisado.
 (Etiquetado de Datos)

                                                 Diseño de Interfaz para Etiquetado Humano

                            Etiquetado Humano Asistido por Máquina

              Etiquetado Selectivo

Un etiquetado preciso es crucial para entrenar modelos de machine learning con alta
precisión. A menudo, este proceso puede requerir expertos humanos (por ejemplo,
etiquetado manual) o incluso plataformas especializadas para facilitar el etiquetado.

**Figura:** Slide con imagen superior izquierda: fotografía de manos tecleando en laptop con título superpuesto «Labeling Data» (blanco cursiva negrita) y «(Etiquetado de Datos)» (azul claro). Tres flechas azules salen del borde inferior de la imagen hacia tres conceptos: derecha — «Diseño de Interfaz para Etiquetado Humano»; diagonal centro — «Etiquetado Humano Asistido por Máquina»; diagonal izquierda — «Etiquetado Selectivo». Definición arriba a la derecha con la frase «asignar etiquetas o categorías a diferentes puntos o conjuntos de datos» resaltada en azul claro. Párrafo inferior con «puede requerir expertos humanos» e «incluso plataformas especializadas para facilitar el etiquetado» resaltados en azul claro. (slide 60)
### Ideación

Es la fase de generación y exploración de nuevas ideas para un producto de datos. Involucra brainstorming, investigación de mercado, identificación de necesidades del usuario y definición de posibles soluciones basadas en datos.

Herramientas de Exploración de Datos

Diseño Generativo

Clustering (Agrupación)

La ideación es crucial para asegurarse de que el producto de datos aborde problemas reales y relevantes, y de que exista una demanda o interés en el mercado para dicho producto.

**Figura:** Párrafo introductorio en la parte superior izquierda; las palabras «ideas», «brainstorming» e «investigación de mercado» resaltadas en azul claro. Fotografía en el cuadrante superior derecho de una mujer con blazer de pie frente a un muro de vidrio con notas adhesivas de colores; sobre la foto, título en blanco itálica «Ideation (Ideación)». Tres flechas de color teal apuntan desde la fotografía hacia tres términos centrales apilados verticalmente: «Herramientas de Exploración de Datos», «Diseño Generativo» y «Clustering (Agrupación)». Párrafo inferior; la frase «aborde problemas reales y relevantes» resaltada en azul claro. (slide 62)
### Usage (Uso)

Se refiere a cómo y cuánto se utiliza un producto de datos por parte de los usuarios finales.

Interfaces Personalizadas y Adaptativas

Interacción con Sistemas de Recomendación y Clasificadores

Interfaces Aumentadas

El seguimiento del uso proporciona insights valiosos sobre la adopción y retención del producto, lo que puede informar decisiones sobre futuras iteraciones o características.

**Figura:** Párrafo definitorio en la parte superior izquierda. Fotografía en el cuadrante inferior izquierdo de una persona sosteniendo e interactuando con un smartphone; sobre la imagen, texto central «Usage / Uso» en blanco. Tres flechas de color teal salen del concepto central hacia la derecha y arriba: flecha superior hacia «Interfaces Personalizadas y Adaptativas»; flecha diagonal superior-derecha hacia «Interacción con Sistemas de Recomendación y Clasificadores»; flecha horizontal hacia «Interfaces Aumentadas». Párrafo conclusivo en la parte inferior derecha sobre seguimiento del uso, adopción y retención. (slide 64)
### Feedback (Retroalimentación)

Es la información que los usuarios proporcionan sobre el producto, ya sea de forma directa o indirecta (a través del análisis del comportamiento del usuario, métricas de uso, etc.).

Adjudicación Humana y Procesos de Escalación

Explicabilidad y Transparencia

**Figura:** Párrafo definitorio en la parte superior. Fotografía central de una pantalla con botones «Report Spam» y «Read»; sobre la imagen, texto grande en blanco «Feedback» y debajo en azul claro «Retroalimentación». Dos flechas de color teal salen de la imagen central hacia la izquierda: flecha superior hacia «Adjudicación Humana y Procesos de Escalación»; flecha inferior hacia «Explicabilidad y Transparencia». (slide 66)
### ¿Qué hace que una interacción humano-máquina sea "buena"?

¿Qué hace que una interacción humano-máquina sea "buena"?

Intuitividad

Eficiencia

Fiabilidad

Satisfacción del usuario

Seguridad

Adaptabilidad

**Figura:** Pregunta central en azul claro: «¿Qué hace que una interacción humano-máquina sea "buena"?». Seis principios dispuestos alrededor de la pregunta en disposición circular, en color teal/cian, en sentido horario desde arriba-izquierda: «Intuitividad», «Eficiencia», «Fiabilidad» (con la «d» final en línea separada), «Seguridad», «Adaptabilidad» y «Satisfacción del usuario». (slide 67)
## Case Study: Discapacidad visual en India

### Contexto en India

Case Study:
Discapacidad visual en India

**Figura:** Texto centrado: primera línea «Case Study:» en azul brillante sans-serif; segunda línea «Discapacidad visual en India» en teal/cian sans-serif.

- India tiene 1/3 de las personas ciegas y con discapacidad visual del mundo.

- El 75% de estos casos son evitables, pero persisten debido a factores socioeconómicos y falta de acceso a tratamiento.

**Figura:** Tres viñetas alineadas a la izquierda en tipografía sans-serif gris oscuro, centradas verticalmente en la slide, sin título explícito. (slides 68–69)
### Hipótesis #1: Braille auditivo

Hipótesis #1:
Braille auditivo que no requiere que lo toques ni sepas cómo leer braille

**Figura:** Texto centrado: «Hipótesis #1:» en azul brillante sans-serif grande; debajo «Braille auditivo que no requiere que lo toques ni sepas cómo leer braille» en teal/cian sans-serif.

**Figura:** Fotografía de dos hombres en un entorno de oficina o laboratorio con pizarra blanca y muro de ladrillo al fondo. Hombre de la izquierda: gafas de montura oscura modificadas con un prototipo montado en el frente (carcasa marrón-beige con lente de cámara o sensor apuntando hacia adelante) y un auricular blanco con cable en el oído izquierdo. El hombre con las gafas mira directamente hacia la taza. (slides 70–71)
### Hipótesis #2: Navegación aumentada

Hipótesis #2:
Herramienta de navegación aumentada que crea automáticamente una guía de navegación a partir de una malla de puntos

**Figura:** Texto centrado: «Hipótesis #2:» en azul brillante sans-serif grande; debajo «Herramienta de navegación aumentada que crea automáticamente una guía de navegación a partir de una malla de puntos» en teal/cian sans-serif.

Visor de Realidad Aumentada HoloLens

Generación 3D de mallas.

Generación en tiempo real de un plano de suelo a partir de una malla de navegación

**Figura:** Tres paneles fotográficos dispuestos horizontalmente con leyendas debajo. Panel izquierdo: fotografía de estudio de un visor Microsoft HoloLens (gris oscuro/negro con visor transparente y diadema acolchada); leyenda «Visor de Realidad Aumentada HoloLens». Panel central: reconstrucción 3D digital de una planta de oficina como malla o nube de puntos de color cian flotando sobre un fondo de cuadrícula 3D blanco y negro; leyenda «Generación 3D de mallas.». Panel derecho: vista cenital en perspectiva de un entorno digital donde una malla de navegación (NavMesh) se genera sobre un área de suelo físico; el suelo está cubierto con polígonos multicolores (tonos teal, púrpura y verde) delimitados por líneas negras finas y puntos; leyenda «Generación en tiempo real de un plano de suelo a partir de una malla de navegación».

**Figura:** Comparación lado a lado en dos paneles. Panel izquierdo (entrada del mundo real): fotografía en primera persona de una mano derecha sosteniendo una manzana roja; fondo de pasillo interior con particiones de vidrio, suelo de madera y personas de pie al fondo. Panel derecho (representación digital): modelo esquelético 3D de la misma pose de mano sobre fondo negro; estructura compuesta por cilindros blancos gruesos (huesos) y esferas rojas pequeñas (articulaciones/landmarks); la pose replica los dedos curvados sujetando un objeto rojo simplificado; aura blanca tenue alrededor de la mano con efecto de motion blur en los huesos. (slides 72–74)
### Hipótesis #3: Interfaz táctil aumentada

Hipótesis #3:
Interfaz táctil aumentada que describe objetos cuando los levantas

**Figura:** Texto centrado: «Hipótesis #3:» en azul brillante sans-serif grande; debajo «Interfaz táctil aumentada que describe objetos cuando los levantas» en teal/verde mar sans-serif.

**Figura:** Cuatro paneles fotográficos dispuestos horizontalmente mostrando la evolución de un dispositivo sensor portátil. Panel 1 (izquierda): persona con camisa a cuadros verde oscuro y negro; arnés negro en el pecho sujeta un módulo sensor rectangular pequeño con cableado visible (prototipo temprano). Panel 2 (centro-izquierda): persona con camisa azul claro y cinturón negro; ensamblaje sensor más grande montado en el cinturón a la altura de la cintura, con soporte blanco que sostiene una cámara arriba y un sensor rectangular horizontal abajo. Panel 3 (centro-derecha): primer plano lateral del dispositivo del panel 2; soporte blanco (posiblemente impreso en 3D) con cámara negra tipo Microsoft LifeCam arriba y controlador Leap Motion (dispositivo rectangular horizontal para seguimiento de manos) abajo; cable USB conectado al lateral del Leap Motion. Panel 4 (derecha): render o foto de producto final de un cinturón estilo cuero marrón con hebilla metálica integrada; en la superficie frontal de la hebilla se ven dos lentes de sensor pequeñas.

**Figura:** Cuadrícula 2×2 con cuatro versiones de la misma fotografía base: una mano izquierda sostiene un bote circular azul de «NIVEA MEN CREME» con el texto «FACE • BODY • HANDS» en la parte inferior, sobre fondo interior luminoso desenfocado con ventanas. Cuadrante superior izquierdo: imagen original sin procesamiento. Cuadrante superior derecho: aproximadamente ocho puntos circulares amarillos brillantes superpuestos como keypoints (cuatro en la mano — uno cerca de la muñeca, tres agrupados cerca del pulgar — y cuatro en el bote — uno en el borde superior, uno sobre la «N», uno sobre la «M» y uno en el borde inferior izquierdo). Cuadrante inferior izquierdo: un único rectángulo delimitador grande de color cian que abarca la mano y el bote juntos. Cuadrante inferior derecho: tres rectángulos delimitadores magenta sobre el texto: uno alrededor de «NIVEA», uno alrededor de «MEN» y uno alrededor de «CREME» y «FACE • BODY • HANDS».

**Figura:** Fotografía de un hombre con polo verde y jeans de pie detrás de una mesa clara con varios productos de supermercado dispuestos de izquierda a derecha: caja rectangular gris/blanca, cartón grande de jugo naranja (marca Tropicana visible con imágenes de frutas), bolsa pequeña morada oscura, caja de jugo blanca con pajita, lata de aluminio plateada con letras rojas «Coke» y lata verde y azul «Sprite». El hombre lleva auriculares blancos con cable y un dispositivo rectangular blanco con cámara frontal montado en una correa negra ajustable alrededor de la cintura; un LED azul encendido en la parte superior del dispositivo; cables conectan el dispositivo a los auriculares. Su mano derecha descansa sobre el cartón de jugo naranja. Fondo: silla de oficina de malla negra a la izquierda, puerta y pared blanca con interruptor. (slides 75–78)
## Conclusiones

### Cierre de la sesión

Cierre de la Sesión

¿Qué les ha parecido más útil o revelador de lo que hemos discutido y practicado hoy?

¿Algún concepto o herramienta que estén ansiosos por aplicar?

¿Por qué es importante MLUX Y MLUI ?

Una buena experiencia e interfaz de usuario pueden hacer que nuestras aplicaciones de machine learning sean más efectivas y accesibles.

**Figura:** Título «Cierre de la Sesión» en negrita negra grande. A la derecha del título, icono lineal azul de una persona junto a un documento o lista de verificación. Tres preguntas reflexivas en gris sans-serif debajo del título. Afirmación conclusiva en la parte inferior sobre experiencia e interfaz de usuario y aplicaciones de machine learning. sección superior con superposición de color teal/cian; en un panel inferior, señal en pilar de concreto con letras apiladas que forman partes de «INGENIERÍA».

**Figura:** Captura de pantalla de una interfaz de plataforma educativa o de evaluación con branding UTEC. Tarjeta central blanca con: título «UX UI DPD»; metadatos con icono de evaluación (checkmark verde), autor «Germain Zanabria» con foto de perfil pequeña, etiquetas «Science», «Universidad», «2 jugadas» y «Fácil» en texto rojo. Botones alineados a la izquierda: «Editar», «Guardar», «Compartir» (con flecha desplegable), «Hoja de cálculo» y menú de tres puntos verticales. Botones alineados a la derecha: «Vista previa» (icono de ojo), «Asignar» (icono de reloj, botón con borde rosa) y «Empezar ahora» (botón magenta sólido con icono de reproducción). en un panel inferior, texto parcial en muro de concreto: «IN GEN NIECI RABLE». (slides 79–80)
### Referencias adicionales

https://medium.com/ml-ux/what-is-ml-ux-71d5e6d6ce9

**Figura:** En el cuadrante superior izquierdo, el título «Referencias Adicionales» en tipografía grande y negrita. Debajo del título, un enlace web: `https://medium.com/ml-ux/what-is-ml-ux-71d5e6d6ce9`. Las fotos están enmarcadas dentro de formas hexagonales y de diamante entrelazadas con bordes blancos delgados. Las fotografías muestran estructuras de concreto, columnas y pasarelas. Una sección hexagonal central tiene una superposición de color azul brillante. En la sección inferior derecha, una pared con texto vertical en negro fragmentado que incluye «NN», «GEVEN», «NIECI» y «RABLE». (slide 81)
## Glosario

- **UX (Diseño de Experiencia de Usuario):** Incluye Investigación, Diseño de Interacción, Arquitectura de Información, y más. Los diseñadores UX trabajan en un modo bastante conceptual, con representaciones aproximadas del mundo, para mejorar los aspectos subjetivos de un producto. UX es la parte oculta del diseño, mientras que UI es la parte visible.

- **DATA:** Aprendizaje Automático, IA, Análisis de Datos, Inferencia Estadística, y más.

- **UI (Diseño de Interfaces / User Interface):** Se refiere a todo aquello con lo que los usuarios interactúan directamente (la capa externa de un producto o servicio digital). Es lo que ve y toca en una página web, una aplicación o un dispositivo cualquiera.

- **DCU (Diseño Centrado en el Usuario):** Proceso que la UI debe entender y que debe ser adaptable a cualquier dispositivo.

- **Guidelines:** Pautas, normas o lineamientos generales para el diseño de interfaces que permiten la coherencia visual entre la interfaz y la plataforma en la cual se desarrollará. Son las guías de diseño de los sistemas operativos.

- **Google Material Design:** Pertenece al Sistema Operativo Android de Google. Se destaca por el uso de diferentes profundidades y superficies. Los bordes y las sombras son características inconfundibles de este diseño.

- **Human Interface Guidelines:** Forma parte del Sistema Operativo iOS Design de Apple. Se caracteriza por la claridad, profundidad y minimalismo de sus pantallas. Maneja el *Content first*, el cual prioriza el contenido.

- **Heurísticas:** Diez reglas generales para el diseño de interacción denominadas "heurísticas", creadas por Jakob Nielsen.

- **Accesibilidad web:** Se basa en cuatro principios fundamentales: perceptible, operable, comprensible y robusto.

- **Diseño adaptativo:** La interfaz de usuario adaptable aprovecha la IA para rastrear y aprender de las acciones del usuario mientras el usuario interactúa con el producto.

- **MLUX (ciclo):** Ciclo de interacción humano-máquina compuesto por cuatro fases: Labeling Data (Etiquetado de Datos), Ideation (Ideación), Usage (Uso) y Feedback (Retroalimentación).

- **Etiquetado de datos:** Proceso de asignar etiquetas o categorías a diferentes puntos o conjuntos de datos. Es un paso esencial en la preparación de datos para algoritmos de aprendizaje supervisado.

- **Ideación:** Fase de generación y exploración de nuevas ideas para un producto de datos. Involucra brainstorming, investigación de mercado, identificación de necesidades del usuario y definición de posibles soluciones basadas en datos.

- **Usage (Uso):** Cómo y cuánto se utiliza un producto de datos por parte de los usuarios finales.

- **Feedback (Retroalimentación):** Información que los usuarios proporcionan sobre el producto, ya sea de forma directa o indirecta (a través del análisis del comportamiento del usuario, métricas de uso, etc.).

