---
curso: REDES
titulo: 03 - Semana 1 _ Introducción + LAB1A_HTTP/LAB1A_HTTP_Part1
slides: 5
fuente: 03 - Semana 1 _ Introducción + LAB1A_HTTP/LAB1A_HTTP_Part1.pdf
---

garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-25




                                    LAB1A - HTTP​
                                        Part 1


 The present evaluation will be received only if the checkpoints of all the
 questions in the LABORATORY SESSION have been completed with the course
 teacher.
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
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-25


1. The Basic HTTP GET/response interaction

  1.1. Instructions:
Do the following:
    1.​ Start up your web browser.
    2.​ Start up the Wireshark packet sniffer, but don’t yet begin packet capture. Enter “http”
        in the display-filter-specification window, so that only captured HTTP messages will
        be displayed later in the packet-listing window. (We’re only interested in the HTTP
        protocol here, and don’t want to see the clutter of all captured packets).
    3.​ Wait a bit more than one minute, and then begin Wireshark packet capture.
    4.​ Enter the following to your browser​
         http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html​
         Your browser should display the very simple, one-line HTML file.
Note. If you don't see any HTTP frames in your trace, check the URL in your browser and
                         make sure it doesn't include the 's' in 'https
    5.​ Stop Wireshark packet capture.

Your Wireshark window should look similar to the window shown in Figure 1.




Figure 1   Wireshark        Display      after    http://gaia.cs.umass.edu/wireshark-labs/
HTTP-wireshark-file1.html has been retrieved by your browser.

The example in Figure 1 shows in the packet-listing window that two HTTP messages were
captured: the GET message (from your browser to the gaia.cs.umass.edu web server) and the
response message from the server to your browser. The packet-contents window shows
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-25

details of the selected message (in this case the HTTP OK message, which is highlighted in
the packet-listing window). Recall that since the HTTP message was carried inside a TCP
segment, which was carried inside an IP datagram, which was carried within an Ethernet
frame, Wireshark displays the Frame, Ethernet, IP, and TCP packet information as well. We
want to minimize the amount of non-HTTP data displayed (we’re interested in HTTP here,
and will be investigating these other protocols is later labs), so make sure the boxes at the far
left of the Frame, Ethernet, IP and TCP information have a plus sign or a right-pointing
triangle (which means there is hidden, undisplayed information), and the HTTP line has a
minus sign or a down-pointing triangle (which means that all information about the HTTP
message is displayed).
(Note: You should ignore any HTTP GET and response for favicon.ico. If you see a reference
to this file, it is your browser automatically asking the server if it (the server) has a small icon
file that should be displayed next to the displayed URL in your browser. We’ll ignore
references to this pesky file in this lab.).


   1.2. Answer the following
By looking at the information in the HTTP GET and response messages, answer the following
questions. If you’re doing this lab as part of class, your teacher will provide details about how
to hand in assignments, whether written or in an LMS.[2]
     1.​ Is your browser running HTTP version 1.0, 1.1, or 2? What version of HTTP is the
         server running?
     2.​ Protocol Negotiation: Compare the HTTP versions in the request and response. Are
         they identical? Mention the versions found for both entities.
     3.​ What languages (if any) does your browser indicate that it can accept to the server?
     4.​ What is the IP address of your computer? What is the IP address of the
         gaia.cs.umass.edu server?
     5.​ What is the status code returned from the server to your browser?
     6.​ When was the HTML file that you are retrieving last modified at the server?
     7.​ Quantify the size of the HTML entity body returned by the server in bytes.
     8.​ Carefully re-examine the raw packet bytes. List a header that appears in the raw
         dump but might be overlooked in the high-level summary.
In your answer to question 5 above (assuming you’re running Wireshark “live”, as opposed to
using an earlier-recorded trace file), you might have been surprised to find that the
document you just retrieved was last modified within a minute before you downloaded the
document. That’s because (for this particular file), the gaia.cs.umass.edu server is setting the
file’s last-modified time to be the current time, and is doing so once per minute. Thus, if you
wait a minute between accesses, the file will appear to have been recently modified, and
hence your browser will download a “new” copy of the document.


                             – Checkpoint 01 –
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-25


2. The HTTP CONDITIONAL GET/response interaction
 Before performing the steps below, make sure your browser’s cache is empty. Now do the
following:


  2.1. Instructions:
   ●​ Start up your web browser, and make sure your browser’s cache is cleared, as
      discussed above. (If it’s necessary, see this link for instructions on clearing your
      browser cache.)
   ●​ Start up the Wireshark packet sniffer
   ●​ Enter         the        following        URL     into        your     browser
      http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html Your browser
      should display a very simple five-line HTML file.
   ●​ Quickly enter the same URL into your browser again (or simply select the refresh
      button on your browser)
   ●​ Stop Wireshark packet capture, and enter “http” (again, in lower case without the
      quotation marks) in the display-filter-specification window, so that only captured
      HTTP messages will be displayed later in the packet-listing window.


  2.2. Answer the following questions:
   1.​ Inspect the contents of the first HTTP GET request from your browser to the
       server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?
   2.​ Inspect the contents of the server response. Did the server explicitly return the
       contents of the file? How can you tell?
   3.​ Now inspect the contents of the second HTTP GET request from your browser to
       the server. Do you see an “IF-MODIFIED-SINCE:” line in the HTTP GET3? If so, what
       information follows the “IF-MODIFIED-SINCE:” header?
   4.​ What is the HTTP status code and phrase returned from the server in response to
       this second HTTP GET? Did the server explicitly return the contents of the file?
       Explain.

                         - Checkpoint 02 -
3. Retrieving Long Documents
 In our examples thus far, the documents retrieved have been simple and short HTML
 files. Let’s next see what happens when we download a long HTML file. Do the following:


  3.1. Instructions:
   ●​ Start up your web browser, and make sure your browser’s cache is cleared, as
      discussed above.
   ●​ Start up the Wireshark packet sniffer
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-25

   ●​ Enter        the        following        URL         into    your         browser
      http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html Your browser
      should display the rather lengthy US Bill of Rights.
   ●​ Stop Wireshark packet capture, and enter “http” in the display-filter-specification
      window, so that only captured HTTP messages will be displayed.
 In the packet-listing window, you should see your HTTP GET message, followed by a
multiple-packet TCP response to your HTTP GET request.


  3.2. Answer the following questions:
   1.​ How many HTTP GET request messages did your browser send?
   2.​ What is the status code and phrase in the response?
   3.​ How many data-containing TCP segments were needed to carry the single HTTP
       response and the text of the Bill of Rights?

                          - Checkpoint 03 -
