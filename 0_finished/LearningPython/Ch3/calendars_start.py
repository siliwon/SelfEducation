#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
# st = c.formatmonth(2021, 3, 0, 0)
# print(st)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# st = hc.formatmonth(2017, 8)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2021, 1):
    # print(i)

# The Calendar module provides useful utilities for the given locale,
# # such as the names of days and months in both full and abbreviated forms
# for day in calendar.day_name:
#     print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2021, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        weektwo[calendar.FRIDAY]

    print("%10s %d" % (calendar.month_name[m], meetday))