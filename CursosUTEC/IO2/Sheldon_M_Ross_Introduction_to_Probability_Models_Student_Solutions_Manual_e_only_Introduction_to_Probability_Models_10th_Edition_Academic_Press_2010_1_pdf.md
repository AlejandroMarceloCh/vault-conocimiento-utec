---
curso: IO2
titulo: Sheldon M Ross-Introduction to Probability Models, Student Solutions Manual (e-only)_ Introduction to Probability Models 10th Edition-Academic Press (2010) (1)
slides: 59
fuente: Sheldon M Ross-Introduction to Probability Models, Student Solutions Manual (e-only)_ Introduction to Probability Models 10th Edition-Academic Press (2010) (1).pdf
---

Student’s Manual to Accompany

  Introduction to
Probability Models
                    Tenth Edition




             Sheldon M. Ross
        University of Southern California
                Los Angeles, CA




     AMSTERDAM • BOSTON • HEIDELBERG • LONDON
        NEW YORK • OXFORD • PARIS • SAN DIEGO
     SAN FRANCISCO • SINGAPORE • SYDNEY • TOKYO
            Academic Press is an imprint of Elsevier
Academic Press is an imprint of Elsevier
30 Corporate Drive, Suite 400, Burlington, MA 01803, USA
525 B Street, Suite 1900, San Diego, California 92101-4495, USA
Elsevier, The Boulevard, Langford Lane, Kidlington, Oxford, OX5 1GB, UK

          2010 Elsevier Inc. All rights reserved.
Copyright c

No part of this publication may be reproduced or transmitted in any form or by any means, electronic or
mechanical, including photocopying, recording, or any information storage and retrieval system, without
permission in writing from the publisher. Details on how to seek permission, further information about the
Publisher’s permissions policies and our arrangements with organizations such as the Copyright Clearance
Center and the Copyright Licensing Agency, can be found at our website: www.elsevier.com/permissions.

This book and the individual contributions contained in it are protected under copyright by the Publisher
(other than as may be noted herein).

Notices
Knowledge and best practice in this ﬁeld are constantly changing. As new research and experience broaden our
understanding, changes in research methods, professional practices, or medical treatment may become necessary.

Practitioners and researchers must always rely on their own experience and knowledge in evaluating and
using any information, methods, compounds, or experiments described herein. In using such information or
methods they should be mindful of their own safety and the safety of others, including parties for whom they
have a professional responsibility.

To the fullest extent of the law, neither the Publisher nor the authors, contributors, or editors, assume any liability
for any injury and/or damage to persons or property as a matter of products liability, negligence or otherwise, or
from any use or operation of any methods, products, instructions, or ideas contained in the material herein.

ISBN: 978-0-12-381446-3


For information on all Academic Press publications
visit our Web site at www.elsevierdirect.com


Typeset by: diacriTech, India

09 10   9 8 7 6 5 4 3 2 1
                                                          Contents

Chapter 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Chapter 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Chapter 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Chapter 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
Chapter 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
Chapter 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
Chapter 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
Chapter 8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
Chapter 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
Chapter 10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
Chapter 11 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
Chapter 1

 1. S = {(R, R), (R, G), (R, B), (G, R), (G, G), (G, B),                 Now,
         (B, R), (B, G), (B, B)}
                                                                         P{win| throw i} = P{i before 7}
    The probability of each point in S is 1/9.
                                                                             ⎧
                                                                             ⎪
                                                                             ⎪       0 i = 2, 12
 3. S = {(e1 , e2 , …, en ), n ≥ 2} where ei ∈ (heads, tails}.               ⎪
                                                                             ⎪
                                                                             ⎪
                                                                             ⎪
    In addition, en = en−1 = heads and for i = 1, …,                         ⎪
                                                                             ⎪   i−1
                                                                             ⎪
    n − 2 if ei = heads, then ei+1 = tails.                                  ⎨ 5 + 1 i = 3, …, 6
                                                                             ⎪
                                                                           =
                                                                             ⎪
                                                                             ⎪
      P{4 tosses} = P{(t, t, h, h)} + P{(h, t, h, h)}                        ⎪
                                                                             ⎪       1 i = 7, 11
                                                                             ⎪
                                                                             ⎪
                      4                                                    ⎪
                                                                             ⎪
                                                                             ⎪
                  =2
                      1
                            =
                                1                                            ⎩ 13 − i i = 8, …, 10
                                                                             ⎪
                      2         8                                               19 − 1

      3                                                                  where above is obtained by using Problems 11
 5.     . If he wins, he only wins $1, while if he loses, he             and 12.
      4
      loses $3.                                                          P{win} ≈ .49.

 7. If (E ∪ F)c occurs, then E ∪ F does not occur, and so
    E does not occur (and so Ec does); F does not occur              17. Prob{end} = 1 − Prob{continue}
    (and so Fc does) and thus Ec and Fc both occur.
                                                                                     = 1 − P({H, H, H} ∪ {T, T, T})
    Hence,
                                                                                     = 1 − [Prob(H, H, H) + Prob(T, T, T)].
      (E ∪ F)c ⊂ Ec Fc
                                                                                                                         
                                                                                                       1 1 1     1 1 1
      If Ec Fc occurs, then Ec occurs (and so E does not),               Fair coin: Prob{end} = 1 −      · · + · ·
      and Fc occurs (and so F does not). Hence, neither E                                              2 2 2     2 2 2
      or F occurs and thus (E ∪ F)c does. Thus,                                                   3
                                                                                               =
                                                                                                  4
      Ec Fc ⊂ (E ∪ F)c                                                                                                  
                                                                                                      1 1 1     3 3 3
      and the result follows.                                            Biased coin: P{end} = 1 −      · · + · ·
                                                                                                      4 4 4     4 4 4
                                                                                                 9
 9. F = E ∪ FEc , implying since E and FEc are disjoint                                       =
    that P(F) = P(E) + P(FE)c .                                                                  16

                  ⎧                                                  19. E = event at least 1 six P(E)
                  ⎪
                  ⎪ i−1
                  ⎨      ,         i = 2, …, 7
                     36                                                        number of ways to get E   11
11. P{sum is i} =                                                          =                           =
                  ⎪
                  ⎪ 13 − i
                  ⎩        ,       i = 8, …, 12                                 number of sample pts     36
                      36
                                                                         D = event two faces are different P(D)
13. Condition an initial toss                                              = 1 − Prob(two faces the same)
                  12
                                                                                  6   5         P(ED)   10/36   1
      P{win} = ∑ P{win | throw i}P{throw i}                                =1−       = P(E|D) =       =       =
                  i=2                                                             36  6         P(D)     5/6    3




                                                                 4
                                                           Answers and Solutions                                               5

