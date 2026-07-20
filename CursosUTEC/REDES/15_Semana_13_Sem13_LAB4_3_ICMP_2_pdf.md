---
curso: REDES
titulo: 15 - Semana 13/Sem13_LAB4_3_ICMP_2
slides: 5
fuente: 15 - Semana 13/Sem13_LAB4_3_ICMP_2.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-16




                                       LAB3​
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
  2026-06-16

                            LAB4C - ICMP P2

 3. ICMP Error Messages via Simulated Network Failure

Analyze ICMP error messages triggered by specific network events such as unreachable
hosts or expired TTL (Time To Live) values, and understand how ICMP supports network
diagnostics and error reporting.


 3.1. Instructions

  3.1.1. Destination Unreachable Simulation

   1.​ Open the Command Prompt and Wireshark as in previous tasks.
   2.​ Begin packet capture in Wireshark.
   3.​ Attempt to ping a non-existent IP address or one that is blocked by a firewall (e.g., if
         your address is 10.23.10.90, then try ping 10.23.20.90. This depends on the class
         or your IP: A, B or C).
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

   1.​ What are the ICMP Type and Code values for the Destination Unreachable
         message?
   2.​ What are the ICMP Type and Code values for the Time Exceeded message?
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-16
  3.​ What fields are included in the ICMP payload?
  4.​ Does the ICMP error message include a portion of the original packet? If yes, which
       part and why?
  5.​ Compare the structure and function of the ICMP error messages with Echo
       Request/Reply used in Ping.
  6.​ Based on the TTL experiment, explain how TTL helps prevent infinite loops in
       networks.


                               Checkpoint 10

4. ICMP: Fragmentation & Path MTU Discovery (PMTUD)
The objective of this experiment is to {explore how routers and hosts use ICMP messages
to report fragmentation issues (Type 3, Code 4 — Fragmentation needed and DF set), and
to understand how Path MTU Discovery (PMTUD) works to avoid IP fragmentation.
You will also identify IP fragments in Wireshark and observe the behavior of the DF
(Don’t Fragment) flag.


Instructions
  1.​ Open:
          a.​ Windows: Command Prompt (CMD)
          b.​ Linux/macOS: Terminal
  2.​ Open Wireshark and start capturing packets on your active network interface.
  3.​ Start capture before running any ping commands.


4.1. Experiment A – Forcing Fragmentation Failure (DF flag set)
On Windows
Run:
                       ping -n 4 -f -l 2000 <destination>
  ●​ -n 4: send 4 packets
  ●​ -f: set DF (Don’t Fragment) flag
  ●​ -l 2000: payload size = 2000 bytes
  ●​ <destination>: You can select a domain name, or an IPV4 address.
On Linux/macOS
Run:
                         ping -M do -s 2000 <destination>
  ●​ -M do: set DF flag (“do not fragment”)
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-16
  ●​ -s 2000: payload size in bytes


You will likely see an error similar to:
                        “Packet needs to be fragmented but DF set.”
Stop capture after the command finishes.
      For this experiment, just hand screenshots of the results of the terminal/cmd.


4.1. Experiment B – Finding the Path MTU (smallest non-fragmented size)
First do a ping with fragmentation to a destination.
Windows command
                  ping -n 3 -l 3000 <destination>
Linux/macOS commands
                              ping -s 3000 <destination>


Now, let’s set the Don’t fragment flag, lowering or increasing the size until the largest
packet goes through without triggering the “fragmentation needed” message.


Windows commands
                       ping -n 3 -f -l 2000 <destination>
                       ping -n 3 -f -l 1800 <destination>
                       ping -n 3 -f -l 1600 <destination>


Linux/macOS commands
                         ping -M do -s 2000 <destination>
                         ping -M do -s 1800 <destination>
                         ping -M do -s 1600 <destination>



Useful Wireshark Filters

                    Purpose                                    Display Filter

             Show all ICMP packets                                 icmp

   Show ICMP “Destination Unreachable” only                   icmp.type == 3

        Show ICMP “Time Exceeded” only                        icmp.type == 11

          Show packets with DF flag set                       ip.flags.df == 1
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-16

           Show fragmented packets                           ìp.frag_offset > 0

       Show ICMP fragmentation needed                icmp.type == 3 && icmp.code == 4


Use Packet Details in Wireshark to inspect IP and ICMP headers.


Answer
These questions are for the successful ping results. The ones that do not meet the
maximum packet size for avoiding fragmentation, don’t show results in wireshark.


  1.​ What is the IP address of your host? What is the IP address of the destination?
  2.​ What are the Type and Code values of the ICMP packet reporting fragmentation
     needed? What textual description does Wireshark show for this message? (Attach
     packet screenshot)
  3.​ Show a packet with the DF flag set. How can you confirm that in Wireshark?
  4.​ Show one of the fragmented packets (from the normal ping). How many fragments
     are generated? Which fields indicate fragmentation (Fragment Offset, MF)?
  5.​ Does the ICMP message contain any MTU-related information (e.g., “Next-Hop
     MTU”)?
  6.​ Explain how the host adjusts its packet size after receiving this ICMP message
     (describe PMTUD in your own words).
  7.​ Compare RTT and behavior between the ping with DF flag (-f / -M do) and the
     normal ping.
  8.​ What differences do you observe in the number and size of packets?


                               Checkpoint 11
