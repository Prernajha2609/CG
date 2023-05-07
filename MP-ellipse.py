import turtle

def draw_ellipse(xc, yc, a, b):
    """Draws an ellipse centered at (xc, yc) with semimajor axis a and semiminor axis b using the Midpoint algorithm."""
    x = 0
    y = b
    a2 = a * a
    b2 = b * b
    d = b2 + a2 * (0.25 - b)
    
    while b2 * (x + 1) < a2 * (y - 0.5):
        # Draw the four symmetric points in the first quadrant
        turtle.goto(xc + x, yc + y)
        turtle.stamp()
        turtle.goto(xc - x, yc + y)
        turtle.stamp()
        turtle.goto(xc - x, yc - y)
        turtle.stamp()
        turtle.goto(xc + x, yc - y)
        turtle.stamp()
        
        # Update the coordinates and decision variable
        x += 1
        if d >= 0:
            y -= 1
            d = d + b2 * (2 * x + 1) - a2 * (2 * y)
        else:
            d = d + b2 * (2 * x + 1)
        
    d = b2 * (x + 0.5) ** 2 + a2 * (y - 1) ** 2 - a2 * b2
    
    while y >= 0:
        # Draw the four symmetric points in the fourth quadrant
        turtle.goto(xc + x, yc + y)
        turtle.stamp()
        turtle.goto(xc - x, yc + y)
        turtle.stamp()
        turtle.goto(xc - x, yc - y)
        turtle.stamp()
        turtle.goto(xc + x, yc - y)
        turtle.stamp()
        
        # Update the coordinates and decision variable
        y -= 1
        if d <= 0:
            x += 1
            d = d + b2 * (2 * x) - a2 * (2 * y + 1)
        else:
            d = d + a2 * (2 * y + 1)
        
# Set up the turtle graphics window
turtle.setup(500, 500)
turtle.penup()
turtle.hideturtle()
turtle.speed(0)

# Draw an ellipse centered at (0, 0) with semimajor axis 100 and semiminor axis 50
draw_ellipse(0, 0, 100, 50)

# Wait for the user to close the window
turtle.done()
