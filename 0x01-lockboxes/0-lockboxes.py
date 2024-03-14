#!/usr/bin/python3
""" Function for lock-boxes """


def canUnlockAll(boxes):
    """ Unlocking the boxes """
    if not boxes or len(boxes) == 0:
        return False
    k = [0]
    for key in k:
        for new_key in boxes[key]:
            if new_key not in k and new_key < len(boxes):
                keys.append(new_key)
    if len(k) == len(boxes):
        return True
    return False
