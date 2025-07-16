class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int eve = 0;
        for(int i: nums){
            if(i%2==0){
                eve+=1;
            }
        }
        int od =0;
        for(int j : nums){
            if(j%2==1){
                od+=1;
            }
        }
        int st_eve =0;
        int eve_rem = 0;
        for(int a:nums){
            if(a%2==eve_rem){
                st_eve+=1;
                eve_rem ^=1;
            }
        }
        int st_od = 0;
        int od_rem = 1;
        for(int b:nums){
            if(b%2==od_rem){
                st_od+=1;
                od_rem ^=1;
            }
        }
        return max({eve,od,st_eve,st_od});
    }
};