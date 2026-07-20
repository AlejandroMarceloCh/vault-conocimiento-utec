---
curso: REDES
titulo: 12 - Semana 10/Sem10_Ex4_TCP
slides: 3
fuente: 12 - Semana 10/Sem10_Ex4_TCP.pdf
---

cwilliams, garias@utec.edu.pe
CS4054: NetwoRks
May 27, 2026
                                     Ex 4: Transport Layer TCP


Question 1. AIMD - AIAD: Show that the TCP AIMD (Additive Increase, Multiplicative Decrease)
algorithm guarantees a fair allocation. Provide a diagram to illustrate this and use example values to
demonstrate step-by-step convergence. Suppose that, instead of multiplicative decrease, TCP reduced the
window size by a constant amount. Would the resulting AIAD (Additive Increase, Additive Decrease)
algorithm converge toward an equal share allocation? Justify your answer using a diagram.
Question 2. GBN, SR, and TCP (no delayed ACK): Assume that the timeout values for the three
protocols are long enough so that five consecutive data segments and their corresponding ACKs can be
received (if they are not lost in the channel) by the receiving host (Host B) and the sending host (Host
A), respectively.
  Suppose Host A sends five data segments to Host B, and the second segment (sent from A) is lost. In
the end, all five data segments are correctly received by Host B.
  a. How many total segments has Host A sent, and how many total ACKs has Host B sent? What are
their sequence numbers? Answer this question for the three protocols.
  b. If the timeout values for the three protocols are much greater than 5 RTT, which of the three protocols
successfully delivers the five data segments in the shortest time interval?
Question 3. NAKs protocol: Consider a reliable data transfer protocol that uses only negative ac-
knowledgments (NAKs). Suppose the sender sends data only infrequently. Would a NAK-only protocol
be preferable to a protocol that uses ACKs? Why? Now suppose the sender has a large amount of data
to send and the end-to-end connection experiences few losses. In this second case, would a NAK-only
protocol be preferable to a protocol that uses ACKs? Why?
                                          Wireshark Exercises

Question 4. TCP Connection Analysis with Wireshark. Capture and analyze a real TCP connec-
tion established between your computer and a web server. Use Wireshark and a web browser to observe
the process of connection establishment, data transfer, and connection termination. Instructions.
    1) Open Wireshark and select the active network interface.
    2) Apply a capture filter for TCP traffic only (e.g., tcp.port == 80 or tcp.port == 443).
    3) Visit a simple webpage such as http://example.com or https://httpbin.org/get.
    4) Stop the capture once the page has fully loaded.
    5) Analyze the packets corresponding to the TCP connection between your host and the server.
   Answer.
    1) What were the IP addresses of the client and the server?
    2) Which port did the client use, and which port did the server use?
    3) Which packets correspond to the three-way handshake?
    4) What indicators confirm that the TCP channel was successfully established?
    5) How many data segments were transmitted before the connection closed?
    6) Which packets indicate the connection termination (FIN and ACK)?
    7) What was the receiver window size (Window Size) observed in the capture?
    8) What differences can you observe between HTTP (port 80) and HTTPS (port 443) traffic in Wire-
       shark?




                                                     1
                                                                                                           2

Question 5. Local TCP Client–Server Communication in Python Design and analyze an advanced
TCP communication system using Python. In this activity, you will extend the simple client–server inter-
action by introducing additional behavior and analyzing the underlying TCP mechanisms that guarantee
reliable data transfer. Instructions.
    1) Create a TCP server in Python that can handle multiple consecutive client connections without
       restarting.
    2) The server must receive a message from the client, wait for 2 seconds before replying (simulate
       network delay), and then send an acknowledgment (ACK message).
    3) The client must:
        (a) Establish the connection,
        (b) Send 3 separate text messages (each spaced by 1 second),
        (c) Wait for the acknowledgment after each message,
        (d) Display the time elapsed between sending and receiving (Round Trip Time approximation).
    4) Run the experiment locally first (127.0.0.1), and then—if possible—between two machines in the
       same network.
    5) Capture the exchange using Wireshark, applying the filter
                                       tcp.port == chosen port
  Answer:
   1) How many TCP segments were exchanged for each message (including acknowledgments)?
   2) What happens to the Sequence and Acknowledgment numbers when multiple messages are sent
      sequentially?
   3) How does introducing a 2-second delay on the server affect the client’s perception of connection
      reliability?
   4) Compare the Round Trip Time (RTT) measured by the client with the one displayed by Wireshark.
      Are they similar? Why or why not?
   5) Observe the TCP window size throughout the communication. Does it change between messages?
      Explain what it represents.
   6) What happens if you abruptly stop the server while a message is in transit? How does TCP handle
      this event compared to UDP?
   7) Analyze the flags in the TCP header (SYN, ACK, PSH, FIN). In what order do they appear, and
      why?

Question 6. (Group) Sending a .txt File Between Two Laptops Using TCP
  Implement a TCP client–server system to send a text file (message.txt) from one laptop to another
connected to the same Wi-Fi network (e.g., a hotspot). The server must receive the file and save it locally.
   1) Connect both laptops to the same network (same hotspot).
   2) Identify the IP address of the laptop acting as the server.
   3) Write a Python TCP server that receives a file and saves it as received.txt.
   4) Write a Python TCP client that connects to the server and sends the file message.txt.
   5) Capture the transmission with Wireshark (you may filter using tcp.port == 5000).
   6) Verify that the received file matches the original file.
  Answer
   1) What were the IP addresses of the server and the client during the connection? (Sreenshot it).
   2) How many TCP segments were generated during the transfer?
   3) What was the size of the last segment transmitted?
   4) Identify the three-way handshake and the connection termination sequence in the capture.
   5) Were there any retransmissions in the capture? If so, what could have caused them?
   6) What was the maximum window size observed in the TCP connection?
   7) What does each acknowledgment number (ACK) correspond to in relation to the file bytes?
   8) What is the relationship between the file size and the number of TCP segments transmitted?
                                                                                                     3

 9) How would packet loss in the Wi-Fi connection affect TCP performance?
10) What difference would you expect if both laptops were connected via Ethernet instead of Wi-Fi?
CS-UTEC
