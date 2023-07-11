#!/usr/bin/python3
"""define JSON to object func"""
import json


def from_json_string(my_str):
    """return Python object represent of JSON string"""
    return json.loads(my_str)
