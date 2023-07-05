#!/usr/bin/python3
"""1-rectangle"""


class Rectangle:
    """in this task the class We create private instance attributes by taking in two arguments
    Args:
        width (int): width_horizontal of Rectangle must be 0
        height (int): height_vertical of Rectangle must be 0 """

    def __init__(self, width=0, height=0):
        """attribute must be defined below"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter

        Return: width (int): width_horizontal of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): Value of Rectangle

        attributes:
            __width (int): width_horizontal of rectangle
            raise:
                  TypeError: If value is not an int
                  valueError: If value is less than 0
            """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """__height getter
        Return: __height (int): height_vertical of Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Args: value int: value of Rectangle
        Attributes: _height int: height_vertical of Rectangle
        raises: 
             TypeError if value not int
             valueErorr if value less than 0 
             """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
