---
curso: EVALFIN
titulo: 03 - Semana 1/EFP - Clase 2 - Pronóstico-1__pptx
slides: 36
fuente: 03 - Semana 1/EFP - Clase 2 - Pronóstico-1__pptx.pdf
---

Métodos de Pronóstico de la Demanda
     Evaluación Financiera de Proyectos - Semana 2
Objetivo(s) de la sesión
                           • Aplicar técnicas de pronóstico
                             cuantitativo (medias móviles y
                             regresión lineal), a partir del estudio
                             de mercado, para estimar la demanda
                             y proyectar los ingresos futuros en la
                             evaluación de proyectos.




                                                                       2
Contenido
1. Estudio de mercado.

2. Pronóstico de la demanda.

3. Método de medias móviles (promedio móvil).

4. Regresión lineal.

5. Casos de aplicación.




                                                3
1.
     Estudio de mercado




                          4
            Estudio de mercado

Análisis sistemático de las condiciones del
mercado para un bien o servicio.

Objetivo:
Entender la demanda, la competencia y las
preferencias del consumidor.

Importancia:
Base para la toma de decisiones en marketing,
producción y estrategia comercial.




                                                5
                             Análisis de la demanda de un bien o servicio

Demanda:                      Cantidad de un bien o servicio que los consumidores están dispuestos a comprar a un
                              precio determinado.




 Factores que influyen                              Métodos para estimar
                                                                                                      Proyección de la demanda
                         Precio del producto.                              Encuestas y entrevistas.                              Uso de modelos
                                                                                                                                 estadísticos (regresión,
                         Ingresos de los                                   Análisis de datos                                     series de tiempo).
                         consumidores.                                     históricos.
                                                                                                                                 Consideración de
                         Gustos y preferencias.                            Estudios de mercado                                   tendencias y
                                                                           secundarios (informes,                                estacionalidad.
                         Precios de bienes                                 estadísticas).
                         sustitutos o
                         complementarios.




                                                                                                                                                            6
           Precios y volúmenes de demanda proyectados

                                                          Proyección de volúmenes
 Determinación de precios         Supuestos de precios
                                                                de demanda

• Basado en costos (margen     • Ejemplo:                • Escenarios:
  sobre costos de                Precio =                  - optimista,
  producción).                   Costo de producción +
                                 Margen de beneficio.      - pesimista y
• Basado en la competencia
  (análisis de precios de la   • Consideración de          - realista.
  competencia).                  descuentos y            • Uso de elasticidad-precio
• Basado en el valor             promociones.
                                                           de la demanda.
  percibido (disposición a
  pagar del consumidor).



                                                                                       7
2.
     Pronóstico de la demanda




                                8
           Pronóstico de la demanda

Proceso de estimar la cantidad de un bien o
servicio que los consumidores comprarán en un
período futuro.

Objetivo:
Apoyar la planificación de producción,
inventarios, marketing y finanzas.

Importancia:
Reduce la incertidumbre en la toma de
decisiones.




                                                9
          Pronóstico de la demanda

                                Encuestas y entrevistas

                                  Juicio de expertos
               Cualitativos
                              Análisis de fuerza de ventas

                                 Estudios de mercado         ( 1 ) Promedio móvil
Métodos                            Series de tiempo           Suavización exponencial

                                                             Descomposición de series

              Cuantitativos                                  ( 2 ) Regresión lineal
                                  Métodos causales
                                                              Modelos econométricos
                               Simulación (Monte Carlo)

                                IA (Machine Learning)
                                                                                        10
3.
     Método de medias móviles
     (promedio móvil)




                                11
              Método de medias móviles (promedio móvil)

Técnica de pronóstico que estima valores futuros
utilizando el promedio de un número definido
de periodos históricos.


Sirve para:
• Pronosticar datos de corto plazo.
• Reducir la variabilidad aleatoria de la serie
  (eliminar "ruido").
• Identificar tendencias de corto plazo.




                                                          12
    Método de medias móviles (promedio móvil)

