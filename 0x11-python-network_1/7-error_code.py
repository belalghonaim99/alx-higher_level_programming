#!/usr/bin/python3
""" HTTP status code is greater than or equal to 400 """

if __name__ == "__main__":
    from requests import get
    from sys import argv

    request_res = get(argv[1])
    if request_res.status_code >= 400:
        print(f"Error code: {request_res.status_code}")
    else:
        print(request_res.text)
