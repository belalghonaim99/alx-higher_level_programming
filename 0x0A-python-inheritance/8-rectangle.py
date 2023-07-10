#!/usr/bin/python3
"""define class rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent a Rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle

        Args: width (int): width of the New rectangle
              height (int): height of the New rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
