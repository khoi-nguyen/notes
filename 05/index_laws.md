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
#) Write 243 as a power of 3
#) Write out $2^4 \times 2^3$ as a product of 2's, then rewrite it as a single index
:::

# Index

::: Definition
Index
: A number (called the base) that is raised to a power (called the index)
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
For each example: which number is the base? Which is the exponent? [1cm]{.gap}

#) $4^7$ [1cm]{.gap}

#) $10^4$ [1cm]{.gap}
:::


# Multiplying Indices

::: Example
Simplify $2^4 \times 2^3$
:::

::: Solution
$$2^4 \times 2^3 = \overbrace{\underbrace{2 \times 2 \times 2 \times 2}_{2^4} \times \underbrace{2 \times 2 \times 2}_{2^3}}^{\text{2 appears 7 times}} = 2^7$$
:::

# Multiplying Indices

::: Exercise
Simplify the following:

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

::: Exercise
Simplify the following indices:

#) `mult('a^4', 'a^7', a=3)`
#) `mult('a^2', 'a^6', a=2)`
#) `mult('a^5', 'a^3', a=6)`
#) `mult('x^3', 'x^2')`
#) `mult('y^4', 'y^8')`
#) `mult('a', 'a^4', a=9)`
#) `mult('z^k', 'z^2')`
#) `mult('a^20', 'a^27', a=32)`
:::

::: {.Extension show=1}
Evaluate the following:

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

::: Exercise
Simplify the following:

#) `frac('a^7', 'a^2', a=3)`
#) `frac('a^6', 'a^4', a=7)`
#) `div('a^12', 'a^9', a=2)`
#) `div('x^8', 'x^3')`
#) `frac('y^10', 'y^2')`
#) `div('z^a', 'z^7')`
#) `div('a^20', 'a^19', a=13)`
#) `frac('x^45', 'x^27')`
:::

::: {.Extension show=1}
Simplify the following:

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

::: Exercise
Simplify the following:

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

::: Exercise
Simplify the following:

#) `power('a^3', 2, a=4)`
#) `power('a^5', 3, a=10)`
#) `power('x^7', 4)`
#) `power('a^8', 6, a=9)`
#) `power('y^2', 20)`
#) `power('z^3', 'x')`
#) `power('a^10', 10, a=10)`
#) `power('a^y', 'b')`
:::

::: {.Extension show=1}
Simplify the following:

#) `power('a^-2', 4, a=5)`
#) `power('a^3', -80, a=49)`
#) `power('x^-y', '-z')`
:::

# Simplifying indices

::: Example
Simplify $3 \times 5x^3$
:::

::: Solution
$$3 \times 5x^3 = {\color{red} 3 \times 5} \times x^3 = {\color{red} 15}x^3$$
:::

::: Example
Simplify $2x^3 \times 4y$
:::

::: Solution
$$2x^3 \times 4y = 2 \times {\color{orange} x^3 \times 4} \times y = 2 \times {\color{orange} 4 \times x^3} \times y = 8x^3y$$
:::

# Simplifying indices

::: Example
Simplify $2x^2 \times 5x^4$
:::

::: Solution
$$2x^2 \times 5x^4 = 2 \times {\color{orange} x^2 \times 5} \times x^4 = 2 \times {\color{orange} 5 \times x^2} \times x^4 = 10x^6$$
:::

::: Example
Simplify $6a^9 \times 5a^9$
:::

::: Solution
$$6a^9 \times 7x^9 = 6 \times {\color{orange} a^9 \times 7} \times a^9 = 6 \times {\color{orange} 7 \times a^9} \times a^9 = 42x^{18}$$
:::

# Simplifying indices

::: Exercise
Simplify the following:

#) `mult('2', '4*a^3')`
#) `mult('6*x', '5*y^2')`
#) `mult('4*b^3', '3*b^2')`
#) `mult('3*y^4', '7*y^2')`
#) `mult('8*m^6', '2*n^4')`
#) `mult('-9*x^10', '4*x^8')`
#) `mult('x^9', '14*x')`
#) `mult('16*c', '-4*c^10')`
:::

::: {.Extension show=1}
Simplify the following:

#) `mult('-4*s^-3', '-6*t^-4')`
#) `mult('4*z^27', '1/4*z^-26')`
#) `mult('-13*a^6', '4*b^-5', '1/8*a^-12')`
:::

# Simplifying indices

::: Example
Simplify $\frac {8x^5} {2x^2}$
:::

::: Solution
$$\frac {8x^5} {2x^2} = \frac {{\color{orange} 8} \times {\color{blue} x^5}} {{\color{orange} 2} \times {\color{blue} x^2}} = {\color{orange} 4}{\color{blue} x^3}$$
:::

# Simplifying indices

::: Example
Simplify $12x^7 \div 3x^3$
:::

::: Solution
$$12x^7 \div 3x^3 = \frac {12x^7} {3x^3} = \frac {{\color{orange} 12} \times {\color{blue} x^7}} {{\color{orange} 3} \times {\color{blue} x^3}} = {\color{orange} 4}{\color{blue} x^4}$$
:::

# Simplifying indices

::: Example
Simplify $\frac {2x^6} {8x^4}$
:::

::: Solution
$$\frac {2x^6} {8x^4} = \frac {{\color{orange} 2} \times {\color{blue} x^6}} {{\color{orange} 8} \times {\color{blue} x^4}} = {\color{orange} {\frac 1 4}}{\color{blue} x^2}$$
:::
