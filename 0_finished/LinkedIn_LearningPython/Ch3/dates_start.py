#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print(today, today.day, today.month, today.year)
    print(today.weekday())

    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class




    # print out the date's individual components


    # retrieve today's weekday (0=Monday, 6=Sunday)
    days = ['mon', 'tue', 'wen', 'thu', 'fri', 'sat', 'sun']
    print("Today is:", today.weekday())

    ## DATETIME OBJECTS
    #   Get today's date from the datetime class
    today = datetime.now()
    print(today)

    # Get the current time
    t = datetime.time(datetime.now())
    print(t)

if __name__ == "__main__":
    main()
