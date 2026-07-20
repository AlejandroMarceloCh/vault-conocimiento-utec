---
curso: FUNDOPS
titulo: Lectura Principios de Administración de Operaciones-7ma Heizer - 319-345 - Capacidad
slides: 27
fuente: Lectura Principios de Administración de Operaciones-7ma Heizer - 319-345 - Capacidad.pdf
---

                                                    SUPLEMENTO                                       7
Planeación
de la capacidad

Esquema del suplemento
Capacidad 288                                        Resumen 305
   Capacidad de diseño y capacidad efectiva          Términos clave 305
      289                                            Uso de software para el análisis del punto de
   Capacidad y estrategia 290                            equilibrio 305
   Consideraciones de la capacidad 290               Problemas resueltos 306
   Manejo de la demanda 291                          Autoevaluación 308
   Manejo de la demanda y la capacidad               Ejercicios para el estudiante 308
      en el sector servicios 293                     Preguntas para análisis 308
Planeación de la capacidad 295                       Problemas 309
                                                     Caso en video: Planeación de la capacidad en
Análisis del punto de equilibrio 296
                                                         el hospital Arnold Palmer 312
  Caso de un solo producto 298
                                                     Estudios de casos adicionales 312
  Caso de productos múltiples 298
                                                     Bibliografía 313
Aplicación de árboles de decisión                    Recursos en internet 313
a las decisiones de capacidad 300
Aplicación del análisis de inversión
a las inversiones impulsadas por la
estrategia 301
    Inversión, costo variable y flujo de efectivo
        302
    Valor presente neto 302




Objetivos de aprendizaje
Al terminar este suplemento, usted será capaz de
  1. Definir capacidad                                 4. Aplicar árboles de decisión a las
  2. Determinar la capacidad de diseño, la                decisiones de capacidad
     capacidad efectiva, y la utilización              5. Calcular el valor presente neto
  3. Calcular el punto de equilibrio



                                                                                                         287
288        Suplemento 7 • Planeación de la capacidad

 Cuando se diseña una sala
de conciertos, la administración
espera que la capacidad
pronosticada (la mezcla de
productos ópera, sinfonía y
eventos especiales y la
tecnología necesaria para
realizar estos eventos) sea
precisa y adecuada para operar
por encima del punto de
equilibrio. Sin embargo, en
muchas salas de conciertos, aun
cuando operan a toda su
capacidad, no logran el punto de
equilibrio y deben obtener
fondos suplementarios.




                                    CAPACIDAD
                                    ¿Cuántos asistentes debe alojar una sala de conciertos? ¿Cuántos clientes por día debe ser capaz de
                                    atender un Olive Garden o un Hard Rock Café? ¿Cuántas computadoras debe producir la planta
                                    de Dell basada en Nashville en un turno de 8 horas? ¿Y cómo debemos construir instalaciones para
                                    satisfacer estas demandas inciertas?
                                        Después de realizar la selección de un proceso de producción (capítulo 7), necesitamos determinar
Capacidad                           la capacidad. La capacidad es el “volumen de producción” (throughput) o número de unidades que
“Volumen de producción              puede alojar, recibir, almacenar o producir una instalación en un periodo de tiempo específico de
(throughput)” o número de           tiempo. A menudo, la capacidad determina los requerimientos de capital y, por consiguiente, una gran
unidades que puede alojar,          parte del costo fijo. La capacidad también determina si se cumplirá la demanda o si las instalaciones
recibir, almacenar o producir una   estarán desocupadas. Si la instalación es demasiado grande, algunas de sus partes estarán ociosas y
instalación en un periodo de        agregarán costos a la producción existente. Si la instalación es demasiado pequeña, se perderán
tiempo específico de tiempo.        clientes y quizá mercados completos. Por lo tanto, la determinación del tamaño de las instalaciones,
                                    con el objetivo de alcanzar altos niveles de utilización y un elevado rendimiento sobre la inversión,
                                    resulta crítica.
Objetivo de aprendizaje                 La planeación de la capacidad puede verse en tres horizontes de tiempo. En la figura S7.1 se observa
                                    que la capacidad a largo plazo (mayor a 1 año) es una función de agregar instalaciones y equipos que
1. Definir capacidad                tienen un tiempo de entrega largo. En el plazo intermedio (3 a 18 meses) podemos agregar equipo,
                                    personal y turnos; podemos subcontratar, y almacenar o utilizar el inventario. Ésta es la tarea de la
                                    planeación agregada. En el corto plazo (por lo general hasta 3 meses), la mayor preocupación consiste
                                    en programar los trabajos y las personas, así como asignar maquinaria. En el corto plazo es difícil
                                    modificar la capacidad; se usa la capacidad que ya existe.

 Figura S7.1
                                                                          Agregar instalaciones.
                                            Planeación a largo plazo
Tipos de planeación en un
horizonte de tiempo
                                                                          Agregar equipo con tiempo de
                                                                          entrega largo.                      *
                                                                          Subcontratar.                           Agregar personal.
                                         Planeación a mediano plazo       Agregar equipo.                         Construir o utilizar el
                                         (planeación agregada)            Agregar turnos.                         inventario.

                                                                                                                  Programar trabajos.
                                           Planeación a corto plazo
                                           (programación)                                                 *       Programar personal.
                                                                                                                  Asignar maquinaria.
                                                                                 Modificar la capacidad               Utilizar la capacidad

                                                                                              * Existen posibilidades limitadas
                                                                                                                         Capacidad       289

Capacidad de diseño y capacidad efectiva
La capacidad de diseño es la producción teórica máxima de un sistema en un periodo dado bajo                  Capacidad de diseño
condiciones ideales. Normalmente se expresa como una tasa, como el número de toneladas de acero               Producción teórica máxima de un
que se pueden producir por semana, por mes o por año. Para muchas compañías, medir la capacidad               sistema en un periodo dado bajo
resulta sencillo: es el número máximo de unidades producidas en un tiempo específico. Sin embargo,            condiciones ideales.
para otras organizaciones, determinar la capacidad puede ser más difícil. La capacidad se puede medir
en términos de camas (un hospital), miembros activos (una iglesia) o tamaño de los salones de clase
(una escuela). Otras organizaciones usan el tiempo de trabajo total disponible como medida de su
capacidad global.
    La mayoría de las organizaciones operan sus instalaciones a una tasa menor que la capacidad de
diseño. Lo hacen porque han encontrado que pueden operar con más eficiencia cuando no tienen que
extender sus recursos hasta el límite. En vez de esto, prefieren operar quizá a un 82% de la capacidad
de diseño. Este concepto se denomina capacidad efectiva.
    La capacidad efectiva es la capacidad que una empresa espera alcanzar dadas las restricciones             Capacidad efectiva
operativas actuales. A menudo la capacidad efectiva es menor que la capacidad diseñada debido a que           Capacidad que espera lograr una
la instalación puede haber sido diseñada para una versión anterior del producto o para una mezcla de          compañía, dados su mezcla de
productos diferente que la que se produce actualmente.                                                        productos, sus métodos de
    Dos medidas del desempeño del sistema son particularmente útiles: la utilización y la eficiencia.         programación, su mantenimiento
La utilización es simplemente el porcentaje de la capacidad de diseño que realmente se logra. La efi-         y sus estándares de calidad.
ciencia es el porcentaje de la capacidad efectiva que se alcanza en realidad. Dependiendo de la forma
                                                                                                              Utilización
en que se usen y administren las instalaciones, puede ser difícil o imposible alcanzar el 100% de efi-        Producción real como porcentaje
ciencia. Los administradores de operaciones tienden a ser evaluados con base en la eficiencia. La             de la capacidad de diseño.
clave para mejorar la eficiencia se encuentra frecuentemente en la corrección de los problemas de cali-
dad, así como en una programación, capacitación y mantenimiento efectivos. A continuación se calculan         Eficiencia
la utilización y la eficiencia:                                                                               Producción real como porcentaje
                                                                                                              de la capacidad efectiva.
                          Utilización = Producción real/Capacidad de diseño                          (S7-1)

                           Eficiencia = Producción real/Capacidad efectiva                           (S7-2)

   En el ejemplo S1 se determinan estos valores.


 Sara James Bakery tiene una planta procesadora de panecillos Deluxe para el desayuno y quiere enten-          EJEMPLO S1
 der mejor su capacidad. Determine la capacidad de diseño, la utilización y la eficiencia para esta planta
 al producir este panecillo Deluxe.                                                                            Determinación de la
 Método: La semana pasada la instalación produjo 148,000 panecillos. La capacidad efectiva es de
 175,000 unidades. La línea de producción opera 7 días a la semana en tres turnos de 8 horas al día. La
                                                                                                               utilización de la
 línea fue diseñada para procesar los panecillos Deluxe, rellenos de nuez y con sabor a canela, a un tasa      capacidad y
 de 1,200 por hora. La empresa calcula primero la capacidad de diseño y después usa la ecuación (S7-1)
 para determinar la utilización y la ecuación (S7-2) para determinar la eficiencia.
                                                                                                               de la eficiencia
 Solución:
 Capacidad de diseño = (7 días  3 turnos  8 horas)  (1,200 panecillos por hora) = 201,600 panecillos                 Modelo activo S7.1

             Utilización = Producción real/Capacidad de diseño = 148,000/201,600 = 73.4%
                                                                                                              El ejemplo S1 se ilustra con más
              Eficiencia = Producción real/Capacidad efectiva = 148,000/175,000 = 84.6%                       detalle en el modelo activo S7.1
 Razonamiento: La pastelería tiene ahora la información necesaria para evaluar la eficiencia.                 en su CD-ROM.
 Ejercicio de aprendizaje: Si la producción real es de 150,000, ¿cuál es la eficiencia? [Respuesta:
 85.7%].
 Problemas relacionados:        S7.1, S7.2, S7.4, S7.5, S7.11


La capacidad diseñada, la eficiencia y la utilización son medidas importantes para un administrador
de operaciones. Pero a menudo los administradores también necesitan conocer la producción esperada de
una instalación o de un proceso. Para lograrlo, se despeja la producción real (o en este caso futura o
esperada) como se muestra en la ecuación (S7-3).
                                                                                                              Objetivo de aprendizaje
                   Producción real (o esperada) = (Capacidad efectiva)(Eficiencia)                   (S7-3)
                                                                                                              2. Determinar la capacidad
    En ocasiones, a la producción esperada se le denomina capacidad tasada. Con el conocimiento de            de diseño, la capacidad
la capacidad efectiva y la eficiencia, un administrador puede encontrar la producción esperada de una         efectiva, y la utilización
instalación. Esto se muestra en el ejemplo S2.
290    Suplemento 7 • Planeación de la capacidad


 EJEMPLO S2                 La administradora de Sara James Bakery (vea el ejemplo S1) ahora necesita incrementar la producción
                            del cada vez más popular panecillo Deluxe. Para satisfacer la demanda, debe agregar una segunda línea
 Determinación de la        de producción.

 producción esperada        Método: La administradora debe determinar la producción esperada en esta segunda línea para el
                            departamento de ventas. La capacidad efectiva en la segunda línea es la misma que en la primera línea,
                            es decir, 175,000 panecillos Deluxe. Como se calculó en el ejemplo S1, la primera línea opera con una
                            eficiencia del 84.6%. Pero la producción en la segunda línea será menor debido a que el personal será
                            primordialmente de nueva contratación; así que se espera que la eficiencia no sea mayor al 75%. ¿Cuál
                            es la producción esperada entonces?
                            Solución:   Use la ecuación (S7-3) para determinar la producción esperada:
                                 Producción esperada = (Capacidad efectiva)(Eficiencia) = (175,000)(.75) = 131,250 panecillos
                            Razonamiento: Ahora se le puede decir al departamento de ventas que la producción esperada es de
                            131,250 panecillos Deluxe.
                            Ejercicio de aprendizaje: Después de un mes de capacitación, se espera que el personal de la
                            segunda línea de producción trabaje con una eficiencia del 80%. ¿Cuál es la producción esperada modi-
                            ficada de los panecillos Deluxe? [Respuesta: 140,000].
                            Problemas relacionados:          S7.3, S7.6, S7.7, S7.8, S7.10



                           Si la producción esperada es inadecuada podría necesitarse capacidad adicional. Gran parte del resto
                           de este suplemento se enfoca en cómo agregar esa capacidad de manera efectiva y eficiente.

                           Capacidad y estrategia
                           Las utilidades sostenidas provienen de la construcción de una ventaja competitiva, no sólo del buen
                           rendimiento financiero de un proceso específico. Las decisiones sobre la capacidad deben estar
                           integradas en la misión y la estrategia de la organización. Las inversiones no deben realizarse como
                           gastos aislados, sino como parte de un plan coordinado para colocar a la empresa en una posición ven-
                           tajosa.1 Las preguntas que deben hacerse son: ¿estas inversiones nos permitirán ganar clientes en
                           algún momento?, y ¿qué ventajas competitivas (como flexibilidad del proceso, velocidad de entrega,
                           mejoramiento de la calidad, etc.) obtendremos?
                              Las 10 decisiones de la administración de operaciones que se analizan en este texto, al igual que
                           otros elementos organizacionales como marketing y finanzas, resultan afectadas por los cambios en la
                           capacidad. El cambio en la capacidad tendrá implicaciones en las ventas y en el flujo de efectivo, de
                           la misma forma que tiene implicaciones en la calidad, la cadena de suministro, los recursos humanos
                           y el mantenimiento. Todo esto debe tomarse en cuenta.

                           Consideraciones de la capacidad
                           Además de la estrecha integración de la estrategia y las inversiones, existen cuatro consideraciones
                           especiales para tomar una buena decisión sobre la capacidad.
                            1. Pronosticar la demanda con exactitud: Un pronóstico preciso resulta esencial para tomar una
                               decisión sobre la capacidad. El nuevo producto puede ser gambas de ternera en el Olive Garden,
                               un platillo que agrega demanda en el servicio de comida del restaurante, o una nueva instalación
                               de maternidad en el hospital Arnold Palmer, o el nuevo modelo híbrido de Lexus. Cualquiera que
                               sea el nuevo producto, se deben determinar las perspectivas y el ciclo de vida de los productos
                               existentes. La administración debe saber cuáles productos se están agregando y cuáles desconti-
                               nuando, así como sus volúmenes esperados.
                            2. Entender la tecnología y los incrementos en la capacidad: El número de alternativas iniciales
                               puede ser grande, pero una vez que se establece el volumen, las decisiones sobre tecnología
                               pueden apoyarse en el análisis de costo, los recursos humanos necesarios, la calidad y la confia-
                               bilidad. Esta revisión suele reducir el número de alternativas a unas cuantas. La tecnología puede
                               dictar el incremento en la capacidad. Satisfacer la demanda adicional con algunas mesas más en
                               el Olive Garden tal vez no sea difícil, pero satisfacer el incremento en la demanda de un nuevo
                               automóvil agregando una nueva línea de ensamble en BMW puede resultar muy complicado y
                               caro. Los administradores de operaciones son responsables de la tecnología y del aumento co-
                               rrecto de la capacidad.
                            3. Encontrar el nivel de operación óptimo (volumen): La tecnología y los incrementos en la capaci-
                               dad suelen dictar el tamaño óptimo de una instalación. Un motel al borde de la carretera puede
                           1Para conocer un análisis excelente sobre inversiones que apoyan la ventaja competitiva, vea Terry Hill, Operations

                           Management, 2da. ed. (Nueva York: Palgrave Macmillan, 2005).
                                                                                                                             Capacidad       291

                                    Estructura de costos para un motel al borde de la carretera                    Figura S7.2
                                                     (sin alberca ni comedor)
                                                                                                                  Economías y deseconomías



                  Costo unitario promedio (dólares
                                                                                                                  de escala

                                                     Motel de 25                             Motel de 75
                                                     habitaciones         Motel de 50        habitaciones
                                                                          habitaciones




                     por habitación por noche)                 Economías          Deseconomías
                                                                de escala           de escala
                                                         25                  50                  75
                                                                    Número de habitaciones

    requerir 50 habitaciones para ser viable. Si es más pequeño, el costo fijo resulta excesivo; si es
    más grande, la instalación se vuelve más de lo que un solo gerente puede supervisar. Un óptimo
    hipotético para el motel se muestra en la figura S7.2. Este aspecto se conoce como economías y
    deseconomías de escala. Alguna vez GM consideró que la planta de automóviles óptima debía
    tener 600 empleados. Como sugiere la foto de Krispy Kreme, la mayoría de los negocios tienen
    un tamaño óptimo al menos hasta que aparezca alguien con un nuevo modelo de negocios.
    Durante décadas, las grandes fundidoras de acero integradas se consideraron óptimas. Hasta que
    surgieron Nucor, CMC y otras fundidoras pequeñas con un nuevo proceso y un nuevo modelo de
    negocios que cambió el tamaño óptimo para una fundidora de acero.
 4. Construir para el cambio: En nuestro acelerado mundo el cambio es inevitable, por lo que los
    administradores de operaciones integran la flexibilidad a las instalaciones y al equipo (vea la
    figura S7.3). Evalúan la sensibilidad de la decisión, probando varias proyecciones de ingresos
    tanto hacia arriba como hacia abajo, para definir los riesgos potenciales. A menudo, los edificios
    se construyen en fases; y el equipo se diseña teniendo en mente las modificaciones necesarias
    para adaptarse a cambios futuros en el producto, la mezcla de productos, y los procesos.
