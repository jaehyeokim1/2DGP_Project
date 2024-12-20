import game_framework
from pico2d import *
import game_world
import play_mode

image = None

def enter():
    global image
    image = load_image('test.png')

def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                game_framework.change_mode(play_mode)
            elif event.key == SDLK_ESCAPE:
                game_framework.quit()

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
