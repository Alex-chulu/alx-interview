#!/usr/bin/python3
"""
island_perimeter - Calculates the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
    - grid: A list of lists of integers where 0 represents water and 1 represents land.

    Returns:
    - The perimeter of the island.
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4  # Start with 4 edges

                # Check the adjacent cells (up, down, left, and right)
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1  # Subtract 1 if there's land above
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1  # Subtract 1 if there's land below
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1  # Subtract 1 if there's land to the left
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1  # Subtract 1 if there's land to the right

    return perimeter
