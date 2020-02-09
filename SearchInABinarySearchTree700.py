# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
    we basically just check if the value of the current node is the value we're searching
    and if it is we return it
'''


class Solution:
    def searchBST(self, node, val):
        if ( (node == None) or (node.val == val) ):
            return node
        else:
            left_search_result = self.searchBST(node.left, val)
            if ( left_search_result != None ):
                return left_search_result
            else:
                return self.searchBST(node.right, val)