class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s = "";
        string k = "";
        for(auto i:word1){
            s+=i;
        }
        for(auto j:word2){
            k+=j;
        }
        return s == k;
    }
};