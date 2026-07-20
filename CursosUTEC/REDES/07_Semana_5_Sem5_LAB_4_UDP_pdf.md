---
curso: REDES
titulo: 07 - Semana 5/Sem5_LAB_4_UDP
slides: 5
fuente: 07 - Semana 5/Sem5_LAB_4_UDP.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-22




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
 2026-04-22


                         LAB2_A_UDP_P4

6. Error Handling with NetCat
Objective: To observe how the network layer (ICMP) must "speak" for the transport layer
(UDP) when things go wrong, and to analyze the minimal overhead of the UDP header.


6.1. Instructions
  1.​ Install the latest version of Nmap (https://nmap.org/download)
  2.​ Wireshark: Start capture with filter udp || icmp.
  3.​ Try opening the CMD or Terminal and run:


     6.1.1. For Windows (Command Prompt / CMD)

         ●​ Open CMD.
         ●​ Run the following command:
                                   ncat -u -v [Target_IP] 1234
         ●​ Once the prompt appears, type a message and press Enter.


     6.1.2. For Linux (Terminal)

         ●​ Open your Terminal.
         ●​ Run the following command (you may need sudo depending on your
            environment, though not usually for high-numbered ports):
                                   ncat -u -v [Target_IP] 1234
         ●​ Type a message and press Enter.
         ●​ Observation: Even though Ncat says "Connected" (or doesn't show an error
            immediately), look at Wireshark.




                                       Capture Example


6.2. Answer
  1.​ Based on your Wireshark capture, does the sender wait for any synchronization or
     confirmation from the target host before transmitting the payload?
 {garias,cwilliams}@utec.edu.pe
 CS4055: Networks and communications
  2026-04-22

   2.​ When you ran the Ncat command, the terminal displayed a "Connected" status or a
       blinking cursor waiting for input. Based on your Wireshark capture, did any network
       traffic actually occur before you typed the message and pressed Enter? Explain
       why Ncat behaves this way with UDP compared to TCP.
   3.​ Locate the UDP header in the packet details pane and calculate its total size in
       bytes; how does this fixed length contribute to lower processing latency compared
       to the variable-length headers found in TCP?
   4.​ (For the Report) Given that a standard TCP header is at least 20 bytes, analyze
       why the 8-byte simplicity of the UDP header is a critical advantage for real-time
       applications such as VoIP or online gaming where "jitter" is a concern.
   5.​ Examine the ICMP "Destination Unreachable" message and identify the specific
       Type and Code numbers; what do these specific values communicate to the source
       operating system about the nature of the failure?
   6.​ Within the ICMP packet, locate the "Encapsulated" data section; why is it
       technically necessary for the network layer to include the original IP header and
       the first 8 bytes of the failed UDP datagram in this error report?
   7.​ Considering that UDP provides no built-in flow control or error recovery, does the
       receipt of an ICMP error message make this specific communication "reliable," or
       does it remain "best-effort"? Hint: Justify your answer based on the lack of
       retransmission mechanisms.
                                    Checkpoint 6

 7. The Echo Test

Objective: To prove that UDP does not maintain a "state" or session, and to observe the
lack of flow control.


 7.1. Instructions
 For this, you will need two terminal windows (or two computers).
   1.​ Setup the Listener (Server): In Terminal A, run:
              ncat -u -l -p 4444 (This tells Ncat to Listen on UDP port 4444).
   2.​ Setup the Sender (Client):
                        In Terminal B, run: ncat -u -v [Your_Local_IP] 4444
   3.​ Send several messages from Terminal B to Terminal A. Then, try sending a message
       from Terminal A back to Terminal B.
   4.​ Wireshark Filter: udp.port == 4444
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-22

 5.​ To make these observations even clearer, run another test using Ncat in TCP mode
    (simply remove the -u from both commands as these commands run default on tcp)
    and look for the sea of ACK and SEQ numbers that UDP ignores.


7.2. Answer the following
 1.​ Look at the very first packet in your Wireshark capture. Did any network traffic
    occur between Terminal A and Terminal B before you sent your first message?
    Contrast this with how TCP begins a session.
 2.​ Based on the lack of a "Three-Way Handshake," what can you conclude about the
    "Connection Latency" of UDP? Why would this be preferred for a DNS query or a
    real-time voice packet?
 3.​ Does the Sender (Terminal B) show any evidence of maintaining a "session state"?
    If you wait 5 minutes between messages, does the protocol require any
    "keep-alive" packets to maintain the connection?
 4.​ When you sent three separate words as three separate entries, did Wireshark show
    one continuous stream of data or three distinct, independent datagrams? Explain
    the concept of "Message Orientation" in UDP.
 5.​ Inspect a packet containing a single short word. How much of the total packet size
    is actual data versus protocol overhead (headers)? How does this compare to your
    expectations of a TCP packet for the same word?
 6.​ Unlike TCP, which confirms receipt of every segment, does Terminal A send any
    Transport Layer acknowledgment (ACK) back to Terminal B after receiving a
    message? What is the impact of this on network congestion?
 7.​ When you close the listener in Terminal A (Ctrl+C), does Wireshark capture any
    "Goodbye" or "Connection Close" packets (like a FIN or RST)? How does Terminal B
    know—or not know—that the listener has stopped?
 8.​ After stopping the listener, you continued to send data from Terminal B. Did the
    Ncat interface on the sender's side provide any error or indication that the packets
    were now being dropped?
 9.​ In the scenario where Terminal A is offline, and assuming no ICMP "Port
    Unreachable" is returned by the OS, does the UDP protocol have any internal
    mechanism to inform the sender that the data was lost?
 10.​If UDP is inherently "unreliable" and "stateless" as demonstrated in this lab, but an
    application still needs to ensure data arrives in the correct order, where must that
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-22

    logic be programmed: in the Network Protocol or the Application Layer? Justify
    your answer.

                          Checkpoint 7
