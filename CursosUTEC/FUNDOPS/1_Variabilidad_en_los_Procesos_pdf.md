---
curso: FUNDOPS
titulo: 1 - Variabilidad en los Procesos
slides: 49
fuente: 1 - Variabilidad en los Procesos.pdf
---

La Variabilidad en los Procesos



                Expositor: Mg. Óscar Gamonal Pajares
                                                                                  Tiempo de Espera
            ¿Cuándo los usuarios de un servicio tienen que esperar para ser atendidos?

            1 – Cuando la demanda esperada es mayor a la capacidad de atención.
            2 – Cuando existe variabilidad en el tiempo entre llegadas, inclusive si
            es que existe capacidad de atención suficiente.




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 169
                                                                         Ejemplo – Call Center
            En un Call Center se ha asignado a una recepcionista de 7 am a 8 am, en
            promedio el Call Center recibe 12 llamadas por hora, y en promedio una
            llamada toma 4 minutos, lo que significa que en promedio recibe una
            llamada cada 5 minutos.

            ¿El proceso tiene la capacidad necesaria para atender la demanda de
            llamadas?
            Capacidad = (60 minutos/hora)/(4 minutos/llamada) = 15 llamadas/hora
            ¿En promedio cuánto tiempo tiene que esperar un cliente para ser atendido?
            Tiempo de Espera = 0 minutos
            ¿Cuál es el porcentaje de utilización del proceso?
            %Utilización = Tasa de Llegadas/Capacidad =12/15 = 80%


Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 169
                                                                         Ejemplo – Call Center




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 169
                                                                         Ejemplo – Call Center




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 170
                                                                         Ejemplo – Call Center




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 171
                     Conceptos Generales
Unidad de Flujo (Flow Unit): Es una unidad que llega al sistema como una
entrada (input), luego se procesa y sale del sistema (output).
Inventario (Inventory): Es el número de unidades de flujo que se encuentran
en el sistema, también se conoce como Work-In-Process - WIP.
Tiempo de Flujo (Flow Time): Es el tiempo que transcurre desde que una
unidad de flujo llega al sistema hasta que sale del sistema, eso significa que el
tiempo de flujo incluye el tiempo que la unidad tiene que esperar para ser
atendida.
Tasa de Flujo (Flow Rate): Es la tasa a la cual las unidades salen fuera del
sistema, también se denomina “throughput rate”. La tasa máxima a la cual el
proceso puede generar salidas se denomina “capacidad del proceso”.
                                                                                          Inventario




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 17
         Tiempo de Flujo Promedio (Average Flow Time)




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 18
                                                       La Ley de Little (Little’s Law)


Inventario Promedio (WIP) = Tasa de Flujo x Tiempo de Flujo

I = WIP = RxT

WIP = Work in Process




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 17
     ¿Por qué hay variabilidad en un Proceso?
Existen 4 fuentes de variabilidad:

1)   Variabilidad de las unidades entrantes.
2)   Variabilidad de procesamiento.
3)   Disponibilidad de los recursos.
4)   Rutas aleatorias para diferentes unidades.
                                                                         Ejemplo – Call Center




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 171
            ¿Cómo se mide la variabilidad?
Una medida de la variabilidad es la desviación estándar, la cual representa una
medida absoluta de la variabilidad, no indica si la variabilidad es alta o baja.

