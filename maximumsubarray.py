
#This solution passes the test but times out
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        temp=[]
        num=len(nums)+1
        maximum=-2147483648
        size=[]
        for i in range(0,len(nums)+1):
            for j in range(i,len(nums)+1):
                t=nums[i:j]
                total=0
                if t!=[]:
                    for l in t:
                        total=total+l
                    if total>maximum:
                        maximum=total
        return maximum

# a little better version but also time limit exceeded lol
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        num=len(nums)
        maximum=nums[0]
        size=[]
        for i in range(0,num+1):
            prevsum=0
            for j in range(i,num):
                prevsum=prevsum+nums[j]
                if maximum<prevsum:
                    maximum=prevsum
        return maximum


class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far


class Solution:
    def maxContiguousSubarraySum(self, nums):
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far