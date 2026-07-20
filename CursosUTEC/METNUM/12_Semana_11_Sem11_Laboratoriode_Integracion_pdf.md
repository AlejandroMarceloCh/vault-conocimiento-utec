---
curso: METNUM
titulo: 12 - Semana 11/Sem11_Laboratoriode Integración
slides: 32
fuente: 12 - Semana 11/Sem11_Laboratoriode Integración.pdf
---

Métodos
Numéricos
Integración - S11
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
                                                      Índice
                                            1 Integración  Numérica
                                              (Newton-Cotes)
                                            2 Integración Numérica
                                              (Romberg)
                                            3 Integración Numérica
                                              (Cuadratura Gaussiana)




Universidad de Ingeniería y Tecnología   Métodos Numéricos       June 1, 2026   1 / 31
        Objetivos:
            Implementar en MATLAB las reglas de Newton–Cotes (Trapecio y Simpson)
            para aproximar integrales definidas y analizar la influencia del número de
            subintervalos en la precisión.
            Aplicar en MATLAB la cuadratura de Gauss utilizando nodos y pesos óptimos
            para aproximar integrales definidas y evaluar su precisión.
            Implementar el método de Romberg en MATLAB aplicando la extrapolación de
            Richardson para mejorar la aproximación de integrales definidas.




Universidad de Ingeniería y Tecnología        Métodos Numéricos              June 1, 2026   2 / 31
1   INTEGRACIÓN

    NUMÉRICA
    (Newton-Cotes)
Integración Numérica
Método del Trapecio
                                Z x1
                                                      h                       h3 ′′
                                         f (x) dx =     [f (x0 ) + f (x1 )] −    f (ξ )
                                  x0                  2                       12


Donde: h = x1 − x0

Método de Simpson
                       Z x2
                                              h                                  h5 (4)
                               f (x) dx =       [f (x0 ) + 4f (x1 ) + f (x2 )] −    f (ξ )
                          x0                  3                                  90


Donde: h = x2 − x1 = x1 − x0

Universidad de Ingeniería y Tecnología                      Métodos Numéricos                June 1, 2026   4 / 31
Continuación...
Método del Trapecio Compuesto
                                                  
         Z b                       n−1
                       h           X                  b − a 2 ′′
             f (x) dx = f (a) + 2     f xj + f (b) −      h f (μ)
           a           2                                12
                                                j=1


                    (b − a)
Donde: h =                  , xj = a + jh, para cada j = 0, 1, . . . , n
                       n
Método de Simpson Compuesto

                                                                 
Z b                          (n/2)−1           n/2
                h             X              X                     b − a 4 (4)
     f (x) dx =    f (a) + 2         f x2j + 4     f x2j−1 + f (b) −      h f (μ)
   a            3                                                      180
                                         j=1            j=1


                    (b − a)
Donde: h =                  , xj = a + jh, para cada j = 0, 1, . . . , n
                       n
Universidad de Ingeniería y Tecnología             Métodos Numéricos       June 1, 2026   5 / 31
Ejemplo                                  Z 3
Aproximar la siguiente integral                x 2 dx
                                          1
       Utilizando el método del Trapecio. Hallar el error.

         1   f=@(x)(x^2)
         2   syms x
         3   Vexacto=int(f(x),1,3)
         4   Vex=vpa(Vexacto,4) % redondea a 4 decimales
         5   a=1; b=3; h=b-a;
         6   Itrap=(h/2)*(f(a)+f(b))




Universidad de Ingeniería y Tecnología                  Métodos Numéricos   June 1, 2026   6 / 31
Continuación...
       Utilizando el método de Simpson. Hallar el error.

         1   f=@(x)(x^3)
         2   syms x
         3   Vexacto=int(f(x),1,3)
         4   Vex=vpa(Vexacto,4) % redondea a 4 decimales
         5   a=1; b=3; h=(b-a)/2;
         6   Isimp=(h/3)*(f(a)+4*f(a+h)+f(b))




