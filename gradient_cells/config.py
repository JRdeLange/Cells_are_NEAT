from vecmath.Vec2D import Vec2D

# Trainer
neat_config_path = "./neat_config"
steps_per_generation = 2500

# Renderer
window_width = 1200
window_height = 800
sun_map_alpha = 100
render = True

# World
world_width = window_width
world_height = window_height
nr_of_cells = 1
friction = 0.97
# "perlin" / "blobs"
sun_map_type = "perlin"
sun_map_scale = 10
sun_map_threshold = 0.3

# Cells
starting_energy = 50
metabolism = 0.5
swim_strength = 0.05
sunlight_probe_length = 25
act_threshold = 0.8
radian_dict = {0: -0.04,
               1: 0,
               2: 0.04,
               3: "swim"}
direction_dict = {0: Vec2D(1, 0),
                  1: Vec2D(0, 1),
                  2: Vec2D(-1, 0),
                  3: Vec2D(0, -1)}
