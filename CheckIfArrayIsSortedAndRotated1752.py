'''
check for a monotonicty change
that happens twice.
'''

class Solution:
    def check(self, nums):
        tone_change = 0
        for i in range(len(nums)):
            if (nums[i] > nums[(i+1) % len(nums)]):
                tone_change += 1
            if (tone_change >= 2):
                return False
        return True