import turtle

# Define the region codes
INSIDE = 0 # 0000
LEFT = 1 # 0001
RIGHT = 2 # 0010
BOTTOM = 4 # 0100
TOP = 8 # 1000

def region_code(x, y, xmin, xmax, ymin, ymax):
    """Computes the region code for a point (x, y) with respect to the given clipping window."""
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def clip_line(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    """Clips a line segment (x1, y1) to (x2, y2) against the given clipping window."""
    # Compute the region codes for the endpoints of the line
    code1 = region_code(x1, y1, xmin, xmax, ymin, ymax)
    code2 = region_code(x2, y2, xmin, xmax, ymin, ymax)
    
    while True:
        if code1 == INSIDE and code2 == INSIDE:
            # Both endpoints are inside the clipping window, so the line is fully visible
            turtle.penup()
            turtle.goto(x1, y1)
            turtle.pendown()
            turtle.goto(x2, y2)
            return
        
        if code1 & code2 != 0:
            # Both endpoints are outside the same clip edge, so the line is invisible
            return
        
        # Select one of the endpoints outside the clipping window
        if code1 != INSIDE:
            code_out = code1
            x, y = x1, y1
        else:
            code_out = code2
            x, y = x2, y2
        
        # Compute the intersection point of the line with the clip edge
        if code_out & TOP:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax
        elif code_out & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin
        
        # Update the appropriate endpoint
        if code_out == code1:
            x1, y1 = x, y
            code1 = region_code(x1, y1, xmin, xmax, ymin, ymax)
        else:
            x2, y2 = x, y
            code2 = region_code(x2, y2, xmin, xmax, ymin, ymax)

# Set up the turtle graphics window
turtle.setup(500, 500)
turtle.penup()
turtle.hideturtle()
turtle.speed(0)

# Draw the clipping window
turtle.goto(-200, -100)
turtle.pendown()
turtle.goto(200, -100)
turtle.goto(200, 100)
turtle.goto(-200, 100)
turtle.goto(-200, -100)
turtle
