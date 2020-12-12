class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = list(set(nums))
        arr.sort()
        for i in arr:
            if nums.count(i) > int(len(nums)/2):
                return(i)
        