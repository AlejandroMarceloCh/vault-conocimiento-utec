---
curso: IO1
titulo: Semana03-Capitulo2
slides: 37
fuente: Semana03-Capitulo2.pdf
---

x1   x2
       x1 x2



max     z = 50x1 + 70x2

40x1 + 30x2 ≤ 360
20x1 + 30x2 ≤ 480
x1 , x2 ≥ 0
C   C = {1, 2, … , ∣C∣}
P   P = {1, 2, … , ∣P ∣}
ui                i∈C
rij         j∈P
      i∈C
Rj                      j∈P

xi          i
max    z = ∑i∈C ui xi
s.t.   ∑i∈C rij xi ≤ Rj   , ∀j ∈ P
       xi ≥ 0             , ∀i ∈ C.
n
m



      xj       cj
                    xj   i
aij
           i                 bi

m
max    z = ∑nj=1 cj xj
s.t.   ∑nj=1 aij xj ≤ bi   ∀i ∈ {1, … , m}
       xj ≥ 0              ∀j ∈ {1, … , n}
min    z = ∑nj=1 cj xj
s.t.   ∑nj=1 aij xj ≥ bi   ∀i ∈ {1, … , m}
       xj ≥ 0              ∀j ∈ {1, … , n}
x1 = 4 x2 = 2
max    z = x1 + x2
s.t.   x1            ≥ x2
       x1            ≤ 60 − 3x2
       x1 , x2       ≥ 0.
max    z = x1 + x2
s.t.   x1            > x2
       x1            < 60 − 3x2
       x1 , x2       ≥ 0.
max    z = x1 + x2
s.t.   x21           ≥ x2
       x1            ≤ 60 − 3x2
       x1 , x2       ≥ 0.
max    z = x1 + x2
s.t.   ∣x1 ∣         ≥ 30
       x1            ≤ 60 − 3x2
       x1 , x2       ≥ 0.

max    z = x1 + x2
s.t.   x1            ≥ ∣u∣
       x1            ≤ v − 3x2
       x1 , x2       ≥ 0.
u v
max    z = x1 + x2
s.t.   x1            ≥ u
       x1            ≤ v − 3x2
       x1 , x2       ≥ 0.
u v
x = (x1 , x2 , … , xn )T
b = (b1 , b2 , … , bm )T

c = (c1 , c2 , … , cn )T

A                          aij   m×n
Forma estaˊndar   Forma cano
                           ˊnica
max    cT x       max    cT x
s.t.   Ax ≤ b     s.t.   Ax = b
       x≥0               x≥0
z          −z

    z∗
    −z ∗
    Ax

b
max z = x1   + 2x2
s.t.    x1   + x2        ≤6
               x2        ≤3
               x1 , x2   ≥0
x1 + x2 ≤ 6
S                       N∗
                    S        S1 S2
            s1 s2            S1 S2

    s1 s2
S                                        N∗
                                 S   n
S1 , S2 , … , Sn
                   s1 , … , sn
S1 , … , Sn

      max{s1 , … , sn } min{s1 , … , sn }

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
