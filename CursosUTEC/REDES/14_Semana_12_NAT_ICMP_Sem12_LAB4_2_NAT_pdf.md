---
curso: REDES
titulo: 14 - Semana 12 _ NAT + ICMP/Sem12_LAB4_2_NAT
slides: 6
fuente: 14 - Semana 12 _ NAT + ICMP/Sem12_LAB4_2_NAT.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-09




                                       LAB4​
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
  2026-06-09

                                 LAB4B - NAT

 1. NAT Lab with Wireshark
 We’ll observe and understand how a router applies NAT (Network Address Translation) by
 translating private IP addresses to a public IP address when sending traffic to the
 Internet.


 1.1. Instructions
   ●​ On each laptop, check and write down your local IP addresses:
                                      ipconfig or ifconfig
   ●​ Open Wireshark on each laptop.
   ●​ Start capturing on the active Wi-Fi interface.
   ●​ In the terminal or browser, initiate a request:
                          Run ping 8.8.8.8 or visit http://example.com
   ●​ Observe the captured packets:
             ○​ Source IP: You’ll see the laptop's private IP address
             ○​ Destination IP: A public IP address.
  Note: You will not see the translated public IP yet, as Wireshark runs on the internal
 host.
Now let’s observe the public IP address.
   ●​ Visit: https://whatismyipaddress.com/
   ●​ Write down the public IP address displayed and screenshot the IP.
   ●​ Now repeat the public IP check on whatismyipaddress.com by using a mobile
         hotspot and screenshot the IP.
   ●​ Compare the new public IP with the previous one.
   ●​ Return to the original WiFi network that you were using.
   ●​ Do a ping to your public IP using the university’s network (screenshot the results).
   ●​ Repeat for the public IP using a mobile hotspot (screenshot the results).


 1.2. Answer:
   1.​ Show the screenshot of the results obtained both from the public IP address search
         and the ping to the IP addresses.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-09
  2.​ What is the difference between the source IP seen in Wireshark and the public IP
     shown on the website?
  3.​ Why   do   all   three   laptops show the same IP address when visiting
     whatismyipaddress.com?
  4.​ What role does the router play in making this possible?
  5.​ What would happen if a device from outside tried to initiate communication with
     one of the private IPs?
  6.​ If all devices show the same public IP, how does the router know how to send the
     response back to the correct device?
  7.​ What port numbers were used in your outbound traffic? Are they the same for each
     device? Why or why not?
  8.​ How can you determine from the captured packets that the request was sent using
     IPv4 and not IPv6?
  9.​ What transport-layer protocols (TCP, UDP, ICMP) are involved in the packets you
     captured?
  10.​Does NAT operate at the same OSI layer as IP addressing? Explain.
  11.​ Compare NAT’s behavior for ICMP (ping) and HTTP requests. Do you notice any
     differences in packet structure or translation?
  12.​(Report) Why is NAT not necessary in IPv6 networks?
  13.​(Report) If you had to design a secure home network, would you rely solely on NAT
     for protection? Justify your answer.
  14.​(Report) In what ways can NAT enhance or limit security? Does NAT count as a
     firewall? Why or why not?

                               Checkpoint 5
2. Real NAT application analysis
 In this lab, we’ll investigate the behavior of the NAT protocol. Because we’re interested
in capturing packets at both the input and output sides of the NAT device, we’ll need to
capture packets at two locations.
  For this part of the experience, we’ll capture packets from a simple web request from a
client PC in a home network to a www.google.com server.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-09




           Figure 1. Nat trace collection scenario for this laboratory experience.
 This file is called NAT_home_side. Because we are also interested in the packets being
sent by the NAT router into the ISP, we’ll collect a second trace file at a PC (not shown)
tapping into the link from the home router into the ISP network, as shown in Figure 1.
(The hub device shown on the ISP side of the router is used to tap into the link between
the NAT router and the first hop router in the ISP). Client-to-server packets captured by
Wireshark at this point will have undergone NAT translation. The Wireshark trace file
captured on the ISP side of the home router is called NAT_ISP_side.


2.1. NAT Home Side Trace Analysis

2.2. Instructions:
  ●​ Download the zip file Wireshark Traces and extract the files needed for this lab.
  ●​ Open the NAT_home_side file and answer the following questions.
  ●​ You might find it useful to use a Wireshark filter so that only frames containing
     HTTP messages are displayed from the trace file.


2.3. Answer:
  1.​ What is the IP address of the client?
        The client actually communicates with several different Google servers in order
      to implement “safe browsing.”The main Google server that will serve up the main
      Google web page has IP address 64.233.169.104. In order to display only those
      frames containing HTTP messages that are sent to/from this Google, server, enter
      the expression “http && ip.addr == 64.233.169.104” (without quotes) into the
      Filter: field in Wireshark .
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-09
 2.​ Consider now the HTTP GET sent from the client to the Google server at time
     7.109267. What are the source and destination IP addresses and TCP source and
     destination ports on the IP datagram carrying this HTTP GET?
 3.​ At what time is the corresponding 200 OK HTTP message received from the
     Google server?
 4.​ What are the source and destination IP addresses and TCP source and destination
     ports on the IP datagram carrying this HTTP 200 OK message?
 Recall that before a GET command can be sent to an HTTP server, TCP must first set up
a connection using the three-way SYN/ACK handshake.
 5.​ At what time is the client-to-server TCP SYN segment sent that sets up the
     connection used by the GET sent at time 7.109267?
 6.​ What are the source and destination IP addresses and source and destination ports
     for the TCP SYN segment?
 7.​ What are the source and destination IP addresses and source and destination ports
     of the ACK sent in response to the SYN. At what time is this ACK received at the
     client? (Note: to find these segments you will need to clear the Filter expression
     you entered above. If you enter the filter “tcp”, only TCP segments will be displayed
     by Wireshark).

                            Checkpoint 6
NAT ISP Side Trace Analysis

2.4. Instructions:
 ●​ Open the NAT_ISP_side file and answer the following questions.
 ●​ You might find it useful to use a Wireshark filter so that only frames containing
     HTTP messages are displayed from the trace file.


2.5. Answer:
 8.​ In the NAT_ISP_side trace file, find the HTTP GET message was sent from the client
     to the Google server at time 7.109267 (where t=7.109267 is time at which this was
     sent as recorded in the NAT_home_side trace file). At what time does this message
     appear in the NAT_ISP_side trace file? What are the source and destination IP
     addresses and TCP source and destination ports on the IP datagram carrying this
     HTTP GET (as recording in the NAT_ISP_side trace file)?
 9.​ Are any fields in the HTTP GET message changed? Which of the following fields in
     the IP datagram carrying the HTTP GET are changed: Version, Header Length,
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-06-09
    Flags, Checksum. If any of these fields have changed, give a reason (in one
    sentence) stating why this field needed to change.
 10.​In the NAT_ISP_side trace file, at what time is the first 200 OK HTTP message
    received from the Google server? What are the source and destination IP addresses
    and TCP source and destination ports on the IP datagram carrying this HTTP 200
    OK message?
 11.​ In the NAT_ISP_side trace file, at what time were the client-to-server TCP SYN
    segment and the server-to-client TCP ACK segment corresponding to the
    segments in question 7 above captured? What are the source and destination IP
    addresses and source and destination ports for these two segments?
 12.​Which of these fields are the same, and which are different than your answer to
    question 7 above?

                           Checkpoint 7
