# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums==None or len(nums)==0:
            return None
        return self.recursion(nums,0,len(nums)-1)
    
    def recursion(self,nums,left,right):
        if left>right:
            return None
        mid=left+(right-left)//2
        current=TreeNode(nums[mid])
        current.left= self.recursion(nums,left,mid-1)
        current.right=self.recursion(nums,mid+1,right)
        return current