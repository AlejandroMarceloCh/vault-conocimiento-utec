---
curso: SIOPS
titulo: 1. El Proceso de Producción - Datos Organizativos y Datos Maestros
slides: 33
fuente: 1. El Proceso de Producción - Datos Organizativos y Datos Maestros.pdf
---

El Proceso de Producción

                Profesor: Carlos Villanueva Q.
Objetivos
1. Describir los datos maestros y organizativos asociados al proceso de
   producción.
2. Utilizar eficazmente SAP® ERP para crear Datos Maestros asociados
   al Proceso de Producción.
Tipos de Fabricación
 Fabricación Discreta, Repetitiva y Por Procesos

 Fabricación Discreta y Repetitiva
    • Materiales tangibles
    • Produce unidades “discretas” (c/unidad es distinta a otras, se puede contar y los
      materiales son identificables): skateboards, bicicletas
 Fabricación Repetitiva
    • Un mismo producto o similar se produce repetidamente en un periodo prolongado de
      tiempo a una tasa relativamente constante.

 Fabricación Por procesos
    • Fabrica materiales (petróleo, pintura, bebidas) que no se fabrican en unidades
      individuales. Se producen en grandes cantidades y se miden en magnitudes como
      galones, litros, etc.
Fig. 1: Un Proceso de Producción Básico




                  Magal and Word | Integrated Business Processes with ERP
                                                                            4
                                     Systems | © 2011
Datos Organizativos

• Mandante
• Sociedad
• Centro (de fabricación)
• Almacén
Datos Maestros
     • Listas de Materiales (LMat)
     • Puesto de Trabajo
     • Hojas de ruta de productos
     • Maestro de materiales
     • Medios auxiliares de fabricación (MAF)




      Magal and Word | Integrated Business Processes with ERP Systems | © 2012
      Traducido por Grandón, Pinto y Soto (2017)        6
Datos Maestros
     • Listas de Materiales (LMat)
     • Puesto de Trabajo
     • Hojas de ruta de productos
     • Maestro de materiales
     • Medios auxiliares de fabricación (MAF)




      Magal and Word | Integrated Business Processes with ERP Systems | © 2012
      Traducido por Grandón, Pinto y Soto (2017)        7
Lista de Materiales (LMat o BOM )
      • También conocido como BOM (Bill Of Materials)
      • Identifica los componentes que son necesarios para
        fabricar un material
      • Un componente puede tener su propio Lmat para crear una
        LMat multinivel.
      • Lmat se usa en
            • Planificación del material
            • Producción
            • Aprovisionamiento
            • Costeo del producto
      Magal and Word | Integrated Business Processes with ERP Systems | © 2012
      Traducido por Grandón, Pinto y Soto (2017)        8
Fig. 2: LMats de uno y múltiples niveles




  Magal and Word | Integrated Business Processes with ERP Systems | © 2012
  Traducido por Grandón, Pinto y Soto (2017)        9
Fig. 3:
Lista de
materiales
para
bicicleta de
turismo




Magal and Word | Integrated
Business Processes with ERP
Systems | © 2012
Traducido por Grandón, Pinto y Soto   10
(2017)
Fig. 4:
Lista de
materiales
para
bicicleta
todo
terreno




             Magal and Word | Integrated Business Processes with ERP Systems | © 2012
             Traducido por Grandón, Pinto y Soto (2017)        11
Lista de Materiales - Cabecera
• Se aplica a toda la lista de materiales
• Estado: activa, inactiva
• Cantidad base: cantidad de productos que se
  pueden producir con los materiales especificados
  en la LMAT
• Utilización: fabricación, ingeniería, cálculo de
  costos, etc.
• Centro: cada centro puede tener una lista de
  materiales diferentes
• Validez: rango de fechas
 Magal and Word | Integrated Business Processes with ERP Systems | © 2012
 Traducido por Grandón, Pinto y Soto (2017)        12
Lista de Materiales – Posiciones
 • Aplica para una posición específica de la Lmat
 • Tipo de Posición:
     • Posición de Almacén – debe tener un maestro de material
     • Posición de no Almacén – no necesita maestro de material
     • Posición de dimensión bruta – debe especificar tamaño
     • Posición de documento – diseños de ingeniería, instrucciones
       adicionales
 • Número de material
 • Cantidad

   Magal and Word | Integrated Business Processes with ERP Systems | © 2012
   Traducido por Grandón, Pinto y Soto (2017)        13
Fig. 5: Estructura de una LMat




  Magal and Word | Integrated Business Processes with ERP Systems | © 2012
  Traducido por Grandón, Pinto y Soto (2017)        14
