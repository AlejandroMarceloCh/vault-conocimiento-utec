---
curso: REDES
titulo: 06 - Semana 4 _ LAB1B_DNS + LAB2_UDP/LAB2_UDP.pptx
slides: 9
fuente: 06 - Semana 4 _ LAB1B_DNS + LAB2_UDP/LAB2_UDP.pptx.pdf
---

  UDP
  (User Datagram
  Protocol)
  Computer Networks




CS4054 - 2026-2
PROF.: garias@utec.edu.pe
SRC: KUROSE – COMPUTER NETWORKS BOOK
   PETERSON AND DAVIE – COMPUTER NETWORKS BOOK
     Transport Layer
       It acts as the liaison between the Application layer and the lower
       network layers.




Computer Networks - CS4054 - 2026-2             Src. NetworkAcademy.io
                           garias@utec.edu.pe
     Transport Layer
       There are two primary ways to move data across the network:
        1. TCP: Connection-oriented. Focuses on reliability.
        2. UDP: Connectionless. Focuses on speed.




Computer Networks - CS4054 - 2026-2             Src. Cheap Ssl Security.
                           garias@utec.edu.pe
     TCP vs UDP
       Reliability vs. Speed



  Feature                        TCP                          UDP

  Connection                     Handshake required (3-way)   No handshake (Connectionless)

  Delivery                       Guaranteed & In-order        Best-effort (No guarantee)
  Error Recovery                 Retransmits lost packets     No retransmission

  Overhead                       Heavy header (20 bytes)      Lightweight header (8 bytes)



Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
     TCP vs UDP




Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
     UDP
       A simple, message-based protocol         that   sends   data   without
       establishing a formal connection.

      1. Stateless: The sender doesn't track if the data was received.
      2. Low Latency: Minimal delay because there is no "ﬂow control" or
         "congestion control."
      3. Header Simplicity: It only contains 4 ﬁelds:
        a. Source Port,
        b. Destination Port,
        c. Length, and
        d. Checksum.


Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
     UDP
                                     0     7 8      15 16    23 24    31
                                   +--------+--------+--------+--------+
                                   |     Source       |   Destination    |
                                   |      Port        |      Port        |
                                   +--------+--------+--------+--------+
                                   |                  |                  |
                                   |     Length       |    Checksum      |
                                   +--------+--------+--------+--------+
                                   |
                                   |           data octets ...
                                   +---------------- ...

                                                User Datagram Header Format
Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
     UDP
       This protocol provides a procedure for application programs to send
       messages     to other programs      with a minimum       of protocol
       mechanism. The protocol is transaction oriented, and delivery and
       duplicate protection are not guaranteed.




Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
     UDP
       Use Cases

      ● Live Streaming: Speed is more important than a perfectly
        reconstructed frame.
      ● Online Gaming: Reducing "lag" is the top priority.
      ● VoIP (Voice over IP): Minor packet loss is unnoticeable in human
        speech, but delays are frustrating.
      ● DNS (Domain Name System): Fast, short request/response cycles.




Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
