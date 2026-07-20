---
curso: REDES
titulo: 04 - Semana 2 _  LAB1A_HTTP + LAB1B_DNS/LAB1B_DNS_Part1
slides: 5
fuente: 04 - Semana 2 _  LAB1A_HTTP + LAB1B_DNS/LAB1B_DNS_Part1.pdf
---

  {garias,cwilliams}@utec.edu.pe
  CS4055: Networks and communications
   2026-04-01




                                LAB1B - DNS


The present evaluation will be received only if the checkpoints of all the questions in
the LABORATORY SESSION have been completed with the course teacher.
  I.​   The submission must consist of:
           A.​ Introduction (include introductory paragraph):
           B.​ Theoretical Framework (definitions with references).
           C.​ State of the Art (research papers, articles, theses, pages with references).
           D.​ Development of the experience (including discussion and correct figure
              formatting)
           E.​ Conclusions (at least one for each experience carried out).
           F.​ References (IEEE format)
 II.​   The submission must be presented in LaTeX or Docs format (pdf file).
III.​   Upload only the PDF of the report to Canvas, use a link to the repository, include
        step-by-step photos of each experience and answer checkpoints where relevant,
        plus codes if they have been developed.
IV.​    Only one member of the group will upload the report.
 V.​    Do not forget to list the names of all members.
 {garias,cwilliams}@utec.edu.pe
 CS4055: Networks and communications
  2026-04-01


                            LAB1 - DNS - Part I

1. Converting a URL to an IP address using DNS

1.1. Instructions
 ●​ Click the Windows Start button, type cmd in the search field and press Enter. The
    command prompt window will appear.
 ●​ At the command prompt, ping the Internet Corporation for Assigned Names and
    Numbers (ICANN) URL, www.icann.net. ICANN coordinates the functions of DNS, IP
    addressing, top-level management of the domain name system, and administration
    of the root server system. The PC must translate www.icann.net into an IP address
    to know where to send Internet Control Message Protocol (ICMP) packets. Use the
    command:
                             ping [theUrlOfTheWebsite]
 ●​ The first line of the output shows the domain name www.icann.net converted to an
    IP address by DNS. You should be able to see the effect of DNS, even if there is a
    firewall installed at the institution that prevents pings or even if the destination
    server has prevented you from pinging your Web server.


1.2. Answer
 1.​ What is the IP address of www.icann.net?
 2.​ Now ping
                              www.unsplash.com
 3.​ When you ping this address, do you get the same IP address as in the example or a
    different IP address? Why?
 4.​ Type the IP address you got when you pinged www.unsplash.com into a browser.
    Does the Web site show up? Why or why not? Investigate if necessary.
                              Checkpoint 1

2. Observing DNS lookup using the nslookup command on a Web
site

2.1. Instructions
 ●​ At the command prompt type the nslookup command. (Windows).
 {garias,cwilliams}@utec.edu.pe
 CS4055: Networks and communications
  2026-04-01

  ●​ What is the default DNS server being used?
  ●​ Note that the command prompt changed to the “greater than” (>) symbol. This is
     the nslookup input prompt. From here you can enter DNS related commands.
  ●​ In the input prompt, type “?” to see a list of all available commands that you can
     use in nslookup mode.
  ●​ In the nslookup input prompt, type www.unsplash.com.
  ●​ Note: For Linux users, the experience of using nslookup requires that the
     commands be inserted on a single line: “nslookup www.unsplash.com”.


2.2. Answer
  1.​ What is the DNS that you are using? Is it a Local? root? TLD? or authoritative? (For
     the report)
  2.​ What is the IP address(es) translated when you search www.unsplash.com
  3.​ Is it the same IP address that appears with the ping command?
  4.​ In the command prompt, type the IP address of the Unsplash Web server you just
     found. What result do you get?
  5.​ Now perform the same experience, but using the cisco.com site. Using the
     nslookup command, insert the IP address of the page. Does it differ from the
     previous result? Why? (Investigate if necessary to answer in the report).
  6.​ Now perform the same experiment, but using the www.cisco.com page. Does the
     resulting IP address change? Why? (Investigate if necessary to answer in the
     report).
  7.​ You can also use it to translate IP addresses to domain names. Using the nslookup
     tool, write down the IP addresses associated with www.google.com.
  8.​ Below the addresses, in addition to the IP address, you will see numbers separated
     by “double dots. What kind of address is this? (Investigate if necessary).
                                Checkpoint 2

3. Using ipconfig
ipconfig (for Windows) and ifconfig (for Linux/Unix) are among the most useful little
utilities in your host, especially for debugging network issues. Here we’ll only describe
ipconfig, although the Linux/Unix ifconfig is very similar. ipconfig can be used to show
your current TCP/IP information, including your address, DNS server addresses, adapter
type and so on. For example, if you all this information about your host simply by
entering
 {garias,cwilliams}@utec.edu.pe
 CS4055: Networks and communications
  2026-04-01


                                ipconfig \all
into the Command Prompt, as shown in the following screenshot.




ipconfig is also very useful for managing the DNS information stored in your host. In
Section 2.5 we learned that a host can cache DNS records it recently obtained. To see
these cached records, after the prompt C:\> provide the following command:
                               ipconfig /displaydns


3.1. Clearing DNS Cache
Most hosts (such as your personal computer) maintain a cache of recently retrieved DNS
records, just as many web browsers store a cache of objects retrieved via HTTP.​
 For this reason, and to continue with the activity, we will proceed to clear the DNS
records cache:
  ●​ On a Mac computer, you can enter the following command in a terminal window to
     clear your DNS resolution cache:
                       sudo killall -HUP mDNSResponder
  ●​ On a Windows computer, you can enter the following command in the command
     prompt:
                                ipconfig /flushdns
  ●​ On a Linux computer, enter:
                   sudo systemd-resolve --flush-caches
Flushing the DNS cache clears all entries and reloads the entries from the hosts file.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications
 2026-04-01


3.2. Answer
 ●​ What is the current IP address, subnet mask, and default gateway of your host?
    (Use ipconfig /all and interpret the output.)
 ●​ List the DNS servers configured on your host. Are they static or assigned via
    DHCP? (How can you tell?)
 ●​ What type of network adapter is used to connect to the internet? Wired, wireless, or
    virtual?
 ●​ Before flushing the DNS cache, what DNS entries are currently stored on your
    machine? (Use ipconfig /displaydns and summarize the results.)
 ●​ What happens when you run ipconfig /flushdns? How does it affect the DNS cache
    content?
                              Checkpoint 3
