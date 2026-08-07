---
curso: SIOPS
titulo: 1. El Proceso de Producción - Datos Organizativos y Datos Maestros
slides: 33
fuente: 1. El Proceso de Producción - Datos Organizativos y Datos Maestros.pdf
---

## Slide 1

Portada del capítulo. Título "El Proceso de Producción". Autor: "Profesor: Carlos Villanueva Q." Logo UTEC (decorativa).

## Slide 2

Título "Objetivos". Lista numerada:
1. Describir los datos maestros y organizativos asociados al proceso de producción.
2. Utilizar eficazmente SAP® ERP para crear Datos Maestros asociados al Proceso de Producción.

## Slide 3

Título "Tipos de Fabricación". Subtítulo "Fabricación Discreta, Repetitiva y Por Procesos". Tres bloques de texto en negrita con bullets:

**Fabricación Discreta y Repetitiva**
- Materiales tangibles
- Produce unidades "discretas" (c/unidad es distinta a otras, se puede contar y los materiales son identificables): skateboards, bicicletas

**Fabricación Repetitiva**
- Un mismo producto o similar se produce repetidamente en un periodo prolongado de tiempo a una tasa relativamente constante.

**Fabricación Por procesos**
- Fabrica materiales (petróleo, pintura, bebidas) que no se fabrican en unidades individuales. Se producen en grandes cantidades y se miden en magnitudes como galones, litros, etc.

## Slide 4

Título "Fig. 1: Un Proceso de Producción Básico". Diagrama de flujo horizontal con 5 pasos alternando iconos de persona/cajas (Almacén) e iconos de persona/engranajes (Producción), conectados por flechas:

`[Almacén: Solicita producción]` → `[Producción: Autoriza producción]` → `[Almacén: Salida de materias primas]` → `[Producción: Crea producto]` → `[Almacén: Recibe productos terminados]`

Pie: "Magal and Word | Integrated Business Processes with ERP Systems | © 2011". Slide 4.

## Slide 5

Título "Datos Organizativos". Lista:
- Mandante
- Sociedad
- Centro (de fabricación)
- Almacén

## Slide 6

Título "Datos Maestros". Lista (sin resaltado):
- Listas de Materiales (LMat)
- Puesto de Trabajo
- Hojas de ruta de productos
- Maestro de materiales
- Medios auxiliares de fabricación (MAF)

## Slide 7

Título "Datos Maestros" (repetida, con flecha roja apuntando al primer ítem resaltado en rosa: "Listas de Materiales (LMat)"). Misma lista de 5 ítems que slide 6, esta vez con un recuadro rosa/flecha señalando el ítem que se va a desarrollar a continuación.

## Slide 8

Título "Lista de Materiales (LMat o BOM )". Contenido:
- También conocido como BOM (Bill Of Materials)
- Identifica los componentes que son necesarios para fabricar un material
- Un componente puede tener su propio Lmat para crear una LMat multinivel.
- Lmat se usa en
  - Planificación del material
  - Producción
  - Aprovisionamiento
  - Costeo del producto

## Slide 9

Título "Fig. 2: LMats de uno y múltiples niveles". Diagrama jerárquico (árbol) que muestra:
- Nodo raíz "Producto terminado" (recuadro superior grande, "LMat de un nivel")
- Se ramifica en 3 nodos: "Producto semielaborado" (izquierda), "Producto semielaborado" (centro), "Materia prima" (derecha)
- El "Producto semielaborado" izquierdo se ramifica en 2 "Materia prima" (formando su propia "LMat de un nivel")
- El "Producto semielaborado" central se ramifica en 1 "Materia prima" (formando otra "LMat de un nivel")

El diagrama ilustra cómo una LMat multinivel se compone de varias LMat de un nivel anidadas.

## Slide 10

Título "Fig. 3: Lista de materiales para bicicleta de turismo". Diagrama jerárquico tipo árbol organizacional:

Nodo raíz: "Bicicleta de turismo"

