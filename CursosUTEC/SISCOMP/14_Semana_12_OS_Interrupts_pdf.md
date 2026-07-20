---
curso: SISCOMP
titulo: 14 - Semana 12/OS Interrupts
slides: 3
fuente: 14 - Semana 12/OS Interrupts.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
October 6th, 2025

                              Laboratorio S12: Interrupts


Objetivos:
●​ Comprender el papel de las interrupciones en el funcionamiento de un sistema
   operativo.
●​ Diferenciar entre interrupciones de hardware, software y excepciones.
●​ Explicar cómo Linux implementa las interrupciones a nivel de usuario mediante
   señales (signals).
●​ Implementar programas en C que gestionen señales como interrupciones de
   software.
●​ Analizar el flujo de ejecución del sistema cuando se produce una interrupción.

Marco teórico:
Una interrupción es un mecanismo mediante el cual el hardware o el software pueden
detener temporalmente la ejecución normal de un programa para solicitar la atención del
procesador. Linux gestiona las interrupciones de hardware a través del kernel, mientras
que las interrupciones de software se implementan mediante señales (signals) en el
espacio de usuario.

Signals: https://man7.org/linux/man-pages/man7/signal.7.html

Requisitos del entorno:
●​ Sistema operativo Linux (Ubuntu o Debian).
●​ Compilador gcc.
●​ Herramientas ps, kill, strace.
●​ Editor de texto (nano, vim o VS Code).

Paso 1: Interrupciones desde el usuario


1. Ejecutar en la terminal:​ yes > /dev/null​
2. Presionar Ctrl + C y luego Ctrl + Z​
3. Observar el comportamiento del proceso usando ps -l​
​
Estas combinaciones generan señales SIGINT y SIGTSTP, equivalentes a
interrupciones de teclado manejadas por el kernel.
Paso 2: Manejo de señales en C


Utilice el siguiente script para implementar un programa en C que capture señales
(interrupciones) del sistema (puede utilizar otro script si desea modificarlo)

​
#include <stdio.h>​
#include <signal.h>​
#include <unistd.h>​
​
void manejador(int signal) {​
    if (signal == SIGINT)​
        printf("\nRecibida señal SIGINT (Ctrl+C). Ignorando
interrupción...\n");​
    else if (signal == SIGTSTP)​
        printf("\nRecibida señal SIGTSTP (Ctrl+Z). Seguiré el
proceso.\n");​
}​
​
int main() {​
    signal(SIGINT, manejador);​
    signal(SIGTSTP, manejador);​
    while (1) {​
        printf("Proceso ejecutándose... PID = %d\n", getpid());​
        sleep(2);​
    }​
    return 0;​
}

Pasos:

Compilar el programa:​       gcc -o handle_int handle_int.c

Ejecutarlo:​   ​     ​       ./handle_int

Presionar Ctrl + C y Ctrl + Z para observar la respuesta del manejador.

Responder:

¿Qué ocurre si se eliminan las líneas signal(SIGINT, manejador)?

¿Qué hace Linux por defecto al recibir esas señales?
¿Por qué estas señales son interrupciones de software?



Paso 3: Generar señales con kill: Simular interrupciones enviadas por otros procesos.​
​
1. Ejecutar el programa anterior y obtener su PID.​
2. Desde otra terminal, enviar señales:​
  kill -SIGUSR1 <PID>​
  kill -SIGTERM <PID>​
3. Modificar el código para manejar SIGUSR1 y SIGTERM con mensajes personalizados.



Paso 4: Temporizador con interrupciones (alarmas)


Usar el temporizador del sistema para generar interrupciones periódicas.​
​
#include <stdio.h>​
#include <signal.h>​
#include <unistd.h>​
​
void alarma(int sig) {​
     printf("Interrupción por temporizador: SIGALRM
recibida.\n");​
     alarm(3);​
}​
​
int main() {​
     signal(SIGALRM, alarma);​
     alarm(3);​
     while (1) pause();​
     return 0;​
}

Paso 5: Responder
• ¿Qué relación existe entre una interrupción de hardware (por ejemplo, del teclado) y la
señal SIGINT?​
• ¿Por qué el sistema operativo necesita diferenciar entre interrupciones y excepciones?​
• ¿Cómo se implementan los manejadores de interrupción (ISR) en el kernel y en el
espacio de usuario?
