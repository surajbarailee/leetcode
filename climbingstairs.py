#Time limit exceeded
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        else:
            return self.climbStairs(n-2)+self.climbStairs(n-1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        first=1
        second=2
        for i in range(3,n+1):
            third=first+second
            first=second
            second=third
        return second