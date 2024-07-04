"""
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False

"""

def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    opened = [False] * n  # Keep track of which boxes have been opened
    opened[0] = True  # The first box is always open
    keys = boxes[0]  # Start with the keys from the first box

    # Use a queue to manage keys we have found
    queue = keys

    while queue:
        new_keys = []
        for key in queue:
            if key < n and not opened[key]:  # If key is valid and the box is not opened
                opened[key] = True  # Mark the box as opened
                new_keys.extend(boxes[key])  # Add keys from the newly opened box
        queue = new_keys  # Update queue with new keys to process

    # Check if all boxes have been opened
    return all(opened)
