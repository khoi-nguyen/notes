---
title: Standard Form
...

# Starter

::: Exercise
Match the equivalent operations
:::

# Standard form

::: {.Definition t="Standard Form"}
A number that can be written as a decimal multiplied by a power of 10
:::

\begin{center}
\begin{tikzpicture}
\node (number) at (0, 0) {\LARGE \color{darkblue} $x$};
\node (numberconditions) at (0, -1.2) {\color{darkblue} $1 \leq x < 10$};
\draw[darkblue,thick,->] (numberconditions.north) -- (number.south);
\node[right=0.1cm of number.east] (power) {\Large $\times {\color{darkred} 10^a}$};
\node (powertext) at (3.5, 0) {\color{darkred} Power of 10};
\draw[darkred,thick,->] (powertext.west) -- (power.east);
\end{tikzpicture}
\end{center}

# Standard form

::: {.Example t="Are the following numbers in standard form?"}
#) $6 \times 10^3$ [1cm]{.gap}
#) $12 \times 10^{-6}$ [1cm]{.gap}
#) $3 \times 8^5$ [1cm]{.gap}
:::

# Mini-Whiteboard Activity

::: {.Example t="Are these numbers in Standard Form? Why?"}
#) $5 \times 10^2$ [1cm]{.gap}
#) $8 \times 10^9$ [1cm]{.gap}
#) $10 \times 10^6$ [1cm]{.gap}
#) $1.8 \times 10^2$ [1cm]{.gap}
#) $0.49 \times 10^{-20}$ [1cm]{.gap}
#) $4.75 \div 10^{-17}$ [1cm]{.gap}
:::

# Standard form

::: {.Example t="What does $5 \times 10^3$ represent?"}
$$5 \times {\color{darkred} 10^3} = 5 \times {\color{darkred} 1000} = 5000$$
:::

::: {.Solution t="Quicker method"}
$$5 \times 10^{\color{darkred} 3} = 5{{\color{darkred} 000}}$$
The power tells us how many NUMBERS come after the 5
:::

# Standard form

::: {.Example t="What does $4.3 \times 10^2$ represent?"}
$$4.3 \times {\color{darkred} 10^2} = 4.3 \times {\color{darkred} 100} = 430$$
:::

::: {.Solution t="Quicker way"}
$$4.3 \times 10^{\color{darkred} 2} = 4{{\color{darkred} 30}}$$
The power tells us how many NUMBERS come after the 4
:::

# Standard form

::: {.Exercise t="Convert the following into ordinary numbers"}
#) `mult(4, '10^2')`
#) `mult(9, '10^2')`
#) `mult(2, '10^4')`
#) `mult('1.5', '10^3')`
#) `mult('2.8', '10^4')`
#) `mult(3, '10^7')`
#) `mult('6.1', '10^6')`
#) `mult('9.75', '10^8')`
:::

::: {.Extension t="Convert the following into ordinary numbers"}
#) `mult('6.74', '10^5')`
#) `mult('8.045', '10^3')`
#) `mult('1.00001', '10^4')`
:::

# Standard form

::: {.Example t="Convert 200 into standard form"}
$$2{\color{darkred} 00} = 2 \times {\color{darkred} 100} = 2 \times {\color{darkred} 10^2}$$
:::

::: {.Solution t="Quicker method"}
$$2{\color{darkred} 00} = 2 \times 10^{\color{darkred} 2}$$
The amount of numbers after the 2 tells us the power of 10
:::

# Standard form

::: {.Example t="Convert 5100 into standard form"}
$$5{\color{darkred} 100} = 5.1 \times {\color{darkred} 1000} = 5.1 \times {\color{darkred} 10^3}$$
:::

::: {.Solution t="Quicker method"}
$$5{\color{darkred} 100} = 5.1 \times 10^{\color{darkred} 3}$$
The amount of numbers after the 5 tells us the
:::

# Standard form

::: {.Exercise t="Convert the following into ordinary numbers"}
#) `mult(4, '10^2')`
#) `mult(9, '10^2')`
#) `mult(2, '10^4')`
#) `mult('1.5', '10^3')`
#) `mult('2.8', '10^4')`
#) `mult(3, '10^7')`
#) `mult('6.1', '10^6')`
#) `mult('9.75', '10^8')`
:::

::: {.Extension t="Convert the following into ordinary numbers"}
#) `mult('6.74', '10^5')`
#) `mult('8.045', '10^3')`
#) `stf(300)`
:::
