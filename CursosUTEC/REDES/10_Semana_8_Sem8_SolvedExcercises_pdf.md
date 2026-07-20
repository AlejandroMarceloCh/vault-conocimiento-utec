---
curso: REDES
titulo: 10 - Semana 8/Sem8_SolvedExcercises
slides: 6
fuente: 10 - Semana 8/Sem8_SolvedExcercises.pdf
---

garias@utec.edu.pe
CS4054: Networks — 26-1
May 16, 2026
                                     Week 08 - Solved Exercises


Question 1. This elementary problem begins to explore propagation delay and transmission delay,
two central concepts in data networking. Consider two hosts, A and B, connected by a single link of
rate R bps. Suppose that the two hosts are separated by m meters, and that the propagation speed along
the link is s meters/sec. Host A needs to send a packet of size L bits to Host B.

  Note
  Propagation delay (dprop ): is the time it takes for a bit to propagate from the sender to the
  receiver.

  Note
  Transmission delay (dtrans ): is the time required to transmit all of the packet’s bits into the link.

  Note
  Round-trip time (RTT): is the time it takes for a small packet to travel from the client to the
  server and then back to the client. The RTT includes packet-propagation delays, packet-queuing
  delays at intermediate routers and switches, and packet-processing delays.

   1) Express the propagation delay dprop in terms of m and s.
   2) Determine the transmission time of the packet dtrans in terms of L and R.
   3) Ignoring processing delay and queuing delay, obtain an expression for the end-to-end delay.
   4) Suppose Host A begins to transmit the packet at time t = 0. At time t = dtrans , where is the last
      bit of the packet?
   5) Suppose dprop is greater than dtrans . At time t = dtrans , where is the first bit of the packet?
   6) Suppose dprop is less than dtrans . At time t = dtrans , where is the first bit of the packet?
   7) Suppose s = 2.5 × 108 , L = 1500 bytes, and R = 10 Mbps. Find the distance m such that
      dprop = dtrans .
  Solution:
   1) Propagation delay (dprop ): The propagation delay is the time it takes for a single bit to travel
      from the sender to the receiver over the distance m at speed s.
                                                          m
                                                  dprop =
                                                           s
   2) Transmission delay (dtrans ): The transmission delay is the time required to push all L bits of the
      packet into the link at a transmission rate of R bps.
                                                           L
                                                 dtrans =
                                                           R
   3) End-to-end delay: Ignoring processing and queuing delays, the total end-to-end delay is the sum
      of the transmission delay and the propagation delay.
                                                                   L m
                                   dend−to−end = dtrans + dprop = +
                                                                   R      s
   4) Position of the last bit at t = dtrans : At t = dtrans , Host A has just finished transmitting the
      entire packet. Therefore, the last bit has just been placed onto the link and is located right at the
      beginning of the link (at Host A).
                                                    1
                                                                                                              2

   5) Position of the first bit at t = dtrans if dprop > dtrans : Since the propagation delay dprop is greater
      than the transmission time, the first bit has not yet reached Host B. It has been traveling for dtrans
                                                                                                 L
      seconds at speed s. Therefore, it is on the link, at a distance of dtrans × s meters (or R    · s meters)
      away from Host A.
   6) Position of the first bit at t = dtrans if dprop < dtrans : Since the propagation delay is less than
      the transmission time, the first bit takes less time to travel the entire link than it takes to transmit
      the packet. Thus, by the time t = dtrans , the first bit has already reached Host B.
   7) Finding the distance m such that dprop = dtrans : First, convert the given units to standard SI
      units:
         • L = 1500 bytes = 1500 × 8 = 12, 000 bits
         • R = 10 Mbps = 10 × 106 bps = 107 bps
         • s = 2.5 × 108 meters/sec
        Calculate dtrans :
                                       12, 000
                             dtrans =          = 1.2 × 10−3 seconds = 1.2 ms
                                         107
        Set dprop = dtrans and solve for m:
                                      m
                                         = dtrans =⇒ m = s × dtrans
                                      s
                         m = (2.5 × 108 m/s) × (1.2 × 10−3 s) = 300, 000 meters
        Therefore, the distance is 300 km (or 3 × 105 meters).

