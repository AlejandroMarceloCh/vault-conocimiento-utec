---
curso: METNUM
titulo: 10 - Semana 9/Sem9_Laboratorio de Spline Cúbico y Ajuste de Curvas
slides: 45
fuente: 10 - Semana 9/Sem9_Laboratorio de Spline Cúbico y Ajuste de Curvas.pdf
---

Métodos Numéricos
Interpolación - Spline
Sesión 09

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

1 Interpolación



2 Splines



3 Ajuste de Curvas



4 Linealización




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 18, 2026   1 / 44
        Objetivos
            Implementar en MATLAB polinomios interpolantes y funciones spline para
            aproximar datos discretos provenientes de aplicaciones de ingeniería.
            Implementar el método de mínimos cuadrados en MATLAB para ajustar
            modelos a datos experimentales y determinar los parámetros óptimos.




Universidad de Ingeniería y Tecnología       Métodos Numéricos             May 18, 2026   2 / 44
1
    INTERPOLACIÓN
    POLINOMIAL
Polinomios
Dado un polinomio de grado n: P(x) = an x n + an−1 x n−1 + . . . + a1 x + a0
       Crear un polinomio p(x) = 2x 3 − 6x + 5

         1   p=[2 0 -6 5]

       Evaluar el polinomio p en x = 2

         1   value01=polyval(p,2)

       Evaluar el polinomio p en x = 3 y x = 5

         1   values01=polyval(p,[3 5])



Universidad de Ingeniería y Tecnología   Métodos Numéricos             May 18, 2026   4 / 44
Continuación...
 Ejemplo
 Graficar el polinomio p(x) = 2x 3 − 6x + 5, para −4 ≤ x ≤ 4

Solución:

 1   xx=linspace(-4,4,50);
 2   yy=polyval(p,xx);
 3   plot(xx,yy,'r')
 4   title('Polinomio')
 5   xlabel('Eje X')
 6   ylabel('Eje Y')
 7   grid on




Universidad de Ingeniería y Tecnología   Métodos Numéricos     May 18, 2026   5 / 44
Continuación...
 Ejemplo
 Crear un polinomio mónico q(x), cuyas raíces sean x1 = 3 y x2 = 7.

Solución:
p(x) = x 2 − (3 + 7)x + 3 × 7 = (x − 3)(x − 7)

 1   q=poly([3 7])


 Ejemplo
 Halle el polinomio mónico cuyas raíces son:
        r1 = 3 de multiplicidad algebraica igual a 4.
        r2 = 4 de multiplicidad algebraica igual a 2.
        r3 = 6 de multiplicidad simple.
Universidad de Ingeniería y Tecnología      Métodos Numéricos     May 18, 2026   6 / 44
Interpolación Polinomial
Dado (n + 1) puntos (x0 ; y0 ), (x1 ; y1 ), . . . , (xn ; yn ) por dichos puntos pasa
exactamente un único polinomio a lo más de grado n
P(x) = an x n + an−1 x n−1 + . . . + a1 x + a0 ; Polinomio Interpolante
Evaluando en x0 :
P(x0 ) = an x0n + an−1 x0n−1 + . . . + a1 x0 + a0 = y0
Evaluando en los puntos restantes, tenemos:

                         x0 x0n−1 . . . x0 1
                        n                                       
                                                              an        y0
                       x n x n−1 . . . x1 1 an−1  y1 
                        1     1
                                               .. ..   ..  =  .. 
                                                                 
                        ..     ..     ..
                       .        .        . . .              .  .
                                    xnn xnn−1 . . . xn 1       a0       yn




Universidad de Ingeniería y Tecnología              Métodos Numéricos           May 18, 2026   7 / 44
Continuación
 Ejemplo
 Halle el polinomio interpolante que pase por los puntos (0; 5), (3; 2), (4; 6), (7; 9)

Solución:

 1   x=[0 3 4 7]'
 2   y=[5 2 6 9]'
 3   M=[x.^3 x.^2 x ones(4,1)] % Matriz de Vandermonde
 4   M=vander(x)
 5   p=M\y %inv(M)*y

