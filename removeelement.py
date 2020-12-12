nums=[0,1,2,2,3,0,4,2]
length = len(nums)-1
val = 2
for i in range(length,0,-1):
    if nums[i]==val:
        nums.pop(i)

print(len(nums))