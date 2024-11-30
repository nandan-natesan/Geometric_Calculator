import math

#Classes for shapes
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

# Main REPL-based geometric calculator
def geometric_calculator():
    shapes = {}

    print("Geomteric Claculator")
    print("For commands to create and calculate shapes type: help, to exit type:exit")

    while True:
        try:
            command = input("> ").strip()
            if command.lower() == "exit":
                print("Exiting the calculator. Goodbye!")
                break
            if command.lower() == "help":
                print("\nCommands:")
                print("Define a Point: <name> = Point(x, y)")
                print("Define a Line: <name> = Line(point1, point2)")
                print("Define a Circle: <name> = Circle(center, radius)")
                print("Define a Rectangle: <name> = Rectangle(bottom_left, top_right)")
                print("Query Distance: point1.distance(point2)")
                print("Query Length: line.length()")
                print("Query Area: shape.area()")
                print("Query Perimeter/Circumference: shape.perimeter() or shape.circumference()")
                print("List all defined shapes and points: list")
                print("Type 'exit' to quit.\n")
                continue

            if command.lower() == "list":
                if not shapes:
                    print("No shapes or points defined yet.")
                else:
                    print("Defined shapes and points:")
                    for name, shape in shapes.items():
                        print(f"- {name}: {shape}")
                continue

            #Commands handling
            if "=" in command:
                name, expr = command.split("=")
                name = name.strip()
                expr = expr.strip()

                if expr.startswith("Point"):
                    x, y = eval(expr[6:-1])
                    shapes[name] = Point(name, x, y)
                    print(f"{name} defined as {shapes[name]}.")

                elif expr.startswith("Line"):
                    p1_name, p2_name = expr[5:-1].split(",")
                    p1 = shapes[p1_name.strip()]
                    p2 = shapes[p2_name.strip()]
                    shapes[name] = Line(name, p1, p2)
                    print(f"{name} defined as {shapes[name]}.")

                elif expr.startswith("Circle"):
                    center_name, radius = expr[7:-1].split(",")
                    center = shapes[center_name.strip()]
                    radius = float(radius.strip())
                    shapes[name] = Circle(name, center, radius)
                    print(f"{name} defined as {shapes[name]}.")

                elif expr.startswith("Rectangle"):
                    bl_name, tr_name = expr[10:-1].split(",")
                    bottom_left = shapes[bl_name.strip()]
                    top_right = shapes[tr_name.strip()]
                    shapes[name] = Rectangle(name, bottom_left, top_right)
                    print(f"{name} defined as {shapes[name]}.")

                else:
                    print("Invalid shape definition. Type 'help' for guidance.")

            else:
                #Query Evaluation
                result = eval(command, {}, shapes)
                print(result)

        except Exception as e:
            print(f"Error: {e}. Type 'help' for guidance.")

if __name__ == "__main__":
    geometric_calculator()
