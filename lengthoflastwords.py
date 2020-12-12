class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=='':
            return 0
        else:
            array=s.split(' ')
            word=' '
            for i in array:
                if i!='':
                    word=i
            if word!=' ':
                return len(word)
            else:
                return 0