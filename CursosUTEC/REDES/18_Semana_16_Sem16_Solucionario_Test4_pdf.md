---
curso: REDES
titulo: 18 - Semana 16/Sem16_Solucionario_Test4
slides: 3
fuente: 18 - Semana 16/Sem16_Solucionario_Test4.pdf
---

garias@utec.edu.pe
CS4054: Redes y Comunicaciones — 26-1
5 de julio de 2026
                           Solucionario - Test de Salida — Laboratorio 4 — Network Layer



                                        Pregunta 1 – Verdadero y Falso (2.0 puntos)
   Indique si las siguientes afirmaciones son verdaderas (V) o falsas (F).                                                         0.25 pt c/u
( V ) Los mensajes ICMP se encapsulan dentro de datagramas IP, pero no llevan información de puertos de la capa de
transporte.
Justificación: ICMP opera nativamente en la capa de red; se identifica por campos de Tipo y Código, prescindiendo de puertos TCP/UDP.
( V ) La fragmentación IP puede ocurrir tanto en el host de origen como en los routers intermedios a lo largo de la ruta.
Justificación: En IPv4, cualquier router intermedio fragmentará el paquete si este supera el MTU del siguiente enlace (y el bit DF está en 0).
( F ) El mecanismo NAT se diseñó y se utiliza principalmente para ampliar el espacio de direccionamiento nativo de redes
IPv6.
Justificación: NAT se diseñó como una solución de emergencia para mitigar el agotamiento de direcciones IPv4, no para IPv6.
( V ) En una red residencial tı́pica con NAT (NAPT), múltiples equipos internos comparten una única dirección IP
pública hacia el exterior.
Justificación: NAPT mapea múltiples direcciones privadas internas y sus puertos a una sola dirección IP pública asignada por el ISP.
( V ) El campo Time to Live (TTL) del encabezado IPv4 se reduce en una unidad por cada router que procesa y reenvı́a
el datagrama.
Justificación: Es el mecanismo estándar para evitar bucles infinitos de enrutamiento en la red.
( F ) Los mensajes ICMP de tipo Destination Unreachable (Destino Inalcanzable) son generados únicamente por el host
de destino final.
Justificación: Cualquier router intermedio puede generarlo si no posee una ruta hacia la red de destino en su tabla de enrutamiento.
( V ) Una de las desventajas técnicas de NAT es que rompe el principio de comunicación de extremo a extremo (end-to-
end) de la arquitectura de Internet.
Justificación: Modifica los encabezados de red/transporte en tránsito, impidiendo que hosts externos inicien conexiones directas hacia el
interior.
( F ) En el encabezado IPv4, las direcciones IP de origen y destino pueden modificarse dinámicamente mediante el uso
de routers estándar sin funciones NAT.
Justificación: Un enrutamiento estándar solo modifica las direcciones MAC (capa de enlace); las direcciones IP de capa 3 permanecen intactas.


                                       Pregunta 2 – ICMP Traceroute (2.50 puntos)
   El comando traceroute (o tracert) utiliza las propiedades del protocolo ICMP y del encabezado IP para inferir la
ruta que sigue un paquete hacia un destino remoto.
    a) Describa brevemente el principio de funcionamiento de este comando, explicando cómo logra descubrir de forma
       secuencial cada salto (router) de la ruta.                                                               1.0pt

            Respuesta

            La herramienta envı́a una serie de paquetes de sondeo (sondas UDP o ICMP Echo Request) orientados al
            destino final, iniciando con el campo TTL = 1. El primer router intermedio recibe el paquete, decrementa
            el TTL a 0, descarta el paquete y devuelve un mensaje de error ICMP Time Exceeded, revelando ası́ su
            dirección IP. Luego, la herramienta envı́a otra ráfaga con TTL = 2, forzando al segundo router a responder
            de la misma manera. Este incremento secuencial del TTL continúa de salto en salto hasta que el paquete
            alcanza al host de destino final.

    b) Explique e indique explı́citamente qué campos del encabezado IP y qué tipo/código de mensajes ICMP varı́an
       durante la ejecución de la herramienta.                                                              0.75pt

            Respuesta

                    Campos del encabezado IP: Varı́a el campo TTL (Time to Live), el cual incrementa linealmente
                    (1, 2, 3, . . . ). Debido a este cambio, también varı́an los campos Header Checksum e Identification.
                    Mensajes ICMP de routers intermedios: Devuelven mensajes ICMP Tipo 11, Código 0
                    (Time to Live exceeded in transit).
                    Mensaje ICMP del destino final: Depende del sistema operativo:
                     • En Linux/Unix (sondas UDP): Devuelve un ICMP Tipo 3, Código 3 (Destination Unreachable
                         - Port Unreachable) debido a que se apunta a un puerto UDP cerrado.
                     • En Windows (sondas ICMP): Devuelve un ICMP Tipo 0, Código 0 (Echo Reply).

                                                                       1
   c) Durante una prueba práctica, usted nota que algunos saltos intermedios muestran asteriscos (* * *) y no respon-
      den. Explique dos causas técnicas por las cuales ocurre este fenómeno.                                  0.75pt

          Respuesta

          El alumno debe mencionar al menos dos de las siguientes razones válidas:
              1. Filtrado por Firewall o ACLs: El router o un dispositivo de seguridad perimetral en ese salto
                 está configurado para descartar los paquetes de sondeo entrantes o bloquear la salida de mensajes
                 de error ICMP.
              2. Limitación de tasa ICMP (ICMP Rate Limiting): Con el fin de proteger la CPU, muchos
                 routers modernos limitan la cantidad de tráfico ICMP generado por segundo. Si se supera este lı́mite,
                 descartan las solicitudes sin responder.
              3. Congestión o pérdida de paquetes: Fluctuaciones extremas en el enlace provocan que se pierda
                 la sonda de ida o el mensaje ICMP de retorno antes de llegar al host origen.




                                 Pregunta 3 – Fragmentación IPv4 (2.0 puntos)
   Al realizar su experiencia con Wireshark en el laboratorio, observa que al enviar un paquete de datos de 3000 bytes
