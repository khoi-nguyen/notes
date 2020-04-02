---
title: The Binomial Theorem
...

# Starter

::: {.Starter t="Binomial Expansion"}
#) Expand `expand('(a + b)^2')`
#) Expand `expand('(a + b)^3')`
#) Expand `expand('(a + b)^4')`
:::

# Another look at $(a + b)^n$

$$(a + b)^3 = (a + b) (a + b) (a + b) = aaa + aab + aba + \dots$$

::: Hint
Possible terms
: $a^3$, $a^2 b$, $a b^2$, $b^3$

**Count** how many times these terms can appear.
:::

::: Solution
:::: {.cols n=2}
$a^3$
: aaa

$a^2 b$
: aa**b**, a**b**a, **b**aa

$a b^2$
: **a**bb, b**a**b, bb**a**

$b^3$
: bbb
::::
$$(a + b)^3 = \mathbf 1 a^3 + \mathbf 3 a^2 b + \mathbf 3 a b^2 + \mathbf 1 b^3$$
:::

# Binomial coefficient

::: Formula
\begin{align*}
(a + b)^7 &= \dots + \Box a^5 b^2 + \dots\\
\Box &= \text{number of permutations of } aaaaabb
\end{align*}
:::

::: {.Definition t="Binomial coefficient"}
$$\binom n k = \text{number of permutations of }
\overbrace{\underbrace{a \dots a}_k \underbrace{b \dots b}_{n - k}}^k$$
:::

# Binomial coefficients

::: Exercise
Expand $(a + b)^4$ in terms of binomial coefficients
:::

::: Exercise
Find the value of the following binomial coefficients

::: {.cols n=2}
#) `binom(1, 1)`
#) `binom(2, 0)`
#) `binom(3, 2)`
#) `binom(7, 1)`
#) `binom(6, 5)`
#) `binom('n', 1)`
:::
:::
