---
curso: REDES
titulo: 13 - Semana 11/Sem11_LAB4_IP_P2
slides: 7
fuente: 13 - Semana 11/Sem11_LAB4_IP_P2.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-02




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
 2026-06-02


                              LAB4A - IP P2
 In this lab, we’ll investigate the celebrated IP protocol, focusing on the IPv4 and IPv6
 datagram. This lab has three parts. In the first part, we’ll analyze packets in a trace of
 IPv4 datagrams sent and received by the traceroute program (the traceroute program
 itself is explored in more detail in the Wireshark ICMP lab). We’ll study IP fragmentation
 in Part 2 of this lab, and take a quick look at IPv6 in Part 3 of this lab.


 https://www.hostinger.com/es/tutoriales/comando-traceroute
 Capturing packets from an execution of
 traceroute
 In order to generate a trace of IPv4 datagrams for the first two parts of this lab, we’ll use
 the traceroute            program to send datagrams of two different sizes to
 gaia.cs.umass.edu.     Recall that traceroute operates by first sending one or more
 datagrams with the time-to-live (TTL) field in the IP header set to 1; it then sends a series
 of one or more datagrams towards the same destination with a TTL value of 2; it then
 sends a series of datagrams towards the same destination with a TTL value of 3; and so
 on.   Recall that a router must decrement the TTL in each received datagram by 1
 (actually, RFC 791 says that the router must decrement the TTL by at least one). If the
 TTL reaches 0, the router returns an ICMP message (type 11 – TTL-exceeded) to the
 sending host. As a result of this behavior, a datagram with a TTL of 1 (sent by the host
 executing traceroute ) will cause the router one hop away from the sender to send
 an ICMP TTL-exceeded message back to the sender; the datagram sent with a TTL of 2
 will cause the router two hops away to send an ICMP message back to the sender; the
 datagram sent with a TTL of 3 will cause the router three hops away to send an ICMP
 message back to the sender; and so on. In this manner, the host executing traceroute
 can learn the IP addresses of the routers between itself and the destination by looking at
 the source IP addresses in the datagrams containing the ICMP TTL-exceeded messages.

Let’s run traceroute and have it send datagrams of two different sizes. The larger of
the two datagram lengths will require traceroute messages to be fragmented across
multiple IPv4 datagrams.

   ●​ Linux/MacOS. With the Linux/MacOS traceroute command, the size of the UDP
       datagram sent towards the final destination can be explicitly set by indicating the
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-02

       number of bytes in the datagram; this value is entered in the traceroute
       command line immediately after the name or address of the destination. For
       example, to send traceroute datagrams of 2000 bytes towards
       gaia.cs.umass.edu, the command would be:

                 %traceroute gaia.cs.umass.edu 2000

   ●​ Windows. The tracert program provided with Windows does not allow one to
       change the size of the ICMP message sent by tracert. So it won’t be possible to
       use a Windows machine to generate ICMP messages that are large enough to force
       IP fragmentation. However, you can use tracert to generate small, fixed length
       packets to perform Part 1 of this lab. At the DOS command prompt enter:

                 >tracert gaia.cs.umass.edu

Do the following:

   ●​ Start up Wireshark and begin packet capture. (Capture->Start or click on the blue
       shark fin button in the top left of the Wireshark window).
   ●​ Enter two traceroute commands, using gaia.cs.umass.edu as the destination,
       the first with a length of 56 bytes. Once that command has finished executing,
       enter a second traceroute command for the same destination, but with a
       length of 3000 bytes.
   ●​ Stop Wireshark tracing.

 4. Basic IPv4

