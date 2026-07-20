---
curso: FUNDOPS
titulo: Administración de Operaciones, Producción y Cadena de Suministros - Cap. 5
slides: 23
fuente: Administración de Operaciones, Producción y Cadena de Suministros - Cap. 5.pdf
---

capítulo
ADMINISTRACIÓN
      ESTRATÉGICA
      DE LA CAPACIDAD
  121   Las compañías farmacéuticas afrontan desafiantes
        decisiones de capacidad

  122   Administración de la capacidad operativa
                                                                           Definición de capacidad
                                               Definición de planeación estratégica de la capacidad


  124   Conceptos de la planeación de la capacidad
           Economías y deseconomías de escala                Definición de mejor nivel de operación
           La curva de aprendizaje                                Definición de índice de utilización
           El punto donde las economías de escala                                   de la capacidad
               se cruzan con la curva de aprendizaje         Definición de enfoque en la capacidad
           Enfoque en la capacidad                             Definición de economías de alcance
           Flexibilidad de la capacidad

  127   Planeación de la capacidad
           Consideraciones para aumentar la capacidad           Definición de colchón de capacidad
           Cómo determinar la capacidad que se requerirá
           Los árboles de decisión utilizados para evaluar
              las alternativas para la capacidad

  133   Planeación de la capacidad en los servicios
           Planeación de la capacidad en los servicios o en la manufactura
           Utilización de la capacidad y calidad de los servicios

  134   Conclusión

  139   Caso: Shouldice Hospital. Un corte superior
5        LAS COMPAÑÍAS FARMACÉUTICAS
         AFRONTAN DESAFIANTES DECISIONES
         DE CAPACIDAD


             L
                    a toma de decisiones con respecto a la capacidad de producción en la in-
                    dustria farmacéutica es muy compleja debido a las diversas opciones que
                    afrontan las compañías. Se trata de una apuesta costosa en razón de que se
              requiere mucho capital para las instalaciones fabriles y del costo de oportunidad
               que representa restringir la inversión en otros proyectos. Piense en un nuevo
                producto biotecnológico que está en la fase II (o sea, el segundo paso de los
                tres que se requieren para demostrar que el producto es seguro) y que tiene
                 un enorme potencial de ventas. La compañía debía asegurar la capacidad en
                  seguida, pero no estaba segura de cuánta debía obtener. La incertidumbre en
                  torno a problemas de infracción de patentes, la capacidad de marketing de la
                   organización y la respuesta de los competidores significaban que hubiera una
                   banda de variación de 600% en las proyecciones de ventas y se había estima-
                   do que la probabilidad del lanzamiento de dichos productos era tan sólo de
                    45%. Parecía una apuesta de 200 millones de euros.




                  Dado lo anterior, ¿cómo manejó este problema el despacho de asesores que
              trabajaba con la compañía de biotecnología? Recurrió, precisamente, a los instru-
             mentos que se explican en este capítulo y consideró:
            • ¿Cuál era el valor esperado del medicamento considerando distintos escenarios
           de suministro? ¿Qué ocurriría si la capacidad de producción resultara limitada?
          • ¿Cuál es el rendimiento sobre la inversión que se espera para diferentes opciones
        de producción?
       • ¿Es más conveniente “asaltar” (compartir) la capacidad de otro producto o tener una
      capacidad con un límite fijo?
    Estos desafiantes problemas son atacados en los niveles altos de la empresa.→
122                           sección 2     PROCESOS


                             Las decisiones de invertir en capacidad de manufactura y servicios son muy complejas. Considere algu-
                             nas de las difíciles preguntas que se deben plantear:
                                 • ¿Cuánto tiempo tardaría en entrar en funcionamiento la nueva capacidad? ¿Encaja con el tiempo
                                     que se tardaría en desarrollar un nuevo producto?
                                 • ¿Cuáles serían las repercusiones de no contar con suficiente capacidad para un producto promisorio?
                                 • ¿La empresa debe utilizar a fabricantes por contrato? ¿Cuánto cobrará un excelente fabricante por
                                     contrato por ofrecer flexibilidad en el volumen de producción?
                             En este capítulo se analizan estas difíciles decisiones estratégicas sobre la capacidad. Se inicia con la
                             explicación de la esencia de la capacidad desde la perspectiva de la AOS.



           ADMINISTRACIÓN DE LA CAPACIDAD OPERATIVA
Capacidad                    Un diccionario define capacidad como “la facultad para tener, recibir, almacenar o dar cabida”. En los
                             negocios, en un sentido general, se suele considerar como la cantidad de producción que un sistema es
                             capaz de generar durante un periodo específico. En el contexto de los servicios, esto se referiría al núme-
                             ro de clientes que se pueden atender entre las 12 a.m. y la 1 p.m. En las manufacturas se podría referir al
                             número de automóviles que se pueden producir en un solo turno.
                                 Cuando los gerentes de operaciones piensan en la capacidad deben considerar los insumos de re-
                             cursos y los productos fabricados. Esto se debe a que, para efectos de planeación, la capacidad real (o
                             efectiva) depende de lo que se piense producir. Por ejemplo, una empresa que fabrica múltiples productos
        Servicio             inevitablemente producirá más de una clase de ellos que de otra con una cantidad determinada de recur-
                             sos. Por lo tanto, aun cuando los gerentes de una fábrica de automóviles declaren que sus instalaciones
                             tienen 6 000 horas hombre disponibles al año, también están pensando que las pueden usar para fabricar
                             150 000 modelos de dos puertas o 120 000 modelos de cuatro puertas (o alguna mezcla de estos dos mo-
                             delos). Ello refleja que saben lo que sus insumos de tecnología y de fuerza de trabajo pueden producir y
                             conocen la mezcla de productos que exigirán a estos recursos.
                                 El punto de vista de la administración de operaciones también hace hincapié en la dimensión de la
                             capacidad referente al tiempo. Es decir, la capacidad también se debe plantear con relación a un periodo
                             dado. La diferencia que se suele marcar entre la planeación para el largo, el mediano o el corto plazo es
                             prueba de lo anterior. (Véase el recuadro “Horizontes de tiempo para la planeación de la capacidad”.)
                                 Por último, la planeación de la capacidad misma tiene diferentes significados para las personas que
      Interfuncional         están en distintos niveles de la jerarquía administrativa de las operaciones. El vicepresidente de produc-
                             ción está interesado en la capacidad agregada de todas las fábricas de la empresa. Su interés se refiere
                             principalmente a los recursos financieros que se necesitan para sostener a las fábricas. Usted estudiará
                             este proceso cuando cubra los presupuestos de capital en su curso de finanzas.
                                 Sin bien no existe el puesto de “gerente de capacidad”, sí hay varios puestos administrativos que se en-
                             cargan de que la capacidad se utilice de forma efectiva. Capacidad es un término relativo y, en el contexto
                             de la administración de operaciones, se podría definir como la cantidad de recursos disponibles que se
                             requerirán para la producción, dentro de un periodo concreto. Nótese que esta definición no hace dife-



        HORIZONTES DE TIEMPO PARA LA PLANEACIÓN DE LA CAPACIDAD
            Por lo general, se considera que la planeación de la capacidad   vas como la contratación, los recortes de personal, las nuevas
            se refiere a tres periodos.                                      herramientas, la adquisición de equipamiento menor y la sub-
                                                                             contratación pueden alterar la capacidad.
            Largo plazo —más de un año—. Cuando se requiere de mu-
            cho tiempo para adquirir o deshacerse de los recursos para       Corto plazo —menos de un mes—. Está ligado al proceso de
            la producción (como edificios, equipamiento o instalaciones),    los programas diarios o semanales e implica efectuar ajustes
            entonces la planeación de la capacidad a largo plazo requiere    para que no haya variación entre la producción planeada y la
            de la participación y la autorización de la alta gerencia.       real. Incluye alternativas como horas extra, transferencias de
                                                                             personal y otras rutas para la producción.
            Mediano plazo —planes mensuales o trimestrales que caben
            dentro de los próximos 6 a 18 meses—. En este caso, alternati-
                                             ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD           capítulo 5                             123

                                                                                                                Jelly Belly Candy Company,
                                                                                                                con domicilio en Fairfield,
                                                                                                                California, produce 100 000
                                                                                                                libras de gomitas de dulce al
                                                                                                                día, alrededor de 347 gomitas
                                                                                                                por segundo. Durante su
                                                                                                                producción, las gomitas
                                                                                                                tardan entre 7 y 21 días para
                                                                                                                curarse en estos recipientes.




rencia alguna entre el uso eficiente o ineficiente de la capacidad. En este sentido, es congruente con lo que
la oficina federal de Estados Unidos, Bureau of Economic Analysis, define como capacidad práctica máxi-
ma en sus encuestas: “La producción generada dentro de un horario normal de turnos por día y de días por
semana para las operaciones, incluyendo el costo excesivo por el uso ineficiente de las instalaciones”.1
    El objetivo de la planeación estratégica de la capacidad es ofrecer un enfoque para determinar el           Planeación estratégica
nivel general de la capacidad de los recursos de capital intensivo (el tamaño de las instalaciones, el equi-    de la capacidad
pamiento y la fuerza de trabajo completa) que apoye mejor la estrategia competitiva de la compañía a
largo plazo. El nivel de capacidad que se elija tiene repercusiones críticas en el índice de respuesta de la
empresa, la estructura de sus costos, sus políticas de inventario y los administradores y personal de apoyo
que requiere. Si la capacidad no es adecuada, la compañía podría perder clientes en razón de un servicio
lento o de que permite que los competidores entren al mercado. Si la capacidad es excesiva, la compañía
tal vez se vería obligada a bajar los precios para estimular la demanda, a subutilizar su fuerza de trabajo,
a llevar un inventario excesivo o a buscar productos adicionales, menos rentables, para permanecer en
los negocios.



                                                                                                                Las instalaciones, el
                                                                                                                equipo, los métodos de
                                                                                                                producción, la mano de obra
                                                                                                                y los suministros afectan la
                                                                                                                capacidad de producción.
                                                                                                                Además, la capacidad de
                                                                                                                esta fábrica de jugo de
                                                                                                                naranja se debe administrar
                                                                                                                considerando los efectos
                                                                                                                que las estaciones del año
                                                                                                                tienen en el abasto de
                                                                                                                recursos y en la demanda de
                                                                                                                los clientes.
