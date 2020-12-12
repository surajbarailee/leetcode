class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return s
        cache = {k: v+1 for (v, k) in enumerate(string.ascii_uppercase)}
        result = 0
        for index, i in enumerate(s[::-1]):
            result += cache[i] * (26**index)
        return result