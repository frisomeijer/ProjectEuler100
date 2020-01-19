'''
Problem 19:
    
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?.
'''

import time
start_time = time.time()

days_in_month ={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}


day_of_week=0
sunday_first_of_month=0
for year in range(1900,2001):
    for month in range(1,13):
        if month==2 and year%4==0 and (year%100!=0 or year%400==0):
            days=days_in_month[month]+1
        else:
            days=days_in_month[month]
        for day in range(1,days+1):
            day_of_week +=1
            if year>1900 and day==1 and day_of_week==7:
                sunday_first_of_month+=1
            if day_of_week==7:
                day_of_week=0
            
# calculation time: 0.009976625442504883 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   