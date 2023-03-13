import math

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
        as_tuple = (self.x, self.y)
        return as_tuple

    def as_radians(self):
        return math.atan2(self.y, self.x)

    def as_degrees(self):
        return math.degrees(self.as_radians())

    def set_from_rad(self, rad):
        self.x = math.cos(rad)
        self.y = math.sin(rad)

    def rotate_by(self, rad):
        curr_rad = self.as_radians()
        self.set_from_rad(curr_rad + rad)

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