124                     sección 2     PROCESOS



          CONCEPTOS DE LA PLANEACIÓN DE LA CAPACIDAD
                        El término capacidad implica el índice de producción que se puede alcanzar, por ejemplo, 300 automó-
                        viles por día, pero no dice nada de cuánto tiempo será posible sostener ese índice. Por lo tanto, no se sabe
                        si esos 300 autos por día se refieren al máximo alcanzado un día o al promedio de seis meses. A efecto
Mejor nivel de          de evitar este problema, se usa el concepto del mejor nivel de operación. Se trata del nivel de capacidad
operación               para el que se ha diseñado el proceso y, por lo mismo, se refiere al volumen de producción en el cual se
                        minimiza el costo promedio por unidad. Es difícil determinar este mínimo porque implica un complejo
                        análisis entre la asignación de los costos para gastos fijos y el costo de las horas extra, el desgaste del
                        equipamiento, los índices de defectos y otros costos.
Índice de utilización       Una medida muy importante es el índice de utilización de la capacidad, el cual revela qué tan cerca
de la capacidad         se encuentra la empresa del mejor punto de operación:
                                                                                           Capacidad utilizada
                                              Índice de utilización de la capacidad =
                                                                                         Mejor nivel de operación

                        Por ejemplo, si el mejor nivel de operación de la planta fuera de 500 automóviles por día y si estuviera
                        operando actualmente 480 automóviles por día, entonces el índice de utilización de la capacidad sería
                        96%.
                                                                                          480
                                               Índice de utilización de la capacidad =           = 0.96 o 96%
                                                                                           500

                        El índice de utilización de la capacidad se expresa como porcentaje y requiere que el numerador y el de-
                        nominador estén medidos en unidades y periodos iguales (como horas máquina/día, barriles de petróleo/
                        día, dólares de producto/día).


                        ECONOMÍAS Y DESECONOMÍAS DE ESCALA
                        La noción básica de las economías de escala dice que a medida que una planta crece y su volumen in-
                        crementa, el costo promedio por unidad de producto va bajando. En parte, esto se debe a que el costo de
                        operación y el del capital disminuye, porque por lo general no cuesta el doble comprar u operar una pieza
                        de equipo que tiene el doble de capacidad que otra. Las plantas también obtienen eficiencias cuando
                        llegan a un tamaño lo bastante grande como para utilizar plenamente los recursos dedicados para tareas
                        como el manejo de materiales, el equipo de cómputo y el personal administrativo de apoyo.
                            En algún punto, el tamaño de la planta resulta demasiado grande y las deseconomías de escala se
                        vuelven un problema. Estas deseconomías se pueden presentar de diferentes maneras. Por ejemplo, a fin
                        de mantener la demanda que se necesita para que una planta muy grande permanezca activa tal vez se
                        requiera ofrecer descuentos sustantivos del producto. Los fabricantes estadounidenses de automóviles
                        afrontan este problema a cada rato. Otro ejemplo típico se refiere al uso de unas cuantas piezas de equipo
                        de enorme capacidad. En este tipo de operación, es esencial minimizar el tiempo que el equipo está inac-
                        tivo. Por ejemplo, M&M Mars tiene un equipo altamente automatizado para producir grandes volúmenes
                        de chocolates M&M. Una sola línea de la empacadora mueve 2.6 millones de paquetes de M&M por
                        hora. Aun cuando el trabajo directo que se requiere para operar el equipo no es mucho, la mano de obra
                        que se requiere para mantener el equipo es mucha.
                            En muchos casos, el tamaño de la planta no está sujeto a la influencia del equipo interno, el trabajo y
                        otros gastos de capital, sino a otros factores. Un factor central sería el costo del transporte de las materias
                        primas y los productos terminados que llegan y salen de la planta. Por ejemplo, una fábrica de cemento
                        tendría dificultades para servir a clientes que no estén ubicados a unas cuantas horas de distancia de la
                        planta. De igual manera, compañías automotrices como Ford, Honda, Nissan y Toyota han encontrado
                        que es provechoso ubicar las plantas dentro de mercados internacionales específicos. El tamaño antici-
        Global          pado de estos mercados pretendidos dictará en gran medida el tamaño de las plantas.
                            En fecha reciente, Jaguar, el productor de automóviles de lujo, encontró que tenía demasiadas plantas.
                        La empresa tenía 8 560 empleados en tres plantas que producían 126 122 automóviles, alrededor de 14
                        automóviles por empleado. En comparación, la planta de Volvo en Torslanda, Suecia, era el doble y pico
                        de productiva y estaba fabricando 158 466 automóviles con 5 472 trabajadores, o 29 automóviles por
                        empleado. Por otro lado, la unidad del Mini de BMW AG estaba produciendo 174 000 vehículos en una
                        sola planta británica con tan sólo 4 500 trabajadores (39 automóviles por empleado).
                                                    ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD          capítulo 5                     125



La curva de aprendizaje                                                                                                    ilustración 5.1


 A. Los costos por unidad producida disminuyen                         B. Se puede expresar con logaritmos:
    un porcentaje específico cada vez que la producción
    acumulada se duplica. Esta relación se puede expresar
    con una escala lineal como la que muestra esta gráfica
    de una curva de aprendizaje de 70%.                                                         (Escala Log-Log)
                                                                                400
              300                                                               300

              250                                                               200
 Costo                                                               Costo
 o precio     200                                                    o precio   150
 por unidad                                                          por unidad
              150                                                               100
              100

                    0        400        800    1 200     1 600                             200        400     800       1 600
                        Producción total acumulada de unidades                        Producción total acumulada de unidades




LA CURVA DE APRENDIZAJE
El concepto de la curva de aprendizaje es muy conocido. A medida que las plantas producen más, van
adquiriendo experiencia en los mejores métodos de producción, los cuales disminuyen sus costos de pro-
ducción de modo previsible. Cada vez que la producción acumulada de una planta se duplica, sus costos
de producción diminuyen un porcentaje específico dependiendo de la índole del negocio. La ilustración
5.1 muestra el efecto que una curva de aprendizaje tiene en los costos de producción de hamburguesas.
    El porcentaje de la curva de aprendizaje varía de una industria a otra. A efecto de aplicar este con-
cepto a la industria restaurantera, piense en una cadena hipotética de establecimientos de comida rápida
que ha producido 5 millones de hamburguesas. Dado un costo variable actual de 55 centavos de dólar por
hamburguesa, ¿cuál será el costo por hamburguesa cuando la producción acumulada llegue a 10 millones
de hamburguesas? Si la empresa tiene una curva de aprendizaje de 90%, los costos disminuirán a 90%
de 55 centavos, o 49.5 centavos, cuando la producción acumulada llegue a 10 millones. Con mil millones de
hamburguesas, el costo variable baja a menos de 25 centavos.
    Advierta que el volumen de ventas es una cuestión que adquiere importancia para poder ahorrar cos-
tos. Si la empresa A sirve al día el doble de hamburguesas que la empresa B, acumulará “experiencia” al
doble de velocidad. (El capítulo 5A contiene una explicación más amplia de las curvas de aprendizaje).


EL PUNTO DONDE LAS ECONOMÍAS DE ESCALA
SE CRUZAN CON LA CURVA DE APRENDIZAJE
El lector astuto notará que las plantas grandes pueden tener una doble ventaja de costos en comparación
con sus competidoras. La planta grande no sólo gana con las economías de escala, sino también produ-
cirá más y ello le brindará además las ventajas de la curva de aprendizaje. Las compañías con frecuencia
utilizan esta doble ventaja como estrategia competitiva y primero construyen una planta grande con eco-
nomías de escala sustantivas y, a continuación, utilizan sus costos más bajos para poner precios agresivos
e incrementar su volumen de ventas. El mayor volumen las hace avanzar por la curva de aprendizaje más
rápido que a sus competidoras, permitiendo a la compañía bajar los precios incluso más y alcanzar un
volumen incluso mayor. No obstante, para que esta estrategia tenga éxito se deben cumplir dos criterios:
1) el producto debe ajustar con las necesidades de los clientes y 2) la demanda debe ser lo bastante grande
para soportar el volumen.


ENFOQUE EN LA CAPACIDAD
El concepto de la fábrica enfocada sostiene que una instalación dedicada a la producción funciona mejor
si se enfoca en una cantidad relativamente limitada de objetivos de producción.2 Esto significa, por ejem-
126                                sección 2     PROCESOS


La fábrica enfocada de Xerox
crea un entorno laboral
flexible y eficiente, en el cual
los equipos de empleados
son los encargados de
manufacturar productos
específicos de principio a fin.
La fábrica fue diseñada con
información aportada por
el personal industrial, que
trabajó al unísono con los
ingenieros y la gerencia.




                                   plo, que una empresa no esperaría ser excelente en todos los aspectos del desempeño de la manufactura;
                                   es decir, en el costo, la calidad, la flexibilidad, las introducciones de productos nuevos, la confiabilidad,
                                   los tiempos cortos de entrega y la inversión baja. Por el contrario, debe elegir un conjunto limitado de las
                                   tareas que contribuyan más a sus objetivos. No obstante, dado el enorme avance de la tecnología de pro-
                                   ducción para la manufactura, los objetivos de las fábricas han ido evolucionando con la intención de tratar
                                   de hacer todo muy bien. ¿Cómo se resuelven estas aparentes contradicciones? Una forma es decir que si
                                   la empresa no cuenta con la tecnología para dominar múltiples objetivos, entonces debe acotar su enfo-
                                   que en una elección lógica. Otra manera es reconocer la realidad práctica de que no todas las empresas
                                   están en industrias que requieren que utilicen toda su gama de capacidades para competir.
