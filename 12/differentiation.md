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

#) `diff('3*x + 5', 'x')`
#) `diff('m*x + c', 'x')`
#) `diff('k', 'x')`
:::

::: Extension
Differentiate from first principles

#) `diff('x^3', 'x')`
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
