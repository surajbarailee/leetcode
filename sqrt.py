class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        return int(math.sqrt(x))

def mySqrt( x: int) -> int:
    sqrt=0
    if x==0 or x==1:
        return x
    for i in range(1,x):
        if i*i>=x:
            sqrt=i
            break
    return sqrt

print(mySqrt(2))

x=100
if x==0 or x==1:
	print(x)

for i in range(1,x+1):
    v=i*i
    if v==x:
        print(i)
        break
    elif v>x:
        print (i-1)
        break
    


