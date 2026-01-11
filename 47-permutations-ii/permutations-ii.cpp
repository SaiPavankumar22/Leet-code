class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        set<vector<int>>permu;
        sort(nums.begin(),nums.end());
        permu.insert(nums);
        while(next_permutation(nums.begin(),nums.end())){
            permu.insert(nums);
        }
        vector<vector<int>>final;
        copy(permu.begin(),permu.end(),back_inserter(final));
        return final;

    }
};