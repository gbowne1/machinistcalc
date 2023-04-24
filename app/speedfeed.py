import machinistcalc as main

def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_app():
    rpm = None
    ipm = None
    sfm = None

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

        rpm = main.calculate_speed(rpm, sfm, d)
        sfm = main.calculate_sfm(rpm, d)

    fpt = get_input("Enter FPT: ")
    z = get_input("Enter Z: ")
    woc = get_input("Enter WOC: ")
    doc = get_input("Enter DOC: ")

    ipm = main.calculate_feed(rpm, fpt, z)
    ipt = main.calculate_ipt(ipm, rpm, z)
    mrr = main.calculate_mrr(ipm, woc, doc)
    afpt = main.calculate_afpt(ipm, d, woc)

    mf_values = {
        "steel": 1,
        "gray iron": 0.65,
        "aluminum": 0.3
    }

    mf = get_input("Enter mf value (steel=1, gray iron=0.65, aluminum=0.3): ")
    hp = main.calculate_hp(mrr, mf)

    print(f"RPM: {rpm:.5f}")
    print(f"IPM: {ipm:.5f}")
    print(f"SFM: {sfm:.5f}")
    print(f"IPT: {ipt:.5f}")
    print(f"MRR: {mrr:.5f}")
    print(f"AFPT: {afpt:.5f}")
    print(f"HP: {hp:.5f}")

if __name__ == "__main__":
    main_app()