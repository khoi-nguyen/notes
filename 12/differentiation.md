---
title: Differentiation
...

# Starter

::: {.Starter cols=2}
Find the gradient of a line going through

#) `gradient(1, 2, 2, 4)`
#) `gradient(-1, 3, 2, -5)`

Find the equation of the line

#) `line_equation(1, 2, 2, 4)`
#) `line_equation(3, 1, 1)`
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
The formulae
$$\sin' = \cos,\quad \cos' = -\sin,\quad \tan' = 1 + \tan^2$$
are only valid in **radians**.
:::

::: {.Question t="Degrees or radians?"}

Which graph is in degrees/radians?

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
