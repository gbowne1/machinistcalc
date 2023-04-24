# User inputs
length = 12 # inches
width = 4 # inches
thickness = 0.25 # inches
bend_angle = 90 # degrees
inner_radius = 0.5 # inches
k_factor = 0.35
tensile_strength = 50000 # psi
die_opening = 1 # inches

# Convert angle to radians
angle_radians = bend_angle * (3.14159265359/180)

# Calculate bend allowance
bend_allowance = angle_radians * (inner_radius + k_factor * thickness)

# Calculate K-factor
k_factor_calculated = (bend_allowance / thickness) / (0.01745 * inner_radius + 1)

# Calculate tonnage
material_factor = 1
k_constant = 50
tonnage = (k_constant * length * thickness * tensile_strength) / (die_opening * material_factor)

# Output results
print("Bend allowance = ", bend_allowance, "inches")
print("K-factor = ", k_factor_calculated)
print("Tonnage required = ", tonnage, "tons")
