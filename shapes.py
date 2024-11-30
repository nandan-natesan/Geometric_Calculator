import math

class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance(self, other):
        if not isinstance(other, Point):
            raise ValueError("Distance can only be calculated between two Points.")
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"{self.name}({self.x}, {self.y})"

class Line:
    def __init__(self, name, p1, p2):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise ValueError("A line must be defined by two Points.")
        self.name = name
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance(self.p2)

    def __repr__(self):
        return f"{self.name}[{self.p1}, {self.p2}]"

class Circle:
    def __init__(self, name, center, radius):
        if not isinstance(center, Point) or not isinstance(radius, (int, float)):
            raise ValueError("Circle must have a Point center and a numeric radius.")
        self.name = name
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"{self.name}[Center: {self.center}, Radius: {self.radius}]"

class Rectangle:
    def __init__(self, name, bottom_left, top_right):
        if not (isinstance(bottom_left, Point) and isinstance(top_right, Point)):
            raise ValueError("Rectangle must be defined by two Points.")
        self.name = name
        self.bottom_left = bottom_left
        self.top_right = top_right

    def area(self):
        width = abs(self.top_right.x - self.bottom_left.x)
        height = abs(self.top_right.y - self.bottom_left.y)
        return width * height

    def perimeter(self):
        width = abs(self.top_right.x - self.bottom_left.x)
        height = abs(self.top_right.y - self.bottom_left.y)
        return 2 * (width + height)

    def __repr__(self):
        return f"{self.name}[{self.bottom_left}, {self.top_right}]"
