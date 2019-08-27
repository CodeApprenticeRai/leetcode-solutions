# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    I'm thinking that the longest path starting at a node is
    1 + the max of the longest path starting at it's left and right child nodes.
    If the current node is none, return 0. There is no path
'''


class Solution:
    def _diameterOfBinaryTree(self, node):
        if (node == None):
            return 0
        else:
            left_path_length = self._diameterOfBinaryTree(node.left)
            right_path_length = self._diameterOfBinaryTree(node.right)
            path_length_through_curr = left_path_length + right_path_length

            self.longest_path_length = max(self.longest_path_length, path_length_through_curr)

            return 1 + max(left_path_length, right_path_length)

    def diameterOfBinaryTree(self, root):
        self.longest_path_length = 0
        self._diameterOfBinaryTree(root)
        return self.longest_path_length