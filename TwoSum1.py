class Solution:
    def twoSum(self, nums, target):
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(nums[i],nums[j], i, j)
                #if (nums[i]+nums[j] == target):
                #    return [i,j]
        return [0,1]


sol = Solution()
zsol.twoSum([3,2,4],6)