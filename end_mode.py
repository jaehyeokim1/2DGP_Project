from pico2d import *
import game_framework
import title_mode

def enter():
    global img2
    img2 = load_image('End.png')  # 필요하면 경로 수정

def exit():
    global img2
    del img2

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(title_mode)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

def draw():
    clear_canvas()
    img2.draw(400, 300)
    update_canvas()

def update():
    pass  # 현재는 아무 동작을 하지 않음
