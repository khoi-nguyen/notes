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
#) `gradient(2, 4, 5, 13)`

Find the equation of the line passing through

#) `line_equation(1, 2, 2, 4)`
#) `line_equation(3, 9, 1, 5)`
#) `line_equation(1, 4, 4, 1)`
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

# Generalising the gradient

::: {.Recall t="Gradient of straight line"}
$$m = \frac {\Delta y} {\Delta x}$$
:::

::: {.Idea t="Approximation by the tangent" cols=2}
~~~ {.graph b=-1.5 l=-3 r=7 t=4.5}
f, x = '0.2*x^2 + 1', 2.5
plot(f)
showcoordinates(f, x, 'x', 'f(x)')
showtangent(f, x)
~~~

[0.5cm]{.gap}
The **gradient** of a curve at a **point**
will be the **gradient** of its **tangent** at that point.
:::

# Approximating the tangent

::: {.cols n="2"}
~~~ {.graph b=-1 l=-3 r=7 t=5.5}
f, x, h = '0.15*x^2*sin(0.2*x) + 1.2', 1.5, 3.5
plot(f)
showcoordinates(f, x, 'x', 'f(x)')
showcoordinates(f, x + h, 'x + h', 'f(x + h)')
showsecant(f, x, x + h)
~~~
~~~ {.graph b=-1 l=-3 r=7 t=5.5}
f, x, h = '0.15*x^2*sin(0.2*x) + 1.2', 1.5, 2.5
plot(f)
showcoordinates(f, x, 'x', 'f(x)')
showcoordinates(f, x + h, 'x + h', 'f(x + h)')
showsecant(f, x, x + h)
~~~
~~~ {.graph b=-1 l=-3 r=7 t=5.5}
f, x, h = '0.15*x^2*sin(0.2*x) + 1.2', 1.5, 1.5
plot(f)
showcoordinates(f, x, 'x', 'f(x)')
showcoordinates(f, x + h, 'x + h', 'f(x + h)')
showsecant(f, x, x + h)
~~~
~~~ {.graph b=-1 l=-3 r=7 t=5.5}
f, x, h = '0.15*x^2*sin(0.2*x) + 1.2', 1.5, 1
plot(f)
showcoordinates(f, x, 'x', 'f(x)')
showcoordinates(f, x + h, 'x + h', 'f(x + h)')
showsecant(f, x, x + h)
~~~
:::

# Approximating the tangent

::: {.Idea cols="2" t="Approximation by secants"}
~~~ {.graph b=-1 l=-2.5 r=5.5 t=5}
f, x, h = '0.15*x^2*sin(0.2*x) + 1.2', 1.5, 2.5
plot(f)
showcoordinates(f, x, 'x', 'f(x)')
showcoordinates(f, x + h, 'x + h', 'f(x + h)')
showsecant(f, x, x + h)
~~~
~~~ {.graph b=-1 l=-2.5 r=5.5 t=5}
f, x, h = '0.15*x^2*sin(0.2*x) + 1.2', 1.5, 1.5
plot(f)
showcoordinates(f, x, 'x', 'f(x)')
showcoordinates(f, x + h, 'x + h', 'f(x + h)')
showsecant(f, x, x + h)
~~~

We approximate the **tangent** by the **secant**,
whose gradient is
$$\frac {f(x + h) - f(x)} {h}$$

[1.2cm]{.gap}
It gets better as $h$ **tends to $0$**.
:::

# Definition

::: {.cols n=2}
~~~ {.graph b=-1.5 l=-3 r=7 t=4.5}
f, x, h = '0.2*x^2 + 1', 2.5, 1
plot(f)
showcoordinates(f, x, 'x', 'f(x)')
showcoordinates(f, x + h, 'x + h', 'f(x + h)')
showsecant(f, x, x + h)
~~~
$\text{\small{Gradient}} = \frac {f(x + h) - f(x)} {h}$

~~~ {.graph b=-1.5 l=-3 r=7 t=4.5}
f, x = '0.2*x^2 + 1', 2.5
plot(f)
showcoordinates(f, x, 'x', 'f(x)')
showtangent(f, x)
~~~
$\text{\small{Gradient}} = \lim_{h \to 0} \frac {f(x + h) - f(x)} {h}$
:::

::: {.Definition t='Derivative'}
$$\frac {df} {dx} \defeq \lim_{h \to 0} \frac {f(x + h) - f(x)} {h}$$
:::

# Differentiation from first principles

::: Example
Differentiate $x^2$ from first principles.
:::

::: Solution
\begin{align*}
\lim_{h \to 0} \frac {\br{x + h}^2 - x^2} h
&= \lim_{h \to 0} \frac {\cancel{x^2} + 2xh + h^2 - \cancel{x^2}} h\\
&= \lim_{h \to 0} \br{2x + h} = 2x
\end{align*}
:::

# Interpretation

::: {.Example t="Derivative of $x^2$"}
$$f(x) = x^2 \qquad \underbrace{\frac {df} {dx} = 2x}_{\text{gradient}}$$

::: {.cols n=2}

 $x$       $f(x)$    Gradient
--------  --------  ----------
 -1.5      2.25      -3
 0         0         0
 2         4         4

~~~ {.graph b=-1 l=-4 r=4}
f = 'x^2'
plot(f)
showtangent(f, -1.5, 'darkgreen', '-2:-1')
showtangent(f, 0, 'darkred', '-1:1')
showtangent(f, 2, 'darkorange', '1.5:2.5')
~~~
:::
:::

# Differentiation from first principles

::: Example
Differentiate $x$ from first principles.
:::

::: Solution
$\lim_{h \to 0} \frac {(\cancel x + h) - \cancel x} h
= \lim_{h \to 0} \frac h h = 1$
:::

::: {.Remark cols=2 t="Gradient and derivatives"}
~~~ {.graph b=-2 l=-3 r=3 t=3}
plot('x')
~~~

The result coincides with the **gradient** of $x$ as expected.
:::

# Exercises

::: {.Exercise t='Differentiation from first principles'}
Differentiate from first principles

#) `diff('3*x + 5')`
#) `diff('m*x + c')`
#) `diff('k')`
:::

::: Extension
Differentiate from first principles

#) `diff('x^3')`
:::

# Tangent

::: {.Remark cols=2 t="Characteristics of the tangent"}
~~~ {.graph b=-1.5 l=-3 r=5 t=4.5}
f, a = '0.2*x^2 + 1', 2.5
plot(f)
showcoordinates(f, a, 'a', 'f(a)')
showtangent(f, a)
~~~

Gradient
: $\frac {df} {dx} (a)$

Passing through
: $(a, f(a))$
:::

::: {.Formula t="Tangent equation"}
$$y = \frac {df} {dx} (a) (x - a) + f(a)$$
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

::: {.Question cols=2 t="Degrees or radians?"}
~~~ {.graph b=-2 t=2 l=-4 r=4}
plot('sin(pi/180*x)')
plot('cos(pi/180*x)', 'darkgreen')
~~~
~~~ {.graph b=-2 t=2 l=-4 r=4}
plot('sin(x)')
plot('cos(x)', 'darkgreen')
~~~
:::

# Leibniz rule

::: {.Theorem t="Leibniz rule"}
$$\frac d {dx} \br{f(x)g(x)} = \frac {df} {dx}(x) g(x) + f(x) \frac {dg} {dx}(x)$$
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
