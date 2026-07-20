---
curso: REDES
titulo: 06 - Semana 4 _ LAB1B_DNS + LAB2_UDP/LAB2_2_UDPpy
slides: 4
fuente: 06 - Semana 4 _ LAB1B_DNS + LAB2_UDP/LAB2_2_UDPpy.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-15




        LAB2 Transport Layer​
                                          UDP​
                P2: P2P UDP CoMM

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
 2026-04-15


                       LAB2_A_UDP_P2

3. Python UDP Implementation (Loopback)
 For this assignment, a python IDE will be needed.
 ●​ Load on a python file the following instructions. This will be the receiver that should
     be named after ‘udp_receiver.py’




 ●​ Load on a python file the following instructions. This will be the receiver that should
     be named after ‘udp_sender.py’
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-15

  ●​ Now, let’s do a UDP packages loopback capture.
  ●​ Run wireshark and select for capture a loop device (e.g.: localhost, lo0, loopback0)
     (usually has the IP 127.0.0.1)




  ●​ Now start the capture
  ●​ Run the receiver python code (‘udp_receiver.py’).
  ●​ Now on a terminal or a different IDE, run the sender python code (‘udp_sender.py’).
  ●​ Stop the capture.


3.1. Answer the following
  1.​ Does the received header transmitted the data defined in our python program?
  2.​ What’s the UDP IP on the code.
  3.​ Analyze the UDP package and explain the UDP datagram.
  4.​ Answer, what would you need to do to send the UDP packet from one computer to
     a different one? Is any material required? How about the IP configuration?
  5.​ Compare the UDP checksum field in at least two captured packets. Was the
     checksum calculated and validated correctly? Explain how you verified this.
  6.​ Examine the Time to Live (TTL) field in the IP header of the UDP packet. Why is the
     TTL value what it is, and how would it change in a multi-hop real network scenario?
  7.​ Explore how Wireshark differentiates between application-layer protocols when
     using UDP (e.g., DNS, DHCP). Is your custom message interpreted as a known
     protocol? Why or why not?
  8.​ Change the destination IP in the sender script to a non-routable or invalid IP (e.g.,
     192.0.2.1) and rerun the test. What happens in the capture, and why is there a
     difference?

                              Checkpoint 3
4. Python UDP Implementation (P2P)
     Establish basic User Datagram Protocol (UDP) communication between two
computers connected to the same network using Python scripts—one acting as a sender
and the other as a receiver (No code help this time!)
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-15


4.1. Requirements
 1.​ Access to the same local area network (LAN) via Wi-Fi or Ethernet (not the
    University’s WiFi).
 2.​ Firewall permissions enabled for UDP traffic (maybe needed).
 3.​ Establish a simple communication between two laptops using python and sending
    and receiving simple UDP packets.
 4.​ Capture the traffic using wireshark.
 5.​ You can use any source as reference.


4.2. For the checkpoint
 1.​ Capture the traffic using wireshark.
 2.​ Show the IP addresses of both laptops used.
 3.​ Provide evidence of successful message transmission.
 4.​ Describe the message format and how it was handled on the receiver side.
 5.​ Suggest one scenario where UDP would be preferred over TCP and justify.
 6.​ Change the message content and observe how the packet length changes in
    Wireshark.
 7.​ Change the message content specifically to an absurd size (like 12 000 bytes) and
    see the behaviour of the messages. Is it possible to send messages with that
    payload size?


                            Checkpoint 4

4.3. Notes
 ●​ UDP is connectionless and does not guarantee message delivery. You may need to
    add retry mechanisms or timeouts in practical scenarios.
 ●​ Ensure you are not using ports already in use by the system or other services (e.g.,
    53, 67, 123).


4.4. References
 ●​ Socket Programming in Python (Guide). https://realpython.com/python-sockets/
