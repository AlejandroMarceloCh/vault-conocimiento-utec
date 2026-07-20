---
curso: SISCOMP
titulo: 08 - Semana 6/S6_ Laboratorio Display 7 segmentos
slides: 3
fuente: 08 - Semana 6/S6_ Laboratorio Display 7 segmentos.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
September 25th, 2025

                                         S6: 7-Segment Display Control

Instrucciones:
• Leer los enunciados y dar respuestas exactas de acuerdo a lo requerido en cada ejercicio. Mostrar su trabajo y justificación
en todas sus respuestas.
• Desarrollar de forma individual.
• No está permitido usar material escrito o electrónico. No está permitido usar audífonos u otros equipos electrónicos.
• Respuestas no legibles no tienen derecho a revisión.


     1.​ Simulación a alto nivel:

Para controlar el display a 7 segmentos sin ayuda de un codificador, se puede mapear el
encendido/apagado de cada uno de los segmentos de manera independiente. En la figura 1
se puede observar el montaje del circuito utilizando una plataforma Arduino, basada en un
microcontrolador Atmega328P.

1.1.​ Crear       una     cuenta    en                       Tinkercad           y       replicar         el       circuito:
https://www.tinkercad.com/dashboard




           Figura 1. Circuito para controlar un display 7 segmentos con un microcontrolador

1.2​   Señale los pines de entrada y salida utilizados en la implementación de su
controlador:


 Señal                                     Input                                     Output

 VDD

 GND
1.3​   Señale los principales aspectos de la arquitectura del microcontrolador utilizado
(Arduino Mega2560).

1.4​   En el anexo 1 puede encontrar el código a alto nivel, compile el código y optimice
para que pueda detectarse cualquier caracter.

1.5​   Compile el código en Arduino IDE y señale la cantidad de memoria utilizada.

   2.​ Simulación a bajo nivel

2.1​   Compile el código en RISC - V en cpulator o ripes y complete la siguiente tabla:


 Característica/Registro

 Nro. de Instrucciones

 Memory

 CPI
   3.​ Simulación a nivel de descripción de hardware

En el archivo: Arch_Guide_7segment.pdf encontrará la simulación para el control de un
display 7 segmentos usando una arquitectura reconfigurable basada en FPGA.

3.1​   Señale los principales aspectos de la arquitectura FPGA.

3.2​  Compile el código en Vivado, muestre las principales métricas de rendimiento
completando la siguiente tabla.


  Platform      Waveform           RTL Design           Implementation        Power    Timing
                                                                              Report   (WNS)
                                Cells      Nodes       LUT         Buff




3.3​   Muestre la captura de pantalla de las formas de onda.
3.4​   Muestre el esquemático.
3.5​   Utilice los constraints colocados en la guía.
3.6​   Muestre la implementación y ocupación en área.
3.7​   Compile el bitstream y muestre sus resultados en la placa, adjunte imágenes.

   4.​ Conclusiones

Detalle cuáles son las principales diferencias y similitudes en la implementación de un
controlador de un display 7 segmentos en las diferentes arquitecturas computacionales
utilizadas.
