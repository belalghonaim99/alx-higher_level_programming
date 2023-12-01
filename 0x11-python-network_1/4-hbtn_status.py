#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status
You must use the package requests
"""


if __name__ == "__main__":
    from requests import get

    requests_content = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(requests_content.text.__class__))
    print("\t- content: {}".format(requests_content.text))