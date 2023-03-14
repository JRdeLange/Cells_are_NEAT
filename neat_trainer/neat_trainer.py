import neat
from world.world import World
import config
from renderer.renderer import Renderer


class NeatTrainer:

    def __init__(self, renderer):
        self.renderer = renderer

        neat_config_path = "./neat_config"
        self.neat_config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                       neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                       neat_config_path)

        self.population = neat.Population(self.neat_config)
        self.statistics = neat.StatisticsReporter()
        self.population.add_reporter(self.statistics)
        self.population.add_reporter(neat.Checkpointer(generation_interval=10, time_interval_seconds=None,
                                                       filename_prefix="testing-"))

        self.population = neat.Checkpointer.restore_checkpoint("./testing-19")
        self.train(101)

        self.render = config.render

    def train(self, generations):
        self.population.run(self.eval_genomes, generations)

    def eval_genomes(self, genomes, neat_config):
        print("generation", self.population.generation)
        self.render = False
        if self.population.generation % 1 == 0:
            self.render = True
        # Create and fill world
        world = World()
        world.populate_world(len(genomes))
        self.assign_genomes_and_nets(world, genomes, neat_config)

        if self.render:
            self.renderer.set_world(world)

        self.run_generation(world)

        if self.render:
            self.renderer.reset()

        self.assign_cell_fitnesses(world)

    def assign_genomes_and_nets(self, world, genomes, neat_config):
        for idx, cell in enumerate(world.cells):
            genome_id, genome = genomes[idx]
            net = neat.nn.FeedForwardNetwork.create(genome, neat_config)
            cell.genome = genome
            cell.net = net

    def run_generation(self, world):
        for step in range(config.steps_per_generation):
            world.tick()
            if self.render:
                self.renderer.tick()

    def assign_cell_fitnesses(self, world):
        total_eaten = 0
        for cell in world.cells + world.cell_archive:
            cell.genome.fitness = cell.plants_eaten
            total_eaten += cell.plants_eaten
        print("eaten plants:", total_eaten)
