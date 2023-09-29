#!/usr/bin/python3
"""You have to manage urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code"""


from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as body_response:
            print(body_response.read().decode('utf-8'))
    except HTTPError as error_code:
        print('Error code:', error_code.code)