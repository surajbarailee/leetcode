class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        value=[1]
        for i in range(rowIndex):
            for j in range(i):
                value[j]=value[j]+value[j+1]
            value=[1]+value
        return value
            