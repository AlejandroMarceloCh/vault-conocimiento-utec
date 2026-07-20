---
curso: SISCOMP
titulo: 03 - Semana 1/dumpbytes
slides: 0
fuente: 03 - Semana 1/dumpbytes.c
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 03 - Semana 1/dumpbytes.c. -->

<!-- INTERPRETAR: código fuente (03 - Semana 1/dumpbytes.c). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

```c
#include <stdio.h>

typedef unsigned char * byte_pointer;

void show_bytes(byte_pointer start, size_t len) {
    printf("%p: ", start);
    int i;
    for (i = 0; i < len; i++) {
        printf("%02X ", start[i]);
    }
    printf("\n");
}

void show_int(int x) {
    show_bytes((byte_pointer) &x, sizeof(int));
}

void show_long(long x) {
    show_bytes((byte_pointer) &x, sizeof(long));
}

void show_float(float x) {
    show_bytes((byte_pointer) &x, sizeof(float));
}

void show_pointer(void *x) {
    show_bytes((byte_pointer) &x, sizeof(void*));
}

int main() {
    int ints[] = {0, 1, -1, 8, -8, 0x00001234, 0x56780000, 0x12345678, 0xDEADBEEF, 0x0A0B0C0D, 15213, -15213};
    long longs[] = {0, 1, -1, 0xDEADBEEFBAADF00D, 0x0102030405060708};
    for (int i = 0; i < sizeof(ints) / sizeof(int); ++i) {
        show_bytes((byte_pointer) &ints[i], sizeof(int));
    }
    for (int i = 0; i < sizeof(longs) / sizeof(long); ++i) {
        show_bytes((byte_pointer) &longs[i], sizeof(long));
    }
    char str[] = "Hello World!";
    show_bytes((byte_pointer) str, sizeof(str));
    show_pointer(ints);
    show_pointer(longs);
    return 0;
}

	
	
```
