---
curso: SISCOMP
titulo: 16 - Semana 14/S14_ Dynamic Memory Allocation
slides: 16
fuente: 16 - Semana 14/S14_ Dynamic Memory Allocation.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
November 20th, 2025

                       S14: Dynamic Memory Allocation
Código base:

   ●​ Un asignador con lista implícita
   ●​ Un asignador con lista explícita
   ●​ Un driver que genera solicitudes de malloc/free
   ●​ Una interfaz común (allocator.h)


Part 1: Heap Size
Analice el tamaño del heap generado y verifique si el heap crece o decrece

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    printf("Heap start: %p\n", sbrk(0));
    int *a = malloc(sizeof(int) * 100);
    printf("After malloc: %p\n", sbrk(0));
    free(a);
    printf("After free : %p\n", sbrk(0));
    return 0;
}


Part 2: Allocator with implicit list
2.1 Diseñe el siguiente bloque:

+------------+----------------------+
| header     | payload              |
| (size + A) | (data for the user) |
+------------+----------------------+


2.2 Implementar find_fit() con first-fit

block_header* find_fit(size_t size) {
    block_header* curr = heap_start;
    while (curr != NULL) {
        if (!curr->allocated && curr->size >= size) {
            return curr;
        }
        curr = next_block(curr);
    }
    return NULL;
}
2.3 Dividir y combinar bloques, implementar las siguientes funciones:

   ●​ split_block()
   ●​ coalesce()

2.4 Evalúe fragmentación, el driver ejecuta secuencias como:

malloc(100)
malloc(200)
free(ptr1)
malloc(50)

Calcule:

   ●​ Fragmentación interna = (tamaño real – tamaño solicitado)
   ●​ Fragmentación externa = bloques libres pequeños no utilizables

Part 3: Allocator with explicit list

3.1 Agregar una free list

header | prev | next | payload

3.2 Insertar y remover bloques de la free list

   ●​ Insertar al inicio
   ●​ Remover un bloque en O(1)
   ●​ Ajustes al hacer split y coalesce

3.3 Comparar rendimiento listas implícitas vs explícitas

El driver mide:

   ●​ Cantidad de iteraciones para encontrar un bloque
   ●​ Tiempo de ejecución
   ●​ Fragmentación generada

Estructura:

/allocator/
│── allocator.h
│── memory_driver.c
│── implicit_allocator.c
│── explicit_allocator.c
│── utils.h
│── utils.c
│── Makefile

──────────────────────────────────────────────────

// allocator.h
#ifndef ALLOCATOR_H
#define ALLOCATOR_H

#include <stddef.h>

// Inicializa el heap simulado con tamaño 'heap_size' bytes
void allocator_init(size_t heap_size);

// Libera recursos
void allocator_destroy(void);

// Asignador (implementaciones mm_*)
void* mm_malloc(size_t size);
void mm_free(void* ptr);
void* mm_realloc(void* ptr, size_t size);

// Imprime estadísticas del asignador
void allocator_stats(void);

#endif // ALLOCATOR_H
──────────────────────────────────────────────────

// utils.h
#ifndef UTILS_H
#define UTILS_H

#include <stddef.h>

#define ALIGNMENT 8

// Alinea a múltiplos de ALIGNMENT
size_t align(size_t size);

// Mensaje de fallo (termina el programa)
void fail(const char *msg);

#endif // UTILS_H
──────────────────────────────────────────────────

// utils.c
#include "utils.h"
#include <stdlib.h>
#include <stdio.h>

size_t align(size_t size) {
    return (size + (ALIGNMENT - 1)) & ~(ALIGNMENT - 1);
}

void fail(const char *msg) {
    fprintf(stderr, "ERROR: %s\n", msg);
    exit(EXIT_FAILURE);
}

──────────────────────────────────────────────────
// implicit_allocator.c
#include "allocator.h"
#include "utils.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdint.h>

// Header de bloque: tamaño total del bloque (incluye header)
y flag allocated.
// Usamos campo 'size' (size_t) y un 'allocated' (int) por
claridad didáctica.
typedef struct {
    size_t size;    // tamaño total del bloque: header +
payload (+padding)
    int allocated; // 0 libre, 1 ocupado
} header_t;

static uint8_t *heap = NULL;
static size_t heap_size = 0;

static header_t* heap_start(void) {
    if (!heap) return NULL;
    return (header_t*)heap;
}

// Devuelve puntero al next block o NULL si se sale del heap
static header_t* next_block(header_t *h) {
    if (!h) return NULL;
    uint8_t *next = (uint8_t*)h + h->size;
    if (next >= heap + heap_size) return NULL;
    return (header_t*)next;
}

