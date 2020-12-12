
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=100000000
        maximum=0
        for i in prices:
            if i<minimum:
                minimum=i
            else:
                maximum=max(maximum,(i-minimum))
        return maximum








#Time limit exceeded
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maximum=0
#         for i in range(0,len(prices)):
#             for j in range(i+1,len(prices)):
#                 if prices[j]-prices[i]>maximum:
#                     maximum=prices[j]-prices[i]
#         return maximum