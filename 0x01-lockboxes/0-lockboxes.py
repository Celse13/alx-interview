#!/usr/bin/python3
""" Function for lock-boxes """


def can_unlock_all(boxes):
    """ Doc """
    if not boxes or len(boxes) == 0:
        return False
    reachable_boxes = [0]
    for box in reachable_boxes:
        for new_box in boxes[box]:
            if new_box not in reachable_boxes and new_box < len(boxes):
                reachable_boxes.append(new_box)
    if len(reachable_boxes) == len(boxes):
        return True
    return False
