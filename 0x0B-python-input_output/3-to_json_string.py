#!/usr/bin/python3
"""define string to json function"""
import json


def to_json_string(my_obj):
    """return the JSON Represent of string object """
    return json.dumps(my_obj)
