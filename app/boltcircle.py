import math

def bolt_circle(diameter, num_holes):
    angle = 360 / num_holes
    coordinates = []
    for i in range(num_holes):
        x = diameter/2 * math.cos(math.radians(i*angle))
        y = diameter/2 * math.sin(math.radians(i*angle))
        coordinates.append((x, y))
    return coordinates

# Example usage
diameter = 6  # inches
num_holes = 12
coordinates = bolt_circle(diameter, num_holes)
for i, (x, y) in enumerate(coordinates, start=1):
    print(f"Hole {i}: ({x:.2f}, {y:.2f})")
