#!/usr/bin/python3

"""
Module for determining if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): The data set represented by a list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    # Number of bytes to expect for the next character based on the first byte
    num_bytes_to_expect = 0

    for byte in data:
        # Check if the current byte starts a new character
        if num_bytes_to_expect == 0:
            # Determine the number of bytes expected for the new character
            if byte & 0b10000000 == 0:
                # Single-byte character
                num_bytes_to_expect = 0
            elif byte & 0b11100000 == 0b11000000:
                # Two-byte character
                num_bytes_to_expect = 1
            elif byte & 0b11110000 == 0b11100000:
                # Three-byte character
                num_bytes_to_expect = 2
            elif byte & 0b11111000 == 0b11110000:
                # Four-byte character
                num_bytes_to_expect = 3
            else:
                # Invalid starting byte for a character
                return False
        else:
            # Check if the current byte is a continuation byte
            if byte & 0b11000000 == 0b10000000:
                # Valid continuation byte, move to the next byte of the character
                num_bytes_to_expect -= 1
            else:
                # Invalid continuation byte
                return False

    # Check if all characters are complete (num_bytes_to_expect is 0)
    return num_bytes_to_expect == 0
