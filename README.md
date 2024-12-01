# Geometric Calculator

## Command to Run the Code

1. Unzip all the 3 files, in the same file directory
2. Open the terminal and navigate to the folder containing the project files.
3. Run the application using, to get the CLI like interface:

   ```bash
   python3 main.py

---

## Functions and Syntax

### Defining Shapes

- **Point**:  
  **Syntax**: `<name> = Point(x, y)`  
  **Example**:  
  ```python
  p1 = Point(0, 0)

- **Line**:  
  **Syntax**: `<name> = Line(point1, point2)`  
  **Example**:  
  ```python
  p1 = Line(p1, p2)

- **Circle**:  
  **Syntax**: `<name> = Circle(center, radius)`  
  **Example**:  
  ```python
  c1 = Circle(p1, 2)

- **Rectangle**:  
  **Syntax**: `<name> = Rectangle(point1, point2, point3, point4)`  
  **Example**:  
  ```python
  r1 = Rectangle(p1, p2, p4, p3)

---

## Queries for Shapes

- **PDistance between Shapes**:  
  **Syntax**: `distance(shape1, shape2)`  
  **Example**:  
  ```python
  distance(p1, l1)

- Use the `help` command after running the program to view the list of available commands.

---

## High-Level Design of the Application

The **Geometric Calculator** is a command-line interface tool implemented using Python. It supports creating and managing basic geometric shapes (points, lines, circles, and rectangles) and allows users to calculate various properties such as distances, areas, perimeters, and lengths.

---

### Design Components

- **Classes**:
  - `Point`, `Line`, `Circle`, and `Rectangle` classes encapsulate geometric entities and their methods.
  - Each class provides a `distance_to` method to compute distances to other shapes.

- **Command Parsing**:
  - User commands are processed using a `parse_command` function, which maps inputs to shape definitions or queries.

- **Main Program Loop**:
  - The main program (`main.py`) provides a REPL-like interface to continuously accept user commands until the `exit` command is entered.

## Assumptions and Known Issues with the Implementation

### Assumptions

- All shapes are defined in a **2D Cartesian coordinate system**.
- If two shapes intersect, the distance between them is **0.0**.
- All user inputs must follow the correct syntax for shape definitions and queries.
- Names of all variables must have no space between them

---

### Known Issues

- **Rotated Rectangles**:
  - Rotated rectangles are supported, but calculations may fail if points are not input correctly to form a valid rectangle.
  - The same applies for all inputs; improper definitions may lead to errors, as it does not check for validity of shape.

## Challenges Faced During the Project

### Dynamic Point Allocation

- Dynamically allocating points while defining complex shapes (like circles or rectangles) was challenging and eventually omitted.
- Resolving dependency issues between shapes required handling of shape initialization, whcih took a lot of time and formulas for each were time consuming.

---

### Distance Calculations

- Computing distances between different shapes (especially between lines, circles, and rectangles) required intricate logic.
- Handling edge cases such as parallel lines and overlapping shapes added complexity.

## Additional Info

### Logic for Distance Calculation

- **Point-to-Point**: Euclidean distance formula.
- **Point-to-Line**: Perpendicular distance from the point to the line segment.
- **Point-to-Circle**: Distance from the point to the circle's center, minus the radius.
- **Point-to-Rectangle**: Shortest distance to any edge of the rectangle.
- **Line-to-Line**:
  - Perpendicular distance for parallel lines.
  - Shortest distance between endpoints otherwise.
- **Line-to-Circle**: Minimum distance from the circle's center to the line, minus the radius.
- **Circle-to-Circle**: Distance between centers minus the sum of radii.
- **Rectangle-to-Rectangle**: Minimum distance between edges of the rectangles.

---

### Quality of Life Addition

- A `list` command was added to allow the user to view all defined shapes, making it easier to track progress in the session.

---

### Testing

- The application was tested using various combinations of shapes and queries to ensure accuracy, visualised using this website: https://www.geogebra.org/m/VWN3g9rE for checking accuracy.

## Test Case

Here is a copy-pasteable test case that can be used:

```python
p1 = Point(0, 0)
p2 = Point(4, 0)
p3 = Point(0, 3)
p4 = Point(4, 3)
p5 = Point(2, 1)
p6 = Point(5, 5)
p7 = Point(1, 4)
p8 = Point(3, 2)
l1 = Line(p1, p2)
l2 = Line(p3, p4)
l3 = Line(p1, p3)
l4 = Line(p5, p6)
c1 = Circle(p1, 2)
c2 = Circle(p6, 3)
r1 = Rectangle(p1, p2, p4, p3)
r2 = Rectangle(p5, p7, p8, p6)
list
distance(p1, p2)
distance(p1, l1)
distance(p5, c1)
distance(p5, r1)
distance(l1, l2)
distance(l1, c1)
distance(l3, r2)
distance(c1, c2)
distance(c1, r1)
distance(r1, r2)
c1.area()
c1.circumference()
l1.length()
r1.area()
r1.perimeter()

