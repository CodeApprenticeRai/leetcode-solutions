'''
Too slow
'''

'''
    Given an integer array nums: 
    return the sum of divisors of the integers in that array that have exactly four divitors, 
    if there is no such integer in the array return 0. 

   Iterate nums
'''


class Solution:
    def __init__(self):
        self.divisor_map = {1: {1: True}}

    '''
    Given a integer, return all numbers that divide it without
    producing a remainder
    '''

    def getDivisors(self, num):
        if num in self.divisor_map:
            return self.divisor_map[num]
        else:
            divisors = {1: True}
            for divisor_candidate in range(2, num):
                if (num % divisor_candidate == 0):
                    if (divisor_candidate in self.divisor_map):
                        divisors = {**divisors, **self.divisor_map[divisor_candidate]}
                    else:
                        divisors = {**divisors, **self.getDivisors(divisor_candidate)}

            divisors[num] = True
            self.divisor_map[num] = divisors
            return self.divisor_map[num]

    def sumFourDivisors(self, nums: List[int]) -> int:
        running_sum = 0
        for i in range(len(nums)):
            divisors = self.getDivisors(nums[i])

            if (len(divisors) == 4):
                running_sum += sum(divisors)
        return running_sum