Otra forma es utilizando el comando polyfit de Matlab:

 1   p=polyfit(x,y,length(x)-1)

Universidad de Ingeniería y Tecnología     Métodos Numéricos              May 18, 2026   8 / 44
Ejemplo
Utilice los nodos x0 = 2, x1 = 2.75 y x2 = 4 para obtener el polinomio interpolante
de segundo grado p(x) para f (x) = sin(x)ex . Graficar p(x) vs f (x).
Solución:

 1   x=[2 2.75 4]';
 2   f=@(x) (sin(x).*exp(x))
 3   y=f(x);
 4   p2=polyfit(x,y,2)
 5   xx=linspace(2,4);
 6   yy1=polyval(p2,xx);
 7   yy2=f(xx);
 8   plot(x,y,'ob',xx,yy1,'r',xx,yy2,'k')
 9   grid on
10   legend('Nodos','P. Interpolante','Funcion f(x)')




Universidad de Ingeniería y Tecnología   Métodos Numéricos           May 18, 2026   9 / 44
Método de Lagrange

 1   function p=lagrange(x,y)
 2       n=length(x);
 3       p=zeros(1,n);
 4       for k=1:n
 5           num=poly(x([1:k-1,k+1:n]));
 6           den=polyval(num,x(k));
 7           L=num/den;
 8           p=p+y(k)*L;
 9       end
10   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 18, 2026   10 / 44
Continuación...
 Ejemplo
 Halle el polinomio interpolante que pase por los puntos (0; 5), (3; 2), (4; 6), (7; 9).
 Utilizando el método de Lagrange.

Solución:

 1   x=[0 3 4 7]'
 2   y=[5 2 6 9]'
 3   p=lagrange(x,y)




Universidad de Ingeniería y Tecnología    Métodos Numéricos              May 18, 2026   11 / 44
Método de Newton: Tabla de Diferencias
Divididas

 1   function M=tabladif(x,y)
 2       n=length(x);
 3       M=zeros(n);
 4       M(1:n,1)=y;
 5       for k=1:n-1
 6           ∆x=x(k+1:n)-x(1:n-k);
 7           ∆y=diff(y)./∆x;
 8           M(1:n-k,k+1)=∆y;
 9           y=∆y;
10       end
11       M=[x M];
12   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 18, 2026   12 / 44
Método de Newton: Polinomio Interpolante

 1   function p=polynewton(x,y)
 2       M=tabladif(x,y)
 3       n=length(x);
 4       b=M(1,2:end);
 5       p=b(1);
 6       for k=2:n
 7           p=[0 p]+b(k)*poly(x(1:k-1));
 8       end
 9   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 18, 2026   13 / 44
Ejemplo

Halle el polinomio interpolante que pase por los puntos (0; 5), (3; 2), (4; 6), (7; 9).
Utilizando el método de Newton.

 1   x=[0 3 4 7]';
 2   y=[5 2 6 9]';
 3   M=tabladif(x,y)
 4   p=polynewton(x,y)




Universidad de Ingeniería y Tecnología    Métodos Numéricos              May 18, 2026   14 / 44
Aplicación de Interpolación
Los datos que se muestran en la siguiente tabla son las velocidades que registra un
paracaidista que se lanza desde un avión:

                                         Tiempo (s)   Velocidad (m/s)
                                             1               5
                                             2              23
                                             3              25
                                             4              26

Basado en esta información:
       Halle el polinomio interpolante de Lagrange y Newton.
       Luego de hallar el polinomio interpolante, determine la velocidad alcanzada por
       el paracaidista en el instante t = 2, 5 segundos.
       Graficar el polinomio interpolante.

Universidad de Ingeniería y Tecnología                Métodos Numéricos   May 18, 2026   15 / 44
2   SPLINES
Spline Cúbico
Una función S(x) es un spline de grado 3 (spline cúbico) definido en el intervalo
[a; b] si se cumple:
       S(x) es continua en [a; b].
       S ′ (x) es continua en [a; b].
       S ′′ (x) es continua en [a; b].




Universidad de Ingeniería y Tecnología   Métodos Numéricos          May 18, 2026   17 / 44
Continuación...
La forma de cada Spline Cúbico para cada subintervalo es:

                        Sk (x) = ak (x − xk )3 + bk (x − xk )2 + ck (x − xk ) + dk

