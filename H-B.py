from tkinter import *

def hermite_curve(p0, p1, r0, r1, num_segments):
    """Returns a list of points that approximate a Hermite curve."""
    points = []
    dt = 1 / num_segments
    for i in range(num_segments):
        t = i * dt
        h00 = 2*t**3 - 3*t**2 + 1
        h01 = -2*t**3 + 3*t**2
        h10 = t**3 - 2*t**2 + t
        h11 = t**3 - t**2
        x = h00*p0[0] + h01*p1[0] + h10*r0[0] + h11*r1[0]
        y = h00*p0[1] + h01*p1[1] + h10*r0[1] + h11*r1[1]
        points.append((x, y))
    return points

def bezier_curve(p0, p1, p2, p3, num_segments):
    """Returns a list of points that approximate a Bezier curve."""
    points = []
    dt = 1 / num_segments
    for i in range(num_segments):
        t = i * dt
        mt = 1 - t
        x = mt**3*p0[0] + 3*mt**2*t*p1[0] + 3*mt*t**2*p2[0] + t**3*p3[0]
        y = mt**3*p0[1] + 3*mt**2*t*p1[1] + 3*mt*t**2*p2[1] + t**3*p3[1]
        points.append((x, y))
    return points

# Example usage:

# Create a window
root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

# Draw a Hermite curve
p0 = (100, 100)
p1 = (300, 100)
r0 = (50, 0)
r1 = (-50, 0)
points = hermite_curve(p0, p1, r0, r1, 100)
canvas.create_line(points, fill="blue")

# Draw a Bezier curve
p0 = (100, 200)
p1 = (150, 100)
p2 = (250, 200)
p3 = (300, 100)
points = bezier_curve(p0, p1, p2, p3, 100)
canvas.create_line(points, fill="red")

# Start the main loop
root.mainloop()
