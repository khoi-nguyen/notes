from manimlib.imports import *
from videos.base import *


class MultiplyIndices(Scene):
    def construct(self):
        question = TexMobject("2^4", "\\times", "2^3", "=")
        question.set_color_by_tex_to_color_map({"4": BLUE, "3": RED})
        question.scale(1.5)
        self.play(Write(question))
        self.wait()

        rhs = TexMobject("2^4", "\\times", "2^3")
        rhs.set_color_by_tex_to_color_map({"4": BLUE, "3": RED})
        rhs.scale(1.5)
        rhs.next_to(question, RIGHT)
        self.play(Write(rhs))
        self.wait()

        equation = VGroup(question, rhs)
        self.play(ApplyMethod(equation.to_edge, LEFT))
        self.wait()

        expanded_rhs = TexMobject(
            "{2} \\times 2 \\times 2 \\times 2", "\\times", "2 {\\times} 2 \\times 2"
        )
        expanded_rhs.set_color_by_tex("{2} ", BLUE)
        expanded_rhs.set_color_by_tex("{\\times}", RED)
        expanded_rhs.scale(1.5)
        expanded_rhs.next_to(question, RIGHT)
        self.play(Transform(rhs, expanded_rhs))
        self.wait(3)

        simplified_rhs = TexMobject("2^7", color=GREEN)
        simplified_rhs.scale(1.5)
        simplified_rhs.next_to(question, RIGHT)
        self.play(Transform(rhs, simplified_rhs))

        self.wait(5)
