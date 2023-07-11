#!/usr/bin/python3
"""define file writing fun"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args: filename (str): name of the file written
        text (str): Text to write the file
    Returns: the numbers of characters has written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
