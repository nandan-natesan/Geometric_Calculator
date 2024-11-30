import math

# Classes for shapes
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

#To input a point
def input_point():
    name = input("Enter name for the point: ").strip()
    x = float(input(f"Enter x-coordinate for point {name}: "))
    y = float(input(f"Enter y-coordinate for point {name}: "))
    return Point(name, x, y)

def input_line(points):
    name = input("Enter name for the line: ").strip()
    p1_name = input("Enter the name of the first point of the line: ").strip()
    p2_name = input("Enter the name of the second point of the line: ").strip()
    if p1_name in points and p2_name in points:
        return Line(name, points[p1_name], points[p2_name])
    else:
        print("One or both points not found.")
        return None

def input_circle():
    name = input("Enter name for the circle: ").strip()
    center_name = input("Enter name for the center point of the circle: ").strip()
    x = float(input(f"Enter x-coordinate for point {center_name}: "))
    y = float(input(f"Enter y-coordinate for point {center_name}: "))
    radius = float(input("Enter the radius of the circle: "))
    center = Point(center_name, x, y)
    return Circle(name, center, radius)

def input_rectangle(points):
    name = input("Enter name for the rectangle: ").strip()
    bl_name = input("Enter the name of the bottom-left point of the rectangle: ").strip()
    tr_name = input("Enter the name of the top-right point of the rectangle: ").strip()
    if bl_name in points and tr_name in points:
        return Rectangle(name, points[bl_name], points[tr_name])
    else:
        print("One or both points not found.")
        return None

def geometric_calculator():
    points = {}
    shapes = {}
    print("Welcome to the Geometric Calculator!")

    # Input shapes
    while True:
        print("\nWhat shape would you like to input?")
        print("1. Point")
        print("2. Line")
        print("3. Circle")
        print("4. Rectangle")
        print("5. Done entering shapes")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            point = input_point()
            points[point.name] = point
            print(f"Point {point} recorded.")
        elif choice == '2':
            if len(points) < 2:
                print("You need at least two points to define a line.")
                continue
            line = input_line(points)
            if line:
                shapes[line.name] = line
                print(f"Line {line} recorded.")
        elif choice == '3':
            circle = input_circle()
            shapes[circle.name] = circle
            print(f"Circle {circle} recorded.")
        elif choice == '4':
            if len(points) < 2:
                print("You need at least two points to define a rectangle.")
                continue
            rectangle = input_rectangle(points)
            if rectangle:
                shapes[rectangle.name] = rectangle
                print(f"Rectangle {rectangle} recorded.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Calculate distance between two points")
        print("2. Calculate length of a line")
        print("3. Calculate area of a shape")
        print("4. Calculate perimeter/circumference of a shape")
        print("5. Exit")
        action = input("Enter your choice (1-5): ").strip()
        if action == '1':
            if len(points) < 2:
                print("Not enough points to calculate distance.")
                continue
            p1_name = input("Enter the name of the first point: ").strip()
            p2_name = input("Enter the name of the second point: ").strip()
            if p1_name in points and p2_name in points:
                distance = points[p1_name].distance(points[p2_name])
                print(f"Distance between {p1_name} and {p2_name} is {distance}")
            else:
                print("One or both points not found.")
        elif action == '2':
            if not any(isinstance(s, Line) for s in shapes.values()):
                print("No lines available to calculate length.")
                continue
            line_name = input("Enter the name of the line: ").strip()
            if line_name in shapes and isinstance(shapes[line_name], Line):
                length = shapes[line_name].length()
                print(f"Length of line {line_name} is {length}")
            else:
                print("Line not found.")
        elif action == '3':
            if not shapes:
                print("No shapes available to calculate area.")
                continue
            shape_name = input("Enter the name of the shape: ").strip()
            if shape_name in shapes:
                shape = shapes[shape_name]
                if isinstance(shape, Circle):
                    area = shape.area()
                    print(f"Area of circle {shape_name} is {area}")
                elif isinstance(shape, Rectangle):
                    area = shape.area()
                    print(f"Area of rectangle {shape_name} is {area}")
                else:
                    print("Area calculation not supported for this shape.")
            else:
                print("Shape not found.")
        elif action == '4':
            if not shapes:
                print("No shapes available to calculate perimeter/circumference.")
                continue
            shape_name = input("Enter the name of the shape: ").strip()
            if shape_name in shapes:
                shape = shapes[shape_name]
                if isinstance(shape, Circle):
                    circumference = shape.circumference()
                    print(f"Circumference of circle {shape_name} is {circumference}")
                elif isinstance(shape, Rectangle):
                    perimeter = shape.perimeter()
                    print(f"Perimeter of rectangle {shape_name} is {perimeter}")
                elif isinstance(shape, Line):
                    length = shape.length()
                    print(f"Length of line {shape_name} is {length}")
                else:
                    print("Perimeter calculation not supported for this shape.")
            else:
                print("Shape not found.")
        elif action == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    geometric_calculator()
