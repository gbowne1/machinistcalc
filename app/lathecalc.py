import math


def lathe_calc(diameter, surface_speed, feed_rate, number_of_teeth):
    # Calculate spindle speed
    spindle_speed = (surface_speed * 12) / (math.pi * diameter)

    # Calculate cutting speed
    cutting_speed = spindle_speed * math.pi * diameter

    # Calculate feed rate
    feed_rate = feed_rate * spindle_speed * number_of_teeth

    # Calculate chip load
    chip_load = feed_rate / (number_of_teeth * spindle_speed)

    # Print results
    print("Spindle speed: {:.2f} RPM".format(spindle_speed))
    print("Cutting speed: {:.2f} feet per minute".format(cutting_speed))
    print("Feed rate: {:.4f} inches per minute".format(feed_rate))
    print("Chip load: {:.4f} inches per tooth".format(chip_load))
