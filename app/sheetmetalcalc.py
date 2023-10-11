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
    num_parts_needed: int,
    num_sheets_supplied: int,
) -> Tuple[int, int, int, int]:
    # Calculate available space with margins
    avail_width = sheet_width - 2 * edge_margin
    avail_length = sheet_length - 2 * edge_margin
    avail_rows = math.floor(avail_length / (part_length + row_margin))
    avail_cols = math.floor(avail_width / (part_width + col_margin))

    # Calculate number of parts
    num_parts = avail_rows * avail_cols

    # Calculate number of parts with 45-degree rotation
    num_parts_rotated = math.floor((avail_rows * avail_cols) / 2)

    # Calculate the number of sheets required to obtain the required number of parts
    num_sheets_required = math.ceil(num_parts_needed / num_parts)

    # Calculate the number of sheets remaining after supplying the required number of parts
    num_sheets_remaining = num_sheets_supplied - num_sheets_required

    return num_parts, num_parts_rotated, num_sheets_required, num_sheets_remaining
