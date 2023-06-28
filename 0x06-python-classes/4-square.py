#!/usr/bin/python3
"""define a class Of Square"""


class Square:
    """represent a Square"""

    def __init__(self, size=0):
        """initialize New Square
        Args: Size (int): the Size of New Square"""
        self.size = size

    @property
    def size(self):
        """ retrieve or set current size of Squar"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