•                          Pasos:
                           • Definir el período n
                             Determinar el número de periodos históricos
                             que se utilizarán para el cálculo del promedio.
                           • Calcular el promedio móvil
                             Obtener el promedio de los últimos n valores
                             observados de la serie.
                           • Estimar el valor futuro
                             Utilizar el promedio calculado como
                             pronóstico para el siguiente periodo.
                           • Actualizar el cálculo
                             Para cada nuevo pronóstico, eliminar el dato
                             más antiguo e incorporar el más reciente.


                                                                            13
                                                                       (2) Valor estimado =
                                                          (1) Ventas                            Error = Valor
                  Ejemplo                          Año
                                                          reales
                                                                       Promedio de 2 anteriores
                                                                       (N=2)
                                                                                                absoluto de (1) – (2)

                                                   2017    524,248
     En una universidad peruana se han reco-
     pilado datos de ventas de 2017 a 2025 y       2018    577,995
     se desea estimar las ventas de 2026.                              Media móvil = 551,121.5    618,391 - 551,121.5 =
                                                   2019    618,391
     1° se decide cuantos números se van a                             (524,248 + 577,995) / 2          67,269.5
     promediar, en este caso decidimos N=2.                             Media móvil = 598,193     648,950 - 598,193 =
                                                   2020    648,950
                                                                        (577,995 + 618,391) / 2         50,757
       Ventas reales y estimadas por               2021    870,772            633,670.5                 237,102
              medias móviles
1,000,000                                          2022    936,594             759,861                  176,733
 800,000                                           2023    792,747             903,683                  110,936
 600,000                                           2024    902,211             864,671                   37,541
 400,000                   Vtas reales             2025    916,889             847,479                   69,410
 200,000                   Vtas estimadas (MM)
                                                   2026                        909,550
       0
         017 018 019 020 021 022 023 024 025 026                 Error medio = 107,107 (promedio de los errores)
        2    2   2   2   2   2   2   2   2   2

                                                                                                                   14
            Ejercicio 3.1
                                              Año    Ventas (S/. 000)
En una empresa peruana, se han recopilado     2016            550,000
los siguientes datos de ventas anuales (en    2017            590,000
miles de soles) desde el año 2016 hasta el
2025.                                         2018            620,000
                                              2019            640,000
La empresa desea estimar las ventas para el   2020            660,000
año 2026 utilizando el método de medias
                                              2021            690,000
móviles con un período N = 4.
                                              2022            720,000

Grafique las ventas y las estimaciones.       2023            710,000
                                              2024            750,000
Calcule, adicionalmente, el error promedio    2025            780,000
                                              2026


                                                                        15
                   Ejercicio 3.1 - Solución
                                                           Año    Ventas (S/. 000)   Media móvil    Error

      Ventas reales y estimadas por medias                 2016            550,000
                     móviles                               2017            590,000
1,000,000
                                                           2018            620,000
 800,000                                                   2019            640,000

 600,000                                                   2020            660,000       600,000   60,000
                                                           2021            690,000       627,500   62,500
 400,000                           Vtas reales
                                   Vtas estimadas (MM)     2022            720,000       652,500   67,500
 200,000
                                                           2023            710,000       677,500   32,500
       0                                                   2024            750,000       695,000   55,000
            20162017201820192020202120222023202420252026
                                                           2025            780,000       717,500   62,500
   Error promedio 56,667.                                  2026                          740,000


                                                                                                      16
            Ejercicio 3.2
                                                          Ventas
                                                 Año
                                                        (S/. 000)
Una empresa ha recopilado los siguientes         2014    450,000
datos de ventas anuales (en miles de soles)      2015   470,000
desde el año 2014 hasta el 2025. Desean          2016   500,000
estimar las ventas para el año 2026 utilizando
                                                 2017   530,000
el método de medias móviles con un período
N = 3 y compararlo con un período N = 5.         2018   560,000
                                                 2019   600,000
¿Cuál es más confiable? N = 3 o N = 5.           2020   650,000
                                                 2021   700,000

