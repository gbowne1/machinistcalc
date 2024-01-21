from app.bendcalc import bend_calc
from app.lathecalc import lathe_calc
from app.punchtonnage import punch_tonnage
from app.sheetmetalcalc import sheetmetal_calc
from app.speedfeed import (calculate_afpt, calculate_feed, calculate_hp,
                           calculate_ipt, calculate_mrr, calculate_sfm,
                           calculate_speed, speed_feed)
from app.boltcircle import bolt_circle


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
            # Call the bend calculator function from bendcalc.py
            bend_calc()
        elif choice == "2":
            # Call the lathe calculator function from lathecalc.py
            lathe_calc()
        elif choice == "3":
            # Call the lathe calculator function from lathecalc.py
            sheetmetal_calc()
        elif choice == "4":
            # Call the speed and feed calculator function from speedfeed.py
            calculate_afpt()
            calculate_feed()
            calculate_hp()
            calculate_ipt()
            calculate_mrr()
            calculate_speed()
            calculate_sfm()
            speed_feed()
            # Add other functions as needed
        elif choice == "5":
            # Call the lathe calculator function from lathecalc.py
            punch_tonnage()
        elif choice == "6":
            # Call the lathe calculator function from lathecalc.py
            bolt_circle()
        elif choice == "7":
            print("Quitting the application")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
