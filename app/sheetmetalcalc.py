import math
from typing import Tuple


def sheetmetal_calc(
    sheet_width: float,
    sheet_length: float,
    part_width: float,
    part_length: float,
    edge_margin: float,
    row_margin: float,
    col_margin: float,
) -> Tuple[float, float]:

    # Calculate available space with margins
    avail_width = sheet_width - 2 * edge_margin
    avail_length = sheet_length - 2 * edge_margin
    avail_rows = math.floor(avail_length / (part_length + row_margin))
    avail_cols = math.floor(avail_width / (part_width + col_margin))

    # Calculate number of parts
    num_parts = avail_rows * avail_cols

    # Calculate number of parts with 45-degree rotation
    num_parts_rotated = math.floor((avail_rows * avail_cols) / 2)

    return num_parts, num_parts_rotated
