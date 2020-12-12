class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        if x < 0:
            return False
        revert=0
        index=0
        while y>0:
            x1 = y%10
            revert = revert * (10) + x1
            y=y//10
            index=index+1
        if revert == x :
            return True
        else:
            return False