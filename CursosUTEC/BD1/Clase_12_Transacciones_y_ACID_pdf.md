---
curso: BD1
titulo: Clase 12 Transacciones y ACID
slides: 80
fuente: Clase 12 Transacciones y ACID.pdf
---

    TRANSACCIONES Y ACID


        CS2041- Base de Datos I
                                   Ciclo 2024 - 1




            Teófilo Chambilla - tchambilla@utec.edu.pe
               Brenner Ojeda - bojeda@utec.edu.pe

En colaboración Aidan Hogan de la Universidad de Chile (https://aidanhogan.com/)
CS2701 Bases de Datos I                               Teófilo Chambilla Aquino



      Índice



       •     Transacciones
       •     Garantías de ACID
       •     Implementación ACID (LOGGING)
       •     Implementación ACID (Secuenciabilidad)
       •     Bloqueos
CS2041
BASES DE DATOS I
CICLO 2023-2




                                                                                             Transacciones y ACID
Introducción



                      Algebra Relacional &       SQL                       Planificación y                NO
Modelo Relacional
                       Cálculo Relacional                                                             SQL/GRAFOS

 Entidad - Relación                          Actualización, Dependencias   Optimización de
                                             Restricciones funcionales     Consultas
Motivación

     “El concepto de transacción es el equivalente
  computacional de un contrato legal. Imagínese una
  sociedad sin ley de contratos. Eso es lo que sería un
   sistema computacional sin transacciones. Si nada
  nunca sale mal, los contratos son sólo un overhead.
  Pero si algo no funciona bien, el contrato especifica
          cómo limpiar la situación.” (J. Gray -
                       A. Reuter)
Una cuenta bancaria …
Una cuenta bancaria … integridad
Restricciones sobre varias tablas (!!)
TRANSACCIONES
Transacciones

 Una transacción es una unidad lógica de procesamiento en una
BASE DE DATOS conformada por una secuencia de operaciones de
   acceso a los datos (lectura, inserción, eliminación, modificación,
                             recuperación).
Operaciones

        R (X)             W (X)

      Lectura del     Escritura del
      elemento X       elemento X




          C                A

     Confirmación/
                     Aborto/Rollback
      compromiso
Ejemplo 1
Dos transacciones, T1 y T2 escriben o leen los elementos X, Y de la base de
datos. La figura indica el orden de entrelazamiento de ellas.




        R2(X); W2(X); R1(Y ); W1(Y ); R1(X); W2(Y ); A2; C1;
 Ejemplo 1

          R2(X); W2(X); R1(Y ); W1(Y ); R1(X); W2(Y ); A2; C1;

Estas operaciones consta de varias suboperaciones (en la operación de escribir
están involucradas al menos las acciones:
- Encontrar la dirección del bloque que contiene X;
- Copiar el bloque a disco en un buffer en memoria principal;
- Copiar X con el nuevo valor en el buffer;
- Almacenar el bloque actualizado desde buffer a disco.
                                                                    Teófilo Chambilla A.




Varios tipos de conflictos cuando hay muchos
usuarios operando concurrentemente
(especialmente cuando se escribe)


 ●   Actualización perdida (conflicto WW)
 -   Una transacción sobre escribe los datos que otra tx ya había
     escrito.

 ●   Lectura sucia (conflicto WR)
 -   Una tx. lee lo que otra tx escribió pero no se había
     confirmado aún.

 ●   Lectura no repetible (conflicto RW):
 -   Una tx. sobreescribe un dato que otra ya había leído antes
     pero no había confirmado.
                                                                                 Teófilo Chambilla A.




Ejemplo de actualización perdida (WW)

➢     “Una transacción sobreescribe los datos que otra tx ya había
      escrito”:




                        Está libre el
                       asiento 24? Si     Reserve el 24



                          R (X)              W (X)
T1

T2

        R (X)                                                   W (X)


      Está libre el                                        Reserve el 24 (pero
     asiento 24? Si                                        estaba ocupado!!!)
                                                                               Teófilo Chambilla A.




Ejemplo de lectura sucia (WR)

➢    “Una TX. lee lo que otra TX escribió pero no se había confirmado
     aún.”



                        ¿Cuántos            Reserve
                      asientos hay?       entonces en
                       No hay más        primera clase


                         R (X)              W (X)
T1

T2

       W (X)                                                      A


     Reserve el 24
                                                         ..pero sí habían!!!
                                                                                   Teófilo Chambilla A.




Ejemplo de lectura no repetible (RW)

➢   “Una TX sobreescribe un dato que otra ya había leído antes pero no había confirmado.”




                                   Reserve el
                                      24


                                     W (X)

        T1

        T2

                R (X)                                   R (X)


         ¿Cuántos asientos
               hay?                                ...ahora si. ¿Cuales
              A ver...                                  asientos?
Vacaciones …
Transacciones: START TRANSACTION/COMMIT




             START TRANSACTION (o a veces BEGIN) inicia la transacción
                        COMMIT realiza/guarda los cambios
Transacciones (por defecto)




                Si no hay una transacción explícita, por defecto, Postgres
                       hace un COMMIT después de cada sentencia
                        (pero se puede cambiar la configuración)
Transacciones: ROLLBACK




                    ROLLBACK deshace/borra los cambios desde el
                              inicio de la transacción

Transacciones: SAVEPOINT




                    ROLLBACK puede deshacer/borrar los cambios
                      desde un punto específico con SAVEPOINT
   Una transacción con valores dinámicos




¿Valor final de saldo_usd en Cuenta?
   Una transacción con valores dinámicos




¿Valor final de saldo_usd en Cuenta?   −268,28 (Se lee el valor actual de la misma transacción)
Una transacción con CHECK




                            ¿Funciona?
                              ¡No!
Atomicidad, Consistencia, Aislamiento, Durabilidad
(Atomicity, Consistency, Isolation, Durability)

LAS GARANTÍAS DE ACID

                                             Capítulo 8.1 | Ramakrishnan / Gehrke
No hay un solo usuario …




   … hay que tener cuidado con la concurrencia
Una cuenta con varios usuarios




             ¿Cuál será el resultado final? …
Caos
Esta vez con transacciones …




 ¿Cuál será el resultado final?   Se rechazará una transacción.
Garantías de ACID
• Atomicidad:
  – La ejecución de cada transacción es atómica:
      • Se realizan todas las acciones o no se realiza ninguna
• Consistencia:
  – Cada transacción debe preservar la integridad
      • La base de datos satisfacen todas las restricciones después
        de una transacción
• Aislamiento (Isolation):
  – Una transacción no puede afectar otra
• Durabilidad:
  – Una vez que haya un COMMIT, la base de datos debe
    persistir los cambios
ACID: Un ejemplo más limpio




Usaremos restricciones con CHECK porque dan ejemplos más claros pero es
  importante tener en cuenta que Postgres no soporta CHECKs diferibles.
ACID: Atomicidad




                                Atomicidad
No se puede actualizar el saldo sin actualizar el gasto directamente después.
                  (Si alguna actualización falla, ambas fallan.)
ACID: Consistencia




                                Consistencia
 Si el resultado de la transacción no satisface todas las restricciones, fallará.
ACID: Aislamiento (Isolation)




                                   Aislamiento
          Una transacción no puede interferir con otra transacción.
En (4), hay que tener cuidado con el ROLLBACK: no se puede restaurar el valor de saldo
              antes del paso (1) porque el valor ya fue cambiado por (2).
ACID: Durabilidad




                                   Durabilidad
        Una vez que haya un COMMIT exitoso, se persisten los cambios.
 (Normalmente la persistencia aquí significa en el disco duro. Sin persistencia, en el
  caso de que la máquina falla y toda la evidencia de los cambios está en memoria
    principal, el sistema de base de datos olvidará los cambios silenciosamente.)
Entonces con las garantías de ACID …




                    … todo está tranquilo.
… pero si uno tiene que implementar ACID




                        … es más difícil ...
¿Cuándo no tenemos ACID?
• Atomicidad:
  × Una transacción se ejecutan solamente a medias pero
    afecta el estado de la base de datos
• Consistencia:
  × Al ejecutar la transacción, la base de datos no
    satisface las restricciones de integridad
• Aislamiento (Isolation):
  × El resultado final de dos transacciones no es
    equivalente a correr cada transacción en serie
• Durabilidad:
  × La base de datos se actualiza momentáneamente y
    luego vuelve al estado anterior.
Modelando una transacción
IMPLEMENTANDO ACID:
REGISTROS (LOGGING)

Mantener un registro de la transacción
Si hay un problema, revertir el registro
Registros ayudan con …
• Atomicidad:
  × Una transacción se ejecutan sólo a medias pero afecta
    el estado de la base de datos
• Consistencia:
  × Al ejecutar la transacción, la base de datos no
    satisface las restricciones de integridad
• Aislamiento (Isolation):
  × El resultado final de dos transacciones no es
    equivalente a correr cada transacción en serie
• Durabilidad:
  × La base de datos se actualiza momentáneamente y
    luego vuelve al estado anterior.

     ¿Cuáles problemas podemos evitar con alguna forma de registro? …
IMPLEMENTANDO ACID:
SECUENCIABILIDAD (SERIALIZABILITY)
                    Capítulo 8.3 (es)/16.3 (en) | Ramakrishnan / Gehrke
Registros no ayudan con …
• Atomicidad:
  × Una transacción se ejecutan sólo a medias pero afecta
    el estado de la base de datos
• Consistencia:
  × Al ejecutar la transacción, la base de datos no
    satisface las restricciones de integridad
• Aislamiento (Isolation):
  × El resultado final de dos transacciones no es
    equivalente a correr cada transacción en serie
• Durabilidad:
  × La base de datos se actualiza momentáneamente y
    luego vuelve al estado anterior.


  … entonces que podemos hacer con respecto a aislamiento/concurrencia? …
La solución más simple: ejecución serial



                                       ¿Cuánto es A + B después?
                                   E       270 + 330 = 600
                                   J
                                   E
                                   C
                                   U
     ¿Hay un problema aquí?        C
                                   I
    ¡Ejecución serial es lenta!    Ó
                                   N
   ¿Se pueden ejecutar partes de
       T1 y T2 en paralelo? …
¿Ejecución paralela?




                                 E
                                 J
                                 E
                                 C
                                 U
                                 C
                                 I
    ¿Cuánto es A + B después?    Ó
            ¯\_(ツ)_/¯            N
   Por simplicidad asumiremos
   un orden de ejecución en el
         caso paralelo …
¿Ejecución paralela?




                                E
                                J
                                E
                                C
                                U
                                C
                                I
                                Ó
                                N
    ¿Cuánto es A + B después?
        270 + 330 = 600
¿Ejecución paralela?




                       E
                       J
                       E
                       C
                       U
                       C
                       I
                       Ó
                       N
                           ¿Cuánto es A + B después?
                               260 + 340 = 600
¡Cuidado cuando el orden importe!



    ¿Cuánto es A + B después?
                                E
        260 + 340 = 600
                                J
                                E
                                C
                                U
                                C
                                I
                                Ó
                                N
¡Cuidado cuando el orden importe!



    ¿Cuánto es A + B después?
                                       E
        260 + 340 = 600
        No tenemos   ningún problema
                                   J con la restricción, pero el
            orden de ejecución puede
                                   E afectar el resultado.
                                         C
       Dependiendo de la aplicación, a veces
                                         U puede ser necesario preservar
             el orden de transacciones y/o
                                         C aplicar ejecución serial.
                                         I
                                         Ó
                                         N
¿Ejecución paralela?




                                E
                                J
                                E
                                C
                                U
                                C
                                I
                                Ó
                                N
    ¿Cuánto es A + B después?
        300 + 340 = 640

                                    ¿Dónde está el problema?
¿Ejecución paralela?




                                E
                                J
                                E
                                C
                                U
                                C
                                I
                                Ó
                                N
    ¿Cuánto es A + B después?
        300 + 340 = 640

                                    ¿Dónde está el problema?
Planificaciones:
 Secuenciables vs. No Secuenciables


                                  “Secuenciable”
                          Equivalente a ejecutar transacción
                          T1 y después transacción T2 (serial)




          “No secuenciable” …
Planificaciones:
 Secuenciables vs. No Secuenciables

   Una planificación es una lista de acciones de un conjunto
          de transacciones en el orden   de ejecución.
                                     “Secuenciable”
                               Equivalente a ejecutar transacción
                               T1 y después transacción T2 (serial)
  Una planificación secuenciable tendrá el mismo efecto que
   una planificación serial (en algún orden de las transacciones).




           “No secuenciable” …
Equivalencia por conflictos


                                      2
                  1           W (X)               R (Y)       W(Y)

      T1                                      3
P1
      T2

           W(X)       R (Y)           W (Y)
                                                              4




                      1                   2

                                      W (X)       R (Y)           W(Y)

      T1
 P2                                           3
      T2                                                  4
           W(X)       R (Y)   W (Y)
Otro ejemplo de Plan secuenciable
Otro ejemplo de No Plan secuenciable
RECUPERABILIDAD
Recuperabilidad
• Una tx puede interrumpirse por diferentes
  problemas:
  – Fallas (caídas) del computador
  – Error (externo) de la transacción o del sistema
  – Errores (internos) o condiciones de excepción de la
    transacción
  – Imposición de control de concurrencia (dead-locks, etc.)
  – Falla de disco
  – Catástrofes (externas)
  – Etc…

 Recuperabilidad
     Un plan P es recuperable si ninguna tx T de P se confirma
     antes de que se hayan confirmado todas las tx T’ que han
     escrito un elemento que T lee posteriormente




                        W (X)                           C
         T1
P1
         T2

              R(X)      Se leyó antes
                                        W (X)   C
Plan No recuperable


            W (X)                                                   C
     T1
P1
     T2
          Ojo: se leyó        R(X)        W (X)         C
          algo no
          confirmado



                         Si T1 fallara se dificultará la recuperación!
Plan recuperable
     T2 TIENE QUE ESPERAR QUE T1 HAGA COMMIT




               W (X)                                  C
         T1
P1
         T2

                           R(X)        W (X)                      C




                       Si T1 falla, T2 también falla en cascada
SOLUCIÓN: BLOQUEOS (LOCKS)
Un protocolo: Bloqueo en 2 fases
• Si una transacción T quiere leer un objeto O, tiene
  que conseguir un bloqueo compartido sobre O
  – Varias transacciones pueden leer el mismo objeto al
    mismo tiempo
• Si una transacción T quiere modificar un objeto O,
  tiene que conseguir un bloqueo exclusivo sobre O
  – Un bloqueo exclusivo excluye bloqueos compartidos
  – T puede leer O (por supuesto)
  – Así nadie (aparte de T) puede ni leer ni modificar O
    mientras T tenga su bloqueo exclusivo sobre O
Conflicto de Lectura–Escritura




                                E
                                J
                                E
                                C
                                U
                                C
                                I
                                Ó
                                N
    ¿Cuánto es A + B después?
        300 + 340 = 640
… con bloqueos




                                       E
                                       J
                                       E
                                       C
                                       U
                                       C
                                       I
                                       Ó
                                       N

 ¿Cómo sería la planificación final?
… con bloqueos




                                E
                                J
                                E
                                C
                                U
                                C
                                I
                                Ó
                                N



 Todavía permite conflictos …
… conflicto




                                 E
                                 J
   ¿Qué tipo de conflicto hay?   E
                                 C
       ¡Escritura-lectura!       U
                                 C
                                 I
                                 Ó
                                 N
                                     ¿Una solución?
                                          …
… bloqueo estricto
     Solución: Liberar los bloqueos solo cuando la transacción haya
                    terminado (bloqueo estricto) …




                                  E
                                  J
                                  E
                                  C
                                  U
                                  C
                                  I
                                  Ó
                                  N
Un protocolo: Bloqueo en 2 fases estricto
• Si una transacción T quiere leer un objeto O, tiene que
  conseguir un bloqueo compartido sobre O
  – Varias transacciones pueden leer el mismo objeto al mismo
    tiempo
• Si una transacción T quiere modificar un objeto O,
  tiene que conseguir un bloqueo exclusivo sobre O
  – Un bloqueo exclusivo excluye bloqueos compartidos
  – T puede leer O (por supuesto)
  – Así nadie (aparte de T) puede ni leer ni modificar O mientras
    T tenga su bloqueo exclusivo sobre O
• (Solo) cuando T haya terminado, liberará sus bloqueos
Un protocolo: Bloqueo en 2 fases estricto
• Si una transacción T quiere leer un objeto O, tiene
  que conseguir un bloqueo compartido sobre O
   – Varias transacciones pueden leer el mismo objeto al
     mismo tiempo
• Si una transacción T quiere modificar un objeto O,
         La forma más popular de garantizar secuenciabilidad.
  tiene que conseguir un bloqueo exclusivo sobre O
   – Un bloqueo exclusivo excluye bloqueos compartidos
   – T puede leer O (por supuesto)
   – Así nadie (aparte de T) puede ni leer ni modificar O
     mientras T tenga su bloqueo exclusivo sobre O
• (Solo) cuando T haya terminado, libará sus bloqueos
… pero cuidado!                     Hay que evitar interbloqueos
                                            (deadlocks)




                            E
                            J
                            E
                            C
                            U
                            C
                            I
                            Ó
                            N



                      Solución 1: Plazos para terminar o …
          Solución 2: Detectar ciclos en transacciones esperando o …
Bloqueo en 2 fases conservativo
       Solución 3: La transacción adquieren todos los bloqueos
            necesarios al inicio y de una forma atómica …




                                  E
                                  J
                                  E
                                  C
                                  U
                                  C
                                  I
                                  Ó
                                  N



                                                      ¿Es estricto?
                                                         No …
Bloqueo en 2 fases estricto/conservativo
    Solo se pueden paralelizar transacciones que no compartan objetos
                   (lo más “fácil” pero lo menos paralelizable)




                                      E
                                      J
                                      E
                                      C
                                      U
                                      C
                                      I
                                      Ó
                                      N
Ejemplo en
APP
Pero para un usuario …
Hemos terminado con bases de datos relacionales
Preguntas?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
