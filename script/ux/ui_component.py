class UI_Component:
    def __init__(self, position):
        #PROPERTIES
        self.id = ''
        self.position = position
        self.size = [120,60]
        self.centered = False

        #STYLE
        self.background_color = (255,255,255)
        self.hover_color = (0,255,0)
        self.border_width = 0
        self.radius = 0
        self.opacity = 100

        #TEXT
        self.font = None
        self.font_color = (0,0,0)
        self.font_scale = 1
        self.font_background = None
        self.font_opacity = 100
