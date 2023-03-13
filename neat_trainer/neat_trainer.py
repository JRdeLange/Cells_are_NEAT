import neat


class NeatTrainer:

    def __init__(self):
        neat_config_path = "./neat_config"
        self.neat_config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                       neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                       neat_config_path)
