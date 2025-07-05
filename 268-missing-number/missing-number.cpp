class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int k=accumulate(nums.begin(),nums.end(),0);
        int f =0;
        for(int i=0;i<n+1;i++){
            f+=i;
        }
        return f-k;
        
    
    }
};