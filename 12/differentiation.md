---
title: Differentiation
...

# Starter

::: Objective
Understanding the importance of the **gradient**.
:::

::: {.Starter cols=2 t="Gradient and line equations"}
Find the gradient of a line going through

#) `gradient(1, 2, 2, 4)`
#) `gradient(-1, 3, 2, -5)`

Find the equation of the line

#) `line_equation(1, 2, 2, 4)`
#) `line_equation(3, 1, 1)`
:::

# Motivations: minimums and maximums

~~~ {.graph b=-2 t=2 l=-5 r=5}
f = s.Integral('0.12*(x + 2)*(x - 3)').doit()
plot(f)
showtangent(f, -2, 'darkgreen', '-3:-1')
showtangent(f, 3, 'darkgreen', '2:4')
~~~

::: {.Question t="Finding extrema"}
How do you find **maximums** and **minimums**?
:::

::: {.Idea t="Critical points"}
We look at points where the **gradient** is **zero**.
:::

# Motivations: polynomial approximations

::: {.Question t="How does the calculator work?"}
How does the calculator compute $\sin(0.4)$?
:::

::: {.Idea t="Polynomial approximation"}
`'$$\\sin(x) \\approx '
+ taylor_poly('sin(x)', 0, 5)
+ ' \\quad \\sin(0.4) \\approx '
+ s.latex(taylor('sin(x)', 0, 5).subs('x', 0.4))
+ '$$'`
:::

~~~ {.graph b=-2 t=2}
f = 'sin(x)'
plot(f)
showtaylor(f, 0, 5, 'darkgreen', '-4:4')
~~~

# Motivations: Finding $x$-intercepts

~~~ {.graph b=-2 t=2 l=-5 r=5}
f = '0.15*(x - 2.2)*(x + 3)'
plot(f)
showtangent(f, 2)
~~~

::: {.Question t="Finding $x$-intercepts"}
How to estimate the $x$-intercept?
:::

::: {.Idea t="Newton-Raphson"}
- The $x$-intercept is close to $2$
- We **approximate by a line** around $2$
- We find the **$x$-intercept** of the **line**.
:::

# Einstein's opinion today's topic

::: {.Quote t="Einstein about Newton"}
In order to put his system into mathematical form at all,
Newton had to devise the concept of **differential quotients**
and propound the **laws of motion** in the form of total differential equations
--perhaps the **greatest advance in thought**
that a single individual was ever privileged to make.
:::

::: {.Formula t="Newton's 2nd law of motion"}
$$F = m {\color{darkred} \frac {d^2x} {dt^2}}$$
:::

# Definition

::: {.cols n=2}
~~~ {.graph b=-1.5 l=-3 r=7 t=4.5}
f, a, x = '0.2*x^2 + 1', 2.5, 3.5
plot(f)
showcoordinates(f, a, 'a', 'f(a)')
showcoordinates(f, x, 'x', 'f(x)')
showsecant(f, a, x)
~~~
$\text{Gradient} = \frac {f(x) - f(a)} {x - a}$

~~~ {.graph b=-1.5 l=-3 r=7 t=4.5}
f, a = '0.2*x^2 + 1', 2.5
plot(f)
showcoordinates(f, a, 'a', 'f(a)')
showtangent(f, a)
~~~
$\text{Gradient} = \lim_{x \to a} \frac {f(x) - f(a)} {x - a}$
:::

::: {.Definition t='Derivative'}
$$f'(a) \defeq \lim_{x \to a} \frac {f(x) - f(a)} {x - a}$$
:::

# Differentiation from first principles

::: Example
Differentiate $x^2$ from first principles at $a$.
:::

::: Solution
$\lim_{x \to a} \frac {x^2 - a^2} {x - a}
= \lim_{x \to a} \frac {\cancel{(x - a)} (x + a)} {\cancel{x - a}}
= 2a$
:::

# Differentiation from first principles

::: Example
Differentiate $x$ from first principles at $a$.
:::

::: Solution
$\lim_{x \to a} \frac {x - a} {x - a}
= \lim_{x \to a} \frac {\cancel{(x - a)}} {\cancel{x - a}}
= 1$
:::

~~~ {.graph b=-3 l=-3 r=3 t=3}
plot('x')
~~~

# Exercises

::: {.Exercise t='Differentiation from first principles'}
Differentiate from first principles at $a$

#) `diff('3*x + 5')`
#) `diff('m*x + c')`
#) `diff('k')`
:::

::: Extension
Differentiate from first principles

#) `diff('x^3')`
:::

# Tangent

~~~ {.graph b=-1.5 l=-3 r=7 t=4.5}
f, a = '0.2*x^2 + 1', 2.5
plot(f)
showcoordinates(f, a, 'a', 'f(a)')
showtangent(f, a)
~~~

Gradient
: $f'(a)$

Point
: $(a, f(a))$

::: {.Formula t="Tangent equation"}
$$y = f'(a) (x - a) + f(a)$$
:::

# Differentiation rules

::: {.Theorem t="Differentiation of usual functions" cols=2}
#) `diff('k')`
#) `diff('x^n')`
#) `diff('sin(x)')`
#) `diff('cos(x)')`
#) `diff('tan(x)')`
:::

::: {.Exercise cols=2 t="Differentiate"}
#) `diff('3*x + 2')`
#) `diff('4*x^3 + 2*x^2')`
#) `diff('2*cos(x) + 2')`
#) `diff('-sin(x) + x^2')`
:::

# Radians and degrees

::: {.Warning t="Radians and degrees"}
$$\frac d {dx} \sin x = \cos x,\quad \frac d {dx} \cos x = -\sin x,\quad \frac d {dx} \tan x = 1 + \tan^2 x$$
are **only** valid in **radians**.
:::

::: {.Question t="Degrees or radians?"}

::: {.cols n=2}
~~~ {.graph b=-2 t=2 l=-4 r=4}
plot('sin(pi/180*x)')
plot('cos(pi/180*x)', 'darkgreen')
~~~
~~~ {.graph b=-2 t=2 l=-4 r=4}
plot('sin(x)')
plot('cos(x)', 'darkgreen')
~~~
:::
:::

# Leibniz rule

::: {.Theorem t="Leibniz rule"}
$$(fg)'(x) = f'(x)g(x) + f(x) g'(x)$$
:::

::: Exercise
#) `diff('x^2*sin(x)')`
#) `diff('sin(x)*cos(x)')`
#) `diff('cos(x)^2')`
#) `diff('sin(x)^2')`
:::

# Chain rule

Derivatives generalize **gradients**.

::: {.Example t="Behaviour of gradients under composition"}
\begin{align*}
\begin{array}{l}
y = \overbrace{m_1}^{\frac {dy} {dt}} t\\
t = \underbrace{m_2}_{\frac {dt} {dx}} x
\end{array}
\implies y = \overbrace{\underbrace{m_1 m_2}_{\frac {dy} {dt} \frac {dt}
{dx}}}^{\frac {dy} {dx}} x
\implies \frac {dy} {dx} = \frac {dy} {dt} \frac {dt} {dx}
\end{align*}
:::

::: {.Formula t="Chain Rule"}
$$\frac {dy} {dx} = \frac {dy} {dt} \frac {dt} {dx}$$
:::

# Chain Rule: example

::: {.Example t='Chain Rule'}
Differentiate `diff('sin(x^2)')`
:::

::: Solution
Let $y = \sin t$ and $t = x^2$.

$$\frac {dy} {dx} = \frac {dy} {dt} \frac {dt} {dx}
= (\cos t) (2x) = 2x \cos(x^2)$$
:::
