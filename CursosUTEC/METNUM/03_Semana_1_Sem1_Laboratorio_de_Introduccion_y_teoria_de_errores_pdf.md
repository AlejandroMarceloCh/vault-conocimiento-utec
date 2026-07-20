---
curso: METNUM
titulo: 03 - Semana 1/Sem1_Laboratorio de Introducción y teoría de errores
slides: 24
fuente: 03 - Semana 1/Sem1_Laboratorio de Introducción y teoría de errores.pdf
---

Métodos
Numéricos
Lab. Teoría de errores - S1
Hermes Yesser Pantoja Carhuavilca
(hpantoja@utec.edu.pe)
Jimmy Mendoza Montalvo
(jmendozam@utec.edu.pe)
Rósulo Pérez Cupe
(rperezc@utec.edu.pe)
Julio Cesar Barraza Bernaola
(jbarraza@utec.edu.pe)
Marco Antonio Cuyubamba Espinoza
(mcuyubamba@utec.edu.pe)
Ronaldo Walter Laureano Huayanay
(rlaureano@utec.edu.pe)


                                    Profesores: Utec-Ciencias
                                                        Índice
                                             1 Programación Matlab
                                             2 Teoría de Errores




Universidad de Ingeniería y Tecnología   Métodos Numéricos       March 25, 2026   1 / 23
        Objetivos
             Implementar funciones y scripts en MATLAB para análisis de errores.




Universidad de Ingeniería y Tecnología        Métodos Numéricos             March 25, 2026   2 / 23
1   PROGRAMACIÓN
    EN MATLAB
Antecedentes generales: ¿De qué estamos
hablando?
       ¿Qué es Matlab?
       MATLAB = MATrix LABoratory
              Lenguaje de programación de alto nivel.
              Herramienta de visualización interactiva.
              Herramienta de cálculo interactiva.
       ¿Qué puedo hacer con MATLAB?
              Automatizar flujos de procesamiento de datos complejos.
              Desarrollar algoritmos.
              Analizar datos.
              Crear modelos y aplicaciones.
              Escribir sus propias herramientas de análisis / cálculo de datos.

Matlab es un paquete completo hecho de un lenguaje de programación, entorno y
muchas cajas de herramientas para el procesamiento y gráfica de datos.

Universidad de Ingeniería y Tecnología         Métodos Numéricos                  March 25, 2026   4 / 23
MATLAB Workspace




Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 25, 2026   5 / 23
Archivos de Matlab




Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 25, 2026   6 / 23
Editor de MATLAB - Live editor
Programación en MATLAB




Los Live-scripts tienen extensión .mlx
Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 25, 2026   7 / 23
Chat de IA de MATLAB




https://la.mathworks.com/matlabcentral/playground/new
Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 25, 2026   8 / 23
Comandos Frecuentes




Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 25, 2026   9 / 23
Programación en MATLAB
       Fundamentos: Variables y Tipos de Datos. Operadores (aritméticos,
       relacionales, lógicos). Entrada y Salida (input, disp, fprintf)
       Funciones: Definición y llamada de funciones. Paso de argumentos.
       Funciones anónimas
       Matrices y Vectores: Creación y manipulación de matrices y vectores.
       Indexación y acceso a elementos. Operaciones matriciales.
       Estructuras de Control: Condicionales (if, else, elseif). Bucles (for, while)
       Gráficos: Creación de gráficos 2D. Personalización de gráficos.
       Tópicos especiales: Vectorización. Cálculo simbólico.




Universidad de Ingeniería y Tecnología     Métodos Numéricos             March 25, 2026   10 / 23
2   TEORÍA
    DE ERRORES
Ejemplo
        Ejemplo 2.1

   Implementar una función en Matlab que permita calcular
                                                    n
                                                    X xk
                                             ex =
                                                          k!
                                                    k=0

   con la siguiente cabecera:

                                         function S=expo(x,n)

   Utilice una sumatoria con 20 términos para calcular una aproximación de e−5 .




Universidad de Ingeniería y Tecnología          Métodos Numéricos   March 25, 2026   12 / 23
Ejemplo
        Ejemplo 2.2

   Aproxime e−5 con el método dado por la fórmula
                                                 1               1
                                         e−x =     x
                                                     =          2  3     ,
                                                 e     1 + x + + x + ...
                                                              x
                                                                2      3!

   utilice solo 20 términos.
   Compara esta aproximación y la hallada anteriormente, considere el valor
   exacto igual a 6.737947 × 10−3 . ¿En qué caso hay más error y a qué cree que
   se debe?