In your trace, you should be able to see the series of UDP segments (in the case of
MacOS/Linux) or ICMP Echo Request messages (Windows) sent by traceroute on your
computer, and the ICMP TTL-exceeded messages returned to your computer by the
intermediate routers. In the questions below, we’ll assume you’re using a MacOS/Linux
computer; the corresponding questions for the case of a Windows machine should be
clear. Your screen should look similar to the screenshot in Figure 2, where we have used
the display filter “udp||icmp” (see the light-green-filled display-filter field in Figure 2) so
that only UDP and/or ICMP protocol packets are displayed.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-02




 Figure 2: Wireshark screenshot, showing UDP and ICMP packets in the tracefile
                             ip-wireshark-trace1-1.pcapng



 4.1. Answer the following questions
  1.​ (Linux) Select the first UDP segment sent by your computer via the traceroute
     command to gaia.cs.umass.edu. (Hint: this is 44th packet in the trace file in the
     ip-wireshark-trace1-1.pcapng file in footnote 2). Expand the Internet Protocol part of
     the packet in the packet details window. What is the IP address of your computer?
  2.​ What is the value in the time-to-live (TTL) field in this IPv4 datagram’s header?
  3.​ What is the value in the upper layer protocol field in this IPv4 datagram’s header?
     [Note: the answers for Linux/MacOS differ from Windows here].
  4.​ How many bytes are in the IP header?
  5.​ How many bytes are in the payload of the IP datagram? Explain how you
     determined the number of payload bytes.
  6.​ Has this IP datagram been fragmented? Explain how you determined whether or
     not the datagram has been fragmented.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-02

Next, let’s look at the sequence of UDP segments being sent from your computer via
traceroute, destined to 128.119.245.12. The display filter that you can enter to do this is
“ip.src==192.168.86.61 and ip.dst==128.119.245.12 and udp and !icmp”. This will allow you
to easily move sequentially through just the datagrams containing just these segments.
Your screen should look similar to Figure 3.




       Figure 3: Wireshark screen shot, showing up segments in the tracefile
     ip-wireshark-trace1-1.pcapng using the display filter ip.src==192.168.86.61 and
                    ip.dst==128.119.245.12 and udp and !icmp

   7.​ Which fields in the IP datagram always change from one datagram to the next
      within this series of UDP segments sent by your computer destined to
      128.119.245.12, via traceroute? Why?
   8.​ Which fields in this sequence of IP datagrams (containing UDP segments) ﻿stay
      constant? Why?
   9.​ Describe the pattern you see in the values in the Identification field of the IP
      datagrams being sent by your computer.

Now let’s take a look at the ICMP packets being returned to your computer by the
intervening routers where the TTL value was decremented to zero (and hence caused the
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-02

ICMP error message to be returned to your computer). The display filter that you can use
to show just these packets is “ip.dst==192.168.86.61 and icmp”.

   10.​What is the upper layer protocol specified in the IP datagrams returned from the
      routers? [Note: the answers for Linux/MacOS differ from Windows here].
   11.​ Are the values in the Identification fields (across the sequence of all of ICMP
      packets from all of the routers) similar in behavior to your answer to question 9
      above?
   12.​ Are the values of the TTL fields similar, across all of ICMP packets from all of the
      routers?

                               Checkpoint 3
 5. Fragmentation

In this section, we’ll look at a large (3000-byte) UDP segment sent by the traceroute
program that is fragmented into multiple IP datagrams.

Sort the packet listing from Checkpoint 1, with any display filters cleared, according to
time, by clicking on the Time column.

NOTE

 If you are running Windows, you may not be able to change the UDP segment size. So for
 this section use the following trace capture.
                  Click here to download the trace file.


 5.1. Answer the following questions
   13.​Find the first IP datagram containing the first part of the segment sent to
      128.119.245.12 sent by your computer via the traceroute command to
      gaia.cs.umass.edu, after you specified that the traceroute packet length should
      be 3000. Has that segment been fragmented across more than one IP datagram?
      (Hint: the answer is yes!)
   14.​What information in the IP header indicates that this datagram been fragmented?
   15.​What information in the IP header for this packet indicates whether this is the first
      fragment versus a latter fragment?
   16.​How many bytes are there in is this IP datagram (header plus payload)?
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-02

   17.​ Now inspect the datagram containing the second fragment of the fragmented UDP
      segment. What information in the IP header indicates that this is not the first
      datagram fragment?
   18.​What fields change in the IP header between the first and second fragment?
   19.​Now find the IP datagram containing the third fragment of the original UDP
      segment. What information in the IP header indicates that this is the last fragment
      of that segment?

Note: If your computer has an Ethernet or WiFi interface, a packet size of 3000 should
cause fragmentation.

                              Checkpoint 4