Enfoque en la capacidad                El concepto del enfoque en la capacidad también se puede aplicar por medio de un mecanismo de
                                   plantas dentro de plantas, o PdP. Una planta enfocada puede tener varias PdP, y cada una de ellas tendrá
                                   su propia suborganización, equipamiento y políticas para el proceso, políticas para la administración del
                                   personal, métodos de control de la producción, etc., para los distintos productos, aun cuando todos se
                                   fabriquen en el mismo lugar. De hecho, esto permite que cada departamento de la organización encuentre
                                   su mejor nivel de operación y, con ello, transmita el concepto del enfoque hacia abajo, hasta el nivel de
                                   las operaciones.


                                   FLEXIBILIDAD DE LA CAPACIDAD
                                   Flexibilidad de la capacidad significa que se tiene la capacidad para incrementar o disminuir los niveles
                                   de producción con rapidez, o de pasar la capacidad de producción de forma expedita de un producto o
                                   servicio a otro. Esta flexibilidad es posible cuando se tienen plantas, procesos y trabajadores flexibles, así
                                   como estrategias que utilizan la capacidad de otras organizaciones.

                                   Plantas flexibles Lo último en flexibilidad de plantas seguramente es aquella que no tarda nada de
                                   tiempo para pasar de un producto a otro. Esta planta usa equipamiento movible, muros desmontables
                                   y suministro de energía eléctrica muy accesible y fácil de cambiar de ruta y, en consecuencia, se puede
                                   adaptar con rapidez al cambio. Una analogía con un negocio de servicios para la familia capta el sentido
                                   muy bien: una planta con equipamiento “fácil de instalar, de desmontar y de trasladar, como el Circo
                                   Ringling Bros. Barnum and Bailey en los viejos tiempos de las carpas de circo”.3
                                             ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD          capítulo 5                      127


Procesos flexibles El epítome de los procesos flexibles son, por un lado, los sistemas flexibles de
producción y, de la otra, el equipamiento simple y fácil de preparar. Estos dos enfoques tecnológicos
permiten pasar rápidamente, a bajo costo, de una línea de productos a otra y ello conlleva a lo que se
conoce como economías de alcance. (Por definición, las economías de alcance existen cuando múlti-              Economías de alcance
ples productos se pueden producir a costo más bajo en combinación que por separado.)

Trabajadores flexibles Los trabajadores flexibles poseen múltiples habilidades y son capaces de
pasar con facilidad de un tipo de tarea a otro. Requieren una capacitación más amplia que la de los
obreros especializados y necesitan el apoyo de gerentes y de personal administrativo para que éstos
cambien rápidamente sus asignaciones laborales.



PLANEACIÓN DE LA CAPACIDAD

CONSIDERACIONES PARA AUMENTAR LA CAPACIDAD
Cuando se proyecta añadir capacidad es preciso considerar muchas cuestiones. Tres muy importantes
son: conservar el equilibrio del sistema, la frecuencia de los aumentos de capacidad y el uso de capacidad
externa.

Conservar el equilibrio del sistema En una planta en equilibrio perfecto, el producto de la etapa 1
es la cantidad exacta del insumo que requiere la etapa 2. El producto de la etapa 2 es la cantidad exacta
del insumo que requiere la etapa 3, y así de manera sucesiva. Sin embargo, en la práctica, llegar a un
diseño tan “perfecto” es prácticamente imposible y no es deseable. Una razón que explica lo anterior
es que los mejores niveles para operar correspondientes a cada etapa suelen ser diferentes. Por ejemplo,
el departamento 1 operaría con suma eficiencia dentro de una banda de 90 a 110 unidades por mes,
mientras que el departamento 2, la siguiente etapa del proceso, es más eficiente dentro de una de 75 a
85 unidades por mes y el departamento 3 trabaja mejor dentro de una banda de 150 a 200 unidades por
mes. Otra razón es que la variabilidad de la demanda del producto y los procesos mismos por lo habitual
llevan al desequilibrio, salvo en el caso de líneas de producción automatizadas, las cuales, en esencia,
sólo son una máquina muy grande.
    Hay varios caminos para atacar el desequilibrio. Uno consiste en sumar capacidad a las etapas que
son cuellos de botella. Lo anterior se puede hacer tomando medidas temporales, como programando
horas extra, arrendando equipo o adquiriendo capacidad adicional por medio de subcontrataciones. Otro
camino es emplear inventarios que sirvan de amortiguador ante la etapa que es un cuello de botella y así
garantizar que siempre haya material para trabajar. Un tercer enfoque implica duplicar las instalaciones
del departamento del que depende otro departamento.

Frecuencia de los aumentos de capacidad Cuando se suma capacidad se deben considerar dos
tipos de costos: el costo de escalar la capacidad con demasiada frecuencia y el costo de hacerlo con
demasiada poca frecuencia. Escalar la capacidad con demasiada frecuencia es muy costoso. Los costos
directos incluyen retirar y sustituir el equipamiento viejo y capacitar a los empleados para usar el nuevo.
Además, es necesario comprar el nuevo equipamiento, muchas veces por una cantidad considerablemen-
te mayor al precio de venta del viejo. Por último, está el costo de oportunidad del lugar de la planta o el
servicio que está inactivo durante el periodo del cambio.
    Por otro lado, escalar la capacidad con demasiada poca frecuencia también es muy costoso. Una
expansión poco frecuente significa que la capacidad se adquiere en bloques más grandes. El exceso de
capacidad que se haya adquirido se debe asentar como un gasto fijo hasta que sea utilizada. (La ilustra-
ción 5.2 muestra la expansión frecuente de la capacidad frente a la poco frecuente.)

Fuentes externas de capacidad En algunos casos tal vez resulte más barato no aumentar la capaci-
dad en absoluto, sino recurrir a alguna fuente externa de capacidad ya existente. Dos estrategias que suelen
utilizar las organizaciones son la subcontratación y la capacidad compartida. Un ejemplo de subcontrata-
ción es el caso de los bancos japoneses de California que subcontratan las operaciones de compensación
de cheques. Un ejemplo de capacidad compartida sería el caso de dos líneas aéreas nacionales, que
recorren diferentes rutas con distintas demandas estacionales y que intercambian aviones (debidamente
repintados) cuando las rutas de una son muy utilizadas y las de la otra no. Un nuevo giro en las líneas
aéreas que comparten rutas es utilizar el mismo número de vuelo aun cuando la compañía cambie a lo
largo de la ruta.
128                    sección 2     PROCESOS



ilustración 5.2         Expansión de la capacidad frecuente versus poco frecuente




                                                                                                   Demanda
                                                                 Nivel de                          pronosticada
                                                                capacidad
                                                              (expansión
                                                           poco frecuente)                  Nivel de capacidad
                                                                                            (expansión frecuente)

                                            Volumen


                                                                               Bloque pequeño    Bloque grande




                                                                               Años




                       CÓMO DETERMINAR LA CAPACIDAD QUE SE REQUERIRÁ
                       Para determinar la capacidad que se requerirá, se deben abordar las demandas de líneas de productos
                       individuales, capacidades de plantas individuales y asignación de la producción a lo largo y ancho de la
                       red de la planta. Por lo general, esto se hace con los pasos siguientes:
                          1. Usar técnicas de pronóstico para prever las ventas de los productos individuales dentro de cada
                             línea de productos.
                          2. Calcular el equipamiento y la mano de obra que se requerirá para cumplir los pronósticos de las
                             líneas de productos.
                          3. Proyectar el equipamiento y la mano de obra que estará disponible durante el horizonte del plan.
Colchón de capacidad       Muchas veces, la empresa decide tener un colchón de capacidad que se mantendrá entre los reque-
                       rimientos proyectados y la capacidad real. Un colchón de capacidad se refiere a la cantidad de capacidad
                       que excede a la demanda esperada. Por ejemplo, si la demanda anual esperada de una instalación es de
                       10 millones de dólares en productos al año y si la capacidad del diseño es de 12 millones de dólares al
                       año, ésta tendrá un colchón de capacidad de 20%. Un colchón de capacidad de 20% es igual a un índice
                       de utilización de 83% (100%/120%).
                           Cuando la capacidad del diseño de la empresa es menor que la capacidad requerida para satisfacer su
                       demanda, se dice que tiene un colchón de capacidad negativo. Por ejemplo, si una empresa tiene una de-
                       manda de 12 millones de dólares en productos por año, pero sólo puede producir 10 millones de dólares
                       por año, tiene un colchón de capacidad negativo de 16.7%.
                           A continuación se aplican estos tres pasos a un ejemplo.


                       EJEMPLO 5.1: Cómo determinar la capacidad que se requerirá
                       Stewart Company produce aderezos para ensalada de dos sabores: Paul’s y Newman’s. Los dos se presentan
                       en botellas y en sobres individuales de plástico de una porción. La gerencia quiere determinar el equipamiento
                       y la mano de obra que se requerirá en los próximos cinco años.




                       SOLUCIÓN
                       Paso 1. Use técnicas de pronóstico para prever las ventas de los productos individuales de cada línea de pro-
      Interfuncional   ductos. El departamento de marketing, que está realizando una campaña promocional del aderezo Newman’s,
                                                     ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD       capítulo 5   129

proporcionó los siguientes valores para el pronóstico de la demanda (en miles) para los próximos cinco años.
Se espera que la campaña dure los próximos dos años.
                                                                             Año

                                                               1       2      3        4       5

            Paul’s
            Botellas (millares)                                60    100      150     200     250
            Sobres individuales de plástico (millares)        100    200     300      400     500
            Newsman’s
            Botellas (millares)                                75     85      95       97      98
            Sobres individuales de plástico (millares)        200    400     600      650     680


     Paso 2. Calcule el equipo y la mano de obra que se requerirán para cumplir con los pronósticos de las
líneas de productos. Ahora, hay tres máquinas disponibles y cada una puede empacar un máximo de 150 000
botellas al año. Cada máquina necesita dos operadores y puede producir botellas de aderezo Newman’s y
también Paul’s. Hay disponibles seis operadores para las máquinas de botellas. Además, hay disponibles cinco
máquinas que pueden empacar, cada una, hasta un máximo de 250 000 sobres individuales de plástico al año.
Cada una de las máquinas que puede producir sobres individuales de aderezo de Newman’s y de Paul’s requie-
re tres operadores. Ahora hay disponibles 20 operadores de las máquinas que producen sobres individuales
de plástico.
     La tabla anterior permite pronosticar el total de las líneas de productos sumando la demanda anual de
botellas y de sobres individuales de plástico así:
                                                                             Año

                                                               1       2      3        4       5

            Botellas                                          135    185     245       297     348
            Sobres individuales de plástico                   300    600     900     1 050   1 180


    Ahora es posible calcular el equipo y la mano de obra que se requerirán para el año en curso (año 1). Dado
