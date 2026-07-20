---
curso: REDES
titulo: 13 - Semana 11/Sem11_LAB4_IP_P1
slides: 5
fuente: 13 - Semana 11/Sem11_LAB4_IP_P1.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2025-10-22




                                       LAB4​
                    NETWORK Layer

 The present evaluation will be received only if the checkpoints of all the questions in
 the LABORATORY SESSION have been completed with the course teacher.
 For the checkpoints presentation, have a doc or text file where you present the answer
 to the questions (including screenshots if necessary). Do not forget to save your
 tracefile.
  I.​   The submission must consist of:
           A.​ Introduction (include introductory paragraph):
           B.​ Theoretical Framework (definitions with references).
           C.​ State of the Art (research papers, articles, theses, pages with references).
           D.​ Development of the experience (including discussion and correct figure
              formatting)
           E.​ Conclusions and recommendations (at least one for each experience
              carried out).
           F.​ References (IEEE format)
 II.​   The submission must be presented in LaTeX or Docs format (pdf file).
III.​   Upload only the PDF of the report to Canvas, use a link to the repository, include
        step-by-step photos of each experience and answer checkpoints where relevant,
        plus codes if they have been developed.
IV.​    Only one member of the group will upload the report.
 V.​    Do not forget to list the names of all members.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2025-10-22


                            LAB4A - IP P1

 1. IPv6
 In this final section we’ll take a quick look at the IPv6 datagram using Wireshark. Your
 own computer or your ISP may not be configured for IPv6, let’s look at a trace of already
 captured packets that contain some IPv6 packets. To generate this trace, our web
 browser opened the youtube.com homepage.            Youtube (and Google) provide fairly
 widespread support for IPv6. Your Wireshark display should look similar to Figure 4.




                          Figure 4: Wireshark screenshot

 Let’s start by taking a closer look at the DNS request (contained in an IPv6 datagram) to
 an IPv6 DNS server for the IPv6 address of youtube.com. The DNS AAAA request type is
 used to resolve names to IPv6 IP addresses.


 1.1. Answer the following questions
   1.​ What is the IPv6 address of the computer making the DNS AAAA request?
   2.​ What is the IPv6 destination address for this datagram? Give this IPv6 address in
      the exact same form as displayed in the Wireshark window.
   3.​ What is the value of the flow label for this datagram?
   4.​ How much payload data is carried in this datagram?
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2025-10-22

   5.​ What is the upper layer protocol to which this datagram’s payload will be delivered
         at the destination?

Lastly, find the IPv6 DNS response to the IPv6 DNS AAAA request. This DNS response
contains IPv6 addresses for youtube.com.

   6.​ How many IPv6 addresses are returned in the response to this AAAA request?
   7.​ What is the first of the IPv6 addresses returned by the DNS for youtube.com (in the
         ip-wireshark-trace2-1.pcapng trace file, this is also the address that is numerically
         the smallest)? Give this IPv6 address in the exact same shorthand form as
         displayed in the Wireshark window.

 Note: Recall that an IPv6 address is shown as 8 sets of 4 hexadecimal digits, with each
 set separated by colons, and with leading zeros omitted. If an IPv6 address has two
 colons in a row (‘::’), this is shorthand meaning that all of the intervening bytes between
 the two colons are zero.
         Thus,    for         example,     fe80::1085:6434:583:e79               is   shorthand        for
 fe80:0000:0000:0000:1085:6434:0583:0e79. Make sure you understand this
 example.

                                         Checkpoint 1
 2. IPv4 address classes and subnet mask

This section will analyze IPv4 address classes, the use of subnet masks, network
addresses, and broadcast addresses. It will also include a practical exercise in observing IP
headers using Wireshark.


 2.1. IPv4 address classes
 The IPv4 address space consists of 32 bits, divided into four octets. The first bits
 determine the network class:


                                         Network
 Class        First octet range                    Host bits   Private address           Typical use
                                          bits


  A                0 – 127                 8          24         10.0.0.0/8           Very large networks


                                                                                        Medium-sized
  B               128 – 191                16         16        172.16.0.0/12
                                                                                           networks
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2025-10-22


  C            192 – 223            24            8          192.168.0.0/16   Small networks


  D           224 – 239              —            —                  —          Multicast


  E           240 – 255              —            —                  —        Experimental


To recognize whether an IPv4 address is a specific class, simply look at the first number of
the IP address:

   ●​ If it is between 0 and 127, it is class A (routable IPv4).
   ●​ If it is between 128 and 191, it is class B (routable IPv4).
   ●​ If it is between 192 and 223, it is class C (routable IPv4).
   ●​ If it is between 224 and 239, it is class D.
   ●​ If it is between 240 and 255, it is class E.




 2.2. Subnet mask
The subnet mask defines which part of the address belongs to the network and which part
belongs to the host.
   ●​ It is expressed in CIDR (Classless Inter-Domain Routing) notation, for example:
   ●​ /8 equals 255.0.0.0
   ●​ /16 is equivalent to 255.255.0.0
   ●​ /24 is equivalent to 255.255.255.0
Example:
   ●​ IP address: 192.168.1.25/24
   ●​ Mask: 255.255.255.0
   ●​ Network address: 192.168.1.0
   ●​ Broadcast address: 192.168.1.255
   ●​ Range of valid hosts: 192.168.1.1 – 192.168.1.254
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2025-10-22




 3. Practical Exercise with Wireshark
 Identify IPv4 address classes and subnet characteristics in real captured traffic.
   1.​ Open Wireshark and start a capture on your main network interface (Ethernet or
      Wi-Fi).
   2.​ In the filter bar, type: ip to display only IPv4 packets.
   3.​ Select any packet using the TCP or ICMP protocol.
   4.​ Expand the Internet Protocol Version 4 section and inspect the following fields:
          ●​ Source Address
          ●​ Destination Address
          ●​ Header Length
          ●​ Flags and Fragment Offset


 3.1. Answer
 Theoretical
   1)​ For each of the following IP addresses, determine: its class, its network address, and
      its broadcast address.
          a)​ 10.15.32.200
          b)​ 172.20.45.7
          c)​ 192.168.10.25
 Wireshark
   2)​ To which class do the source and destination IP addresses belong?
   3)​ What subnet mask could be inferred for each one?
   4)​ Which of them might be a private address?
   5)​ What is the TTL value, and what could it suggest about the device or operating
      system that sent the packet?

                               Checkpoint 2
