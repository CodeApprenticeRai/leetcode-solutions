# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
    Time: O(n),
    Space: O(n)
'''


class Solution:
    def traverseForLevelSum(self, node, level):
        if (type(node) == type(None)):
            return None
        else:
            if level not in self.level_sum_cache:
                self.level_sum_cache[level] = 0
            self.level_sum_cache[level] += node.val
            self.traverseForLevelSum(node.left, level + 1)
            self.traverseForLevelSum(node.right, level + 1)
            return None

    def maxLevelSum(self, root) -> int:
        if (type(root) == type(None)):
            return 0
        self.level_sum_cache = {1: root.val}

        self.traverseForLevelSum(root.left, 2)
        self.traverseForLevelSum(root.right, 2)
        level_of_max_sum = max(self.level_sum_cache, key=lambda level: self.level_sum_cache[level])
        return level_of_max_sum