que la capacidad total disponible para llenar botellas es de 450 000 al año (3 máquinas × 150 000 cada una),
se empleará 135/450 = 0.3 de la capacidad disponible para el año en curso o 0.3 × 3 = 0.9 máquinas. Por otro
lado, se necesitará 300/1 250 = 0.24 de la capacidad disponible para los sobres individuales de plástico para el
año en curso o 0.24 × 5 = 1.2 máquinas. El número de personas necesario para sostener la demanda pronosti-
cada para el primer año será la plantilla necesaria para las máquinas de las botellas y los sobres individuales
de plástico.
    La mano de obra requerida para la operación de las botellas en el año 1 es:
                                  0.9 botellas máquina × 2 operadores = 1.8 operadores
                       1.2 máquinas sobres individuales × 3 operadores = 3.6 operadores.
    Paso 3. Proyecte la mano de obra y el equipo disponibles a lo largo del horizonte del plan. Se repite el
cálculo anterior para los años restantes:
                                                                             Año

                                                               1       2      3        4       5

            Operación de los sobres individuales de plástico
            Porcentaje utilizado de la capacidad             24      48      72      84       94
            Máquinas requeridas                               1.2     2.4     3.6     4.2      4.7
            Mano de obra requerida                            3.6     7.2    10.8    12.6     14.1
            Operación de botellas
            Porcentaje utilizado de la capacidad             30      41      54      66       77
            Máquinas requeridas                                 .9    1.23    1.62    1.98     2.31
            Mano de obra requerida                            1.8     2.46    3.24    3.96     4.62


    Existe un colchón de capacidad positivo para los cinco años, porque la capacidad disponible para las dos
operaciones siempre excede la demanda esperada. Ahora, Stewart Company puede empezar a preparar un
plan para las operaciones o ventas a mediano plazo de las dos líneas de producción.
                                                                                      •
130                     sección 2     PROCESOS


                        LOS ÁRBOLES DE DECISIÓN UTILIZADOS PARA EVALUAR
                        LAS ALTERNATIVAS PARA LA CAPACIDAD
                        Una manera muy conveniente de evaluar la decisión de invertir en capacidad es emplear árboles de de-
                        cisión. El formato de árbol no sólo sirve para comprender el problema, sino también para encontrar una
                        solución. Un árbol de decisión es un esquema que representa la secuencia de pasos de un problema y las
                        circunstancias y consecuencias de cada paso. En años recientes, se han desarrollado algunos paquetes
                        comerciales de software para ayudar a construir y analizar árboles de decisión. Estos paquetes hacen que
                        el proceso sea fácil y rápido.
                            Los árboles de decisión están compuestos de nodos de decisiones con ramas que llegan y salen de
                        ellos. Por lo general, los cuadros representan los puntos de decisión y los círculos los hechos fortuitos.
                        Las ramas que salen de los puntos de decisión muestran las opciones que tiene la persona que toma la
                        decisión, las ramas que salen de los hechos fortuitos muestran las probabilidades de que éstos ocurran.
                            Para resolver problemas con un árbol de decisión, se empieza a analizar el fi nal del árbol avanzando
                        hacia su inicio. A medida que se retrocede, se van calculando los valores esperados de cada paso. Cuan-
                        do se calcula el valor esperado es importante calcular el valor del dinero considerando el tiempo si el
                        horizonte del plan es largo.
                            Cuando se terminan los cálculos, se puede podar el árbol eliminando todas las ramas de cada punto
                        de decisión salvo aquella que promete los rendimientos más altos. Este proceso prosigue hasta el primer
                        punto de decisión y, de tal manera, el problema de la decisión queda resuelto.
                            A continuación se demuestra una aplicación a la planeación de la capacidad de Hackers Computer
                        Store. Las ilustraciones empleadas para resolver el problema fueron generadas utilizando un programa
Software del programa   llamado DATA de TreeAge Software. (El DVD que acompaña a este libro contiene una versión de de-
    DATA TreeAge        mostración del software que sirve para resolver los problemas que se presentan en este capítulo.)




                        EJEMPLO 5.2: Árboles de decisión
                        El dueño de Hackers Computer Store está analizando qué hará con su negocio en los próximos cinco años.
                        El crecimiento de las ventas en años recientes ha sido bueno, pero éstas podrían crecer sustantivamente si,
                        como se ha propuesto, se construye una importante empresa electrónica en su zona. El dueño de Hackers ve
                        tres opciones. La primera es ampliar su tienda actual, la segunda es ubicarla en otro lugar y la tercera es sim-
      Servicio          plemente esperar y no hacer nada. La decisión de expandirse o cambiarse no tomaría mucho tiempo y, por lo
                        mismo, la tienda no perdería ingresos. Si no hiciera nada en el primer año y si hubiera un crecimiento notable,
                        entonces consideraría la decisión de expandirse. Si esperara más de un año, la competencia empezaría a llegar
                        y provocaría que la expansión no fuera viable.
                            Los supuestos y las circunstancias son:
                            1. Un crecimiento notable como consecuencia del incremento de la población de fanáticos de las compu-
                               tadoras procedentes de la nueva empresa electrónica tiene una probabilidad de 55%.
                            2. Un crecimiento notable en otro lugar produciría un rendimiento anual de 195 000 dólares al año. Un
                               crecimiento flojo en otro lugar significaría un rendimiento anual de 115 000 dólares.
                            3. Un crecimiento notable con una expansión produciría un rendimiento anual de 190 000 dólares al año.
                               Un crecimiento flojo con una expansión significaría un rendimiento anual de 100 000 dólares.
                            4. En la tienda existente, sin cambio, el rendimiento anual sería de 170 000 dólares al año, si hubiera un
                               crecimiento notable y de 105 000 dólares si el crecimiento fuera débil.
                            5. La expansión del local actual costaría 87 000 dólares.
                            6. El cambio a otro lugar costaría 210 000 dólares.
                            7. Si el crecimiento es notable y si se amplía el local existente en el segundo año, el costo seguiría siendo
                               de 87 000 dólares.
                            8. Los costos de operaciones son iguales para todas las opciones.



                        SOLUCIÓN
                        Se construye un árbol de decisión para aconsejar al dueño de Hackers cuál sería la mejor acción. La ilustra-
                        ción 5.3 presenta el árbol de decisión de este problema. Hay dos puntos de decisión (presentados en los nodos
                        cuadrados) y tres circunstancias fortuitas (los nodos circulares).
                            Los valores del resultado de cada alternativa que se presentan a la derecha del diagrama de la ilustración
                        5.4 se calculan de la manera siguiente:
                                                     ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD                        capítulo 5                     131



Árbol de decisión para el problema de Hackers Computer Store                                                                            ilustración 5.3

                                                                       Crecimiento notable
                                                                                                   Costo_ingresos_mudarse
                                                Mudarse                         .55
                                                                        Crecimiento flojo
                                                                                                   Costo_ingresos_mudarse
                                                                                .45
                                                                       Crecimiento notable
                                                                                                   Costo_ingresos_expansión
               Hackers Computer                 Expandirse                      .55
                     Store                                               Crecimiento flojo
                                                                                                   Costo_ingresos_expansión
                                                                                .45
                                                                                                          Expandirse
                                                                                                                           Costo_ingresos_expansión
                                                                       Crecimiento notable
                                                                                .55                   No hacer nada
                                             No hacer nada                                                                 Ingresos

                                                                         Crecimiento flojo
                                                                                                   Ingresos
                                                                                .45




Análisis del árbol de decisión utilizando DATA (TreeAge Software, Inc.)                                                                 ilustración 5.4


                                                              Crecimiento notable
                                                                                          Costo_ingresos_mudarse = $765 000
                                                                  .0.550
                                   Mudarse
                                                      $585 000
                                                               Crecimiento flojo
                                                                                          Costo_ingresos_mudarse = $365 000
                                                                    0.450
                                                            Crecimiento notable
                                                                                          Costo_ingresos_expansión = $863 000
                                                                0.550
       Hackers Computer            Expandirse
                                                    $660 500
            Store             No hacer nada; $703 750         Crecimiento flojo
                                                                                          Costo_ingresos_expansión = $413 000
                                                                    0.450
                                                                                            Expandirse
                                                                                                                Costo_ingresos_expansión = $843 000
                                                              Crecimiento notable
                                                                                          No hacer nada; $850 000
                                                                    0.550                  No hacer nada
                                   No hacer nada                                                              Ingresos = $850 000; P = 0.550
                                                      $703 750
                                                                 Crecimiento flojo
                                                                                          Ingresos = $525 000; P = 0.450
                                                                    0.450



Alternativa                                                                          Ingresos              Costo        Valor

Mudarse a otro lugar, crecimiento notable                                            $195 000 × 5 años     $210 000     $765 000
Mudarse a otro lugar, crecimiento flojo                                              $115 000 × 5 años     $210 000     $365 000
Expandir tienda, crecimiento notable                                                 $190 000 × 5 años     $87 000      $863 000
Expandir tienda, crecimiento flojo                                                   $100 000 × 5 años     $87 000      $413 000
No hacer nada por ahora, crecimiento notable, expandirse el año entrante             $170 000 × 1 año +    $87 000      $843 000
                                                                                     $190 000 × 4 años
No hacer nada por ahora, crecimiento notable, no expandirse el año entrante          $170 000 × 5 años     $0           $850 000
No hacer nada por ahora, crecimiento flojo                                           $105 000 × 5 años     $0           $525 000


    Partiendo de las alternativas ubicadas a la derecha, las cuales están asociadas a la decisión de expandirse
o no, se observa que la alternativa de no hacer nada tiene un valor más alto que la de expandirse. Por lo tanto,
132                    sección 2      PROCESOS



