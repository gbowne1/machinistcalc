from app.bendcalc import bend_calc
from app.lathecalc import lathe_calc
from app.punchtonnage import punch_tonnage
from app.sheetmetalcalc import sheetmetal_calc
from app.speedfeed import (calculate_afpt, calculate_feed, calculate_hp,
                           calculate_ipt, calculate_mrr, calculate_sfm,
                           calculate_speed, speed_feed)


def menu():
    while True:
        print("Select a calculator:")
        print("1. Bend Calculator")
        print("2. Lathe Calculator")
        print("3. Sheet Metal Calculator")
        print("4. Speed and Feed Calculator")
        print("5. Punch Tonnage Calculator")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            length = float(input("Enter length in inches: "))
            width = float(input("Enter width in inches: "))
            thickness = float(input("Enter thickness in inches: "))
            bend_angle = float(input("Enter bend angle in degrees: "))
            inner_radius = float(input("Enter inner radius in inches: "))
            k_factor = float(input("Enter K-factor: "))
            tensile_strength = float(input("Enter tensile strength in pounds per square inch: "))
            die_opening = float(input("Enter die opening in inches: "))

            # Call the bend_calc function and capture the calculated values
            bend_allowance, k_factor_calculated, tonnage = bend_calc(
                length, width, thickness, bend_angle, inner_radius, k_factor, tensile_strength, die_opening
            )

            # Now you can use the calculated values as needed
            print("Bend Allowance:", bend_allowance)
            print("K-Factor Calculated:", k_factor_calculated)
            print("Tonnage:", tonnage)

        elif choice == "2":
            diameter = float(input("Enter diameter in inches: "))
            surface_speed = float(input("Enter surface speed in feet per minute: "))
            feed_rate = float(input("Enter feed rate in inches per revolution: "))
            number_of_teeth = float(input("Enter number of teeth: "))
            lathe_calc(diameter, surface_speed, feed_rate, number_of_teeth)
        if choice == "3":
            sheet_width = float(input("Enter sheet width in inches: "))
            sheet_length = float(input("Enter sheet length in inches: "))
            part_width = float(input("Enter part width in inches: "))
            part_length = float(input("Enter part length in inches: "))
            edge_margin = float(input("Enter edge margin in inches: "))
            row_margin = float(input("Enter row margin in inches: "))
            col_margin = float(input("Enter column margin in inches: "))
            num_parts_needed = int(input("Enter the number of parts needed: "))
            num_sheets_supplied = int(input("Enter the number of sheets supplied: "))

            # Call the sheetmetal_calc function and capture the calculated values
            num_parts, num_parts_rotated, num_sheets_required, num_sheets_remaining = sheetmetal_calc(
                sheet_width,
                sheet_length,
                part_width,
                part_length,
                edge_margin,
                row_margin,
                col_margin,
                num_parts_needed,
                num_sheets_supplied,
            )

            # Print the calculated values
            print("Number of parts:", num_parts)
            print("Number of parts with 45-degree rotation:", num_parts_rotated)
            print("Number of sheets required:", num_sheets_required)
            print("Number of sheets remaining:", num_sheets_remaining)
        elif choice == "4":
            speed_feed()
        elif choice == "5":
            punch_tonnage()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
