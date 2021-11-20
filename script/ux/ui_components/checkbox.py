import pygame
from ..ui_component import UI_Component

class CheckBox(UI_Component):
    def __init__(self, menu_editor, menu, data=None):
        super().__init__(menu_editor, menu, 'checkbox', data)

        self.checked = False
        self.just_clicked = False

    def render(self, scroll=[0,0]):
        surface = pygame.Surface(self.size)
        surface.set_colorkey((0,0,0))

        pygame.draw.rect(surface, self.current_color, [0, 0, *self.size], border_radius=self.border_radius)
        pygame.draw.rect(surface, self.border_color, [0, 0, *self.size], width=self.border_width, border_radius=self.border_radius)

        pygame.draw.rect(surface, self.border_color, [10, 10, self.size[1]-20, self.size[1]-20], width=self.border_width)

        if self.checked:
            pygame.draw.rect(surface, self.border_color, [12, 12, self.size[1]-24, self.size[1]-24])

        surface.set_alpha(self.opacity/100*255)

        self.menu_editor.screen.blit(surface, [self.position[0]-self.render_offset[0]-scroll[0], self.position[1]-self.render_offset[1]-scroll[1]])

        if self.font:
            self.text = self.font.remove_unwanted_text(self.text)

            alpha = self.font_opacity/100*255
            self.font.render(self.menu_editor.screen, self.text, [self.font_position[0]+self.size[1]-24-self.render_offset[0]-scroll[0], self.font_position[1]-self.render_offset[1]-scroll[1]], center=(True, True), scale=self.font_scale, color=self.font_color, background_color=self.font_background, alpha=alpha, font_wrapping_width=self.size[0]-self.size[1]-20)

    def update(self, scroll=[0,0]):
        super().update(scroll)

        if self.is_clicked(scroll):
            if not self.just_clicked:
                self.checked = not self.checked
                self.just_clicked = True
        elif not pygame.mouse.get_pressed()[0]:
            self.just_clicked = False
