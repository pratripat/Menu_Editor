import json
from ..ux.menu import Menu

class Format_Panel:
    def __init__(self, menu_editor):
        self.menu_editor = menu_editor
        self.menu = self.menu_editor.menu_manager.get_menu_with_id('format_panel_menu')
        self.menu.render_according_to_scroll = False

    def render(self):
        # self.menu.render()
        pass

    def update(self):
        self.menu.update()

        for object in self.menu.objects:
            if object.id == 'object_id_textbox':
                self.menu_editor.workspace.current_object.id = object.text
            elif object.id == 'object_text_textbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    self.menu_editor.workspace.current_object.text = object.text
            elif object.id == 'object_offset_x_textbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    number = ''.join(i for i in object.text if i.isdigit())
                    if number == '': number = '0'
                    self.menu_editor.workspace.current_object.offset[0] = int(number)
            elif object.id == 'object_offset_y_textbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    number = ''.join(i for i in object.text if i.isdigit())
                    if number == '': number = '0'
                    self.menu_editor.workspace.current_object.offset[1] = int(number)
            elif object.id == 'object_size_x_textbox':
                number = ''.join(i for i in object.text if i.isdigit())
                if number == '': number = '0'
                self.menu_editor.workspace.current_object.size[0] = int(number)
            elif object.id == 'object_size_y_textbox':
                number = ''.join(i for i in object.text if i.isdigit())
                if number == '': number = '0'
                self.menu_editor.workspace.current_object.size[1] = int(number)
            elif object.id == 'object_centered_textbox':
                self.menu_editor.workspace.current_object.centered = object.checked    

    def update_attrs(self):
        if not self.menu_editor.workspace.current_object.is_menu:
            self.menu.get_object_with_id('object_text_textbox').interactable = True
            self.menu.get_object_with_id('object_offset_x_textbox').interactable = True
            self.menu.get_object_with_id('object_offset_y_textbox').interactable = True
            self.menu.change_object_attr('object_text_textbox', 'text', self.menu_editor.workspace.current_object.text)
            self.menu.change_object_attr('object_offset_x_textbox', 'text', str(int(self.menu_editor.workspace.current_object.offset[0])))
            self.menu.change_object_attr('object_offset_y_textbox', 'text', str(int(self.menu_editor.workspace.current_object.offset[1])))
        else:
            self.menu.get_object_with_id('object_text_textbox').interactable = False
            self.menu.get_object_with_id('object_offset_x_textbox').interactable = False
            self.menu.get_object_with_id('object_offset_y_textbox').interactable = False
            self.menu.change_object_attr('object_text_textbox', 'text', '')
            self.menu.change_object_attr('object_offset_x_textbox', 'text', '0')
            self.menu.change_object_attr('object_offset_y_textbox', 'text', '0')

        self.menu.change_object_attr('object_id_textbox', 'text', self.menu_editor.workspace.current_object.id)
        self.menu.change_object_attr('object_size_x_textbox', 'text', str(int(self.menu_editor.workspace.current_object.size[0])))
        self.menu.change_object_attr('object_size_y_textbox', 'text', str(int(self.menu_editor.workspace.current_object.size[1])))
        self.menu.change_object_attr('object_centered_textbox', 'checked', self.menu_editor.workspace.current_object.centered)