En lugar de manejar la capacidad en forma estratégica, los administradores pueden manejar la
demanda tácticamente.

Manejo de la demanda
Aún teniendo un buen pronóstico e instalaciones construidas de acuerdo con éste, puede haber una
correspondencia deficiente entre la demanda real y la capacidad disponible. Una correspondencia
deficiente significa que la demanda supera a la capacidad o que la capacidad excede a la demanda. Sin
embargo, en ambos casos las empresas tienen alternativas.

                                                                                                             En sus orígenes, Krispy Kreme
                                                                                                            tenía tiendas de 8,000 pies cuadrados,
                                                                                                            pero sus dueños descubrieron que
                                                                                                            resultaban demasiado grandes y
                                                                                                            costosas para muchos mercados.
                                                                                                            Entonces probaron con tiendas
                                                                                                            pequeñas de 1,300 pies cuadrados, las
                                                                                                            cuales requerían menos inversión, pero
                                                                                                            esos establecimientos resultaron
                                                                                                            demasiado pequeños como para
                                                                                                            proporcionar la experiencia de ver y
                                                                                                            oler una dona de Krispy Kreme
                                                                                                            mientras es preparada. Finalmente,
                                                                                                            Krispy Kreme acertó con una tienda de
                                                                                                            2,600 pies cuadrados. Ésta incluye una
                                                                                                            enorme ventana de cristal para poder
                                                                                                            ver la producción de las donas.
292         Suplemento 7 • Planeación de la capacidad

 Figura S7.3     Porcentaje de vehículos estadounidenses fabricados                                        100%
en líneas de ensamble flexibles*
                                                                                                            80%
Un porcentaje de automóviles cada vez más grande se fabrica en líneas de ensamble
flexibles. Por ejemplo, Chrysler descubrió hace varios años que su subutilizada planta                      60%
de Belvidere, Illinois, no era lo suficientemente flexible como para pintar un PT Cruiser
(que era demasiado alto por 1 pulgada). La compañía aprendió su lección y ahora es
                                                                                                            40%

                                                                                                                               Chrysler
líder en inversión para la flexibilidad del diseño.
*Estimación de 2007, The Wall Street Journal (11 de abril de 2006): A1 y (14 y 15 de junio de 2006): B14.
                                                                                                            20%       Nissan              Honda   G.M.   Toyota   Ford

                                                                                                                0



                                        La demanda excede a la capacidad Cuando la demanda excede a la capacidad, la empresa
                                        puede ser capaz de reprimir la demanda con el simple aumento de los precios, programando tiempos
                                        de entrega más largos (lo cual podría ser inevitable), y desestimulando otros negocios redituables mar-
                                        ginalmente. Sin embargo, como instalaciones inadecuadas reducen los ingresos más de lo aceptable,
                                        la solución de largo plazo suele ser el incremento de la capacidad (como lo vemos en el recuadro de
                                        AO en acción “Capacidad insuficiente en Dalrymple Bay”).


                                        La capacidad excede a la demanda Cuando la capacidad excede a la demanda, la empresa
                                        puede desear estimular la demanda mediante reducciones de precio o mercadotecnia agresiva, o puede
                                        adaptarse al mercado a través de cambios en el producto. Cuando la disminución de la demanda
                                        del cliente se combina con procesos viejos e inflexibles, pueden ser necesarios despidos y cierres de
                                        planta para poner a la capacidad en línea con la demanda. El recuadro de AO en acción “Demasiada
                                        capacidad en GM y Ford” indica qué tan difícil puede ser el ajuste de la capacidad para una demanda en
                                        declinación.


                                        Ajuste a las demandas estacionales Un patrón estacional o cíclico de demanda representa
                                        otro reto para la capacidad. En estos casos, la administración encuentra útil ofrecer productos con
                                        patrones de demanda complementarios es decir, productos para los que la demanda es alta para uno
                                        cuando es baja para el otro. Por ejemplo, en la figura S7.4 la empresa está agregando una línea de
                                        motores de motocicletas para nieve a su línea de motores de motocicletas para agua a fin de equilibrar
                                        la demanda. Al complementar sus productos adecuadamente, quizá suavice la utilización de las ins-
                                        talaciones, del equipo y del personal.




AO en acción                              Capacidad insuficiente en Dalrymple Bay

    Una mañana reciente, cerca de 20 barcos estaban ancla-                                    El plan actual consiste en invertir $610 millones de
    dos en el Coral Sea. Esperaban ser cargados con carbón                                dólares para expandir la capacidad del puerto a 85 mi-
    para surtir de combustible a las voraces fundidoras de                                llones de toneladas métricas de carbón en los siguientes
    acero ubicadas en Asia. Australia tiene algunas de las                                3 años. Pero esto sigue siendo menor al requerimiento de
    minas de carbón más prolíficas del mundo, pero su puerto                              la demanda estimada, que es de 107 millones de tonela-
    clave de Dalrymple Bay, justo a las afueras de Queensland,                            das métricas. Como resultado, las compañías de carbón,
    no es lo suficientemente grande como para satisfacer la                               incluso después de completar la expansión, pueden
    demanda. Por ello los barcos esperan desocupados durante                              encontrar que su acceso al embarque es limitado.
    días. La capacidad del puerto está muy por debajo de lo                                   La demanda debe existir, el puerto se debe expandir, y
    necesario para la demanda mundial actual. Esto hace de                                las minas se deben agrandar. Sin esa seguridad, el riesgo
    Dalrymple uno de los puntos que más retrasan el proceso.                              permanece alto y el RSI (rendimiento sobre la inversión)
       El proceso es bastante sencillo pero costoso. En las                               no existe. Los administradores no pondrán una cantidad
    minas, el carbón se carga en trenes, los cuales viajan                                significativa de dinero en la expansión de la capacidad del
    varias horas hasta el puerto y descargan su carbón en                                 puerto hasta que estén seguros de que tanto la demanda
    montones que se rocían con agua para evitar que el polvo                              como el suministro de carbón dan soporte a un puerto
    del carbón contamine casas y playas. En cierto tiempo, el                             más grande. Para justificar la inversión en capacidad,
    carbón se carga en una banda transportadora que lo                                    cada fase de la cadena debe soportar esa inversión.
    desplaza 2.5 millas hasta el Coral Sea, donde se sube a                               Fuente: Australasian Business Intelligence (22 de junio de 2006); y The
    los barcos.                                                                           Wall Street Journal (7 de julio de 2005): C1, C4.
                                                                                                                              Capacidad      293


AO en acción                                   Demasiada capacidad en GM y Ford

   Durante décadas GM y Ford agregaron capacidad a sus                         GM y Ford no se han rendido. En un esfuerzo por dis-
   plantas. El mercado de automóviles y camiones se expan-                 minuir costos, ambas compañías están aumentando su
   día, y estas compañías se expandían junto con él. Eran las              productividad y flexibilidad. Por ejemplo, en los últimos
   empresas automotrices más grandes del mundo. Cons-                      6 años, las horas de trabajo por vehículo necesarias para
   truyeron plantas especializadas enfocadas en el producto                el estampado, ensamble y producción de motores ha dis-
   con poca flexibilidad e hicieron crecer su capacidad a mi-              minuido en un 26%, de 46.5 a 34.3 horas. El número de
   llones de automóviles al año. Sólo GM producía más de la                máquinas de estampado necesarias para hacer los guar-
   mitad de los automóviles vendidos en Estados Unidos.                    dafangos, el toldo, las puertas, etc., han disminuido de 330
   Pero el mundo cambió, ahora los automóviles llegan a                    a 241. Esta potente combinación de ventas más bajas y
   Estados Unidos de todos los rincones del mundo. Alema-                  productividad más alta significa que GM y Ford deben
   nia, Italia, Japón, Corea e incluso México y Brasil están               reducir su capacidad. Para 2010, el empleo con estos dos
   entrando al mercado estadounidense con China en el hori-                fabricantes disminuirá en 50,000 personas. Los ajustes a
   zonte. Y GM ahora fabrica menos de un cuarto de los                     la capacidad, particularmente hacia abajo, pueden ser do-
   automóviles vendidos en Estados Unidos.                                 lorosos.
       Toyota, VW, Honda, BMW, Mercedes y otros están
   ganando ventas. Captan las ventas con importaciones y pro-
   ducción local. Recientemente, las plantas de Toyota basadas             Fuente: The Wall Street Journal (21 y 22 de enero de 2006): A2; The
   en Estados Unidos operaban al 111% de la producción es-                 Economist (7 de enero de 2006): 61; y Knight Ridder Tribune Business
   perada, con un 87% para GM y un 79% para Ford.                          News (4 de enero de 2006): 1.




Tácticas para ajustar la capacidad a la demanda Existen diferentes tácticas para ajustar la
capacidad a la demanda. Las alternativas de ajuste incluyen:
 1. Cambios en el personal (aumentar o disminuir el número de empleados o turnos).
 2. Ajustes al equipo (comprar maquinaria adicional o vender o rentar el equipo existente).
 3. Mejora de los procesos para aumentar la producción.
 4. Rediseño de los productos para facilitar más producción.
 5. Aumento de la flexibilidad del proceso para satisfacer de mejor manera las cambiantes preferen-
    cias de producto.
 6. Cierre de instalaciones.
Las tácticas anteriores sirven para ajustar la demanda a las instalaciones existentes. El asunto
estratégico es, por supuesto, cómo tener las instalaciones del tamaño correcto.

Manejo de la demanda y la capacidad en el sector servicios
En el sector servicios, la programación de clientes es el manejo de la demanda, y la programación de
la fuerza de trabajo es el manejo de la capacidad.

Manejo de la demanda Cuando la demanda y la capacidad tienen una buena correspondencia, a
menudo el manejo de la demanda puede realizarse con citas, reservaciones o una regla del tipo
primero en llegar-primero en ser atendido. En algunos negocios, como despachos legales o consultorios
médicos, el programa consiste en un sistema de citas y resulta adecuado. Los sistemas de reserva-
ciones funcionan bien en agencias para la renta de automóviles, hoteles y algunos restaurantes como



                                                                                                                     Figura S7.4
                                                                         Al combinar ambos
                                                                         patrones de demanda                        La capacidad se utiliza de




          Ventas en unidades
                               4,000
                                                                         se reduce la variación                     mejor manera si se
                               3,000                                                                                combinan productos con
                                                                             Ventas de motocicletas
                                                                                                                    patrones estacionales
                               2,000                                         para nieve
                                                                                                                    complementarios
                               1,000                                        Ventas de motocicletas                  Una demanda de ventas
                                                                            para agua                               suavizada contribuye a
                                                                                                                    mejorar la programación
                                       E FMAMJ J ASONDE FMAMJ J ASONDE                                              y las estrategias de recursos
                                                  Tiempo (meses)                                                    humanos.
294         Suplemento 7 • Planeación de la capacidad

 Muchos hospitales de Estados Unidos usan servicios
