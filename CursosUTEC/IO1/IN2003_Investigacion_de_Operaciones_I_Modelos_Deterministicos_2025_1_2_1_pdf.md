---
curso: IO1
titulo: IN2003_Investigacion de Operaciones I_ Modelos Deterministicos_2025 - 1-2 (1)
slides: 9
fuente: IN2003_Investigacion de Operaciones I_ Modelos Deterministicos_2025 - 1-2 (1).pdf
---

Malla 2021
DEPARTAMENTO
Departamento de Industrial



CURSO
Investigación de
Operaciones I: Modelos
Determinísticos

MALLA
2021



MODALIDAD
PRESENCIAL

CREDITOS
4
                                  REGLAS INTEGRIDAD ACADÉMICA



Todo estudiante matriculado en una asignatura de la Universidad de Ingeniería y Tecnología tiene la
obligación de conocer y cumplir las reglas de integridad académica, cuya lista a continuación es de
carácter enunciativo y no limitativo, ya que el/la docente podrá dar mayores indicaciones:

1.  La copia y el plagio son dos infracciones de magnitud muy grave en la Universidad de Ingeniería y
    Tecnología (UTEC) conforme a lo establecido en el Reglamento de Disciplina de los Estudiantes.
    Tienen una sanción desde 2 semestres de suspensión hasta la expulsión.
2. Si se identifica la copia o plagio en evaluaciones individuales, el/la docente puede proceder a
    anular la evaluación.
3. Si la evaluación es personal o grupal-individual, la interacción entre equipos o compañeros se
    considera copia o plagio, según corresponda. Si la evaluación calificada no indica que es grupal, se
    presume que es individual.
4. La copia, plagio, el engaño y cualquier forma de colaboración no autorizada no serán tolerados y
    serán tratados de acuerdo con las políticas y reglamentos de la UTEC, implicando consecuencias
    académicas y sanciones disciplinarias.
5. Aunque se alienta a los estudiantes a discutir las tareas y trabajar juntos para desarrollar una
    comprensión más profunda de los temas presentados en este curso, no se permite la presentación
    del trabajo o las ideas de otros como propios. No se permite el plagio de archivos informáticos,
    códigos, documentos o dibujos.
6. Si el trabajo de dos o más estudiantes es sospechosamente similar, se puede aplicar una sanción
    académica a todos los estudiantes, sin importar si es el estudiante que proveyó la información o es
    quien recibió la ayuda indebida. En ese sentido, se recomienda no proveer el desarrollo de sus
    evaluaciones a otros compañeros ni por motivos de orientación, dado que ello será considerado
    participación en copia.
7. El uso de teléfonos celulares, aplicaciones que permitan la comunicación o cualquier otro tipo de
    medios de interacción entre estudiantes está prohibido durante las evaluaciones o exámenes,
    salvo que el/la docente indique lo contrario de manera expresa. Es irrelevante la razón del uso del
    dispositivo.
8. En caso exista algún problema de internet durante la evaluación, comunicarse con el/la docente
    utilizando el protocolo establecido. No comunicarse con los compañeros dado que eso generará
    una presunción de copia.
9. Se prohíbe tomar prestadas calculadoras o cualquier tipo de material de otro estudiante durante
    una evaluación, salvo que el/la docente indique lo contrario.
10. Si el/la docente encuentra indicios de obtención indebida de información, lo que también implica
    no cumplir con las reglas de la evaluación, tiene la potestad de anular la prueba, advertir al
    estudiante y citarlo con su Director de Carrera. Si el estudiante no asiste a la citación, podrá ser
    reportado para proceder con el respectivo procedimiento disciplinario. Una segunda advertencia
    será reportada para el inicio del procedimiento disciplinario correspondiente.
11. Se recomienda al estudiante estar atento/a a los datos de su evaluación. La consignación de datos
    que no correspondan a su evaluación será considerado indicio concluyente de copia.
                      UNIVERSIDAD DE INGENIERÍA Y TECNOLOGÍA

                                   SÍLABO DEL CURSO



1. ASIGNATURA

   IN2003 – Investigación de Operaciones I: Modelos Determinísticos

2. DATOS GENERALES

   2.1 Ciclo: NIVEL 4
   2.2 Créditos: 4
   2.3 Condición: Obligatorio para Ingeniería Industrial
   2.4 Idioma de dictado: Español
   2.5 Requisitos: CS1112 - Programación II Y CC1103 - Álgebra Lineal


