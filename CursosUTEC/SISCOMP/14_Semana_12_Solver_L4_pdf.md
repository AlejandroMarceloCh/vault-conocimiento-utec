---
curso: SISCOMP
titulo: 14 - Semana 12/Solver_L4
slides: 8
fuente: 14 - Semana 12/Solver_L4.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
November 7th, 2025

                            Laboratorio 04: Syscalls & Interrupts


Objetivos:
●​ Escribir un programa que imprime algo en la consola sin importar ninguna cabecera ni
   usar la biblioteca estándar de C, a partir de una syscall escrita en Ensamblador.
●​ Escribir un programa que gestiona una interrupción para alternar mensajes entre
   alfabeto y numeración decimal, de manera temporizada.


   1.​ Syscalls (12 puntos)

1.1 Crear manualmente una syscall en ensamblador RISC-V usando ecall (1 pto)

   a.​ Usar la llamada al sistema write de Linux para mostrar caracteres en la consola.
   b.​ Observar el archivo unistd.h, ¿Cuál es el número de syscall para write ? 64
   c.​ La página del manual (https://linux.die.net/man/2/write) indica que esta llamada al
       sistema recibe ____ argumentos (indique un número) 3

ssize_t write(int fd, const void buf[.count], size_t count);

1.2 Describir los argumentos (1.5 ptos):

   a.​ fd: _______________________________________
   b.​ buf[.count]:______________________________
   c.​ count:____________________________________
   a.​ Descriptor de archivo
   b.​ Puntero al búfer con los caracteres a imprimir .
   c.​ El número de caracteres.

Escriba un código que imprima cadenas de un solo caracter a partir de la siguiente rutina en
ensamblador, esta rutina imprime en el descriptor de archivo 0 y muestra exactamente 1
caracter (3 ptos).

  ​   addi a7, x0, _____               # Complete con el número de syscall:
write

       addi a0, x0, 0          # primer argumento: fd

  ​    mv      a1, t0          # segundo argumento: buf

  ​    addi a2, x0, 1          # tercer argumento: count

  ​    ecall
Configurar el a7 con el número de la syscall y agregue sus tres argumentos (fd = 0, puntero
= asuma en t0 y la longitud 1)

Configurar el a7 con el número de la syscall. (64) y agregue sus tres argumentos (fd = 0,
puntero = asuma en t0 y la longitud 1)

.global printone

printone:

  mv t0, a0                # guardar el argumento de la función: puntero a
carácter

    # Realizar la llamada al sistema: write(0, t0, 1)

    addi a7, x0, 64        # número de syscall: write

    addi a0, x0, 0         # primer argumento: fd

    mv      a1, t0         # segundo argumento: buf

    addi a2, x0, 1         # tercer argumento: count

    ecall

    ret

1.4 Utilice la función ensamblada desde un código en C, declarando la función (1.5 ptos).

int printone(char* c);

int main() {

         printone("h");

         printone("i");

         printone("\n");

         return 0;

}

1.5 Compilar y ejecutar todo el programa combinando el archivo C y el archivo ensamblador,
muestre y comente sus resultados (1 pto)

$ rv gcc -o printone printone.c printone.s
2. Interrupciones (8 puntos)

Diseñar un código en Linux con arquitectura x86 que muestre siempre el alfabeto, este
proceso debe ser capaz de detectar una interrupción programada cada 5 segundos que
dure dos segundos muestre números desde 0 a 9 (4 ptos)

#include <linux/module.h>

#include <linux/kernel.h>

#include <linux/init.h>

#include <linux/kthread.h>

#include <linux/delay.h>

#include <linux/timer.h>

#include <linux/jiffies.h>

#include <linux/sched.h>

MODULE_LICENSE("GPL");

MODULE_AUTHOR("Antu");

MODULE_DESCRIPTION("Módulo que muestra el alfabeto y números con
interrupción programada");

MODULE_VERSION("1.0");

static struct task_struct *display_thread;

static struct timer_list my_timer;

static bool show_numbers = false;            // Modo actual: false=alfabeto,
true=números

static bool stop_thread = false;

// ─────────────────────────────────────────────

//   Función del temporizador (simula interrupción)

// ─────────────────────────────────────────────

static void timer_callback(struct timer_list *t)
{

     // Activa modo de números por 2 segundos

     show_numbers = true;

     pr_info("[timer] Interrupción: mostrando números por 2s\n");



     // Programa un trabajo diferido en 2 segundos para volver al
modo alfabeto

        schedule_delayed_work((struct       delayed_work     *)t->data,   2   *
HZ);}

// ─────────────────────────────────────────────

//   Trabajo diferido: volver al modo alfabeto

// ─────────────────────────────────────────────

static void stop_numbers_workfn(struct work_struct *work);

static                            DECLARE_DELAYED_WORK(stop_numbers_work,
stop_numbers_workfn);

static void stop_numbers_workfn(struct work_struct *work)

{

     show_numbers = false;

       pr_info("[timer]     Fin    de   ventana   de   números,   volviendo   a
alfabeto\n");

     // Reprograma la siguiente “interrupción” en 5 segundos

     mod_timer(&my_timer, jiffies + 5 * HZ);

}

// ─────────────────────────────────────────────

//   Hilo principal que imprime alfabeto o números

// ─────────────────────────────────────────────

static int display_fn(void *data)

{
     char letter = 'A';

     int num = 0;

     while (!kthread_should_stop() && !stop_thread) {

         if (show_numbers) {

             printk(KERN_INFO "[display] %d\n", num);

             num = (num + 1) % 10;

             msleep(200); // más rápido al mostrar números

         } else {

             printk(KERN_INFO "[display] %c\n", letter);

             letter++;

             if (letter > 'Z')

                    letter = 'A';

             msleep(500); // ritmo normal

         }

     }

     return 0;

}

// ─────────────────────────────────────────────

//   Inicialización del módulo

// ─────────────────────────────────────────────

static int __init alphabet_timer_init(void)

{

     pr_info("alphabet_timer: iniciando módulo\n");

     // Inicializar timer

     timer_setup(&my_timer, timer_callback, 0);

     my_timer.data = (unsigned long)&stop_numbers_work;
        mod_timer(&my_timer,      jiffies   +   5   *   HZ);   //   primera
interrupción a los 5 s

     // Crear hilo de impresión

              display_thread       =   kthread_run(display_fn,        NULL,
"alphabet_display");

     if (IS_ERR(display_thread)) {

         pr_err("No se pudo crear hilo de display\n");

         del_timer_sync(&my_timer);

         return PTR_ERR(display_thread);

     }

     pr_info("alphabet_timer: módulo iniciado correctamente\n");

     return 0;

}

// ─────────────────────────────────────────────

//   Limpieza al descargar módulo

// ─────────────────────────────────────────────

static void __exit alphabet_timer_exit(void)

{

     pr_info("alphabet_timer: deteniendo módulo\n");



     stop_thread = true;

     if (display_thread)

         kthread_stop(display_thread);



     del_timer_sync(&my_timer);

     cancel_delayed_work_sync(&stop_numbers_work);
     pr_info("alphabet_timer: descargado correctamente\n");

}



module_init(alphabet_timer_init);

module_exit(alphabet_timer_exit);




2.1 Seguir los siguientes pasos y responda cuáles son las funciones involucradas en cada
uno de ellos (2 ptos - 0.5 c/u).

    a.​ Crear un temporizador kernel que simule una interrupción periódica.

       timer_setup() + mod_timer()

    b.​ Generar la temporización de la interrupción (2 segundos).

       stop_numbers_work

    c.​ Generar un flag que indique qué imprimir (alfabeto o números).

       show_numbers

    d.​ Generar el hilo de kernel que imprime continuamente.

       kthread_run()

    e.​ Describa cómo se programan los timers en el kernel.

       jiffies + N*HZ

2.2 A través del diagrama de la figura 1, indique cuáles son los registros o rutinas utilizados
para la solución de su problema (2 ptos).
Figura 1
