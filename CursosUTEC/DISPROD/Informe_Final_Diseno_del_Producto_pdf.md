---
curso: DISPROD
titulo: Informe Final Diseno del Producto
slides: 94
fuente: Informe Final Diseno del Producto.pdf
---

         Pastillero Inteligente basado en Arduino para
          Mejorar la Adherencia al Tratamiento en
                        Adultos Mayores

                                    INFORME




                          Docente: Cesar Rolando Nunura Nunura

                    Curso: Principios de Diseño de Productos y Servicios

                                         Integrantes:

                                                                           Porcentaje de
Código      Nombres y Apellidos                   ¿Qué hizo?
                                                                           participación
                                                                               100%


                                                                               100%


                                                                               100%

                                                                               100%


                                        2025–1
                                                                  Índice
1. Introducción .................................................................................................................................... 5
2. Identificación y análisis de la problemática .................................................................................. 6
    2.1. Problemática ............................................................................................................................ 6
    2.2. Insights .................................................................................................................................... 7
         2.2.1. Brecha en el cuidado de adultos mayores en Lima ......................................................... 7
         2.2.2.Cultura del cuidado familiar y apertura limitada a la tecnología ..................................... 7
         2.2.3. Desafíos específicos de la medicación en Lima ............................................................. 8
         2.2.4. Oportunidad de empoderar a cuidadores y asilos ........................................................... 8
    2.3. Criterios ................................................................................................................................... 8
         2.3.1. Funcionales .................................................................................................................... 8
         2.3.2. Usabilidad ...................................................................................................................... 8
         2.3.3. Económicos .................................................................................................................... 8
         2.3.4. Sociales .......................................................................................................................... 9
         2.3.5. Éticos ............................................................................................................................. 9
    2.4. Stakeholders ............................................................................................................................ 9
         2.4.1. Administrar de cerca (Alto Poder / Alto Interés) ............................................................ 9
         2.4.2. Mantener satisfechos (Alto Poder / Bajo Interés) ........................................................... 9
         2.4.3. Mantener informados (Bajo Poder / Alto Interés) .......................................................... 9
         2.4.4. Monitorear (Bajo Poder / Bajo Interés) .........................................................................10
    2.5. Alcance de proyecto ...............................................................................................................10
         2.5.1. El desarrollo abarcará ....................................................................................................11
         2.5.2. Enfoque y Limitaciones ................................................................................................11
    2.6. Objetivos ................................................................................................................................11
         2.6.1. Objetivo General ...........................................................................................................11
         2.6.2. Objetivos Específicos ....................................................................................................11
    2.7. Consideraciones del entorno ...................................................................................................12
3. Análisis de Mercado .......................................................................................................................12
    3.1. Público objetivo......................................................................................................................12
    3.2. Descripción del público objetivo ............................................................................................13
    3.3. Metodología ...........................................................................................................................14
         3.3.1. Enfoque .........................................................................................................................14
         3.3.3. Criterios de selección ....................................................................................................14
         3.3.4. Análisis de resultados ....................................................................................................14
         3.3.5. Resultados preliminares ................................................................................................17
    3.4. Mapa de empatía ....................................................................................................................18
         3.4.1. Mapa de empatía individual ..........................................................................................18
         3.4.2. Mapa de empatía grupal ................................................................................................19
    3.5. ¿Cuál es la competencia? ........................................................................................................21
         3.5.3. Medisafe........................................................................................................................22
         3.5.4. Pastillero simple ............................................................................................................23
    3.6. Matriz de Benchmark .............................................................................................................25
4. Propuesta de valor .........................................................................................................................26
    4.1. Conclusiones de los análisis previos .......................................................................................26
    4.2. Diferencial del producto .........................................................................................................26
    4.3. Conceptos de solución ............................................................................................................27
         4.3.1. Creación de bocetos ......................................................................................................27
         4.3.2. Creación de boceto final ................................................................................................31
         4.3.3. Diagrama de bloques funcional .....................................................................................34
5. Planificación de proyecto...............................................................................................................37
    5.1. Especificaciones Técnicas ......................................................................................................37
         5.1.1. Listar necesidades .........................................................................................................37
         5.1.2. Matriz Necesidad/ Métrica ............................................................................................38
         5.1.3. Lista de Métricas ...........................................................................................................39
         5.1.4. Benchmark Cuantitativo................................................................................................40
         5.1.5. Benchmark Cualitativo..................................................................................................41
         5.1.6. Especificaciones objetivo ..............................................................................................42
         5.1.7.Diagrama de bloques ......................................................................................................43
    5.2. Procesos de Manufactura del Prototipo Funcional( mejorar) ..................................................44
         5.2.1. Compra de Material: .....................................................................................................44
         5.2.2. Selección del Material: ..................................................................................................45
         5.2.3. Proceso de Manufactura que se usará ............................................................................46
    5.3. Criterios de Ergonomía...........................................................................................................49
         5.3.1. Peligros generados por la máquina: ...............................................................................49
             5.3.1.1. Mecánico: ............................................................................................................49
             5.3.1.2. Eléctrico: .............................................................................................................50
         5.3.2. Ergonomía:....................................................................................................................52
             5.3.2.1. Comunicación hombre máquina a través de indicadores .....................................52
             5.3.2.2. Posturas recomendadas ........................................................................................53
             5.3.2.4. Esquema ..............................................................................................................55
    5.4. Criterios de Seguridad y Prevención de Accidentes ...............................................................56
         5.4.1. Recomendación de diseño y protección: .......................................................................56
    5.5. Diagrama de Gantt..................................................................................................................57
    5.6. Presupuesto.............................................................................................................................57
6. Ejecución de Proyecto......................................................................................................................59
    6.1. Propuesta de materiales para una versión comercial ...............................................................59
    6.2. Fabricación de componentes del prototipo funcional ..............................................................62
         6.2.1 Sistema electrónico del prototipo ...................................................................................62
         6.2.2 Diseño de carcasa del prototipo......................................................................................65
    6.3. Ensamblado de componentes del prototipo funcional .............................................................67
         6.3.1 Soldadura de componentes electrónicos .........................................................................67
         6.3.2 Conexionado y pruebas preliminares .............................................................................68
         6.3.3 Impresión 3D de componentes mecánicos .....................................................................69
         6.3.4 Ensamblaje del sistema dispensador ..............................................................................70
         6.3.5 Fabricación de carcasa ...................................................................................................71
         6.3.6 Posicionamiento de piezas internas ................................................................................73
    6.4. Ensayos y pruebas de funcionalidad .......................................................................................74
    6.5. Validación de resultados .........................................................................................................75
7. Conclusiones ...................................................................................................................................76
8. Recomendaciones ...........................................................................................................................77
9. Referencias bibliográficas .............................................................................................................78
10. Anexos ...........................................................................................................................................80
    Video de explosición del pastillero:...............................................................................................90
1. Introducción

En la actualidad, seguir con los tratamientos médicos representa un reto considerable,
particularmente entre la población anciana. En Perú, investigaciones recientes muestran que el
porcentaje de pacientes con enfermedades cronicas que no siguen su medicación es del 37.1%,
siendo el 36.7% en quienes padecen hipertensión y 29.2% en aquellos con diabetes. Asimismo,
el cumplimiento del tratamiento antihipertensivo oscila entre el 55.5% y el 46.6%, y se ve
afectado por situaciones socioeconómicas desfavorables (Silva Caso, Riega López y Zavaleta,
2024).

Esta situación se complica debido a aspectos como la edad avanzada, la falta de educación y la
vida en localidades rurales o en zonas alejadas de la capital, donde las disparidades en el
cumplimiento del tratamiento son más marcadas. En Lima, por ejemplo, un estudio indicó que
el 57.4% de los pacientes con hipertensión mostraban poca adherencia a su medicación,
afectada por percepciones negativas sobre los fármacos y preocupaciones sobre sus efectos
secundarios (Conte, 2020).

La baja adherencia al tratamiento médico conlleva consecuencias graves tanto a nivel
individual como social: aumentan las complicaciones clínicas, se incrementan los gastos en
hospitalización y se reduce la efectividad de los sistemas de salud. Este fenómeno es
especialmente preocupante en adultos mayores, quienes, por sus condiciones físicas y
cognitivas, requieren mayores niveles de seguimiento y apoyo continuo.

Frente a esta realidad, se han estudiado diversos métodos para mejorar la adherencia
terapéutica. Entre ellos destacan las llamadas de seguimiento por parte de personal
farmacéutico, el uso de aplicaciones móviles como Medisafe y Pill Reminder, y sistemas de
alarmas convencionales como pastilleros electrónicos con temporizador. No obstante, estas
estrategias presentan limitaciones importantes: muchas personas mayores no están
familiarizadas con el uso de dispositivos digitales, no poseen teléfonos inteligentes o
simplemente enfrentan barreras visuales, auditivas o motrices que dificultan su implementación
efectiva. De hecho, se estima que más del 80% de los pacientes ha olvidado alguna vez tomar
su medicación a la hora indicada, lo que pone en evidencia que las estrategias actuales no son
completamente eficaces para asegurar la adherencia al tratamiento (Ospina López, Arango y
Ortegón, 2022, p. 15).

Este proyecto propone crear un sistema inteligente que utilice tecnología Arduino, destinado a
dispensar medicamentos en momentos específicos y ofrecer recordatorios visuales y sonoros.
A diferencia de los organizadores de pastillas convencionales, este dispositivo pretende ser un
apoyo en el seguimiento de los tratamientos médicos, especialmente para personas adultas
mayores en el distrito de San Juan de Lurigancho, Lima (INEI). Este distrito, uno de los más
poblados y con alta proporción de población adulta mayor, evidencia desafíos concretos en
términos de acceso, seguimiento médico y autonomía del paciente.
2. Identificación y análisis de la problemática
   2.1. Problemática
   Una de las principales causas del fracaso en tratamientos médicos no se debe a la falta de
   acceso a estos mismos, sino a la falta de adherencia al tratamiento, en términos más
   sencillos es cuando los pacientes no toman los medicamentos en los horarios
   correspondientes, dosis o formas indicadas. Este problema les ocurre frecuentemente a
   personas de tercera edad quienes suelen olvidar sus medicamentos lo que conlleva a un alto
   riesgo en su salud y en su calidad de vida.

   Según” la Organización Mundial de la Salud (OMS), en países de primer mundo, solo el
   50% de los pacientes con enfermedades crónicas toman adecuadamente su tratamiento y
   esa cifra puede ser aún peor en países subdesarrollados”. Además en estudios realizados en
   Panamá por investigadores del Departamento de Investigación y Evaluación de Tecnología
   Sanitaria del Instituto Conmemorativo Gorgas de Estudios de la Salud, utilizó el test de
   Morisky-Green para evaluar la adherencia a la medicación, reveló que 40% de la población
   panameña olvida tomar sus medicamentos en la hora indicada .

La siguiente figura a continuación presenta el estudio realizado del test de Morisky -Green con
el objetivo de mostrarnos el porcentaje de personas que se olvidan tomar sus medicamentos ,
este será un factor clave más adelante para el proyecto.
    Figura 1
    Resultados del test de Morisky-Green en pacientes con tratamiento crónico




Nota. El cuadro muestra los resultados del test de Morisky-Green, una herramienta utilizada
para evaluar la adherencia terapéutica. Adaptado de Llamas Ramo. (2020), Scielo.

   Asimismo la problemática se ve corroborada por investigaciones como la llevada a cabo
   por Antonio Duran Montenegro en la Universidad de Cantabria (España), pone en
   evidencia claramente con su análisis que uno de los factores es la mala administración y
   control de medicación.

La siguiente figura nos muestra los resultados de la investigación mencionada , los errores de
medicación más frecuentes , donde podemos resaltar que uno de los errores más frecuentes es
“ La mala administración del medicamento “
   Figura 2
   Errores de medicación más frecuentes en centros sociosanitarios




Nota. El gráfico muestra los tipos más comunes de errores relacionados con la medicación,
clasificados según su origen. Adaptado de Montes Cabezón (2012).

   2.2. Insights
   A partir de la comprensión de la problemática general y la exploración inicial del contexto
   en Lima, se identificaron los siguientes insights clave.


       2.2.1. Brecha en el cuidado de adultos mayores en Lima
       Muchos adultos mayores en Lima viven solos o pasan gran parte del día sin compañía,
       ya sea por motivos familiares, laborales o personales. El 23,6% de hogares en Lima está
       compuesto por solo un adulto mayor (INEI, 2024). Esta falta de supervisión dificulta el
       seguimiento adecuado de sus tratamientos médicos, generando riesgos de olvido,
       confusiones o complicaciones en su salud.


       2.2.2.Cultura del cuidado familiar y apertura limitada a la tecnología
       Existe una fuerte cultura de cuidado familiar en Perú. Solo en Lima se registró que un
       46,5% de hogares presentan algún miembro que es adulto mayor (INEI, 2024). Sin
       embargo, hay una creciente apertura a usar la tecnología como apoyo, siempre que sea
       percibida como confiable y extremadamente fácil de usar, complementando y no
       reemplazando el cuidado personal.
   2.2.3. Desafíos específicos de la medicación en Lima
       ● Confusión: La variedad de marcas y presentaciones puede confundir a los
         adultos mayores.
       ● Logística: El tráfico dificulta traslados para compras o citas, afectando la
         continuidad.
       ● Costo: El costo de medicamentos y atención médica resalta la necesidad de
         optimizar su uso.


   2.2.4. Oportunidad de empoderar a cuidadores y asilos
   Administrar medicamentos a múltiples personas es demandante y propenso a errores.
   Un pastillero electrónico eficiente puede ser una herramienta valiosa para optimizar su
   trabajo, reducir la carga y mejorar la seguridad.


