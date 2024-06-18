from pyray import Vector2, get_screen_width, get_screen_height, RED, draw_rectangle, Rectangle

from src.game import Game, Window
from src.event import Event
from src.ui import Button, MainMenu, FontConfig, UIText
from src.world import World, Scene
from src.shapes import Rec
from src.board import Board


class debug_object():
    def update(self, res:dict):
        pass

    def draw(self, res:dict):
        width = 10
        height = 10
        draw_rectangle(get_screen_width()//2 - width//2,get_screen_height()//2 - height//2, width, height, RED)

def create_main_menu_scene(world: World) -> Scene:
    scene = Scene("MainMenu")

    def start_game(world: World):
        world.set_scene("InGame")


    def exit_game():
        exit(0)
        

    main_menu = MainMenu(True)
    center = (get_screen_width() / 2, get_screen_height() / 2)
    start_game_event = Event(start_game)
    start_game_event.add_args(world)
    end_game_event = Event(exit_game)
    main_menu.append_object([
        Button(shape=Rec(200,200, RED),
               position=Vector2(center[0],center[1] - 120),
               onclick=start_game_event,
               text=UIText(text="Press to Start",
                           position=Vector2(0,0),
                            font_conf=FontConfig()
                         )
               ),
        Button(shape=Rec(200,200, RED),
               position=Vector2(center[0],center[1] + 120),
               onclick=end_game_event,
               text=UIText(text="exit",
                           position=
                                Vector2(0,0),
                            font_conf=FontConfig()
                         )
               ),
    ]
    )
    scene.append_objects(
        main_menu
    )

    return scene

def create_ingame_scene(world: World):
    scene = Scene("InGame")

    window : Window = world.resources["Window"]
    position = Vector2(window.width//2, window.height //2)
    board = Board(position, 7, 6, 50, 4)
    
    object = debug_object()
    scene.append_objects(board)
    scene.append_objects(object)


    return scene


def main():
    game = Game()
    game.init_scene(create_main_menu_scene)
    game.init_scene(create_ingame_scene)
    game.set_start_scene("InGame")
    game.run()


if __name__ == '__main__':
    main()
    

