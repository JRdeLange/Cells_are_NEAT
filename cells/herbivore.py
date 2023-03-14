import vecmath.vecmath as vm
from vecmath.Vec2D import Vec2D
import config
import cells.senses as senses
import random


class Herbivore:

    def __init__(self, pos: Vec2D, forward: Vec2D, world):
        self.world = world
        self.genome = None
        self.net = None

        self.pos = pos
        self.forward = forward
        self.velocity = 0

        self.swim_strength = config.swim_strength
        self.sunlight_probe_length = config.sunlight_probe_length

        self.plants_eaten = 0
        self.alive = True

        self.action_dict = config.radian_dict

        self.closest_food_info = None

    def set_genome_and_net(self, genome, net):
        self.genome = genome
        self.net = net

    def rotate_by(self, rad):
        self.forward = self.forward.rotated_by(rad)

    def tick(self):
        self.closest_food_info = senses.closest_plant(self)
        angle_to_food = self.forward.angle_to(self.closest_food_info.vector)
        distance_to_food = self.closest_food_info.vector.length()
        observation = [1.0, angle_to_food, distance_to_food]

        output = self.net.activate(observation)
        turn = output[0:2]
        swim = output[3] > config.act_threshold

        turn = self.max_action(turn)
        self.rotate_by(turn)

        self.eat()
        self.move(swim)

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

    def eat(self):
        if self.closest_food_info.vector.length() < config.eating_distance:
            if not self.closest_food_info.plant.already_eaten:
                self.plants_eaten += 1
                self.closest_food_info.plant.eaten()

    def die(self):
        self.world.cell_died(self)

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
