#!/usr/bin/python3
"""define class Student"""


class Student:
    """Represent a Student"""

    def __init__(self, first_name, last_name, age):
        """init new Student
        Args: first_name (str): First name of Student
            last_name (str): Last name of Student
            age (int): Age of  Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get dictionary Represent of Student
        Args: attrs List: Attributes of Represent"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of Student
        Args: json dict: key or value pairs to replace Attributes"""
        for k, v in json.items():
            setattr(self, k, v)
