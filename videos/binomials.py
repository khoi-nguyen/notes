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
        arrows, lengths = [], []
        arrows_data = [
            # Top edge
            (UP + LEFT, a*RIGHT, UP, 'a'),
            (UP + RIGHT, b*LEFT, UP, 'b'),
            # Right edge
            (UP + RIGHT, a*DOWN, RIGHT, 'a'),
            (DOWN + RIGHT, b*UP, RIGHT, 'b'),
            # Bottom edge
            (DOWN + LEFT, a*RIGHT, DOWN, 'a'),
            (DOWN + RIGHT, b*LEFT, DOWN, 'b'),
            # Left edge
            (UP + LEFT, a*DOWN, LEFT, 'a'),
            (DOWN + LEFT, b*UP, LEFT, 'b'),
        ]
        for (corner, vector, shift, tex) in arrows_data:
            arrow = DoubleArrow(
                big_square.get_corner(corner),
                big_square.get_corner(corner) + vector,
                color = GRAY, stroke_width = 1, tip_length = 0.1,
            ).shift(0.2*shift)
            arrows.append(arrow)
            lengths.append(TexMobject(tex, color=GRAY).next_to(arrow, 0.1*shift))
        self.play(
            *[FadeIn(arrow) for arrow in arrows],
            *[Write(length) for length in lengths],
        )
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
        for i in range(0, len(terms)):
            char = '=' if i == 0 else '+'
            link = TexMobject(char).scale(1.5).next_to(previous, RIGHT)
            self.play(
                Write(link),
                Transform(areas[i], terms[i].next_to(link, RIGHT))
            )
            previous = areas[i]
        self.wait(5)
