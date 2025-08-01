class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> k = heights;
        sort(k.begin(), k.end());
        int c = 0;
        for(int i =0;i<heights.size();i++){
            if(heights[i] != k[i]){
                c+=1;
            }
        }
        return c;
    }
};