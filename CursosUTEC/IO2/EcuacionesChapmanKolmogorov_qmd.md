---
curso: IO2
titulo: EcuacionesChapmanKolmogorov
slides: 0
fuente: EcuacionesChapmanKolmogorov.qmd
---

---
title: "Ecuaciones de Chapman-Kolmogorov"
author: "Claudia Antonini"
format: 
    revealjs:
      theme: [default, custom.css]
      logo: UTEC-Logo.jpg
      footer: "Investigación de Operaciones II: Modelos Probabilísticos"
      transition: slide
editor: visual
date: "Junio,2023"
---

## Objetivos: Ecuaciones de Chapman-Kolmogorov

-   Demostrar, entender y aplicar las ecuaciones de Chapman-Kolmogorov en su versión matricial como herramienta fundamental para calcular la matriz de transición en n pasos.

## ¿Qué hacemos con estos modelos?

Queremos calcular la distribución marginal de $X_{n}$. Sea

$$
\begin{align*}\alpha_j^{(n)}=&P\left(X_{n}=j\right)\\              =&\sum_{i\in S} P\left(X_{n}=j\Big|X_{0}=i\right)P\left(X_{0}=i\right)\\              =& \sum_{i \in S} P\left(X_{n}=j\Big|X_{0}=i\right) \alpha_{i}\\              =& \sum_{i \in S}P_{ij}^{(n)}\alpha_{i}\end{align*}
$$

## La probabilidad de transición en n pasos

$P_{ij}^{(n)}$ la llamaremos **la probabilidad de transición en** $n$**-pasos** del estado $i$ al estado $j$

$$P_{ij}^{(n)}\equiv P\left(X_{n}=j\Big|X_{0}=i\right) \quad \forall i,j \in S$$

Si sabemos calcular $P_{ij}^{(n)}$, podremos calcular la distribución marginal de $X_n$.

## Ecuaciones de Chapman -- Kolmogorov

La probabilidad de transición de n-pasos satisface las siguientes ecuaciones:

$$P_{ij}^{(n+m)} = \sum_{k\in S}P_{ik}^{(n)} P_{kj}^{(m)} \quad i,j \in S \quad \forall n,m \geq 0$$

conocidas como las **ecuaciones de Chapman-Kolmogorov**.

## Prueba:

$$
\begin{align*}P_{ij}^{(n+m)} &= P\left(X_{n+m}=j\Big|X_{0}=i\right)\\                &=\sum_{k\in S}P\left(X_{n+m}=j, X_n=k\Big|X_o=i\right)\\               &=\sum_{k\in S}P\left(X_{n+m}=j\Big|X_{n}=k,X_{0}=i\right) P\left(X_n=k\Big|X_{0}=i\right)\\                &=\sum_{k\in S}P\left(X_{n+m}=j\Big|X_{n}=k\right) P\left(X_{n}=k\Big|X_{0}=i\right)\\               &=\sum_{k\in S} P_{kj}^{(n+m-n)} P_{ik}^{(n)} = \\               &=\sum_{k\in S} P_{ik}^{(n)} P_{kj}^{(m)}\end{align*}
$$

## Versión Matricial de las Ecuaciones de Chapman-Kolmogorov

Si definimos $\mathbb{P}^{(n)}$ a la matriz de las probabilidades de transición en $n$-pasos $P_{ij}^{(n)}$, entonces las ecuaciones de Chapman-Kolmogorov pueden escribirse en forma matricial como sigue:

$$\mathbb{P}^{(n+m)}=\mathbb{P}^{(n)} \cdot \mathbb{P}^{(m)}$$

## Operativamente, ¿cómo podemos sacarle provecho?

Observe que si consideramos el caso $n=m=1$, entonces:

$$\mathbb{P}^{(2)}=\mathbb{P^{(1)}} \cdot \mathbb{P^{(1)}} = \mathbb{P}\mathbb{P}=\mathbb{P}^2$$

Es decir, $\mathbb{P}^{(2)}=\mathbb{P}^2$.

En otras palabras, para obtener la matriz de transición en dos pasos, basta con elevar al cuadrado la matriz de transición en un paso. Este resultado no es nada intuitivo pero es cierto.

