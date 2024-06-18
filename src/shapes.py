from pyray import draw_rectangle, Rectangle, Vector2, Color, check_collision_point_rec
from abc import ABC

class Shape(ABC):
    def draw(self, position: Vector2):
        pass


    def check_point_collision(self, position: Vector2, point: Vector2) -> bool:
        pass


class Rec(Shape):
    def __init__(self, width: int, height: int, color: Color):
        self.width = width
        self.height = height
        self.color = color


    def draw(self, position: Vector2):
        x = int(position.x - self.width//2)
        y = int(position.y - self.height//2)
        draw_rectangle(x , y , self.width, self.height, self.color)


    def check_point_collision(self, position: Vector2, point: Vector2, ) -> bool:
        x = int(position.x - self.width//2)
        y = int(position.y - self.height//2)
        rec = Rectangle(x, y, self.width, self.height)
        
        return check_collision_point_rec(point, rec)