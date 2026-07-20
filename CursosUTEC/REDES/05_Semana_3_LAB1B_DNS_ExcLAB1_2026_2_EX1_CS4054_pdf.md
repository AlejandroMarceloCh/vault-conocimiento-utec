---
curso: REDES
titulo: 05 - Semana 3 _ LAB1B_DNS + ExcLAB1/2026-2 EX1 CS4054
slides: 4
fuente: 05 - Semana 3 _ LAB1B_DNS + ExcLAB1/2026-2 EX1 CS4054.pdf
---

cwilliams, garias@utec.edu.pe
CS4054: Networks — 26-1
April 7, 2026
                         Ex 1: Fundamental concepts - Application layer



   Nota
   Propagation delay (dprop ): es el tiempo que tarda un bit en propagarse desde el emisor hasta el
   receptor.

   Nota
   Transmission delay (dtrans ): es el tiempo necesario para transmitir todos los bits de un paquete
   al enlace.


Question 1. Este problema elemental comienza a explorar el propagation delay y el transmission
delay, dos conceptos centrales en data networking. Considera dos hosts, A y B, conectados por un único
enlace de tasa R bps. Supongamos que los dos hosts están separados por m metros, y que la velocidad de
propagación a lo largo del enlace es s metros/seg. El host A debe enviar un paquete de tamaño L bits al
host B.
   1) Expresa el propagation delay dprop en términos de m y s.
   2) Determina el transmission time del paquete dtrans en términos de L y R.
   3) Ignorando los processing delay y queuing delay, obtén una expresión para el end-to-end delay.
   4) Supón que el host A comienza a transmitir el paquete en el tiempo t = 0. En el tiempo t = dtrans ,
      ¿dónde se encuentra el last bit del paquete?
   5) Supón que dprop es mayor que dtrans . En el tiempo t = dtrans , ¿dónde se encuentra el first bit del
      paquete?
   6) Supón que dprop es menor que dtrans . En el tiempo t = dtrans , ¿dónde se encuentra el first bit del
      paquete?
   7) Supón que s = 2.5 × 108 , L = 1500 bytes, y R = 10 Mbps. Encuentra la distancia m tal que
      dprop = dtrans .

   Nota
   Round-trip time (RTT): es el tiempo que tarda un paquete pequeño en viajar desde el cliente
   hasta el servidor y luego regresar al cliente. El RTT incluye packet-propagation delays, packet-queuing
   delays en routers y switches intermedios, y packet-processing delays.




                                                      1
                                                                                                             2

Question 2. Supongamos que al hacer click en un enlace no existe la entrada DNS en la caché local, por
lo que se visitan n DNS servers secuencialmente, con RTT1 , . . . , RTTn los round-trip times a cada uno.
Sea RTT0 el RTT entre el host local y el servidor que contiene el objeto. El objeto es pequeño (texto
HTML) y asumimos tiempo de transmisión cero ¿Cuánto tiempo transcurre desde que el cliente hace click
en el enlace hasta que recibe el objeto?

   Nota: Non-persistent vs Persistent HTTP
   Non-persistent HTTP:
      • Cada objeto (HTML, imagen, script, etc.) requiere una nueva conexión TCP.
      • Para cada objeto: three-way handshake (1 RTT) + petición/respuesta HTTP (1 RTT).
      • Cada objeto adicional incurre en 2 RTT0 , más el tiempo de transmisión si aplica.
   Persistent HTTP:
      • Una sola conexión TCP reutilizada para varios objetos.
      • Handshake inicial: 1 RTT0 .
      • Cada objeto adicional: sólo 1 RTT0 para la petición-respuesta.


Question 3. Refiriéndose al ejercicio anterior, supongamos que el archivo HTML hace referencia a ocho
objetos muy pequeños en el mismo servidor. Despreciando los tiempos de transmisión, ¿cuánto tiempo
transcurre con:
   1) Non-persistent HTTP sin conexiones TCP paralelas?
   2) Non-persistent HTTP con el navegador configurado para 6 parallel connections?
   3) Persistent HTTP?
   4) Asumiendo los valores Valores dados: S = ni=1 RTTi = 120 ms, RTT0 = 80 ms, N = 10..
                                                     P

      Calcule los tiempos para los 3 casos, he indique el más eficiente.
                                         Laboratory Questions

