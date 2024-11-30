from shapes import Point, Line, Circle, Rectangle

def define_point(name, expr, shapes):
    x, y = eval(expr[6:-1])
    shapes[name] = Point(name, x, y)
    return f"{name} defined as {shapes[name]}."

def define_line(name, expr, shapes):
    p1_name, p2_name = expr[5:-1].split(",")
    p1 = shapes[p1_name.strip()]
    p2 = shapes[p2_name.strip()]
    shapes[name] = Line(name, p1, p2)
    return f"{name} defined as {shapes[name]}."

def define_circle(name, expr, shapes):
    center_name, radius = expr[7:-1].split(",")
    center = shapes[center_name.strip()]
    radius = float(radius.strip())
    shapes[name] = Circle(name, center, radius)
    return f"{name} defined as {shapes[name]}."

def define_rectangle(name, expr, shapes):
    bl_name, tr_name = expr[10:-1].split(",")
    bottom_left = shapes[bl_name.strip()]
    top_right = shapes[tr_name.strip()]
    shapes[name] = Rectangle(name, bottom_left, top_right)
    return f"{name} defined as {shapes[name]}."

def parse_command(command, shapes):
    name, expr = command.split("=")
    name = name.strip()
    expr = expr.strip()

    if expr.startswith("Point"):
        return define_point(name, expr, shapes)
    elif expr.startswith("Line"):
        return define_line(name, expr, shapes)
    elif expr.startswith("Circle"):
        return define_circle(name, expr, shapes)
    elif expr.startswith("Rectangle"):
        return define_rectangle(name, expr, shapes)
    else:
        return "Invalid shape definition. Type 'help' for guidance."

def list_shapes(shapes):
    if not shapes:
        return "No shapes or points defined yet."
    return "\n".join([f"- {name}: {shape}" for name, shape in shapes.items()])
