---
title: Indices
...

# Starter

::: {.Starter cols=2}
Expand the following:

#) `expindex(3, 4)`
#) `expindex(10, 3)`
#) `expindex(2, 5)`
#) `expindex(9, 4)`

Evaluate the following:

5) `simplify('3^2')`
#) `simplify('5^2')`
#) `simplify('2^3')`
#) `simplify('7^1')`
:::

::: {.Extension show=1}
#) Write 64 as a power of 4
   `answer(f'4^{{{int(log(64)/log(4))}}}')`
#) Write 243 as a power of 3
   `answer(f'3^{{{int(log(243)/log(3))}}}')`
#) Write out $2^4 \times 2^3$ as a product of 2's,
    then rewrite it as a single index
   `answer('2^7')`
:::

# Index

::: Definition
Index number
: The power of a number (called the base)
:::

\begin{center}
\begin{tikzpicture}
\node (origin) at (0, 0) {\LARGE ${\color{darkblue} x}^{\color{darkred} a}$};
\node[darkblue] (base) at (-1, -1) {base};
\draw[darkblue,thick,->] (base) -- (origin.south west);
\node[darkred] (exponent) at (1, 1) {index/exponent/power};
\draw[darkred,thick,->] (exponent) -- (origin.north east);
\end{tikzpicture}
\end{center}

# Index

::: Example
For each example: which number is the base? Which is the exponent?
[0.5cm]{.gap}

#) $4^7$ [1cm]{.gap}
#) $10^4$ [1cm]{.gap}
:::

# Indices

::: {.Exercise t="Complete the table"}
 Power    $2^k$                      $3^k$                      $10^k$
-------  -------------------------  -------------------------  ------------------
 3        `answer(2**3)`             `answer(3**3)`             `answer(10**3)`
 2        `answer(2**2)`             `answer(3**2)`             `answer(10**2)`
 1        `answer(2**1)`             `answer(3**1)`             `answer(10**1)`
 r        `answer(2**0)`             `answer(3**0)`             `answer(10**0)`
 -1       `answer(latex('2^-1'))`    `answer(latex('3^-1'))`    `answer(latex('10^-1'))`
 -2       `answer(latex('2^-2'))`    `answer(latex('3^-2'))`    `answer(latex('10^-2'))`
 -3       `answer(latex('2^-3'))`    `answer(latex('3^-3'))`    `answer(latex('10^-3'))`
:::

# Multiplying Indices

::: Example
Simplify $2^4 \times 2^3$
:::

::: Solution
$${\color{darkred} 2^4} \times {\color{darkblue} 2^3} = \overbrace{{\color{darkred} 2 \times 2 \times 2 \times 2} \times {\color{darkblue} 2 \times 2 \times 2}}^{\text{2 appears 7 times}} = 2^7$$
:::

# Multiplying Indices

::: {.Exercise t="Simplify the following:"}
#) `mult('a^2', 'a^3', a=4)`
#) `mult('a^4', 'a^2', a=10)`
#) `mult('a^5', 'a^3', a=6)`
#) `mult('x^2', 'x^4')`
#) `mult('y^5', 'y^4')`
#) `mult('x', 'x^3')`
:::

::: Question
How could we spot the answer without writing the product out?
:::

::: {.Formula t="First Law of Indices"}
$$x^a \times x^b = x^{a + b}$$
:::

# Multiplying Indices

::: {.Exercise t="Simplify the following indices:"}
#) `mult('a^4', 'a^7', a=3)`
#) `mult('a^2', 'a^6', a=2)`
#) `mult('a^5', 'a^3', a=6)`
#) `mult('x^3', 'x^2')`
#) `mult('y^4', 'y^8')`
#) `mult('a', 'a^4', a=9)`
#) `mult('z^k', 'z^2')`
#) `mult('a^20', 'a^27', a=32)`
:::

::: {.Extension show=1 t="Evaluate the following:"}

#) `mult('a^5', 'a^-3', a=6)`
#) `mult('x^-2', 'x^7', l='x^{-2} \\times x^7')`
#) `mult('a^13', 'a^-8', a=5)`
:::

