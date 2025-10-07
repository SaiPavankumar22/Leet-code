class Solution {
public:
    bool check(vector<int>& nums) {
        vector<int> k = nums;
        sort(k.begin(),k.end());
        if(nums == k){
            return true;
        }
        bool w = false;
        for(int i =0;i<nums.size();i++){
            int a = k.back();
            k.pop_back();
            k.insert(k.begin(),a);
            if(nums == k){
                w = true;
            }

        }
        return w;

    }
};