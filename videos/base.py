import manimlib.imports as m

class Scene(m.Scene):
    CONFIG = {
        'camera_config': {
            'background_color': m.WHITE,
        },
    }

class DoubleArrow(m.DoubleArrow):
    def __init__(self, a, b, **kwargs):
        options = {
            'color': m.BLACK,
        }
        options.update(kwargs)
        m.DoubleArrow.__init__(self, a, b, **options)

class Rectangle(m.Rectangle):
    def __init__(self, **kwargs):
        options = {
            'color': m.BLACK,
        }
        options.update(kwargs)
        m.Rectangle.__init__(self, **options)

class Square(m.Square):
    def __init__(self, **kwargs):
        options = {
            'color': m.BLACK,
        }
        options.update(kwargs)
        m.Square.__init__(self, **options)

class TexMobject(m.TexMobject):
    def __init__(self, *text, **kwargs):
        options = {
            'color': m.BLACK,
            'background_stroke_width': 0,
        }
        options.update(kwargs)
        m.TextMobject.__init__(self, *text, **options)