Se ramifica en 10 componentes de nivel 1 (con códigos):
TRWA1000/TRWA2000 (Ensamble rueda, cantidad 2), TRFR1000/TRFT2000/TRFT3000 (Cuadro turismo), DGAM1000 (Ensamble cambio de velocidad), TRSK1000 (Kit de asiento), TRHB1000 (Manubrio), PEDL1000 (Ensamble pedal), CHAN1000 (Cadena), BRKT1000 (Kit de frenos), WDOC1000 (Documento garantía), PCKG1000 (Empaque).

El nodo "Ensamble rueda" se ramifica en: TRTR1000 (Llanta turismo), TRTB1000 (Tubo turismo), TRWH1000/TRWH2000 (Rueda), HXNT1000 (Tuerca hexagonal), LWSH1000 (Arandela de seguridad), BOLT1000 (Perno de cabeza hueca).

Recuadro de texto lateral "Bicicletas de turismo":
- Bicicletas profesionales disponibles en tres colores, negro (PRTR1000), plateado (PRTR2000) y rojo (PRTR3000), dependiendo del cuadro usado.
- Bicicletas de turismo de lujo disponibles en tres colores, negro (DXTR1000), plateado (DXTR2000) y rojo (DXTR3000), dependiendo del cuadro usado.
- Cuadros de turismo disponibles en tres colores, negro (TRFR1000), plateado (TRFR2000) y rojo (TRFR3000).
- Cuadros de turismo de lujo usan un ensamble de rueda de aluminio (TRWA1000) que incluye ruedas de turismo de aluminio (TRWH1000).
- Las bicicletas de turismo profesional usan un ensamble de rueda de compuesto de carbono (TRWA2000) que incluye ruedas de compuesto de carbono (TRWH2000).

## Slide 11

Título "Fig. 4: Lista de materiales para bicicleta todo terreno". Diagrama jerárquico análogo al de Slide 10 pero para bicicleta todo terreno:

Nodo raíz: "Bicicleta todo terreno"

Ramas de nivel 1: ORWA1000 (Ensamble rueda todo terreno de aluminio), OFFR1000/OFFR2000 (Cuadro), EDGAM1000 (Ensamble cambio de velocidad), ORSK1000 (Kit de asiento todo terreno), ORHB1000 (Manubrio todo terreno), PEDL1000 (Ensamble pedal), CHAN1000 (Cadena), BRKT1000 (Kit de frenos), WDOC1000 (Documento garantía), PCKG1000 (Embalaje).

"Ensamble rueda todo terreno de aluminio" se ramifica en: ORTR1000 (Llanta todo terreno), ORTB1000 (Tubo todo terreno), ORWH1000 (Rueda todo terreno de aluminio).

Recuadro de texto "Bicicletas todo terreno":
- Bicicletas todo terreno disponibles en dos modelos - de hombre (ORMN1000) y de mujer (ORWN1000).
- Las bicicletas de hombre usan un cuadro de hombre (OFFR1000) y las de mujer usan un cuadro de mujer (OFFR2000).
- Ambas bicicletas, las de hombre y las de mujer, usan ensambles de rueda todo terreno de aluminio (ORWA1000) las que incluyen ruedas todo terreno de aluminio (ORWH1000).

## Slide 12

Título "Lista de Materiales - Cabecera". Contenido:
- Se aplica a toda la lista de materiales
- Estado: activa, inactiva
- Cantidad base: cantidad de productos que se pueden producir con los materiales especificados en la LMAT
- Utilización: fabricación, ingeniería, cálculo de costos, etc.
- Centro: cada centro puede tener una lista de materiales diferentes
- Validez: rango de fechas

## Slide 13

Título "Lista de Materiales – Posiciones". Contenido:
- Aplica para una posición específica de la Lmat
- Tipo de Posición:
  - Posición de Almacén – debe tener un maestro de material
  - Posición de no Almacén – no necesita maestro de material
  - Posición de dimensión bruta – debe especificar tamaño
  - Posición de documento – diseños de ingeniería, instrucciones adicionales
- Número de material
- Cantidad

