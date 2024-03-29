#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header """
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.headers['X-Request-Id']:
        print(r.headers['X-Request-Id'])
