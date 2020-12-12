# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(target):
            if not target:
                return 0
            l_depth, r_depth = check(target.left), check(target.right)
            if abs(l_depth - r_depth) > 1:
                return float("inf")
            return max(l_depth, r_depth) + 1
        
        return check(root) != float("inf")