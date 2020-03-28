---
title: Indices
...

# Starter

::: Starter
Evaluate the following:

#) `simplify('3^2')`
#) `simplify('5^2')`
#) `simplify('2^3')`
#) `simplify('7^1')`
#) `simplify('3^3')`
#) `simplify('12^2')`
#) `simplify('4^3')`
#) `simplify('1^4')`
:::

::: {.Extension show=1}
#) Write 64 as a power of 4
#) Write 243 as a power of 3
#) Write out $2^4 \times 2^3$ as a product of 2's, then rewrite it as a single index
:::

# Index

::: Definition
Index
: A number (called the base) that is raised to a power (called the exponent)
:::

\begin{center}
\begin{tikzpicture}
\node (origin) at (0, 0) {\LARGE ${\color{darkblue} x}^{\color{darkred} a}$};
\node[darkblue] (base) at (-1, -1) {base};
\draw[darkblue,thick,->] (base) -- (origin.south west);
\node[darkred] (exponent) at (1, 1) {exponent};
\draw[darkred,thick,->] (exponent) -- (origin.north east);
\draw[darkorange,thick] (0, 0) circle (0.7cm);
\node[darkorange] (index) at (2, 0) {index};
\draw[darkorange,thick,->] (0.8, 0) -- (index.west);
\end{tikzpicture}
\end{center}

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
#) `mult('a^2', 'a^6', a=10)`
#) `mult('a^4', 'a^-2', a=6)`
#) `mult('a^-3', 'a^-9', a=5)`
#) `mult('a', 'a^3', a=9)`
:::

::: {.Extension show=1}
Evaluate the following:

#) `mult('a^4', 'a^-4', a=10)`
#) $7^0$ [1]{.answer}
#) $x^0$ [1]{.answer}
:::
