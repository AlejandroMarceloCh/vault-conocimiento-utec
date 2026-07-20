---
curso: SIOPS
titulo: 1. Teoria - Proceso de Gestión de Pedidos - Datos Organizativos
slides: 33
fuente: 1. Teoria - Proceso de Gestión de Pedidos - Datos Organizativos.pdf
---

Proceso de Gestión de Pedidos
                     (Datos Organizativos)

                                                                Profesor: Carlos Villanueva Q.




Adaptado de: Magal and Word | Integrated Business Processes with ERP Systems | © 2011            1
                       Traducido por Grandón, Pinto y Soto ( 2017)
                          Objetivos de Aprendizaje

1.   Describir los niveles organizativos clave asociados al proceso de Gestión
     de Pedidos.
2.   Identificar Datos Maestros de Clientes en un Sistema empresarial
     (S/4HANA).




                                                                                 2
 Agenda                    1) Mandante

                           2)   Sociedad
                           3)   Centro
1.   Datos Organizativos   4)   Almacén                   ○ Organización de ventas
                           5)   Área de ventas            ○ Canal de distribución

                           6)   Puesto de expedición      ○ Sector (división)

                           7) Área de Control de Créditos

                           1)   Maestro de Materiales

                           2)   Maestro de Cliente

2. Datos Maestros          3) Registro de Información (INFO) Cliente-Material

                           4)   Condiciones de Precio

                           5)   Condiciones de Mensajes
                           6)   Registro Maestro Gestión de Créditos
           Proceso básico de gestión de pedidos




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    4
                                  Datos Organizativos

● Mandante ✔                                               ● Área de ventas
                                                                 ○ Organización de ventas
● Sociedad ✔
                                                                 ○ Canal de distribución
● Centro ✔
                                                                 ○ Sector (división)
● Almacén ✔                                                ● Cadena de distribución
                                                           ● Puesto de Expedición
                                                           ● Área de control de créditos


         Magal and Word | Integrated Business Processes with ERP Systems | © 2011 Traducido por Grandón,
                                                  Pinto y Soto ( 2017)
                                                                                                           6
 Agenda                    1) Mandante

                           2)   Sociedad
                           3)   Centro
1.   Datos Organizativos   4)   Almacén                   ○ Organización de ventas
                           5)   Área de ventas            ○ Canal de distribución

                           6)   Puesto de expedición      ○ Sector (división)

                           7) Área de Control de Créditos

                           1)   Maestro de Materiales

                           2)   Maestro de Cliente

2. Datos Maestros          3) Registro de Información (INFO) Cliente-Material

                           4)   Condiciones de Precio

                           5)   Condiciones de Mensajes
                           6)   Registro Maestro Gestión de Créditos
                                        Organización de ventas

● Responsable de:
   ○ Vender y Distribuir bienes y servicios
   ○ Negociar condiciones de ventas
   ○ Responsable de los clientes con respecto a las obligaciones y derechos de recurso en
     caso de disputas
● Utilizada para dividir el mercado basado en áreas geográficas.
● Nivel de agregación más alto en reportes relacionados con ventas.
● Una sociedad tiene al menos una Organización de Ventas.
● Una Organización de Ventas pertenece solo a una sociedad.

              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  9
               Organización de ventas de GBI




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    10
 Agenda                    1) Mandante

                           2)   Sociedad
                           3)   Centro
1.   Datos Organizativos   4)   Almacén                   ○ Organización de ventas
                           5)   Área de ventas            ○ Canal de distribución

                           6)   Puesto de expedición      ○ Sector (división)

                           7) Área de Control de Créditos

                           1)   Maestro de Materiales

                           2)   Maestro de Cliente

2. Datos Maestros          3) Registro de Información (INFO) Cliente-Material

                           4)   Condiciones de Precio

                           5)   Condiciones de Mensajes
                           6)   Registro Maestro Gestión de Créditos
                          Canal de distribución

● Medio por el cual la empresa distribuye sus productos y servicios
  a sus clientes
● Se usa para:
  ○ Diferenciar estrategias o enfoques de distribución
  ○ Diferenciar precios, responsabilidades
  ○ Tipos de canales: mayoristas, ventas al detalle, en línea.
  ○ Estadísticas y reportes al nivel del canal de distribución
● Una organización de ventas debe tener al menos un canal de
  distribución
                                                                      13
  Canales de distribución de GBI US




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    14
 Agenda                    1) Mandante

                           2)   Sociedad
                           3)   Centro
1.   Datos Organizativos   4)   Almacén                   ○ Organización de ventas
                           5)   Área de ventas            ○ Canal de distribución

                           6)   Puesto de expedición      ○ Sector (división)

                           7) Área de Control de Créditos

                           1)   Maestro de Materiales

                           2)   Maestro de Cliente

2. Datos Maestros          3) Registro de Información (INFO) Cliente-Material

                           4)   Condiciones de Precio

                           5)   Condiciones de Mensajes
                           6)   Registro Maestro Gestión de Créditos
                               Sectores
● Unidad utilizada por las empresas para combinar materiales y
  servicios con características similares.
  - Asociados con una línea de producto

  - Diferentes estrategias de venta, acuerdos de precio

  - Estadísticas y reportes a nivel de sector

