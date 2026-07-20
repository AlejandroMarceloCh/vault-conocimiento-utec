---
curso: IO2
titulo: Bienvenida IO2-2026-1__pptx
slides: 20
fuente: Bienvenida IO2-2026-1__pptx.pdf
---

BIENVENIDOS
Investigación de Operaciones II:
Modelos Probabilísticos
Ciclo 2026-1

Prof. Claudia Antonini
Investigación de operaciones II: Modelos probabilísticos             Ingeniería Industrial




             Índice



             •    Visión general
             •    Evaluación
             •    Recomendaciones y reglas de integridad académica
             •    R y RStudio
Investigación de operaciones II: Modelos Probabilísticos                    Ingeniería Industrial




                                1                          VISIÓN GENERAL
Investigación de operaciones II: Modelos Probabilísticos                                 Ingeniería Industrial




  Visión general

Éste es un curso obligatorio de la carrera de Ingeniería Industrial de
UTEC y forma parte del área de analítica de decisiones.

Aquí aprenderán un conjunto de herramientas del modelado
probabilístico y la teoría de colas, input indispensable para el
correcto diseño de simulaciones computarizadas. Las mismas son
herramientas modernas útiles para enriquecer el proceso de toma
de decisiones complejas y en proyectos de gran envergadura.

Es muy posible que necesiten ayuda, por favor, no duden en
pedirla.




                                                                         ¡Bienvenidos!
Investigación de operaciones II: Modelos probabilísticos                                                                  Ingeniería Industrial


    Diferencias con otros cursos
    Cambio de formato:
    Las presentaciones tipo PPT no son la norma en este curso, son la excepción. Se espera que lleven apuntes en
    algún tipo de formato, nuestra recomendación es que trabajen en el formato Quarto Document; un formato que
    podrán acceder desde Rstudio. Es conveniente que desde el comienzo trabajen con un proyecto creado en R para
    colocar los archivos asociados a cada clase. Las clases estarán todas en formato Quarto Presentation.

    Abundancia de material:
    En este curso hay abundante material para estudiar. Los mismos serán publicados a medida que los vayan
    necesitando para evitar que se sientan abrumados por la cantidad a la que tendrán acceso. Por esta misma razón,
    es indispensable llevar la materia al día.

    Investigación requerida:
    Tendrán que investigar algunos temas por su cuenta. Esto es particularmente cierto en el desarrollo del proyecto de
    campo ya que el mismo está diseñado en un formato de aprendizaje basado en proyectos. Se les va a
    proporcionar de materiales de lectura que normalmente son suficientes para acabar con éxito el proyecto pero si se
    espera que ustedes lean y aprendan el material proporcionado.

    Conocimiento previo:
    El curso no es particularmente difícil, pero requiere de conocimientos previos de cálculo diferencial e integral
    en variables variables, probabilidades y ecuaciones diferenciales.
    Investigación de operaciones II: Modelos Probabilísticos                                                                                                         Ingeniería Industrial




        Una semana típica: técnicas sugeridas de estudio
                                                                                                                                        Soluciones de Ejercicios de
                                                                                                                                                   refuerzo
        Fin de la semana anterior                                                                                                       El estudiante:
     Comienzo de la semana siguiente                                       Clase No. 2
                                                                                                                                        • Compara sus soluciones con las
• Se publican en Canvas las soluciones de                                                                                                  publicadas.
  los ejercicios de refuerzo de la semana                        Se sugiere que el estudiante se                                        • Presta atención no sólo a si el
  anterior identificados con la letra S de                       presente a clase habiendo estudiado                                       resultado es correcto sino también
  soluciones                                                     el material de la clase del jueves y                                      al procedimiento y el cómo está
• Se envía por correo y a través de                                                                                                        escrita la solución
                                                                 habiendo actualizado el resumen de la
  un anuncio en Canvas la planificación                                                                                                 • Corrige sus soluciones y
                                                                 teoría
  de semana siguiente.                                                                                                                     actualiza su resumen de teoría

                                                                                                              De jueves a
                                               Jueves
                                                                                                               viernes


                                                                                                                                                 Al final de la
                                                                              Viernes
                                                                                                                                                   semana
                                             Clase No. 1
                                                                                                          Ejercicios de refuerzo
                                Se recomienda que el alumno:
                                                                                                El estudiante:
                                • Asista con puntualidad.
                                                                                                • Resuelva individualmente los ejercicios de refuerzo
                                • Haya resuelto los ejercicios de refuerzo de la
                                                                                                   identificados con la letra T de tareas
                                  semana anterior así como corroborado que sus                  • Interactúa con su grupo de estudio para resolver
                                  soluciones eran correctas y estaban bien                         las
                                  escritas.                                                        dudas de los ejercicios de refuerzo que no haya
                                • Lleve un resumen de la teoría acumulada hasta
                                                                                                   podido resolver sólo.
                                  el                                                            • Aclara las dudas en las sesiones de asesoría
                                  momento y la tenga clara.                                        disponibles en el curso
