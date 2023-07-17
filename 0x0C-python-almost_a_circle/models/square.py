#!/usr/bin/python3
"""defines Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init a new Square
        Args:
            Size of int: The size of new Square
            x of int: x coordinate of new Square
            y of int: y coordinate of new Square
            id of int: identity of new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get or set the size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the Square
        Args:
            *args ints: New attribute values.
                first argument represents the id of the attribute
                Second argument represent the size of the attribute
                Third argument represent x of the attribute
                Fourth argument represent y of the attribute
            **kwargs dict: New key or value pairs of the attributes"""
        if args and len(args) != 0:
            B = 0
            for arg in args:
                if B == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif B == 1:
                    self.size = arg
                elif B == 2:
                    self.x = arg
                elif B == 3:
                    self.y = arg
                B += 1

        elif kwargs and len(kwargs) != 0:
            for W, i in kwargs.items():
                if W == "id":
                    if i is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = i
                elif W == "size":
                    self.size = i
                elif W == "x":
                    self.x = i
                elif W == "y":
                    self.y = i

    def to_dictionary(self):
        """Return the dictionary represent of the new Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
