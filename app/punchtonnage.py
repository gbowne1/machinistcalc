import math


def punch_tonnage():
    print("Punch Tonnage Calculator")
    print("-----------------------")

    # Get input from user
    diameter = float(input("Enter punch diameter in inches: "))
    material_thickness = float(input("Enter material thickness in inches: "))
    shear_resistance = float(input("Enter shear resistance in pounds per square inch: "))

    # Calculate tonnage
    # Area of the punch in square inches
    punch_area = (math.pi * (diameter / 2) ** 2)
    # Shear force in pounds
    # Shear force = Area * Shear Resistance
    # Tonnage = Shear Force / 2000 (to convert to tons)
    # Tonnage = (Area * Shear Resistance) / 2000
    shear_force = punch_area * shear_resistance
    tonnage = shear_force / 2000  # Convert to tons
    shear_force = material_thickness * shear_resistance
    tonnage = shear_force / (2 * math.pi * (diameter / 2))

    # Print results
    print(f"Tonnage: {tonnage:.2f} tons")
    print(f"Shear Force: {shear_force:.2f} pounds")
    print(f"Punch Area: {punch_area:.2f} square inches")
    print(f"Material Thickness: {material_thickness:.2f} inches")
    print(f"Shear Resistance: {shear_resistance:.2f} pounds per square inch")
    print("-----------------------")
    print("End of Punch Tonnage Calculator")
    print("")
    
    
