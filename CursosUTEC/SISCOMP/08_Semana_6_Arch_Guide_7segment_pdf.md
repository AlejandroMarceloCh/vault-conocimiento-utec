---
curso: SISCOMP
titulo: 08 - Semana 6/Arch_Guide_7segment
slides: 6
fuente: 08 - Semana 6/Arch_Guide_7segment.pdf
---

                               Guía de
                           Laboratorio           2025-1

7 segment HEX display
    CS3051 - Computer Architecture
            cwilliams, jgonzalez@utec.edu.pe
          TAs: lcarranza, mchincha@utec.edu.pe
Displaying values in basys 3

Display de 7 segmentos en la Basys 3
La placa Basys 3 incorpora un display de 7 segmentos de cuatro dígitos. Cada dígito está compuesto por siete seg-
mentos LED más un punto decimal (DP), que permiten representar caracteres numéricos y algunas letras (A–F) en formato
hexadecimal.

El siguiente diagrama muestra la distribución física del display en la placa:




                     Figure 1: Ubicación del display de 7 segmentos en la Basys 3 (Fuente: Digilent)


Los segmentos del display se controlan mediante los siguientes puertos:




                                 Figure 2: Puertos de conexión entre el FPGA y el display

Este display utiliza una configuración de ánodo común, lo que significa que todos los segmentos comparten las líneas de
cátodo, mientras que cada dígito tiene un ánodo independiente. Para encender un segmento, se debe enviar un 0 lógico
Page 3                                                                                                            Page 3


(nivel bajo) por la línea correspondiente, ya que el display opera con lógica negada. Por tanto, un segmento se apaga con
un 1 y se enciende con un 0.

Debido a que los cátodos están compartidos por todos los dígitos, solo se puede activar un dígito a la vez. Activar
múltiples dígitos simultáneamente puede provocar interferencias o encendidos incorrectos en los segmentos. Para resolver
esta limitación, se emplea una técnica llamada multiplexado dinámico, que consiste en encender un dígito a la vez de
forma cíclica y rápida (normalmente por encima de 120 Hz por digito).


Idea de implementación de hex_display
La idea de implementación del controlador del display consiste en dos componentes principales: una FSM (hFSM) con
un divisor de reloj, y un decodificador hexadecimal (HexDecode). El módulo recibe como entrada un valor de 16 bits
llamado data, y genera como salida las señales correspondientes al ánodo y cátodo del display de 7 segmentos.




                             Figure 3: Estructura del módulo hex_display en Verilog.

hFSM
El módulo hFSM se encarga de realizar el multiplexado dinámico del display. Aunque físicamente sólo se muestra un
dígito a la vez, al recorrerlos rápidamente de forma secuencial se logra el efecto visual de que todos los dígitos están
encendidos simultáneamente.
El valor de entrada data, de 16 bits, se interpreta como una secuencia de 4 nibbles (valor de 4 bits). En cada ciclo de
reloj, hFSM selecciona un nibble por cada digito, y lo entrega mediante la señal digit al módulo HexDecode, que
genera el patrón de segmentos correspondiente. Al mismo tiempo, genera la señal anode, que activa el dígito físico del
display donde se debe mostrar el valor seleccionado.




                      𝐷0                        𝐷1                      𝐷2                     𝐷3
                    ABCD                       EFGH                    IJKL                   MNOP


                             Figure 4: Diagrama de estados de hFSM con entrada de datos

La salida en cada estado corresponde a un grupo de 4 bits del valor de entrada data, que en conjunto representa los 16
bits rotulados como ABCDEFGHIJKLMNOP. Asumiendo que el estado D0 corresponde al dígito más significativo, cada
estado extrae secuencialmente uno de los siguientes grupos: ABCD, EFGH, IJKL y MNOP.
Page 4                                                                                                          Page 4


HexDecode
El módulo HexDecode funciona como un decodificador de 4 bits a display de 7 segmentos. Su función es traducir un
valor hexadecimal (0–F) en las señales necesarias para activar los segmentos correspondientes (a--g y dp) de un display
de cátodo común.
El siguiente diagrama permite determinar qué segmentos deben activarse (cátodos en estado bajo) para representar cada
uno de los valores hexadecimales del 0 al F. Cada combinación de segmentos encendidos corresponde a un carácter en el
display de 7 segmentos.




                             Figure 5: Diagrama de cada dígito del display de 7 segmentos.




                                   Figure 6: Dígitos hexadecimales de referencia (0-F)

CLKdivider
Divide la señal de reloj original de 100 MHz a una frecuencia cercana a 480 Hz.
Chapter 1

Anexos

Source template
module HexTo7Segment (input[3:0] digit, output reg[7:0] catode);
    ....
endmodule

module CLKdivider(input clk, input reset, output reg t);
    ...
endmodule

module hFSM(input clk,input reset,input[15:0] data,output reg[3:0]
 ↩→ digit,output reg[3:0] anode);
    ...
endmodule

// Main module
module hex_display(input clk, input reset, input[15:0] data, output
 ↩→ wire[3:0]anode, output wire[7:0]catode);
    wire scl_clk;
    wire[3:0] digit;
    CLKdivider sc(
        .clk(clk),
        .reset(reset),
        .t(scl_clk)
    );

    hFSM m(
        .clk(scl_clk),
        .reset(reset),
        .data(data),
        .digit(digit),
        .anode(anode)
    );

    HexTo7Segment decoder (
        .digit(digit),
        .catode(catode)
    );
endmodule
Page 6                                                                     Page 6



XDC template
## Clock signal
set_property PACKAGE_PIN W5 [get_ports clk]
set_property IOSTANDARD LVCMOS33 [get_ports clk]
create_clock -add -name sys_clk_pin -period 10.00 -waveform {0 5} [get_ports clk]


## VOLTAGE SETUP
set_property CONFIG_VOLTAGE 3.3 [current_design]
set_property CFGBVS VCCO [current_design]


## You can change the button if used
## Reset button (btnC)
set_property PACKAGE_PIN U18 [get_ports reset]
set_property IOSTANDARD LVCMOS33 [get_ports reset]

## Catodes
set_property PACKAGE_PIN W7 [get_ports {catode[7]}] ;# A
set_property PACKAGE_PIN W6 [get_ports {catode[6]}] ;# B
set_property PACKAGE_PIN U8 [get_ports {catode[5]}] ;# C
set_property PACKAGE_PIN V8 [get_ports {catode[4]}] ;# D
set_property PACKAGE_PIN U5 [get_ports {catode[3]}] ;# E
set_property PACKAGE_PIN V5 [get_ports {catode[2]}] ;# F
set_property PACKAGE_PIN U7 [get_ports {catode[1]}] ;# G
set_property PACKAGE_PIN V7 [get_ports {catode[0]}] ;# P
set_property IOSTANDARD LVCMOS33 [get_ports {catode[*]}]
set_property DRIVE 4 [get_ports {catode[*]}]
set_property SLEW SLOW [get_ports {catode[*]}]

## Anodes
set_property PACKAGE_PIN U2 [get_ports {anode[0]}]
set_property PACKAGE_PIN U4 [get_ports {anode[1]}]
set_property PACKAGE_PIN V4 [get_ports {anode[2]}]
set_property PACKAGE_PIN W4 [get_ports {anode[3]}]
set_property IOSTANDARD LVCMOS33 [get_ports {anode[*]}]
set_property DRIVE 4 [get_ports {anode[*]}]
set_property SLEW SLOW [get_ports {anode[*]}]


Ejemplo de funcionamiento
Video: Demostración de dsplay con un contador de 16 bits
