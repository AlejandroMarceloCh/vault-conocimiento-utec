---
curso: REDES
titulo: 07 - Semana 5/Sem5_LAB_3_UDP
slides: 3
fuente: 07 - Semana 5/Sem5_LAB_3_UDP.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-21




        LAB2 Transport Layer​
                                          UDP

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
  2026-04-21


                         LAB2_A_UDP_P3

 5. UDP Fragmentation and the MTU Limit
Use a Python script to generate a UDP datagram that exceeds the standard Ethernet
Maximum Transmission Unit (MTU) of 1500 bytes.
You must use a Python script to bypass high-level application limitations and generate a
specific payload size.
      Why?
      In future lab sessions, we will observe that testing MTU limits requires sending
      pings of variable sizes. In Linux, this is handled differently because the system
      often utilizes UDP packets for trace operations, whereas Windows defaults to ICMP
      messages (as seen in Lab 3). To remain consistent and ensure the generation of
      segmented UDP packets, we will be using a Python script.


 5.1. Instructions
   1.​ Open a text editor and create a file named cs4054UdpFragment.py.
   2.​ Input the following code, ensuring the TARGET_IP corresponds to a reachable host
      on the local network (e.g., a peer’s workstation).
             Note: Sending traffic to 127.0.0.1 (localhost) may bypass fragmentation due
        to the high MTU of the loopback interface. A physical network target is required.
        So try using your partner laptop as the Destination IP (just like the last
        experience).




                                      Code example.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-21

 3.​ Initiate a Wireshark capture on the active network interface.
 4.​ Apply the following display filter: ip.flags.mf == 1 || (ip.frag_offset > 0) || udp.
 5.​ Execute the script: python fragment_test.py.
 6.​ Stop the capture and locate the sequence of packets related to the 1200-byte
    transmission.
 7.​ Now change the payload size to 3000 bytes.
 8.​ Compare both UDP fragmented messages and answer.


5.2. Answer the following
 1.​ Present the IP addresses of both devices used for this experience. It would have
    been possible if you headed the UDP segments to your local hotspot gateway?
 2.​ Identify the total number of IP packets generated for this single UDP datagram.
 3.​ Examine the protocol stack for each fragment. Why does the User Datagram
    Protocol (Layer 4) header appear exclusively in the first fragment?
 4.​ Locate the Fragment Offset field in the IP header. The offset is measured in 8-byte
    blocks.
 5.​ Calculate the byte-equivalent of the offset for the second fragment.
 6.​ Compare the Identification (ID) field across all fragments. Explain the function of
    this field in the reassembly process at the destination host.
 7.​ Present a screenshot of the packet list showing the fragments and the
    "Reassembled IPv4" tab in the packet details pane.


                              Checkpoint 5
