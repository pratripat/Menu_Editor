import pygame, json
from ..ux.menu import Menu

class Workspace:
    def __init__(self, menu_editor):
        self.menu_editor = menu_editor
        self.main_menu = self.menu_editor.menu_manager.get_menu_with_id('main_menu')
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
            self.menu_editor.options_panel.update_attrs()
        elif not self.menu_editor.menu_manager.get_selected_object():
            self.update_scrolling()
            if pygame.K_l in self.menu_editor.input.keys_pressed:
                self.menu_editor.load_open_dialogbox()
                self.current_menu = [menu for menu in self.menu_editor.menu_manager.menus if menu.id not in ['selection_panel_menu', 'format_panel_menu', 'options_menu']][0]
                self.set_current_object(self.current_menu)
            elif pygame.K_o in self.menu_editor.input.keys_pressed:
                self.menu_editor.load_save_dialogbox()

    def update_current_object(self):
        to_be_checked_menus = []

        if self.menu_editor.format_panel.menu.is_mouse_hovering(self.scroll) or self.menu_editor.selection_panel.menu.is_mouse_hovering(self.scroll) or self.menu_editor.options_panel.menu.is_mouse_hovering(self.scroll):
            return

        for menu in self.menu_editor.menu_manager.menus:
            if menu.id not in ['selection_panel_menu', 'format_panel_menu', 'options_menu']:
                to_be_checked_menus.append(menu)

        for menu in to_be_checked_menus:
            if menu.is_mouse_hovering(self.scroll):
                self.current_menu = menu
                break

        for object in self.current_menu.objects:
            if object.is_mouse_hovering(self.scroll):
                self.set_current_object(object)
                return

        self.set_current_object(self.current_menu)
        self.current_menu.selected_object = None

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

    def set_current_object(self, object):
        self.current_object = object
        self.menu_editor.format_panel.update_attrs()
        self.menu_editor.options_panel.update_attrs()

    def set_start_position(self, position):
        self.start_position = [position[0]+self.scroll[0], position[1]+self.scroll[1]]
