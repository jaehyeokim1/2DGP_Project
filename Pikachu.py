from pico2d import *

class Character:
    def __init__(self):
        self.pos_x, self.pos_y = 80, 120  # 캐릭터의 초기 위치
        self.animation_frame = 0  # 애니메이션 프레임
        self.dir = 0  # 이동 방향
        self.jumping = False  # 점프 여부
        self.jumping_velocity = 10  # 점프 속도
        self.max_jumping_height = 200  # 최대 점프 높이
        self.initial_y_position = 0  # 초기 Y 위치
        self.gravity_force = 1  # 중력
        self.downward_speed = 0  # 하강 속도
        self.sprite = load_image('walk_animation.png')  # 애니메이션 스프라이트 이미지 로드

    def update(self):
        self._animate()  # 애니메이션 갱신
        self._jump()  # 점프 처리
        self._move()  # 이동 처리

    def _animate(self):
        # 애니메이션 프레임 업데이트
        self.animation_frame = (self.animation_frame + 1) % 5  # 애니메이션의 총 프레임 수에 맞게 수정

    def _jump(self):
        # 점프 처리
        if self.jumping:
            self.pos_y += self.jumping_velocity
            if self.pos_y >= self.initial_y_position + self.max_jumping_height:
                self.jumping = False
                self.downward_speed = 0
        else:
            self.downward_speed += self.gravity_force
            self.pos_y -= self.downward_speed
            if self.pos_y <= 120:  # 바닥에 닿으면 멈춤
                self.pos_y = 120
                self.downward_speed = 0
            self.initial_y_position = self.pos_y if not self.jumping else self.initial_y_position

    def _move(self):
        # 이동 처리
        self.pos_x += 10 * self.dir
        # 화면 밖으로 나가지 않도록 제한
        self.pos_x = max(40, min(self.pos_x, 350))

    def start_jumping(self):
        if not self.jumping:
            self.jumping = True
            self.downward_speed = 0

    def draw(self):
        # 스프라이트 이미지를 애니메이션에 맞게 그리기
        self.sprite.clip_draw(int(self.animation_frame) * 110, 0, 110, 110, self.pos_x, self.pos_y)

def process_events(player):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            return False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                return False
            elif event.key == SDLK_g:
                player.dir += 1  # 오른쪽으로 이동
            elif event.key == SDLK_d:
                player.dir -= 1  # 왼쪽으로 이동
            elif event.key == SDLK_r:
                player.start_jumping()  # 점프 시작
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_g:
                player.dir -= 1
            elif event.key == SDLK_d:
                player.dir += 1
    return True

def main():
    open_canvas(800, 600)
    background = load_image('map.png')  # 배경 이미지 로드
    player = Character()  # 플레이어 캐릭터 생성
    is_running = True

    while is_running:
        is_running = process_events(player)  # 이벤트 처리
        player.update()  # 캐릭터 업데이트
        render_scene([player], background)  # 화면 그리기
        delay(0.05)

    close_canvas()

def render_scene(objects, background):
    clear_canvas()
    background.draw(400, 300)  # 배경을 화면 중앙에 그리기
    for obj in objects:
        obj.draw()  # 객체 그리기
    update_canvas()

if __name__ == '__main__':
    main()
