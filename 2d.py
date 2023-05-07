import math

def rotate(vertices, angle):
    """Rotates a list of vertices by an angle (in degrees) around the origin."""
    rad = math.radians(angle)
    cos = math.cos(rad)
    sin = math.sin(rad)
    new_vertices = []
    for vertex in vertices:
        x = vertex[0] * cos - vertex[1] * sin
        y = vertex[0] * sin + vertex[1] * cos
        new_vertices.append((x, y))
    return new_vertices

def translate(vertices, dx, dy):
    """Translates a list of vertices by dx and dy."""
    new_vertices = []
    for vertex in vertices:
        x = vertex[0] + dx
        y = vertex[1] + dy
        new_vertices.append((x, y))
    return new_vertices

def scale(vertices, sx, sy):
    """Scales a list of vertices by sx and sy."""
    new_vertices = []
    for vertex in vertices:
        x = vertex[0] * sx
        y = vertex[1] * sy
        new_vertices.append((x, y))
    return new_vertices

# Example usage:

# Define a square as a list of vertices
square = [(0, 0), (0, 100), (100, 100), (100, 0)]

# Rotate the square by 45 degrees around the origin
square = rotate(square, 45)

# Translate the square by (200, 100)
square = translate(square, 200, 100)

# Scale the square by a factor of 2 in both the x and y directions
square = scale(square, 2, 2)

# Print the transformed square
print(square)
