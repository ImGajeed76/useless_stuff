import math


class Vec2:
    x = 0
    y = 0

    def __init__(self, x: int or float, y: int or float):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vec2(self.x / other.x, self.y / other.y)

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def set_magnitude(self, magnitude):
        return self.normalize() * Vec2(magnitude, magnitude)

    def normalize(self):
        return self / Vec2(self.magnitude(), self.magnitude())

    def direction(self):
        return Vec2(self.x / self.magnitude(), self.y / self.magnitude())

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def angle(self, other):
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def rotate(self, angle):
        return Vec2(self.x * math.cos(angle) - self.y * math.sin(angle),
                    self.x * math.sin(angle) + self.y * math.cos(angle))

    def lerp(self, other, t):
        return self + (other - self) * Vec2(t, t)

    def distance(self, other):
        return (self - other).magnitude()

    def angle_between(self, other):
        return math.atan2(other.y - self.y, other.x - self.x)

    def angle_to(self, other):
        return math.atan2(other.y - self.y, other.x - self.x)

    def angle_from(self, other):
        return math.atan2(self.y - other.y, self.x - other.x)
