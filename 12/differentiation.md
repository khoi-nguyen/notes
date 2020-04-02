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

~~~ {.graph b=-2 l=-3 r=7}
f = '0.2*x^2 + 1'
plot(f)
showtangent(f, 2)
~~~

::: {.Definition t='Derivative'}
$$f'(a) = \lim_{x \to a} \frac {f(x) - f(a)} {x - a}$$
:::
