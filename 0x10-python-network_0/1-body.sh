#!/bin/bash
# cript that takes in a URL, sends a GET request to the URL
# and displays the body of the response
if [ $(curl -L -s -X HEAD -w "%{Http_code}" "$1") == '200' ]; then curl -Ls "$1";
fi