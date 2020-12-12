class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lst=[]
        while nums:
            a=nums.pop(0)
            if a in nums:
                nums.pop(nums.index(a))
            else:
                return a