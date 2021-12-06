import json

from .ux.menu import Menu

class Menu_Manager:
    def __init__(self, menu_editor):
        self.menu_editor = menu_editor
        self.menus = []

    def load_menus(self, filepath):
        try:
            menus = json.load(open(filepath, 'r'))

            for menu_data in menus:
                menu = Menu(menu_data)
                self.menus.append(menu)
        except Exception as e:
            print('=========================================')
            print(e)
            print(filepath, 'could not be loaded...')
            print('=========================================')

    def clear_menus(self, exception_ids=[]):
        for menu in self.menus.copy():
            if menu.id not in exception_ids:
                self.menus.remove(menu)

    def add_menu(self, filepath):
        try:
            data = json.load(open(filepath, 'r'))
            menu = Menu(data)
            self.menus.append(menu)
        except Exception as e:
            print('=========================================')
            print(e)
            print(filepath, 'could not be loaded...')
            print('=========================================')

    def render(self):
        for menu in self.menus:
            menu.render(self.menu_editor.screen, self.menu_editor.workspace.scroll)

    def update(self):
        for menu in self.menus:
            menu.update(self.menu_editor.workspace.scroll, self.menu_editor.input.keys_pressed)

    def get_menu_with_id(self, id):
        for menu in self.menus:
            if menu.id == id:
                return menu

        return None

    def arrange_menus(self, order):
        arranged_menus = [None for _ in range(len(self.menus))]
        other_menus = []

        for i, menu_id in enumerate(order):
            if menu_id == '*':
                for menu in self.menus:
                    if menu.id not in order:
                        other_menus.append(menu)
                arranged_menus = arranged_menus[:i] + other_menus + arranged_menus[i+1:]
                continue

            menu = self.get_menu_with_id(menu_id)
            if menu:
                arranged_menus[i+len(other_menus)-1] = menu

        self.menus = [menu for menu in arranged_menus if menu != None]

    def get_menu_data(self, exception_ids=[]):
        data = [menu.get_data() for menu in self.menus if menu.id not in exception_ids]
        return data
