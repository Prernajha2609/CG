import turtle

def polygon_scanline_fill(polygon):
    """Fills a polygon using the scanline algorithm."""
    # Find the y-coordinate range of the polygon
    ymin = polygon[0][1]
    ymax = polygon[0][1]
    for vertex in polygon:
        if vertex[1] < ymin:
            ymin = vertex[1]
        if vertex[1] > ymax:
            ymax = vertex[1]

    # Initialize the active edge table and the edge table
    edge_table = []
    active_edge_table = []
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        if p1[1] < p2[1]:
            ymin = p1[1]
            ymax = p2[1]
            xmin = p1[0]
            slope = (p2[0] - p1[0]) / (p2[1] - p1[1])
            edge_table.append((ymin, ymax, xmin, slope))
        elif p1[1] > p2[1]:
            ymin = p2[1]
            ymax = p1[1]
            xmin = p2[0]
            slope = (p2[0] - p1[0]) / (p2[1] - p1[1])
            edge_table.append((ymin, ymax, xmin, slope))

    # Sort the edge table by the y-coordinate of the first endpoint
    edge_table.sort()

    # Initialize the current y-coordinate and the active edge table index
    y = edge_table[0][0]
    aet_index = 0

    # Iterate over the scanlines
    while y <= ymax:
        # Add edges from the edge table to the active edge table
        while aet_index < len(edge_table) and edge_table[aet_index][0] == y:
            active_edge_table.append(edge_table[aet_index])
            aet_index += 1

        # Remove edges from the active edge table that end at the current y-coordinate
        active_edge_table = [edge for edge in active_edge_table if edge[1] != y]

        # Sort the active edge table by the x-coordinate of the intersection point with the scanline
        active_edge_table.sort(key=lambda edge: edge[2])

        # Fill the pixels between the edges in the active edge table
        for i in range(0, len(active_edge_table), 2):
            xmin = int(active_edge_table[i][2])
            xmax = int(active_edge_table[i + 1][2])
            for x in range(xmin, xmax + 1):
                turtle.goto(x, y)
                turtle.stamp()

        # Increment the current y-coordinate
        y += 1

        # Update the x-coordinate of the edges in the active edge table
        for i in range(len(active_edge_table)):
            active_edge_table[i] = (active_edge_table[i][0], active_edge_table[i][1], active_edge_table[i][2] + active_edge_table[i][3], active_edge_table[i][3])
polygon = [(0, 0), (50, 100), (100, 50), (75,