Para medir la variabilidad en términos relativos se debe utilizar el coeficiente
de variación:

                   CV = Desviación Estándar/Media = σ/μ
                                                                          Proceso de Llegadas
       Tiempo de llegada (arrival time - AT): Es el tiempo en el cual llega una unidad para
       ser procesada.
       Tiempo entre llegadas (interarrival time - IA): Es el tiempo que transcurre entre 2
       llegadas consecutivas.

                                                                                           IAi = ATi+1 – ATi




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 173
                                          Proceso Estacionario de Llegadas
       Proceso estacionario de llegadas: Es aquel proceso en el que para cualquier
       intervalo de tiempo el número esperado de llegadas depende del tamaño del
       intervalo, no depende del tiempo de inicio del intervalo.
       Cuando el tiempo entre llegadas es exponencialmente distribuido el proceso se
       denomina proceso de llegadas Poisson.
       Un proceso de llegadas que contiene estacionalidad no es estacionario.




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 173
                                                                                Datos de Llegadas
           Calcular los tiempos entre
           llegadas a partir de los
           tiempos de llegadas




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 174
                                                                          Proceso de Llegadas
       Análisis para determinar si un proceso es estacionario: La curva de tiempos de
       llegada no debe alejarse de la recta que une el primer y el último punto del intervalo.




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 173
Distribución Exponencial de Tiempo entre Llegadas

 Si los tiempos entre llegadas se distribuyen aleatoriamente según una función
 exponencial se cumple que:


                            Probabilidad [IA <= t] = 1 – e –t/a
 Donde:
          a = Tiempo promedio entre llegadas = Desviación estándar del tiempo entre llegadas


 Si los tiempos entre llegadas son exponenciales, el proceso de llegadas es
 Poisson.
 Una propiedad importante de la función exponencial es que “no tiene
 memoria”, esto significa que la siguiente llegada al proceso no depende de la
 llegada más reciente.
