#!/usr/bin/python3

"""Module that calculates the island perimeter."""


def island_perimeter(grid):
    """Calculates the island perimeter.

    Args:
        grid: A list of lists of integers representing the island.
              0 represents water, 1 represents land.

    Returns:
        The perimeter of the island as an integer.

    Raises:
        ValueError: If the grid dimensions exceed the limit (100x100).
    """

    rows, cols = len(grid), len(grid[0])
    if rows > 100 or cols > 100:
        raise ValueError("Grid dimensions exceed the limit (100x100)")

    num_land_boxes = 0
    removed_lines = 0
    for row in range(rows):
        for col in range(cols):
            current_box = grid[row][col]
            if current_box == 0:
                continue  # Skip water cells

            num_land_boxes += 1
            if col > 0 and grid[row][col - 1] == 1:  # Check left neighbor
                removed_lines += 1
            if col < cols - 1 and grid[row][col + 1] == 1:
                removed_lines += 1
            if row > 0 and grid[row - 1][col] == 1:  # Check upper neighbor
                removed_lines += 1
            if row < rows - 1 and grid[row + 1][col] == 1:
                removed_lines += 1

    area = num_land_boxes * 4
    perimeter = area - removed_lines
    return perimeter