2.3. Criterios
Basados en el análisis anterior, se establecen los siguientes criterios para guiar el diseño
del pastillero:


   2.3.1. Funcionales
       ● Precisión y confiabilidad: Dispensación exacta y fiable.
       ● Programabilidad flexible: Múltiples horarios y dosis adaptables.
       ● Sistema de alerta efectivo: Alertas sonoras y visuales claras, distintivas y
         perceptibles por adultos mayores (considerar posibles limitaciones auditivas o
         visuales).

   2.3.2. Usabilidad
       ● Interfaz intuitiva: Prioridad alta, sencillez, botones grandes, texto claro,
         lenguaje fácil, mínimo número de pasos para operar (Conexión directa con
         insight de baja experiencia tecnológica).
       ● Facilidad de llenado y mantenimiento: Diseño simple para recargar pastillas y
         limpiar.
       ● Portabilidad (Opcional): Evaluar si es necesario para el perfil de usuario
         objetivo o si un diseño estacionario es más apropiado inicialmente.

   2.3.3. Económicos
       ● Costo de producción accesible: Materiales y componentes para un precio viable
         en el mercado peruano.
       ● Eficiencia energética: Bajo consumo (baterías duraderas o bajo consumo
         eléctrico).
   2.3.4. Sociales
      ● Aceptación cultural: Diseño que respete la percepción local sobre tecnología y
        cuidado, evitando sentirse "reemplazados" por una máquina.
      ● Apoyo a la independencia: Fomentar la autonomía del adulto mayor en su
        medicación (Responde a necesidad emocional identificada).
      ● Reducción de la carga de cuidadores: Aliviar el trabajo y preocupación de los
        cuidadores.

   2.3.5. Éticos
      ● Privacidad y seguridad: Si almacena datos (aunque no previsto en el prototipo
        inicial), asegurar protección.
      ● Consentimiento informado: Información clara sobre uso y funcionamiento.

2.4. Stakeholders

   2.4.1. Administrar de cerca (Alto Poder / Alto Interés)

      ● Cuidadores y familiares: Tienen un alto interés en que el pastillero funcione
        bien, ya que afecta directamente su responsabilidad y la salud de sus seres
        queridos. También tienen poder para influir en la decisión de compra y el uso
        del dispositivo.
      ● Usuarios finales (adultos mayores): Aunque su poder de decisión puede variar,
        tienen un alto interés en el pastillero porque impacta directamente en su salud y
        bienestar. Es fundamental considerar sus necesidades y preferencias para el
        éxito del proyecto.

   2.4.2. Mantener satisfechos (Alto Poder / Bajo Interés)

      ● Institución educativa (UTEC): Tiene interés en el éxito del proyecto (por el
        prestigio, la innovación, etc.), pero su interés directo en el día a día del uso del
        pastillero es menor. Sin embargo, tiene el poder de asignar recursos, evaluar el
        proyecto, etc.
      ● Posibles Inversionistas/Financiadores: Si buscas financiamiento externo, los
        inversionistas tendrían el poder de decidir si apoyan o no el proyecto. Su interés
        se centraría principalmente en la viabilidad y el retorno de la inversión.

   2.4.3. Mantener informados (Bajo Poder / Alto Interés)

      ● Profesionales de la salud (médicos, farmacéuticos): Tienen un alto interés en
        que el pastillero mejore la adherencia de sus pacientes, lo que impacta
        positivamente en los resultados de los tratamientos. Sin embargo, su poder
        directo sobre la decisión de compra del usuario final puede ser limitado.
       2.4.4. Monitorear (Bajo Poder / Bajo Interés)

           ● Otros fabricantes de dispositivos médicos: Pueden tener un interés lejano en el
             mercado de dispositivos para el cuidado en el hogar, pero su poder de influencia
             directa en este proyecto específico es bajo.
           ● Comunidad local: La comunidad en general puede tener un interés indirecto en
             proyectos que mejoren la calidad de vida de los adultos mayores, pero su poder
             de influencia es limitado.

     Figura 3
     Matriz de poder e interés de los stakeholders del proyecto




Nota. La matriz de la clasificación de los actores clave del proyecto según su nivel de poder e
interés en relación con el desarrollo del dispositivo.


   2.5. Alcance de proyecto
   El presente proyecto tiene como objetivo desarrollar un prototipo funcional de pastillero
   electrónico programado con Arduino, diseñado para facilitar la administración de
   medicamentos en personas que requieren una ingesta organizada y puntual. Este dispositivo
   permitirá:
           ● Programar horarios específicos para la dispensación de pastillas.
           ● Emitir alertas sonoras y visuales claras para recordar la toma.
           ● Dispensar las dosis correspondientes mediante compartimentos automatizados.
           ● Ser operado a través de una interfaz sencilla y accesible, sin requerir
       conocimientos técnicos previos.
   2.5.1. El desarrollo abarcará

       1.   Diseño y ensamblaje del prototipo físico.
       2.   Programación en Arduino para gestión de horarios, alertas y dispensación.
       3.   Implementación del sistema de notificación (luces, sonido).
       4.   Pruebas iniciales y ajustes para garantizar funcionamiento y precisión.

   2.5.2. Enfoque y Limitaciones

   El proyecto está enfocado principalmente en adultos mayores que requieren un control
   en la toma de sus medicinas. Este primer prototipo tendrá las siguientes limitaciones
   intencionadas:

       ●    No incluirá conectividad a internet, aplicaciones móviles o sistemas externos.
       ●    No contará con sensores biométricos, ni monitorización avanzada del paciente.
       ●    Se centrará en la dispensación de pastillas sólidas de tamaño estándar.
       ●    La capacidad de almacenamiento será definida durante el diseño detallado, pero
            será limitada para un prototipo inicial.

   Estas funcionalidades podrían considerarse para futuras versiones, pero están fuera del
   alcance de este proyecto inicial para mantener la viabilidad y el enfoque en la
   funcionalidad central y la usabilidad. Se busca ofrecer una solución accesible, funcional
   y fácil de usar que contribuya a mejorar la adherencia a los tratamientos y brinde mayor
   independencia.


2.6. Objetivos
   2.6.1. Objetivo General
   Desarrollar un prototipo funcional de pastillero electrónico basado en Arduino que
   facilite la administración de medicamentos a adultos mayores, mediante la dispensación
   automatizada de pastillas en horarios programados y la emisión de alertas efectivas para
   recordar su toma.


   2.6.2. Objetivos Específicos

       ● Analizar el contexto social y tecnológico de la administración de medicamentos
         en adultos mayores en Lima, identificando los principales problemas,
         necesidades, criterios de diseño y actores clave que sustenten el desarrollo del
         prototipo.
       ● Diseñar y ensamblar un prototipo físico del pastillero que permita almacenar de
         forma segura y dispensar automáticamente dosis de pastillas sólidas.
       ● Programar y validar un sistema en Arduino capaz de gestionar múltiples
           horarios de dispensación (configurables por el usuario/cuidador) y activar
           alertas sonoras y visuales claras y perceptibles.
         ● Implementar una interfaz de usuario física (botones, pantalla simple) que sea
           intuitiva y fácil de operar por adultos mayores con limitada experiencia
           tecnológica para la configuración básica y confirmación de toma.
         ● Evaluar la usabilidad y funcionalidad del prototipo mediante pruebas con
           usuarios potenciales (adultos mayores y/o cuidadores) para recoger feedback e
           identificar mejoras.
         ● Analizar la viabilidad preliminar del dispositivo en términos de costos de
           componentes del prototipo y facilidad de ensamblaje para una posible futura
           implementación a mayor escala.


  2.7. Consideraciones del entorno
     Al momento de desarrollar este proyecto, se han tomado en cuenta distintos aspectos
     del entorno que podrían influir tanto en su diseño, como en su uso final.
     En la actualidad, uno de los grupos más vulnerables en cuanto al manejo adecuado de
     la medicación son los adultos mayores. Muchos de ellos deben seguir tratamientos
     médicos constantes para controlar enfermedades crónicas como la hipertensión,
     diabetes, artritis, entre otras. Sin embargo, debido a factores como el deterioro de la
     memoria, la pérdida de visión o la dependencia de terceros, pueden tener dificultades
     para recordar la toma adecuada de sus medicamentos en los horarios establecidos.
     Por ello, es común que las familias adquieran pastilleros tradicionales para ayudar a
     organizar las dosis diarias. A pesar de su bajo costo, estos dispositivos son
     completamente manuales y requieren que el adulto mayor recuerde por sí mismo
     cuándo tomar la pastilla, lo cual puede no ser efectivo en muchos casos.
     En otros casos, muchas personas adultas mayores ni siquiera utilizan pastilleros, sino
     que suelen guardar sus medicamentos en cajas improvisadas o los colocan en desorden
     sobre una mesa, estante o en su mesita de noche. Esta forma de organización puede
     generar confusiones, olvidos o incluso errores en la toma, como repetir dosis o saltarse
     pastillas, lo cual pone en riesgo su salud y bienestar.


3. Análisis de Mercado


  3.1. Público objetivo
     El público objetivo primario y secundario para este pastillero electrónico incluye:
         ● Primario: Adultos mayores (60+ años) residentes en Lima, que toman múltiples
           medicamentos diariamente debido a enfermedades crónicas (diabetes,
           hipertensión, etc.) y presentan olvidos frecuentes o dificultades para gestionar
           sus horarios de medicación. Buscan mantener su independencia pero necesitan
             apoyo confiable.
           ● Secundario: Cuidadores (familiares o profesionales) y familiares directos de
             estos adultos mayores, quienes buscan asegurar la correcta administración de
             los medicamentos, reducir su carga de supervisión y tener mayor tranquilidad.
           ● Potencial Terciario: Pacientes con enfermedades crónicas de otras edades que
             requieran un control riguroso de su medicación y valoren la automatización y
             los recordatorios.
   3.2. Descripción del público objetivo


       Figura 5
       Perfil del usuario principal para el diseño del pastillero inteligente




Nota. Se ha elaborado a partir del análisis de entrevistas y observaciones aplicadas a personas
mayores de 60 años en Lima Metropolitana.
Link del formato: Canva
Resultados de entrevistas:Entrevistas


3.3. Metodología
   3.3.1. Enfoque
   Se emplea un enfoque cualitativo para comprender con profundidad los hábitos,
   dificultades y perspectivas de adultos mayores en torno a la toma de medicamentos.
   3.3.2. Técnicas de recolección de datos
   Se realizaron entrevistas semiestructuradas a un total de 16 adultos mayores del Centro
   Integral del Adulto Mayor (CIAM) ubicado en Barranco, enfocadas en sus experiencias
   personales con la administración de medicamentos, su relación con la tecnología y
   disposición a usar dispositivos electrónicos de asistencia.
   3.3.3. Criterios de selección
   Los participantes fueron seleccionados considerando la variedad en edad y
   disponibilidad de tiempo que contaban para ser entrevistados.
   3.3.4. Análisis de resultados
   Las entrevistas fueron registradas en un documento word, además de ser registradas en
   un forms, así podremos identificar patrones comunes, dificultades recurrentes y
   oportunidades de mejora por medio de gráficos didácticos.

       ➔ Gráficos de las entrevistas
   En la Figura 5, se puede visualizar en que entre las 16 adultos mayores entrevistados,
   el 43.8% (7 personas) solo consume un medicamento al día, además de que el 18.8%
   (3 personas) consumen 2 y el 25% (3 personas) consume 3 medicamentos. Mientras
   tanto, el porcentaje del consumo de 4 a más medicamentos es mucho mejor que las
   anteriores.

   Figura 5
   Frecuencia diaria de toma de medicamentos entre adultos mayores entrevistados
Mientras que en la Figura 6, se observa que el 25% de los entrevistados (4 personas)
organiza sus medicamentos utilizando un pastillero, mientras que otro 25% (4 personas)
prefiere hacerlo mediante una lista escrita.

Figura 6
Gráfica de organización de medicamentos




En la Figura 7, se visualiza que la mayor dificultad que manejan los adultos mayores
es el olvido, que cuenta con un 75% (12 personas). También que la confusión por la
cantidad y horarios completos cuentan con un 18.8% (3 personas cada uno).

Figura 7
Gráfica dificultades o desafíos para tomar medicamentos.
En la Figura 8, se puede se puede visualizar que hay un 40% (6 personas) de
entrevistados que sí usan aparatos electrónicos pero les cuesta mucho. Con un 33.3%
(5 personas) que si saben usar y los usa con frecuencia. También que solo hay un
13.3% (2 personas) que no los usa y no tienen intereses.

Figura 8
Utilización de aparatos electrónicos en adultos mayores




De igual forma en la Figura 9, se visualiza que hay un 81% (13 personas) que
sugieren que si existiría un aparato así, la función que sería más útil es el aviso con
sonido. La segunda función más útil llega a ser el aviso con luz, con un 50% (8
personas).

Figura 9
Gráfica funciones necesarias que consideran los adultos mayores
En la Figura 10, podemos concluir que la mayor preocupación al usar este dispositivo
llega a ser quedarse sin batería con un 37.5% (6 personas), también se ve que no
funcione bien y no hay preocupación tiene un 31.3% (5 personas).

Figura 10
Gráfica de preocupaciones que podrían surgir al comprar el dispositivo




3.3.5. Resultados preliminares
A partir de las entrevistas realizadas, se identificaron patrones y comportamiento
comunes respecto a la administración de medicamentos y el uso de tecnología:

    ● Se realizaron entrevistas a 16 adultos mayores residentes en Lima, con el
