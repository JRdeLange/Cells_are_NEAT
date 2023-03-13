import pygame
from vecmath.Vec2D import Vec2D

class PygameToolkit:

    def __init__(self):
        pygame.init()

        self.window = None

        self.cached_sprites = {}

    def init_pygame(self, height, width, title):
        pygame.init()
        window = pygame.display.set_mode([width, height])
        self.window = window
        pygame.display.set_caption(title)
        clock = pygame.time.Clock()

        return window, clock

    def set_window(self, window):
        self.window = window

    def clear(self, color=(255, 255, 255)):
        self.window.fill(color)

    def add_sprite(self, name, path=None, surface=None):
        if path:
            sprite = pygame.image.load(path)
            self.cached_sprites[name] = sprite
        elif surface:
            self.cached_sprites[name] = surface

    def render_sprite(self, sprite_name, pos: Vec2D, angle=0, size=Vec2D(1, 1), centered=False):
        try:
            sprite = self.cached_sprites[sprite_name]
        except KeyError:
            print("Tried to access cached sprite with name \"" + sprite_name + "\" but it does not exist.")
            return

        transformed = pygame.transform.scale_by(sprite, size.as_tuple())
        transformed = pygame.transform.rotate(transformed, -angle)

        if not centered:
            pos = pos - Vec2D(transformed.get_width(), transformed.get_height()) / 2

        self.window.blit(transformed, pos.as_tuple())

