from .menu_editor_components.workspace import Workspace
from .menu_editor_components.selection_panel import Selection_Panel
from .menu_editor_components.format_panel import Format_Panel

class Menu_Editor:
    def __init__(self):
        self.workspace = Workspace()
        self.selection_panel = Selection_Panel()
        self.format_panel = Format_Panel()