3. INTRODUCCIÓN AL CURSO

   El curso desarrolla competencias para identificar, modelar y resolver problemas de
   optimización lineal, entera, mixta y combinatoria. Se presentan los conceptos
   importantes de la programación matemática lineal, así como los métodos básicos de
   resolución de esos problemas de optimización. Se presentan finalmente los conceptos
   básicos de los métodos heurísticos que permiten obtener buenas soluciones factibles de
   problemas más complejos frecuentemente encontrados en la realidad industrial. De ser
   posible, los conceptos del curso serán ilustrados con varios modelos clásicos aplicables
   en áreas tales como operaciones, logística, producción, marketing o finanzas




4. OBJETIVOS

      Semana 1:
      Semana 2:
      Semana 3:
      Semana 4:
      Semana 5:
      Semana 6:
      Semana 7:
      Semana 8: Formular y resolverlos problemas de optimización lineal entera y mixta con
       el paquete JuMP en Julia.
      Semana 9:
      Semana 10:
      Semana 11:
   Semana 12:
   Semana 13:
   Semana 14:
   Semana 15:
   Describir el ámbito de la investigación de operaciones
   Definir los conceptos “optimizar” y “solución óptima”
   Dar ejemplos de problemas “fáciles” de optimización
   Dar ejemplos de problemas “difíciles” de optimización
   Dar ejemplos de aplicaciones de problemas de optimización en diferentes sectores de
    actividad
   Instalar Julia en su computadora
   Instalar nuevos paquetes en Julia
   Programar programas simples en Julia con funciones, con sus estructuras de control (if-
    elseif-else, while, for, etc.) y sus tipos básicos (integer, float, boolean, string, struct,
    mutable struct, array, dictionary, etc.)
   Formular un problema lineal simple
   Definir las variables de decisión de un programa lineal simple
   Definir la función objetivo de un programa lineal simple
   Definir las restricciones de un programa lineal simple
   Distinguir un programa lineal y un programa no lineal
   Sustituir una variable libre por dos variables no-negativas
   Formular problemas simples de optimización lineal y resolverlos con el paquete JuMP
    en Julia
   Introducir el concepto de complejidad computacional
   Justificar la utilización de métodos heurísticos
   Definir, explicar y utilizar el concepto de vecindad
   Describir y utilizar el método de métodos de máxima pendiente
   Definir el concepto de óptimo local
   Definir y utilizar el concepto de algoritmo de construcción
   Definir y utilizar el concepto de algoritmo de mejora
   Explicar la diferencia entre estrategias “Best Improvement” y “First Improvement”
   Dar ejemplos de métodos de construcción para los problemas de Bin Packing y Traveling
    Salesman Problem
   Definir el concepto de vecindad conexa
   Identificar la conexidad de una vecindad
   Adaptar el algoritmo de máxima pendiente a la búsqueda local
   Entender la importancia de la aleatoriedad en un algoritmo de búsqueda local
   Dar ejemplos de aleatoriedad en un algoritmo de búsqueda local
   Formular programas lineales enteros y mixtos
   Utilizar variables binarias para formular problemas con condiciones lógicas
   Formular y resolverlos problemas de optimización lineal entera y mixta con el paquete
    JuMP en Julia.
   Dar una expresión matemática de una combinación lineal
   Dar una expresión matemática de combinaciones afín, cónica y convexa
      Dar una definición matemática de un conjunto convexo
      Dar una expresión matemática de un hiperplano y semiespacio
      Explicar el vínculo entre semiespacio convexo y programación lineal
      Definir el concepto de punto extremo
      Explicar el vínculo entre puntos extremos y programación lineal
      Explicar el vínculo entre convexidad y programación lineal
      Explicar de manera intuitiva el método simplex
      Explicar el interés del método simplex comparado a la enumeración exhaustiva de
       puntos extremos
      - Escribir un programa lineal en su forma estándar
      - Utilizar variables de holgura para obtener un sistema de ecuaciones
      Escribir un programa lineal en su forma canónica
      Definir el concepto de base, de variables básicas y no-básicas
      Escribir un diccionario
      Determinar la variable de entrada (en la base)
      Determinar la variable de salida (de la base)
      Determinar el valor máximo de la variable de entrada
      Aplicar el método del pivote a un diccionario
      Aplicar el método del problema auxiliar para encontrar una solución factible no trivial
      Definir el dual de un problema de programación lineal
      Aplicar el método simplex dual
      Identificar las variables de entrada y de salida en el contexto del método simplex dual
      Identificar una solución inicial no trivial con el método simplex dual
      Dar una interpretación económica de las variables duales (precios sombras)
      Dar una interpretación económica de las restricciones duales (costos reducidos)
      Definir un programa lineal entero, mixto, o binario
      Plantear el concepto de relajación lineal de un problema entero, mixto o binario
      Reconocer las relaciones entre espacios factibles de un problema, su relajación lineal,
       límite superior
      Definir el concepto de envolvente convexa de un problema y entender su importancia
       en programación entera, mixta o binaria
      Aplicar el algoritmo de branch-and-bound para resolver problemas enteros, mixtos y
       binaries
      Dar ejemplos de cortes válidos en los problemas de Traveling Salesman Problem y de
       mochila
      Definir y utilizar los concepto de restricción válida, plano de corte y corte válido para un
       punto del espacio relajado
      Explicar de manera intuitiva el algoritmo de planos de corte
      Presentación de proyectos

