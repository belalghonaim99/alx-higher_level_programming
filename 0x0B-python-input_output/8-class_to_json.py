#!/usr/bin/python3
"""define python class to JSON func"""


def class_to_json(obj):
    """return the dictionary Represnt of Simple data Structure"""
    return obj.__dict__
