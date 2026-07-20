---
curso: FUNDOPS
titulo: F5-S6 Cuello de Botella y Dimensionamiento (Version2)
slides: 35
fuente: F5-S6 Cuello de Botella y Dimensionamiento (Version2).pdf
---

FUNDAMENTOS DE OPERACIONES
Semana 6 - Dimensionamiento de Operaciones
Índice:

1. Cuello de Botella
2. Dimensionamiento de Operaciones
3. Criterio Económico para el
  dimensionamiento
Objetivos:

Al finalizar esta sesión, deberás ser capaz
de:

1. Identificar y analizar cuellos de botellas
  en las operaciones.
2. Determinar la capacidad productiva de
  una operación por criterio económico.
3. Calcular la eficiencia, aprovechamiento
  de material y costos de producción.
Cuello de Botella
                  PRODUCCIÓN POR PRODUCTO

Cuando nos enfrentamos a una distribución por producto, la capacidad queda determinada por
el CUELLO DE BOTELLA de la línea. Ejemplo: La capacidad de la línea está determinada por la máquina 3.




            P1                      P2                      P3                        P4


           0.5’                     1’                      2’                        1’                   T. Unitario

       120 und/hr               60 und/hr               30 und/hr               60 und/hr                  Flow Rate




                                                                          FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
                   PRODUCCIÓN POR PRODUCTO

Sin embargo, existe un factor importante a considerar; EL NÚMERO DE MÁQUINAS de cada tipo que existen
en la línea puede hacer variar el cuello de botella y por lo tanto la capacidad.


            M1                        M2                 M3    M3      M3             M4        M4


             P1                       P2                       P3                          P4


            0.5’                      1’                        2’                         1’              T. Unitario x maq

             1                         1                        3                          2                    C. Máquinas

        120 und/hr                60 und/hr                90 und/hr                 120 und/hr                 Flow Rate




                                                                               FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
                   PRODUCCIÓN POR PROCESO

Cuando nos enfrentamos a una distribución por proceso, la pregunta es ¿Cuál es la capacidad de producción
de cada sección?, podríamos pensar en determinar la capacidad en función de cada producto pero tendríamos
tantas capacidades como productos se fabriquen.

           P1                     P2                     P3                        P4

           0.5’                    1’                     2’                        1’                   T. Unitario
       120 und/hr              60 und/hr              30 und/hr               60 und/hr                  Flow Rate

           0.25’                   1’                     2.5’                       2’                   T. Unitario
        240 und/hr              60 und/hr              15 und/hr               30 und/hr                  Flow Rate

            1’                     1’                     1’                         2’                   T. Unitario
        60 und/hr               60 und/hr              60 und/hr               30 und/hr                  Flow Rate

                                                                        FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
                         PRODUCCIÓN POR PROCESO

    Lo más aconsejable es expresar la capacidad en función del MIX de producción de la sección, estableciendo
    para ello equivalencias.
                         P1                        P2                        P3                       P4

                        0.5’                       1’                        2’                       1’                   T. Unitario

                        0.25’                      1’                       2.5’                      2’                   T. Unitario

                         1’                        1’                        1’                       2’                   T. Unitario

                        0.5’                       1’                        2’                      1.3’                  T. Unitario

                    120 und/hr                 60 und/hr                30 und/hr                46 und/hr                 Flow Rate
Para el proceso P1:
El tiempo unitario se obtiene de la siguiente forma (70% x 0.5 min) + (20% x 0.25min) + (10% x 1 min) = 0.5 min
y con esto se obtiene 120 unid/ hora
                                                                                            FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
Dimensionamiento
de Operaciones
 DIMENSIONAMIENTO DE OPERACIONES


●¿Cuál debe ser el espacio comercial de mi tienda?
●¿Cuántos agentes bancarios debería tener mi agencia?
●¿Cuánto personal de enfermería debería atender en la sala de emergencias?


Una forma estandarizada de verlo:
Capacidad máxima de procesamiento de productos en una planta


Unidades: productos u órdenes por unidad de tiempo




                                                             FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
  CRITERIOS DE DIMENSIONAMIENTO


Definir cuál debería ser la capacidad productiva de una operación.

1. Criterio económico: escoger la alternativa que minimiza el costo medio unitario
   o el valor presente del proyecto máximo.

1. Criterio de servicio: escoger aquella que brinda un nivel de servicio aceptable




                                                        FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
Criterio
Económico
                           CRITERIOS ECONÓMICO

1. Economías de escala a corto plazo

          Economías de escala
          - Utilización de activos / menos cambios (set-up)
          - Efectos de aprendizaje (velocidad, calidad)
          - Se diluyen los costos fijos


                  Costo Unitario


                  Promedio

         Costo
         Mínimo

                         0
                                   Velocidad: Trabajos / hora



                                                                FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
                        CRITERIOS ECONÓMICO
- Dis-economías de escala
- Búsqueda toma más tiempo
- Tasa mayor de fallas & ausentismo
- Errores de calidad
- Trabajo en horas extras
- Trabajo tercerizado
- Ineficiencia en comunicación (burocracia)


               Costo Unitario


               Promedio

      Costo
      Mínimo

                      0
                                Velocidad: Trabajos / hora



                                                             FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
RELACIONES DE COSTOS

      El costo marginal es el costo incremental necesario para
      producir una unidad adicional.




      Asumiendo que son variables derivables,
      se tiene que el costo promedio unitario
      es mínimo cuando este es igual .



                                     FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
RELACIONES DE COSTOS (CORTO PLAZO)




                          FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
   RELACIONES DE COSTOS (LARGO PLAZO)
