#!/usr/bin/python3
"""define a fun to write a file"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
        Args: filename (str): name of file to write
        text (str): text to write the file
    Returns: The numbers of characters been written """
    with open(filename, "w", encoding="utf-8") as f:
         return f.write(text)