Demo 6.1 Revisión de una LMat para una
bicicleta y ensamble de rueda
  • Revisión de algunos de los datos incluidos en un
    maestro de materiales




  Magal and Word | Integrated Business Processes with ERP Systems | © 2012
  Traducido por Grandón, Pinto y Soto (2017)        15
Datos Maestros
     • Listas de Materiales (LMat)
     • Puesto de Trabajo
     • Hojas de ruta de productos
     • Maestro de materiales
     • Medios auxiliares de fabricación (MAF)




      Magal and Word | Integrated Business Processes with ERP Systems | © 2012
      Traducido por Grandón, Pinto y Soto (2017)        16
Puesto de Trabajo
    • Lugar donde se realiza trabajo de valor agregado
      necesario para producer un material.
    • Puede ser también una máquina o un grupo de
      máquinas, una línea entera de producción, un área de
      trabajo o una persona o grupo de personas
      responsables de completar operaciones en diferentes
      lugares del centro.




      Magal and Word | Integrated Business Processes with ERP Systems | © 2012
      Traducido por Grandón, Pinto y Soto (2017)        17
Fig. 6: Datos de un puesto de trabajo




                                           Puesto de Trabajo




  Magal and Word | Integrated Business Processes with ERP Systems | © 2012
  Traducido por Grandón, Pinto y Soto (2017)        18
Fig. 7: Ejemplo de
puesto de trabajo
(ensamblaje de
un Boeing 757)




                     19
Fig. 8: Planta de fabricación de GBI en
Dallas


Puestos de
Trabajo




                     20

Fig. 9: Puestos de trabajo de GBI




  Magal and Word | Integrated Business Processes with ERP Systems | © 2012
  Traducido por Grandón, Pinto y Soto (2017)        21
Demo 6.2 Revisión del puestos de trabajo de
GBI
• Revisión de puestos de trabajo de GBI




          Magal and Word | Integrated Business Processes with ERP Systems | © 2012
          Traducido por Grandón, Pinto y Soto (2017)        22
Datos Maestros
     • Listas de Materiales (LMat)
     • Puesto de Trabajo
     • Hojas de ruta de productos
     • Maestro de materiales
     • Medios auxiliares de fabricación (MAF)




      Magal and Word | Integrated Business Processes with ERP Systems | © 2012
      Traducido por Grandón, Pinto y Soto (2017)        23
   Hojas de ruta de productos
Lista de operaciones a ejecutar para fabricar un material
   • Operaciones
       • Secuencia
           • Estándar
           • Alternativa
           • Paralela
   • Puesto de trabajo
   • Tiempo
       • Preparación, Tratamiento, Desmontaje



   Magal and Word | Integrated Business Processes with ERP Systems | © 2012
   Traducido por Grandón, Pinto y Soto (2017)        24
Fig. 10:
Estructura
de una hoja
de ruta



Magal and Word | Integrated Business
Processes with ERP Systems | © 2012
Traducido por Grandón, Pinto y Soto (2017)   25
Fig. 11:
Hoja de ruta del ensamble de rueda de turismo de lujo




        Tiempo de mano de obra para ensamblar 50 ruedas = 160 min. (5+50*3+5)
                                        26
Fig. 12:
Hoja de
ruta de la
bicicleta
de turismo
de lujo


             27
Demo 6.3 Revisión de la hoja de ruta de una
bicicleta y de un ensamble de rueda
• Revisión de la hoja de ruta de una bicicleta y de un
  ensamble de rueda




  Magal and Word | Integrated Business Processes with ERP Systems | © 2012
  Traducido por Grandón, Pinto y Soto (2017)        28
Fig. 13 Hojas de ruta y puestos de trabajo




                       29
Asignación de componentes

     • Especifica la relación entre una lista de materiales
       LMat y una hoja de ruta
     • Asigna componentes (materiales) en una lista de
       materiales, ya sea a una ruta o a una operación
       específica dentro de la hoja de ruta
     • Si no se asignan, supone que está asignado a la
       primera operación



       Magal and Word | Integrated Business Processes with ERP Systems | © 2012
       Traducido por Grandón, Pinto y Soto (2017)        30
Fig. 14: Asignación de Componentes




  Magal and Word | Integrated Business Processes with ERP Systems | © 2012
  Traducido por Grandón, Pinto y Soto (2017)        31
Capacidad de producción
     • Una medida de la cantidad de unidades de un
       material que un centro puede producir en un plazo
       determinado
     • Una fuente de datos para la planificación de la
       producción




      Magal and Word | Integrated Business Processes with ERP Systems | © 2012
      Traducido por Grandón, Pinto y Soto (2017)        32
Fig. 15: Ejemplo de plan de producción de GBI




Magal and Word | Integrated Business
                                       33
Processes with ERP Systems | © 2011

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
