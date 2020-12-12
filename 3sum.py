
nums = [-1, 0, 1, 2, -1, -4]
answer = []
mylist = []
length = len(nums)
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            if(nums[i]+nums[j]+nums[k]) == 0:
                myans = sorted([nums[i], nums[j], nums[k]])
                if myans not in mylist:
                    answer.append(myans)
                    mylist.append(myans)


nums.sort()
triplets = []

for i in range(len(nums)-2):
    left = i + 1
    right = len(nums)-1
    while left < right:
        currentsum = nums[i]+nums[left] + nums[right]
        if currentsum == 0:
            if [nums[i], nums[left], nums[right]] not in triplets:
                triplets.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
        elif currentsum < 0:
            left += 1
        else:
            right -= 1
print(triplets)

nums.sort()
triplets = []

for i in range(len(nums)-2):

    if i>0 and nums[i] == nums[i-1]: continue

    left = i + 1
    right = len(nums)-1
    while left < right:
        currentsum = nums[i]+nums[left] + nums[right]
        if currentsum == 0:
            if [nums[i], nums[left], nums[right]] not in triplets:
                triplets.append([nums[i], nums[left], nums[right]])
                while left <right and nums[left] == nums[left+1]:
                    left +=1
                while left <right and nums[right]==nums[right-1]:
                    right-=1
            left += 1
            right -= 1
        elif currentsum < 0:
            left += 1
        else:
            right -= 1
print(triplets)





#  def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i, a in enumerate(nums):
#             if i > 0 and a == nums[i - 1]:
#                 continue

#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
#         return res
                        
