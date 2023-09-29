#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    post_request = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        response_body = post_request.json()
        if response_body == {}:
            print('No result')
        else:
            print(f"[{response_body.get('id')}, {response_body.get('name')}]")

    except ValueError:
        print('Not a valid JSON')
