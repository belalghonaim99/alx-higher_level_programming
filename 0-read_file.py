#!/usr/bin/python3
"""define a function"""


def read_file(filename=""):
    """print the content of UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
