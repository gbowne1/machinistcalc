# User inputs
diameter = float(input("Enter workpiece diameter in inches: "))
surface_speed = float(input("Enter surface speed in SFM: "))
feed_rate = float(input("Enter feed rate in inches per revolution: "))
number_of_teeth = int(input("Enter number of teeth on cutting tool: "))
spindle_speed = (surface_speed * 12) / (3.14159265359 * diameter)
chip_load = feed_rate / (number_of_teeth * spindle_speed)

# Output results
print("Spindle speed = ", spindle_speed, "RPM")
print("Chip load = ", chip_load, "in/tooth")
