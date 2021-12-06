import pygame, sys, json

from tkinter import *
from tkinter import filedialog

from .menu_manager import Menu_Manager
from .menu_editor_components.workspace import Workspace
from .menu_editor_components.selection_panel import Selection_Panel
from .menu_editor_components.format_panel import Format_Panel
from .input_system import Input

pygame.display.set_caption('Menu Editor')

class Menu_Editor:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)

        self.menu_manager = Menu_Manager(self)
        self.menu_manager.load_menus('data/configs/ui/menu_editor_ui.json')
        self.workspace = Workspace(self)
        self.format_panel = Format_Panel(self)
        self.selection_panel = Selection_Panel(self)
        self.options_menu = self.menu_manager.get_menu_with_id('options_menu')
        self.input = Input()

        self.workspace.set_current_object(self.workspace.main_menu)

        self.options_menu.render_according_to_scroll = False

        self.clock = pygame.time.Clock()
        self.fps = 100

    def render(self):
        self.screen.fill((0,0,0))

        self.menu_manager.render()
        self.workspace.render()
        self.selection_panel.render()
        self.format_panel.render()

        pygame.display.update()

    def update(self):
        self.clock.tick()

        self.input.update()
        self.menu_manager.update()
        self.workspace.update()
        self.selection_panel.update()
        self.format_panel.update()

        self.inputs()

    def inputs(self):
        if self.input.mouse_states['left']:
            self.workspace.update_current_object()
        elif self.input.mouse_states['right']:
            self.workspace.set_start_position(pygame.mouse.get_pos())

        if self.input.mouse_states['right_release']:
            self.workspace.add_object(pygame.mouse.get_pos())

        if self.options_menu.selected_object:
            if self.options_menu.selected_object.id == 'image_button':
                filepath = self.load_open_image_dialogbox()

                if filepath != () and self.workspace.current_object:
                    self.workspace.current_object.set_image(filepath)

                self.options_menu.selected_object = None
            elif self.options_menu.selected_object.id == 'delete_image_button':
                if self.workspace.current_object:
                    self.workspace.current_object.image_filepath = self.workspace.current_object.image = None
                self.options_menu.selected_object = None

    def run(self):
        while True:
            self.update()
            self.render()

    def load_open_dialogbox(self):
        filepath = filedialog.askopenfilename(initialdir = '/home/shubhendu/Documents/puttar/github-ssh/Menu_Editor/data/configs', filetypes = [('Json', '*.json')])

        try:
            self.menu_manager.clear_menus(['selection_panel_menu', 'format_panel_menu', 'options_menu'])
            self.menu_manager.load_menus(filepath)
            self.menu_manager.arrange_menus(['*', 'selection_panel_menu', 'format_panel_menu', 'options_menu'])
        except:
            pass

    def load_save_dialogbox(self):
        filepath = filedialog.asksaveasfilename(initialdir = '/home/shubhendu/Documents/puttar/github-ssh/Menu_Editor/data/configs', defaultextension = '.json', filetypes = [('Json', '*.json')])

        try:
            file = open(filepath, 'w')
            data = self.menu_manager.get_menu_data(['selection_panel_menu', 'format_panel_menu', 'options_menu'])
            json.dump(data, file)
            file.close()
        except:
            pass

    def load_open_fontfile_dialogbox(self):
        filepath = filedialog.askopenfilename(initialdir = '/home/shubhendu/Documents/puttar/github-ssh/Menu_Editor/data/graphics/spritesheet', filetypes = [('PNG', '*.png')])

        try:
            image = pygame.image.load(filepath)
            return filepath
        except:
            return None

    def load_open_image_dialogbox(self):
        filepath = filedialog.askopenfilename(initialdir = '/home/shubhendu/Documents/puttar/github-ssh/Menu_Editor/data/graphics', filetypes = [('PNG', '*.png')])

        try:
            image = pygame.image.load(filepath)
            return filepath
        except:
            return None

    @property
    def dt(self):
        return 1/self.clock.get_fps()+0.00001
