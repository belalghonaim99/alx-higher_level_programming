#!/usr/bin/python3
"""define a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init new Rectangle

        Args:
            width int: width of the new Rectangle
            height int: The height of the new Rectangle
            x int: The x coordinate of the new Rectangle
            y int: The y coordinate of the new Rectangle
            id int: The identity of the new Rectangle
        Raises:
            TypeError: if either of width or height is not an int.
            ValueError: if either of width or height <= 0.
            TypeError: if either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set or get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set or get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set or get the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set orget the [y] coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """print () the Rectangle using the hashtag character """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for y in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for f in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updated the Rectangle

        Args:
            *args ints: New attribute values.
                first argument represent id attribute
                sec argument represent width attribute
                third argument represent height attribute
                fourth argument represent x attribute
                fifth argument represent y attribute
            **kwargs dict: the new key or value pairs of attributes """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return the dictionary represent of the Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """return the print and str() represent of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"
    .format(self.id, self.x, self, self.width, self.height)
