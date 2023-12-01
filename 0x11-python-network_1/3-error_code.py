#!/usr/bin/python3
"""You have to manage urllib.error.
HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""


from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as body:
            print(body.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code:', error.code)