a distancia para manejar la capacidad de sus radiólogos
durante los turnos nocturnos. Night Hawk, un servicio
basado en Idaho con 50 radiólogos localizados en Zurich
y Sydney, tiene contrato con 900 instalaciones
(un 20% de todos los hospitales estadounidenses).
Estos expertos capacitados, completamente despiertos
en sus horas de trabajo diurno, suelen regresar un
diagnóstico en un lapso de entre 10 y 20 minutos, con
una garantía de 30 minutos.




                                      un medio para minimizar el tiempo de espera del cliente y evitar el desagrado de un servicio poco
                                      satisfactorio. En tiendas al menudeo, oficinas postales o restaurantes de comida rápida, una regla del
                                      tipo primero en llegar-primero en ser atendido para dar servicio a los clientes puede ser suficiente.
                                      Cada industria desarrolla sus propios métodos para lograr la correspondencia adecuada entre demanda
                                      y capacidad. Otros enfoques más agresivos para el manejo de la demanda incluyen muchas varia-
                                      ciones de descuentos: ofertas para “madrugadores” en restaurantes, descuentos para presentaciones
                                      matutinas o para conseguir asientos en las horas más desocupadas de una aerolínea, y llamadas tele-
                                      fónicas más baratas los fines de semana.


                                      Manejo de la capacidad Cuando el manejo de la demanda no es factible, una alternativa es
                                      manejar la capacidad a través de cambios en el personal de tiempo completo, eventual, o de tiempo
                                      parcial. Éste es el enfoque en muchos servicios. Por ejemplo, los hospitales pueden encontrar capaci-
                                      dad limitada por la falta de radiólogos certificados que quieran cubrir los turnos difíciles. Contar con
                                      lecturas radiológicas rápidas y confiables puede ser la diferencia entre la vida y la muerte de un
                                      paciente en la sala de emergencias. Como lo ilustra la fotografía de arriba, cuando se requiere una lec-
                                      tura durante la noche (y el 40% de las tomografías computarizadas (CT scans) se realizan durante las
                                      8 P.M. y las 8 A.M.), la imagen puede enviarse por correo electrónico a un médico residente en Europa
                                      o Australia para su análisis inmediato.

 La enorme flota aérea de FedEx se usa
casi a toda su capacidad para la entrega
nocturna de paquetes, pero está
desocupada al 100% durante el día. En un
intento por utilizar de mejor manera su
capacidad (y apalancar sus activos), FedEx
consideró la implementación de dos
servicios con patrones de demanda
opuestos o contracíclicos para su servicio
nocturno: servicio de conmutador para
pasajeros y servicio charter para pasajeros.
Sin embargo, después de un análisis
amplio, el 12 o el 13% del rendimiento
sobre la inversión se juzgó insuficiente
como para correr los riesgos involucrados.
Por otra parte, aunque enfrenta problemas
similares, UPS decidió iniciar operaciones
con una aerolínea de servicio charter que
opera los fines de semana.
                                                                                                                      Planeación de la capacidad      295

PLANEACIÓN DE LA CAPACIDAD
Establecer los requerimientos de capacidad futuros puede ser un procedimiento complicado, el cual se                                 Video S7.1
basa principalmente en la demanda futura. Cuando la demanda de bienes y servicios se puede pronos-
ticar con un grado de precisión razonable, la definición de los requerimientos de capacidad puede                          Planeación de la capacidad en el
resultar sencilla. Normalmente, la determinación de la capacidad requiere dos etapas. Durante la                           hospital Arnold Palmer
primera fase, la demanda futura se pronostica con los modelos tradicionales, como se vio en el capí-
tulo 4. En la segunda fase, este pronóstico se usa para determinar los requerimientos de capacidad y el
tamaño creciente de cada adición a la capacidad.2 Resulta interesante que el crecimiento de la
demanda suela ser gradual y en pequeñas unidades, mientras que las adiciones a la capacidad son por
lo general instantáneas y en unidades grandes. Con frecuencia, esta contradicción dificulta la expan-
sión de la capacidad.
    En la figura S7.5 se revelan cuatro enfoques para la nueva capacidad. Como se observa en la figu-
ra S7.5(a), la nueva capacidad se adquiere al principio del año 1. Esa capacidad servirá para manejar
el aumento de la demanda hasta iniciar el año 2. Al principio del año 2, se adquiere otra vez capacidad
nueva con el fin de que la organización se adelante a la demanda prevista hasta que comience el año 3.
Este proceso puede continuar de manera indefinida.
    El plan de capacidad que se muestra en la figura S7.5(a) es sólo uno del casi ilimitado número de
planes posibles para satisfacer la demanda futura. En esta figura, la nueva capacidad se adquirió en forma
incremental al inicio del año 1 y al inicio del año 2. En la figura S7.5(b), se adquirió un gran incremento
en la capacidad al comienzo del año 1 para satisfacer la demanda esperada hasta el inicio del año 3.
    El exceso de capacidad proporcionado por los planes de las figuras S7.5(a) y S7.5(b) da flexibili-
dad a los administradores de operaciones. Por ejemplo, en la industria hotelera, la capacidad agregada
en forma de habitaciones permite una mayor variedad de alternativas y quizá flexibilidad en la progra-
mación de la limpieza de las habitaciones. En la manufactura, el exceso de capacidad puede utilizarse
para hacer más preparaciones que permitan acortar las corridas de producción y, por ende, disminuir

             (a) Adelantarse a la demanda con                             (b) Adelantarse a la demanda                      Figura S7.5
                 una ampliación incremental                                   con una ampliación en un
                                                                              solo paso                                    Enfoques para la
                                      Demanda                                                  Demanda                     ampliación
                                      esperada                                                 esperada
                                                                                                                           de la capacidad
               Nueva
             capacidad


   Demanda                                                Demanda
                                                                      Nueva
                                                                    capacidad




                    1        2              3                                   1        2         3
                    Tiempo (años)                                               Tiempo (años)

             (c) Retrasarse con respecto a la                             (d) Intentar tener una capacidad
                 demanda mediante expansión                                   promedio que se iguale a la demanda
                 incremental                                                  con ampliación incremental
                                   Demanda
                                                                                                Demanda
                                   esperada
                                                                                                esperada
                     Nueva                                                Nueva
                   capacidad                                            capacidad

   Demanda                                                Demanda




                    1        2              3                                   1        2         3
                    Tiempo (años)                                               Tiempo (años)
2En este punto, suponemos que la administración conoce la tecnología y el tipo de instalaciones que se emplearán para

satisfacer los requerimientos de la demanda futura que no es un asunto menor, pero está fuera del alcance de este libro.
296        Suplemento 7 • Planeación de la capacidad

                                   el inventario. La capacidad adicional también puede permitir a la administración producir un inven-
                                   tario en exceso y, por consiguiente, demorar los gastos de capital y las interrupciones que implica
                                   agregar nueva capacidad adicional.3
                                       Las alternativas de las figuras S7.5(a) y S7.5(b), adelantan la capacidad es decir, adquieren la
                                   capacidad para mantenerse por delante de la demanda pero en la figura S7.5(c) se muestra una posi-
                                   bilidad que retrasa la capacidad, quizá usando tiempo extra o subcontratando para adaptarse al exce-
                                   dente de la demanda. En la figura S7.5(d) se busca igualar la demanda al construir una capacidad
                                   “promedio”, a veces retrasándose con respecto a la demanda y en otras adelantándose a ésta.
                                       En algunos casos, la decisión a tomar entre las distintas alternativas puede ser relativamente
                                   sencilla. Se puede calcular el costo total de cada alternativa y después seleccionar aquélla que tenga el
                                   menor costo total. En otros casos, la determinación de la capacidad y cómo lograrla puede ser algo
Objetivo de aprendizaje            mucho más complicado. La mayor parte de las veces, numerosos factores subjetivos resultan difíciles
                                   de cuantificar y medir. Estos factores incluyen alternativas tecnológicas; estrategias de la competen-
3. Calcular el punto de
                                   cia; restricciones en la construcción; costo de capital; alternativas de recursos humanos; así como
equilibrio
                                   leyes y regulaciones locales, estatales y federales.
Análisis del punto de
equilibrio                         ANÁLISIS DEL PUNTO DE EQUILIBRIO
Medio para encontrar el punto,
                                   El análisis del punto de equilibrio es una herramienta crucial para determinar la capacidad que debe
en dinero y unidades, donde los
costos son iguales a los
                                   tener una instalación a fin de lograr rentabilidad. El objetivo del análisis del punto de equilibrio es
ingresos.                          encontrar el punto, en dinero y unidades, donde el costo y el ingreso sean iguales. Este punto se llama
                                   punto de equilibrio. Las compañías deben operar por arriba de este nivel para lograr rentabilidad.
Costos fijos                       Como se muestra en la figura S7.6, el análisis del punto de equilibrio requiere una estimación de los
Costos que continúan igual         costos fijos, de los costos variables, y del ingreso.
incluso cuando no se producen          Los costos fijos son aquellos costos que continúan igual incluso cuando no se producen unidades.
unidades.                          Los ejemplos incluyen pagos por concepto de depreciación, impuestos, deudas e hipotecas. Los costos
                                   variables son los que varían con el volumen de unidades producidas. Los componentes principales de
Costos variables
                                   los costos variables son mano de obra y materiales. Sin embargo, otros costos, como la porción de los
Costos que varían con el
volumen de unidades
                                   suministros que varía con el volumen, también son costos variables. La diferencia entre el precio de
producidas.                        venta y los costos variables es la contribución. Sólo cuando la contribución total exceda al costo fijo
                                   total se tendrán utilidades.
Contribución                           Otro elemento incluido en el análisis del punto de equilibrio es la función de ingreso. En la figu-
Diferencia entre precio de venta   ra S7.6, el ingreso comienza en el origen y procede a subir hacia la derecha, incrementándose con el
y costos variables.                precio de venta de cada unidad. En el sitio donde la función de ingreso cruza la línea del costo total
                                   (la suma de los costos fijos y variables) está el punto de equilibrio, con un corredor de utilidad a la
Función de ingreso                 derecha y un corredor de pérdida hacia la izquierda.
Función que se incrementa con
el precio de venta de cada         Supuestos Cierta cantidad de supuestos representa el fundamento del modelo básico del punto de
unidad.                            equilibrio. Resulta notable que los costos y el ingreso se presenten como líneas rectas. Se muestran

 Figura S7.6
                                                                                                                                 Línea de ingreso total
Punto de equilibrio básico                                      900
                                                                                                                               s
                                                                800                                                         de
                                                                                                                          da
                                                                                                                    utili           Línea de costo total
                                                                                                               de
                                                                700
                                                                                                         d  or
                                                                        Punto de equilibrio:          rre



                                              Costo (dólares)
                                                                600   Costo total = Ingreso total   Co

                                                                500
                                                                                                                    Costo variable
                                                                400

                                                                300            r
                                                                            do as
                                                                200    o rre rdid
                                                                      C pé
                                                                      de
                                                                100                                                 Costo fijo


                                                                  0   100 200 300 400 500 600 700 800 900 1000 1100
                                                                                Volumen (unidades por periodo)
                                   3Vea un análisis relacionado en S. Rajagopalan y J. M. Swaminathan, “Coordinated Production Planning Model with

                                   Capacity Expansion and Inventory Management”, Management Science 47, núm. 11 (noviembre de 2001): 1562-1580.
                                                                                                                 Análisis del punto de equilibrio   297
con un incremento lineal es decir, en proporción directa con el volumen de unidades producidas. Sin
embargo, ni los costos fijos ni los costos variables (y por tal razón, ni la función de ingreso) necesitan
ser líneas rectas. Por ejemplo, los costos fijos cambian en la medida en que se usan más bienes de ca-
pital o más espacio de almacén; los costos de mano de obra cambian con el tiempo extra o si se
emplean trabajadores no calificados; la función de ingreso puede cambiar con factores como los des-                         Los costos fijos no
cuentos por volumen.                                                                                                        permanecen constantes
                                                                                                                            para todo el volumen;
Enfoque gráfico El primer paso en el enfoque gráfico para el análisis del punto de equilibrio es                            nuevos almacenes y
definir los costos que son fijos y sumarlos. Los costos fijos se trazan como una línea horizontal que                       nuevos cargos por gastos
comienza en la cantidad en dólares anotada sobre el eje vertical. Después se estiman los costos varia-                      generales resultan en
bles mediante el análisis de los costos por mano de obra, materiales y otros costos relacionados con la
                                                                                                                            funciones escalonadas
producción de cada unidad. Los costos variables se muestran como un costo creciente incremental,
cuyo origen está en la intersección de los costos fijos con el eje vertical y que aumenta con cada
                                                                                                                            para los costos fijos.
cambio suscitado en el volumen cuando nos movemos hacia la derecha sobre el eje del volumen (o eje
horizontal). Por lo general, la información de los costos fijos y variables está disponible en el departa-
mento de contabilidad de la empresa, aunque también el departamento de ingeniería industrial puede
almacenar información de costos.
Enfoque algebraico A continuación se muestran las fórmulas respectivas del punto de equilibrio
en unidades y dólares. Sean
    PEQx = punto de equilibrio en unidades                      IT = ingreso total = Px
    PEQ$ = punto de equilibrio en dólares                        F = costos fijos
       P = precio por unidad (después de todos los descuentos)   V = costos variables por unidad
       x = número de unidades producidas                       CT = costos totales = F + Vx
El punto de equilibrio ocurre cuando el ingreso total es igual a los costos totales. Por lo tanto:
                                        IT = CT         o   Px = F + Vx
    Al despejar x, se obtiene
                                                             F
                                                PEQx =
                                                            P−V
y
                                                             F          F
                                  PEQ $ = PEQx P =              P=
                                                            P−V    ( P − V )/P
                                                F
                                         =
                                             1 − V /P
                                Utilidad = IT − CT
                                         = Px − ( F + Vx ) = Px − F − Vx
                                         = (P − V ) x − F


                                                                     Algunas compañías se adaptan para un
                                                                    cambio en la capacidad modificando la
                                                                    maquinaria o utilizando equipo antiguo aunque no
                                                                    sea el más eficiente. Por ejemplo, los
                                                                    administradores de la empresa familiar que
                                                                    produce las mezclas de la marca Jiffy decidieron
                                                                    que la estrategia de AO de su compañía no
                                                                    contemplaba una inversión de capital adicional en
                                                                    nuevo equipo. En consecuencia, al hacer
                                                                    reparaciones, modificaciones de equipo o ajustes
                                                                    para las cargas pico, utilizan equipo de repuesto,
                                                                    a menudo antiguo.
