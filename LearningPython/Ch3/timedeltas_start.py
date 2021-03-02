#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print(str(now + timedelta(days=365, hours=-32)))

# print today's date one year from now
print("In 2 days and 3 weeks it will be:" + str(now + timedelta(days=2, weeks=3)))

# create a timedelta that uses more than one argument


# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?
today = date.today()
apd = date(today.year, 4, 1)
if apd < today:
    print("April Fool's Day already went by %d days ago" % ((today - apd).days))
    apd = apd.replace(year= today.year + 1)
time_to_apd = apd - today
print("It's just", time_to_apd.days, "days until AFD")

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day