## En general: {.scrollable}

Por esta razón podemos continuar el argumento de la siguiente manera:

$$\mathbb{P}^{(3)}=\mathbb{P}^{(2)}\mathbb{P}^{(1)}=\mathbb{P}^2\mathbb{P}^1=\mathbb{P}^3$$

Asumiento como hipótesis inductiva que

$$\mathbb{P}^{(n-1)}=\mathbb{P}^{n-1}$$

entonces aplicando de nuevo las ecuaciones de Chapman-Kolmogorov vemos que:

$$\mathbb{P}^{(n)}=\mathbb{P}^{(n-1+1)} = \mathbb{P}^{(n-1)} \cdot \mathbb{P} = \mathbb{P}^n$$

Es decir, **la matriz de transición de** $n$**-pasos se puede obtener multiplicando la matriz** $\mathbb{P}$ **por sí misma** $n$ **veces.**

## Corolario:

Ahora, si definimos las distribución incondicional de $X_{n}$ como

$$\alpha^{(n)} = \left(\alpha_j^{(n)}\right) = \left(P(X_{n}=j)\right)$$

entonces

$$\alpha^{(n)} = \alpha^{(0)}\mathbb{P}^{(n)}$$

**Prueba: Ejercicio**

## Ejemplo:

**Sea** $\{X_n,n\geq 0\}$ **una CMTD con conjunto de estados** $S=\{1,2,3,4\}$ **y matriz de transición en 1 paso dada por**

$$
\begin{equation*} \mathbb{P}=\begin{bmatrix}0.1 & 0.2 & 0.3 & 0.4 \\0.2 & 0.2 & 0.3 & 0.3 \\0.5 & 0 & 0.5 & 0 \\0.6 & 0.2 & 0.1 & 0.1 \\\end{bmatrix}\end{equation*}
$$

**y distribución inicial:**

$$\quad \alpha = [0.25, 0.25, 0.25, 0.25]$$

a\) **Calcule** $P\left(X_{3}=4, X_{2}=1, X_{1} = 3, X_{0} = 1\right)$

## 

a\) **Calcule**

$$P\left(X_{3}=4, X_{2}=1, X_{1} = 3, X_{0} = 1\right)$$

Condicionemos:

$$
\begin{align*}&P\left(X_{3}=4\Big|X_{2}=1, X_{1} = 3, X_{0} = 1\right) P\left(X_{2}=1, X_{1} = 3, X_{0} = 1\right)\\ &=P\left(X_{3}=4\Big|X_{2}=1\right)P\left(X_{2}=1\Big|X_{1}=3\right)\cdot\\&\qquad \qquad \cdot P\left(X_{1}=3\Big|X_{0}=1\right)P\left(X_{0}=1\right)\\&=P_{14}P_{31}P_{13} \alpha_1 = (0.4)(0.5)(0.3)(0.25) = 0.015\end{align*}
$$

**¿Se le ocurre una manera más fácil para calcular esto mismo?**

## 

b\) **Calcule** $\alpha^{(4)}$

Usando el Corolario de las ecuaciones de Chapman-Kolmogorov:

$$
\alpha^{(4)} = \alpha^{(0)} P^{4} = [\underbrace{0.34105}_{=P(X_{4} =1)}, \underbrace{0.13540}_{=P(X_{4}=2)}, \underbrace{0.32530}_{=P(X_{4}=3)}, \underbrace{0.19825}_{=P(X_{4}=4)}]
$$

c\) **Calcule** $E[X_{4}]$

$$
\begin{align*}&E[X_{4}]=\\=&1P(X_{4}=1)+2P(X_{4}=2)+3P(X_{4}=3)+4P(X_{4}=4)\\=&1(0.34105)+2(0.13540)+3(0.32530)+4(0.19825)\\=& 2.38075 \end{align*}
$$

```{r echo=TRUE}
1*(0.34105)+2*(0.13540)+3*(0.32530)+4*(0.19825)
```

## Ejemplo:

