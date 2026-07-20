---
curso: REDES
titulo: 03 - Semana 1 _ Introducción + LAB1A_HTTP/LAB0_Wireshark.pptx
slides: 17
fuente: 03 - Semana 1 _ Introducción + LAB1A_HTTP/LAB0_Wireshark.pptx.pdf
---

  Wireshark
  Computer Networks




CS4054 - 2026-2
PROF.: garias@utec.edu.pe
SRC: KUROSE – COMPUTER NETWORKS BOOK
   PETERSON AND DAVIE – COMPUTER NETWORKS BOOK
      Executive Summary
  2

      • Motivation: Computer network abstraction allows to have a large
        implementation such as the Internet
      • Problem: We need to observe the details in data transmission over the
        network.
      • Overview:
       -Introduce a sniffer tool: Wireshark.
       -Analyze the behavior of web browsing.
       -Evaluate the packet contents under the HTTP protocol.
      • Conclusion: We can begin with network experimentation and packet
        analysis.
Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
      Outline
  3

      Introduction

      Installation

      Getting started

      Test

      Conclusions


Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
     Our course
 4
       A common Mistake: The usual “Networks course”: Primarily
       for         learning                network      design,       conﬁguration,   and
       troubleshooting of Cisco devices.




Computer Networks - CS4054 - 2026-2             Cisco Packet Tracer
                           garias@utec.edu.pe
     Our course
 4
       Capture, inspect, and analyze real network trafﬁc to understand
       network protocols (e.g., TCP, UDP, ICMP, HTTP, DNS) at a deep level,
       troubleshooting network issues, and monitoring security threats.




Computer Networks - CS4054 - Source:
                             2026-2     BMC
                           garias@utec.edu.pe
     What is wireshark used for?
6


       Wireshark is commonly used for:
      ● Network troubleshooting
      ● Security analysis
      ● Protocol development
      ● Educational purposes (learning how networks function)
      ● Packet-level network analysis


Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
      Wireshark
  5

      •   Wireshark is a packet sniffer.
          •Popular: ~1 million downloads monthly.

                                                                                User level: from hello world to
                                                                                spotify and beyond




                                                                                OS kernel: linux, win, mac, etc.




                                 On kernel, because:
                                 • Library functions associated to drivers.
                                 • Requires direct control on the link layer.

Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
      Wireshark
  5

      •   Wireshark is a packet sniffer.
          •Popular: ~1 million downloads monthly.




Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe   Source: ByteByteGo
     What is wireshark used for?
      ● Example: NAT Protocol




                                                Source: Xataka

Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
      Outline
  5

      Introduction

      Installation

      Getting started

      Test

      Conclusions


Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
      Get Wireshark
  6

  http://www.wireshark.org/download.html

  Available for: Windows, Mac, Linux

  Don’t forget to restart your computer.


      Install in Ubuntu:
      1.sudo apt install wireshark
      2.Select YES (for root privileges on the pop up window) or (manually):
          sudo dpkq-reconfigure wireshark-common
           •


          sudo usermod -aG wireshark <yourusername>
           •




Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
      Outline
  7

      Introduction

      Installation

      Getting started

      Test

      Conclusions


Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
      First steps                                       1
  8
                                                3
      1. Execute Wireshark



      2.       Select a network
               interface:                           2
           •   Ethernet (eth, en) or
           •   Wireless (w, en)

      3. Start capturing!




Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
    Change
  9
    interface




Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
     Expected output
10
       •   Packet: unit in network layer
       •   Frame: unit in data link layer.




Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
     Outline
11

     Introduction

     Installation

     Getting started

     Test

     Conclusions


Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe
     Test
   12
   Start the capture.

   Open a browser and
   access:
      https://www.cisco.com/


   Stop the capture


   Filter http messages.

Computer Networks - CS4054 - 2026-2
                           garias@utec.edu.pe

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
