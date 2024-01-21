import math

class GearCalculator:
    def __init__(self, module, number_of_teeth, pressure_angle):
        self.module = module
        self.number_of_teeth = number_of_teeth
        self.pressure_angle = pressure_angle

    def calculate_reference_diameter(self):
        return self.module * self.number_of_teeth

    def calculate_addendum(self):
        return self.module

    def calculate_dedendum(self):
        return 1.25 * self.module

    def calculate_tooth_height(self):
        return self.calculate_addendum() + self.calculate_dedendum()

    def calculate_gear_ratio(self, teeth1, teeth2):
        return teeth2 / teeth1

# Example usage
if __name__ == "__main__":
    module = 1.0
    number_of_teeth = 20
    pressure_angle = 20  # in degrees

    calc = GearCalculator(module, number_of_teeth, pressure_angle)
    print("Reference Diameter:", calc.calculate_reference_diameter())
    print("Addendum:", calc.calculate_addendum())
    print("Dedendum:", calc.calculate_dedendum())
    print("Tooth Height:", calc.calculate_tooth_height())
    print("Gear Ratio:", calc.calculate_gear_ratio(20, 40))
