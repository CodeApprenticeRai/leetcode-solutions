'''
    We duplicate the zeros, pushing down the elements after the occurence of the zero,
    stopping when we get to arrays max length
'''
from collections import deque


class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = deque(arr)
        q_i = 0
        i = 0

        while (i  < len(arr)):
            if (((i + 1) < len(arr)) and (queue[q_i] == 0)):
                arr[i] = 0
                arr[i + 1] = 0
                i += 2
                q_i += 1
            else:
                arr[i] = queue[q_i]
                i += 1
                q_i += 1
        return None

sol = Solution()
print(sol.duplicateZeros([1,0,2,3,0,4,5,0]))