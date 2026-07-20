---
curso: REDES
titulo: 14 - Semana 12 _ NAT + ICMP/Sem12_LAB4_3_ICMP_1
slides: 6
fuente: 14 - Semana 12 _ NAT + ICMP/Sem12_LAB4_3_ICMP_1.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-10




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
 2026-06-10

                       LAB4C - ICMP P1

1. ICMP and Ping

1.1. Instructions
  ●​ Open the Windows Command Prompt application.
  ●​ Start up the Wireshark packet sniffer, and begin Wireshark packet capture.
  ●​ The ping command is in c:\windows\system32, so type either
                               “ping –n 10 hostname” or ​
                    “c:\windows\system32\ping –n 10 hostname”
 in the MS-DOS command line (without quotation marks), where hostname is a host on
another continent. If you’re outside of Asia, you may want to enter www.ust.hk for the
Web server at Hong Kong University of Science and Technology. The argument “-n 10”
indicates that 10 ping messages should be sent.
  ●​ At the end of the experiment, your Command Prompt Window should look
     something like the screenshot shown in figure 1. In this example, the source ping
     program is in Massachusetts and the destination Ping program is in Hong Kong.
     From this window we see that the source ping program sent 10 query packets and
     received 10 responses. Note also that for each response, the source calculates the
     round-trip time (RTT), which for the 10 packets is on average 375 msec.




                    Figure 1. CMD with ping test to Hong Kong server.
  ●​ When the Ping program terminates, stop the packet capture in Wireshark.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-10
  ●​ Filter the captured packets by entering “icmp” into the filter display window.


1.2. Hand in:
 You should hand in a screenshot of the Command Prompt window. Whenever possible,
when answering a question below, you should hand in a printout of the packet(s) within
the trace that you used to answer the question asked. Annotate the printout to explain
your answer. To print a packet, use File->Print, choose Selected packet only, choose
Packet summary line, and select the minimum amount of packet detail that you need to
answer the question.


 1.2.1. Answer:
  1.​ What is the IP address of your host? What is the IP address of the destination host?
  2.​ Why is it that an ICMP packet does not have source and destination port numbers?
  3.​ What is the protocol number shown into the IP datagram of the first packet.
  4.​ Examine one of the ping request packets sent by your host. What are the ICMP type
     and code numbers? What other fields does this ICMP packet have? How many
     bytes are the checksum, sequence number and identifier fields?
  5.​ Examine the corresponding ping reply packet. What are the ICMP type and code
     numbers? What other fields does this ICMP packet have? How many bytes are the
     checksum, sequence number and identifier fields?


                                Checkpoint 8


2. ICMP and Traceroute
 You may recall that the Traceroute program can be used to figure out the path a packet
takes from source to destination.


2.1. Instructions:​       ​         ​    ​
  ●​ Open the CMD.
  ●​ Start up the Wireshark packet sniffer, and begin Wireshark packet ​ capture.
  ●​ The tracert command is in c:\windows\system32, so type either “tracert
     hostname” or “c:\windows\system32\tracert ​ hostname”          in    the     MS-DOS
     command line (without quotation ​        marks), where hostname is a host on
     another continent. If you’re outside of Europe, you may want to enter www.inria.fr
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-10
     for the Web server at INRIA, a computer science research institute in France. Then
     run the Traceroute program by typing return.
 At the end of the experiment, your Command Prompt Window should look something
like shown in figure 2. Here, the client Traceroute program is in Massachusetts and the
target destination is in France. From this figure we see that for each TTL value, the source
program sends three probe packets. Traceroute displays the RTTs for each of the probe
packets, as well as the IP address (and possibly the name) of the router that returned the
ICMP TTL-exceeded message.




   Figure 2. Command Prompt window displays the results of the Traceroute program.



2.2. Answer the Following:
  ●​ For this part of the lab, you should hand in:
         ○​ a screenshot of the Command Prompt window.
         ○​ A printout of the packet(s) within the trace that you used to answer the
            question asked.
  ●​ What is the IP address of your host?
  ●​ What is the IP address of the target destination host?
  ●​ If ICMP sent UDP packets instead (as in Unix/Linux), would the IP protocol number
     still be 01 for the probe packets? If not, what would it be?
  ●​ Examine the ICMP echo packet in your screenshot. Is this different from the ICMP
     ping query packets in the first half of this lab? If yes, how so?
  ●​ Examine the ICMP error packet in your screenshot. It has more fields than the ICMP
     echo packet. What is included in those fields?
 {garias,cwilliams}@utec.edu.pe
 CS4055: Networks and communications
  2026-06-10
   ●​ Examine the last three ICMP packets received by the source host. How are these
         packets different from the ICMP error packets? Why are they different?
                                    Checkpoint 9


 3. ICMP Error Messages via Simulated Network Failure

Analyze ICMP error messages triggered by specific network events such as unreachable
hosts or expired TTL (Time To Live) values, and understand how ICMP supports network
diagnostics and error reporting.


 3.1. Instructions

  3.1.1. Destination Unreachable Simulation

   1.​ Open the Command Prompt and Wireshark as in previous tasks.
   2.​ Begin packet capture in Wireshark.
   3.​ Attempt to ping a non-existent IP address or one that is blocked by a firewall (e.g.,
         ping 192.0.2.1 — an IP reserved for documentation and testing).
   4.​ Observe the response on the Command Prompt and capture the corresponding
         ICMP error messages (typically Type 3: Destination Unreachable).
   5.​ Stop packet capture.


  3.1.2. TTL Expired Simulation (Time Exceeded)
  In CMD, type:
                                      ping [destination] -i 1
   1.​
            ○​ Replace [destination] with a reachable host (ip or web).
            ○​ -i 1 sets TTL to 1, so the packet expires quickly.
   2.​ Observe the ICMP Time Exceeded message (Type 11) in Wireshark.
   3.​ Capture and analyze the packet content.


 3.2. Answer the following

Provide annotated screenshots and packet summaries for each:
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-10
 1.​ What are the ICMP Type and Code values for the Destination Unreachable
    message?
 2.​ What are the ICMP Type and Code values for the Time Exceeded message?
 3.​ What fields are included in the ICMP payload?
 4.​ Does the ICMP error message include a portion of the original packet? If yes, which
    part and why?
 5.​ Compare the structure and function of the ICMP error messages with Echo
    Request/Reply used in Ping.
 6.​ Based on the TTL experiment, explain how TTL helps prevent infinite loops in
    networks.


                             Checkpoint 10
