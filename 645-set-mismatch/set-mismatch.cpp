class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int l = nums.size();
        vector <int> c(l+1,0);
        int d = -1 , m = -1;
        for(int num:nums){
            c[num]++;
        }
        for(int i=0;i<=l;i++){
            if(c[i]==2){
                d=i;
            }
            if(c[i]==0){
                m=i;
            }

        }
        return {d,m};

    }
};