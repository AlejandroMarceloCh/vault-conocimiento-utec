---
curso: SISCOMP
titulo: 16 - Semana 14/14. Dynamic Memory Allocation
slides: 39
fuente: 16 - Semana 14/14. Dynamic Memory Allocation.pdf
---

COMPUTING SYSTEMS

    Dynamic Memory Allocation
    Professor: Luz A. Adanaqué
Motivation
User programs need to perform tasks securely.
Operating Systems has ﬁle management systems which
involves Directories and Descriptors.




Goals
Understand how Files, Directories and Descriptors are
managed in Operating Systems.
Summary

1.   Introduction




2.   Background




3.   System Calls
1.
     Dynamic Memory
     Allocation
Malloc Package
Malloc Example
Allocation Example
Constraints
Throughput
Peak Memory Utilization
2.
     Fragmentation
Internal Fragmentation
External Fragmentation
How much to free?
Keeping Track of free blocks
Method 1:
 Implicit
   List
Detailed Implicit Free List Example
Implicit List: Finding a free block

Allocating in free block
Freeing a block
Coalescing
Bidirectional Coalescing
Constant time coalescing
Constant time coalescing (case 1)
Constant time coalescing (case 2)
Constant time coalescing (case 3)
Constant time coalescing (case 4)
Boundary Tags
Key Allocator Policies
Implicit Lists
Method 2: Explicit free lists
Explicit free lists
Insertion Policy
Summary
Segregated List Allocators
Segregated List Allocators
Segregated List Allocators

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
