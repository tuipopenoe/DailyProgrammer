#!/usr/bin/env python

import sys

months = {
    '01' : 'January',
    '02' : 'February',
    '03' : 'March',
    '04' : 'April',
    '05' : 'May',
    '06' : 'June',
    '07' : 'July',
    '08' : 'August',
    '09' : 'September',
    '10' : 'October',
    '11' : 'November',
    '12' : 'December'
}

days = {
    '01' : '1st',
    '02' : '2nd',
    '03' : '3rd',
    '04' : '4th',
    '05' : '5th',
    '06' : '6th',
    '07' : '7th',
    '08' : '8th',
    '09' : '9th',
    '10' : '10th',
    '11' : '11th',
    '12' : '12th',
    '13' : '13th',
    '14' : '14th',
    '15' : '15th',
    '16' : '16th',
    '17' : '17th',
    '18' : '18th',
    '19' : '19th',
    '20' : '20th',
    '21' : '21st',
    '22' : '22nd',
    '23' : '23rd',
    '24' : '24th',
    '25' : '25th',
    '26' : '26th',
    '27' : '27th',
    '28' : '28th',
    '29' : '29th',
    '30' : '30th',
    '31' : '31st'
}

def convert_dates(dates):
    in_dates = dates.split()
    year1 = '' if in_dates[0][:4] == '2015' else in_dates[0][:4]
    year2 = '' if in_dates[1][:4] == '2015' else in_dates[1][:4]
    date1 = ('%s %s, %s' % (months[in_dates[0][5:7]], days[in_dates[0][8:10]],
                            year1))
    date2 = ('%s %s, %s' % (months[in_dates[1][5:7]], days[in_dates[1][8:10]],
                            year2))
    return ('%s - %s' % (date1, date2))

def main():
    if len(sys.argv) > 1:
        print(convert_dates(sys.argv[1:]))
    else:
        print(convert_dates(sys.stdin.readline()))

if __name__=='__main__':
    main()