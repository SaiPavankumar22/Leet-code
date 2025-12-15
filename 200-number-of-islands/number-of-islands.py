from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        cnt =0
        for i in range(n):
            for j in range(m):
                if(not visited[i][j] and grid[i][j]== '1'):
                    cnt+=1
                    self.bfs(i,j,grid,visited)
        return cnt
    def bfs(self, row,col,grid,visited):
        q = deque()
        q.append((row,col))
        visited[row][col] = True
        n_row = [-1,0,1,0] #[-1,-1,-1,0,1,1,1,0]
        n_col = [0,1,0,-1] #[-1,0,1,1,1,0,-1,-1]
        while q:
            fi, se = q.popleft()
            for x in range(4):
                new_row = fi + n_row[x]
                new_col = se + n_col[x]
                if(0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and not visited[new_row][new_col] and grid[new_row][new_col]=='1'):
                    visited[new_row][new_col] = True
                    q.append((new_row,new_col))
