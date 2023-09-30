import math
from typing import Tuple


def punchtonnage():
    print("Punch Tonnage Calculator")
    print("-----------------------")

    # Get input from user
    diameter = float(input("Enter punch diameter in inches: "))
    material_thickness = float(input("Enter material thickness in inches: "))
    shear_resistance = float(input("Enter shear resistance in pounds per square inch: "))

    # Calculate tonnage
    circumference = diameter * math.pi
    shear_force = material_thickness * shear_resistance
    tonnage = shear_force / (2 * math.pi * (diameter / 2))

    # Print results
    print(f"Tonnage: {tonnage:.2f} tons")