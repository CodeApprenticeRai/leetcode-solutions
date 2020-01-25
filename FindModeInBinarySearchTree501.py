# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if (root == None):
            return []

        visited = []
        stack = []

        stack.append(root)

        while (len(stack) > 0):
            curr = stack[-1]
            visited.append(curr.val)

            stack.pop(-1)

            if (curr.right != None):
                stack.append(curr.right)

            if (curr.left != None):
                stack.append(curr.left)
        return visited

    def findMode(self, root: TreeNode) -> List[int]:
        if (type(root) == type(None)):
            return []

        all_values = self.preorderTraversal(root)

        value_count_record = {}

        for value in all_values:
            if value in value_count_record:
                value_count_record[value] += 1
            else:
                value_count_record[value] = 1

        modes = []

        mode = max(value_count_record, key=lambda value_key: value_count_record[value_key])
        max_count = value_count_record[mode]

        # check for other modes
        for value_key in value_count_record:
            if (value_count_record[value_key] == max_count):
                modes.append(value_key)

        return modes