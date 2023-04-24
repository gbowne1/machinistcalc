from app import lathecalc, sheetmetalcalc, speedfeed, bendcalc

print("Select module to run:")
print("1. Lathe Calculator")
print("2. Sheet Metal Calculator")
print("3. Speed Feed Calculator")
print("4. Bend Calculator")

selection = input("Enter selection: ")

if selection == "1":
    lathecalc.run()
elif selection == "2":
    sheetmetalcalc.run()
elif selection == "3":
    speedfeed.run()
elif selection == "4":
    bendcalc.run()
else:
    print("Invalid selection")

if __name__ == "__main__":
    main()