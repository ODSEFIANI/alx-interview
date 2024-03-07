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
                pass  # Skip water cells

            if current_box == 1:
                num_land_boxes += 1
                if col > 0 and grid[row][col - 1] == 1:  # Check left neighbor
                    removed_lines += 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    removed_lines += 1
                if row > 0 and grid[row - 1][col] == 1:  # Check upper neighbor
                    removed_lines += 1
                if row < rows - 1 and grid[row + 1][col] == 1:
                    removed_lines += 1
                if (
                    col > 0 and grid[row][col - 1] == 0 and
                    col < cols - 1 and grid[row][col + 1] == 0 and
                    row > 0 and grid[row - 1][col] == 0 and
                    row < rows - 1 and grid[row + 1][col] == 0
                ):
                    raise ValueError("normal isolated island")
                if col == 0:
                    # Check top, bottom, and right for cells on the extreme left
                    if (
                        row > 0 and grid[row - 1][col] == 0 and
                        row < rows - 1 and grid[row + 1][col] == 0 and
                        col < cols - 1 and grid[row][col + 1] == 0
                    ):
                        raise ValueError("Isolated cell at the extreme left position.")

                elif col == cols - 1:
                    # Check top, bottom, and left for cells on the extreme right
                    if (
                        row > 0 and grid[row - 1][col] == 0 and
                        row < rows - 1 and grid[row + 1][col] == 0 and
                        col > 0 and grid[row][col - 1] == 0
                    ):
                        raise ValueError("Isolated cell at the extreme right position.")

                elif row == 0:
                    # Check left, right, and bottom for cells at the top
                    if (
                        col > 0 and grid[row][col - 1] == 0 and
                        col < cols - 1 and grid[row][col + 1] == 0 and
                        row < rows - 1 and grid[row + 1][col] == 0
                    ):
                        raise ValueError("Isolated cell at the top position.")

                elif row == rows - 1:
                    # Check left, right, and top for cells at the bottom
                    if (
                        col > 0 and grid[row][col - 1] == 0 and
                        col < cols - 1 and grid[row][col + 1] == 0 and
                        row > 0 and grid[row - 1][col] == 0
                    ):
                        raise ValueError("Isolated cell at the bottom position.")

    # Check for corner positions
    if grid[0][0] == 1 and grid[0][1] == 0 and grid[1][0] == 0:
        raise ValueError("Isolated cell at the top-left corner.")

    if grid[0][cols - 1] == 1 and grid[0][cols - 2] == 0 and grid[1][cols - 1] == 0:
        raise ValueError("Isolated cell at the top-right corner.")

    if grid[rows - 1][0] == 1 and grid[rows - 1][1] == 0 and grid[rows - 2][0] == 0:
        raise ValueError("Isolated cell at the bottom-left corner.")

    if grid[rows - 1][cols - 1] == 1 and grid[rows - 1][cols - 2] == 0 and grid[rows - 2][cols - 1] == 0:
        raise ValueError("Isolated cell at the bottom-right corner.")

    area = num_land_boxes * 4
    perimeter = area - removed_lines
    return perimeter

