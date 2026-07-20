---
curso: SISCOMP
titulo: 09 - Semana 7/LabCalificado3
slides: 2
fuente: 09 - Semana 7/LabCalificado3.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
October 7, 2025
                                               Laboratorio 3

Question 1. (10 ptos) Se dispone de una arquitectura con direcciones fı́sicas de 32 bits y una jerarquı́a
de memoria con un tamaño de bloque de 64B, formada por tres niveles de caché (L1, L2, L3) y la memoria
principal. El objetivo del ejercicio es rastrear completamente el acceso a una dirección fı́sica considerando
que los tres niveles de caché son 4-way associative y cuentan con un offset de 6 bits. Completar la tabla
en base a los datos ya existentes y muestre a detalle todos sus cálculos. Calcule además la dirección fı́sica
referenciada en el ejercicio.
      Levels        Sets            Offbits   Indbits       Tagbits      OffVal        IndVal        TagVal
      L1                            6                                    0x02          0x84          0x3122A
      L2                            6                                    0x02          0x284
      L3                            6                                    0x02          0xA84
  Si los miss rate de los niveles L1 y L2 son 20%, 50% respectivamente, y sus tiempos son 1, 5 y 10 ciclos.
¿Es posible obtener un AMAT de 3 ciclos? ¿Cuánto deberı́a ser el miss rate en L3? Considere que la
memoria principal tiene un tiempo de 100 ciclos.

Question 2. (10 ptos) Considere el esquema de la figura, para la arquitectura RISC - V la instrucción es
de 32 bits. Recorra el camino de las cuatro instrucciones de la rutina message, comente de qué instrucción
se trata y marque los registros en salida y sus respectivos valores. Considere que todos los valores de los
registros son previos al inicio del programa, cargue los valores finales en las direcciones indicadas.

  1   Message :
  2               add   x1 ,   x1 , x2
  3               mul   x3 ,   x1 , x1
  4               neg   x2 ,   x1
  5               and   x3 ,   x2 , x1


 Lı́nea Instrucción                     PC             WriteMem          DataMem             AddressMem
 5
 6
 7
 8

  IS-UTEC




                                                        1
                                                  2




Figure 1. CPU Implementation of an architecture
