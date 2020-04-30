---
title: Index Laws
publish: true
...

# Starter

::: {.Starter t="Replace ... by < , > or = . Explain your choice"}

#) $2$ ... $2 \times 2$
#) $5 \times 5$ ... $5 \times 5$
#) $4 \times 4 \times 4 \times 4$ ... $4 \times 4 \times 4$
#) $7 \times 7 \times 7 \times 7 \times 7$ ... $7 \times 7 \times 7 \times 7$
#) $1 \times 1 \times 1 \times 1 \times 1$ ... $1 \times 1 \times 1 \times 1 \times 1 \times 1 \times 1 \times 1$
:::

::: Extension
#) Work out $2^4 \times 2^2$ and `simplify('2^3*2^3')`
#) Work out $3 \times 3^4$ and `simplify('3^2*3^3')`
#) Work out $10^2 \times 10^5$ and `simplify('10^4*10^3')`
:::

# Index

::: Definition
Index number
: The power of a number (called the base)
:::

~~~ picture
text('index', '\\LARGE ${\\color{darkblue} x}^{\\color{darkred} a}$', 0, 0)
text('base', 'base', -1, -1, 'darkblue')
text('exponent', 'index/exponent/power', 1, 1, 'darkred')
arrow('base', 'index.south west', 'darkblue, thick')
arrow('exponent', 'index.north east', 'darkred, thick')
~~~

# Index

::: Example
For each example: which number is the base? Which is the exponent?
[0.5cm]{.gap}

#) $4^7$ [1cm]{.gap}
#) $10^4$ [1cm]{.gap}
:::

# Indices

::: Exercise

Complete the table by evaluating, keeping your answers as a fraction where necessary.[1cm]{.gap}

 Power $k$    $2^k$                      $3^k$                      $10^k$                       $x^k$
----------  -------------------------  -------------------------  -------------------------   --------------
 3          `answer(2**3)`             `answer(3**3)`             `answer(10**3)`             `answer(latex('x^3'))`
 2          `answer(2**2)`             `answer(3**2)`             `answer(10**2)`             `answer(latex('x^2'))`
 1          `answer(2**1)`             `answer(3**1)`             `answer(10**1)`             `answer(latex('x^1'))`
 ?          `answer(2**0)`             `answer(3**0)`             `answer(10**0)`             `answer(latex('x^0'))`
 -1         `answer(latex('2^-1'))`    `answer(latex('3^-1'))`    `answer(latex('10^-1'))`    `answer(latex('x^-1'))`
 -2         `answer(latex('2^-2'))`    `answer(latex('3^-2'))`    `answer(latex('10^-2'))`    `answer(latex('x^-2'))`
 -3         `answer(latex('2^-3'))`    `answer(latex('3^-3'))`    `answer(latex('10^-3'))`    `answer(latex('x^-3'))`

:::

# Negative indices

::: {.Formula t="Negative Power rule"}
$$x^{-a} = \frac {1} {x^a}$$
:::

::: {.Formula t="Power of 0"}
$$x^0 = 1$$
:::

# Multiplying Indices

::: Example
Simplify $2^4 \times 2^3$
:::

::: Solution
$${\color{darkred} 2^4} \times {\color{darkblue} 2^3} = \overbrace{{\color{darkred} 2 \times 2 \times 2 \times 2} \times {\color{darkblue} 2 \times 2 \times 2}}^{\text{2 appears 7 times}} = 2^7$$
:::

# Multiplying Indices

::: {.Exercise t="Simplify the following:"}
#) `mult('4^2', '4^3')`
#) `mult('10^4', '10^2')`
#) `mult('6^5', '6^3')`
#) `mult('m^2', 'm^4')`
#) `mult('n^5', 'n^4')`
#) `mult('p', 'p^3')`
#) `mult('y^4', 'y^b')`
#) `mult('x^a', 'x^b')`
:::

::: Question
How could we spot the answer without writing the product out?
:::

::: {.Formula t="First Law of Indices"}
$$x^a \times x^b = x^{a + b}$$
:::

# Multiplying Indices

