class Options_Panel:
    def __init__(self, menu_editor):
        self.menu_editor = menu_editor
        self.menu = self.menu_editor.menu_manager.get_menu_with_id('options_menu')
        self.menu.render_according_to_scroll = False

    def update(self):
        if self.menu.selected_object and self.menu_editor.workspace.current_object and not self.menu_editor.workspace.current_object.is_menu:
            if self.menu.selected_object.id == 'image_button':
                filepath = self.menu_editor.load_open_image_dialogbox()
                if filepath != ():
                    self.menu_editor.workspace.current_object.set_image(filepath)
                self.menu.selected_object = None

            elif self.menu.selected_object.id == 'delete_image_button':
                self.menu_editor.workspace.current_object.image_filepath = self.menu_editor.workspace.current_object.image = None
                self.menu.selected_object = None

            elif self.menu.selected_object.id == 'image_scale_textbox':
                scale = ''.join(i for i in self.menu.selected_object.text if i.isdigit() or i == '.')
                if scale == '' or scale == '.': scale = '1'
                self.menu_editor.workspace.current_object.set_image_scale(float(scale))

    def update_attrs(self):
        if not self.menu_editor.workspace.current_object.is_menu:
            self.menu.get_object_with_id('image_scale_textbox').interactable = True
            self.menu.get_object_with_id('image_button').interactable = True
            self.menu.get_object_with_id('delete_image_button').interactable = True
            self.menu.change_object_attr('image_scale_textbox', 'text', str(self.menu_editor.workspace.current_object.image_scale))
        else:
            self.menu.get_object_with_id('image_scale_textbox').interactable = False
            self.menu.get_object_with_id('image_button').interactable = False
            self.menu.get_object_with_id('delete_image_button').interactable = False
            self.menu.change_object_attr('image_scale_textbox', 'text', '')
