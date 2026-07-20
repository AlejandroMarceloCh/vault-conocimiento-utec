---
curso: REDES
titulo: 03 - Semana 1 _ Introducción + LAB1A_HTTP/L0_WiresharkInstallation
slides: 12
fuente: 03 - Semana 1 _ Introducción + LAB1A_HTTP/L0_WiresharkInstallation.pdf
---

garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24


                  LAB 0 - Wireshark Introduction

1. What is Wireshark?
Wireshark is a powerful open-source network protocol analyzer used to capture and
inspect data packets traveling over a network in real time. It allows users to analyze
network traffic, identify performance issues, and detect security threats.




2. What is Wireshark Used For?
Wireshark is commonly used for:
   ●​ Network troubleshooting
   ●​ Security analysis
   ●​ Protocol development
   ●​ Educational purposes (learning how networks function)
   ●​ Packet-level network analysis


3. How to Install Wireshark

3.1. Windows:

   1.​ Download Wireshark from the official website:

                          https://www.wireshark.org/download.html
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24




  2.​ Run the installer and follow the on-screen instructions.
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24




  3.​ During installation, select "WinPcap" or "Npcap" (recommended for Windows
      10+).




(Note: If Wireshark is already installed, the installer may prompt you to update or skip
                                 certain components)
  4.​ Restart your computer if required.


3.2. macOS:

  1.​ Download the macOS installer from the Wireshark website.
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24


   2.​ Open the .dmg file and drag Wireshark into the Applications folder.
   3.​ Install "ChmodBPF" to allow packet capturing without root permissions.


3.3. Linux (Ubuntu/Debian-based):

                                 sudo apt update
                          sudo apt install wireshark


3.4. Linux (Fedora-based):

                          sudo dnf install wireshark


To run Wireshark as a non-root user:
                    sudo usermod -aG wireshark $(whoami)
Then log out and log back in.


4. Simple Packet Sniffing Exercise
Capture and analyze live network traffic to understand packet structures.


4.1. Launch Wireshark

          ○​ Open Wireshark from the Start Menu or terminal.
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24


         ○​ Select a network interface (e.g., Wi-Fi or Ethernet) to capture packets.




         ○​ Click the "Start" button (shark fin icon) to begin capturing.




The Wireshark main window consists of five primary components:
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24


  a.​ The command menus are standard pulldown menus at the top of the Wireshark
     window (on a Mac, they also appear at the top of the screen). The most
     relevant menus are File and Capture. The File menu allows users to save
     captured packet data, open previously captured files, and exit Wireshark. The
     Capture menu is used to start packet capture.
  b.​ The packet-listing window provides a one-line summary of each captured
     packet, including the packet number (assigned by Wireshark, not by any
     protocol), capture time, source and destination IP addresses, upper-layer
     protocol type, and protocol-specific details. Clicking on a column name sorts
     the listing by that category. The protocol type field indicates the highest-level
     protocol responsible for sending or receiving the packet.
  c.​ The packet-header details window displays detailed information about the
     selected packet. Users can select a packet by clicking on its summary in the
     packet-listing window. This section includes Ethernet frame details (if
     applicable), IP datagram information, and, if the packet was transmitted over
     TCP or UDP, corresponding protocol details. Users can expand or collapse
     these details using plus/minus boxes or small arrows.
  d.​ The packet-contents window shows the full contents of the captured frame in
     both ASCII and hexadecimal format.
  e.​ At the top of the Wireshark interface, the packet display filter field allows users
     to enter a protocol name or other criteria to filter displayed packets. In the
     following example, we will use this field to hide non-HTTP packets.


4.2. Generate Network Traffic

         ○​ Open a web browser and visit a website like

                                      http://example.com/


                                      http://httpbin.org/

         ○​ Observe the packets appearing in Wireshark in real time.
         ○​ Click the red stop button to halt packet capture.
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24




4.3. Filter Packets

         ○​ Use the display filter bar at the top and type http to view only HTTP
            traffic.
         ○​ Alternatively, use icmp to view ping requests or udp to view user
            datagram protocol messages.
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24


4.4. Analyze Packets

         ○​ Click on a packet to see detailed information.
         ○​ Expand different protocol layers (Ethernet, IP, TCP/UDP, etc.).




         ○​ Look at the source and destination IP addresses.




5. Exercise: Exploring Wireshark's Interface
  1.​ Open Wireshark and start a packet capture on an active network interface.
  2.​ Let the capture run for 30 seconds, then stop it.
  3.​ Identify the following elements:
         ○​ The total number of captured packets (found at the bottom of the
            window).
         ○​ The different colors Wireshark uses in the packet list.
         ○​ The IP address of at least one source and one destination.
         ○​ The highest packet length recorded in the capture.
  4.​ Save the capture file as Test_CS4054_262.pcapng.
  5.​ Open the Statistics menu and navigate to Packet Lengths. What do you
     observe?
  6.​ Close Wireshark when finished.



                                         Done.
                       You are ready go through all the course
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24


6. First Experience
The best way to understand new software is by using it. This guide walks through the
process of capturing and analyzing network packets using Wireshark.


