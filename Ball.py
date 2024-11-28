import Collision
from pico2d import *
import play_mode
import game_world

class Ball:
    def __init__(self):
       self.image = load_image('ball.png')
       self.frame = 0
       self.x = 150
       self.y = 500
       self.tx = 0
       self.ty = 6
       self.speed_y = 6
       self.touch = load_wav('touch.wav')
       self.spike = load_wav('spike.wav')

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def draw(self):
        self.image.clip_draw(self.frame * 40, 0, 40, 40, self.x, self.y, 50, 50)

    def update(self):
        if game_world.objects[1][0].win == True or game_world.objects[1][0].lose == True:
            game_world.remove_object(self)
        self.frame = (self.frame + 1) % 5
        if play_mode.pikachu.z == 1:
            if (Collision.collide(self, play_mode.pikachu)):
                    self.speed_y = 20
                    self.tx = 5
                    self.ty = self.speed_y
                    self.touch.play(1)
                    self.touch.set_volume(40)

                    if(play_mode.pikachu.jump == 1):
                        self.speed_y = 30
                        self.tx = 23
                        self.ty = self.speed_y
                        if(play_mode.pikachu.locate == 6):
                            self.speed_y = 40
                            self.tx = 40
                            self.ty = self.speed_y
                            self.spike.play(1)
                            self.spike.set_volume(60)
            if (Collision.collide(self, play_mode.pikachu2)):
                    self.speed_y = 20
                    self.tx = -5
                    self.ty = self.speed_y
                    self.touch.play(1)
                    self.touch.set_volume(40)

                    if(play_mode.pikachu2.jump == 1):
                        self.speed_y = 30
                        self.tx = -23
                        self.ty = self.speed_y
                        if (play_mode.pikachu2.locate == 6):
                            self.speed_y = 40
                            self.tx = -40
                            self.ty = self.speed_y
                            self.spike.play(1)
                            self.spike.set_volume(60)

        if (Collision.collide(self, play_mode.netTop)):
            self.tx = -self.tx
            self.ty = 5

        if (Collision.collide(self, play_mode.net)):
            self.tx = -self.tx
            self.ty = -16

        if self.x <= 50 or self.x >= 750:
            self.tx = -self.tx
        if self.y < 40:
            self.ty = self.speed_y
            self.speed_y -= 2
        else:
            self.ty -= 0.5
        if self.y >= 580:
            self.ty = -self.ty
        self.x += self.tx
        self.y += self.ty

