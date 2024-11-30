from commands import parse_command, list_shapes

def geometric_calculator():
    shapes = {}

    print("Geometric Calculator")
    print("For queries to create and calculate shapes type: help, to exit type: exit")

    while True:
        try:
            command = input("> ").strip()
            if command.lower() == "exit":
                print("Exiting the calculator. Goodbye!")
                break
            elif command.lower() == "help":
                print("\nCommands:")
                print("Define a Point: <name> = Point(x, y)")
                print("Define a Line: <name> = Line(point1, point2)")
                print("Define a Circle: <name> = Circle(center, radius)")
                print("Define a Rectangle: <name> = Rectangle(point1, point2, point3, point4)")
                print("Query Distance: distance(shape1, shape2)")
                print("Query Area of Circle/Rectangle: <shape>.area()")
                print("Query Perimeter of Rectangle: <shape>.perimeter()")
                print("Query Circumference of Circle: <shape>.circumference()")
                print("Query Length of Line: <line>.length()")
                print("List all defined shapes and points: list")
                print("Type 'exit' to quit.\n")
            elif command.lower() == "list":
                list_shapes(shapes)
            else:
                parse_command(command, shapes)
        except Exception as e:
            print(f"Error: {e}. Type 'help' for guidance.")

if __name__ == "__main__":
    geometric_calculator()
