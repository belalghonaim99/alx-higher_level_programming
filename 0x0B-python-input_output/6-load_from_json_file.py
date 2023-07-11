#!/usr/bin/python3
"""define JSON file to reading a func"""
import json


def load_from_json_file(filename):
    """create Python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
