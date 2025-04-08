from app.bendcalc import bend_calc
from app.boltcircle import bolt_circle
from app.lathecalc import lathe_calc
from app.millingcalc import milling_calc
from app.punchtonnage import punch_tonnage
from app.sheetmetalcalc import sheetmetal_calc


def menu():
    while True:
        print("Select a calculator:")
        print("1. Bend Calculator")
        print("2. Lathe Calculator")
        print("3. Sheet Metal Calculator")
        print("4. Speed and Feed Calculator")
        print("5. Punch Tonnage Calculator")
        print("6. Bolt Circle Calculator")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            thickness = float(input("Enter the thickness: "))
            bend_angle = float(input("Enter the bend angle: "))
            inner_radius = float(input("Enter the inner radius: "))
            k_factor = float(input("Enter the k-factor: "))
            tensile_strength = float(input("Enter the tensile strength: "))
            die_opening = float(input("Enter the die opening: "))
            bend_calc(length, width, thickness, bend_angle, inner_radius, k_factor, tensile_strength, die_opening)
        elif choice == "2":
            lathe_calc()
        elif choice == "3":
            sheet_width = float(input("Enter the sheet width: "))
            sheet_length = float(input("Enter the sheet length: "))
            part_width = float(input("Enter the part width: "))
            part_length = float(input("Enter the part length: "))
            edge_margin = float(input("Enter the edge margin: "))
            row_margin = float(input("Enter the row margin: "))
            col_margin = float(input("Enter the column margin: "))
            num_parts_needed = int(input("Enter the number of parts needed: "))
            num_sheets_supplied = int(input("Enter the number of sheets supplied: "))
            sheetmetal_calc(sheet_width, sheet_length, part_width, part_length, edge_margin, row_margin, col_margin, num_parts_needed, num_sheets_supplied)
        elif choice == "4":
            milling_calc()
        elif choice == "5":
            punch_tonnage()
        elif choice == "6":
            diameter = float(input("Enter the diameter of the bolt circle: "))
            num_holes = int(input("Enter the number of holes: "))
            coordinates = bolt_circle(diameter, num_holes)
            for i, (x, y) in enumerate(coordinates, start=1):
                print(f"Hole {i}: ({x:.2f}, {y:.2f})")
        elif choice == "7":
            print("Quitting the application")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
    # This is the main entry point of the application.
    # The menu function is called to start the application.
    # The application will continue to run until the user chooses to quit.
    # Each calculator function is called based on the user's choice.
    # The input values are collected from the user for each calculator.
    # The results are printed to the console.
    # The application is designed to be user-friendly and interactive.
    # The user can select different calculators and perform calculations as needed.
    # The application is modular, with each calculator function defined in separate modules.
    # This allows for easy maintenance and updates to individual calculators.
    # The application is intended for use in manufacturing and engineering contexts.
    # It provides quick and accurate calculations for various machining and fabrication processes.
    # The application can be extended with additional calculators in the future.
    # The user interface is simple and intuitive, making it accessible to users with different levels of expertise.
    
    