objetivo de conocer sus hábitos y dificultades en la administración de medicamentos
diarios.
    ● El 43.8% (7 personas) consume solo un medicamento al día. Un 18.8% (3
   personas) toma dos medicamentos y el 25% (4 personas) consume tres o más,
   evidenciando una diversidad en la carga de medicación diaria.
        ● Respecto a cómo se organizan para tomar sus pastillas, el 25% (4 personas)
   utiliza un pastillero semanal, otro 25% (4 personas) sigue listas escritas, mientras que
   el resto depende de la memoria o rutinas personales sin herramientas específicas.
        ● El olvido fue mencionado como la principal dificultad por el 75% (12 personas),
   seguido por la confusión con las dosis o los horarios (18.8%).
        ● En relación al uso de tecnología, el 40% (6 personas) declaró usar aparatos
   electrónicos pero con dificultad, el 33.3% (5 personas) los utiliza con confianza, y el
   13.3% (2 personas) no los usa ni tiene interés en hacerlo.
        ● Sobre las funciones deseadas en un dispositivo de ayuda, el 81% (13 personas)
   valoró los avisos sonoros como los más útiles, y el 50% (8 personas) mencionó los
   avisos visuales con luz como complemento ideal.
        ● La principal preocupación sobre el uso de un dispositivo electrónico es quedarse
   sin batería (37.5%), seguida por el temor a fallos técnicos (31.3%). Un grupo menor
   expresó no tener preocupaciones al respecto.
3.4. Mapa de empatía
   3.4.1. Mapa de empatía individual
   Nos ayuda a entender mejor la experiencia personal de cada entrevistado. Ya que cada
   persona tiene su propia historia, rutina y forma de organizarse.


   Figura 11
   Mapa de empatía individual
Nota. Mapa construido a partir de la entrevista realizada a un adulto mayor del distrito de
Barranco, con el fin de identificar sus percepciones, emociones y necesidades respecto al
cumplimiento de su tratamiento médico.


       Análisis:
          ● Tiene una rutina establecida, lo que le facilita tomar su medicación, pero admite
            que eventos como el cansancio pueden hacerle olvidar alguna dosis.
          ● Valora los recordatorios claros (alarmas, avisos) como apoyo, especialmente si
            fueran parte de un dispositivo sencillo y confiable.
          ● No ha usado tecnología para la salud, pero está abierto a aprender si se ofrecen
            talleres o explicaciones claras.
          ● Reconoce que otras personas mayores pueden tener más dificultades, por lo que
            ve valor en dispositivos que apoyen la autonomía en esa etapa de la vida.
          ● Preocupación por la precisión y el orden, lo que sugiere que soluciones
            tecnológicas deben ser fáciles de usar, seguras y adaptadas para adultos
            mayores.


       3.4.2. Mapa de empatía grupal
       Permite identificar lo que varios entrevistados tienen en común. Así podemos ver más
       fácilmente qué necesidades, frustraciones o deseos se repiten en el grupo, y pensar en
soluciones que funcionen para la mayoría


Figura 12
Mapa de empatía grupal




Nota. Mapa construido en base a entrevistas y observaciones realizadas a un grupo de
adultos mayores con tratamientos médicos continuos. Se utilizó como herramienta de
análisis para comprender sus hábitos, barreras tecnológicas y necesidades funcionales.
Análisis:
   ● El olvido y la confusión con horarios y dosis son los principales retos
     compartidos entre los adultos mayores entrevistados.
   ● Aunque algunos utilizan alarmas o pastilleros, muchos no se sienten cómodos
     con la tecnología, lo que limita el uso de aplicaciones o dispositivos
     electrónicos.
   ● Existe un fuerte deseo de mantener su autonomía en el manejo de la medicación,
     sin depender completamente de familiares o cuidadores.
   ● Preocupa el no seguir adecuadamente el tratamiento, tanto por efectos adversos
     como por la responsabilidad que sienten con su salud.
   ● Se valoran las soluciones simples, claras y accesibles, como dispositivos con

              recordatorios visuales o sonoros, que no requieran tanto conocimientos técnicos
              para su uso.
Link del formato: Canva


3.5. ¿Cuál es la competencia?
      3.5.1. MedMinder
       Es una plataforma revolucionaria para gestión de medicamentos. Mejora la adherencia
       al tratamiento con el dispensador automático de pastillero MedMinder.
       Mercado: Funciona en varios países, entre ellos Alemania, Australia y Perú.
       Costo: Tiene una tarifa de iniciación de $100 USD (372. 31 sol peruano), para luego
       pagar una suscripción mensual de $125 USD (465.38 soles peruano). Estos costos
       incluyen al pastillero.


       Figura 13
       Pastillero MedMinder




Nota. Imagen tomada del sitio web oficial de MedMinder Technologies Inc. El dispositivo
permite programar compartimentos con alertas y conexión remota. Tomado de MedMinder
(s.f.), https://www.medminder.com

      3.5.2. Hero
      Es un dispensador inteligente que avisa cuando es hora de tomar las pastillas, cuenta
      con una app que realiza un seguimiento para una mejora administración de cada
      consumo de pastillas.
      Mercado: Su mercado se extiende principalmente en países latinoamericanos como
      México, Brasil, Argentina y Chile. El pastillero no tiene una presencia oficial
      ampliamente reconocida en Perú, pero es posible que se realice por compras online o
      distribuidoras.
      Costo: Tiene un costo de suscripción de $44.99 USD (169.30 soles peruano) te
       permitirá tener acceso a funciones adicionales de la app, aparte el costo del dispensador
       de pastillas tiene un costo de $99.99 USD (376.26 soles peruano).

       Figura 14
       Dispensador de pastillas HERO




Nota. Dispositivo inteligente que dispensa automáticamente medicamentos y permite controlar
la adherencia mediante una aplicación móvil. Imagen tomada de HERO Health (s.f.),
https://www.herohealth.com

       3.5.3. Medisafe
       Es una aplicación que te ayuda a llevar un registro de la toma de tus medicamentos. Te
       permite crear una lista de medicamentos y configurar recordatorios o indicaciones para
       recordar la correcta toma.
       Mercado: Para el alcance de todos
       Costo: Se puede tener la aplicación de forma gratuita pero solo hasta dos medicamentos.
       Para añadir más, es necesario suscribirse con un costo entre $2.99 y $9.99 USD ( 11.25
       y 37.59 soles peruano).
   Figura 15
   Aplicación Medisafe




Nota. Captura de la tienda de aplicaciones de Google Play que muestra la interfaz de la app
Medisafe    para   recordatorio    de   medicamentos.      Tomado      de   Medisafe     (s.f.),
https://play.google.com/store/apps/details?id=com.medisafe.android.client


       3.5.4. Pastillero simple
       Es un recipiente que se utiliza para organizar las dosis de medicamentos, ayuda a
       planificar la toma regular de medicamentos y tomar la dosis correcta de medicamentos.
       Mercado: Para el alcance de todos
       Costo: Tiene un precio de S/. 21 hasta S/. 81 soles, todo dependerá del tamaño, cantidad
       y lugar de compra del pastillero.


       Figura 16
       Pastillero simples
Nota. Captura de pantalla de resultados de búsqueda de pastilleros en una tienda en línea,
utilizada como referencia visual del tipo de productos disponibles para la organización manual
de medicamentos. Tomado de Mercado Libre Perú (s.f.), https://www.mercadolibre.com.pe
3.6. Matriz de Benchmark
      La Tabla 1, presenta un análisis comparativo de diversos productos existentes en el mercado relevantes para el pastillero electrónico
      propuesto. Esta matriz tiene como propósito contrastar las características técnicas y operacionales de distintos dispositivos y aplicaciones
      utilizados para la gestión de medicamentos. Los productos que se incluyen en esta comparativa son MedMinder, Hero, la aplicación móvil
      Medisafe, los pastilleros simples o manuales, y el pastillero electrónico que constituye la propuesta del proyecto. Las características
      específicas consideradas para la comparación en la tabla abarcan las Dimensiones, el Tipo de producto (como Dispensador automático,
      App móvil u Organizador manual), el Peso, el Costo y la Fuente de Alimentación (Adaptador de corriente, Batería del celular, N/A o Pilas).

      Tabla 1
      Matriz de Benchmark

          Características /                                                                                             Pastillero
                                   Medminer                 Hero               Medisafe         Pastillero simple
            Productos                                                                                                  electrónico

                                                                                                     Varía
                                                      22.9 x 22.9 x 38.1
          Dimensiones            30 x 23 x 5 cm                                   N/A           dependiendo del      25 x 10 x 4 cm
                                                              cm
                                                                                                   pastillero

                                   Dispensador           Dispensador                              Organizador          Dispensador
          Tipo                                                                 App móvil
                                   automático            automático                                 manual             automático

          Peso                        0,8 kg               4,54 kg                N/A              Muy ligero             0,8 kg

          Costo                     $125/mes               $50/mes              $10/mes               S/. 81              S/. 30

                                  Adaptador de          Adaptador de          Batería del
          Alimentación                                                                                 N/A                 Pilas
                                   corriente             corriente             celular
4. Propuesta de valor
  4.1. Conclusiones de los análisis previos
          ● La mayoría de los encuestados toma medicamentos más de una vez al día, lo
     que confirma la necesidad de un dispositivo que administre múltiples dosis diarias de
     forma programada.
          ● El olvido y la confusión con los horarios o tipos de medicamentos se
     identificaron como los principales problemas en la gestión diaria, evidenciando la
     importancia de incorporar recordatorios efectivos.
          ● Muchos usuarios aún utilizan métodos manuales como pastilleros simples o
     listas escritas, y más de la mitad no ha usado tecnología relacionada con su salud, lo
     que refuerza la necesidad de una solución sencilla y accesible.
          ● Las funciones más valoradas por los usuarios fueron los avisos sonoros y
     visuales, lo cual valida su inclusión en el diseño del producto.
          ● La recepción general de la idea fue positiva, destacando más el interés por un
     dispositivo que facilite la toma correcta de medicamentos sin depender de otros.
          ● A pesar de que existen otros dispositivos parecidos analizados en la
     competencia , estos no tienen las funcionalidades que tiene el pastillero electrónico ,
     convirtiéndolo en un pastillero multiusos.


  4.2. Diferencial del producto
  El producto se diferencia notablemente de los pastilleros tradicionales y de algunos
  modelos inteligentes disponibles actualmente en el mercado.A diferencia de los sistemas
  actuales como Medminder y Hero, que se concentran en dispensaciones automatizadas y
  alertas móviles, nuestra píldora inteligente ofrece más características adaptadas hacia este
  público.


  El proyecto propone un dispositivo que no solo alerta mediante luz y sonido cuando es
  momento de tomar el medicamento, sino que también dispensa la pastilla correcta y la dosis
  indicada, incluso si requiere estar dividida (media píldora), debido a un mecanismo de corte
  incorporado.

  A diferencia de los pastilleros comunes , que requieren operación manual para acceder a
  los compartimentos y recuperar las tabletas, el dispositivo inteligente automatiza el
  procedimiento de dispensación. La programación se realiza de forma sencilla desde casa,
  sin necesidad de asistencia técnica, lo cual lo hace ideal para personas mayores que no
  siempre tienen supervisión médica o familiar constante.


  Además muchos dispositivos electrónicos actuales para la gestión de medicamentos están
  diseñados para administrar una única pastilla por día o tienen una capacidad limitada para
   manejar múltiples dosis diarias. Por ejemplo, el pastillero electrónico VitaCarry permite
   configurar alarmas sonoras y visuales para recordar la toma de medicamentos, pero su
   diseño está orientado a dispensar una sola dosis en momentos específicos, sin la capacidad
   de gestionar múltiples tipos de medicamentos o fraccionar dosis. El pastillero inteligente
   podrá programar más de una pastilla al día , haciéndolo más eficaz y eficiente .


   4.3. Conceptos de solución
       4.3.1. Creación de bocetos
       A continuación, se presentan los diferentes bocetos realizados para el diseño conceptual
       del pastillero inteligente. Estos bocetos reflejan las primeras ideas sobre la estructura y
       funcionalidad del dispositivo, con el objetivo de explorar distintas configuraciones que
       permitan una interacción eficiente del usuario con el sistema. Cada boceto muestra
       diferentes soluciones para la organización interna del pastillero, los mecanismos de
       dispensado y las interfaces de usuario, tales como botones de programación y activación
       de alarmas. Estos diseños conceptuales sirven como punto de partida para el desarrollo
       y perfeccionamiento de un prototipo funcional del dispositivo.
       Suangyi

       Figura 17

       Boceto 1 de pastillero electrónico




Nota. Primer diseño conceptual a mano alzada del prototipo de pastillero electrónico, que
incluye divisiones por horario y botón de activación de alarma.
       Cesar
       Figura 18
       Boceto 2 de pastillero electrónico




Nota. Boceto digital que muestra la disposición de componentes internos y vista superior del
dispositivo. Diseñado como parte del proceso iterativo de desarrollo.
       Nataly
       Figura 19
       Boceto 2 de pastillero electrónico




Nota. Propuesta de pastillero con forma de cápsula, luces indicadoras y panel de programación
con pantalla y botones.
       Marycielo
       Figura 20
       Boceto 2 de pastillero electrónico




