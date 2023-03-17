import math
import vecmath.vecmath as vm


class Vec2D:

    def __init__(self, x=None, y=None, rad=None):
        self.x = None
        self.y = None
        if x is not None and y is not None:
            self.x = x
            self.y = y
        elif rad is not None:
            self.set_from_rad(rad)
        else:
            raise ValueError("Improper initialisation of Vec2D. Provide an x and y or a rad")

    def as_tuple(self):
        return self.x, self.y

    def as_list(self):
        return [self.x, self.y]

    def as_radians(self):
        return math.atan2(self.y, self.x)

    def as_degrees(self):
        return math.degrees(self.as_radians())

    def normalized(self):
        return self / self.length()

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def set_from_rad(self, rad):
        self.x = math.cos(rad)
        self.y = math.sin(rad)

    def rotated_by(self, rad):
        curr_rad = self.as_radians()
        return Vec2D(rad=curr_rad + rad)

    def wrapped(self, x_min=0, y_min=0, x_max=100, y_max=100):
        new = Vec2D(self.x, self.y)
        if new.x <= x_min:
            new.x += (x_max - x_min)
        elif new.x >= x_max:
            new.x -= (x_max - x_min)

        if new.y <= y_min:
            new.y += (y_max - y_min)
        elif new.y >= y_max:
            new.y -= (y_max - y_min)
        return new

    def angle_to(self, to):
        return vm.wrapping_angle(self, to)

    def wrapping_vector_to(self, to, space_width, space_height):
        return vm.wrapping_vector(self, to, space_width, space_height)

    # Redefine adding
    def __add__(self, other):
        if isinstance(other, Vec2D):
            return Vec2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vec2D(self.x + other, self.y + other)
        else:
            raise TypeError("Adding unsupported thing to Vec2D")

    def __radd__(self, other):
        return self.__add__(other)

    # Redefine subtraction
    def __sub__(self, other):
        if isinstance(other, Vec2D):
            return Vec2D(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vec2D(self.x - other, self.y - other)
        else:
            raise TypeError("Adding unsupported thing to Vec2D")

    def __rsub__(self, other):
        return self.__sub__(other)

    # Redefine multiplication
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vec2D(self.x * other, self.y * other)
        else:
            raise TypeError("Multiplying unsupported thing with Vec2D")

    def __rmul__(self, other):
        return self.__mul__(other)

    # Redefine division
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vec2D(self.x / other, self.y / other)
        else:
            raise TypeError("unsupported operand type(s) for /")

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    # Redefine str(), mostly for printing
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Redefine equals
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)