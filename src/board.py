from .world import GameObject
from pyray import Vector2,get_screen_height, check_collision_point_rec, draw_rectangle,draw_rectangle_rec, RED, Rectangle, draw_text
from .shapes import Rec
from colorsys import hls_to_rgb

class Entry:
    def __init__(self,position:Vector2):
        self.size = 50
        self.rec = Rectangle(
            int(position.x) - self.size //4,
            0,
            int(self.size) + self.size //2,
            int(self.size * get_screen_height())
        )
        self.not_selected_color = (255,0,0,100)
        self.selected_color = (255,0,0,150)
        self.color = self.not_selected_color

    def check_input(self, position: Vector2, input:bool) -> bool:
        self.color = self.not_selected_color
        if check_collision_point_rec(position, self.rec):
            self.color = self.selected_color
            if input == True:
                return True
        return False

    def draw(self):        
        draw_rectangle_rec(self.rec, self.color) 


class Cell:
    def __init__(self, position: Vector2,owner: int = 1 , index = -1):
        self.owner = owner
        self.index = index
        self.size = 50
        self.position = position
        self.default_color = (200,200,200,255) 

    def draw(self):
        color = self.default_color
        if self.owner > 0:
            color = index_to_color(self.owner)

        draw_rectangle(int(self.position.x) , int(self.position.y) , int(self.size), int(self.size),color) 
        if self.index > 0:
            # place text
            number = int(self.index)
            draw_text(str(number), int(self.position.x), int(self.position.y),20,(0,0,0,255))


    def is_empty(self) -> bool:
        if self.owner < 0:
            return True
        return False


    def set_owner(self, owner_index):
        self.owner = owner_index


class Player:
    def __init__(self,index):
        self.index = index


class Board(GameObject):
    def __init__(self, position: Vector2, rows: int , columns: int, spacing: int = 0, player_count : int = 2):
        self.position = position
        self.columns = columns
        self.rows = rows
        self.spacing = spacing
        self.cells: dict[int,Cell] = {}
        self.entrys: dict[int,Entry] = {}
        self.players: dict[int, Player]
        self.cell_size = Cell(Vector2()).size
        self.width = self.cell_size * rows + (rows-1) * spacing  
        self.height = self.cell_size * columns + (columns-1) * spacing
        
        self.player_count = player_count
        self.current_player = 1


        #Create cells
        for column in range(0,columns,1):
            for row in range(0, rows, 1):
                coord = Vector2(row,column)
                position = self._calc_position_from_coord(coord.x,coord.y)
                index = self._calc_index(coord.x,coord.y)
                self.cells[index] = Cell(position,-1, index=index)

        #Create Entrys
        for entry in range (0, rows, 1):
            coord = Vector2(entry,0)
            position = self._calc_position_from_coord(coord.x,coord.y)
            index = self._calc_index(coord.x,coord.y)
            self.entrys[index] = Entry(position)


    def update(self, res: dict):
        mouse_click_left = res["MouseClickLeft"]
        mouse_position = res["MousePosition"]
        for index, entry in self.entrys.items():
            if entry.check_input(mouse_position,mouse_click_left):
                self._handle_column(index)        
                

    def draw(self, res: dict):
        for entry in self.entrys.values():
            entry.draw()

        
        for cell in self.cells.values():
            cell.draw()

        

    def _calc_index(self, row: int, column: int) -> int:
        index = self.columns * row + column 
        return int(index)
    

    def _calc_coord(self, index) -> Vector2:
        column = index // self.columns
        row = index % self.columns

        return Vector2(row, column)
    

    def _calc_position_from_coord(self, row: int, column: int) -> Vector2:
        return Vector2(
            row * self.cell_size + self.position.x - self.width//2 + (row * (self.spacing )),
            column * self.cell_size + self.position.y - self.height//2 + (column * (self.spacing) )
        )


    def _handle_column(self, index: int):
        to_place=-1
        for i in range(index,index+self.columns,1):
            if self.cells[i].is_empty():
                to_place = i
        self._player_turn(to_place)

    def _player_turn(self, index):
        self.cells[index].set_owner(self.current_player)
        self.current_player +=1
        if self.current_player > self.player_count:
            self.current_player = 1


def index_to_color(index: int) -> tuple[int, int, int, int]:
    hue = (index * 60) % 360  
    saturation = 0.5
    lightness = 0.5
    r, g, b = hls_to_rgb(hue / 360, lightness, saturation)
    return (int(r * 255), int(g * 255), int(b * 255), int (255))