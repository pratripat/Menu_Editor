import pygame, json

from .ui_components.button import Button

class Menu:
    def __init__(self, menu_editor, data=None):
        self.menu_editor = menu_editor

        if not data:
            data = json.load(open('data/configs/default/menu.json'))

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
        # self.text_boxes = data['text_boxes']
        # self.check_boxes = data['check_boxes']
        # self.radio_buttons = data['radio_buttons']
        # self.sub_menus = data['sub_menus']
        self.events = {}

    def load_buttons(self, buttons_data):
        buttons = []

        for data in buttons_data:
            button = Button(self.menu_editor, self, data)
            buttons.append(button)

        return buttons

    def render(self):
        surface = pygame.Surface(self.size)
        surface.set_colorkey((0,0,0))

        pygame.draw.rect(surface, self.background_color, [0, 0, *self.size], border_radius=self.border_radius)
        pygame.draw.rect(surface, self.border_color, [0, 0, *self.size], width=self.border_width, border_radius=self.border_radius)

        surface.set_alpha(self.opacity/100*255)

        self.menu_editor.screen.blit(surface, self.position)

        for button in self.buttons:
            button.render()

    def update(self):
        for button in self.buttons:
            button.update()

    def send_event(self, event_type, object_id):
        if event_type in self.events.keys():
            self.events[event_type].append(object_id)
        else:
            self.events[event_type] = [object_id]
