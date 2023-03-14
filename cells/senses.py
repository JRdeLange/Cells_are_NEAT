from vecmath.Vec2D import Vec2D
import math


def sense_sunlight(cell):
    probe_radians = [-math.pi / 4, 0, math.pi / 4]
    probes = [cell.forward.rotated_by(rad) for rad in probe_radians]
    for idx, probe in enumerate(probes):
        probes[idx] = probe * cell.sunlight_probe_length

    observation = []
    for probe in probes:
        probe_pos = cell.pos + probe
        value = cell.world.sun_map.value_at(probe_pos.wrapped(x_max=cell.world.width, y_max=cell.world.height))
        observation.append(value)

    return observation


def closest_plant(cell):
    return cell.world.closest_plant_dict[cell]


class PlantInfo:

    def __init__(self, plant, vector):
        self.plant = plant
        self.vector = vector
