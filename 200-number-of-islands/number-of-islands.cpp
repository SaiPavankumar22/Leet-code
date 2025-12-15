class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>>visited(n,vector<int>(m,0));
        int cnt = 0;
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(!visited[i][j] && grid[i][j]=='1'){
                    cnt++;
                    bfs(i,j,visited,grid);
                }
            }
        }
        return cnt;
    }

    void bfs(int row, int col, vector<vector<int>> &visited, vector<vector<char>> &grid){
        queue<pair<int,int>>q;
        q.push({row,col});
        visited[row][col] = 1;

        int n_row[] = {-1,0,1,0};
        int n_col[] = {0,1,0,-1};
        while(!q.empty()){
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            for(int i = 0;i<4;i++){
                int nrow = r + n_row[i];
                int ncol = c+ n_col[i];
                if(nrow>=0 && nrow<grid.size() && ncol>=0 && ncol<grid[0].size() && !visited[nrow][ncol] && grid[nrow][ncol] == '1'){
                    visited[nrow][ncol] = 1;
                    q.push({nrow,ncol});

                }
            }
        }
    }

};