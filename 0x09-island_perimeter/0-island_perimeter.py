#!/usr/bin/python3
"""
module that calculates the island permietre
"""


def island_perimeter(grid):
    """
    calculates the island permietre

    parametres:
        grid : represents the island
    return : int value (perimter of given island)

    """
    nb_box = 0
    removed_lines = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            current_box = grid[row][col]
            if current_box == 0:
                pass
            else:
                nb_box += 1
                if grid[row][col - 1] == 1:
                    removed_lines += 1
                if grid[row][col + 1] == 1:
                    removed_lines += 1
                if grid[row - 1][col] == 1:
                    removed_lines += 1
                if grid[row + 1][col] == 1:
                    removed_lines += 1
    area = nb_box*4
    perimeter = area - removed_lines
    return perimeter
