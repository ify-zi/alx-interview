#!/usr/bin/python3
""" function that check if a key can unlock all box"""

def canUnlockAll(boxes):
    """ lockbox algorithm """
    length = len(boxes)
    i = 0
    opened = []
    keyVal = len(boxes[0])
    while i <= length:
        for box in boxes:
            key = len(box)
            if key <= keyVal:
                opened.append('True')
            else:
                opened.append('False')
        i += 1

    for bool in opened:
        if bool == 'False':
            return False

    return True