Investigación de operaciones II: Modelos Probabilísticos                Ingeniería Industrial




                                2                          EVALUACIÓN
Investigación de operaciones II: Modelos Probabilísticos                                           Ingeniería Industrial


  Evaluación del curso

                               • Examen de                                       • Examen de
            EP                   desarrollo                         EF             desarrollo
                                 presencial.                                       presencial
         20%                   • Se toma y
                                                                    30%          • Se toma y
                                 califica en                        10/07          califica en
        15/05                    Gradescope.                                       Gradescope.



                                                                            • Proyecto
                                                   • Exámenes               • P1 (5%) para
                                   EC                cortos,
                                                     presenciales
                                                                     P        recibir feedback
                                                                            • P2 (15%)
                                   30%               y escritos.
                                                                    20%       Sustentación final
                                                                            • 5 integrantes
      Investigación de operaciones II: Modelos Probabilísticos                                                                                       Ingeniería Industrial




        Fechas importantes

Inicio del curso                           Evaluación continua 2:                          Examen parcial:                      Evaluación continua 5:
  Motivación y                               Propiedades de la                         Incluirá los temas de las                 Cadenas de Markov a
reglas del juego                                exponencial                                  tres primeras                         tiempo continuo
                                                                                        evaluaciones continuas

                     Semana 03                                           Semana 07                                 Semana 11                             Semana 15 y 16


 Semana 01                                        Semana 05                                  Semana 08                                Semana 14


              Evaluación continua 1:                                Evaluación continua 3:                   Evaluación continua 4:                 Sustentaciones del
              Esperanza condicional,                                 Procesos de Poisson                      Cadenas de Markov a                   proyecto (Sem. 15)
              varianza condicional y                                                                            tiempo discreto
                 propiedad torre                                                                                                                  Examen final (Sem. 16):
                                                                                                                                                  Incluirá los temas de las
                                                                                                                                                         dos últimas
                                                                                                                                                   evaluaciones continuas


Adicionalmente, en semana 10 se tendrá la entrega parcial del proyecto (P1).
Investigación de operaciones II: Modelos Probabilísticos                                                                      Ingeniería Industrial




     Exámenes
     Tendremos dos exámenes de desarrollo. Normalmente se tratará de un caso real de alguna rama de ingeniería industrial
     y sobre dicho caso se formularán las preguntas a desarrollar.


     Advertencia:
     Las principales razones por la que los alumnos pierden puntos en los exámenes son:

       ●    Por interpretar incorrectamente el enunciado de la pregunta.
       ●    Por no saber filtrar la información relevante del caso para alimentar los modelos probabilísticos estudiados.
       ●    Por no definir correctamente los modelos probabilísticos a utilizar.
       ●    Por no enunciar los parámetros y sus unidades de los modelos probabilísticos a utilizar.
       ●    Por no validar las suposiciones del modelo probabilístico a utilizar en términos del enunciado del caso.
       ●    Por no saber escoger correctamente el modelo probabilístico a utilizar.


            Normalmente, cuando el estudiante hace bien estos pasos, todo lo demás lo hace bien. Inclusive la
            interpretación del resultado numérico dentro del caso de estudio. Considere esta lista de errores frecuentes un
            check list a la hora de resolver los problemas de refuerzo.
    Investigación de operaciones II: Modelos Probabilísticos                                                              Ingeniería Industrial




        Evaluación continua
         Tendremos cinco exámenes cortos para desarrollar sobre un contexto pequeño relacionado a temas variados.




                           EC1                     EC2         EC3                              EC4                 EC5




                                      Primera nota de la                                      Segunda nota de la
                                  evaluación continua (20%)                                evaluación continua (10%)

•    Las evaluaciones continuas se realizarán de forma presencial y por escrito. Al finalizar cada evaluación,
     deberán entregar la hoja de desarrollo para su revisión. La calificación será publicada por el profesor en el
     curso de Gradescope.
