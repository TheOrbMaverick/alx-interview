#!/usr/bin/python3
"""
Valid UTF-8
"""


def validUTF8(data):

    def is_valid_byte(byte):
        return 0 <= byte <= 255

    n = len(data)
    i = 0

    while i < n:
        byte = data[i]

        # Determine the number of bytes in the current UTF-8 character
        if byte & 0x80 == 0:
            num_bytes = 1
        elif byte & 0xE0 == 0xC0:
            num_bytes = 2
        elif byte & 0xF0 == 0xE0:
            num_bytes = 3
        elif byte & 0xF8 == 0xF0:
            num_bytes = 4
        else:
            return False

        # Check that we have enough remaining bytes
        if i + num_bytes > n:
            return False

        # Validate subsequent bytes
        for j in range(1, num_bytes):
            if data[i + j] & 0xC0 != 0x80:
                return False

        # Move to the next character
        i += num_bytes

    return True