21. Let C = event person is color blind.                                33. Let S = event student is sophomore; F = event
                                                                            student is freshman; B = event student is boy;
     P(Male|C)
                                                                            G = event student is girl. Let x = number of
                         P(C|Male) P(Male)                                  sophomore girls; total number of students =
          =                                                                 16 + x.
              P(C|Male P(Male) + P(C|Female) P(Female)
                                                                                      10            10               4
                     .05 × .5                                               P(F) =         P(B) =        P(FB) =
          =                                                                         16 + x        16 + x          16 + x
              .05 × .5 + .0025 × .5                                            4
                                                                                    = P(FB) = P(F)P(B) =
                                                                                                             10
                                                                            16 + x                         16 + x
              2500   20
          =        =                                                          10
              2625   21                                                             ⇒x=9
                                                                            16 + x
23. P(E1 )P(E2 |E1 )P(E3 |E1 E2 ) · · · P(En |E1 · · · En−1 )           35. (a) 1/16
                     P(E1 E2 ) P(E1 E2 E3 )      P(E1 · · · En )            (b) 1/16
          = P(E1 )                          ···                             (c) 15/16, since the only way in which the
                      P(E1 ) P(E1 E2 )          P(E1 · · · En−1 )
                                                                                pattern H, H, H, H can appear before the pat-
          = P(E1 · · · En )                                                     tern T, H, H, H is if the ﬁrst four ﬂips all land
                                                                                heads.
25. (a) P{pair} = P{second card is same
                    denomination as ﬁrst}                               37. Let W = event marble is white.
                                                                                                 P(W|B1 )P(B1 )
                       = 3/51                                                P(B1 |W) =
                                                                                         P(W|B1 )P(B1 ) + P(W|B2 )P(B2 )
      (b) P{pair|different suits}                                                            1 1           1
              P{pair, different suits}                                                        ·                 3
            =                                                                          =     2 2       = 4 =
                 P{different suits}                                                      1 1     1 1       5    5
                                                                                           · + ·
            = P{pair}/P{different suits}                                                 2 2     3 2      12
                    3/51                                                39. Let W = event woman resigns; A, B, C are events
               =         = 1/13                                             the person resigning works in store A, B, C, respec-
                   39/51
                                                                            tively.
27. P(E1 ) = 1                                                               P(C|W)
    P(E2 |E1 ) = 39/51, since 12 cards are in the ace of                                        P(W|C)P(C)
    spades pile and 39 are not.                                                =
                                                                                 P(W|C)P(C) + P(W|B)P(B) + P(W|A)P(A)
     P(E3 |E1 E2 ) = 26/50, since 24 cards are in the piles                                 .70 ×
                                                                                                  100
     of the two aces and 26 are in the other two piles.                        =                  225
                                                                                       100         75         50
     P(E4 |E1 E2 E3 ) = 13/49                                                    .70 ×     + .60 ×     + .50
                                                                                       225         225       225
                                                                                  70  140    1
     So                                                                        =           =
                                                                                 225 225      2
     P{each pile has an ace} = (39/51)(26/50)(13/49)
                                                                        41. Note ﬁrst that since the rat has black parents and
29. (a) P(E|F) = 0                                                          a brown sibling, we know that both its parents are
      (b) P(E|F) = P(EF)/P(F) = P(E)/P(F) ≥                                 hybrids with one black and one brown gene (for
          P(E) = .6                                                         if either were a pure black then all their offspring
                                                                            would be black). Hence, both of their offspring’s
      (c) P(E|F) = P(EF)/P(F) = P(F)/P(F) = 1
                                                                            genes are equally likely to be either black or brown.
31. Let S = event sum of dice is 7; F = event ﬁrst                           (a) P(2 black genes | at least one black gene)
    die is 6.
                                                                                            P(2 black genes)
            1         1          P(F|S)                                            =
     P(S) = P(FS) =     P(F|S) =                                                       P(at least one black gene)
            6        36           P(S)
            1/36   1                                                                   1/4
          =      =                                                                 =       = 1/3
             1/6   6                                                                   3/4
6                                                 Answers and Solutions

     (b) Using the result from part (a) yields the                                      rb
                                                                                =
         following:                                                               rb + (r + c)r
                                                                                      b
         P(2 black genes | 5 black offspring)                                   =
                                                                                  b+r+c
                 P(2 black genes)
           =                                                  47. 1.        0 ≤ P(A|B) ≤ 1
                P(5 black offspring)
                                                                                       P(SB)   P(B)
           =
                        1/3                                        2.       P(S|B) =         =      =1
                                                                                       P(B)    P(B)
                1(1/3) + (1/2)5 (2/3)
                                                                   3.       For disjoint events A and D
           = 16/17
                                                                                           P((A ∪ D)B)
                                                                        P(A ∪ D|B) =
    where P(5 black offspring) was computed by con-                                           P(B)
    ditioning on whether the rat had 2 black genes.
                                                                                           P(AB ∪ DB)
                                               i                                       =
43. Let i = event coin was selected; P(H|i) =    .                                            P(B)
                                              10
                                                                                           P(AB) + P(DB)
                                5 1                                                    =
               P(H|5)P(5)         ·                                                            P(B)
    P(5|H) =              =    10   10
              10             10
                                 1 1                                                   = P(A|B) + P(D|B)
             ∑ P(H|i)P(i) ∑ 10 · 10
             i=1            i=1                                    Direct veriﬁcation is as follows:
                   5       1                                       P(A|BC)P(C|B) + P(A|BCc )P(Cc |B)
            =          =
                 10        11
                ∑i                                                      =
                                                                            P(ABC) P(BC)
                                                                                         +
                                                                                           P(ABCc ) P(BCc )
                i=1
                                                                             P(BC) P(B)     P(BCc ) P(B)
45. Let Bi = event ith ball is black; Ri = event ith ball
                                                                            P(ABC)   P(ABCc )
    is red.                                                             =          +
                                                                             P(B)      P(B)
                            P(R2 |B1 )P(B1 )
    P(B1 |R2 ) =
                  P(R2 |B1 )P(B1 ) + P(R2 |R1 )P(R1 )                       P(AB)
                                                                        =
                                   r         b                               P(B)
                                         ·
                =            b+r+c b+r
                                                                        = P(A|B)
                      r          b          r+c       r
                             ·        +            ·
                  b+r+c b+r              b+r+c b+r
Chapter 2

                                
                7               10     14              P{X = k}
 1. P{X = 0} =                       =          15.
                2                2     30             P{X = k − 1}
                                                                      n!
                                                                             pk (1 − p)n−k
               1                                                 (n − k)! k!
 3. P{X = −2} = = P{X = 2}                              =
               4                                                   n!
                                                                                pk−1 (1 − p)n−k+1
                    1                                     (n − k + 1)!(k − 1)!
      P{X = 0} =                                          n−k + 1 p
                    2                                   =
                                                              k     1−p

                        11                            Hence,
 5. P{max = 6} =           = P{min = 1}
                        36                             P{X = k}
                                                                   ≥ 1 ↔ (n − k + 1)p > k(1 − p)
                  1                                   P{X = k − 1}
      P{max = 5} = = P{min = 2}
                  4                                                    ↔ (n + 1)p ≥ k
                        7                             The result follows.
      P{max = 4} =         = P{min = 3}
                        36
                                                                                   n!
                         5                      17. Follows since there are                   permutations of n
      P{max = 3} =         = P{min = 4}                                       x1 ! · · · xr !
                        36                            objects of which x1 are alike, x2 are alike, …, xr are
                         1                            alike.
      P{max = 2} =         = P{min = 5}
                        12
                         1                      19. P{X1 + · · · + X k = m}
      P{max = 1} =         = P{min = 6}                    
                        36                                 n
                                                       =         (p + · · · + pk )m (pk+1 + · · · + pr )n−m
                                                           m 1
 7. p(0) = (.3)3 = .027

      p(1) = 3(.3)2 (.7) = .189                                     4      3  2
                                                             3 5       3   7    5  3    7
                                                21. 1−            −5          −
      p(2) = 3(.3)(.7)2 = .441                               10       10   10   2 10    10

      p(3) = (.7)3 = .343                       23. In order for X to equal n, the ﬁrst n − 1 ﬂips must
                                                    have r − 1 heads, and then the nth ﬂip must land
                                                    heads. By independence the desired probability is
             1            1         1
 9. p(0) =     , p(1) =     , p(2) = ,              thus
             2           10         5                     
                                                      n − 1 r −1
      p(3) =
              1
                , p(3.5) =
                              1                              p (1 − p)n−r xp
                                                      r−1
             10              10
                                                25. A total of 7 games will be played if the ﬁrst 6 result
      3                                             in 3 wins and 3 losses. Thus,
11.
      8
                                                                         6
                                                      P{7 games} =           p3 (1 − p)3
      10          10                                                   3
            10    1
13.   ∑      i    2                                   Differentiation yields
      i=7



                                            7
8                                                     Answers and Solutions

     d                                                            37. P{M ≤ x} = P{max(X 1 , …, X n ) ≤ x}
        P{7} = 20 3p2 (1 − p)3 − p3 3(1 − p)2
     dp
                                                                                     = P{X1 ≤ x, …, X n ≤ x}
             = 60p2 (1 − p)2 1 − 2p
                                                                                           
                                                                                           n
    Thus, the derivative is zero when p = 1/2. Taking                                  =         P{Xi ≤ x}
    the second derivative shows that the maximum is                                        i=1
                                                                                            n
    attained at this value.                                                            =x

                                                                                   d
27. P{same number of heads} = ∑ P{A = i, B = i}                        fM (x) =      P{M ≤ x} = nxn−1
                                                                                  dx
                                            i
                     k            n−k
         =∑              (1/2)k            (1/2)n−k                               31
             i
                     i             i                              39. E [X] =
                     k   n−k                                                      6
         =∑                    (1/2)n
                     i    i
             i                                                    41. Let Xi equal 1 if a changeover results from the ith
                      k     n−k
         =∑                       (1/2)n                              ﬂip and let it be 0 otherwise. Then
             i
                     k−i     i
                                                                                                             n
                 n
         =           (1/2)n                                            number of changeovers = ∑ Xi
                 k
                                                                                                             i=2

    Another argument is as follows:                                    As,
                                                                       E [Xi ] = P{Xi = 1} = P{ﬂip i − 1 = ﬂip i}
    P{# heads of A = # heads of B}
                                                                              = 2p(1 − p)
         = P{# tails of A = # heads of B}
                                                                       we see that
    since coin is fair                                                                                             n
                                                                       E[number of changeovers] = ∑ E [Xi ]
         = P{k − # heads of A = # heads of B}                                                                      i=2

         = P{k = total # heads}                                                                              = 2(n − 1)p(1 − p)

                                                                                       n
29. Each ﬂip after the ﬁrst will, independently, result           43. (a)     X = ∑ Xi
                                                                                   i=1
    in a changeover with probability 1/2. Therefore,
                                                                       (b) E [Xi ] = P{Xi = 1}
                                   n−1                                       = P{red ball i is chosen before all n
    P{k changeovers}=                      (1/2)n−1
                                    k                                              black balls}
                                                                                = 1/(n + 1) since each of these n + 1
         1     
                                                                                    balls is equally likely to be the
33. c      1 − x2 dx = 1
      −1                                                                           one chosen earliest
               1
              x3                                                            Therefore,
       c x−        =1
               3                                                                           n
                    −1
                         3                                                    E [X] = ∑ E [Xi ] = n/(n + 1)
                      c=                                                                   i=1
                         4
             
           3 1                                                    45. Let Ni denote the number of keys in box i,
    F(y) =       (1 − x2 )dx                                          i = 1, …, k. Then, with X equal to the number
           4 −1
                                                                                                                        k
           3       y3 2
         = y−
           4        3
                       + ,
                         3
                                         −1 < y < 1                    of collisions we have that X =                    ∑ (Ni − 1)+ =
                                                                                                                         i=1
                                                                        k
                          ∞
                               10      1
                                                                       ∑ (Ni − 1 + I{Ni = 0}) where I{Ni = 0} is equal
                                                                       i=1
35. P{X > 20}=                    dx =                                 to 1 if Ni = 0 and is equal to 0 otherwise. Hence,
                          20   x2      2
                                                          Answers and Solutions                                                          9
                k                                                                  r
     E[X] = ∑ (rpi − 1 + (1 − pi )r ) = r − k                          51. N = ∑ Xj where Xi is the number of ﬂips between
             i=1                                                                  i=1
                     k                                                       the (i − 1)st and ith head. Hence, Xi is geometric
             + ∑ (1 − pi )r                                                  with mean 1/p. Thus,
                    i=1
                                                                                         r
                                                                                                        r
    Another way to solve this problem is to let Y denote                     E[N] = ∑ E[X i ] =
                                                                                                        p
    the number of boxes having at least one key, and                                    i=1
    then use the identity X = r − Y, which is true since                                                       2
    only the ﬁrst key put in each box does not result in                      1             1                1
                                                                       53.       ,              −                  .
                                       k                                     n+1         2n + 1             n+1
    a collision. Writing Y = ∑ I{Ni > 0} and taking                                                j
                                                                                                        j − 2λ j
    expectations yields
                                      i=1
                                                                       55. (a) P(Y = j) = ∑               e   λ /j!
                                                                                                  i=0   i
                                  k                                                                             j
                                                                                                            λj     j
     E[X] = r − E[Y] = r − ∑ [1 − (1 − pi )r ]                                                = e−2λ           ∑ i 1 i 1j − i
                                i=1
                                                                                                            j! i=0
                           k
          = r − k + ∑ (1 − pi )r                                                                            (2λ) j
                                                                                              = e−2λ
                          i=1                                                                                 j!

47. Let Xi be 1 if trial i is a success and 0 otherwise.                                          ∞
                                                                                                        j −2λ j
                                                                             (b) P(X = i) = ∑             e  λ /j!
                                                                                                  j=i   i
    (a) The largest value is .6. If X1 = X2 = X3 , then
                                                                                                  1 − 2λ ∞       1
         1.8 = E[X] = 3E[X 1 ] = 3P{X 1 = 1}                                                  =
                                                                                                  i!
                                                                                                     e   ∑   ( j − i)!
                                                                                                                       λj
                                                                                                         j=i

         and so                                                                                   λ i − 2λ ∞ k
                                                                                              =
                                                                                                  i!
                                                                                                     e     ∑ λ /k!
         P{X = 3} = P{X1 = 1} = .6                                                                        k=0

                                                                                                        λi
         That this is the largest value is seen by Markov’s                                   = e−λ
                                                                                                        i!
         inequality, which yields
                                                                             (c) P(X = i, Y − X = k) = P(X = i, Y = k + i)
         P{X ≥ 3} ≤ E[X]/3 = .6
                                                                                                                     k + i −2λ λk+i
                                                                                                                 =         e
    (b) The smallest value is 0. To construct a probabil-                                                              i      (k + i)!
        ity scenario for which P{X = 3} = 0 let U be a                                                                   λi −λ λk
        uniform random variable on (0, 1), and deﬁne                                                             = e−λ      e
                                                                                                                         i!    k!
                1 if U ≤ .6                                                       showing that X and Y − X are independent
         X1 =
                0 otherwise                                                       Poisson random variables with mean λ. Hence,

                1 if U ≥ .4                                                                                                     λk
         X2 =                                                                                     P(Y − X = k) = e−λ
                0 otherwise                                                                                                     k!

                1 if either U ≤ .3          or   U ≥ .7                57. It is the number of successes in n + m independent
         X3 =                                                              p-trials.
                0 otherwise
         It is easy to see that                                        59. (a) Use the fact that F(Xi ) is a uniform (0, 1) ran-
                                                                               dom variable to obtain
         P{X1 = X2 = X3 = 1} = 0
                                                                                  p = P{F(X1 ) < F(X2 ) > F(X3 ) < F(X4 )}
                                                                                    = P{U1 < U2 > U3 < U4 }
49. E[X 2 ] − (E[X])2 = Var(X) = E(X − E[X])2 ≥ 0.
    Equality when Var(X) = 0, that is, when X is                                  where the Ui , i = 1, 2, 3, 4, are independent
    constant.                                                                     uniform (0, 1) random variables.
10                                                          Answers and Solutions
                  1  1  x2  1                                                                               n              n
     (b) p =                             dx4 dx3 dx2 dx1                65. Cov(X i , Xj ) = Cov(μi + ∑ aik Zk , μj + ∑ ajt Zt )
                  0     x1    0     x3                                                                         k=1             t=1
                  1  1  x2                                                                      n   n
                                                                                             = ∑ ∑ Cov(ajk Zk , ajt Zt )
             =                     (1 − x3 )dx3 dx2 dx1
                  0     x1    0                                                                t=1 k=1
                                                                                                n n
                  1 1                                                                      = ∑ ∑ aik ajt Cov(Zk , Zt )
             =               (x2 − x22 /2)dx2 dx1                                              t=1 k=1
                  0     x1                                                                      n
                  1                                                                         = ∑ aik ajk
                                                                                               k=1
             =         (1/3 − x12 /2 + x13 /6)dx1
                  0                                                          where the last equality follows since
             = 1/3 − 1/6 + 1/24 = 5/24                                                            1    if k = t
                                                                             Cov(Zk , Zt ) =
                                                                                                  0    if k = t
     (c) There are 5 (of the 24 possible) orderings such
         that X1 < X2 > X3 < X4 . They are as follows:                                                 2
                                                                        67. P{5 < X < 15} ≥
                                                                                                       5
         X2 > X4 > X3 > X1                                                            
                                                                                      1
         X2 > X4 > X1 > X3                                              69. Φ(1) − Φ      = .1498
                                                                                      2
         X2 > X1 > X4 > X3                                                                                                    
                                                                                              n    m                         n+m
                                                                        71. (a) P {X = i} =
         X4 > X2 > X3 > X1                                                                    i   k−i                         k
         X4 > X2 > X1 > X3
                                                                                                       i = 0, 1,…, min(k, n)
                        ∞                                                               k
                                                                             (b) X = ∑ Xi
61. (a) fX (x) =              λ2 e−λy dy                                                i=1
                        x
                   = λe−λx
                                                                                              K
                                                                                                                kn
                                                                                 E[X] = ∑ E[X i ] =
                        y                                                                    i=1              n+m
                              2 −λy
     (b) fY (y) =            λ e      dx                                         since the ith ball is equally likely to be
                        0
                                                                                 either of the n + m balls, and so
                  = λ ye−λy
                        2                                                                               n
                                                                                 E[X i ] = P{Xi = 1} =
                                                                                                       n+m
     (c) Because the Jacobian of the transformation
                                                                                               n
         x = x, w = y − x is 1, we have                                               X = ∑ Yi
                                                                                              i=1
         fX,W (x, w) = fX,Y (x, x + w) = λ2 e−λ(x+w)                                           n
                                                 = λe−λx λe−λw                      E[X] = ∑ E[Y i ]
                                                                                              i=1
                                                                                               n
     (d) It follows from the preceding that X and                                        = ∑ P{ith white ball is selected}
         W are independent exponential random vari-                                           i=1
         ables with rate λ.                                                                    n
                                                                                                    k       nk
                                                                                         =∑             =
                                                                                              i=1 n + m   n +m
             ∞
63. φ(t) = ∑ etn (1 − p)n−1 p                                           73. As Ni is a binomial random variable with para-
             n=1                                                            meters (n, Pi ), we have (a) E[Ni ] = nPji (b) Var(Xi ) =
                   ∞                                                        nPi = (1 − Pi ); (c) for i = j, the covariance of Ni and
         = pet ∑ ((1 − p)et )n−1                                            Nj can be computed as
                  n=1
                                                                                                                
                  pet                                                        Cov (N i , N j ) = Cov ∑ Xk , ∑ Yk
         =
             1 − (1 − p)et                                                                                 k         k
                                                        Answers and Solutions                                               11

    where Xk (Yk ) is 1 or 0, depending upon whether or                                      1 i −1    i−1
    not outcome k is type i( j). Hence,                                    (c) E[N i ] =        ∑
                                                                                             i k=0
                                                                                                    k=
                                                                                                        2
    Cov(N i , Nj ) = ∑ ∑ Cov(X k , Y  )
                                                                                             1 i −1 2 (i − 1)(2i − 1)
                         k                                                     E[N 2i ] =      ∑k =
                                                                                             i k=0           6
    Now for k = , Cov(Xk , Y ) = 0 by independence of
    trials and so                                                               and so
     Cov (N i , Nj ) = ∑ Cov(X k , Yk )
                                                                                             (i − 1)(2i − 1) (i − 1)2
                         k                                                      Var(N i ) =                 −
                                                                                                    6            4
                    = ∑ (E[X k Yk ] − E[X k ]E[Y k ])
                                                                                             i2 − 1
                         k                                                                 =
                                                                                               12
                    = − ∑ E[X k ]E[Y k ] (since Xk Yk = 0)
                             k                                        77. If g1 (x, y) = x + y, g2 (x, y) = x − y, then
                    = − ∑ Pi Pj                                                         
                                                                                ∂g1 ∂g1 
                             k                                                          
                                                                                ∂x ∂y 
                    = −nPi Pj                                              J =  ∂g ∂g  = 2
                                                                                2     2
                                                                                ∂x ∂y 
    (d) Letting
                                                                          Hence, if U = X + Y, V = X − Y, then
           1, if no type i’s occur
    Yi =                                                                                                   
           0, otherwise                                                                  1        u + v u−v
                                                                           fU, V (u, v) = fX, Y        ,
    we have that the number of outcomes that never                                       2          2    2
                             r
                                                                                                           
    occur is equal to ∑ Yi and thus,                                                                                   2
                                                                                          2             1      u+v
                             1                                                        =        exp   −             − μ
                                                                                      4τ σ 2         2σ 2     2
          r          r
     E ∑ Yi = ∑ E[Y i ]                                                                                 2 
                                                                                                  u−v
          1          1
                     r                                                                   +            −μ
                                                                                                   2
                  = ∑ P{outcomes i does not occur}
                     1                                                                                       
                     r                                                                  e−μ2 /σ 2      uμ  u2
                  = ∑ (1 − Pi )n                                                      =           exp 2 − 2
                                                                                          4τ σ 2       σ  4σ
                     1
                                                                                                       
75. (a) Knowing the values of N1 , …, Nj is equivalent                                             v2
                                                                                             exp − 2
        to knowing the relative ordering of the ele-                                              4σ
        ments a1 , …, aj . For instance, if N1 = 0, N2 = 1,                              
        N3 = 1 then in the random permutation a2                                   E XetX
                                                                      79. K  (t) =   
        is before a3 , which is before a1 . The indepen-                            E etX
        dence result follows for clearly the number                                                     
        of a1 ,…, ai that follow ai+1 does not proba-                            E etX E X 2 etX − E2 XetX
        bilistically depend on the relative ordering of                    K (t) =               
                                                                                            E2 etX
        a1 , …, ai .
                       1
    (b) P{N i = k} = , k = 0, 1,…, i − 1                                   Hence,
                        i
        which follows since of the elements a1 , …, ai+1                   K  (0) = E[X]
        the element ai+1 is equally likely to be ﬁrst or
        second or … or (i + 1)st .                                         K  (0) = E[X 2 ] − E2 [X] = Var(X)
Chapter 3

                     ∑x p(x, y) = pY(y) = 1                    9. E[X|Y = y] = ∑ xP{X = x|Y = y}
1.   ∑ pX|Y(x|y) =     pY(y)        pY(y)                                           x
     x
                                                                               = ∑ xP{X = x}             by independence
                                                                                    x
3. E[X|Y = 1] = 2                                                              = E[X]
                5
   E[X|Y = 2] =
                3                                                                        y
                12                                            11. E[X|Y = y] = C              x(y2 − x2 )dx = 0
   E[X|Y = 3] =                                                                          −y
                 5

5. (a) P{X = i|Y = 3} = P{i white balls selected              13. The conditional density of X given that X > 1 is
       when choosing 3 balls from 3 white and 6 red}
                                                                                     f (x)    λ exp−λx
                                                              fX |X > 1(x) =            =          when x > 1
                3    6                                                             P{X > 1}    exp−λ
                i   3−i                                                                        ∞
             =          ,     i = 0, 1, 2, 3
                   9                                                                     λ
                                                                  E[X|X > 1] = exp                  xλ exp−λx dx = 1 + 1/λ
                   3                                                                           1

                                                                  by integration by parts.
     (b) By same reasoning as in (a), if Y = 1, then
         X has the same distribution as the number
         of white balls chosen when 5 balls are chosen                              1             1
                                                                                      exp−y         exp−y
         from 3 white and 6 red. Hence,                                             y             y
                                                              15. fX |Y = y (x|y) =          = y
                                                                                      fy (y)      1
                                                                                                    exp−y dx
                            3   5                                                              0 y
           E[X|Y = 1] = 5     =                                                     1
                            9   3                                                 = , 0<x<y
                                                                                    y
7. Given Y = 2, the conditional distribution of X                                         y
   and Z is                                                           2         1                        y2
                                                                  E[X |Y = y] =                x2 dx =
                                                                                y         0              3
                                    1
     P{(X, Z) = (1, 1)|Y = 2} =
                                    5
                                                              17. With K = 1/P{X = i}, we have that
     P{(1, 2)|Y = 2} = 0
                                                                       
     P{(2, 1)|Y = 2} = 0                                          fY|X y|i = KP{X = i|Y = y}fY (y)

                       4                                                    = K1 e−y yi e−αy ya−1
     P{(2, 2)|Y = 2} =
                       5
                                                                            = K1 e−(1+α)y ya+i−1
     So,
                                                                  where K1 does not depend on y. But as the pre-
                     1  8  9
     E[X|Y = 2] =      + =                                        ceding is the density function of a gamma random
                     5  5  5                                      variable with parameters (s + i, 1 + α) the result
     E[X|Y = 2, Z = 1] = 1                                        follows.


                                                         12
                                                       Answers and Solutions                                                      13
      
19.       E[X|Y = y] fY (y)dy                                             Substituting back gives
                    
                                                                          E[N|X] = (X + 1)(p2 + pq) + (X + 2)pq
                =          xfX |Y (x|y)dx fY (Y)dy
                                                                                       + (X + 2 + E[N])q2
                            f (x, y)
                =         x          dx fY (y)dy
                             fY (y)                                       Taking expectations, and using the fact that X is
                                                                        geometric with mean 1/p, we obtain
                =      x     f (x · y)dydx
                                                                               E[N] = 1 + p + q + 2pq + q2 /p + 2q2 + q2 E[N]
                   
                = xfX (x)dx                                               Solving for E[N] yields
                                                                                         2 + 2q + q2 /p
                       = E[X]                                                  E[N] =
                                                                                             1 − q2
                     N                                               25. (a) Let F be the initial outcome.
21. (a) X = ∑ Ti
                                                                                    3                       3
                     i=1                                                                                           2
                                                                         E[N] = ∑ E[N|F = i]pi = ∑ 1 +                pi = 1 + 6 = 7
      (b) Clearly N is geometric with parameter 1/3;                               i=1                     i=1     pi
          thus, E[N] = 3.
                                                                          (b) Let N1,2 be the number of trials until both out-
      (c) Since TN is the travel time corresponding to                        come 1 and outcome 2 have occurred. Then
          the choice leading to freedom it follows that
                                                                                 E[N1,2 ] = E[N1,2 |F = 1]p1 + E[N1,2 |F = 2]p2
          TN = 2, and so E [TN ] = 2.
                                                                                                  + E[N1,2 |F = 3]p3
      (d) Given that N = n, the travel times Ti i = 1,…,
          n − 1 are each equally likely to be either 3 or                                            1                 1
          5 (since we know that a door leading back to the                                = 1+            p1 +   1+         p2
                                                                                                     p2                p1
          nine is selected), whereas Tn is equal to 2 (since
                                                                                            + (1 + E[N1,2 ])p3
          that choice led to safety). Hence,
                                                                                            p    p
                 N                     n− 1                                               = 1 + 1 + 2 + p3 E[N1,2 ]
            E ∑ Ti |N = n = E           ∑ Ti |N = n                                             p2   p1
                 i=1                   i=1
                                                                          Hence,
                                    + E[Tn |N = n]                                            p      p
                                                                                         1 + p12 + p21
                                  = 4(n − 1) + 2                          E[N1,2 ] =
                                                                                           p1 + p2
      (e) Since part (d) is equivalent to the equation
                                                                   27. Condition on the outcome of the ﬁrst ﬂip to obtain
                 N
           E ∑ Ti |N = 4N − 2                                             E[X] = E[X|H]p + E[X|T](1 − p)
              i=1
                                                                                  = (1 + E[X])p + E[X|T](1 − p)
           we see from parts (a) and (b) that
                                                                          Conditioning on the next ﬂip gives
            E[X] = 4E[N] − 2
                                                                          E[X|T] = E[X|TH]p + E[X|TT](1 − p)
                     = 10
                                                                                    = (2 + E[X])p + (2 + 1/p)(1 − p)
23. Let X denote the ﬁrst time a head appears. Let us
    obtain an equation for E[N|X] by conditioning on                      where the ﬁnal equality follows since given that
    the next two ﬂips after X. This gives                                 the ﬁrst two ﬂips are tails the number of additional
                                                                          ﬂips is just the number of ﬂips needed to obtain a
      E[N|X] = E[N|X, h, h]p2 + E[N|X, h, t]pq                            head. Putting the preceding together yields
                       + E[N|X, t, h]pq + E[N|X, t, t]q2                  E[X] = (1 + E[X])p + (2 + E[X])p(1 − p)

      where q = 1 − p. Now                                                          + (2 + 1/p)(1 − p)2
                                                                          or
      E [N|X, h, h] = X + 1, E[N|X, h, t] = X + 1                                       1
                                                                          E[X] =
      E [N|X, t, h] = X + 2, E[N|X, t, t] = X + 2 + E[N]                            p(1 − p)2
14                                                      Answers and Solutions

                                                                                       ∞
29. Let qi = 1 − pi , i = 1.2. Also, let h stand for hit and
                                                                                    = ∑ E[I(T ≥ i)]E[Ri ]
    m for miss.                                                                       i=1
                                                                                       ∞
     (a) μ1 = E[N|h]p1 + E[N|m]q1                                                   = ∑ P{T ≥ i}E[Ri ]
                                                                                      i=1
              = p1 (E[N|h, h]p2 + E[N|h, m]q2 )
                                                                                       ∞
                  + (1 + μ2 )q1                                                     = ∑ β i−1 E[Ri ]
                                                                                      i=1
              = 2p1 p2 + (2 + μ1 )p1 q2 + (1 + μ2 )q1                                                        
                                                                                            ∞
                                                                                                  i −1
           The preceding equation simpliﬁes to                                      =E ∑β                Ri
                                                                                            i=1
           μ1 (1 − p1 q2 ) = 1 + p1 + μ2 q1

           Similarly, we have that                                  35. np1 = E[X1 ]

           μ2 (1 − p2 q1 ) = 1 + p2 + μ1 q2                                 = E[X1 |X2 = 0](1 − p2 )n

           Solving these equations gives the solution.                           + E[X1 |X2 > 0][1 − (1 − p2 )n ]
                                                                                    p1
            h1 = E[H|h]p1 + E[H|m]q1                                        =n           (1 − p2 )n
                                                                                  1 − p2
              = p1 (E[H|h, h]p2 + E[H|h, m]q2 ) + h2 q1
                                                                                 + E[X1 |X2 > 0][1 − (1 − p2 )n ]
              = 2p1 p2 + (1 + h1 ) p1 q2 + h2 q1
                                                                        yielding the result
           Similarly, we have that

           h2 = 2p1 p2 + (1 + h2 )p2 q1 + h1 q2                                               np1 (1 − (1 − p2 )n−1 )
                                                                        E[X1 |X2 > 0] =
                                                                                                  1 − (1 − p2 )n
           and we solve these equations to ﬁnd h1
           and h2 .
                                                                    37. (a) E[X] = (2.6 + 3 + 3.4)/3 = 3
31. Let Li denote the length of run i. Conditioning on
                                                                        (b) E[X 2 ] = [2.6 + 2.62 + 3 + 9 + 3.4 + 3.42 ]/3
    X, the initial value gives
                                                                                    = 12.1067, and Var(X) = 3.1067
     E[L1 ] = E[L1 |X = 1]p + E[L1 |X = 0](1 − p)

                1      1                                            39. Let N denote the number of cycles, and let X be the
             =     p + (1 − p)                                          position of card 1.
               1−p     p
                p     1−p
             =      +                                                                1 n               1 n
               1−p      p                                               (a) mn =       ∑
                                                                                     n i=1
                                                                                           E[N|X = i] = ∑ (1 + mn−1 )
                                                                                                       n i=1
     and
                                                                                            1 n− 1
     E[L2 ] = E[L2 |X = 1]p + E[L2 |X = 0](1 − p)                                 =1 +         ∑ mj
                                                                                            n j=1
              1    1
             = p+     (1 − p)                                           (b) m1 = 1
              p   1−p
             =2                                                                 m2 = 1 +
                                                                                          1
                                                                                            = 3/2
                                                                                          2
33. Let I(A) equal 1 if the event A occurs and let it equal
                                                                                          1
    0 otherwise.                                                                m3 = 1 + (1 + 3/2) = 1 + 1/2 + 1/3
                                                                                      3
        T                 ∞                                                        = 11/6
     E ∑ Ri = E ∑ I(T ≥ i)Ri
       i=1              i=1                                                                 1
                                                                                m4 = 1 +      (1 + 3/2 + 11/6) = 25/12
                    ∞                                                                       4
                  = ∑ E[I (T ≥ i) Ri ]
                    i=1
                                                                        (c) mn = 1 + 1/2 + 1/3 + · · · + 1/n
                                                     Answers and Solutions                                                      15
                                                                                                        ∞
                                                                                                n            1 − x /2      n−2
    (d) Using recursion and the induction hypothesis                                    =                      e      (x/2) 2 −1 dx
        gives                                                                               2Γ (n/2)   0     2
                               n− 1
                          1                                                               nΓ (n/2 − 1)
           mn = 1 +         ∑ (1 + · · · + 1/j)
                          n j=1
                                                                                        =
                                                                                            2Γ (n/2)
                         1                                                                     n
               =1 +        (n − 1 + (n − 2)/2 + (n − 3)/3                               =
                         n                                                                2(n/2 − 1)
                   + · · · + 1/(n − 1))                                                     n
                                                                                        =
                        1                                                                 n−2
               =1 +       [n + n/2 + · · · + n/(n − 1)
                        n                                          45. Now
                   − (n − 1)]
                                                                        E[Xn |Xn−1 ] = 0,     Var(Xn |Xn−1 ) = βXn2−1
               = 1 + 1/2 + · · · + 1/n                                  (a) From the above we see that
                   n
    (e) N = ∑ Xi                                                             E[X n ] = 0
                 i=1
                                                                        (b) From (a) we have that Var(xn ) = E[Xn2 ]. Now
                   n                  n
    (f)    mn = ∑ E[Xi ] = ∑ P{i is last of 1,…, i}                          E[Xn2 ] = E{E[Xn2 |Xn−1 ]}
                   i=1                i=1
                    n                                                               = E[βXn2−1 ]
               = ∑ 1/i
                   i=1
                                                                                    = βE[Xn2−1 ]

    (g) Yes, knowing for instance that i + 1 is the last                            = β 2 E[Xn2−2 ]
        of all the cards 1, …, i + 1 to be seen tells us                            ·
        nothing about whether i is the last of 1, …, i.                             = β n X02
                           n                n
    (h) Var(N) = ∑ Var(Xi ) = ∑ (1/i)(1 − 1/i)                     47. E[X 2 Y 2 |X] = X 2 E[Y 2 |X]
                          i=1               i=1
                                                                                       ≥ X 2 (E[Y|X])2 = X 2
41. Let N denote the number of minutes in the maze.                     The inequality following since for any random
    If L is the event the rat chooses its left, and R the               variable U, E[U 2 ] ≥ (E[U])2 and this remains true
    event it chooses its right, we have by conditioning                 when conditioning on some other random variable
    on the ﬁrst direction chosen:                                       X. Taking expectations of the above shows that
           1          1
    E(N) = E(N|L) + E(N|R)                                              E[(XY)2 ] ≥ E[X 2 ]
           2          2
                                                                      As
           1 1       2           1
         =     (2) + (5 + E(N)) + [3 + E(N)]
           2 3       3           2                                      E[XY] = E[E[XY|X]] = E[XE[Y|X]] = E[X]
           5        21
         = E(N) +                                                       the result follows.
           6        6
            = 21                                                   49. Let A be the event that A is the overall winner, and
                                                                       let X be the number of games played. Let Y equal
                         1                  1                          the number of wins for A in the ﬁrst two games.
43. E[T|χ2n ] =            E[Z|χ2n ] =          E[Z] = 0
                         χ2n /n            χ2n /n                       P(A) = P(A|Y = 0)P(Y = 0)
                         n               n            n
          E[T 2 |χ2n ] = 2 E[Z2 |χ2n ] = 2 E[Z2 ] = 2                            + P(A|Y = 1)P(Y = 1)
                        χn              χn           χn
                                                                                 + P(A|Y = 2)P(Y = 2)
    Hence, E[T] = 0, and
                                                                            = 0 + P(A)2p(1 − p) + p2
                2        n
    Var(T) = E[T ] = E 2
                        χn                                              Thus,
                        ∞ 1 −x /2       n
                           1 2e    (x/2) 2 −1                                         p2
                   =n                         dx                        P(A) =
                        0  x    Γ (n/2)                                          1 − 2p(1 − p)
16                                                     Answers and Solutions

     E[X] = E[X|Y = 0]P(Y = 0)                                                            n
                                                                                                                     n k
                                                                   59. (a) P(Ai Aj ) = ∑ P(Ai Aj |Ni = k)              p (1 − pi )n−k
                    + E[X|Y = 1]P(Y = 1)                                                 k=0
                                                                                                                     k i
                                                                                          n
                    + E[X|Y = 2]P(Y = 2)                                                              n k
                                                                                       = ∑ P(Aj |Ni = k)  p (1 − pi )n−k
                                                                                                      k i
              = 2(1 − p)2 + (2 + E[X])2p(1 − p) + 2p2                                   k=1
                                                                                                               
                                                                                        n− 1       pj      n− k
              = 2 + E[X]2p(1 − p)                                                                                 n
                                                                                       = ∑ 1− 1−
                                                                                         k=1
                                                                                                 1 −  p i         k
     Thus,
                                                                                         × pki (1 − pi )n−k
                  2
     E[X] =                                                                              n− 1                        n−1
            1 − 2p(1 − p)                                                                         n k
                                                                                       = ∑          pi (1 − pi )n−k − ∑
                                                                                         k=1
                                                                                                  k                   k=1
51. Let α be the probability that X is even. Condition-                                               pj      n− k
                                                                                                                       n
    ing on the ﬁrst trial gives                                                          × 1−
                                                                                                    1 − pi             k
     α = P(even|X = 1)p + P(even|X > 1)(1 − p)                                           × pki (1 − pi )n−k
       = (1 − α)(1 − p)
                                                                                                                     n− 1
                                                                                                                             n
     Thus,                                                                             = 1 − (1 − pi )n − pni − ∑
                                                                                                                     k=1
                                                                                                                             k
        1−p                                                                              × pki (1 − pi − pj )n−k
     α=
        2−p
                                                                                       = 1 − (1 − pi )n − pni − [(1 − pj )n
     More computationally                                                                −(1 − pi − pj )n − pni ]
              ∞
                                     p ∞                                               = 1 + (1 − pi − pj )n − (1 − pi )n
     α = ∑ P(X = 2n) =                   ∑ (1 − p)2n
              n=1                  1 − p n=1                                             −(1 − pj )n
                p       (1 − p)2   1−p
          =                      =
              1 − p 1 − (1 − p)2   2−p                                      where the preceding used that conditional on
                                                                            Ni = k, each of the other n − k trials indepen-
                         ∞                                                 dently results in outcome j with probability
53. P{X = n} =                P{X = n|λ}e−λ dλ                                pj
                         0                                                         .
                                                                            1 − pi
                         ∞ −λ n
                            e λ −λ
                      =               e dλ                                                n
                         0     n!                                      (b) P(Ai Aj ) = ∑ P(Ai Aj |Fi = k) pi (1 − pi )k−1
                         ∞                                                              k=1
                                       dλ                                                + P(Ai Aj |Fi > n) (1 − pi )n
                      =     e − 2λ λ n
                         0             n!
                                                                                          n
                         ∞                                                          = ∑ P(Aj |Fi = k) pi (1 − pi )k−1
                                     dt 1 n+1
                      =     e −t t n                                                     k=1
                         0           n! 2                                                                                                  
                                                                                          n        pj                 k −1
                                                                                                                                     n− k
     The result follows since                                                          = ∑ 1− 1−                             (1 − pj )
                                                                                         k=1
                                                                                                 1 − pi
      ∞                                                                                 × pi (1 − pi )k−1
              e−t tn dt = Γ (n + 1) = n!
      0
                                                                       (c) P(Ai Aj ) = P(Ai ) + P(Aj ) − P(Ai ∪ Aj )
57. Let X be the number of storms.                                                     = 1 − (1 − pi )n + 1 − (1 − pj )n
     P{X ≥ 3} = 1 − P{X ≤ 2}                                                             −[1 − (1 − pi − pj )n ]
                     5                                                                = 1 + (1 − pi − pj )n − (1 − pi )n
                                      1
              =1−       P{X ≤ 2|Λ = x} dx                                                −(1 − pj )n
                     0                5
                              5                                   61. (a) m1 = E[X|h]p1 + E[H|m]q1 = p1 + (1 + m2 )
                                                        1
                      =1−       [e−x + xe−x + e−x x2 /2] dx
                              0                         5                      q1 = 1 + m2 q1 .
                                                       Answers and Solutions                                                     17

        Similarly, m2 = 1 + m1 q2 . Solving these equa-                   The ﬁnal equality follows because given that there
        tions gives                                                       are still n − j − 1 uncollected types when the ﬁrst
                                                                          type i is obtained, the probability starting at that
                 1 + q1                  1 + q2
        m1 =               ,   m2 =                                       point that it will be the last of the set of n − j types
                1 − q 1 q2              1 − q 1 q2                        consisting of type i along with the n − j − 1 yet
                                                                          uncollected types to be obtained is, by symmetry,
    (b) P1 = p1 + q1 P2
                                                                          1/(n − j). Hence,
         P2 = q2 P1                                                               
                                                                               n                   n
                                                                                                      1
        implying that                                                     E ∑ Si = nE[Si ] = ∑
                                                                              i=1                 k=1
                                                                                                      k
                   p1                   p1 q2
        P1 =               ,   P2 =
                1 − q 1 q2            1 − q 1 q2
                                                                     65. (a) P{Yn = j} = 1/(n + 1),          j = 0, …, n
     (c) Let fi denote the probability that the ﬁnal hit
         was by 1 when i shoots ﬁrst. Conditioning on                     (b) For j = 0, …, n − 1
         the outcome of the ﬁrst shot gives                                                       n
                                                                                                       1
                                                                               P{Yn−1 = j} = ∑             P{Yn−1 = j|Yn = i}
        f1 = p1 P2 + q1 f2        and      f2 = p2 P1 + q2 f1                                    i=0 n + 1
                                                                                                  1
        Solving these equations gives                                                        =       (P{Yn−1 = j|Yn = j}
                                                                                                 n+1
               p1 P2 + q1 p2 P1                                                                  + P{Yn−1 = j|Yn = j + 1})
        f1 =
                   1 − q 1 q2
                                                                                                  1
    (d) and (e) Let Bi denote the event that both hits                                       =       (P(last is nonred| j red)
                                                                                                 n+1
        were by i. Condition on the outcome of the ﬁrst
        two shots to obtain                                                                      + P(last is red| j + 1 red)

         P(B1 ) = p1 q2 P1 + q1 q2 P(B1 ) → P(B1 )                                                1      n−j j + 1
                                                                                             =              +               = 1/n
                                                                                                 n+1      n    n
                  p q P
                = 1 2 1
                 1 − q 1 q2                                               (c) P{Yk = j} = 1/(k + 1),         j = 0, …, k
        Also,                                                             (d) For j = 0, …, k − 1
                                                                                                  k
         P(B2 ) = q1 p2 (1 − P1 ) + q1 q2 P(B2 ) → P(B2 )
                                                                               P{Yk−1 = j} = ∑ P{Yk−1 = j|Yk = i}
                    q1 p2 (1 − P1 )                                                              i=0
                =
                       1 − q 1 q2                                                                P{Yk = i}

     (f) E[N] = 2p1 p2 + p1 q2 (2 + m1 )                                                          1
                                                                                             =       (P{Yk−1 = j|Yk = j}
                                                                                                 k+1
                  + q1 p2 (2 + m1 ) + q1 q2 (2 + E[N])
                                                                                                 + P{Yk−1 = j|Yk = j + 1})
        implying that                                                                          1     k−j    j+1
                                                                                             =           +         = 1/k
                                                                                             k+1      k       k
                    2 + m1 p1 q2 + m1 q1 p2
        E[N] =                                                                 where the second equality follows from the
                          1 − q 1 q2
                                                                               induction hypothesis.
63. Let Si be the event there is only one type i in the
    ﬁnal set.                                                        67. A run of j successive heads can occur in the fol-
                    n− 1                                                 lowing mutually exclusive ways: (i) either there is
    P{Si = 1} = ∑ P{Si = 1|T = j}P{T = j}                                a run of j in the ﬁrst n − 1 ﬂips, or (ii) there is no
                    j=0                                                  j-run in the ﬁrst n − j − 1 ﬂips, ﬂip n − j is a tail,
                      n−1                                                and the next j ﬂips are all heads. Consequently, (a)
                    1
                =     ∑ P{Si = 1|T = j}
                    n j=0
                                                                         follows. Condition on the time of the ﬁrst tail:
                                                                                    j
                    1 n−1 1
                =      ∑ n−j                                              Pj (n) = ∑ Pj (n − k)pk−1 (.1 − p) + p j ,       j≤n
                    n j=0                                                         k=1
18                                                   Answers and Solutions

69. (a) Let I(i, j) equal 1 if i and j are a pair and 0                  So,
        otherwise. Then                                                                
                     ⎛ ⎞                                               E g(X, Y)|Y = y = ∑ g(x, y)P{X = x|Y = y}
                           n                                                                            k
                               1 1
        E ∑ I(i, j) = ⎝ ⎠              = 1/2                                                     = E[g(x, y)|Y = y
           i <j
                           2   nn−1
                                                                      (c) E[XY] = E[E[XY|Y]]
         Let X be the size of the cycle containing person
         1. Then                                                                  = E[YE[X|Y]]                  by (a)
                 n
                                              1
         Qn = ∑ P{no pairs|X = i}1/n =
                                              n i∑
                                                     Qn − i      79. Let us suppose we take a picture of the urn before
                i=1                              =2
                                                                     each removal of a ball. If at the end of the exper-
73. Condition on the value of the sum prior to going                 iment we look at these pictures in reverse order
    over 100. In all cases the most likely value is 101.             (i.e., look at the last taken picture ﬁrst), we will
    (For instance, if this sum is 98 then the ﬁnal sum               see a set of balls increasing at each picture. The
    is equally likely to be either 101, 102, 103, or 104. If         set of balls seen in this fashion always will have
    the sum prior to going over is 95 then the ﬁnal sum              more white balls than black balls if and only if in
    is 101 with certainty.)                                          the original experiment there were always more
                                                                     white than black balls left in the urn. Therefore,
75. (a) Since A receives more votes than B (since a > a)             these two events must have same probability, i.e.,
        it follows that if A is not always leading then              n − m/n + m by the ballot problem.
        they will be tied at some point.
     (b) Consider any outcome in which A receives                                               1
         the ﬁrst vote and they are eventually tied,             81. (a) f (x) = E[N] =              E[N|X1 = y]dy
         say a, a, b, a, b, a, b, b…. We can correspond this                                    0
         sequence to one that takes the part of the
                                                                                                    1             if y < x
         sequence until they are tied in the reverse                      E[N|X1 = y] =
         order. That is, we correspond the above to the                                             1 + f (y)     if y > x
         sequence b, b, a, b, a, b, a, a… where the remain-
         der of the sequence is exactly as in the original.               Hence,
         Note that this latter sequence is one in which                                   1
         B is initially ahead and then they are tied. As                  f (x) = 1 +          f (y)dy
         it is easy to see that this correspondence is one                                x
         to one, part (b) follows.
     (c) Now,                                                         (b) f  (x) = −f (x)
         P{B receives ﬁrst vote and they are                          (c) f (x) = ce−x . Since f (1) = 1, we obtain that
         eventually tied}                                                 c = e, and so f (x) = e1−x .
         = P{B receives ﬁrst vote}= n/(n + m)
                                                                     (d) P{N > n} = P{x < X1 < X2 < · · · < Xn } =
         Therefore, by part (b) we see that                              (1 − x)n /n! since in order for the above event to
         P{eventually tied}= 2n/(n + m)                                  occur all of the n random variables must exceed
         and the result follows from part (a).                           x (and the probability of this is (1 − x)n ), and
                                                                         then among all of the n! equally likely order-
77. We will prove it when X and Y are discrete.                          ings of this variables the one in which they are
     (a) This part follows from (b) by taking                            increasing must occur.
         g(x, y) = xy.                                                               ∞
     (b) E[g(X, Y)|Y = y] = ∑ ∑ g(x, y)                               (e) E[N] = ∑ P{N > n}
                               y   x                                                n=0
                              P{X = x, Y = y|Y = y}                              = ∑ (1 − x)n /n! = e1−x
         Now,                                                                        n

         P{X = x, Y = y|Y = y}
             ⎧                                                   83. Let Ij equal 1 if ball j is drawn before ball i and
             ⎨ 0,                      if y = y                      let it equal 0 otherwise. Then the random variable
           =
             ⎩ P{X = x, Y = y},        if y = y                      of interest is ∑ Ij . Now, by considering the ﬁrst
                                                                                     j = i
                                                           Answers and Solutions                                                19

     time that either i or j is withdrawn we see that                              the number of ones between the ﬁrst and sec-
     P{ j before i} = wj /(wi + wj ). Hence,                                       ond zeros, and so on. As there are (n + m −
                                                                                 1)!/n!(m − 1)! such permutations, the result
                        wj                                                         follows.
     E ∑ Ij = ∑
         j=i
                     w + wj
                 j=i i                                                        (b) The number of positive solutions of x1 + · · · +
                                                                                   xm = n is equal to the number of nonnegative
85. Consider the following ordering:                                               solutions of y1 + · · · + ym = n − m, and thus
    e1 , e2 , …, el−1 , i, j, el+1 , …, en where Pi < Pj                                       n−1
                                                                                   there are           such solutions.
                                                                                               m−1
     We will show that we can do better by inter-
     changing the order of i and j, i.e., by taking                            (c) If we ﬁx a set of k of the xi and require them
     e1 , e2 , …, el−1 , j, i, el+2 , …, en . For the ﬁrst ordering,               to be the only zeros, then⎡there are ⎤by (b)
     the expected position of the element requested is                                                              n−1
                                                                                   (with m replaced by m − k) ⎣            ⎦ such
     Ei,j = Pe1 + 2Pe2 + · · · + (l − 1)Pel−1                                                                     m−k−1
            + lpi + (l + 1)Pj + (l + 2)Pel+2 + · · ·                                                            ⎡ ⎤⎡            ⎤
                                                                                                                  m     n−1
     Therefore,                                                                    solutions. Hence, there are ⎣ ⎦ ⎣            ⎦
                                                                                                                  k    m−k−1
     Ei,j − Ej,i = l(Pi − Pj ) + (l + 1)(Pj − Pi )
                                                                                   outcomes such that exactly k of the Xi are
                = Pj − P i > 0                                                     equal
                                                                                      ⎡ ⎤to⎡zero, and ⎤so%the
                                                                                                            ⎡ desired probability
                                                                                                                       ⎤
     and so the second ordering is better. This shows                                  m      n−1             n + m−1
     that every ordering for which the probabilities are                           is ⎣ ⎦ ⎣           ⎦     ⎣          ⎦.
                                                                                       k    m−k−1               m−1
     not in decreasing order is not optimal in the sense
     that we can do better. Since there are only a ﬁnite
     number of possible orderings, the ordering for                      89. Condition on the value of In . This gives
     which p1 ≥ p2 ≥ p3 ≥ · · · ≥ pn is optimum.                                                          &
                                                                                             n

87. (a) This can be proved by induction on m. It is
                                                                               Pn (K) = P   ∑ jIj ≤ K|In = 1 1/2
                                                                                            j=1
        obvious when m = 1 and then by ﬁxing the                                                                        &
        value of x1 and using the induction hypothe-                                              n
                                     n                                               +P        ∑ jIj ≤ K|In = 0 1/2
                                         n−i + m−2
        sis, we see that there are ∑                                                             j=1
                                             m−2
                                   i=0                                                                          &
                             n−i + m−2                                                      n− 1
        such solutions. As                    equals the
                                  m−2                                                =P     ∑ jIj + n ≤ K             1/2
        number of ways of choosing m − 1 items from                                         j=1
        a set of size n + m − 1 under the constraint                                                          &
                                                                                                 n−1
        that the lowest numbered item selected is
        number i + 1 (that is, none of 1, …, i are
                                                                                       +P         ∑ jIj ≤ K       1/2
                                                                                                 j=1
        selected where i + 1 is), we see that
         n                                                                       = [Pn−1 (k − n) + Pn−1 (K)]/2
             n−i + m−2           n + m−1
        ∑        m−2
                            =
                                   m−1
        i=0
                                                                                    1           1       1
          It also can be proven by noting that each solu-                91.               + 2        +
                                                                               p5 (1 − p)3  p (1 − p)   p
          tion corresponds in a one-to-one fashion with
          a permutation of n ones and (m − 1) zeros.                     95. With α = P(Sn < 0 for all n > 0), we have
          The correspondence being that x1 equals the
          number of ones to the left of the ﬁrst zero, x2                                          −E[X] = α = p−1 β
Chapter 4

                       1             4                                                              4
                                                                                                   P2,
1. P01 = 1,       P10 =  ,     P21 =   ,     P32 = 1                   11. The answer is
                                                                                                       2
                                                                                                      for the Markov chain with
                       9             9                                                      1 − P2,
                                                                                                  4
                                                                                                    0
                       4             4                                       transition probability matrix
                  P11 = ,      P22 =
                       9             9                                       ⎡          ⎤
                       4             1                                          1 0 0
                  P12 = ,      P23 =                                         ⎣.3 .4 .3 ⎦
                       9             9
                                                                               .2 .3 .5
3.
                                                                                     n− r r
                (RRR) (RRD) (RDR) (RDD) (DRR) (DRD) (DDR) (DDD)        13. Pijn = ∑ Pik  Pkj > 0
          (RRR) .8      .2    0     0     0     0     0     0                        k
          (RRD)               .4    .6
          (RDR)
         (RDD)
                                          .6    .4
                                                      .4    .6
                                                                       15. Consider any path of states i0 = i, i1 , i2 , …, in = j
     P = (DRR) .6       .4                                                 such that Pik ik+1 > 0. Call this a path from i to j.
         (DRD)                .4    .6
         (DDR)                            .6    .4                         If j can be reached from i, then there must be a
         (DDD)                                        .2    .8             path from i to j. Let i0 , …, in be such a path. If all
                                                                           of the values i0 , …, in are not distinct, then there
     where D = dry and R = rain. For instance, (DDR)                       is a subpath from i to j having fewer elements (for
     means that it is raining today, was dry yesterday,                    instance, if i, 1, 2, 4, 1, 3, j is a path, then so is i, 1, 3, j).
     and was dry the day before yesterday.                                 Hence, if a path exists, there must be one with all
                                                                           distinct states.
5. Cubing the transition probability matrix, we obtain
                                                                              n
   P3 :
   ⎡                       ⎤                                           17.   ∑ Yj /n → E[Y] by the strong law of large num-
     13/36 11/54 47/108                                                      i=1
   ⎢                       ⎥                                                 bers. Now E[Y] = 2p − 1. Hence, if p > 1/2, then
   ⎣ 4/9    4/27     11/27 ⎦
                                                                             E[Y] > 0, and so the average of the Yi s converges
      5/12   2/9     13/36                                                   in this case to a positive number, which implies
                                                                                   n
     Thus,                                                                   that ∑ Yi → ∞ as n → ∞. Hence, state 0 can be
                                                                                   1
     E[X3 ] = P(X3 = 1) + 2P(X3 = 2)                                         visited only a ﬁnite number of times and so must
              1 3    1 3     1 3                                             be transient. Similarly, if p < 1/2, then E[Y] < 0,
            = P01  + P11   + P21                                                               n
              4     4       2                                              and so lim ∑ Yi = −∞, and the argument is
                  1 3     1 3    1 3
              + 2 P02 + P12 + P22                                                              1
                  4       4      2                                           similar.
    2     2
7. P30 + P31 = P31 P10 + P33 P11 + P33 P31                             19. The limiting probabilities are obtained from
                 = (.2)(.5) + (.8)(0) + (.2)(0) + (.8)(.2)                   r0 = .7r0 + .5r1
                 = .26                                                       r1 = .4r2 + .2r3
                                                                             r2 = .3r0 + .5r1
9. It is not a Markov chain because information about
   previous color selections would affect probabili-                         r0 + r1 + r2 + r3 = 1
   ties about the current makeup of the urn, which                           and the solution is
   would affect the probability that the next selection                           1          3         3                     9
   is red.                                                                   r0 = , r1 =       , r2 =    ,           r3 =
                                                                                  4         20        20                    20


                                                                  20

                                              Answers and Solutions                                                21

    The desired result is thus                                   Squaring this matrix gives P2 :
              2
    r0 + r1 =                                                      5/12      7/12
              5                                                    7/18      11/18
21. The transition probabilities are                             Hence, if Si is the number of storms in year i then
            
              1 − 3α, if j = i
    Pi, j =                                                      E[S1 ] = E[S1 |X1 = 0]P00 + E[S1 |X1 = 1]P01
              α,      if j = i
                                                                         = 1/2 + 3/2 = 2
    By symmetry,
                                                                                        2                  2
                                                                 E[S2 ] = E[S2 |X2 = 0]P00 + E[S2 |X2 = 1]P01
             1
    Pijn = (1 − Piin ), j = i                                            = 5/12 + 21/12 = 26/12
             3
    So, let us prove by induction that                           Hence, E[S1 + S2 ] = 25/6.
             ⎧
             ⎪
             ⎪ 1  3
             ⎨ + (1 − 4α)n ,     if j = i                        (b) Multiplying the ﬁrst row of P by the ﬁrst column
               4  4                                              of P2 gives
    Pi,n j =
             ⎪
             ⎪ 1 1
             ⎩ − (1 − 4α)n ,     if j = i                         3
               4 4                                               P00 = 5/24 + 7/36 = 29/72
    As the preceding is true for n = 1, assume it for n.         Hence, conditioning on the state at time 3 yields
    To complete the induction proof, we need to show
    that                                                                                      29
             ⎧                                                   P(S3 = 0) = P(S3 = 0|X3 = 0)    + P(S3 = 0|X3 = 1)
                                                                                              72
             ⎪
             ⎪ 1  3
             ⎨ + (1 − 4α)n+1 ,      if j = i                                      43   29 −1   43 −3
               4  4                                                             ×    =    e +     e
    Pi,n+1 =                                                                      72   72      72
        j    ⎪
             ⎪ 1 1
             ⎩ − (1 − 4α)n+1 ,      if j = i                     (c) The stationary probabilities are the solution of
               4 4
    Now,                                                                 1      1
                                                                 π0 = π0   + π1
                                                                         2      3
        i = Pi, i Pi, i + ∑ Pi, j Pj, i
    Pi,n+1   n               n
                                                                 π0 + π1 = 1
                          j=i
              1    3                                             giving
          =     + (1 − 4α)n (1 − 3α)
              4    4                                                               π0 = 2/5 ,   π1 = 3/5.
                   1 1                                           Hence, the long-run average number of storms is
            + 3      − (1 − 4α)n α
                   4 4                                           2/5 + 3(3/5) = 11/5.
            1    3
          = + (1 − 4α)n (1 − 3α − α)
            4    4                                          25. Letting Xn denote the number of pairs of shoes
            1    3                                              at the door the runner departs from at the begin-
          = + (1 − 4α)n+1                                       ning of day n, then {Xn } is a Markov chain with
            4    4
                                                                transition probabilities
    By symmetry, for j = i
             1            1 1                                         Pi, i = 1/4,   0<i<k
    Pijn+1 =    1 − Piin+1 = − (1 − 4α)n+1
             3              4 4                                       Pi, i−1 = 1/4,   0<i<k
    and the induction is complete.                                    Pi, k−i = 1/4,   0<i<k
    By letting n → ∞ in the preceding, or by using that          Pi, k−i+1 = 1/4,      0<i<k
    the transition probability matrix is doubly stochas-         The ﬁrst equation refers to the situation where the
    tic, or by just using a symmetry argument, we                runner returns to the same door she left from and
    obtain that πi = 1/4.                                        then chooses that door the next day; the second to
                                                                 the situation where the runner returns to the oppo-
23. (a) Letting 0 stand for a good year and 1 for a bad          site door from which she left from and then chooses
    year, the successive states follow a Markov chain            the original door the next day; and so on. (When
    with transition probability matrix P:                        some of the four cases above refer to the same tran-
      1/2 1/2                                                    sition probability, they should be added together.
      1/3 2/3                                                    For instance, if i = 4, k = 8, then the preceding
22                                                                      Answers and Solutions

     states that Pi, i = 1/4 = Pi, k−i . Thus, in this case,                            The equations for the long-run proportions are
     P4, 4 = 1/2.) Also,
                                                                                             1       1
                                                                                        r0 =   r1 + r2
        P0, 0 = 1/2                                                                          4       4
                                                                                             1       1   1
        P0, k = 1/2                                                                     r1 = r0 + r1 + r2
                                                                                             2       2   4
        Pk, k = 1/4                                                                          1       1   1
                                                                                        r2 = r0 + r1 + r2
        Pk, 0 = 1/4                                                                          2       4   2
       Pk, 1 = 1/4                                                                      r0 + r1 + r2 = 1
     Pk, k−1 = 1/4                                                                      By symmetry it is easy to see that r1 = r2 . This
                                                                                        makes it easy to solve and we obtain the result
     It is now easy to check that this Markov chain is
     doubly stochastic—that is, the column sums of the                                          1            2            2
                                                                                        r0 =      ,   r1 =     ,   r2 =
     transition probability matrix are all 1—and so the                                         5            5            5
     long-run proportions are equal. Hence, the propor-
     tion of time the runner runs barefooted is 1/(k + 1).                          33. Consider the Markov chain whose state at time n is
                                                                                        the type of exam number n. The transition proba-
                                                                                        bilities of this Markov chain are obtained by condi-
27. The limiting probabilities are obtained from                                        tioning on the performance of the class. This gives
             1                                                                          the following:
     r0 =      r1
             9                                                                           P11 = .3(1/3) + .7(1) = .8
               4      4
     r1 = r0 + r1 + r2                                                                   P12 = P13 = .3(1/3) = .1
               9      9
          4      4                                                                       P21 = .6(1/3) + .4(1) = .6
     r2 = r1 + r2 + r3
          9      9
     r0 + r1 + r2 + r3 = 1                                                               P22 = P23 = .6(1/3) = .2

                                                   1              9                      P31 = .9(1/3) + .1(1) = .4
     and the solution is r0 = r3 =                   , r1 = r2 =    .
                                                  20             20                      P32 = P33 = .9(1/3) = .3

29. Each employee moves according to a Markov chain                                     Let ri denote the proportion of exams that are type
    whose limiting probabilities are the solution of                                    i, i = 1, 2, 3. The ri are the solutions of the following
                                                                                        set of linear equations:
                            
        = .7     + .2    + .1                                                           r1 = .8 r1 + .6 r2 + .4 r3
        1               1              2              3
                                                                                    r2 = .1 r1 + .2 r2 + .3 r3
            = .2            + .6           + .4
        2               1           2              3
                                                                                        r1 + r2 + r3 = 1
                          
            +           +          =1                                                   Since Pi2 = Pi3 for all states i, it follows that
        1           2          3
                                                                                     r2 = r3 . Solving the equations gives the solution
     Solving        yields                 = 6/17,            = 7/17,          =        r1 = 5/7,      r2 = r3 = 1/7
                                       1                  2                3
     4/17. Hence, if N is large, it follows from the law
     of large numbers that approximately 6, 7, and 4 of                             35. The equations are
     each 17 employees are in categories 1, 2, and 3.
                                                                                                 1     1    1
                                                                                        r0 = r1 +  r2 + r3 + r4
                                                                                                 2     3    4
31. Let the state on day n be 0 if sunny, 1 if cloudy, and 2                                  1    1     1
    if rainy. This gives a three-state Markov chain with                                r1 = r2 + r3 + r4
                                                                                              2    3     4
    transition probability matrix                                                             1    1
                                                                                        r2 = r3 + r4
                                                                                              3    4
                        0           1              2                                          1
                                                                                        r3 = r4
       0             0             1/2            1/2                                         4
     P=1            1/4            1/2            1/4                                   r 4 = r0
       2            1/4            1/4            1/2                                   r0 + r1 + r2 + r3 + r4 = 1
                                                              Answers and Solutions                                                    23

     The solution is                                                             satisﬁes the above, which is equivalent to
                                                                                                              
     r0 = r4 = 12/37,                r1 = 6/37,      r2 = 4/37,                                  P2 P1   P P
                                                                                 P 1 P 2 = P1          + 2 3
     r3 = 3/37                                                                                  1 − P2  1 − P2
                                                                                            P1
37. Must show that                                                                    =          P2 (P1 + P3 )
                                                                                          1 − P2
     πj = ∑ πi Pi,k j                                                                 = P1 P2      since P1 + P3 = 1 − P2
                 i

     The preceding follows because the right-hand side                           By symmetry all of the other stationary equations
     is equal to the probability that the Markov chain                           also follow.
     with transition probabilities Pi, j will be in state j
                                                                            45. (a) 1, since all states communicate and thus all are
     at time k when its initial state is chosen according
                                                                                    recurrent since state space is ﬁnite.
     to its stationary probabilities, which is equal to its
     stationary probability of being in state j.                                (b) Condition on the ﬁrst state visited from i.
                                                                                            N −1
                                                                                      xi = ∑ Pij xj + PiN ,         i = 1, … , N − 1
39. Because recurrence is a class property it follows                                       j=1
    that state j, which communicates with the recur-                                 x0 = 0, xN = 1
    rent state i, is recurrent. But if j were positive recur-
    rent, then by the previous exercise i would be as                            (c) Must show
                                                                                          N −1
    well. Because i is not, we can conclude that j is null                            i        j
                                                                                        = ∑      Pij + PiN
    recurrent.                                                                       N     j=1 N
                                                                                             N
41. (a) The number of transitions into state i by time                                          j
                                                                                          =∑      Pij
        n, the number of transitions originating from                                       j=0 N
        state i by time n, and the number of time peri-                               and follows by hypothesis.
        ods the chain is in state i by time n all differ
        by at most 1. Thus, their long-run proportions                      47. {Yn , n ≥ 1} is a Markov chain with states (i, j).
        must be equal.                                                                           
                                                                                                   0,    if j = k
     (b) ri Pij is the long-run proportion of transitions                       P(i, j),(k, ) =
                                                                                                   Pj , if j = k
         that go from state i to state j.
     (c)    ∑j ri Pij is the long-run proportion of transi-                      where Pj is the transition probability for {X n }.
            tions that are into state j.
                                                                                  lim P{Y n = (i, j)} = lim P{X n = i, X n+1 = j}
     (d) Since rj is also the long-run proportion of tran-                       n→∞                         n
         sitions that are into state j, it follows that                                                  = lim [P{X n = i}Pij ]
                                                                                                             n

            rj = ∑ ri Pij                                                                                = ri Pij
                     j                                                      49. (a) No.
                                                                                      lim P{X n = i} = pr1 (i) + (1 − p)r2 (i)
43. Consider a typical state—say, 1 2 3. We must show
                                                                              (b) Yes.
         =        P123, 123 +      P213, 123
           123           123                   213
                                                                                                  (1)            (2)
                                                                                     Pij = pP        + (1 − p)P
                                                                                                  ij             ij
                     +           P231, 123
                           231

     Now P123, 123 = P213, 123 = P231, 123 = P1 and thus,                   53. With πi (1/4) equal to the proportion of time
                                                                                a policyholder whose yearly number of acci-
                                 
         = P1          +         +                                              dents is Poisson distributed with mean 1/4 is in
           123                 123       213         231                        Bonus-Malus state i, we have that the average pre-
     We must show that                                                          mium is
                                                                                 2             1
                P P        P P        P P                                       (326.375) + [200π1 (1/4) + 250π2 (1/4)
               = 1 2 ,     = 2 1 ,     = 2 3                                     3             3
           123  1 − P1 213  1 − P2 231  1 − P2                                      + 400π3 (1/4) + 600π4 (1/4)]
24                                                       Answers and Solutions

55. S11 = P{offspring is aa | both parents dominant}                 65. r ≥ 0 = P{X0 = 0}. Assume that
                                                                         r ≥ P{Xn−1 = 0}
             P{aa, both dominant}
         =
              P{both dominant}                                           P{X n = 0 = ∑ P{X n = 0|X 1 = j}Pj
                                                                                              j
                  1                                                                                    
               r2       r2                                                               = ∑ P{X n−1 = } j Pj
         =      4 =                                                                           j
           (1 − q)2 4(1 − q)2
                                                                                            ≤ ∑ rj Pj
              P{aa, 1 dominant and 1 recessive parent}                                             j
     S10 =
               P{1 dominant and 1 recessive parent}                                      =r
              P{aa, 1 parent aA and 1 parent aa}                     67. (a) Yes, the next state depends only on the present
         =
                           2q(1 − q)                                         and not on the past.
                 1                                                       (b) One class, period is 1, recurrent.
               2qr
         =       2                                                                       N−i
           2q(1 − q)                                                     (c) Pi, i+1 = P       , i = 0, 1, …, N − 1
                                                                                           N
               r                                                                                i
         =                                                                   Pi, i−1 = (1 − P) , i = 1, 2, …, N
           2(1 − q)                                                                            N
                                                                                       i            (N − i)
57. Let A be the event that all states have been visited                     Pi, i = P + (1 − p)            , i = 0, 1, …, N
    by time T. Then, conditioning on the direction of                                 N                N
                                                                         (d) See (e).
    the ﬁrst step gives                                                             
                                                                                    N i
     P(A) = P(A|clockwise)p                                              (e) ri =       p (1 − p)N −i , i = 0, 1,…, N
                                                                                    i
               + P(A|counterclockwise)q                                  (f) Direct substitution or use Example 7a.
                    1 − q/p       1 − p/q                                                   N −1
             =p               +q                                         (g) Time = ∑ Tj , where Tj is the number of
                   1 − (q/p)n    1 − (p/q)n
                                                                                              j=i
     The conditional probabilities in the preceding                           ﬂips to go from j to j + 1 heads. Tj is geo-
     follow by noting that they are equal to the proba-                       metric with E[T j ] = N/j. Thus, E[time] =
     bility in the gambler’s ruin problem that a gambler                      N −1
     that starts with 1 will reach n before going broke                          ∑ N/j.
     when the gambler’s win probabilities are p and q.                           j=i
                                                                                                              M
59. Condition on the outcome of the initial play.                                                     M!      1
                                                                     69. r(n1 ,…, nm ) =
                                                                                                  n1 ,…, nm ! m
61. With P0 = 0, PN = 1
                                                                         We must now show that
     Pi = αi Pi+1 + (1 − αi )Pi−1 ,       i = 1, … , N − 1                                                nj + 1 1
                                                                         r(n1 ,…, ni − 1,…, nj + 1,…)
     These latter equations can be rewritten as                                                               M M−1
     Pi+1 − Pi = βi (Pi − Pi−1 )                                                                      i       1
                                                                            = r(n1 ,…, ni ,…, nj ,…)
                                                                                                     M M−1
     where βi = (1 − αi )/αi . These equations can now                           nj + 1              ni
     be solved exactly as in the original gambler’s ruin                 or                      =          , which follows.
     problem. They give the solution                                        (ni − 1)!(nj + 1)!     ni !nj !
                        i −1
             1 + ∑j=1 Cj                                                               Pij
     Pi =                      ,   i = 1, …, N − 1                   71. If rj = c         , then
                        N −1                                                           Pji
             1 + ∑j=1 Cj
                                                                                       Pij Pjk
     where                                                               rj Pjk = c
                                                                                        Pji
            j
                                                                                      Pjk Pkj
     Cj =          βi                                                    rk Pkj = c
             i=1                                                                        Pki
     (c) PN −i ,        where αi = (N − i)/N                             and are thus equal by hypothesis.
                                                                       Answers and Solutions                                                          25
                                                                                                             ∞
73. It is straightforward to check that ri Pij = rj Pji . For
                                                                                                    = bj + ∑ an+1 ∑ Eβ I{Xn = i, an = a} Pij (a)
    instance, consider states 0 and 1. Then                                                                 n=0        i, a

     r0 p01 = (1/5)(1/2) = 1/10
                                                                                                    = bj + a ∑ ∑ an Eβ I(X n = i, an = a} Pij (a)
     whereas                                                                                                  i, a n

     r1 p10 = (2/5)(1/4) = 1/10                                                                     = bj + a ∑ yia Pij (a)
                                                                                                              i, a
75. The number of transitions from i to j in any interval                                 (c) Let dj, a denote the expected discounted time
    must equal (to within 1) the number from j to i since                                     the process is in j, and a is chosen when policy
    each time the process goes from i to j in order to get                                    β is employed. Then by the same argument as
    back to i, it must enter from j.                                                          in (b):
                                                                  
77. (a)    ∑ yja = ∑ Eβ ∑ a I{Xn = j, an = a}
                                         n                                                     ∑ dja
           a           a            n                                                           a
                                                                  
                                                                                                    = bj + a ∑ ∑ an Eβ [I{Xn = i, an = a}] Pij (a)
                    = Eβ ∑ an ∑ I{Xn = j, an = a}                                                            i, a n
                               n         a
                                                                                                                                     yia
                                                                                                    = bj + a ∑ ∑ an Eβ I{X = i}             Pij (a)
                    = Eβ ∑ a I{Xn = j}
                                     n
                                                                                                              i, a n
                                                                                                                                  n
                                                                                                                                      ∑ yia
                               n                                                                                                      a
                                                            
                                                                                                                      y
                                                                                                    = bj + a ∑ ∑ dia, ia Pij (a)
     (b)   ∑ ∑ yja = Eβ ∑ an ∑ I{Xn = j}                                                                     i, a a  ∑ yia
           j    a                    n       j                                                                                a
                                                    1
                      = Eβ          ∑a   n
                                                 =
                                                   1−α
                                                                                               and we see from Equation (9.1) that the above
                                                                                               is satisﬁed upon substitution of dia = yia . As
           ∑ yja                                                                                                                  1
           a                                                                                   it is easy to see that ∑i,a dia =     , the result
                                                                                                                               1−a
                                   ∞                                                           follows since it can be shown that these linear
               = bj + Eβ           ∑ = a I { Xn = j }
                                             n
                                                                                               equations have a unique solution.
                                   n=1
                                                                                        (d) Follows immediately from previous parts.
                                   ∞
               = bj + Eβ           ∑a    n+1
                                                 I{Xn+1 = j}                                  It is a well-know result in analysis (and
                                   n=0                                                        easily proven) that if limn→∞ an /n = a then
                                                                                              limn → ∞ ∑i ai /n also equals a. The result fol-
                                                                                                         n
                               
                                   ∞
               = bj + Eβ           ∑ = an+1 ∑ I{Xn = i, an = a}                               lows from this since
                                   n=0                i, a
                                                                                               E[R(X n )] = ∑ R( j)P{X n = j}
                                                                                                                j
                                   I(Xn+1 = j}                                                              = ∑ R( j)rj
                                                                                                                 i
Chapter 5

 1. (a) e−1        (b) e−1                                           (b) When n = 2,
                                                                         P{max Yi < X}
 3. The conditional distribution of X, given that                             ∞
    X > 1, is the same as the unconditional distribution                   =     P{max Yi < X|X = x}λe−λx dx
    of 1 + X. Hence, (a) is correct.
                                                                              ∞
                                                                              0

 5. e−1 by lack of memory.                                                 =     P{max Yi < x}λe−λx dx
                                                                              ∞
                                                                              0

 7. P{X1 < X2 | min(X1 , X 2 ) = t}                                        =     (1 − e−μx )2 λe−λx dx
                                                                              ∞
                                                                              0
            P{X1 < X2 , min(X1 , X2 ) = t}
       =                                                                   =     (1 − 2e−μx + e−2μx )2 λe−λx dx
               P{min(X1 , X2 ) = t}                                              0
                                                                                      2λ     λ
                   P{X1 = t, X2 > t}                                         = 1−        +
       =                                                                             λ+μ   2μ + λ
         P{X1 = t, X2 > t} + P{X2 = t, X1 > t}
                                                                                       2μ2
                                                                             =
                     f1 (t)F̄2 (t)                                               (λ + μ)(λ + 2μ)
       =
            f1 (t)F̄2 (t) + f2 (t)F̄1 (t)
                                                                 13. Let Tn denote the time until the nth person in line
    Dividing though by F̄1 (t)F̄2 (t) yields the result.
                                                                     departs the line. Also, let D be the time until the ﬁrst
    (For a more rigorous argument, replace  = t”
                                                                     departure from the line, and let X be the additional
    by ” ∈ (t, t + )” throughout, and then let → 0.)
                                                                     time after D until Tn . Then,
 9. Condition on whether machine 1 is still working at               E[Tn ] = E[D] + E[X]
    time t, to obtain the answer,
                                                                                   1     (n − 1)θ + μ
                                    λ1                                      =          +              E[Tn−1 ]
    1−e    −λ1 t
                   +e   −λ1 t                                                   nθ + μ      nθ + μ
                                λ 1 + λ2
                                                                     where E[X] was computed by conditioning on
                                                                     whether the ﬁrst departure was the person in line.
11. (a) Using Equation (5.5), the lack of memory prop-
                                                                     Hence,
        erty of the exponential, as well as the fact that
        the minimum of independent exponentials is                   E[Tn ] = An + Bn E[Tn−1 ]
        exponential with a rate equal to the sum of
        their individual rates, it follows that                      where
                    nμ                                                         1                     (n − 1)θ + μ
        P(A1 ) =                                                     An =          ,          Bn =
                  λ + nμ                                                    nθ + μ                      nθ + μ
           and, for j > 1,                                           Solving gives the solution
                                                                                   n− 1       n
                                         (n − j + 1)μ                E[Tn ] = An + ∑ An−i                  Bj
           P(Aj |A1 · · · Aj−1 ) =
                                       λ + (n − j + 1)μ                                i=1       j=n−i+1
           Hence,                                                                      n− 1
                                                                            = An + ∑ 1/(nθ + μ)
                
                n
                        (n − j + 1)μ                                                   i=1
           p=                                                                      n
                      λ + (n − j + 1)μ                                      =
                j=1                                                             nθ + μ




                                                            26
                                                    Answers and Solutions                                                    27

    Another way to solve the preceding is to let Ij equal               By the lack of memory property of the exponential
    1 if customer n is still in line at the time of the ( j −           it follows that the amounts by which the costs of
    1)st departure from the line, and let Xj denote the                 the other links exceed C1 are independent exponen-
    time between the ( j − 1)st and jth departure from                  tials with rate 1. Therefore, C2 is equal to C1 plus
    line. (Of course, these departures only refer to the                the minimum of 2(n − 2) independent exponentials
    ﬁrst n people in line.) Then                                        with rate 1, and so
                                                                                              1
            n                                                           E[C2 ] = E[C1 ] +
    Tn = ∑ Ij Xj                                                                           2(n − 2)
           j=1                                                          Similar reasoning then gives
    The independence of Ij and Xj gives                                                         1
                                                                        E[C3 ] = E[C2 ] +
                 n                                                                           3(n − 3)
    E[Tn ] = ∑ E[Ij ]E[Xj ]                                             and so on.
                 j=1

    But,                                                          19.   (c) Letting A = X(2) − X(1) we have
                                                                            E[X(2) ]
                (n − 1)θ + μ     (n − j + 1)θ + μ
     E[Ij ] =                ···                                                = E[X(1) ] + E[A]
                   nθ + μ        (n − j + 2)θ + μ
                (n − j + 1)θ + μ                                                       1      1     μ1     1     μ2
           =                                                                    =           +            +
                     nθ + μ                                                         μ1 + μ2   μ2 μ1 + μ2   μ1 μ1 + μ2

    and                                                                     The formula for E[A] being obtained by condi-
                                                                            tioning on which Xi is largest.
                         1
    E[Xj ] =                                                            (d) Let I equal 1 if X1 < X2 and let it be 2 otherwise.
                 (n − j + 1)θ + μ
                                                                            Since the conditional distribution of A (either
    which gives the result.                                                 exponential with rate μ1 or μ2 ) is determined
                                                                            by I, which is independent of X(1) , it follows
15. Let Ti denote the time between the (i − 1)th and                        that A is independent of X(1) .
    the ith failure. Then the Ti are independent with Ti                    Therefore,
    being exponential with rate (101 − i)/200. Thus,                        Var(X (2) ) = Var(X (1) ) + Var(A)
                  5           5
                                 200                                        With p = μ1 /(μ1 + μ2 ) we obtain, upon condi-
       E[T] = ∑ E[Ti ] = ∑
                 i=1        i=1 101 −i                                      tioning on I,
                  5                5
                                       (200)2                                  E[A] = p/μ2 + (1 − p)/μ1 ,
    Var(T) = ∑ Var(Ti ) = ∑
                 i=1              i=1 (101 − i)
                                               2                            E[A2 ] = 2p/μ22 + 2(1 − p)/μ21
                                                                            Therefore,
17. Let Ci denote the cost of the ith link to be                            Var(A) = 2p/μ22 + 2(1 − p)/μ21
    constructed, i = 1, …, n − 1. Note that the ﬁrst
                                      n                                                    − (p/μ2 + (1 − p)/μ1 )2
    link can be any of the                 possible links.
                                      2
    Given the ﬁrst one, the second link must connect                        Thus,
    one of the 2 cities joined by the ﬁrst link with one of                  Var(X (2) )
    the n − 2 cities without any links. Thus, given the
                                                                                 = 1/(μ1 + μ2 )2 + 2[p/μ22 + (1 − p)/μ21 ]
    ﬁrst constructed link, the next link constructed will
    be one of 2(n − 2) possible links. Similarly, given the                         −(p/μ2 + (1 − p)/μ1 )2
    ﬁrst two links that are constructed, the next one to
    be constructed will be one of 3(n − 3) possible links,        21. E[time] = E[time waiting at 1] + 1/μ1
    and so on. Since the cost of the ﬁrst link to be built                          + E[time waiting at 2] + 1/μ2
                            n
    is the minimum of           exponentials with rate 1,               Now,
                            2
    it follows that                                                     E[time waiting at 1] = 1/μ1 ,
                n
                                                                                                            μ1
    E[C1 ] = 1                                                          E[time waiting at 2] = (1/μ2 )
                   2                                                                                     μ1 + μ2
28                                                      Answers and Solutions

     The last equation follows by conditioning on                                                  1 − e−(λ−μ)c (1 + (λ − μ)c)
                                                                          (b) E[X|X + Y = c] =
     whether or not the customer waits for server 2.                                                 λ(1 − e−(λ−μ)c )
     Therefore,
                                                                          (c) c = E [X + Y|X + Y = c] = E [X|X + Y = c]
     E[time] = 2/μ1 + (1/μ2 )[1 + μ1 /(μ1 + μ2 )]
                                                                                                            + E [Y|X + Y = c]
23. (a) 1/2.                                                                  implying that
    (b) (1/2)n−1 : whenever battery 1 is in use and a
        failure occurs the probability is 1/2 that it is                      E[Y|X + Y = c]
        not battery 1 that has failed.                                                     1 − e−(λ−μ)c (1 + (λ − μ)c)
                  n−i+1                                                             = c−
     (c) (1/2)      , i > 1.                                                                    λ(1 − e−(λ−μ)c )
     (d) T is the sum of n − 1 independent exponentials
         with rate 2μ (since each time a failure occurs             31. Condition on whether the 1 PM appointment is still
         the time until the next failure is exponential                 with the doctor at 1:30, and use the fact that if she or
         with rate 2μ).                                                 he is then the remaining time spent is exponential
     (e) Gamma with parameters n − 1 and 2μ.                            with mean 30. This gives
                                                                          E[time spent in ofﬁce]
25. Parts (a) and (b) follow upon integration. For part
    (c), condition on which of X or Y is larger and use                     = 30(1 − e−30/30 ) + (30 + 30)e−30/30
    the lack of memory property to conclude that the
                                                                            = 30 + 30e−1
    amount by which it is larger is exponential rate λ.
    For instance, for x < 0,
                                                                    33. (a) By the lack of memory property, no matter
     fx − y(x)dx
                                                                            when Y fails the remaining life of X is expo-
        = P{X < Y}P{−x < Y − X < −x + dx|Y > X}                             nential with rate λ.
          1 λx                                                            (b) E [min (X, Y) |X > Y + c]
        =   λe dx
          2                                                                       = E [min (X, Y) |X > Y, X − Y > c]
     For (d) and (e), condition on I.
                                                                                  = E [min (X, Y) |X > Y]
               μ1
27. (a)                                                                   where the ﬁnal equality follows from (a).
            μ1 + μ3
               μ1      μ2
     (b)                                                                  1   1
            μ1 + μ3 μ2 + μ3                                         37.     +
               1      μ        μ     1                                    μ   λ
     (c)    ∑ μi + μ1 +1 μ3 μ2 +2 μ3 μ3
            i
                                                                  39. (a) 196/2.5 = 78.4
               1      μ1      1       μ2 1
     (d)    ∑ μi + μ1 + μ2 μ2 + μ2 + μ3 μ3                                (b) 196/(2.5)2 = 31.36
            i
                     μ2      μ1      μ2   1                               We use the central limit theorem to justify approx-
              +                                                           imating the life distribution by a normal distri-
                  μ1 + μ2 μ1 + μ3 μ2 + μ3 μ3
                                                                          bution
                                                                          √        with mean 78.4 and standard deviation
29. (a) fX |X + Y(x|c) = CfX. X+Y(x, c)                                      31.36 = 5.6. In the following, Z is a standard nor-
                                                                          mal random variable.
                          = C1 fXY (x, c−x)                                                                         
                                                                                                        67.2 − 78.4
                                                                           (c) P{L < 67.2} ≈ P Z <
                          = fX (x) fY (c − x)                                                                5.6
                                                                                              = P{Z < −2} = .0227
                          = C2 e−λx e−μ(c−x) ,    0<x<c                                                         
                                                                                                       90 − 78.4
                                                                          (d) P{L > 90} ≈ P Z >
                          = C3 e−(λ−μ)x ,       0<x<c                                                     5.6
                                                                                           = P{Z > 2.07} = .0192
            where none of the Ci depend on x. Hence, we                                                            
            can conclude that the conditional distribution                                              100 − 78.4
                                                                           (e) P{L > 100} ≈ P Z >
            is that of an exponential random variable con-                                                  5.6
            ditioned to be less than c.                                                      = P{Z > 3.857} = .00006
                                                     Answers and Solutions                                                29

41. λ1 /(λ1 + λ2 )                                                           Also,
                                                                                         λ+μ
43. Let Si denote the service time at server i, i = 1, 2 and                 E[T1 ] =
                                                                                           λ2
    let X denote the time until the next arrival. Then,
    with p denoting the proportion of customers that                    (c) Let Li denote the time until a customer is lost
    are served by both servers, we have                                     when you start with i busy servers. Then,
      p = P{X > S1 + S2 }                                                   reasoning as in part (b) gives that

       = P{X > S1 }PX > S1 + S2 |X > S1 }                                                 1            μ
                                                                             E[L2 ] =        + E[L1 ]
           μ1      μ2                                                                    λ+μ          λ+μ
       =
         μ1 + λ μ2 + λ                                                                    1                       μ
                                                                                     =       + (E[T1 ] + E[L2 ])
                                                                                         λ+μ                     λ+μ
45.    E[N(T)] = E[E[N(T)|T]] = E[λT] = λE[T]
                                                                                          1    μ            μ
                                                                                     =       + 2 + E[L2 ]
      E[TN(T)] = E[E[TN(T)|T]] = E[TλT] = λE[T 2 ]                                       λ+μ  λ           λ + μ
                                                                             Thus,
      E[N 2 (T)] = E E[N 2 (T)|T] = E[λT + (λT)2 ]                                       1   μ(λ + μ)
                                                                             E[L2 ] =      +
                  = λE[T] + λ2 E[T 2 ]                                                   λ      λ3
      Hence,
                                                                   49. (a) P{N(T) − N(s) = 1} = λ(T − s)e−λ(T −s)
                                 2                   2
      Cov(T, N(T)) = λE[T ] − E[T]λE[T] = λσ                           (b) Differentiating the expression in part (a) and
      and                                                                  then setting it equal to 0 gives

      Var(N(T)) = λE[T] + λ2 E[T 2 ] − (λE[T])2                              e−λ(T −s) = λ(T − s)e−λ(T −s)
                    = λμ + λ2 σ 2                                            implying that the maximizing value is
         )                                                                   s = T − 1/λ
47. (a) 1 (2μ) + 1/λ
                                                                        (c) For s = T − 1/λ, we have that λ(T − s) = 1 and
    (b) Let Ti denote the time until both servers are                       thus,
        busy when you start with i busy servers i =
        0, 1. Then,                                                          P{N(T) − N(s) = 1} = e−1

            E[T0 ] = 1/λ + E[T1 ]                                  51. Condition on X, the time of the ﬁrst accident, to
            Now, starting with 1 server busy, let T be the             obtain
                                                                                 ∞
            time until the ﬁrst event (arrival or departure);
                                                                       E[N(t] =     E[N(t)|X = s]βe−β s ds
            let X = 1 if the ﬁrst event is an arrival and let it                     0
            be 0 if it is a departure; let Y be the additional                      t
            time after the ﬁrst event until both servers are                   =         (1 + α(t − s))βe−β s ds
            busy.                                                                    0

            E[T1 ] = E[T] + E[Y]                                   53. (a) e−1
                          1                 λ                          (b) e−1 + e−1 (.8)e−1
                    =         + E[Y|X = 1]
                        λ+μ                λ+μ
                                      μ                            55. As long as customers are present to be served,
                        + E[Y|X = 0]                                   every event (arrival or departure) will, inde-
                                     λ+μ
                                                                       pendently of other events, be a departure with
                         1            μ
                    =       + E[T0 ]                                   probability p = μ/(λ + μ). Thus P{X = m} is the
                        λ+μ          λ+μ                               probability that there have been a total of m tails at
            Thus,                                                      the moment that the nth head occurs, when indepen-
                        1    1            μ                            dent ﬂips of a coin having probability p of coming
            E[T0 ] −      =     + E[T0 ]
                        λ   λ+μ          λ+μ                           up heads are made: that is, it is the probability that
            or                                                         the nth head occurs on trial number n + m. Hence,
                        2λ + μ                                                             n + m−1
            E[T0 ] =                                                    p{X = m} =                      pn (1 − p)m
                          λ2                                                                 n−1
30                                                 Answers and Solutions

57. (a) e−2                                                                  the system becomes empty when that cus-
     (b) 2 p.m.                                                              tomer departs.
                                                                             Condition on R, the remaining service time:
59. The unconditional probability that the claim is type                     P{empty}
    1 is 10/11. Therefore,                                                           ∞
                           P(4000|1)P(1)                                        =          P{empty|R = t}μe−μt dt
     P(1|4000) =                                                                     0
                   P(4000|1)P(1) + P(4000|2)P(2)
                                                                                     ∞         t         
                          e−4 10/11                                             =          exp −λ   e −μy
                                                                                                          dy μe−μt dt
               = −4
                e 10/11 + .2e−.8 1/11                                                0                0
                                                                                     ∞                    
                                                                                                λ
61. (a) Poisson with mean cG(t).                                                =          exp − (1 − e−μt ) μe−μt dt
                                                                                     0          μ
     (b) Poisson with mean c[1 − G(t)].                                              1
     (c) Independent.                                                           =         e−λx/μ dx
                                                                                     0
63. Let X and Y be respectively the number of cus-                                  μ
    tomers in the system at time t + s that were present                        =     (1 − e−λ/μ )
                                                                                    λ
    at time s, and the number in the system at t + s
    that were not in the system at time s. Since there                       where the preceding used that P{empty|
    are an inﬁnite number of servers, it follows that                        R = t} is equal to the probability that an
    X and Y are independent (even if given the num-                          M/M/∞ queue is empty at time t.
    ber is the system at time s). Since the service dis-
                                                               65. This is an application of the inﬁnite server Pois-
    tribution is exponential with rate μ, it follows that
                                                                   son queue model. An arrival corresponds to a new
    given that X(s) = n, X will be binomial with param-
                                                                   lawyer passing the bar exam, the service time is
    eters n and p = e−μt . Also Y, which is indepen-
                                                                   the time the lawyer practices law. The number in
    dent of X(s), will have the same distribution as X(t).
                                           t                      the system at time t is, for large t, approximately a
                                                                   Poisson random variable with mean λμ where λ is
    Therefore, Y is Poisson with mean λ e−μy dy
                                                                   the arrival rate and μ the mean service time. This
                                           0                       latter statement follows from
       = λ(1 − e−μt )/μ                                             n
                                                                       [1 − G(y)]dy = μ
     (a) E[X(t + s)|X(s) = n]                                        0

            = E[X|X(s) = n] + E[Y|X(s) = n].                       where μ is the mean of the distribution G. Thus, we
                                                                   would expect 500 · 30 = 15, 000 lawyers.
            = ne−μt + λ(1 − e−μt )/μ
     (b) Var(X(t + s)|X(s) = n)                                67. If we count a satellite if it is launched before time
                                                                   s but remains in operation at time t, then the num-
            = Var(X + Y|X(s) = n)
                                                                    of items counted is Poisson with mean m(t) =
                                                                   ber
                                                                         s
            = Var(X|X(s) = n) + Var(Y)                                       Ḡ(t − y)dy. The answer is e−m(t) .
                                                                     0
                  −μt      −μt           −μt
           = ne (1 − e ) + λ(1 − e )/μ
                                                               69. (a) 1 − e−λ(t−s)
         The above equation uses the formulas for the
         variances of a binomial and a Poisson random              (b) e−λs e−λ(t−s) [λ(t − s)]3 /3!
         variable.
                                                                   (c) 4 + λ(t − s)
     (c) Consider an inﬁnite server queuing system in
         which customers arrive according to a Poisson             (d) 4s/t
         process with rate λ, and where the service
         times are all exponential random variables            71. Let U1 , … be independent uniform (0, t) random
         with rate μ. If there is currently a single cus-          variables that are independent of N(t), and let U(i, n)
         tomer in the system, ﬁnd the probability that             be the ith smallest of the ﬁrst n of them.
                                                               Answers and Solutions                                                        31
                              &
        N(t)                                                                             that given that the ﬁrst event of the ﬁrst pro-
    P    ∑ g(Si ) < x                                                                    cess occurred at time t the number of events of
        i=1
                                                   &                                     the second process by this time is Poisson with
                    N(t)                                                                 mean λ(1 − p)t.
        = ∑P            ∑ g(Si ) < x|N(t) = n P{N(t) = n}
          n             i=1
                                                   &                         75. (a) {Yn } is a Markov chain with transition proba-
                        n                                                            bilities given by
        = ∑P        ∑ g(Si ) < x|N(t) = n P{N(t) = n}
          n         i=1                                                                  P0j = aj ,   Pi, i−1+j = aj ,   j≥0
                                              &
                        n
        = ∑P        ∑ g(U(i,n) ) < x P{N(t) = n}                                         where
          n         i=1                                                                        −λt
                                                                                                e (λt)j
                                                                                         aj =           dG(t)
                                               (Theorem 5.2)                                      j!
                                         &
                        n
        = ∑P        ∑ g(Ui ) < x P{N(t) = n}                                      (b) {Xn } is a Markov chain with transition proba-
          n         i=1                                                               bilities
                                      *                             +                                                                ∞
                                          n               n
                                          ∑ g(U(i, n) ) = ∑ g(Ui )                       Pi, i+1−j = βj , j = 0, 1, …, i, Pi, 0 =    ∑ βj
                                         i=1             i=1                                                                        k=i+1
                                                   &                                     where
                        n
        = ∑P        ∑ g(Ui ) < x|N(t) = n P{N(t) = n}                                          −μt
                                                                                                e (μt)j
          n         i=1                                                                  βj =           dF(t)
                                                   &                                              j!
                    N(t)
        = ∑P            ∑ g(Ui ) < x|N(t) = n P{N(t) = n}                               μ
          n             i=1                                                  77. (a)
                                     &                                                λ+μ
               N(t)
                                                                                        λ     2μ
        =P        ∑ g(Ui ) < x                                                    (b)
                                                                                      λ + μ λ + 2μ
                  i=1
                                                                                         j −1
                                                                                                 λ      jμ
73. (a) It is the gamma distribution with parameters                              (c)                         , j>1
                                                                                                λ + iμ λ + jμ
        n and λ.                                                                         i=1
                                                                                  (d) Conditioning on N yields the solution; namely
    (b) For n ≥ 1,                                                                     ∞
                                                                                          1
        P{N = n|T = t}                                                                ∑ j P(N = j)
                                                                                      j=1
                  P{T = t|N = n}p(1 − p)n−1                                               ∞
              =                                                                                          j
                                                                                                               1
                            fT (t)                                                (e)     ∑ P(N = j) ∑ λ + iμ
                    (λt)n−1
                                                                                          j=1           i=0
              =C             (1 − p)n−1
                    (n − 1)!
                                                                             79. Consider a Poisson process with rate λ in which an
                 (λ(1 − p)t)n−1                                                  event at time t is counted with probability λ(t)/λ
              =C
                    (n − 1)!                                                     independently of the past. Clearly such a process
                                                                                 will have independent increments. In addition,
                                  (λ(1 − p)t)n−1
              = e−λ(1−p)t
                                     (n − 1)!                                     P{2 or more counted events in(t, t + h)}
         where the last equality follows since the                                     ≤ P{2 or more events in(t, t + h)}
         probabilities must sum to 1.                                                  = o(h)
    (c) The Poisson events are broken into two classes,
        those that cause failure and those that do not.                           and
        By Proposition 5.2, this results in two indepen-                          P{1 counted event in (t, t + h)}
        dent Poisson processes with respective rates
        λp and λ(1 − p). By independence it follows                                     = P{1 counted | 1 event}P(1 event)
32                                                                  Answers and Solutions

           + P{1 counted | ≥ 2 events}P{≥ 2}                                             Hence, as each of the N(t) injured parties have
            t+h                                                                         the same probability p of being out of work at
                     λ(s) ds                                                             t, we see that
       =                     (λh + o(h)) + o(h)
                      λ h
            t                                                                            E[X(t)]|N(t)] = N(t)p
         λ(t)
       =      λh + o(h)                                                                  and thus,
          λ
                                                                                         E[X(t)] = pE[N(t)]
       = λ(t)h + o(h)
                                                                                                  = pm(t)
81. (a) Let Si denote the time of the ith event, i ≥ 1.                                              t
        Let ti + hi < ti+1 , tn + hn ≤ t.                                                         =     [1 − F(t − s)]λ(s) ds
                                                                                                      0
        P{ti < Si < ti + hi , i = 1, …, n|N(t) = n}
        P{1 event in (ti , ti + hi ), i = 1, …, n,                              83. Since m(t) is increasing it follows that nonover-
                                                                                    lapping time intervals of the {N(t)} process will
                    no events elsewhere in (0, t)
                =                                                                   correspond to nonoverlapping intervals of the
                           P{N(t) = n}
                 n                                                                {No (t)} process. As a result, the independent
                                                                                   increment property will also hold for the {N(t)}
                          e−(m(ti +hi )−m(ti )) [m(ti + hi ) − m(ti )]              process. For the remainder we will use the identity
                    i=1
                                                                                    m(t + h) = m(t) + λ(t)h + o(h)
                              e
                                  −[m(t)−   ∑i m(ti +hi )−m(ti )]
                =                                                                   P{N(t + h) − N(t) ≥ 2}
                                      e−m(t) [m(t)]n /n!
                     
                     n                                                                 = P{No [m(t + h)] − No [m(t)] ≥ 2}
                    n [m(ti + hi ) − m(ti )]
                                                                                       = P{No [m(t) + λ(t)h + o(h)] − No [m(t)] ≥ 2}
                          i
                =
                       [m(t)]n                                                         = o[λ(t)h + o(h)] = o(h)
         Dividing both sides by h1 · · · hn and using the
                                           ti +h                                   P{N(t + h) − N(t) = 1}
         fact that m(ti + hi ) − m(ti ) =         λ(s) ds =
                                                            ti                         = P{No [m(t) + λ(t)h + o(h)] − No [m(t)] = 1}
         λ(ti )h + o(h) yields upon letting the hi → 0:
         fS1 ··· S2 (t1 , …, tn |N(t) = n)                                             = P{1 event of Poisson process in interval
                                                                                            of length λ(t)h + o(h)]}
                       
                       n
                = n!     [λ(ti )/m(t)]                                                 = λ(t)h + o(h)
                       i=1
         and the right-hand side is seen to be the joint                        85. $ 40,000 and $1.6 × 108 .
         density function of the order statistics from a
         set of n independent random variables from                             87. Cov[X(t), X(t + s)]
         the distribution with density function f (x) =
                                                                                    = Cov[X(t), X(t) + X(t + s) − X(t)]
         m(x)/m(t), x ≤ t.
                                                                                    = Cov[X(t), X(t)] + Cov[X(t), X(t + s) − X(t)]
     (b) Let N(t) denote the number of injuries by time
         t. Now given N(t) = n, it follows from part (b)                            = Cov[X(t), X(t)] by independent increments
         that the n injury instances are independent and
         identically distributed. The probability (den-                             = Var[X(t)] = λtE[Y 2 ]
         sity) that an arbitrary one of those injuries was
                                                                                89. Let Ti denote the arrival time of the ﬁrst type i
         at s is λ(s)/m(t), and so the probability that
                                                                                    shock, i = 1, 2, 3.
         the injured party will still be out of work at
         time t is                                                                  P{X1 > s, X2 > t}
              t
                                                  λ(s)
         p = P{out of work at t|injured at s}          dζ                              = P{T1 > s, T3 > s, T2 > t, T3 > t}
              0                                   m(t)
               t                                                                      = P{T1 > s, T2 > t, T3 > max(s, t)}
                                 λ(s)
            =     [1 − F(t − s)]      dζ
                0                m(t)                                                  = e−λ1s e−λ2t e−λ3max(s, t)
                                                      Answers and Solutions                                                 33

91. To begin, note that                                                        and so both sides equal Xn . By symmetry the
                                                                             result follows for all other possible orderings
                                                                               of the X  s.
               n
     P X 1 > ∑ Xi
               2                                                         (c) Taking expectations of (b) where Xi is the time
       = P{X 1 > X2 }P{X 1 − X2 > X3 |X1 > X2 }                              of the ﬁrst event of the ith process yields

       = P{X 1 − X2 − X3 > X4 |X 1 > X2 + X3 }…                                 ∑ λi−1 − ∑ ∑(λi + λj )−1
                                                                                i         i <j
       = P{X 1 − X2 · · · − Xn−1 > Xn |X 1 > X2
                                                                                         + ∑ ∑ ∑(λi + λj + λk )−1 − · · ·
            + · · · + Xn− 1 }                                                                i <j <k
                                                                                                                   −1
       = (1/2)n−1                                                                                            n
                                                                                         + (−1)    n+1
                                                                                                             ∑ λi
     Hence,                                                                                                  1
                                                                                            
                          &                           &
                n                 n             n                                                xg(x)e−xt (xt)n dx
     P M > ∑ Xi − M             = ∑ P X1 > ∑ Xi                     95. E[L|N(t) = n] = 
                                 i −1          j=i
                                                                                                  g(x)e−xt (xt)n dx
               i=1
                                        n− 1
                                = n/2
                                                                         Conditioning on L yields
93. (a) max(X 1 , X 2 ) + min(X 1 , X 2 ) = X 1 + X2 .
                                                                         E[N(s)|N(t) = n]
     (b) This can be done by induction:
                                                                              = E[E[N(s)|N(t) = n, L]|N(t) = n]
          max{(X 1 , …, X n )
                                                                              = E[n + L(s − t)|N(t) = n]
            = max(X 1 , max(X 2 , …, X n ))
                                                                              = n + (s − t)E[L|N(t) = n]
            = X1 + max(X 2 , …, X n )
                                                                         For (c), use that for any value of L, given that there
               − min(X 1 , max(X 2 , …, X n ))                           have been n events by time t, the set of n event times
            = X1 + max(X 2 , …, X n )                                    are distributed as the set of n independent uniform
                                                                         (0, t) random variables. Thus, for s < t
               − max(min(X 1 , X2 ), …, min (X 1 , Xn )).
                                                                         E[N(s)|N(t) = n] = ns/t
         Now use the induction hypothesis.
         A second method is as follows:                             97. With C = 1/P(N(t) = n), we have
         Suppose X1 ≤ X2 ≤ · · · ≤ Xn . Then the coefﬁ-
                                                                                                 (λt)n −pλ (pλ)m−1
         cient of Xi on the right side is                                fL|N(t) (λ|n) = Ce−λt        pe
                                                                                            n!       (m − 1)!
               n−i        n−i        n−i
         1−           +          −          + ···
                 1          2          3                                              = Ke−(p+t)λ λn+m−1

            = (1 − 1)n−i                                                 where K does not depend on λ. But we recognize
                                                                        the preceding as the gamma density with param-
                0, i = n                                                 eters n + m, p + t, which is thus the conditional
            =
                1, i = n                                                 density.
Chapter 6

1. Let us assume that the state is (n, m). Male i mates              7. (a) Yes!
   at a rate λ with female j, and therefore it mates at a               (b) For n = (n1 , … , ni , ni+1 , …, nk−1 ) let
   rate λm. Since there are n males, matings occur at
   a rate λnm. Therefore,                                                        Si (n) = (n1 , …, ni−1 , ni+1 + 1, …, nk−1 ),

   v(n, m) = λnm                                                                          i = 1, …, k − 2
                                                                             Sk−1 (n) = (n1 , …, ni , ni+1 , …nk−1 − 1),
   Since any mating is equally likely to result in a
   female as in a male, we have                                                S0 (n) = (n1 + 1, …, ni , ni+1 , …, nk−1 )
                                           1                                  Then
   P(n, m); (n+1, m) = P(n, m)(n, m+1) =
                                           2                                  qn , S1 (n) = ni μ,       i = 1, …, k − 1
                                                                              qn , S0 (n) = λ
3. This is not a birth and death process since we need
   more information than just the number working.
   We also must know which machine is working. We                    9. Since the death rate is constant, it follows that as
   can analyze it by letting the states be                              long as the system is nonempty, the number of
                                                                        deaths in any interval of length t will be a Poisson
        b : both machines are working                                   random variable with mean μt. Hence,
        1 : 1 is working, 2 is down                                       Pij (t) = e−μt (μt)i − j /(i − j)!,   0<j≤i
        2 : 2 is working, 1 is down                                                 ∞
                                                                        Pi, 0 (t) = ∑ e−μt (μt)k /k!
        01 : both are down, 1 is being serviced
                                                                                   k=i
        02 : both are down, 2 is being serviced
                                                                    11. (b) Follows from the hint upon using the lack of
     vb = μ1 + μ2 , v1 = μ1 + μ, v2 = μ2 + μ,                               memory property and the fact that i , the min-
                                                                            imum of j − (i − 1) independent exponentials
    v01 = v02 = μ                                                           with rate λ, is exponential with rate (j − i + 1)λ.
              μ                                  μ                       (c) From (a) and (b)
   Pb, 1 = μ +2 μ = 1 − Pb, 2 ,        P1, b = μ + μ
            2    1                                    1                                                                         
         = 1 − P1,02                                                          P{T1 + · · · + Tj ≤ t} = P            max Xi ≤ t
                                                                                                                1≤i≤j
              μ
   P2, b = μ + μ = 1 − P2, 01 ,       P01 , 1 = P02 , 2 = 1
                 2                                                                                        = (1 − e−λt ) j

                                                                         (d) With all probabilities conditional on X(0) = 1
5. (a) Yes.
   (b) It is a pure birth process.                                            P1j (t) = P{X(t) = j}
   (c) If there are i infected individuals then                                      = P{X(t) ≥ j} − P{X(t) ≥ j + 1}
       since a contact will involve an infected and
       an uninfected individual with probability                                     = P{T1 + · · · + Tj ≤ t}
       i (n − i) /(n2 ), it follows that the birth rates are                             −P{T1 + · · · + Tj+1 ≤ t}
       λi = λi(n − i)/(n2 ), i = 1, …, n. Hence,
                                                                         (e) The sum of independent geometrics, each
                               n(n − 1) n
        E[time all infected] =          ∑ 1/[i(n−i)]                         having parameter p = e−λt , is negative bino-
                                  2λ i=1                                     mial with parameters i, p. The result follows



                                                               34
                                                    Answers and Solutions                                                35

        since starting with an initial population of i is              Therefore, the balance equations reduce to
        equivalent to having i independent Yule pro-                       3           3     9        3    27
        cesses, each starting with a single individual.                P1 =  P0 , P2 = P1 = P0 , P3 = P2 =    P0
                                                                           2           4     8        4    32
                                                                      And therefore,
13. With the number of customers in the shop as the                                        
    state, we get a birth and death process with                                  3   9  27 −1     32
                                                                      P0 = 1 + + +             =
    λ0 = λ1 = 3,         μ1 = μ2 = 4                                              2   8  32       143

    Therefore                                                          (a) The fraction of potential customers that enter
                                           2                             the system is
           3                   3           3
    P1 =     P0 ,       P2 =     ,   P1 =      P0                          λ(1 − P3 )                 27     32   116
           4                   4           4                                          = 1 − P3 = 1 −     ×      =
                                                                               λ                      32 143      143
                    2
                                                                       (b) With a server working twice as fast we would
    And since ∑ Pi = 1, we get
                                                                           get
                    0                                                                              2            3
               2 −1                                                          3         3        3             3
            3   3         16                                               P 1 = P0 P 2 = P1 =           P0 P3 =      P0
    P0 = 1 + +          =                                                        4         4        4             4
            4   4         37                                                                     2  3 −1
                                                                                             3     3        3          64
                                                                           and P0 = 1 + +               +           =
    (a) The average number of customers in the                                               4     4        4         175
        shop is                                                             So that now
                           2                                                           27      64    148
        P1 + 2P2 =
                     3
                       +2
                            3
                                  P0                                        1 − P3 = 1 −      = 1−     =
                     4      4                                                              64      175   175
                                 2 −1                         17. Say the state is 0 if the machine is up, say it is i
                   30       3     3         30
                 =       1+ +             =                           when it is down due to a type i failure, i = 1, 2. The
                   16       4     4         37                        balance equations for the limiting probabilities are
    (b) The proportion of customers that enter the                    as follows.
        shop is                                                       λP0 = μ1 P1 + μ2 P2
        λ(1 − P2 )                9 16    28                           μ1 P1 = λpP0
                   = 1 − P2 = 1 −   ·   =
            λ                     16 37   37
                                                                       μ2 P2 = λ(1 − p)P0
    (c) Now μ = 8, and so
                                                                       P0 + P1 + P2 = 1
                      2 −1
                 3     3         64                                    These equations are easily solved to give the results
        P0 = 1 + +             =
                 8     8         97
                                                                       P0 = (1 + λp/μ1 + λ(1 − p)/μ2 )−1
        So the proportion of customers who now enter
        the shop is                                                    P1 = λpP0 /μ1 ,      P2 = λ(1 − p)P0 /μ2
                      2
                      3 264           9   88                      19. There are 4 states. Let state 0 mean that no
        1 − P2 = 1 −           = 1−     =
                      8    97        97   97                          machines are down, state 1 that machine 1 is down
                                                                      and 2 is up, state 2 that machine 1 is up and 2 is
        The rate of added customers is therefore
                                                                      down, and 3 that both machines are down. The bal-
                                                                ance equations are as follows:
           88        28       88 28
        λ      −λ        =3     −       = 0.45
           97        37       97 37                                           (λ1 + λ2 )P0 = μ1 P1 + μ2 P2
        The business he does would improve by 0.45                            (μ1 + λ2 )P1 = λ1 P0 + μ1 P3
        customers per hour.
                                                                              (λ1 + μ2 )P2 = λ2 P0
15. With the number of customers in the system as the                                 μ1 P3 = μ2 P1 + μ1 P2
    state, we get a birth and death process with
                                                                       P0 + P1 + P2 + P3 = 1
    λ0 = λ1 = λ2 = 3, λi = 0,            i≥4
                                                                       These equations are easily solved and the
    μ1 = 2, μ2 = μ3 = 4                                                proportion of time machine 2 is down is P2 + P3 .
36                                                     Answers and Solutions

21. How we have a birth and death process with                          (d) Pn, m (λ + μ1 + μ2 ) = λPn−1, m + μ1 Pn+1, m−1
    parameters                                                                                    + μ2 Pn, m+1
     λi = λ,      i = 1, 2
                                                                       We will try a solution of the form Cαn β m = Pn, m .
     μi = iμ,     i = 1, 2
                                                                       From (a), we get
     Therefore,
                                                                                            λ
                                                                       λC = μ2 Cβ = β =
                    1 + λ/μ                                                                 μ2
     P0 + P1 =
               1 + λ/μ + (λ/μ)2 /2
                                                                       From (b),
     and so the probability that at least one machine is
     up is higher in this case.                                        (λ + μ1 ) Cαn = λCαn−1 + μ2 Cαn β

                                                                       or
23. Let the state denote the number of machines that
    are down. This yields a birth and death process                                                                λ
                                                                       (λ + μ1 ) α = λ + μ2 αβ = λ + μ2 α            = λ + λα
    with                                                                                                           μ
                                                                                                   λ
          3         2         1                                        and     μ1 α = λ ⇒ α =
     λ0 =   , λ1 =    , λ2 =    , λi = 0,        i≥3                                               μ1
         10        10        10
         1        2
     μ1 = , μ2 = , μ3 =
                           2                                           To get C, we observe that ∑ Pn, m = 1
         8        8        8                                                                            n, m

     The balance equations reduce to                                   but                                                 
                                                                                                  1                      1
     P1 =
          3/10
               P0 =
                    12
                       P0                                              ∑ Pn, m = C ∑ α ∑ β = C 1 − α
                                                                                             n      m
                                                                                                                        1−β
           1/8      5                                                  n, m
                                                                                
                                                                                   n     m
                                                                                              
            2/10      4     48                                                       λ       λ
     P2 =        P 1 = P1 =    P0                                      and C = 1 −        1−
             2/8      5     25                                                       μ1      μ2

            1/10      4       192                                      Therefore a solution of the form Cαn β n must be
     P3 =        P2 =    P3 =     P0
             2/8      10      250                                      given by
                                                                                       n            m
                     3                                                              λ     λ         λ     λ
     Hence, using ∑ Pi = 1 yields                                      Pn, m = 1 −              1−
                                                                                   μ1    μ1         μ2    μ2
                     0
                                                                     It is easy to verify that this also satisﬁes (c) and
              12   48   192 −1    250
     P0 = 1 +    +    +        =                                       (d) and is therefore the solution of the balance
              5    25   250      1522                                  equations.
     (a) Average number not in use
                                                                   27. It is a Poisson process by time reversibility. If
                                2136   1068                            λ > δμ, the departure process will (in the limit) be
             = P1 + 2P2 + 3P3 =      =
                                1522   761                             a Poisson process with rate δμ since the servers will
                                                                       always be busy and thus the time between depar-
     (b) Proportion of time both repairmen are busy                    tures will be independent random variables each
                              672   336                                with rate δμ.
             = P2 + P3 =          =
                             1522   761
                                                                   29. (a) Let the state be S, the set of failed machines.
25. If Ni (t) is the number of customers in the ith
    system (i = 1, 2), then let us take {N1 (t), N 2 (t)}               (b) For i ∈ S, j ∈ Sc ,
    as the state. The balance equation are with                              qS, S − i = μi /|S|, qS, S+j = λj
    n ≥ 1, m ≥ 1.
                                                                             where S − i is the set S with i deleted and S + j
     (a) λP0, 0 = μ2 P0, 1                                                   is similarly S with j added. In addition, |S|
     (b) Pn, 0 (λ + μ1 ) = λPn−1, 0 + μ2 Pn, 1                               denotes the number of elements in S.
     (c) P0, m (λ + μ2 ) = μ1 P1, m−1 + μ2 P0, m+1                      (c) PS qS, S−i = PS−i qS − i, S
                                                  Answers and Solutions                                                      37

    (d) The equation in (c) is equivalent to                    33. Suppose ﬁrst that the waiting room is of
                                                                    inﬁnite size. Let Xi (t) denote the number of cus-
         PS μi /|S| = PS − i λi
                                                                    tomers at server i, i = 1, 2. Then since each of
         or                                                         the M/M/1 processes {Xi (t)} is time-reversible,
                                                                    it follows by Problem 28 that the vector process
         PS = PS−i |S|λi /μi                                        {(X 1 (t), X 2 (t)), t ≥ 0} is a time-reversible Markov
         Iterating this recursion gives                             chain. Now the process of interest is just the trun-
                                                                   cation of this vector process to the set of states A
         PS = P0 (|S|)!    (λi /μi )                                where
                               i ∈S
                                                                     A = {(0, m) : m ≤ 4} ∪ {(n, 0) : n ≤ 4}
         where 0 is the empty set. Summing over all S
         gives                                                                ∪ {(n, m) : nm > 0, n + m ≤ 5}
                         
         1 = P0 ∑ (|S|)!   (λi /μi )                                 Hence, the probability that there are n with server 1
                    S            i ∈S
                                                                     and n with server 2 is

         and so                                                      Pn, m = k(λ1 /μ1 )n (1 − λ1 /μ1 )(λ2 /μ2 )m (1 − λ2 /μ2 ),
                            
                  (|S|)!             (λi /μi )                               = C(λ1 /μ1 )n (λ2 /μ2 )m ,   (n, m) ∈ A
                              i ∈S
         PS =                                                       The constant C is determined from
                ∑ (|S|)!              (λi /μi )
                S              i ∈S                                  ∑ Pn, n = 1
        As this solution satisﬁes the time reversibility             where the sum is over all (n, m) in A.
        equations, it follows that, in the steady state,
        the chain is time reversible with these limiting        35. We must ﬁnd probabilities Pin such that
        probabilities.
                                                                     Pin qnij = Pjn qnji
31. (a) This follows because of the fact that all of the
        service times are exponentially distributed and              or
        thus memoryless.                                             cPni qij = Pjn qji , if i ∈ A, j ∈
                                                                                                      /A
    (b) Let      n = (n1 , …, ni , …, nj , …, nr ),   where           Pi qij = cPnj qji , if i ∈
                                                                                               / A, j ∈ A
        ni > 0     and      let      n = (n1 , …, ni − 1, …,         Pi qij = Pj qji ,   otherwise
        nj − 1, …, nr ). Then qn, n = μi /(r − 1).
                                                                     Now, Pi qij = Pj qji and so if we let
    (c) The process is time reversible if we can ﬁnd
        probabilities P(n) that satisfy the equations                        kPi /c        if i ∈ A
                                                                     Pin =
         P(n)μi /(r − 1) = P(n )μj /(r − 1)                                 kPi           if i ∈
                                                                                                /A
                                                                     then we have a solution to the above equations. By
         where n and n are as given in part (b). The
                                                                     choosing k to make the sum of the Pjn equal to 1, we
         above equations are equivalent to
                                                                     have the desired result. That is,
         μi P(n) = μj /P(n )                                            *                +−1
         Since ni = n i + 1 and n j = nj + 1 (where nk             k=       ∑ Pi /c − ∑ Pi
                                                                              i ∈A            i∈
                                                                                               /A
         refers to the k th component of the vector n), the
         above equation suggests the solution
                                                                37. The state of any time is the set of down
                        
                        r
                                                                    components at that time. For S ⊂ {1, 2, …, n},
                                         n
         P(n) = C             (1/μk ) k
                                                                    i∈
                                                                     / S, j ∈ S
                        k=1

         where C is chosen to make the probabili-                    q(S, S + i) = λi
         ties sum to 1. As P(n) satisﬁes all the time                q(S, S − j) = μj α|S|
         reversibility equations it follows that the chain
         is time reversible and the P(n) given above are             where S + i = S ∪ {i}, S − j = S ∩ {j}c , |S| = number
         the limiting probabilities.                                 of elements in S.
38                                                   Answers and Solutions

     The time reversible equations are                                   exponential time with rate λ. As qik = vi Pik ,
                                                                         the result follows.
     P(S)μi α|S| = P(S − i)λi ,        i∈S
                                                                     (b) From (a)
     The above is satisﬁed when, for S = {i1 , i2 , …, ik }
                                                                             (λ + vi )P̄ij = ∑ qik P̄kj + λδij
                   λi1 λi2 · · · λik                                                           k
     P(S) =                                 P(φ)                         or
              μi1 μi2 · · · μik αk(k+1)/2
     where P(φ) is determined so that                                        −λδij = ∑ rik P̄kj − λP̄ij
                                                                                       k
     ∑ P(S) = 1                                                          or, in matrix terminology,
     where the sum is over all the 2n subsets of                             −λI = RP̄ − λI P̄
     {1, 2, …, n}.
                                                                                 = (R − λI)P̄
39. E[0(t)|x(0) = 1] = t − E[time in 1|X(0) = 1]                         implying that
                  λt     μ                                               P̄ = −λI(R − λI)−1 = −(R/λ − I)−1
       = t−          −         [1 − e−(λ+μ)t ]
                λ + μ (λ + μ)2                                                 = (I − R/λ)−1
     The ﬁnal equality is obtained from Example 7b (or                (c) Consider, for instance,
     Problem 38) by interchanging λ and μ.
                                                                             P{X(Y 1 + Y2 ) = j|X(0) = i}
41. (a) Letting Ti denote the time until a transition out
        of i occurs, we have                                                   = ∑ P{X(Y 1 + Y2 ) = j|X(Y 1 ) = k, X(0) = i)
                                                                                   k
          Pij = P{X(Y) = j} = P{X(Y) = j | Ti < Y}                               P{X(Y 1 ) = k|X(0) = i}

                 ×       vi + P{X(Y) = j|Y ≤ T } λ
                      vi + λ                  i λ+v
                                                   i                           = ∑ P{X(Y 1 + Y2 ) = j|X(Y 1 ) = k}P̄ik
                                vi + δij λ
                                                                                   k
              = ∑ Pik Pkj
                  k
                             vi + λ λ + vi                                     = ∑ P{X(Y 2 ) = j|X(0) = k}P̄ik
                                                                                   k
         The ﬁrst term on the right follows upon con-
                                                                               = ∑ P̄kj P̄ik
         ditioning on the state visited from i (which is k                         k
         with probability Pik ) and then using the lack of
         memory property of the exponential to assert                    and thus the state at time Y1 + Y2 is just the
         that given a transition into k occurs before time               2-stage transition probabilities of P̄ij . The gen-
         Y then the state at Y is probabilistically the                  eral case can be established by induction.
         same as if the process had started in state k               (d) The above results in exactly the same approx-
         and we were interested in the state after an                    imation as Approximation 2 in Section 6.8.
Chapter 7

1. (a) Yes,     (b) no,    (c) no.                                     Thus,

3. By the one-to-one correspondence of m(t) and F, it                  E[T|W] = (E[T] + 1/λ)(1 − e−λW )
   follows that {N(t), t ≥ 0} is a Poisson process with                Taking expectations gives
   rate 1/2. Hence,
                                                                       E[T] = (E[T] + 1/λ)(1 − E[e−λW ])
   P{N(5) = 0) = e−5/2
                                                                       and so
5. The random variable N is equal to N(I) + 1 where
                                                                                   1 − E[e−λW ]
   {N(t)} is the renewal process whose interarrival                    E[T] =
   distribution is uniform on (0, 1). By the results of                             λE[e−λW ]
   Example 2c,                                                         In the above, W is a random variable having distri-
                                                                       bution F and so
   E[N] = a (1) + 1 = e
                                                                                        ∞
                                                                             −λW
7. Once every ﬁve months.                                              E[e         ]=        e−λw f (w)dw
                                                                                        0
9. Ajob completion constitutes a reneval. Let T denote
   the time between renewals. To compute E[T] start                    N(t)  1  number of renewals in (X1 , t)
   by conditioning on W, the time it takes to ﬁnish the          11.        = +
                                                                        t    t               t
   next job:
                                                                       Since X1 < ∞, Proposition 3.1 implies that
   E[T] = E[E[T|W]]
                                                                       number of renewals in (X1 , t) 1
                                                                                                     − as t − ∞.
   Now, to determine E[T|W = w] condition on S, the                                 t                 μ
   time of the next shock. This gives
                     ∞                                          13. (a) N1 and N2 are stopping times. N3 is not.
   E[T|W = w] =           E[T|W = w, S = x]λe−λx dx                    (b) Follows immediately from the deﬁnition of Ii .
                     0                                                 (c) The value of Ii is completely determined
   Now, if the time to ﬁnish is less than the time of the                  from X1 , …, Xi−1 (e.g., Ii = 0 or 1 depend-
   shock then the job is completed at the ﬁnish time;                      ing upon whether or not we have stopped
   otherwise everything starts over when the shock                         after observing X1 , …, Xi−1 ). Hence, Ii is inde-
   occurs. This gives                                                      pendent of Xi .
                                                                             ∞               ∞
                           x + E[T], if x < w
   E[T|W = w, S = x] =
                           w,            if x ≥ w
                                                                       (d)    ∑ E[Ii ] = ∑ P{N ≥ i} = E[N]
                                                                             i=1             i=1
                                                                                            
   Hence,                                                              (e) E X1 + · · · + XN1 = E[N 1 ]E[X]
   E[T|W = w]                                                                 But X1 + · · · + XN1 = 5, E[X] = p and so

         w                            ∞                                     E[N 1 ] = 5/p
                                                                                               
     =        (x + E[T])λe−λx dx + w        λe−λx dx                          E X1 + · · · + XN2 = E[N 2 ]E[X]
         0                     w                                              E[X] = p, E[N 2 ] = 5p + 3(1 − p) = 3 + 2p
               −λ
     = E[T][1−e ] + 1/λ − we
                  w         −λ w  1
                                 − e−λw −we−λw                                                  
                                            λ                                 E X1 + · · · + XN2 = (3 + 2p)p


                                                            39
40                                                     Answers and Solutions

15. (a) Xi = amount of time he has to travel after his ith         25. Say that a new cycle begins each time a train is
        choice (we will assume that he keeps on mak-                   dispatched. Then, with C being the cost of a cycle,
        ing choices even after becoming free). N is the                we obtain, upon conditioning on N(t), the number
        number of choices he makes until becoming                      of arrivals during a cycle, that
        free.
                                                                     E[C] = E[E|C|N(t)]] = E[K + N(t)ct/2]
                      N
      (b) E[T] = E ∑ Xi = E[N]E [X]                                            = k + λct2 /2
                      1
          N is a geometric random variable with                        Hence,
          P = 1/3, so                                                                             E[C]
                                                                       average cost per unit time =    =
                                                                                                          K
                                                                                                            + λct/2
                                                                                                    t     t
                             1
          E[N] = 3, E[X] =     (2 + 4 + 6) = 4                         Calculus shows
                                                                                     that the preceding is minimized
                             3
                                                                       when t = 2K/(λc), with the average cost equal to
                                                                       √
          Hence, E[T] = 12.                                              2λKc.
                       
              N
                                     1
      (c) E   ∑ Xi |N = n = (n − 1) 2 (4 + 6) + 2 = 5n −               On the other hand, the average cost for the N
                                                                       policy of Example 7.12 is c(N − 1)/2 + λK/N. Treat-
              1
          3, since given N = n, X1 , …, Xn−1 are
                                              equally
                                                  
                                                                       ing N as a continuousvariable yields that its
          likely to be either 4 or 6, Xn = 2, E   ∑ 1 Xi =
                                                   n                   minimum occurs at N = √ 2λK/c, with a resulting
          4n.                                                          minimal average cost of 2λKc − c/2.
      (d) From (c),                                                27. Say that a new cycle begins when a machine fails;
                                                                     let C be the cost per cycle; let T be the time of a
              N
          E   ∑ Xi = E [5N − 3] = 15 − 3 = 12                          cycle.
              1
                                                                                        c2           λ1   c1         λ2   c1
                                                                       E[C] = K +             +               +
                                                                                    λ 1 + λ2     λ 1 + λ2 λ 2    λ 1 + λ2 λ 1
17. (i) Yes. (ii) No—Yes, if F exponential.
                                                                                  1            λ1     1        λ2     1
                                                                       E[T] =            +              +
19. Since, from Example 2c, m(t) = et − 1, 0 < t ≤ 1,                         λ 1 + λ2     λ 1 + λ2 λ 2    λ 1 + λ2 λ 1
    we obtain upon using the identity t + E[Y(t)] =                    T the long-run average cost per unit time is
    μ[m(t) + 1] that E[Y(1)] = e/2 − 1.                                E[C]/E[T].

        μG                                                    29. (a) Imagine that you are paid a reward equal to
21.           ,   where μG is the mean of G.
      μ + 1/λ                                                         Wi on day i. Since everything starts over when
                                                                      a busy period ends, it follows that the reward
23. Using that E[X] = 2p − 1, we obtain from Wald’s                   process constitutes a renewal reward process
    equation when p = 1/2 that                                        with cycle time equal to N and with the reward
                                                                    during a cycle equal to W1 + · · · + WN . Thus
                         T
                                                                      E[W], the average reward per unit time, is
    E[T](2p − 1) = E ∑ Xj
                        j=1
                                                                      E[W 1 + · · · + WN ]/E[N].
                                                                (b) The sum of the times in the system of all
                            1 − (q/p)i           1 − (q/p)i
                 = (N − i)             − i   1 −                      customers and the total amount of work that
                            1 − (q/p)N           1 − (q/p)N           has been processed both start equal to 0 and
                       1 − (q/p)i                                     both increase at the same rate. Hence, they are
                 =N               −i
                      1 − (q/p)N                                      always equal.
                                                                  (c) This follows from (b) by looking at the value
    yielding the result:                                              of the two totals at the end of the ﬁrst busy
                                                                      period.
               1 − (q/p)i
            N              −i                                     (d) It is easy to see that N is a stopping time
              1 − (q/p)N
    E[T] =                     , p = 1/2                                 the Li , i ≥ 1, and so, by Wald’s Equation,
                                                                      for
                 2p − 1                                                   N
                                                                      E ∑ Li = E[L]E[N]. Thus, from (a) and (c),
    When p = 1/2, we can easily show by a condition-                     i=1
    ing argument that E[T] = i(N − i)                                 we obtain that E[W] = E[L].

                                               Answers and Solutions                                                   41
                                                                                        ∞
31. P{E(t) > x|A(t) = s}                                               where μ =             (1 − F(s))ds is the mean time
                                                                                         0
         = P{0 renewals in (t, t + x]|A(t) = s}                        that a satellite orbits. Hence,
         = P{interarrival > x + s|A(t) = s}
                                                                                    1/λ
         = P{interarrival > x + s|interarrival > s}                    e−λμ =
                                                                                 1/λ + E[T]
           1 − F(x + s)
         =                                                             and so
             1 − F(s)
                                                                                 1 − e−λμ
33. Let B be the amount of time the server is busy in                  E[T] =
                                                                                  λe−λμ
    a cycle; let X be the remaining service time of the
    person in service at the beginning of a cycle.             37. (a) This is an alternating renewal process, with
    E[B] = E[B|X < t](1 − e−λt ) + E[B|X > t]e−λt                      the mean off time obtained by conditioning on
                                                                       which machine fails to cause the off period.
                                            1
        = E[X|X < t](1 − e−λt ) +     t+            e−λt                          3
                                           λ+μ                         E[off] = ∑ E[off|i fails]P{i fails}
                                                                                 i=1
                                               1
        = E[X] − E[X|X > t]e−λt +        t+             e−λt                                λ1                  λ2
                                              λ+μ                              = (1/5)              + (2)
                                                                                     λ 1 + λ2 + λ3        λ 1 + λ2 + λ3
                     1                    1                                                    λ3
        = μ1 − t +         e−λt +   t+           e−λt                            + (3/2)
                     μ                   λ+μ                                             λ 1 + λ2 + λ 3
                          
             1       λ −λt
        =        1−     e                                              As the on time in a cycle is exponential with
             μ      λ+μ                                                rate equal to λ1 + λ2 + λ3 , we obtain that p,
    More intuitively, writing X = B + (X − B), and not-                the proportion of time that the system is
    ing that X − B is the additional amount of service                 working is
    time remaining when the cycle ends, gives
                                                                              1/(λ1 + λ2 + λ3 )
    E[B] = E[X] − E[X − B]                                             p=
                                                                                    E[C]
          1  1                                                         where
         =  − P(X > B)
          μ μ
                                                                       E[C] = E[cycle time]
          1  1      λ
         = − e−λt                                                           = 1/(λ1 + λ2 + λ3 ) + E[off]
          μ μ     λ+μ
    The long-run proportion of time that the server is             (b) Think of the system as a renewal reward pro-
              E[B]                                                     cess by supposing that we earn 1 per unit time
    busy is         .                                                  that machine 1 is being repaired. Then, r1 , the
            t + 1/λ
                                                                       proportion of time that machine 1 is being
35. (a) We can view this as an M/G/∞ system where                      repaired is
        a satellite launching corresponds to an arrival
                                                                                            λ1
        and F is the service distribution. Hence,                             (1/5)
                                                                                      λ 1 + λ2 + λ3
                                                                       r1 =
        P{X(t) = k} = e−λ(t) [λ(t)]k /k!                                                 E[C]
                        t
                                                                   (c) By assuming that we earn 1 per unit time when
        where λ(t) = λ     (1 − F(s))ds.
                           0                                           machine 2 is in a state of suspended anima-
    (b) By viewing the system as an alternating                        tion, shows that, with s2 being the propor-
        renewal process that is on when there is at least              tion of time that 2 is in a state of suspended
        one satellite orbiting, we obtain                              animation,
                                  1/λ                                                       λ1                    λ3
        lim P{X(t) = 0} =                                                     (1/5)                 + (3/2)
                               1/λ+ E[T]                                              λ 1 + λ2 + λ3         λ 1 + λ2 + λ3
                                                                       s2 =
                                                                                                   E[C]
        where T, the on time in a cycle, is the quantity
        of interest. From part (a)
                                                               39. Let B be the length of a busy period. With S equal
        lim P{X(t) = 0} = e−λμ                                     to the service time of the machine whose failure
42                                                    Answers and Solutions

      initiated the busy period, and T equal to the                   or
      remaining life of the other machine at that moment,                            2             1
      we obtain                                                       r1 = r2 =        ,    r3 =
                                                                                    5             5
      E[B] = E[B|S = s]g(s)ds                                                        2
                                                                      (a) r1 =
                                                                                     5
      Now,                                                                            ri μi
                                                                      (b) Pi =                and so,
      E[B|S = s] = E[B|S = s, T ≤ s](1 − e−λs )                                      ∑i ri μi
                      + E[B|S = s, T > s]e−λs                                        2       4       3
                                                                              P1 =     , P2 = , P 3 = .
                                                                                     9       9       9
                    = (s + E[B])(1 − e−λs ) + se−λs
                                                                  47. (a) By conditioning on the next state, we obtain
                    = s + E[B](1 − e−λs )                                 the following:
      Substituting back gives
                                                                              μj = E[time in i]
      E[B] = E[S] + E[B]E[1 − e−λs ]                                            = ∑ E[time in i|next state is j]Pij
      or                                                                        = ∑ tij Pij
                  E[S]                                                               i
      E[B] =
                 E[e−λs ]                                             (b) Use the hint. Then,
      Hence,
                                                                              E[reward per cycle]
                   1/(2λ)
      E[idle] =                                                                 = E[reward per cycle|next state is j]Pij
                1/(2λ) + E[B]
                                                                                = tij Pij
       1
          (1 − F(x)dx                                                      Also,
41.
                μ
       0                                                                   E[time of cycle] = E[time between visits to i]
         ⎧
         ⎪
         ⎪
             1 2−x         3                                               Now, if we had supposed a reward of 1 per unit
         ⎪
         ⎪            dx = in part (i)
         ⎨ 0      2        4                                               time whenever the process was in state i and
      =                                                                   0 otherwise then using the same cycle times as
         ⎪
         ⎪   1
         ⎪
         ⎪                                                                 above we have that
         ⎩     e−x dx = 1 − e−1 in part (ii)
             0                                                                       E[reward is cycle]         μi
                                                                           Pi =                         =
                                                                                      E[time of cycle]    E[time of cycle]
43. Since half the interarrival times will be exponential
    with mean 1 and half will be exponential with mean                     Hence,
    2, it would seem that because the exponentials with
    mean 2 will last, on average, twice as long, that                      E[time of cycle] = μi /Pi

                2         1                                                and so
      F̄e (x) = e−x/2 + e−x
                3         3
                                                                           average reward per unit time = tij Pij Pi /μi
      With μ = (1)1/2 + (2)1/2 = 3/2 equal to the mean
      interarrival time                                                    The above establishes the result since the aver-
                 ∞                                                        age reward per unit time is equal to the pro-
                    F̄(y)
      F̄e (x) =           dy                                               portion of time the process is in i and will next
                  x   μ
                                                                           enter j.
      and the earlier formula is seen to be valid.
                                                                  49. Think of each interarrival time as consisting of n
45. The limiting probabilities for the Markov chain are               independent phases—each of which is exponen-
    given as the solution of                                          tially distributed with rate λ—and consider the
                 1                                                    semi–Markov process whose state at any time is
      r1 = r2      + r3                                               the phase of the present interarrival time. Hence,
                 2
      r2 = r1                                                         this semi-Markov process goes from state 1 to 2 to
                                                                      3 … to n to 1, and so on. Also the time spent in each
      r1 + r2 + r3 = 1                                                state has the same distribution. Thus, clearly the
                                                 Answers and Solutions                                                     43

    limiting probabilities of this semi-Markov chain are            gives the results
    Pi = 1/n, i = 1, …, n. To compute lim P{Y(t) < x},
    we condition on the phase at time t and note that if            P(2) ≈ .4425, E[M] ≈ 12.18
    it is n – i + 1, which will be the case with probability
    1/n, then the time until a renewal occurs will be the                T                     T
    sum of i exponential phases, which will thus have          57. P{ ∑ Xi > x} = P{ ∑ Xi > x|T = 0}(1 − ρ)
                                                                         i=1                   i=1
    a gamma distribution with parameters i and λ.
                                                                                                     T
51. It is an example of the inspection paradox. Because                                      + P{ ∑ Xi > x|T > 0}ρ
                                                                                                     i=1
    every tourist spends the same time in departing
    the country, those questioned at departure consti-                         T
    tute a random sample of all visiting tourists. On               = P{ ∑ Xi > x|T > 0}ρ
                                                                             i=1
    the other hand, if the questioning is of randomly
    chosen hotel guests then, because longer staying                       ∞            T
                                                                                                                F̄(y)
    guests are more likely to be selected, it follows that          =ρ             P{ ∑ Xi > x|T > 0, X1 = y}         dy
                                                                             0       i=1                          μ
    the average time of the ones selected will be larger
    than the average of all tourists. The data that the                       x         T
                                                                         ρ
    average of those selected from hotels was approx-               =              P{ ∑ Xi > x|T > 0, X1 = y}F̄(y)dy
                                                                         μ     0     i=1
    imately twice as large as from those selected at
                                                                                    ∞
    departure are consistent with the possibility that                   ρ
                                                                         +      F̄(y)dy
    the time spent in the country by a tourist is expo-                  μ x
    nential with a mean approximately equal to 9.                                                
                                                                      ρ x                       ρ ∞
                                                                    =       h(x − y)F̄(y)dy +         F̄(y)dy
55. E[T(1)] = (.24)−2 + (.4)−1 = 19.8611,                             μ 0                       μ x
                                                                                                        
     E[T(2)] = 24.375, E[T12 ] = 21.875,                                     ρ x                      ρ x
                                                                    = h(0) +        h(x − y)F̄(y)dy −       F̄(y)dy
     E[T2, 1 ] = 17.3611. The solution of the equations                      μ 0                      μ 0

     19.861 = E[M] + 17.361P(2)                                     where the ﬁnal equality used that
                                                                                
     24.375 = E[M] + 21.875P(1)                                                ρ ∞
                                                                    h(0) = ρ =       F̄(y)dy
          1 = P(1) + P(2)                                                      μ 0
Chapter 8

1. (a) E[number of arrivals]                                    Also, CA = $C + $1/customer × LA customers
          = E[E{number of arrivals|service                                           1
                                                                         = $C + $1 ×
               period is S}]                                                         2
                                                                                1
                                                                         = $C + / hour
          = E[λS]                                                               2
          = λ/μ                                                 (b) We can restate the problem this way: If CA =
   (b) P{0 arrivals}                                                CM , solve for C.

          = E[P{0 arrivals|service period is S}]                               1
                                                                     4=C+        ⇒ C = $3.50/hour
                                                                               2
          = E[P{N(S) = 0}]
                                                                     i.e., $3.50/hour is the most the employer
          = E[e−λS ]                                                 should be willing to pay Alice to work. At a
             x                                                      higher wage his average cost is lower with
          =     e−λs μe−μs ds                                        Mary working.
             0
               μ
          =                                                                       ∗
                                                             5. Let I equal 0 if WQ = 0 and let it equal 1 otherwise.
            λ+μ
                                                                Then,
3. Let CM = Mary’s average cost/hour and CA =                        ∗ |I = 0] = 0
                                                                  E[WQ
   Alice’s average cost/hour.
                                                                     ∗ |I = 1] = (μ − λ)−1
                                                                  E[WQ
   Then, CM = $3 + $1× (Average number of cus-
                                                                     ∗ |I = 0) = 0
                                                                Var(WQ
   tomers in queue when Mary works),
                                                                     ∗ |I = 1) = (μ − λ)−2
                                                                Var(WQ
   and CA = $C + $1 × (Average number of cus-
   tomers in queue when Alice works).                           Hence,
   The arrival stream has parameter λ = 10, and there                   ∗ |I] = (μ − λ)−2 λ/μ
                                                                 E[Var(WQ
   are two service parameters—one for Mary and one
                                                                       ∗ |I]) = (μ − λ)−2 λ/μ(1 − λ/μ)
                                                                Var(E[WQ
   for Alice:

   μM = 20,    μA = 30.                                         Consequently, by the conditional variance formula,

   Set   LM = average number of customers in                         ∗           λ                   λ
                                                                Var(WQ )=               2
                                                                                            +    2
              queue when Mary works and                                      μ(μ − λ)           μ (μ − λ)
         LA = average number of customers in
              queue when Alice works.                        7. To compute W for the M/M/2, set up balance equa-
                                                                tions as
                                          10
   Then using Equation (3.2), LM =               =1                      λp0 = μp1               (each server has rate μ)
                                       (20 − 10)
                                          10       1              (λ + μ)p1 = λp0 + 2μp2
                                LA =             =
                                       (20 − 10)   2
                                                                (λ + 2μ)pn = λpn−1 + 2μpn+1 ,               n≥2
   So    CM = $3 + $1/customer × LM customers
            = $3 + $1                                           These have solutions Pn = ρn /2n−1 p0 where
            = $4/hour                                           ρ = λ/μ.


                                                        44
                                        Answers and Solutions                                                   45
                              ∞
                                                           Then,
The boundary condition ∑ Pn = 1 implies
                              n=0
                                                           WQ1 > W2 ⇔ 1 >    λ
                                                                  Q   2   (2μ + λ)
       1 − ρ/2   (2 − ρ)                                   λ < 2μ
P0 =           =
       1 + ρ/2   (2 + ρ)
                                                           Since we assume λ < 2μ for stability in the
Now we have Pn , so we can compute L, and hence            M/M/1, WQ    2
                                                                           < WQ1
                                                                                 whenever this comparison is
W from L = λW :                                            possible, i.e., whenever λ < 2μ.
       ∞              ∞
                             ρ n−1
L = ∑ npn = ρp0 ∑ n                                    9. Take the state to be the number of customers at
                             2
      n=0            n=0                                  server 1. The balance equations are
                      ∞
                             ρ n
              = 2p0 ∑ n                                    μP0 = μP1
                             2
                     n=0
                   (2 − ρ) (ρ/2)                           2μPj = μPj+1 + μPj−1 ,      1≤j<n
              =2
                   (2 + ρ) (1 − ρ/2)2                      μPn = μPn−1
                       4ρ                                       n
              =
                  (2 + ρ)(2 − ρ)                           1 = ∑ Pj
                                                                j=0
                        4μλ
              =
                  (2μ + λ)(2μ − λ)                         It is easy to check that the solution to these equa-
From L = λW we have                                        tions is that all the Pj s are equal, so Pj = 1/(n + 1),
                                                           j = 0, …, n.
                          4μ
W = W m/ m/ 2 =
                    (2μ + λ)(2μ − λ)                  11. (a) λP0 = αμP1
The M/M/1 queue with service rate 2μ has                        (λ + αμ)Pn = λPn−1 + αμPn+1 ,        n≥1
                1
Wm/m/1 =                                                        These are exactly the same equations as in the
              2μ − λ                                            M/M/1 with αμ replacing μ. Hence,
from Equation (3.3). We assume that in the                            n           
                                                                       λ           λ
M/M/1 queue, 2μ > λ so that the queue is stable.                Pn =         1−        , n≥0
                             4μ                                       αμ          αμ
But then 4μ > 2μ + λ, or           > 1, which
                          2μ + λ                                and we need the condition       λ < αμ.
implies Wm/m/2 > Wm/m/1.
                                                           (b) If T is the waiting time until the customer ﬁrst
The intuitive explanation is that if one ﬁnds the              enters service, then conditioning on the num-
queue empty in the M/M/2 case, it would do no                  ber present when he arrives yields
good to have two servers. One would be better off              E[T] = ∑ E[T|n present]Pn
with one faster server.                                                   n
                                                                            n
         1 = W (M/M/1)
Now let WQ                                                            =∑      Pn
                                                                          n μ
              Q

             2 = W (M/M/2)
            WQ                                                          L
                  Q                                                   =
                                                                        μ
Then,
                                                                Since L = ∑ nPn , and the Pn are the same as
 1 = Wm/m/1 − 1/2μ
WQ                                                              in the M/M/1 with λ and αμ, we have that
 2 = Wm/m/2 − 1/μ                                               L = λ/(αμ − λ) and so
WQ
                                                                             λ
So,                                                             E[T] =
                                                                          μ(αμ − λ)
 1          λ
WQ =                       (3.3)
        2μ(2μ − λ)                                         (c) P{enters service exactly n times}
and                                                                 = (1 − α)n−1 α
 2             λ2                                          (d) This is expected number of services × mean
WQ =                                                           services time = 1/αμ
        μ(2μ − λ)(2μ + λ)
46                                                    Answers and Solutions

     (e) The distribution is easily seen to be memory-                the state refers to the number of customers at server
         less. Hence, it is exponential with rate αμ.                 i, i = 1, 2. The balance equations are

13. Let the state be the idle server. The balance equa-                 2P0, 0 = 6P0, 1
    tions are                                                           8P0, 1 = 4P1, 0 + 4P1, 1
        Rate Leave = Rate Enter,                                        6P1, 0 = 2P0, 0 + 6P1, 1
                         μ           μ
       (μ2 + μ3 )P1 = μ +1 μ P3 + μ +1 μ P2 ,                          10P1, 1 = 2P0, 1 + 2P1, 0
                       1    2      1    3
                         μ           μ
       (μ1 + μ3 )P2 = μ +2 μ P1 + μ +2 μ P3 ,                                  1 = P0, 0 + P0, 1 + P1, 0 + P1, 1
                       2    3      2    1
     μ1 + μ2 + μ3 = 1.                                                Solving these equations gives P0, 0 = 1/2,
                                                                      P0, 1 = 1/6, P1, 0 = 1/4, P1, 1 = 1/12.
     These are to be solved and the quantity Pi repre-
     sents the proportion of time that server i is idle.
                                                                      (a) P1, 1 = 1/12
15. There are four states = 0, 1A , 1B , 2. Balance equa-                           L    P0, 1 + P1, 0 + 2P1, 1   7
    tions are                                                         (b) W =          =                        =
                                                                                    λa         2(1 − P1, 1 )      22
      2P0 = 2P1B                                                              P0, 0 + P0, 1   8
     4P1A = 2P0 + 2P2                                                 (c)                   =
                                                                               1 − P1, 1      11
     4P1B = 4P1A + 4P2
      6P2 = 2P1B                                                  19. (a) Say that the state is (n, 1) whenever it is a good
                                                                          period and there are n in the system, and say
                                          3                               that it is (n, 2) whenever it is a bad period and
     P0 + P1A + P1B + P2 = 1 ⇒ P0 =
                                          9                               there are n in the system, n = 0, 1.
             2        3       1                                       (b) (λ1 + α1 )P0, 1 = μP1, 1 + α2 P0, 2
     P1A =     , P1B = , P2 =
             9        9       9
                                                                              (λ2 + α2 )P0, 2 = μP1, 2 + α1 P0, 1
                      2
     (a) P0 + P1B =                                                            (μ + α1 )P1, 1 = λ1 P0, 1 + α2 P1, 2
                      3
     (b) By conditioning upon whether the state was 0                          (μ + α2 )P1, 2 = λ2 P0, 2 + α1 P1, 1
         or 1B when he entered we get that the desired
         probability is given by                                            P0, 1 + P0, 2 + P1, 1 + P1, 2 = 1

          1   12   4                                                  (c) P0, 1 + P0, 2
            +    =
          2   26   6                                                  (d) λ1 P0, 1 + λ2 P0, 2
                            7
     (c) P1A + P1B + 2P2 =                                        21. (a) λ1 P10
                            9
     (d) Again, condition on the state when he enters                 (b) λ2 (P0 + P10 )
         to obtain
                                                                  (c) λ1 P10 /[λ1 P10 + λ2 (P0 + P10 )]
         1 1     1     1 1   21      7
              +      +     +      =                                   (d) This is equal to the fraction of server 2’s cus-
         2 4     2     2 4   62      12                                   tomers that are type 1 multiplied by the pro-
          This could also have been obtained from (a)                     portion of time server 2 is busy. (This is true
                                      L                                   since the amount of time server 2 spends with
          and (c) by the formula W = .                                    a customer does not depend on which type of
                                      λa
                            7                                             customer it is.) By (c) the answer is thus
                                  7
          That is, W = 9  =       .                                       (P01 + P11 )λ1 P10 /[λ1 P10 + λ2 (P0 + P10 )]
                            2    12
                          2
                            3
                                                                  23. (a) The states are n, n ≥ 0, and b. State n means
17. The state space can be taken to consist of states                     there are n in the system and state b means
    (0, 0), (0, 1), (1, 0), (1, 1), where the ith component of            that a breakdown is in progress.
                                                   Answers and Solutions                                                 47

    (b) βPb = a(1 − P0 )                                                   PnS = Pr{n customers in system, special cus-
                                                                                  tomer in service}, and
          λP0 = μP1 + βPb
                                                                           P0 = Pr{0 customers in system}.
          (λ + μ + a)Pn = λPn−1 + μPn+1 ,      n≥1                         (λ + θ)P0 = μP1 + μ1 P1S
                         ∞                                                 (λ + θ + μ)Pn = λPn−1 + μPn+1 + μ1 Pn+1
                                                                                                               S
    (c) W = L/λn = ∑ nPa /[λ(1 − Pb )]
                        n=1                                                (λ + μ)PnS = θPn−1 + λPnS−1 ,
    (d) Since rate at which services are completed =                                                  
                                                                                        n ≥ 1 P0S = P0
        μ(1 − P0 − Pb ) it follows that the proportion of
        customers that complete service is
                                                                      (c) Since service is memoryless, once a customer
        μ(1 − P0 − Pb )/λa                                                resumes service it is as if his service has
           = μ(1 − P0 − Pb )/[λ(1 − Pb )]                                 started anew. Once he begins a particular ser-
        An equivalent answer is obtained by condi-                        vice, he will complete it if and only if the next
        tioning on the state as seen by an arrival. This                  arrival of the special customer is after his ser-
        gives the solution                                                vice. The probability of this is Pr {Service <
                                                                          Arrival of special customer} = μ/(μ + θ), since
          ∞
                                                                          service and special arrivals are independent
          ∑ Pn [μ/(μ + a)]n+1                                             exponential random variables. So,
          n=0
                                                                           Pr{bumped exactly n times}
          where the above uses that the probability that
          n + 1 services of present customers occur                            = (1 − μ/(μ + θ))n (μ/(μ + θ))
          before a breakdown is [μ/(μ + a)]n+1 .
                                                                               = (θ/(μ + θ))n (μ/(μ + θ))
    (e) Pb
                                                                           In essence, the number of times a customer is
25. (a)                λP0 = μA PA + μB PB                                 bumped in service is a geometric random vari-
                                                                           able with parameter μ/(μ + θ).
                (λ + μA )PA = aλP0 + μB P2
                                                                 29. (a) Let state 0 mean that the server is free; let state
                (λ + μB )PB = (1 − a)λP0 + μA P2
                                                                         1 mean that a type 1 customer is having a wash;
          (λ + μA +μB )Pn = λPn−1 + (μA + μB )Pn+1                      let state 2 mean that the server is cutting hair;
                                                                         and let state 3 mean that a type 3 is getting a
          n≥2      where     P1 = PA + PB .                              wash.
                                                                     (b) λP0 = μ1 P1 + μ2 P2
                             ∞
                                                                           μ1 P1 = λp1 P0
    (b) L = PA + PB + ∑ nPn
                           n=2                                             μ2 P2 = λp2 P0 + μ1 P3
          Average number of idle servers = 2P0 +
          PA + PB .                                                        μ1 P3 = λp3 P0
                                 ∞
                        μA                                                 P0 + P1 + P2 + P3 = 1
    (c) P0 + PB +             ∑ Pn
                      μA + μB n=2
                                                                      (c) P2
27. (a) The special customer’s arrival rate is act θ                  (d) λP0
        because we must take into account his ser-                        Direct substitution now veriﬁes the equation.
        vice time. In fact, the mean time between his
        arrivals will be 1/θ + 1/μ1 . Hence, the arrival         31. The total arrival rates satisfy
        rate is (1/θ + 1/μ1 )−1 .
    (b) Clearly we need to keep track of whether the                  λ1 = 5
        special customer is in service. For n ≥ 1,                             1    1
        set                                                           λ2 = 10 +  5 + λ3
                                                                               3    2
        Pn = Pr{n customers in system regular cus-                             1
               tomer in service},                                     λ3 = 15 + 5 + λ2
                                                                               3
48                                                 Answers and Solutions

     Solving yields that      λ1 = 5, λ2 = 40, λ3 = 170/3.         (b) The average amount of work as seen by a
     Hence,                                                            departure is equal to the average number it
           3                                                           sees multiplied by the mean service time (since
                λi       82
      L=∑              =                                               no customers seen by a departure have yet
             μ
          i=1 i −  λ i   13                                            started service). Hence,
               L          41                                           Average work as seen by a departure
     W=                =
          r1 + r2 + r3   195                                              = average number it sees × E[S]
                                                                          = average number an arrival sees × E[S]
33. (a) Use the Gibbs sampler to simulate a Markov                        = LE[S] by Poisson arrivals
        chain whose stationary distribution is that of
        the queuing network system with m − 1 cus-                           = λ(W Q + E[S])E[S]
        tomers. Use this simulated chain to estimate
                                                                                 2          2
        Pi, m−1 , the steady state probability that there                    = λ E[S]E[S ] + λ(E[S])2
        are i customers at server j for this system.                            λ − λE[S]
        Since, by the arrival theorem, the distribu-
        tion function of the time spent at server j in         39. (a) a0 = P0 due to Poisson arrivals. Assuming
                                      m− 1                             that each customer pays 1 per unit time
        the m customer system is ∑i=0 Pi, m−1 Gi+1(x) ,
                                                                       while in service the cost identity (2.1) states
        where Gk (x) is the probability that a gamma                   that
        (k, μ) random variable is less than or equal to                Average number in service = λE[S]
        x, this enables us to estimate the distribution
                                                                       or
        function.
     (b) This quantity is equal to the average number                   1 − P0 = λE[S]
         of customers at server j divided by m.
                                                                   (b) Since a0 is the proportion of arrivals that have
35. Let S and U denote, respectively, the service time                 service distribution G1 and 1 − a0 the propor-
    and value of a customer. Then U is uniform on                      tion having service distribution G2 , the result
    (0, 1) and                                                         follows.
                                                                   (c) We have
     E[S|U] = 3 + 4U,      Var(S|U) = 5
                                                                                     E[I]
     Hence,                                                             P0 =
                                                                                 E[I] + E[B]
     E[S] = E{E[S|U]} = 3 + 4E[U] = 5                                      and   E[I] = 1/λ and thus,
     Var(S) = E[Var(S|U)] + Var(E[S|U])
                                                                                 E[B] = 1 − P0
               = 5 + 16Var(U) = 19/3                                                     λP0
     Therefore,                                                                       = E[S]
                                                                                        1 − λE[S]
     E[S2 ] = 19/3 + 25 = 94/3                                          Now from (a) and (b) we have
                          94λ/3                                         E[S] = (1 − λE[S])E[S1 ] + λE[S]E[S2 ]
     (a) W = WQ + E[S] =          +5
                          1 − δλ
                                                                        or
                            94λ/3
     (b) WQ + E[S|U = x] =         + 3 + 4x                                                 E[S1 ]
                            1 − δλ                                      E[S] =
                                                                                     1 + λE[S1 ] + λE[S2 ]
37. (a) The proportion of departures leaving behind                     Substitution into E[B] = E[S]/(1 − λE[S]) now
        0 work                                                          yields the result.
          = proportion of departures leaving an
             empty system                                      41. E[N] = 2, E[N 2 ] = 9/2, E[S2 ] = 2E2 [S] = 1/200
          = proportion of arrivals ﬁnding an empty                         1 5
                                                                               /4 + 4 · 2/400   41
            system                                                    W = 20 2                =
          = proportion of time the system is empty                              1 − 8/20        480
            (by Poisson arrivals)                                             41   1   17
                                                                     WQ =        −   =
          = P0                                                                480 20   480
                                               Answers and Solutions                                                      49

43. Problem 42 shows that if μ1 > μ2 , then serving 1’s           Hence,
    ﬁrst minimizes average wait. But the same argu-                                           
                                                                                    2           α
    ment works if c1 μ1 > c2 μ2 , i.e.,                           E[S2 ] =                +2
                                                                                (μ + β) 2   β(μ  + α)
    E(S1 )
           <
             E(S2 )                                                                                 
     c1       μ1                                                                     α    1    α
                                                                                +           +
                                                                                   μ+α μ      μβ
45. By regarding any breakdowns that occur during a                                                                 
                                                                                     α    2    2 1      α          2
    service as being part of that service, we see that                          +            +        +      + E[S   ]
                                                                                   μ + α β2    β μ      μβ
    this is an M/G/1 model. We need to calculate the
    ﬁrst two moments of a service time. Now the time              Now solve for E[S2 ]. The desired answer is
    of a service is the time T until something happens
    (either a service completion or a breakdown) plus                             λE[S2 ]
                                                                  WQ =
    any additional time A. Thus,                                               2(1 − λE[S])
    E[S] = E[T + A]                                               In the above, Sα is the additional service needed
                                                                  after the breakdown is over. Sα has the same dis-
          = E[T] + E[A]
                                                                  tribution as S. The above also uses the fact that
    To compute E[A] we condition upon whether the                 the expected square of an exponential is twice the
    happening is a service or a breakdown. This gives             square of its mean.
                             μ
    E[A] = E[A|service]                                          Another way of calculating the moments of S is to
                            μ+α                                  use the representation
                                  α
              + E[A|breakdown]
                                μ+α                                        N
                                α                                 S = ∑ (T i + Bi ) + TN+1
             = E[A|breakdown]                                           i=1
                               μ+α
                             α                                    where N is the number of breakdowns while a cus-
             = (1/β + E[S])
                            μ+α                                   tomer is in service, Ti is the time starting when ser-
    Since, E[T] = 1/(α + μ)       we obtain                       vice commences for the ith time until a happening
               1                  α                               occurs, and Bi is the length of the ith breakdown.
    E[S] =        + (1/β + E[S])                                  We now use the fact that, given N, all of the ran-
              α+μ                μ+α
                                                                  dom variables in the representation are indepen-
    or
                                                                  dent exponentials with the Ti having rate μ + α
    E[S] = 1/μ + α/(μβ)                                           and the Bi having rate β. This yields
    We also need E[S2 ], which is obtained as follows.                 E[S|N] = (N + 1)/(μ + α) + N/β
    E[S2 ] = E[(T + A)2 ]                                         Var(S|N) = (N + 1)/(μ + α)2 + N/β 2
             = E[T 2 ] + 2E[AT] + E[A2 ]                          Therefore, since 1 + N is geometric with mean
                   2
             = E[T ] + 2E[A]E[T] + E[A ]   2                      (μ + α)/μ (and variance α(α + μ)/μ2 ) we obtain
    The independence of A and T follows because                   E[S] = 1/μ + α/(μβ)
    the time of the ﬁrst happening is independent of
    whether the happening was a service or a break-               and, using the conditional variance formula,
    down. Now,
                                                                  Var(S) = [1/(μ + α) + 1/β]2 α(α + μ)/μ2
         2         2
    E[A ] = E[A |breakdown]        α
                                  μ+α                                            + 1/[μ(μ + α)] + α/μβ 2 )
             α
         =      E[(down time + Sα )2 ]
           μ+α                                               47. For k = 1, Equation (8.1) gives
             α ,                                    -
         =        E[down2 ] + 2E[down]E[S] + E[S2 ]                            1           (λ)                  λ(ES)
           μ+α                                                    P0 =               =                 P1 =
                                                                           1 + λE(S)   (λ) + E(S)             1 + λE(S)
                                           
             α     2   2 1      α          2                                 E(S)
         =           +       +        + E[S ]                          =
           μ + α β2    β μ      μβ                                         λ + E(S)
50                                                       Answers and Solutions

     One can think of the process as an alteracting                      These are exactly the Erlang probabilities given
     renewal process. Since arrivals are Poisson, the time               above since E[A] = 1/λ. Note this uses Poisson
     until the next arrival is still exponential with                    arrivals in an essential way, viz., to know the distri-
     parameter λ.                                                        bution of time until the next arrival after a service
                                                                         is still exponential with parameter λ.
     end of                      end of
     service       arrival       service                                        (λE[S])3
                                                                     49. P3 =      3!      ,   λ = 2, E[S] = 1
                                                                               3
                                                                                  (λE[S])j
                                           A         S    states              ∑ j!
               A             S                                                j=0
                                                                               8
                                                                            =
     The basic result of alternating renewal processes is                     38
     that the limiting probabilities are given by
                                                                     51. Note that when all servers are busy, the depar-
                                E(S)                                     tures are exponential with rate kμ. Now see
     P{being in “state S”} =             and
                             E(A) + E(S)                                 Problem 26.

                                          E(A)                       53. 1/μF < k/μG , where μF and μG are the respective
     P{being in “state A”} =
                                       E(A) + E(S)                       means of F and G.
Chapter 9

1. If xi = 0, φ(x) = φ(0i , x).                                     9. (a) A component is irrelevant if its functioning or
    If xi = 1, φ(x) = φ(1i , x).                                           not functioning can never make a difference as
                                                                           to whether or not the system functions.
3. (a) If φ is series, then φ(x) = mini xi and so φD (x) =             (b) Use the representation (2.1.1).
       1 − mini (1 − xi ) = max xi , and vice versa.                   (c) Use the representation (2.1.2).
   (b) φD,D (x) = 1 − φD (1 − x)
                                                                   11. r(p) = P{either x1 x3 = 1 or x2 x4 = 1}
                       = 1 − [1 − φ(1 − (1 − x))]
                                                                               P{either of 5 or 6 work}
                       = φ(x)
   (c) An n − k + 1 of n.                                                    = (p1 p3 + p2 p4 − p1 p3 p2 p4 )
   (d) Say {1, 2, …, r} is a minimal path set. Then                            (p5 + p6 − p5 p5 )
       φ(1, 1, …, 1, 0, 0, …0) = 1, and so
         . /0 1
               r                                                   13. Taking expectations of the identity
        φD (0, 0, …, 0, 1, 1, …, 1) = 1 − φ(1, 1, …,
            . /0 1                                                     φ(X) = Xi φ(1i , X) + (1 − Xi )φ(0i , X)
                   r
        1, 0, 0, …, 0) = 0, implying that {1, 2, …, r} is a            noting the independence of Xi and φ(1i , X) and of
        cut set. We can easily show it to be minimal.                  φ(0i , X).
        For instance,
         φD (0, 0, …, 0, 1, 1, …, 1)                               15. (a)    7 ≤ r 1 ≤ 1 − 7 3 = 169
             . /0 1                                                          32       2         8      512
                r −1                                                         The exact value is r(1/2) = 7/32, which
           = 1 − φ(1, 1, …, 1, 0, 0, …, 0) = 1,                              agrees with the minimal cut lower bound since
                   . /0 1                                                    the minimal cut sets {1}, {5}, {2, 3, 4} do not
                            r −1
                                                                             overlap.
        since φ(1, 1, …, 1, 0, 0, …, 0) = 0 since
                . /0 1
                        r −1                                       17. E[N 2 ] = E[N 2 |N > 0]P{N > 0}
        {1, 2, …, r − 1} is not a path set.
                                                                               ≥ (E[N|N > 0])2 P{N > 0}
5. (a) Minimal path sets are
                                                                       since E[X 2 ] ≥ (E[X])2 .
         {1, 8}, {1, 7, 9}, {1, 3, 4, 7, 8}, {1, 3, 4, 9},
                                                                       Thus,
         {1, 3, 5, 6, 9}, {1, 3, 5, 6, 7, 8}, {2, 5, 6, 9},
                                                                       E[N 2 ]P{N > 0} ≥ (E[N|N > 0]P{N > 0})2
         {2, 5, 6, 7, 8}, {2, 4, 9}, {2, 4, 7, 8},
                                                                                           = (E[N])2
         {2, 3, 7, 9}, {2, 3, 8}.
                                                                       Let N denote the number of minimal path sets
        Minimal cut sets are
                                                                       having all of its components functioning. Then
         {1, 2}, {2, 3, 7, 8}, {1, 3, 4, 5}, {1, 3, 4, 6},             r(p) = P{N > 0}.

         {1, 3, 7, 9}, {4, 5, 7, 8}, {4, 6, 7, 8}, {8, 9}.             Similarly, if we deﬁne N as the number of minimal
                                                                       cut sets having all of its components failed, then
7. {1, 4, 5}, {3}, {2, 5}.                                             1 − r(p) = P{N > 0}.


                                                              51
52                                                   Answers and Solutions

     In both cases we can compute expressions for E[N]               since IFRA.
     and E[N 2 ] by writing N as the sum of indicator (i.e.,
     Bernoulli) random variables. Then we can use the                Hence,
     inequality to derive bounds on r(p).                            1 − F(x) ≥ (1 − p)x/ξ = e−θx

19. X(i) is the system life of an n − i + 1 of n system          27. If p > p0 , then p = p0 α for some a ∈ (0, 1). Hence,
    each having the life distribution F. Hence, the result
                                                                     r(p) = r(p0 α ) ≥ [r(p0 )]α = p0 α = p
    follows from Example 5e.
                                                                     If p < p0 , then p0 = pα for some a ∈ (0, 1). Hence,
21. (a) (i), (ii), (iv) − (iv) because it is two-of-three.           pα = p0 = r(p0 ) = r(pα ) ≥ [r(p)]α
     (b) (i) because it is series, (ii) because it can be
         thought of as being a series arrangement of 1
                                                                 29. Let X denote the time until the ﬁrst failure and let
         and the parallel system of 2 and 3, which as
                                                                     Y denote the time between the ﬁrst and second fail-
         F2 = F3 is IFR.
                                                                     ure. Hence, the desired result is
     (c) (i) because it is series.
                                                                                     1
                                                                     EX + EY =            + EY
                    2
                    n                                                             μ1 + μ2
23. (a) F̄(t) =         Fi (t)                                       Now,
                  i=1
                                                                                                              μ
                             n                                      E[Y] = E[Y|μ1 component fails ﬁrst] μ +1 μ
                                                                                                           1      2
                   d         ∑  Fj (t)      Fj (t)
                                                                                                                  μ
                      F̄(t) j=1        i=j                                 + E[Y|μ2 component fails ﬁrst] μ +2 μ
          λF (t) = dt      =                                                                                    1    2
                    F̄(t)        n
                                                                                     μ           μ
                                      Fi (t)                                 = μ1 μ +1 μ + μ1 μ +2 μ
                                                                                 2 1    2    1 1    2
                                            i=1
                                      n
                                             
                                     ∑ Fj (t)                    31. Use the remark following Equation (6.3).
                                     j=1
                                 =
                                         Fj (t)                  33. The exact value can be obtained by conditioning
                                     n                               on the ordering of the random variables. Let M
                                 = ∑ λj (t)                          denote the maximum, then with Ai,j,k being the
                                     j=1
                                                                     even that Xi < Xj < Xk , we have that
     (b) Ft (a) = P{additional life of t-year-old > a}
                                                                     E[M] = ∑ E[M|Ai, j, k ]P(Ai, j, k )
                    
                    n
                                                                     where the preceding sum is over all 6 possible per-
                         Fi (t + a)
                                                                     mutations of 1, 2, 3. This can now be evaluated by
                    1
                =                                                    using
                         Fi (t)
         where Fi is the life distribution for component                                     λi          λj
                                                                      P(Ai, j, k ) =
         i. The point being that as the system is series,                              λ i + λj + λk λ j + λ k
         it follows that knowing that it is alive at time t           E[M|Ai, j, k ] =          1       +     1    + 1
         is equivalent to knowing that all components                                     λ i + λj + λk   λ j + λk   λk
         are alive at t.
                                                                 35. (a) It follows
                                                                                  when
                                                                                             i = 1 since 0 = (1 − 1)n
25. For x ≥ ξ,                                                           = 1 − n1 + n2 · · · ± [nn ]. So assume it true for
                                                                         i and consider i + 1. We must show that
     1 − p = 1 − F(ξ) = 1 − F(x(ξ/x)) ≥ [1 − F(x)]ξ/x                                               
                                                                           n−1         n             n              n
     since IFRA.                                                                  =          −             + ···±
                                                                             i       i+1          i+2               n
     Hence,                                                                which, using the induction hypothesis, is
                                                                           equivalent to
     1 − F(x) ≤ (1 − p)x/ξ = e−θx                                                              
                                                                             n−1       n      n−1
     For x ≤ ξ,                                                                    =      −
                                                                              i         i     i−1
     1 − F(x) = 1 − F(ξ(x/ξ)) ≥ [1 − F(ξ)]x/ξ                              which is easily seen to be true.
                                            Answers and Solutions                                        53

(b) It is clearly true when i = n, so assume it for i.              which, using the induction   hypothesis,
    We must show that                                               reduces to
                                                                                      
                                                                      n−1       n      n−1
                                                                      =       −
        n−1      n      n−1          n                                i−2      i−1     i−1
             =       −        + ···±
        i−2     i−1     i−1          n                              which is true.
Chapter 10

1. X(s) + X(t) = 2X(s) + X(t) − X(s).                                  Now, use that

   Now 2X(s) is normal with mean 0 and variance 4s                     P(M|X(t1 ) = y) = 1,                y≥x
   and X(t) − X(s) is normal with mean 0 and variance
   t − s. As X(s) and X(t) − X(s) are independent, it                  and, for y < x
   follows that X(s) + X(t) is normal with mean 0 and                                
                                                                       P M|X(t1 ) = y = P{ max                           X(s) > x − y}
   variance 4s + t − s = 3s + t.                                                                         0<s<t2 −t1
                                                                                               = 2P{X(t2 − t1 ) > x − y}
3. E[X(t1 )X(t2 )X(t3 )]
      = E[E[X(t1 )X(t2 )X(t3 ) | X(t1 ), X(t2 )]]                  11. Let X(t) denote the value of the process at time
                                                                       t = nh. Let Xi = 1 if the ith change results in the
      = E[X(t1 )X(t2 )E[X(t3 ) | X(t1 ), X(t2 )]]                      state value becoming larger,  and let√Xi = 0 other-
                                                                                               √
      = E[X(t1 )X(t2 )X(t2 )]                                          wise. Then, with u = eσ                   h
                                                                                                                     , d = e−σ   h

      = E[E[X(t1 )E[X 2 (t2 ) | X(t1 )]]                                                   n
                                                                       X(t) = X(0)u∑i=1 Xi dn−∑i=1 Xi
                                                                                                             n


      = E[X(t1 )E[X 2 (t2 ) | X(t1 )]]              (∗)                                    u ∑n
                                                                                                        i=1 Xi
      = E[X(t1 ){(t2 − t1 ) + X 2 (t1 )}]                                    = X(0)dn
                                                                                               d
      = E[X 3 (t1 )] + (t2 − t1 )E[X(t1 )]                             Therefore,
      =0                                                                         X(t)                                n
                                                                       log               = n log(d) + ∑ Xi log(u/d)
   where the equality (∗) follows since given X(t1 ),                            X(0)                            i=1
                                                                                                                          t /h
   X(t2 ) is normal with mean X(t1 ) and variance                                           t √      √
   t2 − t1 . Also, E[X 3 (t)] = 0 since X(t) is normal with                              = − σ h + 2σ h ∑ Xi
                                                                                            h           i=1
   mean 0.
                                                                       By the central limit theorem, the preceding
5. P{T1 < T−1 < T2 } = P{hit 1 before − 1 before 2}                    becomes a normal random variable as h → 0. More-
                                                                       over, because the Xi are independent, it is easy to
      = P{hit 1 before −1}
                                                                       see that the process has independent increments.
          × P{hit −1 before 2 | hit 1 before −1}                       Also,
                                                                                     
                                                                                X(t)
        1                                                              E log
      =   P{down 2 before up 1}                                                 X(0)
        2
        11    1                                                               t √         √ t 1       μ√
      =     =                                                             = − σ h + 2σ h         (1 +    h)
        23    6                                                               h              h 2      σ
                                                                          = μt
   The next to last equality follows by looking at the
   Brownian motion when it ﬁrst hits 1.                                and
                                                                                                  
                                                                                        X(t)                   t
7. Let M = {maxt1 ≤s≤t2 X(s) > x}. Condition on X(t1 )                 Var log                         = 4σ 2 h p(1 − p)
   to obtain                                                                            X(0)                   h
            ∞                                                                                         → σ2 t
                                   1
                                       e−y /2t1 dy
                                          2
   P(M) =       P(M|X(t1 ) = y) √                                      where the preceding used that p → 1/2 as h → 0.
             −∞                   2πt1



                                                              54
                                                            Answers and Solutions                                                55

13. If the outcome is i then our total winnings are                            Using the formula for the moment generating func-
                                                                               tion of a normal random variable we see that
                       oi (1 + oi )−1 − ∑ (1 + oj )−1
                                                                               e−c t/2 E[ecB(t) |B(s)]
                                                                                     2
                                           j=i
    xi oi − ∑ xj =
           j=i             1 − ∑ (1 + ok )−1
                                                                                    = e−c t/2 ecB(s)+(t−s)c /2
                                                                                            2                    2
                                   k
                       (1 + oi )(1 + oi )−1 − ∑ (1 + oj )−1
                                                                                    = e−c s/2 ecB(s)
                                                                                            2
                                                     j
                   =
                               1 − ∑ (1 + ok )−1
                                                                                    = Y(s)
                                       k
                   =1                                                          Thus, {Y(t)} is a Martingale.

15. The parameters of this problem are                                         E[Y(t)] = E[Y(0)] = 1

    σ = .05,       σ = 1,    xo = 100,            t = 10.                 21. By the Martingale stopping theorem
    (a) If K = 100 then from Equation (4.4)                                    E[B(T)] = E[B(0)] = 0
                                    √
        b = [.5 − 5 − log(100/100)]/ 10                                        But, B(T) = (x − μT)/σ and so
                 √                                                             E[(x − μT)/σ] = 0
          = −4.5 10 = −1.423
         and                                                                   or
                       √
         c = 100φ( 10 − 1.423) − 100e−.5 φ(−1.423)                             E[T] = x/μ

           = 100φ(1.739) − 100e−.5 [1 − φ(1.423)]                         23. By the Martingale stopping theorem we have
           = 91.2                                                              E[B(T)] = E[B(0)] = 0
         The other parts follow similarly.                                     Since B(T) = [X(T) − μT]/σ this gives the equality

17. E [B(t)|B(u), 0 ≤ u ≤ s]                                                   E[X(T) − μT] = 0
                                                                               or
       = E[B(s) + B(t) − B(s)|B(u), 0 ≤ u ≤ s]
                                                                               E[X(T)] = μE[T]
       = E[B(s)|B(u), 0 ≤ u ≤ s]
                                                                               Now
         + E[B(t) − B(s)|B(u), 0 ≤ u ≤ s]
                                                                               E[X(T)] = pA − (1 − p)B
       = B(s) + E[B(t) − B(s)] by independent
                                                                               where, from part (c) of Problem 22,
          increments
                                                                                            1 − e2μB/σ
                                                                                                         2

                                                                               p=
       = B(s)                                                                            e−2μA/σ − e2μB/σ
                                                                                                2                2


                                                                               Hence,
19. Since knowing the value of Y(t) is equivalent to
                                                                                            A(1 − e2μB/σ ) − B(e−2μA/σ − 1)
                                                                                                             2               2
    knowing B(t) we have
                                                                               E[T] =
                                                                                                    μ(e−2μA/σ − e2μB/σ )
                                                                                                                     2   2
    E[Y(t)|Y(u), 0 ≤ u ≤ s]

       = e−c t/2 E[ecB(t) |B(u), 0 ≤ u ≤ s]
               2
                                                                          25. The means equal 0.
                                                                                    1          1
       = e−c t/2 E[ecB(t) |B(s)]
               2                                                                                               1
                                                                               Var       tdX(t) =     t2 dt =
                                                                                      0            0           3
                                                                                   1            1
    Now, given B(s), the conditional distribution of                                                           1
    B(t) is normal with mean B(s) and variance t − s.                         Var       t2 dX(t) =     t4 dt =
                                                                                     0              0          5
56                                                       Answers and Solutions

                       1                                                 (b) E[Y(t)Y(t + s)]
27. E[X(a2 t)/a] =       E[X(a2 t)] = 0
                       a
                                                                                        ∞
     For s < t,                                                                    =             E[Y(t)Y(t + s) | Y(t) = y]λe−λy dy
                         1                                                             0 ∞
     Cov(Y(s), Y(t)) =     Cov(X(a2 s), X(a2 t))                                   =             yE[Y(t + s) | Y(t) = y]λe−λy dy
                        a2
                                                                                        0
                         1                                                                   ∞
                       = 2 a2 s = s
                        a                                                              +           y(y − s)λe−λy dy
                                                                                             s
     As {Y(t)} is clearly Gaussian, the result follows.
                                                                                        s                     ∞
                                                                                           1
29. {Y(t)} is Gaussian with                                                        =      y λe−λy dy +              y(y − s)λe−λy dy
                                                                                        0  λ                   s

     E[Y(t)] = (t + 1)E(Z[t/(t + 1)]) = 0                                    where the above used that
     and for s ≤ t                                                               E[Y(t)Y(t + s)|Y(t) = y]
                                                                                     ⎧
     Cov(Y(s), Y(t))                                                                 ⎨ yE(Y(t + s)) = y ,             if y < s
                                                                             =                    λ
                                     s                  t                            ⎩ y(y − s),                      if y > s
       = (s + 1)(t + 1) Cov Z           ,     Z
                                    s+1                t+1
                                                                           Hence,
                         s        t                                          Cov(Y(t), Y(t + s))
       = (s + 1)(t + 1)       1−                   (∗)
                        s+1      t+1                                              s               ∞
                                                                                        −y λ                             1
       =s                                                                      =     ye      dy +     y(y − s)λe−λy dy − 2
                                                                                  0                s                    λ
     where (∗) follows since Cov(Z(s), Z(t)) = s(1 − t).
     Hence, {Y(t)} is Brownian motion since it is also               33. Cov(X(t), X(t + s))
     Gaussian and has the same mean and covariance
                                                                            = Cov(Y1 cos wt + Y2 sin wt,
     function (which uniquely determines the distribu-
     tion of a Gaussian process).                                                      Y1 cos w(t + s) + Y2 sin w(t + s))
                                                                            = cos wt cos w(t + s) + sin wt sin w(t + s)
31. (a) Starting at any time t the continuation of the
        Poisson process remains a Poisson process                           = cos(w(t + s) − wt)
        with rate λ.                                                        = cos ws
Chapter 11

                                            i −1             i                                             j −1
1. (a) Let u be a random number. If ∑ Pj < u ≤ ∑ Pj                                                    N − ∑ Ii
                                            j=1             j=1                                               1
                                                                          P{Ij = 1| I1 , …, Ij−1 } =               . Hence, we
          then simulate from Fi .
          *                                             +                                          N + M − (j − 1)
                            i −1                                          can simulate I1 , …, In by generating random num-
            In the above ∑ Pj ≡ 0 when i = 1.                             bers U1 , …, Un and then setting
                             j=1
                                                                              ⎧
                                                                              ⎪                        j −1
                                                                              ⎪
                                                                              ⎪
   (b) Note that                                                              ⎨                    N − ∑ Ii
                                                                          Ij = 1, if U <                 1
                   1         2                                                ⎪
                                                                              ⎪           j
                                                                                                  +    −   (j − 1)
          F(x) =     F1 (X) + F2 (x)                                          ⎪
                                                                              ⎩                N     M
                   3         3                                                  0, otherwise
          where                                                                 n
                                                                          X = ∑ Ij      has the desired distribution.
          F1 (x) = 1 − e−2x ,      0<x<∞                                       j=1


                       x,    0<x<1                                        Another way is to let
          F2 (x) =                                                             ⎧
                       1,    1<x                                               ⎨1, the jth acceptable item is in the sample
                                                                          Xj =
          Hence, using (a), let U1 , U2 , U3 be random                         ⎩0, otherwise
          numbers and set
                                                                          and then simulate X1 , …, XN by generating random
             ⎧                                                            numbers U1 , …, UN and then setting
             ⎨ −log U2
                       ,           if U1 < 1/3                                 ⎧
          X=        2                                                          ⎪                       j −1
             ⎩                                                                 ⎪
                                                                               ⎪
               U3 ,                if U1 > 1/3                                 ⎪
                                                                               ⎨                  N − ∑ Ii
                                                                          Xj = 1, if Uj <              i=1
                                                                               ⎪
                                                                               ⎪              N   +  M − (j − 1)
                                            −log U2                            ⎪
                                                                               ⎪
          The above uses the fact that              is expo-                   ⎩
                                                                                 0, otherwise
                                               2
          nential with rate 2.
                                                                                N
                                                                          X = ∑ Xj       then has the desired distribution.
3. If a random sample of size n is chosen from a set of                        j=1
   N + M items of which N are acceptable then X, the
                                                                          The former method is preferable when n ≤ N and
   number of acceptable items in the sample, is such
                                                                          the latter when N ≤ n.
   that
                                    
                 N     M          N+M                                  7. Use the rejection method with g(x) = 1. Differen-
   P{X = k} =
                 k   n−k             k                                    tiating f (x)/g(x) and equating to 0 gives the two
                                                                          roots 1/2 and 1. As f (.5) = 30/16 > f (1) = 0, we
   To simulate X note that if                                             see that c = 30/16, and so the algorithm is
            1,       if the jth section is acceptable
   Ij =                                                                   Step 1: Generate random numbers U1 and U2 .
            0,       otherwise
                                                                          Step 2: If U2 ≤ 16(U12 − 2U13 + U14 ), set X = U1 .
   then                                                                           Otherwise return to step 1.



                                                                  57
58                                                        Answers and Solutions

13. P{X = i} = P{Y = i|U ≤ PY /CQY }                                      (d) fU(1) , …|U(n) (y1 , …, yn−1 |yn )

                      P{Y = i, U ≤ PY /CQY }                                             f (y1 , …, yn )
                =                                                                   =
                                                                                            fU(n) (yn )
                                K
                      Qi P{U ≤ PY /CQY |Y = i}                                      =      n!
                =                                                                        nyn−1
                                 K
                      Qi Pi /CQi                                                         (n − 1)!
                =                                                                   =             , 0 < y1 < · · · < yn−1 < y
                          K                                                               y n− 1
                      Pi                                                         where the above used that
                =
                      CK                                                         FU(n) (y) = P{max U i ≤ y} = yn
     where K = P{U ≤ PY /CQY }. Since the above is a                             and so
     probability mass function it follows that KC = 1.
                                                                                 FU(n) (y) = nyn−1

15. Use 2μ = X.                                                           (e) Follows from (d) and the fact that if
                                                                              F(y) = yn then F−1 (U) = U 1/n .
17. (a) Generate the X(i) sequentially using that given
        X(1) , …, X(i−1) the conditional distribution of              21. Pm+1 {i1 , …, ik−1 , m + 1}
        X(i) will have failure rate function λi (t) given                                                                  k 1
        by                                                                   =         ∑          Pm {i1 , …, ik−1 , j}
                                                                                                                          m+1k
                                                                                       j≤m
                 ⎧                                                                j=i1 ,…,ik−1
                 ⎪
                 ⎨ 0,                t < X(i−1) ,
        λi (t) =                     X(0) ≡ 0.                                               1  1   1
                                                                             = (m − (k − 1)) m        
                 ⎪
                 ⎩                                                                             m+1 m+1
                   (n − i + 1)λ(t), t > X(i−1)                                               k      k

                                                                      25. See Problem 4.
     (b) This follows since as F is an increasing function
         the density of U(i) is
                                                                      27. First suppose n = 2.

         f(i) (t) =         n!        (F(t))i−1                           Var(λX1 + (1 − λ)X2 ) = λ2 σ12 + (1 − λ)2 σ22 .
                      (i − 1)!(n − i)
                                                                          The derivative of the above is 2λσ12 − 2(1 − λ)σ22 and
                      × (F(t))n−i f (t)                                   equating to 0 yields

                =           n!        ti−1 (1 − t)n−i ,                                σ22                  1/σ12
                      (i − 1)!(n − i)                                     λ=                   =
                                                                                  σ12 + σ2   2
                                                                                                    1/σ12 + 1/σ22
                      0<t<1                                               Now suppose the result is true for n − 1. Then
                                                                                                    
                                                                                   n                          n− 1
         which shows that U(i) is beta.
                                                                           Var     ∑ λi Xi = Var              ∑ λi Xi + Var(λn Xn )
                                   th                                              i=1                        i=1
     (c) Interpret Yi as the i interarrival time of a Pois-                                                                                
         son process. Now given Y1 + · · · + Yn+1 =                                                                          n− 1
         t, the time of the (n + 1)st event, it fol-                                               = (1 − λn )2 Var          ∑ 1 −λiλn Xi
                                                                                                                             i=1
         lows that the ﬁrst n event times are distri-
         buted as the ordered values of n uniform (0, t)                                                +   λ2n Var Xn
         random variables. Hence,
                                                                          Now by the inductive hypothesis for ﬁxed λn the
          Y1 + · · · + Yi                                                 above is minimized when
                           ,        i = 1, …, n
         Y1 + · · · + Yn+i                                                         λi       1/σi2
                                                                          (∗ )          =           ,               i = 1, …, n − 1
                                                                                 1 − λn   n− 1
         will have the same distribution as U(1) , …,                                      ∑ 1/σj 2
         U(n) .                                                                                   j=1
                                                    Answers and Solutions                                                59

    Hence, we now need choose λn so as to minimize                     so we should use the simulated data to determine
                                                                       Dn and then use this as an estimate of E[Dn ].
                        1
    (1 − λn )2                  + λ2n σn2
                 n− 1
                 ∑ 1/σj2                                          33. (a) E[X 2 ] ≤ E[aX] = aE[X]
                 j=1

    Calculus yields that this occurs when                              (b) Var(X) = E[X 2 ] − E2 [X] ≤ aE[X] − E2 [X]
                                                                       (c) From (b) we have that
                        1                   1/σn2
    λn =                              =
                        n−1               n
           1 + σn2      ∑     1/σj2       ∑ 1/σj2                           Var(X) ≤ a2
                                                                                            E[X]
                        j=1               j=1                                                 a
    Substitution into (*) now gives the result.                                      E[X]
                                                                                1−           ≤ a2 max p(1 − p) = a2 /4
                                                                                       a            0<p<1
29. Use Hint.
                                                                                              k
31. Since E[W n |Dn ] = Dn + μ, it follows that to                35. Use the estimator ∑ Ni /k 2 where Ni = number
    estimate E[W n ] we should use Dn + μ. Since                                            i=1
    E[Dn |Wn ] = Wn − μ, the reverse is not true and                   of j = 1, …, k : Xi < Yj .
