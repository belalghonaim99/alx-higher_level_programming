#!/usr/bin/python3
"""script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    email = {"email": argv[2]}
    request_email = Request(
            argv[1], urlencode(email).encode("ascii"))
    with urlopen(request_email) as web:
        header = web.headers.get('X-Request-Id')
        print(web.read().decode('utf-8'))