from app.bendcalc import bend_calc
from app.boltcircle import bolt_circle
from app.lathecalc import lathe_calc
from app.punchtonnage import punch_tonnage
from app.sheetmetalcalc import sheetmetal_calc
from app.lathecalc import lathe_calc
from app.millingcalc import milling_calc

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
            bend_calc()
        elif choice == "2":
            lathe_calc()
        elif choice == "3":
            sheetmetal_calc()
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

