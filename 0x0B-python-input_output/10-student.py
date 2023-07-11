#!/usr/bin/python3
"""define class Student"""


class Student:
    """represent Student"""

    def __init__(self, first_name, last_name, age):
        """init New Student
        Args: first_name (str): First name of student
            last_name (str): Last name of student
            age (int): Age of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary represent of Student
        Args:attrs list: Optional attributes to represent"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
