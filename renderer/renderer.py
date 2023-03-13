import pygame
from pygame_toolkit.pygame_toolkit import PygameToolkit
from vecmath.Vec2D import Vec2D
import config

class Renderer:

    def __init__(self, world):
        pygame.init()
        self.world = world

        title = "Cells are NEAT"
        self.tk = PygameToolkit()
        self.window, self.clock = self.tk.init_pygame(config.window_height, config.window_width, title)

    def set_world(self, world):
        self.world = world
        self.cache_sprites()

    def tick(self):
        self.tk.clear(color=[100, 100, 170])
        self.draw()
        pygame.display.flip()
        self.clock.tick(60)

    def draw(self):
        self.draw_sun_map()
        self.draw_cells()

    def draw_sun_map(self):
        self.tk.render_sprite("sun_map", Vec2D(0, 0), centered=True)

    def draw_cells(self):
        for cell in self.world.cells:
            self.tk.render_sprite("cell", cell.pos, cell.forward.as_degrees())

    def cache_sprites(self):
        self.tk.add_sprite("cell", path="./sprites/cell.png")

        sun_map = pygame.surfarray.make_surface(self.world.sun_map.as_image())
        sun_map = pygame.transform.scale_by(sun_map, [self.world.sun_map.scale, self.world.sun_map.scale])
        sun_map.set_alpha(config.sun_map_alpha)
        self.tk.add_sprite("sun_map", surface=sun_map)

    # Remove all generation-specific things
    def reset(self):
        self.tk.reset()
        self.world = None
