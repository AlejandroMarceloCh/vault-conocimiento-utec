---
curso: REDES
titulo: 12 - Semana 10/Sem10_LAB3_RDT
slides: 7
fuente: 12 - Semana 10/Sem10_LAB3_RDT.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-05-26




        LAB3 Transport Layer​
                                  RDT 2.0

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
 2026-05-26


                             LAB3_Part2
Note. If wireshark is not capturing traffic in Linux visit the following link.
RDT (Reliable Data Transfer) is a communication protocol designed to ensure data
transmission over channels that may introduce errors, such as bit corruptions. It's part of
a series of protocols aimed at providing reliable data transfer, addressing issues like
packet corruption and ensuring error detection and recovery.
RDT 2.0 handles errors using checksums, and employs an acknowledgment (ACK) and
negative acknowledgment (NAK) system. If the receiver detects a corrupted packet, it
sends a NAK, prompting the sender to retransmit the packet. The sender waits for either
an ACK or NAK before proceeding, making it a stop-and-wait protocol. However, one
major limitation of RDT 2.0 is its inability to handle cases where the acknowledgment
itself is corrupted, which can lead to unnecessary retransmissions or missed packets.




                         Figure 1. RDT 2.0 Finite State Machine.
  ●​ Packet Corruption: Simulate a random chance of packet corruption.
  ●​ ACK/NAK: The receiver will respond with either an ACK if the packet is received
     correctly or a NAK if the packet is corrupted or out of order.
  ●​ Stop-and-Wait Protocol: The sender waits for an ACK or NAK before sending the
     next packet.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-05-26


1. Objective.
In this lab, you will implement the RDT 2.0 (Reliable Data Transfer) protocol using two
separate Python programs for the Sender and Receiver. You will simulate a
communication system that sends packets over a potentially unreliable channel where
packets may be corrupted, and the receiver must respond with either an
acknowledgment (ACK) or a negative acknowledgment (NAK).

2. Design the Sender Program

2.1. Initialize the sender:
        -​ Design a Sender class that will handle packet creation, sending packets, and
           receiving ACKs or NAKs from the receiver.
        -​ Choose a unique identifier for each packet (e.g., a sequence number) and
           ensure the packet has this information.


2.2. Simulate sending packets:
        -​ Write a function to send a packet over the network using UDP (User
           Datagram Protocol).
        -​ After sending each packet, wait for an acknowledgment from the receiver.
        -​ If no response is received after a set timeout period, simulate a timeout by
           resending the same packet.


2.3. Handle ACKs and NAKs:
        -​ Wait for an ACK or NAK message from the receiver.
        -​ If an ACK is received, move to the next packet. If a NAK is received, resend
           the current packet.


2.4. Simulate the stop-and-wait mechanism:
        -​ Make sure the sender only sends one packet at a time and waits for a
           response (ACK/NAK) before sending the next one.


2.5. Add corruption simulation (optional but recommended):
        -​ Include a small chance that the sender’s packet could be corrupted (e.g., by
           manipulating the packet data).
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-05-26

        -​ This corruption will be detected by the receiver, and a NAK will be sent.


# Simulate packet corruption
def is_corrupted():
return random.random() < 0.1                       #    10%     chance       of
corruption




3. Design the Receiver Program

3.1. Initialize the receiver:
        -​ Design a Receiver class that will receive packets from the sender.
        -​ The receiver should be able to listen on a specific port and decode any
           incoming packet.


3.2. Simulate packet corruption detection:
        -​ Write logic to determine if the packet received from the sender is corrupted
           (use a random probability function to simulate corruption).
        -​ If a packet is corrupted, respond with a NAK (Negative Acknowledgment) to
           request a retransmission of the current packet.


3.3. Send ACKs or NAKs:
        -​ If the received packet is valid and in order, send an ACK (Acknowledgment)
           back to the sender.
        -​ If the packet is corrupted or out of order, send a NAK.


3.4. Manage packet sequence:
        -​ Ensure that the receiver expects packets to arrive in the correct sequence. If
           a packet is received out of order, send a NAK to the sender.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-05-26


4. Establish Communication Between Sender and Receiver

4.1. Simulate the network connection:
       -​ Use Python’s socket library to create a UDP connection between the sender
          and receiver. The sender will send packets to the receiver over a designated
          IP address and port.


4.2. Run the programs on the same machine:
       -​ First, start the Receiver program, which will wait for incoming packets.
       -​ Then, run the Sender program to begin sending packets to the receiver.
       -​ Use localhost (127.0.0.1) as the IP address for communication and select any
          available port (e.g., 12345).


4.3. Test communication:
       -​ The sender will start sending packets and expect responses from the
          receiver.
       -​ The receiver will receive packets, process them, and send back ACK or NAK
          messages depending on the correctness of the packets.

5. Implement and Simulate Packet Loss or Corruption

5.1. Introduce corruption simulation:
       -​ Add a random probability to simulate packet corruption. This can be done by
          modifying packet data before sending or by adding random errors to the
          packet.


5.2. Handle timeouts on the sender:
       -​ If the sender does not receive an ACK or NAK within a given time, implement
          a timeout that triggers the retransmission of the current packet.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-05-26


6. Testing and Validation

6.1. Test the protocol with multiple packet transmissions:
         -​ Simulate sending multiple packets (e.g., 10 packets) from the sender to the
              receiver.
         -​ Verify that the sender handles ACKs and NAKs correctly and resends
              packets when needed.


6.2. Introduce random corruption and verify the response:
         -​ Verify that when a packet is corrupted, the receiver sends a NAK, and the
              sender resends the corrupted packet until an ACK is received.


6.3. Measure performance:
         -​ Test different timeout durations and packet corruption rates to see how they
              affect the overall communication process.

7. Final Deliverables:
  -​ Code Implementation: Submit both the rdt_sender() and rdt_receiver() Python
     files.
  -​ Output Logs: Provide output logs showing successful communication between
     sender and receiver, as well as handling of timeouts and retransmissions.
  -​ Wireshark: Show the packets sended in the simulation by capturing the loopback
     traffic using wireshark.

                                Checkpoint
8. Example:
What you should present in the python code simulation.


8.1. Sender:

      Sender: Sending Packet 0
      Sender: Received ACK 0
      Sender: ACK received for Packet 0
      Sender: Sending Packet 1
      Sender: Timeout, resending packet 1.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-05-26


     Sender: Received NAK 1
     Sender: Resending Packet 1
     Sender: Received ACK 1
     Sender: ACK received for Packet 1


8.2. Receiver

     Receiver: Successfully received Packet 0. Sending ACK.
     Receiver: Packet 1 is corrupted. Sending NAK.
     Receiver: Successfully received Packet 1. Sending ACK.
