import math
from typing import Tuple


def calculate_sfpm(diameter, rpm):
    sfpm = (diameter * math.pi * rpm) / 12
    return sfpm

def calculate_ipm(sfpm, feed_per_rev):
    ipm = sfpm * feed_per_rev
    return ipm

def calculate_feed_per_rev(ipr, rpm):
    feed_per_rev = ipr * rpm
    return feed_per_rev

def lathe_speed_feed_calc():
    diameter = float(input("Enter the diameter: "))
    rpm = float(input("Enter the RPM: "))
    ipr = float(input("Enter the inches per revolution: "))

    sfpm = calculate_sfpm(diameter, rpm)
    ipm = calculate_ipm(sfpm, ipr)
    feed_per_rev = calculate_feed_per_rev(ipr, rpm)

    print(f"Surface Feet per Minute: {sfpm:.2f}")
    print(f"Inches per Minute: {ipm:.2f}")
    print(f"Feed per Revolution: {feed_per_rev:.2f}")
