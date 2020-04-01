---
title: Quadratic Equations
subtitle: Completing the square
...

# Starter

::: Objective
Completing the square
:::

#) Solve `equation('2*x - 5 = 4')`
#) Solve `equation('4*x - 5 = 2*x + 7')`
#) Solve `equation('x^2 + 3 = 12')`
#) Solve `equation('2*x^2 + 3 = 53')`
#) Solve `equation('3*x^2 - 4 = -4')`
#) Factorise `factorise('(x - 2)*(x + 3)')`

# Difficulty of quadratic equations

::: Question
*Which* question is harder and *why*?

- Solve `equation('x^2 - 9 = 16')`
- Solve `equation('x^2 - 5*x = -6')`
:::

::: Solution
The second one is *harder* because $x$ appears twice.

It makes it harder to *change the subject*.
:::

# Completing the square

::: Recall
$$a^2 - b^2 = (a - b)(a + b)$$
:::

::: Exercise
Expand $\br{x + \frac b 2}^2 - \br{\frac {b} 2}^2$
:::

::: Solution
$$\br{x + \frac b 2}^2 - \br{\frac b 2}^2 = x (x + b) = x^2 + bx$$
:::

::: Remark
Count how many $x$ are on either sides
:::

# Completing the square

::: Recall
$$x^2 + bx = \br{x + \frac b 2}^2 - \br{\frac b 2}^2$$
:::

::: Example
$$x^2 + 6x = \br{x + 3}^2 - 9$$
:::

::: Example
Make $x$ only appear once in `complete_square('x^2 - 5*x + 6')`
:::

# Exercises

::: Exercise
#) `complete_square('x^2 + 10*x')`
#) `complete_square('x^2 - 8*x')`
#) `complete_square('x^2 + 8*x - 3')`
#) `complete_square('x^2 - 2*x + 10')`
#) `complete_square('x^2 - 5*x + 1')`
#) `complete_square('3*x^2 - 5*x + 1')`
#) `complete_square('a*x^2 + b*x + c')`
:::

# Solving equations

Now that $x$ appears only **once**, we can **change the subject**.

::: Exercise
#) `equation('x^2 - 2*x + 1')`
#) `equation('x^2 - 5*x + 6')`
#) `equation('x^2 - 4*x - 3')`
#) `equation('2*x^2 + 3*x - 1')`
#) `equation('3*x^2 - 5*x + 2')`
:::

# Completing the square

::: Exercise
Complete the square `complete_square('2*x^2 - 3*x + 1')`
:::

::: Remark
Every quadratic equation can be written in the form
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

# Graphing $x^2$

~~~ {.graph b=-1 t=9}
plot('x^2')
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

Similarities
: - Line of symmetry
- Curvature
- Convexity

# Summary