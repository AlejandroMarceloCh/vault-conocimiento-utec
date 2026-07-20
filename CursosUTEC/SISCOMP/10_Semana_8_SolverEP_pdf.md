---
curso: SISCOMP
titulo: 10 - Semana 8/SolverEP
slides: 3
fuente: 10 - Semana 8/SolverEP.pdf
---

  ladanaque@utec.edu.pe
  IS2021: Computing Systems
  October 10, 2025
                                              Examen Parcial - E1


  Question 1. (3pt) Convierta los siguientes números decimales en formato complemento a dos (6-bit) y
  opere la adición correspondiente. Indicar si existe overflow en la operación si el resultado debe ser a 6 bits.
  Considere que una respuesta incorrecta invalida una correcta.
         • 16 + 9
         • 27 + 31
         • −4 + 19
         • 3 + −32
         • −16 + −9
         • −27 + −31
    Sol:
         • 16+9 = 25 = 011001 (va de 0 a 63)
         • 111010 = 58 = 111010 (va de 0 hasta 63) no hay overflow
         • −4 + 19 = 15 = 001111 (va desde 0 hasta 63)
         • 3 −32 = −29 = 011101 = 100011 (va desde −32 hasta 31)
         • −16+-9 = −25 = 011001 = 100111 (va desde −32 hasta 31)
         • −27−31 = −58 = 111010 = 000110 (va desde −32 hasta 31) por eso hay overflow.

  Question 2. (2pt) En el sistema BCD (Binary Coded Decimal), se utilizan 4 bits para representar un
  dı́gito decimal (de 0 a 9). Por ejemplo: 3710 se escribe como 00110111BCD
         • Escriba 28910 in BCD.
         • Convierta 100101010001BCD a decimal.
         • Convierta 01101001BCD a binario.
         • Explique porqué el sistema BCD serı́a útil para representar números.
  Sol:
      • 0010 = 2, 1000 = 8, 1001 = 9
      • 001010001001
      • 100101010001 = 951BCD 01101001 = 6910 = 010001012
• Porque los sistemas de un dı́gito decimal no necesitan representación de 10, 11, 12, 13, etc, por ejemplo el
  display a 7 segmentos
    Tip: 1010 = 00010000BCD
  Question 3. Considerar un microprocessor de 32−bit que tiene on−chip cache de 16−KByte four-way
  set-associative. Asumir que la cache tiene un tamaño de lı́nea (line size) de cuatro (4) words de 32−bit.
         • (1pt) Definir los campos y su cantidad de bits sobre el address.
         • (2pt) Dibujar la caché mostrando su organización. Detallar tamaños y lógica para que se puedan
           realizar hits y misses. Calcular los números de sets y blocks necesarios.
         • (1pt) Usando su diseño calcular y mostrar en donde se encontrará el word de memoria 0xABCDE8F8.




                                                          1
                                                                                                                  2

Question 4. Una función llamada strcpy es capaz de copiar una cadena desde una cadena de origen (src)
a una cadena de destino (dst), según el siguiente código en alto nivel:

  1 // C code
  2 void strcpy ( char dst [] , char src []) {
  3     int i = 0;
  4     do {
  5     dst [ i ] = src [ i ];
  6     } while ( src [ i ++]) ;
  7 }


       • (2pt) Implemente la función en RISC-V utilizando s0 para i.
       • (2pt) Diseñe el stack antes, durante y después de la ejecución de la función, asuma que sp = 0xFFC00
         antes de que strcpy sea llamada.
Sol:

  1 // Assembly       Code
  2 # a0 = dst
  3 # a1 = src
  4 # s0 = i
  5 strcpy :
  6       addi sp , sp , -4
  7       sw s0 ,0( sp )
  8       addi s0 , zero ,0
  9 bucle :
 10       add t1 , a1 , s0
 11       add t2 , a0 , s0
 12       lb t3 ,0( t1 )
 13       sb t3 ,0( t2 )
 14       beq t3 , zero , fin
 15       addi s0 , s0 ,1
 16       j bucle
 17 fin :
 18       lw sp ,0( sp )
 19       addi sp , sp ,4
 20       jr ra
 21 }

  At the begin: 0xFFC00 = sp Function: 0xFFCFC = sp At the end: 0xFFC00 = sp
  0xFFC00 = sp 0xFFC00 0xFFC00 = sp 0xFFCFC 0xFFCFC = sp 0xFFCFC 0xFFCF8 0xFFCF4
Question 5. (8pt) Se dispone de un fragmento de código que implementa una función cuyo propósito es
determinar y retornar el valor máximo dentro de un arreglo numérico denominado array. Sin embargo, el
código presentado contiene siete errores distribuidos entre la definición de la función, el manejo de variables,
la estructura de control, los tipos de datos y la sintaxis general.

  1 . data
  2 numbers :     . skip 40 (10 enteros = 40 bytes )
  3 . text
  4 Largestnum :
  5     la a5 , numbers         # a5 := & numbers
  6     la a0 , ( a5 )          # a0 ( largest ) := numbers [0]
  7     li a1 , 1               # a1 ( i ) := 1
  8     la t4 , 10
  9     for :
 10           bgt a1 , t4 , end     # if i >= 10 , then exit the loop ( end label )
 11           srli t1 , a1 , 2      # t1 := i * 4
 12           add t2 , a5 , t1      # t2 := & numbers + i *4
                                                                                                            3

13            lw t3 , ( t2 )          # t3 := numbers [ i ]
14            blt t3 , a0 , skip      # if numbers [ i ] < largest , then skip
15            add a0 , t3             # update largest
16      skip :
17            addi a1 , a1 , 2
18      j for
19      end :
20      nop                          # return

   • (7pt) Analice detalladamente el código e identifique los siete errores presentes, justificando por qué
     cada uno impide o altera la ejecución correcta del programa. Para cada error detectado, proporcione
     la instrucción o argumento corregido, explicando brevemente la lógica detrás de la corrección y su
     impacto en la ejecución.
   • (1pt) Verifique que, una vez corregidos los errores, la función produzca el resultado esperado para
     un arreglo de prueba (por ejemplo, [3, 7, 1, 9, 5] → salida esperada: 9). Asigne valores a los registros
     y actualice la salida de la función con el mayor valor.
 Solve

1 . data
2 numbers : . skip 40 (10      enteros = 40 bytes )
3 . text
4 Largestnum :
5      la a5 , numbers         # a5 := & numbers
 6     lw a0 , ( a5 )          # a0 ( largest ) := numbers [0]
 7     li a1 , 1               # a1 ( i ) := 1
 8     li t4 , 10
 9     for :
10     bge a1 , t4 , end       # if i >= 10 , then exit the loop ( end label )
11          slli t1 , a1 , 2      # t1 := i * 4
12          add t2 , a5 , t1      # t2 := & numbers + i *4
13          lw t3 , ( t2 )        # t3 := numbers [ i ]
14          blt t3 , a0 , skip    # if numbers [ i ] < largest , then skip
15          mv a0 , t3            # update largest
16     skip :
17          addi a1 , a1 , 1      # i := i + 1
18        j for
19    end :
20    ret                         # return

 IS-UTEC
