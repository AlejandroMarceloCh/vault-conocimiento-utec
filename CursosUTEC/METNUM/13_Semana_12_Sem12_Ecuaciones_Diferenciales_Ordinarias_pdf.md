---
curso: METNUM
titulo: 13 - Semana 12/Sem12_Ecuaciones Diferenciales Ordinarias
slides: 40
fuente: 13 - Semana 12/Sem12_Ecuaciones Diferenciales Ordinarias.pdf
---

Métodos Numéricos
Ecuaciones Diferenciales
Ordinarias - S12
Hermes Yesser Pantoja Carhuavilca
(hpantoja@utec.edu.pe)
Jimmy Mendoza Montalvo
(jmendoza@utec.edu.pe)
Rósulo Pérez Cupe
(rperezc@utec.edu.pe)
Julio Cesar Barraza Bernaola
(jbarraza@utec.edu.pe)
Marco Antonio Cuyubamba Espinoza
(mcuyubamba@utec.edu.pe)


                                    Profesores: Utec-Ciencias
Temas

                                         1 Ecuaciones Diferenciales Ordinar-
                                           ias con Valores Iniciales
Índice                                   2 Método de Euler
                                         3 Métodos de Runge-Kutta
                                         4 Análisis de Error




Universidad de Ingeniería y Tecnología   Métodos Numéricos              1 / 39
        Objetivos:
            Resolver problemas de valor inicial (PVI) mediante los métodos de Euler, Heun
            y Runge–Kutta de cuarto orden (RK4).

            Resolver sistemas de ecuaciones diferenciales ordinarias mediante métodos
            numéricos de un paso (Euler, Heun y RK4).




Universidad de Ingeniería y Tecnología            Métodos Numéricos                     2 / 39
1   ECUACIONES
    DIFERENCIALES
    ORDINARIAS DE
    PRIMER ORDEN CON
    VALOR INICIAL
        Objetivos:
            Resolver problemas de valor inicial (PVI) mediante los métodos de Euler, Heun
            y Runge–Kutta de cuarto orden (RK4).

            Resolver sistemas de ecuaciones diferenciales ordinarias mediante métodos
            numéricos de un paso (Euler, Heun y RK4).




Universidad de Ingeniería y Tecnología            Métodos Numéricos                     4 / 39
 Introducción
                                           Los sistemas dinámicos, como el
                                           péndulo, se describen con EDOs.
                                           En ingeniería, se requiere poder:
                                                 Predecir trayectorias.
                                                 Evaluar estabilidad.
                                                 Resolver sistemas acoplados.
                                           Las soluciones analíticas existen para
                                           pequeñas oscilaciones: sin(θ) ≈ θ ⇒
La ecuación diferencial que describe       EDO lineal.
el movimiento del péndulo es:              Si θ es grande ⇒ EDO no lineal:
                                                 Transformación de ecuaciones.
             d 2θ g
                  + sin(θ) = 0                   Métodos de integración numérica.
             dt 2  l

  Universidad de Ingeniería y Tecnología   Métodos Numéricos                        5 / 39
Problema de valor inicial (PVI)
Sean:
    t variable independiente.
    x = x(t) variable dependiente o función incógnita.
    x (1) , x (2) , · · · , x (n) las derivadas de la variable dependiente.
En general, a una expresión de la forma:
                                                                       
                                   F t, x, x (1) , x (2) , · · · , x (n) = 0

A la cual agregamos las condiciones (llamadas condiciones iniciales):
                             
                                  x (t0 ) = x0
                                     ′ (t ) = x
                             
                                   x
                             
                                          0      1
                             
                             
                                   x ′′ (t0 ) = x2
                             
                                           ..
                                             .
                             
                             
                             
                             
                              (n−1)
                                x        (t0 ) = xn−1

Universidad de Ingeniería y Tecnología            Métodos Numéricos            6 / 39
Problema de valor inicial (PVI)
       Se le denomina: Ecuación Diferencial Ordinaria (en adelante llamado EDO) de
       orden n con valores iniciales.
       Resolver la EDO con condiciones iniciales significa encontrar una función
       x = x(t) que satisfaga la ecuación dada y las condiciones iniciales.
       En principio se intenta hallar la solución analítica. Sin embargo, existen
       ecuaciones diferenciales imposibles de resolver analíticamente.
       Luego surge la necesidad de buscar una solución numérica de dicha
       ecuación.




