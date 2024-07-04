#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

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
    # Total number of boxes
    n = len(boxes)
    # Keep track of which boxes have been opened
    opened = [False] * n
    # The first box is always open
    opened[0] = True
    # Start with the keys from the first box
    keys = boxes[0]

    # Use a queue to manage keys we have found
    queue = keys

    while queue:
        new_keys = []
        for key in queue:
            # If key is valid and the box is not opened
            if key < n and not opened[key]:
                # Mark the box as opened
                opened[key] = True
                # Add keys from the newly opened box
                new_keys.extend(boxes[key])
        # Update queue with new keys to process
        queue = new_keys

    # Check if all boxes have been opened
    return all(opened)
