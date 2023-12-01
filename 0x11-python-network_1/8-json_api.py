#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    v = ""
    if len(sys.argv) > 1:
        v = sys.argv[1]
    q = {"q": v}
    response = requests.post("http://0.0.0.0:5000/search_user", data=q)
    try:
        response = response.json()
        if response:
            print("[{}] {}".format(response.get("id"),
                                   response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