● Opciones diferentes para diferentes requerimientos de demanda
                                                                                                                   Curva de largo plazo
                                                                                      Decisión óptima              de economías




                                         operación
                                          reducida
                                                                                          operación




            Costo unitario promedio
                                                              operación
                                                               mediana                   muy grande
                                                                          operación
                                                                           grande




                                      Velocidad: Trabajos / hora



                                                                                             FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
          EJEMPLO DE DIMENSIONAMIENTO
Tenemos una empresa que fabrica 3 valvulas: X106, X107 y X108.
Su principal insumo es el acero galvanizado y tiene 3 potenciales dimensiones de planta
Con diferente tamaño.

Para una determinada demanda:
1. ¿Qué dimensión de planta sería elegida?
2. ¿Debería trabajarse en primer turno solamente o implementar horas extras y segundos turnos?




              Planta                        Planta                         Planta
           Pequeña A                     Mediana B                       Grande C
         Semi-automática               Semi-automática                Semi-automática


                                                                   FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
           ANÁLISIS DE CUELLO DE BOTELLA
1. Definir lotes promedio




2. Analizar tasa de producción por paso (aproximado)




3. Identificar cuello de botella (para j sistemas en serie o paralelo)




                                                                         FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
          ANÁLISIS DE CUELLO DE BOTELLA
Ejemplo, 3 productos en metal mecánica

       Productos         Demanda anual      Tamaño de Lotes
         X105                 300,000           8,000
         X106                 95,000            5,000
         X107                 145,000           6,000


Además, se tiene el siguiente proceso

                 Habilitado
                                         Armado               Soldado   Pintado
                De planchas




                                          Fabricación
                                         de accesorios


                                                                         FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2

          ANÁLISIS DE CUELLO DE BOTELLA
y los siguientes tiempos de ejecución por etapa




                                                  FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
          ANÁLISIS DE CUELLO DE BOTELLA
1. Estimar lotes de producción promedio
2. Identificar cuellos de botella y capacidad máxima productiva por planta.




                                                                    FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
          ANÁLISIS DE CUELLO DE BOTELLA
1. Estimar lotes de producción promedio
2. Identificar cuellos de botella y capacidad máxima productiva por planta.




                                                                    FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
          ANÁLISIS DE CUELLO DE BOTELLA
1. Estimar lotes de producción promedio
2. Identificar cuellos de botella y capacidad máxima productiva por planta.




                                                                   FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
EFICIENCIA Y APROVECHAMIENTO DE MATERIAL


                                                                     Cap. Efectiva / Cap. Diseño



                                                       (Productos buenos)


                                                       (Toda la producción)


      Notas:
      1. Los valores permitidos de eficiencia y aprovechamiento van de 0 a 100%.
      2. La condición se puede referir a trabajar en segundo turno por ejemplo en horas extras.
      3. La medida de aprovechamiento puede incluir problemas sea por calidad (material descartado
      por defectos) o eficiencia en el aprovechamiento del material.




                                                                          FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
 ESTIMACIÓN DE LA PRODUCCIÓN MÁXIMA




*La producción máxima se debe estimar para las horas disponibles para el 1er, 2do turno
según corresponda.




                                                                FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
                        ANÁLISIS DE EFICIENCIA
Ejemplo, 3 productos en metal mecánica

       Productos         Demanda anual      Tamaño de Lotes
         X105                 300,000           8,000
         X106                 95,000            5,000
         X107                 145,000           6,000


Además, se tiene el siguiente proceso

                 Habilitado
                                         Armado               Soldado   Pintado
                De planchas




                                          Fabricación
                                         de accesorios


                                                                         FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
               LÓGICA DE USO DE CAPACIDAD

                                         Se usa primero la capacidad del turno más barato,
                                         luego se incluyen los restantes.

                                         Puede ser más barato obviar horas extras y usar capacidad
                                         De 2do turno primero.

Capacidad                                        Supuesto:
de 1er turno


                Capacidad                        - Pagamos a destajo o pagamos solo las horas
                En horas extras
                                                 Horas trabajadas en cada turno.

                                                 - Por ejemplo: si se trabajan 1.5 hr de 8 horas
                                  Capacidad       de segundo turno, puede ser equivalente
                                  de 2do turno   A trabajar 1.5/8 x 24 días laborales = 3.93 días


                                                                      FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
     LÓGICA DE USO DE CAPACIDAD
                                                          *Nota: Aquí se asume que se puede
Sí      ¿Demanda < Capacidad        No                    Trabajar horas extras en turnos a destajo.
          Máxima 1 er tuno?
                                                          No se cobra por bloque. Se asume que se
                                                          puede producir parcialmente por turnos.

                                                                     No
                               ¿ Demanda < Capacidad
                    Sí         Máxima 1 er tuno + Horas
                                       Extras?




                                                            ¿ Demanda < Capacidad               No
                                    Sí
                                                            Máxima 1er tuno + Horas
                                                               Extras +2do turno?




                                                                  FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
                     CRITERIO ECONÓMICO

Costo Total de Producción = Costo de Mano de Obra Directa
                          + Costo de Materiales
                          + Costo de Servicios y Administración
                          + Costo de Implementación de 2do turno…

Costo de Producción Unitario = Costo Total de Producción / Producción Total

Costo de Mano de Obra Directa Horas Extras =
Número de Horas extras Requeridas x (Costo por Hora) x (1+ Factor Costo Laboral) x
(1+Suplemento Hora Extra)


  Costo laboral incluye gratificaciones, vacaciones, seguros sociales:
  https://excelnoconvencional.com/costos-laborales-peru-comparado-por-regimen-en-excel/



                                                                  FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
Datos de Eficiencia y Aprovechamiento




                             FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
Datos de Costos




                  FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
Solución




           FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2
Solución




           FUNDAMENTOS DE OPERACIONES / Semana 6 / Ciclo 2024-2

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
