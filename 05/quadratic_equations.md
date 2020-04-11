---
title: Quadratic Equations
#
...

# Starter

::: {.Exercise cols=2}
Expand the brackets for:

#) `expand('(x + 1)*(x + 1)')`
#) `expand('(x - 2)^2')`
#) `expand('(2*x - 3)^2')`

Factorise the following by 3:

#) `factorise('3*x + 3')`
#) `factorise('3*x + 1')`
#) `factorise('3*x - 5')`
:::

::: {.Extension t="Solve the following equations:"}
#) `equation(s.expand('(x + 3)^2'))`
#) `equation(s.expand('(5*x - 1)^2'))`
#) `equation(s.expand('(8*x - 9)^2'))`
:::

# Completing the square

::: Solution
(Proof TODO)
:::

# Completing the square

::: {.Example t="Complete the square"}
$$x^2 + 6x$$
:::

::: Solution
$$x^2 + 6x = \underbrace{(x + 3)^2}_{x^2 + 6x  {\color{darkred} + 9}} {\color{darkred} - 3^2} = (x + 3)^2 - 9$$
:::

# Completing the square

::: {.Example t="Complete the square"}
$$x^2 - 10x$$
:::

::: Solution
$$x^2 - 10x = \underbrace{(x - 5)^2}_{x^2 - 10x {\color{darkred} + 25}} {\color{darkred} - 5^2} = (x - 5)^2 - 25$$
:::

# Completing the square

::: {.Example t="Complete the square"}
$$3x^2 + 3x + 4$$
:::

::: Solution
$3x^2 + 3x + 4 = 3 ({\color{darkred} x^2 + x}) + 4 = 3[{{\color{darkred} \underbrace{{(x + \frac {1} {2})}^2}_{x^2 + x + \frac {1} {4}} - {\frac {1} {2}}^2}}] + 4$
$$= 3{(x + \frac {1} {2})}^2 {\color{darkblue} - 3 (\frac {1} {4}) + 4} = {(x + \frac {1} {2})}^2 {\color{darkblue} + \frac {13} {4}}$$
:::

# Exercises

::: {.Exercise t="Complete the square"}

#) `complete_square('x^2 + 10*x')`
#) `complete_square('x^2 - 8*x')`
#) `complete_square('x^2 + 8*x - 3')`
#) `complete_square('x^2 - 2*x + 10')`
#) `complete_square('x^2 - 5*x + 1')`
#) `complete_square('3*x^2 - 5*x + 1')`
#) `complete_square('a*x^2 + b*x + c')`
:::

# Solving equations

When $x$ appears only **once**, we can **make $x$ the subject**.

::: {.Example t="Complete the square, then solve for x"}
$$x^2 - 8x = 0$$
:::

::: Solution

$x^2 - 8x = {(x - 4)}^2 - 16$

${(x - 4)}^2 - 16 = 0$

${(x - 4)}^2 = 16$

$x - 4 = ± 4$

Hence, $x = 0$ or $x = 8$
:::

# Completing the square

::: {.Exercise t="Complete the square, then solve for $x$"}

#) `equation('x^2 - 2*x + 1')`
#) `equation('x^2 - 5*x + 6')`
#) `equation('x^2 - 4*x - 3')`
#) `equation('2*x^2 + 3*x - 1')`
#) `equation('3*x^2 - 5*x + 2')`
:::

# Role of $a$ in $a \br{x - \alpha}^2 + \beta$

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

# Role of $\alpha$ in $a \br{x - \alpha}^2 + \beta$

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
$$a^2 - b^2 = \br{a + b}\br{a - b}$$
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

# Quadratic Formula

Suppose we are given an equation of the form $ax^2 + bx + c = 0$.

${\color{darkred} ax^2 + bx} + c = 0$

${\color{darkred} a[(x + \frac {b} {2a})^2 - \frac {b^2} {4a^2}]} = -c$

$(x + \frac {b} {2a})^2 {\color{darkblue} - \frac {b^2} {4a^2}} = {\color{darkblue} - \frac {c} {a}}$

$(x + \frac {b} {2a})^2 = {\color{darkblue} \frac {b^2 - 4ac} {4a^2}}$
