# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,leftSub,rightSub):
        if leftSub==None and rightSub==None:
            return True
        elif leftSub!=None and rightSub!=None:
            return leftSub.val==rightSub.val and self.check(leftSub.left,rightSub.right) and self.check(leftSub.right,rightSub.left)
        else:
            return False
    def isSymmetric(self, root: TreeNode) -> bool:

        if root==None:
            return True
        else:
            return self.check(root.left,root.right)