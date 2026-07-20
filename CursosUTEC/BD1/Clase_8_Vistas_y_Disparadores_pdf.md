---
curso: BD1
titulo: Clase 8 Vistas y Disparadores
slides: 54
fuente: Clase 8 Vistas y Disparadores.pdf
---

                                 CLASE 8:
                          VISTAS Y DISPARADORES
                                   (SQL)

                             CS2041- Base de Datos I
                                             Ciclo 2024-1



Teófilo Chambilla - tchambilla@utec.edu.pe
   Brenner Ojeda - bojeda@utec.edu.pe
       CS2041 Base de Datos I
       Teófilo Chambilla Aquino




Índice
• Introducción
• Vistas
• Vistas Actualizable
• Vistas Materializadas
• Disparadores
CS2041
BASE DE DATOS I
CICLO 2024-1

  Introducción                                                SQL -Vistas y Disparadores

Modelo Relacional     Algebra Relacional &        SQL                 Formas Normales
                       Cálculo Relacional

 Entidad - Relación                          Actualización,
                                             Restricciones
¿Acaso hemos visto todo de SQL?




                                  (no)
Lo que exploraremos hoy día




                              (vistas y disparadores)
Motivación: Metacritic
Motivación: Metacritic
Metacritic: Evaluaciones de música
Agregación de evaluaciones




               ¿Pero si quisiéramos hacer este tipo de consulta con mucha frecuencia? …
Agregación de evaluaciones




                             ¿Algún problema aquí? …
Agregación de evaluaciones dinámicas
VISTAS

         Capítulo 3.6 | Ramakrishnan / Gehrke
Vistas: tablas virtuales
Vista: una tabla virtual
Vista: facilitan consultas más simples
¿Cómo funcionan las vistas?                                (0) Crear la vista




        (2) Ejecutar la consulta extendida sobre las   (1) Extender la consulta de conformidad
        tablas bases                                   con la vista
¿Cómo funcionan las vistas?
    Con la vista, guardamos una sub-consulta frecuente para
                   reutilizarla en varias consultas.
 (No estamos guardando/materializando los datos de la tabla
 virtual. ¡Así no hay problema con actualizaciones en los datos
                            subyacentes!)
Eliminar una vista
Eliminar una vista
VISTAS ACTUALIZABLES

¿Actualizar una vista?




          ¿Qué pasa aquí entonces? …
¿Actualizar una vista? ¡Hay ambigüedad!




  La idea es actualizar las tablas bases mediante la vista (no la
                           vista misma).
                   ¿Entonces, cuál sería el resultado de esta inserción sobre las tablas bases? …
                          ¡No basta la información para actualizar las tablas bases!
Vistas de solo lectura




  Cuando la vista permite ambigüedad, la vista es solo lectura:
                     no se puede actualizar.
Vistas actualizables
Vistas actualizables
Actualizando una vista
• Es difícil caracterizar precisamente las vistas actualizables,
  (incluyendo en la teoría de bases de datos) pero una vista es
  “solo lectura” cuando involucra, por ejemplo:
  – Agregación (conteo, suma, etc)
  – Proyección que elimine una columna que no permita nulos
• A menudo, los motores no implementan vistas actualizables
  sobre varias tablas


      Pero por supuesto, no hay problema actualizar las tablas bases directamente (si uno tiene acceso) …
                               La vista se actualizará automáticamente
Vistas: ¡No son tablas físicas!
¿Para qué sirven las vistas entonces?
• Abreviatura/abstracción
  – Reducir la complejidad de consultas, evitando repeticiones de
    patrones comunes


• Seguridad
  – Se puede dar acceso a una vista (un subconjunto de los datos) y no a
    todos los datos


                    ¿Cuáles son los costos de mantener una vista?
               ¡Casi nada con respecto a la gestión de los datos! Pero …
El costo de consulta




        Son equivalentes pero la consulta extendida es mucho más difícil de optimizar

                        ¿Y si el rendimiento de las consultas importa?

                                                                                        …
VISTAS MATERIALIZADAS
Vista materializada: guardar tablas virtuales
Vista materializada: consultar directamente
Vista materializada: actualización
Vista materializada: actualización
Materializar vistas vs. Crear tablas




                   ¿Cuál es la diferencia más importante entre crear una tabla
                                  y crear una vista materializada?
       En una vista materializada, se guarda la consulta para facilitar la actualización de la
                                    vista en una fase posterior
¿Se pueden cambiar vistas?




                             … es limitado.
   Vistas “virtuales” son estándares

Vistas materializadas no son estándares
    (pero hay soporte en Oracle y Postgres 13+)
DISPARADORES
(O GATILLOS/TRIGGERS)

                        Capítulo 3.6 | Ramakrishnan / Gehrke
¿Actualizar una tabla automáticamente?



    ¿Cómo podríamos actualizar la tabla
 ÁlbumEval dada una inserción a Evaluación?
Disparadores: Evento/Condición/Acción




                                     ¿Qué hace el disparador?
                            Si intentamos reducir el pm de un álbum, se
                                      restaurará el valor previo
                              ¿Dónde están Evento/Condición/Acción?

Disparadores: Evento/Condición/Acción




                                        No cambia.
Disparadores: Evento/Condición/Acción




    ¿Cómo podríamos actualizar la tabla
 ÁlbumEval dada una inserción a Evaluación?
Disparadores: Evento/Condición/Acción




                                                        Actualizaciones atrasadas
          ¿Qué pasaría si tuviéramos BEFORE INSERT …?
     Disparadores son estándares

 !Pero su implementación en varios
     motores varía muchísimo!
Por ejemplo, Postgres usa "stored procedures" …
Disparadores en Postgres




                  Stored Procedure


                           Trigger
Disparadores + Vistas Mat. en Postgres


                         Vista Mat.




                   Stored Procedure




                            Trigger
Disparadores en Postgres

                      Vista Mat.




                Stored Procedure




                                   Stored Procedure


                         Trigger            Trigger
Disparadores en Postgres


                          Vista Mat.




                    Stored Procedure




                      ¿Cuál es la diferencia entre ambos?                Stored Procedure

             La opción izquierda actualizará la vista entera cada vez.
                              Trigger                                             Trigger
            La opción derecha actualizará solo el álbum que cambió.
RESUMEN
El mundo cambia …




                    … las bases de datos cambian
• Vistas:                                                      • Tablas físicas (sin disparadores)
   – No hay datos físicos                                         – Hay que actualizarlas a mano
       • Más caro ejecutar consultas                                  • Más barato ejecutar consultas
       • Los resultados no pueden ser obsoletos                       • Los resultados pueden ser obsoletos
       • Más barato actualizar tablas




• Vistas materializadas:                                       • Tablas físicas (con disparadores)
   – Las actualizaciones ejecutan a veces                         – Las actualizaciones ejecutan automáticamente
       • Más barato ejecutar consultas                                 • Más barato ejecutar consultas
       • Los resultados pueden ser obsoletos                           • Los resultados deberían ser actualizados
            – (pero se puede usar un disparador con un costo           • Más caro actualizar tablas
              de actualización)
                                                                       • Agregan mucha complejidad
       • Poco portable
                                                                       • Poco portable
Preguntas?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
