class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> res;
        int n = arr.size();
        for(int currsize = n; currsize>1;currsize--){
            int idx = 0;
            for(int i = 1; i<currsize; i++){
                if(arr[i]>arr[idx]){
                    idx = i;
                }
            }
            if(idx == currsize){
                continue;
            }
            if(idx!=0){
                res.push_back(idx+1);
                reverse(arr.begin(),arr.begin()+idx+1);
            }
            res.push_back(currsize);
            reverse(arr.begin(),arr.begin()+currsize);
        }
        return res;
    }
};