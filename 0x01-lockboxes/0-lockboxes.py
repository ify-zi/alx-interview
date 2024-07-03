#!/usr/bin/python3
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    """lockbox algo
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
