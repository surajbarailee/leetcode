'''
create a dictionary
Take each  position and number from list using enumerate
check if target-number is in dictionary
if yes:
    return dictionary[target-number],position
else:
    dictionary[number]=position

'''

def twoSum(nums, target):
        myseennumbers={}
        for index ,number in enumerate(nums):
            if target-number in myseennumbers:
                return myseennumbers[target-number],index
            myseennumbers[number]=index

print(twoSum([2,7,11,15],9))




        