::: {.Exercise t="Simplify the following indices:"}
#) `mult('3^4', '3^7')`
#) `mult('2^2', '2^6')`
#) `mult('6^5', '6^3')`
#) `mult('x^3', 'x^2')`
#) `mult('y^4', 'y^8')`
#) `mult('9', '9^4')`
#) `mult('z^k', 'z^2')`
#) `mult('32^20', '32^27')`
:::

::: {.Extension show=1 t="Evaluate the following:"}

#) `mult('6^5', '6^-3')`
#) `mult('x^-2', 'x^7')`
#) `mult('5^13', '5^-8')`
:::

# Dividing indices

::: Example
Simplify $2^5 \div 2^3$
:::

::: Solution
\begin{align*}
2^5 \div 2^3
= \frac {2^5} {2^3}
= \frac {2 \times 2 \times \cancel 2 \times \cancel 2 \times \cancel 2}
{\cancel 2 \times \cancel 2 \times \cancel 2}
= 2^2
\end{align*}
:::

# Dividing indices

::: {.Exercise cols=2 t="Simplify the following"}

#) `frac('4^5', '4^2')`
#) `frac('6^6', '6^3')`
#) `div('2^9', '2^4')`
#) `frac('m^6', 'm^2')`
#) `div('n^4', 'n^3')`
#) `div('y^k', 'y^3')`
#) `div('x^a', 'x^b')`
:::

::: Question
How could we spot the answer without writing the product out?
:::

::: {.Formula t="Second Law of Indices"}
$$x^a \div x^b = \frac {x^a} {x^b} = x^{a - b}$$
:::

# Dividing indices

::: {.Exercise t="Simplify the following:"}
#) `frac('3^7', '3^2')`
#) `frac('7^6', '7^4')`
#) `div('2^12', '2^9')`
#) `div('x^8', 'x^3')`
#) `frac('y^10', 'y^2')`
#) `div('z^a', 'z^7')`
#) `div('13^20', '13^19')`
#) `frac('x^45', 'x^27')`
:::

::: {.Extension show=1 t="Simplify the following:"}
#) `div('7^4', '7^-2')`
#) `div('y^2', 'y^-5')`
#) `div('23^14', '23^14')`
:::

# Powers of indices

::: Example
Simplify $\br{2^3}^4$
:::

::: Solution
$$\br{2^3}^4 = 2^3 \times 2^3 \times 2^3 \times 2^3 = 2^{12}$$
:::

# Powers of indices

::: {.Exercise t="Simplify the following:"}
#) `power('3^2', '2')`
#) `power('5^4', '3')`
#) `power('7^3', '3')`
#) `power('5^10', '2')`
#) `power('m^5', '4')`
#) `power('n^10', '7')`
#) `power('y^k', '5')`
#) `power('x^a', 'b')`
:::

::: Question
How could we spot the answer without writing the product out?
:::

::: {.Formula t="Third Law of Indices"}
$$(x^a)^b = x^{ab}$$
:::

# Powers of Indices

::: {.Exercise t="Simplify the following:"}
#) `power('4^3', 2)`
#) `power('10^5', 3)`
#) `power('x^7', 4)`
#) `power('9^8', 6)`
#) `power('y^2', 20)`
#) `power('z^3', 'x')`
#) `power('10^10', 10)`
#) `power('a^y', 'b')`
:::

::: {.Extension show=1 t="Simplify the following:"}
#) `power('5^-2', 4)`
#) `power('49^3', -80)`
#) `power('x^-y', '-z')`
:::

# Simplifying indices

::: Example
Simplify $3 \times 5x^3$
:::

::: Solution
$$3 \times 5x^3 = {\color{darkred} 3 \times 5} \times x^3 = {\color{darkred} 15}x^3$$
:::

::: Example
Simplify $2x^3 \times 4y$
:::

::: Solution
$2x^3 \times 4y = 2 \times {\color{darkred} x^3 \times 4} \times y = 2 \times {\color{darkred} 4 \times x^3} \times y = 8x^3y$
:::

# Simplifying indices

::: Example
Simplify $2x^2 \times 5x^4$
:::

::: Solution
$2x^2 \times 5x^4 = 2 \times {\color{darkred} x^2 \times 5} \times x^4 = 2 \times {\color{darkred} 5 \times x^2} \times x^4 = 10x^6$
:::

