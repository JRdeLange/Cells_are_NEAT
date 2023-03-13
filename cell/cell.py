import vecmath.vecmath as vm
from vecmath.Vec2D import Vec2D
import config

class Cell:

    def __init__(self, pos: Vec2D, forward: Vec2D, world, genome, net):
        self.world = world
        self.genome = genome
        self.net = net

        self.pos = pos
        self.forward = forward
        self.velocity = 0

        self.energy = config.starting_energy
        self.metabolism = config.metabolism
        self.swim_strength = config.swim_strength

        self.age = 0
        self.alive = True

    def rotate_by(self, rad):
        self.forward.rotate_by(rad)

    def tick(self):
        self.age += 1

        self.move()
        self.photosynthesize()
        self.metabolize()

    def photosynthesize(self):
        sun_strength = self.world.sun_map.value_at(self.pos)
        self.energy += sun_strength

    def metabolize(self):
        self.energy -= self.metabolism
        print(self.energy)
        if self.energy <= 0:
            self.alive = False

    def die(self):
        pass

    def move(self):
        self.velocity *= config.friction

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