Universidad de Ingeniería y Tecnología    Métodos Numéricos   June 1, 2026   7 / 31
Continuación...

       Utilizando el método del Trapecio Compuesto. Considere 4 subintervalos.
       Hallar el error.

         1   f=@(x)(x^2)
         2   f1=@(x)(x.^2)
         3   syms x
         4   Vexacto=int(f(x),1,3)
         5   Vex=vpa(Vexacto,4) % redondea a 4 decimales
         6   a=1; b=3; N=4;
         7   h=(b-a)/N; %N es el numero de subintervalos
         8   x=[a:h:b];
         9   Itrapcomp=(h/2)*(f1(a)+2*sum(f1(x(2:length(x)-1)))+f1(b))



Universidad de Ingeniería y Tecnología   Métodos Numéricos           June 1, 2026   8 / 31
Continuación...
       Utilizando el método de Simpson Compuesto. Considere 4 subintervalos.
       Hallar el error.

         1   f=@(x)(x^2)
         2   f1=@(x)(x.^2)
         3   syms x
         4   Vexacto=int(f(x),1,3)
         5   Vex=vpa(Vexacto,4) % redondea a 4 decimales
         6   a=1; b=3; N=4;
         7   h=(b-a)/N; %N es el numero de subintervalos
         8   x=[a:h:b];
         9   xpar=x(2:2:length(x)-1);
       10    ximpar=x(3:2:length(x)-2);
       11    Isimpcomp=(h/3)*(f1(a)+4*sum(f1(xpar))+2*sum(f1(ximpar))+f1(b))
       12    Error=vpa(abs(Vex-Isimpcomp),4)

Universidad de Ingeniería y Tecnología   Métodos Numéricos         June 1, 2026   9 / 31
Ejercicio
Calcule el valor exacto y valor aproximado de la siguiente integral:
                         Z 0.8
                   I=            (0.2 + 25x − 200x 2 + 675x 3 − 900x 4 + 400x 5 ) dx
                           0

El valor aproximado debe ser calculado por los diferentes métodos vistos en esta
sección.




Universidad de Ingeniería y Tecnología              Métodos Numéricos             June 1, 2026   10 / 31
Funciones en Matlab
Ejercicio 1
Implementar la función Trapecio Compuesto, con la siguiente cabecera:

 1   function I=trapecomp(f,a,b,h)


Ejercicio 2
Implementar la función Simpson Compuesto, con la siguiente cabecera:

 1   function I=simpcomp(f,a,b,h)




Universidad de Ingeniería y Tecnología   Métodos Numéricos       June 1, 2026   11 / 31
El comando quad de Matlab
La sintaxis del comando quad, basado en el método adaptativo de integración de
Simpson, es la siguiente:




Universidad de Ingeniería y Tecnología   Métodos Numéricos       June 1, 2026   12 / 31
Ejemplo
Utilizar integración numérica para calcular la siguiente integral:
                                         Z 8
                                                       0.8
                                               (xe−x         + 0.2) dx
                                          0

Solución:

 1   f=@(x)(x.*exp(-x.^(0.8))+0.2)
 2   I=quad(f,0,8)

También:

 1   I=quad('x.*exp(-x.^(0.8))+0.2',0,8)


Universidad de Ingeniería y Tecnología                 Métodos Numéricos   June 1, 2026   13 / 31
El comando trapz de Matlab
Este comando se puede utilizar para integrar una función que se da en forma de
datos o puntos. Este método utiliza integración por el método de los trapecios. La
sintaxis de este comando es:

                                         q=trapz(X,Y)

donde X e Y son vectores con las coordenadas x e y de los puntos que se van a
integrar. Los dos vectores deben tener el mismo tamaño.




Universidad de Ingeniería y Tecnología       Métodos Numéricos      June 1, 2026   14 / 31
Ejemplo
Halle el área bajo la curva formada por los siguientes datos tabulados:

                                         X 0 0, 1 0, 2 0, 3 0, 4 0, 5
                                         Y 1 7     4    3    5    2

Solución:

 1   x=[0 0.1 0.2 0.3 0.4 0.5]
 2   y=[1 7 4 3 5 2]
 3   %Utilizando el comando trapz de Matlab
 4   I=trapz(x,y)

¿Cuál sería el valor del área si se utiliza el método de Simpson Compuesto?


Universidad de Ingeniería y Tecnología               Métodos Numéricos   June 1, 2026   15 / 31
    Método de Romberg

