class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        unordered_map<char,int> k;
        for(auto i : licensePlate){
            if(isalpha(i)){
                char ch = tolower(i); 
                k[ch]++;
            }
        }
        int mi = INT_MAX;
        string res = "";
        
        for(auto j : words){  
            unordered_map<char,int> d;
            for(auto h : j){
                d[h]++;
            }
            
            bool s = true;  
            for(auto p : k){
                char a = p.first;
                int b = p.second;
                if(d.count(a) != 0){
                    if(d[a] < b){
                        s = false;
                        break;
                    }
                }
                else{
                    s = false;
                    break;
                }
            }
            
            if(s && j.length() < mi){ 
                res = j;
                mi = j.size();
            }
        }  
        
        return res;
    }
};