Universidad de Ingeniería y Tecnología                  Métodos Numéricos    March 25, 2026   13 / 23
Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 25, 2026   14 / 23
Error Relativo




Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 25, 2026   15 / 23
Ejercicio: Cifras Significativas
        Ejercicio: Cifras Significativas

   Escriba una función en MATLAB que determine el número de cifras significa-
   tivas n de una aproximación a respecto a un valor exacto A, dado el error
   relativo δr = |A−a|
                   |A| .



Ejemplo: Si δr = 0.00032, la función debe devolver n = 4.




Universidad de Ingeniería y Tecnología     Métodos Numéricos    March 25, 2026   16 / 23
Ejemplo 3
        Ejemplo 2.3

   Determine el número de términos necesarios para aproximar cos(x) a 9 cifras
   significativas con el uso de la serie de Maclaurin

                                                   x2 x4 x6 x8
                                    cos(x) = 1 −     +    −    +    − ...
                                                   2   4!   6!   8!
   Calcule la aproximación en donde el valor de x = 0.3π (considere el valor de
   π determinado por Matlab). Escriba un programa en Matlab para determinar el
   resultado.




Universidad de Ingeniería y Tecnología                Métodos Numéricos     March 25, 2026   17 / 23
Ejercicio: Integración Numérica con la Regla del
Trapecio
        Ejercicio

   Implemente una función en MATLAB que aproxime la integral definida de
              2
   f (x) = e−x desde a = 0 hasta b = 1 usando la regla del trapecio con n
   subintervalos. Determine el valor mínimo de n para
                                                   R 1 que el error relativo sea
                −4                                     −x2
   menor que 10 , comparando con el valor exacto 0 e       dx ≈ 0.746824.


                                         Fórmula de la Regla del Trapecio

                                                         n−1
                 Z b                                                            !
                                h                        X                                 b−a
                     f (x) dx ≈              f (a) + 2         f (a + ih) + f (b) ,   h=
                   a            2                                                           n
                                                         i=1


Universidad de Ingeniería y Tecnología                     Métodos Numéricos               March 25, 2026   18 / 23
Ejercicio
Determine el menor número de términos necesarios para que en la aproximación
dada por
                                    ∞
                                    X 1
                               eA =       An ,
                                       n!
                                                 n=0

donde                                                    
                                             0.2  5 −0.1
                                         A= 0   0.2 −0.3  ,
                                            0.02 0    0.5
cada elemento tenga 8 o más cifras significativas. Utilizar el comando de Matlab
expm para hallar la sumatoria como el valor exacto.

Además, halle el elemento de la matriz aproximada con mayor error relativo
porcentual. ¿Piensa que es necesario adaptar la noción de errores al mundo de las
matrices?

Universidad de Ingeniería y Tecnología           Métodos Numéricos   March 25, 2026   19 / 23

Actividad de Bonificación - Salida (AB-S1)
Indicaciones

    Descargue el archivo .mlx desde Canvas
    Una vez terminada la actividad, suba a
    Canvas el archivo .mlx con el siguiente
    nombre:
    Nombre_ApellidoPaterno.mlx
    Responda usando comandos de MATLAB
    cuando corresponda.
    Cuando se indique, guarde los resultados en
    las variables especificadas.
   Justifique brevemente sus respuestas
   cuando corresponda.


Universidad de Ingeniería y Tecnología        Métodos Numéricos   March 25, 2026   20 / 23
Conclusiones
       MATLAB es una herramienta esencial para la computación numérica,
       destacándose por su capacidad para realizar cálculos complejos, análisis de
       datos y visualización de resultados de manera eficiente e intuitiva.
       MATLAB permite realizar cálculos con gran precisión lo que permite comprobar
       cómo el es proceso de aproximación y el cálculo de errores.




Universidad de Ingeniería y Tecnología   Métodos Numéricos          March 25, 2026   21 / 23
Bibliografía
      Steven C. Chapra and Raymond P. Canale
      Métodos numéricos para ingenieros, 7a ed.
      Richard L. Burden and J. Douglas Faires
      Análisis numérico, 7a ed.




Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 25, 2026   22 / 23
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