ilustración 5.5          Análisis de árbol de decisión usando valor presente neto


                                                        Crecimiento notable
                                                                                Costo_ingresos_mudarse = $428 487
                                                               .0.550
                                    Mudarse
                                                      $310 613
                                                          Crecimiento flojo
                                                                                Costo_ingresos_mudarse = $166 544
                                                                  0.450
                                                         Crecimiento notable
                                                                                Costo_ingresos_expansión = $535 116
                                                                0.550
            Hackers Computer        Expandirse
                                                       $402 507
                 Store
                                                          Crecimiento flojo     Costo_ingresos_expansión = $240 429
                                                                0.450
                                                                                  Expandirse
                                                                                                    Costo_ingresos_expansión = $529 874
                                                         Crecimiento notable
                                                                                No hacer nada; $556 630
                                                                  0.550           No hacer nada
                                    No hacer nada                                                   Ingresos = $556 630; P = 0.550
                                                       $460 857
               Análisis VPN
               Índice = 16%                                Crecimiento flojo
                                                                                Ingresos = $343 801; P = 0.450
                                                                  0.450




                       se elimina la expansión en las alternativas del segundo año. Esto significa que si no se hace nada en el primer
                       año y si se registra un crecimiento notable, entonces no tiene sentido expandirse en el segundo año.
                            Ahora se pueden calcular los valores esperados asociados a las alternativas de decisión actuales. Simple-
                       mente se multiplica el valor de la alternativa por su probabilidad y se suman los valores. El valor esperado para
                       la alternativa de mudarse ahora es de 585 000 dólares. La alternativa de la expansión tiene un valor esperado
                       de 660 500 dólares, y no hacer nada por el momento tiene un valor esperado de 703 750 dólares. El análisis
                       indica que la mejor decisión será no hacer nada (por ahora y el año entrante).
                            Dado que el horizonte de tiempo es de cinco años, sería conveniente considerar el valor de los ingresos
                       en relación con el tiempo y los flujos de costos cuando se resuelve este problema. El suplemento A (“Análisis
                       financiero”) presenta los detalles respecto al cálculo de los valores monetarios descontados. Por ejemplo, si se
                       supone una tasa de interés de 16%, el resultado de la primera alternativa (mudarse ahora, crecimiento notable)
                       tiene un ingreso descontado por valor de 428 487 dólares (195 000 × 3.274293654) menos el costo de 210 000
                       dólares por mudarse en seguida. La ilustración 5.5 muestra el análisis considerando los flujos descontados. A
                       continuación se presentan los detalles de los cálculos. Se puede utilizar la tabla G3 de los valores presentes (en
                       el apéndice G) para ver los factores de descuento. A efecto de que los cálculos coincidan con los presentados
                       por el programa de computadora, se han utilizado factores de descuento calculados con 10 dígitos de precisión
                       (es fácil hacerlo con Excel). El único cálculo que es algo engañoso es el de los ingresos cuando no se hace nada
                       por el momento y la expansión se hace al principio del año entrante. En tal caso, se tiene un flujo de ingresos de
                       170 000 dólares el primer año, seguido de cuatro años con 190 000 dólares. La primera parte del cálculo (170 000
                       × 0.862068966) descuenta los ingresos del primer año al momento presente. La siguiente parte (190 000 ×
                       2.798180638) descuenta los próximos cuatro años al principio del año dos. A continuación, se descuenta este
                       flujo de cuatro años a valor presente. El programa de cómputo utilizado para generar la ilustración 5.5 realizó
                       estos cálculos de manera automática.
                           Alternativa                                            Ingresos                       Costo         Valor

                           Mudarse a otro lugar, crecimiento notable              $195 000 × 3.274293654         $210 000      $428 487
                           Mudarse a otro lugar, crecimiento flojo                $115 000 × 3.274293654         $210 000      $166 544
                           Expandir tienda, crecimiento notable                   $190 000 × 3.274293654         $87 000       $535 116
                           Expandir tienda, crecimiento flojo                     $100 000 × 3.274203654         $87 000       $240 429
                           No hacer nada por ahora, crecimiento notable,          $170 000 × 0.862068966         $87 000 ×     $529 874
                             expandirse el año entrante                           $190 000 × 2.798180638 ×       0.862068966
                                                                                         0.862068966
                           No hacer nada por ahora, crecimiento notable,          $170 000 × 3.274293654         $0            $556 630
                            no expandirse el año entrante
                           No hacer nada por ahora, crecimiento flojo             $105 000 × 3.274293654         $0            $343 801
                                                                                                                                          •
                                             ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD          capítulo 5               133



PLANEACIÓN DE LA CAPACIDAD EN LOS SERVICIOS

PLANEACIÓN DE LA CAPACIDAD EN LOS SERVICIOS
O EN LA MANUFACTURA
Aun cuando la planeación de la capacidad en los servicios está sujeta a muchas de las mismas cuestiones
que la planeación de la capacidad en la manufactura y que el cálculo del tamaño de las instalaciones se
puede hacer de manera muy parecida, también existen algunas diferencias importantes entre ellas. La
capacidad en los servicios depende más del tiempo y la ubicación está sujeta a las fluctuaciones de una
demanda más volátil y su utilización repercute directamente en la calidad de los servicios.                    Servicio

Tiempo Los servicios, a diferencia de los bienes, no se pueden guardar para usarlos más adelante.
Debe haber capacidad disponible para producir un servicio en el momento que se necesita. Por ejemplo,
un asiento que no estuvo ocupado en el vuelo anterior de una línea aérea no se le puede proporcionar a un
cliente si el vuelo actual está completo. El cliente tampoco puede comprar un asiento en el vuelo de un
día particular y llevárselo a casa para usarlo más adelante.

Ubicación La capacidad del servicio se debe ubicar cerca del cliente. En el caso de la manufactura,
cuando ha ocurrido la producción, los bienes son distribuidos para que lleguen al cliente. En el caso de
los servicios, sin embargo, ocurre justo lo contrario. Primero se debe distribuir la capacidad para brindar
el servicio (sea de forma física o a través de un medio de comunicación como el teléfono) y a continua-
ción se producirá el servicio. Una habitación de hotel o un automóvil rentado que están disponibles en
otra ciudad no le sirven de nada al cliente, éstos deben estar en el lugar donde el cliente los necesita.

Volatilidad de la demanda La volatilidad de la demanda de un sistema de prestación de servicios
es mucho mayor que en un sistema de producción de manufactura por tres razones. En primer término,
como se acaba de decir, los servicios no se pueden guardar. Esto significa que el inventario no puede
nivelar la demanda como en el caso de la manufactura. La segunda razón es que los clientes interactúan
directamente con el sistema de producción, y estos clientes muchas veces tienen necesidades diferentes,
distintos niveles de experiencia con el proceso y tal vez requieran diferente número de transacciones.
Lo anterior contribuye a una variabilidad mucho mayor en el tiempo de procesamiento que se requiere
para cada cliente y, por lo mismo, a una mayor variabilidad de la capacidad mínima que se necesita. La
tercera razón que explica la mayor volatilidad de la demanda en los servicios es que el comportamiento
de los consumidores la afecta directamente. Las influencias en el comportamiento del cliente, desde el
clima hasta un hecho mayor, afectan directamente la demanda de distintos servicios. Si usted acude a
un restaurante cerca de su universidad en tiempo de vacaciones es probable que lo encuentre casi vacío.
¡Trate de reservar una habitación en un hotel local el fin de semana que los estudiantes vuelven a casa!
Este efecto conductual es evidente incluso en periodos más breves, como los amontonamientos en la
ventanilla del banco a la hora de la comida o el repentino brote de órdenes de pizza durante el medio
tiempo del domingo del Superbowl. Dada esta volatilidad, la capacidad en los servicios se suele planear
en incrementos de tan sólo 10 a 30 minutos, a diferencia de los incrementos de una semana que son
comunes en la manufactura.


UTILIZACIÓN DE LA CAPACIDAD Y CALIDAD
DE LOS SERVICIOS
La planeación de los niveles de capacidad en los servicios debe tomar en cuenta la relación diaria entre
la utilización del servicio y la calidad del mismo. La ilustración 5.6 presenta una situación de servicios
planteada en términos de una línea de espera (índices de llegada e índices de servicio).4 Como han se-
ñalado Haywood-Farmer y Nollet, el mejor punto para operar es cerca de 70% de la capacidad máxima.
Esto “basta para mantener ocupados a los servidores, pero permite tiempo suficiente para atender a los
clientes individualmente y tener una cantidad suficiente de capacidad reservada como para no producir
demasiados dolores de cabeza administrativos”.5 En la zona crítica, los clientes pasan por el proceso del
sistema, pero la calidad del servicio disminuye. Por encima de la zona crítica, la línea crece y es probable
que muchos clientes jamás lleguen a ser atendidos.
134                              sección 2        PROCESOS



ilustración 5.6                   Relación entre el índice de utilización del servicio (ρ) y la calidad del servicio



                                                             λ                                                   ρ = 100%
                                                                    Zona de ausencia de servicio
                                                                    (μ < λ)                      Zona
                                                                                                      crítica    ρ = 70%


                                              Índice de media
                                               de llegadas (λ)


                                                                                          Zona de servicio


                                                                                                                 μ
                                                                       Índice de media de servicios (μ)

                                             Fuente: J. Haywood-Farmer y J. Nollet, Services Plus: Effective Service
                                             Management (Boucherville, Quebec, Canadá: G. Morin Publisher Ltd., 1991), p. 59.




                                                                                         Haywood-Farmer y Nollet también apuntan que el índice óp-
                                                                                     timo de utilización es específico del contexto. Cuando el grado
                                                                                     de incertidumbre y la apuesta son muy altos, entonces los índi-
                                                                                     ces bajos son adecuados. Por ejemplo, las salas de urgencias de
                                                                                     los hospitales y las estaciones de bomberos deben buscar una
                                                                                     escasa utilización debido al elevado grado de incertidumbre y el
                                                                                     carácter de vida o muerte de sus actividades. Los servicios rela-
                                                                                     tivamente previsibles, como los de trenes suburbanos, o las ins-
                                                                                     talaciones de servicios que no tienen contacto con los clientes,
                                                                                     como las operaciones de clasificación de correo, pueden planear
                                                                                     sus operaciones a un nivel de utilización mucho más próximo a
                                                                                     100%. Cabe señalar que existe un tercer grupo para el cual es
                                                                                     deseable una elevada utilización. A todos los equipos deportivos
                                                                                     les gusta que se agoten las localidades, no sólo porque el margen
                                                                                     de contribución de cada cliente es prácticamente de 100%, sino
                                                                                     porque la casa llena crea un ambiente que agrada a los clientes,
                                                                                     motiva al equipo de casa a desempeñarse mejor y alienta las ven-
