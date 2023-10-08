#!/usr/bin/python3
"""
Determines if all the boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
    - boxes (list of lists): A list of lists representing boxes and keys.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    visited = [False] * len(boxes)
    visited[0] = True  # The first box is unlocked by default
    
    stack = [0]  # Start with the first box
    
    while stack:
        current_box = stack.pop()
        
        # Check the keys in the current box
        for key in boxes[current_box]:
            if key >= 0 and key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)
    
    # Check if all boxes have been visited
    return all(visited)

