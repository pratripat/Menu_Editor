import pygame, json
from ..ux.menu import Menu

class Selection_Panel:
    def __init__(self, menu_editor):
        self.menu_editor = menu_editor
        self.menu = self.menu_editor.menu_manager.get_menu_with_id('selection_panel_menu')
        self.menu.render_according_to_scroll = False

    def render(self):
        # self.menu.render()
        pass

    def update(self):
        # self.menu.update()
        pass
