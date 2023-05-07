import turtle

def draw_circle(xc, yc, r):
    """Draws a circle centered at (xc, yc) with radius r using the Midpoint algorithm."""
    x = r
    y = 0
    p = 1 - r
    
    while x >= y:
        # Draw the eight symmetric points
        turtle.goto(xc + x, yc + y)
        turtle.stamp()
        turtle.goto(xc + y, yc + x)
        turtle.stamp()
        turtle.goto(xc - y, yc + x)
        turtle.stamp()
        turtle.goto(xc - x, yc + y)
        turtle.stamp()
        turtle.goto(xc - x, yc - y)
        turtle.stamp()
        turtle.goto(xc - y, yc - x)
        turtle.stamp()
        turtle.goto(xc + y, yc - x)
        turtle.stamp()
        turtle.goto(xc + x, yc - y)
        turtle.stamp()
        
        # Update the coordinates and decision variable
        y += 1
        if p <= 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * y - 2 * x + 1

# Set up the turtle graphics window
turtle.setup(500, 500)
turtle.penup()
turtle.hideturtle()
turtle.speed(0)

# Draw a circle centered at (0, 0) with radius 100
draw_circle(0, 0, 100)

# Wait for the user to close the window
turtle.done()
