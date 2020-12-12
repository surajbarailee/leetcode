class Solution:
    def convertToTitle(self, n: int) -> str:
        import string
        alphabet = string.ascii_uppercase
        string = ''
        while(n>0):
            n-=1
            i = n%26
            n = int(n/26)
            string = alphabet[i]+ string
        
        return string