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
            bend_calc(length, width, thickness, bend_angle, inner_radius, k_factor, tensile_strength, die_opening)
        elif choice == "2":
            lathe_calc(diameter, surface_speed, feed_rate, number_of_teeth)
        elif choice == "3":
            sheet_width = float(input("Enter sheet width in inches: "))
            sheet_length = float(input("Enter sheet length in inches: "))
            part_width = float(input("Enter part width in inches: "))
            part_length = float(input("Enter part length in inches: "))
            edge_margin = float(input("Enter edge margin in inches: "))
            row_margin = float(input("Enter row margin in inches: "))
            col_margin = float(input("Enter column margin in inches: "))
            sheetmetal_calc(sheet_width, sheet_length, part_width, part_length, edge_margin, row_margin, col_margin)
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