**Sea** $X_{n}$ **el estado del n-ésimo artículo producido en una fábrica, con** $X_{n}=0$ **siendo el evento "el enésimo artículo fabricado funciona" y** $X_{n}=1$ **siendo el evento "el enésimo artículo fabricado es defectuoso". Supongamos que** $\{X_{n}, n\geq 0\}$ **evoluciona como una cadena de Markov con matriz de transición en un paso dada por:**

$$
\begin{equation*} \mathbb{P}=\begin{bmatrix}0.97 & 0.03 \\0.04 & 0.96\end{bmatrix}\end{equation*}
$$

**y distribución inicial**

$$\alpha_0=P(X_{0}=0)=0.7\\ \alpha_1=P(X_{0}=1)=0.3$$

## 

a\) **Calcular** $\mathbb{P}^{(2)}$

Recuerde que $\mathbb{P}^{(2)}=\mathbb{P}^{2}$,

la matriz de transición en un paso multiplicada por si misma:

$$
\begin{align*} \mathbb{P}^{(2)}=&\mathbb{P}\mathbb{P}\\=&\begin{bmatrix}0.97 & 0.03 \\0.04 & 0.96\end{bmatrix}\cdot \begin{bmatrix}0.97 & 0.03 \\0.04 & 0.96\end{bmatrix}\\=&\begin{bmatrix}0.9421 & 0.0579 \\0.0772 & 0.9228\end{bmatrix}\end{align*}
$$

## 

b\) **Determinar la probabilidad de que el segundo artículo fabricado sea defectuoso dado que el 0-ésimo era defectuoso**

La probabilidad requerida es:

$$P\left(X_{2}=1\Big|X_{0}=1\right)=P_{11}^{(2)}=0.9228$$

Note que la misma corresponde a tomar el elemento en la fila 2, columna 2 (las correspondientes al estado 1) de la matriz resultante de elevar al cuadrado la matriz de transición en un paso.

## 

c\) **Determinar la probabilidad de que el segundo artículo fabricado sea defectuoso dado que el primer artículo era defectuoso.**

$$P\left(X_2=1\Big|X_{1}=1\right)=P\left(X_1=1\Big|X_0=1\right)=P_{11}^{(1)}=0.96$$

## 

d\) **Determinar la probabilidad incondicional de que el segundo artículo fabricado sea defectuoso**

Haciendo uso del Corolario de las ecuaciones de Chapman- Kolmogorov tenemos que:

$$
\begin{align*}&\left(P(X_{2}=0),P(X_{2}=1)\right)\\=&\alpha^{(0)}\mathbb{P}^{(2)}=[0.7 , 0.3] \begin{bmatrix}0.9421 & 0.0579 \\0.0772 & 0.9228\end{bmatrix} \\\\&\Rightarrow P\left(X_{2}=1\right)\\=&(0.7)(0.0579)+0.3(0.9228) = 0.31737\end{align*}
$$

## 

e\) **Determinar la probabilidad de que los dos primeros artículos fabricados funcionen y que el tercer artículo fabricado sea defectuoso**

$$
\begin{align*}&P\left(X_{2}=1, X_{1}=0,X_{0}=0\right)\\ =&P\left(X_{2}=1\Big|X_{1}=0,X_{0}=0\right)P\left(X_{1}=0,X_{0}=0\right)\\=&P\left(X_{2}=1\Big|X_{1}=0\right)P\left(X_{1}=0|X_{0}=0\right)P\left(X_{0}=0\right)\\ =&P\left(X_{1}=1\Big|X_{0}=0\right)P\left(X_{1}=0\Big|X_{0}=0\right)P\left(X_{0}=0\right)\\ &=P_{01}^{(1)}P_{00}^{(1)}\alpha_{0} = (0.03)(0.97)(0.7)=0.02037\end{align*}
$$

## 

f\) **Calcule la probabilidad de que el primer y el tercer artículo fabricado funcionen**.

$$P\left(X_{0}=0,X_{2}=0\right)=P\left(X_{2}=0|X_{0}=0\right)P\left(X_{0}=0\right) = \\ P_{00}^{(2)}\alpha_0 = (0.9421)(0.7)=0.65947$$

## ¿Qué aprendimos hoy?