298        Suplemento 7 • Planeación de la capacidad

                                   Mediante estas ecuaciones se despejan directamente el punto de equilibrio y la rentabilidad. Las dos
                                   fórmulas de interés particular son:

                                                                                                   Costo fijo total
                                                        Punto de equilibrio en unidades =                                               (S7-4)
                                                                                                Precio – Costo variable

                                                                                                   Costo fijo total
                                                           Punto de equilibrio en dólares =                                             (S7-5)
                                                                                                    Costo variable
                                                                                                 1−
                                                                                                    Precio de venta

                                   Caso de un solo producto
                                   En el ejemplo S3 se determina el punto de equilibrio en dólares y en unidades para un producto.



 EJEMPLO S3                         Stephens Inc., quiere determinar el volumen mínimo necesario en dólares y unidades para lograr el
                                    punto de equilibrio en su nueva instalación.
 Análisis del punto                 Método:     La compañía determina primero que en este periodo tiene costos fijos de $10,000. La mano
 de equilibrio para un              de obra directa cuesta $1.50 por unidad, y el material $.75 por unidad. El precio de venta unitario es de
                                    $4.00.
 solo producto
                                    Solución:    El punto de equilibrio en dólares se calcula de la siguiente manera:
         Archivo de datos para
         Excel OM                                                  F               $10,000            $10,000
         Ch07SExS3.xls                               PEQ$ =              =                          =         = $22,857.14
                                                              1 − (V /P ) 1 − [(1.50 + .75)/(4.00)]    .4375

                                        El punto de equilibrio en unidades es:
         Modelo activo S7.2
                                                                             F        $10,000
                                                                  PEQx =        =                    = 5,714
El ejemplo S3 se ilustra con más                                           P − V 4.00 − (1.50 + .75)
detalle en el modelo activo S7.2
                                    Observe que se utilizan los costos variables totales (es decir, mano de obra y material).
del CD-ROM.
                                    Razonamiento: Ahora la administración de Stephens Inc., ya tiene una estimación tanto en dólares
                                    como en unidades del volumen necesario para la nueva instalación.
                                    Ejercicio de aprendizaje: Si Stephens encuentra que el costo fijo se incrementará a $12,000, ¿qué
                                    le pasa al punto de equilibrio en unidades y en dólares? [Respuesta: El punto de equilibrio en unidades
                                    aumenta a 6,857, y el punto de equilibrio en dólares se incrementa a $27,428.57].
                                    Problemas relacionados:         S7.9, S7.12, S7.13, S7.14, S7.15, S7.16, S7.17, S7.18, S7.19, S7.20,
                                    S7.21, S7.22, S7.23



                                   Caso de productos múltiples
                                   La mayoría de las empresas, desde las manufactureras hasta los restaurantes (incluso restaurantes de
                                   comida rápida), tienen una variedad de ofertas. Cada producto ofrecido puede tener precio de venta y
                                   costo variable diferentes. Utilizando el análisis del punto de equilibrio, modificamos la ecuación (S7-5)
                                   para reflejar la proporción de las ventas de cada producto. Esto se hace “ponderando” la contribución
                                   de cada producto mediante su proporción de ventas. Entonces la fórmula es:
                                                                                           F
                                                                        PEQ$ =
                                                                                     ⎡⎛ V ⎞             ⎤                               (S7-6)
                                                                                 ∑   ⎢⎜ 1 − i ⎟ × (Wi ) ⎥
                                                                                     ⎢⎣⎝   Pi ⎠         ⎥⎦

                                   donde        V = costo variable por unidad
                                                P = precio por unidad
                                                F = costo fijo
                                                W = porcentaje de cada producto de las ventas totales en dólares
                                                 i = cada producto
                                   En el ejemplo S4 se muestra cómo determinar el punto de equilibrio para el caso de productos múlti-
                                   ples en el restaurante Le Bistro.
                                                                                                          Análisis del punto de equilibrio   299

                                                                       Las máquinas de papel como las que
                                                                      se muestran aquí, de International Paper,
                                                                      requieren una inversión de capital alta.
                                                                      Esta inversión resulta en un costo fijo
                                                                      alto, pero permite una producción de
                                                                      papel con costo variable muy bajo.
                                                                      El trabajo del gerente de producción es
                                                                      mantener la utilización por arriba del
                                                                      punto de equilibrio para lograr
                                                                      rentabilidad.




Le Bistro elabora más de un producto y le gustaría conocer su punto de equilibrio en dólares.                        EJEMPLO S4
Método:     La información de Le Bistro es como se muestra en la tabla siguiente. Los costos fijos son
de $3,500 al mes.                                                                                                    Análisis del punto
                                                                                                                     de equilibrio con
                                                                    Ventas anuales
              Artículo           Precio          Costo         pronosticadas en unidades                             productos múltiples
              Emparedado        $2.95            $1.25                   7,000
              Refresco            .80              .30                   7,000
              Papa al horno      1.55              .47                   5,000
              Té                  .75              .25                   5,000
              Barra de ensaladas 2.85             1.00                   3,000
Con una variedad de productos a la oferta, procedemos con el análisis del punto de equilibrio igual que
en el caso de un solo producto, excepto que ponderamos cada uno de los productos por su proporción de
las ventas totales usando la ecuación (S7.6).
Solución:   Punto de equilibrio para múltiples productos: Determinación de la contribución

       1             2            3         4            5           6            7               8
                                                                 Pronóstico            Contribución
                 Precio de    Costo                              de ventas     % de     ponderada
  Artículo (i)   venta (P) variable (V) (V/P)      1 − (V/P)     anuales $     ventas (col. 5 × col. 7)
 Emparedado        $2.95        $1.25      .42        .58         $20,650         .446          .259
 Refresco            .80          .30      .38        .62           5,600         .121          .075
 Papa al horno      1.55          .47      .30        .70           7,750         .167          .117
 Té                  .75          .25      .33        .67           3,750         .081          .054
 Barra de ensaladas 2.85         1.00      .35        .65           8,550         .185          .120
                                                                  $46,300        1.000          .625

    Nota: El ingreso por emparedados es de $20,650 (2.95 × 7,000), que es un 44.6% del ingreso total
de $46,300. Por lo tanto, la contribución de los emparedados se “pondera” por .446. La contribución
ponderada es .446 × .58 = .259. De esta manera, su contribución relativa se refleja apropiadamente.
    Si usamos este enfoque para cada producto, encontramos que la contribución total ponderada es de
.625 por cada dólar de ventas, y el punto de equilibrio en dólares es igual a $67,200:

                                     F               $3,500 × 12 $42,000
                  PEQ$ =                           =            =        = $67,200
                               ⎡⎛ V ⎞           ⎤       .625      .625
                           ∑   ⎢⎜ 1 − ⎟ × (Wi ) ⎥
                               ⎢⎣⎝
                                      i
                                     Pi ⎠       ⎥⎦
300       Suplemento 7 • Planeación de la capacidad


                                  La información de este ejemplo implica ventas totales diarias (52 semanas de 6 días cada una) de:
                                                                           $67,200
                                                                                    = $215.38
                                                                           312 días
                                  Razonamiento: Ahora la administración de Le Bistro ya sabe que debe generar ventas prome-
                                  dio de $215.38 al día para lograr el equilibrio. La administración también sabe que si las ventas
                                  pronosticadas de $46,300 son correctas, Le Bistro perderá dinero, puesto que el punto de equilibrio
                                  es de $67,200.
                                  Ejercicio de aprendizaje: Si el administrador de Le Bistro quiere hacer $2,000 adicionales por
                                  mes y considera esto como un costo fijo, ¿cuál es el nuevo punto de equilibrio en las ventas diarias
                                  promedio? [Respuesta: $338.46].
                                  Problemas relacionados:       S7.24a, S7.25, S7.26a


                                 Las cifras del punto de equilibrio por producto proporcionan al administrador un conocimiento
                                 adicional del realismo de su pronóstico de ventas. Indican exactamente lo que debe venderse cada día,
                                 como se ilustra en el ejemplo S5.


 EJEMPLO S5                       Le Bistro también quiere conocer el punto de equilibrio para el número de emparedados que se debe
                                  vender cada día.
 Ventas unitarias                 Método:    Usando los datos del ejemplo S4, tomamos el pronóstico de ventas de emparedados del
 en el punto de                   44.6% veces el punto de equilibrio diario de $215.38 dividido entre el precio de venta de cada bocadillo
                                  ($2.95).
 equilibrio                       Solución:    Entonces, en el punto de equilibrio, las ventas de emparedados deben ser:

                                              .446 × $215.38
                                                             = Número de emparedados = 32.6 ≈ 33 emparedados diarios
                                                  $2.95
                                  Razonamiento: Con el conocimiento de las ventas de los productos individuales, el administrador
                                  tiene una base para determinar los requerimientos de materiales y mano de obra.
                                  Ejercicio de aprendizaje:     Con un punto de equilibrio en dólares de $338.46 diarios, ¿cuántos
                                  emparedados debe vender Le Bistro cada día?
                                  Problemas relacionados:       S7.24b, S7.26b, S7.35


                                     Después de haber preparado, analizado y juzgado en forma razonable el análisis del punto de equi-
                                 librio, es posible tomar las decisiones sobre el tipo y la capacidad del equipo que se necesita. De
                                 hecho, ahora se puede realizar un mejor juicio sobre la probabilidad de éxito de la empresa.
                                     Cuando los requerimientos de capacidad están sujetos a factores significativos que son desconoci-
                                 dos, se recomienda aplicar los modelos “probabilísticos”. Una técnica para tomar decisiones exitosas
                                 con respecto a la planeación de la capacidad con demanda incierta es la teoría de decisiones, la cual
                                 incluye el uso de árboles de decisión.


                                 APLICACIÓN DE ÁRBOLES DE DECISIÓN
Objetivo de aprendizaje          A LAS DECISIONES DE CAPACIDAD
4. Aplicar árboles de decisión   Los árboles de decisión requieren que las alternativas y los distintos estados de naturaleza se especi-
a las decisiones de capacidad    fiquen. Para situaciones donde se planea la capacidad, el estado de naturaleza normalmente es la
                                 demanda futura o la preferencia del mercado. Al asignar valores de probabilidad a los diversos estados de
                                 naturaleza, podemos tomar decisiones que maximicen el valor esperado de las alternativas. En el
                                 ejemplo S6 se muestra la forma de aplicar árboles de decisión a una decisión de capacidad.


 EJEMPLO S6                       Southern Hospital Supplies, una compañía que fabrica batas de hospital, está considerando aumentar su
                                  capacidad.
 Árbol de decisión                Método:      Las alternativas principales de Southern son: no hacer nada, construir una planta pequeña,
 aplicado a una                   construir una planta mediana, o construir una planta grande. La nueva instalación produciría un nuevo
                                  tipo de bata cuyo potencial de comercialización se desconoce. Si se construye una planta grande y existe
 decisión de capacidad            un mercado favorable, podría obtenerse una utilidad de $100,000. Un mercado desfavorable produciría
                                                                      Aplicación de árboles de decisión a las decisiones de capacidad   301


 una pérdida de $90,000. Sin embargo, con una planta mediana y un mercado favorable las utilidades
 llegarían a $60,000. El resultado de un mercado desfavorable sería una pérdida de $10,000. Por otra
 parte, con una planta pequeña se tendrían utilidades por $40,000 con condiciones de mercado favorables
 y se perderían sólo $5,000 en un mercado desfavorable. Por supuesto, siempre está la alternativa de no
 hacer nada.
      Una investigación de mercado reciente indica que existe una probabilidad de .4 de tener un mercado
 favorable, lo cual significa que también existe una probabilidad de .6 de que el mercado sea desfavo-
 rable. Con esta información se selecciona la alternativa que dará como resultado el mayor valor mone-
 tario esperado (VME).
 Solución:    Prepare un árbol de decisión y calcule el VME para cada rama:




                                                –$14,000
                                                           Mercado favorable (.4)
                                                                                       $100,000


                                                           Mercado desfavorable (.6)
                                            e                                          –$90,000
                                       d
                                   ran
                             ntag               $18,000
                        Pla                                Mercado favorable (.4)
                                                                                        $60,000
                      Planta mediana

                       Pla                                 Mercado desfavorable (.6)
                          nta                                                          –$10,000
                                  pe
                                       qu
                                         eñ
                                            a   $13,000
                         No                                Mercado favorable (.4)
                              ha                                                        $40,000
                                  ce
                                   rn
                                       ad
                                        a
                                                           Mercado desfavorable (.6)
                                                                                        –$5,000




                                                                                        $0




                  VME (planta grande) = (.4)($100,000) + (.6)(−$90,000) = −$14,000
                VME (planta mediana) = (.4)($60,000) + (.6)(−$10,000) = +$18,000
                VME (planta pequeña) = (.4)($40,000) + (.6)(−$5,000) = +$13,000
                  VME (no hacer nada) = $0

 Con base en el criterio de VME, Southern debe construir una planta mediana.
 Razonamiento: Si Southern toma muchas decisiones como ésta, entonces la determinación del
 VME para cada rama y la selección del VME más alto es un buen criterio de decisión.
 Ejercicio de aprendizaje: Si una nueva estimación de la pérdida resultante por la construcción de
 una planta mediana en un mercado desfavorable aumenta a –$20,000, ¿cuál es el nuevo VME para esta
 rama? [Respuesta: $12,000, lo cual cambia la decisión porque ahora el VME de la planta pequeña es
 más alto].
 Problemas relacionados:            S7.27, S7.28


                                                                                                                 Un administrador de
APLICACIÓN DEL ANÁLISIS DE INVERSIÓN                                                                             operaciones puede ser el
A LAS INVERSIONES IMPULSADAS POR LA ESTRATEGIA                                                                   responsable del
                                                                                                                 rendimiento sobre la
