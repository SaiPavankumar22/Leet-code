class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();
        vector<vector<int>> vis(n,vector<int>(m,0));
        vector<vector<int>> res(n,vector<int>(m,0));
        queue<pair<pair<int,int>,int>>q;
        for(int i =0;i<n;i++){
            for(int j=0;j<m;j++){
                if (mat[i][j] == 0) {
                    vis[i][j] = 1;
                    q.push({{i, j}, 0});}
            }
        }
        int drow[] = {-1, 0, 1, 0};
        int dcol[] = {0, 1, 0, -1};

        while(!q.empty()){
            int r = q.front().first.first;
            int c = q.front().first.second;
            int s = q.front().second;
            q.pop();
            

            for(int i =0;i<4;i++){
                int n_r = r + drow[i];
                int n_c = c + dcol[i];
                if(n_r>=0 && n_r<n && n_c>=0 && n_c<m && vis[n_r][n_c] == 0){
                    vis[n_r][n_c] = 1;
                    res[n_r][n_c] = s+1;
                    q.push({{n_r,n_c},s+1});
                }
            }
        }
        return res;
    }
};