from manimlib.imports import *
from videos.base import *

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
        a_plus_b_squared = big_square.write('(a + b)^2')
        self.play(Write(a_plus_b_squared))
        self.wait()

        # Left-hand side
        lhs = TexMobject('(a + b)^2', color=GREEN).scale(1.5).to_edge(UP).shift(3.5*LEFT)
        self.play(Transform(a_plus_b_squared, lhs))

        # Decomposition
        squares, areas, terms = [], [], []
        squares_data = [
            (UL, a, a, BLUE, 'a^2'),
            (DL, a, b, GRAY, 'ab'),
            (UR, b, a, GRAY, 'ab'),
            (DR, b, b, RED, 'b^2'),
        ]
        for (corner, width, height, color, text) in squares_data:
            square = Rectangle(
                width = width, height = height,
                fill_opacity = opacity,
                fill_color = color,
            ).move_to(big_square.get_corner(corner), corner)
            squares.append(square)
            areas.append(square.write(text))
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
            groups[squares_data[i][4]] += [link, areas[i]]
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

class ASquaredMinusBSquared(Scene):

    def construct(self):
        a, b, opacity = 5, 1.75, 0.5

        # Big square
        big_square = Square(
            side_length = a,
            fill_opacity = opacity,
            fill_color = BLUE,
        ).to_edge(DOWN).shift(0.5*UP)
        a_squared = big_square.write('a^2')
        self.play(
            FadeIn(big_square),
            Write(a_squared)
        )
        self.wait()

        # Small square
        small_square = Square(
            side_length = b,
            fill_opacity = 1,
            fill_color = RED,
        ).move_to(big_square.get_corner(DR), DR)
        b_squared = small_square.write('b^2')
        self.play(
            FadeIn(small_square),
            Write(b_squared)
        )
        self.wait()

        # Preparing LHS
        lhs1 = TexMobject('a^2', color=BLUE).scale(1.5).to_edge(UP).shift(3*LEFT)
        lhs2 = TexMobject('-b^2', color=RED).scale(1.5).next_to(lhs1, RIGHT)
        self.play(
            Transform(a_squared, lhs1),
            Transform(b_squared, lhs2),
        )

        # Lengths
        lengths = [
            (DOWN, RIGHT, 'b', b),
            (LEFT, UP, 'a', a), (UP, LEFT, 'a', a),
            (RIGHT, UP, 'a-b', a-b), (RIGHT, DOWN, 'b', b),
        ]
        lengths_objs = [big_square.length(*l) for l in lengths]
        self.play(*[FadeIn(o) for o in lengths_objs])
        self.wait()

        # Square difference
        shape = Polygon(
            big_square.get_corner(UL),
            big_square.get_corner(UR),
            small_square.get_corner(UR),
            small_square.get_corner(UL),
            small_square.get_corner(DL),
            big_square.get_corner(DL),
            color = BLACK,
            fill_color = GREEN,
            fill_opacity = opacity,
        )
        b_label = lengths_objs[-1]
        aminusb = lengths_objs[-2]
        self.play(
            FadeOut(VGroup(big_square, small_square)),
            FadeIn(shape),
            ApplyMethod(b_label.shift, b*LEFT),
            FadeOut(lengths_objs[0]),
            FadeOut(lengths_objs[1]),
        )

        # Split shape
        rect = Rectangle(
            width = a,
            height = a - b,
            fill_color = GREEN,
            fill_opacity = opacity,
        ).move_to(big_square.get_corner(UL), UL)
        rect2 = Rectangle(
            width = a - b,
            height = b,
            fill_color = GREEN,
            fill_opacity = opacity,
        ).move_to(big_square.get_corner(DL), DL)
        self.play(
            FadeIn(VGroup(rect, rect2)),
            FadeOut(shape),
        )
        self.wait()

        # Reorganise pieces
        self.play(
            ApplyMethod(VGroup(rect2, b_label).shift, b*UR),
            FadeOut(b_label),
        )
        aplusb = rect.length(DOWN, LEFT, 'a + b', a + b)
        b_label = rect.length(UP, RIGHT, 'b', -b)
        self.play(
            ApplyMethod(aminusb.shift, b*RIGHT),
            Rotate(rect2, -PI/2, about_point=rect2.get_corner(DR)),
            FadeIn(aplusb),
            FadeIn(b_label)
        )
        self.wait()

        # Print rhs
        eq = TexMobject('=', color=GREEN).scale(1.5).next_to(lhs2, RIGHT)
        rhs1 = TexMobject('(a + b)', color=GREEN).scale(1.5).next_to(eq, RIGHT)
        rhs2 = TexMobject('(a - b)', color=GREEN).scale(1.5).next_to(rhs1, RIGHT)
        self.play(
            FadeIn(eq),
            Transform(aplusb.copy(), rhs1),
        )
        self.wait()
        self.play(
            Transform(aminusb.copy(), rhs2),
        )
        self.wait(5)
