from typing import Tuple


def lathe_calc(
    diameter: float, surface_speed: float, feed_rate: float, number_of_teeth: int
) -> tuple[float, float]:

    spindle_speed = (surface_speed * 12) / (3.14159265359 * diameter)
    chip_load = feed_rate / (number_of_teeth * spindle_speed)

    return spindle_speed, chip_load