// Buscar primer bloque libre con tamaño >= asize
static header_t* find_fit(size_t asize) {
    header_t *h = heap_start();
    while (h) {
        if (!h->allocated && h->size >= asize) return h;
        h = next_block(h);
    }
    return NULL;
}

static const size_t MIN_BLOCK = sizeof(header_t) + ALIGNMENT;
// mínimo para split

// Divide el bloque h para dejar un bloque de tamaño asize y
uno libre con el resto
static void split_block(header_t *h, size_t asize) {
    if (!h) return;
    if (h->size >= asize + MIN_BLOCK) {
        uint8_t *newpos = (uint8_t*)h + asize;
        header_t *newb = (header_t*)newpos;
        newb->size = h->size - asize;
        newb->allocated = 0;
        h->size = asize;
    }
}

// Coalescencia simple: recorre el heap y concatena bloques
libres contiguos
static void coalesce_all(void) {
    header_t *h = heap_start();
    while (h) {
        header_t *n = next_block(h);
        if (n && !h->allocated && !n->allocated) {
            h->size += n->size; // merge
            // No avanzamos h para intentar fusionar múltiples
vecinos
        } else {
            h = n;
        }
    }
}

void allocator_init(size_t size) {
    if (heap) return; // ya inicializado
    heap_size = align(size);
    heap = malloc(heap_size);
    if (!heap) fail("allocator_init: malloc fallo");
    // crear un único bloque libre que ocupa todo el heap
    header_t *h = (header_t*)heap;
    h->size = heap_size;
    h->allocated = 0;
}

void allocator_destroy(void) {
    if (heap) {
        free(heap);
        heap = NULL;
        heap_size = 0;
    }
}

void* mm_malloc(size_t size) {
    if (size == 0) return NULL;
    if (!heap) fail("mm_malloc: allocator no inicializado");

    // tamaño solicitado con header + alineación
    size_t asize = align(size + sizeof(header_t));
    if (asize < sizeof(header_t) + ALIGNMENT) asize =
sizeof(header_t) + ALIGNMENT;

    header_t *h = find_fit(asize);
    if (!h) return NULL; // sin memoria suficiente

    split_block(h, asize);
    h->allocated = 1;
    // payload empieza justo después del header
    return (void*)((uint8_t*)h + sizeof(header_t));
}

void mm_free(void *ptr) {
    if (!ptr) return;
    header_t *h = (header_t*)((uint8_t*)ptr -
sizeof(header_t));
    if ((uint8_t*)h < heap || (uint8_t*)h >= heap + heap_size)
return; // ptr inválido (silencioso)
    h->allocated = 0;
    coalesce_all();
}

void* mm_realloc(void *ptr, size_t size) {
    if (!ptr) return mm_malloc(size);
    if (size == 0) {
        mm_free(ptr);
        return NULL;
    }

    header_t *old = (header_t*)((uint8_t*)ptr -
sizeof(header_t));
    size_t old_payload = old->size - sizeof(header_t);

    // si el tamaño nuevo cabe en el bloque actual,
reutilizamos (sin shrink)
    if (size <= old_payload) return ptr;

    // si no, allocate-copy-free
    void *newptr = mm_malloc(size);
    if (!newptr) return NULL;
    memcpy(newptr, ptr, old_payload);
    mm_free(ptr);
    return newptr;
}

void allocator_stats(void) {
    if (!heap) {
        printf("Allocator no inicializado.\n");
        return;
    }

    header_t *h = heap_start();
    int used = 0, free_blocks = 0;
    size_t free_total = 0, largest_free = 0, used_total = 0;

    while (h) {
        if (h->allocated) {
            used++;
            used_total += h->size;
        } else {
            free_blocks++;
            free_total += h->size;
            if (h->size > largest_free) largest_free =
h->size;
        }
        h = next_block(h);
    }

    printf("=== Implicit Allocator Stats ===\n");
    printf("Heap size: %zu bytes\n", heap_size);
    printf("Bloques usados: %d, total usado (incl headers):
%zu bytes\n", used, used_total);
    printf("Bloques libres: %d, total libre: %zu bytes\n",
free_blocks, free_total);
    printf("Mayor hueco libre: %zu bytes\n", largest_free);
}

──────────────────────────────────────────────────
// explicit_allocator.c
#include "allocator.h"
#include "utils.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdint.h>

// Bloque con punteros de free list (prev/next) y flag
allocated.
// size: tamaño total del bloque (incluye este header)
typedef struct block {
    size_t size;
    int allocated;
    struct block *prev; // prev free (solo válido si está en
free list)
    struct block *next; // next free
} block_t;

