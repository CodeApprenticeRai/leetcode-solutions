'''
    A Binary Serach problem

    See Leetcode for a better binary search solution,

    their's is 13 lines.
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def isBadVersion(self, version_number):
        if version_number not in self.isBadVerisionCache:
            self.isBadVerisionCache[version_number] = isBadVersion(version_number)
        return self.isBadVerisionCache[version_number]

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.isBadVerisionCache = {}

        if (self.isBadVersion(1)):
            return 1
        elif (n == 2):
            return 1 if self.isBadVersion(1) else 2
        else:
            window_bottom = 1
            window_top = n
            mid = window_bottom + ((window_top - window_bottom) // 2)

            while (window_bottom < window_top):
                mid = window_bottom + ((window_top - window_bottom) // 2)

                if ((not self.isBadVersion(mid - 1)) and self.isBadVersion(mid)):
                    return mid
                else:
                    if self.isBadVersion(mid - 1):
                        window_top = mid - 1
                    else:  # this would mean that mid-1->false and mid->false
                        window_bottom = mid + 1
            return window_top