#!/usr/bin/python3
"""define a class Square"""


class Square:
    """represent a Square"""

    def __init__(self, size):
        """Initialize a New Square
        Args: Size (int): the Size of New Square"""
        self.size = size

    @property
    def size(self):
        """ Retrieve or Set the Current Size of the Square"""
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

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
