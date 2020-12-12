class Solution:
    def trailingZeroes(self, n: int) -> int:
        i,trailing_zeroes = 1,0
        while (n // 5**i) > 0:
            trailing_zeroes += n // 5**i
            i += 1
        return trailing_zeroes