#!/usr/bin/python3
"""Method that determines data set represents a valid UTF-8 encodin"""


def validUTF8(data):
    """Initialise UTF-8 encoding"""
    pre_bytes = 0

    for byte in data:

        if pre_bytes == 0:
            if (byte >> 5) == 0b110:
                pre_bytes = 1
            elif (byte >> 4) == 0b1110:
                pre_bytes = 2
            elif (byte >> 3) == 0b11110:
                pre_bytes = 3
            elif (byte >> 7) != 0:
                return True

        elif (byte >> 6) != 0b10:
            return False

        else:
            pre_bytes -= 1
    return pre_bytes == 0
