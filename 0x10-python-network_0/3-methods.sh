#!/bin/bash
# displays all HTTP methods on the server
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d ' 