import json

from .ux.menu import Menu

class Menu_Manager:
    def __init__(self, menu_editor):
        self.menu_editor = menu_editor
        self.menus = []

        self.load_menu([
            'data/configs/menus/main_menu.json',
            'data/configs/menus/selection_panel.json',
            'data/configs/menus/format_panel.json'
        ])

    def load_menu(self, filepaths):
        for filepath in filepaths:
            menu = Menu(json.load(open(filepath, 'r')))
            self.menus.append(menu)

    def render(self):
        for menu in self.menus:
            menu.render(self.menu_editor.screen, self.menu_editor.workspace.scroll)

    def update(self):
        for menu in self.menus:
            menu.update(self.menu_editor.workspace.scroll, self.menu_editor.keys_pressed)

    def get_menu_with_id(self, id):
        for menu in self.menus:
            if menu.id == id:
                return menu

        return None
