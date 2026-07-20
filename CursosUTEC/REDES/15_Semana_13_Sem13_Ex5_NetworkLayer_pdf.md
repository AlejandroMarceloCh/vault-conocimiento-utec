---
curso: REDES
titulo: 15 - Semana 13/Sem13_Ex5_NetworkLayer
slides: 2
fuente: 15 - Semana 13/Sem13_Ex5_NetworkLayer.pdf
---

cwilliams, garias@utec.edu.pe
CS4054: Networks
June 17, 2026
                                        Ex 5: Network Layer


Question 1. AIMD - AIAD: Show that TCP’s AIMD (Additive Increase, Multiplicative Decrease) al-
gorithm guarantees that a fair allocation exists. Make a diagram to illustrate this and use example values
to illustrate the step-by-step convergence.

Suppose that, instead of a multiplicative decrease, TCP reduced the window size by a constant amount.
Would the resulting AIAD (Additive Increase, Additive Decrease) algorithm converge towards an equal
share allocation? Justify your answer using a diagram.
Question 2. When a large datagram is fragmented into several smaller datagrams, where are these
small datagrams reassembled into a single larger datagram? Suppose an application generates 40-byte
data blocks every 20 msec, and that each block is encapsulated in a TCP segment and then in an IP
datagram. What percentage of each datagram will be overhead, and what percentage will correspond to
the application data?
Question 3. A host A must send a 5200-byte IP datagram (including the IP header) to a host B. The
datagram traverses two consecutive networks, each with a different MTU (Maximum Transmission Unit):
    • Network 1: MTU = 1500 bytes
    • Network 2: MTU = 620 bytes
  The IP header has a size of 20 bytes and contains no options. The original datagram does not have the
DF (Don’t Fragment) bit set.
   1) Will it be necessary to fragment the datagram?
   2) How many fragments are generated upon leaving host A (for the first network)?
   3) How many fragments are generated after passing through the second network, considering that the
      previous fragments can be fragmented again?
   4) For each final fragment that arrives at host B, indicate:
        • The total size (total length).
        • The size of the data bytes.
        • The fragment offset value (in 8-byte units).
        • The value of the MF (More Fragments) bit.
                                         Wireshark Exercises

Question 4. IPv4 Address Classes and Subnet Analysis
  A small company is organizing its internal network. You are given the following IPv4 addresses and
asked to determine their class, subnet characteristics, and implications for network design.
  Addresses to analyze:
   1) 10.24.56.12/8
   2) 172.18.20.5/16
   3) 192.168.25.200/24
   4) 200.45.10.3/26
  Answer:
   1) Identify the class (A, B, C, D, or E) of each IP address.
   2) For each, specify the default subnet mask and the CIDR prefix (e.g., /8, /16, /24).
   3) Determine the network address and broadcast address of each subnet.
   4) Calculate the number of valid host addresses available in each subnet.
   5) Which of these addresses belong to private network ranges? Explain.
                                                    1
                                                                                                       2

   6) If you wanted to divide the 192.168.25.0/24 network into 4 equal subnets, what would be the new
      subnet mask and range of hosts in the first subnet?
   7) Explain how the classful addressing system differs from CIDR (Classless Inter-Domain Routing).
   8) Why is classful addressing no longer practical for modern networks? Provide at least two technical
      reasons.
Question 5. NAT
   • Connect to a shared Wi-Fi network.
   • Open Wireshark and start a capture on your active interface.
   • Open your browser and go to https://whatismyipaddress.com/ and then ping 8.8.8.8.
   • Stop the capture and analyze packets using the filter (use the correct statement):
                                       ip and (icmp or tcp)
    • Compare your local IP (ipconfig / ifconfig) with the public IP shown on the website.
  Answer:
   1) What is your local private IP address as seen in Wireshark?
   2) What public IP is displayed on the website? Are they the same? Why or why not?
   3) What is the source IP address of the packets leaving your computer vs. the address seen by the
      destination server?
   4) Identify the port numbers used in your outbound packets. Are they unique per connection? Explain
      how NAT uses port translation.
   5) Why do all devices on the same network show the same public IP on the website?
   6) If an external device attempted to contact your local IP directly, what would happen and why?
   7) Does NAT modify any field in the IP header other than the source address? Justify your answer.
   8) Does NAT operate at the same OSI layer as IP? If not, which layer does it interact with, and how?
Question 6. IP and ICMP
   • Start Wireshark capture on the main interface.
   • In the terminal, run:
       – ping -n 4 www.inria.fr
       – tracert www.inria.fr (or traceroute on Linux/Mac).
   • Stop the capture and filter ICMP traffic with:
                                                 icmp
    • Analyze both Echo Requests/Replies (Ping) and Time Exceeded messages (Traceroute).
  Answer
   1) What are the source and destination IP addresses in your Ping requests and replies?
   2) What are the ICMP Type and Code values for Echo Request and Echo Reply messages?
   3) Why does ICMP not include port numbers in its header, unlike TCP or UDP?
   4) In Traceroute, which ICMP message type is returned when TTL expires? What is its significance?
   5) Compare the TTL values in successive packets during Traceroute. What pattern do you observe,
      and why?
   6) In your Ping packets, what is the round-trip time (RTT) reported, and what network factors might
      influence it?
   7) Compare the IP headers of ICMP Echo Request and ICMP Time Exceeded packets — which fields
      differ and why?
   8) How do ICMP and IP work together to support network diagnostics and error reporting?
  CS-UTEC