Nota. Representación esquemática del dispositivo que incluye programación de alarma, luz
parpadeante y salida de sonido.
       4.3.2. Creación de boceto final
       La figura 21 muestra el primer boceto conceptual, esta fue una propuesta inicial para el
       diseño del pastillero electrónico, cuyo objetivo era automatizar la administración de
       medicamentos. El dispositivo se basaba en un sistema de fajas transportadoras, que
       permite la distribución precisa de las pastillas según el horario programado por el
       usuario. Asimismo, el sistema de control Arduino gestiona tanto el proceso de
       dispensación como la interacción del usuario con el dispositivo. El diseño incluía una
       estructura compacta que alberga tanto el mecanismo de las fajas como la interfaz de
       usuario, que cuenta con una pantalla LCD para mostrar la cantidad de pastillas y un
       botón para activar la alarma de recordatorio. Este primer diseño estaba orientado a
       asegurar la funcionalidad básica del sistema, con énfasis en la correcta organización y
       entrega de las dosis de manera programada.

       Figura 21
       Primer Boceto de pastillero electrónico




Nota. Representa la primera propuesta del dispositivo, basado en un sistema de bandas y control
Arduino.
Boceto final (cambia parte interna)
Luego de evaluar los espacios requeridos y los requisitos de almacenamiento, se decidió
modificar el diseño inicial del pastillero para maximizar la capacidad de con respecto a
la cantidad de pastillas. La Figura 22 muestra la vista externa del pastillero automático
final, donde se pueden observar los componentes principales que conforman el
dispositivo. Se destaca la estructura compacta que permite maximizar la capacidad de
almacenamiento de pastillas, facilitando al mismo tiempo la accesibilidad para el
usuario. En esta vista se aprecian la pantalla LCD, que proporciona información clara,
y los botones de control que permiten la programación del dispositivo. Además, cuenta
con una salida para la dispensación de las pastillas, lo que facilita su retiro. Este diseño
externo está orientado a optimizar la funcionalidad y la simplicidad de uso del
pastillero.
Figura 22
Vista externa del pastillero automático final.
La Figura 23, muestra la vista interna del pastillero automático final, donde se aprecian
los componentes clave que permiten el funcionamiento del dispositivo. Se observa el
mecanismo de almacenamiento y dispensación de pastillas, que incluye los tubos
contenedores para cada tipo de pastilla, asegurando una correcta separación y
almacenamiento. Además, en esta vista se destacan la pantalla LCD, que proporciona
información al usuario, y los botones de control para la programación del dispositivo.
El sistema está impulsado por motores de liberación, que, una vez activados, permiten
el desplazamiento de las pastillas a través de los tubos hasta la salida. Este diseño
interno asegura un flujo eficiente y controlado de las pastillas, contribuyendo a la
correcta dispensación según lo programado por el usuario.


Figura 23
Vista interna del pastillero automático final.
4.3.3. Diagrama de bloques funcional

Los diagramas funcionales que se presentan a continuación ilustran el flujo de
información y control dentro del pastillero automático. Estos diagramas proporcionan
una visión general de cómo interactúan los diferentes componentes del sistema, desde
las entradas iniciales hasta las salidas finales, permitiendo una comprensión clara de
cómo se gestiona el proceso de dispensación de medicamentos. Cada diagrama resalta
diferentes aspectos del funcionamiento del dispositivo, incluyendo el manejo de los
datos, los procesos de activación y los mecanismos involucrados en la entrega precisa
de las pastillas
4.3.3.1 Diagrama funcional principal
En la figura 24, se muestra el diagrama funcional este presenta una visión simplificada del flujo de información y control dentro
del pastillero automático. Este diagrama divide el proceso en tres bloques principales: entradas, proceso y salidas. Las entradas
incluyen la hora de toma programada, los botones de programación y los sensores que detectan la presencia de pastillas. El bloque
de proceso es gestionado por un controlador Arduino, que se encarga de activar los servomotores conectados a una cremallera para
liberar las pastillas en el momento adecuado. Finalmente, las salidas incluyen las alertas visuales y sonoras, así como los mensajes
en la pantalla LCD y la activación de los motores para el movimiento de las pastillas. Este diagrama facilita la comprensión del
flujo de trabajo y las interacciones dentro del sistema, mostrando cómo cada componente contribuye al funcionamiento general del
pastillero.

Figura 24
Diagrama funcional del sistema pastillero automático.
4.3.3.2. Diagrama funcional general:
En la figura 25 se muestra el diagrama funcional general este proporciona una visión detallada de la arquitectura funcional del
sistema dispensador de pastillas. En este diagrama, se muestra el flujo de energía y control desde la fuente de alimentación hasta la
salida de las pastillas, incluyendo la interacción entre los componentes esenciales del sistema, como el procesador Arduino, los
sensores de presencia y los servomotores conectados a las cremalleras. El diagrama también destaca los componentes de control,
como el display LCD, el control de alarma y las señales de entrada, que permiten la interacción del usuario con el dispositivo.
Figura 25
Arquitectura funcional del sistema dispensador de pastillas.
5. Planificación de proyecto
      5.1. Especificaciones Técnicas
         5.1.1. Listar necesidades
         En la tabla 2 presentada a continuación, se muestran las funciones necesarias para el
         funcionamiento del pastillero inteligente, organizadas por tipo de componente y con su
         respectivo nivel de importancia. Cada necesidad está clasificada en diferentes áreas
         como control, almacenamiento, dispensación, energía y materiales, reflejando los
         requisitos esenciales que debe cumplir el sistema. Los valores de importancia asignados
         a cada necesidad permite priorizar las funcionalidades clave para el desarrollo y la
         eficiencia del dispositivo. Esta tabla es fundamental para garantizar que el diseño del
         pastillero cumpla con los estándares y objetivos establecidos.

         Tabla 2
         Identificación de necesidades del sistema pastillero inteligente.


                                                                                    Importancia
Ítem         Elemento                                Necesidad
                                                                                       (0-5)


 1            Control       Tiene que controlar 4 servomotores                           5


 2            Control       Tiene que emitir una alarma sonora                           4


 3            Control       Tiene que emitir una alarma visual                           4


 4            Control       Tiene que ser programable para horarios diferentes           5


 5            Control       Tiene que mostrar datos en un display                        3


 6            Control       Tiene que detectar cuando ya no hay pastillas                3


 7            Control       Fácil de programar                                           5


 8        Almacenamiento    Tubos que puedan contener varias pastillas                   4


 9        Almacenamiento    Tubos que puedan contener diversos tipos de pastillas        4


 10        Dispensación     Tiene que ser dispensado mediante una cremallera             4


 11           Energía       Que tenga un bajo voltaje de alimentación                    3
12    Energía     Que tenga la potencia necesaria para que funcione   3


13    Energía     Que funcione a pilas                                3


14   Materiales   Que sea de fácil limpieza                           4


15   Materiales   Que tenga un peso adecuado                          5
             5.1.2. Matriz Necesidad/ Métrica

             La Tabla 3 se muestra la matriz de correlación entre necesidades y métricas esta tiene
             como objetivo vincular las funciones esenciales del pastillero inteligente con las
             métricas técnicas que permitirán evaluar su rendimiento. En esta tabla, cada necesidad
             funcional se asocia con una o más métricas técnicas, lo que facilita el diseño y la
             validación del sistema. Esta herramienta es crucial para garantizar que las
             características del dispositivo, como el control de motores, el sistema de alarmas o la
             capacidad de almacenamiento, se cumplan de acuerdo con los parámetros técnicos
             establecidos, optimizando recursos y asegurando el cumplimiento de los requisitos del
             proyecto.

             Tabla 3
             Matriz de correlación entre necesidades del sistema y métricas técnicas.

                                                             1   2   3   4   5   6   7   8   9   10   11   12   13




             Necesidad / Métrica                             N
                                                             N
                                                             i
                                                             I
                                                                                 V
                                                                                 C
                                                                                 D               F
                                                                                                 a
                                                                                                 T
                                                                                                 i
                                                                                                 T
                                                             N
                                                             ú
                                                             V                   P               i
                                                                                                 C
                                                                                                 a




1    Tiene que controlar 4 servomotores                      X
2    Tiene que emitir una alarma sonora                          X
3    Tiene que emitir una alarma visual                              X
4    Tiene que ser programable para horarios diferentes                                               X
5    Tiene que mostrar datos en un display                   X
6    Tiene que detectar cuando ya no hay pastillas                                                    X         X
7    Fácil de programar                                                                               X
8    Tubos que puedan contener varias pastillas                          X X
9    Tubos que puedan contener diversos tipos de pastillas                   X
10   Tiene que ser dispensado por una cremallera             X
11   Caída de tensión                                                            X
12   Potencia necesaria para que funciones el equipo                             X X
13   Que utilice pilas                                                                   X
14   Requiere que sea de fácil limpieza                                                          X
15   Que tenga un peso adecuado                                                        X              X
            5.1.3. Lista de Métricas
            La Tabla 4 presentada a continuación es fundamental para establecer una relación entre
            las necesidades funcionales del sistema del pastillero inteligente y los requisitos
            técnicos necesarios para garantizar su correcto desempeño. Cada necesidad identificada
            en el dispositivo está vinculada a una métrica específica que se utilizará para validar si
            las funcionalidades del sistema se cumplen adecuadamente. Esta lista de métricas no
            solo proporciona las unidades de medida para cada parámetro, sino que también asigna
            un nivel de importancia a cada uno, asegurando que las características más críticas del
            dispositivo reciban la atención y el diseño adecuados. A través de estas métricas, el
            equipo de desarrollo puede asegurar que el pastillero cumpla con las expectativas tanto
            de funcionalidad como de rendimiento, logrando así un sistema eficiente y efectivo para
            la administración automatizada de medicamentos.

            Tabla 4
            Definición de métricas técnicas para validar requerimientos del sistema.

            Número de                                                Importancia
     Ítem                                     Métrica                                      Unidades
            necesidad                                                   (0-5)

      1       1, 5, 10    Número de salidas de control                    5                  unid

      2          2        Nivel sonoro                                    4                  dB

      3          3        Intensidad de luz                               4                  lm

      4          8        Número de compartimientos                       5                  unid

      5         8, 9      Volumen de compartimentos                       5                  𝑚2

      6        11, 12     Voltaje                                         4                   V

      7          12       Consumo de corriente                            5                   A

      8          13       Duración de batería                             5                 horas

      9          15       Peso                                            5                  Kg

      10         14       Facilidad de limpieza                           4                   -

      11       4, 6, 7    Tiempo/pasos de programaciòn                    4                   s

      12         15       Tipo de material                                3                   -

      13         6        Cantidad y tipo de sensores                     3                  unid

       5.1.4. Benchmark Cuantitativo
       La Tabla 5 presentada en esta sección tiene como objetivo evaluar el rendimiento de
       las métricas clave del diseño del pastillero inteligente frente a dos dispositivos
       comerciales de referencia: Medminder y Hero. Esta comparación es esencial para medir
       y validar la efectividad y eficiencia del pastillero propuesto en aspectos como el número
       de salidas de control, la intensidad de la luz, el consumo de energía, y otros parámetros
       fundamentales para su funcionalidad. A través de esta tabla, podemos observar cómo
       se alinean las características del pastillero inteligente con las expectativas y
       especificaciones de dispositivos comerciales en el mercado, lo cual facilita la
       identificación de áreas de mejora y asegura que el diseño cumpla con los estándares
       más altos.

       Tabla 5
       Comparación de métricas técnicas entre dispositivos comerciales Medminder y Hero.

Íte   Número de                          Imp (0-                     Compt. 1        Compt. 2
                            Métrica                  Unidades
m     necesidad                            5)                      (Medminder)        (Hero)

                  Número de salidas de
1       1, 5, 6                             5          unid             4               3
                  control

2         2       Nivel sonoro              4           dB              70              65

3         3       Intensidad de luz         4          lum              15              25

                  Número de
4         8                                 5          unid             28              10
                  compartimientos

                  Volumen de
5        8, 9                               5          𝑐𝑚3              18             100
                  compartimentos

6       10, 11    Voltaje                   4           V               9               12

7         11      Consumo de corriente      5          mA            100-200         200-400

8         12      Duraciòn de batería       5         horas             48              6

9         12      Peso                      5          Kg               1.5             4.5

                  Tiempo/pasos de
