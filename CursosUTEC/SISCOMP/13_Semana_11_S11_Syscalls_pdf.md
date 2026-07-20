---
curso: SISCOMP
titulo: 13 - Semana 11/S11 Syscalls
slides: 3
fuente: 13 - Semana 11/S11 Syscalls.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
October 31th, 2025

                                      S11: Linux Syscalls

Objetivos:

Al finalizar el laboratorio, el estudiante será capaz de:

   1.​ Comprender qué es una llamada al sistema (syscall) y su rol en la comunicación
       entre procesos de usuario y el kernel.
   2.​ Identificar las principales syscalls en Linux (open, read, write, fork, exec, exit, etc.).
   3.​ Implementar programas en C que utilicen syscalls directamente.
   4.​ Analizar el comportamiento de los programas mediante herramientas de monitoreo
       como strace.
   5.​ Diferenciar entre funciones de biblioteca (libc) y llamadas al sistema.

Conocimientos previos:

Responda brevemente, indique al menos una referencia bibliográfica.
   1.​ ¿Cuál es la relación entre funciones de biblioteca (por ejemplo printf) y syscalls
       (write)?
   2.​ ¿Cómo Linux implementa syscalls (tablas del sistema, número de syscall, etc.)?

Requerimientos:

   1.​ Entorno Linux (Ubuntu o Debian).
   2.​ Compilador gcc.
   3.​ Herramienta strace.
   4.​ Editor de texto (nano, vim, VS Code, etc.).

Experimento 1: Syscalls con strace

   1.​ Crear un archivo simple:

echo "Hola mundo" > hola.txt

   2.​ Ejecutar un comando con strace:

strace cat hola.txt

   3.​ Observar las syscalls: openat, read, write, close, etc.

   4.​ Responder:
          ●​ ¿Qué llamada abre el archivo?
          ●​ ¿Qué syscall imprime el texto?
         ●​ ¿Qué sucede al cerrar el archivo?
   5.​ ¿Qué diferencia hay entre ejecutar cat y escribir un programa en C que use read y
      write?

Experimento 2: Programa con syscalls directas

   1.​ Analice el siguiente código base, llamado hola_syscall.c

#include <unistd.h>
#include <sys/syscall.h>

int main() {
    const char *msg = "Hola desde syscall!\n";
    syscall(SYS_write, 1, msg, 20); // 1 = STDOUT
    return 0;
}

   2.​ ¿Qué función realiza el código?
   3.​ Compilar y ejecutar:

gcc -o hola_syscall hola_syscall.c
./hola_syscall

   4.​ Comparar con el siguiente código:

#include <stdio.h>
int main() {
    printf("Hola desde printf!\n");
    return 0;
}

   5.​ Usar strace ./hola_syscall y strace ./hola_printf para comparar.
   6.​ ​¿Qué diferencia hay en las syscalls llamadas en cada caso?
   7.​ ¿Por qué printf hace más syscalls que write?

Experimento 3:

   1.​ Se tiene el siguiente código:

#include <unistd.h>
#include <sys/syscall.h>
#include <fcntl.h>

int main() {
    char buffer[128];
    int fd = syscall(SYS_open, "hola.txt", O_RDONLY);
    int n = syscall(SYS_read, fd, buffer, sizeof(buffer));
     syscall(SYS_write, 1, buffer, n);
     syscall(SYS_close, fd);
     return 0;
}

    2.​ Modificar el programa para que lea el nombre del archivo desde argumentos
        (argv[1]).
    3.​ Maneje errores (si el archivo no existe, mostrar mensaje con write).
