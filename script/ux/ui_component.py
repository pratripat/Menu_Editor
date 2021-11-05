import pygame

from ..font_renderer import Font

class UI_Component:
    def __init__(self, menu_editor, menu, object_type, data=None):
        self.menu_editor = menu_editor
        self.menu = menu

        if not data:
            data = json.load(open('data/configs/'+object_type+'.json'))

        #PROPERTIES
        self.id = data['id']
        self.text = data['text']
        self.offset = data['offset']
        self.size = data['size']
        self.centered = data['centered']

        #STYLE
        self.background_color = data['background_color']
        self.border_color = data['border_color']
        self.hover_color = data['hover_color']
        self.border_width = data['border_width']
        self.border_radius = data['border_radius']
        self.opacity = data['opacity']

        #TEXT
        if data['font'] != None:
            self.font = Font('data/graphics/spritesheet/'+data['font'])
        else:
            self.font = None

        self.font_color = data['font_color']
        self.font_scale = data['font_scale']
        self.font_background = data['font_background']
        self.font_opacity = data['font_opacity']

        self.current_color = self.background_color

    def render(self):
        surface = pygame.Surface(self.size)
        surface.set_colorkey((0,0,0))

        pygame.draw.rect(surface, self.current_color, [0, 0, *self.size], border_radius=self.border_radius)
        pygame.draw.rect(surface, self.border_color, [0, 0, *self.size], width=self.border_width, border_radius=self.border_radius)

        surface.set_alpha(self.opacity/100*255)

        self.menu_editor.screen.blit(surface, self.position)

        if self.font:
            alpha = self.font_opacity/100*255
            self.font.render(self.menu_editor.screen, self.text, self.font_position, center=(True, True), scale=self.font_scale, color=self.font_color, background_color=self.font_background, alpha=alpha)

    def update(self):
        if self.is_mouse_hovering():
            self.current_color = self.hover_color
        else:
            self.current_color = self.background_color

        if self.is_clicked():
            self.menu.send_event('button_click', self.id)

    def is_mouse_hovering(self):
        mouse_pos = pygame.mouse.get_pos()

        return (
            self.position[0] < mouse_pos[0] < self.position[0]+self.size[0] and
            self.position[1] < mouse_pos[1] < self.position[1]+self.size[1]
        )

    def is_clicked(self):
        return self.is_mouse_hovering() and pygame.mouse.get_pressed()[0]

    @property
    def position(self):
        return [self.menu.position[0]+self.offset[0], self.menu.position[1]+self.offset[1]]

    @property
    def font_position(self):
        return [self.position[0]+self.size[0]/2, self.position[1]+self.size[1]/2]