11       4, 6                               4          min            10-15             10
                  programaciòn
       5.1.5. Benchmark Cualitativo
       La Tabla 6 de evaluación de cumplimiento de necesidades compara cómo los
       dispositivos comerciales Medminder y Hero satisfacen las necesidades identificadas en
       el diseño del pastillero inteligente. Cada necesidad ha sido evaluada en función de su
       importancia (de 0 a 5), y se analiza el cumplimiento de estas por parte de ambos
       dispositivos. Este análisis permite identificar las fortalezas y debilidades de los
       productos comerciales existentes, en relación con las características clave que se
       requieren para el funcionamiento óptimo del pastillero, como la capacidad para
       controlar motores, emitir alarmas sonoras y visuales, la facilidad de programación, la
       detección de pastillas, y otros parámetros esenciales. A través de esta comparación, se
       pueden tomar decisiones informadas sobre cómo mejorar el diseño del sistema
       propuesto.

       Tabla 6
       Evaluación de cumplimiento de necesidades por los dispositivos Medminder y Hero.


                                                         Imp (0-     Compt. 1      Compt. 2
Ítem                        Necesidad
                                                           5)      (Medminder)      (Hero)


 1     Tiene que controlar 4 servomotores                  5            0             0

 2     Tiene que emitir una alarma sonora                  4            5             4

 3     Tiene que emitir una alarma visual                  4            5             4

       Tiene que ser programable para horarios
 4                                                         5            5             5
       diferentes

 5     Tiene que mostrar datos en un display               3            5             3

 6     Tiene que detectar cuando ya no hay pastillas       3            3             3

 7     Fácil de programar                                  5            0             0

 8     Tubos que puedan contener varias pastillas          4            5             5

       Tubos que puedan contener diversos tipos de
 9                                                         4            4             4
       pastillas

 10    Tiene que ser dispensado por minipistones           4            3             3

 11    Caída de tensión                                    3            3             3

 12    Potencia necesaria para que funciones el equipo     3            4             2

 13    Que utilice pilas                                   3            4             4

 14    Requiere que sea de fácil limpieza                  4            3             3

 15    Que tenga un peso adecuado                          5            3             3
         5.1.6. Especificaciones objetivo
         La Tabla 7 de especificaciones de diseño presenta los valores marginales e ideales para
         cada una de las métricas clave del sistema, basados en su importancia y requisitos
         funcionales. Esta tabla es fundamental para establecer los rangos aceptables que
         garantizan el correcto funcionamiento del pastillero inteligente. A través de la
         comparación entre los valores marginales y los ideales, se define un estándar de diseño
         que debe cumplirse para asegurar que el dispositivo sea eficiente, seguro y cumpla con
         las expectativas del usuario. Estos valores se han establecido considerando las
         necesidades más importantes del sistema, tales como el número de salidas de control,
         el volumen de compartimentos, la duración de la batería y el peso del dispositivo, entre
         otros.

         Tabla 7
         Especificaciones de diseño: valores marginales e ideales por métrica técnica.


       Número de                                       Impt (0-             Valor
Ítem                               Métrica                        Unid.                  Valor Ideal
       necesidad                                         5)                Marginal


 1       1, 5, 6    Número de salidas de control          5       unid         1           2 o más


 2         2        Nivel sonoro                          4        dB          60            80


 3         3        Intensidad de luz                     4       lum         200           400


 4         8        Número de compartimientos             5       unid         4             6


 5        8, 9      Volumen de compartimentos             5       𝑐𝑚3          5             10


 6       10, 11     Voltaje                               4        V           5             3.7


 7         11       Consumo de corriente                  5       mA          500           200



 8         12       Duraciòn de batería                   5       horas        6          24 o más



 9         12       Peso                                  5        Kg          4             3


 11       4, 6      Tiempo/pasos de programaciòn          4       min          4             2
5.1.7.Diagrama de bloques
En la Figura 26 se presenta el diagrama de bloques del sistema pastillero automático,
donde se detallan las diferentes etapas que conforman su funcionamiento: sensado,
control, comunicación de datos, fuente de energía, actuadores, interfaz de usuario y
dispensado. Este diagrama es de gran importancia porque ofrece una visión general y
clara de cómo interactúan los distintos componentes del sistema, lo cual es fundamental
para su diseño, implementación y diagnóstico. Además, facilita la comprensión del
flujo de información y energía, asegurando que el sistema opere de manera eficiente y
coordinada.

Figura 26
Diagrama de bloques del sistema pastillero automático.
Nota. Se representan los módulos funcionales del dispositivo y la interacción entre sus
componentes electrónicos y mecánicos.

   5.2. Procesos de Manufactura del Prototipo Funcional( mejorar)

       Para la creación del prototipo funcional del pastillero electrónico, se emplearán
       materiales y procesos que garanticen la viabilidad del diseño, la facilidad de
       fabricación y la funcionalidad de los componentes.

       5.2.1. Compra de Material:

       La Tabla 8 presenta un resumen detallado de los materiales necesarios para la
       adquisición en diferentes procesos, indicando sus formatos o presentaciones comunes,
       así como los canales habituales para su compra. Esta información es esencial para
       facilitar la identificación y obtención de los insumos requeridos en proyectos o
       actividades específicas. En la tabla se incluyen materiales como MDF, acrílico, motores
       paso a paso, tubos de PVC, interruptores y componentes electrónicos, especificando
       tanto las características físicas de cada material (como dimensiones o presentaciones)
          como los lugares y tipos de proveedores donde pueden ser adquiridos, tales como
          tiendas de materiales de construcción, ferreterías, distribuidores especializados y
          plataformas en línea. Esta guía resulta fundamental para optimizar la logística y
          asegurar la disponibilidad oportuna de los recursos en los proyectos.

          Tabla 8

          Materiales, formatos y canales de adquisición para el pastillero electrónico.


                                             Presentación/Formato de
               Material                                                             Canales de Adquisición
                                                   Adquisición
                                                                            Tiendas de materiales de construcción,
MDF (Tablero de Fibra de Densidad    Planchas o láminas (e.g., 3mm, 5mm,
                                                                            carpinterías, distribuidores de tableros
Media)                               6mm)
                                                                            de madera.
                                                                            Tiendas de plásticos, distribuidores de
Acrílico (Transparente para 1 cara,  Planchas o láminas (e.g., 3mm, 4mm
                                                                            materiales para rótulos, ferreterías
Opaco/Color para otras)              de espesor)
                                                                            grandes.
                                                                            Tiendas de electrónica, distribuidores
Motores Paso a Paso (NEMA 17 o
                                     Por unidad o en pequeños lotes         de componentes para robótica,
similares)
                                                                            plataformas en línea.
Tubos de Almacenamiento de Pastillas Barras o tramos (diámetro interior 1.5 Ferreterías, tiendas de materiales de
(PVC)                                cm a 2.5 cm aprox.)                    plomería, distribuidores de plásticos.
                                                                            Tiendas de electrónica, plataformas en
Interruptores (Switch)               Por unidad o en pequeños paquetes
                                                                            línea.
                                                                            Tiendas de electrónica especializadas,
Componentes Electrónicos (Arduino,
                                     Por unidad o en kits                   distribuidores de componentes,
Drivers, LCD, LEDs, Cables, etc.)
                                                                            plataformas en línea.




          5.2.2. Selección del Material:

          La elección de MDF y acrílico para la carcasa del prototipo funcional, y PVC para los
          tubos de almacenamiento, se justifica por las siguientes razones:

              ● MDF para Estructura Principal: Ofrece una base sólida, estable y económica
                para la estructura interna y algunas caras externas del pastillero. Es un material
                fácil de cortar y ensamblar con precisión mediante técnicas de corte láser.
              ● Acrílico Transparente para Visibilidad: La cara frontal o lateral de la carcasa se
                fabricará con acrílico transparente. Esto es fundamental para el prototipo, ya
                que permitirá al usuario y al diseñador observar el funcionamiento interno del
                mecanismo de dispensación, el movimiento de los motores, los pistones y el
                flujo de las pastillas desde los tubos hacia la salida. Esta visibilidad es crucial
                para la depuración, validación visual del prototipo y para la confianza del
       usuario. Además, el acrílico transparente ofrece un acabado estético limpio y
       moderno.
   ●   Facilidad de Procesamiento: Ambos materiales son ideales para técnicas de
       corte asistido por computadora como el corte láser y el ruteado CNC, lo que
       permite fabricar piezas con alta precisión y repetibilidad a partir de diseños
       digitales (CAD). El acrílico, además, se puede termoformar (doblar con calor)
       para crear curvas o ángulos si el diseño lo requiere.
   ●   Costo-Efectividad: Son materiales relativamente económicos y de fácil acceso,
       lo que resulta ventajoso para la fase de prototipado donde pueden ser necesarias
       varias iteraciones de diseño y fabricación.
   ●   Rigidez Estructural: Ambos materiales ofrecen una rigidez adecuada para la
       carcasa de un prototipo funcional, soportando los componentes internos sin
       deformaciones significativas bajo condiciones de uso normales.
   ●   Aislamiento Eléctrico: Son materiales no conductores, lo que contribuye a la
       seguridad al aislar los componentes eléctricos internos del contacto directo con
       el usuario.

Para los Tubos de Almacenamiento de Pastillas, se ha seleccionado el PVC sobre el
MDF debido a las siguientes consideraciones:

   ● Adecuación para Pastillas y Higiene: El PVC es un material inerte, no reactivo
     con la mayoría de los medicamentos y de superficie lisa. Su lisura interna es
     crucial para facilitar el deslizamiento de las pastillas sin que se adhieran o se
     generen fricciones que puedan dañarlas. A diferencia del MDF, el PVC no es
     poroso, lo que lo hace más higiénico y fácil de limpiar, evitando la absorción de
     humedad o la acumulación de residuos de pastillas que podrían comprometer la
     calidad o el dispensado.
   ● Forma Cilíndrica y Precisión: El PVC se produce en formas tubulares precisas,
     lo cual es fundamental para un flujo constante y controlado de las pastillas. El
     MDF, al ser un tablero de fibras, sería muy difícil de moldear en tubos lisos y
     uniformes que garanticen un dispensado fiable.
   ● Variedad de Diámetros para el Tamaño de Pastillas en General: El PVC se
     fabrica en una amplia gama de diámetros estándar, lo que permite seleccionar
     el tamaño adecuado para acomodar diversas formas y tamaños de pastillas
     genéricas (desde comprimidos pequeños hasta cápsulas más grandes) sin
     problemas de atasco, asegurando la versatilidad del pastillero.
   ● Disponibilidad y Costo: Los tubos de PVC están ampliamente disponibles en el
     mercado local y son muy económicos.

Tabla 9

Materiales seleccionados para la construcción del dispositivo y su justificación

   Material                              Justificación para la Selección
                               Ofrece una base sólida, estable y económica para la estructura interna y
MDF (Tablero de Fibra de
                               algunas caras de la carcasa. Es un material fácil de cortar y ensamblar con
Densidad Media)
                               precisión mediante técnicas de corte láser.

                               Para una de las caras de la carcasa, permitiendo visualizar el funcionamiento
                               interno (mecanismo de dispensación, motores, pistones, flujo de pastillas).
Acrílico Transparente
                               Crucial para depuración, validación visual y confianza del usuario. Ofrece un
                               acabado estético.
                             Material inerte y no reactivo con medicamentos, superficie lisa para fácil
PVC (Tubos de Almacenamiento deslizamiento. Más higiénico y fácil de limpiar que el MDF (no poroso). Se
de Pastillas)                produce en formas tubulares precisas para flujo constante. Amplia variedad
                             de diámetros para tamaño general de pastillas. Económico y disponible.

Nota. Esta tabla detalla los materiales clave empleados en el diseño del dispositivo,
considerando funcionalidad, costo y facilidad de fabricación

       5.2.3. Proceso de Manufactura que se usará

       Para la fabricación del prototipo funcional, se emplearán principalmente los siguientes
       procesos:

            ● Diseño CAD: Todas las piezas de la carcasa (internas y externas), incluyendo
              los soportes y guías para los tubos de pastillas, se diseñarán en el software
              Inventor para asegurar el encaje preciso de los componentes electrónicos y
              mecánicos, y para generar los archivos necesarios para el corte láser o CNC.

            ● Fabricación de la Carcasa (MDF y Acrílico):
                 ○ Corte Láser: Las piezas de MDF y acrílico se cortarán utilizando una
                     máquina de corte láser. Este método asegura bordes limpios, precisión
                     dimensional y eficiencia en la producción de las formas complejas
                     requeridas para la carcasa y los compartimentos internos. La cara
                     transparente de acrílico se cortará con el mismo proceso, con especial
                     cuidado para evitar daños a la superficie.
                 ○ Ruteado CNC: Para piezas de mayor grosor de MDF o para operaciones
                     como el grabado o el fresado de ranuras más profundas, se podría utilizar
                     un ruteador CNC si el corte láser no fuera suficiente para ciertos detalles
                     estructurales.
                 ○ Termoformado (Acrílico, si aplica): Si el diseño incluye curvas, se
                     realizará un doblado en caliente de las láminas de acrílico.
                 ○ Lijado y Pulido: Los bordes cortados se lijarán y pulirán (especialmente
                     el acrílico) para eliminar rebabas, suavizar las superficies y mejorar la
                     seguridad y la estética.

            ● Ensamblaje de la Carcasa:
                 ○ Las piezas de la carcasa se ensamblarán utilizando adhesivos adecuados
                    para MDF y acrílico (ej. pegamento cianocrilato, pegamento para
              acrílico, epoxi) y/o mediante uniones mecánicas como tornillos o
              encajes machihembrados diseñados en el CAD. Se prestará especial
              atención a la fijación del panel transparente para asegurar su estabilidad
              y la clara visualización interna.

   ● Mecanizado de Tubos de Almacenamiento (PVC): Los tubos de PVC se
     cortarán a la longitud deseada con una sierra o cortatubos, y sus extremos se
     pueden lijar para un acabado suave y para asegurar que no haya obstrucciones
     o raspaduras al introducir las pastillas.

   ● Ensamblaje Electrónico:
        ○ Soldadura: Los componentes electrónicos (Arduino, drivers de motor,
           cables, sensores, LEDs, etc.) se soldarán a un protoboard o a una PCB
           (Printed Circuit Board) diseñada específicamente, siguiendo el diagrama
           esquemático. Esto incluye la conexión de los cables a los motores paso
           a paso y a la pantalla LCD.
        ○ Cableado y Conexiones: Se realizarán las conexiones eléctricas entre el
           Arduino y los demás módulos (motores, sensores, pantalla, switch)
           utilizando cables jumper y asegurando un aislamiento adecuado para
           evitar cortocircuitos.

   ● Integración y Montaje Final:
         ○ Los motores paso a paso se montarán de forma segura dentro de la
            carcasa, alineados con los mecanismos de dispensación que
            interactuarán con los tubos de PVC.
         ○ Los tubos de PVC se insertarán en sus ranuras o soportes dentro de la
            estructura de MDF/acrílico, asegurando que las pastillas caigan
            correctamente en el mecanismo de dispensación.
         ○ La pantalla LCD, botones e interruptores se fijarán en las aberturas pre-
            cortadas en la carcasa.
         ○ El Arduino y los demás módulos se montarán en soportes internos (que
            podrían ser impresos en 3D) o fijados directamente a la base de la
            carcasa, cuidando que no interfieran con la visualización a través del
            panel transparente.

   ● Programación: El código para el Arduino se cargará y se realizarán pruebas de
     funcionamiento exhaustivas para verificar la correcta operación de los motores,
     la pantalla, las alarmas y el mecanismo de dispensación de pastillas. Se validará
     visualmente el proceso a través de la cara transparente para identificar posibles
     fallos mecánicos o de flujo.



