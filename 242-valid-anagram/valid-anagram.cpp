class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int>original;
        unordered_map<char,int>anagram;
        for(auto i:s ){
            original[i]++;
        }
        for(auto j:t){
            anagram[j]++;
        }
        if(original == anagram){
            return true;
        }
        else{
            return false;
        }
    }
};