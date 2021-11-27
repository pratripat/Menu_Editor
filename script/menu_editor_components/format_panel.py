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
            elif object.id == 'object_centered_checkbox':
                self.menu_editor.workspace.current_object.centered = object.checked
            elif object.id == 'object_background_color_textbox':
                color = [min(255, int(i)) for i in object.text.split(' ') if i.isdigit()]
                for i in range(3-len(color)): color.append(0)
                self.menu_editor.workspace.current_object.background_color = tuple(color)
            elif object.id == 'object_border_color_textbox':
                color = [min(255, int(i)) for i in object.text.split(' ') if i.isdigit()]
                for i in range(3-len(color)): color.append(0)
                self.menu_editor.workspace.current_object.border_color = tuple(color)
            elif object.id == 'object_hover_color_textbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    color = [min(255, int(i)) for i in object.text.split(' ') if i.isdigit()]
                    for i in range(3-len(color)): color.append(0)
                    self.menu_editor.workspace.current_object.hover_color = tuple(color)
            elif object.id == 'object_border_width_textbox':
                number = ''.join(i for i in object.text if i.isdigit())
                if number == '': number = '0'
                self.menu_editor.workspace.current_object.border_width = int(number)
            elif object.id == 'object_border_radius_textbox':
                number = ''.join(i for i in object.text if i.isdigit())
                if number == '': number = '0'
                self.menu_editor.workspace.current_object.border_radius = int(number)
            elif object.id == 'object_opacity_textbox':
                number = ''.join(i for i in object.text if i.isdigit())
                if number == '': number = '0'
                self.menu_editor.workspace.current_object.opacity = int(number)
            elif object.id == 'object_font_button' and object.is_clicked(self.menu.get_scroll(self.menu_editor.workspace.scroll)):
                if not self.menu_editor.workspace.current_object.is_menu:
                    filepath = self.menu_editor.load_open_fontfile_dialogbox()
                    if filepath:
                        self.menu_editor.workspace.current_object.load_font(filepath)
            elif object.id == 'object_font_color_textbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    color = [min(255, int(i)) for i in object.text.split(' ') if i.isdigit()]
                    for i in range(3-len(color)): color.append(0)
                    self.menu_editor.workspace.current_object.font_color = tuple(color)
            elif object.id == 'object_font_scale_textbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    number = ''.join(i for i in object.text if i.isdigit() or i == '.')
                    if number == '' or number == '.': number = '1'
                    self.menu_editor.workspace.current_object.font_scale = float(number)
            elif object.id == 'object_font_background_textbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    color = [min(255, int(i)) for i in object.text.split(' ') if i.isdigit()]
                    for i in range(3-len(color)): color.append(0)
                    color = tuple(color)
                    if color == (0, 0, 0): color = None
                    self.menu_editor.workspace.current_object.font_background = color
            elif object.id == 'object_font_opacity_textbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    number = ''.join(i for i in object.text if i.isdigit())
                    if number == '': number = '0'
                    self.menu_editor.workspace.current_object.font_opacity = int(number)
            elif object.id == 'object_interactable_checkbox':
                if not self.menu_editor.workspace.current_object.is_menu:
                    self.menu_editor.workspace.current_object.interactable = object.checked

        self.menu.update()

    def update_attrs(self):
        if not self.menu_editor.workspace.current_object.is_menu:
            self.menu.get_object_with_id('object_text_textbox').interactable = True
            self.menu.get_object_with_id('object_offset_x_textbox').interactable = True
            self.menu.get_object_with_id('object_offset_y_textbox').interactable = True
            self.menu.get_object_with_id('object_hover_color_textbox').interactable = True
            self.menu.get_object_with_id('object_font_button').interactable = True
            self.menu.get_object_with_id('object_font_color_textbox').interactable = True
            self.menu.get_object_with_id('object_font_scale_textbox').interactable = True
            self.menu.get_object_with_id('object_font_background_textbox').interactable = True
            self.menu.get_object_with_id('object_font_opacity_textbox').interactable = True
            self.menu.get_object_with_id('object_interactable_checkbox').interactable = True
            self.menu.change_object_attr('object_text_textbox', 'text', self.menu_editor.workspace.current_object.text)
            self.menu.change_object_attr('object_offset_x_textbox', 'text', str(int(self.menu_editor.workspace.current_object.offset[0])))
            self.menu.change_object_attr('object_offset_y_textbox', 'text', str(int(self.menu_editor.workspace.current_object.offset[1])))
            self.menu.change_object_attr('object_hover_color_textbox', 'text', ''.join(str(i)+' ' for i in self.menu_editor.workspace.current_object.hover_color)[:-1])
            self.menu.change_object_attr('object_font_button', 'text', self.menu_editor.workspace.current_object.font_filename)
            self.menu.change_object_attr('object_font_color_textbox', 'text', ''.join(str(i)+' ' for i in self.menu_editor.workspace.current_object.font_color)[:-1])
            self.menu.change_object_attr('object_font_scale_textbox', 'text', str(self.menu_editor.workspace.current_object.font_scale))
            self.menu.change_object_attr('object_font_background_textbox', 'text', ''.join(str(i)+' ' for i in self.menu_editor.workspace.current_object.get_font_background())[:-1])
            self.menu.change_object_attr('object_font_opacity_textbox', 'text', str(self.menu_editor.workspace.current_object.font_opacity))
            self.menu.change_object_attr('object_interactable_checkbox', 'checked', self.menu_editor.workspace.current_object.interactable)
        else:
            self.menu.get_object_with_id('object_text_textbox').interactable = False
            self.menu.get_object_with_id('object_offset_x_textbox').interactable = False
            self.menu.get_object_with_id('object_offset_y_textbox').interactable = False
            self.menu.get_object_with_id('object_hover_color_textbox').interactable = False
            self.menu.get_object_with_id('object_font_button').interactable = False
            self.menu.get_object_with_id('object_font_color_textbox').interactable = False
            self.menu.get_object_with_id('object_font_scale_textbox').interactable = False
            self.menu.get_object_with_id('object_font_background_textbox').interactable = False
            self.menu.get_object_with_id('object_font_opacity_textbox').interactable = False
            self.menu.get_object_with_id('object_interactable_checkbox').interactable = False
            self.menu.change_object_attr('object_text_textbox', 'text', '')
            self.menu.change_object_attr('object_offset_x_textbox', 'text', '0')
            self.menu.change_object_attr('object_offset_y_textbox', 'text', '0')
            self.menu.change_object_attr('object_hover_color_textbox', 'text', '')
            self.menu.change_object_attr('object_font_button', 'text', '')
            self.menu.change_object_attr('object_font_color_textbox', 'text', '')
            self.menu.change_object_attr('object_font_scale_textbox', 'text', '')
            self.menu.change_object_attr('object_font_background_textbox', 'text', '')
            self.menu.change_object_attr('object_font_opacity_textbox', 'text', '')
            self.menu.change_object_attr('object_interactable_checkbox', 'checked', False)

        self.menu.change_object_attr('object_id_textbox', 'text', self.menu_editor.workspace.current_object.id)
        self.menu.change_object_attr('object_size_x_textbox', 'text', str(int(self.menu_editor.workspace.current_object.size[0])))
        self.menu.change_object_attr('object_size_y_textbox', 'text', str(int(self.menu_editor.workspace.current_object.size[1])))
        self.menu.change_object_attr('object_centered_checkbox', 'checked', self.menu_editor.workspace.current_object.centered)
        self.menu.change_object_attr('object_background_color_textbox', 'text', ''.join(str(i)+' ' for i in self.menu_editor.workspace.current_object.background_color)[:-1])
        self.menu.change_object_attr('object_border_color_textbox', 'text', ''.join(str(i)+' ' for i in self.menu_editor.workspace.current_object.border_color)[:-1])
        self.menu.change_object_attr('object_border_width_textbox', 'text', str(self.menu_editor.workspace.current_object.border_width))
        self.menu.change_object_attr('object_border_radius_textbox', 'text', str(self.menu_editor.workspace.current_object.border_radius))
        self.menu.change_object_attr('object_opacity_textbox', 'text', str(self.menu_editor.workspace.current_object.opacity))
