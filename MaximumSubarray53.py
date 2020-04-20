'''
    By contiguous, they mean 'side-by-side'

    Basically:
        we're at the ith step:
        either running_sum + arr[i] > arr[i] or not
        if true: running_sum += arr[i]
        if not true running_sum = arr[i]

'''


class Solution:
    def maxSubArray(self, nums):
        running_sum = nums[0]
        max_running_sum = running_sum
        for num in nums[1:]:
            if ((running_sum + num) > num):
                running_sum += num
            else:
                running_sum = num
            max_running_sum = max(max_running_sum, running_sum)
        return max_running_sum