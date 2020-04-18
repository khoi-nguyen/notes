from manimlib.imports import *
from base import *

class APlusBSquared(Scene):
    def construct(self):
        a, b, opacity = 3.25, 1.75, 0.5

        # Draw square
        big_square = Square(
            side_length = a + b,
            fill_opacity = opacity,
            fill_color = GREEN,
        ).to_edge(DOWN).shift(0.5*UP)
        self.play(FadeIn(big_square))
        self.wait()

        # Display Lengths
        lengths = [
            (UP, LEFT, 'a', a), (UP, RIGHT, 'b', b),
            (RIGHT, UP, 'a', a), (RIGHT, DOWN, 'b', b),
            (BOTTOM, LEFT, 'a', a), (BOTTOM, RIGHT, 'b', b),
            (LEFT, UP, 'a', a), (LEFT, DOWN, 'b', b),
        ]
        self.play(*[FadeIn(big_square.length(*l)) for l in lengths])
        self.wait()

        # Total area
        a_plus_b_squared = TexMobject('(a + b)^2').scale(2).move_to(big_square.get_center())
        self.play(Write(a_plus_b_squared))
        self.wait()

        # Left-hand side
        lhs = TexMobject('(a + b)^2', color=GREEN).scale(1.5).to_edge(UP).shift(3.5*LEFT)
        self.play(Transform(a_plus_b_squared, lhs))

        # Decomposition
        squares, areas, terms = [], [], []
        squares_data = [
            (UP, LEFT, a, a, BLUE, 'a^2'),
            (DOWN, LEFT, a, b, GRAY, 'ab'),
            (UP, RIGHT, b, a, GRAY, 'ab'),
            (DOWN, RIGHT, b, b, RED, 'b^2'),
        ]
        for (vert, hor, width, height, color, text) in squares_data:
            square = Rectangle(
                width = width, height = height,
                fill_opacity = opacity,
                fill_color = color,
            ).move_to(big_square.get_corner(vert + hor) - height/2*vert - width/2*hor)
            squares.append(square)
            areas.append(TexMobject(text).scale(2).move_to(square.get_center()))
            terms.append(TexMobject(text, color=color).scale(1.5))
        self.play(
            ApplyMethod(big_square.set_fill, WHITE),
            *[FadeIn(s) for s in squares],
            *[Write(t) for t in areas],
        )

        # Display right-hand side
        previous = a_plus_b_squared
        groups = {'a^2': [], 'ab': [], 'b^2': []}
        for i in range(0, len(terms)):
            char = '=' if i == 0 else '+'
            link = TexMobject(char).scale(1.5).next_to(previous, RIGHT)
            groups[squares_data[i][5]] += [link, areas[i]]
            self.play(
                Write(link),
                Transform(areas[i], terms[i].next_to(link, RIGHT))
            )
            previous = areas[i]
        self.wait()

        # Collect like terms
        two_ab = TexMobject('+', '2ab').scale(1.5).next_to(VGroup(*groups['a^2']), RIGHT)
        two_ab.set_color_by_tex_to_color_map({'2': GRAY})
        b_squared = VGroup(*groups['b^2']).copy().next_to(two_ab, RIGHT)
        self.play(
            Transform(VGroup(*groups['ab']), two_ab),
            Transform(VGroup(*groups['b^2']), b_squared),
        )
        self.wait(5)
