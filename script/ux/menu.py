import pygame, json

from .ui_components.button import Button
from .ui_components.textbox import TextBox

class Menu:
    def __init__(self, menu_editor, data=None):
        self.menu_editor = menu_editor

        if not data:
            data = json.load(open('data/configs/default/menu.json', 'r'))

        self.is_menu = True    

        #PROPERTIES
        self.id = data['id']
        self.position = data['position']
        self.size = data['size']
        self.centered = data['centered']

        # #STYLE
        self.background_color = tuple(data['background_color'])
        self.border_color = tuple(data['border_color'])
        self.border_width = data['border_width']
        self.border_radius = data['border_radius']
        self.opacity = data['opacity']

        self.buttons = self.load_buttons(data['buttons'])
        self.textboxes = self.load_textboxes(data['textboxes'])
        # self.check_boxes = data['check_boxes']
        # self.radio_buttons = data['radio_buttons']
        # self.sub_menus = data['sub_menus']
        self.events = {'button_click': [], 'textbox_click': []}

        self.selected_object = None

    def load_buttons(self, buttons_data):
        buttons = []

        for data in buttons_data:
            button = Button(self.menu_editor, self, data)
            buttons.append(button)

        return buttons

    def load_textboxes(self, textboxes_data):
        textboxes = []

        for data in textboxes_data:
            textbox = TextBox(self.menu_editor, self, data)
            textboxes.append(textbox)

        return textboxes

    def render(self, scroll=[0,0]):
        surface = pygame.Surface(self.size)
        surface.set_colorkey((0,0,0))

        pygame.draw.rect(surface, self.background_color, [0, 0, *self.size], border_radius=self.border_radius)
        pygame.draw.rect(surface, self.border_color, [0, 0, *self.size], width=self.border_width, border_radius=self.border_radius)

        surface.set_alpha(self.opacity/100*255)

        offset = [0, 0]
        if self.centered:
            offset = [self.size[0]/2, self.size[1]/2]

        position = [self.position[0]-offset[0]-scroll[0], self.position[1]-offset[1]-scroll[1]]

        self.menu_editor.screen.blit(surface, position)

        for button in self.buttons:
            button.render(scroll)

        for textbox in self.textboxes:
            textbox.render(scroll)

        if self.selected_object:
            self.selected_object.highlight(scroll)

    def update(self, scroll=[0,0]):
        self.events = {'button_click': [], 'textbox_click': []}

        for button in self.buttons:
            button.update(scroll)

        for textbox in self.textboxes:
            textbox.update(scroll)

        if self.selected_object:
            self.selected_object.check_for_inputs()

    def send_event(self, event_type, object_id):
        self.events[event_type].append(object_id)

    def add_button(self, start_position, end_position):
        button = Button(self.menu_editor, self)
        button.offset = [start_position[0]-self.position[0], start_position[1]-self.position[1]]
        button.size = [end_position[0]-start_position[0], end_position[1]-start_position[1]]

        if 0 in button.size:
            return None

        if button.size[0] < 0:
            button.offset[0] += button.size[0]
            button.size[0] = abs(button.size[0])
        if button.size[1] < 0:
            button.offset[1] += button.size[1]
            button.size[1] = abs(button.size[1])

        if button.id in [b.id for b in self.buttons]:
            button.id += str(len(self.buttons))

        self.buttons.append(button)
        return button

    def add_textbox(self, start_position, end_position):
        textbox = TextBox(self.menu_editor, self)
        textbox.offset = [start_position[0]-self.position[0], start_position[1]-self.position[1]]
        textbox.size = [end_position[0]-start_position[0], end_position[1]-start_position[1]]

        if 0 in textbox.size:
            return None

        if textbox.size[0] < 0:
            textbox.offset[0] += textbox.size[0]
            textbox.size[0] = abs(textbox.size[0])
        if textbox.size[1] < 0:
            textbox.offset[1] += textbox.size[1]
            textbox.size[1] = abs(textbox.size[1])

        if textbox.id in [b.id for b in self.textboxes]:
            textbox.id += str(len(self.textboxes))

        self.textboxes.append(textbox)
        return textbox

    def change_object_attr(self, object_id, attribute, value):
        for object in self.objects:
            if object.id == object_id:
                try:
                    setattr(object, attribute, value)
                except Exception as e:
                    print(e)
                    print('attribute setting error.')

    def get_data(self):
        return {
            'id': self.id,
            'position': self.position,
            'size': self.size,
            'centered': self.centered,
            'background_color': self.background_color,
            'border_color': self.border_color,
            'border_width': self.border_width,
            'border_radius': self.border_radius,
            'opacity': self.opacity,
            'buttons': self.buttons
        }

    def get_object_with_id(self, id):
        for object in [*self.buttons, *self.textboxes]:
            if object.id == id:
                return object

        return None

    def is_mouse_hovering(self, scroll=[0,0]):
        mouse_pos = pygame.mouse.get_pos()

        return (
            self.position[0]-self.render_offset[0] < mouse_pos[0]+scroll[0] < self.position[0]-self.render_offset[0]+self.size[0] and
            self.position[1]-self.render_offset[1] < mouse_pos[1]+scroll[1] < self.position[1]-self.render_offset[1]+self.size[1]
        )

    def is_clicked(self, scroll=[0,0]):
        return self.is_mouse_hovering(scroll) and pygame.mouse.get_pressed()[0]

    @property
    def objects(self):
        return [*self.buttons, *self.textboxes]

    @property
    def render_offset(self):
        if self.centered:
            return [self.size[0]/2, self.size[1]/2]
        return [0, 0]