## Slide 14

Título "Fig. 5: Estructura de una LMat". Dos paneles lado a lado.

Panel izquierdo "Cabecera" (tabla LMAT.):
| Campo | Valor |
|---|---|
| Material | DXTR1000 |
| Centro | DL00 |
| Utilización | 1 |
| Validez | Fecha |
| Status | Activo |
| Cantidad base | 1 un |

Panel derecho "Posiciones (detalle)" (tabla):
| Pos. | Tipo pos. | Material | Denominación | Ctd. |
|---|---|---|---|---|
| 0010 | L | TRWA1000 | Ensamble de rueda de turismo de aluminio | 2 |
| 0020 | L | TRFR1000 | Cuadro turismo - negro | 1 |
| 0030 | L | DGAM1000 | Ensamble de cambio de velocidad | 1 |
| 0040 | D | WDOC1000 | Documento garantía (en lugar de instrucciones de ensamble) | 1 |
| 0050 | L | CHAIN1000 | Cadena | 1 |

## Slide 15

Título "Demo 6.1 Revisión de una LMat para una bicicleta y ensamble de rueda". Texto: "Revisión de algunos de los datos incluidos en un maestro de materiales". Slide introductoria de demo, sin captura de pantalla real.

## Slide 16

Título "Datos Maestros". Misma lista de 5 ítems, con flecha roja/recuadro rosa resaltando el segundo ítem: "Puesto de Trabajo".

## Slide 17

Título "Puesto de Trabajo". Contenido:
- Lugar donde se realiza trabajo de valor agregado necesario para producer un material.
- Puede ser también una máquina o un grupo de máquinas, una línea entera de producción, un área de trabajo o una persona o grupo de personas responsables de completar operaciones en diferentes lugares del centro.

## Slide 18

Título "Fig. 6: Datos de un puesto de trabajo". Diagrama radial: nodo central "Puesto de Trabajo" (icono de persona con engranajes) conectado mediante flechas a 6 recuadros alrededor:

- **Datos básicos**: Nombre y descripción; Persona responsable; Utilización de hoja de ruta; Clave para valor prefijado
- **Capacidades**: Capacidad disponible; Clave de fórmula
- **Valores propuestos**: Clave de control; Clave de modelo; Datos de salario
- **Programación**: Base de programación; Clave de fórmula
- **Centro de coste**: Centro de costo; Claves de actividad; Clave de fórmula
- **Asignación de RRHH**: Personas; Cargos; Cualificaciones

## Slide 19

Título "Fig. 7: Ejemplo de puesto de trabajo (ensamblaje de un Boeing 757)". Fotografía en blanco y negro de un hangar industrial mostrando varios aviones Boeing 757 en distintas etapas de ensamblaje, con andamios, plataformas móviles, trabajadores y equipos alrededor.

## Slide 20

Título "Fig. 8: Planta de fabricación de GBI en Dallas". Diagrama esquemático de planta con dos zonas:

**Área de fabricación**: barra "Cinta transportadora", flecha "Flujo de trabajo" apuntando hacia la derecha, y 3 puestos de trabajo en secuencia: ASSY1000 (Ensamblaje), INSP1000 (Inspección), PACK1000 (Embalaje). Etiqueta lateral "Puestos de Trabajo" con flecha apuntando a estos 3 recuadros.

**Área de almacenamiento**: etiqueta lateral "Muelles de carga", y 4 almacenes: RM00 (Almacén de materias primas), FG00 (Almacén de productos terminados), SF00 (Almacén de productos semielaborados), MI00 (Almacén de materiales varios).

## Slide 21

Título "Fig. 9: Puestos de trabajo de GBI". Tres tarjetas de detalle:

**ASSY1000 Ensamblaje**: Centro de costo NAPR1000; Mano de obra 8 horas; Actividades: Poner materiales a disposición, Ensamblar ruedas, Ensamblar cuadro de bicicleta.

**INSP1000: Inspección**: Centro de costo NAPR1000; Mano de obra 8 horas; Máquina 8 horas; Actividad: Inspeccionar materiales.

