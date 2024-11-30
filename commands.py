from shapes import Point, Line, Circle, Rectangle

def parse_point_inline(expr, shapes):
    if "(" in expr and ")" in expr:
        try:
            name, coords = expr.split("(", 1)
            coords = coords.strip()[:-1]
            x, y = map(float, coords.split(","))
            if name.strip() not in shapes:
                shapes[name.strip()] = Point(name.strip(), x, y)
            return shapes[name.strip()]
        except ValueError:
            raise ValueError("Invalid point syntax. Use name(x, y).")
    elif expr.strip() in shapes:
        return shapes[expr.strip()]
    else:
        raise ValueError(f"Point '{expr.strip()}' is not defined or invalid syntax.")

def define_point(name, expr, shapes):
    x, y = eval(expr[6:-1])
    shapes[name] = Point(name, x, y)
    return f"{name} defined as {shapes[name]}."

def define_line(name, expr, shapes):
    p1_expr, p2_expr = expr[5:-1].split(",")
    p1 = parse_point_inline(p1_expr.strip(), shapes)
    p2 = parse_point_inline(p2_expr.strip(), shapes)
    shapes[name] = Line(name, p1, p2)
    return f"{name} defined as {shapes[name]}."

def define_circle(name, expr, shapes):
    center_expr, radius = expr[7:-1].split(",")
    center = parse_point_inline(center_expr.strip(), shapes)
    radius = float(radius.strip())
    shapes[name] = Circle(name, center, radius)
    return f"{name} defined as {shapes[name]}."

def define_rectangle(name, expr, shapes):
    bl_expr, tr_expr = expr[10:-1].split(",")
    bottom_left = parse_point_inline(bl_expr.strip(), shapes)
    top_right = parse_point_inline(tr_expr.strip(), shapes)
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
