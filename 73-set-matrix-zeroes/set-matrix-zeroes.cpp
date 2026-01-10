class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<vector<int>>posi;
        for(int i = 0;i<matrix.size();i++){
            for(int j =0;j<matrix[i].size();j++){
                if(matrix[i][j]==0){
                    posi.push_back({i,j});
                }
            }

        }
        for(auto k:posi){
            for(int a =0;a<matrix[k[0]].size();a++){
                matrix[k[0]][a] = 0;
            }
            for(int b = 0; b<matrix.size();b++){
                matrix[b][k[1]] = 0;
            }
        }

    }
};