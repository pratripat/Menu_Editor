from ..ui_component import UI_Component

class Text_Box(UI_Component):
    def __init__(self, menu_editor, menu, data=None):
        super().__init__(menu_editor, menu, 'text_box', data)
