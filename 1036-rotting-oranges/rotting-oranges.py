class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        rows= len(grid)
        cols =len(grid[0])
        queue = deque()
        count_fresh=0
        time = 0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 2):
                    queue.append((i,j))
                elif(grid[i][j] ==1):
                    count_fresh +=1
        if count_fresh == 0:
            return 0
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        while(queue and count_fresh>0):
            time +=1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    nrow= row + dr
                    ncol =col + dc
                    
                    if (0<=nrow< rows and 0 <=ncol <cols and grid[nrow][ncol] ==1):
                        grid[nrow][ncol] = 2
                        count_fresh -=1
                        queue.append((nrow,ncol))
        
        if(count_fresh ==0):
            return time
        else:
            return -1