•    Cada examen tendrá una duración máxima de 20 minutos y constará de cuatro preguntas de desarrollo.
•    Recomendación: completen todos los ejercicios de la tarea y asistan a las asesorías.
Investigación de operaciones: Modelos Probabilísticos                                                                            Ingeniería Industrial




    Proyecto
     El proyecto de este curso tiene dos entregas, las primera tendrá un peso de 5% y su entrega es obligatoria para recibir
     feedback para continuar con buen pie. Se proporcionarán materiales y rúbricas para los avances de esta forma los
     grupos podrán guiarse si están haciendo lo correcto. El feedback de los proyectos las dará el asistente de cátedra. Es un
     trabajo grupal que presenta algunos retos novedosos para la mayoría de los estudiantes de pregrado, por tratarse de un
     vistazo al mundo de las simulaciones computarizadas.

     En el proyecto, deberán enfrentarse a un problema no estructurado, abierto y contextualizado

     Se tomarán en cuenta diversos aspectos como son:
      ● Interés: el problema identificado debería ser de interés para la audiencia, esto normalmente no es un problema.
      ● Originalidad: el problema no debe estar previamente resuelto, esto es un desafío si se trabaja con datos
           existentes.
      ● Plausibilidad: que tan sensato es pensar que se podrá atacar exitosamente el problema.
      ● Factibilidad: que tan posible es que logren responder las preguntas, este usualmente es bastante
           problemático.
      ● Especificidad: que tan específico es el problema o la pregunta que quieren responder, más específico es mejor.




    Advertencias:
    El proyecto será un sólo para todos los grupos. Sin embargo, cada equipo hará su propio proyecto.
Investigación de operaciones: Modelos probabilísticos                       Ingeniería Industrial




                               3                        RECOMENDACIONES Y
                                                        REGLAS
Investigación de operaciones II: Modelos Probabilísticos                                                            Ingeniería Industrial




    Recomendaciones
● Mantengan el curso al día, asistiendo a clase puntualmente y siguiendo las recomendaciones de los
     docentes. Vengan preparados a clase, para que podamos aclarar sus dudas.
● Resuelvan los ejercicios de refuerzo y comparen sus soluciones con las publicadas.
● Aprovechen las asesorías que se van a dictar, aunque la asistencia no sea obligatoria.
● Hagan un esfuerzo por conocer a sus compañeros, los van a necesitar durante el curso.
● Ayúdense entre ustedes, no todos tienen las mismas dificultades y no todos tienen las mismas destrezas.
●    Sean honestos, recuerden que deben mantener una conducta íntegra en todo momento. En este curso tenemos la política

     de cero tolerancia al plagio y a la copia.

●    Si están en riesgo académico o deben mantener una beca, deben ser mucho más cuidadosos y diligentes con todo.
Investigación de operaciones: Modelos probabilísticos                                                                                   Ingeniería Industrial




           Reglas de integridad académica
      ●     Todo estudiante matriculado en una asignatura de la Universidad de Ingeniería y Tecnología tiene la obligación de conocer y
            cumplir las reglas de integridad académica, cuya lista a continuación es de carácter enunciativo y no limitativo, ya que el/la
            docente podrá dar mayores indicaciones:
            La copia y el plagio son dos infracciones de magnitud muy grave en la Universidad de Ingeniería y Tecnología
            (UTEC) conforme a lo establecido en el Reglamento de Disciplina de los Estudiantes. Tienen una sanción desde 2
            semestres de suspensión hasta la expulsión.

      ●     Si se identifica la copia o plagio en evaluaciones individuales, el/la docente puede proceder a
            anular la evaluación.

      ●    Si la evaluación es personal o grupal-individual, la interacción entre equipos o compañeros se considera copia o
           plagio, según corresponda. Si la evaluación calificada no indica que es grupal, se presume que es individual.

      ●     La copia, plagio, el engaño y cualquier forma de colaboración no autorizada no serán tolerados y serán
            tratados de acuerdo con las políticas y reglamentos de la UTEC, implicando consecuencias académicas y
            sanciones disciplinarias.

      ●     Aunque se alienta a los estudiantes a discutir las tareas y trabajar juntos para desarrollar una comprensión más
            profunda de los temas presentados en este curso, no se permite la presentación del trabajo o las ideas de otros
            como propios. No se permite el plagio de archivos informáticos, códigos, documentos o dibujos.
