from vecmath.Vec2D import Vec2D
import random
import math
import config


class Plant:

    def __init__(self, pos, forward, world):
        self.pos = pos
        self.forward = forward
        self.angle = random.random() * 2 * math.pi
        self.speed = config.plant_speed + random.random() * 0.2
        self.world = world

    def tick(self):
        self.move()

    def move(self):
        self.pos += (self.forward * self.speed)
        self.angle += config.plant_spin_speed
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

    def eaten(self):
        print("eaten!")
        self.world.plant_eaten(self)
