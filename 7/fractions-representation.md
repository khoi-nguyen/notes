---
title: Fractions
subtitle: Representing fractions
...

# Fractions

::: {.cols n=4}
`showfrac(7, 13)`
`showfrac(4, 6)`
`showfrac(3, 5)`
`showfrac(5, 7)`
:::

::: {.Hint t='Representing fractions'}
Denominator
: Number of slices per cake

Numerator
: Number of slices you eat
:::

# Numerator and denominator

::: Vocabulary
Numerator
: Number at the top

Denominator
: Number at the bottom
:::

::: {.cols n=3}

\begin{center}
\begin{tikzpicture}
\node (frac) at (0, 0) {\LARGE $\frac {\color{darkgreen} 2} {\color{darkred} 3}$};
\node[darkgreen] (num) at (2, 1) {numerator};
\draw[darkgreen,thick,->] (frac.north east) -- (num.west);
\node[darkred] (den) at (2, -1) {denominator};
\draw[darkred,thick,->] (frac.south east) -- (den.west);
\draw[darkorange, thick] (0, 0) circle (0.7cm);
\node[darkorange] at (1.5, 0) {fraction};
\end{tikzpicture}
\end{center}

`showfrac(2, 3, False)`
`rectfrac(2, 3, 1, 1, 2.5)`
:::

# Equivalent fractions

Despite being cut differently, some cake quantities are the same:

::: {.cols n=4}
`showfrac(3, 6)`
`showfrac(1, 2)`
`showfrac(6, 12)`
`showfrac(12, 24)`
:::

::: Vocabulary
- We call these **equivalent fractions**
- The fraction with the **lowest possible denominator** (largest
  possible slices) is called simplified.
:::

# Equivalent fractions

::: Question
Which fractions are equivalent?

:::: {.cols n=4}
`showfrac(3, 6)`
`showfrac(1, 4)`
`showfrac(4, 6)`
`showfrac(2, 5)`
`showfrac(6, 15)`
`showfrac(3, 12)`
`showfrac(2, 3)`
`showfrac(1, 2)`
::::
:::

# Equivalent fractions

# Adding fractions

::: {.cols n=4}
`showsum(1, 4, 2, 4)`
`showsum(1, 3, 1, 3)`
`showsum(2, 5, 1, 5)`
`showsum(1, 6, 2, 6)`
:::

. . .

::: Method
When adding fractions with the **same denominator**:

- We **add** the **numerators**
- We **keep** the **denominator**
- **Simplify** the result
:::

# Adding fractions with different denominators

::: {.cols n=4}
`showsum(1, 4, 2, 3)`
`showsum(1, 3, 1, 4)`
`showsum(2, 5, 1, 3)`
`showsum(1, 6, 2, 3)`
:::

# Fraction multiplication

::: Example
Represent `mult('1/4', '2/3')`
:::

::: Solution
`rectfrac(2, 3, 1, 1)`
`rectfrac(2, 3, 1, 4)`
:::
