import math
from typing import Tuple


def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_speed(rpm=None, sfm=None, d=None):
    if rpm is None or sfm is None or d is None:
        # handle missing parameters
        return None
    speed = (rpm * sfm) / (3.82 * d)
    return speed

def calculate_sfm(rpm=None, d=None):
    if rpm is None or d is None:
        return None
    sfm = (3.82 * rpm * d) / 12
    return sfm

def calculate_feed(rpm=None, fpt=None, z=None):
    if rpm is None or fpt is None or z is None:
        return None
    feed = rpm * fpt * z
    return feed

def calculate_ipt(ipm=None, rpm=None, z=None):
    if ipm is None or rpm is None or z is None:
        return None
    ipt = (ipm * 12) / (rpm * z)
    return ipt

def calculate_mrr(ipm=None, woc=None, doc=None):
    if ipm is None or woc is None or doc is None:
        return None
    mrr = ipm * woc * doc
    return mrr

def calculate_afpt(ipm=None, d=None, woc=None):
    if ipm is None or d is None or woc is None:
        return None
    afpt = (ipm * 12) / (d * woc)
    return afpt

def calculate_hp(mrr=None, mf=None):
    if mrr is None or mf is None:
        return None
    hp = (mrr * mf) / 33000
    return hp

def speed_feed():
    rpm = None
    ipm = None
    sfm = None
    d = 0.0  # Initialize d to a default value

    while rpm is None or ipm is None or sfm is None:
        rpm_input = input("Enter RPM (leave blank if unknown): ")
        ipm_input = input("Enter IPM (leave blank if unknown): ")
        sfm_input = input("Enter SFM (leave blank if unknown): ")

        if rpm_input:
            rpm = float(rpm_input)
        if ipm_input:
            ipm = float(ipm_input)
        if sfm_input:
            sfm = float(sfm_input)

        d = get_input("Enter D: ")

        rpm = calculate_speed(rpm, sfm, d)
        sfm = calculate_sfm(rpm, d)

    fpt = get_input("Enter FPT: ")
    z = get_input("Enter Z: ")
    woc = get_input("Enter WOC: ")
    doc = get_input("Enter DOC: ")

    ipm = calculate_feed(rpm, fpt, z)
    ipt = calculate_ipt(ipm, rpm, z)
    mrr = calculate_mrr(ipm, woc, doc)
    afpt = calculate_afpt(ipm, d, woc)

    mf_values = {
        "steel": 1,
        "gray iron": 0.65,
        "aluminum": 0.3
    }

    mf = get_input("Enter mf value (steel=1, gray iron=0.65, aluminum=0.3): ")
    hp = calculate_hp(mrr, mf)

    print(f"RPM: {rpm:.5f}")
    print(f"IPM: {ipm:.5f}")
    print(f"SFM: {sfm:.5f}")
    print(f"IPT: {ipt:.5f}")
    print(f"MRR: {mrr:.5f}")
    print(f"AFPT: {afpt:.5f}")
    print(f"HP: {hp:.5f}")
