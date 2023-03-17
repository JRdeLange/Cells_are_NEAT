import toadally_neat
from world.world import World
import config
from renderer.renderer import Renderer


class NeatTrainer:

    def __init__(self, renderer):
        self.renderer = renderer

        neat_config_path = "./neat_config"
        self.neat_config = toadally_neat.Config(toadally_neat.DefaultGenome, toadally_neat.DefaultReproduction,
                                                toadally_neat.DefaultSpeciesSet, toadally_neat.DefaultStagnation,
                                                neat_config_path)

        self.population = toadally_neat.Population(self.neat_config)
        self.statistics = toadally_neat.StatisticsReporter()
        self.population.add_reporter(self.statistics)
        self.population.add_reporter(toadally_neat.Checkpointer(generation_interval=10, time_interval_seconds=None,
                                                       filename_prefix="testing-"))
        self.population.add_reporter(toadally_neat.StdOutReporter(True))

        self.population = toadally_neat.Checkpointer.restore_checkpoint("./testing-49")
        self.showcase_best = False
        self.train(101)

        self.render = config.render

    def train(self, generations):
        self.population.run(self.eval_genomes, generations)

    def eval_genomes(self, genomes, neat_config):
        self.render = False
        if self.population.generation == self.population.generation:
            self.render = True
            self.showcase_best = False
            config.steps_per_generation = 1000000
            config.nr_of_plants = 5
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
            if self.showcase_best:
                net = toadally_neat.nn.FeedForwardNetwork.create(self.population.best_genome, neat_config)
            else:
                net = toadally_neat.nn.FeedForwardNetwork.create(genome, neat_config)
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
