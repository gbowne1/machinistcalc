from app.bendcalc import bend_calc
from app.lathecalc import lathe_calc
from app.sheetmetalcalc import sheetmetal_calc
from app.speedfeed import speed_feed
from app.speedfeed import calculate_speed, calculate_sfm, calculate_feed, calculate_ipt, calculate_mrr, calculate_afpt, calculate_hp

def menu():
    while True:
        print("Select a calculator:")
        print("1. Bend Calculator")
        print("2. Lathe Calculator")
        print("3. Sheet Metal Calculator")
        print("4. Speed and Feed Calculator")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bend_calc()
        elif choice == "2":
            lathe_calc()
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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
