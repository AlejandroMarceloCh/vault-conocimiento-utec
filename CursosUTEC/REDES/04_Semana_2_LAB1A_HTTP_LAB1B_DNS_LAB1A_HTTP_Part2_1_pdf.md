---
curso: REDES
titulo: 04 - Semana 2 _  LAB1A_HTTP + LAB1B_DNS/LAB1A_HTTP_Part2-1
slides: 3
fuente: 04 - Semana 2 _  LAB1A_HTTP + LAB1B_DNS/LAB1A_HTTP_Part2-1.pdf
---

garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-31




                                    LAB1A - HTTP​
                                       Part 2


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
 2026-03-31


4. HTML Documents with Embedded Objects
 Now we can look at what happens when your browser downloads a file with embedded
objects, i.e., a file that includes other objects (in the example below, image files) that are
stored on another server(s).


  4.1. Instructions:
   ●​ Start up your web browser, and make sure your browser’s cache is cleared, as
      discussed above.
   ●​ Start up the Wireshark packet sniffer
   ●​ Enter         the         following     URL         into       your        browser
      http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html
   ●​ Your browser should display a short HTML file with two images. These two images
      are referenced in the base HTML file. That is, the images themselves are not
      contained in the HTML; instead the URLs for the images are contained in the
      downloaded HTML file. As discussed in the textbook, your browser will have to
      retrieve these logos from the indicated web sites. Kurose’s book publisher’s logo is
      retrieved from the gaia.cs.umass.edu web site. The image of the 8th edition cover
      is stored at a server in France.
   ●​ Stop Wireshark packet capture, and enter “http” in the display-filter-specification
      window, so that only captured HTTP messages will be displayed.


  4.2. Answer the following questions:
   1.​ How many HTTP GET request messages did your browser send? To which Internet
       addresses were these GET requests sent?
   2.​ Can you tell whether your browser downloaded the two images serially, or whether
       they were downloaded from the two websites in parallel? Explain.

                           - Checkpoint 04 -
5. HTTP Authentication
Finally, let’s try visiting a web site that is password-protected and examine the sequence
of     HTTP         message      exchanged        for    such     a    site.   The    URL
http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html is
password protected. The username is “wireshark-students” (without the quotes), and the
password is “network” (again, without the quotes). So let’s access this “secure”
password-protected site.


  5.1. Instructions:
   ●​ Make sure your browser’s cache is cleared, as discussed above, and close down
      your browser. Then, start up your browser
   ●​ Start up the Wireshark packet sniffer
   ●​ Enter        the       following       URL       into      your       browser
      http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark
garias@utec.edu.pe
CS4055: Networks and communications
 2026-03-31

      file5.html
   ●​ Type the requested user name and password into the pop up box.
   ●​ Stop Wireshark packet capture, and enter “http” in the display-filter-specification
      window, so that only captured HTTP messages will be displayed later in the
      packet-listing window.


  5.2. Answer the following questions:
   1.​ What is the server’s response (status code and phrase) in response to the initial
       HTTP GET message from your browser?
   2.​ When your browser’s sends the HTTP GET message for the second time, what new
       field is included in the HTTP GET message?
   3.​ What’s        the      content       of  this    field?     Now      go       to
       http://www.motobit.com/util/base64-decoder-encoder.asp and paste the content
       (without the “basic ”) of the field.
   4.​ Is the information above encrypted or encoded?

                          - Checkpoint 05 -
6. For the report
Do some research on the following HTTP protocols:
   ●​ HTTP/2
   ●​ HTTP/3
   ●​ HTTP/Secure
