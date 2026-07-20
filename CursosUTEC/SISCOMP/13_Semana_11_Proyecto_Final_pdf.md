---
curso: SISCOMP
titulo: 13 - Semana 11/Proyecto Final
slides: 1
fuente: 13 - Semana 11/Proyecto Final.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
October 28, 2025
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
                                                             4. Escenarios

  IS-UTEC




                                                                        1
