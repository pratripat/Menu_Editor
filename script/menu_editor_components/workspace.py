import pygame, json
from ..ux.menu import Menu

class Workspace:
    def __init__(self, menu_editor):
        self.menu_editor = menu_editor
        self.main_menu = self.menu_editor.menu_manager.get_menu_with_id('main_menu')
        # self.main_menu = Menu(self.menu_editor, json.load(open('data/configs/menus/main_menu.json', 'r')))
        self.current_menu = self.main_menu
        self.start_position = None

        self.scroll = [0,0]

    def render(self):
        # self.current_menu.render(self.scroll)
        pass

    def update(self):
        self.current_menu.update(self.scroll)

        if self.current_menu.selected_object and self.current_menu.selected_object.object_id == 'textbox':
            self.menu_editor.format_panel.update_attrs()
        else:
            self.update_scrolling()
            if 'l' in self.menu_editor.keys_pressed:
                self.menu_editor.load_open_dialogbox()
        pass

    def update_current_object(self):
        for object in self.current_menu.objects:
            if object.is_clicked(self.scroll):
                self.set_current_object(object)
                return

        #TEMP
        if self.current_menu.is_clicked(self.scroll):
            self.set_current_object(self.current_menu)

    def update_scrolling(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.scroll[0] -= 5 * self.menu_editor.fps * self.menu_editor.dt
        if keys[pygame.K_d]:
            self.scroll[0] += 5 * self.menu_editor.fps * self.menu_editor.dt
        if keys[pygame.K_w]:
            self.scroll[1] -= 5 * self.menu_editor.fps * self.menu_editor.dt
        if keys[pygame.K_s]:
            self.scroll[1] += 5 * self.menu_editor.fps * self.menu_editor.dt

    def add_object(self, position):
        if not self.start_position or not self.menu_editor.selection_panel.menu.selected_object:
            self.start_position = None
            return

        object = None
        if self.menu_editor.selection_panel.menu.selected_object.id == 'button_button':
            object = self.current_menu.add_button(self.start_position, [position[0]+self.scroll[0], position[1]+self.scroll[1]])
        elif self.menu_editor.selection_panel.menu.selected_object.id == 'textbox_button':
            object = self.current_menu.add_textbox(self.start_position, [position[0]+self.scroll[0], position[1]+self.scroll[1]])
        elif self.menu_editor.selection_panel.menu.selected_object.id == 'checkbox_button':
            object = self.current_menu.add_checkbox(self.start_position, [position[0]+self.scroll[0], position[1]+self.scroll[1]])
        elif self.menu_editor.selection_panel.menu.selected_object.id == 'radiobutton_button':
            object = self.current_menu.add_radiobutton(self.start_position, [position[0]+self.scroll[0], position[1]+self.scroll[1]])

        if object:
            self.set_current_object(object)

        self.start_position = None
        pass

    def load_data(self, filepath):
        self.main_menu = Menu(self.menu_editor, json.load(open(filepath, 'r')))
        self.current_menu = self.main_menu

    def set_current_object(self, object):
        self.current_object = object
        self.menu_editor.format_panel.update_attrs()

    def set_start_position(self, position):
        self.start_position = [position[0]+self.scroll[0], position[1]+self.scroll[1]]
