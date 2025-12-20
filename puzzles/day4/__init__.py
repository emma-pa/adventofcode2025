import numpy as np
from numpy.typing import NDArray


def resolve_grid(grid: NDArray) -> NDArray:
    """1 means roll can be taken, 0 means can't be taken or no rolls is on the position."""
    grid_shape_x, grid_shape_y = grid.shape
    resolved_grid = grid.copy()

    for y in range(grid_shape_y):
        for x in range(grid_shape_x):
            roll_position = grid[y, x]
            # print(f"Position ({y},{x}): {roll_position}")
            is_roll = roll_position == 1
            if not is_roll:
                continue

            x_start = max(x - 1, 0)
            x_end = min(x + 2, grid_shape_x)
            y_start = max(y - 1, 0)
            y_end = min(y + 2, grid_shape_y)

            window = grid[y_start:y_end, x_start:x_end]
            # print(window)

            nof_rolls_in_window = (
                window.sum() - roll_position
            )  # Remove the roll if any to avoid counting it twice

            # Roll can be taken only if there are less than 4 rolls in the 8 adjacent positions
            if nof_rolls_in_window < 4:
                resolved_grid[y, x] = 1
            else:
                resolved_grid[y, x] = 0

    return resolved_grid


def count_accessible_rolls(resolved_grid: NDArray) -> int:
    return resolved_grid.sum()


def parse_shelves(shelves: list[str]) -> NDArray:
    """Replace . with 0 and @ with 1 and convert to np.array for conveniency."""
    parsed_grid: list[list[int]] = []

    for row in shelves:
        row = row.replace(".", "0").replace("@", "1")
        row = [int(position) for position in row]
        parsed_grid.append(row)

    np_parsed_grid = np.array(parsed_grid)
    return np_parsed_grid
