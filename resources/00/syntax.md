---
title: Syntax
...

# Metadata

At the beginning of each file, you will find

    ---
    title: Put your slideshow title here
    ...

# Slides

A slide starts with a **title**:

::: {.Code t="Slide title"}
    # I am a title
:::

::: {.Warning t="Blank lines"}
Make sure that there is a blank line **before** and **after** your slide title.
:::

# Syntax

::: Code
    This is the *first* paragraph.
    This is **very important**.

    In the *second* paragraph,
    I could put a link to
    [Google](https://google.com).
:::

::: Result
This is the *first* paragraph.
This is **very important**.

In the *second* paragraph,
I could put a link to
[Google](https://google.com).
:::

# Lists

::: {.Code t="Lists"}
    - First
    - Second

    #) First
    #) Second
:::

::: {.Result t="Lists"}
- First
- Second

#) First
#) Second
:::

# Maths

Inline formulas are between *dollars*,
bigger formulas between *double dollars*.

::: {.Code t="LaTeX"}
    $x^2$, $\frac {x + 2} {x^2 - 1}$,
    $$\int_a^b f'(x) dx$$
:::

::: {.Result t="LaTeX"}
$x^2$, $\frac {x + 2} {x^2 - 1}$,
$$\int_a^b f'(x) dx$$
:::

# Python

Text between backticks will be **executed as Python code**.

::: {.Code t="Python code"}
    34 times 47 is `34*47`.
:::

::: {.Result t="Python"}
34 times 47 is `34*47`.
:::

# Algebra

::: {.Code t="Algebra"}
    #) `equation('3*x + 2 = 5')`
    #) `equation(Expand('2*(x - 1)*(x + 2)'))`
    #) `complete_square('x^2 + 3*x + 2')`
:::

::: {.Result t="Algebra"}
#) `equation('3*x + 2 = 5')`
#) `equation(Expand('2*(x - 1)*(x + 2)'))`
#) `complete_square('x^2 + 3*x + 2')`
:::
