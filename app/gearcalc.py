import math
from typing import Optional


class GearCalculator:

    def __init__(self, num_teeth: Optional[int] = None, module: Optional[float] = None, pitch_diameter: Optional[float] = None, pressure_angle: float = 20):
        """
        Initialize the GearCalculator with number of teeth, module, pitch diameter, and pressure angle.

        :param num_teeth: Number of teeth on the gear
        :param module: Module of the gear
        :param pitch_diameter: Pitch diameter of the gear
        :param pressure_angle: Pressure angle in degrees
        """
        if num_teeth is not None and num_teeth <= 0:
            raise ValueError("Number of teeth must be greater than zero")
        if module is not None and module <= 0:
            raise ValueError("Module must be greater than zero")
        if pitch_diameter is not None and pitch_diameter <= 0:
            raise ValueError("Pitch diameter must be greater than zero")
        if not (0 <= pressure_angle <= 90):
            raise ValueError("Pressure angle must be between 0 and 90 degrees")

        self.num_teeth = num_teeth
        self.module = module
        self.pitch_diameter = pitch_diameter
        self.pressure_angle = math.radians(pressure_angle)  # convert to radians

    def calculate_pitch_diameter(self) -> Optional[float]:
        """
        Calculate the pitch diameter of the gear.

        :return: Pitch diameter or None if not calculable
        """
        if self.num_teeth and self.module:
            self.pitch_diameter = self.num_teeth * self.module
        return self.pitch_diameter

    def calculate_module(self) -> float:
        """
        Calculate the module of the gear.

        :return: Module
        """
        if self.pitch_diameter and self.num_teeth:
            self.module = self.pitch_diameter / self.num_teeth
        if self.module is not None:
            return self.module
        raise ValueError("Module is not defined, cannot calculate module")

    def calculate_circular_pitch(self) -> float:
        """
        Calculate the circular pitch of the gear.

        :return: Circular pitch
        """
        if self.module:
            return self.module * math.pi
        raise ValueError("Module is not defined, cannot calculate circular pitch")

    def calculate_addendum(self) -> float:
        """
        Calculate the addendum of the gear.

        :return: Addendum
        """
        if self.module:
            return self.module
        raise ValueError("Pitch diameter or pressure angle is not defined, cannot calculate base circle diameter")

    def calculate_dedendum(self) -> float:
        """
        Calculate the dedendum of the gear.

        :return: Dedendum
        """
        if self.module:
            return 1.25 * self.module
        raise ValueError("Module is not defined, cannot calculate gear tooth thickness")

    def calculate_tooth_height(self) -> float:
        """
        Calculate the total tooth height of the gear.

        :return: Tooth height
        """
        return self.calculate_addendum() + self.calculate_dedendum()

    def calculate_clearance(self) -> float:
        """
        Calculate the clearance of the gear.

        :return: Clearance
        """
        if self.module:
            return 0.25 * self.module
        raise ValueError("Module is not defined, cannot calculate gear tooth thickness")

    def calculate_gear_tooth_thickness(self) -> float:
        """
        Calculate the gear tooth thickness.

        :return: Gear tooth thickness
        """
        if self.module:
            return math.pi / 2 * self.module / 2
        raise ValueError("Module is not defined, cannot calculate gear tooth thickness")

    def calculate_base_circle_diameter(self) -> float:
        """
        Calculate the base circle diameter of the gear.

        :return: Base circle diameter
        """
        if self.pitch_diameter and self.pressure_angle:
            return self.pitch_diameter * math.cos(self.pressure_angle)
        raise ValueError("Pitch diameter or pressure angle is not defined, cannot calculate base circle diameter")

    def calculate_outside_diameter(self) -> float:
        """
        Calculate the outside diameter of the gear.

        :return: Outside diameter
        """
        if self.pitch_diameter and self.module:
            return self.pitch_diameter + 2 * self.module
        raise ValueError("Pitch diameter or module is not defined, cannot calculate root diameter")

    def calculate_root_diameter(self) -> float:
        """
        Calculate the root diameter of the gear.

        :return: Root diameter
        """
        if self.pitch_diameter and self.module:
            return self.pitch_diameter - 2.5 * self.module
        raise ValueError("Pitch diameter or module is not defined, cannot calculate root diameter")

    def calculate_gear_ratio(self, other_gear_teeth: int) -> float:
        """
        Calculate the gear ratio given the number of teeth on two gears.

        :param other_gear_teeth: Number of teeth on the other gear
        :return: Gear ratio
        """
        if self.num_teeth and other_gear_teeth:
            return self.num_teeth / other_gear_teeth
        raise ValueError("Number of teeth for either gear is not defined, cannot calculate gear ratio")

# Example usage
if __name__ == "__main__":
    gear = GearCalculator(num_teeth=20, module=2)
    print("Pitch Diameter:", gear.calculate_pitch_diameter())
    print("Outside Diameter:", gear.calculate_outside_diameter())
    print("Root Diameter:", gear.calculate_root_diameter())
    print("Base Circle Diameter:", gear.calculate_base_circle_diameter())
    print("Circular Pitch:", gear.calculate_circular_pitch())
    print("Addendum:", gear.calculate_addendum())
    print("Dedendum:", gear.calculate_dedendum())
    print("Tooth Height:", gear.calculate_tooth_height())
    print("Clearance:", gear.calculate_clearance())
    print("Gear Tooth Thickness:", gear.calculate_gear_tooth_thickness())
    print("Gear Ratio with 40 teeth gear:", gear.calculate_gear_ratio(40))
    print("Gear Ratio with 40 teeth gear:", gear.calculate_gear_ratio(40))
    print("Gear Ratio with 40 teeth gear:", gear.calculate_gear_ratio(40))
