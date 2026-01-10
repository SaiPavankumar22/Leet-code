class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            line = [1]*(i+1)
            for j in range(1,i):
                line[j]=pascal[i-1][j-1] + pascal[i-1][j]
            pascal.append(line)
        return pascal
        