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

    def distance_to(self, other):
        if isinstance(other, Point):
            return self.distance(other)
        elif isinstance(other, Circle):
            return max(0, self.distance(other.center) - other.radius)
        elif isinstance(other, Line):
            line_dist = abs((other.p2.y - other.p1.y) * self.x - (other.p2.x - other.p1.x) * self.y +
                            other.p2.x * other.p1.y - other.p2.y * other.p1.x) / other.length()
            return line_dist
        elif isinstance(other, Rectangle):
            x_dist = max(0, other.bottom_left.x - self.x, self.x - other.top_right.x)
            y_dist = max(0, other.bottom_left.y - self.y, self.y - other.top_right.y)
            return math.hypot(x_dist, y_dist)
        else:
            raise ValueError("Unsupported shape combination for distance calculation.")

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

    def is_parallel_to(self, other):
        dx1 = self.p2.x - self.p1.x
        dy1 = self.p2.y - self.p1.y
        dx2 = other.p2.x - other.p1.x
        dy2 = other.p2.y - other.p1.y
        return dx1 * dy2 == dx2 * dy1

    def distance_to(self, other):
        if isinstance(other, Point):
            return other.distance_to(self)
        elif isinstance(other, Circle):
            d1 = self.p1.distance_to(other)
            d2 = self.p2.distance_to(other)
            return min(d1, d2)
        elif isinstance(other, Rectangle):
            return min(self.p1.distance_to(other), self.p2.distance_to(other))
        elif isinstance(other, Line):
            if self.is_parallel_to(other):
                return abs((other.p2.y - other.p1.y) * self.p1.x - (other.p2.x - other.p1.x) * self.p1.y +
                           other.p2.x * other.p1.y - other.p2.y * other.p1.x) / other.length()
            elif self.p1.distance_to(other.p1) == 0 and self.p2.distance_to(other.p2) == 0:
                return 0  # Identical lines
            else:
                return 0  # Intersecting lines
        else:
            raise ValueError("Unsupported shape combination for distance calculation.")

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

    def distance_to(self, other):
        if isinstance(other, Point):
            return other.distance_to(self)
        elif isinstance(other, Circle):
            center_dist = self.center.distance(other.center)
            return max(0, center_dist - self.radius - other.radius)
        elif isinstance(other, Line):
            return other.distance_to(self)
        elif isinstance(other, Rectangle):
            return max(0, self.center.distance_to(other) - self.radius)
        else:
            raise ValueError("Unsupported shape combination for distance calculation.")

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

    def distance_to(self, other):
        if isinstance(other, Point):
            return other.distance_to(self)
        elif isinstance(other, Circle):
            return other.distance_to(self)
        elif isinstance(other, Line):
            return min(other.p1.distance_to(self), other.p2.distance_to(self))
        elif isinstance(other, Rectangle):
            x_dist = max(0, other.bottom_left.x - self.top_right.x, self.bottom_left.x - other.top_right.x)
            y_dist = max(0, other.bottom_left.y - self.top_right.y, self.bottom_left.y - other.top_right.y)
            return math.hypot(x_dist, y_dist)
        else:
            raise ValueError("Unsupported shape combination for distance calculation.")

    def __repr__(self):
        return f"{self.name}[{self.bottom_left}, {self.top_right}]"
