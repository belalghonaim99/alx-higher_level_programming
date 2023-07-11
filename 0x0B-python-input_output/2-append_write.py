#!/usr/bin/python3
"""defines file to append a function"""


def append_write(filename="", text=""):
    """appending a string to the end of a UTF8 text file

    Args: filename (str): name of file to append to
        text (str): string to append to file
    Returns: The number of characters appended"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
