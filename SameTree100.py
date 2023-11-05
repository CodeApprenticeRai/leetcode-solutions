# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if ((p == None) or  (q == None)):
            if (p == q):
                return True
            else:
                return False
        if (
            (p.val != q.val) or
            not self.isSameTree(p.left, q.left) or
            not self.isSameTree(p.right, q.right)
        ):
            return False
        return True
