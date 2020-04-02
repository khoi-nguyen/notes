---
title: Differentiation
...

# Starter

::: Starter
#) Calculate `integrate('sin(x)', 0, pi)`
#) Differentiate `diff('exp(x^2 + y^2)', 'x', 2, 'y')`
#) Find the tangent of `tangent('x^x', 2)`
:::

::: {.Hint show=1 t='Find the tangent'}
$$y = f'(a) (x - a) + f(a)$$
:::

# Definition

::: {.cols n=2}
~~~ {.graph b=-1.5 l=-3 r=7 t=4.5}
f, a, x = '0.2*x^2 + 1', 2.5, 3.5
plot(f)
showsecant(f, a, x)
showcoordinates(f, a, 'a', 'f(a)')
showcoordinates(f, x, 'x', 'f(x)')
~~~
$\text{Gradient} = \frac {f(x) - f(a)} {x - a}$

~~~ {.graph b=-1.5 l=-3 r=7 t=4.5}
f, a = '0.2*x^2 + 1', 2.5
plot(f)
showtangent(f, a)
showcoordinates(f, a, 'a', 'f(a)')
~~~
$\text{Gradient} = \lim_{x \to a} \frac {f(x) - f(a)} {x - a}$
:::

::: {.Definition t='Derivative'}
$$f'(a) \defeq \lim_{x \to a} \frac {f(x) - f(a)} {x - a}$$
:::