donde x ∈ [xk ; xk +1 ] y k = 0, 1, 2, . . . , n − 1. n es el número de subintervalos.
Nota:
Si S ′′ (x0 ) = S ′′ (xn ) = 0 se denomina el Spline Cúbico Natural.




Universidad de Ingeniería y Tecnología             Métodos Numéricos                 May 18, 2026   18 / 44
Spline Natural
 1   function S=splinenatural(X,Y)
 2   N=length(X)-1; H=diff(X); E=diff(Y)./H;
 3   diagprinc=2*(H(1:N-1)+H(2:N)); diagsupinf=H(2:N-1);
 4   g0=0; gn=0;
 5   A=diag(diagprinc)+diag(diagsupinf,1)+diag(diagsupinf,-1);
 6   b=6*diff(E'); g=A\b;
 7   g=[g0 g' gn];
 8   for i=1:N
 9       S(i,1)=(g(i+1)-g(i))/(6*H(i));
10       S(i,2)=g(i)/2;
11       S(i,3)= E(i)-H(i)*(g(i+1)+2*g(i))/6;
12       S(i,4)=Y(i);
13       xx=linspace(X(i),X(i+1),100);
14       yy=S(i,1)*(xx-X(i)).^3+S(i,2)*(xx-X(i)).^2+S(i,3)*(xx-X(i))+S(i,4);
15       plot(xx,yy), hold on
16   end
17   grid on, hold off
18   end
Universidad de Ingeniería y Tecnología   Métodos Numéricos    May 18, 2026   19 / 44

Ejemplo
Obtener una interpolación por spline cúbico natural para el polinomio p(x) = x 4 ,
para x = 0, 1, 2, 3. Muestre el Spline S(x) para cada subintervalo.
Solución:

 1   clf
 2   x=[0 1 2 3];
 3   y=x.^4;
 4   S=splinenatural(x,y)

                       S0 (x) = 0.4(x − 0)3 + 0(x − 0)2 + 0.6(x − 0) + 0,
                      
                                                                                    x ∈ [0, 1]
               S(x) =   S (x) = 12(x − 1)3 + 1.2(x − 1)2 + 1.8(x − 1) + 1,          x ∈ [1, 2]
                       1
                        S2 (x) = −12.4(x − 2)3 + 37.2(x − 2)2 + 40.2(x − 2) + 16,   x ∈ [2, 3]




Universidad de Ingeniería y Tecnología              Métodos Numéricos                    May 18, 2026   20 / 44
Comando Spline
Si x e y son los vectores que contienen los puntos iniciales, la orden Matlab:

                                         y ∗ = spline(x, y, x ∗ )

calcula el valor y ∗ = S(x ∗ ), siendo S(x) la función definida por los splines cúbicos.
Si se desea la función S(x), se deben generar un número suficiente de valores de
la gráfica de S(x).
El comando de Matlab Spline, impone como condición adicional la derivada tercera
continua en el segundo y en penúltimo nodo.




Universidad de Ingeniería y Tecnología             Métodos Numéricos    May 18, 2026   21 / 44
Ejemplo

Se desea diseñar la trayectoria plana a seguir por un brazo robot para que trasporte
diferentes piezas de un lugar a otro. Dicho mecanismo ha de moverse de forma
suave para que no caigan los elementos transportados, y para que no se dañen sus
articulaciones. Se ha de diseñar la trayectoria con un número de puntos por los que
debe pasar: partiendo de punto inicial que suponemos el origen (0, 0), el brazo
debe dirigirse al punto (7, 6) en donde recogerá una pieza, aunque previamente
tendrá que pasar por dos puntos de control, el (2, 4) y el (6, 4). Finalmente debe
llegar hasta el punto (15, 1) en donde dejará la pieza en cuestión, pero pasando
antes por el punto de control (12, 7).




Universidad de Ingeniería y Tecnología   Métodos Numéricos           May 18, 2026   22 / 44
Polinomio interpolante (6 puntos, grado 5)

 1   x=[0 2 6 7 12 15]
 2   y=[0 4 4 6 7 1]
 3   p=polyfit(x,y,5)
 4   xx=[0:0.01:15];
 5   yy=polyval(p,xx);
 6   plot(x,y,'or',xx,yy,'b')
 7   grid on




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 18, 2026   23 / 44
Spline

 1   %Calculo de 100 puntos de la ...
         grafica de S(x)
 2   xx=linspace(0,15,100);
 3   yy=spline(x,y,xx);
 4   %Dibujo de la funcion ...
         interpoladora
 5   %S(x) sobre el conjunto de ...
         datos (x,y)
 6   hold on
 7   plot(xx,yy,'m')
 8   legend('Data','Interpolacion',...
 9       'Spline')




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 18, 2026   24 / 44
3
    AJUSTE
    DE CURVAS
Ajuste Lineal
Dado (x1 ; y1 ), (x2 ; y2 ), . . . , (xn ; yn ), la función ajuste lineal es: g(x) = a1 x + a0 ,
función ajuste lineal.

 Ejemplo
 Dado los puntos (1; 4), (3; 7), (10; 12), (16; 18), halla la función ajuste lineal (re-
 gresora) g1 (x) = a1 x + a0


 1   x=[1 3 10 16]'
 2   y=[4 7 12 8]'
 3   g1=polyfit(x,y,1)
 4   xx=linspace(1,16,50);
 5   yy=polyval(g1,xx);
 6   plot(x,y,'ob',xx,yy,'r')
 7   grid on
 8   title('Ajuste Lineal')

Universidad de Ingeniería y Tecnología          Métodos Numéricos                  May 18, 2026    26 / 44
Continuación...
Otra forma de hallar la función ajuste lineal es formando un sistema
sobredeterminado, para ello reemplazamos los puntos en la función

                                           g1 (x) = a1 x + a0
                                                         
                                           1 1            4
                                          3 1 a1        7
                                         10 1 a0 = 12
                                                         

                                          16 1              8


 1   M=[x ones(4,1)]




Universidad de Ingeniería y Tecnología           Métodos Numéricos     May 18, 2026   27 / 44
Continuación...
Mu = y
M T Mu = M T y ; Ecuaciones Normales
u = (M T M)−1 M T y
Donde:                                      
                                            a
                                         u= 1
                                            a0


 1   u=inv(M'*M)*M'*y




Universidad de Ingeniería y Tecnología    Métodos Numéricos   May 18, 2026   28 / 44
Bondad de Ajuste Lineal
                                                                   b 2
                                                        Pn            
                                             2          i=1 yi − yi
                                         R       = 1 − Pn              2
                                                         i=1 (yi − ȳ )



Donde:
ybi = a1 xi + a0 de la función ajuste
yi de la data
      Xn
          yi
ȳ = i=1n




Universidad de Ingeniería y Tecnología                   Métodos Numéricos   May 18, 2026   29 / 44
Ejemplo
Dado los siguientes puntos:

                                         X   0    3     4      7       9
                                         Y   0   30    60     90      120

Determinar la calidad del ajuste lineal.
Solución:

 1   x=[0 3 4 7 9]'
 2   y=[0 30 60 90 120]'
 3   p1=polyfit(x,y,1)
 4   yc=polyval(p1,x)
 5   R2 = 1 - sum((y - yc).^2)/sum((y - mean(y)).^2)




Universidad de Ingeniería y Tecnología                Métodos Numéricos     May 18, 2026   30 / 44
Ajuste Cuadrático
Dado (x1 ; y1 ), (x2 ; y2 ), . . . , (xn ; yn ), la función ajuste cuadrático es:
g(x) = a2 x 2 + a1 x + a0 , función ajuste cuadrático.

 Ejemplo
 Dado los puntos (1; 4), (3; 7), (10; 12), (16; 18), halla la función ajuste cuadrático
 (regresora) g2 (x) = a2 x 2 + a1 x + a0


 1   x=[1 3 10 16]'
 2   y=[4 7 12 8]'
 3   M=[x.^2 x ones(4,1)]
 4   u=inv(M'*M)*M'*y
 5   u=polyfit(x,y,2)




Universidad de Ingeniería y Tecnología          Métodos Numéricos                   May 18, 2026   31 / 44
4   LINEALIZACIÓN
Ajuste Exponencial
Se desea ajustar una curva exponencial de la forma

                                            g(x) = CeAx               (2)

a un conjunto de datos {(xk ; yk )}N
                                   k =1 dado de antemano. Tomando logaritmo en (2):

                                              ln(g(x)) = Ax + ln(C)

Haciendo un cambio de variables (y de constante):

                                         Y = ln(g(x)), X = x, B = ln(C).

se obtiene una relación lineal entre las nuevas variables X y Y :

                                                  Y = AX + B


Universidad de Ingeniería y Tecnología                 Métodos Numéricos    May 18, 2026   33 / 44
Ejemplo
Dado los puntos (1; 4), (3; 7), (10; 12), (16; 8), halle la función regresora
g(x) = CeAx

 1   x1=[1 3 10 16]'
 2   y1=[4 7 12 8]'
 3   X=x1;
 4   Y=log(y1)
 5   g1=polyfit(X,Y,1)
 6   A=g1(1)
 7   C=exp(g1(2))
 8   syms x
 9   g=inline(subs(C*exp(A*x)),'x')
10   xx=linspace(1,16,50);
11   yy=g(xx);
12   plot(xx,yy,'r',x1,y1,'ob')
13   grid on


Universidad de Ingeniería y Tecnología    Métodos Numéricos              May 18, 2026   34 / 44
Aplicación
A partir del conjunto de datos accidents, cargue los datos de accidentes en la
variable y y los datos de población de estado en la variable x.
Encuentre la relación de regresión lineal y = β1 x entre los accidentes ocurridos en
un estado y la población de un estado mediante el operador \. El operador \ realiza
una regresión de mínimos cuadrados.

 1   load accidents
 2   x = hwydata(:,14); %Population of states
 3   y = hwydata(:,4); %Accidents per state
 4   format long
 5   b1 = x\y




Universidad de Ingeniería y Tecnología   Métodos Numéricos           May 18, 2026   35 / 44
Continuación...
b1 =
1.372716735564871e − 04
b1 es la pendiente o el coeficiente de regresión. La relación lineal es
y = β1 x = 0.0001372x.
Calcule los accidentes por estado y asigne a la variable yc1 para los valores de x
utilizando la relación y = β1 x. Visualice la regresión representando los valores
reales y y los valores calculados yc1.

 1   yc1 = b1*x;
 2   scatter(x,y,'r')
 3   hold on
 4   plot(x,yc1,'b')
 5   xlabel('Poblacion del estado')
 6   ylabel('Accidentes de trafico mortales por estado')
 7   title('Relacion de regresion lineal')
 8   grid on
Universidad de Ingeniería y Tecnología   Métodos Numéricos            May 18, 2026   36 / 44
Continuación...
Mejore el ajuste mediante la inclusión de una intersección sobre el eje Y en β0 de
la forma
                                   y = β1 x + β0
Calcule β0 y β1 utilizando el operador \

 1   X = [ones(length(x),1) x]
 2   format long
 3   b = X\y

Este resultado representa la relación y = β1 x + β0 = 142.7120 + 0.0001256x




Universidad de Ingeniería y Tecnología     Métodos Numéricos        May 18, 2026   37 / 44
Continuación...
Representación gráfica:

 1   yc2 = X*b;
 2   plot(x,yc2,'--')
 3   legend('Data','Slope','Slope & Intercept');

En la figura obtenida, se observa que las dos funciones regresoras tienen un
aspecto similar. Un método para encontrar el mejor ajuste es calcular el coeficiente
de determinación, R 2 .

 1   Rsq1 = 1 - sum((y - yc1).^2)/sum((y - mean(y)).^2)
 2   Rsq2 = 1 - sum((y - yc2).^2)/sum((y - mean(y)).^2)

¡Comente sus resultados!


Universidad de Ingeniería y Tecnología   Métodos Numéricos           May 18, 2026   38 / 44
Ejercicio 1 - Examen EL2 - 2025-0
Al construir un spline cúbico natural para aproximar f (x) = cos(π x) en el intervalo
x ∈ [0, 1], utilizando los siguientes puntos: x0 = 0, x1 = 0.25, x2 = 0.5, x3 = 0.75 y x4 = 1,
se obtuvo lo siguiente:
       
       
       S0 (x) = a0 x 3 + b0 x 2 + c0 x + d0 ,                               si 0 ≤ x ≤ 0.25,
       S (x) = a (x − 0.25)3 + b (x − 0.25)2 + c (x − 0.25) + d , si 0.25 ≤ x ≤ 0.5,
       
         1        1                    1                  1                1
S(x) =                         3                2
       
       
       S2 (x) = a2 (x  − 0.5)   + b 2 (x − 0.5)  + c 2 (x  − 0.5) + d 2 ,   si 0.5 ≤ x ≤ 0.75,
        S3 (x) = a3 (x − 0.75)3 + b3 (x − 0.75)2 + c3 (x − 0.75) + d3 , si 0.75 ≤ x ≤ 1.
       


       Halle el valor de c2 y asígnelo a la variable C.
       Utilizando el spline cúbico natural, halle S(0.6) y asigne el valor a valor1.
       Halle S ′ (0.6) y asigne el valor a la variable valor2.
       Halle S ′′ (1) y asigne el valor a la variable valor3.


Universidad de Ingeniería y Tecnología          Métodos Numéricos              May 18, 2026   39 / 44

Ejercicio 2 - Examen EL2 - 2025-0
Considere la gráfica de la función f (x) = log3 (x) − cos(x) en puntos del dominio
[1, 8] (la gráfica siguiente muestra el eje x en paso de 1 : 0.5 : 8.5)

                                                                                    I
                                         D   E
                                                                         H
                                                      F              G
                       C

                 B


             A

se le pide implementar un script que efectúe lo siguiente:


Universidad de Ingeniería y Tecnología           Métodos Numéricos           May 18, 2026   40 / 44
Ejercicio 2 - Examen EL2 - 2025-0
   1   Crear un vector fila llamado xx que almacene las respectivas abscisas de los puntos
       marcados en la gráfica.
   2   Crear un vector fila llamado yy que almacene las respectivas ordenadas de los puntos
       marcados en la gráfica.
   3   Encuentre el polinomio P interpolante de Newton (diferencias divididas) y almacene el
       valor de P(6) en la variable newton6.
   4   Encuentre el polinomio Q interpolante de Lagrange y almacene el valor de Q(6) en la
       variable Lagrange6.
   5   Utilice splines cúbico natural para encontrar el polinomio S interpolante (con la nube
       de puntos dada al inicio) y almacene S(6) en la variable spcubic6.
   6   Bajo el criterio del error relativo, determine cuál de los polinomios encontrados en los
       puntos 3, 4 y 5 se aproxima peor a f (6). Si considera que lo hace Newton, asigne la
       variable op = 1; si lo hace Lagrange, asigne op = 2; y si lo hace el spline cúbico, asigne
       op = 3.


Universidad de Ingeniería y Tecnología         Métodos Numéricos                May 18, 2026   41 / 44
Actividad de Bonificación - Salida (AB-S4)
Indicaciones

    Descargue el archivo .mlx desde Canvas
    Una vez terminada la actividad, suba a
    Canvas el archivo .mlx con el siguiente
    nombre: Nombre_ApellidoPaterno.mlx
    Responda usando comandos de MATLAB
    cuando corresponda.
    Cuando se indique, guarde los resultados en
    las variables especificadas.
   Justifique brevemente sus respuestas
   cuando corresponda.



Universidad de Ingeniería y Tecnología        Métodos Numéricos   May 18, 2026   42 / 44
Conclusiones
       La interpolación polinomial (Lagrange/Newton) es útil pero puede oscilar
       excesivamente con muchos puntos.
       Los Splines cúbicos ofrecen una aproximación más suave por tramos, ideal
       para trayectorias.
       La elección del método depende de la naturaleza de los datos y la precisión
       requerida.




Universidad de Ingeniería y Tecnología   Métodos Numéricos            May 18, 2026   43 / 44

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
