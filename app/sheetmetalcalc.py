import math

# User inputs
sheet_width = float(input("Enter sheet width in inches: "))
sheet_length = float(input("Enter sheet length in inches: "))
part_width = float(input("Enter part width in inches: "))
part_length = float(input("Enter part length in inches: "))
edge_margin = float(input("Enter edge margin in inches: "))
row_margin = float(input("Enter row margin in inches: "))
col_margin = float(input("Enter column margin in inches: "))

# Calculate available space with margins
avail_width = sheet_width - 2 * edge_margin
avail_length = sheet_length - 2 * edge_margin
avail_rows = math.floor(avail_length / (part_length + row_margin))
avail_cols = math.floor(avail_width / (part_width + col_margin))

# Calculate number of parts
num_parts = avail_rows * avail_cols

# Calculate number of parts with 45-degree rotation
num_parts_rotated = math.floor((avail_rows * avail_cols) / 2)

# Output results
print("Number of parts (no rotation) = ", num_parts)
print("Number of parts (with 45-degree rotation) = ", num_parts_rotated)