---
curso: REDES
titulo: 08 - Semana 6/Sem6_Ex2
slides: 5
fuente: 08 - Semana 6/Sem6_Ex2.pdf
---

cwilliams, garias@utec.edu.pe
CS4054: Networks — 26-1
April 29, 2026
                                         Ex 2: Transport Layer

Question 1. Considera distribuir un archivo de F = 20 Gbits a N peers. El server tiene un upload rate
de us = 30 Mbps, y cada peer tiene un download rate de di = 2 Mbps y un upload rate de u.
   Para N = 10, 100, y 1, 000 y u = 300 Kbps, 700 Kbps, y 2 Mbps, prepara una tabla que muestre
el minimum distribution time para cada una de las combinaciones de N y u, tanto para client-server
distribution como para P2P distribution.
Question 2. Considera distribuir un archivo de F bits a N peers usando una arquitectura client-server.
Asume un fluid model donde el server puede transmitir simultáneamente a múltiples peers, transmitiendo
a cada peer a diferentes rates, siempre que la tasa combinada no exceda us .
                  us                                                                              NF
    a. Supón que    ≤ dmin . Especifica un distribution scheme que tenga un distribution time de      .
                  N                                                                                us
                  us                                                                               F
    b. Supón que    ≥ dmin . Especifica un distribution scheme que tenga un distribution time de      .
                  N                                                                               dmin
    c. Concluye que el minimum distribution time está dado en general por
                                                   NF     F
                                                            
                                            max        ,       .
                                                    us dmin
Question 3. Considera distribuir un archivo de F bits a N peers usando una arquitectura P2P. Asume
un fluid model. Para simplificar, supón que dmin es muy grande, de modo que el peer download bandwidth
nunca es un bottleneck.
    a. Supón que
                                               us + u1 + · · · + uN
                                         us ≤                       .
                                                       N
                                                                                F
       Especifica un distribution scheme que tenga un distribution time igual a .
                                                                                us
   b. Supón que
                                               us + u1 + · · · + uN
                                         us ≥                       .
                                                       N
       Especifica un distribution scheme que tenga un distribution time igual a
                                                    NF
                                                                 .
                                            us + u1 + · · · + uN
    c. Concluye que el minimum distribution time viene dado en general por
                                                                      
                                                                      
                                             F           NF           
                                          max
                                              ,            N
                                                                       .
                                                                       
                                              us           X          
                                             
                                                     us +         ui   
                                                            i=1

Question 4. Consideremos nuestra motivación para corregir el protocolo rdt2.1. Muestra que el receiver
(Figura 1), cuando opera con el sender (Figura 2), puede llevar al sender y al receiver a entrar en un estado
de deadlock, donde cada uno espera un evento que nunca ocurrirá.




                                                      1
                                                                                                         2




                                        Figure 1. receiver rdt 2.1




                                        Figure 2. sender rdt 2.1


Question 5. UDP y TCP usan 1’s complement para sus checksums. Supongamos que tienes los siguientes
tres bytes de 8 bits: 01010011, 01100110, 01110100. ¿Cuál es el 1’s complement de la suma de estos bytes
de 8 bits? (Ten en cuenta que aunque UDP y TCP usan palabras de 16 bits en el cálculo del checksum,
para este problema se te pide considerar sumas de 8 bits). Muestra todo el procedimiento.
   ¿Por qué UDP toma el 1’s complement de la suma; es decir, por qué no usar simplemente la suma? Con
el esquema de 1’s complement, ¿cómo detecta el receptor los errores? ¿Es posible que un error de 1 bit no
sea detectado? ¿Y qué hay de un error de 2 bits?
                                                                                                      3

Question 6. Considera un canal que puede perder packets pero cuyo maximum delay es conocido.
Modifica el protocolo rdt2.1 para incluir un timeout en el sender y retransmit. Argumenta de manera
informal por qué tu protocolo puede comunicarse correctamente sobre este canal.
   Seccion de Ejercicios en Wireshark
