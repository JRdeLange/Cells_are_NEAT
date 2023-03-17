from world.spawner import Spawner
from world.sun_map import SunMap
from cells.herbivore import Herbivore
from cells.senses import PlantInfo
import config

class World:

    def __init__(self):
        # Properties
        self.width = config.world_width
        self.height = config.world_height

        # Things to own
        self.spawner = Spawner(self)
        self.cells = []
        self.cell_archive = []
        self.plants = []
        # self.sun_map = SunMap()

        self.closest_plant_dict = {}

        # Initialize
        # self.populate_world()

    def populate_world(self, n_cells=config.nr_of_cells):
        self.spawner.spawn_n_cells(n_cells)
        self.spawner.spawn_n_plants(config.nr_of_plants)

    def tick(self):
        self.fill_closest_plant_dict()

        # Everyone acts
        for plant in self.plants:
            plant.tick()

        for cell in self.cells:
            cell.tick()

        # Dead cells are removed
        for cell in self.cells:
            if not cell.alive:
                cell.die()
                self.cell_archive.append(cell)
                self.cells.remove(cell)

    def cell_died(self, cell):
        self.cell_archive.append(cell)
        self.cells.remove(cell)

    def plant_eaten(self, plant):
        self.plants.remove(plant)
        self.spawner.spawn_plant()

    def fill_closest_plant_dict(self):
        self.closest_plant_dict = {}
        for cell in self.cells:
            min_distance = self.width
            closest_vector = None
            closest_plant = None
            for plant in self.plants:
                vector = cell.pos.wrapping_vector_to(plant.pos, self.width, self.height)
                if vector.length() < min_distance:
                    min_distance = vector.length()
                    closest_vector = vector
                    closest_plant = plant

            self.closest_plant_dict[cell] = PlantInfo(closest_plant, closest_vector)
