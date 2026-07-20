---
curso: REDES
titulo: 17 - Semana 15/Sem15_Experience_Ethernet_2
slides: 6
fuente: 17 - Semana 15/Sem15_Experience_Ethernet_2.pdf
---

{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications




                    Graded Experience​


                    Ethernet


                                          Guidelines
 ●​ Individual Evaluation: This graded experience and the hands-on checkpoint are strictly
    individual.
 ●​ Live Testing: The final cable functionality must be verified and demonstrated using the
    RJ45 network tester during the session.

                                Grading & Penalty Policy
 ●​ Base Score: The cable connection and implementation component has a base score of 2.0
    points.
 ●​ Crimping Penalties: A 0.25-point deduction will be applied for every poorly crimped,
    wrong color ordering or defective RJ45 connector.
        ○​ If a connector fails the test, you will be provided with a replacement to re-attempt
              the connection, but the penalty will still be deducted from the base score.
 {garias,cwilliams}@utec.edu.pe
 CS4055: Networks and communications



  Technical Guide: RJ45 Ethernet Cable Implementation
                                 (T568A Standard)

 1. Objective
 This guide provides the step-by-step procedure to correctly assemble, crimp, and test a
 Category 5e (Cat5e) Ethernet cable using the T568A wiring standard.

 2. Materials Required
   ●​ Cat5e Ethernet Cable: 1 meter.
   ●​ RJ45 Connectors: 2 units (plus spares if re-crimping is needed).
   ●​ Crimping Tool: For securing the RJ45 connectors onto the cable.
   ●​ Cable Stripper (On the Crimping Tool): For removing the cable's outer jacket.
   ●​ Scissors / Cable Cutter: For trimming the wires evenly.
   ●​ Network Cable Tester: To verify end-to-end connectivity.

 3. Step-by-Step Procedure

 3.1. Strip the Cable Jacket:
Use the cable stripper to remove approximately 1.5 inches (4 cm) of the outer insulation from each
end of the cable.
      Caution: Do not score or cut too deeply, or you will nick the copper wires inside.
 {garias,cwilliams}@utec.edu.pe
 CS4055: Networks and communications



 3.2. Separate the Wires:
   ●​ Inside the jacket, you will find 4 twisted pairs (8 wires total).
   ●​ Untwist the pairs completely and straighten each individual wire as much as possible using
       your fingers to make alignment easier.


 3.3. Arrange the Wires (T568A Standard)
Line up the 8 wires flat and side-by-side from left to right following the T568A standard color
sequence strictly:


            Pin Assignment                                     T568A Wire Color

                Position 1                                        White / Green

                Position 2                                            Green

                Position 3                                       White / Orange

                Position 4                                                Blue

                Position 5                                         White / Blue

                Position 6                                           Orange

                Position 7                                        White / Brown

                Position 8                                            Brown




                                                Pinout
 {garias,cwilliams}@utec.edu.pe
 CS4055: Networks and communications



 3.4. Trim the Wires
   ●​ Hold the sorted wires firmly between your thumb and forefinger.
   ●​ Use your cutter to trim the wires in a perfectly straight line, leaving exactly 0.5 inches (1.2
       cm) of exposed wire measured from the edge of the cable jacket.




Note: If the wires are left too long, the outer jacket will not sit inside the connector, failing
the strain-relief test.




 3.5. Insert the Wires into the RJ45 Connector
   ●​ Hold the RJ45 connector with the plastic clip facing DOWN (towards the floor) and the
       gold pins facing UP (towards you).
   ●​ Carefully slide the wires into the connector. Ensure that each wire enters its corresponding
       slot without crossing over others.
   ●​ Push firmly until all 8 copper ends are fully visible against the clear plastic window at the
       front of the connector. The outer cable jacket must sit well inside the back of the
       connector.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications




3.6. Crimp the RJ45 Connector
  ●​ Insert the prepared connector into the 8P slot of the crimping tool.
  ●​ Squeeze the handles of the tool completely and firmly. The tool will push the gold pins
     down into the wires and clamp the jacket wedge.
  ●​ Release the tool and gently pull the connector to ensure it is securely locked onto the
     cable.




3.7. Repeat for the Other End
Repeat steps on the opposite end of the cable, ensuring you use the exact same T568A color
sequence.
{garias,cwilliams}@utec.edu.pe
CS4055: Networks and communications



3.8. Test the Cable & Teacher Checkpoint
  ●​ Connect one end of your cable to the master unit of the cable tester and the other end to
     the remote unit.
  ●​ Turn on the tester. The LED lights must illuminate sequentially from 1 to 8 on both sides at
     the exact same time.
  ●​ Call the teacher to verify your live test and sign off on your individual checkpoint.




⚠️ Evaluation Reminder: This implementation component starts with a base score of 2.0
points. Every failed attempt or poorly crimped head that requires a replacement connector
will result in a 0.25-point deduction.



4. Troubleshooting
  ●​ LEDs out of order or flashing randomly: The wires were mixed up before insertion. Cut the
     connector off, realign carefully following the T568A table, and try again.
  ●​ One or more LEDs do not light up: A wire didn't reach the end of the connector or wasn't
     crimped hard enough. Cut the head off, ensure you push the wires all the way to the front
     next time, and crimp firmly.
  ●​ The cable jacket slips out of the connector: The wires were trimmed too long in Step 3.4.
     Cut the head off and ensure you leave only 0.5 inches (1.2 cm) of exposed wire before
     inserting.