Después de haber considerado las implicaciones estratégicas de las inversiones potenciales, es                   inversión (ROI, return
adecuado realizar un análisis tradicional de la inversión. A continuación presentamos los aspectos de la         on investment).
inversión que están relacionados con la capacidad.
302        Suplemento 7 • Planeación de la capacidad

                                 Inversión, costo variable y flujo de efectivo
 La inversión de capital         Debido a que existen alternativas para capacidad y proceso, también las hay para las inversiones de
 requiere flujo de               capital y el costo variable. Los administradores deben elegir entre las diferentes posibilidades
 efectivo, así como una          financieras, así como entre las alternativas de capacidad y proceso. El análisis debe mostrar la inver-
 evaluación del                  sión de capital, el costo variable y los flujos de efectivo, así como el valor presente neto para cada
 rendimiento sobre la            alternativa.
 inversión.
                                 Valor presente neto
                                 La determinación del valor descontado de una serie de ingresos de efectivo futuros se conoce como téc-
Valor presente neto              nica del valor presente neto. A manera de introducción, consideremos el valor del dinero en el tiempo.
Medio para determinar el valor   Digamos que usted invirtió $100.00 en un banco al 5% anual. Su inversión valdrá $100.00 + ($100.00)(.05)
descontado de una serie de       = $105.00. Si usted invierte los $105.00 un año más, su valor será $105.00 + ($105.00)(.05) = $110.25
ingresos de efectivo futuros.    al final del segundo año. Por supuesto que podemos calcular el valor futuro de $100.00 al 5% para el
                                 número de años que queramos simplemente extendiendo este análisis. Sin embargo, existe una forma
                                 más sencilla de expresar matemáticamente esta relación. Para el primer año:

                                                                                $105 = $100(1 + .05)

                                 Para el segundo año:

                                                                    $110.25 = $105(1 + .05) = $100(1 + .05)2

                                 En general:

                                                                                     F = P(1 + i)N                                                 (S7-7)

                                 donde         F = valor futuro (tal como $110.25 o $105)
                                               P = valor presente (tal como $100.00)
                                                i = tasa de interés (tal como .05)
                                               N = número de años (tal como 1 año o 2 años)

Objetivo de aprendizaje          Sin embargo, en la mayoría de las decisiones de inversión nos interesa calcular el valor presente de
                                 una serie de pagos futuros. Si despejamos P, obtenemos:
5. Calcular el valor presente
neto
                                                                                               F
                                                                                     P=                                                            (S7-8)
                                                                                           (1 + i) N

                                 Cuando el número de años no es demasiado grande, la ecuación anterior es efectiva. Sin embargo, cuan-
                                 do el número de años, N, es grande, la fórmula se vuelve difícil de manejar. Para 20 años usted tendría
                                 que calcular (1 + i)20. Sin una calculadora sofisticada este cálculo resultaría complicado.




                                  Lograr la correspondencia apropiada entre capacidad y demanda puede ser un reto. Cuando una participación en el
                                 mercado está disminuyendo y las instalaciones son antiguas e inflexibles, como en el caso de esta planta de General
                                 Motors, la disparidad entre la demanda y la capacidad implica vaciar las plantas y despedir empleados (foto izquierda).
                                 Por otro lado, cuando la demanda excede a la capacidad, como en esta apertura de la tienda Apple en las afueras de Roma,
                                 Italia, la disparidad implica la frustración de los clientes y la pérdida de ingresos (foto derecha).
                                                                           Aplicación de árboles de decisión a las decisiones de capacidad   303

                                                                                                                     Tabla S7.1
 Año          5%          6%          7%            8%         9%             10%          12%           14%
   1          .952        .943        .935          .926       .917           .909          .893          .877      Valor presente de $1
   2          .907        .890        .873          .857       .842           .826          .797          .769
   3          .864        .840        .816          .794       .772           .751          .712          .675
   4          .823        .792        .763          .735       .708           .683          .636          .592
   5          .784        .747        .713          .681       .650           .621          .567          .519
   6          .746        .705        .666          .630       .596           .564          .507          .456
   7          .711        .665        .623          .583       .547           .513          .452          .400
   8          .677        .627        .582          .540       .502           .467          .404          .351
   9          .645        .592        .544          .500       .460           .424          .361          .308
  10          .614        .558        .508          .463       .422           .386          .322          .270
  15          .481        .417        .362          .315       .275           .239          .183          .140
  20          .377        .312        .258          .215       .178           .149          .104          .073



Las tablas de tasas de interés, como la tabla S7.1, simplifican esta situación. Primero, replanteamos la
ecuación del valor presente:

                                                      F
                                             P=             = FX                                          (S7-9)
                                                  (1 + i) N

   donde    X = un factor de la tabla S7.1 que se define como = 1/(1 + i)N           y   F = valor futuro

Así, todo lo que tenemos que hacer es encontrar el factor X y multiplicarlo por F para calcular el valor
presente, P. Los factores son, por supuesto, una función de la tasa de interés, i, y el número de años,
N. En la tabla S7.1 se relacionan algunos de estos factores.
   Las ecuaciones (S7-8) y (S7-9) se usan para determinar el valor presente de una cantidad futura de
efectivo, pero hay algunas situaciones en las que una inversión genera una serie de cantidades uni-
formes e iguales de efectivo. Este tipo de inversión se llama anualidad. Por ejemplo, considere una
inversión que reditúa $300 por año durante 3 años. Por supuesto, puede usarse tres veces la ecuación
(S7-8), para los años 1, 2 y 3, aunque hay un método más corto. Aún cuando existe una fórmula para
calcular el valor presente de una serie anual de flujos de efectivo iguales y uniformes (una anualidad),
se ha desarrollado una tabla fácil de usar para este propósito. De igual forma que los cálculos acos-
tumbrados del valor presente, este cálculo involucra un factor. Los factores para las anualidades se
presentan en la tabla S7.2. La relación básica es

                                                   S = RX

donde        X = factor de la tabla S7.2
             S = valor presente de una serie de pagos anuales uniformes
             R = pagos que se reciben cada año durante la vigencia de la inversión (la anualidad)

El valor presente de una serie anual uniforme de cantidades es una extensión del valor presente de una
cantidad única y, por lo tanto, la tabla S7.2 se puede construir directamente a partir de la tabla S7.1.
Los factores para una tasa de interés dada en la tabla S7.2 no son sino la suma acumulada de valores
de la tabla S7.1. Por ejemplo, en la tabla S7.1, .952, .907 y .864 son los factores para los años 1, 2 y 3

                                                                                                                     Tabla S7.2
 Año          5%           6%           7%            8%           9%          10%          12%          14%
   1          .952         .943         .935          .926          .917        .909         .893         .877      Valor presente de una
   2         1.859        1.833        1.808         1.783         1.759       1.736        1.690        1.647      anualidad de $1
   3         2.723        2.673        2.624         2.577         2.531       2.487        2.402        2.322
   4         3.546        3.465        3.387         3.312         3.240       3.170        3.037        2.914
   5         4.329        4.212        4.100         3.993         3.890       3.791        3.605        3.433
   6         5.076        4.917        4.766         4.623         4.486       4.355        4.111        3.889
   7         5.786        5.582        5.389         5.206         5.033       4.868        4.564        4.288
   8         6.463        6.210        5.971         5.747         5.535       5.335        4.968        4.639
   9         7.108        6.802        6.515         6.247         5.985       5.759        5.328        4.946
  10         7.722        7.360        7.024         6.710         6.418       6.145        5.650        5.216
  15        10.380        9.712        9.108         8.559         8.060       7.606        6.811        6.142
  20        12.462       11.470       10.594         9.818         9.128       8.514        7.469        6.623
304    Suplemento 7 • Planeación de la capacidad

                           cuando la tasa de interés es del 5%. La suma acumulada de estos factores es 2.723 = .952 + .907 +
                           .864. Ahora observe en la tabla S7.2 el punto donde la tasa de interés es del 5% y el número de años
                           es 3. El factor para el valor presente de una anualidad es 2.723, como era de esperarse. La tabla S7.2 es
                           muy útil para disminuir la cantidad de operaciones necesarias para tomar decisiones financieras. (Sin
                           embargo, observe que pueden presentarse pequeñas diferencias de redondeo entre las tablas).
                              En el ejemplo S7 se muestra cómo determinar el valor presente de una anualidad.


 EJEMPLO S7                 La clínica River Road Medical está pensando invertir en un nuevo y sofisticado equipo médico. Esta
                            inversión generará ingresos por $7,000 anuales durante 5 años.
 Determinación del          Método: Determine el valor presente de este flujo de efectivo; suponga una tasa de interés del 6%.
 valor presente neto        Solución: El factor de la tabla S7.2 (4.212) se obtiene al encontrar el valor cuando la tasa de interés es
                            del 6% y el número de años es 5:
 de pagos futuros con
                                                               S = RX = $7,000(4.212) = $29,484
 el mismo valor
                            Razonamiento:        Hay otra forma de ver este ejemplo. Si usted fuera a un banco y tomara un préstamo
                            por $29,484 el día de hoy, sus pagos serían de $7,000 anuales durante 5 años si el banco empleara una
                            tasa de interés del 6% compuesto anual. Por lo tanto, el valor presente es de $29,484.
                            Ejercicio de aprendizaje:        Si la tasa de interés es del 8%, ¿cuál es el valor presente? [Respuesta:
                            $27,951].
                            Problemas relacionados:         S7.29, S7.30, S7.31


                           El método del valor presente neto es uno de los mejores que existen para calificar las alternativas de
                           inversión. El procedimiento es directo: simplemente calcule el valor presente de todos los flujos
                           de efectivo para cada alternativa de inversión. Para decidir entre las alternativas de inversión, se elige
                           la inversión que tenga el valor presente neto más alto. De manera similar, cuando se realizan varias
                           inversiones, aquellas con mayores valores presentes netos son preferibles a las inversiones con valores
                           presentes netos inferiores.
                               En el ejemplo S8 se muestra cómo usar el valor presente neto para elegir entre varias alternativas
                           de inversión.


 EJEMPLO S8                 Quality Plastics, Inc., está considerando dos alternativas de inversión diferentes.
                            Método:       Para encontrar el valor presente neto de cada inversión, Quality necesita determinar primero
 Determinación del          la inversión inicial, los flujos de efectivo, y la tasa de interés. La inversión A tiene un costo inicial de
 valor presente neto        $25,000, y la inversión B un costo inicial de $26,000. Ambas inversiones tienen una vida útil de 4 años.
                            A continuación se presentan los flujos de efectivo de dichas inversiones. El costo de capital o tasa de
 de pagos futuros           interés (i) es del 8%. (Los factores se tomaron de la tabla S7.1).
 con valor diferente                    Flujo de efectivo        Flujo de efectivo                        Factor de valor
                                        de la inversión A        de la inversión B           Año          presente al 8%
                                           $10,000                     $9,000                  1                   .926
                                             9,000                      9,000                  2                   .857
                                             8,000                      9,000                  3                   .794
                                             7,000                      9,000                  4                   .735

                            Solución:    Para encontrar el valor presente de los flujos de efectivo para cada inversión, multiplicamos
                            el factor de valor presente por el flujo de efectivo de cada inversión para cada año. La suma de estos
                            cálculos del valor presente menos la inversión inicial es el valor presente neto para cada inversión.
                            Los cálculos aparecen en la tabla siguiente:

                                                                        Flujo de efectivo                         Flujo de efectivo
                              Año                                       de la inversión A                         de la inversión B
                               1                                   $ 9,260 = (.926)($10,000)               $ 8,334 = (.926)($9,000)
                               2                                     7,713 = (.857)($9,000)                   7,713 = (.857)($9,000)
                               3                                     6,352 = (.794)($8,000)                   7,146 = (.794)($9,000)
                               4                                     5,145 = (.735)($7,000)                   6,615 = (.735)($9,000)
                              Totales                              $28,470                                 $29,808
                              Menos inversión inicial              −25,000                                 −26,000
                              Valor presente neto                  $ 3,470                                  $ 3,808
                                                                                  Uso de software para el análisis del punto de equilibrio   305


 Razonamiento: El criterio del valor presente neto muestra que la inversión B es más atractiva
 que la inversión A porque tiene un valor presente más alto.
 Ejercicio de aprendizaje: Si la tasa de interés fuera del 10%, ¿cambiaría esto la decisión?
 [Respuesta: No, pero la diferencia entre las dos inversiones se reduce. El VPN de la inversión
 A = $2,243 y el de la inversión B = $2,500].
 Problemas relacionados:        S7.32, S7.33, S7.34, S7.36



    En el ejemplo S8 no fue necesario realizar todos los cálculos del valor presente para la inversión B.
Debido a que todos los flujos de efectivo son uniformes, la tabla S7.2 de anualidades proporciona el
factor de valor presente. Por supuesto, esperaríamos tener la misma respuesta. Como recordamos,
la tabla S7.2 proporciona los factores para el valor presente de una anualidad. En este ejemplo, para
pagos de $9,000, el costo de capital es del 8% y el número de años es 4. Buscamos en la tabla S7.2
la intersección de 8% y 4 años y encontramos el factor 3.312. Así, el valor presente para esta anuali-
dad es (3.312)($9,000) = $29,808; el mismo valor que en el ejemplo S8.
    Aunque el valor presente neto es uno de los mejores enfoques existentes para evaluar las alternativas
de inversión, tiene sus fallas. Las limitaciones del método de valor presente neto incluyen lo siguiente:
 1. Inversiones con el mismo valor presente neto llegan a tener una vida proyectada significativa-
    mente diferente y valores de recuperación distintos.
 2. Inversiones con el mismo valor presente neto pueden tener flujos de efectivo diferentes. Estos
    flujos de efectivo distintos pueden establecer diferencias sustanciales en la capacidad de una
    compañía para pagar sus cuentas.
 3. El supuesto es que conocemos las tasas de interés que habrá en el futuro, lo cual no es cierto.
 4. Los pagos siempre se realizan al final del periodo (semana, mes o año), lo que no siempre sucede
    en la realidad.



Resumen
Los administradores vinculan la selección de equipo y las deci-         nistradores de operaciones cuando se toman decisiones acerca
siones sobre la capacidad con la misión y la estrategia de la           de la capacidad.
compañía. Diseñan su equipo y sus procesos para obtener                    Las inversiones en capacidad son efectivas cuando se asegura
capacidades que superen la tolerancia requerida por sus clientes        que apoyen una estrategia de largo plazo. Los criterios para to-
mientras aseguran la flexibilidad necesaria para realizar ajustes       mar las decisiones de inversión son la contribución al plan estraté-
en tecnología, características y volúmenes.                             gico global y obtener pedidos redituables, no sólo el rendimiento
   Las técnicas de pronóstico, el análisis del punto de equilibrio,     sobre la inversión. Las empresas eficientes seleccionan los pro-