static uint8_t *heap = NULL;
static size_t heap_size = 0;
static block_t *free_list = NULL; // cabeza de la free list
(bloques libres)
static block_t* heap_start(void) {
    if (!heap) return NULL;
    return (block_t*)heap;
}

static block_t* next_block(block_t *b) {
    if (!b) return NULL;
    uint8_t *next = (uint8_t*)b + b->size;
    if (next >= heap + heap_size) return NULL;
    return (block_t*)next;
}

// Inserta al inicio de la free_list (O(1))
static void insert_free(block_t *b) {
    if (!b) return;
    b->prev = NULL;
    b->next = free_list;
    if (free_list) free_list->prev = b;
    free_list = b;
}

// Remueve b de la free_list (O(1))
static void remove_free(block_t *b) {
    if (!b) return;
    if (b->prev) b->prev->next = b->next;
    else free_list = b->next;
    if (b->next) b->next->prev = b->prev;
    b->prev = b->next = NULL;
}

// Buscar primer bloque libre que quepa (first-fit) en la
free_list
static block_t* find_fit(size_t asize) {
    block_t *b = free_list;
    while (b) {
        if (!b->allocated && b->size >= asize) return b;
        b = b->next;
    }
    return NULL;
}

static const size_t MIN_BLOCK = sizeof(block_t) + ALIGNMENT;
// Divide un bloque 'b' si sobra suficiente espacio para un
nuevo bloque libre
static void split_block(block_t *b, size_t asize) {
    if (!b) return;
    if (b->size >= asize + MIN_BLOCK) {
        uint8_t *newpos = (uint8_t*)b + asize;
        block_t *nb = (block_t*)newpos;
        nb->size = b->size - asize;
        nb->allocated = 0;
        // insertar nuevo bloque en free list
        nb->prev = nb->next = NULL;
        b->size = asize;
        insert_free(nb);
    }
}

// Encuentra el bloque anterior físicamente (recorrida desde
inicio del heap)
// Retorna NULL si b es el primer bloque.
static block_t* find_phys_prev(block_t *b) {
    block_t *cur = heap_start();
    block_t *prev = NULL;
    while (cur && cur != b) {
        prev = cur;
        cur = next_block(cur);
    }
    return prev;
}

// Coalesce: fusiona b con vecinos libres (izquierda y/o
derecha)
static void coalesce(block_t *b) {
    if (!b) return;

    // intentar fusionar con siguiente físico
    block_t *n = next_block(b);
    if (n && !n->allocated) {
        // si next está en free_list, removerlo
        // Puede ocurrir que n==free_list etc.
        remove_free(n);
        b->size += n->size;
    }

    // intentar fusionar con anterior físico
    block_t *p = find_phys_prev(b);
    if (p && !p->allocated) {
        // remover p de free_list y fusionar
        remove_free(p);
        p->size += b->size;
        // insertar p (bloque fusionado) en free_list
        insert_free(p);
    } else {
        // si no fusionamos con anterior, insertar b (ya
fusionado con next si aplica)
        insert_free(b);
    }
}

