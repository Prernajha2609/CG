import turtle

def draw_circle(xc, yc, r):
    """Draws a circle centered at (xc, yc) with radius r using the Bresenham algorithm."""
    x = 0
    y = r
    d = 3 - 2 * r
    
    while x <= y:
        # Draw the eight symmetric points
        turtle.goto(xc + x, yc + y)
        turtle.stamp()
        turtle.goto(xc + x, yc - y)
        turtle.stamp()
        turtle.goto(xc - x, yc + y)
        turtle.stamp()
        turtle.goto(xc - x, yc - y)
        turtle.stamp()
        turtle.goto(xc + y, yc + x)
        turtle.stamp()
        turtle.goto(xc + y, yc - x)
        turtle.stamp()
        turtle.goto(xc - y, yc + x)
        turtle.stamp()
        turtle.goto(xc - y, yc - x)
        turtle.stamp()
        
        # Update the coordinates and decision variable
        x += 1
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1

# Set up the turtle graphics window
turtle.setup(500, 500)
turtle.penup()
turtle.hideturtle()
turtle.speed(0)

# Draw a circle centered at (0, 0) with radius 100
draw_circle(0, 0, 100)

# Wait for the user to close the window
turtle.done()
