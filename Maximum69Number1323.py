'''
    Given a positive integer num, consisting of digits 6 an d9,
    return the maximum number you can get by chaning at most one digit.

    ::
    Iterating through the string representation of the number from left to right, change the first 6 digit encountered to a 9.
    If no 6's are encountered the number can't be increased
'''


class Solution:
    def maximum69Number(self, num):
        found_a_6 = False
        num = list(str(num))
        i = 0
        while ((not found_a_6) and i < (len(num))):
            if (num[i] == "6"):
                found_a_6 = True
                num[i] = "9"
            i += 1
        return int("".join(num))