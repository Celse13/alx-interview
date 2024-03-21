#!/usr/bin/python3
""" Function for lock-boxes """


def canUnlockAll(boxes):
    """ Docs """
    if not boxes or len(boxes) == 0:
        return False
    kys = [0]
    for key in kys:
        for n_key in boxes[key]:
            if n_key not in kys and n_key < len(boxes):
                kys.append(n_key)
    if len(kys) == len(boxes):
        return True
    return False