Grafique las ventas y las estimaciones.          2022   750,000
                                                 2023   800,000
                                                 2024   850,000
                                                 2025   900,000
                                                 2026

                                                                    17
                   Ejercicio 3.2 - Solución
                                                                        Ventas    Media     Media      Error    Error
                                                               Año
      Ventas reales y estimadas por medias                            (S/. 000) móvil N=3 móvil N=5     N=3      N=5
                     móviles                                   2014    450,000
1,000,000
                                                               2015   470,000
 800,000                                                       2016   500,000
 600,000                                                       2017   530,000    473,333              56,667
                                                               2018   560,000    500,000              60,000
 400,000                                 Ventas
                                                               2019   600,000    530,000   502,000    70,000   98,000
                                         Media móvil N=3
 200,000                                 Media móvil N=5       2020   650,000    563,333   532,000    86,667 118,000
       0                                                       2021   700,000    603,333   568,000    96,667 132,000
         014 015 016 017 018 019 020 021 022 023 024 025 026   2022   750,000    650,000   608,000 100,000 142,000
        2 2 2 2 2 2 2 2 2 2 2 2 2

     Comparamos los errores promedio de ambos                  2023   800,000    700,000   652,000 100,000 148,000
     N desde 2019, año desde el cual disponemos                2024   850,000    750,000   700,000 100,000 150,000
     de los errores para ambos.                                2025   900,000    800,000   750,000 100,000 150,000
     Error promedio N=3: 93,333.      Mejor                    2026              850,000   800,000
     Error promedio N=5: 134,000.
                                                                                                                  18
4.
     Regresión lineal




                        19
            Regresión lineal

Técnicas estadísticas utilizadas para estimar        Aplicaciones:
valores futuros estableciendo una relación lineal
                                                     • Economía y Finanzas: para prever el
entre una variable dependiente y una o más
                                                       comportamiento de variables económicas,
variables independientes a partir de datos
                                                       como la inflación o el crecimiento del PIB, en
históricos.
                                                       función de factores como la tasa de interés o
                                                       la inversión.
Sirve para:                                          • Marketing: para determinar cómo los cambios
• Pronosticar datos de corto y mediano plazo.          en el precio de un producto afectan las ventas.
• Identificar tendencias en los datos.               • Ingeniería: para analizar la relación entre la
• Analizar la relación entre variables relevantes.     temperatura y la resistencia de materiales.
                                                     • Medicina: para entender la relación entre
                                                       dosis de un medicamento y su efectividad o
                                                       efectos secundarios.


                                                                                                        20

                 Pasos del proceso de regresión lineal

                            Recopilar y           Estimar la            Evaluar el
       Definir las                                                                           Realizar la
                           organizar los         ecuación de            ajuste del
       variables                                                                             proyección
                              datos               regresión              modelo
• Identificar la      • Utilizar datos     • Calcular la recta   • Analizar            • Utilizar la
  variable              históricos           que mejor ajusta      indicadores           ecuación
  independiente         consistentes y       los datos,            como el               estimada para
  (X) y la variable     relevantes para      generalmente          coeficiente de        predecir valores
  dependiente (Y)       el análisis.         mediante el           determinación y       futuros de la
  que se desea                               método de             el coeficiente de     variable
  estimar.                                   mínimos               correlación.          dependiente.
                                             cuadrados.




                                                                                                        21
            Regresión lineal simple

La relación entre las variables se expresa mediante
la ecuación:

                   Y=a+bX
Donde:
Y variable dependiente (se intenta predecir).
X variable independiente (se utiliza para hacer la
  predicción).

a intersección con el eje Y cuando X es cero.
  (intercepto o constante).
b pendiente o inclinación de la recta (indica el
  cambio en Y por cada unidad de cambio en X).

                                                      22
https://www.youtube.com/watch?v=VE19S9iWuWk (hasta el minuto 3:12)   23
           Ejercicio 4.1

Se cuenta con la siguiente información sobre
                                                  Año    Ventas en miles
