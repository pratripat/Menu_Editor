import pygame, json
from ..ux.menu import Menu

class Selection_Panel:
    def __init__(self, menu_editor):
        self.menu_editor = menu_editor
        self.menu = Menu(self.menu_editor, self.get_menu_data())

    def render(self):
        self.menu.render()

    def update(self):
        self.menu.update()

    def get_menu_data(self):
        return json.load(open('data/configs/menus/selection_panel.json', 'r'))
