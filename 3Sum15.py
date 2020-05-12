'''
    Given an array nums of n integers, are there element a,b,c such that
    a+b+c=0
    Find all unique triplets in the array which give the the sum zeor

    Sort Array, then search, disqualifying search paths already explored.
'''

class Solution:
    def threeSum(self, nums):
        nums.sort()
        solutions = []
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1

            if ((i > 0) and (nums[i] == nums[i - 1])):
                continue

            while (start < end):
                if ((end < len(nums) - 1) and (nums[end] == nums[end + 1])):
                    end -= 1
                    continue

                candidate_set = [nums[i], nums[start], nums[end]]
                set_sum = sum(candidate_set)

                if (set_sum == 0):
                    solutions.append(candidate_set)
                    start += 1
                    end -= 1

                elif (set_sum < 0):
                    start += 1
                else:
                    end -= 1
        return solutions