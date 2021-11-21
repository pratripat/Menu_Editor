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
            if object.id == 'object_text_textbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    self.menu_editor.workspace.current_object.text = object.text

    def update_attrs(self):
        self.menu.change_object_attr('object_id_textbox', 'text', self.menu_editor.workspace.current_object.id)

        if not self.menu_editor.workspace.current_object.is_menu:
            self.menu.get_object_with_id('object_text_textbox').interactable = True
            self.menu.change_object_attr('object_text_textbox', 'text', self.menu_editor.workspace.current_object.text)
        else:
            self.menu.get_object_with_id('object_text_textbox').interactable = False
            self.menu.change_object_attr('object_text_textbox', 'text', '')
