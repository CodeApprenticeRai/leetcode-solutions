'''
    Given a string ~date, representing a date in YYYY-MM-DD, return the day number of the year
'''
'''
    Approach:
        every month has a different number of days,
        iterate through a list of each days in each month, which is ordered !!how it would regularly be ordered.
        while ()
'''


class Solution:
    def isLeapYear(self, year):
        if not ((year % 4) == 0):
            return False
        elif not ((year % 100) == 0):
            return True
        elif not ((year % 400) == 0):
            return False
        else:
            return True

    def dayOfYear(self, date):
        DAYS_IN_EACH_MONTH = [0, 31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date = date.split("-")
        date = [int(item) for item in date]

        month = 0
        day_of_the_year = 0
        while (month < date[1]):
            if month == 2:
                day_of_the_year += DAYS_IN_EACH_MONTH[month][1] if (self.isLeapYear(date[0])) else \
                DAYS_IN_EACH_MONTH[month][0]
            else:
                day_of_the_year += DAYS_IN_EACH_MONTH[month]
            month += 1
        return day_of_the_year + date[2]