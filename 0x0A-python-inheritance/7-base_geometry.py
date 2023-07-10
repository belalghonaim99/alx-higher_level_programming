#!/usr/bin/python3
"""define base Geometry class BaseGeometry"""


class BaseGeometry:
    """reprsent base Geometry"""

    def area(self):
        """not Implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter an integer

        Args: name (str): name of the Parameter
            value (int): Parameter to Validate
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
