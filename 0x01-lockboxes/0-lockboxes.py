#!/usr/bin/python3
"""
Module for solving the canUnlockAll problem.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each inner list represents
                               a box and contains keys (positive integers) to
                               other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    n = len(boxes)  # Total number of boxes
    visited = [False] * n  # To keep track of visited boxes
    stack = [0]  # Start with the first box (box 0) as the initial stack

    visited[0] = True  # Mark the first box as visited

    while stack:
        current_box = stack.pop()  # Get the current box from the stack

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to an unvisited box
            if 0 <= key < n and not visited[key]:
                stack.append(key)  # Add the unvisited box to the stack
                visited[key] = True  # Mark it as visited

    # If all boxes have been visited, return True
    return all(visited)

