import vecmath.vecmath
from world.world import World
from renderer.renderer import Renderer
from neat_trainer.neat_trainer import NeatTrainer
from vecmath.Vec2D import Vec2D
import math


def main():
    renderer = Renderer(None)
    trainer = NeatTrainer(renderer)

    # For debug
    if False:
        world = World()
        world.populate_world(1)
        renderer.set_world(world)
        while True:
            world.tick()
            renderer.tick()


if __name__ == "__main__":
    main()
