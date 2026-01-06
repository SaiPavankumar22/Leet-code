class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int k = nums.size();
        int actual = (k*(k+1))/2;
        int curr = 0;
        for(auto j:nums){
            curr+=j;
        }
        return actual-curr;
    }
};