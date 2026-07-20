---
curso: SISCOMP
titulo: 07 - Semana 5/Labs_IS2021_2025___2-4
slides: 1
fuente: 07 - Semana 5/Labs_IS2021_2025___2-4.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
September 18, 2025
                                            S5: Array Exercises

Question 1. Escribir un código en RISC - V capaz de contar el número de unos en una cadena de 32 bits.

Question 2. Escribir un código en RISC - V capaz de detectar, dado un string, si la palabra es un
palı́ndromo.
Question 3. Considere el siguiente código en alto nivel

  1 int f ( int n , int k ) {
  2     int b ;
  3     b = k + 2;
  4     if ( n == 0)
  5           b = 10;
  6     else
  7           b = b + ( n * n ) + f (n -1 , k +1) ;
  8     return b * k ;
  9 }


      • Traducir el código a RISC - V
      • Comentar el código
      • Asuma que el código inicia en la dirección 0x8100, almacene la variable local b en s4.
      • Diseñe el mapa de memoria para cuando f(2,4), asuma que sp = 0xBFF00100, s4 = 0xABCD y ra
        = 0x8100 cuando se llama a f.
  IS-UTEC




                                                      1
