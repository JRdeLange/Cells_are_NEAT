import vecmath.vecmath as vm
from cell.cell import Cell

class Spawner:

    def __init__(self, world):
        self.world = world

    def spawn_n_cells(self, n):
        for idx in range(n):
            self.spawn_cell()

    def spawn_cell(self):
        pos = vm.random_vector_2d(self.world.width, self.world.height)
        forward = vm.random_direction_vector()
        new_cell = Cell(pos, forward)
        self.world.cells.append(new_cell)
