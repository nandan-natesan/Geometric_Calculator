from commands import parse_command, list_shapes, calculate_distance

def geometric_calculator():
    shapes = {}

    print("Geomteric Calculator")
    print("For queries to create and calculate shapes type: help, to exit type:exit")

    while True:
        try:
            command = input("> ").strip()
            if command.lower() == "exit":
                print("Exit Success")
                break
            if command.lower() == "help":
                print("\nCommands:")
                print("Define a Point: <name> = Point(x, y)")
                print("Define a Line: <name> = Line(point1, point2)")
                print("Define a Circle: <name> = Circle(center, radius)")
                print("Define a Rectangle: <name> = Rectangle(bottom_left, top_right)")
                print("Query Distance: distance(shape1, shape2)")
                print("List all defined shapes and points: list")
                print("Type 'exit' to quit.\n")
                continue

            if command.lower() == "list":
                print(list_shapes(shapes))
                continue

            if command.lower().startswith("distance"):
                _, args = command.split("(", 1)
                shape1_name, shape2_name = args.strip()[:-1].split(",")
                shape1_name = shape1_name.strip()
                shape2_name = shape2_name.strip()
                print(calculate_distance(shape1_name, shape2_name, shapes))
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