Distribución Exponencial de Tiempo entre Llegadas




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 177
Distribución Exponencial de Tiempo entre Llegadas




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 177

                        Variabilidad del Tiempo de Procesamiento




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 180
            Tiempos de Procesamiento con Estacionalidad




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 181
                       Variabilidad del Tiempo de Procesamiento
       Las unidades llegan al sistema siguiendo un patrón de demanda aleatorio.

       a = 1/λ = Tiempo esperado entre Llegadas
       Tasa de Flujo de Llegadas (Flow Rate) = R = λ = 1/a




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 181
                    Tiempo de Espera Promedio con 1 Recurso
       Las unidades son procesadas en un tiempo de procesamiento aleatorio.

       p = Tiempo Promedio de Procesamiento de una Unidad en el Servidor
       Capacidad del Servidor = 1/p
       Utilización (u) = Flow Rate/Capacidad = (1/a)/(1/p) = p/a < 100%




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 181
                    Tiempo de Espera Promedio con 1 Recurso
       El tiempo de flujo (flow time) es igual al tiempo de espera en la cola (waiting
       time) más el tiempo de procesamiento (processing time).

       Tq = Tiempo de Espera en la Cola
       Tiempo de Flujo (Flow Time): T = Tq + p




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 182
                    Tiempo de Espera Promedio con 1 Recurso
       El inventario total es igual al inventario en la cola más el inventario en proceso.

       Iq = Inventario en la Cola
       Ip = Inventario en Proceso o Inventario en Servicio
       I = Inventario en el Sistema o Inventario Total (WIP-Work in Process)
       I = Iq + Ip




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 182
                    Tiempo de Espera Promedio con 1 Recurso
       Para un proceso estacionario el tiempo de espera en la cola depende de 3
       factores: del tiempo de procesamiento, del porcentaje de utilización y de las
       variabilidades del tiempo entre llegadas y del tiempo de servicio o
       procesamiento, no se requiere que el tiempo entre llegadas y el tiempo de
       servicio sigan una distribución estadística específica.



               Tiempo en la Cola = Tq = p.[Utilización/(1-Utilización)].[(CVa2+ CVp2)/2]




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 182
                                                                         Ejemplo – Call Center
            En un Call Center se ha asignado a una recepcionista de 2 am a 3 am,
            en promedio una llamada toma 90 segundos, y la desviación estándar
            del tiempo de procesamiento es 120 segundos. En ese horario se
            reciben 3 llamadas en el lapso de 15 minutos. Calcular:

            a) El tiempo entre llegadas.
            b) El porcentaje de utilización.

            a = 15/3 = 5 minutos = 300 segundos
            p = 90 segundos
            σp = 120 segundos
            Utilización = p/a = 90/300 = 0.3 = 30%

Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 169
                                                                         Ejemplo – Call Center
            Considerando que las llegadas se distribuyen de acuerdo a un proceso
            Poisson (los tiempos entre llegadas son exponenciales, CVa = 1), calcular
            el tiempo esperado en la cola y el tiempo de flujo.

            Tq = p.[Utilización/(1-Utilización)].[(CVa2+ CVp2)/2]

            Tq = 90.[0.3/(1-0.3)].[(12 + (120/90)2)/2] = 53.57 segundos

            T = Tq + p = 53.57 + 90 = 143.57 segundos




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 169
                                                                         Ejemplo – Call Center
            Calcular el inventario promedio en el sistema.

            Por la Ley de Little: I = R.T = 1/a(Tq + p)

            R = 1/a
            R = 1/300 unidades/segundo

            T = Tq + p
            T = 143.57 segundos
            I = 143.57/300 = 0.479 unidades



Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 169
                                                                         Ejemplo – Call Center
            Calcular el inventario promedio en la cola.

            Por la Ley de Little: Iq = R.Tq = Tq /a
            R = 1/a
            R = 1/300 unidades/segundo
            Tq = 53.57 segundos
            Iq = 53.57/300 = 0.179 unidades




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 169
                                                                         Ejemplo – Call Center
            Calcular el número promedio de llamadas en servicio.

            Ip = Prob[0 llamadas]x0 + Prob[1 llamada].1

            Ip = (1 - Utilización)x0 + Utilización.1 = (1-u).0 + u.1 = u

            Ip = 0.3 llamadas




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 169
      Tiempo de Espera Promedio con Múltiples Recursos




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 186
      Tiempo de Espera Promedio con Múltiples Recursos
       Capacidad = m/p
       Utilización = Tasa de Flujo/Capacidad = (1/a)/(m/p) = p/(axm)
       Flow Time = Tiempo de Flujo = T = Tq + p

       Tq = (p/m).[Utilización 𝟐(𝒎 + 𝟏) − 𝟏/(1-Utilización)].[(CVa2+ CVp2)/2]

       I = I p + Iq

       Inventario en Proceso = Número de Recursos x Utilización

       Ip = m.u = p/a
       Iq = R.Tq = (1/a).Tq
Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 182
      Tiempo de Espera Promedio con Múltiples Recursos




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 187
 Ejemplo de Tiempo de Espera Promedio con Múltiples Recursos
       En cierto día llegan 79 clientes a un banco desde las 8:00 am hasta las 8:15
       am, existen 10 ventanillas de atención, si en promedio el tiempo de atención
       es igual a 1.5 minutos por cliente y la desviación estándar es igual a 2 minutos,
       calcular el tiempo promedio que cada cliente tiene que esperar en la cola.
       Considere que el tiempo entre llegadas siguen una distribución exponencial.
       σp = 2 minutos
       p = 1.5 minutos
       m = 10
       a = Tamaño del Intervalo de Tiempo/Nro. de Clientes = 15x60/79 = 11.39 seg.
       u = p/am = 90/(11.39x10) = 0.79
       CVp = σp/p = 2/1.5 = 1.33
       CVa = 1

Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 182
 Ejemplo de Tiempo de Espera Promedio con Múltiples Recursos
       Tq = (p/m).[Utilización 𝟐(𝒎 + 𝟏) − 𝟏/(1-Utilización)].[(CVa2+ CVp2)/2]
       Tq = (90/10).[0.79 2(10 + 1) − 1/(1-0.79)].[(12+ 1.332)/2]
       Tq = 24.94 segundos




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 182
   Caso de Tiempo de Espera Promedio con Múltiples Recursos
       Considerando los datos del Call Center del archivo Excel, en el rango de 6:00 am a
       10:00 am, y sabiendo que se han asignado 10 recepcionistas, si en promedio el
       tiempo de atención es igual a 3 minutos por cliente y la desviación estándar del
       tiempo de atención es igual a 5 minutos, calcular:
       a) El tiempo esperado entre llegadas.
       b) La tasa de flujo (flow rate o throughput).
       c) El porcentaje de utilización de los recursos.
       d) El tiempo promedio que cada cliente tiene que esperar en la cola.
       e) El tiempo de flujo (flow time).
       f) El inventario en servicio.
       g) El inventario en la cola.
       h) El inventario total.
       i) ¿Cuál es el número mínimo de recepcionistas que se deben asignar para que el
           tiempo de espera sea inferior a 1 minuto?
Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 182
      Tiempo de Espera Promedio con Múltiples Recursos
       σp = 5 minutos
       p = 3 minutos
       m = 10 recepcionistas
       a) Intervalo de Tiempo = 4 horas, Nro. de Llamadas = 687 llamadas
          a = Tiempo entre Llegadas Promedio
          a = 20.89 segundos (obtenido del archivo Excel 4)
       b) R = 1/a = (1 /20.89)x60 = 2.87 clientes/minuto
       c) u = p/am = (3x60)/(20.89x10) = 86.17%
       d) CVp = σp/p = 5/3 = 1.667, CVa = 1.275 (obtenido del archivo Excel 4)
          Tq = (p/m).[Utilización 𝟐(𝒎 + 𝟏) − 𝟏/(1-Utilización)].[(CVa2+ CVp2)/2]
          Tq = (3/10).[0.8617 2(10 + 1) − 1/(1-0.8617)].[(1.2752+ 1.6672)/2]
          Tq = 2.76 minutos
Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 182
      Tiempo de Espera Promedio con Múltiples Recursos
       e) T = Tq + p = 2.76 + 3 = 5.76 minutos
       f) Ip = mxu = 10x0.8617 = 8.617 clientes
       g) Iq = RxTq = 2.87x2.76 = 7.92 clientes
       h) I = Ip + Iq = 16.53 clientes
       i) m = 12 recepcionistas, Tq = 0.502 minutos = 30.12 segundos




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 182

               Nivel de Servicio para los Tiempos de Espera
       Es la probabilidad de que los clientes empiecen a ser atendidos en un tiempo
       menor o igual a un tiempo límite.

                            Nivel de Servicio = Probabilidad[t de espera <= tiempo límite]

       Nivel de Servicio = Prob[t de espera <= 3 minutos] = 95%




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 188
               Nivel de Servicio para los Tiempos de Espera




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 189
      Trade-Off entre el Tiempo de Espera y el Número de Servidores

       Para llevar a cabo el análisis del trade-off entre el tiempo de espera y el
       número de servidores se deben considerar los siguientes costos:

       •       Costo de espera.
       •       Costo del servicio (costo de los servidores).
       •       Costo de los clientes que se retiran de la cola mientras esperan el servicio.
       •       Costo relacionado a llamadas de clientes que reciben la señal de “ocupado”.

                                             Costo de M.O. Directa = Salario Total/Tasa de Flujo




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 190
      Trade-Off entre el Tiempo de Espera y el Número de Servidores




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 190
      Trade-Off entre el Tiempo de Espera y el Número de Servidores

       El costo de una recepcionista en un Call Center es de 10 US$/hora, las
       llamadas se reciben a través del servicio 1-800, el cual representa un costo de
       0.05 $/minuto, que se debe aplicar al tiempo de espera y al tiempo de atención
       de la llamada. El gerente del Call Center desea que las llamadas sean
       contestadas en un promedio de 10 segundos. La duración de cada llamada es
       igual a 3 minutos en promedio.

       Considerando el rango de 8:00 am a 8:15 am del archivo Excel de registro de
       llamadas del Call Center, elabore una tabla que muestre el valor esperado del
       tiempo de espera para varios valores correspondientes al número de
       recepcionistas disponibles, de tal forma que sea posible elegir el menor
       número de recepcionistas que hagan que se cumpla con los requerimientos
       especificados por el gerente del Call Center.

Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 190
      Trade-Off entre el Tiempo de Espera y el Número de Servidores

       σp = 5 minutos, p = 3 minutos
       Costo de Llamada 1-800 = 0.05 US$/minuto
       Costo de Recepcionista = 10 US$/hora x recepcionista
       Tiempo de Espera deseado <= 10 segundos
       Hora inicial = 8:00 am
       Hora Final = 8:15 am
       Intervalo de Tiempo = 900 segundos
       Número de Clientes = 42 clientes (obtenido de la hoja de cálculo 5)
       a = 19.49 segundos/cliente (obtenido de la hoja de cálculo 5)
       R = 1/a = 60/19.49 = 3.08 clientes/minuto
       CVp = σp/p = 5/3 = 1.667
       CVa = σa/a = 0.954 (obtenido de la hoja de cálculo 5)
Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 190
      Trade-Off entre el Tiempo de Espera y el Número de Servidores
                                                                         Trade-Off entre Tiempos de Espera y Número de Servidores


                                                         σp =                                                    5 minutos
                                                         p=                                                      3 minutos
                                                         Hora Inicial =                                   08:00:00 am
                                                         Hora Final =                                     08:15:00 am
                                                         Tamaño del intervalo =                                900 segundos
                                                         Número de Clientes =                                   42 clientes
                                                                                            Se utiliza este valor para todos los cálculos
                                                         a (cuando no hay datos de llamadas) =               21.43 segundos/cliente
                                                         a (cuando hay datos de llamadas) =                  19.49 segundos/cliente
                                                         R=                                                   3.08 clientes/minuto
                                                         CVp =                                               1.667
                                                         CVa (para el rango de 8:00 a 8:15 am) =             0.954
                                                                Se obtiene del rango de tiempo entre llamadas de 8:00 am a 8:15 am



                                                         Costo de Llamada 1-800 =                              0.05 US$/minuto
                                                         Costo de Recepcionista =                                10 US$/horaxrecepcionista
                                                         Tiempo de Espera Deseado <=                             10 segundos

Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 190
      Trade-Off entre el Tiempo de Espera y el Número de Servidores
                                                                           Importante: Se está considerando los datos de las llamadas de 8:00 am a 8:15 am

                                                                                           % Utilización       Tq      Costo de M.O. Costo de la Línea Costo Total
                                                                            m
                                                                                            (u = p/am)   (segundos) por Llamada        por Llamada     por Llamada
                                                                             1                   923.65%      -372.21
                                                                             2                   461.83%      -421.36
                                                                             3                   307.88%      -415.97
                                                                             4                   230.91%      -387.13
                                                                             5                   184.73%      -355.46
                                                                             6                   153.94%      -334.67
                                                                             7                   131.95%      -340.94
                                                                             8                   115.46%      -427.78
                                                                             9                   102.63%    -1,535.44
                                                                            10                    92.37%       324.31         0.5413            0.4203       0.9616
                                                                            11                    83.97%        95.23         0.5955            0.2294       0.8248
                                                                            12                    76.97%        41.08         0.6496            0.1842       0.8338
                                                                            13                    71.05%        20.34         0.7037            0.1670       0.8707
                                                                            14                    65.98%        10.83         0.7579            0.1590       0.9169
                                                                            15                    61.58%          6.02        0.8120            0.1550       0.9670
                                                                            16                    57.73%          3.45        0.8661            0.1529       1.0190
                                                                            17                    54.33%          2.02        0.9203            0.1517       1.0719
                                                                    Número de Recepcionistas necesarias para que el tiempo
                                                                    esperado en la cola (Tq) sea menor a 10 segundos.




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 190
     Número de Servidores y Número de Clientes por Rango Horario




Adapted from “Matching Supply with Demand”, Author: Gerard Cachon, 4th Edition, page 192

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
