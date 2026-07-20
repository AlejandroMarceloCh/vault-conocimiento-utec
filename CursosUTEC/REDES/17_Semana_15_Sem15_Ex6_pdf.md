---
curso: REDES
titulo: 17 - Semana 15/Sem15_Ex6
slides: 3
fuente: 17 - Semana 15/Sem15_Ex6.pdf
---

cwilliams, garias@utec.edu.pe
CS4054: Networks
July 1, 2026
                                   Ex 6: TCP and Network Layer


                                         Theoretical Exercises

Question 1. IP Fragmentation and MTU
   A host A must send a 4200-byte IP datagram (including the IP header) to a host B. The datagram
traverses two consecutive networks, each with a different MTU (Maximum Transmission Unit):
    • Network 1: MTU = 1500 bytes
    • Network 2: MTU = 820 bytes
 The IP header has a size of 20 bytes and contains no options. The original datagram does not have the
DF (Don’t Fragment) bit set.
   1) Will it be necessary to fragment the datagram? Explain briefly.
   2) How many fragments are generated upon leaving host A (for the first network)?
   3) How many fragments are generated after passing through the second network, considering that the
      previous fragments must be fragmented again to fit the new MTU?
   4) For each final fragment that arrives at host B, indicate:
        • The total size (total length).
        • The size of the data bytes (payload).
        • The fragment offset value (in 8-byte units).
        • The value of the MF (More Fragments) flag.

Question 2. IPv4 Address Classes, Connectivity, and Subnetting
  Consider the following IP configurations for devices connected to the same Layer 2 switch, along with a
configured router interface acting as a gateway:
    • PC1: 192.168.100.50 /26
    • PC2: 192.168.100.110 /26
    • PC3: 192.168.100.150 /26
    • GW1 (Router Interface): 192.168.100.1 /26
  Answer:
   1) Identify the IP class (A, B, or C) for the base network address 192.168.100.0. What is the default
      classful subnet mask for this class?
   2) If PC1 and PC2 attempt to communicate, will their traffic be sent directly between them at Layer
      2, or will it require a router? Justify your answer by calculating their respective network addresses.
   3) Can PC3 successfully send an IP datagram directly to GW1 at the local network level? Explain the
      reason based on their subnet configurations.
   4) A separate department is assigned the network block 200.50.10.0/24. The network administrator
      needs to divide this block to support exactly 6 subnets of equal size. What will be the new subnet
      mask (in decimal and CIDR notation), and how many usable host addresses will be available per
      subnet?




                                                     1
                                                                                                           2

Question 3. Reliable Data Transfer: GBN, SR, and TCP
   Assume that the timeout values for Go-Back-N (GBN), Selective Repeat (SR), and TCP (no delayed
ACK) are long enough so that six consecutive data segments and their corresponding ACKs can be received
(if they are not lost in the channel) by the receiving host (Host B) and the sending host (Host A).
   Suppose Host A sends six data segments to Host B, and the third segment (sent from A) is lost in
transit. Ultimately, all six data segments are correctly received by Host B after necessary retransmissions.
     1) How many total segments has Host A sent, and how many total ACKs has Host B sent? What
        are the sequence numbers of the segments sent by A and the acknowledgment numbers sent by B?
        Answer this question for the three protocols (GBN, SR, and TCP).
     2) If the timeout values for the three protocols are much greater than 6 RTT, which of the three
        protocols successfully delivers the six data segments in the shortest time interval? Justify your
        answer.
                             Laboratory Exercises (Wireshark & Python)

Question 4. Network Layer Analysis: NAT, IP, and ICMP
   • Connect to a Wi-Fi network. Open Wireshark and start a capture on your active interface.
   • Open your browser and go to https://whatismyipaddress.com/ to find your public IP.
   • Open a terminal and run a traceroute to Cloudflare’s DNS:
       – tracert 1.1.1.1 (Windows) or traceroute 1.1.1.1 (Linux/Mac).
   • Stop the capture and analyze packets using the following filter:
                                               ip and icmp
  Answer:
   1) Compare your local IP with the public IP. How does NAT maintain the mapping for multiple local
      hosts communicating with the same external server?
   2) In the Traceroute capture, which ICMP message type and code are returned by intermediate routers
      when the TTL expires?
   3) Trace the TTL values in the IP headers of successive outbound packets. What specific pattern is
      used by Traceroute to map the network topology?
   4) Select one ICMP Time Exceeded packet. Inspect its payload. What specific information from the
      original discarded packet is encapsulated, and why is this strictly required by the sender?
   5) Consider the NAT router processing the returning ICMP Time Exceeded message. How does it know
      which internal host should receive this ICMP error, given that the original packet’s TCP/UDP ports
      are embedded inside the ICMP payload?
   6) Analyze the IP Identification (IPv4 ID) field in your outbound ICMP requests. Does it increment
      sequentially, or is it randomized? Explain how predictable IP ID sequences can be exploited for
      passive OS fingerprinting or identifying the number of distinct devices behind a NAT.

Question 5. TCP Congestion and Reliability with Python
 Modify the standard TCP client-server interaction to observe TCP’s reliability mechanisms under stress.
 Instructions.
  1) Create a TCP server in Python that receives messages, waits for 1 second before replying (simu-
     lating network delay), and sends an ACK message back to the client.
  2) The client must:
      (a) Establish the connection.
      (b) Send 5 separate text messages in rapid succession (spaced by only 0.1 seconds), without
          waiting for the server’s application-level ACK between them.
      (c) Wait to receive all replies.
  3) Run the experiment locally (127.0.0.1).
  4) Capture the exchange using Wireshark, applying the filter:
                                      tcp.port == <chosen port>
                                                                                                     3

Answer:
 1) How many total TCP segments were captured for the entire session? Identify the specific packets
    (by relative number) corresponding to the 3-way handshake and connection termination.
 2) Detail the Sequence (Seq) and Acknowledgment (Ack) numbers for the first 3 data messages sent
    by the client. Did the client wait for the first TCP ACK before pushing the second payload to the
    network?
 3) Did the server’s TCP stack acknowledge each message individually, or did you observe TCP Cumu-
    lative ACKs? Explain the conditions under which TCP utilizes a cumulative ACK.
 4) Observe the TCP Window Size value. Did the receiver’s window decrease at any point while the
    server application was delaying its read operations? What would happen if the receiver’s window
    reached zero?
 5) Analyze the TCP flags. Which specific flag is set by the client to indicate that the buffered data
    should be immediately pushed to the receiving application?
 6) Look at the connection setup (SYN packets). What is the TCP Window Scale option, and what
    was its negotiated value? Explain mathematically why the original 16-bit Window Size field in
    the TCP header is insufficient for modern high-bandwidth, high-latency networks, referencing the
    Bandwidth-Delay Product (BDP).
CS-UTEC