2
Método de Romberg
       Si consideramos que se ha aplicado el método del trapecio simple con tamaño
       de paso h1 obteniendo la aproximación I(h1 ), siendo h2 una "mejora" de h1
       (por ejemplo h2 = h21 ), obtenemos una mejor aproximación I(h2 ).
       Finalmente combinando estas dos aproximaciones obtenemos una tercera
       "mejor" aproximación I.
       Es decir:

  Extrapolación de Richardson
                                                            4         1
                                              I         ≈     I(h2 ) − I(h1 )
                                            |{z}            3 | {z } 3 | {z }
                                         mejor aprox.        aprox. 2        aprox. 1


       Nota: Las aproximaciones del trapecio compuesto son del orden O(h2 ),
       mientras que las mejoras son del orden O(h4 ).

Universidad de Ingeniería y Tecnología                       Métodos Numéricos          June 1, 2026   17 / 31
Ejemplo
       Para los cálculos utilizamos en toda esta sección la siguiente integral:
                             Z 0.8
                       I=            (0.2 + 25x − 200x 2 + 675x 3 − 900x 4 + 400x 5 ) dx
                               0

       cuyo valor exacto es 1.6405333333333.
       Y el siguiente script:

         1   function [Itrapcomp]=Tcomp(f,a,b,n)
         2       %f=@(x)(0.2+25*x-200*x.^2+675*x.^3-900*x.^4+400*x.^5)
         3       h=(b-a)/n; %N es el numero de subintervalos
         4       x=[a:h:b];
         5       Itrapcomp=(h/2)*(f(a)+2*sum(f(x(2:length(x)-1)))+f(b));
         6   end



Universidad de Ingeniería y Tecnología                Métodos Numéricos            June 1, 2026   18 / 31
Continuación...
Haciendo uso del script anterior realizamos algunas aproximaciones:

    Nro de interv. (n)              Tam. de paso (h)             I(h)      Error relativo (%)
            1                              0.8           0.1728000000000          89.5
            2                              0.4           1.0688000000000          34.9
            4                              0.2           1.4848000000000           9.5
            8                              0.1           1.6008000000000           2.4
           16                             0.05           1.6305500000000         0.006




Universidad de Ingeniería y Tecnología                 Métodos Numéricos         June 1, 2026   19 / 31

Algoritmo de Integración de Romberg
Las aproximaciones calculadas en la tabla anterior pueden ser tomadas como base
para construir otras mas exactas según el esquema general:

  Método de Romberg
                            4k −1                  1              4k −1 Ij+1,k−1 − Ij,k−1
                Ij,k =              Ij+1,k−1 −           Ij,k−1 =
                          4k −1 − 1            4k −1 − 1                 4k −1 − 1

       Ij+1,k −1 e Ij,k −1 son las integrales mas y menos exactas respectivamente.
       Ij,k la integral mejorada.
       k es el nivel de integración, siendo k = 1 (primera columna) la estimación
       original con la regla del trapecio.
       La primera columna inicia con un intervalo y luego va duplicando la cantidad
       de intervalos para cada fila de dicha primera columna.

Universidad de Ingeniería y Tecnología              Métodos Numéricos                June 1, 2026   20 / 31
Forma Tabular de Romberg
En la notación anterior j indica la fila y k la columna en una disposición tabular, por
ejemplo tenemos la siguiente distribución:


              k = 1 ; O(h2 )             k = 2 ; O(h4 )    k = 3 ; O(h6 )     k = 4 ; O(h8 )    k = 5 ; O(h10 )
 j =1              I11                        I12               I13                I14               I15
 j =2              I21                        I22               I23                I24
 j =3              I31                        I32               I33
 j =4              I41                        I42
 j =5              I51




Universidad de Ingeniería y Tecnología                    Métodos Numéricos              June 1, 2026   21 / 31
Método de Romberg (Funcionamiento)

 1   function [T,R]=romberg(fun,a,b,orden)
 2       interv=1;
 3       for j=1:orden
 4           T(j,1)=Tcomp(fun,a,b,interv);
 5           interv=interv*2;
 6       end
 7       for k=2:orden
 8           for j=1:(orden-k+1)
 9               T(j,k)=(4^(k-1)*T(j+1,k-1)-T(j,k-1))/(4^(k-1)-1);
