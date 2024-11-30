from shapes import Point, Line, Circle, Rectangle

def parse_command(command, shapes):
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
            p1_name, p2_name, p3_name, p4_name = expr[10:-1].split(",")
            p1 = shapes[p1_name.strip()]
            p2 = shapes[p2_name.strip()]
            p3 = shapes[p3_name.strip()]
            p4 = shapes[p4_name.strip()]
            shapes[name] = Rectangle(name, p1, p2, p3, p4)
            print(f"{name} defined as {shapes[name]}.")

        else:
            print("Invalid shape definition. Type 'help' for guidance.")
    elif command.startswith("distance(") and command.endswith(")"):
        handle_distance_command(command, shapes)
    else:
        process_query(command, shapes)

def handle_distance_command(command, shapes):
    try:
        shape1_name, shape2_name = command[9:-1].split(",")
        shape1 = shapes[shape1_name.strip()]
        shape2 = shapes[shape2_name.strip()]
        result = shape1.distance_to(shape2)
        print(f"Distance between {shape1_name.strip()} and {shape2_name.strip()}: {result}")
    except Exception as e:
        print(f"Error: {e}. Type 'help' for guidance.")

def process_query(command, shapes):
    try:
        if command.lower() == "list":
            if not shapes:
                print("No shapes or points defined yet.")
            else:
                print("Defined shapes and points:")
                for name, shape in shapes.items():
                    print(f"- {name}: {shape}")
        else:
            # Evaluate the query using the shapes context
            result = eval(command, {}, shapes)
            print(result)
    except Exception as e:
        print(f"Error: {e}. Type 'help' for guidance.")

def list_shapes(shapes):
    if not shapes:
        print("No shapes or points defined yet.")
    else:
        print("Defined shapes and points:")
        for name, shape in shapes.items():
            print(f"- {name}: {shape}")
