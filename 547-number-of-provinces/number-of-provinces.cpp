class Solution {
private:
    void dfs(int node , vector<vector<int>>&adjlist,vector<int>&vis){
        vis[node] =1;
        for(auto y : adjlist[node]){
            if(!vis[y]){
                dfs(y,adjlist,vis);
            }
        }
    }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<vector<int>>adjlist(n);
        for(int i=0;i<n;i++){
            for(int j =0; j<n;j++){
                if(isConnected[i][j]==1 && i!=j){
                    adjlist[i].push_back(j);
                    adjlist[j].push_back(i);
                }
            }
        }
        vector<int> vis(n,0);
        int count = 0;
        for(int x=0 ;x<n;x++){
            if(!vis[x]){
                count++;
                dfs(x,adjlist,vis);
            }
        }
        return count;


    }
};