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


# Typing??
def remove_roll(position):
    if position >= 2:
        return 0
    else:
        return position


# This function doesn't do any assert if position in grid is 1 and position in resoled_grid is 1 as well, but it should, as this condition is necessary, otherwise there is a bug
# Might make things hard to debug
def remove_rolls_from_grid(grid: NDArray, resolved_grid: NDArray) -> NDArray:
    """Use resolved_grid as a mask on the original grid to remove the rolls where position in mask is 1.
    Removing a roll means changing the a 1 in the original grid into a 0.
    """
    v_remove_roll = np.vectorize(remove_roll)
    remove_rolls_grid = grid + resolved_grid
    remove_rolls_grid = v_remove_roll(remove_rolls_grid)
    return remove_rolls_grid


# TODO: Try with recursion
def remove_rolls(grid: NDArray) -> int:
    """Remove rolls until count_accessible_rolls is 0"""
    resolved_grid = resolve_grid(grid)
    accessible_rolls = count_accessible_rolls(resolved_grid)
    total_removed_rolls = 0

    while accessible_rolls > 0:
        grid = remove_rolls_from_grid(grid, resolved_grid)
        total_removed_rolls += accessible_rolls
        resolved_grid = resolve_grid(grid)
        accessible_rolls = count_accessible_rolls(resolved_grid)

    return total_removed_rolls