El software para centros de contacto multimedia, como Solidus eCare de               tas futuras de entradas. Los espectáculos en escenarios y bares
Ericsson, permite que las organizaciones de servicios al cliente que están           comparten este fenómeno. Por otro lado, muchos pasajeros de
dispersadas se comporten como una sola unidad. El software encamina las              líneas aéreas piensan que un vuelo está demasiado lleno cuando
llamadas a los agentes con base en las capacidades que poseen, mezclando             el asiento junto al suyo va ocupado. Las líneas aéreas capitalizan
las llamadas con e-mail, Web-chat, navegación por la Web con los clientes            esta respuesta vendiendo más asientos en clase ejecutiva.6
y respuestas automatizadas para preguntas planteadas con frecuencia. Esta
flexibilidad expande en efecto la capacidad para brindar servicios a los
clientes.




            CONCLUSIÓN
                                La planeación estratégica de la capacidad implica una decisión de invertir en la cual las capacidades de
                                recursos deben coincidir con el pronóstico de la demanda a largo plazo. Como se ha explicado en este
                                capítulo, algunos de los factores que se deben tomar en cuenta para decidir si se aumenta la capacidad en
                                el caso de la manufactura y también de los servicios son:
                                     •   Los efectos probables de las economías de escala.
                                     •   Los efectos de las curvas de aprendizaje.
                                              ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD           capítulo 5                          135

   •   Las repercusiones de cambiar el enfoque de las instalaciones y el equilibrio entre las etapas de
       producción.
   •   El grado de flexibilidad de las instalaciones y de la fuerza de trabajo.
    En el caso particular de los servicios, una consideración fundamental es el efecto que los cambios
de capacidad tienen en la calidad del servicio que se ofrece. Más adelante, en otro capítulo, se trata de la
cuestión de dónde se deben ubicar las instalaciones de una empresa.                                                      Servicio



VOCABULARIO BÁSICO
Capacidad El volumen de producción que un sistema puede alcan-          Enfoque en la capacidad Se puede aplicar con el concepto de las
zar durante un periodo específico.                                      plantas dentro de plantas, en cuyo caso una planta tiene varias su-
                                                                        borganizaciones especializadas para diferentes productos, a pesar
Planeación estratégica de la capacidad Determinar el nivel gene-        de que estén todas bajo un mismo techo. Esto permite encontrar el
ral de capacidad de los recursos de capital intensivo que mejor apoye   mejor nivel de operación correspondiente a cada suborganización.
la estrategia competitiva de la compañía a largo plazo.
                                                                        Economías de alcance Se presentan cuando múltiples productos
Mejor nivel de operación El nivel de capacidad para el que se di-       se pueden producir a costo más bajo combinados que por separado.
señó el proceso y el volumen de producción con el cual se minimiza
el costo promedio por unidad.                                           Colchón de capacidad     Capacidad que excede a la demanda es-
                                                                        perada.
Índice de utilización de la capacidad Mide qué tanto se acerca la
empresa a su mejor nivel de operación.



PROBLEMA RESUELTO
E-Education es un negocio nuevo que prepara y comercializa cursos de Maestría en Administración que
ofrece por Internet. La compañía tiene su domicilio en Chicago y cuenta con 150 empleados. Debido a un
crecimiento notable, la compañía necesita más espacio de oficinas. Tiene la opción de arrendar espacio adi-
cional en su actual ubicación en Chicago para dos años más, pero después tendrá que mudarse a otro edificio.
Otra opción que está considerando la compañía es mudar en seguida la operación entera a un pequeño pueblo
del Oeste medio. Una tercera opción es que la compañía arriende de inmediato otro edificio en Chicago. Si la
compañía elige la primera opción y arrienda más espacio en su ubicación actual, al paso de dos años, podría
arrendar otro edificio en Chicago o mudarse al pequeño pueblo del Oeste medio.
    A continuación se presentan algunos datos adicionales sobre las alternativas y la situación actual.

    1. La compañía tiene 75% de probabilidad de sobrevivir los siguientes dos años.
    2. Arrendar el nuevo espacio en su actual ubicación en Chicago durante dos años costaría 750 000 dó-
       lares al año.
    3. Mudar la operación entera a un pueblo del Oeste medio costaría 1 millón de dólares. Arrendar espacio
       sólo costaría 500 000 dólares al año.
    4. Mudarse a otro edificio en Chicago costaría 200 000 dólares y arrendar más espacio en el edificio
       costaría 650 000 dólares al año.
    5. La compañía puede cancelar el contrato de arrendamiento en cualquier momento.
    6. La compañía construiría su propio edificio dentro de cinco años, si sobrevive.
    7. Suponga que todos los demás costos e ingresos no cambian independientemente del lugar donde se
       ubique la compañía.

   ¿Qué debe hacer E-Education?

   Solución
   Paso 1. Construya un árbol de decisión que incluya todas las alternativas de E-Education. A continuación
   se presenta un árbol donde los puntos de decisión (nodos cuadrados) van seguidos de los hechos fortuitos
   (nodos circulares). En el caso del primer punto de decisión, si la compañía sobrevive, se deben considerar
   dos puntos de decisión adicionales.
136   sección 2     PROCESOS


                                                                                          Arrendar nuevo
                                                                                          espacio en Chicago
                                                                                                                   $3 650 000
                                                                  Sobrevivir (.75)
                             Permanecer en Chicago                                        Mudarse al Oeste medio
                             Arrendar espacio por dos años                                                         $4 000 000
                                                               $3 112 500
                                                                  Fracasar (.25)
                                                                                                                   $1 500 000
                                                                  Sobrevivir (.75)
                             Permanecer en Chicago                                                                 $3 450 000
                             Arrendar nuevo espacio
      E-Education                                              $2 962 500
                                                                  Fracasar (.25)
                                                                                                                   $1 500 000
                                                                  Sobrevivir (.75)
                             Mudarse a pueblo                                                                      $3 500 000
                             del Oeste medio
                                                               $3 125 000
                                                                  Fracasar (.25)
                                                                                                                   $2 000 000


             Paso 2: Calcular los valores de cada alternativa de la manera siguiente:
         Alternativa                                                                 Cálculo                       Valor

         Permanecer en Chicago, arrendar espacio para dos años,                      (750 000) × 2 + 200 000 +     $3 650 000
           sobrevivir, arrendar otro edificio en Chicago                             (650 000) × 3 =
         Permanecer en Chicago, arrendar espacio para dos años,                      (750 000) × 2 + 1 000 000 +   $4 000 000
           sobrevivir, mudarse al Oeste medio                                        (500 000) × 3 =
         Permanecer en Chicago, arrendar espacio para dos años, fracasar             (750 000) × 2                 $1 500 000
         Permanecer en Chicago, arrendar otro edificio en Chicago, sobrevivir        200 000 + (650 000) × 5 =     $3 450 000
         Permanecer en Chicago, arrendar otro espacio en Chicago, fracasar           200 000 + (650 000) × 2 =     $1 500 000
         Mudarse al Oeste medio, sobrevivir                                          1 000 000 + (500 000) × 5 =   $3 500 000
         Mudarse al Oeste medio, fracasar                                            1 000 000 + (500 000) × 2 =   $2 000 000

         Partiendo de las alternativas del extremo derecho, las primeras dos terminan en nodos de decisión. Como
         la primera opción, la de permanecer en Chicago y arrendar espacio para dos años, representa el costo más
         bajo, esto es lo que se haría si se decide permanecer en Chicago durante los dos primeros años. Si se fracasa
         después de los primeros dos años, representado por la tercera alternativa, el costo es sólo 1 500 000 dólares.
         El valor esperado de la primera opción de permanecer en Chicago y arrendar espacio para los primeros
         dos años es 0.75 × 3 650 000 + 0.25 × 1 500 000 = 3 112 500 dólares.
             La segunda opción, la de permanecer en Chicago y arrendar de inmediato otro edificio, tiene un valor
         esperado de 0.75 × 3 450 000 + 0.25 × 1 500 000 = 2 962 500 dólares.
             Por último, la tercera opción de mudarse al Oeste medio en seguida tiene un valor esperado de 0.75 ×
         3 500 000 + 0.25 × 2 000 000 = 3 125 000 dólares.
             Con base en lo anterior, parece que la mejor alternativa es permanecer en Chicago y arrendar otro
         edificio de inmediato.

      PREGUNTAS DE REPASO Y DISCUSIÓN
         1. ¿Qué problemas de capacidad surgen cuando un nuevo fármaco es introducido al mercado?
         2. Enumere algunos límites prácticos para las economías de escala, es decir, ¿cuándo debe dejar de
            crecer una planta?
         3. ¿Cuáles son algunos de los problemas del equilibrio de la capacidad que afrontan las organizaciones
            o las instalaciones siguientes?
            a) La terminal de una línea aérea.
            b) El centro de cómputo de una universidad.
            c) Un fabricante de ropa.
         4. ¿Cuáles son algunas de las consideraciones más importantes en torno a la capacidad en el caso de un
            hospital? ¿En qué difieren de las de una fábrica?
         5. La administración puede optar por aumentar la capacidad anticipándose a la demanda o en respuesta a
            la demanda creciente. Mencione las ventajas y las desventajas de los dos planteamientos.
         6. ¿Qué quiere decir equilibrio de la capacidad? ¿Por qué es difícil de lograr? ¿Qué métodos se utilizan
            para atacar los desequilibrios de la capacidad?
                                               ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD          capítulo 5   137

  7. ¿Cuáles son algunas razones que llevan a una planta a tener un colchón de capacidad? ¿Qué puede
     decir de un colchón negativo de capacidad?
  8. A primera vista, parecería que los conceptos de la fábrica enfocada y la flexibilidad de la capacidad se
     contraponen. ¿Lo hacen en realidad?


