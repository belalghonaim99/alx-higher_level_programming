#!/usr/bin/python3
"""define a fun"""

def read_file(filename=""):
    """print content of UTF8 Text File it to stdout"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
