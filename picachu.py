from pico2d import *

class Character:
    def __init__(self):
        self.pos_x, self.pos_y = 80, 120
        self.animation_frame = 0
        self.dir = 0
        self.jumping = False
        self.jumping_velocity = 10
        self.max_jumping_height = 200
        self.initial_y_position = 0
        self.gravity_force = 1
        self.downward_speed = 0
        self.sprite = load_image('walk_animation.png')

    def update(self):
        self._animate()
        self._jump()
        self._move()

    def _animate(self):
        # Update animation frame
        self.animation_frame = (self.animation_frame + 1) % 5

    def _jump(self):
        if self.jumping:
            self.pos_y += self.jumping_velocity
            if self.pos_y >= self.initial_y_position + self.max_jumping_height:
                self.jumping = False
                self.downward_speed = 0
        else:
            self.downward_speed += self.gravity_force
            self.pos_y -= self.downward_speed
            if self.pos_y <= 120:
                self.pos_y = 120
                self.downward_speed = 0
            self.initial_y_position = self.pos_y if not self.jumping else self.initial_y_position

    def _move(self):
        self.pos_x += 10 * self.dir
        # Boundary constraints
        self.pos_x = max(40, min(self.pos_x, 350))

    def start_jumping(self):
        if not self.jumping:
            self.jumping = True
            self.downward_speed = 0

    def draw(self):
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
                player.dir += 1
            elif event.key == SDLK_d:
                player.dir -= 1
            elif event.key == SDLK_r:
                player.start_jumping()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_g:
                player.dir -= 1
            elif event.key == SDLK_d:
                player.dir += 1
    return True

def main():
    open_canvas(800, 600)
    player = Character()
    is_running = True

    while is_running:
        is_running = process_events(player)
        player.update()
        render_scene([player])

        delay(0.05)

    close_canvas()

def render_scene(objects):
    clear_canvas()
    for obj in objects:
        obj.draw()
    update_canvas()

if __name__ == '__main__':
    main()
