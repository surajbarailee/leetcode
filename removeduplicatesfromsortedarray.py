#remove duplicates from the same array and return the length
nums = [0,0,1,1,1,2,2,3,3,4]

length = len(nums)-1

for i in range(length,0,-1):
    if nums[i]==nums[i-1]:
        nums.pop(i)





