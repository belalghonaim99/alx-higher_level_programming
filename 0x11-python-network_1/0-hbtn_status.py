#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as w:
        c = w.read()
        print("Body response:")
        print("\t- type: {}".format(type(c)))
        print("\t- content: {}".format(c))
        print("\t- utf8 content: {}".format(c.decode('utf-8')))