Question 4. Considera la siguiente cadena de caracteres ASCII que fue capturada por Wireshark cuando
el navegador envió un mensaje HTTP GET (es decir, este es el contenido real de un mensaje HTTP GET). Los
caracteres <cr><lf> son caracteres de retorno de carro y salto de lı́nea (es decir, la cadena en itálica <cr>
en el texto representa el carácter de retorno de carro que estaba contenido en ese punto del header HTTP).
GET /cs453/index.html HTTP/1.1<cr><lf>
Host: gaia.cs.umass.edu<cr><lf>
User-Agent: Mozilla/5.0 (Windows;U; Windows NT 5.1; en-US; rv:1.7.2)
Gecko/20040804 Netscape/7.2 (ax)<cr><lf>
Accept: text/xml, application/xml, application/xhtml+xml, text/html;q=0.9,
text/plain;q=0.8, image/png,*/*;q=0.5<cr><lf>
Accept-Language: en-us,en;q=0.5<cr><lf>
Accept-Encoding: zip,deflate<cr><lf>
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7<cr><lf>
Keep-Alive: 300<cr><lf>
Connection: keep-alive<cr><lf><cr><lf>
   Responde a las siguientes preguntas, indicando en qué parte del mensaje HTTP GET se encuentra la
respuesta:
    1) ¿Cuál es la URL del documento solicitado por el navegador?
    2) ¿Qué versión de HTTP está utilizando el navegador?
    3) ¿El navegador solicita una conexión non-persistent o persistent?
    4) ¿Cuál es la dirección IP del host en el que se está ejecutando el navegador?
    5) ¿Qué tipo de navegador inicia este mensaje? ¿Por qué es necesario el tipo de navegador en un
       mensaje HTTP request?
                                                                                                      3



Question 5. . Comprehensive HTTP/1.1 Analysis with Wireshark
 Instructions
  1) Clear your browser cache.
  2) Open Wireshark, set the capture filter to http, and begin capturing traffic.
  3) Visit the following URL in your browser:
        http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html (HTML file with
     embedded objects).
  4) Once the page is fully loaded, stop the capture.
  5) Expand the packet details in Wireshark to inspect Frame, Ethernet, IP, TCP, and HTTP informa-
     tion. Make sure you can navigate between the different protocol layers.
 Based on your Wireshark capture, answer.
  1) How many HTTP GET requests were generated in total? List their corresponding destination IP
     addresses.
  2) What HTTP version does your browser use in these requests? How can you confirm this inside
     Wireshark?
  3) Inspect one HTTP GET request: list at least three headers included by the browser (e.g., Host,
     User-Agent, Accept-Language). Explain what each header communicates to the server.
  4) For one of the server responses, identify the status code and phrase. What additional headers are
     present in the response (e.g., Content-Type, Content-Length)?
  5) Do all objects (HTML + images) come from the same server, or do they involve multiple servers?
     Support your answer with the IP addresses and Host fields shown in Wireshark.
  6) Were the embedded images retrieved sequentially or in parallel? Explain how you used Wireshark’s
     time-stamps or packet order to determine this.
  7) Navigate through the packet details pane: at which layer (Frame, Ethernet, IP, TCP, HTTP) do
     you find information about the source MAC address, the source IP address, and the HTTP status
     code?
  8) Compare the Content-Length or Transfer-Encoding fields among the responses. Does the server send
     all resources in a single chunk or in multiple segments? Explain how Wireshark helps you confirm
     this.
  9) Identify the TCP handshake packets (SYN, SYN/ACK, ACK) associated with the first HTTP
     connection. How does this handshake relate to the later HTTP GET request?
 10) Check whether any packets were retransmitted or lost during the transfer (look for “[TCP Retrans-
     mission]” or similar notes in Wireshark). If so, explain how this could affect the user’s browsing
     experience.
 11) Export the captured HTTP objects using Wireshark’s “File → Export Objects → HTTP” feature.
     Compare the size of one exported object (e.g., an image) with the Content-Length reported in the
     HTTP header. Do they match? Why might there be a difference?
Question 6. Perform and analyze DNS queries that force both UDP and TCP communication. Follow
these steps:
   1) Clear the DNS cache on your host machine.
   2) Open Wireshark and apply the dns filter.
   3) Using the command prompt, perform the following queries in order:
        (a) nslookup -type=A www.icann.org
       (b) nslookup -type=ANY google.com
        (c) nslookup -type=AAAA www.youtube.com
   4) Stop the capture and analyze the traffic:
          • Compare the queries that used UDP with those that switched to TCP.
          • Check whether multiple queries were generated for the same request.
          • Observe the response sizes and note when truncation occurs.
                                                                                                        4

  Answer.
   1) Which queries were handled entirely over UDP, and which required TCP? Explain the reason.
   2) In the ANY google.com query, how many answers were returned? Which types of records were
      included?
   3) What does the “TC” (Truncated) flag in the DNS header indicate, and in which query did you
      observe it?
   4) Compare the source/destination ports in UDP vs. TCP DNS messages. Why does the behavior
      differ?
   5) How does the DNS cache affect repeated queries? Provide an example from your capture.
   6) What differences did you observe between IPv4 (A) and IPv6 (AAAA) responses?
   7) Suppose a firewall blocked TCP port 53. Which of your queries would fail, and why?
   8) In large-scale deployments (e.g., CDNs), why is the ability to fall back to TCP important for DNS
      reliability?
Question 7. Change your system’s configuration to use a public DNS server (for example, Google’s
8.8.8.8 or Cloudflare’s 1.1.1.1) instead of the default DNS. Perform a lookup of www.cisco.com and
capture the traffic in Wireshark. Compare the results with those obtained when using your original DNS
server.
    1) What DNS server was originally configured on your host? Was it local (ISP/university) or public?
    2) After switching to 8.8.8.8 or 1.1.1.1, to what IP address are the DNS queries sent? Verify this in
       Wireshark.
    3) Compare the response time (latency) between the original DNS and the public DNS. Which was
       faster? What factors could explain this difference?
    4) Are the IP addresses returned for www.cisco.com identical in both cases? If not, explain why
       different DNS servers might return different results.
    5) Which transport protocol was used (UDP or TCP)? Did you observe any differences in behavior
       between the two servers?
    6) Do the responses include IPv4 (A), IPv6 (AAAA), or both? Are the results consistent across DNS
       servers?
    7) From a security perspective, what are the pros and cons of using a public DNS instead of the local
       DNS?
    8) How could a network administrator detect that a client is bypassing the institution’s DNS policies
       by using a public resolver?
    9) Suppose one DNS server returned only IPv6 addresses while the other returned IPv4. How would
       this affect client connectivity?
  10) Based on your results, which DNS would you recommend for a corporate environment: a public
       resolver or a local one? Justify your answer.
  CS-UTEC
