---
curso: SISCOMP
titulo: 13 - Semana 11/P1_SC
slides: 14
fuente: 13 - Semana 11/P1_SC.pdf
---

COMPUTING SYSTEMS

           Final Project
    Professor: Luz A. Adanaqué
Goal
Implement a kernel to manage three processes related
to remote sensing on a satellite.
Summary

1.   Context




2.   OS Management




3.   Final presentation
                                 Project Tasks

1. Processes

Implement processes related to remote sensing of parameters, detection of out-of-range values, and
communication of received data.

2. Scheduler

Implement a scheduler capable of managing process priorities, ﬁrst in an imposed manner and then
automatically through syscalls.

3. OS Application

Integrate processes and the scheduler into an application hosted on an operating system, capable of
operating manually or automatically, taking into account best practices for control and access to
information.
1.
     Context
Satellite System
                                   Bright Area




1. Temperature sensor:

Sensing time: every 5 minutes
Transmission data time: 1 minute
                                                 Dark Area
2. LEO Orbit: 100 minutes:

Bright Area: 42 minutes
Dark Area: 58 minutes
                                                   Processes
Process 1:
Temperature signal acquisition process: enter data corresponding to the temperature, which ranges from 45°C to 105°C during a
LEO orbit, which lasts around 100 minutes (for testing purposes, this time can be shortened). Be sure to insert some data into
this process that generates anomalies in the temperature value to trigger the deployment of cooling techniques and their
subsequent restoration.

Process 2:
Process that deploys the cooling technique used whenever the reading from process 1 exceeds the 90°C, and it turn off when
the temperature is 60°C. This process must display warnings via alerts when it is activated and deactivated.

Process 3:
Process that displays the reading received from the sensor (with UART protocol), originating from process 1. This reception must
be based on a serial communication protocol.

Cada proceso debe ser desarrollado mediante la perspectiva de procesador y diseño de hardware en RISC - V,
                                               estableciendo trade-offs
  2.
         OS Management

El scheduler en el sistema operativo debe gestionar
los siguientes escenarios de manera rápida y con alta
performance.
                                                     1st Scenario: Baseline
In this scenario, all processes run sequentially, without any priority associated with their operation. The OS must be able to detect
which process is being performed through a request.




                    P1                          P1                  P1                     P1                    P1
                         OFF                         ON                  ON                     OFF                   OFF




   PROCESSES
                         P2                          P2                  P2                     P2                    P2



                               P3                         P3                  P3                      P3                    P3




                                                                                                                                       t (min)
                5                              10              42                                                                100


                               ZONA LUMINOSA                                              ZONA OSCURA
                                                                 2nd Scenario
In this scenario, an order of priorities is imposed, the scheduler must be able to switch between processes, and the OS must
indicate if there is any loss of information due to the abrupt change between non-consecutive processes.




                   P1                             P1                      P1                                   P1




   PROCESSES
                        P3                             P3                      P3                                   P3
                             OFF                            ON                      OFF                                  OFF


                             P2                             P2                      P2                                   P2




                                                                                                                                     t (min)
               5                             10                      42                                   95                   100


                             ZONA LUMINOSA                                                ZONA OSCURA
                                                                 3rd Scenario
    In this scenario, an order of priorities is imposed, the scheduler must be able to switch between processes, and the OS must
    indicate if there is any loss of information due to the abrupt change between non-consecutive processes.




                   P2                             P2                     P2                                    P2



PROCESSES
                        P1                             P1                     P1                                    P1



                             P3                             P3                     P3                                    P3


                                                                                                                                    t (min)
               5                             10                     42                                    95                  100


                             ZONA LUMINOSA                                               ZONA OSCURA
                                                     4th Scenario: Syscalls
In this scenario, the application runs automatically, i.e., data is transmitted continuously, respecting its times and ranges, then
a communication ﬂag is activated and syscalls are generated to switch to the other processes. The OS must be able to store
the value of the PC where the current process stopped and resume it when the system call is ﬁnished executing.




                P                         P
                                                           P1                      P1                      P1
                1                         1




  PROCESSES
                                                 P                   P                       P                        P
                                                 2                   2                       2                        2


                        P3                           P3                  P3                      P3                       P3




                                                                                                                                     t (min)
                    5        6                        10
                                                                                                                               100


                                 ZONA LUMINOSA                                             ZONA OSCURA
                                                         Handling Data
As one process is interrupted by other, is necessary to handle information about PC (and the stack) and the status execution of
the current process in order to continue the execution of the interrupted process.


                                                                PC    PC

              P                         P
                                                           P1                P1                     P1
              1                         1




PROCESSES
                                               P                 P                     P                      P
                                               2                 2                     2                      2


                      P3                           P3                P3                    P3                     P3




                                                                                                                             t (min)
                  5        6                        10
                                                                                                                       100


                               ZONA LUMINOSA                                         ZONA OSCURA
Reference Books
 Patterson, D. A., & Hennessy, J. L. (2020). Computer Organization and
 Design RISC-V Edition: The Hardware Software Interface. Morgan
 Kaufmann


 “The elements of computing systems: building a modern computer
 from ﬁrst principles” Nisan, N., & Schocken, S. (2021). MIT press



 Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). Operating system concepts
 (9th edition, international student version). John Wiley & Sons Inc.



 ”Digital Design and Computer Architecture, RISC-V Edition”. Morgan
 Kaufmann. Harris, S., & Harris, D. (2021).

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
