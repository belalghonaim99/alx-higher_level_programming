#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response."""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    post_Request = post(argv[1], email_request={'email': argv[2]})
    print(post_Request.text)