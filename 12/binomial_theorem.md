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

# Induction

::: Question
How do you find the value of $\binom 5 3$?
:::

If we **separate** the last character, a $5$-string with 3 $a$ is

- a $4$-string with 2 $a$ followed by $a$: $\binom 4 2$
- a $4$-string with 3 $a$ followed by $b$: $\binom 4 3$

Therefore, $\binom 5 3 = \binom 4 2 + \binom 4 3$.

# Pascal's property

::: Question
How do you find the value of $\binom n k$?
:::

If we **separate** the last character, an $n$-string with k $a$ is

- a $(n - 1)$-string with $k - 1$ $a$ followed by $a$: $\binom {n - 1}
  {k - 1}$
- a $(n - 1)$-string with $k$ $a$ followed by $b$: $\binom {n - 1} k$

::: {.Formula t="Pascal's property"}
$$\binom n k = \binom {n - 1} {k - 1} + \binom {n - 1} k$$
:::

# Normal

::: Exercise
#) `normal(-1, oo, 0, 1)`
#) `bin(2, 5, 10, 0.25)`
#) `poisson(2, 5, 2, 1)`
:::