Investigación de operaciones: Modelos probabilísticos                                                                                Ingeniería Industrial




    ●    Si el trabajo de dos o más estudiantes es sospechosamente similar, se puede aplicar una sanción académica a todos
         los estudiantes, sin importar si es el estudiante que proveyó la información o es quien recibió la ayuda indebida. En
         ese sentido, se recomienda no proveer el desarrollo de sus evaluaciones a otros compañeros ni por motivos de
         orientación, dado que ello será considerado participación en copia.


    ●    El uso de teléfonos celulares, aplicaciones que permitan la comunicación o cualquier otro tipo de medios de interacción
         entre estudiantes está prohibido durante las evaluaciones o exámenes, salvo que el/la docente indique lo contrario de
         manera expresa. Es irrelevante la razón del uso del dispositivo.

    ●    En caso exista algún problema de internet durante la evaluación, comunicarse con el/la docente utilizando el
         protocolo establecido. No comunicarse con los compañeros dado que eso generará una presunción de copia.

    ●    Se prohíbe tomar prestadas calculadoras o cualquier tipo de material de otro estudiante durante una evaluación,
         salvo que el/la docente indique lo contrario.

    ●    Si el/la docente encuentra indicios de obtención indebida de información, lo que también implica no cumplir con las
         reglas de la evaluación, tiene la potestad de anular la prueba,
         advertir al estudiante y agendar una cita con su Director de Carrera. Si el estudiante no asiste a la citación, podrá ser
         reportado para proceder con el respectivo procedimiento disciplinario. Una segunda advertencia será reportada para el
         inicio del procedimiento disciplinario correspondiente.

    ●    Se recomienda al estudiante estar atento/a a los datos de su evaluación. La consignación de datos que no
         correspondan a su evaluación será considerado indicio concluyente de copia.
Investigación de operaciones: Modelos Probabilísticos                 Ingeniería Industrial




                               4                        R y RStudio
Investigación de operaciones: Modelos probabilísticos                                                                             Ingeniería Industrial




    R y RStudio
     El curso no es un curso de programación, pero ciertamente los estudiantes con experiencia en programación tendrán una
     ligera ventaja.

     R ofrece un conjunto de herramientas poderosas para hacer el análisis estadístico completo de un conjunto de datos, el
     ambiente de trabajo que ofrece R es muy limitado y francamente hostil, es básicamente una línea de comando y ya.
     RStudio es una fachada para R. En RStudio trabajaremos mayormente el formato R Notebook y el formato Quarto. Ambos
     formatos son formatos textuales basados en Markdown, que sirve para dar formato muy sencillo a texto. Si usted usa
     asteriscos para poner palabras en negrillas en WhatsApp, ya está utilizando una versión limitada de Markdown.

     Lo interesante de los formatos R Notebook y Quarto, para cuaderno de trabajo y presentación respectivamente, es que
     permiten crear documentos sofisticados y profesionales con código vivo y todo el poder de las librerías disponibles en R.
     Un documento en estos formatos es un ejemplo de lo que se conoce como programación letrada.

     La gracia es entremezclar la narrativa de cómo se resuelve el problema, con el código que la resuelve. El texto explica lo
     que los fragmentos de código hacen. El acto de generar el documento final, con el análisis estadístico completo, por
     ejemplo se denomina tejer. y permite tener, entre otras cosas, resultados reproducibles.

     En este momento, R es junto con Python, estándar de industria para análisis estadístico, RStudio ofrece una plataforma
     estable y gratuita para trabajar en R (o Python) con formatos donde se enfatiza la repetibilidad y la correctitud del
     análisis.
Investigación de operaciones II: Modelos Probabilísticos                                                   Ingeniería Industrial




    Instalación de R y RStudio
    La instalación de R y RStudio es una tarea técnica, relativamente sencilla que todos los estudiantes
    del curso deben completar. Tanto R como RStudio están siendo continuamente mejorados, por lo que
    recomendamos instalar las versiones que mencionaremos a continuación.


     1.    Instalar R
           Instalar la última versión y mantenerla actualizada
            Disponible en https://www.r-project.org

     2.    Instalar RStudio
           Instalar la última versión y mantenerla actualizada
           Disponible en https://rstudio.com

     3.    Configurar todo
           Descargar las librerías necesarias para poder usar los formatos RNotebook y Quarto, descargar
           los diccionarios en español, establecer un directorio de trabajo y finalmente abrir un proyecto para
           trabajar de manera organizada.

                                                                               ¡ B U E NA S U E RT E !
Investigación de operaciones II: Modelaje Probabilístico                            Ingeniería Industrial




    Docente:
                                                               Prof. Claudia Antonini
                                                               cantonini@utec.edu.pe




 Asistente
 de cátedra:                                               Fabián Vallebuona Zender
                                                           fabian.vallebuona@utec.edu.pe




                                                               ¡Éxitos!

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
