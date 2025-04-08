import math
from typing import Tuple


def bend_calc(
    length: float,
    width: float,  # Ensure width is used in calculations
    thickness: float,
    bend_angle: float,
    inner_radius: float,
    k_factor: float,
    tensile_strength: float,  # Used in the tonnage calculation
    die_opening: float = 1.0,  # Used in the tonnage calculation
    k_constant: float = 50,
) -> Tuple[float, float, float]:
# Convert angle to radians (used in bend allowance calculation)
angle_radians = bend_angle * (math.pi / 180)

# Calculate bend allowance using angle_radians
bend_allowance = angle_radians * (inner_radius + k_factor * thickness) * length

# Ensure die_opening is used and k_constant is defined if not passed as a parameter
k_constant = k_constant or 50  # Default value if not provided
if die_opening <= 0:
    raise ValueError("die_opening must be greater than 0")

# Calculate tonnage
material_factor = 1  # Define material_factor with a default value, tensile_strength is used here
tonnage = (k_constant * length * width * thickness * tensile_strength) / (
    die_opening * material_factor
)  # Ensure die_opening is used in the calculation

return bend_allowance, tonnage, 0.0  # Return a tuple with a placeholder third value
