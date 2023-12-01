#!/usr/bin/python3
"""script that takes and sends a POST request to the passed URL """


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    e = {"email": argv[2]}
    request = Request(
            argv[1], urlencode(e).encode("ascii"))
    with urlopen(request) as w:
        h = w.headers.get('X-Request-Id')
        print(w.read().decode('utf-8'))