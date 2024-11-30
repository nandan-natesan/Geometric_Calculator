from commands import parse_command, list_shapes

def geometric_calculator():
    shapes = {}

    print("Geomteric Calculator")
    print("For queries to create and calculate shapes type: help, to exit type: exit")

    while True:
        try:
            command = input("> ").strip()
            if command.lower() == "exit":
                print("Exit Success")
                break
            if command.lower() == "help":
                print("\nCommands:")
                print("Define a Point: <name> = Point(x, y)")
                print("Define a Line: <name> = Line(point1, point2){points must be predefined}")
                print("Define a Circle: <name> = Circle(center, radius){points must be predefined}")
                print("Define a Rectangle: <name> = Rectangle(bottom_left, top_right){points must be predefined}")
                print("Query Distance: point1.distance(point2)")
                print("Query Length: line.length()")
                print("Query Area: shape.area()")
                print("Query Perimeter/Circumference: shape.perimeter() or shape.circumference()")
                print("List all defined shapes and points: list")
                print("Type 'exit' to quit.\n")
                continue

            if command.lower() == "list":
                print(list_shapes(shapes))
                continue

            if "=" in command:
                print(parse_command(command, shapes))
            else:
                result = eval(command, {}, shapes)
                print(result)

        except Exception as e:
            print(f"Error: {e}. Type 'help' for guidance.")

if __name__ == "__main__":
    geometric_calculator()
