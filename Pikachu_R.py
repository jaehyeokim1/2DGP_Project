from pico2d import*
import Collision
import os
import play_mode

class pikachu_r:
    def __init__(self):
        self.pos_x = 650
        self.pos_y = 70
        self.frame = 0
        self.frame2 = 5
        self.img = load_image('Pikachu_R.png')
        self.dirx = 0
        self.diry = 0
        self.jump = 0
        self.locate = 0
        self.win = False
        self.lose = False
        self.q_jump = 0
        self.font = load_font('ENCR10B.TTF', 25)
        self.sec = 0

    def update(self):
        self.frame = (self.frame + 1) % self.frame2
        if self.sec < 10:
            self.sec += 0.03
        else:
            self.sec = 10
        if self.lose == False and self.win == False:
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
            if (Collision.collide(play_mode.pikachu2, play_mode.net)):
                play_mode.pikachu2.x = 450
        if (play_mode.point.l_point == 4):
            self.lose = True
            self.locate = 0
            self.frame2 = 5
            self.sec = 0
        elif (play_mode.point.r_point == 4):
            self.win = True
            self.locate = 1
            self.frame2 = 5
            self.sec = 0
        if self.pos_x >= 750:
            self.pos_x = 750
        elif self.pos_x <= 440:
            self.pos_x = 440
    def draw(self):
        if self.lose == False and self.win == False:
            if self.locate:
                self.img.clip_draw(self.frame * 64, self.locate * 64, 64, 64, self.pos_x, self.pos_y, 100, 100)
            else:
                self.img.clip_draw(0, 320, 64, 64, self.pos_x, self.pos_y, 100, 100)
        elif self.win == True:
            self.img.clip_draw(self.frame * 64, self.locate * 64, 64, 64, self.pos_x, self.pos_y, 100, 100)
            delay(0.05)
        elif self.lose == True:
            self.img.clip_draw(256, self.locate * 64, 64, 64, self.pos_x, self.pos_y, 100, 100)
            delay(0.05)
        self.font.draw(self.pos_x - 10, self.pos_y + 60, str(int(self.sec)), (255, 0, 255))
    def get_bb(self):
        return self.pos_x - 40, self.pos_y - 30, self.pos_x + 10, self.pos_y + 40