void allocator_init(size_t size) {
    if (heap) return; // ya inicializado
    heap_size = align(size);
    heap = malloc(heap_size);
    if (!heap) fail("allocator_init: malloc fallo
(explicit)");
    // crear único bloque libre
    block_t *b = (block_t*)heap;
    b->size = heap_size;
    b->allocated = 0;
    b->prev = b->next = NULL;
    free_list = b;
}

void allocator_destroy(void) {
    if (heap) {
        free(heap);
        heap = NULL;
        heap_size = 0;
        free_list = NULL;
    }
}

void* mm_malloc(size_t size) {
    if (size == 0) return NULL;
    if (!heap) fail("mm_malloc: allocator no inicializado
(explicit)");

    size_t asize = align(size + sizeof(block_t));
    if (asize < sizeof(block_t) + ALIGNMENT) asize =
sizeof(block_t) + ALIGNMENT;

    block_t *b = find_fit(asize);
    if (!b) return NULL;

    // quitar del free list y preparar bloque
    remove_free(b);
    split_block(b, asize);
    b->allocated = 1;
    // payload
    return (void*)((uint8_t*)b + sizeof(block_t));
}

void mm_free(void *ptr) {
    if (!ptr) return;
    block_t *b = (block_t*)((uint8_t*)ptr - sizeof(block_t));
    if ((uint8_t*)b < heap || (uint8_t*)b >= heap + heap_size)
return;
    b->allocated = 0;
    b->prev = b->next = NULL;
    coalesce(b);
}

void* mm_realloc(void *ptr, size_t size) {
    if (!ptr) return mm_malloc(size);
    if (size == 0) {
        mm_free(ptr);
        return NULL;
    }

    block_t *old = (block_t*)((uint8_t*)ptr -
sizeof(block_t));
    size_t old_payload = old->size - sizeof(block_t);

    if (size <= old_payload) return ptr; // cabe en el mismo
bloque

    void *newptr = mm_malloc(size);
    if (!newptr) return NULL;
    memcpy(newptr, ptr, old_payload);
    mm_free(ptr);
    return newptr;
}
void allocator_stats(void) {
    if (!heap) {
        printf("Allocator no inicializado.\n");
        return;
    }

    // contar bloques libres desde la free list y recorrer el
heap para estadísticas globales
    int free_count = 0;
    size_t free_total = 0, largest_free = 0;
    block_t *b = free_list;
    while (b) {
        free_count++;
        free_total += b->size;
        if (b->size > largest_free) largest_free = b->size;
        b = b->next;
    }

    // recorrer heap para contar usados
    int used_count = 0;
    size_t used_total = 0;
    block_t *cur = heap_start();
    while (cur) {
        if (cur->allocated) {
            used_count++;
            used_total += cur->size;
        }
        cur = next_block(cur);
    }

    printf("=== Explicit Allocator Stats ===\n");
    printf("Heap size: %zu bytes\n", heap_size);
    printf("Bloques usados: %d, total usado (incl headers):
%zu bytes\n", used_count, used_total);
    printf("Bloques libres (en free list): %d, total libre:
%zu bytes\n", free_count, free_total);
    printf("Mayor hueco libre: %zu bytes\n", largest_free);
}

──────────────────────────────────────────────────
// memory_driver.c
#include "allocator.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define OPS 2000
#define PTRS 1000
#define HEAP_BYTES (1024 * 64) // 64 KB

int main(int argc, char *argv[]) {
    (void)argc; (void)argv;
    allocator_init(HEAP_BYTES);

    void *ptrs[PTRS];
    for (int i = 0; i < PTRS; ++i) ptrs[i] = NULL;

    srand((unsigned)time(NULL));

    for (int i = 0; i < OPS; ++i) {
        int idx = rand() % PTRS;
        int op = rand() % 3; // 0: malloc, 1: free, 2: realloc
(opcional)

          if (op == 0) {
              size_t size = rand() % 512; // hasta 511 bytes
              void *p = mm_malloc(size);
              // opcional: si falla, dejar ptrs[idx] como estaba
              if (p) {
                  ptrs[idx] = p;
                  // escribir algo para detectar corrupciones
simples
                 if (size > 0) ((char*)p)[0] = (char)(i &
0xFF);
              }
          } else if (op == 1) {
              if (ptrs[idx]) {
                  mm_free(ptrs[idx]);
                  ptrs[idx] = NULL;
              }
          } else {
              // realloc
              if (ptrs[idx]) {
                  size_t size = rand() % 512;
                  void *p = mm_realloc(ptrs[idx], size);
                  ptrs[idx] = p;
              } else {
                // si no hay puntero, hacer malloc
                size_t size = rand() % 512;
                ptrs[idx] = mm_malloc(size);
            }
        }
    }

    allocator_stats();
    allocator_destroy();
    return 0;
}


──────────────────────────────────────────────────
//MAKEFILE
CC=gcc
CFLAGS=-Wall -Wextra -g -std=c11

all: implicit explicit

# build target 'implicit' (usa implicit_allocator.c)
implicit: memory_driver.o implicit_allocator.o utils.o
​    $(CC) $(CFLAGS) -o implicit memory_driver.o
implicit_allocator.o utils.o

# build target 'explicit' (usa explicit_allocator.c)
explicit: memory_driver.o explicit_allocator.o utils.o
​    $(CC) $(CFLAGS) -o explicit memory_driver.o
explicit_allocator.o utils.o

memory_driver.o: memory_driver.c allocator.h
​    $(CC) $(CFLAGS) -c memory_driver.c

implicit_allocator.o: implicit_allocator.c allocator.h utils.h
​    $(CC) $(CFLAGS) -c implicit_allocator.c

explicit_allocator.o: explicit_allocator.c allocator.h utils.h
​    $(CC) $(CFLAGS) -c explicit_allocator.c

utils.o: utils.c utils.h
​    $(CC) $(CFLAGS) -c utils.c

clean:
​    rm -f *.o implicit explicit
¿Cómo compilar y ejecutar?

En la carpeta allocator/ ejecuta:
make clean
make implicit        # compila el binario con el implicit allocator
./implicit

make explicit
./explicit

Cada ejecución ejecutará el memory_driver con 2000 operaciones aleatorias y mostrará
las estadísticas del heap al final.
