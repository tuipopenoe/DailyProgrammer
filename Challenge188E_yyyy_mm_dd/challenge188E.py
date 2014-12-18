#!python2
# Tui Popenoe
# challenge188E.py - yyyy-mm-dd

import sys

def convert_date(date):
    """Converts a number of date formats to iso 8601 yyyy-mm-dd"""
    # mm/dd/yy
    if date[2:3] is '/':
        month = date[0:2]
        day = date[3:5]
        year = date[6:]
        if int(year) < 50 :
            year = "20" + year
        else:
            year = "19" + year
        date = year + '-' + month + '-' + day
        return date
    # mm#yy#dd
    elif date[2:3] is '#':
        month = date[0:2]
        day = date[3:5]
        year = date[6:]
        if int(year) < 50 :
            year = "20" + year
        else:
            year = "19" + year
        date = year + '-' + month + '-' + day
        return date
    # dd*mm*yyyy
    elif date[2:3] is '*':
        day = date[0:2]
        month = date[3:5]
        year = date[6:]
        date = year + '-' + month + '-' + day
        return date
    # (month word) dd, yy || (month word) dd, yy
    elif date[3:4] is ' ':
        month = convert_month_word(date[0:3])
        day = date[4:6]
        year = date[8:]
        if len(year) < 3:
            if int(year) < 50:
                year = "20" + year
            else:
                year = "19" + year
        date = year + '-' + month + '-' + day
        return date
    # yyyy-mm-dd
    else:
        return date

def convert_month_word(word):
    months = {'Jan': '01',
              'Feb': '02',
              'Mar': '03',
              'Apr': '04',
              'May': '05',
              'Jun': '06',
              'Jul': '07',
              'Aug': '08',
              'Sep': '09',
              'Oct': '10',
              'Nov': '11',
              'Dec': '12'
              }
    return months[word]

def main():
    output = []
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            inp = f.read().splitlines()
            for i in inp:
                output.append(convert_date(i))
            return output
    else:
        with open('input.txt', 'r') as f:
            inp = f.read().splitlines()
            for i in inp:
                output.append(convert_date(i))
            return output

if __name__ == '__main__':
    for i in main():
        print(i)