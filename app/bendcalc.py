import math
from typing import Tuple


def bend_calc(
    length: float,
    width: float,
    thickness: float,
    bend_angle: float,
    inner_radius: float,
    k_factor: float,
    tensile_strength: float,
    die_opening: float,
    k_constant: float = 50,
    material_factor: float = 1,
) -> Tuple[float, float, float]:
    # Convert angle to radians
    angle_radians = bend_angle * (math.pi / 180)

    # Calculate bend allowance
    bend_allowance = angle_radians * (inner_radius + k_factor * thickness)

    # Calculate K-factor
    k_factor_calculated = (bend_allowance / thickness) / (0.01745 * inner_radius + 1)

    # Calculate tonnage
    tonnage = (k_constant * length * width * thickness * tensile_strength) / (
        die_opening * material_factor
    )

    return bend_allowance, k_factor_calculated, tonnage