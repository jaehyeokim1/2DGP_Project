from pico2d import *
import game_framework
import title_mode
import Ball
class map:
    def __init__(self):
        self.image = load_image('map.png')


    def draw(self):
        self.image.draw(400, 300)


    def update(self):
        pass
class NetBottom:
    def __init__(self):
        self.net = load_image('NetBottom.png')
        self.pos_x = 400
        self.pos_y = 120
    def draw(self):
        self.net.draw(self.pos_x, self.pos_y)
    def update(self):
        pass
    def get_bb(self):
        return self.pos_x - 5, self.pos_y - 110, self.pos_x + 5, self.pos_y + 110

class NetTop:
    def __init__(self):
        self.net = load_image('NetTop.png')
        self.pos_x = 400
        self.pos_y = 250
    def draw(self):
        self.net.draw(self.pos_x, self.pos_y)
    def update(self):
        pass
    def get_bb(self):
        return self.pos_x - 18, self.pos_y - 15, self.pos_x + 18, self.pos_y + 15