---
curso: SISCOMP
titulo: 08 - Semana 6/06. Memory Cache
slides: 25
fuente: 08 - Semana 6/06. Memory Cache.pdf
---

COMPUTING SYSTEMS

     Memory & Cache
Goals

Learn about how computers store information, and the
different memory levels are used to improve
performance
Summary

1.   Memory Hierarchy




2.   Cache Locality




3.   ….
1.
     Memory Hierarchy
                    RISC-V Pseudoinstructions


● Not part of the instruction set (cannot be directly converted to machine code).

● They are useful to programmers and compilers.

● Their intended goal CAN be achieved with one or more “real” instructions.

● They are converted into CPU compatible instructions during assembly.


          Pseudoinstructions are useful when coding, but the CPU
                ends up executing something different☺
Computer performance
depends on:
• Processor performance
• Memory system performance
           Memory Hierarchy




Capacity
             Memory Hierarchy




Capacity




           Fast Memory is Expensive
           Cheap Memory is Slow
    Locality Principles
9

    Exploit locality to make memory accesses fast

    1. Temporal Locality:
       • Locality in time
       • If data used recently, likely to use it again soon
       • How to exploit: keep recently accessed data in higher levels of memory
         hierarchy

    2. Spatial Locality:
       • Locality in space
       • If data used recently, likely to use nearby data soon
       • How to exploit: when access data, bring nearby data into higher levels of
         memory hierarchy too
      Memory Performance
• Hit: data found in that level of memory hierarchy
• Miss: data not found (must go to next level)
  Hit Rate          = # hits / # memory accesses
           = 1 – Miss Rate
  Miss Rate         = # misses / # memory accesses
           = 1 – Hit Rate
• Average memory access time (AMAT): average time for
  processor to access data
  AMAT = tcache + MRcache[tMM + MRMM(tVM)]
       Example: Performance
• A program has 2,000 loads and stores
• 1,250 of these data values in cache
• Rest supplied by other levels of memory hierarchy
• Suppose processor has 2 levels of hierarchy: cache and
  main memory: tcache = 1 cycle, tMM = 100 cycles
• What are the hit and miss rates for the cache?
• What is the AMAT?
Hit Rate = 1250/2000 = 0.625
Miss Rate = 750/2000 = 0.375 = 1 – Hit Rate
       Example: Performance
• A program has 2,000 loads and stores
• 1,250 of these data values in cache
• Rest supplied by other levels of memory hierarchy
• Suppose processor has 2 levels of hierarchy: cache and main
  memory: tcache = 1 cycle, tMM = 100 cycles
• What are the hit and miss rates for the cache?
• What is the AMAT?

                                              AMAT =              tcache       +
Hit Rate = 1250/2000 = 0.625                    MRcache(tMM)
Miss Rate = 750/2000 = 0.375 = 1 – Hit Rate              =   [1   +   0.375(100)]
                                                cycles
                                                         = 38.5 cycles
2.
     Cache Organization
     What data is held in the cache?
14

     • Ideally, cache anticipates needed data and puts it in cache
     • But impossible to predict future

     • Recall: Use past to predict future: temporal and spatial locality
        • Temporal locality: copy newly accessed data into cache
        • Spatial locality: copy neighboring data into cache too
Cache Terminology
• Capacity (C):
15 • number of data bytes in cache
• Block size (b) (a.k.a. line size):
   • bytes of data brought into cache at once
• Number of blocks (B = C/b):
   • number of blocks in cache: B = C/b
• Degree of associativity (N):
   • number of blocks in a set
• Number of sets (S = B/N):
   • each memory address maps to exactly one cache set
      Cache Overview
  • Example:
  16
  • Multi-level:
      • Level 1 cache (64KB)
      • Level 2 cache (256KB)
      • Level 3 cache (>10MB)
  • Block size: 64B
  • High associativity.

Note: For educational purposes, we analyze
a system with only 1 level cache and a few-
Bytes of line size.
     Cache Organization: How is data found?
17

     • Cache organized into S sets
     • Each memory address maps to exactly one set
     • Caches categorized by # of blocks in a set:
        1. Direct mapped: 1 block per set
        2. N-way set associative: N blocks per set
        3. Fully associative: all cache blocks in 1 set

     • Example: Examine each organization for a (small) cache with:
        • Capacity (C = 8 words)
        • Block size (b = 1 word)
        • So, number of blocks (B = 8)
Direct Mapped Cache

18
Direct Mapped Cache Performance

19
     RISC-V Assembly Code
         li x1, 5
         li x2, 0
     LOOP:
         beq x1, x0, DONE

         lw x2, 4(x1)
         lw x3, 12(x1)
         lw x4, 8(x1)        Miss Rate = 3/15
                                    = 20%
         addi x1,x1,-1
         j   LOOP           Temporal Locality
     DONE:
                            Compulsory Misses
N-Way Set Associative Cache

20

     N-Way Set Associative Performance
21

     RISC-V Assembly Code
        li      x1, 5
                               Miss Rate = 2/10
        li      x2, 0                 = 20%

     LOOP:                     Associativity reduces
         beq    x1, x0, DONE   conflict misses
         lw     x3, 4(x2)
         lw     x4, 36(x2)
         addi   x1, x1, -1
         j      LOOP

     DONE:
     Full Associativity
22
     • Fully associative cache
        • A block can be placed in any cache location

              Tag
              store
                          =?     =?     =?     =?           =?    =?             =?   =?

                                                    Logic

                                                        Hit?


             Data store

                                                 MUX
                                                                 byte in block
                                                 MUX
Fully Associative Cache

23




                Reduces conflict misses
                Expensive to build
Reference Books
 Patterson, D. A., & Hennessy, J. L. (2020). Computer Organization and
 Design RISC-V Edition: The Hardware Software Interface. Morgan
 Kaufmann


 “The elements of computing systems: building a modern computer from
 first principles” Nisan, N., & Schocken, S. (2021). MIT press



 Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). Operating system concepts
 (9th edition, international student version). John Wiley & Sons Inc.



 ”Digital Design and Computer Architecture, RISC-V Edition”. Morgan
 Kaufmann. Harris, S., & Harris, D. (2021).
Questions?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
