import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
from vecmath.vecmath import Vec2D
import config
import numpy as np

class SunMap:

    def __init__(self):
        self.noise = PerlinNoise(octaves=3, seed=1)
        self.scale = 10
        self.width = int(config.world_width / self.scale)
        self.height = int(config.world_height / self.scale)
        self.map = [[0] * self.height for x in range(self.width)]
        self.fill_map()
        self.image_of_map = self.as_image()

    def fill_map(self):
        for x in range(self.width):
            for y in range(self.height):
                # Noise is from -0.5 to 0.5, we want it from 0 to 1
                self.map[x][y] = self.noise([x / self.width, y / self.height]) + 0.5

    def plot_map(self):
        plt.imshow(self.map, cmap='gray')
        plt.show()

    def value_at(self, pos: Vec2D):
        return self.image_of_map[int(pos.x / self.scale)][int(pos.y / self.scale)][0] / 255

    def as_image(self):
        image = [[0] * self.height for x in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                value = self.map[x][y]
                image[x][y] = [value * 255, value * 255, value * 255]
        return np.array(image)
