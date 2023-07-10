#!/usr/bin/python3
"""
the method is_same_class"""




def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the class ; otherwise False"""

    if type(obj) == a_class:
        return True
    return False
