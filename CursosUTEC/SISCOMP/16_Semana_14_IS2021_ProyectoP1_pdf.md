---
curso: SISCOMP
titulo: 16 - Semana 14/IS2021_ProyectoP1
slides: 2
fuente: 16 - Semana 14/IS2021_ProyectoP1.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
November 19, 2025
                                                             Proyecto - P1

  Instrucciones:
    • El proyecto se realizará en grupos.
    • En la entrega final se deberá adjuntar un informe y todos los archivos de simulación y pruebas que sean necesarios para mostrar sus
      resultados.
    • El proyecto tiene un checkpoint, el cual se desarrollará en el Laboratorio 5, este será en la sesión indicada en el Anexo y es en modalidad
      presencial, este checkpoint es obligatorio para la entrega final del proyecto.
    • La calificación del proyecto incluye una exposición de todos los miembros del grupo, esta se realizará durante la semana 15.

                                                                  1. Tema
   En un sistema satelital, los datos tomados por un sensor de temperatura ubicado en la estructura interna
del satélite permiten detectar algún malfuncionamiento a través del calentamiento de los componentes
electrónicos que se encuentran funcionando. Diseñar un sistema que transmita esta medida hacia un
receptor ubicado en el computador a bordo del satélite y que sea capaz de desplegar alguna técnica de
escudo (shield) o enfriamiento (peltier cells) cuando la temperatura sobrepase los 90° C, este sistema debe
desactivarse cuando la temperatura desciende por debajo de los 55° C.
                                                        2. Caracterı́sticas
  Para desarrollar el proyecto debe implementar tres procesos:
   • Proceso 1: Proceso de adquisición de la señal de temperatura, ingresan datos correspondientes a
      la temperatura, que van en un rango entre 45° C hasta 105° C durante una órbita LEO, que dura
      alrededor de 100 minutos (para pruebas, puede acortar este tiempo). Asegúrese de insertar en
      este proceso algunos datos que generen anomalı́as en el valor de la temperatura, para provocar el
      despliegue de las técnicas de enfriamiento y su posterior restauración.
   • Proceso 2: Proceso que despliega la técnica de enfriamiento empleada, cada vez que la lectura del
      proceso 1 exceda el valor del rango estipulado. Este proceso debe mostrar avisos mediante alertas,
      en su activación y desactivación.
   • Proceso 3: Proceso que despliega el valor transmistido del proceso 1, la recepción se realiza con un
      protocolo serial (UART).
                                                        3. Consideraciones
    • Diseñar un priority scheduler para recrear los cuatro escenarios mostrados en las siguientes figuras.
    • Cada proceso debe implementarse en Assembly RISC - V a fin de obtener el valor del PC una vez
      que se detecte un valor lı́mite de temperatura.
                                                               4. Pruebas
  Puede considerar dos tipos diferentes de pruebas:
    • Utilizar diversos tipos de archivos de entrada (valores diferentes de temperatura, valores random, un
      mismo valor, 100 minutos de valores, 200 minutos de valores, etc) y probarlos en todos los escenarios.
      Por ejemplo, si utiliza cuatro archivos de entrada tendrı́a un total de 16 pruebas.
    • Utilizar un solo tipo de archivo de entrada para todos los escenarios, en este caso solo tendrı́a 4
      pruebas.
Su tabla de pruebas deberı́a lucir ası́:




                                                                        1
                                                                                                           2

                                                  Arch1                     Arch2
                 Metric/Test
                                     Esc1      Esc2      Esc3 Esc4 Esc1 Esc2 Esc3 Esc4
              Texe                   0.14      0.08      0.10 0.02 0.2  0.15 0.04 0.6
              Speedup (Esc1)         0.14/0.14 0.14/0.08 ...  ...  ...  ...    ... ...
              Syscalls
              Interrupts
              Mem. Occupation
              CPU Occupation
              Insert other metric

  También puede generar gráficas con los tiempos del P1, P2, P3 y P4, de acuerdo a cada prueba, no es
necesario reportar en la tabla, pero podrı́a añadir las siguientes columnas:

                                               Arch1                                       Arch2
    Metric/Test
                                    Esc1               Esc2   Esc3 Esc4             Esc1          Esc2 Esc3 Esc4
                       P1      P2     P3   Ptot                             P1 P2     P3   Ptot
 Texe                  0.14 0.15 0.06 0.35        0.08        0.10   0.02   0.2 0.18 0.14 0.52    0.15   0.04   0.16
 Speedup (Esc1)                            1      0.35/0.08 ...      ...    ...            1
 Syscalls                                                            X                                          X
 Interrupts
 Mem. Occupation
 CPU Occupation
 Insert other metric


  IS-UTEC