los árboles de decisión, el flujo de efectivo y el valor presente       cesos correctos y la capacidad correcta que contribuyen con su
neto (VPN) resultan particularmente útiles para los admi-               estrategia de largo plazo.


Términos clave
Análisis del punto de equilibrio (p. 296)       Contribución (p. 296)                             Función de ingreso (p. 296)
Capacidad (p. 288)                              Costos fijos (p. 296)                             Utilización (p. 289)
Capacidad de diseño (p. 289)                    Costos variables (p. 296)                         Valor presente neto (p. 302)
Capacidad efectiva (p. 289)                     Eficiencia (p. 289)



Uso de software para el análisis del punto de equilibrio
 Excel, Excel OM y POM para Windows manejan problemas de análisis del punto de equilibrio y de
 costo-volumen.

 Uso de Excel
 En Excel, desarrollar las fórmulas para realizar un análisis del punto de equilibrio es una tarea sencilla.
 Aunque aquí no se demuestran todos los pasos básicos, la mayor parte del análisis en hoja de cálculo se
 puede ver en el software preprogramado en Excel OM que acompaña a este texto.
306       Suplemento 7 • Planeación de la capacidad



                                                                                    La gráfica se crea en Excel 2007 usando las opciones de gráficas
                                                                                    incluidas en el menú de insertar tabla. En versiones más antiguas de
                                                                                    Excel, la gráfica se crea usando la ayuda para gráficas. En cualquier
                                                                                    caso, seleccione las celdas de A20 a C22 y elija la herramienta
                          Introduzca los costos fijos y variables y el precio de    apropiada para su versión de Excel.
                          venta en el área de datos. Puede introducir un
                          volumen, con el cual se realiza un análisis de volumen.




                                       Dos componentes
Costo total                            son = 1.5 + 0.75
= B9 + B10*A21

                                                                             = B9/(B11 – B10)
                                                                             = B9 + B10*B16

                                                                                        Ingreso total
                                                                                        = B11*A22


                      Para dibujar la gráfica, necesitamos dos
                      puntos para cada línea. Hemos elegido
                      el eje 0 como el valor del eje x para un
                      punto, y dos veces el punto de equilibrio
                      (= 2*B16) como el valor del eje x para
                      el otro punto.


                                      Programa S7.1                         Análisis del punto de equilibrio en Excel OM, usando los datos del ejemplo S3


                                     X Uso de Excel OM
                                     El módulo de Excel OM para el análisis del punto de equilibrio se ilustra en el programa S7.1. Con los
                                     datos de Stephens, Inc., del ejemplo S3, el programa S7.1 muestra los datos de entrada, las fórmulas de
                                     Excel para calcular los puntos de equilibrio y la solución, así como las gráficas de salida.
                                     P Uso de POM para Windows
                                     En forma similar a Excel OM, POM para Windows también contiene un módulo para efectuar el análi-
                                     sis del punto de equilibro y el análisis de costo-volumen.



Problemas resueltos                                                                               Horas virtuales en la oficina


Problema resuelto S7.1
Sara James Bakery, descrita anteriormente en los ejemplos S1 y S2,                         Solución
ha decidido ampliar sus instalaciones agregando una línea de pro-
ceso adicional. La empresa tendrá dos líneas de proceso, cada una                               Producción esperada = (Capacidad efectiva)(Eficiencia)
trabajando 7 días a la semana, 3 turnos al día, 8 horas por turno. En
este momento su capacidad efectiva es de 300,000 panecillos. Sin                                                       = 300,000(.85)
embargo, esta adición reducirá la eficiencia de todo el sistema al                                                     = 255,000 panecillos por semana
85%. Calcule la producción esperada con esta nueva capacidad
efectiva.



Problema resuelto S7.2
Marty McDonald tiene un negocio de empaquetado de software en                              Solución
Wisconsin. Su costo fijo anual es de $10,000, el costo por mano
de obra directa es de $3.50 por empaque, y el costo de material es de                                        F            $10,000          $10,000
$4.50 por empaque. El precio de venta será de $12.50 por empaque.                            PEQ$ =                =                     =         = $27,777
                                                                                                        1 − (V /P ) 1 − ($8.00 / $12.50)     .36
¿Cuál es el punto de equilibrio en dólares? ¿Cuál es el punto de
equilibrio en unidades?                                                                                   F      $10,000       $10,000
                                                                                             PEQx =          =               =         = 2,222 unidades
                                                                                                        P − V $12.50 − $8.00    $4.50

                                                                                                                    Problemas resueltos      307



Problema resuelto S7.3
A John se le pidió determinar si el costo de $22.50 de los boletos para el teatro-restaurante de la comunidad permitirá al grupo lograr el
punto de equilibrio y si la capacidad de 175 asientos es adecuada. El costo para cada actuación de una temporada de diez actuaciones es de
$2,500. El costo por la renta del local para 10 actuaciones es de $10,000. Las bebidas y el estacionamiento son cargos adicionales y tienen
su propio precio y sus propios costos variables, como se muestra a continuación:

           1                 2           3              4                  5         6          7           8             9
                                                                                 Cantidad                          Contribución
                                                   Porcentaje                   estimada de                       ponderada por
                                    Costo           del costo                    unidades     Ventas               el porcentaje
                         Precio de variable         variable       Contribución vendidas    en dólares Porcentaje    de ventas
                         venta (P)   (V)             (V/P)          1 − (V/P)     (ventas) (Ventas × P) de ventas (col. 5 × col. 8)

Boletos con alimentos $22.50          $10.50          0.467               0.533             175        $3,938       0.741            0.395
Bebidas               $ 5.00          $ 1.75          0.350               0.650             175        $ 875        0.165            0.107
Estacionamiento       $ 5.00          $ 2.00          0.400               0.600             100        $ 500        0.094            0.056
                                                                                            450        $5,313       1.000            0.558
Solución                                           F                 $(10 × 2,500) + $10,000 $35,000
                              PEQ$ =                               =                        =        = $62,724
                                             ⎡⎛ V ⎞             ⎤             0.558           0.558
                                        ∑    ⎢⎜ 1 − i ⎟ × (Wi ) ⎥
                                             ⎢⎣⎝   Pi ⎠         ⎥⎦

Ingreso para cada día (de la columna 7) = $5,313
Ingreso pronosticado para las 10 actuaciones = (10  $5,313) = $53,130
El ingreso pronosticado con esta mezcla de ventas muestra un punto de equilibrio de $62,724
    Así, dada esta mezcla de costos, ventas y capacidad, John determina que el teatro no logrará el equilibrio.



Problema resuelto S7.4
Su jefe le pidió que evaluara el costo de dos máquinas. Después de
algunas preguntas, se le asegura que las máquinas tienen los costos                                             Máquina A         Máquina B
mostrados aquí a la derecha. Suponga que:
a) La vida de cada máquina es de 3 años, y                                   Costo original                      $13,000             $20,000
b) La compañía piensa que obtendrá el 14% sobre inversiones                  Costo en mano de obra por año         2,000               3,000
   cuyo riesgo no es mayor que este porcentaje.                              Espacio de planta por año               500                 600
Determine mediante el método de valor presente cuál máquina debe             Energía (electricidad) anual          1,000                 900
comprarse.                                                                   Mantenimiento anual                   2,500                 500
                                                                             Costo total anual                   $ 6,000             $ 5,000
                                                                             Valor de recuperación               $ 2,000             $ 7,000

Solución
                                                         Máquina A                                               Machine B
                                      Columna 1          Columna 2             Columna 3          Columna 4      Columna 5           Columna 6

Ahora                    Gasto           1.000              $13,000               $13,000           1.000          $20,000            $20,000
Año 1                    Gasto            .877                6,000                 5,262            .877            5,000              4,385
Año 2                    Gasto            .769                6,000                 4,614            .769            5,000              3,845
Año 3                    Gasto            .675                6,000                 4,050            .675            5,000              3,375
                                                                                  $26,926                                             $31,605
Año 3 Valor de recuperación                .675             $ 2,000                −1,350            .675          $ 7,000             −4,725
                                                                                  $25,576                                             $26,880
Usamos 1.0 para pagos sin descuentos aplicados (es decir, cuando            El cálculo para la máquina A durante el primer año es:
los pagos se hacen ahora, no se necesita el descuento). Los otros
valores de las columnas 1 y 4 se obtuvieron de la columna del 14%                     .877 × ($2,000 + $500 + $1,000 + $2,500) = $5,262
y el año respectivo, incluidos en la tabla S7.1 (por ejemplo, la inter-     El valor de recuperación del producto se resta a la suma de los cos-
sección del 14% y el año 1 es .877, etc.). Las columnas 3 y 6 son los       tos, porque es un ingreso de efectivo. Como la suma de los costos
productos de las cifras de valor presente multiplicadas por los cos-        netos de la máquina B es mayor que la suma de los costos netos de
tos combinados. Este cálculo se realiza para cada año y para el valor       la máquina A, la máquina A es la compra de menor costo, y así se lo
de recuperación.                                                            debe informar usted a su jefe.
308          Suplemento 7 • Planeación de la capacidad


Autoevaluación
• Antes de realizar la autoevaluación, revise los objetivos de                 c) el porcentaje de la capacidad que se logra en realidad
  aprendizaje enlistados al inicio del suplemento y los términos               d) la producción real
  clave relacionados al final del mismo.                                       e) la eficiencia
• Revise sus respuestas en el apéndice V.                                   5. La eficiencia es:
• Vuelva a estudiar las páginas que correspondan a cada pre-                   a) la capacidad que una empresa espera alcanzar dadas sus
  gunta que respondió incorrectamente o al material sobre el cual                  restricciones operativas actuales.
  se sienta inseguro.                                                          b) el porcentaje de la capacidad de diseño que se logra en realidad
1. Las decisiones de capacidad deben tomarse con base en:                      c) el porcentaje de la capacidad efectiva que se logra en realidad
   a) la construcción de una ventaja competitiva sostenida                     d) la producción real
   b) buenos rendimientos financieros                                          e) la capacidad de diseño
   c) un plan coordinado                                                    6. Los ajustes a la capacidad se logran a través de:
   d) la integración a la estrategia de la compañía                            a) cambios del personal
   e) todas las respuestas anteriores son correctas                            b) ajustes al equipo
                                                                               c) mejoras al proceso
2. Los supuestos del modelo del punto de equilibrio son:                       d) el rediseño del producto
   a) los costos fijos y variables son lineales y el ingreso es expo-          e) todas las respuestas anteriores son válidas
      nencial
   b) los costos fijos son lineales y los costos variables y el ingreso     7. El punto de equilibrio es:
      son exponenciales                                                        a) la adición de procesos para alcanzar el punto de cambio de
   c) los costos fijos, los costos variables y el ingreso son lineales             las demandas del producto
   d) el punto de equilibrio sólo se calcula en dólares                        b) la mejora de los procesos para aumentar la capacidad
   e) el punto de equilibrio sólo se calcula en unidades                       c) el punto en dólares o unidades donde los costos y el ingreso
                                                                                   son iguales
3. La capacidad efectiva es:                                                   d) la adición o remoción de capacidad para satisfacer la
   a) la capacidad que una compañía espera alcanzar dadas sus                      demanda
       restricciones operativas actuales                                       e) el costo total de una alternativa del proceso
   b) el porcentaje de la capacidad de diseño que se logra en realidad
                                                                            8. La contribución es:
   c) el porcentaje de la capacidad que se logra en realidad
                                                                               a) el costo que permanece igual incluso cuando no se producen
   d) la producción real
                                                                                   unidades
   e) la eficiencia
                                                                               b) la diferencia entre el precio de venta y los costos variables
4. La utilización es:                                                          c) el ingreso que está en directa proporción con las unidades
   a) la capacidad que una empresa espera alcanzar dadas sus                       vendidas
       restricciones operativas actuales                                       d) aquel costo que varía con las unidades vendidas
   b) el porcentaje de la capacidad de diseño que se logra en realidad         e) todas las respuestas anteriores son correctas




Ejercicios para el estudiante
Consulte en nuestro sitio web y en el CD-ROM los materiales de apoyo disponibles para este capítulo.
         En nuestro sitio web                             En el CD-ROM del estudiante                   En el CD-ROM de videos
•     Exámenes de auto-estudio                      •   Problemas de práctica                       • Video clips
•     Problemas de práctica                         •   Ejercicios de modelo activo                 • Caso en video
•     Recorrido por una compañía virtual            •   Excel OM
•     Casos en internet                             •   Archivos de datos para Excel OM
•     Presentación en Power Point                   •   POM para Windows




Preguntas para análisis
    1. ¿Cuál es la distinción entre capacidad de diseño y capacidad         6. Explique por qué el valor presente neto es una herramienta
       efectiva?                                                               apropiada para comparar inversiones.
    2. ¿Cuáles son los supuestos del análisis del punto de equilibrio?      7. ¿Qué es la capacidad efectiva?
    3. ¿Dónde obtiene un administrador los datos necesarios para            8. ¿Qué es la eficiencia?
       realizar el análisis del punto de equilibrio?                        9. ¿Cómo se calcula la producción real o esperada?
    4. ¿Qué evita que los datos del ingreso graficados caigan en una
       línea recta cuando se realiza el análisis del punto de equilibrio?
    5. ¿Bajo qué condiciones querría una empresa que su capacidad
       se retrasara con respecto a la demanda?, ¿y que se adelantara a
       la demanda?
                                                                                                                             Problemas      309

Problemas*
•      S7.1 Si una planta se diseñó para producir 7,000 martillos          •     S7.12 Markland Manufacturing busca aumentar su capacidad,
por día, pero se ha limitado a hacer 6,000 martillos diarios debido al     resolviendo una operación que representa un cuello de botella, al
tiempo necesario para cambiar el equipo según los estilos de mar-          agregar un nuevo equipo. Dos proveedores presentaron sus propues-
tillo, ¿cuál es la utilización?                                            tas. Los costos fijos para la propuesta A son de $50,000 y, para la
•     S7.2 Durante el mes pasado, la planta del problema S7.1, la          propuesta B, de $70,000. Los costos variables para A son de $12.00
cual tiene una capacidad efectiva de 6,500, fabricó sólo 4,500 mar-        y para B de $10.00. El ingreso que genera cada unidad es de $20.00.
tillos por día debido a demoras de material, ausencias de los              a) ¿Cuál es el punto de equilibrio en unidades para la propuesta A?
empleados y otros problemas. ¿Cuál es su eficiencia?                       b) ¿Cuál es el punto de equilibrio en unidades para la propuesta B?
                                                                                PX
