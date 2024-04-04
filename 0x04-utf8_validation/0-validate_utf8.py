#!/usr/bin/python3
"""validates UTF-8 encoding of a list of integers"""


def validUTF8(data):
    """validates UTF-8 encoding of a list of integers"""
    byte_counter = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if byte_counter == 0:
            while mask & num:
                byte_counter += 1
                mask = mask >> 1

            if byte_counter == 0:
                continue

            if byte_counter == 1 or byte_counter > 4:
                return False
        else:
            if not (num & mask_1 and not (num & mask_2)):
                return False
        byte_counter -= 1
    return byte_counter == 0
