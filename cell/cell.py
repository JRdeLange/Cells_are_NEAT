import vecmath.vecmath as vm
from vecmath.Vec2D import Vec2D
import config
import cell.senses as senses
import random


class Cell:

    def __init__(self, pos: Vec2D, forward: Vec2D, world):
        self.world = world
        self.genome = None
        self.net = None

        self.pos = pos
        self.forward = forward
        self.velocity = 0

        self.energy = config.starting_energy
        self.metabolism = config.metabolism
        self.swim_strength = config.swim_strength
        self.sunlight_probe_length = config.sunlight_probe_length

        self.age = 0
        self.alive = True

        self.action_dict = config.radian_dict

    def set_genome_and_net(self, genome, net):
        self.genome = genome
        self.net = net

    def rotate_by(self, rad):
        self.forward = self.forward.rotated_by(rad)

    def tick(self):
        self.age += 1

        observation = senses.sense_sunlight(self)
        observation.insert(0, 1.0)

        output = self.net.activate(observation)
        turn = output[0:2]
        swim = output[3] > config.act_threshold
        turn = self.max_action(turn)
        self.rotate_by(turn)

        self.move(swim)
        self.photosynthesize()
        self.metabolize()

    def max_action(self, output):
        highest = None
        action = []
        for idx, value in enumerate(output):
            if highest is None or value > highest:
                highest = value
                action = [self.action_dict[idx]]
            if value == highest:
                action.append(self.action_dict[idx])
        return random.choice(action)

    def photosynthesize(self):
        sun_strength = self.world.sun_map.value_at(self.pos)
        self.energy += sun_strength

    def metabolize(self):
        self.energy -= self.metabolism
        #if self.energy <= 0:
        #    self.alive = False

    def die(self):
        pass

    def move(self, swim):
        self.velocity *= config.friction

        if swim:
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
