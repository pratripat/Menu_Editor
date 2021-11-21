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
            #backspace
            if key == '\x08':
                self.text = self.text[:-1]
            #other keys
            else:
                self.text += key
