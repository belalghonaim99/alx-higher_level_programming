#!/usr/bin/python3
"""define class Student"""


class Student:
    """represent student"""

    def __init__(self, first_name, last_name, age):
        """init New student
        Args: first_name (str): First name of Student
            last_name (str): Last name of Student
            age (int): Age of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get dictionary represent of Student"""
        return self.__dict__
