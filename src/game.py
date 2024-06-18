from pyray import Vector2, get_screen_width, get_screen_height, set_trace_log_level, init_window, close_window, clear_background, begin_drawing, window_should_close, end_drawing, GRAY, RED
from typing import Callable
from .ui import Button, MainMenu, UIText
from .shapes import Rec
from .event import Event
from .world import World, Scene
from .font import FontConfig

class Window:
    def __init__(self):
        self.width = get_screen_width()
        self.height = get_screen_height()


class Game:
    def __init__(self):
        self.should_run = False
        self.world = World()
        self.scenes_to_add = []

    def startup(self): 
        set_trace_log_level(6)
        init_window(1920,1080, "Four Wins")
        self.world.resources["Window"] = Window()

        self.should_run = True
        for scene in self.scenes_to_add:
            self.world.add_scene(scene(self.world))
        self.world.set_scene(self.start_scene)


    def shutdown(self):
        close_window()


    def run(self):
        self.startup()
        while self.should_run:
            self.update_frame()
    
        self.shutdown()


    def update_frame(self):
        clear_background(GRAY)
        begin_drawing()
        if window_should_close():
            self.emit_close()
        self.world.frame()
        end_drawing()

    
    def emit_close(self):
        self.should_run = False


    def init_scene(self, scene: Callable[...,Scene]):
        self.scenes_to_add.append(scene)


    def set_start_scene(self, scene_name: str):
        self.start_scene = scene_name