#!python2
# Tui Popenoe
# Challenge100E.py - Sleep Cycle Estimator

def estimate_sleep():
    print('Input time to wake up: ')
    wake = raw_input()
    wake_time = wake.split(':')

    sleep_times = list()

    for i in range(1,5):
        hour = int(wake_time[0]) - 1
        if i % 2 == 1:
            minute = int(wake_time[1]) - 30
        else:
            minute = wake_time[1]
        if minute < 0:
            minute += 60
            hour -= 1
        if hour <= 0:
            hour += 12
        time = (str(hour), ':', str(minute))
        wake_time[0] = str(hour)
        sleep_times.append(''.join(time))

    return sleep_times

def main():
    print(estimate_sleep())

if __name__=='__main__':
    main()