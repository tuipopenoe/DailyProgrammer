#!/usr/bin/env python
# Tui Popenoe
# challenge201E.py - Counting the Days Until

import sys
from datetime import datetime

def count_days(date):
    date_formatted = datetime.strptime(date.strip(), '%Y %m %d')
    today = datetime.utcnow()
    delta = today - date_formatted
    return delta

def main():
    while True:
        line = sys.stdin.readline()
        print('%s apart') % (count_days(line))
        if not line:
            break

if __name__ == '__main__':
    main()