import pygame

from ..ui_component import UI_Component

class TextBox(UI_Component):
    def __init__(self, menu, data=None):
        super().__init__(menu, 'textbox', data)

    def update(self, scroll=[0,0]):
        super().update(scroll)

    def check_for_inputs(self, keys=[]):
        if not self.interactable:
            return

        for key in keys:
            key_name = pygame.key.name(key)
            if key_name == 'backspace':
                self.text = self.text[:-1]
            elif key_name == 'space':
                self.text += ' '
            elif key_name == 'return':
                self.text += '\r'
            elif key_name in [letter for letter in 'abcdefghijklmnopqrstuvwxyz0123456789,./;"!@#$%^&*()_+=-'+"'"]:
                self.text += key_name
            else:
                print(key_name, 'was not added to the text...')