Tabla 10
                Etapas del proceso de fabricación e integración del dispositivo

         Etapa del Proceso                                 Descripción/Actividades Concisas

                                  Diseño de piezas en Inventor para carcasa y guías. Generación de archivos para corte
Diseño CAD
                                  láser/CNC.
                                  Corte láser (MDF/Acrílico, cuidando acrílico transparente), Ruteado CNC (opcional),
Fabricación de la Carcasa
                                  Termoformado (acrílico, si aplica), Lijado/Pulido.

Ensamblaje de la Carcasa          Unión de piezas con adhesivos/tornillos. Enfoque en panel transparente.


Mecanizado de Tubos (PVC)         Corte de tubos de PVC a medida. Lijado de extremos.

                                  Soldadura de componentes (Arduino, drivers, etc.). Cableado y conexiones con
Ensamblaje Electrónico
                                  aislamiento.
                                  Montaje seguro de motores, tubos PVC, pantalla, botones, Arduino dentro de la carcasa.
Integración y Montaje Final
                                  Asegurar alineación y visibilidad.

Programación y Pruebas de         Carga de código Arduino. Pruebas para verificar operación y dispensación. Validación
Funcionamiento                    visual por cara transparente.




        Nota. Esta tabla describe las fases técnicas clave en la producción del dispositivo, desde el
        diseño hasta la verificación de su funcionamiento.
5.3. Criterios de Ergonomía
   5.3.1. Peligros generados por la máquina:

   Se deben identificar y mitigar los riesgos inherentes al diseño y funcionamiento del
   dispositivo.

   5.3.1.1. Mecánico:
   Los peligros mecánicos se derivan de las partes móviles y la estructura física del
   prototipo.

      ● Atrapamiento o Pinzamiento:
         ○ Mecanismo de Dispensación: Los motores paso a paso que accionan los
             pistones o mecanismos rotatorios para dispensar las pastillas pueden
             generar un riesgo de pinzamiento si el usuario introduce los dedos en la
             zona de salida de las pastillas o en los mecanismos internos durante su
             funcionamiento. Es vital que la apertura de dispensación sea lo
             suficientemente estrecha para evitar la introducción accidental de dedos
             (especialmente de niños), o que se incorpore un mecanismo de seguridad
             que detenga el movimiento si se detecta una obstrucción.
         ○ Cierre de Compartimentos/Tapas: Si el sistema de carga o recarga de las
             pastillas involucra tapas o compartimentos móviles, un diseño inadecuado
             podría causar un riesgo de atrapamiento de dedos durante el cierre.

      ● Corte o Abrasión:
         ○ Bordes de la Carcasa: Los bordes de las piezas de MDF o acrílico, si no
             están debidamente lijados o pulidos después del corte láser o CNC, pueden
             ser afilados y causar cortes o abrasiones, especialmente al manipular el
             dispositivo para recargar o limpiar.
         ○ Mecanismos Internos Accesibles: Si alguna parte del mecanismo interno
             (ej. engranajes, ejes de motores, bordes del sistema de pistones) es
             accesible, podría causar cortes o abrasiones. La cara transparente de
             acrílico ayudará a visualizar, pero también debe asegurar un sellado
             completo para evitar el acceso a estas partes.

      ● Impacto o Golpe:
          ○ Componentes Móviles: Si alguna parte móvil del mecanismo de
            dispensación (ej. el pistón al salir de su posición de reposo) se extiende o
            retrae con fuerza y está expuesta, podría generar un leve riesgo de impacto
            si el usuario se acerca demasiado.
          ○ Inestabilidad del Dispositivo: Un diseño inestable o con un centro de
            gravedad alto puede provocar que el pastillero se caiga, generando un
            riesgo de golpe para el usuario (especialmente si es un adulto mayor frágil)
            o daños al dispositivo.
   ● Obstrucción o Bloqueo:
      ○ Pastillas Atascadas: Si el mecanismo de dispensación no es preciso o las
          pastillas no son homogéneas en tamaño/forma, podrían atascarse en los
          tubos de PVC o en el mecanismo. Esto puede llevar a frustración y a que
          el usuario intente desobstruir el mecanismo manualmente, lo que podría
          derivar en un riesgo de daño al dispositivo o lesiones.
      ○ Entrada de Objetos Extraños: Si hay ranuras o aberturas por donde puedan
          introducirse objetos pequeños (ej. clips, juguetes) dentro del mecanismo,
          podría provocar un bloqueo y un mal funcionamiento, y generar un peligro
          si el usuario intenta remover el objeto.

5.3.1.2. Eléctrico:
Los peligros eléctricos están asociados con la fuente de alimentación y los componentes
electrónicos del pastillero.

   ● Choque Eléctrico (Descarga):
      ○ Exposición de Cables y Conexiones: Un cableado interno mal aislado o
          expuesto, o la presencia de conexiones directas a la fuente de alimentación
          (pilas o adaptador externo, si aplica) sin protecciones adecuadas, podría
          causar una descarga eléctrica si el usuario entra en contacto directo,
          especialmente en ambientes húmedos o con manos mojadas. La carcasa
          (incluyendo la cara transparente de acrílico) debe sellar eficazmente todos
          los componentes eléctricos para evitar el contacto accidental.
      ○ Contactos de Batería: Si los compartimentos de las pilas o sus contactos
          metálicos están expuestos y el usuario los toca directamente con objetos
          conductores o manos mojadas, podría haber un riesgo de descarga (aunque
          bajo con pilas AA de 1.5V). El compartimento de las pilas debe ser de
          acceso seguro y solo para el cambio de estas, con una tapa que requiera
          una herramienta simple o sea de difícil apertura para niños.
   ● Cortocircuito y Sobrecalentamiento:
      ○ Cableado Incorrecto o Dañado: Un cortocircuito debido a un cableado
          defectuoso, una instalación incorrecta o un daño en los cables puede
          generar un calor excesivo, humo, fusión del material de la carcasa (MDF
          o acrílico, que son inflamables en condiciones extremas) e incluso riesgo
          de incendio. Se deben utilizar fusibles adecuados para proteger el circuito
          y asegurar que el cableado esté ordenado y protegido.
      ○ Sobrecarga de Componentes: Si los motores o drivers son sometidos a una
          carga excesiva o si el diseño eléctrico no incluye protecciones adecuadas
          (ej. disipadores de calor en drivers de motor, si es necesario), pueden
          sobrecalentarse y dañarse, generando un riesgo de incendio.
      ○ Baterías Defectuosas o Instalación Incorrecta: Aunque es poco común con
          pilas AA, las baterías defectuosas o las instaladas incorrectamente podrían
          sobrecalentarse. Si se considera una batería recargable o un adaptador
                       AC/DC en el futuro, los riesgos de sobrecalentamiento y falla aumentan
                       si el circuito de carga o la fuente no son seguros y certificados.
               ● Quemaduras:
                   ○ Componentes Calientes: Algunos componentes como los drivers de
                       motores o reguladores de voltaje pueden generar calor durante el
                       funcionamiento prolongado. Si son accesibles (lo cual se evitará con la
                       carcasa y la cara transparente) y no están aislados o tienen disipadores,
                       podrían causar quemaduras leves por contacto.
               ● Interferencia Electromagnética (EMI):
                   ○ Aunque no es un peligro directo de seguridad física, el dispositivo podría
                       generar interferencias electromagnéticas si no está diseñado con la
                       compatibilidad adecuada, lo que podría afectar el funcionamiento de otros
                       dispositivos electrónicos sensibles cercanos (como marcapasos, audífonos
                       o radios), lo cual es una preocupación importante para los adultos
                       mayores. Se recomienda un buen apantallamiento de los circuitos si es
                       posible y realizar pruebas de compatibilidad electromagnética.

            Tabla 11

            Identificación de peligros mecánicos y eléctricos en el dispositivo


    Tipo de Peligro                 Peligro Específico                      Descripción Concisa
                                                                 Dedos en salida/mecanismos móviles o
Mecánico                  Atrapamiento o Pinzamiento             tapas.
                                                                 Bordes afilados de carcasa o mecanismos
Mecánico                  Corte o Abrasión                       internos.
                                                                 Partes móviles expuestas o caídas del
Mecánico                  Impacto o Golpe                        dispositivo.
                                                                 Pastillas atascadas o entrada de objetos
Mecánico                  Obstrucción o Bloqueo                  extraños.

                                                                 Contacto con cables/conexiones expuestas
Eléctrico                 Choque Eléctrico (Descarga)            o fuente de energía.
                                                                 Cableado defectuoso o sobrecarga de
Eléctrico                 Cortocircuito y Sobrecalentamiento     componentes/baterías.
                                                                 Contacto con componentes electrónicos
Eléctrico                 Quemaduras                             calientes.

                                                                 Afectación a otros dispositivos electrónicos
Eléctrico                 Interferencia Electromagnética (EMI)   cercanos.


Nota. La tabla presenta los riesgos mecánicos y eléctricos más relevantes identificados
durante el análisis de seguridad del dispositivo.
       5.3.2. Ergonomía:

       5.3.2.1. Comunicación hombre máquina a través de indicadores
       La siguiente Tabla 12 nos indica los diferentes usos de ejemplo que tendrá el pastillero
       ,entre el dispositivo y el usuario. Con el objetivo de mejorar la comunicación entre
       hombre-máquina mediante los siguientes indicadores mostrados en la misma tabla,
       además que nos ayuda a mejorar la accesibilidad del dispositivo .

       Tabla 12
       Usos y ejemplos de comunicación hombre-máquina mediante indicadores en el
       sistema

                           Usos                                             Ejemplos

                                                        Colores distintos para cada compartimento
     Identificar función
                                                        (mañana, tarde, noche)

     Dar instrucciones                                  Voz grabada diciendo “Tome su pastilla”

     Dar advertencias                                   Alarmas

     Mostrar información cualitativa                    LED rojo: pendiente / LED verde: dispensada

                                                        Pantalla LCD mostrando horas restantes para la
     Mostrar información cuantitativa
                                                        próxima dosis


Nota. Se describen diferentes formas en que el dispositivo comunica información al usuario
mediante señales visuales y auditivas.


       A continuación se muestra la Tabla 13 donde se puede apreciar los indicadores
       visuales que tendrá el pastillero a comparación con los indicadores auditivos detallando
       sus características y beneficios específicos que tendrá con el usuario.El objetivo es
       analizar cómo estas señales se utilizan para comunicar la información.

       Tabla 13
       Comparación entre indicadores auditivos y visuales en el sistema.

    Indicadores Auditivos                                 Indicadores Visuales

    Emiten sonido corto y reconocible                     Led rojo :pendiente/Led verde dispensada

    Útil si el usuario no está mirando el dispositivo     Útil si el usuario tiene problema auditivos

    No requiere que el usuario esté cerca
                                                          Útil incluso en lugares demasiados ruidosos
    visualmente
       En la siguiente Tabla 14 explora la relación entre el tipo de información de los
       indicadores preferidos escogidos y algunos comentarios , sugerencias u
       observaciones que podría tener al implementarlo en el sistema con el objetivo de
       analizar las formas más efectivas de llegar al usuario y que éste a su vez se le pueda
       hacer fácil de entender.

       Tabla 14
       Relación entre tipo de información, indicador preferido y su aplicación en el sistema.

                         Indicador
 Tipo de información                                Comentarios                     Aplicaciones
                         preferido

                                        Mucha precisión para mostrar la hora
                                                                                Muestra: ”Próxima
Cuantitativa           Pantalla (LCD)   exacta en la que deben tomar las
                                                                                dosis en 2h 15min”
                                        pastillas

                                        Fácil de reconocer para adultos
                        Luz LED con                                             Verde :Dispensada
Cualitativa                             mayores , y más que todo con los
                            color                                               Rojo:Pendiente
                                        colores representativos




                                                                                A la hora de tomar
                                        La combinación de esto puede resultar
                                                                                pastillas , indica un
                                        beneficioso para usuarios con
                        Sonido +Luz                                             sonido y una luz
Aviso /Alerta                           limitaciones sensoriales , incluso se
                        intermitente                                            intermitente que es
                                        combina con sonido lo que le haces
                                                                                hora de tomar las
                                        mucho más fácil darse cuenta
                                                                                pastillas




                                                                                Etiqueta de un icono
                          Etiquetas     Deben ser muy simples y un poco
Símbolo o Gráfico                                                               en el pastillero:
                           grandes      grandes para mejorar su visualización
                                                                                ”Aquí tomar”
       5.3.2.2. Posturas recomendadas
       En la Tabla 15 se presenta una comparación entre dos alternativas de postura (A y B)
       para el uso funcional de un dispositivo, considerando parámetros como carga ligera,
       uso prolongado, buena iluminación, trabajo preciso, uso intermitente, portabilidad,
       espacio reducido y uso en cama o silla. Esta tabla es útil para identificar la postura más
       ergonómica y adecuada según el contexto operativo, permitiendo al usuario tomar
       decisiones informadas sobre la mejor forma de utilizar el dispositivo en distintos
       escenarios, optimizando la comodidad, eficiencia y adaptabilidad del diseño a las
       condiciones reales de uso.

       Tabla 15
       Comparación de alternativas A y B según parámetros de uso funcional.

      Parámetros                                                  A              B

      Carga ligera                                                P             SP

      Uso prolongado                                              S             SP

      Buena iluminación                                           SP             P

      Trabajo preciso                                             S             SP

      Uso intermitente                                            SP             S

      Portabilidad                                                SP             P

      Espacio reducido                                            SP             S

      Uso en cama o silla                                         S             SP


       P = De pie; S = Sentado; SP = Sentado o de pie.

