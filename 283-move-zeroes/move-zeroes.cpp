class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int c=0;
        for(int i = 0;i< nums.size();i++){
            if(nums[i] != 0){
                nums[c] = nums[i];
                c+=1;
            }
        }
        for(int j =c;j< nums.size();j++){
            nums[j]=0;
        }
    }
};