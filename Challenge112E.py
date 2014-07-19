# Tui Popenoe
# Challenge 112E.py - Get that URL

import httplib
import json

def getUrl(URL):
    c = httplib.HTTPConnection(URL)
    c.request("HEAD", '')
    if c.getresponse().status == 200:
        q = URL.index('s')
        v = URL[q+1:]
        k = URL.split('=')
        formattedString = {k[i]: k[i+1] for i in range(0, len(k), 2)}
    for k, v in formattedString.iteritems():
        print(k, v)

    else:
        print("The given URL is invalid")