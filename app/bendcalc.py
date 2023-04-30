from typing import Tuple


def bend_calc(
    length,
    width,
    thickness,
    bend_angle,
    inner_radius,
    k_factor,
    tensile_strength,
    die_opening,
    material_factor=1,
    k_constant=50,
) -> Tuple[float, float, float]:

    # Convert angle to radians
    angle_radians = bend_angle * (3.14159265359 / 180)

    # Calculate bend allowance
    bend_allowance = angle_radians * (inner_radius + k_factor * thickness)

    # Calculate K-factor
    k_factor_calculated = (bend_allowance / thickness) / (0.01745 * inner_radius + 1)

    tonnage = (k_constant * length * thickness * tensile_strength) / (
        die_opening * material_factor
    )

    return bend_allowance, k_factor_calculated, tonnage
