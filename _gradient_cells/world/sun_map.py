import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
from vecmath.vecmath import Vec2D
import config
import numpy as np

class SunMap:

    def __init__(self):
        self.scale = config.sun_map_scale
        self.width = int(config.world_width / self.scale)
        self.height = int(config.world_height / self.scale)
        self.map = [[0] * self.height for x in range(self.width)]

        if config.sun_map_type == "perlin":
            self.noise = PerlinNoise(octaves=3, seed=1)
            self.fill_map_with_perlin()
        elif config.sun_map_type == "blobs":
            self.place_blob(Vec2D(self.width / 2, self.height / 2), self.height / 3)
        else:
            raise ValueError("Provided invalid sun map type")

        self.image_of_map = self.as_image()

    def fill_map_with_perlin(self):
        for x in range(self.width):
            for y in range(self.height):
                # Noise is from -0.5 to 0.5, we want it from 0 to 1
                self.map[x][y] = self.noise([x / self.width, y / self.height]) + 0.5
                # Threshold
                self.map[x][y] *= self.map[x][y] + 0.2
                if self.map[x][y] < config.sun_map_threshold:
                    self.map[x][y] = 0

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

    def place_blob(self, pos, radius):
        for x in range(self.width):
            for y in range(self.height):
                current = Vec2D(x, y)
                dist = (pos - current).length()
                value = (radius - dist) / radius
                if value > 0:
                    self.map[x][y] = value
                # Threshold
                if self.map[x][y] < config.sun_map_threshold:
                    self.map[x][y] = 0

