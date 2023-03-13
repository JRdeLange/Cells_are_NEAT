from world.world import World
from renderer.renderer import Renderer

def main():
    world = World()
    renderer = Renderer(world)
    print(renderer.window)

    while True:
        world.tick()
        renderer.tick()




if __name__ == "__main__":
    main()
