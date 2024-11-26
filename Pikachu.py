from pico2d import load_image, load_font, delay
import Collision
import play_mode
import game_framework
import end_mode
class pikachu_l:
    def __init__(self):
        self.pos_x = 150
        self.pos_y = 70
        self.frame = 0
        self.frame2 = 5
        self.img = load_image('Pikachu.png')
        self.dirx = 0
        self.jump = 0
        self.locate = 0
        self.sec = 0
        self.win = False
        self.lose = False
        self.finish = 0
        self.font = load_font('ENCR10B.TTF', 25)

    def update(self):
        self.frame = (self.frame + 1) % self.frame2
        self.update_time()
        if not self.win and not self.lose:
            self.update_position()
            self.check_collision_with_net()

        self.check_game_status()

    def update_time(self):
        if self.sec < 10:
            self.sec += 0.03
        else:
            self.sec = 10

    def update_position(self):
        self.pos_x += self.dirx * 5
        if self.jump == 1:
            self.pos_y += 15
            if self.pos_y >= 400:
                self.jump = -1
        elif self.jump == -1:
            self.pos_y -= 15
            if self.pos_y <= 70:
                self.jump = 0
        else:
            self.pos_y = 70

    def check_collision_with_net(self):
        if Collision.collide(play_mode.pikachu, play_mode.net):
            self.pos_x = 350  # or any appropriate behavior

    def check_game_status(self):
        if play_mode.point.l_point == 2:
            self.set_game_result(win=True)
        elif play_mode.point.r_point == 2:
            self.set_game_result(win=False)

    def set_game_result(self, win):
        self.win = win
        self.lose = not win
        self.locate = 1 if win else 0
        self.frame2 = 5
        self.finish += 1
        self.sec = 0

    def draw(self):
        self.draw_pikachu()
        self.font.draw(self.pos_x, self.pos_y + 60, str(int(self.sec)), (255, 0, 255))

    def draw_pikachu(self):
        if not self.win and not self.lose:
            if self.locate:
                self.img.clip_draw(self.frame * 64, self.locate * 64, 64, 64, self.pos_x, self.pos_y, 100, 100)
            else:
                self.img.clip_draw(0, 320, 64, 64, self.pos_x, self.pos_y, 100, 100)
        elif self.win:
            self.img.clip_draw(self.frame * 64, self.locate * 64, 64, 64, self.pos_x, self.pos_y, 100, 100)
            delay(0.05)
        elif self.lose:
            self.img.clip_draw(256, self.locate * 64, 64, 64, self.pos_x, self.pos_y, 100, 100)
            delay(0.05)
        if self.finish == 50:
            game_framework.change_mode(end_mode)

    def get_bb(self):
        return self.pos_x - 10, self.pos_y - 30, self.pos_x + 40, self.pos_y + 40
