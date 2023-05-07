import turtle

def clip_polygon(subject_polygon, clip_polygon):
    """Clips a subject polygon against a clip polygon using the Sutherland-Hodgman algorithm."""
    # Initialize the output list with the subject polygon vertices
    output_list = subject_polygon.copy()
    
    # Iterate over each edge of the clip polygon
    for i in range(len(clip_polygon)):
        # Define the clip edge endpoints
        clip_edge_start = clip_polygon[i]
        clip_edge_end = clip_polygon[(i + 1) % len(clip_polygon)]
        
        # Initialize the input list with the current output list
        input_list = output_list.copy()
        output_list = []
        
        # Iterate over each edge of the input list
        for j in range(len(input_list)):
            # Define the input edge endpoints
            input_edge_start = input_list[j]
            input_edge_end = input_list[(j + 1) % len(input_list)]
            
            # Compute the intersection point of the input edge with the clip edge
            p1_inside = inside(input_edge_start, clip_edge_start, clip_edge_end)
            p2_inside = inside(input_edge_end, clip_edge_start, clip_edge_end)
            if p1_inside and p2_inside:
                # Both endpoints of the input edge are inside the clip edge
                output_list.append(input_edge_end)
            elif p1_inside and not p2_inside:
                # Only the start point of the input edge is inside the clip edge
                intersection = intersect(input_edge_start, input_edge_end, clip_edge_start, clip_edge_end)
                output_list.append(intersection)
            elif not p1_inside and p2_inside:
                # Only the end point of the input edge is inside the clip edge
                intersection = intersect(input_edge_start, input_edge_end, clip_edge_start, clip_edge_end)
                output_list.append(intersection)
                output_list.append(input_edge_end)
        
    return output_list

def inside(point, clip_edge_start, clip_edge_end):
    """Checks if a point is inside a clip edge."""
    if clip_edge_start[0] < clip_edge_end[0]:
        xmin = clip_edge_start[0]
        xmax = clip_edge_end[0]
    else:
        xmin = clip_edge_end[0]
        xmax = clip_edge_start[0]
    if clip_edge_start[1] < clip_edge_end[1]:
        ymin = clip_edge_start[1]
        ymax = clip_edge_end[1]
    else:
        ymin = clip_edge_end[1]
        ymax = clip_edge_start[1]
    x, y = point
    return xmin <= x <= xmax and ymin <= y <= ymax

def intersect(p1, p2, q1, q2):
    """Computes the intersection point of two line segments."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = q1
    x4, y4 = q2
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if d == 0:
        return None
    else:
        xi = ((x3 - x4) * (x1 * y2 - y1 * x2) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
        yi = ((y3 - y4) * (x1 * y2 - y1 * x2) - (y1 - y2