10           end
11       end
12       R=T(1,orden);
13   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos     June 1, 2026   22 / 31
Método de Romberg (MatLab)




Universidad de Ingeniería y Tecnología   Métodos Numéricos   June 1, 2026   23 / 31
    Cuadratura Gaussiana

3
Preliminares
                                         Z b
       Dada la integral I =                    f (x) dx, en primer lugar transformamos los límites de
                                          a
       integración mediante el cambio de variable:

                                                       (b + a) + (b − a)z
                                                  x=
                                                                2
       donde
                                                                                     b−a
                                 z ∈ [−1; 1];          x ∈ [a; b]     y       dx =       dz
                                                                                      2
       En consecuencia:
              Z b            Z 1                               Z 1
                                   (b + a) + (b − a)z b − a
           I=     f (x) dx =     f                          dz =     g(z) dz
               a              −1            2           2         −1




Universidad de Ingeniería y Tecnología                    Métodos Numéricos                   June 1, 2026   25 / 31
Continuación
       Siendo:                                                                 
                                                        (b + a) + (b − a)z          b−a
                                         g(z) = f
                                                                 2                   2
       Entonces, de acuerdo al método de Cuadratura de Gauss, la integral se puede
       calcular mediante:
                 Z b            Z 1
              I=     f (x) dx =     g(z) dz
                  a
                              −1           
                          −1              1
               ≈1×g √           +1×g √
                            3               3
               ≈ 0.5556 × g(−0.7746) + 0.8889 × g(0) + 0.5556 × g(0.7746)

       Que son las aproximaciones con dos y tres puntos respectivamente, pudiendo
       usarse más puntos (según la tabla mostrada).

Universidad de Ingeniería y Tecnología                      Métodos Numéricos             June 1, 2026   26 / 31
Universidad de Ingeniería y Tecnología   Métodos Numéricos   June 1, 2026   27 / 31
Cuadratura para n puntos
En los módulos de Canvas (Semana 11) encontrarán un valioso código elaborado
por los estudiantes del ciclo 2022-2 para la cuadratura gaussiana con n puntos.
Este grupo registró el mayor rendimiento académico en la historia del curso, y su
trabajo destaca por la precisión, claridad y excelencia técnica.
Revisen este material con atención.




Universidad de Ingeniería y Tecnología   Métodos Numéricos         June 1, 2026   28 / 31
Aplicación EL2 - 2024 - 2
Una masa m está sujeta a un resorte de longitud libre b y rigidez k , tal y como se
aprecia en la figura siguiente:




El coeficiente de fricción entre la masa y la barra horizontal es μ. La aceleración de
la masa se puede expresar como: ẍ = −f (x), donde:
                                                                 
                                     k                     b
                      f (x) = −μg − (μb − x) 1 − √
                                     m                   b2 − x 2
Universidad de Ingeniería y Tecnología   Métodos Numéricos             June 1, 2026   29 / 31
...Continuación
Donde: m = 0.8kg, b = 0.4m, μ = 0.3, k = 80N/m y g = 9.81m/s2 . Si la masa se
libera desde el reposo en x = b, su velocidad en x = 0 está dada por:
                                    s
                                        Z b
                              v0 = 2        f (x) dx
                                               0


Realice lo siguiente:
  1   Determine el valor de v0 usando el cálculo simbólico con el comando int de Matlab,
      luego almacene su valor en la variable vexac .
  2   Utilice la cuadratura gaussiana de 3 puntos para encontrar el valor de v0 , luego
      almacene en la variable vgauss .
  3   Determine el error relativo porcentual generado por la aproximación vgauss con
      respecto a la integral exacta del ítem (1). Almacene dicho error en la variable ErrorG1.
  4    Determine el error relativo porcentual de la aproximación con respecto de la integral
       exacta del ítem (1) cuando se usa 7 puntos en la cuadratura gaussiana. Guarde dicho
       error en la variable ErrorG2.
Universidad de Ingeniería y Tecnología       Métodos Numéricos              June 1, 2026 30 / 31
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