PROBLEMAS
  1. AlwaysRain Irrigation, Inc., quiere establecer la capacidad que requerirá en los próximos cuatro años.
     En la actualidad cuenta con dos líneas de producción de rociadores de bronce y de plástico. Los
     rociadores de bronce y los de plástico vienen en tres presentaciones: rociadores con boquilla de 90
     grados, rociadores con boquilla de 180 grados y rociadores con boquilla de 360 grados. La gerencia
     ha pronosticado la demanda siguiente para los próximos cuatro años:

                                                    Demanda anual

                                1 (en miles)       2 (en miles)    3 (en miles)     4 (en miles)

         Plástico 90                 32                44              55                56
         Plástico 180                 15               16               17               18
         Plástico 360                50                55              64                67
         Bronce 90                      7               8                9               10
         Bronce 180                     3               4                5                6
         Bronce 360                    11              12               15               18


     Las dos líneas de producción pueden fabricar todos los tipos de boquillas. Cada máquina de bronce
     requiere dos operadores y puede producir un máximo de 12 000 rociadores. La moldeadora de inyec-
     ción de plástico requiere cuatro operadores y puede producir un máximo de 200 000 rociadores. La
     compañía tiene tres máquinas de bronce y sólo una moldeadora de inyección. ¿Qué capacidad reque-
     rirá para los próximos cuatro años?
  2. Suponga que el departamento de marketing de AlwaysRain Irrigation iniciará una campaña intensiva
     de los rociadores de bronce, que son más caros pero también duran más que los de plástico. La deman-
     da pronosticada para los próximos cuatro años es:

                                                    Demanda anual

                                1 (en miles)       2 (en miles)    3 (en miles)     4 (en miles)

         Plástico 90                 32                44              55                56
         Plástico 180                 15               16               17               18
         Plástico 360                50                55              64                67
         Bronce 90                     7               15              18                23
         Bronce 180                    3                5                6                9
         Bronce 360                   15                6                7               20


     ¿Cuáles son las implicaciones que la campaña de marketing tiene para la capacidad?
  3. Anticipándose a la campaña publicitaria, AlwaysRain compró una máquina adicional de bronce. ¿Bas-
     tará para garantizar que la empresa tenga capacidad suficiente?
  4. Suponga que los operadores cuentan con bastante preparación para operar las máquinas de bronce
     y la moldeadora de inyección de los rociadores de plástico. En la actualidad, AlwaysRain tiene 10
     empleados de este tipo. Anticipándose a la campaña publicitaria descrita en el problema 2, la gerencia
     autorizó la compra de dos máquinas adicionales de bronce. ¿Cuáles son las implicaciones para la mano
     de obra que requerirá?
  5. Expando, Inc., está considerando la posibilidad de construir una fábrica adicional que produciría una
     nueva adición a su línea de productos. En la actualidad, la compañía está considerando dos opciones.
     La primera es una instalación pequeña cuya edificación costaría 6 millones de dólares. Si la demanda
     de los nuevos productos es floja, la compañía espera recibir 10 millones de dólares en forma de ingre-
     sos descontados (valor presente de ingresos futuros) con la fábrica pequeña. Por otro lado, si la deman-
     da es mucha, espera 12 millones de dólares por concepto de ingresos descontados utilizando la fábrica
     pequeña. La segunda opción es construir una fábrica grande con un costo de 9 millones de dólares. Si
     la demanda fuera poca, la compañía esperaría 10 millones de dólares de ingresos descontados con la
138   sección 2     PROCESOS


            planta grande. Si la demanda es mucha, la compañía estima que los ingresos descontados sumarían 14
            millones de dólares. En los dos casos, la probabilidad de que la demanda sea mucha es 0.40 y la pro-
            babilidad de que sea poca es 0.60. El hecho de no construir una nueva fábrica daría por resultado que
            no se generaran ingresos adicionales porque las fábricas existentes no podrían producir estos nuevos
            productos. Construya un árbol de decisión que ayude a Expando a tomar la mejor decisión.
         6. Una constructora ha encontrado un terreno que quiere adquirir para construir en él más adelante. En la
            actualidad, el terreno está clasificado para contener cuatro casas por acre, pero ella está pensando so-
            licitar un cambio de clasificación. Lo que ella construya dependerá de la autorización del cambio que
            piensa solicitar y del análisis que usted haga de este problema para aconsejarla. Con la información de
            ella y la intervención de usted, el proceso de decisión ha quedado reducido a los costos, las alternativas
            y las probabilidades siguientes:
                  Costo del terreno: 2 millones de dólares.
                  Probabilidad de cambio de clasificación: 0.60.
                  Si el terreno es reclasificado habrá 1 millón de dólares de costos adicionales por concepto de nue-
                  vos caminos, alumbrado, etcétera.
                 Si el terreno es reclasificado, el contratista debe decidir si construye un centro comercial o 1 500
            departamentos, como un plan tentativo muestra que se podría hacer. Si ella construye un centro co-
            mercial, existe 70% de probabilidad de que lo pueda vender a una cadena de tiendas de departamentos
            por 4 millones de dólares más que su costo de construcción, excluyendo el costo del terreno; y existe
            30% de probabilidad de que lo pueda vender a una compañía aseguradora por 5 millones de dólares
            más por encima de su costo de construcción (también excluyendo el terreno). En cambio, si en lugar
            del centro comercial decide construir los 1 500 departamentos, su cálculo de las probabilidades de
            utilidad son: 60% de probabilidad de que pueda vender los departamentos a una compañía de bienes
            raíces por 3 000 dólares cada uno por encima de su costo de construcción; 40% de probabilidad de
            que sólo pueda obtener 2 000 dólares de cada uno sobre su costo de construcción (los dos excluyen el
            costo del terreno).
                 Si el terreno no es reclasificado, ella cumplirá con las restricciones existentes de la clasificación
            actual y simplemente construirá 600 casas, en cuyo caso espera ganar 4 000 dólares sobre el costo de
            construcción por cada una (excluyendo el costo del terreno).
                 Prepare un árbol de decisión del problema y determine la mejor solución y la utilidad neta esperada.
         7. Si el rédito por elegir la máquina A es de 40 500 dólares con una probabilidad de 90% y el rédito por
            elegir la máquina B es de 80 000 dólares con una probabilidad de 50%, ¿cuál máquina escogería si su
            objetivo es maximizar el rédito?
         8. Si el mejor índice de operación de una máquina es de 400 unidades por hora y la capacidad real utili-
            zada durante una hora es de 300 unidades, ¿cuál es el índice de utilización de la capacidad?
         9. Una compañía tiene una licencia que le otorga el derecho de buscar petróleo en un terreno determina-
            do. Puede vender la licencia por 15 000 dólares y permitir que otra compañía corra el riesgo o puede
            perforar con la esperanza de encontrar petróleo y/o gas. A continuación se presentan los cuatro resul-
            tados posibles de la perforación, así como la probabilidad de que ocurran y los réditos:

                             Resultado posible                Probabilidad          Rédito

                             Pozo seco                             0.16            −$100 000

                             Pozo sólo de gas                      0.40               50 000

                             Combinación de petróleo y gas         0.24              100 000

                             Pozo de petróleo                      0.20              200 000


            Prepare un árbol de decisión para este problema. ¿La compañía debería perforar o vender la licencia?
        10. Plastic Production Company necesita expandir su capacidad de producción. Lo puede hacer de dos
            maneras: utilizar horas extra en su planta actual o arrendar otra planta. Las horas extra tienen una
            penalización en los costos (sobre el tiempo normal) de 3 dólares por caja de producto fabricada y sólo
            se pueden utilizar por un máximo de 15 000 cajas al año. Arrendar otra planta entrañaría un costo
            anual fijo de arrendamiento de 25 000 dólares; sin embargo, se remuneraría a los trabajadores de esta
            planta con base en tiempo normal y podría producir un número cualquiera de cajas hasta un máximo
            de 20 000 al año.
                La compañía estima que la demanda adicional (más allá de lo que puede producir en su planta ac-
            tual en tiempo normal) puede adoptar los valores siguientes, con las probabilidades correspondientes:

                                               ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD              capítulo 5                             139

                                    Demanda adicional
                                    (cajas por año)           Probabilidad

                                            5 000                   0.3
                                           10 000                   0.5
                                           15 000                   0.5


        Prepare un árbol de decisión para este problema y encuentre la decisión óptima para minimizar los
        costos esperados.


C A S O : SHOULDICE HOSPITAL. UN CORTE SUPERIOR7
“Shouldice Hospital, la casa construida por hernias, es una casa de       área de Toronto que acudan a la clínica
campo modificada que imprime al hospital el atractivo de ‘un club         para un diagnóstico. Los estudios se
de campo’.”                                                               hacen entre las 9 a.m. y las 3:30 p.m.,
                                   Cita de American Medical News          de lunes a viernes, y de 10 a.m. a 2 p.m.
                                                                          los sábados. A los pacientes que no vi-
Shouldice Hospital de Canadá es muy conocido por una cosa: ¡la
                                                                          ven en la ciudad se les envía por correo        Excel: Shouldice
reparación de hernias! De hecho, es la única operación que hace y
                                                                          un cuestionario para que proporcionen
hace muchas de ellas. En los pasados 20 años este pequeño hospital                                                            Hospital
                                                                          la información médica (que también
de 90 camas ha registrado un promedio de 7 000 operaciones al año.
                                                                          está disponible en Internet) que se ne-
El año pasado fue un año récord y realizó cerca de 7 500 operacio-
                                                                          cesita para el diagnóstico. Se niega el tratamiento a un pequeño por-
nes. Los nexos de los pacientes con Shouldice no terminan cuando
                                                                          centaje de los pacientes que están pasados de peso o que representan
abandonan el hospital. Cada año, la cena de gala Hernia Reunión
                                                                          algún otro riesgo médico impropio. Los pacientes restantes reciben
(con una revisión gratis de hernias) atrae a más de mil ex pacientes,
                                                                          tarjetas de confirmación con la fecha que se ha programado para su
algunos llevan asistiendo al evento más de 30 años.
                                                                          operación. El expediente del paciente se envía al escritorio de recep-
     Una serie de características destacadas del sistema de Shouldice
                                                                          ción una vez que se confirma la fecha de admisión.
para brindar sus servicios contribuye a su éxito. 1) Shouldice sólo
                                                                              Los pacientes se presentan en la clínica entre la 1 y las 3 p.m. del
acepta pacientes que tienen hernias externas poco complicadas y
                                                                          día anterior a la intervención. Tras una breve espera, se someten a un
utiliza una técnica superior inventada por el doctor Shouldice du-
                                                                          breve estudio preoperatorio. A continuación se les envía con un em-
rante la Segunda Guerra Mundial para este tipo de hernia. 2) Los
                                                                          pleado de admisiones para que realicen los trámites correspondientes.
pacientes son sometidos muy pronto al tratamiento con movimiento,
                                                                          Después, los pacientes acuden a una de las dos estaciones de enfer-
