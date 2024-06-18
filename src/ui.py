from pyray import get_mouse_position, is_mouse_button_down, MouseButton, Vector2, draw_text_pro, measure_text_ex, get_font_default, Font
from typing import List, Callable
from .shapes import Shape
from .event import Event
from .world import GameObject
from .font import FontConfig



class UIText:
    def __init__(self, text: str, position: Vector2, font_conf: FontConfig):
        self.text = text
        self.position = position
        self.font_conf = font_conf

    def draw(self, position: Vector2):
        font_size = self.font_conf.font_size
        text_len = measure_text_ex(get_font_default(), self.text, font_size , self.font_conf.spacing)
        draw_text_pro(self.font_conf.font,self.text, position,Vector2(text_len.x / 2, text_len.y/2),0, font_size, self.font_conf.spacing, self.font_conf.color)

class Button(GameObject):
    def __init__(self, 
                 shape: Shape, 
                 position: Vector2 = Vector2(), 
                 onclick: Event = None,
                 text: UIText = None
                 ):
        self.shape = shape
        self.position = position
        self.onclick = onclick
        self.gameobjects: List[GameObject] = []
        self.text = text

    def draw(self):
        self.shape.draw(self.position)
        if(self.text):
            self.text.draw(self.position)
        for go in self.gameobjects:
            go.draw()


    def append_object(self,object: GameObject | List[GameObject]):
        if type(object) is not list:
            self.gameobjects.append(object)
        else:
            self.gameobjects.extend(object)


    def update(self, res: dict):
        self.shape
        self.check_click(res["MousePosition"], MouseButton.MOUSE_BUTTON_LEFT)

        for go in self.gameobjects:
            go.update(res)
        pass


    def check_click(self, mouse_position: Vector2, button: MouseButton):
        if is_mouse_button_down(int(button)):
            if self.shape.check_point_collision(self.position, mouse_position):
                self.onclick.call()
        


class MainMenu(GameObject):
    def __init__(self, active: bool):
        self.gameobjects: List[GameObject] = [] 
        self.active : bool = active 


    def set_state(self,state: bool):
        self.active = state


    def append_object(self,object: GameObject | List[GameObject]):
        if type(object) is not list:
            self.gameobjects.append(object)
        else:
            self.gameobjects.extend(object)


    def draw(self, res: dict):
        if self.active:
            for go in self.gameobjects:
                go.draw()


    def update(self, res: dict):
        if self.active:
            for go in self.gameobjects:
                go.update(res)