6.1. Starting Wireshark

Begin by opening your preferred web browser and launching Wireshark. Initially,
Wireshark will be idle, not capturing any packets.


6.2. Selecting a Network Interface

To start packet capture, open the Capture menu and select Interfaces (on Windows) or
Options (on Mac). This displays a list of available network interfaces, showing the
number of packets observed so far.


6.3. Beginning Packet Capture

On Windows, click Start next to the interface you wish to monitor. On Mac, select the
interface and press Start at the bottom of the window. Wireshark will now begin
capturing all incoming and outgoing packets on that interface.


6.4. Generating Network Traffic

               With Wireshark running, open your web browser and visit:​
         http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html
Your browser will initiate communication with the HTTP server, exchanging messages
to download the page. Wireshark captures these HTTP exchanges within Ethernet or
WiFi frames.


6.5. Stopping the Capture and Viewing Results

After the page loads, stop the capture by selecting Stop in Wireshark. The main
window will now display recorded packets, including HTTP messages exchanged with
the web server, along with other protocol traffic. This reveals background network
activity beyond just the requested webpage.
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24


6.6. Filtering HTTP Packets

Figure 1. looking at the details of the HTTP message that contained a GET
of http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html                    ...
To isolate HTTP traffic, type "http" in the display filter bar and press Enter. This filters
the packet list to show only HTTP messages (Figure 1). The detailed view allows
analysis at different protocol levels, from Ethernet frames to HTTP messages.
This hands-on exercise demonstrates how Wireshark captures and displays network
communication, helping users understand underlying internet protocols.




     Figure 1. looking at the details of the HTTP message that contained a GET of
          http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html


                           – Checkpoint 01 –




6.7. Find the HTTP GET message

Find the HTTP GET message that was sent from your computer to the
gaia.cs.umass.edu HTTP server. (Look for an HTTP GET message in the “listing of
captured packets” portion of the Wireshark window that shows “GET” followed by the
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24


gaia.cs.umass.edu URL that you entered. When you select the HTTP GET message,
the Ethernet frame, IP datagram, TCP segment, and HTTP message header
information will be displayed in the packet-header window . By clicking on ‘+’ and ‘-'
and right-pointing and down-pointing arrowheads to the left side of the packet details
window, minimize the amount of Frame, Ethernet, Internet Protocol, and Transmission
Control Protocol information displayed. Maximize the amount information displayed
about the HTTP protocol. Your Wireshark display should now look roughly as shown in
Figure 1. (Note, in particular, the minimized amount of protocol information for all
protocols except HTTP, and the maximized amount of protocol information for HTTP in
the packet-header window).


7. Answer the following
   1.​ Which of the following protocols are shown as appearing (i.e., are listed in the
       Wireshark “protocol” column) in your trace file: TCP, QUIC, HTTP, DNS, UDP,
       TLSv1.2?
   2.​ How long did it take from when the HTTP GET message was sent until the
       HTTP OK reply was received? (By default, the value of the Time column in the
       packet-listing window is the amount of time, in seconds, since Wireshark
       tracing began. (If you want to display the Time field in time-of-day format,
       select the Wireshark View pull down menu, then select Time Display Format,
       then select Time-of-day.)
   3.​ What is the Internet address of the gaia.cs.umass.edu (also known as
       www-net.cs.umass.edu)? What is the Internet address of your computer or (if
       you are using the trace file) the computer that sent the HTTP GET message?

To answer the following two questions, you’ll need to select the TCP packet containing
the HTTP GET request (hint: this is packet number 286 in Figure 1). The purpose of
these next two questions is to familiarize you with using Wireshark’s “Details of
selected packet window”.      To do this, click on Packet 286.    To answer the first
question below, then look in the “Details of selected packet” window toggle the
triangle for HTTP (your screen should then look similar to Figure 1); for the second
question below, you’ll need to expand the information on the Transmission Control
Protocol (TCP) part of this packet.
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-24


  4.​ Expand the information on the HTTP message in the Wireshark “Details of
     selected packet” window so you can see the fields in the HTTP GET request
     message. What type of Web browser issued the HTTP request? The answer is
     shown at the right end of the information following the “User-Agent:” field in the
     expanded HTTP message display. [This field value in the HTTP message is how
     a web server learns what type of browser you are using.]

                ·   Firefox, Safari, Microsoft Internet Edge, Other

  5.​ Expand the information on the Transmission Control Protocol for this packet in
     the Wireshark “Details of selected packet” window (see Figure 3 in the lab
     writeup) so you can see the fields in the TCP segment carrying the HTTP
     message. What is the destination port number (the number following “Dest
     Port:” for the TCP segment containing the HTTP request) to which this HTTP
     request is being sent?
  6.​ Print the two HTTP messages (GET and OK) referred to in question 2 above. To
     do so, select Print from the Wireshark File command menu, and select the
     “Selected Packet Only” and “Print as displayed” radial buttons, and then click
     OK.


                        – Checkpoint 02 –

                                        Done.
           Show the results to the instructor on a docs or markdown file.
