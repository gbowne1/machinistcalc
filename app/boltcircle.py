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
if __name__ == "__main__":
    diameter = float(input("Enter the diameter of the bolt circle: "))  # Accept user input for the diameter
    num_holes = int(input("Enter the number of holes: "))  # Accept user input for the number of holes
    coordinates = bolt_circle(diameter, num_holes)
    for i, (x, y) in enumerate(coordinates, start=1):
        print(f"Hole {i}: ({x:.2f}, {y:.2f})")
