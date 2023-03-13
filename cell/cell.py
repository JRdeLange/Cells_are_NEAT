import vecmath.vecmath as vm
from vecmath.Vec2D import Vec2D
import config

class Cell:

    def __init__(self, pos: Vec2D, forward: Vec2D):
        self.pos = pos
        self.forward = forward
        self.velocity = 0

        self.energy = 100
        self.swim_strength = config.swim_strength

        self.count = 0



    def rotate_by(self, rad):
        self.forward.rotate_by(rad)

    def move(self):
        self.count += 1

        self.rotate_by(0.01)
        if self.count > 100 and self.count < 400:
            self.velocity += self.forward * self.swim_strength
        self.pos += self.velocity
        self.wrap_position()

    def wrap_position(self):
        if self.pos.x > config.world_width:
            self.pos.x -= config.world_width
        if self.pos.x < 0:
            self.pos.x += config.world_width

        if self.pos.y > config.world_height:
            self.pos.y -= config.world_height
        if self.pos.y < 0:
            self.pos.y += config.world_height
