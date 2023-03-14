from vecmath.Vec2D import Vec2D
import math
import random

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

