class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rl=len(matrix)
        cl=len(matrix[0])
        row=[0]*rl
        col=[0]*cl
        for i in range(0,rl):
            for j in range(0,cl):
                if(matrix[i][j]==0):
                    row[i]=1
                    col[j]=1
        for n in range(0,rl):
            for m in range(0,cl):
                if (row[n]==1 or col[m]==1):
                    matrix[n][m]=0
                    