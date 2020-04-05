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
