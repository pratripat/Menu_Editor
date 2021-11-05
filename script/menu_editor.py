import pygame, sys
from .menu_editor_components.workspace import Workspace
from .menu_editor_components.selection_panel import Selection_Panel
from .menu_editor_components.format_panel import Format_Panel

pygame.display.set_caption('Menu Editor')

class Menu_Editor:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 700), pygame.RESIZABLE)
        self.workspace = Workspace(self)
        self.selection_panel = Selection_Panel(self)
        self.format_panel = Format_Panel(self)

    def render(self):
        self.screen.fill((0,0,0))
        
        self.workspace.render()
        self.selection_panel.render()
        self.format_panel.render()

        pygame.display.update()

    def update(self):
        self.workspace.update()
        self.selection_panel.update()
        self.format_panel.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def run(self):
        while True:
            self.event_loop()
            self.update()
            self.render()