utilizando IPv4, este se ve obligado a fragmentarse debido a las limitaciones del enlace. Cada fragmento resultante viaja
con un MTU máximo de 1460 bytes. Suponga una cabecera IP estándar de 20 bytes y sin opciones adicionales.

   a) Calcule detalladamente cuántos fragmentos totales se generan para transmitir la carga útil (payload) total y
      determine el tamaño de la carga útil del último fragmento.                                            1.0pt

          Procedimiento y Solución

          1. Datos Iniciales:
                   Tamaño total del datagrama original = 3000 bytes
                   Tamaño de la cabecera IP (Header) = 20 bytes
                   Carga útil total a transmitir (Payload total) = 3000 − 20 = 2980 bytes
                   MTU del enlace = 1460 bytes
                   Carga útil máxima por fragmento = 1460 − 20 = 1440 bytes
          Nota técnica: El valor de 1440 es divisible por 8 (1440/8 = 180), por lo que es un tamaño de fragmento
          válido.
          2. Distribución de fragmentos:
                   Fragmento 1: Carga útil = 1440 bytes (Tamaño total = 1460 bytes)
                   Fragmento 2: Carga útil = 1440 bytes (Tamaño total = 1460 bytes)
                   Carga útil acumulada en F1 y F2: 1440 + 1440 = 2880 bytes
                   Carga útil restante para F3: 2980 − 2880 = 100 bytes
                   Fragmento 3: Carga útil = 100 bytes (Tamaño total = 100 + 20 = 120 bytes)
          Respuesta: Se generan un total de 3 fragmentos y el último tiene una carga útil de 100 bytes.


   b) ¿Qué valor numérico exacto (en unidades de 8 bytes) tiene el campo Fragment Offset en el segundo fragmento
      generado? Muestre su procedimiento de cálculo.                                                         0.5pt

          Procedimiento y Solución

          El campo Fragment Offset expresa el desplazamiento de los datos con respecto al inicio del payload del
          datagrama original, medido en bloques de 8 bytes.
          El segundo fragmento comienza inmediatamente después de los datos enviados en el primer fragmento
          (1440 bytes).
                                            Bytes enviados previamente      1440 bytes
                           Fragment Offset =                            =                = 180
                                                        8                 8 bytes/unidad
          Respuesta: El valor exacto del campo Fragment Offset para el segundo fragmento es 180.


   c) Explique detalladamente qué ocurrirı́a en el destino final y con el rendimiento de la red si solo uno de los fragmentos
      intermedios se pierde o se corrompe durante la transmisión.                                                       0.5pt
                                                              2
Respuesta

  En el destino final: IPv4 no cuenta con un mecanismo para recuperar o solicitar la retransmisión de
  fragmentos individuales. Por lo tanto, el receptor retiene los fragmentos válidos en un búfer de reensam-
  blado hasta que expire su temporizador interno (reassembly timer). Al cumplirse el tiempo, el destino
  **descarta todos los fragmentos recibidos** de ese datagrama y envı́a un mensaje ICMP Tipo 11,
  Código 1 (Fragment reassembly time exceeded).
  En el rendimiento de la red: Provoca un **desperdicio ineficiente de recursos** (ancho de banda y
  procesamiento), ya que los fragmentos que sı́ viajaron con éxito terminan siendo basura en el receptor.
  Esto obliga a los protocolos de la capa de transporte (como TCP) a **retransmitir desde el origen el
  paquete completo original de 3000 bytes**, amplificando notablemente la congestión en la red.




                                                  3
