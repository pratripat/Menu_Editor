import pygame, sys

from tkinter import *
from tkinter import filedialog

from .menu_manager import Menu_Manager
from .menu_editor_components.workspace import Workspace
from .menu_editor_components.selection_panel import Selection_Panel
from .menu_editor_components.format_panel import Format_Panel

pygame.display.set_caption('Menu Editor')

class Menu_Editor:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)

        self.menu_manager = Menu_Manager(self)
        self.workspace = Workspace(self)
        self.format_panel = Format_Panel(self)
        self.selection_panel = Selection_Panel(self)

        self.workspace.set_current_object(self.workspace.main_menu)

        self.clock = pygame.time.Clock()
        self.fps = 100

    def render(self):
        self.screen.fill((0,0,0))

        self.menu_manager.render()
        self.workspace.render()
        self.selection_panel.render()
        self.format_panel.render()

        pygame.display.update()

    def update(self):
        self.clock.tick(self.fps)

        self.menu_manager.update()
        self.workspace.update()
        self.selection_panel.update()
        self.format_panel.update()

    def event_loop(self):
        self.keys_pressed = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                self.keys_pressed.append(event.unicode)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.workspace.update_current_object()
                elif event.button == 3:
                    self.workspace.set_start_position(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                self.workspace.add_object(pygame.mouse.get_pos())

    def run(self):
        while True:
            self.event_loop()
            self.update()
            self.render()

    def load_open_dialogbox(self):
        filepath = filedialog.askopenfilename(initialdir = '//home//shubhendu//Documents//puttar//github-ssh//Menu_Editor//data/configs', filetypes = [("Json", '*.json')])

        if filepath != ():
            self.workspace.load_data(filepath)

    @property
    def dt(self):
        return 1/self.clock.get_fps()+0.00001
