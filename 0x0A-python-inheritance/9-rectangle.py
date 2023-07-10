#!/usr/bin/python3
"""define Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize New Rectangle

        Args:width (int): width of New rectangle
            height (int): height of New rectangle """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return print() and str() represent of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