Question 2. Consider the following ASCII string captured by Wireshark when the browser sent an HTTP
GET message (i.e., this is the actual content of an HTTP GET message). The characters <cr><lf> are carriage
return and line feed characters (i.e., the italicized string <cr> in the text represents the carriage return
character that was contained at that point in the HTTP header).
GET /cs453/index.html HTTP/1.1<cr><lf>
Host: gaia.cs.umass.edu<cr><lf>
User-Agent: Mozilla/5.0 (Windows;U; Windows NT 5.1; en-US; rv:1.7.2)
Gecko/20040804 Netscape/7.2 (ax)<cr><lf>
Accept: text/xml, application/xml, application/xhtml+xml, text/html;q=0.9,
text/plain;q=0.8, image/png,*/*;q=0.5<cr><lf>
Accept-Language: en-us,en;q=0.5<cr><lf>
Accept-Encoding: zip,deflate<cr><lf>
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7<cr><lf>
Keep-Alive: 300<cr><lf>
Connection: keep-alive<cr><lf><cr><lf>
  Answer the following questions, indicating where in the HTTP GET message the answer is located:
    1) What is the URL of the document requested by the browser?
    2) Which version of HTTP is the browser using?
    3) Does the browser request a non-persistent or persistent connection?
    4) What is the IP address of the host on which the browser is running?
    5) What type of browser initiates this message? Why is the browser type needed in an HTTP request
       message?
  Solution:
    1) URL of the document requested: The complete URL is http://gaia.cs.umass.edu/cs453/index.htm
         • Location: This is derived by combining the relative path found in the Request Line (line 1:
           /cs453/index.html) with the value of the Host: header field found on line 2 (gaia.cs.umass.edu).
    2) HTTP Version: The browser is using HTTP/1.1.
         • Location: Found at the end of the Request Line (line 1): GET /cs453/index.html HTTP/1.1.
                                                                                                             3

   3) Connection Type (Persistent vs. Non-persistent): The browser requests a persistent con-
      nection.
        • Location: Found in the Connection: header field (line 10), which explicitly states keep-alive.
           This is also supported by the presence of the Keep-Alive: 300 header field on line 9.
   4) IP Address of the Host: The IP address of the host running the browser is not contained
      anywhere within this HTTP GET message.
        • Explanation: HTTP is an Application Layer protocol and does not include network-layer
           parameters like IP addresses in its text headers. This information is instead contained within
           the network-layer IP packet header that encapsulates the TCP segment carrying this HTTP
           message.
   5) Browser Type and Purpose:
        • Browser Type: The browser is Netscape 7.2 (running on Windows XP / NT 5.1, and built
           on the Mozilla 5.0 / Gecko layout engine).
        • Location: Found in the User-Agent: header field across lines 3 and 4: User-Agent: Mozilla/5.0
           ... Netscape/7.2 (ax).
        • Why it is needed: The server uses the browser type to optimize and format the application
           response. Since different browsers and browser versions have distinct capabilities, HTML/CSS
           support, and rendering engines, knowing the User-Agent allows the server to deliver a cus-
           tomized version of the requested web page that is compatible with that specific browser.

Question 3. Consider distributing a file of F bits to N peers using a client-server architecture. Assume
a fluid model where the server can transmit simultaneously to multiple peers, transmitting to each peer at
different rates, provided that the combined rate does not exceed us .
                      us                                                                        NF
    a. Suppose that      ≤ dmin . Specify a distribution scheme that has a distribution time of      .
                      N                                                                          us
                      us                                                                         F
    b. Suppose that      ≥ dmin . Specify a distribution scheme that has a distribution time of      .
                      N                                                                         dmin
     c. Conclude that the minimum distribution time is generally given by
                                                NF   F
                                                            
                                            max    ,    .
                                                us dmin
  Solution:
                                   us
   a. Distribution scheme for          ≤ dmin : In this scenario, the bottleneck constraint is entirely the
                                   N
      upload capacity of the server rather than the download rates of individual peers.
        The server can evenly divide its total upload rate us among all N peers, dedicating a constant
                                us                                       us
      transmission rate of r =     to each peer simultaneously. Since       ≤ dmin ≤ di for all individual
                                N                                        N
      peers i, every peer’s download link can fully accommodate this rate without bottlenecking.
        The time required for any single peer to completely download the file of size F at this rate is:
                                                      F     NF
                                             Ti =         =
                                                    us /N   us
      Since all N peers are served in parallel at this exact rate, the total distribution time for the archi-
                 NF
      tecture is     .
                  us
                                   us
   b. Distribution scheme for          ≥ dmin : In this scenario, the system is constrained by the download
                                   N
      capacity of the slowest peer(s).
        The server can transmit data to each peer i at a rate exactly matching the minimum download
      capacity, r = dmin . The aggregate upload rate required from the server to support all N channels
                                                                   us
      simultaneously is N · dmin . Because we are given that          ≥ dmin , it follows that us ≥ N · dmin ,
                                                                   N
      meaning the server possesses more than enough upload bandwidth to sustain this scheme.
                                                                                                           4

        The time required for each peer to download the file at this rate is:
                                                    F
                                              Ti =
                                                   dmin
                                                                                                      F
      Thus, the overall distribution time for all peers to obtain the file under this configuration is    .
                                                                                                     dmin
   c. Conclusion for the Minimum Distribution Time: Regardless of the distribution strategy or
      architecture used:
         • The server must upload a total of N · F bits (since there are N peers each needing a copy of
           the file F ). Because its maximum capacity is us , the distribution time can never be less than
           NF
                .
            us
         • The slowest peer cannot download faster than its maximum limit dmin . Therefore, it requires
                            F
           a minimum of         seconds to obtain the entire file, meaning the overall distribution process
                           dmin
           cannot finish sooner than this limit.
      Consequently, the absolute minimum distribution time must respect both physical bounds simulta-
      neously, establishing the lower bound:
                                                        NF    F
                                                                 
                                          Tmin ≥ max        ,
                                                         us dmin
      Parts (a) and (b) demonstrate that this theoretical lower bound is perfectly achievable in both mu-
      tually exclusive cases covering all possible values. Thus, the minimum distribution time is precisely:
                                                    NF     F
                                                             
                                              max       ,
                                                     us dmin
Question 4. UDP and TCP use 1’s complement for their checksums. Suppose you have the following
three 8-bit bytes: 01010011, 01100110, 01110100. What is the 1’s complement of the sum of these 8-bit
bytes? (Note that although UDP and TCP use 16-bit words in the checksum calculation, for this problem
you are asked to consider 8-bit sums). Show your entire procedure.
  Why does UDP take the 1’s complement of the sum; that is, why not just use the sum? With the 1’s
complement scheme, how does the receiver detect errors? Is it possible for a 1-bit error to go undetected?
What about a 2-bit error?
  Solution:
  1. Mathematical Procedure for the 1’s Complement Checksum:
  First, we perform binary addition on the three given 8-bit bytes. Any carry-out bit resulting from the
8th position must be added back to the least significant bit (end-around carry).
  Summing the first two bytes:
                                                 01010011
                                             + 01100110
                                                 10111001
  Adding the third byte to the previous partial sum:
                                              10111001
                          +                   01110100
                            100101101 (9-bit result due to a carry-out of 1)
  Perform the end-around carry by removing the leftmost 1 and adding it to the rightmost bit:
                                               00101101
                               +               00000001
                                   00101110 (Final 1’s complement sum)
  Finally, to get the checksum, take the 1’s complement (invert all bits) of the final sum:
                                   Checksum =∼ 00101110 = 11010001
                                                                                                                5

  2. Theoretical Questions:
    • Why does UDP take the 1’s complement of the sum instead of just using the sum? By
      transmitting the inverted sum (the 1’s complement) as the checksum, the receiver’s verification task
      becomes computationally streamlined. The receiver can simply compute the 1’s complement sum
      over all received data fields plus the checksum field. If no errors occurred during transmission, this
      complete sum will result in all bits being 1 (11111111). Checking if a word is entirely filled with 1s
      is exceptionally fast and simple to implement in both hardware and software.
    • How does the receiver detect errors? The receiver adds all received data bytes together with the
      checksum byte using 1’s complement addition (applying the end-around carry rule for any overflow
      bits). After evaluating the total, it inspects the final bit pattern. If even a single bit in the resulting
      sum is a 0, the receiver knows that an error has occurred and drops the packet.
    • Is it possible for a 1-bit error to go undetected? No, it is impossible for a 1-bit error to
      go undetected. Flipping exactly one bit from 0 to 1 or from 1 to 0 will invariably alter the final
      mathematical sum, ensuring that the receiver’s calculated total will contain at least one 0.
    • What about a 2-bit error? Yes, it is possible for a 2-bit error to go completely undetected. If
      one bit is flipped from 0 to 1 and another bit in the exact same column/position of a different byte
      is flipped from 1 to 0, the errors counteract each other. The arithmetic sum remains identical to the
      original calculation, meaning the checksum evaluation will pass successfully despite the corruption.

Question 5. Consider Figure 1, for which there is an institutional network connected to the Internet.
Suppose that the average object size is 1, 000, 000 bits and that the average request rate from the insti-
tution’s browsers to the origin servers is 16 requests per second. Also suppose that the amount of time
it takes from when the router on the Internet side of the access link forwards an HTTP request until it
receives the response is three seconds on average. Model the total average response time as the sum of the
average access delay (that is, the delay from Internet router to institution router) and the average Internet
delay. For the average access delay, use ∆/(1 − ∆β), where ∆ is the average time required to send an
object over the access link and β is the arrival rate of objects to the access link.




                   Figure 1. Bottleneck between an institutional network and the Internet


   a. Find the total average response time.
   b. Now suppose a cache is installed in the institutional LAN. Suppose the miss rate is 0.4. Find the
      total response time.
  Solution:
                                                                                                        6

a. Find the total average response time without a cache:
     First, we extract the necessary parameters from the problem description and the provided diagram:
     • Average object size (L): 1, 000, 000 bits
     • Average request rate (β): 16 requests/sec
     • Average Internet delay: 3 seconds
     • Access link capacity (R): 15 Mbps = 15, 000, 000 bps (from the diagram)
     Next, calculate ∆, the average time required to transmit a single object over the access link:
                              L     1, 000, 000 bits     1
                         ∆=      =                   =      seconds ≈ 0.0667 s
                              R    15, 000, 000 bps     15
     Now, determine the traffic intensity (ρ) on the access link:
                                               1           16
                                 ρ=∆·β =          × 16 =      ≈ 1.0667
                                               15          15
     Analysis: Because the traffic intensity ρ > 1, the rate at which data arrives at the access link
   exceeds its maximum capacity to transmit it. In queuing theory, when the arrival rate is greater
   than or equal to the service rate, the queue grows infinitely.
     Using the provided formula for the access delay:
                     ∆          1/15         1/15
 Access Delay =            =             =          = −1 (mathematically invalid due to instability)
                  1 − ∆β     1 − 16/15      −1/15
     Therefore, the average access delay grows without bound and approaches infinity (∞). Conse-
   quently, the total average response time is infinite / unbounded (the system is completely unstable).
b. Find the total response time with an institutional cache:
     When a local cache is introduced, a fraction of the requests are satisfied directly inside the high-
   speed institutional LAN without traversing the bottleneck access link.
     • Miss rate = 0.4 (40% of requests must go to the Internet)
     • Hit rate = 1 − 0.4 = 0.6 (60% of requests are fulfilled locally)
     Calculate the modified request arrival rate that actually reaches the access link (β ′ ):
                         β ′ = Miss rate × β = 0.4 × 16 = 6.4 requests/sec
     Recalculate the traffic intensity on the access link under this new arrival rate:
                                              1           6.4
                               ρ′ = ∆ · β ′ =    × 6.4 =      ≈ 0.4267
                                              15          15
   Since ρ′ < 1, the queuing system on the access link is now completely stable.
     Calculate the new average access delay using the given formula:
                                                1        1
                                     ∆         15       15     1
                 Access Delay =          ′
                                           =      6.4 = 8.6 =     ≈ 0.1163 seconds
                                  1 − ∆β     1 − 15     15
                                                              8.6
     Determine the response time based on whether it is a hit or a miss:
     • Cache Hit (60% of requests): Satisfied within the high-speed LAN, so the delay is approx-
       imately 0 seconds.
     • Cache Miss (40% of requests): Must go out to the Internet, experiencing both access link
       and external Internet delay:
      Response Timemiss = Access Delay + Internet Delay = 0.1163 s + 3 s = 3.1163 seconds
     Finally, compute the total average response time as a weighted average:
       Total Average Response Time = (Hit Rate × 0) + (Miss Rate × Response Timemiss )
           Total Average Response Time = (0.6 × 0) + (0.4 × 3.1163) = 1.2465 seconds
CS-UTEC
