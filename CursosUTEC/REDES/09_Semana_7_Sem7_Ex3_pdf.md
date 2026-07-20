---
curso: REDES
titulo: 09 - Semana 7/Sem7_Ex3
slides: 4
fuente: 09 - Semana 7/Sem7_Ex3.pdf
---

cwilliams, garias@utec.edu.pe
CS4054: Networks — 26-1
May 6, 2026
                                                   Ex 3

Question 1. Consider the motivation for refining the rdt2.1 protocol. Demonstrate that the receiver
(Figure 1), when operating in conjunction with the sender (Figure 2), can lead both entities into a deadlock
state. Specifically, describe a scenario where both the sender and the receiver become trapped waiting for
an event that will never occur.




                                         Figure 1. receiver rdt 2.1




                                         Figure 2. sender rdt 2.1

                                                     1
                                                                                                           2

Question 2. Suppose a user clicks on a link to retrieve a base HTML file that contains references to 12
additional small objects (such as images or scripts) located on the same server.
  Assume that there are no entries in the local DNS cache, so n DNS servers must be visited sequentially
with round-trip times RTT1 , RTT2 , . . . , RTTn . Let RTT0 be the round-trip time between the local host
and the web server. Ignoring the transmission times of all objects, answer the following:
   a. Define the general formula for the total time elapsed from the click until the last object is received
      using Non-persistent HTTP without parallel TCP connections.
   b. Define the general formula if Non-persistent HTTP is used with a maximum of 5 parallel
      connections.
   c. Define the general formula if Persistent HTTP with pipelining is used.
   d. Numerical Calculation: Using the following values:
                      n
                      X
                 S=         RTTi = 120 ms,   RTT0 = 80 ms,     N = 12 additional objects
                      i=1

      Calculate the total time for the three cases above (a, b, and c) and identify which scheme is the
      most efficient.

   Protocol Reminders
       • DNS: Total resolution time is S = RTTi .
                                             P

       • Non-persistent HTTP: Each object requires a TCP handshake (1 RTT0 ) and a request/re-
         sponse (1 RTT0 ), totaling 2 RTT0 per download cycle.
       • Persistent HTTP (Pipelining): After the base HTML is downloaded, all referenced objects
         are requested in a single burst over the same connection, ideally taking only 1 RTT0 for all
         additional objects.


Question 3. Suppose a client host wants to obtain the IP address associated with a domain name. The
client first contacts its local DNS server. Let RT T0 be the delay between the client and the local server.
For external queries, the delays between the local server and the rest of the hierarchy are RT T1 (Root),
RT T2 (TLD), and RT T3 (Authoritative).
   a. Assuming no caching is involved, calculate the total delay for an iterative query from the perspec-
      tive of the local DNS server.
   b. Calculate the total delay if a pure recursive query is used (where each server in the chain queries
      the next one).
   c. What critical advantage does DNS caching at the local server provide to reduce traffic toward Root
      and TLD servers? Discuss whether this affects data consistency.
                                                                                                          3

Question 4. Consider Figure 3, for which there is an institutional network connected to the Internet.
Suppose that the average object size is 1, 000, 000 bits and that the average request rate from the insti-
tution’s browsers to the origin servers is 16 requests per second. Also suppose that the amount of time
it takes from when the router on the Internet side of the access link forwards an HTTP request until it
receives the response is three seconds on average (see Section 2.2.5). Model the total average response
time as the sum of the average access delay (that is, the delay from Internet router to institution router)
and the average Internet delay. For the average access delay, use ∆/(1 − ∆β), where ∆ is the average time
required to send an object over the access link and β is the arrival rate of objects to the access link.




                  Figure 3. Bottleneck between an institutional network and the Internet


   a. Find the total average response time.
   b. Now suppose a cache is installed in the institutional LAN. Suppose the miss rate is 0.4. Find the
      total response time.
                                                                                                        4

Question 5. Consider the scenario in Figure 4, which shows a Web server (Host B) interacting with two
different hosts (Host A and Host C). Host C has two simultaneous connections to the server.
    a. For the segments flowing from the server (Host B) back to the clients, specify the port values and
       IP addresses for each connection:
          • To Host A: Source Port, Destination Port, Source IP, and Destination IP.
          • To Host C (Left process): Source Port, Destination Port, Source IP, and Destination IP.
          • To Host C (Right process): Source Port, Destination Port, Source IP, and Destination IP.
    b. Suppose that a receiver (using UDP or TCP) computes the Internet checksum for a received segment
       and finds that it matches the value carried in the checksum field.
          • Can the receiver be absolutely certain that no bit errors have occurred?
          • Explain your answer, considering the mathematical limitations of the 1’s complement sum used
            in the Internet checksum.




                                   Figure 4. Communication Scheme


  CS-UTEC
