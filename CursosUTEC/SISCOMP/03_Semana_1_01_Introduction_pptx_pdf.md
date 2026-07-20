---
curso: SISCOMP
titulo: 03 - Semana 1/01.Introduction.pptx
slides: 22
fuente: 03 - Semana 1/01.Introduction.pptx.pdf
---

COMPUTER SYSTEMS

      MOTIVATION
Goals

Analyze the principal concepts of the course and the
               historical perspective.
Summary

1.   Course motivation
                         4.   Trends




2.   Performance
                         5.   Challenges




3.   History
                         6.   Conclusions
1.
     Course Motivation
Why we study Computer Systems?


- Have an idea of how computers work.

- Be familiar with system programming.

- Better understand performance and system tools.
2.
 Performance
             Let’s look at an example
                   Feature                              Speciﬁcation
 Model                                   MacBook Pro 9,1

 Processor                               Quad-Core Intel Core i7

 Processor Speed                         2,3 GHz

 Number of processors                    1

 Number of cores                         4

 Floating - point Operations per Cycle   4

 L2 Cache (per core)                     256 KB

 L3 Cache                                6 MB

 Hyper - Threading Technology            Enables

 Memory                                  8 GB




Best effort mode: 2.3 G * 1 * 4 * 4 = 36 800 MFLOPS
                   Best effort is also call performance
                                                         What performance is:

                                                         Efﬁciency with a computer system
                                                         performs a task




                                                                                Programming
Algorithm
Is the ﬁrst step.
                                                                                Language, compiler and architecture.
Determines both source-level statements
                                                                                Determines the number of computer
and I/O operations need to be executed
                                                                                instructions for each source-level




                                                                                       I/O System
                    Processor and memory system

                                                                                       I/O operations are bottlenecks.
                    How fast instructions can be
                                                                                       How fast I/O operations can be
                    executed improves the performance.
                                                                                       executed improves the performance
3.
     History
                 0th generation: Mechanics


● Designed by Charles Babbage (1834).

● Mechanical gears: Discrete values.

● Programs: Punched cards.

● Technological restrictions.




                                        https://www.computerhistory.org/babbage/
1st generation: Vacuum tubes



             ● 1945: ENIAC, Colossus.

             ● Machine language.

             ● Punched cards, boards and wires.

             ● Store concept.



                                https://www.computerhistory.org/babbage/
                  2nd generation: Transistors


● 1955: IBM 7094 (mainframes).

● Assembly language and FORTRAN.

● I/O separated from calculations.

● Punched cards and magnetic tape.

● Loaders (OS ancestors)
3rd generation: Integrated Circuits


                  ● 1965: IBM 360 (Instruction set architecture).

                  ● First Operating Systems (OS/360 MULTICS).

                  ● Multiprogramming.

                  ● Programming languages and compilers
                    (BASIC, C).
                  ●
                 4th generation: VLSI and PCs

● 1980: Personal Computers (Apple, IBM).

● Architectures: x86-64, ARM, MIPS, PowerPC,
  SPARC, RISC-V.

● Operating Systems: UNIX, MINIX, Linux,
  MacOS, DOS, Windows.

● ISA (CISC, RISC): Cache, pipeline, SIMD,
  hyperthreading, multicore.
4.
 Trends
                                Some trends
                                                   Memory Capacity

Scaling on electronics continues to evolve:

● Increased capacity and performance.
● Reduced cost.

      Moore’s law says:
                                              Limited by power consumption.
 Number of transistors on a computer chip
    doubles every year (since 1965).
                                                  Slow down since 2010.
Some performance graphics
5.
 Challenges
                                What we can do now?
1. No more single core performance improvement

 ● More powerful microprocessor might not help.

2. Memory - efﬁcient programming

 ● Temporal and spatial locality.

3. Parallelism

 ● Data - level, thread - level, request - level to improve performance.

4. Application
                                Conclusions


To create software that works efﬁciently with big data, it
    is necessary to understand how the hardware is
   organized and managed by an operating system.

● Computer architecture.

● Assembly language.

● Operating systems.

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
Questions?
  PhD. (C) Luz Adanaqué

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
