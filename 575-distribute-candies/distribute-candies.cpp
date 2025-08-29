class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_map<int,int>k;
        for(auto c:candyType){
            k[c]++;
        }
        int f = (candyType.size())/2;
        int y = k.size();
        if(f<=y){
            return f;
        }
        else{
            return y;
        }
    }
};