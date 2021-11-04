import pygame

class Selection_Panel:
    def __init__(self, menu_editor):
        self.menu_editor = menu_editor

    def render(self):
        pygame.draw.rect(self.menu_editor.screen, (99, 92, 109), (0, 0, 200, self.menu_editor.screen.get_height()))

    def update(self):
        pass