::: Example
Simplify $6a^9 \times 5a^9$
:::

::: Solution
$6a^9 \times 7x^9 = 6 \times {\color{darkred} a^9 \times 7} \times a^9 = 6 \times {\color{darkred} 7 \times a^9} \times a^9 = 42x^{18}$
:::

# Simplifying indices

::: {.Exercise t="Simplify the following:"}
#) `mult('2', '4*a^3')`
#) `mult('6*x', '5*y^2')`
#) `mult('4*b^3', '3*b^2')`
#) `mult('3*y^4', '7*y^2')`
#) `mult('8*m^6', '2*n^4')`
#) `mult('-9*x^10', '4*x^8')`
#) `mult('x^9', '14*x')`
#) `mult('16*c^k', '-4*c^10')`
:::

::: {.Extension show=1 t="Simplify the following:"}
#) `mult('-4*s^-3', '-6*t^-4')`
#) `mult('4*z^27', '1/4*z^-26')`
#) `mult('-13*a^6', '4*b^-5', '1/8*a^-12')`
:::

# Simplifying indices

::: Example
Simplify $\frac {8x^5} {2x^2}$
:::

::: Solution
$$\frac {8x^5} {2x^2} = \frac {{\color{darkred} 8} \times {\color{darkblue} x^5}} {{\color{darkred} 2} \times {\color{darkblue} x^2}} = {\color{darkred} 4}{\color{darkblue} x^3}$$
:::

# Simplifying indices

::: Example
Simplify $15x^7 \div \br{3x^3}$
:::

::: Solution
$$15x^7 \div \br{3x^3} = \frac {15x^7} {3x^3} = \frac {{\color{darkred} 15} \times {\color{darkblue} x^7}} {{\color{darkred} 3} \times {\color{darkblue} x^3}} = {\color{darkred} 5}{\color{darkblue} x^4}$$
:::

# Simplifying indices

::: Example
Simplify $\frac {2x^6} {8x^4}$
:::

::: Solution
$$\frac {2x^6} {8x^4} = \frac {{\color{darkred} 2} \times {\color{darkblue} x^6}} {{\color{darkred} 8} \times {\color{darkblue} x^4}} = {\color{darkred} {\frac 1 4}}{\color{darkblue} x^2}$$
:::

# Simplifying indices

::: Exercise
#) `frac('6*a^5', '2*a^2')`
#) `frac('14*a^10', '7*a^4')`
#) `div('2*a^12', '6*a^9')`
#) `div('3*x^4', 'x^3')`
#) `frac('8*y^7', '8*y^5')`
#) `div('5*z^8', '-10*z^7')`
#) `div('54*a^20', '-9*a^19')`
#) `frac('-17*x^y', '-51*x^7')`
:::

::: {.Extension show=1 t="Simplify the following:" cols=2}
#) `div('90*m^-4', '18*m^5')`
#) `div('13/2*a^-5', '6.5*a^-(10/2)')`
:::

# Simplifying indices

::: Example
Simplify $\br{2x^2}^3$
:::

::: Solution
$$\br{2x^2}^3 = {\color{darkred} 2^3} \times {\color{darkblue} \br{x^2}^3} = {\color{darkred} 8}{\color{darkblue} x^6}$$
:::

::: Example
Simplify $\br{2x^2y}^3$
:::

::: Solution
$$\br{2x^2y}^3 = {\color{darkred} 2^3} \times {\color{darkblue} \br{x^2}^3} \times y^3 = {\color{darkred} 8}{\color{darkblue} x^6}y^3$$
:::

# Simplifying indices

::: {.Exercise title="Simplify the following:"}
#) `power('3*a', 2)`
#) `power('5*c^2', 2)`
#) `power('2*x*y', 3)`
#) `power('6*x*y^-2', 2)`
#) `power('m^10*n^12', 4)`
#) `power('-3*x^5*x^4', 3)`
#) `power('2*m^-10*n^-12', 4)`
#) `power('-5*p^-8*q^-13', -3)`
:::

::: {.Extension show=1 t="Simplify the following:"}
#) `power('-2*a^4*b^-m*c^3', -5)`
#) `power('3/4*x^-a*y^-b*z^-(2*c)', -3)`
:::
