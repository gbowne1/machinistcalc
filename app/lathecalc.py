import math
from typing import Tuple

def lathe_calc():
    # Prompt the user for inputs
    rpm = float(input("Enter the RPM: "))
    ipr = float(input("Enter the inches per revolution: "))
    diameter = float(input("Enter the workpiece diameter before machining: "))
    feed_rate = float(input("Enter the feed rate: "))
    depth_of_cut = float(input("Enter the depth of cut: "))
    metal_removal_rate = float(input("Enter the metal removal rate: "))
    spindle_rpm = input("Enter the available spindle rpm range: ")
    surface_finish_unit = input("Enter the unit, UM or RA, for surface finish (µm or Ra): ").upper()
    tooling_material = input("Enter the tooling material: ")
    calculated_feed_per_rev = calculate_feed_per_rev(ipr, rpm)

    # Calculate sfpm
    sfpm = calculate_sfpm(diameter, rpm)

    # Prompt for surface finish value based on user preference
    if surface_finish_unit == "UM":
        surface_finish = float(input("Enter the required surface finish in micrometers (µm): "))
        print(f"Using micrometers (µm) for surface finish.")
    elif surface_finish_unit == "RA":
        surface_finish = float(input("Enter the required surface finish (Ra): "))
        print(f"Using Roughness Average (Ra) for surface finish.")
    else:
        print(f"Invalid unit entered. Please enter 'µm' or 'Ra'.")
        # Handle the case where the user enters an invalid unit

    # Calculate ipm (if needed)
    ipm = calculate_ipm(sfpm, calculated_feed_per_rev)

    # Print the results
    print(f"Calculated feed rate: {feed_rate}")
    print(f"Calculated spindle RPM: {spindle_rpm}")
    print(f"Calculated material removal rate: {metal_removal_rate}")
    print(f"Calculated Inches per Revolution: {ipr:.2f}")
    print(f"Calculated Surface Feet per Minute: {sfpm:.2f}")
    print(f"Calculated Inches per Minute: {ipm:.2f}")  # Print ipm only if calculated
    print(f"Calculated Feed per Revolution: {calculated_feed_per_rev:.2f}")


def calculate_sfpm(diameter, rpm):
    sfpm = (diameter * math.pi * rpm) / 12
    return sfpm

def calculate_ipm(sfpm, feed_per_rev):
    ipm = sfpm * feed_per_rev
    return ipm

def calculate_feed_per_rev(ipr, rpm):
    feed_per_rev = ipr * rpm
    return feed_per_rev
