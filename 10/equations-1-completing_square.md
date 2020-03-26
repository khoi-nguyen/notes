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
