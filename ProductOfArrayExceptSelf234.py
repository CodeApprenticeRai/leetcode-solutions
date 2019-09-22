'''
    Given an array nums of n integers,
    return an array output such that output[i] is equal to the product of
    all the elements of nums except nums[i]
'''

class Solution:
    def product(self, arr):
        product = 1
        for num in arr:
            product *= num
        return product

    def productExceptSelf(self, nums):
        output = []
        left_products = [1, ]
        right_products = [0 for i in range(len(nums))]
        right_products[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            left_products.append(left_products[i - 1] * nums[i - 1])

        for i in range(len(nums) - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            output.append(left_products[i] * right_products[i])

        return output