Question 7. Perform and analyze DNS queries that force both UDP and TCP communication. Follow
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

Question 8. (UDP) Analyze DHCP traffic between your host and the DHCP server.
  1) Use the command ipconfig /release and then ipconfig /renew on Windows or dhclient -r;
     dhclient on Linux).
  2) Start a Wireshark capture and apply the dhcp filter (DHCP is identified this way).
  3) Observe the full DHCP exchange: Discover, Offer, Request, Acknowledgment.
  4) Stop the capture and analyze:
       • Identify the source and destination ports.
       • Examine the offered IP addresses and lease time.
       • Observe any retransmissions or duplicate requests.
 Answer.
  1) What are the ports used for DHCP in UDP communication?
  2) What IP address was finally assigned to your host, and what was the lease duration?
  3) How does the DHCP client identify itself? Which field in the packet shows this?
  4) Why is DHCP implemented over UDP instead of TCP?
  5) Which DHCP message type (Discover, Offer, Request, ACK) was the first one observed in your
     capture? Did the sequence follow the expected DORA process?
  6) Compare the size of DHCP messages in UDP. Do you see any fragmentation at the IP layer? Under
     what conditions could fragmentation occur?
  7) Since UDP does not guarantee delivery, how does DHCP handle lost Discover or Request messages?
     What evidence of retransmissions did you find in your capture?
                                                                                                          4

   8) What options were included in the DHCP Offer (e.g., subnet mask, default gateway, DNS servers)?
      Were they transmitted in a single UDP packet?
   9) How does the server’s UDP response (Offer or Ack) reach the client if the client does not yet have
      an IP address?
  10) Did you observe any negative responses or DHCP NACK messages? How were they delivered over
      UDP?

Question 9. (UDP) Explore UDP port usage with a custom Python client-server implementation.
   1) Open Wireshark and apply the filter udp.
   2) Create a simple UDP server in Python that listens on port 9999:
      # udp_server.py
      import socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.bind(("0.0.0.0", 9999))
      print("UDP server listening on port 9999...")
      while True:
          data, addr = sock.recvfrom(1024)
          print(f"Received from {addr}: {data.decode()}")
          sock.sendto(b"ACK", addr)
   3) In another terminal, run a UDP client that sends messages to the server:
      # udp_client.py
      import socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      for i in range(3):
          msg = f"Message {i+1}".encode()
          sock.sendto(msg, ("127.0.0.1", 9999))
          data, _ = sock.recvfrom(1024)
          print(f"Server reply: {data.decode()}")
   4) Start Wireshark before running the client and capture the packets.
   5) Stop the capture and analyze:
        • Observe the source and destination ports in the UDP headers.
        • Compare ephemeral client port numbers with the fixed server port.
        • Check whether ACK responses reuse the same ports.
  Answer.
   1) Which UDP port did the server use, and was it consistent across all packets?
   2) What ephemeral port was chosen by the client? Did it remain constant for all messages?
   3) How does the operating system decide which ephemeral port to assign?
   4) Were the server’s responses sent back to the same client port? Explain why this is necessary.
   5) What differences would you expect if multiple clients contacted the server simultaneously?
   6) What happens if you change the server port to a different number (e.g., 10001)? How is this reflected
      in the captured packets?
   7) What happens if you try to run two servers on the same UDP port? What error does Python return?
   8) What happens if you send a message to the server while it is turned off? What do you observe in
      Wireshark and in the client output?
   9) What is the maximum UDP message size you can send on your system? What happens if you try
      to send a message larger than 65,507 bytes (the theoretical UDP payload limit)?
  10) How does the behavior change if you run the client on a different machine within the same network
      instead of using 127.0.0.1?
  11) If the client sends messages to ports where no server is listening, how does the operating system
      respond? Did you observe any ICMP “Port Unreachable” messages?
          5

CS-UTEC
