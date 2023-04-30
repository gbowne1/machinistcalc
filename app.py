from app.lathecalc import lathe_calc
from app.sheetmetalcalc import sheetmetal_calc
from app.bendcalc import bend_calc


class Menu:
    def _lathecalc(self) -> None:

        diameter = float(input("Enter workpiece diameter in inches: "))
        surface_speed = float(input("Enter surface speed in SFM: "))
        feed_rate = float(input("Enter feed rate in inches per revolution: "))
        number_of_teeth = int(input("Enter number of teeth on cutting tool: "))

        spindle_speed, chip_load = lathe_calc(
            diameter, surface_speed, feed_rate, number_of_teeth
        )

        print("\n")
        print("Spindle speed = ", spindle_speed, "RPM")
        print("Chip load = ", chip_load, "in/tooth")

        return

    def _sheetmetalcalc(self) -> None:
        sheet_width = float(input("Enter sheet width in inches: "))
        sheet_length = float(input("Enter sheet length in inches: "))
        part_width = float(input("Enter part width in inches: "))
        part_length = float(input("Enter part length in inches: "))
        edge_margin = float(input("Enter edge margin in inches: "))
        row_margin = float(input("Enter row margin in inches: "))
        col_margin = float(input("Enter column margin in inches: "))

        num_parts, num_parts_rotated = sheetmetal_calc(
            sheet_width,
            sheet_length,
            part_width,
            part_length,
            edge_margin,
            row_margin,
            col_margin,
        )

        print("\n")
        print("Number of parts (no rotation) = ", num_parts)
        print("Number of parts (with 45-degree rotation) = ", num_parts_rotated)

        return

    def _bendcalc(self) -> None:
        length = float(input("Enter length in inches: "))
        width = float(input("Enter width in inches: "))
        thickness = float(input("Enter thickness in inches: "))
        bend_angle = float(input("Enter the degree og thickness bend angle: "))
        inner_radius = float(input("Enter inner radius in inches: "))
        k_factor = float(input("Enter k-factor in inches: "))
        tensile_strength = float(input("Enter tensile strenght in psi: "))
        die_opening = float(input("Enter die opening in inches: "))

        bend_allowance, k_factor_calculated, tonnage = bend_calc(
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
        )

        print("\n")
        print("Bend allowance = ", bend_allowance, "inches")
        print("K-factor = ", k_factor_calculated)
        print("Tonnage required = ", tonnage, "tons")

        return

    def menu(self, option: int) -> None:
        options = {1: self._lathecalc, 2: self._sheetmetalcalc, 3: self._bendcalc}
        try:
            options[option]()
        except KeyError:
            print("Invalid selection")

    def run(self) -> None:
        try:
            while True:
                print("\n")
                print("Select module to run:")
                print("1. Lathe Calculator")
                print("2. Sheet Metal Calculator")
                print("3. Bend Calculator")
                print("\n")

                selection = int(input("Enter selection: "))
                print("\n")
                self.menu(selection)
        except KeyboardInterrupt:
            print("Program interrupted by user")


if __name__ == "__main__":
    Menu().run()