**PACK1000: Embalaje**: Centro de costo NAPR1000; Mano de obra 8 horas; Actividades: Desensamblar bicicleta, Embalar bicicleta.

## Slide 22

Título "Demo 6.2 Revisión del puestos de trabajo de GBI". Texto: "Revisión de puestos de trabajo de GBI". Slide introductoria de demo, sin captura real.

## Slide 23

Título "Datos Maestros". Misma lista de 5 ítems, flecha roja/recuadro rosa resaltando el tercer ítem: "Hojas de ruta de productos".

## Slide 24

Título "Hojas de ruta de productos". Subtítulo: "Lista de operaciones a ejecutar para fabricar un material". Estructura jerárquica en bullets:
- Operaciones
  - Secuencia
    - Estándar
    - Alternativa
    - Paralela
- Puesto de trabajo
- Tiempo
  - Preparación, Tratamiento, Desmontaje

## Slide 25

Título "Fig. 10: Estructura de una hoja de ruta". Dos diagramas de árbol lado a lado.

Izquierda "Hoja de ruta RI": Cabecera (Status, utilización, responsable, validez) → Secuencia 1 (estándar) con Operación 1, Operación 2, ..., Operación n → Secuencia 2 (alternativa) con Operación 2, Operación 1, ..., Operación n.

Derecha "Hoja de ruta de GBI": Cabecera → Secuencia 1 (estándar) con operaciones concretas: 10 Puesta a disposición del material, 20 Fijar asiento al cuadro, 30 Fijar manubrio, ..., 80 Probar bicicleta, ..., 100 Embalar bicicleta, 110 Trasladar a almacén.

## Slide 26

Título "Fig. 11: Hoja de ruta del ensamble de rueda de turismo de lujo". Tabla:

Cabecera: "Nombre material: Ensamble de rueda de turismo de aluminio" — "Número material: TRWA 1000"

| Nº operación | Puesto de trabajo | Tiempo de preparación (min) | Tiempo de tratamiento (min) | Operación | Materiales asignados |
|---|---|---|---|---|---|
| 10 | ASSY1000 | 0 | 5 para 50 | Poner a disposición material | Llanta de turismo, tubo de turismo, rueda de turismo de aluminio, tuerca hexagonal 5mm, arandela de seguridad 5mm, perno de cabeza hueca 5x20 mm. |
| 20 | ASSY1000 | 0 | 3 por rueda | Ensamblar componentes | (mismos materiales que fila anterior) |
| 30 | ASSY1000 | 0 | 5 para 50 | Trasladar a almacén | Ensamble de rueda |

Nota al pie con fórmula: "Tiempo de mano de obra para ensamblar 50 ruedas = 160 min. (5+50*3+5)"

$$T = 5 + 50 \times 3 + 5 = 160 \text{ min}$$

## Slide 27

Título "Fig. 12: Hoja de ruta de la bicicleta de turismo de lujo". Tabla:

Cabecera: "Nombre material: Bicicleta de turismo de lujo" — "Número material: DXTR1000"

| Nº Op. | Puesto de trabajo | Prep. (min) | Tratamiento (min) | Operación | Materiales asignados |
|---|---|---|---|---|---|
| 10 | ASSY1000 | | 10 para 15 bicicletas | Poner a disposición material | Todos los materiales |
| 20 | ASSY1000 | | 1 | Fijar asiento al cuadro | Cuadro, kit de asiento |
| 30 | ASSY1000 | | 2 | Fijar manubrio | Manubrio |
| 40 | ASSY1000 | | 2 | Fijar ensamble de cambio de velocidad a la rueda trasera | Ensamble de rueda, ensamble de cambio de velocidad |
| 50 | ASSY1000 | | 5 | Fijar ruedas frontal y trasera y cadena | Ensambles de rueda, cadena |
| 60 | ASSY1000 | | 2 | Fijar frenos | Kit de frenos |
| 70 | ASSY1000 | | 2 | Fijar pedales | Ensamble de pedal |
| 80 | INSP1000 | 2 | 5 | Probar bicicleta | Bicicleta ensamblada |
| 90 | PACK1000 | | 4 | Desensamblar (quitar ruedas y cadena) | Bicicleta ensamblada |
| 100 | PACK1000 | | 4 | Embalar bicicleta (embalada individualmente) | Bicicleta desensamblada, documento de garantía, embalaje |
| 110 | PACK1000 | | 5 para 15 bicicletas | Trasladar a almacén | Bicicleta embalada |

