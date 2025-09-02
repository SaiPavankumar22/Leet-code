class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int pre = nums[0];
        int pre2 = 0;
        for(int i =1;i<n;i++){
            int pick = nums[i];
            if(i>1){
                pick+=pre2;
            }
            int notpick = 0 + pre;
            int cur = max(pick , notpick);
            pre2 = pre;
            pre = cur;
        }
        return pre;
    }
    

};