lo cual propicia su curación. (Los pacientes literalmente salen cami-
                                                                          mería para que les hagan análisis de sangre y de orina y, después, son
nando de la mesa de operaciones y practican un ejercicio ligero a lo
                                                                          acompañados a su habitación. Pasan el tiempo restante previo a la
largo de toda su estadía, que sólo dura tres días.) 3) Su ambiente de
                                                                          orientación acomodando sus cosas y conociendo a sus compañeros
club de campo, el amable personal de enfermería y la socialización
                                                                          de habitación.
inherente hacen que sea una experiencia asombrosamente agrada-
                                                                              La orientación empieza a las 5 p.m. y después se sirve la cena
ble, derivada de un problema médico inherentemente desagradable.
                                                                          en el comedor general. Esa misma noche, a las 9 p.m., los pacientes
Se apartan horarios regulares para tomar té y galletas, y para so-
                                                                          se reúnen en un salón para tomar té y galletas. Así, los nuevos pa-
cializar. Todos los pacientes están en pareja con un compañero de
                                                                          cientes pueden charlar con los que ya han sido operados. La hora de
cuarto que tiene antecedentes e intereses similares.
                                                                          dormir es entre las 9:30 y las 10 p.m.
EL SISTEMA DE PRODUCCIÓN                                                      El día de la operación, los pacientes que son intervenidos tem-
Las instalaciones médicas de Shouldice son cinco quirófanos, una          prano son despertados a las 5:30 a.m. para sedarlos antes de la inter-
sala de recuperación, un laboratorio y seis habitaciones para revisio-    vención. Las primeras operaciones inician a las 7:30 a.m. Poco antes
nes. Shouldice realiza, en promedio, 150 operaciones por semana y         de que empiece la operación, se administra al paciente anestesia
los pacientes por lo general permanecen tres días en el hospital. Aun     local, dejándolo alerta y totalmente consciente de lo que ocurre. Al
cuando las operaciones sólo se realizan cinco días a la semana, el        término de la operación, se invita al paciente a que vaya caminando
resto del hospital opera de forma continua para atender a los pacien-     de la mesa de operaciones a una silla de ruedas cercana, que lo está
tes en recuperación.                                                      esperando para llevarlo a su habitación. Tras un breve periodo de re-
    Una operación en Shouldice Hospital la realiza uno de los 12 ci-      poso, se recomienda al paciente que se ponga de pie y haga ejercicio.
rujanos de tiempo completo, ayudado por uno de los siete cirujanos        A las 9 p.m. de ese mismo día, el paciente está en el salón tomando
auxiliares de medio tiempo. Los cirujanos por lo general toman una        té y galletas y charlando con los pacientes nuevos que acaban de
hora para prepararse y realizar cada operación de hernia y operan a       ingresar.
cuatro pacientes al día. La jornada del cirujano termina a las 4 p.m.,        Al día siguiente, se le aflojan los clips que unen la piel de la in-
aun cuando esperan estar de guardia nocturna cada 14 días y de fin        cisión y algunos otros se les quitan. Los restantes son retirados a la
de semana cada 10 semanas.                                                mañana siguiente, justo antes de dar de alta al paciente.
L A EXPERIENCIA EN SHOULDICE                                                  Cuando Shouldice Hospital empezó, la internación promedio en el
Cada paciente es sometido a exámenes preoperatorios antes de es-          hospital por una operación de hernia era de tres semanas. Hoy en
tablecer la fecha para su intervención. Se sugiere a los pacientes del    día, muchas instituciones son partidarias de la “cirugía el mismo
140                           sección 2      PROCESOS



ilustración 5.7               Operaciones con 90 camas (30 pacientes al día)

                                                                                         Camas requeridas

                                Día de admisión       Lunes        Martes       Miércoles      Jueves       Viernes       Sábado       Domingo
                                Lunes                   30           30             30
                                Martes                               30             30            30
                                Miércoles                                           30            30           30
                                Jueves                                                            30           30            30
                                Viernes
                                Sábado
                                Domingo                 30           30                                                                   30
                                  Total                 60           90             90            90           60            30           30




día” por diversas razones. Shouldice Hospital cree decididamente          que ingresaron en un día dado. Las columnas indican el número de
que esto no es lo que más conviene a los pacientes y está convencido      pacientes que hubo en el hospital un día dado. Por ejemplo, el primer
de su proceso de tres días. El programa de rehabilitación postopera-      renglón de la tabla muestra que 30 personas ingresaron el lunes y
toria de Shouldice está diseñado para que el paciente pueda reanudar      permanecieron en el hospital lunes, martes y miércoles. Si se suman
sus actividades normales con un mínimo de interrupción y malestar.        las columnas de la tabla que corresponden al miércoles, se encontra-
Los pacientes de Shouldice con frecuencia regresan a trabajar en          rá que ese día había 90 pacientes internados en el hospital.
unos cuantos días, con un tiempo total promedio de ocho días.
    “Es interesante señalar que, de cada cien pacientes de Shouldi-             1. ¿Qué tan bien está utilizando el hospital actualmente sus
ce, uno es un médico”.                                                             camas?
                                                                                2. Prepare una tabla similar para mostrar los efectos que ten-
P LANES FUTUROS                                                                    dría añadir operaciones los sábados. (Suponga que de cual-
La gerencia de Shouldice está pensando en expandir la capacidad                    quier manera se realizarían 30 operaciones cada día.) ¿Cómo
del hospital para poder cubrir una cantidad considerable de deman-                 afectaría esto la utilización de la capacidad de camas? ¿Esta
da que en la actualidad no cubre. Para tal efecto, el vicepresidente               capacidad bastaría para los pacientes adicionales?
está considerando seriamente dos opciones. La primera implica aña-              3. Ahora analice el efecto de un incremento de 50% en el nú-
dir un día más de operaciones (sábados) al calendario actual de cin-               mero de camas. ¿Cuántas operaciones podría realizar el
co días, lo cual incrementaría la capacidad en 20%. La otra opción                 hospital al día antes de quedarse sin capacidad de camas?
es añadir otro piso de habitaciones al hospital, incrementando 50%                 (Suponga que las operaciones se realizan cinco días a la se-
el número de camas. Esto requeriría una programación más intensa                   mana, con el mismo número de operaciones cada día.) ¿Los
de los quirófanos.                                                                 nuevos recursos cómo se utilizarían en comparación con la
    Sin embargo, al administrador del hospital le preocupa cómo                    actual operación? ¿El hospital de hecho podría realizar esta
podría conservar el control de la calidad de los servicios brindados.              cantidad de operaciones? ¿Por qué? (Pista: Analice la capa-
Considera que el hospital ya se está utilizando debidamente. Los                   cidad de los 12 cirujanos y los cinco quirófanos.)
médicos y el personal están contentos con su trabajo y los pacientes            4. Aun cuando los datos financieros son muy generales, un
están satisfechos con el servicio. En su opinión, una mayor expan-                 cálculo realizado por una constructora indica que sumar ca-
sión de la capacidad dificultaría la posibilidad de mantener el mismo              pacidad de camas costaría alrededor de 100 000 dólares por
tipo de relaciones y actitudes laborales.                                          cama. Además, el monto cobrado por la cirugía de hernia
                                                                                   varía entre 900 dólares y 2 000 dólares, con un promedio de
PREGUNTAS                                                                          1 300 dólares por operación. Los cirujanos reciben 600 dó-
                                                                                   lares cerrados por operación. Debido a la incertidumbre por
La ilustración 5.7 es una tabla de la ocupación de habitaciones con                las leyes relativas a los servicios de salud, Shouldice querría
el sistema existente. Cada renglón de la tabla sigue a los pacientes               justificar una expansión dentro de un periodo de cinco años.




                              BIBLIOGRAFÍA SELECCIONADA
             Amran, M y N. Kulatilaka, “Disciplined Decisions: Aligning Stra-     Bakke, N.A. y R. Hellberg, “The Challenges of Capacity Planning”.
                 tegy with the Financial Markets”, Harvard Business Review,           International Journal of Production Economics, 30-31, 1993,
                 enero-febrero de 1999, pp. 95-104.                                   pp. 243-264.
                                                   ADMINISTRACIÓN ESTRATÉGICA DE LA CAPACIDAD                 capítulo 5                             141

               Correll, J.G. y N.W. Edson, Gaining Control: Capacity Management        Hammesfahr, R.D. Jack; J.A. Pope y A. Ardalan, “Strategic Planning
                     and Scheduling, 2a. ed. Nueva York: Wiley, 1998.                      for Production Capacity”, International Journal of Operations
               Giffi, C., A.V. Roth, y G.M. Seal, eds. Competing in World-Class            and Production Management 13, núm. 5 (1993), pp. 41-53.
                     Manufacturing: National Center for Manufacturing Sciences.        Meyer, C., Fast Cycle Time: How to Align Purpose, Strategy, and
                     Homewood, IL: Business One-Irwin, 1990.                               Structure for Speed, Nueva York: Free Press, 1993.
               Govil M. y J. Proth, Supply Chain Design and Management, Bur-           Yu-Lee, R.T., Essentials of Capacity Management, Nueva York: Wi-
                     lington, MA., Academic Press, 2001.                                   ley, 2002.




NOTAS
1.   Para reunir estadísticas de la capacidad, el análisis del Bureau of Economic Analysis plantea dos preguntas a las em-
     presas encuestadas: 1) ¿Cuál fue el porcentaje de la capacidad de producción al que su empresa operó en (mes y año)?
     2) ¿A qué porcentaje de capacidad de producción en (mes y año) habría querido operar su compañía para obtener una
     utilidad máxima o para alcanzar otro objetivo? Véase “Survey of Current Business”, una publicación anual de U.S.
     Department of Commerce Journal.
2.   W. Skinner, “The Focused Factory”, Harvard Business Review, mayo-junio de 1974, pp. 113-121.
3.   Véase R.J. Schonberger, “The Rationalization of Production”, Proceedings of the 50th Anniversary of the Academy of
     Management (Chicago: Academy of Management, 1986), pp. 64-70.
4.   El capítulo 8A habla de las líneas de espera.
5.   J. Haywood-Farmer y J. Nollet, Services Plus: Effective Service Management (Boucherville, Quebec, Canadá, G.
     Morin Publisher Ltd., 1991), p. 58.
6.   Ibid.
7.   Encontrará el Shouldice Hospital en http://www.shouldice.com. El sito Web contiene mucha información adicional
     en torno a la historia de los hospitales y sus procedimientos actuales para las operaciones de hernias.