Nota. Se evaluaron las opciones A y B de acuerdo con criterios como portabilidad, iluminación,
uso prolongado y espacio disponible.

       5.3.2.4. Esquema

       En la Figura 27 se presenta un mapa conceptual del pastillero inteligente, donde se
       representa su estructura lógica y funcional. La figura clasifica los componentes
       principales del dispositivo en tres bloques: mecánicos, electrónicos y lógicos, y describe
       la secuencia de funcionamiento desde la programación del horario por parte del usuario
       hasta la liberación automática de la pastilla. Esta representación es útil para visualizar
       de forma clara e integrada cómo interactúan las distintas partes del sistema, facilitando
       la comprensión de su diseño, operación y lógica de automatización para el suministro
       de medicamentos.
       Figura 27
       Mapa conceptual del pastillero inteligente: componentes y funcionamiento.




Nota. Se representa la estructura lógica y funcional del dispositivo, clasificando sus
componentes principales en bloques mecánicos, electrónicos y lógicos, junto con su secuencia
de uso.

   5.4. Criterios de Seguridad y Prevención de Accidentes
       El diseño del pastillero inteligente se ha elaborado teniendo en cuenta criterios de
       ergonomía que aspiran a optimizar la experiencia de uso, en particular para individuos
       de edad avanzada. Dentro de los factores evaluados, se incluyen la iluminación y el
       ruido.
           ● Iluminación: Dado que los usuarios objetivo pueden presentar limitaciones
               visuales, se ha contemplado la incorporación de indicadores luminosos tipo
               LED de alta visibilidad. Estos serán ubicados en zonas estratégicas para
               mostrar que ya es hora de consumir su medicamento.
              ● Ruido: El sistema utilizará señales sonoras para emitir recordatorios sobre la
                toma de medicamentos. De acuerdo con estándares internacionales de
                ergonomía, se ha determinado que los niveles de ruido emitidos por el
                dispositivo no deberán superar los 80 decibeles (dB).
        5.4.1. Recomendación de diseño y protección:
        En la Tabla 16 se recopilan recomendaciones fundamentales de seguridad organizadas
        en tres ejes: prevención, protección e información, considerando tanto las medidas que
        debe aplicar el diseñador como aquellas que corresponden al usuario final del
        dispositivo. Esta clasificación permite abordar de manera integral los riesgos
        potenciales durante el diseño, fabricación y uso del pastillero inteligente. La utilidad de
        esta tabla radica en que proporciona una guía clara para minimizar accidentes,
        garantizar la integridad del usuario, facilitar el entendimiento del funcionamiento del
        equipo, y reforzar el uso adecuado mediante elementos visuales, capacitaciones y
        advertencias accesibles.

        Tabla 16
        Recomendaciones de diseño, protección e información para la seguridad del usuario
        y del dispositivo.

                        Prevención                     Protección                      Información

                                                - Compartimentos seguros
               - Diseño compacto y estable                                  - Manual visual con pictogramas
                                                - Alarmas sin sobresalto
Medidas de     - Batería protegida                                          - Indicadores LED y sonoros claros
                                                - Mecanismo bloqueable
seguridad      - Evitar esquinas agudas                                     - Instrucciones accesibles y grandes
                                                - Batería con protección
del            - Uso de materiales                                          - Instrucciones escritas en letra
                                                interna
diseñador      resistentes                                                  grande
                                                - Material no tóxico y
               - Diseño de fácil limpieza
                                                antialérgico

                                                - Limpieza periódica
                                                                            - Capacitación para el familiar
               - Uso en superficies firmes      - No exponer a humedad
                                                                            - Supervisión si hay deterioro
Medidas de     - No forzar mecanismos           - Uso en ambientes
                                                                            cognitivo
seguridad      - Ubicar en superficie estable   ventilados
                                                                            - Señales claras para mantenimiento
del usuario    - No manipular con manos         - No mojar el dispositivo
                                                                            - Señales sonoras fáciles de
               mojadas                          - Mantener fuera del
                                                                            reconocer
                                                alcance de niños
Nota. La tabla organiza medidas de seguridad del diseñador y del usuario en tres enfoques:
prevención, protección e información, aplicadas al diseño del dispensador automático.


    5.5. Diagrama de Gantt
        Link: Diagrama de gantt
5.6. Presupuesto
   Este presupuesto se encuentra alineado con las actividades del diagrama de Gantt y
   responde directamente a los objetivos específicos del proyecto, permitiendo
   materializar el diseño, programación, ensamblaje, validación y análisis de viabilidad
   del prototipo.

   Tanto el objetivo “Evaluación con usuarios potenciales” y “Investigación y análisis de
   contexto socio-tecnológico y de stakeholders”, no tienen relación con los cuadros de
   presupuesto presentados presentes.


   Tabla 17
   Materiales Electrónicos y de Ensamblaje
Nota: La tabla está relacionada con los objetivos específicos “Diseño y ensamblaje físico del prototipo”,
“Programación del sistema y gestión de alertas” y “Interfaz de usuario intuitiva” que muestra los
componentes electrónicos y materiales de ensamblaje utilizados en la construcción del prototipo. Los
precios están expresados en soles peruanos y corresponden a valores referenciales según cotizaciones
locales. Esta tabla no incluye servicios de fabricación ni costos logísticos.




Tabla 18

Materiales de Fabricación (estructura y carcasa)

 Ítem              Descripción                          Cant.                 Subtotal (S/.)


   1       ¼ plancha MDF                                   1                  25.00

   2       Retazo de acrílico 3 mm                         1                  20.00

   3       PLA (para impresión 3D)                       1 kg                 70.00


Nota: La tabla está relacionada con los objetivos específicos “Diseño y ensamblaje
físico del prototipo” y “Análisis de viabilidad técnica y económica” . La tabla 18 nos
muestra los materiales utilizados para la fabricación de la estructura y carcasa del
pastillero electrónico. El PLA fue empleado para las piezas impresas en 3D, mientras

que el MDF y el acrílico conforman el cuerpo y los compartimentos internos del
dispositivo.



Tabla 19

Servicios técnicos

  Ítem                           Servicio                         Subtotal (S/.)

    1           Servicio de corte láser MDF                             25

    2           Servicio de corte láser acrílico                        50

    3           Servicio de impresión 3D                                70

    4           Diseño y planos de fabricación                         100

    5           Mano de obra                                           870

Nota: La tabla 19 está relacionada con los objetivos específicos “Diseño y ensamblaje
físico del prototipo” y “Análisis de viabilidad técnica y económica”. Se puede visualizar
los servicios técnicos detallados en la tabla comprenden procesos especializados
tercerizados para la elaboración del prototipo. Incluyen el diseño digital de planos, la
fabricación mediante impresión 3D y corte láser, así como la mano de obra para el
ensamblaje completo del dispositivo.

Tabla 20

Costos logísticos

  Ítem                           Servicio                         Subtotal (S/.)

    1           Pasajes de transporte                                   40

    2           Transporte de piezas y materiales                       20

Nota: La tabla 20, está relacionada con el objetivo específico “Análisis de viabilidad
técnica y económica”. Este monto corresponde a los gastos de transporte realizados
durante el desarrollo del proyecto, incluyendo traslados para la adquisición de
materiales, entrega a proveedores y recojo de piezas fabricadas.

El costo total del proyecto asciende a S/ 1,508.90, e incluye los materiales electrónicos
y de ensamblaje utilizados en el prototipo (S/ 218.90), los materiales de fabricación
para la estructura y carcasa (S/ 115.00), los servicios técnicos como corte láser,
       impresión 3D y mano de obra (S/ 1,115.00), así como los costos logísticos asociados al
       transporte de piezas y materiales (S/ 60.00).


6. Ejecución de Proyecto
   6.1. Propuesta de materiales para una versión comercial

Si bien nuestro prototipo fue desarrollado con materiales accesibles y funcionales para validar
el concepto, consideramos importante identificar qué componentes serían más adecuados para
una futura versión comercial del pastillero.

La Tabla 21 presenta una propuesta de materiales que podrían ser utilizados en un modelo
optimizado para el mercado, priorizando mayor durabilidad, mejor desempeño eléctrico y una
fabricación más profesional. Estos elementos incluyen componentes de marcas reconocidas,
conectores reforzados, placas PCB diseñadas para producción y sistemas de alimentación más
seguros.

Complementariamente, en la Tabla 22 se muestra una comparación entre los materiales
empleados en el prototipo y aquellos que se podrían implementar en un diseño comercial. Esta
diferencia evidencia cómo se puede mejorar el producto en términos de calidad, resistencia,
seguridad y presentación, aspectos clave si se busca escalar el proyecto hacia un uso real en
centros de salud o comercialización abierta.




       Tabla 21

       Materiales adecuados para el pastillero dentro del mercado

         Ítem               Descripción                 Cant.            Subtotal (S/.)

          1       Bornera de 2 pines (atornillable,       1              1.20
                  grado industrial)


          2       Capacitor 1000 uF 25 V                  1              1.50
                  (electrolítico bajo ESR)

          3       Conectores JST 3 pines con              4              3.60
                  terminal crimpado
   4       Conectores Molex KK 2 pines                     4                 2.50
           reforzados

   5       Capacitor 470 uF 25 V                           1                 1.20
           (panasonic o nichicon)

   6       Buzzer piezoeléctrico                           1                 2.00
           encapsulado 5V

   7       Módulo LM2596 con protección                    1                 8.50
           térmica y contra inversión

   8       Encoder rotativo con eje                        1                 9.00
           metálico y botón táctil

   9       Microcontrolador ATmega328                      1                 10.00
           standalone con base DIP

   10      LEDs SMD 3 mm alta                              5                 1.50
           luminosidad

   11      Transistor 2N2222 encapsulado                   1                 0.60
           metálico (mejor disipación)

   12      Conectores dupont hembra con                    2                 2.50
           carcasa de seguridad

   13      Batería recargable Li-ion 3.7V                  1                 12.00
           con circuito de protección

   14      Servomotor digital MG90S con                    4                 45.00
           engranaje metálico

   15      Kit tornillos acero inoxidable M3               1                 8.00
           + tuercas

Nota. La Tabla 21 presenta los materiales seleccionados para una versión comercial del pastillero
electrónico, priorizando criterios de calidad, seguridad y durabilidad. Los componentes listados
responden a estándares de diseño electrónico profesional, optimizados para producción a mayor escala y
uso prolongado. Incluyen mejoras en conectividad, resistencia mecánica y protección eléctrica.

Tabla 22

Diferencias con nuestros materiales



                   Actual                                        Comercial


Capacitores y resistencias genéricas, sin       Capacitores de marca reconocida (Panasonic,
marca ni protección especial                     Nichicon) con baja ESR y mayor vida útil
       Servomotores plásticos comunes (SG90)               Servomotores MG90S con engranajes
                                                            metálicos, mayor torque y duración

       Placa virgen perforada (protoboard o PCB         PCB FR4 doble capa, diseñado y producido
       básica)                                                    profesionalmente

       Pila de botón genérica y batería sin              Batería Li-ion con circuito de protección y
       protección                                         módulo de respaldo con control de carga

       Componentes visibles, sin protección ni               Cables siliconados, conectores con
       acabado estético                                  aislamiento, tornillos de acero inoxidable




       Nota. La Tabla 22 resume las diferencias clave entre los materiales empleados en el prototipo funcional
       y aquellos que serían adecuados para una versión comercial del producto. Las mejoras incluyen el uso
       de componentes de mayor calidad, durabilidad y seguridad eléctrica, con estándares que permiten una
       fabricación más robusta, segura y estéticamente apta para el usuario final. Esta comparación se basa en
       criterios de diseño electrónico profesional y buenas prácticas de manufactura.




6.2. Fabricación de componentes del prototipo funcional
6.2.1 Sistema electrónico del prototipo
Para el desarrollo del prototipo, se diseñó e implementó el circuito electrónico que permite
controlar las funciones principales del pastillero. Este circuito integra los componentes
previamente seleccionados, tales como sensores, actuadores, módulos de control y
visualización. El diseño fue realizado mediante software especializado de diseño electrónico,
considerando la distribución de las pistas, el ruteo adecuado y la asignación de pines del
microcontrolador.
La Figura 28 muestra el diagrama esquemático de la placa electrónica desarrollada, donde se
detalla la conexión de cada componente con el Arduino Nano, así como la integración del
módulo RTC DS3231, los sensores LDR, el regulador LM2596, los servomotores y el display
LCD.

Figura 28

Esquemático del circuito electrónico del prototipo de pastillero, diseñado con software EDA
para el control de dispensado, visualización y alarmas.




Una vez definido el esquema electrónico general, se procedió al diseño de la placa PCB (Printed
Circuit Board), la cual permite montar y conectar de forma compacta todos los componentes
del circuito. Este diseño fue realizado utilizando software de diseño asistido por computadora
(CAD) especializado en electrónica, asegurando la correcta ubicación de los pines, el ruteo
eficiente de las pistas y la organización de las conexiones en una sola cara.