# Dividing indices

::: Example
Simplify $2^5 \div 2^3$
:::

::: Solution
\begin{align*}
2^5 \div 2^3
= \frac {2^5} {2^3}
= \frac {2 \times 2 \times \cancel 2 \times \cancel 2 \times \cancel 2}
{\cancel 2 \times \cancel 2 \times \cancel 2}
= 2^2
\end{align*}
:::

# Dividing indices

::: {.Exercise cols=2 t="Simplify the following"}

#) `frac('a^5', 'a^2', a=4)`
#) `frac('a^6', 'a^3', a=6)`
#) `div('x^9', 'x^4')`
#) `frac('y^6', 'y^2')`
#) `div('x^4', 'x^3')`
:::

::: Question
How could we spot the answer without writing the product out?
:::

::: {.Formula t="Second Law of Indices"}
$$x^a \div x^b = \frac {x^a} {x^b} = x^{a - b}$$
:::

# Dividing indices

::: {.Exercise t="Simplify the following:"}
#) `frac('a^7', 'a^2', a=3)`
#) `frac('a^6', 'a^4', a=7)`
#) `div('a^12', 'a^9', a=2)`
#) `div('x^8', 'x^3')`
#) `frac('y^10', 'y^2')`
#) `div('z^a', 'z^7')`
#) `div('a^20', 'a^19', a=13)`
#) `frac('x^45', 'x^27')`
:::

::: {.Extension show=1 t="Simplify the following:"}
#) `div('a^4', 'a^-2', a=7)`
#) `div('y^2', 'y^-5', l='y^2 \\div y^{-5}')`
#) `div('a^14', 'a^14', a=23)`
:::

# Powers of indices

::: Example
Simplify `power('a^3', 4, a=2)`
:::

::: Solution
$$\br{2^3}^4 = 2^3 \times 2^3 \times 2^3 \times 2^3 = 2^{12}$$
:::

# Powers of indices

::: {.Exercise t="Simplify the following:"}
#) `power('a^2', '2', a=3)`
#) `power('a^4', '3', a=5)`
#) `power('a^3', '3', a=7)`
#) `power('a^10', '2', a=5)`
#) `power('x^5', '4')`
#) `power('y^10', '7')`
:::

::: Question
How could we spot the answer without writing the product out?
:::

::: {.Formula t="Third Law of Indices"}
$$(x^a)^b = x^{ab}$$
:::

# Powers of Indices

::: {.Exercise t="Simplify the following:"}
#) `power('a^3', 2, a=4)`
#) `power('a^5', 3, a=10)`
#) `power('x^7', 4)`
#) `power('a^8', 6, a=9)`
#) `power('y^2', 20)`
#) `power('z^3', 'x')`
#) `power('a^10', 10, a=10)`
#) `power('a^y', 'b')`
:::

::: {.Extension show=1 t="Simplify the following:"}
#) `power('a^-2', 4, a=5)`
#) `power('a^3', -80, a=49)`
#) `power('x^-y', '-z')`
:::

# Simplifying indices

::: Example
Simplify $3 \times 5x^3$
:::

::: Solution
$$3 \times 5x^3 = {\color{darkred} 3 \times 5} \times x^3 = {\color{darkred} 15}x^3$$
:::

::: Example
Simplify $2x^3 \times 4y$
:::

::: Solution
$$2x^3 \times 4y = 2 \times {\color{darkred} x^3 \times 4} \times y = 2 \times {\color{darkred} 4 \times x^3} \times y = 8x^3y$$
:::

# Simplifying indices

::: Example
Simplify $2x^2 \times 5x^4$
:::

::: Solution
$$2x^2 \times 5x^4 = 2 \times {\color{darkred} x^2 \times 5} \times x^4 = 2 \times {\color{darkred} 5 \times x^2} \times x^4 = 10x^6$$
:::

::: Example
Simplify $6a^9 \times 5a^9$
:::

