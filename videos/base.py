import manimlib.imports as m


class Scene(m.Scene):
    CONFIG = {
        "camera_config": {"background_color": m.WHITE},
    }


class DoubleArrow(m.DoubleArrow):
    def __init__(self, a, b, **kwargs):
        options = {
            "color": m.BLACK,
        }
        options.update(kwargs)
        m.DoubleArrow.__init__(self, a, b, **options)


class Rectangle(m.Rectangle):
    def __init__(self, **kwargs):
        options = {
            "color": m.BLACK,
        }
        options.update(kwargs)
        m.Rectangle.__init__(self, **options)

    def write(self, tex):
        return TexMobject(tex).scale(2).move_to(self.get_center())

    def length(self, edge, start_direction, text, length, shift=0.2):
        arrow = m.DoubleArrow(
            self.get_corner(edge + start_direction),
            self.get_corner(edge + start_direction) - length * start_direction,
            color=m.GRAY,
            stroke_width=1,
            tip_length=0.1,
            buff=0,
        ).shift(shift * edge)
        label = TexMobject(text, color=m.GRAY).next_to(arrow, 0.1 * edge)
        return m.VGroup(arrow, label)


class Square(Rectangle, m.Square):
    def __init__(self, **kwargs):
        options = {
            "color": m.BLACK,
        }
        options.update(kwargs)
        m.Square.__init__(self, **options)


class TexMobject(m.TexMobject):
    def __init__(self, *text, **kwargs):
        options = {
            "color": m.BLACK,
            "background_stroke_width": 0,
        }
        options.update(kwargs)
        m.TextMobject.__init__(self, *text, **options)
