from typing import Any, Callable 
from pyray import get_mouse_position, is_mouse_button_pressed, MouseButton

class GameObject:
    def update():
        pass


    def draw():
        pass


class Scene:
    def __init__(self, name: str):
        self.name: str = name
        self.game_objects : list[GameObject]= []

    def update(self, res: dict):
        for g_o in self.game_objects:
            g_o.update(res)
    

    def draw(self, res: dict):
        for g_o in self.game_objects:
            g_o.draw(res)


    def append_objects(self, object : GameObject | list[GameObject] ):
        if type(object) == list:
            self.game_objects.extend(object)
        else:
            self.game_objects.append(object)


class World:
    def __init__(self):
        self.resources: dict[str, Any] = {}
        self.scenes: dict[str, Scene] = {}
        self.current_scene: Scene= None


    def frame(self):
        self.resources["MousePosition"] = get_mouse_position() 
        self.resources["MouseClickLeft"] = is_mouse_button_pressed(int(MouseButton.MOUSE_BUTTON_LEFT))
        if self.current_scene != None:
            self.current_scene.update(self.resources)
            self.current_scene.draw(self.resources)


    def set_scene(self,name: str):
        self.current_scene = self.scenes[name]
    

    def add_scene(self, scene: Scene):
        self.scenes[scene.name] = scene
