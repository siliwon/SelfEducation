#
# Example file for formatting time and date output
#

from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()

    #### Date Formatting ####
    # print(now.strftime("The current year is: %Y"))
    # # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    # print(now.strftime("%a, %d %B, %y"))
    # print(now.strftime("%c"))
    # print(now.strftime("%x"))
    # print(now.strftime("%X"))
    # %c - locale's date and time, %x - locale's date, %X - locale's time

    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S"))


if __name__ == "__main__":
    main()