ventas anuales.
                                                  2019         685
Utilizando el método de regresión lineal estime
                                                  2020         698
las ventas para el año 2026.
                                                  2021         710
                                                  2022         735
                                                  2023         745
                                                  2024         798
                                                  2025         821
                                                  2026


                                                                           24
                        Ejercicio 4.1 - Solución

                          Gráfico de Ventas en miles                    Año    Ventas en miles
                  850
                                                                        2019         685
                  800    f(x) = 22.9642857142857 x − 45692.0714285714   2020         698
                         R² = 0.943913007744009



Ventas en miles
                  750                                                   2021         710
                                                                        2022         735
                  700
                                                                        2023         745
                  650
                                                                        2024         798
                  600
                   2018 2019 2020 2021 2022 2023 2024 2025 2026         2025         821
                                        Años
                                                                        2026         833


                                                                                                 25
           Ejercicio 4.2

Una empresa desea entender cómo el gasto en       Muestre lo siguiente:
publicidad afecta las ventas mensuales de su
producto. Se muestran los datos recopilados de    1. Diagrama de dispersión.
los últimos 6 meses:
                                                  2. Ecuación de la recta de ajuste.

  Gasto en Publicidad            Ventas           3. Coeficiente de determinación.
 (en miles de dólares)   (en miles de unidades)
            2                      30             4. Coeficiente de correlación.
            4                      40             5. Calcule las ventas para un gasto de
            6                      50                publicidad de 15 mil dólares.
            8                      65
           10                      80
           12                      95



                                                                                           26
           Ejercicio 4.2 - Solución

       Ventas (en miles de unidades)
100                                                   1. Diagrama de dispersión.
           f(x) = 6.57142857142857 x + 14             2. Ecuación de la recta de ajuste. Y = 14 + 6.57 X
 80        R² = 0.991100702576112
                                                      3. Coeficiente de determinación. 99.11%
 60                                                   4. Coeficiente de correlación.    99.55%
                                                                                        (relación direc.)
 40                                                   5. Calcule las ventas para un gasto de
                                                         publicidad de 15 mil dólares. 112.55

 20


  0
   0   2        4       6      8      10    12   14


                                                                                                 27
           Ejercicio 4.3

Una tienda de electrónica quiere analizar cómo    Muestre lo siguiente:
el precio de un producto afecta la demanda
(cantidad vendida). Se muestran los datos de      1. Diagrama de dispersión.
ventas y precios correspondientes a los últimos
                                                  2. Ecuación de la recta de ajuste.
5 meses:
                                                  3. Coeficiente de determinación.
 Precio del producto      Demanda
    (en dólares)        (en unidades)             4. Coeficiente de correlación.
         100                 250                  5. Calcule la demanda si la tienda decide
         150                 200                     fijar el precio en 180 dólares.
         200                 150
         250                 120
         300                 100


                                                                                              28
                  Ejercicio 4.3 - Solución

                     Curva de Demanda
           300                                            1. Diagrama de dispersión.
           250                                            2. Ecuación de la recta de ajuste. Y = 316 - 0.76 X
                     f(x) = − 0.76 x + 316
           200       R² = 0.967828418230563               3. Coeficiente de determinación. 96.78%

Cantidad
           150                                            4. Coeficiente de correlación.     -98.38%
                                                                                             (relación inver.)
           100                                            5. Calcule la demanda si la tienda decide
                                                             fijar el precio en 180 dólares. 179.2
            50

             0
             50    100   150     200    250   300   350
                               Precio


                                                                                                      29
5.
     Casos de aplicación




                           30
                                                         Ventas
                                                 Año
            Ejercicio 5.1                        2018
                                                        (S/. 000)
                                                        550,000
                                                 2019   570,000
La empresa ABC S.A., ha recopilado datos de      2020   590,000
sus ventas anuales (en miles de soles) desde     2021   610,000
el año 2018 hasta el 2025. La empresa ahora
                                                 2022   630,000
