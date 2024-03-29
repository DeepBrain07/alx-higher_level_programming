#!/usr/bin/python3
""" This script takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8) """
import sys
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    req = urllib.request.Request(sys.argv[1], data=data, method="POST")
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
