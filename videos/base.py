import manimlib.imports as m

class Scene(m.Scene):
    CONFIG = {
        'camera_config': {
            'background_color': m.WHITE,
        },
    }

class TexMobject(m.TexMobject):
    def __init__(self, *text, **kwargs):
        options = {
            'color': m.BLACK,
            'background_stroke_width': 0,
        }
        options.update(kwargs)
        m.TextMobject.__init__(self, *text, **options)
