#!/usr/bin/python3
""" Write a Python script that takes in a URL, sends a request to the URL
displays the value of the X-Request-Id
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as web:
        header = web.headers.get('X-Request-Id')
        print(header)