se enfrenta al reto de estimar las ventas para
los próximos 7 años (2026 a 2032) utilizando     2023   650,000
el método de medias móviles con un período       2024   670,000
de N=4.                                          2025   690,000
                                                 2026
Grafique las ventas y las estimaciones.          2027
                                                 2028
                                                 2029
                                                 2030
                                                 2031
                                                 2032


                                                                    31
                                                                             Ventas     Media móvil
                                                                     Año                              Error
                Ejercicio 5.1 - Solución                             2018
                                                                            (S/. 000)
                                                                            550,000
                                                                                           N=4


                                                                     2019   570,000
      Ventas reales y estimadas por medias móviles                   2020   590,000
800,000                                                              2021   610,000
                                                                     2022   630,000       580,000     50,000
600,000                                                              2023   650,000       600,000     50,000
                                                                     2024   670,000       620,000     50,000
400,000                                                              2025   690,000       640,000     50,000
                                                 Ventas              2026   660,000       660,000      NA
                                                 Media móvil
200,000                                                              2027   667,500       667,500      NA
                                                                     2028   671,875       671,875      0A
     0                                                               2029   672,344       672,344
        18 019 020 021 022 023 024 025 026 027 028 029 030 031 032
                                                                                                       NA
       0
      2 2 2 2 2 2 2 2 2 2 2 2 2 2 2                                  2030   667,930       667,930      NA
                                                                     2031   669,912       669,912      NA
   Error promedio N=4: 50,000.
                                                                     2032   670,515       670,515      NA

                                                                                                              32
            Ejercicio 5.2

La empresa Green Garden SAC está evaluando expandir su área de cultivo de paltas y le solicita la
elaboración de un pronóstico que le permita conocer el crecimiento del consumo per cápita en
EEUU para la temporada 2026, para lo cual tiene a disposición el siguiente reporte:

Informe del USDA ERS sobre Suministro y Utilización de Vegetales Frescos
                    Suministro                            Utilización
                                                                                       Consumo de
 Año                                                                  Consumo de
       Producción Importaciones     Total Exportaciones    Doméstico                     paltas (kg)
                                                                     paltas (libras)
2018        527.6             1.9   529.5          50.7       478.8             2.08           0.94    Los datos están
2019        383.4             1.5   384.9          24.9         360             1.55           0.70    en millones de
2020        458.0             3.4   461.4          28.9       432.5             1.85           0.84    libras 1 Kg =
2021        553.0             7.3   560.3          41.9       518.4             2.19           0.99
                                                                                                       0.453592 libras
2022        457.0             3.7   460.7          24.1       436.6             1.83           0.83
2023        369.4            15.8   385.2          22.6       362.6             1.51           0.68
2024        614.0             4.0   618.0          47.2       570.8             2.35           1.07
2025        414.0            12.5   426.5          38.8       387.7             1.58           0.72

                                                                                                                33
            Ejercicio 5.2

Muestre lo siguiente:

1. Ecuación de la recta de ajuste.


2. Coeficiente de determinación.


3. Coeficiente de correlación.


4. Consumo per cápita de paltas
   (en Kg) en EEUU para la temporada 2026.




                                             34
            Ejercicio 5.2 - Solución

                                                         Consumo de paltas (kg)
                                             1.20
1. Ecuación de la recta de ajuste.
   Y = 10.453 - 0.0048 X
                                             1.00
2. Coeficiente de determinación.
                                             0.80   f(x) = − 0.0047519161904762 x + 10.4530816390476
   0.66%                                            R² = 0.00663288554503749
3. Coeficiente de correlación.               0.60
   -8.12% (relación inversa)
                                             0.40
4. Consumo per cápita de paltas
   (en Kg) en EEUU para la temporada 2026.
                                             0.20
   0.73 kg
                                             0.00
                                               2017 2018 2019 2020 2021 2022 2023 2024 2025 2026


                                                                                               35
Métodos de Pronóstico de la Demanda
     Evaluación Financiera de Proyectos - Semana 2

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