● Una organización de venta tiene al menos un sector.
● Un producto o material se asocia solo a un sector
● Un sector puede ser asignado a múltiples organizaciones de venta.


                                                                      17
                 Sectores de GBI EE.UU.




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    18
                      Sectores de GBI Alemania




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    20
 Agenda                    1) Mandante

                           2)   Sociedad
                           3)   Centro
1.   Datos Organizativos   4)   Almacén                     ○ Organización de ventas
                           5)   Área de ventas              ○ Canal de distribución

                           6)   Puesto de expedición        ○ Sector (división)

                           7) Área de Control de Créditos

                           1)   Maestro de Materiales

                           2)   Maestro de Cliente

2. Datos Maestros          3) Registro de Información (INFO) Cliente-Material

                           4)   Condiciones de Precio

                           5)   Condiciones de Mensajes
                           6)   Registro Maestro Gestión de Créditos
                                           Área de ventas


•   Combinación única de:                                                     Determina qué productos serán
       Organización de Venta                                                  vendidos a través de qué canal y
                                                                              quién es responsable de esa venta
        Canal de distribución
        Sector


● Puede ser asignada solo a una sociedad.
● Todos los documentos asociados con el proceso de gestión de pedidos, tales
  como ofertas y listas de embalaje, pertenecen a un área de ventas.




        Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                 Pinto y Soto ( 2017)
                                                                                                                  22
                          Áreas de ventas de GBI




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    23
 Agenda                    1) Mandante

                           2)   Sociedad
                           3)   Centro
1.   Datos Organizativos   4)   Almacén                   ○ Organización de ventas
                           5)   Área de ventas            ○ Canal de distribución

                           6)   Puesto de expedición      ○ Sector (división)

                           7) Área de Control de Créditos

                           1)   Maestro de Materiales

                           2)   Maestro de Cliente

2. Datos Maestros          3) Registro de Información (INFO) Cliente-Material

                           4)   Condiciones de Precio

                           5)   Condiciones de Mensajes
                           6)   Registro Maestro Gestión de Créditos
                                                Centro


● En el proceso de gestión de pedidos un centro suministrador es
  una instalación desde la cual la empresa entrega sus productos y
  servicios a sus clientes.

● Un centro se puede asignar a más de un canal de distribución.

● A la inversa, una cadena de distribución puede estar asociada a
  más de un centro.




    Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                             Pinto y Soto ( 2017)
                                                                                                        26

                                         Centros




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    27
                                      Cadena de distribución


Una única combinación de organización de ventas y canal de distribución

   • Algunos datos maestros son mantenidos a este nivel
   • Maestro de material
   • Condiciones de precio


            Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                     Pinto y Soto ( 2017)
                                                                                                                28
 Agenda                    1) Mandante

                           2)   Sociedad
                           3)   Centro
1.   Datos Organizativos   4)   Almacén                     ○ Organización de ventas
                           5)   Área de ventas              ○ Canal de distribución

                           6)   Puesto de expedición        ○ Sector (división)

                           7) Área de Control de Créditos

                           1)   Maestro de Materiales

                           2)   Maestro de Cliente

2. Datos Maestros          3) Registro de Información (INFO) Cliente-Material

                           4)   Condiciones de Precio

                           5)   Condiciones de Mensajes
                           6)   Registro Maestro Gestión de Créditos
                                       Puesto de expedición

● Un lugar en un centro desde el cual se despachan las entregas de
  salida.
     ■ Muelle de carga
     ■ Sala de correo
     ■ Estación de tren
     ■ Se asocia también a un grupo de empleados que maneja entregas especiales o rápidas


● Un centro debe tener al menos un punto de expedición
● Un centro puede tener más de un puesto de expedición
● Un punto de expedición se asocia a uno o más centros
           Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                    Pinto y Soto ( 2017)
                                                                                                               30
             Puestos de expedición compartidos




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    31
                 Puestos de expedición múltiples




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    32
                Puesto de expedición. Ejemplo 1




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    33
                Puesto de expedición. Ejemplo 2




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    34
 Puesto de expedición. Ejemplo 3




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    35
 Agenda                    1) Mandante

                           2)   Sociedad
                           3)   Centro
1.   Datos Organizativos   4)   Almacén                     ○ Organización de ventas
                           5)   Área de ventas              ○ Canal de distribución

                           6)   Puesto de expedición        ○ Sector (división)

                           7) Área de Control de Créditos

                           1)   Maestro de Materiales

                           2)   Maestro de Cliente

2. Datos Maestros          3) Registro de Información (INFO) Cliente-Material

                           4)   Condiciones de Precio

                           5)   Condiciones de Mensajes
                           6)   Registro Maestro Gestión de Créditos
                               Área de control de créditos

● Nivel organizativo responsable por los créditos del cliente
● Determina la solvencia de los clientes, establece el límite de crédito y
  monitorea y maneja las prórrogas de crédito de los clientes.
● Sistema Centralizado
   ○ Un área de control de crédito para todas las sociedades en la empresa global
   ○ Todos los clientes de una sociedad son gestionados por un área de control de crédito
● Sistema Descentralizado
   ○ Más de un área de control de crédito en la empresa global
   ○ Cada área de control de crédito            gestiona   los créditos   para      una   o más
     sociedades en la empresa global

                                                                                              37
          Area de control de crédito centralizada




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    38
      Area de control de crédito descentralizada




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    39

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