•    S7.3 Si una planta tiene una capacidad efectiva de 6,500 y
una eficiencia del 88%, ¿cuál es su producción real (planeada)?            •    S7.13 Usando los datos del problema S7.12:
                                                                           a) ¿Cuál es el punto de equilibrio en dólares para la propuesta A si
•    S7.4 La capacidad efectiva de una planta es de 900 unidades
                                                                              se agregan al costo fijo $10,000 por la instalación?
por día y produce 800 unidades diarias con su mezcla de productos;
¿cuál es su eficiencia?                                                    b) ¿Cuál es el punto de equilibrio en dólares para la propuesta B si
                                                                              se agregan al costo fijo $10,000 por la instalación? PX
•     S7.5 Las demoras de material han limitado rutinariamente la
producción de lavamanos para el hogar a 400 unidades por día. Si           •   S7.14 Dados los datos del problema S7.12, ¿para qué volu-
la eficiencia de la planta es del 80%, ¿cuál es su capacidad efectiva?     men (unidades) de producción las dos alternativas generarán la
                                                                           misma utilidad? PX
• • S7.6 ¿Cuál es la producción esperada para una planta con
capacidad de diseño de 108 sillas por día si su capacidad efectiva es      • • S7.15 Janelle Heinke, propietaria de Ha’Peppas!, está con-
de 90 sillas y su eficiencia del 90 por ciento?                            siderando un nuevo horno para cocinar la especialidad de la casa,
•    S7.7 Un centro de trabajo que contiene 4 máquinas con la              pizza vegetariana. El horno tipo A puede manejar 20 pizzas por
misma capacidad opera dos turnos por día 5 días a la semana                hora. Los costos fijos asociados con el horno A son de $20,000 y los
(8 horas por turno). Esta es la capacidad efectiva. Si el centro de tra-   costos variables de $2.00 por pizza. El horno B es más grande y
bajo tiene una eficiencia del sistema del 95%, ¿cuál es la producción      puede manejar 40 pizzas por hora. Los costos fijos asociados con el
esperada en horas por semana?                                              horno B son de $30,000 y los costos variables de $1.25 por pizza.
                                                                           Cada pizza se vende en $14.
•    S7.8 La capacidad efectiva y la eficiencia de tres departa-           a) ¿Cuál es el punto de equilibrio para cada horno?
mentos de MMU Mfg., basada en Waco, Texas, para el próximo                 b) Si la propietaria espera vender 9,000 pizzas, ¿qué horno debe
trimestre son las siguientes:                                                 comprar?
                                                                           c) Si la propietaria espera vender 12,000 pizzas, ¿qué horno debe
                               Capacidad            Eficiencia                comprar?
       Departamento             efectiva             reciente              d) ¿En qué volumen debe Janelle cambiar los hornos? PX
       Diseño                    93,600                  .95
       Fabricación              156,000                 1.03
       Acabado                   62,400                 1.05

Calcule la producción esperada durante el siguiente trimestre para
cada departamento.
•     S7.9 Smithson Cutting está abriendo una nueva línea de
tijeras para su distribución en supermercados. Estima su costo fijo
en $500.00 y su costo variable en $0.50 por unidad. Se espera que el
precio de venta promedie $0.75 por unidad.
a) ¿Cuál es el punto de equilibrio de Smithson en unidades?
b) ¿Cuál es el punto de equilibrio de Smithson en dólares? PX
• • S7.10 Bajo condiciones ideales, una estación de servicio de
Fast Lube puede atender a 6 automóviles por hora. Se sabe que la
capacidad efectiva y la eficiencia de una estación de servicio de Fast
Lube son de 5.5 y 0.880, respectivamente. ¿Cuál es el número mí-
nimo de estaciones de servicio que necesita Fast Lube para alcanzar
una producción anticipada de 200 automóviles por cada jornada de
8 horas?
• • S7.11 El programa de negocios de la Southeastern Oklahoma
State University tiene instalaciones y profesorado para manejar una        •     S7.16 Dados los siguientes datos, calcule: a) PEQ(x); b) PEQ($),
matrícula de 2,000 nuevos estudiantes por semestre. Sin embargo,           y c) la utilidad en 100,000 unidades:
en un esfuerzo por limitar el tamaño de las generaciones a un nivel
“razonable” (en general, abajo de 200), el decano de la universidad,           P = $8 por unidad V = $4 por unidad F = $50,000 PX
Tom Choi, estableció un tope de 1,500 nuevos estudiantes en la
inscripción. Aunque el semestre pasado hubo una demanda amplia
                                                                           • • S7.17 Usted está pensando abrir un servicio de copiado en la
para los cursos de negocios, un problema con los horarios permitió
                                                                           unión de estudiantes. Estima su costo fijo en $15,000 y el costo va-
inscribir sólo a 1,450 estudiantes en dichos cursos. ¿Cuál es la uti-
                                                                           riable por copia vendida en $.01. Usted espera que el precio de
lización y la eficiencia de este sistema?
                                                                           venta promedie $.05.
*Nota: PX significa que el problema se puede resolver con POM para         a) ¿Cuál es el punto de equilibrio en dólares?
Windows y/o Excel OM.                                                      b) ¿Cuál es punto de equilibrio en unidades? PX
310       Suplemento 7 • Planeación de la capacidad

• • S7.18 La doctora Aleda Roth, autora prolífica, planea abrir su         unidad. El volumen del nuevo producto mejorado deberá aumentar
propia compañía editorial. La llamará DSI Publishing, Inc. Los cos-        a 50,000 unidades.
tos estimados de DSI son:                                                  a) ¿Debe invertir la compañía en el nuevo equipo?
                                                                           b) ¿En qué volumen cambia la elección del equipo?
           Costo fijo                         $250,000.00                  c) Con un volumen de 15,000 unidades, ¿qué proceso se debe usar?
           Costo variable por libro                $20.00                  • • • S7.24 Como posible propietario de un club conocido como
           Precio de venta por libro               $30.00                  The Red Rose, usted está interesado en determinar el volumen nece-
                                                                           sario de ventas en dólares para llegar al punto de equilibrio el pró-
¿Cuántos libros debe vender DSI para llegar al punto de equilibrio?        ximo año. Usted decidió desglosar las ventas del club en cuatro
¿Cuál es el punto de equilibrio en dólares? PX                             categorías, donde la cerveza es la primera. Su estimación de la venta
• • S7.19 Además de los costos del problema S7.18, la doctora              de cerveza es que servirá 30,000 raciones. El precio de venta por
Roth desea pagarse un sueldo de $75,000 anuales.                           unidad promediará $1.50; su costo es de $.75. La segunda categoría
a) ¿Ahora cuál es su punto de equilibrio en unidades?                      es alimentos, de los cuales espera vender 10,000 unidades con un
b) ¿Cuál es su punto de equilibrio en dólares? PX                          precio unitario promedio de $10.00 y un costo de $5.00. La tercera
                                                                           categoría es postres y vino, de los que también espera vender 10,000
• • S7.20 Una empresa de artículos electrónicos fabrica actual-            unidades, pero con un precio unitario promedio de $2.50 y un costo
mente un artículo con un costo variable de $.50 por unidad, cuyo           de $1.00. La última categoría es almuerzos y emparedados
precio de venta es de $1.00 por unidad. Los costos fijos son de $14,000.   económicos, de los cuales espera vender un total de 20,000 unidades
Su volumen actual es de 30,000 unidades. La empresa mejoraría la           con un precio promedio de $6.25 y con un costo por unidad de
calidad del producto de manera sustancial si agregara un nuevo             $3.25. Sus costos fijos (es decir, renta, servicios públicos, etc.) son
equipo con un costo fijo adicional de $6,000. El costo variable            de $1,800 al mes más $2,000 mensuales por entretenimiento.
aumentará a $.60, pero el volumen debe elevarse a 50,000 unidades          a) ¿Cuál es su punto de equilibrio en dólares por mes?
debido a que el producto será de mayor calidad. ¿Considera usted           b) ¿Cuál es el número esperado de comidas por día si el estableci-
que la compañía debe comprar el equipo nuevo? PX                                miento abre 30 días al mes?
• • S7.21 La empresa de artículos electrónicos del problema                • • • S7.25 Use los datos del problema S7.24 y haga más realista el
S7.20 ahora está considerando el nuevo equipo y además aumentar            ejercicio al agregar el costo por mano de obra (como costo variable)
el precio de venta a $1.10 por unidad. Con el producto de mayor            que equivale a una tercera parte del costo total de comidas y
calidad, se espera un nuevo volumen de 45,000 unidades. Bajo esas          emparedados. También agregue gastos variables (implementos de
circunstancias, ¿debería la compañía comprar el nuevo equipo y             cocina, manteles, servilletas, etc.) equivalentes al 10% del costo
aumentar el precio de venta? PX                                            de cada categoría.
                                                                           a) ¿Cuál es su punto de equilibrio?
• • • • S7.22 Zan Azlett y Angela Zesiger se unieron para fundar           b) Si usted espera tener una utilidad anual de $35,000 (antes de
A&Z Lettuce Products, procesadora de lechuga cortada en tiras y                 impuestos) con jornadas de 12 horas, ¿cuáles deben ser sus ven-
empacada para uso institucional. Zan tiene años de experiencia en el            tas totales?
procesamiento de alimentos y Angela tiene amplia experiencia en la
preparación comercial de alimentos. El proceso consistirá en abrir         • • • S7.26 Como gerente de St. Cloud Theatre Company, usted
las cajas de lechuga para después seleccionarla, lavarla, cortarla,        decidió que las ventas concesionadas deben mantenerse por sí mis-
desinfectarla y, por último, empacarla ya preparada. Juntas, con           mas. En la tabla siguiente se proporciona la información que ha
ayuda de vendedores, consideran que pueden estimar en forma ade-           reunido hasta el momento:
cuada la demanda, los costos fijos, los ingresos y el costo variable
de una bolsa de 5 libras de lechuga. Piensan que un proceso princi-                            Precio de           Costo                % del
palmente manual tendrá costos fijos mensuales de $37,500 y costos           Artículo            venta             variable             ingreso
variables de $1.75 por bolsa. Un proceso más mecanizado tendrá
costos fijos de $75,000 mensuales y costos variables de $1.25 por           Refresco              $1.00             $ .65                 25
bolsa de 5 libras. Esperan vender cada bolsa de 5 libras de lechuga         Vino                   1.75               .95                 25
cortada en $2.50.                                                           Café                   1.00               .30                 30
a) ¿Cuál es el punto de equilibrio para el proceso manual?                  Dulce                  1.00               .30                 20
b) ¿Cuál es el ingreso en el punto de equilibrio para el proceso
     manual?                                                                   El gerente del año pasado, Jim Freeland, le aconsejó cerciorarse
c) ¿Cuál es el punto de equilibrio para el proceso mecanizado?             de agregar un 10% de costo variable como holgura por desperdicio
d) ¿Cuál es el ingreso en el punto de equilibrio para el proceso           en todas las categorías.
     mecanizado?                                                               Usted estimó el costo por mano de obra en $250.00 (5 mostrado-
e) ¿Cuál es la utilidad o pérdida mensual en el proceso manual si          res con 3 personas cada uno). Aun cuando no se vendiera nada, el
     esperan vender 60,000 bolsas de lechuga al mes?                       costo por mano de obra será de $250.00, por lo cual decidió consi-
f) ¿Cuál es la utilidad o pérdida mensual en el proceso mecanizado         derarlo como un costo fijo. La renta de cada mostrador, que es un
     si esperan vender 60,000 bolsas de lechuga al mes?                    costo contractual de $50.00 por cada mostrador por noche, también
g) ¿En qué cantidad el proceso seleccionado por Zan y Angela será          es un costo fijo.
     indistinto?                                                           a) ¿Cuál es el volumen del punto de equilibrio por noche de pre-
h) ¿En qué rango de demanda será preferible el proceso manual                  sentación?
     sobre el mecanizado? ¿En qué rango de demanda será preferible         b) ¿Qué cantidad de vino espera vender en el punto de equilibrio?
     el proceso mecanizado sobre el manual? PX
                                                                           • • S7.27 La posada con servicio de desayuno de James Lawson,
• • S7.23 Carter Manufacturing produce actualmente un                      ubicada en un pequeño poblado histórico de Mississippi, debe
despachador de cinta adhesiva con un costo variable de $0.75 por           decidir la forma de subdividir (remodelar) la gran casa antigua que
unidad y un precio de venta de $2.00 por unidad. Los costos fijos          convertirá en posada. Existen tres alternativas: la alternativa A
son de $20,000. El volumen actual es de 40,000 unidades. La com-           implica modernizar todos los baños y combinar habitaciones, con lo
pañía puede producir un mejor producto si agrega un nuevo equipo           cual la posada constaría de cuatro suites, para recibir de dos a cuatro
en la línea del proceso. Este equipo representa una adición de             adultos en cada una. Con la alternativa B se modernizaría sólo el
$5,000 al costo fijo. El costo variable disminuiría a $0.25 por            segundo piso y su resultado serían seis suites, cuatro para recibir de
                                                                                                                              Problemas      311
dos a cuatro adultos y dos para sólo dos adultos. La alternativa C                                          Máquina A            Máquina B
(la de estatus quo) dejaría intactas todas las paredes; en este caso se
dispondría de ocho habitaciones pero sólo dos podrían recibir cua-         Costo original                    $10,000               $20,000
tro adultos, y cuatro habitaciones no contarían con baño privado.          Mano de obra por año                2,000                 4,000
Abajo se presentan los detalles de la utilidad y la demanda que            Mantenimiento por año               4,000                 1,000
acompañan a cada alternativa:                                              Valor de recuperación               2,000                 7,000
                                                                          Determine, mediante el método del valor presente, qué máquina
                                    Utilidad anual bajo varios            debe recomendar Tim.
                                      patrones de demanda                 • • S7.34 Su jefe le ha pedido que evalúe dos hornos para Tink-
 Alternativas                    Alto      p          Promedio p          the-Tinkers, una tienda de emparedados gourmet. Después de investi-
                                                                          gar con los proveedores y de recibir las especificaciones, le aseguran
 A (modernizar todo)           $90,000     .5          $25,000     .5     que los hornos tienen los atributos y costos que se presentan en la
 B (modernizar el 2° piso)     $80,000     .4          $70,000     .6     tabla siguiente. Resulta apropiado considerar los siguientes supuestos:
 C (estatus quo)               $60,000     .3          $55,000     .7     1) La vida útil de cada horno es de 5 años.
                                                                          2) La compañía considera que sabe cómo ganar un 14% en inver-
