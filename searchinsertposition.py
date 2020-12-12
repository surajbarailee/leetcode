class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        for i in range(0,length):
            if nums[i]==target:
                return i
            if nums[i]>target:
                if i==0:
                    return 0
                else:
                    return i
        return length