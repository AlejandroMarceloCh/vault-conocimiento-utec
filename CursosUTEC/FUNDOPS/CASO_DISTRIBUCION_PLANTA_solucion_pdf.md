---
curso: FUNDOPS
titulo: CASO DISTRIBUCION PLANTA solución
slides: 9
fuente: CASO DISTRIBUCION PLANTA solución.pdf
---

La empresa Maquinaria XYZ que cuenta con una planta de determinadas
características, se debe aplicar el método SLP para determinar una propuesta
de distribución de planta buscando minimizar el manejo de materiales y
cumpliendo con las restricciones dadas. La empresa cuenta con diez
departamentos, cada uno con un área requerida previamente determinada (los
espacios requeridos para pasillos y manipulación ya se encuentran
considerados).




El 85% de la actividad del sistema equivale al desarrollo de cuatro productos,
para los que se usa un montacargas y tarimas para su manejo. La secuencia
de fabricación, la cantidad de unidades producidas y las unidades que puede
llevar el montacargas por viaje se presentan a continuación:




Para el problema se presentan las siguientes condiciones:
1. Por seguridad no se desea colocar los Procesos A y F juntos, ni el proceso D
cerca de las oficinas.
2. Se desea que las oficinas den al parqueadero.
3. La zona de mantenimiento debe estar cerca a todos los procesos,
principalmente del A y del E.
4. Los almacenes MP y PT deben estar junto a la zona de carga y descarga.
El plano de la empresa es el siguiente:




   1. ¿HACER UN ANALISIS DE PRODUCTO CANTIDAD?
   2. HACER EL ANALISIS DE FLUJO DE MATERIALES (DIAGRAMA MULTIPRODUCTO), MATRIZ
      “DESDE-HASTA” CALCULAR LA CANTIDAD DE VIAJES POR SEMANA DEL MONTACARGA.
   3. REALIZAR LA RELACION ENTRE ACTIVIDADES, LA MATRIZ DE CERCANIAS Y EL
      DIAGRAMA DE RELACIONES. UTILICE LA SIGUENTE TABLA DE IMPORTANCIAS Y LA
      TABLA DE RELACIONES.
  4. REALIZAR EL DIAGRAMA RELACIONAL DE RECORRIDOS – ACTIVIDADES. UTILICE LA
     SIGUIENTE TABLA DE FLUJO DE MATERIALES




  5. REALIZZAR EL DIAGRAMA RELACIONAL DE ESPACIOS



SOLUCION:

  1. ANALISIS PRODUCTO -CANTIDAD (P-Q)


Producto     unidades/semana

producto 3            15000
producto 4             5000
producto 2             5000
producto 1              800
                  unidades/semana
20000

15000

10000

5000

   0
         producto 3   producto 4   producto 2   producto 1




  2. RECORRIDO DE PRODUCTOS
        Se realiza el diagrama multiproducto y se agregan las unidades de
        transporte entre departamentos de trabajo o secciones de producción.
        Como el objetivo de realizar una adecuada distribución de planta es
        reducir costos, se tendrá en cuenta los viajes que debe realizar el
        montacargas para transportar los materiales y no la cantidad de
        materiales como tal.
      Flujo
                     800       5000           15000                5000
     semanal

    unidades/
      viajes          50       100              75                  25

     viajes /
     semana           16        50             200                  200
   (montacargas)


Con los viajes por semana del montacargas y el diagrama multiproducto, se
procede a realizar la Matriz “desde-hasta”, que representa la cantidad de viajes
que hace por semana el montacargas desde una sección a otra.


                      MP A B C D E F PT
                   MP 0 250 16 200
                   A     0     200 50        200
                   B         0        416
                   C        400 0
                   D               0 50
                    E   200            0 266
                    F                     0 266
                   PT                         0
Luego, se procede a realizar la matriz de flujo que agrupa la cantidad de flujo
que se mueve entre secciones, es decir, que los valores de esta matriz no
tienen en cuenta la dirección de flujo.



                      MP A B C D E F PT
                   MP 0 250 16 200
                   A     0     200 50 200   200
                   B        0 400     416
                   C           0
                   D               0 50
                   E                  0 266
                   F                      0 266
                   PT                       0
   3. RELACION ENTRE ACTIVIDADES



Teniendo estas valoraciones, se procede a reemplazar las claves dentro de la
matriz de flujo para obtener la matriz de importancia de cercanías.


                 NODOS MP      A   B    C    D   E    F   PT
                  MP    -      I   O    I    U   U    U   U
                   A           -   U    I    O   I    U    I
                   B               -    A    U   A    U   U
                   C                    -    U   U    U   U
                   D                         -   O    U   U
                    E                            -    I   U
                    F                                 -    I
                   PT                                      -

El siguiente paso del método SLP, es hacer la gráfica de relaciones. Para esto,
primero es necesario conocer las otras razones que pueden dar importancia de
cercanía entre departamentos diferentes a la cantidad de flujo (medida en
viajes por semana).
   4. DIAGRAMA DE RELACIONES

Una forma de facilitar la construcción del diagrama, es realizando primero una
tabla de valores que sume las importancias de cada departamento:


                                 DEPARTAMENTOS
                 1   2   3   4   5 6     7     8       9     10     TOTAL
       1         -   0   0   0   0 0     0    -1       0      0       -1
       2             -   0   0   2 1     2     0       0      0        5
       3                 -   0   2 0     0     0       0      2        4
       4                     -   3 2     2     2       3      2       14
       5                          - 0    2     1       2     -1        4
       6                             -   4     0       4      0        8
       7                                 -     1       0      0        1
       8                                       -       1      0        1
       9                                               -      2        2
      10                                                      -        0
     TOTAL       0   0   0   0   7   3    10     3    10      5



DEPARTAMENTOS TOTAL
      1         -1
      2          5
      3          4
      4         14
      5         11
      6         11
      7         11
      8          4
      9         12
      10         5


La diagramación que se propone partiendo de la tabla de valores, es asignando
en un punto medio el departamento que sume la mayor importancia teniendo
en cuenta todas las otras secciones. Luego se van asignando los nodos que
tengan una mayor valoración con respecto a este, y se continúa de la misma
manera buscando los valores más altos.
5. DIAGRAMA DE RELACIONES DE ESPACIO
Trasladando el diagrama al plano, se esboza una de las tantas soluciones que puede haber.
