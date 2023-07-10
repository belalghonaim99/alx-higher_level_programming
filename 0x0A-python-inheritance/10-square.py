#!/usr/bin/python3
"""define subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """initialize New square
        Args: Size (int): size of new Square
        size must be int"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
