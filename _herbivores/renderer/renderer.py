import pygame
from pygame_toolkit.pygame_toolkit import PygameToolkit
from vecmath.Vec2D import Vec2D
import numpy as np
import config

class Renderer:

    def __init__(self, world=None):
        pygame.init()
        self.world = world

        title = "Cells are NEAT"
        self.tk = PygameToolkit()
        self.window, self.clock = self.tk.init_pygame(config.window_height, config.window_width, title)

    def set_world(self, world):
        self.world = world
        self.cache_sprites()

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        self.tk.clear(color=[100, 100, 170])
        self.draw()
        pygame.display.flip()
        self.clock.tick(60)

    def draw(self):
        # self.draw_sun_map()
        self.draw_plants()
        self.draw_cells()

    def draw_sun_map(self):
        self.tk.render_sprite("sun_map", Vec2D(0, 0), centered=True)

    def draw_cells(self):
        for cell in self.world.cells:
            fatness = 1 + cell.plants_eaten / 6
            self.tk.render_sprite("cell", cell.pos, cell.forward.as_degrees(), size=Vec2D(fatness, fatness))

    def draw_plants(self):
        for plant in self.world.plants:
            self.tk.render_sprite("plant", plant.pos, np.degrees(plant.angle))

    def cache_sprites(self):
        self.tk.add_sprite("cell", path="./sprites/cell.png", size=Vec2D(1, 1))

        self.tk.add_sprite("plant", path="./sprites/plant.png", size=Vec2D(1.5, 1.5))

    # Remove all generation-specific things
    def reset(self):
        self.tk.reset()
        self.world = None