Universidad de Ingeniería y Tecnología        Métodos Numéricos                     7 / 39
Ejemplos
       Ecuación diferencial ordinaria de valores iniciales de 1er orden:

                                            x ′ = t 2 − 3x;        x(0) = 1
                                                                   2
                                         25 −3t
       cuya solución explícita es x(t) = 27 e   + t3 − 2t9 + 27
                                                              2
                                                                .

       EDO de tercer orden:
                                                      
                                tetx x (3) − sin tx (2) + x (1) + cos(x) = t 2 sin(t)
                                x(0) = 0;    x ′ (0) = 1      ;   x ′′ (0) = −1.

       La solución analítica se desconoce, se debe usar un método numérico.




Universidad de Ingeniería y Tecnología                        Métodos Numéricos         8 / 39
Algunos ejemplos aplicados

  Ley                                    Expresión matemática         Variables y parámetros
                                                dv   F
  Segunda ley de Newton                            =                  Velocidad (v ), fuerza (F ) y masa (m)
                                                dt   m
  del movimiento
                                                       dT
  Ley del calor de Fourier                    q = −k                  Flujo de calor (q), conductividad tér-
                                                       dx
                                                                      mica (k ) y temperatura (T )
                                                       dc
  Ley de difusión de Fick                     J = −D                  Flujo másico (J), coeficiente de di-
                                                       dx
                                                                      fusión (D) y concentración (c)
                                                        di
  Ley de Faraday (induc-                      ∆Vl = L                 Caída de voltaje (∆Vl ), inductancia
                                                        dt
  tor)                                                                (L) y corriente (i)




Universidad de Ingeniería y Tecnología                       Métodos Numéricos                         9 / 39
Forma normal de un problema de valor inicial
  Forma normal o explícita de una EDO de primer orden

                             F (t, x, x ′ ) = 0    es equivalente a       x ′ = f (t, x)

 Ejemplos
                                                                          2
                            2                                        e−t
        (1 + t 2 )x ′ = e−t              es equivalente a    x′ =
                                                                    1 + t2
                                                                                  t − x2
        x ′ et sin(πx) + x 2 − t = 0              es equivalente a       x′ =
                                                                                et sin(πx)
                ′
        ex+x = cos(πx 2 )                es equivalente a     x ′ = ln(cos(πx 2 )) − x

Observación: No todas las EDO admiten una forma normal.


Universidad de Ingeniería y Tecnología                      Métodos Numéricos                10 / 39
Solución numérica de una EDO de primer orden
con valor inicial
Resolver numéricamente una EDO de primer orden con valor inicial, requiere las
siguientes condiciones:
   1   La EDO en su forma normal:                x ′ = f (t, x)
   2   El intervalo donde se hallará la solución:                 t ∈ [a, b]
   3   La condición inicial:             x(a) = x0
   4   La cantidad de intervalos para la discretización:                  n




Universidad de Ingeniería y Tecnología                    Métodos Numéricos    11 / 39
Solución numérica de una EDO de primer orden
con valor inicial
Luego realizar los cálculos iniciales:
                                           b−a
       Calcular el tamaño de paso                          h=
                                              n
       Hallar los puntos de discretización ti = a + ih para i = 0, 1, 2, · · · , n, es decir:

                                     t0       ,   t1   ,    t2   ,    ···    ,    tn−1   ,       tn

       Finalmente aproximar los valores de x(ti ) mediante:

                                   x0     ,       x1   ,    x2   ,    ···     ,   xn−1       ,   xn




Universidad de Ingeniería y Tecnología                               Métodos Numéricos                12 / 39
Esquema general de los métodos de paso
  Esquema general (tamaño de paso constante)
 Considerando que x0 es conocido, cada una de las otras aproximaciones se hallan
 mediante:
                            xi+1 = xi + hφ(ti , xi , h)
 para i = 0, 1, 2, · · · , (n − 1)

Siendo φ(ti , xi , h) una aproximación a x ′ (ti ), es decir, una aproximación a la
pendiente de la recta tangente a la función x(t) en el punto ti .




