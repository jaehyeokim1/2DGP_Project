from pico2d import *
import play_mode

class Point:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 75)
        self.l_point = 0
        self.r_point = 0

    def draw(self):
        self.font.draw(200, 550, str(self.l_point), (255, 0, 0))
        self.font.draw(600, 550, str(self.r_point), (255, 0, 0))

    def handle_point(self, is_left):
        if is_left:
            self.l_point += 1
            play_mode.ball.x, play_mode.ball.y = 650, 550
            print("L_bottom")
        else:
            self.r_point += 1
            play_mode.ball.x, play_mode.ball.y = 150, 550
            print("R_bottom")

        play_mode.pikachu2.x = 650
        play_mode.pikachu.x = 150
        play_mode.pikachu.jump = 0
        play_mode.pikachu2.jump = 0
        play_mode.ball.to_x = 0
        play_mode.ball.to_y = 0
        delay(1)

    def update(self):
        if play_mode.ball.x > 400 and play_mode.ball.y < 40:
            self.handle_point(is_left=True)
        elif play_mode.ball.x < 400 and play_mode.ball.y < 40:
            self.handle_point(is_left=False)
