import vecmath.vecmath as vm
from cells.herbivore import Herbivore
from cells.plant import Plant


class Spawner:

    def __init__(self, world):
        self.world = world

    def spawn_n_cells(self, n):
        for idx in range(n):
            self.spawn_cell()

    def spawn_cell(self):
        pos = vm.random_vector_2d(self.world.width, self.world.height)
        forward = vm.random_direction_vector()
        new_cell = Herbivore(pos, forward, self.world)
        self.world.cells.append(new_cell)

    def spawn_n_plants(self, n):
        for idx in range(n):
            self.spawn_plant()

    def spawn_plant(self):
        pos = vm.random_vector_2d(self.world.width, self.world.height)
        forward = vm.random_direction_vector()
        new_plant = Plant(pos, forward, self.world)
        self.world.plants.append(new_plant)

