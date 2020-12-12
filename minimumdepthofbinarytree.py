# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        return self.findMinDepth(root)
    
    
    
    def findMinDepth(self,root):
        if (root==None):
            return 2147483647
        if root.left == None and  root.right == None:
            return 1
        return min(self.findMinDepth(root.left),self.findMinDepth(root.right))+1
        