Universidad de Ingeniería y Tecnología         Métodos Numéricos                      13 / 39
Método de Euler
  Problema de Valor Inicial (PVI)
                                                      dx
                                             (
                                                 x′ =    = f (t, x)
                                                      dt
                                                 x(a) = x0
                                                                       b−a
             t ∈ [a, b]        ;     n (subintervalos)    ;     h=         (tamaño de paso)
                                                                        n

  Método de EULER
  *xi+1 = xi + hf (ti , xi )




Universidad de Ingeniería y Tecnología                        Métodos Numéricos               14 / 39
Método de Euler
                   dx
Considere el PVI:      = f (t, x) ; x(t0 ) = x0
                   dt
El siguiente esquema nos ayudará a entender el funcionamiento geométrico del
método de Euler:




Universidad de Ingeniería y Tecnología   Métodos Numéricos                15 / 39
Ejemplo (Método de Euler)
Resuelva la EDO de primer orden con valor inicial o PVI, utilizando el método de
Euler:
                                 dx
                              
                              
                                   = t 2 − 3x
                                 dt
                              
                              
                                 x(1) = 10
Considerando el intervalo t ∈ [1; 3] y n = 4 (subintervalos).




Universidad de Ingeniería y Tecnología       Métodos Numéricos               16 / 39
   Método de Euler (continúa el ejemplo)
          Calculamos el tamaño de paso: h = 3−1
                                             4 = 0.5
          Discretizamos el intervalo [1, 3], hallando los puntos:

                       t0 = 1.0         ,   t1 = 1.5   ,   t2 = 2.0    ,    t3 = 2.5   y   t4 = 3.0

          Valor inicial: x0 = 10
        Función: f (t, x) = t 2 − 3x
        
         x1 = x0 + h · f (t0 , x0 )
Paso 1:       = 10 + 0.5(1.02 − 3(10))
              = −4.5
        




   Universidad de Ingeniería y Tecnología                      Métodos Numéricos                      17 / 39
   continúa
     
            ejemplo
         x2 = x1 + h · f (t1 , x1 )
Paso 2:      = −4.5 + 0.5(1.52 − 3(−4.5))
             = 3.375
        

        
         x3 = x2 + h · f (t2 , x2 )
Paso 3:      = 3.375 + 0.5(2.02 − 3(3.375))
             = 0.3125
        

        
         x4 = x3 + h · f (t3 , x3 )
Paso 4:      = 0.3125 + 0.5(2.52 − 3(0.3125))
             = 2.9688
        




   Universidad de Ingeniería y Tecnología   Métodos Numéricos   18 / 39
Métodos de Runge-Kutta
Podemos mejorar las aproximaciones obtenidas por el método de Euler.
Aplicaremos los métodos de Runge-Kutta para hallar la solución numérica de una
EDO con valor inicial de la forma:
                                   dy
                                 
                                 
                                      = f (x, y )
                                   dx
                                 
                                 
                                   y (x0 ) = y0

en el intervalo x ∈ [x0 ; b].




Universidad de Ingeniería y Tecnología   Métodos Numéricos                19 / 39

Métodos de Runge-Kutta
Del conjunto de métodos numéricos para EDOs, los métodos de Runge-Kutta
logran mayor exactitud usando la expansión de la serie de Taylor sin calcular
derivadas de orden superior. Trabajan bajo la forma general:

                                         yi+1 = yi + h · φ(xi , yi , h)

Donde φ se conoce como la función incremento (pendiente representativa en el
intervalo [xi , xi+1 ]):
                         φ = a1 k1 + a2 k2 + . . . + an kn




Universidad de Ingeniería y Tecnología                    Métodos Numéricos     20 / 39
Método de Runge-Kutta de segundo orden
En el caso de n = 2 tenemos los métodos de segundo orden de Runge-Kutta
(RK2):                  
                        yi+1 = yi + (a1 k1 + a2 k2 ) h
                        
                                             k1 = f (ti , yi )
                                         
                                             k2 = f (ti + p1 h, yi + q11 k1 h)
                                         

Donde las constantes se determinan expandiendo la serie de Taylor de segundo
grado, generando el sistema no lineal:




Universidad de Ingeniería y Tecnología                           Métodos Numéricos   21 / 39
Método de Runge-Kutta de segundo orden
  Sistema obtenido
                                         a1 + a2 = 1
                                                     1
                                          a2 · p 1 =
                                                     2
                                                     1
                                         a2 · q11 =
                                                     2
Al elegir un valor arbitrario para a2 , se obtienen los valores de a1 , p1 y q11 .




Universidad de Ingeniería y Tecnología           Métodos Numéricos                   22 / 39
Método de Runge-Kutta de segundo orden
                           a2       a1    p1    q11   Método Asociado
                          1/2       1/2   1     1     Heun con un solo corrector
                            1        0    1/2   1/2   Del punto medio
                          2/3       1/3   3/4   3/4   Ralston




Universidad de Ingeniería y Tecnología                    Métodos Numéricos        23 / 39
uation (10.56) can also be derived by integrating the ODE
 erval  x i x i + 1  using the trapezoidal method.
            Método de Runge-Kutta de segundo orden
        Método de Heun Estructural
of the slope at
f the interval.         y
     y(x)                                                         y(x)
                                                                                    yi+1
on                   Eu
                   yi+1                                   Solución
                                                          exacta

                                                                                                         Eu
                               Eu )
             Slope: f (xi+1 , yi+1          yi                           Pend.: f (xi , yi) + f (xi+1 , yi+1)
                                                                                             2
                                x                                                          x
h           xi+1                                     xi       h          xi+1
    (b

10: The modified Euler method.
            Universidad de Ingeniería y Tecnología                              Métodos Numéricos               24 / 39
Método de Runge-Kutta de segundo orden
  Método de Heun (RK2)
                                                                            
                                                               1     1
                                         yi+1 = yi + h ·         k1 + k2
                                                               2     2

siendo:
                                           k1 = f (xi , yi )
                                           k2 = f (xi + h, yi + k1 · h)
Donde k1 es la pendiente al inicio y k2 es la pendiente calculada en el extremo final.




Universidad de Ingeniería y Tecnología                         Métodos Numéricos   25 / 39
Ejemplo (Método de Runge-Kutta de segundo
orden)
Resuelva la EDO de primer orden con valor inicial utilizando el método de RK2
(Heun):
                                 dy
                              
                              
                                   = x 2 − 3y
                                 dx
                              
                              
                                y (1) = 10
Considerando el intervalo x ∈ [1; 3] y n = 4 (subintervalos).




Universidad de Ingeniería y Tecnología      Métodos Numéricos               26 / 39
Método de RK2 (continúa el ejemplo)
       Tamaño de paso: h = 3−1
                            4 = 0.5
       Puntos: x0 = 1.0, x1 = 1.5, x2 = 2.0, x3 = 2.5, x4 = 3.0.
       Valor inicial: y0 = 10, y la función de control f (x, y ) = x 2 − 3y .
                             
                              k1 = f (xi , yi )
                             
                             
                                  k2 = f (xi + h, yi + k1 · h)
                             
                                       = y + h · 1k + 1k
                             
                              y                                 
                                         i+1   i      2 1      2 2




Universidad de Ingeniería y Tecnología             Métodos Numéricos            27 / 39
          
           k1 = f (1, 10) = −29
          
          
Paso 1:     k2 = f (1.5, −4.5) = 15.75
          
           y = 10 + 0.5 · 1 (−29) + 1 (15.75) = 6.6875
          
             1                2        2
          
           k1 = f (1.5, 6.6875) = −17.8125
          
          
Paso 2:     k2 = f (2, −2.21875) = 10.6562
          
           y = 6.6875 + 0.5 · 1 (−17.8125) + 1 (10.6562) = 4.8984
          
             2                   2            2




   Universidad de Ingeniería y Tecnología   Métodos Numéricos         28 / 39
   continúa
     
            ejemplo
         k1 = f (2, 4.8984) = −10.6952
        
        
Paso 3:   k2 = f (2.5, −0.4492) = 7.5976
        
         y = 4.8984 + 0.5 · 1 (−10.6952) + 1 (7.5976) = 4.1240
        
           3                    2           2
        
         k1 = f (2.5, 4.1240) = −6.1220
        
        
Paso 4:     k2 = f (3, 1.0630) = 5.8110
          
           y = 4.1240 + 0.5 · 1 (−6.1220) + 1 (5.8110) = 4.0463
          
             4                    2          2




   Universidad de Ingeniería y Tecnología   Métodos Numéricos       29 / 39
Resolución tabular
Todo el cálculo anterior puede consolidarse de la siguiente forma estructurada:

                i      xi           yi   k1 = f (xi , yi )   k2 = f (xi + h, yi + k1 h)    yi+1
                0     1.0      10.0000    −29.0000                   15.7500              6.6875
                1     1.5       6.6875    −17.8125                   10.6563              4.8984
                2     2.0       4.8984    −10.6952                    7.5976              4.1240
                3     2.5       4.1240     −6.1220                    5.8110              4.0463
                4     3.0       4.0463




Universidad de Ingeniería y Tecnología                       Métodos Numéricos                     30 / 39
        the slope K 3 ; figure (c) shows how slope K 3 is used to find the slop
Método de
        K 4 ;Runge-Kutta           de cuarto
             and figure (d) illustrates            orden
                                        the application of Eq. (10.86) where th
Método de RK4 Clásico
y                    y(x)                                    y                  y(x)

                                                Solución                                                    Solución
                                                exacta                                                      exacta
                                                                   yi+ 12 K2h
                                                                                                Pendiente: K3
       yi+ 12 K1h
 yi                              Pendiente: K2               yi
                       Pendiente: K1                                            Pendiente: K2           x
                                         x
         xi            xi+ 12 h          xi+1                       xi          xi+ 12 h         xi+1

                          h                                                       h


y                                                            y                     y(x)                 Solución
                         yi+K3h                                                                         numérica
                                                            Pendiente: 1 (K1+2K2+2K3+K4)
                                                                       6
Universidad de Ingeniería y Tecnología          Solución   Métodos Numéricos                                   31 / 39
         xi            xi+ 12 h          xi+1                        xi         xi+ 12 h    xi+1
Método de Runge-Kutta de cuarto orden
                                 h
                          h
Método de RK4 Clásico

y                                                             y                    y(x)            Solución
                         yi+K3h                                                                    numérica
                                                             Pendiente: 1 (K1+2K2+2K3+K4)
                                                                        6
                                                 Solución                                              Solución
              y(x)                               exacta                                                exacta


                                         Pendiente: K4
 yi                                                           yi
                      Pendiente: K3
                                             x                                                     x
         xi                              xi+h                        xi                     xi+1= xi+h
                          h                                                       h



               Figure 10-12: The classical fourth-order Runge–Kutta method.
Universidad de Ingeniería y Tecnología                      Métodos Numéricos                             32 / 39
Método de Runge-Kutta de cuarto orden
  Algoritmo RK4 de un Paso

                                         *yi+1 = yi + h6 (k1 + 2k2 + 2k3 + k4 )


Donde:
                                             k1 = f (xi , yi )
                                                                          
                                                               h         h
                                             k2 = f xi + , yi + k1 ·
                                                              2         2
                                                               h         h
                                             k3 = f xi + , yi + k2 ·
                                                               2         2
                                             k4 = f (xi + h, yi + k3 · h)



Universidad de Ingeniería y Tecnología                         Métodos Numéricos   33 / 39
Ejercicio
Resuelva el mismo PVI anterior utilizando el método de RK4:
                                         dx
                                            = t 2 − 3x,    x(1) = 10.
                                         dt
Considerando el intervalo t ∈ [1; 3] y n = 4 subintervalos.




Universidad de Ingeniería y Tecnología                    Métodos Numéricos   34 / 39
Resolución por RK4
           i      ti          xi            k1        k2          k3          k4      xi+1
           0     1.0      10.0000        −29.0000   −6.6875    −23.4218     7.3827   3.1803
           1     1.5       3.1803        −7.2909    −1.0103    −5.7206      3.0400   1.7042
           2     2.0       1.7042        −1.1126    0.7842     −0.6381      2.0947   1.8104
           3     2.5       1.8104         0.8188    1.5172      0.9934      2.0787   2.4703
           4     3.0       2.4703




Universidad de Ingeniería y Tecnología                  Métodos Numéricos                     35 / 39
Análisis de Error
Dado el PVI y ′ (t) = f (t, y ), y (t0 ) = y0 , sea una aproximación numérica yi en los nodos con
paso h.

  Tipos de error
        Error local (EL ): Error cometido en un solo paso aisladamente, asumiendo que los
        datos del nodo anterior fuesen exactos.

                                         EL = y (ti+1 ) − yi+1,local

        Error global (EG ): Error acumulado real al avanzar desde el origen t0 hasta tn .

                                             EG = y (tn ) − yn

Ejemplo: Para el método de Euler el error local es O(h2 ) y el global es O(h).




Universidad de Ingeniería y Tecnología                Métodos Numéricos                     36 / 39
Error Local vs. Error Global




  Conclusiones
        Reducir h disminuye los errores, pero incrementa el costo de cómputo.
        Emplear un método con mayor orden de error (como RK4) mejora
        drásticamente la precisión general.

Universidad de Ingeniería y Tecnología       Métodos Numéricos                  37 / 39
Tabla Comparativa de Métodos de un Paso
  Método de un paso                                           Orden p   Error local   Error global
  Euler (explícito)                                               1       O(h2 )         O(h)
  yi+1 = yi + h f (ti , yi )
  RK2–Heun                                                        2       O(h3 )         O(h2 )
  k1 = f (ti , yi ), k2 = f (ti + h, yi + hk1 )
  yi+1 = yi + h2 (k1 + k2 )
  RK4 Clásico                                                     4       O(h5 )         O(h4 )
  yi+1 = yi + h6 (k1 + 2k2 + 2k3 + k4 )
  RK de orden Pp (general)                                        p      O(hp+1 )        O(hp )
  yi+1 = yi + h bj kj
  RK23 (Bogacki–Shampine)                                         3       O(h4 )         O(h3 )
  Paso Adaptativo Ligero
  RK45 (Dormand–Prince / ode45)                                   5       O(h6 )         O(h5 )
  Solver estándar de MATLAB




Universidad de Ingeniería y Tecnología            Métodos Numéricos                             38 / 39

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