## Slide 28

Título "Demo 6.3 Revisión de la hoja de ruta de una bicicleta y de un ensamble de rueda". Texto: "Revisión de la hoja de ruta de una bicicleta y de un ensamble de rueda". Slide introductoria de demo, sin captura real.

## Slide 29

Título "Fig. 13 Hojas de ruta y puestos de trabajo". Diagrama "Hoja de ruta" mostrando el detalle de la Operación 80 "Probar bicicleta":
- Puesto de trabajo INSP1000
- "Cap." con valores 001 y 002 conectados a "Base de programación"
- Columna "Valor prefijado": Preparación, Máquina, RRHH, Variable 1...
- Columna "Fórmula de programación" con 3 pasos: 1. Preparación (2 min.), 2. Tratamiento (5 min., 5 min.), 3. Desmontaje
- Anotaciones: "Elementos de tiempo fijo (independientes del tamaño del lote)" para Preparación; "Elementos de tiempo variable (dependientes del tamaño del lote)" para Tratamiento.

## Slide 30

Título "Asignación de componentes". Contenido:
- Especifica la relación entre una lista de materiales LMat y una hoja de ruta
- Asigna componentes (materiales) en una lista de materiales, ya sea a una ruta o a una operación específica dentro de la hoja de ruta
- Si no se asignan, supone que está asignado a la primera operación

## Slide 31

Título "Fig. 14: Asignación de Componentes". Dos diagramas conectados por una flecha.

Izquierda: "Hoja de ruta" con Op. 10, Op. 20, Op. 30; panel "LMAT." con Mat. A, Mat. B, Mat. C, donde flechas muestran Mat. A → Op. 20, y Mat. B y Mat. C → Op. 30.

Derecha: recuadro de texto "Consumo de componentes ocurre al inicio de la operación a la que se los asignó." Debajo, un diagrama de "Secuencia de operaciones" tipo línea de tiempo: Op. 10, Op. 20, Op. 30 en la parte superior, con flechas ascendentes desde Mat. A (bajo Op. 20) y Mat. B / Mat. C (bajo Op. 30), eje horizontal etiquetado "Tiempo".

## Slide 32

Título "Capacidad de producción". Contenido:
- Una medida de la cantidad de unidades de un material que un centro puede producir en un plazo determinado
- Una fuente de datos para la planificación de la producción

## Slide 33

Título "Fig. 15: Ejemplo de plan de producción de GBI". Tabla de planificación semanal (días L-V repetidos por 5 semanas, 25 columnas) con 4 filas:

| | L | M | M | J | V | (×5 semanas) |
|---|---|---|---|---|---|---|
| Producción de ruedas | 50 | 0 | 50 | 0 | 50 | ... patrón se repite |
| Stock de ruedas | 30 | 0 | 30 | 0 | 30 | ... |
| Producción de bicicletas | 10 | 15 | 10 | 15 | 10 | ... |
| Stock de bicicletas | 10 | 25 | 35 | 50 | 60 | ... acumulativo creciente hasta 310 |

Nota: el stock de bicicletas es acumulativo y termina en 310 al final de las 5 semanas mostradas.

Recuadro "Supuestos":
| Parámetro | Valor | Parámetro derivado | Valor |
|---|---|---|---|
| Número de turnos | 1 | Bicicletas por semana | 50 |
| Horas por turno | 8 | Bicicletas por año | 2500 |
| Días por semana | 5 | Ruedas por semana | 100 |
| Semanas por año | 50 | Ruedas por año | 5000 |
