import turtle

def draw_line(x0, y0, x1, y1):
    """Draws a line from (x0, y0) to (x1, y1) using the Bresenham algorithm."""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    while x0 != x1 or y0 != y1:
        # Draw the current point
        turtle.goto(x0, y0)
        turtle.stamp()
        
        # Calculate the error term
        e2 = 2 * err
        
        # Update the x coordinate
        if e2 > -dy:
            err -= dy
            x0 += sx
        
        # Update the y coordinate
        if e2 < dx:
            err += dx
            y0 += sy
    
    # Draw the final point
    turtle.goto(x1, y1)
    turtle.stamp()

# Set up the turtle graphics window
turtle.setup(500, 500)
turtle.penup()
turtle.hideturtle()
turtle.speed(0)

# Draw a line from (100, 100) to (200, 300)
draw_line(100, 100, 200, 300)

# Wait for the user to close the window
turtle.done()
