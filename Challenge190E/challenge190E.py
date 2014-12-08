#!python2
# Tui Popenoe
# challenge190E.py - Webscraping Sentiments

import lxml
import logging
import urllib2
import sys

import lxml.html

def parse_page(url):
    try:
        # Fetch the url
        doc = urllib2.urlopen(url)
        if doc:
            # parse the tree.
            tree = lxml.html.parse(doc)
            # use xpath to find nodes
            nodes = tree.xpath('//div[@class="Ct"')
            for node in nodes:
                print(node)
    except Exception, ex:
        logging.error(ex)

def main():
    if len(sys.argv) > 1:
        parse_page(sys.argv[1])
    else:
        parse_page(raw_input("Enter a URL to parse: "))

if __name__ == '__main__':
    main()