# URL: https://www.hackerrank.com/challenges/calendar-module/problem

"""
Sample Input

08 05 2015
Sample Output

WEDNESDAY

"""

import calendar

month, day, year = map(int, input().split())

day_index = calendar.weekday(year, month, day)

print(calendar.day_name[day_index].upper())