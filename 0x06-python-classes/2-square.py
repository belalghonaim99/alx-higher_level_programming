#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize New Square

        Arg: Size (int): the size of New Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
