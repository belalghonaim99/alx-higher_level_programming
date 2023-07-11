#!/usr/bin/python3
"""define JSON file to write func"""
import json


def save_to_json_file(my_obj, filename):
    """write object to text file using JSON represent"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