a) Dibuje el árbol de decisiones para Lawson.
                                                                                siones menos riesgosas que ésta.
b) ¿Qué alternativa tiene el valor esperado más alto? PX
                                                                                                 Tres hornos pequeños      Dos hornos grandes
• • • S7.28 Como administrador de operaciones de Holz Furniture,                                   a $1,250 cada uno        a $2,500 cada uno
usted debe tomar una decisión de agregar o no una línea de muebles         Costo original         $3,750                   $5,000
rústicos. Al analizar las posibilidades con su gerente de ventas Steve     Costo de la mano
Gilbert, usted decide que definitivamente existe un mercado y que            de obra excedente
su empresa debe entrar a él. Sin embargo, como el acabado de los             para modelos más
muebles rústicos es distinto al de su producto estándar, necesitará          grandes              $ 750 (total)
otra línea de proceso. En su mente no hay duda de su decisión y está       Limpieza y             $ 750                    $ 400
seguro de necesitar un segundo proceso, pero desearía saber qué tan          mantenimiento        ($250 cada uno)          ($200 cada uno)
grande debe ser. Una línea de proceso grande costará $400,000 y            Valor de               $ 750                    $1,000
una línea pequeña, $300,000. Por lo tanto, la cuestión es conocer la         recuperación         ($250 cada uno)          ($500 cada uno)
demanda de muebles rústicos. Después de una extensa discusión
con el señor Gilbert y Tim Ireland, de Ireland Market Research,           a) Determine, mediante el método del valor presente, qué decirle a
Inc., usted determina que la mejor estimación es que sus posibili-             su jefe acerca de la máquina que debe comprar.
dades de obtener utilidad son dos de tres si logra ventas de alrededor    b) ¿Qué supuesto hizo usted sobre los hornos?
de $600,000, y una de tres posibilidades con ventas de aproximada-        c) ¿Qué supuestos está haciendo en su metodología?
mente $300,000.                                                           • • • • S7.35 Andre está investigando la viabilidad de instalar un
     Con una línea de proceso grande, usted podría manejar la cifra       puesto de crepas en el campus. Puede rentar un espacio en la unión
de $600,000; pero con una línea pequeña no podría y se vería              de estudiantes (el cual cuesta $300 al mes por concepto de renta y
forzado a realizar una expansión (con un costo de $150,000),              gastos generales). Sus costos por materiales y mano de obra son de
después de lo cual su utilidad sería de $500,000 en vez de $600,000       $1 por crepa, y el precio de venta es de $4 por crepa.
debido al tiempo perdido en ampliar el proceso. Si usted no amplía        a) ¿Cuál es la cantidad del punto de equilibrio para esta alternativa
el proceso pequeño, podría tener una utilidad por ventas de $400,000.          (es decir, ¿cuántas crepas por mes tendrá que vender Andre antes
Si construye un proceso pequeño y la demanda es baja, podría ma-               de obtener alguna utilidad?
nejar toda la demanda.                                                    b) Andre podría usar una máquina portátil para hacer crepas que le
     ¿Debe abrir una línea de proceso grande o una pequeña?                    prestaría un amigo y colocar el puesto fuera del ámbito de la
                                                                               unión de estudiantes. No tendría costos por renta o gastos gene-
• • S7.29 ¿Cuál es el valor presente neto de una inversión que                 rales (es decir, no tendría costos fijos), pero su amigo le pediría
cuesta $75,000 y tiene un valor de recuperación de $45,000? La                 $1.50 por cada crepa vendida. ¿Cuál es la cantidad del punto de
utilidad anual de la inversión es de $15,000 anuales durante 5 años.           equilibrio para esta posibilidad?
El costo de capital con este nivel de riesgo es del 12%. PX               c) Suponga que un sondeo informal muestra que Andre podría
                                                                               esperar vender 350 crepas al mes. ¿Qué alternativa de capacidad
                                                                               debería elegir: puesto en la unión de estudiantes o máquina
•    S7.30 El costo inicial de una inversión es de $65,000 y el                portátil para hacer crepas?
costo de capital es del 10%. El rendimiento es de $16,000 anuales         d) ¿Cuál sería la utilidad mensual con la mejor alternativa?
durante 8 años. ¿Cuál es su valor presente neto? PX                       e) ¿Por cuánto (y en qué dirección) tendría que ser diferente la
                                                                               demanda antes de considerar un cambio a la otra alternativa de
•    S7.31 Una inversión producirá $2,000 luego de tres años.                  capacidad?
¿Cuál es su valor hoy? Es decir, ¿cuál es su valor presente si la tasa    • • • • S7.36 Bold’s Gym, una cadena de clubes para hacer ejercicio,
de interés es del 9%? PX                                                  está considerando expandirse a una nueva ubicación: la inversión
                                                                          inicial sería de $1 millón por concepto de equipo, renovación y un
•    S7.32 ¿Cuál es el valor presente de $5,600 cuando la tasa de         préstamo a 6 años, y sus gastos de mantenimiento anual serían de
interés es del 8% y el rendimiento sobre los $5,600 se recibirá den-      $75,000. Su horizonte de planeación es de 6 años y al final de éstos
tro de 15 años? PX                                                        puede vender el equipo en $50,000. La capacidad del club es de 500
                                                                          miembros quienes pagarían una cuota anual de $600. Bold’s espera
• • S7.33 Se le pidió a Tim Smunt que evaluara dos máquinas.              no tener problemas para vender todas sus membresías. Suponga que
Después de algunas investigaciones determinó que los costos son           la tasa de interés es del 10%. (Vea la tabla S7.1).
los que se muestran en la tabla siguiente. Se le dijo a Tim que           a) ¿Cuál es el valor presente de la utilidad o pérdida del negocio?
supusiera que:                                                            b) El club está considerando ofrecer un contrato especial a sus
a) la vida útil de cada máquina es de 3 años, y                                miembros durante el primer año. Por un pago de $3,000 ahora
b) la compañía sabe cómo hacer una inversión al 12% con un riesgo              obtendrán una membresía total por 6 años (es decir, un año
   no mayor que éste.                                                          gratis). ¿Tendría algún sentido financiero hacer esta oferta?
312       Suplemento 7 • Planeación de la capacidad




Estudio de caso
 Planeación de la capacidad en el hospital Arnold Palmer Caso en
                                                          video
Desde su apertura en 1989, el hospital Arnold Palmer ha experimen-           Con una población en crecimiento continuo en su área de mer-
tado un crecimiento explosivo de la demanda de sus servicios. Es        cado, le da servicio a 18 condados del centro de Florida, el hospital
uno de los seis hospitales de Estados Unidos que se especializan en     Arnold Palmer daba asistencia en el nacimiento del equivalente a una
el cuidado de la salud de mujeres y niños. El hospital Arnold Palmer    clase de jardín de niños diariamente, pero ni así satisfacía la demanda.
ha atendido a más de 1’500,000 pacientes, quienes llegan a sus          Con base en un análisis demográfico adicional, el hospital estaba listo
instalaciones de Orlando desde las 50 entidades de Estados Unidos       para llevar a cabo un plan de expansión de su capacidad y construir un
y más de 100 países. El Arnold Palmer tiene calificaciones por la       nuevo edificio de 11 pisos frente a la instalación existente.
satisfacción del cliente ubicadas en el 10% superior para los hospi-         Se establecieron treinta y cinco equipos de planeación para
tales encuestados en Estados Unidos (más del 95% de los pacientes       estudiar aspectos como (1) sus pronósticos específicos; (2) los servi-
recomendarían el hospital a otras personas). Uno de los principales     cios que se transferirían a la nueva instalación; (3) los servicios que
enfoques del hospital es el nacimiento de bebés. Originalmente cons-    podrían permanecer en la instalación existente; (4) las necesidades
truido para 281 camas y capacidad para atender 6,500 nacimientos        de personal; (5) la inversión de capital en equipo; (6) los datos conta-
al año, el hospital se aproximó de manera gradual a los 10,000          bles pro forma, y (7) los requerimientos regulatorios. Al final, el
nacimientos y después superó esa cifra. Al observar la tabla S7.3, la   hospital Arnold Palmer estuvo listo para ejecutar un presupuesto de
directora ejecutiva Kathy Swanson supo que se necesitaba una            100 millones de dólares y estableció un compromiso para atender
expansión.                                                              150 camas adicionales. Pero dado el crecimiento de la región central
                                                                        de Florida, Swanson decidió expandir el hospital en etapas: los dos
                   Tabla S7.3                                          pisos superiores quedarían vacíos para ser completados en una fecha
                  Nacimientos en el hospital                            posterior, y el cuarto piso de quirófanos podría duplicarse en tamaño
                  Arnold Palmer                                         cuando fuera necesario. “Con la nueva instalación lista, ahora somos
                                                                        capaces de manejar 16,000 nacimientos al año”, dice Swanson.
                    Año            Nacimientos
                    1995                6,144                           Preguntas para análisis*
                    1996                6,230                            1. Dado el análisis de planeación de la capacidad examinado en el
                    1997                6,432                               texto (vea la figura S7.5), ¿qué enfoque está tomando el hospital
                    1998                6,950                               Arnold Palmer para lograr la correspondencia entre capacidad y
                                                                            demanda?
                    1999                7,377
                                                                         2. ¿Qué tipo de cambios importantes podría ocurrir en el pronós-
                    2000                8,655                               tico de la demanda del hospital Arnold Palmer que pudiera
                    2001                9,536                               dejarlo con una instalación subutilizada (es decir, cuáles son los
                    2002                9,825                               riesgos relacionados con esta decisión de capacidad)?
                    2003               10,253                            3. Use un análisis de regresión para pronosticar el punto en el cual
                    2004               10,555                               Swanson necesita “terminar” los dos pisos superiores del edifi-
                    2005               12,316                               cio nuevo, es decir, ¿cuándo excederá la demanda los 16,000
                    2006               13,070                               nacimientos?
                    2007 (est.)        13,600                           *Quizá desee ver el caso en video en su DVD antes de responder estas
                                                                        preguntas.




Estudios de casos adicionales
 Estudio de caso en internet: visite nuestro sitio web para consultar este estudio de caso:
 • Southwestern University’s Food Service D: Requiere el desarrollo de una solución de punto de equilibrio para productos múltiples.
 Harvard seleccionó estos casos de Harvard Business School para acompañar este suplemento:
 harvardbusinessonline.hbsp.harvard.edu
 • National Cranberry Cooperative (#688-122): Requiere que el estudiante analice el proceso, los cuellos de botella, y la capacidad.
 • Lenzing AG: Expanding in Indonesia (#796-099): Considera la forma en que la expansión afecta la posición competitiva de la
   compañía.
 • Chaparral Steel (#687-045): Examina la propuesta de una expansión importante de la capacidad en Chaparral Steel, una minifundi-
   dora de acero.
 • Align Technology, Inc., Matching Manufacturing Capacity to Sales Demand (#603-058): Análisis y planeación de la capacidad de
   producción.
 • Samsung Heavy Industries: The Koje Shipyard (#695-032): Explora las mejoras a la manufactura pero disminuyendo el desempeño
   después de expansiones de capital importantes.
                                                                                                         Recursos en internet   313

Bibliografía
Atamturk, A. y D. S. Hochbaum. “Capacity Acquisition,                 and Operations Management 12, núm. 4 (invierno de 2003):
     Subcontracting, and Lot-Sizing”. Management Science 47,          480-501.
     núm. 8 (agosto de 2001): 1081-1100.                           Jonsson, Patrik y Stig-Arne Mattsson. “Use and Applicability of
Bowers, John, et al. “Modelling Outpatient Capacity for a             Capacity Planning Methods”. Production and Inventory
   Diagnosis and Treatment Center”. Health Care Management            Management Journal (3° y 4° trimestres de 2002): 89-95.
   Science 8, núm. 3 (agosto de 2005): 205.                        Kekre, Sunder, et al. “Reconfiguring a Remanufacturing Line at
Cheng, H. K., K. Dogan, R. A. Einicki. “Pricing and Capacity          Visteon, Mexico”. Interfaces 33, núm. 6 (noviembre-diciembre
   Decisions for Non-Profit Internet Service Providers”.              de 2003): 30-43.
   Information Technology and Management 7, núm. 2                 Koste, L. L., M. K. Malhotra y S. Sharma. “Measuring Dimensions
   (abril de 2006): 91.                                               of Manufacturing Flexibility”. Journal of Operations
Goodale, John C., Rohit Verma y Madeleine E. Pullman. “A              Management 22, núm. 2 (abril de 2004): 171-196.
   Market Utility-Based Model for Capacity Scheduling in Mass      Lovejoy, William S. y Ying Li, “Hospital Operating Room
   Services”. Production and Operations Management 12, núm. 2         Expansion”. Management Science 48, núm. 11 (noviembre de
   (verano de 2003): 165-185.                                         2002): 1369-1387.
Hanfield, Robert B. y Kevin McCormack. “What You Need to           Wacker, J. G. y C. Sheu. “Effectiveness of Manufacturing Planning
   Know About Sourcing from China”. Supply Chain Management           and Central Systems on Manufacturing Competitiveness”.
   Review 9, núm. 6 (septiembre de 2005): 28-37.                      International Journal of Production Research 44, núm. 5
Jack, Eric P. y Amitabh S. Raturi. “Measuring and Comparing           (marzo de 2006): 1015.
   Volume Flexibility in the Capital Goods Industry”. Production



Recursos en internet
American Council of Engineering Companies: www.acec.org            DARPA: U.S. Defense Dept., Innovative Prototype Systems:
Association for Manufacturing Excellence: www.ame.org                 www.DARPA.mil
