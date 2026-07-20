---
curso: SIOPS
titulo: 4.2. Introducción a los Sistemas Empresariales
slides: 29
fuente: 4.2. Introducción a los Sistemas Empresariales.pdf
---

       Sistemas de Información
       para Operaciones

      Introducción a los Sistemas Empresariales




Profesor: Carlos Villanueva Qwistgaard
Objetivos de Aprendizaje

1.   Explicar el rol de los sistemas empresariales en el soporte de los procesos
     del negocio.
2.   Entender la arquitectura ERP
3.   Introducción a Global Bike
4.   Explorar SAP
Sistemas Empresariales

      Los sistemas empresariales permiten a las empresas gestionar
      efectivamente los procesos de negocio a través de las áreas
      funcionales.



      Contribuyen a lograr la eficiencia operacional mediante la
      transparencia entre las áreas funcionales y proporcionan
      información consistente para la toma de decisiones gerencial.



      El impacto de la ejecución de los procesos en el estado
      financiero de la empresa se puede monitorear y analizar en
      tiempo real a través del uso de un sistema empresarial integrado.
¿Qué es un ERP?

▪ Sistema de gestión empresarial que sirve de soporte en las tareas administrativas, de
  control, de planificación y operación del negocio.
▪ Sistema de información que busca integrar las funciones y procesos de una organización
  con el objeto de atender las necesidades de sus distintas áreas.
▪ Tres características fundamentales:
    ▪   Son multifuncionales
    ▪   Son integrados
    ▪   Son modulares
ERP: Características funcionales

▪ Cálculo automatizado de necesidades
  de recursos materiales, financieros,
  de personal, entre otros;
  proyecciones de venta, financieras,
  etc.
▪ Operaciones transaccionales (registro
  de mercadería, emisión de facturas,
  transferencias bancarias, emisión de
  cheques, etc.)
ERP: Características Funcionales (cont.)

▪ Generación de documentos legales (EEFF,
  reportes SUNAT, registros de Aduana,
  certificado de retención, etc.)
▪ Alertas y autorizaciones (alertas de nivel de
  stock, bloqueo a clientes morosos, venta con
  bajo margen, etc.)
 ERP: Beneficios




Integración de procesos   Reducción de tiempos y       Obtención de       Reduce inventarios      Estandarización de
  críticos de negocios      costos en procesos     información –veraz y                          actividades bajo una
                               ineficientes              oportuna                              plataforma tecnológica.
2023
Módulos SAP ERP
(Antes de S/4HANA)
Mapa de Procesos y Módulos SAP


 Procure-to-Pay (MM-FI)

 Plan-to-Produce (PP-MM-FI)

 Order-to-Cash (SD-MM-FI)
 Record-to-Report (FI-CO)

 Warehouse Management (WM-MM)
SAP Business Suite
Unificando Aplicaciones + Datos + IA



                                        Agentes IA




                                          Datos




                                       Aplicaciones
                                       SAP & No SAP
Integración con otras Empresas
Datos de un sistema empresarial

                           Datos
                       organizativos




           Datos de                     Datos
         transacción                   Maestros
Datos
Organizativos
   Define la estructura del negocio
    en términos legales o propósitos
    del negocio.
   Los datos rara vez cambian
    Dato organizativo- Mandante

   Mandante:

       Es el nivel de la organización más alto

       Representa a la empresa global; está compuesta de muchas sociedades.
    Dato organizativo- Sociedad

   Elemento central de la organización para la contabilidad financiera

   Los libros se mantienen a este nivel para reportes legales

   Identifica entidades legales de la empresa global (Mandante)
   Son legalmente independientes de las otras sociedades de la empresa global
   Un mandante puede tener múltiples sociedades
   Una sociedad pertenece a un único Mandante.
    Dato organizativo- Centro

   Realiza múltiples funciones

   Usados en muchos procesos

   Puede ser una fábrica, un almacén, una oficina, un centro de distribución,
    etc.
Datos organizativos de GBI

    Mandante




    Sociedad




      Centro




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón, Pinto y Soto
                                                                                                                 20
(2017)

    Dato maestro
   Datos de largo plazo que
    típicamente representan entidades
    asociadas con varios procesos
       Cliente
       Proveedor
       Material
   Típicamente incluye:
       Datos generales (generales a
        todas las sociedades)
       Datos financieros (centro de
        costo específico)
                                        Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón, Pinto y Soto
       Datos de Área-específico        (2017)
        (ventas, compras, centros)
Maestro de materiales
   Maestro de material se utiliza en numerosos procesos:
         Aprovisionamiento

         Gestión de pedidos

         Producción

         Planeación de material
         Gestión de activos fijos
         Proyectos

         Gestión del ciclo de vida
Maestro de materiales
   Los datos se agrupan por:
       Proceso

       Tipo de Material

       Elemento de organización
Tipo de material
   Materias Primas (ROW)
        Se compran, no se venden, se usan en producción

        Tiene vistas relativas a la compra y producción

        No tiene vista relativa a las ventas

   Semi elaborados(HALB)
        Se producen usando otros materiales (ROH, HALB)
        Utilizado en la producción de otros materiales (HALB, FERT)

        No se compran y tampoco se venden
Tipo de material (Continuación)
   Productos terminados(FERT)
       Se producen usando otros materiales (ROH, HALB)

       Se venden a los clientes

   Mercaderías(HAWA)

       Se compran y se re-venden sin un proceso adicional
       Numerosos tipos
Lista de Materiales de GBI
Elementos de organización
   El mismo material se puede usar de forma diferente por los distintos elementos de
    organización

   Diferentes sociedades

   Semielaborados (HALB) en una, terminados(FERT) en otra

   Diferentes centros

   Sólo exporta e importa en un centro específico, no en todos
   Diferentes puntos de venta
   Por mayor vs. Por menor
Estructura
    de
productos
  de GBI
     Datos de
     Transacción
   Los datos se generan durante la
    ejecución las etapas de los procesos
   Requiere:
       Datos organizativos
       Datos maestros
       Datos situacionales
   Ejemplo: Creación de pedido del
    cliente
       Elementos organizativos:
        Mandante, Sociedad, Área de
        Ventas
       Datos maestros: Cliente, Material
       Datos situacionales: Fecha,
        Tiempo, Persona

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
