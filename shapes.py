import math

class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance_to(self, other):
        if isinstance(other, Point):
            return math.hypot(self.x - other.x, self.y - other.y)
        elif isinstance(other, Circle):
            return max(0, self.distance_to(other.center) - other.radius)
        elif isinstance(other, Line):
            line_dist = abs((other.p2.y - other.p1.y) * self.x - (other.p2.x - other.p1.x) * self.y +
                            other.p2.x * other.p1.y - other.p2.y * other.p1.x) / other.length()
            return line_dist
        elif isinstance(other, Rectangle):
            return other.distance_to(self)
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
        return self.p1.distance_to(self.p2)

    def distance_to(self, other):
        if isinstance(other, Point):
            return other.distance_to(self)
        elif isinstance(other, Line):
            if self.is_parallel_to(other):
                return abs((other.p2.y - other.p1.y) * self.p1.x - (other.p2.x - other.p1.x) * self.p1.y +
                           other.p2.x * other.p1.y - other.p2.y * other.p1.x) / other.length()
            elif self._lines_intersect(other):
                return 0
            else:
                return min(
                    self.p1.distance_to(other), self.p2.distance_to(other),
                    other.p1.distance_to(self), other.p2.distance_to(self)
                )
        elif isinstance(other, Circle):
            return min(self.p1.distance_to(other), self.p2.distance_to(other))
        elif isinstance(other, Rectangle):
            return min(self.p1.distance_to(other), self.p2.distance_to(other))
        else:
            raise ValueError("Unsupported shape combination for distance calculation.")

    def is_parallel_to(self, other):
        dx1 = self.p2.x - self.p1.x
        dy1 = self.p2.y - self.p1.y
        dx2 = other.p2.x - other.p1.x
        dy2 = other.p2.y - other.p1.y
        return dx1 * dy2 == dx2 * dy1

    def _lines_intersect(self, other):
        def ccw(A, B, C):
            return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)
        return (ccw(self.p1, self.p2, other.p1) != ccw(self.p1, self.p2, other.p2) and
                ccw(other.p1, other.p2, self.p1) != ccw(other.p1, other.p2, self.p2))

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
            center_dist = self.center.distance_to(other.center)
            return max(0, center_dist - self.radius - other.radius)
        elif isinstance(other, Line):
            return other.distance_to(self)
        elif isinstance(other, Rectangle):
            x_dist = max(0, other.p1.x - self.center.x, self.center.x - other.p2.x)
            y_dist = max(0, other.p1.y - self.center.y, self.center.y - other.p3.y)
            return max(0, math.hypot(x_dist, y_dist) - self.radius)
        else:
            raise ValueError("Unsupported shape combination for distance calculation.")

    def __repr__(self):
        return f"{self.name}[Center: {self.center}, Radius: {self.radius}]"


class Rectangle:
    def __init__(self, name, p1, p2, p3, p4):
        if not all(isinstance(p, Point) for p in [p1, p2, p3, p4]):
            raise ValueError("Rectangle must be defined by four Points.")
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def area(self):
        return 0.5 * abs(
            self.p1.x * self.p2.y + self.p2.x * self.p3.y + self.p3.x * self.p4.y + self.p4.x * self.p1.y -
            (self.p2.x * self.p1.y + self.p3.x * self.p2.y + self.p4.x * self.p3.y + self.p1.x * self.p4.y)
        )

    def perimeter(self):
        return (
            self.p1.distance_to(self.p2)
            + self.p2.distance_to(self.p3)
            + self.p3.distance_to(self.p4)
            + self.p4.distance_to(self.p1)
        )

    def distance_to(self, other):
        if isinstance(other, Point):
            edges = [(self.p1, self.p2), (self.p2, self.p3), (self.p3, self.p4), (self.p4, self.p1)]
            return min(other.distance_to(Line("", edge[0], edge[1])) for edge in edges)
        elif isinstance(other, Circle):
            edges = [(self.p1, self.p2), (self.p2, self.p3), (self.p3, self.p4), (self.p4, self.p1)]
            return max(0, min(other.center.distance_to(Line("", edge[0], edge[1])) for edge in edges) - other.radius)
        elif isinstance(other, Rectangle):
            edges_self = [(self.p1, self.p2), (self.p2, self.p3), (self.p3, self.p4), (self.p4, self.p1)]
            edges_other = [(other.p1, other.p2), (other.p2, other.p3), (other.p3, other.p4), (other.p4, other.p1)]
            return min(Line("", edge1[0], edge1[1]).distance_to(Line("", edge2[0], edge2[1]))
                       for edge1 in edges_self for edge2 in edges_other)
        else:
            raise ValueError("Unsupported shape combination for distance calculation.")

    def __repr__(self):
        return f"{self.name}[{self.p1}, {self.p2}, {self.p3}, {self.p4}]"
