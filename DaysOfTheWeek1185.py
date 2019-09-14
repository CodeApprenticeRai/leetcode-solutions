from timeit import timeit

class Solution:
    def __init__(self):
        self.DAYS_OF_THE_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.DAYS_IN_EACH_MONTH = [0, 31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.memo_table = {}

        index_of_day_of_the_week = 5
        for year in range(1971, 2101):
            if (year not in self.memo_table):
                self.memo_table[year] = {}

            for month in range(1, 13):
                if (month not in self.memo_table[year]):
                    self.memo_table[year][month] = {}

                if (month != 2):
                    number_of_days_in_current_month = self.DAYS_IN_EACH_MONTH[month]
                else:
                    if (self.isLeapYear(year)):
                        number_of_days_in_current_month = self.DAYS_IN_EACH_MONTH[month][1]
                    else:
                        number_of_days_in_current_month = self.DAYS_IN_EACH_MONTH[month][0]

                for day in range(1, number_of_days_in_current_month + 1):
                    self.memo_table[year][month][day] = index_of_day_of_the_week % len(self.DAYS_OF_THE_WEEK)
                    index_of_day_of_the_week += 1

    def isLeapYear(self, year):
        if not ((year % 4) == 0):
            return False
        elif not ((year % 100) == 0):
            return True
        elif not ((year % 400) == 0):
            return False
        else:
            return True

    def dayOfTheWeek(self, day, month, year):
        day_of_the_week_index = self.memo_table[year][month][day]
        return self.DAYS_OF_THE_WEEK[day_of_the_week_index]

time = timeit()
sol = Solution()