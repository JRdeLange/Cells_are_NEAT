from world.spawner import Spawner
from world.sun_map import SunMap
from cell.cell import Cell
import config

class World:

    def __init__(self):
        # Properties
        self.width = config.world_width
        self.height = config.world_height

        # Things to own
        self.spawner = Spawner(self)
        self.cells = []
        self.sun_map = SunMap()

        # Initialize
        self.populate_world()

    def populate_world(self):
        self.spawner.spawn_n_cells(config.nr_of_cells)

    def tick(self):
        # Everyone acts
        for cell in self.cells:
            cell.tick()

        # Dead cells are removed
        for cell in self.cells:
            if not cell.alive:
                cell.die()
                self.cells.remove(cell)

    def move_cells(self):
        for cell in self.cells:
            cell.move()
            cell.metabolize()

            # Apply friction
            cell.velocity *= config.friction
