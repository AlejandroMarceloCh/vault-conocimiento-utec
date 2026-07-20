---
curso: REDES
titulo: 06 - Semana 4 _ LAB1B_DNS + LAB2_UDP/LAB2_1_UDP
slides: 4
fuente: 06 - Semana 4 _ LAB1B_DNS + LAB2_UDP/LAB2_1_UDP.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-14




             LAB2 Transport Layer​

                                   UDP
The present evaluation will be received only if the checkpoints of all the
questions in the LABORATORY SESSION have been completed with the course
teacher.
For the checkpoints presentation, have a doc or text file where you present the
answer to the questions (including screenshots if necessary). Do not forget to
save your tracefile in case you miss any answer.
  I.​   The submission must consist of:
           A.​ Introduction (include introductory paragraph):
           B.​ Theoretical Framework (definitions with references).
           C.​ State of the Art (research papers, articles, theses, pages with
              references).
           D.​ Development of the experience (including discussion and correct
              figure formatting)
           E.​ Conclusions (at least one for each experience carried out).
           F.​ References (IEEE format)
 II.​   The submission must be presented in LaTeX or Docs format (pdf file).
III.​   Upload only the PDF of the report to Canvas, use a link to the repository,
        include step-by-step photos of each experience and answer checkpoints
        where relevant, plus codes if they have been developed.
IV.​    Only one member of the group will upload the report.
 V.​    Do not forget to list the names of all members.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-14


                     LAB2 UDP Part 1
 In this lab, we’ll take a quick look at the UDP transport protocol. UDP is a
streamlined, no-frills protocol.

1. Simple UDP Capture
  ●​ Start capturing packets in Wireshark
  ●​ Go to your browser and open:
       www.utec.edu.pe or www.unsplash.com or www.cisco.com
  ●​ You should be able to send and receive several UDP packets. It’s also likely
     that just by doing nothing (except capturing packets via Wireshark) that
     some UDP packets sent by others will appear in your trace.
  ●​ Now stop the packet capture.
  ●​ Set your packet filter so that Wireshark only displays the UDP packets sent
     and received at your host.


 Answer the following
  1.​ How many UDP packets were captured during your session? Were they
     mostly sent or received by your host? (Try using the “Statistics” options).
  2.​ Did you notice any UDP traffic that was not related to accessing the
     www.utec.edu.pe website? If so, what could be the source of that traffic?
  3.​ Pick a UDP packet from your host and describe its main fields (e.g., source
     port, destination port, length, checksum).
  4.​ Is the UDP checksum marked as verified or unverified? What does this
     indicate in the context of your operating system and network interface?
  5.​ Compare UDP with TCP based on what you observed in Wireshark. What are
     the key differences in terms of packet structure and reliability?
  6.​ What are the potential risks or vulnerabilities of using UDP in a network? Did
     you observe any unusual or potentially malicious UDP traffic?
  7.​ (Report) How could an administrator use Wireshark to detect suspicious UDP
     behavior, such as a port scan or DDoS attempt?
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-14


                           Checkpoint 1

2. Using nslookup
 ●​ Now let’s try the UDP sending segments using nslookup. Specifically, the
    nslookup command invokes the underlying DNS protocol, which in turn will
    send UDP segments from/to the host issuing the nslookup.
 ●​ Start capturing packets in Wireshark
 ●​ Now through a terminal enter the nslookup command.
 ●​ Now search for the domain:
                                 www.cisco.com
 ●​ Now stop the packet capture. We don’t need to go into any more details
    about nslookup or DNS now, as we’re just interested in getting a few UDP
    segments into Wireshark.
 ●​ Set your packet filter so that Wireshark only displays the UDP packets sent
    and received at your host.


 2.1. Answer
 1.​ How many UDP packets were captured during the nslookup www.cisco.com
    query? Were they sent, received, or both?
 2.​ Why does the nslookup command generate UDP traffic? Which network
    service relies on UDP in this context?
 3.​ What are the source and destination port numbers of the captured DNS
    packets? What does this indicate about how DNS communication works?
 4.​ Describe the typical UDP length for the DNS request and response observed.
    Are the packet sizes similar or different? Why might that be?
 5.​ Was the DNS query resolved successfully? How can you tell this by analyzing
    the UDP response in Wireshark?
 6.​ Why is DNS usually implemented over UDP instead of TCP? Based on your
    observations, what advantages does UDP offer in this case?
 7.​ Expand the UDP layer of a selected DNS packet. What are the values of the
    source port, destination port, length, and checksum? Provide a brief
    explanation of each field.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-14

 8.​ What is the maximum number of bytes that can be included in a UDP
    payload? (Research and present in the lab session).
 9.​ What is the largest possible source port number? (Research and present in
    the lab session).
 10.​What is the protocol number for UDP? Give your answer in both hexadecimal
    and decimal notation. To answer this question, you’ll need to look into the
    Protocol field of the IP datagram containing this UDP segment.
 11.​ Examine a pair of UDP packets in which your host sends the first UDP packet
    and the second UDP packet is a reply to this first UDP packet. Describe the
    relationship between the port numbers in the two packets.
                          Checkpoint 2
