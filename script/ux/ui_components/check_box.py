from ..ui_component import UI_Component

class Check_Box(UI_Component):
    def __init__(self, menu_editor, menu, data=None):
        super().__init__(menu_editor, menu, 'check_box', data)
