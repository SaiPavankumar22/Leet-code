class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_set<char>res(jewels.begin(),jewels.end());
        int cou = 0;
        for(auto n:stones){
            if(res.count(n)){
                cou++;
            }
        }
        return cou;
    }
};