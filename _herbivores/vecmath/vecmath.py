from vecmath.Vec2D import Vec2D
import math
import random
import numpy as np


two_pi = math.pi * 2

def random_vector_2d(x_bound, y_bound):
    x = random.random() * x_bound
    y = random.random() * y_bound
    vector = Vec2D(x, y)
    return vector


def random_direction_vector():
    radians = random.random() * 2 * math.pi - math.pi
    x = math.cos(radians)
    y = math.sin(radians)
    vector = Vec2D(x, y)
    return vector


def wrapping_vector(origin, to, space_width, space_height):
    options_x = [to.x - space_width, to.x, to.x + space_width]
    distances_x = [option - origin.x for option in options_x]

    options_y = [to.y - space_height, to.y, to.y + space_height]
    distances_y = [option - origin.y for option in options_y]

    # Select the best options
    vector = Vec2D(distances_x[np.argmin(list(map(abs, distances_x)))],
                   distances_y[np.argmin(list(map(abs, distances_y)))])

    return vector


def wrapping_angle(origin, to):
    global two_pi
    to = to.as_radians()
    origin = origin.as_radians()
    nothing = to - origin
    minus = (to - two_pi) - origin
    if abs(minus) < abs(nothing):
        return minus
    plus = (to + two_pi) - origin
    if abs(plus) < abs(nothing):
        return plus
    return nothing

