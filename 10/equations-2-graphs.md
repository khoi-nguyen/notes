---
title: Quadratic equations
subtitle: Graphing quadratic equations
...

# Completing the square

::: Exercise
Complete the square `complete_square('2*x^2 - 3*x + 1')`
:::

::: Remark
Every quadratic equation can be written under the form
$$a \br{x - \alpha}^2 + \beta$$
:::

# Role of $a$ in $a \br{x - \alpha}^2 + \beta$

$$a(x + 2)^2 - 1$$

~~~ graph
plot('1/2*(x + 2)^2 - 1', 'black')
plot('1/4*(x + 2)^2 - 1', 'darkred')
plot('1/7*(x + 2)^2 - 1', 'darkgreen')
plot('1/20*(x + 2)^2 - 1', 'darkblue')
plot('-1/9*(x + 2)^2 - 1', 'darkorange')
plot('-1/5*(x + 2)^2 - 1', 'gray')
~~~

# Role of $a$ in $a \br{x - \alpha}^2 + \beta$

::: Question
What happens if $a$ changes?
:::

Differences
: - Curvature (straight/curved)
- Convexity (upward, downward)

Similarities
: - Turning point
- Line of symmetry

# Role of $\alpha$ in $a \br{x - \alpha}^2 + \beta$

$$\frac 1 2 \br{x - \alpha}^2 - 4$$

~~~ graph
plot('1/2*(x - 2)^2 - 4', 'black')
plot('1/2*(x - 1)^2 - 4', 'darkred')
plot('1/2*(x + 0)^2 - 4', 'darkgreen')
plot('1/2*(x + 1)^2 - 4', 'darkblue')
plot('1/2*(x + 2)^2 - 4', 'darkorange')
plot('1/2*(x + 3)^2 - 4', 'gray')
~~~

# Role of $a$ in $a \br{x - \alpha}^2 + \beta$

::: Question
What happens if $\alpha$ changes?
:::

Differences
: - $x$-coordinate of turning point
- Line of symmetry

Similarities
: - Curvature
- Convexity

# Role of $\beta$ in $a \br{x - \alpha}^2 + \beta$

$$\frac 1 2 \br{x + 2}^2 + \beta$$

~~~ graph
plot('1/2*(x + 2)^2 - 4', 'black')
plot('1/2*(x + 2)^2 - 3', 'darkred')
plot('1/2*(x + 2)^2 - 2', 'darkgreen')
plot('1/2*(x + 2)^2 - 2', 'darkblue')
plot('1/2*(x + 2)^2 + 0', 'darkorange')
plot('1/2*(x + 2)^2 + 1', 'gray')
~~~

# Role of $\beta$ in $a \br{x - \alpha}^2 + \beta$

::: Question
What happens if $\beta$ changes?
:::

Differences
: - $y$-coordinate of turning point

Similarities:
: - Line of symmetry
- Curvature
- Convexity

# Summary
