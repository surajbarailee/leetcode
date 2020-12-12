# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pvalue=self.myfunction(p)
        qvalue=self.myfunction(q)
        print(pvalue,qvalue)
        return pvalue==qvalue
    def myfunction(self,root):
        if root is None:
            return [None]
        return [root.val] + self.myfunction(root.left) + self.myfunction(root.right)
