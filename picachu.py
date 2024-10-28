from pico2d import *

# 캔버스 열기
open_canvas()

# 스프라이트 시트 이미지 로드
character = load_image('sprite_sheet.png')  # sprite_sheet.png 파일을 지정하세요.

def handle_events():
    global running, dir_x, dir_y, animation_type
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x = 1
                animation_type = 'right'
            elif event.key == SDLK_LEFT:
                dir_x = -1
                animation_type = 'left'
            elif event.key == SDLK_UP:
                dir_y = 1
                animation_type = 'up'
            elif event.key == SDLK_DOWN:
                dir_y = -1
                animation_type = 'down'
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key in (SDLK_RIGHT, SDLK_LEFT):
                dir_x = 0  # 멈출 때 이동 중단
            elif event.key in (SDLK_UP, SDLK_DOWN):
                dir_y = 0

running = True

# 피카츄의 위치 및 애니메이션 설정
x = 800 // 2
y = 300
frame = 0
dir_x = 0
dir_y = 0
animation_type = 'idle'  # 기본 정지 애니메이션

# 스프라이트의 애니메이션 시작 위치 (예시: 각 방향에 따라 행이 다름)
ANIMATIONS = {
    'idle': (0, 550),    # 정지 애니메이션: (x, y)
    'right': (0, 450),   # 오른쪽 이동 애니메이션
    'left': (0, 350),    # 왼쪽 이동 애니메이션
    'up': (0, 250),      # 위로 이동 애니메이션
    'down': (0, 150)     # 아래로 이동 애니메이션
}

while running:
    clear_canvas()

    # 현재 애니메이션의 위치 가져오기
    anim_x, anim_y = ANIMATIONS[animation_type]

    # 움직이지 않을 때 기본 정지 애니메이션 출력
    if dir_x == 0 and dir_y == 0:
        character.clip_draw(anim_x, anim_y, 70, 70, x, y)
    else:
        # 움직일 때: 해당 방향의 애니메이션 프레임을 순환
        character.clip_draw(frame * 70, anim_y, 70, 70, x, y)
        frame = (frame + 1) % 8  # 8 프레임 애니메이션

    update_canvas()
    handle_events()

    # 좌표 업데이트 (화면 경계 내에서 이동)
    x = min(750, max(50, x + dir_x * 5))
    y = min(550, max(50, y + dir_y * 5))

    delay(0.05)

close_canvas()