5. COMPETENCIAS Y CRITERIOS DE DESEMPEÑO

   Competencias Especificas ABET - INGENIERIA
       La capacidad de identificar, formular y resolver problemas complejos de ingeniería
        mediante la aplicación de principios de ingeniería, ciencias y matemáticas.
   Competencias Generales ABET - INGENIERIA

       La capacidad de funcionar de manera efectiva en un equipo cuyos miembros
        conjuntamente brindan liderazgo, crean un entorno colaborativo e inclusivo, establecen
        metas, planifican tareas y cumplen objetivos.
   Competencias TEC

       Aplicar conocimientos científicos y técnicos de diversas disciplinas para resolver
        eficazmente situaciones complejas en su entorno.

6. RESULTADOS DE APRENDIZAJE

   Aplicar algoritmos de programación lineal, entera o mixta para resolver problemas de
    optimización de la vida real.
   Reconocer qué problemas de la vida real pueden ser resueltos de manera exacta con
    modelos de programacion lineal o entera.
   Reconocer qué problemas de la vida real deben ser resueltos de forma aproximada
    utilizando heurísticas de construccion (Greedy, Grasp) y/o de mejoramiento (busqueda
    local).
   Identificar, formular y resolver problemas de optimización combinatoria NP-Difíciles de la
    vida real, mediante un trabajo en equipo, implementando métodos heurísticos de
    búsqueda local en un lenguaje de programación.
   Identificar, formular y resolver problemas de optimización combinatoria NP-Difíciles de la
    vida real, mediante un trabajo en equipo, implementando métodos heurísticos de
    búsqueda local en un lenguaje de programación.

7. TEMAS

  1. Problemas combinatorios y métodos heurísticos.

       1.1. Métodos de construcción, algoritmos greedy
       1.2.Vecindades y métodos de búsqueda local
       1.3.Intensificación y diversificación
       1.4.Evaluación de un método de investigación local: tiempo y calidad de solución
       1.5.Métodos metaheurísticos

  2. Programación lineal:

       2.1. Formulación de modelos de programación lineal
       2.2. Solución de modelos de programación lineal por el método gráfico
       2.3. Solución de modelos de programación lineal por el método simplex
       2.4. Dualidad

  3. Programación entera y binaria
      3.1. Modelos clásicos de programación entera
      3.2. Modelamiento de restricciones lógicas con variables binarias
      3.3. Big-M
      3.4. Algoritmo de branch-and-bound.


8. PLAN DE TRABAJO

   8.1 Metodología
   La metodología utilizada en las sesiones de teoría consiste en una combinación del
   método activo y expositivo.




   8.2 Sesiones de teoría
   Las sesiones teóricas con clases magistrales son focalizadas en el estudiante, a través de
   su participación activa, respondiendo a preguntas, resolviendo problemas relacionados al
   curso y fomentando preguntas. Todo atraso de más de 10 minutos en llegar a clase
   después del horario de inicio oficial de la sesión impide al estudiante realizar su
   evaluación, de ser el caso, y de ingresar al aula antes de que se complete el desarrollo de
   la evaluación.
   A menos que se acuerde explícitamente lo contrario, el uso de computadoras portátiles,
   tabletas y teléfonos celulares está prohibido en el aula. Los teléfonos deben estar
   apagados antes de ingresar en el aula. La violación de esta política puede resultar en una
   solicitud para salir del aula, y una calificación con la nota CERO en la evaluación, de ser el
   caso.




9. SISTEMA DE EVALUACIÓN
   El curso consta de los siguientes espacios de evaluación:


                   Teoría

                   TEORIA 100%
    Evaluación     5 Quizzes (C) (70%)
                   Proyecto (P) (30%)


                   100%
10. REFERENCIAS BIBLIOGRÁFICAS




    •Hillier, F. S., & Lieberman, G. J. (2010).Introduccion a la investigacion de operaciones.
      McGraw-Hill Interamericana.
    •Taha, H.A. (2017) Operations Research: An Introduction. Pearson/Prentice Hall.
    •Vanderbei, R.J. (2020) Linear Programming: Foundations and Extensions. Springer
      International Publishing.
