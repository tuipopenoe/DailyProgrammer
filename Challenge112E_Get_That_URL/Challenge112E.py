#!python2
# Tui Popenoe
# Challenge 112E.py - Get that URL

import json
import httplib
import sys

def get_url(URL):
    c = httplib.HTTPConnection(URL)
    c.request("HEAD", '')
    if c.getresponse().status == 200:
        q = URL.index('s')
        v = URL[q+1:]
        k = URL.split('=')
        formatted_string = {k[i]: k[i+1] for i in range(0, len(k), 2)}
        for k, v in formatted_string.iteritems():
            print(k, v)
    else:
        print("The given URL is invalid")

def main():
    if len(sys.argv) > 1:
        print(get_url(sys.argv[1]))
    else:
        print(get_url(sys.stdin.readline()))

if __name__ == '__main__':
    main()