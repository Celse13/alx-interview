#!/usr/bin/python3
"""validUTF8 module"""


def validUTF8(data):
    """validUTF8 function"""
    byte_count = 0
    bit_mask_1 = 1 << 7
    bit_mask_2 = 1 << 6

    for number in data:
        bit_mask = 1 << 7
        if byte_count == 0:
            while bit_mask & number:
                byte_count += 1
                bit_mask = bit_mask >> 1

            if byte_count == 0:
                continue

            if byte_count == 1 or byte_count > 4:
                return False
        else:
            if not (number & bit_mask_1 and not (number & bit_mask_2)):
                return False
        byte_count -= 1
    return byte_count == 0
