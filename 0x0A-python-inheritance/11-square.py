#!/usr/bin/python3
"""define Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent Square"""

    def __init__(self, size):
        """initialize a new square
        Args: Size (int): Size of New Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