::: Solution
$$6a^9 \times 7x^9 = 6 \times {\color{darkred} a^9 \times 7} \times a^9 = 6 \times {\color{darkred} 7 \times a^9} \times a^9 = 42x^{18}$$
:::

# Simplifying indices

::: {.Exercise t="Simplify the following:"}
#) `mult('2', '4*a^3')`
#) `mult('6*x', '5*y^2')`
#) `mult('4*b^3', '3*b^2')`
#) `mult('3*y^4', '7*y^2')`
#) `mult('8*m^6', '2*n^4')`
#) `mult('-9*x^10', '4*x^8')`
#) `mult('x^9', '14*x')`
#) `mult('16*c^k', '-4*c^10')`
:::

::: {.Extension show=1 t="Simplify the following:"}
#) `mult('-4*s^-3', '-6*t^-4')`
#) `mult('4*z^27', '1/4*z^-26')`
#) `mult('-13*a^6', '4*b^-5', '1/8*a^-12')`
:::

# Simplifying indices

::: Example
Simplify $\frac {8x^5} {2x^2}$
:::

::: Solution
$$\frac {8x^5} {2x^2} = \frac {{\color{darkred} 8} \times {\color{darkblue} x^5}} {{\color{darkred} 2} \times {\color{darkblue} x^2}} = {\color{darkred} 4}{\color{darkblue} x^3}$$
:::

# Simplifying indices

::: Example
Simplify $15x^7 \div 3x^3$
:::

::: Solution
$$15x^7 \div 3x^3 = \frac {15x^7} {3x^3} = \frac {{\color{darkred} 15} \times {\color{darkblue} x^7}} {{\color{darkred} 3} \times {\color{darkblue} x^3}} = {\color{darkred} 5}{\color{darkblue} x^4}$$
:::

# Simplifying indices

::: Example
Simplify $\frac {2x^6} {8x^4}$
:::

::: Solution
$$\frac {2x^6} {8x^4} = \frac {{\color{darkred} 2} \times {\color{darkblue} x^6}} {{\color{darkred} 8} \times {\color{darkblue} x^4}} = {\color{darkred} {\frac 1 4}}{\color{darkblue} x^2}$$
:::

# Simplifying indices

::: Exercise
#) `frac('6*a^5', '2*a^2')`
#) `frac('14*a^10', '7*a^4')`
#) `div('2*a^12', '6*a^9')`
#) `div('3*x^4', 'x^3')`
#) `frac('8*y^7', '8*y^5')`
#) `div('5*z^8', '-10*z^7')`
#) `div('54*a^20', '-9*a^19')`
#) `frac('-17*x^y', '-51*x^7')`
:::

::: {.Extension show=1 t="Simplify the following:" cols=2}
#) `div('90*m^-4', '18*m^5')`
#) `div('13/2*a^-5', '6.5*a^-(10/2)')`
:::

# Simplifying indices

::: Example
Simplify $\br{2x^2}^3$
:::

::: Solution
$$\br{2x^2}^3 = {\color{darkred} 2^3} \times {\color{darkblue} \br{x^2}^3} = {\color{darkred} 8}{\color{darkblue} x^6}$$
:::

::: Example
Simplify $\br{2x^2y}^3$
:::

::: Solution
$$\br{2x^2y}^3 = {\color{darkred} 2^3} \times {\color{darkblue} \br{x^2}^3} \times y^3 = {\color{darkred} 8}{\color{darkblue} x^6}y^3$$
:::

# Simplifying indices

::: {.Exercise title="Simplify the following:"}
#) `power('3*a', 2)`
#) `power('5*c^2', 2)`
#) `power('2*x*y', 3)`
#) `power('6*x*y^-2', 2)`
#) `power('m^10*n^12', 4)`
#) `power('-3*x^5*x^4', 3)`
#) `power('2*m^-10*n^-12', 4)`
#) `power('-5*p^-8*q^-13', -3)`
:::

::: {.Extension show=1 t="Simplify the following:"}
#) `power('-2*a^4*b^-m*c^3', -5)`
#) `power('3/4*x^-a*y^-b*z^-(2*c)', -3)`
:::
