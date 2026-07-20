---
curso: SISCOMP
titulo: 12 - Semana 10/S10_Test Memory
slides: 1
fuente: 12 - Semana 10/S10_Test Memory.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
October 21th, 2025

                                     S10: Test Memory

   1.​ Experimento 1

Compilar y ejecutar el programa en C testMemory.c. Puede realizar las modificaciones
necesarias para que funcione correctamente y mejorar el código. Sin embargo, debe
especificar el porqué y donde se realizó la modificación a modo de comentario.

NOTA: En un terminal de Linux, escriba la instrucción getconf -a | grep CACHE. Reporte los
valores que obtiene para la computadora donde está realizando sus pruebas. De no reportar
este valor, no podrá acceder al puntaje completo de los demás ítems. Puede cambiar el
valor de MAX_SIZE según la capacidad de memoria RAM disponible. En un terminal de
Linux, escriba la instrucción free -m y reporte lo que le sale.

Utilizar TODOS los conceptos vistos en clase sobre memoria.

Para el experimento 1, responder de forma breve y concisa.

a. Para el loop 1, justificar el porqué de la diferencia entre el primer tiempo de ejecución y
los 4 restantes.
b. Para el loop 2, ¿qué puede concluir del comportamiento de la memoria caché a partir de
los tiempos obtenidos? ¿Existe alguna relación entre los tiempos de ejecución y el tamaño
de la memoria caché de datos L1?
c. ¿Cuántos bytes en memoria se están utilizando para almacenar el arreglo? ¿Cuántos
números enteros podría almacenar teóricamente en cada nivel de memoria caché?

Para el experimento 2, responder de forma breve y concisa.

d. El experimento 2 realiza la misma operación que el loop 2 del experimento 1, la diferencia
es que ahora debe acceder solamente a un rango restringido de memoria. Por ejemplo,
para restringir el rango de acceso a memoria a los primeros 16 kiB se realiza la
siguiente operación con los índices: arr[ i & 0xFFF ].

       i. Calcular los tiempos de ejecución para cada valor de la variable k cuando el loop 3
accede a los primeros 16 kiB, 32 kiB, 64 kiB, 256 kiB, 512 kiB, 6 MiB, y 10 MiB de memoria.
Graficar las curvas de tiempo de ejecución en función del valor del log2(k). NOTA: los
tiempos para cara k se almacenan en el archivo tiempos_exp2.txt de forma
automática luego de la ejecución del programa.

Argumentar sobre las posibles razones por las cuales se presentan o no diferencias en las
curvas para cada restricción de acceso. ¿Influye el tamaño de cada nivel de memoria caché
en los tiempos de ejecución encontrados para el loop 3? Justificar su respuesta.