En la Figura 29 se muestra la distribución de componentes sobre la placa, mientras que la
Figura 30 presenta el diseño final de las pistas, preparado para el proceso de fabricación
mediante serigrafía o insolado.

       Figura 29

       Distribución de componentes en la placa PCB del sistema electrónico.
Figura 30
Diseño de pistas para la fabricación de la placa electrónica.
6.2.2 Diseño de carcasa del prototipo

Para complementar el sistema electrónico, se elaboró el diseño técnico de la carcasa que
contiene todos los componentes del pastillero electrónico. Este diseño fue desarrollado en
software CAD y presenta las dimensiones exactas de las caras superior, frontal y posterior del
prototipo. La carcasa no solo cumple una función estructural, sino que también facilita el
montaje de sensores, actuadores y accesos para visualización y carga de medicamentos.

Las vistas presentadas permiten una visualización clara del espacio interior disponible, los
cortes para componentes, y las perforaciones necesarias para conexiones eléctricas. Estas
especificaciones fueron fundamentales para la fabricación por corte láser y ensamblaje
posterior del dispositivo.
      Figura 31

      Planos técnicos de la carcasa: vista superior, vista frontal y vista posterior.




Nota: Los planos técnicos de la carcasa detallan las dimensiones y formas necesarias para el
corte y ensamblaje de las piezas del prototipo. Incluyen vistas superior, frontal y posterior,
fundamentales para la fabricación mediante corte láser.
Figura 32
 Visualización en 3D de la carcasa del pastillero electrónico.
Nota: El modelo tridimensional de la carcasa permite validar el diseño general antes de su
fabricación, facilitando la visualización del volumen, distribución de aberturas y
compatibilidad con los componentes internos del prototipo.




6.3. Ensamblado de componentes del prototipo funcional

6.3.1 Soldadura de componentes electrónicos
Para el ensamblado inicial del sistema electrónico, se realizó la soldadura de todos los
componentes sobre la placa PCB, siguiendo el diseño previamente elaborado. Esta tarea fue
fundamental para consolidar las conexiones eléctricas y asegurar el correcto funcionamiento
del circuito. La Figura 33, que se presenta a continuación, muestra la placa con los
componentes electrónicos ya soldados, lista para el conexionado con los demás módulos del
prototipo.

      Figura 33

      Soldadura de los componentes eléctricos en la placa del prototipo.




6.3.2                                                                       Conexionado y
pruebas                                                                     preliminares
Una vez finalizada la soldadura, se procedió al conexionado de los módulos complementarios
como el display LCD y el encoder rotativo, necesarios para la interacción con el usuario. Esta
etapa permitió realizar las primeras pruebas funcionales del sistema antes de integrarlo al
conjunto físico del pastillero. En la Figura 34, que se muestra a continuación, se aprecia la
conexión de estos módulos a la placa electrónica, evidenciando el inicio del proceso de
validación funcional.

      Figura 34

       Conexión de la placa electrónica con el display y el encoder para pruebas
      funcionales.




6.3.3                                                                              Impresión
3D de componentes mecánicos
Se llevó a cabo la impresión 3D de los tubos dispensadores y de la cremallera, la cual permite
el desplazamiento controlado de las pastillas durante el proceso de dispensado. Estas piezas
fueron diseñadas considerando la geometría interna del prototipo y su compatibilidad con los
servomotores empleados. En la Figura 35, que se muestra a continuación, se observa el
conjunto de piezas impresas en PLA listas para su posterior ensamblaje dentro del sistema.

      Figura 35

      Piezas impresas en 3D para el sistema de dispensado de pastillas.
6.3.4 Ensamblaje del sistema dispensador

Se ensambló el sistema de dispensado uniendo el tubo impreso en 3D con la cremallera y el
servomotor, verificando que el acople fuera adecuado para el movimiento rotacional del motor
y el empuje de las pastillas hacia el exterior. La Figura 36, presentada a continuación, muestra
el ensamblaje de estos elementos, evidenciando la correcta integración mecánica entre el tubo
dispensador, el servomotor y el mecanismo de desplazamiento.

      Figura 36

       Acople del tubo de pastillas con el servomotor y la cremallera del sistema
      dispensador.
6.3.5 Fabricación de carcasa

Para la fabricación de la carcasa del pastillero se utilizó acrílico blanco, el cual fue cortado
mediante láser de acuerdo con las dimensiones establecidas en los planos técnicos. Las piezas
obtenidas fueron ensambladas manualmente, cuidando que se respeten las dimensiones
internas y externas necesarias para contener los componentes del sistema.

La Figura 37, que se presenta a continuación, muestra la vista frontal de la carcasa ya
fabricada, mientras que la Figura 38 presenta la parte posterior del mismo prototipo, donde se
aprecian los detalles de armado, uniones y perforaciones posteriores necesarias para el
conexionado.

      Figura 37
Vista frontal de la carcasa del pastillero fabricada en acrílico blanco.




Figura 38

Vista posterior de la carcasa ensamblada
6.3.6 Posicionamiento de piezas internas

Una vez completado el armado de la carcasa, se procedió al posicionamiento de los
componentes internos. Esto incluye la placa electrónica, los tubos dispensadores impresos en
3D, la rampa central y el cableado general del sistema. Esta etapa permitió verificar que la
distribución física sea compatible con el funcionamiento del prototipo y que se respeten las
ubicaciones de montaje previstas en el diseño.

La Figura 39, que se muestra a continuación, evidencia el acomodo interno de las piezas
dentro de la carcasa ya ensamblada, destacando la integración ordenada del sistema
electrónico y mecánico.

      Figura 39

      Distribución interna de piezas y componentes dentro de la carcasa del prototipo
6.4.                                                                                     Ensayos y pruebas d

Concluida la etapa de ensamblaje, se procedió a realizar ensayos de funcionamiento del sistema
dispensador mediante un enfoque iterativo basado en prueba y error. Estas pruebas permitieron
verificar no solo el acoplamiento correcto entre el servomotor, la cremallera y el tubo
dispensador, sino también la precisión en la liberación de las pastillas.

Durante este proceso, se identificaron fallos relacionados con el atascamiento de pastillas y la
desalineación de los componentes móviles. Como resultado, fue necesario realizar
modificaciones en el diseño inicial de los tubos dispensadores, ajustando sus dimensiones
internas y externas para asegurar un flujo adecuado de pastillas sin comprometer la estructura
del sistema.

Paralelamente, se llevaron a cabo múltiples ajustes en la programación del microcontrolador
Arduino, con el fin de lograr una secuencia de control óptima. Estas modificaciones incluyeron
la calibración de los ángulos de giro del servomotor, el tiempo de retardo entre ciclos y la lógica
de control que garantiza la correcta sincronización entre el envío de la señal digital y la
respuesta mecánica del sistema.

Finalmente, se evaluó la sincronización entre la señal enviada desde el microcontrolador y la
respuesta del servomotor, confirmando que el mecanismo era capaz de realizar movimientos
precisos y repetibles en cada ciclo de dispensado.

En la siguiente evidencia audiovisual, se muestra el comportamiento del sistema una vez
optimizado, destacando el correcto funcionamiento del conjunto servomotor-cremallera-tubo
dispensador, así como la efectividad del algoritmo implementado en Arduino:

https://drive.google.com/file/d/1oz7Nc8-
0HzjBM3dW0Y8KfUZUQ6CZiiRP/view?usp=sharing

6.5. Validación de resultados

La validación consistió en comprobar el funcionamiento integral del pastillero electrónico a
través de pruebas prácticas, con el objetivo de verificar que cumple con los requerimientos
funcionales definidos en la etapa de diseño. Para ello, se evaluó el correcto desempeño de los
siguientes aspectos:

           ● Activación y respuesta del sistema de dispensación automatizada de pastillas.

           ● Precisión del módulo RTC (tiempo real) en la activación del sistema.

           ● Estabilidad del sistema electrónico tras un uso continuo.

           ● Interacción intuitiva del usuario con los botones del dispositivo.


Las pruebas se realizaron en un entorno controlado. Los resultados evidenciaron un
funcionamiento correcto en todos los sistemas evaluados, demostrando la viabilidad técnica
del prototipo.

A continuación, se presenta un video que muestra el funcionamiento del dispositivo en
tiempo real:

https://drive.google.com/drive/folders/1Pxl2s3bsbQhuVCTtYWV8irIEtt1Afo72
7. Conclusiones

El desarrollo del pastillero inteligente basado en Arduino ha permitido dar una respuesta
funcional e innovadora a la problemática de baja adherencia a tratamientos médicos en adultos
mayores. A través del diseño y fabricación de un prototipo funcional, se logró integrar de forma
efectiva la alerta sonoras con un sistema automatizado de dispensación de pastillas, facilitando
así la toma oportuna de medicamentos sin depender exclusivamente de la memoria del usuario.

Los análisis realizados a través de entrevistas, pruebas de usabilidad y comparativas de
mercado evidenciaron que los adultos mayores valoran especialmente la simplicidad, la
confiabilidad y la independencia que ofrece este tipo de dispositivos. Asimismo, se confirmó
que el olvido y la confusión de horarios son las principales causas de errores en la
administración de medicamentos, por lo que la incorporación de recordatorios efectivos y
mecanismos automatizados representa un avance significativo respecto a soluciones
tradicionales.

Desde el punto de vista técnico, se logró implementar una interfaz sencilla de operar, adecuada
para personas con poca experiencia en tecnología, y un sistema de dispensación fiable basado
en servomotores y tubos de PVC. El uso de materiales accesibles como MDF y acrílico permitió
mantener bajos costos de producción sin comprometer la funcionalidad.

Finalmente, este proyecto no solo propone una mejora en la calidad de vida de los adultos
mayores, sino que también representa una oportunidad para empoderar a cuidadores y reducir
su carga diaria, contribuyendo a un entorno más seguro y autónomo en el manejo de
medicamentos.




8. Recomendaciones
           ➔ Ampliar la capacidad del dispositivo: Se sugiere considerar en futuras
       versiones un diseño modular que permita almacenar mayor cantidad y variedad de
       pastillas, de acuerdo con tratamientos más complejos y prolongados.

           ➔ Incorporar conectividad inalámbrica: La integración de tecnologías como
       Bluetooth o Wi-Fi permitiría vincular el dispositivo con aplicaciones móviles,
       facilitando el monitoreo remoto por parte de familiares o cuidadores.

           ➔ Desarrollar una batería recargable: Para responder a la preocupación de los
       usuarios sobre el agotamiento de batería, se recomienda implementar un sistema de
       batería recargable de larga duración o un indicador de nivel de carga visible.

           ➔ Agregar un sistema de confirmación de toma: Un botón o sensor que registre
       la confirmación de que la pastilla fue retirada puede mejorar el control del tratamiento
       y abrir la posibilidad de generar alertas si no se registra la toma.

          ➔ Optimizar el diseño físico: Se recomienda trabajar en una versión más
       compacta y ligera del prototipo para facilitar su colocación en diferentes espacios del
       hogar y asegurar su comodidad de uso diario.

           ➔ Evaluar la viabilidad comercial: Finalmente, se sugiere desarrollar un estudio
       de costos y análisis de mercado más profundo para explorar el potencial de
       comercialización del producto en sectores vulnerables, como asilos, centros de salud o
       programas públicos.




9. Referencias bibliográficas


MedMinder. (s.f.). Recuperado el 17 de abril del 2025, de https://medminder.com/


Hero Health. (s.f.). Recuperado el 17 de abril del 2025, de https://herohealth.com/


Medisafe. (s.f.). Recuperado el 17 de abril del 2025, de
https://www.medisafe.com/


Mercado libre Perú. (s.f.) Patilleros - Productos en venta. Recuperado el 17 de
abril de 2025, de https://listado.mercadolibre.com.pe/pastillero
Conte, E., Morales, Y., Niño, C., Zamorano, C., Benavides, M., Donato, M., Llorach,

C., Gómez, B., & Toro, J. (2020). La adherencia a los medicamentos en pacientes

hipertensos y en muestra de la población general. Deleted Journal, 30(4), 313-323.

https://doi.org/10.4321/s1699-714x2020000400011



Montes Cabezón, A. (2020). Diseño y desarrollo de un pastillero inteligente para

personas mayores [Trabajo de Fin de Grado, Universidad de Cantabria]. Repositorio

Institucional de la Universidad de Cantabria.

https://repositorio.unican.es/xmlui/bitstream/handle/10902/3001/MontesCabezonA.pd

f

Calderon-Ramirez, P. M., Huamani-Merma, E., Mirano-Ortiz-De-Orue, M. G.,

Fernandez-Guzman, D., & Toro-Huamanchumo, C. J. (2024). Factors associated with

poor adherence to medication in patients with diabetes and hypertension in Peru:

findings from a pooled analysis of six years of population-based surveys. Public

Health, 231, 108-115. https://doi.org/10.1016/j.puhe.2024.03.012

Silva-Caso, W., Riega-López, P., & Zavaleta, A. (2024). Prevalencia de

incumplimiento terapéutico en pacientes con enfermedades crónicas en centros de

salud del Perú. medRxiv.

https://www.medrxiv.org/content/10.1101/2024.06.12.24308773v1

300 adultos mayores se benefician en campaña integral de salud en San Juan de

Lurigancho. (s. f.). Noticias - Dirección de Redes Integradas de Salud Lima Centro -

Plataforma del Estado Peruano.

https://www.gob.pe/institucion/dirislimacentro/noticias/740481-300-adultos-mayores-

se-benefician-en-campana-integral-de-salud-en-san-juan-de-lurigancho?utm_source
10. Anexos
Video de explosición del pastillero:




       Link del video
