'''
    Implement strStr(),
    return the index of the first occurence of needle in haystack or -1 if needle is not a part of haystack,

    okay for case: "mississippi","issip", I need to start from the next match if it exists within the itr substring I've built
'''
from collections import deque


class Solution:
    def strStr(self, haystack, needle):
        if (len(needle) == 0):
            return 0

        starting_index = None
        i = 0
        needle_i = 0
        itr = deque()  # rolling window

        while ((i < len(haystack)) and (len(itr) < len(needle))):
            if (haystack[i] == needle[needle_i]):
                if (len(itr) == 0):
                    starting_index = i
                itr.append(haystack[i])
                needle_i += 1
            else:  # this is a little expensive here, this only needs to happen if needle_i != 0
                itr = deque()
                needle_i = 0
                if (starting_index != None):
                    i = starting_index
                    starting_index = None
            i += 1
        return starting_index if (len(itr) == len(needle)) else -1

sol = Solution()
# print( sol.strStr(haystack = "hello", needle = "ll") == 2 )
print( sol.strStr("mississippi","issip") == 4)