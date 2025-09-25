class Solution {
private:
    void dfs(int sr, int sc, int color, vector<vector<int>>& image, vector<vector<int>>&res, int initial, int drow[], int dcol[]){
        res[sr][sc] = color;
        int n = image.size();
        int m = image[0].size();
        for(int i =0;i<4;i++){
            int nrow = drow[i] + sr;
            int ncol = dcol[i] + sc;
            if(nrow>=0 && nrow<n && ncol>=0 && ncol<m && image[nrow][ncol]== initial && res[nrow][ncol]!=color ){
                dfs(nrow, ncol,color, image, res, initial, drow, dcol);
            }
        }
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int initial = image[sr][sc];
        vector<vector<int>> res = image;
        int drow[] = {-1, 0, 1, 0};
        int dcol[] = {0, 1, 0, -1};
        dfs(sr, sc, color, image, res,initial, drow, dcol);
        return res; 
    }
};