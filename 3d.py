import math
import numpy as np

def rotate_x(vertices, angle):
    """Rotates a list of vertices by an angle (in degrees) around the x-axis."""
    rad = math.radians(angle)
    cos = math.cos(rad)
    sin = math.sin(rad)
    rotation_matrix = np.array([[1, 0, 0],
                                [0, cos, -sin],
                                [0, sin, cos]])
    new_vertices = np.dot(rotation_matrix, vertices.T).T
    return new_vertices.tolist()

def rotate_y(vertices, angle):
    """Rotates a list of vertices by an angle (in degrees) around the y-axis."""
    rad = math.radians(angle)
    cos = math.cos(rad)
    sin = math.sin(rad)
    rotation_matrix = np.array([[cos, 0, sin],
                                [0, 1, 0],
                                [-sin, 0, cos]])
    new_vertices = np.dot(rotation_matrix, vertices.T).T
    return new_vertices.tolist()

def rotate_z(vertices, angle):
    """Rotates a list of vertices by an angle (in degrees) around the z-axis."""
    rad = math.radians(angle)
    cos = math.cos(rad)
    sin = math.sin(rad)
    rotation_matrix = np.array([[cos, -sin, 0],
                                [sin, cos, 0],
                                [0, 0, 1]])
    new_vertices = np.dot(rotation_matrix, vertices.T).T
    return new_vertices.tolist()

def translate(vertices, dx, dy, dz):
    """Translates a list of vertices by dx, dy, and dz."""
    translation_vector = np.array([dx, dy, dz])
    new_vertices = np.array(vertices) + translation_vector
    return new_vertices.tolist()

def scale(vertices, sx, sy, sz):
    """Scales a list of vertices by sx, sy, and sz."""
    scaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, sz]])
    new_vertices = np.dot(scaling_matrix, np.array(vertices).T).T
    return new_vertices.tolist()

# Example usage:

# Define a cube as a list of vertices
cube = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0),
        (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)]

# Rotate the cube by 45 degrees around the x-axis
cube = rotate_x(cube, 45)

# Rotate the cube by 30 degrees around the y-axis
cube = rotate_y(cube, 30)

# Rotate the cube by 60 degrees around the z-axis
cube = rotate_z(cube, 60)

# Translate the cube by (2, 3, 4)
cube = translate(cube, 2, 3, 4)

# Scale the cube by a factor of 2 in the x direction, 3 in the y direction, and 4 in the z direction
cube = scale(cube, 2, 3, 4)

# Print the transformed cube
print(cube)
